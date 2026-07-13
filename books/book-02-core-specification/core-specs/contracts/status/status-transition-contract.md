# Status Transition Contract

Spec ID: B02-CONTRACT-STATUS-TRANSITION
Spec Type: Contract Specification
Contract Name: Status Transition Contract
Contract File: core-specs/contracts/status/status-transition-contract.md
Contract Category: Status
Related Owning Specs: [Trademark Status Values](../../controlled-state-values/trademark-status-values.md), [Order Status Values](../../controlled-state-values/order-status-values.md), [Matter Status Values](../../controlled-state-values/matter-status-values.md), [Task Status Values](../../controlled-state-values/task-status-values.md)
Related Controlled State Value Specifications: B02-CSV-TRADEMARK-STATUS; B02-CSV-ORDER-STATUS; B02-CSV-MATTER-STATUS; B02-CSV-TASK-STATUS
Related Parent Objects: [Trademark](../../objects/trademark.md); [Order](../../objects/order.md); [Matter](../../objects/matter.md); [Task](../../objects/task.md)
Related Owning Services: [Trademark Service](../../services/trademark-service.md); [Order Service](../../services/order-service.md); [Matter Service](../../services/matter-service.md); [Task Service](../../services/task-service.md)
Related API Contracts: [Trademark API Contract](../api/trademark-api-contract.md); [Order API Contract](../api/order-api-contract.md); [Matter API Contract](../api/matter-api-contract.md); [Task API Contract](../api/task-api-contract.md)
Related Common Contracts: [references](../common/references.md); [audit-context](../common/audit-context.md); [permission-context](../common/permission-context.md); [policy-context](../common/policy-context.md); [human-review](../common/human-review.md); [idempotency](../common/idempotency.md); [versioning](../common/versioning.md); [errors](../common/errors.md)
Related Event Specs: TrademarkStatusChanged; OrderStatusChanged; MatterStatusChanged; TaskStatusChanged
Status: Draft
Version: 0.1.0
Contract Version: v0.1.0
MVP Phase: Phase 2
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# 1. Purpose

Defines the shared transition request, decision, and owner-Service result contract for controlled status values.

# 2. Contract Meaning

The contract shape separates request, decision, and owner-Service result so validation can route without mutating parent objects.

# 3. Contract Boundary

This contract does not own parent state, create status values, define domain guards, or authorize external action.

# 4. Related Owning Specifications

It consumes the four Controlled State Value Specifications listed in metadata.

# 5. Supported Subject Types

Supported subject types are Trademark, Order, Matter, and Task only.

# 6. Required References

References must comply with common Reference, Audit, Permission, Policy, Human Review, Idempotency, Versioning, and Error contracts.

# 7. Transition Request Shape

```yaml
status_transition_request:
  contract_version: string
  transition_request_reference_id: string
  correlation_id: string | null
  idempotency_key: string | null
  subject:
    object_type: Trademark | Order | Matter | Task
    object_reference_id: string
    owner_service: string
  current_status: string
  requested_status: string
  requested_action: string
  reason_code: string | null
  actor_context:
    actor_reference_id: string | null
    organization_reference_id: string | null
    agent_reference_id: string | null
    agent_contract_reference_id: string | null
  permission_context:
    permission_decision_reference_id: string | null
    permission_status: Allowed | Denied | Unknown | null
  policy_context:
    policy_decision_reference_id: string | null
    policy_status: Allowed | Restricted | ReviewRequired | Unknown | null
  human_review_context:
    human_review_reference_id: string | null
    review_status: Approved | Rejected | Pending | Missing | NotRequired | null
  approval_context:
    approval_reference_id: string | null
    approval_status: Approved | Rejected | Pending | Missing | NotRequired | null
  source_context:
    source_reference_id: string | null
    source_type: string | null
    source_version_or_timestamp: string | null
    jurisdiction_reference_id: string | null
    normalization_evidence_reference_id: string | null
    source_validation_status: Valid | Invalid | Conflicting | Unverified | NotRequired | null
  domain_guard_context:
    assignee_reference_id: string | null
    completion_context_reference_id: string | null
    matter_reference_id: string | null
    blocker_resolution_reference_id: string | null
    domain_context: object | null
```

