# Bilateral Assignment — Formal Change Proposal Gate

## Candidate

```text
B02-CP-RESEARCH-B1
Accepted Bilateral / Cross-Workplace Assignment
```

## Current status

```text
Semantically distinct from simple Task assignment: YES
Noncanonical fixture available: YES
Independent L2 consumer proof: NO
Formal Change Proposal ready: NO
```

## Problem statement

Frozen Task can identify an assignee and responsibility reference. It does not fully preserve a bilateral or cross-Workplace agreement to accept exact work, including offer, acceptance, expiry, revocation, data access and continuity obligations.

The candidate must remain narrower than a universal Assignment Object.

## Proposed narrow scope

The gate concerns only an Assignment that:

- binds two or more separately accountable parties;
- crosses an Organization or Workplace boundary, or otherwise requires attributable acceptance;
- refers to exact work and version;
- has an independently meaningful lifecycle;
- carries bounded access, communication or commercial obligations;
- must survive Task reassignment or replacement as an auditable record.

It does not cover simple internal Task allocation.

## Required evidence before formal opening

### Consumer evidence

- Execution L2 fixture implementation;
- one Product L2 fixture implementation, preferably MarkReg;
- field-by-field comparison;
- lifecycle comparison;
- evidence that Task assignment alone is insufficient.

### Semantic evidence

- stable identifier;
- required fields;
- lifecycle and transition owners;
- exact relationship to Task and Work Package;
- relation to Permission, Policy and Eligibility;
- relation to Provider Appointment and Professional Authority;
- cancellation and revocation behavior;
- correction and supersession rules.

### Compatibility evidence

- no change to frozen Task statuses;
- no required renaming of Task fields;
- additive or profile-first migration strategy;
- no automatic creation for existing Tasks;
- no public export before version and migration review.

### Negative fixture evidence

Must reject:

```text
Task assignee set = Assignment accepted
Eligibility passed = Assignment accepted
Provider listed = Assignment accepted
Assignment accepted = Professional Authority
Assignment accepted = Customer Relationship transferred
Assignment completed = Outcome accepted
Assignment completed = Formal State updated
```

## Authority and ownership requirements

The formal proposal must identify:

- candidate Assignment-owning Service;
- which actor may offer;
- which actor may accept;
- who may suspend or revoke;
- whether acceptance may be delegated;
- how represented Organization or Workplace is recorded;
- how conflicts and professional appointment remain separate;
- how Task Service consumes the record without losing Task ownership;
- how Book 03 enforces the lifecycle at runtime.

## Lifecycle research set

Candidate states:

```text
Draft
Offered
Accepted
Active
Declined
Expired
Suspended
Revoked
Completed
Cancelled
Replaced
```

These are not approved controlled values.

The proposal must show whether all are necessary and whether `Accepted` and `Active` need to remain separate.

## Gate decision logic

### Advance to formal Change Proposal

Only when:

- two independent L2 consumers use materially identical fields;
- both require attributable acceptance independent of Task state;
- lifecycle ownership is stable;
- negative authority tests pass;
- F1 Task composition and F2 Task profile are demonstrably insufficient;
- compatibility and migration plan exist.

### Retain as F2 profile

When:

- only one Product needs it;
- lifecycle is local workflow policy;
- Task plus Event and Human Review are sufficient;
- cross-Workplace acceptance is rare or not independently stored;
- shared fields are unstable.

### Reject

When the candidate:

- duplicates Task;
- absorbs Provider Appointment;
- creates Professional Authority;
- transfers Customer Relationship;
- owns formal-state mutation;
- requires Book 03 runtime logic inside Core.

## Current gate result

```text
Consumer evidence: INCOMPLETE
Semantic fixture: COMPLETE AT RESEARCH LEVEL
Ownership decision: INCOMPLETE
Compatibility decision: INCOMPLETE
Legal/professional review: NOT REQUIRED FOR GENERIC ASSIGNMENT,
BUT REQUIRED WHERE RESERVED PROFESSIONAL ACTION IS REFERENCED
Formal proposal opening: BLOCKED
```

## Next decision owner

After Execution and MarkReg or Lite complete L2 proofs, run `CROSS-CONSUMER-REVIEW-001`.

That review may issue one of:

```text
RETAIN_AS_TASK_PROFILE
ADVANCE_B1_TO_FORMAL_CHANGE_PROPOSAL
MORE_EVIDENCE_REQUIRED
REJECT_B1
```

## Constitutional lock

```text
Assignment records acceptance of exact work.
It does not create capability, qualification,
professional authority, customer ownership
or formal-state authority.
```
