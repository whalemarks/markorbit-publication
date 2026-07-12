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

It has no independent global identity.
It is not a Workflow instance.
It does not own the target object's business state.

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
- Do not use an independent Core Object ID.
- An active Workflow Contract has at least one initial state.
- Unless multi-entry is explicitly supported, exactly one initial state is allowed.
- Terminal states do not have ordinary outgoing transitions.
- Product UI label is never canonical `state_key`.
- Meaning is stable and not decided by UI copy.
- State components do not mutate, call Services, or authorize external action.

# State Categories

```text
Initial
Active
Waiting
Review
Approval
Blocked
Completed
Cancelled
Terminal
Archived
CustomGoverned
```

These are component categories, not mandatory fixed state values for every Workflow.

# Ownership and Boundaries

Workflow Contract owns definitions. Workflow Contract Service validates structure. Owning domain Services perform target mutation. Events trace outcomes. AI and Product consume but do not define or mutate.

# Prohibited Overreach

No independent aggregate, source of truth, Product UI definition authority, Service mutation, external protected action authorization or runtime engine is created by this component.