# 8. Transition Request Field Rules

Current status must match the parent object; requested status must be canonical for the subject; domain_guard_context only passes guard evidence and arbitrary metadata cannot replace explicit guard fields.

# 9. Transition Decision Shape

```yaml
status_transition_decision:
  transition_request_reference_id: string
  decision: Allowed | Denied | Blocked | ReviewRequired | ApprovalRequired | PermissionRequired | PolicyRequired | InvalidState | InvalidTransition | Unknown
  mutation_authorized_for_owner_service: boolean
  current_status: string
  requested_status: string
  required_next_action: string | null
  reason_code: string
  missing_requirements:
    - string
  decision_reference_id: string | null
  evaluated_at: datetime
```

# 10. Canonical Decision Vocabulary

Canonical decision vocabulary in order: Allowed, Denied, Blocked, ReviewRequired, ApprovalRequired, PermissionRequired, PolicyRequired, InvalidState, InvalidTransition, Unknown. No other decision values are valid.

# 11. Transition Decision Rules

Allowed routes to the owning Service only. Invalid values fail InvalidState; unlisted edges fail InvalidTransition; missing guard evidence fails with the applicable requirement decision.

# 12. Transition Result Shape

```yaml
status_transition_result:
  transition_request_reference_id: string
  decision_reference_id: string | null
  performed: boolean
  owner_service: string
  owner_service_operation: string
  object_type: string
  object_reference_id: string
  previous_status: string
  next_status: string
  status_changed: boolean
  event_type: string | null
  event_reference_id: string | null
  audit_reference_id: string | null
  correlation_id: string | null
  idempotency_key: string | null
  performed_at: datetime | null
  failure_reason_code: string | null
```

# 13. Transition Result Rules

If performed=false then status_changed=false, event_type=null, event_reference_id=null, and performed_at=null. If performed=true then the decision was Allowed, mutation_authorized_for_owner_service=true, status_changed=true, previous/next are canonical, event and audit references exist, and performed_at exists.

# 14. Owning Service Mutation Boundary

Only the owning Service named by the subject may perform mutation and produce a performed result.

# 15. Permission and Policy

Permission and policy contexts are evidence for validation; they do not mutate status.

# 16. Human Review and Approval

Human review and approval contexts are required for guarded exits and cannot be replaced by AI output.

# 17. Source and Evidence

Official/procedural source-sensitive transitions require source reference, source type, timestamp/version, jurisdiction, normalization evidence, and source_validation_status.

# 18. Idempotency

Idempotent replay may return the original result but must not create a second mutation or second Event.

# 19. Event and Audit Trace

Performed mutations require the correct status-changed Event and audit trace.

# 20. AI Boundary

AI may explain and recommend review only; AI cannot approve or mutate.

# 21. Compatibility and Versioning

Version changes must preserve canonical state truth unless a governed specification version changes first.

# 22. Error Semantics

Error semantics use the canonical decision vocabulary and common errors contract.

# 23. Fixture Requirements

Fixtures must use the full request/decision/result envelope and distinguish decision-only from performed-result cases.

# 24. Valid Examples

Valid example: an Allowed request routed to owner Service, followed by a separate performed result with Event and audit proof.

# 25. Invalid Examples

Invalid example: decision-only fixture expecting a status-changed Event, or Workflow Contract mutating a parent object.

# 26. Prohibited Overreach

No runtime engine, database enum, endpoint path, production seed data, or protected external action authorization is created.

# 27. Acceptance Criteria

All sections, exact shapes, decision vocabulary, fixture semantics, and validator checks pass.

# 28. Revision Notes

0.1.0 Draft; completed by PUB-TASK-B02-003-FIX-01.
