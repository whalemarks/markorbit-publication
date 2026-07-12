# Workflow Contract Component Specification — Workflow State Definition

Spec ID: B02-WFC-STATE-DEFINITION
Spec Type: Workflow Contract Component Specification
Component Name: Workflow State Definition
Parent Contract: Workflow Contract
Owning Domain/System: Workflow Contract
Legacy Object ID: OBJ-WFC-002 — Reclassified
Status: Draft
Version: 0.1.0
MVP Phase: Phase 3
MVP Depth: Must Implement
Owner: MarkOrbit Publications Editorial Board

# Purpose

Defines the embedded state-node component used inside a Workflow Contract version.

# Canonical Meaning

Workflow State Definition is an embedded, versioned component inside a Workflow Contract that defines one allowed state node.

It has no independent global identity. It is not a Workflow instance. It does not own the target object's business state.

# Parent Contract

Workflow State Definition exists only inside a specific Workflow Contract version. Its `state_key` is unique only within that Workflow Contract/version and must not be treated as a global Core Object identifier.

# Component Classification

This is a Workflow Contract Component Specification. It is not a Core Object, Workflow instance, Task, Event, Service, Product UI definition or external authorization artifact.

# Scope

In scope: state key, display name, meaning, category, initial/terminal behavior, active flag, entry/exit requirements, allowed actor types, permission/policy/review/approval references, document/evidence/event requirements, external-action boundary and metadata.

# Boundary

Out of scope: domain object current state, workflow instance state storage, UI column definition, Task status, Matter status, external action authority and Service execution.

# Required Fields

```text
state_key
display_name
meaning
state_category
is_initial
is_terminal
is_active
entry_requirements
exit_requirements
allowed_actor_types
required_permission_references
required_policy_references
required_review_references
required_approval_references
required_document_references
required_evidence_references
required_event_references
external_action_boundary
metadata
```

# Validation Rules

- `state_key` is unique only inside one Workflow Contract/version.
- An active Workflow Contract has at least one initial state.
- Unless multi-entry is explicitly supported, exactly one initial state is allowed.
- Terminal states do not have ordinary outgoing transitions.
- Product UI label is never canonical `state_key`.
- Meaning is stable and not decided by UI copy.
- State components do not mutate, call Services or authorize external action.

# Ownership

Workflow Contract owns the component definition. Workflow Contract Service validates structure. Owning domain Services own target object mutation.

# Service Usage

Workflow Contract Service validates component structure, validates key uniqueness, validates initial/terminal rules and does not mutate target domain objects.

# Event Usage

A state definition may require Event references for entry, exit or audit expectations, but the component does not emit Events itself.

# Permission and Policy

A state may declare required permission and policy references. The state definition does not grant permissions or evaluate policies.

# Human Review and Approval

A state may declare required review or approval references. The state definition does not complete reviews, grant approvals or perform mutation after review.

# AI Boundary

AI may explain state meaning or highlight missing references. AI must not create, rename, activate, deprecate or silently modify state definitions.

# Product Consumption

Product may display labels derived from state definitions. Product label changes must not alter canonical `state_key` or state meaning.

# Compatibility

Renaming a state display label is compatible when `state_key` and meaning remain stable. Changing `state_key`, meaning, terminal behavior or entry/exit requirements requires version governance.

# Versioning

State definitions are version-bound to their Workflow Contract. Deprecated state keys must remain resolvable for existing compatible contract versions. New versions must not silently change active instance paths.

# Failure Behavior

```text
InvalidStateDefinition
DuplicateStateKey
MissingInitialState
MultipleInitialStates
InvalidTerminalState
MissingRequiredReference
UnsupportedVersion
```

These are component validation failures, not new Core Object statuses.

# Examples

Valid: `state_key=review_required`, category `Review`, not terminal, with required review reference and event requirement.

Invalid: two states with the same `state_key`, or a terminal state with ordinary outgoing transitions.

# Prohibited Overreach

No independent aggregate, source of truth, Product UI definition authority, Service mutation, external protected action authorization or runtime engine is created by this component.

# Acceptance Criteria

A valid Workflow State Definition has stable key semantics, required references, initial/terminal consistency, version compatibility and no mutation authority.

# Revision Notes

0.1.0 Draft for PUB-TASK-B02-002; completed component governance structure in PUB-TASK-B02-002-FIX-02.
