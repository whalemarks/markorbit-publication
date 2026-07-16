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
→ B06-APP-0001–B06-APP-0007
→ B06-REV-0016 RC Review
→ B06-REL-0002 RC1 Decision
→ B06-REL-0003 RC1 Freeze
→ later implementation specifications / ADRs or final-publication work
```

Specifications remain authoritative over chapter prose and Reader Apparatus. Release records identify accepted publication baselines; they do not redefine Product meaning.

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

## 4. Accepted reader-facing publication

```text
B06-TOC-V0.1
B06-CH-00–B06-CH-33
B06-APP-0001–B06-APP-0007
34 chapter files
7 Reader Apparatus files
41 ordered reader-facing inputs
```

A manuscript chapter or Reader Apparatus record may explain a controlled record but may not change its meaning.

## 5. Whole-book integrity locks

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

## 6. RC hardening history

Release Candidate hardening was governed by `B06-PLN-0008`:

```text
Work Package A — Editorial and Structural Normalization — ACCEPTED
Work Package B — Reader Apparatus — ACCEPTED
Work Package C — Source, Citation, Render and RC Validation — ACCEPTED
```

### Hardening A

`B06-REV-0014` records 34 normalized chapter headers, zero chapter ID/title/order changes, zero controlled-meaning changes and zero blocking, major or upstream findings.

### Hardening B

`B06-REV-0015` records seven Reader Apparatus files, 63 glossary entries, 30 distinctions, 12 semantic figure sources and complete coverage of all controlled records, journeys, scenarios, Handoff contracts and MVP criteria.

### Hardening C

`B06-REV-0016` records:

```text
Source and citation review: PASS
Machine assembly order: PASS
Local links: 283 checked / 0 broken
Anchors: 10 checked / 0 broken
Controlled IDs: 93 / 93
Mermaid figures: 12 / 12
PDF validation render: 410 pages / 0 near-blank pages
External URLs: 0
Material external claims requiring citation: 0
Blocking / major / warning findings: 0 / 0 / 0
Upstream conflicts: 0
Change Proposal required: NO
```

All `RC-H01–RC-H06` requirements are closed.

## 7. Release Candidate 1 identity

`B06-REL-0002` records the accepted RC1 decision. `B06-REL-0003` permanently freezes the identity:

```text
Reader-facing content baseline:
7ce03755e03bb4876768a34a4ee3d2c3b74bddb1

Owner-decision activation commit:
060e807be90081977bcc322f1557b9fc950f5209

Machine release manifest:
release/B06-RC1.yaml

Release pointer after freeze merge:
release/book-06-rc1
```

The content SHA is authoritative for the 41 reader-facing inputs. The owner-decision SHA proves RC1 acceptance. The release branch is a human-readable pointer and must not be moved to another baseline.

## 8. Validation evidence

```text
Content/render workflow run: 29477787207
Artifact ID: 8367264203
Artifact digest:
sha256:2446561090311a6d6e5912ebdc1e109a2b0e5cf525109db9eb3b0762ee27236b

Final governance workflow run: 29478801425
Artifact ID: 8367659673
Artifact digest:
sha256:dcfd3f85169f1275d38dd09e34f8338089bd4b6dbd90573a3ebe0dbd5c3819da
```

The generated PDF is a validation render, not the final branded publication.

## 9. RC1 change control

After the freeze:

1. the 41 reader-facing RC1 inputs are immutable under the RC1 identity;
2. administrative records outside that source set do not silently alter RC1;
3. any source change requires impact classification and renewed validation;
4. typographical, packaging or design corrections must be recorded and assessed;
5. material semantic or authority change creates a new candidate baseline or explicit owner supersession;
6. the `release/book-06-rc1` branch must not be force-moved to another baseline.

## 10. Commercial and evolution rules

```text
Product Constitution
→ Product Edition
→ Commercial Plan
→ Entitlement Window
→ Fulfillment Observation
```

Price, content cadence, Prospect Candidate quantity, Render quota, support and Review level may change independently of the Product Charter.

Changes remain classified as:

```text
Class A — Editorial clarification
Class B — Implementation change
Class C — Product Increment
Class D — Product Baseline change
Class E — Constitutional change
```

Class D requires Product Baseline versioning and owner acceptance. Class E requires Product Charter revision, cross-Book review and owner acceptance.

## 11. Publication and implementation separation

Release Candidate 1 means the Product publication is structurally complete, source-reviewed and reproducibly renderable. It does not prove runtime conformance or authorize implementation, production or distribution.

RC1 may support:

- controlled review and proofing;
- final brand/design preparation;
- implementation-specification and ADR drafting;
- bounded MVP planning.

Each remains a separate approval track.

## 12. Owner gates

Owner acceptance is required for:

- Product Charter;
- Product Baseline;
- Chapter Map;
- manuscript and Reader Apparatus baselines;
- Release Candidate and any superseding candidate;
- final branded publication and distribution;
- material Product or authority changes.

## 13. Current authorization

```text
Product Charter v0.3: ACCEPTED
Product Baseline v0.1: ACCEPTED
Chapter Map v0.1: ACCEPTED
Waves 1–7: ACCEPTED
Whole-Book Complete Draft 1: ACCEPTED
RC Hardening A/B/C: ACCEPTED
Release Candidate 1: ACCEPTED
RC1 freeze on owner merge: AUTHORIZED
Final branded publication: NOT AUTHORIZED
Product implementation: NOT AUTHORIZED
Production deployment: NOT AUTHORIZED
Final public/commercial distribution: NOT AUTHORIZED
Autonomous professional action: NOT AUTHORIZED
External Protected Action: NOT AUTHORIZED
```
