"""Meaningful contract safeguards; these do not test the future clinic runtime."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_project import contract_errors, load_json, package_digest, validate_project


class ContractTests(unittest.TestCase):
    def example(self, name):
        return copy.deepcopy(load_json(ROOT / "examples" / (name + ".json")))

    def assert_invalid(self, name, data):
        self.assertTrue(contract_errors(name, data))

    def test_baseline_is_consistent(self):
        self.assertEqual(validate_project()[0], [])

    def test_unknowns_are_explicit(self):
        data = self.example("observation")
        data.update(value=None, unit=None, observed_at=None, date_precision="unknown")
        self.assertEqual(contract_errors("observation", data), [])
        data["observed_at"] = "2026-10-10"
        self.assert_invalid("observation", data)

    def test_date_precision_is_not_fabricated(self):
        data = self.example("observation")
        data["observed_at"] = "2026-10-10T12:00:00+08:00"
        self.assert_invalid("observation", data)

    def test_impossible_dates_fail(self):
        data = self.example("observation")
        data["observed_at"] = "2026-02-30"
        self.assert_invalid("observation", data)

    def test_unreviewed_facts_fail(self):
        data = self.example("observation")
        data["source"]["human_reviewed"] = False
        self.assert_invalid("observation", data)

    def test_user_recollection_is_not_clinician_evidence(self):
        data = self.example("clinical-entry")
        data["record_type"] = "clinician_diagnosis"
        data["source"] = {"kind": "user_statement", "encounter_id": "demo-encounter-001",
                          "human_reviewed": True}
        self.assert_invalid("clinical-entry", data)
        data["record_type"] = "user_report"
        self.assertEqual(contract_errors("clinical-entry", data), [])

    def test_revision_chain_cannot_skip_or_change_record(self):
        data = self.example("clinical-entry")
        data.update(revision=3, supersedes={"record_id": data["record_id"], "revision": 1})
        self.assert_invalid("clinical-entry", data)
        data["supersedes"]["revision"] = 2
        self.assertEqual(contract_errors("clinical-entry", data), [])
        data["supersedes"]["record_id"] = "another-record"
        self.assert_invalid("clinical-entry", data)

    def test_confirmation_evidence_required(self):
        data = self.example("clinical-entry")
        del data["confirmed_by"]
        self.assert_invalid("clinical-entry", data)

    def test_reminders_stay_disabled(self):
        data = self.example("task")
        data["reminder_enabled"] = True
        self.assert_invalid("task", data)

    def test_model_context_has_no_raw_path_field(self):
        data = self.example("context")
        data["original_path"] = "/private/record.pdf"
        self.assert_invalid("context", data)

    def test_context_member_and_sensitive_scope(self):
        data = self.example("context")
        data["records"][0]["member_id"] = "another-member"
        self.assert_invalid("context", data)
        data = self.example("context")
        data["records"][0]["sensitivity"] = "mental_health"
        self.assert_invalid("context", data)

    def test_tampered_exchange_hash_fails(self):
        data = self.example("exchange")
        data["records"][0]["fact"]["value"] = 99
        self.assert_invalid("exchange", data)

    def test_rehashed_unauthorized_category_still_fails(self):
        data = self.example("exchange")
        data["records"][0]["sensitivity"] = "reproductive"
        data["integrity"]["value"] = package_digest(data)
        self.assert_invalid("exchange", data)

    def test_exchange_does_not_promote_another_primary_vault(self):
        data = self.example("exchange")
        data["records"][0]["primary_vault_id"] = "another-vault"
        data["integrity"]["value"] = package_digest(data)
        self.assert_invalid("exchange", data)

    def test_exchange_date_scope_is_enforced_by_contract_checker(self):
        data = self.example("exchange")
        data["authorization"]["date_from"] = "2026-10-11"
        data["integrity"]["value"] = package_digest(data)
        self.assert_invalid("exchange", data)

    def test_duplicate_record_revision_rejected(self):
        data = self.example("exchange")
        data["records"].append(copy.deepcopy(data["records"][0]))
        data["integrity"]["value"] = package_digest(data)
        self.assert_invalid("exchange", data)

    def test_document_source_must_have_summary(self):
        data = self.example("exchange")
        data["source_summaries"] = []
        data["integrity"]["value"] = package_digest(data)
        self.assert_invalid("exchange", data)


if __name__ == "__main__":
    unittest.main()
