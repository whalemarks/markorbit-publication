# Book 06 Release Records

This directory contains publication-release inputs, validation records and the permanent Release Candidate 1 identity for **Book 06 — MarkOrbit Lite**.

## Authority

```text
Product Charter v0.3
→ Product Baseline v0.1 / B06-SPEC-0001–0004
→ B06-TOC-V0.1
→ B06-CH-00–B06-CH-33
→ B06-APP-0001–B06-APP-0007
→ source and rendered validation
→ B06-REV-0016 owner RC1 decision
→ B06-REL-0003 permanent RC1 freeze
```

Release records identify and protect an accepted publication baseline. They do not redefine Product meaning or authorize implementation, production or distribution.

## Records

- [B06-SRC-0001 — Source and Citation Policy](B06-SRC-0001_Source_and_Citation_Policy.md)
- [B06-VAL-0001 — RC Validation Protocol](B06-VAL-0001_RC_Validation_Protocol.md)
- [B06-REL-0001 — RC Assembly Manifest](B06-REL-0001_RC_Assembly_Manifest.md)
- [B06-REL-0002 — Release Candidate 1 Decision Record](B06-REL-0002_Release_Candidate_1_Record.md)
- [B06-REL-0003 — Book 06 RC1 Freeze Record](B06-REL-0003_Book_06_RC1_Freeze_Record.md)
- [`B06-RC1.yaml`](B06-RC1.yaml) — machine-readable frozen release manifest
- [`book06-assembly.yaml`](book06-assembly.yaml) — ordered reader-facing source inputs
- [B06-REV-0016 — RC Hardening C and RC Review](../reviews/B06-REV-0016_RC_Hardening_C_Source_Render_and_RC_Review.md)

## Immutable RC1 identity

```text
Reader-facing content baseline:
7ce03755e03bb4876768a34a4ee3d2c3b74bddb1

Owner-decision activation commit:
060e807be90081977bcc322f1557b9fc950f5209

Release pointer created after freeze merge:
release/book-06-rc1
```

The release pointer is human-readable. The immutable SHAs and release records are authoritative.

## Validation evidence

```text
Content/render run: 29477787207
Content artifact ID: 8367264203
Content artifact digest:
sha256:2446561090311a6d6e5912ebdc1e109a2b0e5cf525109db9eb3b0762ee27236b

Final governance run: 29478801425
Governance artifact ID: 8367659673
Governance artifact digest:
sha256:dcfd3f85169f1275d38dd09e34f8338089bd4b6dbd90573a3ebe0dbd5c3819da
```

Validated result:

```text
Decision: PASS
Chapters: 34 / 34
Reader Apparatus: 7 / 7
Controlled IDs: 93 / 93
Mermaid figures: 12 / 12
Local links: 283 checked / 0 broken
Anchors: 10 checked / 0 broken
PDF pages: 410
Near-blank pages: 0
Blocking / Major / Warning findings: 0 / 0 / 0
```

The generated PDF is a validation render, not the final branded public edition.

## Change control

Any change to the 41 reader-facing inputs requires impact classification, renewed validation and a release decision. Administrative records outside that source set do not silently alter RC1.

The `release/book-06-rc1` branch must be created from the freeze PR merge commit and must not later be moved to a different baseline.

## Gate boundary

```text
Release Candidate 1: APPROVED AND FROZEN ON OWNER MERGE
Final branded publication: NOT APPROVED
Public/commercial distribution: NOT APPROVED
Product implementation: NOT AUTHORIZED
Production deployment: NOT AUTHORIZED
Autonomous professional action: NOT AUTHORIZED
External Protected Action: NOT AUTHORIZED
```
