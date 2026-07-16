# Book 06 Release Validation

This directory contains publication-release inputs and validation records for **Book 06 — MarkOrbit Lite**.

## Authority

```text
Product Charter v0.3
→ Product Baseline v0.1 / B06-SPEC-0001–0004
→ B06-TOC-V0.1
→ B06-CH-00–B06-CH-33
→ B06-APP-0001–B06-APP-0007
→ release validation records
```

Release validation records do not redefine Product meaning. They prove that an accepted publication source set can be assembled, navigated and rendered consistently.

## Records

- [B06-SRC-0001 — Source and Citation Policy](B06-SRC-0001_Source_and_Citation_Policy.md)
- [B06-VAL-0001 — RC Validation Protocol](B06-VAL-0001_RC_Validation_Protocol.md)
- [B06-REL-0001 — RC Assembly Manifest](B06-REL-0001_RC_Assembly_Manifest.md)
- [`book06-assembly.yaml`](book06-assembly.yaml) — machine-readable source order

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

The generated PDF is a validation render, not the final designed public edition.

## Gate boundary

A passing validation run may support a Whole-Book RC Review. It does not itself authorize:

- implementation;
- production deployment;
- public or commercial distribution;
- autonomous professional action;
- External Protected Action.
