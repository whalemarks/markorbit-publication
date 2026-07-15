# B06-SPEC-0001 — Product-Local Records and Ownership

## 1. Identity

```text
Specification: B06-SPEC-0001
Book: Book 06 — MarkOrbit Lite
Version: v0.1
Status: Candidate — accepted as Product Baseline on owner merge
Scope: Product-local records, controlled IDs, ownership and formalization boundaries
Implementation schema authorized: NO
```

## 2. Purpose

This Specification answers four questions:

1. Which records may Lite own?
2. Which formal objects may Lite only reference or request?
3. What minimum metadata must every material Lite record preserve?
4. At which point must a Product-local candidate be handed to an Owning Service?

The central rule is:

```text
Lite owns Product experience, candidate state, preparation and continuity.
Owning Services own formal business truth.
```

## 3. Common metadata

Every material `ML-*` record should preserve, where applicable:

- controlled ID and record type;
- Product origin and active Organization;
- user and responsible participant;
- customer, trademark, Matter and subject references;
- purpose and intended audience;
- source, source version and freshness;
- data classification and controller;
- confidence, uncertainty and missing information;
- transformation history and parent records;
- current Product-local state;
- allowed destinations;
- required Review or confirmation;
- expiry, suppression and retirement state;
- creation, update and disposition timestamps.

No common field implies permission or formal authority.

## 4. Record classification

| Class | Meaning |
| --- | --- |
| Product-local | Lite may create and mutate within its Product boundary |
| Projection | Lite presents a sourced view of another service's record |
| Request | Lite prepares a request; destination decides whether formal state is created |
| Envelope | Versioned transfer package with source and intended consequence |
| Evaluation | Evidence about Product behavior; not business truth |
| External formal | Never owned by Lite |

## 5. Session, Today and interaction — `ML-S01–S05`

| ID | Record | Lite ownership | Required boundary |
| --- | --- | --- | --- |
| ML-S01 | Lite Session | Product-local | Active user, Organization, Product mode and expiry |
| ML-S02 | Today Snapshot | Product-local projection set | Must retain source time; not a Task list or deadline source |
| ML-S03 | Attention Item | Product-local presentation | References a source observation, returned result or candidate |
| ML-S04 | User Disposition | Product-local | Inspect, accept-for-preparation, dismiss, snooze, suppress, correct or route |
| ML-S05 | Continuation State | Product-local | Preserves unfinished Product context without claiming destination state |

`ML-S02` and `ML-S03` may display formal records, but the displayed status remains sourced from the relevant Owning Service.

## 6. Observations and value candidates — `ML-O01–O08`

| ID | Record | Purpose | Formalization boundary |
| --- | --- | --- | --- |
| ML-O01 | Source Observation | Normalized, source-linked observation | Never becomes canonical merely through extraction |
| ML-O02 | Customer / Trademark Signal | Connect observation to authorized subject context | Must not create Customer, Trademark or Matter truth |
| ML-O03 | Service-Value Candidate | Explain a possible professional service need | Opportunity Service decides formal Opportunity |
| ML-O04 | Reactivation Candidate | Explain a current reason to revisit an inactive relationship | Contact and customer ownership remain external |
| ML-O05 | Prospect Candidate | Candidate organization/person from authorized source | Not Customer, Qualified Lead or Opportunity |
| ML-O06 | Work-Product Candidate | Candidate output needed for a defined purpose | Becomes Artifact only through `ML-W02` |
| ML-O07 | Recommendation Presentation | Ranked explanation and options | Recommendation is not Decision or approval |
| ML-O08 | Qualification Result | User/Review disposition of a candidate | May trigger a formalization request; not formal state itself |

Candidate lifecycle:

```text
observed
→ explained
→ inspected
→ accepted_for_preparation / deferred / rejected / suppressed / corrected
→ qualified_for_handoff
→ handed_off / expired / retired
```

## 7. Work products and Prepared Actions — `ML-W01–W10`

| ID | Record | Purpose | Critical distinction |
| --- | --- | --- | --- |
| ML-W01 | Structured Content | Purpose-bound content and factual structure | Content ≠ Artifact |
| ML-W02 | Artifact Draft | Business result under preparation | Artifact ≠ Document or Evidence |
| ML-W03 | Artifact Version | Immutable version for review/use | Later edits create a new version |
| ML-W04 | Review Package | Exact-version context for Human Review | User confirmation ≠ Human Review |
| ML-W05 | Prepared Action | Exact subject, destination, consequence and required checks | Prepared Action ≠ execution |
| ML-W06 | Development Package | Customer/prospect explanation, work product and follow-up | Does not prove purchase intent |
| ML-W07 | Render Request | Requested representation and deterministic fields | Tool choice remains implementation-local |
| ML-W08 | Render Result | File/representation result with success/failure | Render complete ≠ approved |
| ML-W09 | Delivery / Publish Package Candidate | Prepared distribution package | Ready ≠ delivered or published |
| ML-W10 | Readiness Result | Ready, blocked, stale, incomplete or unsupported | Must list missing information and blockers |

