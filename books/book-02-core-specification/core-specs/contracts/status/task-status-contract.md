# Task Status Contract

Spec ID: B02-CONTRACT-STATUS-TASK
Spec Type: Contract Specification
Contract Name: Task Status Contract
Contract File: core-specs/contracts/status/task-status-contract.md
Contract Category: Status
Related Controlled State Value Specification: [Task Status Values](../../controlled-state-values/task-status-values.md)
Related Parent Object: [Task](../../objects/task.md)
Related Owning Service: [Task Service](../../services/task-service.md)
Related API Contract: [Task API Contract](../api/task-api-contract.md)
Related Event Specs: TaskStatusChanged
Status: Draft
Version: 0.1.0
Contract Version: v0.1.0
MVP Phase: Phase 2
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# 1. Purpose

Defines enforceable status transition contract behavior for `Task.status`.

# 2. Contract Meaning

The contract consumes the canonical status value specification and makes transition request, decision, and owner-Service result shapes enforceable.

# 3. Contract Boundary

It does not own state, perform mutation, create a Core Object, create a database enum, or authorize external action. Unlisted transitions return InvalidTransition.

# 4. Canonical Source

Canonical values and transition matrix come only from [Task Status Values](../../controlled-state-values/task-status-values.md).

# 5. Parent Ownership

[Task](../../objects/task.md) owns current status truth.

# 6. Owning Service

Only [Task Service](../../services/task-service.md) executes `TaskService.changeStatus` and produces performed results.

# 7. Transition Request Shape

Uses [Status Transition Contract](status-transition-contract.md). Required shared fields: contract_version, transition_request_reference_id, subject, current_status, requested_status, requested_action, actor_context, permission_context, policy_context, human_review_context, approval_context, source_context, and domain_guard_context. Open -> Assigned requires assignee_reference_id. InProgress -> Completed requires completion_context_reference_id. Governed reopen requires actor, permission Allowed, policy Allowed, reason_code, idempotency, audit, and Workflow validation where applicable; only Completed -> Open and Cancelled -> Open are allowed. Reopened is never next status.

# 8. Transition Decision Shape

Uses shared status_transition_decision. Applicable decisions: Allowed, Denied, Blocked, ReviewRequired, ApprovalRequired, PermissionRequired, PolicyRequired, InvalidState, InvalidTransition, Unknown.

# 9. Transition Result Shape

Uses shared status_transition_result. Performed results require owner_service `Task Service`, operation `TaskService.changeStatus`, and event `TaskStatusChanged`.

# 10. Canonical Values

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

# 11. Allowed Transitions

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

# 12. Guard Requirements

Open -> Assigned requires assignee_reference_id. InProgress -> Completed requires completion_context_reference_id. Governed reopen requires actor, permission Allowed, policy Allowed, reason_code, idempotency, audit, and Workflow validation where applicable; only Completed -> Open and Cancelled -> Open are allowed. Reopened is never next status.

# 13. Permission and Policy

Sensitive, terminal, cancellation, completion, archival, reopen, externally sourced, or protected transitions require explicit permission/policy evidence as applicable.

# 14. Human Review and Approval

Review and approval contexts must be explicit for guarded review exits, conflicting sources, and approval-sensitive transitions; AI cannot replace them.

# 15. Source and Evidence Requirements

Open -> Assigned requires assignee_reference_id. InProgress -> Completed requires completion_context_reference_id. Governed reopen requires actor, permission Allowed, policy Allowed, reason_code, idempotency, audit, and Workflow validation where applicable; only Completed -> Open and Cancelled -> Open are allowed. Reopened is never next status.

# 16. Idempotency

Retryable operations require idempotency_key; replay must not duplicate mutation or Events.

# 17. Event and Audit Trace

Performed mutation requires `TaskStatusChanged` plus audit_reference_id; decision-only or failed results must not include status-changed Event proof.

# 18. API Consumption

[Task API Contract](../api/task-api-contract.md) must consume this contract and the shared transition contract without endpoint path changes.

# 19. AI Boundary

AI may explain or recommend review only; it cannot approve, mutate, file, send, pay, engage providers, record official action, or execute professional action.

# 20. Compatibility and Versioning

Status contract version can clarify shape and guards but cannot drift from canonical values or transition matrix.

# 21. Error Semantics

InvalidState for noncanonical status; InvalidTransition for unlisted edge; PermissionRequired, PolicyRequired, ReviewRequired, ApprovalRequired, Blocked, Denied, or Unknown for guard outcomes.

# 22. Fixture Requirements

Fixtures are in [status-workflow/status/task](../fixtures/status-workflow/status/task/) and must use full request/decision/result envelopes.

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
