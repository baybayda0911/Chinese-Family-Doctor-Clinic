"""Validate the implementation baseline, not medical or runtime behavior."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "chinese-family-doctor-clinic"
CHECKER = FormatChecker()


@CHECKER.checks("date-time", raises=(ValueError, TypeError))
def check_datetime(value):
    if not isinstance(value, str):
        return True
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})", value):
        return False
    return datetime.fromisoformat(value.replace("Z", "+00:00")).tzinfo is not None


def load_json(path):
    def reject_constant(value):
        raise ValueError("Non-finite JSON constant: " + value)
    return json.loads(path.read_text(encoding="utf-8"), parse_constant=reject_constant)


def schemas_and_registry(root=ROOT):
    schemas = {}
    registry = Registry()
    for path in sorted((root / "contracts").glob("*.schema.json")):
        schema = load_json(path)
        Draft202012Validator.check_schema(schema)
        schemas[path.name.removesuffix(".schema.json")] = schema
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
    return schemas, registry


def package_digest(package):
    payload = {key: value for key, value in package.items() if key != "integrity"}
    encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False,
                         separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def contract_errors(name, data, root=ROOT):
    schemas, registry = schemas_and_registry(root)
    validator = Draft202012Validator(schemas[name], registry=registry, format_checker=CHECKER)
    errors = ["schema/" + "/".join(map(str, error.absolute_path)) + ": " + error.message
              for error in validator.iter_errors(data)]
    if errors:
        return errors
    if name == "clinical-entry":
        prior = data["supersedes"]
        if prior and (prior["record_id"] != data["record_id"]
                      or prior["revision"] != data["revision"] - 1):
            errors.append("supersedes must identify the immediately preceding revision")
    if name in ("context", "exchange"):
        member_id = data["member_id"] if name == "context" else data["member"]["member_id"]
        categories = data["categories"] if name == "context" else data["authorization"]["categories"]
        seen = set()
        for record in data["records"]:
            errors.extend(contract_errors("clinical-entry", record, root))
            if record["member_id"] != member_id:
                errors.append("record belongs to another member")
            if record["sensitivity"] not in categories:
                errors.append("record outside declared category scope")
            key = (record["record_id"], record["revision"])
            if key in seen:
                errors.append("duplicate record revision inside one snapshot/package")
            seen.add(key)
            if name == "exchange":
                grant = data["authorization"]
                if record["record_type"] not in grant["record_types"]:
                    errors.append("record outside authorized type scope")
                if record["primary_vault_id"] != data["member"]["primary_vault_id"]:
                    errors.append("record primary vault mismatch")
                observed = record["observed_at"]
                if grant["date_from"] or grant["date_to"]:
                    if observed is None:
                        errors.append("unknown observation date in a date-limited export")
                    else:
                        date = observed[:10]
                        if (grant["date_from"] and date < grant["date_from"]) or (
                            grant["date_to"] and date > grant["date_to"]):
                            errors.append("record outside authorized date range")
        if name == "exchange":
            if data["sender_vault_id"] == data["receiver_vault_id"]:
                errors.append("sender and receiver must be distinct")
            grant = data["authorization"]
            if grant["date_from"] and grant["date_to"] and grant["date_from"] > grant["date_to"]:
                errors.append("invalid authorized date range")
            doc_ids = {source["doc_id"] for source in data["source_summaries"]}
            if len(doc_ids) != len(data["source_summaries"]):
                errors.append("duplicate source summary")
            for record in data["records"]:
                if record["source"].get("doc_id") and record["source"]["doc_id"] not in doc_ids:
                    errors.append("missing source summary for document reference")
            if data["integrity"]["value"] != package_digest(data):
                errors.append("integrity digest mismatch")
    if name == "source-register":
        ids = [source["source_id"] for source in data["sources"]]
        if len(ids) != len(set(ids)):
            errors.append("duplicate source_id")
        for source in data["sources"]:
            if source["review_status"] == "approved_for_scope" and not source["approved_scope"]:
                errors.append("approved source requires explicit scope")
    return errors


def validate_project(root=ROOT):
    errors = []
    schemas, _ = schemas_and_registry(root)
    skill = root / ".agents" / "skills" / "chinese-family-doctor-clinic"
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, flags=re.S)
    if not match:
        errors.append("missing Skill frontmatter")
    else:
        metadata = yaml.safe_load(match.group(1))
        if metadata.get("name") != skill.name or not metadata.get("description"):
            errors.append("invalid Skill name/description")
    ui = yaml.safe_load((skill / "agents" / "openai.yaml").read_text(encoding="utf-8"))
    if "$" + skill.name not in ui["interface"]["default_prompt"]:
        errors.append("default prompt must invoke the Skill")
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv", "__pycache__"} for part in path.relative_to(root).parts):
            continue
        body = re.sub(r"(?ms)^\s*```.*?^\s*```[^\n]*", "", path.read_text(encoding="utf-8"))
        for target in re.findall(r"\]\(([^)]+)\)", body):
            target = target.strip().strip("<>")
            if re.match(r"^(?:https?://|mailto:|#)", target):
                continue
            resolved = (path.parent / unquote(target.split("#")[0])).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(str(path.relative_to(root)) + ": broken/outside link " + target)
    for path in sorted((root / "examples").glob("*.json")):
        data = load_json(path)
        if data.get("synthetic") is not True:
            errors.append(path.name + ": fixture must be marked synthetic")
        errors.extend(path.name + ": " + error for error in contract_errors(path.stem, data, root))
    register = load_json(skill / "references" / "source-register.json")
    errors.extend(contract_errors("source-register", register, root))
    cases = load_json(root / "tests" / "acceptance-cases.json")
    expected = {"A%02d" % number for number in range(1, 29)}
    ids = [case["id"] for case in cases["cases"]]
    if set(ids) != expected or len(ids) != 28 or cases["synthetic_only"] is not True:
        errors.append("acceptance IDs must contain exactly A01 through A28")
    if any(case["status"] != "not_run" for case in cases["cases"]):
        errors.append("baseline cannot claim functional acceptance passed")
    return errors, len(schemas)


if __name__ == "__main__":
    failures, count = validate_project()
    if failures:
        for failure in failures:
            print(failure)
        raise SystemExit(1)
    print(f"PASS: {count} schemas, synthetic examples, Skill metadata, local links and 28 planned cases.")
    print("No OCR, records transaction, two-device or clinical validation was performed.")
