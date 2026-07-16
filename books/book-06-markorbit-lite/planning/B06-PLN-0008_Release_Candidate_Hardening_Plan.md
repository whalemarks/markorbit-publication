# B06-PLN-0008 — Release Candidate Hardening Plan

## 1. Identity

```text
Record: B06-PLN-0008
Book: Book 06 — MarkOrbit Lite
Record type: Release Candidate Hardening Plan
Status: Work Packages A–C complete — RC1 ready for owner acceptance on merge
Authority: B06-REV-0013
Current review: B06-REV-0016
Release Candidate 1 accepted on owner merge: YES
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
RC-H06 — source, citation and rendered validation: READY TO CLOSE ON PACKAGE C / RC1 OWNER MERGE
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
Status: COMPLETE — ACCEPTED
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
Status: COMPLETE — ACCEPTED
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

### Branch

```text
agent/book-06-rc-hardening-b-reader-apparatus
```

## 7. Work Package C — Source, Citation, Render and RC Validation

### 7.1 Validation records and tooling

```text
B06-SRC-0001 — Source and Citation Policy
B06-VAL-0001 — RC Validation Protocol
B06-REL-0001 — RC Assembly Manifest
B06-REL-0002 — Release Candidate 1 Record
book06-assembly.yaml
tools/book06_rc_validate.py
.github/workflows/book06-rc-validation.yml
```

### 7.2 Source and citation result

```text
External URLs: 0
Date markers: 2 — both illustrative 2026-07-15 placeholders in CH09
Currency markers: 11 — all RMB 99 commercial-hypothesis references
Material external current claims requiring citation: 0
Source/citation decision: PASS
```

### 7.3 Mechanical and coverage result

```text
Chapter files: 34 / 34
Reader Apparatus files: 7 / 7
Markdown files scanned: 82
Local links checked: 283
Broken local links: 0
Anchors checked: 10
Broken anchors: 0
Controlled IDs: 93 / 93
Unresolved editorial markers: 0
YAML and assembly order: PASS
```

### 7.4 Rendered validation result

```text
Mermaid figures: 12 / 12 rendered
Combined Markdown: generated
HTML: generated
PDF: generated
PDF pages: 410
PDF bytes: 842,295
Near-blank PDF pages: 0
Required chapter and appendix IDs present: PASS
SHA-256 checksum set: generated
```

### 7.5 Workflow evidence

```text
Reader-facing validation baseline: 7ce03755e03bb4876768a34a4ee3d2c3b74bddb1
Successful workflow run: 29477787207
Artifact ID: 8367264203
Artifact digest: sha256:2446561090311a6d6e5912ebdc1e109a2b0e5cf525109db9eb3b0762ee27236b
```

### 7.6 Whole-book RC review

```text
Status: COMPLETE — READY FOR OWNER RC1 DECISION
Review: B06-REV-0016
Decision: PASS
Blocking findings: 0
Major findings: 0
Warnings: 0
Upstream conflicts: 0
Change Proposal required: NO
```

### Branch

```text
agent/book-06-rc-hardening-c-source-render-review
```

## 8. Work order result

```text
Whole-Book Complete Draft 1 — ACCEPTED
→ Work Package A — ACCEPTED
→ Work Package B — ACCEPTED
→ Work Package C — PASS
→ Book 06 Release Candidate 1 — READY FOR OWNER ACCEPTANCE ON MERGE
```

The work packages used one coherent branch and Draft PR each, not one branch per chapter.

## 9. Change escalation

- editorial clarification stays in the active publication PR;
- implementation questions are deferred to later Specifications/ADRs;
- Product Increment proposals use the controlled Product process;
- Product Baseline changes require versioning and owner acceptance;
- constitutional changes require Charter revision and cross-Book review.

No RC hardening PR may silently change the Product.

## 10. Gate decision

```text
Whole-Book Complete Draft 1: ACCEPTED
Work Package A: ACCEPTED
Work Package B: ACCEPTED
Work Package C: PASS — ACCEPTED ON OWNER MERGE
Release Candidate 1: ACCEPTED ON OWNER MERGE
Implementation: NOT AUTHORIZED
Production: NOT AUTHORIZED
Final public/commercial distribution: NOT AUTHORIZED
Autonomous professional action: NOT AUTHORIZED
External Protected Action: NOT AUTHORIZED
```
