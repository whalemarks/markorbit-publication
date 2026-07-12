# Workflow Transition Definition Contract

Spec ID: B02-CONTRACT-WORKFLOW-TRANSITION-DEFINITION
Spec Type: Contract Specification
Contract Version: v0.1.0
Related Component Specification: ../../../workflows/components/workflow-transition-definition.md

# Definition Shape
```yaml
workflow_transition_definition:
  transition_key: required
  from_state_key: required
  to_state_key: required
  trigger_type: required
  requested_action: required
  owning_service_reference: required
  owning_service_operation: required
  guard_references: required
  permission_references: required
  policy_references: required
  capability_references: required
  responsibility_references: required
  review_requirement: required
  approval_requirement: required
  document_requirements: required
  evidence_requirements: required
  event_requirements: required
  notification_requirements: required
  idempotency_requirement: required
  audit_requirement: required
  external_action_boundary: required
  failure_behavior: required
  metadata: required
workflow_transition_validation_request:
  workflow_contract_reference_id: string
  workflow_contract_version: string
  transition_key: string | null
  current_state_key: string
  requested_state_key: string
  target_object_type: string
  target_object_reference_id: string
  actor_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
  human_review_reference_id: string | null
  approval_reference_id: string | null
  idempotency_key: string | null
  correlation_id: string | null
workflow_transition_validation_result:
  decision: Allowed | Denied | Blocked | ReviewRequired | ApprovalRequired | PermissionRequired | PolicyRequired | InvalidState | InvalidTransition | Unknown
  mutation_performed: false
  owning_service_reference: string | null
  owning_service_operation: string | null
  required_next_action: string | null
  reason_code: string
  missing_requirements:
    - string
```

Workflow Contract validates and routes. Owning Service mutates. Workflow validation result always has `mutation_performed: false`. Protected external action defaults denied.
