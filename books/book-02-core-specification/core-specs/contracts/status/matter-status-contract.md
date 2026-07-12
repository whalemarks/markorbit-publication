# Matter Status Contract

Spec ID: B02-CONTRACT-STATUS-MATTER
Spec Type: Contract Specification
Contract Name: Matter Status Contract
Contract File: matter-status-contract.md
Contract Category: Status
Related Controlled State Value Specification: ../../controlled-state-values/matter-status-values.md (B02-CSV-MATTER-STATUS)
Related Parent Object: Matter
Related Owning Service: Matter Service
Related API Contract: ../api/matter-api-contract.md
Related Event Specs: MatterStatusChanged
Status: Draft
Version: 0.1.0
Contract Version: v0.1.0
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# 1. Purpose
Defines enforceable transition contract coverage for `Matter.status`.

# 2. Contract Boundary
This contract consumes the Controlled State Value Specification and does not own state, perform mutation, define a database schema, or create an independent Core Object. Unlisted transitions return `InvalidTransition`.

# 3. Owning Service
Only Matter Service may mutate `Matter.status`; API and Workflow Contract validation route only.

# 4. Canonical Values
```text
Draft
Open
InProgress
WaitingForCustomer
WaitingForAgent
WaitingForOffice
ReviewRequired
Blocked
Completed
Cancelled
Archived
DeletedReferenceOnly
```

# 5. Allowed Transitions
```text
Draft -> Open
Draft -> Cancelled
Draft -> Archived
Open -> InProgress
Open -> WaitingForCustomer
Open -> WaitingForAgent
Open -> WaitingForOffice
Open -> ReviewRequired
Open -> Blocked
Open -> Completed
Open -> Cancelled
InProgress -> WaitingForCustomer
InProgress -> WaitingForAgent
InProgress -> WaitingForOffice
InProgress -> ReviewRequired
InProgress -> Blocked
InProgress -> Completed
InProgress -> Cancelled
WaitingForCustomer -> InProgress
WaitingForCustomer -> ReviewRequired
WaitingForCustomer -> Blocked
WaitingForCustomer -> Cancelled
WaitingForAgent -> InProgress
WaitingForAgent -> ReviewRequired
WaitingForAgent -> Blocked
WaitingForAgent -> Cancelled
WaitingForOffice -> InProgress
WaitingForOffice -> ReviewRequired
WaitingForOffice -> Blocked
WaitingForOffice -> Cancelled
ReviewRequired -> InProgress
ReviewRequired -> WaitingForCustomer
ReviewRequired -> WaitingForAgent
ReviewRequired -> WaitingForOffice
ReviewRequired -> Blocked
ReviewRequired -> Completed
ReviewRequired -> Cancelled
Blocked -> InProgress
Blocked -> ReviewRequired
Blocked -> Cancelled
Completed -> Archived
Cancelled -> Archived
```

# 6. Guard Requirements
Leaving ReviewRequired requires review outcome; leaving Blocked requires blocker resolution; WaitingForOffice is not official outcome; Suspended is not canonical.

# 7. Transition Request Decision Result Shapes
Uses `B02-CONTRACT-STATUS-TRANSITION` request, decision, and result shapes.

# 8. Event and Audit Trace
Mutation requires `MatterStatusChanged` with previous status, next status, actor, reason, correlation/idempotency where applicable, and audit reference.

# 9. Fixtures
Fixtures: `../fixtures/status-workflow/status/matter/`.

# 10. Prohibited Overreach
No external protected action, filing, send, payment, provider engagement, official recordal, autonomous professional action, endpoint path change, runtime engine, or production data is authorized.
