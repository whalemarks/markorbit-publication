# B06-PLN-0008 — Release Candidate Hardening Plan

## 1. Identity

```text
Record: B06-PLN-0008
Book: Book 06 — MarkOrbit Lite
Record type: Release Candidate Hardening Plan
Status: Work Package A complete — effective on owner merge
Authority: B06-REV-0013
Current review: B06-REV-0014
Release Candidate accepted: NO
Implementation authorized: NO
Production authorized: NO
Public/commercial distribution authorized: NO
```

## 2. Purpose

The Complete Draft 1 establishes the full Book 06 argument and controlled Product meaning.

Release Candidate hardening converts that complete draft into a consistent, reader-ready, source-validated and renderable publication without changing Product Charter v0.3, Product Baseline v0.1 or B06-TOC-V0.1 silently.

```text
Complete argument
→ editorial normalization
→ reader apparatus
→ source and rendered validation
→ whole-book RC review
→ owner RC decision
```

## 3. Hardening principles

- hardening may clarify and compress but may not change controlled meaning;
- Specifications remain authoritative over prose;
- any Product Baseline or constitutional change requires its own gate;
- internal repository governance and public manuscript content must be separated;
- reader aids must explain controlled terms without creating new authority;
- figures must remain semantic diagrams, not implementation architecture commitments;
- source validation must distinguish stable architecture claims from current external facts;
- no hardening task authorizes implementation or production.

## 4. Required findings and current disposition

```text
RC-H01 — chapter metadata normalization: CLOSED ON PACKAGE A MERGE
RC-H02 — reader-facing governance cleanup: CLOSED ON PACKAGE A MERGE
RC-H03 — controlled terms and distinction apparatus: OPEN — PACKAGE B
RC-H04 — repetition and cross-reference hardening: CLOSED ON PACKAGE A MERGE
RC-H05 — figures, appendices and index: OPEN — PACKAGE B
RC-H06 — source, citation and rendered validation: OPEN — PACKAGE C
```

## 5. Work Package A — Editorial and Structural Normalization

### Scope

- normalize all CH00–CH33 chapter headers;
- remove wave-merge acceptance wording from reader-facing chapter metadata;
- preserve draft/release state in repository governance instead;
- standardize chapter purpose/role and conclusion structure where useful;
- standardize Product, Organization, Human Review and controlled-term capitalization;
- choose and apply one spelling and punctuation convention;
- remove internal drafting-wave details from CH01 reader content;
- review CH33 roadmap language so it remains useful to readers without exposing unnecessary repository process;
- reduce avoidable repeated boundary lists;
- replace repeated full explanations with precise chapter/Specification cross-references where useful;
- preserve all deliberate zero-tolerance repetitions.

### Acceptance criteria

```text
34 / 34 chapter headers normalized
internal merge-state wording in public prose: 0
controlled meaning changes: 0
chapter order/title changes: 0
unresolved editorial inconsistencies: 0
```

### Result

```text
Status: COMPLETE — EFFECTIVE ON OWNER MERGE
Review: B06-REV-0014
Chapter files audited: 34
Chapter files modified: 23
Blocking findings: 0
Major findings: 0
Upstream findings: 0
```

### Branch / PR

```text
agent/book-06-rc-hardening-a-editorial-structure
one coherent Draft PR
```

## 6. Work Package B — Reader Apparatus

### 6.1 Controlled-term glossary

Create a reader-facing glossary covering at least:

- Product;
- Organization;
- Customer;
- Trademark;
- Matter;
- Opportunity;
- Task;
- Workflow;
- Communication;
- Document;
- Evidence;
- Artifact;
- Review;
- Prepared Action;
- Handoff;
- Return;
- Today;
- Candidate families;
- MarkReg;
- MGSN;
- Owning Service;
- Product Edition;
- Commercial Plan;
- Entitlement;
- Fulfillment Observation;
- Product Increment;
- Product Baseline;
- Constitutional Change.

### 6.2 Distinction matrix

Create a compact authoritative index of recurring distinctions, including:

