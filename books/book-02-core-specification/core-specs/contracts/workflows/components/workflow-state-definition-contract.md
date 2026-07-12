# Workflow State Definition Contract

Spec ID: B02-CONTRACT-WORKFLOW-STATE-DEFINITION
Spec Type: Contract Specification
Contract Version: v0.1.0
Related Component Specification: ../../../workflows/components/workflow-state-definition.md

# Shape
```yaml
workflow_state_definition:
  state_key: required
  display_name: required
  meaning: required
  state_category: required
  is_initial: required
  is_terminal: required
  is_active: required
  entry_requirements: required
  exit_requirements: required
  allowed_actor_types: required
  required_permission_references: required
  required_policy_references: required
  required_review_references: required
  required_approval_references: required
  required_document_references: required
  required_evidence_references: required
  required_event_references: required
  external_action_boundary: required
  metadata: required
workflow_state_definition_set:
  workflow_contract_reference_id: string
  workflow_contract_version: string
  states:
    - workflow_state_definition
```

# Validation
state_key unique inside contract version; at least one initial state; terminal state has no ordinary outgoing transition; display label is not canonical key; component has no independent global identity; external action boundary is not authorization.
