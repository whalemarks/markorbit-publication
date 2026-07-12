# Task Status Contract

Spec ID: B02-CONTRACT-STATUS-TASK
Spec Type: Contract Specification
Contract Name: Task Status Contract
Contract File: task-status-contract.md
Contract Category: Status
Related Controlled State Value Specification: ../../controlled-state-values/task-status-values.md (B02-CSV-TASK-STATUS)
Related Parent Object: Task
Related Owning Service: Task Service
Related API Contract: ../api/task-api-contract.md
Related Event Specs: TaskStatusChanged
Status: Draft
Version: 0.1.0
Contract Version: v0.1.0
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# 1. Purpose
Defines enforceable transition contract coverage for `Task.status`.

# 2. Contract Boundary
This contract consumes the Controlled State Value Specification and does not own state, perform mutation, define a database schema, or create an independent Core Object. Unlisted transitions return `InvalidTransition`.

# 3. Owning Service
Only Task Service may mutate `Task.status`; API and Workflow Contract validation route only.

# 4. Canonical Values
```text
Draft
Open
Assigned
InProgress
Waiting
Blocked
ReviewRequired
Completed
Cancelled
Archived
DeletedReferenceOnly
```

# 5. Allowed Transitions
```text
Draft -> Open
Draft -> Assigned
Draft -> Cancelled
Draft -> Archived
Open -> Assigned
Open -> InProgress
Open -> Waiting
Open -> Blocked
Open -> ReviewRequired
Open -> Completed
Open -> Cancelled
Assigned -> InProgress
Assigned -> Waiting
Assigned -> Blocked
Assigned -> ReviewRequired
Assigned -> Completed
Assigned -> Cancelled
InProgress -> Waiting
InProgress -> Blocked
InProgress -> ReviewRequired
InProgress -> Completed
InProgress -> Cancelled
Waiting -> Assigned
Waiting -> InProgress
Waiting -> Blocked
Waiting -> ReviewRequired
Waiting -> Cancelled
Blocked -> Assigned
Blocked -> InProgress
Blocked -> Waiting
Blocked -> ReviewRequired
Blocked -> Cancelled
ReviewRequired -> Assigned
ReviewRequired -> InProgress
ReviewRequired -> Completed
ReviewRequired -> Cancelled
Completed -> Archived
Cancelled -> Archived
Completed -> Open
Cancelled -> Open
```

# 6. Guard Requirements
Reopened is not a status. Governed reopen is only Completed -> Open or Cancelled -> Open and requires actor, permission, policy, reason, audit, event and Workflow validation.

# 7. Transition Request Decision Result Shapes
Uses `B02-CONTRACT-STATUS-TRANSITION` request, decision, and result shapes.

# 8. Event and Audit Trace
Mutation requires `TaskStatusChanged` with previous status, next status, actor, reason, correlation/idempotency where applicable, and audit reference.

# 9. Fixtures
Fixtures: `../fixtures/status-workflow/status/task/`.

# 10. Prohibited Overreach
No external protected action, filing, send, payment, provider engagement, official recordal, autonomous professional action, endpoint path change, runtime engine, or production data is authorized.
