# B06-VAL-0001 — Release Candidate Validation Protocol

## 1. Identity

```text
Record: B06-VAL-0001
Book: Book 06 — MarkOrbit Lite
Record type: Publication validation protocol
Status: Active for RC Hardening C
Product meaning authority: NO
Implementation authority: NO
```

## 2. Purpose

This protocol defines the repeatable checks required before Book 06 may be presented for owner Release Candidate decision.

It validates publication structure, reader navigation, source classification and rendered output. It does not validate a runtime Product implementation.

## 3. Validation source set

```text
B06-CH-00–B06-CH-33
B06-APP-0001–B06-APP-0007
B06-SPEC-0001–B06-SPEC-0004
B06-PLN-0004 v0.3
B06-PLN-0007 / B06-TOC-V0.1
B06-PLN-0008
publication.yaml
book06-assembly.yaml
```

The machine-readable assembly order is defined in `book06-assembly.yaml`.

## 4. Mechanical validation

The validation workflow must check:

- 34 chapter files exist and are ordered `B06-CH-00–B06-CH-33`;
- 7 Reader Apparatus files exist and are ordered `B06-APP-0001–B06-APP-0007`;
- normalized chapter metadata remains present;
- Markdown fences are balanced;
- YAML files parse successfully;
- unresolved `TODO`, `TBD`, `FIXME` or placeholder markers are absent from reader-facing content;
- internal drafting-wave or merge-state language does not return to reader-facing chapters;
- local Markdown links resolve;
- linked anchors exist;
- controlled IDs appear in the accepted coverage appendices;
- publication inputs remain inside the repository boundary.

## 5. Source and citation validation

The workflow produces an inventory of:

- external URLs and domains;
- year markers;
- currency and price markers;
- source-policy classification.

Human RC review must determine whether each material external claim is either:

- appropriately sourced and scoped; or
- architectural/illustrative and not represented as current external fact.

Automated URL discovery does not replace editorial source judgment.

## 6. Figure validation

The workflow must:

1. locate all Mermaid source blocks in the Reader Apparatus;
2. render each block independently to SVG;
3. fail on Mermaid parser or browser errors;
4. confirm the expected figure count;
5. include SVG outputs in the validation artifact;
6. place rendered figures in the assembled HTML and PDF.

The expected core figure count is:

```text
12 / 12
```

A successful render proves publication compatibility. It does not select implementation architecture.

## 7. Long-form assembly

The validation assembly must use the following order:

```text
validation title page
→ B06-CH-00–B06-CH-33
→ Reader Apparatus title
→ B06-APP-0001–B06-APP-0007
```

It must generate:

- one combined Markdown source;
- one HTML render;
- one PDF render;
- rendered SVG figures;
- machine-readable validation report;
- human-readable validation report;
- SHA-256 checksums.

## 8. PDF checks

The workflow must confirm:

- the PDF exists and exceeds a minimum file-size threshold;
- the page count is consistent with a complete long-form manuscript;
- chapter-front and end-matter identifiers survive text extraction;
- near-blank pages remain below the accepted threshold;
- tables, code blocks and figures are represented in the source HTML;
- a font family available on the runner is explicitly selected.

The validation PDF is not the final designed edition. Visual brand design may be applied later without changing content meaning, subject to a new render check.

## 9. Required output report

The report must state:

```text
PASS or FAIL
source commit
blocking findings
major findings
warnings
chapter and appendix counts
link and anchor counts
controlled-ID coverage
Mermaid render count
PDF page count and size
source inventory counts
```

A failing workflow must still upload any available diagnostic artifact.

## 10. Finding severity

```text
BLOCKING
- missing chapter or required appendix;
- invalid YAML required for release state;
- missing controlled-ID coverage;
- Mermaid figure cannot render;
- PDF cannot be generated;
- publication source escapes repository scope.

MAJOR
- broken local link or anchor;
- malformed chapter metadata;
- unresolved editorial marker;
- unexpectedly short or incomplete PDF;
- excessive blank pages;
- required chapter or end-matter text missing from PDF extraction.

WARNING
- review item that does not invalidate the assembly but requires editorial attention.
```

## 11. RC gate rule

A Book 06 RC review may be marked ready for owner decision only when:

```text
workflow decision: PASS
blocking findings: 0
major findings: 0
all RC-H01–RC-H06 requirements: closed
whole-book rendered validation: PASS
upstream conflicts: 0
```

The owner Release Candidate decision remains a separate merge gate.

## 12. Authorization boundary

Passing this protocol does not authorize:

- Product implementation;
- deployment or production use;
- public/commercial distribution;
- autonomous professional action;
- External Protected Action.