Work-product lifecycle:

```text
candidate
→ draft
→ versioned
→ review_required / ready_for_confirmation
→ prepared_for_handoff
→ handed_off
→ returned_result_observed
→ reused / corrected / retired
```

## 8. Memory, cases and reusable Assets — `ML-M01–M08`

| ID | Record | Product meaning | Promotion requirement |
| --- | --- | --- | --- |
| ML-M01 | Feedback Record | Explicit user/reviewer response | No automatic policy change |
| ML-M02 | Correction Record | Sourced correction to Product behavior or content | Must identify affected record/version |
| ML-M03 | Preference Candidate | Candidate personal preference | Explicit acceptance and scope required |
| ML-M04 | Personal Memory Candidate | Private continuity candidate | Remains personal unless promoted |
| ML-M05 | Organization Memory Candidate | Candidate shared operating memory | Organization review required |
| ML-M06 | Case Lesson Candidate | Bounded lesson derived from authorized case context | Case success ≠ universal rule |
| ML-M07 | Reusable Asset Candidate | Template, example or approved case asset | Rights, audience and reuse scope required |
| ML-M08 | Knowledge Contribution Candidate | Proposed contribution to governed Knowledge | Knowledge governance decides acceptance |

Promotion chain:

```text
activity or outcome
→ sourced feedback/correction
→ scoped candidate
→ Human Review
→ accepted personal memory / organization memory / reusable Asset / Knowledge contribution
```

No promotion may be inferred from repeated use alone.

## 9. Handoff, Return and continuity — `ML-H01–H08`

| ID | Record | Purpose |
| --- | --- | --- |
| ML-H01 | Handoff Envelope | Common versioned package: origin, subject, purpose, sources, selected version, intended consequence and return address |
| ML-H02 | Return Envelope Presentation | Lite presentation of destination result with source and status |
| ML-H03 | MarkReg Handoff | Launch/continue request mapped to Book 05 contracts |
| ML-H04 | MGSN Capability Need Handoff | Minimum capability need and authorized context |
| ML-H05 | Review Handoff | Exact-version review request and required decision |
| ML-H06 | Communication Handoff | Draft, recipient, channel, purpose and send consequence |
| ML-H07 | Opportunity Formalization Request | Qualified candidate and evidence sent to Opportunity Service |
| ML-H08 | Task / Execution Handoff | Proposed work or protected action request sent to the correct boundary |

Required result classes:

```text
accepted
more_information_required
rejected
blocked
failed
unknown_external_outcome
formal_record_reference_returned
completed_by_destination
```

A Return is a sourced destination result. It does not create new Lite-owned formal truth.

## 10. Evaluation and commercial experiments — `ML-E01–E06`

| ID | Record | Purpose |
| --- | --- | --- |
| ML-E01 | Evaluation Run | Bounded test scope, dataset, version and time window |
| ML-E02 | Outcome Observation | Typed observation of use, response, Handoff or returned outcome |
| ML-E03 | Reuse Evidence | Evidence that a work product, lesson or Asset was reused within scope |
| ML-E04 | Safety / Privacy Finding | Defect, blocked action or boundary violation |
| ML-E05 | Commercial Experiment | Price, plan, entitlement, quota and hypothesis |
| ML-E06 | Entitlement / Fulfillment Observation | Whether an edition-specific promise was fulfilled |

Commercial experiment records may change without changing the Product Charter.

## 11. Formal objects consumed but not owned

Lite must not create parallel ownership for:

- User, Organization, Membership, Role, Permission or Policy;
- Customer, Contact, Trademark, Matter, Order or Provider;
- formal Opportunity;
- active Task or Workflow;
- Communication send state;
- Document or Evidence;
- Review approval;
- official status or External Protected Action;
- MGSN Trust, Routing or cross-Organization collaboration;
- MarkReg lifecycle records.

Lite may reference, prepare a request, send an Envelope and present the returned result.

## 12. Database and implementation warning

The `ML-*` families are semantic publication records.

They do not require:

- one database table per record;
- the same field names in every implementation;
- a cloud-only architecture;
- a specific AI, renderer, CRM or workflow engine.

Implementation must demonstrate the distinctions and scenarios, not copy the publication names mechanically.
