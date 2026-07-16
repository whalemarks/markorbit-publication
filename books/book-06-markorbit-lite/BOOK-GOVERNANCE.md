# Book 06 Governance — MarkOrbit Lite

## 1. Authority chain

```text
Architecture Canon
→ Books 01–04 Portfolio Baseline
→ Book 05 MarkReg RC1 contracts
→ Book 06 Product Charter v0.3
→ Book 06 Product Baseline v0.1
→ B06-TOC-V0.1
→ B06-CH-00–B06-CH-33
→ B06-APP-0001–B06-APP-0007 Reader Apparatus
→ Source, Citation, Render and RC Validation
→ owner Release Candidate decision
→ later implementation specifications / ADRs
```

Specifications remain authoritative over chapter prose and Reader Apparatus.

## 2. Book responsibility

Book 06 may define Lite purpose, users, four Product loops, Today, Product-local records, customer/service growth, professional work products, memory/assets, Handoff/Return, conformance, MVP and commercial experiments.

Book 06 may not redefine Core, Execution, Workplace, MarkReg, MGSN, Owning-Service, Knowledge governance or External Protected Action authority.

## 3. Accepted Product Baseline

```text
B06-SPEC-0001–0004 v0.1
ML-S01–S05
ML-O01–O08
ML-W01–W10
ML-M01–M08
ML-H01–H08
ML-E01–E06
ML-J01–J04
ML-SCN-01–24
ML-HC-01–HC-08
ML-AC-01–AC-12
```

## 4. Accepted chapter map, manuscript and apparatus

```text
B06-TOC-V0.1
B06-CH-00–B06-CH-33
7 Parts plus Front Matter
34 / 34 chapter files
Whole-Book Complete Draft 1 — ACCEPTED
B06-APP-0001–B06-APP-0007 — ACCEPTED
41 ordered reader-facing inputs
```

A manuscript chapter or Reader Apparatus record may explain a controlled record but may not change its meaning.

## 5. Reader Apparatus rule

Reader Apparatus uses publication IDs `B06-APP-*` and may:

- define reader-facing glossary entries;
- collect recurring distinctions;
- provide abbreviations and controlled-ID guidance;
- visualize accepted relationships through semantic figures;
- map records, journeys, scenarios, Handoff contracts and criteria to chapters;
- provide reading routes, anchors and a subject index.

Reader Apparatus may not:

- create or redefine `ML-*` records;
- change Product Charter, Product Baseline or Chapter Map;
- add implementation schema, database tables, APIs or providers;
- transfer formal ownership or authority;
- claim runtime conformance;
- grant implementation or external-action authority.

```text
Product Charter / Specifications / Chapter Map
→ chapter prose
→ Reader Apparatus
```

A conflict is resolved upward in that order.

## 6. Whole-book integrity locks

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

## 7. RC hardening governance

Release Candidate hardening is governed by `B06-PLN-0008`:

```text
Work Package A — Editorial and Structural Normalization
Work Package B — Reader Apparatus
Work Package C — Source, Citation, Render and RC Validation
```

Hardening may clarify, normalize, compress, add reader aids and prove renderability. It may not silently change Product Charter, Product Baseline, Chapter Map, formal ownership or Human/External Action authority.

## 8. RC Hardening A

`B06-REV-0014` records:

```text
34 / 34 chapter headers normalized
internal wave-merge metadata remaining: 0
chapter ID/title/order changes: 0
controlled meaning changes: 0
blocking / major / upstream findings: 0
```

Work Package A closes `RC-H01`, `RC-H02` and `RC-H04`.

## 9. RC Hardening B

`B06-REV-0015` records:

```text
B06-APP-0001–B06-APP-0007 complete
Glossary entries: 63
Core distinctions: 30
Semantic figure sources: 12
Product-local records covered: 45 / 45
Journeys / scenarios / Handoff contracts / acceptance criteria: complete
Stable anchors and subject index: complete
Product Charter / Baseline / Chapter Map changes: 0
blocking / major / upstream findings: 0
```

Work Package B closes `RC-H03` and `RC-H05`.

## 10. RC Hardening C

`B06-REV-0016` records:

```text
Source and citation review: PASS
Machine assembly order: PASS
Local links: 283 checked / 0 broken
Anchors: 10 checked / 0 broken
Controlled IDs: 93 / 93
Mermaid figures: 12 / 12 rendered
PDF: 410 pages / 842,295 bytes / 0 near-blank pages
External URLs: 0
Material external claims requiring citation: 0
Blocking / major / warning findings: 0 / 0 / 0
Upstream conflicts: 0
Change Proposal required: NO
```

Validation evidence:

```text
Reader-facing baseline: 7ce03755e03bb4876768a34a4ee3d2c3b74bddb1
Workflow run: 29477787207
Artifact ID: 8367264203
Artifact digest:
sha256:2446561090311a6d6e5912ebdc1e109a2b0e5cf525109db9eb3b0762ee27236b
```

Work Package C is `PASS` and closes `RC-H06` on owner merge.

## 11. Release Candidate 1 rule

`B06-REL-0002` defines the RC1 content baseline:

```text
34 chapters
+ 7 Reader Apparatus records
= 41 ordered reader-facing inputs
```

Owner merge of `B06-REV-0016` accepts Book 06 Release Candidate 1.

Release Candidate 1 means the Product publication is structurally complete, source-reviewed and reproducibly renderable. It does not mean final brand/design production, Product implementation, runtime conformance, production deployment or public/commercial distribution is approved.

Any later change to the 41 reader-facing source files requires a new validation run and release-impact decision.

## 12. Commercial and evolution rules

```text
Product Constitution
→ Product Edition
→ Commercial Plan
→ Entitlement Window
→ Fulfillment Observation
```

Price, content cadence, Prospect Candidate quantity, Render quota, support and Review level may change independently of the Product Charter.

Changes are classified as:

```text
Class A — Editorial clarification
Class B — Implementation change
Class C — Product Increment
Class D — Product Baseline change
Class E — Constitutional change
```

Class D requires Product Baseline versioning and owner acceptance. Class E requires Product Charter revision, cross-Book review and owner acceptance.

## 13. Branch and PR rule

Publication changes use one coherent branch and Draft PR per controlled work package. A change to the accepted RC1 content baseline must state its impact and rerun validation.

## 14. Owner gates

Owner acceptance is required for:

- Product Charter;
- Product Baseline;
- Chapter Map;
- manuscript waves;
- Whole-Book Complete Draft 1;
- each RC hardening package;
- Release Candidate;
- final public/commercial publication.

## 15. Current authorization

```text
Product Charter v0.3: ACCEPTED
Product Baseline v0.1: ACCEPTED
Chapter Map v0.1: ACCEPTED
Waves 1–7: ACCEPTED
Whole-Book Complete Draft 1: ACCEPTED
RC Hardening A: ACCEPTED
RC Hardening B: ACCEPTED
RC Hardening C: PASS — ACCEPTED ON OWNER MERGE
Release Candidate 1: ACCEPTED ON OWNER MERGE
Implementation: NOT AUTHORIZED
Production deployment: NOT AUTHORIZED
Final public/commercial distribution: NOT AUTHORIZED
Autonomous professional action: NOT AUTHORIZED
External Protected Action: NOT AUTHORIZED
```
