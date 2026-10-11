# Project instructions

- Read README.md, capabilities.json and docs/roadmap.md before implementation. Respect the current milestone; distinguish instructions, contracts, implementations and clinical validation.
- Repository root is the code boundary. Real health data, identity mappings, original files, exports and backups must stay outside it. Use synthetic fixtures in development and tests.
- Keep the clinic Skill in .agents/skills/chinese-family-doctor-clinic. Load room references on demand; keep shared rules in one place.
- Clinical facts, user statements, clinician documents and AI analysis are distinct types. Never promote a candidate explanation to a clinician diagnosis.
- Local ingestion and review precede model context. Raw files, identifiers and raw OCR text must not appear in model-visible tool inputs/results. Design local UI/backend contracts separately from model tools.
- Yungho workflow adaptations retain MIT notices; an optional TCM workflow adaptation is separately CC BY-NC. No complete knowledge library or textbook is bundled. Record file/commit/license details before copying additional third-party content. Preserve LICENSE and third-party notices.
- All member writes are serialized through the records service after a single confirmation per new batch. This service is planned, not implemented.
- Run python scripts/validate_project.py and python -m unittest discover -s tests -v after changing contracts or examples. Install validation dependencies only in a dedicated environment.
- Functional acceptance and clinical review are separate. Update capability status only with evidence. Do not call schema checks clinical or OCR tests.
- Changes to remote repositories, publication, real-data processing, global Skill installation, paid services and scheduled reminders require authorization for that action.
