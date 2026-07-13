# Book 02 Change Proposals

## Purpose

Book 02 Change Proposals govern semantic changes to the frozen Book 02 Core Specification baseline.

## When a proposal is required

A proposal is required before changing frozen Book 02 semantics, including Core Objects, ownership, canonical status values, transition matrices, API or Contract semantics, decision vocabulary, Permission / Policy / Human Review boundaries, Event semantics, Workflow mutation authority, or normative implementation behavior.

## Proposal lifecycle

```text
Proposed
    ↓
Triaged
    ↓
ImpactReviewed
    ↓
OwnerReview
    ↓
Accepted | Rejected | Deferred
    ↓
ScheduledForVersion
```

## Decision authority

The MarkOrbit Publications Editorial Board owns final Book 02 Change Proposal decisions unless a later governance record delegates authority explicitly.

## Compatibility classification

Each proposal must classify compatibility as one of:

- Documentation-only
- Clarification
- Additive-compatible
- Behavior-changing
- Breaking
- Deprecation
- Removal

## Implementation impact review

Each proposal must identify affected implementation repositories, runtime contracts, validators, migrations, fixtures, tests, and rollout constraints before owner review.

## Cross-book impact review

Each proposal must identify effects on Book 03, Book 04, product repositories, implementation architecture, and cross-project conformance expectations.

## Acceptance and rejection

Accepted proposals record an approved semantic decision. Rejected proposals record why the baseline remains unchanged. Deferred proposals remain inactive until explicitly rescheduled.

An accepted proposal does not modify Book 02 by itself.

A separate approved implementation/publication task
must apply the accepted proposal.

## Versioning effect

Accepted semantic changes must be scheduled for a Book 02 version or errata vehicle before publication edits are made.

## Prohibited shortcuts

Do not bypass this process through direct edits, implementation-driven rewrites, product-specific Core additions, silent contract changes, or unversioned semantic expansion.
