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

Workflow Transition Definition is an embedded, versioned rule inside a Workflow Contract that defines whether and how movement from one Workflow State to another may be validated. It validates and routes. It does not perform domain mutation itself.

# Parent Contract

Workflow Transition Definition exists only inside a specific Workflow Contract version. Its `transition_key` is unique only within that Workflow Contract/version.

# Component Classification

This is a Workflow Contract Component Specification. It is not a Core Object, Workflow instance, Task, Event, Service, Product UI rule or protected external action authorization.

# Scope

In scope: transition key, source/target state keys, trigger type, requested action, owning Service reference/operation, guards, permissions, policies, capabilities, responsibility, review, approval, document/evidence/event/notification requirements, idempotency, audit, external-action boundary, failure behavior and metadata.

# Boundary

Transition definition validates possible movement; it does not perform mutation, own target state, create Task directly, emit Event directly, send Communication, submit filing, execute payment, engage provider, record official action or authorize protected external action.

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

# Validation Rules

## Canonical Transition Decision Vocabulary

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

## Validation Order

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

# Ownership

Workflow Contract owns transition definitions. Workflow Contract Service validates and returns decisions. Owning domain Services perform target mutation.

# Service Usage

Workflow Contract Service defines structure, validates transition requests, returns a decision and references the owning Service operation. It must not directly mutate Trademark, Order, Matter or Task.

# Event Usage

Transition definitions may require requested, allowed/denied, performed and failed event references. Actual Events are produced by the appropriate owning Service or approved orchestration, not by the component itself.

# Permission and Policy

`PermissionRequired` means permission is missing or insufficient. `PolicyRequired` means a policy requirement blocks or conditions transition. Neither result grants access.

# Human Review and Approval

`ReviewRequired` and `ApprovalRequired` are distinct. Completing review or approval satisfies a requirement only; it does not automatically execute mutation.

# AI Boundary

AI may explain transition requirements or recommend review. AI must not create transition definitions, decide protected approvals, mutate target state or bypass guards.

# Product Consumption

Product may render available actions from validated transition definitions. Product UI cannot define canonical transitions or bypass validation.

# Compatibility

| Legacy term | Canonical term |
| --- | --- |
| Rejected | Denied |
| BlockedByPermission | PermissionRequired |
| BlockedByPolicy | PolicyRequired |
| BlockedByGuard | Blocked |

Legacy terms are historical compatibility references only and are not active canonical decision values.

# Versioning

Transition keys are unique within a contract version. Contract version changes may alter transition availability. Existing instances must use their bound or compatible contract version. A new version must not silently change running-instance legal paths.

# Failure Behavior

`Denied`, `Blocked`, `ReviewRequired`, `ApprovalRequired`, `PermissionRequired`, `PolicyRequired`, `InvalidState`, `InvalidTransition` and `Unknown` are non-Allowed outcomes. Undefined transition returns `InvalidTransition`; missing/mismatched current state returns `InvalidState`; unauthorized protected external action must not return `Allowed`.

# Examples

Allowed: `draft_to_open` validates actor, permission, policy and current state, then routes mutation to the owning Service.

ReviewRequired: `prepare_to_file` requires Human Review before a filing-sensitive mutation can be requested.

InvalidTransition: request from `archived` to `draft` has no transition definition.

Protected external action denial: a transition requesting filing submission without authorization returns a non-Allowed decision and does not submit.

# Prohibited Overreach

Workflow Transition Definition must not directly create tasks, emit events, mutate domain objects, execute external protected actions, bypass Human Review or become a product-defined state machine.

# Acceptance Criteria

A valid transition definition uses canonical decision vocabulary, exact source/target state keys, required guard references, route-only Service behavior, version governance and default-deny failure semantics.

# Revision Notes

0.1.0 Draft for PUB-TASK-B02-002; completed component governance structure in PUB-TASK-B02-002-FIX-02.
