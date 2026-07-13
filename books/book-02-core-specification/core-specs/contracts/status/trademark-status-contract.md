# Trademark Status Contract

Spec ID: B02-CONTRACT-STATUS-TRADEMARK
Spec Type: Contract Specification
Contract Name: Trademark Status Contract
Contract File: core-specs/contracts/status/trademark-status-contract.md
Contract Category: Status
Related Controlled State Value Specification: [Trademark Status Values](../../controlled-state-values/trademark-status-values.md)
Related Parent Object: [Trademark](../../objects/trademark.md)
Related Owning Service: [Trademark Service](../../services/trademark-service.md)
Related API Contract: [Trademark API Contract](../api/trademark-api-contract.md)
Related Event Specs: TrademarkStatusChanged
Status: Draft
Version: 0.1.0
Contract Version: v0.1.0
MVP Phase: Phase 2
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# 1. Purpose

Defines enforceable status transition contract behavior for `Trademark.status`.

# 2. Contract Meaning

The contract consumes the canonical status value specification and makes transition request, decision, and owner-Service result shapes enforceable.

# 3. Contract Boundary

It does not own state, perform mutation, create a Core Object, create a database enum, or authorize external action. Unlisted transitions return InvalidTransition.

# 4. Canonical Source

Canonical values and transition matrix come only from [Trademark Status Values](../../controlled-state-values/trademark-status-values.md).

# 5. Parent Ownership

[Trademark](../../objects/trademark.md) owns current status truth.

# 6. Owning Service

Only [Trademark Service](../../services/trademark-service.md) executes `TrademarkService.changeStatus` and produces performed results.

# 7. Transition Request Shape

Uses [Status Transition Contract](status-transition-contract.md). Required shared fields: contract_version, transition_request_reference_id, subject, current_status, requested_status, requested_action, actor_context, permission_context, policy_context, human_review_context, approval_context, source_context, and domain_guard_context. Official/procedural-sensitive transitions require source_reference_id, source_type, source_version_or_timestamp, jurisdiction_reference_id, normalization_evidence_reference_id, and source_validation_status=Valid. Conflicting source_validation_status returns ReviewRequired, performed=false, and no status-changed Event. ReviewRequired is not an invalid-transition bypass.

# 8. Transition Decision Shape

Uses shared status_transition_decision. Applicable decisions: Allowed, Denied, Blocked, ReviewRequired, ApprovalRequired, PermissionRequired, PolicyRequired, InvalidState, InvalidTransition, Unknown.

# 9. Transition Result Shape

Uses shared status_transition_result. Performed results require owner_service `Trademark Service`, operation `TrademarkService.changeStatus`, and event `TrademarkStatusChanged`.

# 10. Canonical Values

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

# 11. Allowed Transitions

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

# 12. Guard Requirements

Official/procedural-sensitive transitions require source_reference_id, source_type, source_version_or_timestamp, jurisdiction_reference_id, normalization_evidence_reference_id, and source_validation_status=Valid. Conflicting source_validation_status returns ReviewRequired, performed=false, and no status-changed Event. ReviewRequired is not an invalid-transition bypass.

# 13. Permission and Policy

Sensitive, terminal, cancellation, completion, archival, reopen, externally sourced, or protected transitions require explicit permission/policy evidence as applicable.

# 14. Human Review and Approval

Review and approval contexts must be explicit for guarded review exits, conflicting sources, and approval-sensitive transitions; AI cannot replace them.

# 15. Source and Evidence Requirements

Official/procedural-sensitive transitions require source_reference_id, source_type, source_version_or_timestamp, jurisdiction_reference_id, normalization_evidence_reference_id, and source_validation_status=Valid. Conflicting source_validation_status returns ReviewRequired, performed=false, and no status-changed Event. ReviewRequired is not an invalid-transition bypass.

# 16. Idempotency

Retryable operations require idempotency_key; replay must not duplicate mutation or Events.

# 17. Event and Audit Trace

Performed mutation requires `TrademarkStatusChanged` plus audit_reference_id; decision-only or failed results must not include status-changed Event proof.

# 18. API Consumption

[Trademark API Contract](../api/trademark-api-contract.md) must consume this contract and the shared transition contract without endpoint path changes.

# 19. AI Boundary

AI may explain or recommend review only; it cannot approve, mutate, file, send, pay, engage providers, record official action, or execute professional action.

# 20. Compatibility and Versioning

Status contract version can clarify shape and guards but cannot drift from canonical values or transition matrix.

# 21. Error Semantics

InvalidState for noncanonical status; InvalidTransition for unlisted edge; PermissionRequired, PolicyRequired, ReviewRequired, ApprovalRequired, Blocked, Denied, or Unknown for guard outcomes.

# 22. Fixture Requirements

Fixtures are in [status-workflow/status/trademark](../fixtures/status-workflow/status/trademark/) and must use full request/decision/result envelopes.

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
