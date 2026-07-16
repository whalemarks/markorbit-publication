# B06-APP-0003 — Abbreviations and Controlled ID Guide

## Status and authority

```text
Record: B06-APP-0003
Type: Reader-facing abbreviation and identifier guide
Status: Candidate — accepted on RC Hardening B owner merge
Authority: editorial projection only
```

## 1. Publication identifiers

| Prefix | Meaning | Authority effect |
| --- | --- | --- |
| `B06-CH-*` | Book 06 manuscript chapter | Reader-facing projection of accepted Product meaning |
| `B06-PLN-*` | Book 06 planning or owner-decision record | May govern scope, gates and accepted planning decisions |
| `B06-SPEC-*` | Book 06 Product Baseline Specification | Authoritative over simplified manuscript explanation |
| `B06-REV-*` | Book 06 review record | Records findings, decisions and gate effects |
| `B06-APP-*` | Book 06 Reader Apparatus record | Navigation and explanation only; no new Product authority |
| `B06-TOC-*` | Controlled Chapter Map | Governs chapter numbering, titles, order and Part ranges |
| `RC-H*` | Release Candidate hardening requirement | Editorial/release requirement, not a Product record |

## 2. Product-local record families

| Range | Family | Primary meaning |
| --- | --- | --- |
| `ML-S01–S05` | Session, Today and interaction | Lite Session, Today Snapshot, Attention Item, User Disposition, Continuation State |
| `ML-O01–O08` | Observations and Candidates | Source Observation, Signal, service/reactivation/prospect/work-product Candidates, Recommendation, Qualification |
| `ML-W01–W10` | Work products and Prepared Actions | Structured Content, Artifact, Review Package, Prepared Action, Development Package, Render, Delivery/Publish and Readiness |
| `ML-M01–M08` | Feedback, memory, cases and Assets | Feedback, Correction, preference/personal/Organization memory, Case Lesson, Reusable Asset, Knowledge contribution |
| `ML-H01–H08` | Handoff and Return | Common Envelope, Return presentation and destination-specific Handoffs |
| `ML-E01–E06` | Evaluation and commercial evidence | Evaluation Run, outcomes, reuse, safety/privacy, commercial experiments and fulfillment |

These `ML-*` families are semantic publication records. They do not require one database table per record or identical implementation names.

## 3. Controlled journey and test families

| Range | Meaning |
| --- | --- |
| `ML-J01–J04` | Reference Product journeys |
| `ML-SCN-01–SCN-24` | Conformance scenarios and failure paths |
| `ML-HC-01–HC-08` | Destination-specific Handoff contracts |
| `ML-AC-01–AC-12` | MVP 0 acceptance criteria |

## 4. General abbreviations

| Abbreviation | Meaning in Book 06 |
| --- | --- |
| ADR | Architecture Decision Record; implementation/governance artifact created after publication authority allows it |
| AI | Artificial Intelligence; assistance capability, not professional authority |
| API | Application Programming Interface; implementation detail not selected by Book 06 |
| CRM | Customer Relationship Management system; Lite does not become a universal CRM |
| CTA | Call to action in a work product or communication |
| MGSN | Mark Global Service Network |
| MVP | Minimum Viable Product; in Book 06, MVP 0 is the Customer Opportunity-to-Governed-Service Loop |
| PDF | Portable Document Format; one possible Artifact representation |
| PNG | Portable Network Graphics; one possible image representation |
| MP4 | MPEG-4 video file; one possible video representation |
| QR | Quick Response code; a representation element that must remain linked to the correct destination/version |
| RC | Release Candidate |
| TTS | Text-to-Speech; a rendering capability subject to cost, quality and rights controls |
| UI | User Interface; may evolve without changing Product constitution |
| URL | Uniform Resource Locator; may serve as a source or destination reference |

## 5. Named systems and boundaries

| Name | Meaning |
| --- | --- |
| MarkOrbit Lite | AI business operating system for independent trademark professionals and small agencies |
| Core | Shared meaning, identity and formal-object semantics defined by upstream books/services |
| Workplace | Organization context, roles and collaboration boundary |
| Execution | Governed work and protected-action boundary |
| MarkReg | Formal trademark Product Session and lifecycle Product defined by Book 05 |
| MGSN | Provider capability, Trust, Routing and cross-Organization collaboration boundary |
| Knowledge Governance | Destination that evaluates Knowledge Contribution Candidates |
| Communication Service | Destination that owns formal send state and evidence |
| Opportunity Service | Destination that owns formal Opportunity state |
| Task / Execution Service | Destination that owns active Task, Workflow and protected execution state |
| Owning Service | Service responsible for authoritative formal state and mutation |

## 6. Severity and decision labels

| Label | Meaning |
| --- | --- |
| `BLOCKING` | Violation invalidates the affected capability or pilot |
| `MAJOR` | Must be corrected before baseline or release |
| `STANDARD` | Expected conforming behavior |
| `PASS` | Reviewed scope meets its acceptance criteria |
| `PASS WITH ...` | Scope passes but named later requirements remain |
| `FAIL — CORRECTION REQUIRED` | Blocking or major issue prevents the gate |

## 7. State vocabulary

Book 06 preserves typed states rather than flattening everything into `done` or `failed`.

```text
observed
explained
inspected
accepted_for_preparation
deferred
rejected
suppressed
corrected
qualified_for_handoff
handed_off
ready_for_review
ready_for_confirmation
blocked
incomplete
stale
unsupported
expired
retired
accepted_by_destination
more_information_required
failed
unknown_external_outcome
completed_by_destination
```

State labels are semantic guidance. An implementation may use different internal names if it preserves the same observable meaning.

## 8. Identifier rules

1. Publication IDs identify documents and reader aids.
2. `ML-*` IDs identify accepted semantic Product records, journeys, scenarios, contracts or criteria.
3. A reader-aid ID must never be treated as a Product record.
4. A Product record ID must not be assumed to equal one database table.
5. Commercial plan names and quotas are independently versioned and do not alter `ML-*` meaning.
6. A new `ML-*` family requires Product Baseline governance; it cannot be created by an appendix.

## Authority links

- [B06-SPEC-0001](../specifications/B06-SPEC-0001_Product_Local_Records_and_Ownership.md)
- [B06-SPEC-0002](../specifications/B06-SPEC-0002_Reference_Journeys_and_State_Transitions.md)
- [B06-SPEC-0003](../specifications/B06-SPEC-0003_Conformance_Scenarios_and_Failure_Paths.md)
- [B06-SPEC-0004](../specifications/B06-SPEC-0004_Handoff_Work_Product_MVP_and_Historical_Reconciliation.md)
