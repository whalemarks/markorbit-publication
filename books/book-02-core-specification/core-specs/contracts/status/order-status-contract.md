# Order Status Contract

Spec ID: B02-CONTRACT-STATUS-ORDER
Spec Type: Contract Specification
Contract Name: Order Status Contract
Contract File: order-status-contract.md
Contract Category: Status
Related Controlled State Value Specification: ../../controlled-state-values/order-status-values.md (B02-CSV-ORDER-STATUS)
Related Parent Object: Order
Related Owning Service: Order Service
Related API Contract: ../api/order-api-contract.md
Related Event Specs: OrderStatusChanged
Status: Draft
Version: 0.1.0
Contract Version: v0.1.0
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# 1. Purpose
Defines enforceable transition contract coverage for `Order.status`.

# 2. Contract Boundary
This contract consumes the Controlled State Value Specification and does not own state, perform mutation, define a database schema, or create an independent Core Object. Unlisted transitions return `InvalidTransition`.

# 3. Owning Service
Only Order Service may mutate `Order.status`; API and Workflow Contract validation route only.

# 4. Canonical Values
```text
Draft
PendingConfirmation
Confirmed
ReadyForMatter
MatterCreated
InProgress
WaitingForCustomer
Completed
Cancelled
Archived
DeletedReferenceOnly
```

# 5. Allowed Transitions
```text
Draft -> PendingConfirmation
Draft -> Cancelled
Draft -> Archived
PendingConfirmation -> Draft
PendingConfirmation -> Confirmed
PendingConfirmation -> Cancelled
Confirmed -> ReadyForMatter
Confirmed -> InProgress
Confirmed -> Cancelled
ReadyForMatter -> MatterCreated
ReadyForMatter -> InProgress
ReadyForMatter -> Cancelled
MatterCreated -> InProgress
MatterCreated -> Completed
MatterCreated -> Cancelled
InProgress -> WaitingForCustomer
InProgress -> Completed
InProgress -> Cancelled
WaitingForCustomer -> InProgress
WaitingForCustomer -> Cancelled
Completed -> Archived
Cancelled -> Archived
```

# 6. Guard Requirements
acceptOrder only requests PendingConfirmation -> Confirmed. Accepted and Rejected are not statuses. Confirmed is not payment completion. MatterCreated requires Matter reference.

# 7. Transition Request Decision Result Shapes
Uses `B02-CONTRACT-STATUS-TRANSITION` request, decision, and result shapes.

# 8. Event and Audit Trace
Mutation requires `OrderStatusChanged` with previous status, next status, actor, reason, correlation/idempotency where applicable, and audit reference.

# 9. Fixtures
Fixtures: `../fixtures/status-workflow/status/order/`.

# 10. Prohibited Overreach
No external protected action, filing, send, payment, provider engagement, official recordal, autonomous professional action, endpoint path change, runtime engine, or production data is authorized.