```text
Today item ≠ active Task
Candidate ≠ formal truth
Recommendation ≠ Decision
User confirmation ≠ Human Review
Content ≠ Artifact
Artifact ≠ Document / Evidence / file
Render complete ≠ approved
Package ready ≠ externally completed
Prepared Action ≠ execution
Handoff ≠ destination acceptance
Return ≠ Lite-owned formal truth
Capability Need ≠ provider appointment
Personal Memory ≠ Organization Memory
Reusable Asset ≠ canonical Knowledge
local readability ≠ synchronization / disclosure authority
unknown outcome ≠ safe to retry
Product identity ≠ Commercial Plan
payment / premium edition ≠ authority
```

### 6.3 Figure register

Candidate core figures:

1. Lite position in the MarkOrbit architecture;
2. four connected Product loops;
3. Today daily operating sequence;
4. Observation → Signal → Candidate → Recommendation → Disposition;
5. four customer-growth sources and three reference journeys;
6. professional work-product lifecycle;
7. case/memory/Asset/Knowledge promotion path;
8. common Handoff/Return model and destination ownership;
9. Local/Private Hybrid Minimization flow;
10. Customer Opportunity-to-Governed-Service MVP 0;
11. Product Identity → Edition → Plan → Entitlement → Fulfillment;
12. editorial / implementation / Increment / Baseline / constitutional change ladder.

Figures must not select database, API, model or infrastructure design.

### 6.4 Appendices and index

Create or confirm:

- controlled-record-to-chapter coverage appendix;
- journey/scenario/Handoff/acceptance-criteria appendix;
- reading routes;
- abbreviation list;
- subject index or generated index source;
- figure list;
- stable cross-reference anchors.

### Acceptance criteria

```text
glossary coverage of controlled terms: complete
recurring distinction matrix: complete
figure register: approved
figures rendered and semantically reviewed: complete
controlled coverage appendix: complete
reader navigation and index source: complete
```

### Branch / PR

```text
agent/book-06-rc-hardening-b-reader-apparatus
one coherent Draft PR
```

## 7. Work Package C — Source, Citation, Render and RC Validation

### 7.1 Source and citation policy

- distinguish architecture authority from illustrative external facts;
- identify claims requiring external verification;
- verify temporally sensitive legal, commercial or technology examples;
- add source notes where a reader may otherwise treat an example as authoritative law;
- avoid turning illustrative examples into jurisdictional legal advice;
- validate all internal paths and cross-references.

### 7.2 Whole-book consistency checks

- chapter numbering and title validation;
- controlled term and capitalization check;
- controlled ID uniqueness and coverage;
- code-block and table syntax;
- broken links;
- orphan figures or appendices;
- duplicate headings and anchors;
- unresolved TODO, candidate or internal-process wording;
- Book 01–05 and Book 07 boundary review;
- commercial-plan/Product separation;
- implementation and production authorization check.

### 7.3 Rendered validation

Validate at least:

- Markdown navigation;
- PDF or equivalent long-form render;
- headings and page breaks;
- tables and code blocks;
- figure legibility;
- glossary and index navigation;
- internal links;
- front matter and end matter;
- missing assets and font substitution;
- release manifest and immutable content baseline inputs.

### 7.4 RC review

Create a separate whole-book RC review that may decide:

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

### Branch / PR

```text
agent/book-06-rc-hardening-c-source-render-review
one coherent Draft PR
```

## 8. Work order

```text
Whole-Book Complete Draft 1 — ACCEPTED
→ Work Package A — COMPLETE ON OWNER MERGE
→ Work Package B — AUTHORIZED NEXT
→ Work Package C — sequential gate
→ owner Release Candidate decision
```

The three packages must not be split into one branch per chapter.

## 9. Change escalation

During hardening:

- editorial clarification stays in the active hardening PR;
- implementation questions are recorded for later Specification/ADR work;
- Product Increment proposals are deferred to a controlled Product process;
- Product Baseline changes require explicit review;
- constitutional changes require Product Charter revision and cross-Book review.

No RC hardening PR may silently change the Product.

## 10. Gate decision

```text
Whole-Book Complete Draft 1: ACCEPTED
Work Package A acceptance on merge: AUTHORIZED
Work Package B after merge: AUTHORIZED
Work Package C: governed by sequential hardening gate
Release Candidate acceptance: NOT AUTHORIZED
Implementation: NOT AUTHORIZED
Production: NOT AUTHORIZED
Public/commercial distribution: NOT AUTHORIZED
Autonomous professional action: NOT AUTHORIZED
External Protected Action: NOT AUTHORIZED
```