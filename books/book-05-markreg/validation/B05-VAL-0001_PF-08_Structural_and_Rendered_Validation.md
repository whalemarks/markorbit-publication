# B05-VAL-0001 — PF-08 Structural and Rendered Validation

## Status

- **Status:** PASS — Controlled Validation Baseline v1.0
- **Scope:** Book 05 source, figures and reader-validation edition
- **Workflow:** `.github/workflows/book-05-pf08-validation.yml`
- **Validator:** `validation/validate_book05.py`
- **Accepted by:** B05-REV-0028
- **Publication state:** Complete Draft 1; not Release Candidate 1

## 1. Exact Validation Run

```text
GitHub Actions run: 29388230449
Workflow run number: 27
Validated head SHA: 27f2b4759773ff4f591282e60f0a3eacc778f8dd
Artifact ID: 8332248319
Artifact name: book-05-pf08-validation
Artifact digest: sha256:2a582f53a95bc50a2d9159ff6f8cf3a11e3811ccfc4bd96ed42adbd29e980e00
Artifact size: 1,181,942 bytes
Artifact retention expiry: 2026-08-14T04:09:33Z
```

The artifact is reproducible from the committed workflow and validator after its retention period expires.

## 2. Validation Result

```text
Total checks: 573
Passed: 573
Warnings: 0
Errors: 0
Result: PASS
```

## 3. Structural Coverage

The validator confirmed:

- forty-eight manuscript files, CH00–CH47;
- chapter numbering, headings and accepted metadata;
- Appendix A–G inventory;
- B05-SPEC-0001–0004 inventory;
- eleven retained Figure sources and the merged FIG-05 disposition;
- balanced Markdown fences;
- hierarchical heading-path uniqueness;
- repository-local Markdown links and fragments;
- `MR-CR`, `MR-A`, `MR-C`, `MR-D`, `MR-E`, `MR-B`, `MR-V`, `MR-G` and `MR-SCN` ranges and coverage;
- `EL-01–EL-40` and `RK-01–RK-18` ranges and coverage;
- Manifest/YAML stage and Figure-count agreement.

## 4. Figure Validation

All eleven retained Figure sources passed:

- exactly one Mermaid block;
- caption presence;
- controlled Source references;
- accessibility description;
- grayscale and legibility notes;
- simplification and authority boundary;
- actual Mermaid CLI parsing;
- actual SVG generation;
- grayscale explicit RGB-color scan.

Generated Figure outputs:

```text
SVG files: 11
Total SVG bytes: 729,913
B05-FIG-01–04 and B05-FIG-06–12: rendered
B05-FIG-05: no separate source; merged into B05-FIG-03
```

## 5. Reader-Validation Edition

The workflow assembled the controlled reader order and generated:

```text
HTML bytes: 623,202
PDF bytes: 948,073
PDF pages: 360
Extracted selectable-text characters: 475,563
PDF navigation annotations: 135
```

The rendered validation confirmed:

- CH00–CH47 identifiers present;
- Appendix A–G present;
- Source and Authority Notes present;
- Glossary present;
- Subject Index present;
- all eleven Figure captions present;
- all stable reader-source identifiers present;
- selectable text available;
- navigation annotations present;
- no source-document omission detected by the completeness scan.

## 6. Validation Corrections During PF-08

Early runs correctly exposed toolchain and validator defects before acceptance:

1. Node cache configuration incorrectly required an absent npm lockfile;
2. Chromium required an explicit no-sandbox CI configuration;
3. the initial controlled-ID regular expression did not reflect the actual `MR-A01` form;
4. heading validation needed fenced-block exclusion and hierarchical paths;
5. CH01 uses the valid `Chapter Map ID` metadata label;
6. Figure Boundary headings use more than one reviewed wording;
7. rendered completeness needed stable IDs rather than line-wrap-sensitive full titles.

These were validation-rule or CI corrections. No chapter, Specification, Appendix, Figure journey fact or authority meaning was changed to obtain a passing run.

## 7. Reproducibility and Ongoing Use

The workflow runs on relevant Book 05 pushes and pull requests and may also be dispatched manually.

Each run:

1. installs pinned Python dependencies;
2. installs Mermaid CLI and headless Chromium;
3. performs structural and controlled-ID checks;
4. renders the eleven SVGs;
5. generates HTML and PDF validation editions;
6. inspects the PDF;
7. publishes the summary to the pull request;
8. uploads the complete validation artifact.

A future source or toolchain change must produce a new passing run. This record does not make later runs equivalent without evidence.

## 8. Authority Boundary

```text
PF-08 validation pass ≠ PF-09 owner Decision
Rendered validation edition ≠ Release Candidate 1
Release Candidate 1 ≠ final publication
Publication ≠ implementation
Implementation ≠ production deployment
Validation ≠ External Protected Action authority
```

This record validates publication structure and rendering for the stated commit. It does not validate current law, live matter facts, production software or professional outcomes.
