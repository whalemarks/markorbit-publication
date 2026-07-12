# Trademark Status Contract

Spec ID: B02-CONTRACT-STATUS-TRADEMARK
Spec Type: Contract Specification
Contract Name: Trademark Status Contract
Contract File: trademark-status-contract.md
Contract Category: Status
Related Controlled State Value Specification: ../../controlled-state-values/trademark-status-values.md (B02-CSV-TRADEMARK-STATUS)
Related Parent Object: Trademark
Related Owning Service: Trademark Service
Related API Contract: ../api/trademark-api-contract.md
Related Event Specs: TrademarkStatusChanged
Status: Draft
Version: 0.1.0
Contract Version: v0.1.0
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# 1. Purpose
Defines enforceable transition contract coverage for `Trademark.status`.

# 2. Contract Boundary
This contract consumes the Controlled State Value Specification and does not own state, perform mutation, define a database schema, or create an independent Core Object. Unlisted transitions return `InvalidTransition`.

# 3. Owning Service
Only Trademark Service may mutate `Trademark.status`; API and Workflow Contract validation route only.

# 4. Canonical Values
```text
Draft
Planned
PendingFiling
Filed
UnderExamination
Published
Opposed
Registered
Refused
Abandoned
Cancelled
Expired
Invalidated
RenewalDue
ReviewRequired
Archived
DeletedReferenceOnly
```

# 5. Allowed Transitions
```text
Draft -> Planned
Planned -> Draft
Draft -> PendingFiling
Planned -> PendingFiling
PendingFiling -> Planned
PendingFiling -> Filed
PendingFiling -> ReviewRequired
PendingFiling -> Abandoned
Filed -> UnderExamination
Filed -> Published
Filed -> Opposed
Filed -> Registered
Filed -> Refused
Filed -> Abandoned
Filed -> ReviewRequired
UnderExamination -> Published
UnderExamination -> Opposed
UnderExamination -> Registered
UnderExamination -> Refused
UnderExamination -> Abandoned
UnderExamination -> ReviewRequired
Published -> Opposed
Published -> Registered
Published -> Refused
Published -> Abandoned
Published -> ReviewRequired
Opposed -> Registered
Opposed -> Refused
Opposed -> Abandoned
Opposed -> ReviewRequired
Registered -> RenewalDue
Registered -> Expired
Registered -> Cancelled
Registered -> Invalidated
Registered -> ReviewRequired
RenewalDue -> Registered
RenewalDue -> Expired
RenewalDue -> Cancelled
RenewalDue -> ReviewRequired
Refused -> ReviewRequired
Refused -> Abandoned
Refused -> Archived
Abandoned -> ReviewRequired
Abandoned -> Archived
Cancelled -> ReviewRequired
Cancelled -> Archived
Expired -> ReviewRequired
Expired -> Archived
Invalidated -> ReviewRequired
Invalidated -> Archived
```

# 6. Guard Requirements
Official/procedural-sensitive transitions require source reference, timestamp or version, jurisdiction reference, normalization evidence, and validation result. Source conflict returns ReviewRequired; Archived and DeletedReferenceOnly are terminal for ordinary flow.

# 7. Transition Request Decision Result Shapes
Uses `B02-CONTRACT-STATUS-TRANSITION` request, decision, and result shapes.

# 8. Event and Audit Trace
Mutation requires `TrademarkStatusChanged` with previous status, next status, actor, reason, correlation/idempotency where applicable, and audit reference.

# 9. Fixtures
Fixtures: `../fixtures/status-workflow/status/trademark/`.

# 10. Prohibited Overreach
No external protected action, filing, send, payment, provider engagement, official recordal, autonomous professional action, endpoint path change, runtime engine, or production data is authorized.
