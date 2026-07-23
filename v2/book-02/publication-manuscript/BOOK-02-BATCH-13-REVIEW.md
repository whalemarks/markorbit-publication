# Book 02 v2 — Publication Reconstruction Batch 13 Review

## 1. Scope

Batch 13 converted the Batch 12 pre-proposal findings into noncanonical research fixtures and a consumer-proof gate.

Files added:

- `RESEARCH-FIXTURE-01-PRODUCTION-AUTHORIZATION-PERMISSION-PROFILE.md`;
- `RESEARCH-FIXTURE-02-WORK-PACKAGE-TASK-WORKFLOW-PROFILE.md`;
- `RESEARCH-FIXTURE-03-BILATERAL-ASSIGNMENT-LIFECYCLE.md`;
- `RESEARCH-FIXTURE-04-CONTRIBUTION-SUBMISSION-AND-SUPERSESSION.md`;
- `RESEARCH-FIXTURE-05-OUTCOME-ACCEPTANCE-WITHOUT-FORMALIZATION.md`;
- `BOOK-02-CONSUMER-PROOF-MATRIX.md`;
- `EXTERNAL-QUALIFICATION-SOURCE-AND-PRIVACY-REVIEW-PLAN.md`;
- this review record.

All fixtures are explicitly noncanonical. They do not modify frozen Book 02 contracts, public Core exports or downstream repositories.

## 2. Production Authorization fixture result

The fixture demonstrates that a bounded Production Authorization can plausibly be represented as:

```text
Frozen Permission
+ Policy constraints
+ Capability reference
+ implementation/version binding
+ effective period
+ data and Tool ceilings
+ Human Review requirement
```

The profile supports both human and AI/system subjects while preserving:

```text
Production Authorized
≠ Assigned
≠ Professionally Authorized
≠ Approved for External Action
```

Result:

```text
Permission-profile hypothesis: PLAUSIBLE
Frozen Permission change required now: NO
New Production Authorization Object proven necessary: NO
```

## 3. Work Package fixture result

The fixture models a package-level envelope over several frozen Tasks and one Workflow Contract.

It demonstrates possible value when:

- several Tasks contribute to one bounded deliverable;
- acceptance occurs at package level;
- a Task can be replaced without losing package continuity;
- several Contributors or reviewers participate;
- package purpose and exclusions must be preserved.

It also preserves:

```text
Every Task ≠ Work Package
All Tasks Completed ≠ Work Package Accepted
Work Package State ≠ Task State
```

Result:

```text
F2 Task / Workflow profile is plausible: YES
Shared root Object proven necessary: NO
Independent consumer proof required: YES
```

## 4. Bilateral Assignment fixture result

The fixture isolates the narrow case not fully represented by frozen Task assignee fields:

```text
Offered
→ Accepted
→ Active
→ Completed
```

with possible decline, expiry, suspension, revocation, replacement and cancellation.

It demonstrates the need to preserve:

- attributable acceptance;
- cross-Workplace parties;
- exact work and version;
- data and Tool access;
- Permission, Policy and Eligibility;
- professional-authority and conflict references;
- customer-contact and commercial rules;
- revocation effects.

The following locks remain:

```text
Assignment Accepted
≠ Customer Relationship Transferred
≠ Professional Authority Created
≠ Formal State Updated
```

Result:

```text
Bilateral Assignment is semantically distinct: YES
Potential F3 candidate: YES
Consumer proof completed: NO
Formal proposal ready: NO
```

## 5. Contribution fixture result

Contribution was successfully modeled as an attributable submission profile over frozen Task, Document, Evidence, Event and Human Review references.

The fixture preserves:

- exact work basis;
- contributor identity and represented organization;
- submitted artifacts and Evidence;
- submission version;
- scope, exclusions, assumptions and Unknowns;
- exact-version Review;
- supersession without erasure.

```text
Contribution Submitted
≠ Contribution Accepted
≠ Task Completed
≠ Official Truth
```

Result:

```text
F2 submission profile is plausible: YES
Document/Evidence ownership remains unchanged: YES
Root Object proven necessary: NO
```

## 6. Outcome fixture result

Outcome was modeled as a purpose-limited acceptance profile with exact accepted input versions, Human Review, accepting authority, scope, exclusions, expiry and correction trace.

The formalization boundary remains explicit:

```text
Outcome Accepted
≠ Apply
≠ External Submission
≠ Formal State Updated
```

The fixture also demonstrates that one Contribution can be accepted for one purpose but not another.

Result:

```text
F2 acceptance profile is plausible: YES
Formal-state separation demonstrated: YES
Shared root identity proven necessary: NO
```

