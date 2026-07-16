# B06-REL-0001 — Release Candidate Assembly Manifest

## 1. Identity

```text
Record: B06-REL-0001
Book: Book 06 — MarkOrbit Lite
Record type: RC source assembly manifest
Status: Validation candidate
Release Candidate accepted: NO
Public/commercial distribution authorized: NO
```

## 2. Canonical source set

The RC validation assembly contains:

```text
34 chapter files
+ 7 Reader Apparatus files
= 41 ordered reader-facing Markdown inputs
```

The exact order and paths are machine-readable in `book06-assembly.yaml`.

## 3. Authority order

```text
Product Charter v0.3
→ Product Baseline v0.1 / B06-SPEC-0001–0004
→ B06-TOC-V0.1
→ B06-CH-00–B06-CH-33
→ B06-APP-0001–B06-APP-0007
```

The assembly operation may concatenate and render these inputs. It may not rewrite controlled meaning.

## 4. Excluded governance records

The validation PDF does not treat the following as reader-facing book chapters:

- Planning records;
- Review records;
- Book Status, Governance or Manifest files;
- machine state;
- workflow definitions;
- validation scripts;
- historical V1 source inventories.

They remain auditable publication governance.

## 5. Generated validation outputs

The GitHub Actions validation run generates:

```text
combined Markdown
HTML
PDF
12 rendered SVG figures
validation-report.json
validation-report.md
SHA256SUMS.txt
```

Generated outputs are tied to the workflow source commit through the artifact name, report and checksum file.

## 6. Immutable release input rule

A future accepted RC or final release must identify:

- source commit SHA;
- assembly manifest version;
- validation report;
- generated artifact checksum set;
- owner decision record;
- any non-blocking release notes.

Any content change after validation requires a new source commit and validation run.

## 7. Rendering boundary

The generated PDF is a publication-validation render. It proves that:

- the complete source set can be assembled;
- figures can be rendered;
- content survives long-form conversion;
- required identifiers remain discoverable;
- a reproducible checksum set can be created.

It is not automatically the final branded or commercially distributed edition.

## 8. Current gate

```text
RC Hardening A: ACCEPTED
RC Hardening B: ACCEPTED
RC Hardening C: IN VALIDATION
Release Candidate: NOT ACCEPTED
Implementation: NOT AUTHORIZED
Production: NOT AUTHORIZED
Public/commercial distribution: NOT AUTHORIZED
```
