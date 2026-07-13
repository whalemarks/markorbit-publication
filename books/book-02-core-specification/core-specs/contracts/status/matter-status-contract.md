# Matter Status Contract

Spec ID: B02-CONTRACT-STATUS-MATTER
Spec Type: Contract Specification
Contract Name: Matter Status Contract
Contract File: core-specs/contracts/status/matter-status-contract.md
Contract Category: Status
Related Controlled State Value Specification: [Matter Status Values](../../controlled-state-values/matter-status-values.md)
Related Parent Object: [Matter](../../objects/matter.md)
Related Owning Service: [Matter Service](../../services/matter-service.md)
Related API Contract: [Matter API Contract](../api/matter-api-contract.md)
Related Event Specs: MatterStatusChanged
Status: Draft
Version: 0.1.0
Contract Version: v0.1.0
MVP Phase: Phase 2
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# 1. Purpose

Defines enforceable status transition contract behavior for `Matter.status`.

# 2. Contract Meaning

The contract consumes the canonical status value specification and makes transition request, decision, and owner-Service result shapes enforceable.

# 3. Contract Boundary

It does not own state, perform mutation, create a Core Object, create a database enum, or authorize external action. Unlisted transitions return InvalidTransition.

# 4. Canonical Source

Canonical values and transition matrix come only from [Matter Status Values](../../controlled-state-values/matter-status-values.md).

# 5. Parent Ownership

[Matter](../../objects/matter.md) owns current status truth.

# 6. Owning Service

Only [Matter Service](../../services/matter-service.md) executes `MatterService.changeStatus` and produces performed results.

# 7. Transition Request Shape

Uses [Status Transition Contract](status-transition-contract.md). Required shared fields: contract_version, transition_request_reference_id, subject, current_status, requested_status, requested_action, actor_context, permission_context, policy_context, human_review_context, approval_context, source_context, and domain_guard_context. ReviewRequired -> active state requires approved Human Review outcome. Blocked -> active state requires blocker_resolution_reference_id. WaitingForOffice is not official result. Suspended is not a status.

# 8. Transition Decision Shape

Uses shared status_transition_decision. Applicable decisions: Allowed, Denied, Blocked, ReviewRequired, ApprovalRequired, PermissionRequired, PolicyRequired, InvalidState, InvalidTransition, Unknown.

# 9. Transition Result Shape

Uses shared status_transition_result. Performed results require owner_service `Matter Service`, operation `MatterService.changeStatus`, and event `MatterStatusChanged`.

# 10. Canonical Values

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

# 11. Allowed Transitions

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

# 12. Guard Requirements

ReviewRequired -> active state requires approved Human Review outcome. Blocked -> active state requires blocker_resolution_reference_id. WaitingForOffice is not official result. Suspended is not a status.

# 13. Permission and Policy

Sensitive, terminal, cancellation, completion, archival, reopen, externally sourced, or protected transitions require explicit permission/policy evidence as applicable.

# 14. Human Review and Approval

Review and approval contexts must be explicit for guarded review exits, conflicting sources, and approval-sensitive transitions; AI cannot replace them.

# 15. Source and Evidence Requirements

ReviewRequired -> active state requires approved Human Review outcome. Blocked -> active state requires blocker_resolution_reference_id. WaitingForOffice is not official result. Suspended is not a status.

# 16. Idempotency

Retryable operations require idempotency_key; replay must not duplicate mutation or Events.

# 17. Event and Audit Trace

Performed mutation requires `MatterStatusChanged` plus audit_reference_id; decision-only or failed results must not include status-changed Event proof.

# 18. API Consumption

[Matter API Contract](../api/matter-api-contract.md) must consume this contract and the shared transition contract without endpoint path changes.

# 19. AI Boundary

AI may explain or recommend review only; it cannot approve, mutate, file, send, pay, engage providers, record official action, or execute professional action.

# 20. Compatibility and Versioning

Status contract version can clarify shape and guards but cannot drift from canonical values or transition matrix.

# 21. Error Semantics

InvalidState for noncanonical status; InvalidTransition for unlisted edge; PermissionRequired, PolicyRequired, ReviewRequired, ApprovalRequired, Blocked, Denied, or Unknown for guard outcomes.

# 22. Fixture Requirements

Fixtures are in [status-workflow/status/matter](../fixtures/status-workflow/status/matter/) and must use full request/decision/result envelopes.

# 23. Valid Examples

A canonical edge with all required guard evidence may return Allowed; owner-Service execution may later return performed=true with event/audit proof.

# 24. Invalid Examples

A noncanonical status, unlisted transition, missing guard evidence, or direct API/Workflow mutation fails closed.

# 25. Prohibited Overreach

No independent status object, runtime implementation, endpoint, production data, or protected external action authorization.

# 26. Acceptance Criteria

All 27 sections exist; metadata links resolve; values/matrix match CSV spec and matrix fixture; fixture and validator semantic checks pass.

# 27. Revision Notes

0.1.0 Draft; completed by PUB-TASK-B02-003-FIX-01.
