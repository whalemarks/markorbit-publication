# Status Transition Contract

Spec ID: B02-CONTRACT-STATUS-TRANSITION
Spec Type: Contract Specification
Contract Name: Status Transition Contract
Contract File: status-transition-contract.md
Contract Category: Status
Status: Draft
Version: 0.1.0
Contract Version: v0.1.0
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# 1. Purpose
Defines the shared status transition request, validation decision, and owner-Service result envelope.

# 2. Transition Request Shape
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
```

# 3. Transition Decision Shape
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

# 4. Transition Result Shape
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

# 5. Rules
`Allowed` does not equal `performed=true`; performed mutation can only be produced by the owning Service. Successful mutation requires a status-changed Event trace and idempotent replay must not duplicate mutation or Event. AI cannot approve transitions.
