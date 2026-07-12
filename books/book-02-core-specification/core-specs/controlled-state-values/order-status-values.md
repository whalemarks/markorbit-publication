# Controlled State Value Specification — Order Status Values



Spec ID: B02-CSV-ORDER-STATUS

Spec Type: Controlled State Value Specification

Parent Object: Order

Owning Domain: Order

Owning Service: Order Service

Parent Field: Order.status

Legacy Object ID: OBJ-ORD-004 — Reclassified

Status: Draft

Version: 0.1.0

MVP Phase: Phase 3

MVP Depth: Must Implement

Owner: MarkOrbit Publications Editorial Board



# 1. Purpose

Defines legal values, semantics, transitions and governance for `Order.status`. The parent object owns state truth; Order Service is the only mutation authority.

# 2. Classification

This is not an independent Core Object, aggregate root, repository, table, source of truth or UI status list.

# 3. Parent Ownership

Order owns the state field. The owning Service validates current status, requested status and transition before mutation.

# 4. Parent Field

`Order.status` consumes these exact values.

# 5. Canonical Values

```text

Draft

PendingConfirmation

Confirmed

ReadyForMatter

MatterCreated

InProgress

WaitingForCustomer

Completed

Cancelled

Archived

DeletedReferenceOnly

```

# 6. Value Semantics

| Canonical value | Core meaning | State category | Initial allowed | Active / inactive | Terminal behavior | Reopenable | Official-source-sensitive | Human-review-sensitive | Typical entry condition | Typical exit condition | Event expectation |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Draft | Canonical Order lifecycle state `Draft`. | Internal Planning State | Yes | Active | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

| PendingConfirmation | Canonical Order lifecycle state `PendingConfirmation`. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

| Confirmed | Canonical Order lifecycle state `Confirmed`. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

| ReadyForMatter | Canonical Order lifecycle state `ReadyForMatter`. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

| MatterCreated | Canonical Order lifecycle state `MatterCreated`. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

| InProgress | Canonical Order lifecycle state `InProgress`. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

| WaitingForCustomer | Canonical Order lifecycle state `WaitingForCustomer`. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

| Completed | Canonical Order lifecycle state `Completed`. | Inactive State | No | Inactive | Non-terminal | Guarded | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

| Cancelled | Canonical Order lifecycle state `Cancelled`. | Inactive State | No | Inactive | Non-terminal | Guarded | No | Yes | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

| Archived | Canonical Order lifecycle state `Archived`. | Archival / Reference-Only State | No | Inactive | Terminal | Guarded | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

| DeletedReferenceOnly | Canonical Order lifecycle state `DeletedReferenceOnly`. | Archival / Reference-Only State | No | Inactive | Terminal | No | No | Yes | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `OrderStatusChanged` with previous and next status. |

# 7. State Categories

Internal Planning State; Official / Procedural Normalized State; Maintenance State; Governance State; Inactive State; Archival / Reference-Only State.

# 8. Initial State Rules

`Draft` is the default initial state unless a governed import contract explicitly validates another initial state.

# 9. Terminal and Inactive State Rules

`Archived` is terminal archival. `DeletedReferenceOnly` is terminal reference/tombstone and does not allow normal business transitions.

# 10. Transition Model

```text

Draft -> PendingConfirmation

Draft -> Cancelled

Draft -> Archived

PendingConfirmation -> Draft

PendingConfirmation -> Confirmed

PendingConfirmation -> Cancelled

Confirmed -> ReadyForMatter

Confirmed -> InProgress

Confirmed -> Cancelled

ReadyForMatter -> MatterCreated

ReadyForMatter -> InProgress

ReadyForMatter -> Cancelled

MatterCreated -> InProgress

MatterCreated -> Completed

MatterCreated -> Cancelled

InProgress -> WaitingForCustomer

InProgress -> Completed

InProgress -> Cancelled

WaitingForCustomer -> InProgress

WaitingForCustomer -> Cancelled

Completed -> Archived

Cancelled -> Archived

```

# 11. Transition Validation

Default deny: unlisted transitions return `InvalidTransition` unless an applicable Workflow Contract defines a stricter allowed route. Validate current status, requested status, actor, permission, policy, guards, idempotency and event trace.

# 12. Owning Service Mutation Authority

Only Order Service mutates `Order.status` and must preserve previous status, next status, actor, reason, source and audit context.

# 13. Permission and Policy

Permission and Policy are mandatory for sensitive, terminal, reopening or externally sourced transitions.

# 14. Human Review

Leaving `ReviewRequired` requires Human Review outcome. Sensitive professional decisions require Human Review and may not be automated.

# 15. Event Requirements

Each mutation produces or requires `OrderStatusChanged` with previous/next state and reason semantics.

# 16. API and Contract Consumption

API requests cannot define states or bypass transition validation. Contracts consume this spec and may constrain but not expand status truth.

# 17. AI Boundary

AI may explain, summarize or recommend for review only; AI cannot create values, mutate status or approve protected actions.

# 18. Product Consumption

Product UI consumes these values and labels only; UI text is not canonical state definition.

# 19. Source and Official-Status Boundary

External or operational signals must be validated before status mutation and do not become state truth by themselves.

# 20. Compatibility and Versioning

Legacy Object ID is historical only and must not be used as a new Spec ID.

# 21. Failure and Reason Semantics

Failures include InvalidState, InvalidTransition, PermissionRequired, PolicyRequired, ReviewRequired, ApprovalRequired and Blocked. Reasons must be auditable.

# 22. Valid Examples

Valid: `Draft -> PendingConfirmation` through Order Service with event trace.

# 23. Invalid Examples

Invalid: Product UI directly changes `Order.status` or invents a new state.

# 24. MVP Scope

Must implement specification semantics, validation references and event trace.

# 25. Deferred Scope

Runtime fixtures, typed implementation mapping and negative tests are future gates.

# 26. Prohibited Overreach

No independent Core Object, source of truth, database enum, ORM model, runtime workflow engine or endpoint path change is created here.

# 27. Acceptance Criteria

Canonical value list is exact; transitions are default-deny; owning Service and Event trace are preserved.

# 28. Revision Notes

0.1.0 Draft for PUB-TASK-B02-002.
