# Book 02 v2 Reconciliation Review

## Decision

`READY FOR OWNER REVIEW — NO CORE CHANGE ACTIVATED`

## What this phase completed

This package reconciles the merged v2 Books 01, 03, 04, 05, 06 and 07 against the frozen Core boundary.

It:

- defines a five-level semantic classification method;
- maps major v2 concepts into existing, compositional, profile, candidate and Change Proposal classes;
- separates root objects from contextual roles, profiles, controlled vocabularies and Product-local records;
- identifies the strongest candidate additions;
- writes a reconciled Book 02 v2 manuscript that labels candidates explicitly;
- preserves the frozen baseline and active Canon.

## Main conclusion

The v2 rewrite does not require every new concept to enter Core.

Most new terms can remain:

- profiles;
- controlled roles;
- projections;
- Product-local specializations;
- shared contract profiles over existing semantics.

The strongest candidate cluster is:

```text
Work Package
Assignment
Contribution
Outcome
```

The second candidate cluster is:

```text
Engagement
Engagement Role vocabulary
Relationship Owner
Delivery Owner
Professional Authority
```

The third candidate cluster is:

```text
Need
Capability Certification
Production Authorization
shared level and mode vocabularies
```

## Locks preserved

- Core remains semantic authority, not central business-state owner.
- Owning Services retain formal-state authority.
- Matter remains distinct from Order.
- Workflow, Work Package, Step and Task are not collapsed.
- Contribution remains distinct from accepted Outcome.
- accepted Outcome remains distinct from formal mutation.
- Projection does not transfer ownership.
- Return requires originating validation.
- certification does not equal professional qualification.
- Product-local commerce and network objects remain outside Core unless later evidence justifies promotion.

## Critical unresolved questions

1. Does the frozen task model already contain enough fields to represent Work Package, Assignment and Contribution without new root objects?
2. Can Engagement be represented by an existing Contract, Matter, Relationship and participant-role composition?
3. Is Need distinct enough from Request, Intake and Opportunity to justify a new identifier?
4. Should Production Authorization share a generic authorization lifecycle or become a dedicated object?
5. Which L1–L5, M0–M5, R0–R4 and P0–P4 vocabularies are stable semantics rather than policy presets?
6. Which service owns each candidate object’s formal lifecycle?

## Recommended next gate

Do not immediately expand this into unrestricted prose or implementation.

Proceed in this order:

```text
1. frozen Core field-level inventory
2. work-object cluster mapping
3. Engagement cluster mapping
4. credential and authorization mapping
5. formal Core Change Proposal decisions
6. cross-book terminology and authority audit
7. Portfolio v2 release-state decision
```

## Recommended first implementation-facing task

The first follow-up should be a contract audit, not code generation:

> Compare the frozen Core Task, Workflow, Evidence, Actor, Review, Matter, Order, Handoff and Return contracts against the proposed Work Package, Assignment, Contribution and Outcome meanings. Produce a field-by-field equivalence and gap report without changing implementation.

This is the safest route because Books 03 and 05 depend most directly on the work-object cluster.
