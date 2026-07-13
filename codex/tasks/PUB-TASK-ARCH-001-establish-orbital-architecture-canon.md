# PUB-TASK-ARCH-001 — Establish Orbital Architecture Canon

## Purpose

Record the owner-confirmed MarkOrbit Orbital Professional Operating Architecture vNext and align repository-level publication metadata with it.

## Scope

- Create Architecture Canon, Decision Register and Open Questions records under `architecture/`.
- Link the Canon from root metadata.
- Align publication roadmap and book registry for Book 01–07.
- Preserve Book 02 as the frozen Core Specification baseline.

## Exclusions

- No Book 01, Book 02 or Book 03 manuscript changes.
- No Book 04–07 directories or manuscript scaffolding.
- No product, runtime, API, schema, database, service or microservice implementation.
- No external protected-action authorization.

## Changed-file plan

- Add `architecture/README.md`.
- Add `architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.md`.
- Add `architecture/DECISION-REGISTER-vNEXT.md`.
- Add `architecture/OPEN-QUESTIONS-vNEXT.md`.
- Add this Codex task record.
- Update root and books metadata only as needed.

## Validation requirements

Run `git diff --check`, `python tools/validate_manifest.py`, `python tools/validate_links.py`, and `python tools/validate_links.py architecture`. Confirm no Book 04–07 directories were created and Book 01–03 content boundaries were preserved.

## Next gate

`PUB-TASK-B04-001 — Create the minimal Book 04 Workplace and Product Architecture scaffold` after owner review and merge.
