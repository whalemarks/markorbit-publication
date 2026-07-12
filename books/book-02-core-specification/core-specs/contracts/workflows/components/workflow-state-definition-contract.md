# Workflow State Definition Contract

Spec ID: B02-CONTRACT-WORKFLOW-STATE-DEFINITION
Spec Type: Contract Specification
Contract Name: Workflow State Definition Contract
Contract File: core-specs/contracts/workflows/components/workflow-state-definition-contract.md
Contract Category: Workflow Component
Related Component Specification: [Workflow State Definition](../../../workflows/components/workflow-state-definition.md)
Related Workflow Contract Object: [Workflow Contract](../../../objects/workflow-contract.md)
Related Workflow Contract Service: [Workflow Contract Service](../../../services/workflow-contract-service.md)
Related Workflow Contract API: [Workflow Contract API Contract](../../api/workflow-contract-api-contract.md)
Related Common Contracts: [References](../../common/references.md), [Permission Context](../../common/permission-context.md), [Policy Context](../../common/policy-context.md), [Human Review](../../common/human-review.md), [Audit Context](../../common/audit-context.md), [Versioning](../../common/versioning.md), [Errors](../../common/errors.md)
Status: Draft
Version: 0.1.0
Contract Version: v0.1.0
MVP Phase: Phase 3
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# 1. Purpose

Defines the enforceable shape for Workflow State Definition Contract.

# 2. Contract Meaning

This is an embedded Workflow Contract component and has no independent global identity.

# 3. Contract Boundary

It validates structure and routing only; it is not a Workflow instance, Task, domain mutation service, or external action authorization.

# 4. Related Component Specification

Consumes [Workflow State Definition](../../../workflows/components/workflow-state-definition.md).

# 5. Parent Workflow Contract

Exists only inside a versioned [Workflow Contract](../../../objects/workflow-contract.md).

# 6. Required References

Uses Workflow Contract, Workflow Contract Service, API Contract, common reference, permission, policy, human review, audit, versioning, and errors contracts.

# 7. Contract Shape

```yaml
workflow_state_definition:
  state_key: string
  display_name: string
  meaning: string
  state_category: string
  is_initial: boolean
  is_terminal: boolean
  is_active: boolean
  entry_requirements:
    - string
  exit_requirements:
    - string
  allowed_actor_types:
    - string
  required_permission_references:
    - string
  required_policy_references:
    - string
  required_review_references:
    - string
  required_approval_references:
    - string
  required_document_references:
    - string
  required_evidence_references:
    - string
  required_event_references:
    - string
  external_action_boundary: string
  metadata: object | null
workflow_state_definition_set:
  workflow_contract_reference_id: string
  workflow_contract_version: string
  states:
    - workflow_state_definition
```

# 8. Field Types

Field types are the literal YAML types shown in the contract shape; `mutation_performed: false` is a fixed literal where present.

# 9. Field Rules

state_key must be non-empty and unique in the set; display_name cannot replace state_key; external_action_boundary must be non-empty; terminal states cannot have ordinary outgoing transitions.

# 10. Collection Rules

State keys and transition keys are unique within one workflow contract version; default contracts have exactly one initial state.

# 11. Validation Rules

state_key must be non-empty and unique in the set; display_name cannot replace state_key; external_action_boundary must be non-empty; terminal states cannot have ordinary outgoing transitions.

# 12. Permission and Policy

References declare required decisions but do not grant permissions or evaluate policies.

# 13. Human Review and Approval

References declare review/approval requirements but do not complete review or approval.

# 14. Event and Audit Rules

Components may require event/audit references; they do not emit events or audit by themselves.

# 15. External Action Boundary

External action boundary text is descriptive and never authorization.

# 16. AI Boundary

AI may explain missing references only and cannot mutate definitions or authorize actions.

# 17. Compatibility and Versioning

Changing canonical keys or behavior requires version governance.

# 18. Failure Semantics

Failures use InvalidState, InvalidTransition, PermissionRequired, PolicyRequired, ReviewRequired, ApprovalRequired, Blocked, Denied, Unknown, or UnsupportedVersion semantics as applicable.

# 19. Fixture Requirements

Fixtures in ../fixtures/status-workflow/workflow/ must use full structured input and expected result shapes.

# 20. Valid Examples

A state set with one initial state and no terminal outgoing transition; a transition validation result with mutation_performed=false.

# 21. Invalid Examples

Duplicate state key, missing initial state, terminal outgoing transition, missing target reference, or protected action Allowed.

# 22. Prohibited Overreach

No runtime engine, target object mutation, external protected action, or independent Core Object is created.

# 23. Acceptance Criteria

Required fields, types, validation rules, fixtures, and validator checks all pass.

# 24. Revision Notes

0.1.0 Draft; completed by PUB-TASK-B02-003-FIX-01.