## 7. Consumer-proof audit

The following repositories or publication consumers were evaluated:

```text
whalemarks/markorbit-execution
whalemarks/markorbit-lite
Book 05 / MarkReg publication architecture
```

Observed repository facts:

- `markorbit-execution` exists and states that it implements Book 03 coordination, does not redefine Book 02, is not a Product UI or external action system and currently identifies `EXEC-TASK-001` as its programme;
- `markorbit-lite` exists, but a `README.md` was not resolved on `main` during this batch;
- no candidate-profile implementation was identified in either repository;
- MarkReg currently provides publication-level use cases rather than independent implementation proof for these profiles.

Current proof levels:

```text
Book 03 Execution: L1 publication/repository intent
MarkReg: L1 publication use case
Lite: L1 publication/repository existence
Two independent L2 consumers: NO
```

Therefore the formal shared-contract consumer gate has not passed.

## 8. Recommended consumer cases

### Book 03

Must prove fixture-level validation and state separation for all five profiles.

### MarkReg

Recommended use case:

```text
reviewable international trademark filing package
```

The proof should show:

```text
filing-readiness Outcome
≠ customer final instruction
≠ official filing
```

### Lite

Recommended use case:

```text
source-backed trademark content package
```

The proof should preserve Product-local Content Brief and Campaign Asset records outside Core.

## 9. External qualification review plan

The review plan establishes:

- official and nonofficial source hierarchy;
- external credential state versus platform verification state;
- minimum source and verification fields;
- privacy, disciplinary-data and cross-border questions;
- source terms, storage, redistribution and AI-training questions;
- conflict and privileged-information boundaries;
- correction and dispute processes;
- jurisdiction research template;
- three-jurisdiction minimum sample requirement.

No jurisdiction-specific legal conclusion was made in this batch.

Current status:

```text
Source hierarchy: DEFINED
Privacy questions: DEFINED
Rights questions: DEFINED
Legal review: NOT COMPLETED
Professional review: NOT COMPLETED
Formal A1 proposal gate: NOT PASSED
```

## 10. Research task recommendations

The batch recommends, but does not create, the following downstream tasks:

```text
EXEC-RESEARCH-001
Fixture-only parsing and validation of the five profiles
outside public Core exports.

MARKREG-RESEARCH-001
One filing-readiness consumer proof.

LITE-RESEARCH-001
One source-backed content consumer proof.

CROSS-CONSUMER-REVIEW-001
Field, lifecycle and ownership comparison.
```

## 11. Candidate status after fixtures

| Candidate | Status after Batch 13 |
|---|---|
| Production Authorization | Permission profile remains preferred |
| Work Package | F2 profile remains preferred |
| Bilateral Assignment | strongest remaining F3 candidate |
| Contribution | F2 submission profile remains preferred |
| Outcome | F2 acceptance profile remains preferred |
| External Qualification Reference | pre-proposal source/legal research remains required |
| Professional Authority Reference | no fixture yet; depends on A1 and appointment research |

## 12. Authority locks

```text
Active Canon modified: NO
Frozen Book 02 modified: NO
Formal Change Proposal opened: NO
New Core Object activated: NO
Public Core export changed: NO
Task or Human Review replaced: NO
Permission controlled values changed: NO
Book 03 implementation changed: NO
MarkReg or Lite implementation changed: NO
Professional qualification issued by platform: NO
Professional Authority granted: NO
AI external-action authority granted: NO
Production or migration authorized: NO
```

## 13. Batch verdict

```text
Noncanonical Production Authorization fixture: COMPLETE
Noncanonical Work Package fixture: COMPLETE
Noncanonical bilateral Assignment fixture: COMPLETE
Noncanonical Contribution fixture: COMPLETE
Noncanonical Outcome fixture: COMPLETE
Consumer-proof matrix: COMPLETE
External qualification review plan: COMPLETE
Independent L2 consumer proof: INCOMPLETE
Formal Change Proposal readiness: INCOMPLETE
Frozen replacement: NOT AUTHORIZED
```

## 14. Recommended Batch 14

Batch 14 should prepare downstream executable task instructions rather than expand Book 02 prose:

```text
1. Codex-ready EXEC-RESEARCH-001 task for markorbit-execution
2. fixture schemas and validation acceptance criteria
3. MarkReg filing-readiness consumer-proof specification
4. Lite content-package consumer-proof specification
5. cross-consumer comparison checklist
6. formal gate deciding whether bilateral Assignment advances to a Change Proposal
```

No downstream implementation should occur until its repository-local task is separately reviewed and accepted.