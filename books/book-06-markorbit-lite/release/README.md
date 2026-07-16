# Book 06 Release Validation

This directory contains publication-release inputs, validation records and the Release Candidate record for **Book 06 — MarkOrbit Lite**.

## Authority

```text
Product Charter v0.3
→ Product Baseline v0.1 / B06-SPEC-0001–0004
→ B06-TOC-V0.1
→ B06-CH-00–B06-CH-33
→ B06-APP-0001–B06-APP-0007
→ release validation records
→ owner Release Candidate decision
```

Release validation records do not redefine Product meaning. They prove that an accepted publication source set can be assembled, navigated and rendered consistently.

## Records

- [B06-SRC-0001 — Source and Citation Policy](B06-SRC-0001_Source_and_Citation_Policy.md)
- [B06-VAL-0001 — RC Validation Protocol](B06-VAL-0001_RC_Validation_Protocol.md)
- [B06-REL-0001 — RC Assembly Manifest](B06-REL-0001_RC_Assembly_Manifest.md)
- [B06-REL-0002 — Release Candidate 1 Record](B06-REL-0002_Release_Candidate_1_Record.md)
- [`book06-assembly.yaml`](book06-assembly.yaml) — machine-readable source order
- [B06-REV-0016 — RC Hardening C and RC Review](../reviews/B06-REV-0016_RC_Hardening_C_Source_Render_and_RC_Review.md)

## Validated source baseline

```text
Reader-facing source commit:
7ce03755e03bb4876768a34a4ee3d2c3b74bddb1

Successful workflow run:
29477787207

Artifact digest:
sha256:2446561090311a6d6e5912ebdc1e109a2b0e5cf525109db9eb3b0762ee27236b
```

## Reproducible outputs

The `Book 06 RC Validation` GitHub Actions workflow creates, but does not commit, the following artifact set:

```text
Book-06-MarkOrbit-Lite-RC-Validation.md
Book-06-MarkOrbit-Lite-RC-Validation.html
Book-06-MarkOrbit-Lite-RC-Validation.pdf
figures/figure-01.svg–figure-12.svg
validation-report.json
validation-report.md
SHA256SUMS.txt
```

Validated result:

```text
Decision: PASS
Chapters: 34 / 34
Reader Apparatus: 7 / 7
Controlled IDs: 93 / 93
Mermaid figures: 12 / 12
PDF pages: 410
Near-blank pages: 0
Blocking / Major / Warning findings: 0 / 0 / 0
```

The generated PDF is a validation render, not the final designed public edition.

## Gate boundary

Owner merge of the RC review PR accepts Book 06 Release Candidate 1.

It does not itself authorize:

- implementation;
- production deployment;
- final public or commercial distribution;
- autonomous professional action;
- External Protected Action.
