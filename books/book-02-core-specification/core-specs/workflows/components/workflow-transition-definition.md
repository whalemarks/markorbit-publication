# Workflow Contract Component Specification — Workflow Transition Definition

Spec ID: B02-WFC-TRANSITION-DEFINITION
Spec Type: Workflow Contract Component Specification
Component Name: Workflow Transition Definition
Parent Contract: Workflow Contract
Owning Domain/System: Workflow Contract
Legacy Object ID: OBJ-WFC-003 — Reclassified
Status: Draft
Version: 0.1.0
MVP Phase: Phase 3
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# Purpose

Defines the embedded transition-rule component used inside a Workflow Contract version.

# Canonical Meaning

Workflow Transition Definition is an embedded, versioned rule inside a Workflow Contract that defines whether and how movement from one Workflow State to another may be validated.

It validates and routes.
It does not perform domain mutation itself.

# Required Fields

```text
transition_key
from_state_key
to_state_key
trigger_type
requested_action
owning_service_reference
owning_service_operation
guard_references
permission_references
policy_references
capability_references
responsibility_references
review_requirement
approval_requirement
document_requirements
evidence_requirements
event_requirements
notification_requirements
idempotency_requirement
audit_requirement
external_action_boundary
failure_behavior
metadata
```

# Canonical Transition Decision Vocabulary

```text
Allowed
Denied
Blocked
ReviewRequired
ApprovalRequired
PermissionRequired
PolicyRequired
InvalidState
InvalidTransition
Unknown
```

# Compatibility Notes

| Legacy term | Canonical term |
| --- | --- |
| Rejected | Denied |
| BlockedByPermission | PermissionRequired |
| BlockedByPolicy | PolicyRequired |
| BlockedByGuard | Blocked |

Legacy terms are historical compatibility references only and are not active canonical decision values.

# Validation Order

1. Resolve Workflow Contract and version.
2. Confirm contract is active and applicable.
3. Confirm current state exists.
4. Confirm requested state exists.
5. Confirm transition definition exists.
6. Confirm target object reference and current state.
7. Check idempotency.
8. Check actor and responsibility.
9. Check permission.
10. Check policy.
11. Check capability.
12. Check document/evidence/data guards.
13. Check Human Review requirement.
14. Check approval requirement.
15. Check external-action boundary.
16. Return transition decision.
17. Route allowed mutation to owning Service.
18. Record required Event and audit context.

# Service Boundary

Workflow Contract Service defines structure, validates transitions, returns decisions and references owning Service action. It must not directly modify Trademark, Order, Matter or Task; create tasks except through Task Service; send Communication; submit filing; execute payment; engage provider; execute official recordal; or bypass Human Review.

# Default Deny

Missing state returns `InvalidState`. Undefined transition returns `InvalidTransition`. Incompatible version, permission failure, policy failure, incomplete review or approval, guard failure, target state mismatch, idempotency conflict and unauthorized external protected action must return a non-Allowed decision.
