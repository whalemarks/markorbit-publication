# B06-PLN-0008 — Release Candidate Hardening Plan

## 1. Identity

```text
Record: B06-PLN-0008
Book: Book 06 — MarkOrbit Lite
Record type: Release Candidate Hardening Plan
Status: Work Packages A and B complete — effective on owner merge
Authority: B06-REV-0013
Current review: B06-REV-0015
Release Candidate accepted: NO
Implementation authorized: NO
Production authorized: NO
Public/commercial distribution authorized: NO
```

## 2. Purpose

Release Candidate hardening converts the accepted Whole-Book Complete Draft 1 into a consistent, reader-ready, source-validated and renderable publication without silently changing Product Charter v0.3, Product Baseline v0.1 or `B06-TOC-V0.1`.

```text
Complete argument
→ editorial normalization
→ reader apparatus
→ source and rendered validation
→ whole-book RC review
→ owner RC decision
```

## 3. Hardening principles

- hardening may clarify, normalize, compress and add reader aids but may not change controlled meaning;
- Specifications remain authoritative over chapter prose and appendices;
- any Product Baseline or constitutional change requires a separate gate;
- internal repository governance and public manuscript content remain separate;
- figures remain semantic diagrams, not implementation architecture;
- source validation distinguishes stable architecture claims from current external facts;
- no hardening task authorizes implementation, production or protected action.

## 4. RC requirement disposition

```text
RC-H01 — chapter metadata normalization: CLOSED ON PACKAGE A MERGE
RC-H02 — reader-facing governance cleanup: CLOSED ON PACKAGE A MERGE
RC-H03 — controlled terms and distinction apparatus: CLOSED ON PACKAGE B MERGE
RC-H04 — repetition and cross-reference hardening: CLOSED ON PACKAGE A MERGE
RC-H05 — figures, appendices and index: CLOSED ON PACKAGE B MERGE
RC-H06 — source, citation and rendered validation: OPEN — PACKAGE C
```

## 5. Work Package A — Editorial and Structural Normalization

### Scope

- normalize CH00–CH33 headers and reader-facing structure;
- remove internal wave-merge wording from chapter metadata;
- keep acceptance history in Governance, Status, Manifest and Review records;
- remove internal drafting-wave details from CH01;
- make CH33’s evolution sequence reader-facing;
- reduce avoidable repetition without changing controlled meaning.

### Result

```text
Status: COMPLETE — ACCEPTED ON OWNER MERGE
Review: B06-REV-0014
Chapter files audited: 34
Chapter files modified: 23
Normalized chapter headers: 34 / 34
Controlled meaning changes: 0
Blocking / major / upstream findings: 0
```

### Branch

```text
agent/book-06-rc-hardening-a-editorial-structure
```

## 6. Work Package B — Reader Apparatus

### Scope

Create a reader-facing end-matter layer containing:

- controlled-term glossary;
- recurring distinction matrix;
- abbreviations and controlled-ID guide;
- figure register and semantic diagrams;
- controlled-record-to-chapter coverage appendix;
- journey/scenario/Handoff/acceptance coverage appendix;
- reading routes and reader entry points;
- subject index and stable anchors.

### Accepted apparatus set

```text
reader-apparatus/README.md
B06-APP-0001 — Controlled Term Glossary
B06-APP-0002 — Core Distinction Matrix
B06-APP-0003 — Abbreviations and Controlled ID Guide
B06-APP-0004 — Figure Register and Semantic Diagrams
B06-APP-0005 — Controlled Record Coverage
B06-APP-0006 — Journey, Scenario, Handoff and Acceptance Coverage
B06-APP-0007 — Subject Index
```

### Result

```text
Status: COMPLETE — EFFECTIVE ON OWNER MERGE
Review: B06-REV-0015
Glossary entries: 63
Core distinctions: 30
Semantic figure sources: 12 / 12
Product-local records covered: 45 / 45
Reference journeys: 4 / 4
Conformance scenarios: 24 / 24
Handoff contracts: 8 / 8
MVP acceptance criteria: 12 / 12
Reader navigation, index and anchors: complete
Controlled meaning changes: 0
Blocking / major / upstream findings: 0
```

Mermaid sources and semantic review are complete. Cross-format rendering, links, fonts, page breaks and final publication validation remain Package C.

### Branch

```text
agent/book-06-rc-hardening-b-reader-apparatus
```

## 7. Work Package C — Source, Citation, Render and RC Validation

### 7.1 Source and citation policy

- distinguish architecture authority from illustrative external facts;
- identify claims requiring external verification;
- verify temporally sensitive legal, commercial or technology examples;
- add source notes where examples could be mistaken for authoritative law;
- avoid turning examples into jurisdictional legal advice;
- validate all internal paths and cross-references.

### 7.2 Whole-book consistency checks

- chapter numbering and title validation;
- controlled term and capitalization check;
- controlled ID uniqueness and coverage;
- Markdown, Mermaid, code-block and table syntax;
- broken links and anchors;
- orphan figures or appendices;
- duplicate headings and anchors;
- unresolved TODO, candidate or internal-process wording;
- Books 01–05 and Book 07 boundary review;
- commercial-plan/Product separation;
- implementation and authorization checks.

### 7.3 Rendered validation

Validate at least:

- Markdown navigation;
- PDF or equivalent long-form render;
- headings and page breaks;
- tables and code blocks;
- Mermaid figure rendering and legibility;
- glossary and index navigation;
- internal links and anchors;
- front matter and end matter;
- missing assets and font substitution;
- release manifest and immutable content baseline inputs.

### 7.4 Whole-book RC review

The separate RC review may decide:

```text
PASS
PASS WITH NON-BLOCKING RELEASE NOTES
FAIL — CORRECTION REQUIRED
```

### Acceptance criteria

```text
blocking editorial/render/source findings: 0
major findings: 0
upstream conflicts: 0
open RC-H01–RC-H06 requirements: 0
whole-book rendered validation: PASS
RC review: READY FOR OWNER DECISION
```

### Branch

```text
agent/book-06-rc-hardening-c-source-render-review
```

## 8. Work order

```text
Whole-Book Complete Draft 1 — ACCEPTED
→ Work Package A — ACCEPTED
→ Work Package B — ACCEPTED ON OWNER MERGE
→ Work Package C — AUTHORIZED NEXT
→ owner Release Candidate decision
```

The work packages use one coherent branch and Draft PR each, not one branch per chapter.

## 9. Change escalation

- editorial clarification stays in the active hardening PR;
- implementation questions are deferred to later Specifications/ADRs;
- Product Increment proposals use the controlled Product process;
- Product Baseline changes require versioning and owner acceptance;
- constitutional changes require Charter revision and cross-Book review.

No RC hardening PR may silently change the Product.

## 10. Gate decision

```text
Whole-Book Complete Draft 1: ACCEPTED
Work Package A: ACCEPTED
Work Package B acceptance on merge: AUTHORIZED
Work Package C after merge: AUTHORIZED
Release Candidate acceptance: NOT AUTHORIZED
Implementation: NOT AUTHORIZED
Production: NOT AUTHORIZED
Public/commercial distribution: NOT AUTHORIZED
Autonomous professional action: NOT AUTHORIZED
External Protected Action: NOT AUTHORIZED
```
