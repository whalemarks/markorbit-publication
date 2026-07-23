# Book 07 v2 — Glossary and Cross-reference Plan

## 1. Purpose

This plan defines the reader-facing glossary and cross-reference system required before publication freeze.

It is editorial apparatus, not a new semantic baseline.

## 2. Glossary structure

Each glossary entry should contain:

```text
Preferred Term
Reader-facing Definition
Primary Chapter
Related Terms
Do Not Confuse With
Cross-book Source Where Useful
```

## 3. Core glossary candidates

| Term | Reader-facing definition | Primary chapter |
|---|---|---|
| Accountable Route | The complete service path joining an accountable Provider, qualified Capability, valid Package, current Eligibility, explicit Acceptance, versioned authority, observable fulfillment, Evidence and recovery. | CH32 |
| Capability | A bounded service that an Organization may be able to provide in a defined context. | CH05 |
| Capability Claim | A Provider’s assertion about the Capability it proposes to supply. | CH06 |
| Capability Need | A purpose-limited representation of external capability required by an Originating Workplace. | CH09 |
| Candidate Route Set | A bounded set of materially different Eligible Routes presented for decision. | CH11 |
| Eligibility | A current decision that a particular Provider, Capability and Package may be considered for an exact Need now. | CH10 |
| Evidence | Attributable material supporting an assertion, milestone or state. | CH08 / CH22 |
| External Protected Action | An external act requiring specific authority and controls. | CH14 |
| Incident | A governed review of an event that may create material risk or harm. | CH26 |
| Instruction Package | The versioned, attributable handoff stating exactly what a Provider may prepare or do. | CH14 |
| MGSN | Mark Global Service Network, the managed professional fulfillment network described by Book 07. | CH03 / CH04 |
| MGSN Connection | The controlled boundary through which a Workplace projects Needs and receives governed Returns. | CH04 / CH09 |
| MGSN Qualification | Network permission for a Provider to offer a specific Capability under current MGSN rules. | CH08 |
| Milestone | An observable fulfillment stage with an expected result, Evidence and acceptance criteria. | CH21 |
| Originating Workplace | The Workplace projecting the Need while retaining the customer relationship and internal Matter context. | CH04 / CH09 |
| Owning Service | The service holding formal business-state authority. | CH04 / CH22 |
| Professional Authority | Authority to perform a professional act within the applicable scope and jurisdiction. | CH08 |
| Professional Qualification | An externally grounded recognized status relevant to professional service. | CH08 |
| Provider Acceptance | The Provider’s explicit commitment to the exact engagement conditions. | CH13 |
| Provider Allocation | A pending request asking a Provider to consider and accept a defined route. | CH13 |
| Provider Network Profile | MGSN’s governed representation of an Organization as potential supply. | CH05 |
| Provider Organization | The accountable Organization supplying or proposing to supply the service. | CH05 |
| Provider Return | A typed Evidence package returned by a Provider for a milestone, exception or closure. | CH22 |
| Recommendation | An explainable preferred route among Eligible alternatives. | CH12 |
| Relationship Provenance | Evidence of how a participant relationship originated and which bounded protections apply. | CH05 / CH29 |
| Service Package | A reusable, admitted baseline defining scope, cost layers, assumptions, deliverables, Evidence and exclusions. | CH07 / CH17 |
| Trust | Service-specific, evidence-backed, time-bound operating confidence. | CH25 |
| User Disposition | The user’s decision to confirm, reject, question or rematch a Recommendation. | CH12 |
| Workplace | A sovereign operating context that retains its own customers, Knowledge, permissions and obligations. | CH04 |

## 4. Required distinction boxes

The final glossary should include a compact distinction section:

```text
Capability Claim
≠ Professional Qualification
≠ MGSN Qualification
≠ Eligibility
≠ Matter-specific Authority
```

```text
Service Package
≠ Instruction Package
```

```text
Recommendation
≠ Provider Allocation
≠ Provider Acceptance
≠ Customer Instruction
```

```text
Provider Return
≠ Official Evidence
≠ Formal State Update
```

```text
Incident
≠ Dispute
```

## 5. Cross-book map

Book 07 should include one reader-facing map:

| Related book | What Book 07 relies on | What remains outside Book 07 |
|---|---|---|
| Book 02 | Shared semantic objects, Evidence and authority distinctions | Core semantic ownership and controlled values |
| Book 03 | Governed execution, review, recovery and safe retry | Runtime execution authority |
| Book 04 | Workplace sovereignty and MGSN Connection | Workplace-owned customer and operational context |
| Book 05 | Service delivery and formal-state handoff examples | MarkReg service-specific formal state |
| Book 06 | Demand guidance and opportunity pathways | Lite-owned user guidance and daily-work context |

## 6. Chapter cross-reference rules

Use cross-references only when they prevent repeated explanation.

Preferred form:

> CH08 distinguishes Professional Qualification from MGSN Qualification; this chapter asks whether the qualified route is currently Eligible for the exact Need.

Avoid:

> See above.

Avoid repository-facing identifiers in reader prose.

## 7. Planned high-value cross-references

- CH05 → CH08 for Qualification and Professional Authority;
- CH06 → CH07 for Service Package admission;
- CH08 → CH10 for current Eligibility;
- CH09 → CH15 for later communication disclosure;
- CH12 → CH13 for Provider Allocation and Acceptance;
- CH14 → CH18 for Funds Checkpoints;
- CH19 → CH21 for Milestone Evidence;
- CH22 → CH23 for Correction-created Needs;
- CH24 → CH25 for recovery Evidence entering Trust;
- CH26 → CH27 for unresolved contested issues;
- CH28 → CH29 for learning becoming reliability rather than lock-in;
- CH31 → CH32 for the infrastructure scorecard.

## 8. Publication action

The final glossary should be generated only after final terminology normalization so it does not preserve obsolete variants.

The cross-book map and distinction boxes should appear in reader apparatus or appendices, not be repeated at length in every chapter.