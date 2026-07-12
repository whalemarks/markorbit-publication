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

Defines legal values, semantics, transitions and governance for `Order.status`.

# 2. Classification

This is a Controlled State Value Specification owned by the parent object. It is not an independent Core Object, aggregate root, repository, table, source of truth or UI list.

# 3. Parent Ownership

Order owns state truth. Order Service is the only mutation authority.

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

| Draft | Record is being prepared and is not ready for committed execution. | Internal Planning State | Yes | Active | Non-terminal | Yes | No | No | Enter when record is being prepared and is not ready for committed execution. | Exit only through an allowed transition with owning-Service validation. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

| PendingConfirmation | Order awaits customer or internal confirmation before commitment. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when order awaits customer or internal confirmation before commitment. | Exit only through an allowed transition with owning-Service validation. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

| Confirmed | Service request has been confirmed by an authorized actor after scope and commercial context validation; it does not mean paid. | Internal Planning State | No | Active | Non-terminal | Yes | No | Guarded | Enter when service request has been confirmed by an authorized actor after scope and commercial context validation; it does not mean paid. | Exit only through an allowed transition with owning-Service validation. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

| ReadyForMatter | Order is ready to create/link a Matter but the Matter reference may not yet exist. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when order is ready to create/link a matter but the matter reference may not yet exist. | Exit only through an allowed transition with owning-Service validation. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

| MatterCreated | Order has a valid Matter reference linking commercial request to execution container. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when order has a valid matter reference linking commercial request to execution container. | Exit only through an allowed transition with owning-Service validation. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

| InProgress | Work or fulfillment related to the parent is actively underway. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when work or fulfillment related to the parent is actively underway. | Exit only through an allowed transition with owning-Service validation. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

| WaitingForCustomer | Parent remains active but requires customer input or response. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when parent remains active but requires customer input or response. | Exit only through an allowed transition with owning-Service validation. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

| Completed | Parent-level work is complete according to its own completion criteria. | Inactive State | No | Inactive | Non-terminal | Guarded | No | Guarded | Enter when parent-level work is complete according to its own completion criteria. | Exit only through an allowed transition with owning-Service validation. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

| Cancelled | Cancellation outcome or governed cancellation has been recorded. | Inactive State | No | Inactive | Non-terminal | Guarded | No | Yes | Enter when cancellation outcome or governed cancellation has been recorded. | Exit only through an allowed transition with owning-Service validation. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

| Archived | Inactive archival state retained for history and ordinary reporting. | Archival / Reference-Only State | No | Inactive | Terminal | Guarded | No | Guarded | Enter when inactive archival state retained for history and ordinary reporting. | No ordinary exit; restoration is deferred governance. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

| DeletedReferenceOnly | Terminal tombstone/reference-only state with no normal business transition. | Archival / Reference-Only State | No | Inactive | Terminal | No | No | Yes | Enter when terminal tombstone/reference-only state with no normal business transition. | No ordinary business exit. | `OrderStatusChanged` with prior status, next status, actor, reason and audit context. |

# 7. State Categories

```text
Internal Planning State
Inactive State
Archival / Reference-Only State
```

# 8. Initial State Rules

`Draft` is the normal initial state unless governed import validation permits another existing-source state.

# 9. Terminal and Inactive State Rules

`Archived` is terminal archival for ordinary flow. `DeletedReferenceOnly` is terminal reference/tombstone state.

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

Unlisted transitions return `InvalidTransition` unless a stricter applicable Workflow Contract also validates the route. Validate current status, requested status, actor, permission, policy, guards, idempotency and event trace.

# 12. Owning Service Mutation Authority

Only Order Service mutates `Order.status` and must preserve previous status, next status, actor, reason, source and audit context.

# 13. Permission and Policy

Permission and Policy are mandatory for sensitive, terminal, reopening, cancellation, completion, archival or externally sourced transitions.

# 14. Human Review

Human Review is a transition guard or precondition and does not have to appear as an Order status. `PendingConfirmation -> Confirmed` may require Human Review when commercial information is incomplete, price or scope is anomalous, or policy requires review. `Confirmed -> Cancelled` and `ReadyForMatter -> Cancelled` must preserve actor, reason, permission and policy context. `InProgress -> Completed` and `MatterCreated -> Completed` require order-level completion validation. `Completed -> Archived` and `Cancelled -> Archived` are governance operations. AI must not confirm, cancel, complete or archive Orders autonomously.

# 15. Event Requirements

Each mutation produces or requires `OrderStatusChanged` with previous/next status and reason semantics.

# 16. API and Contract Consumption

API requests cannot define states or bypass transition validation. Contracts consume this spec and may constrain but not expand state truth.

# 17. AI Boundary

AI may explain, summarize or recommend for review only; AI cannot create values, mutate status, approve, cancel, complete, archive or execute protected action.

# 18. Product Consumption

Product UI consumes these values and may render labels; UI text is not canonical state definition.

# 19. Source and Official-Status Boundary

`Confirmed` does not mean payment completed. `MatterCreated` requires a Matter reference. `Completed` means order-layer service request completion, not legal-right success.

# 20. Compatibility and Versioning

Legacy Object ID is historical/reclassified metadata only and must not be used as a new Spec ID.

# 21. Failure and Reason Semantics

Failures include InvalidState, InvalidTransition, PermissionRequired, PolicyRequired, ReviewRequired, ApprovalRequired and Blocked. Reasons must be auditable.

# 22. Valid Examples

Valid: `Draft -> PendingConfirmation` through Order Service with event trace.

# 23. Invalid Examples

Invalid: Product UI directly changes `Order.status` or invents a new state.

# 24. MVP Scope

Must implement specification semantics, validation references and event trace.

# 25. Deferred Scope

Runtime fixtures, typed implementation mapping and negative tests beyond this validator are future gates.

# 26. Prohibited Overreach

No independent Core Object, source of truth, database enum, ORM model, workflow engine or endpoint path change is created here.

# 27. Acceptance Criteria

Canonical value list is exact; transition matrix is exact; owning Service and Event trace are preserved; semantics are meaningful and not boilerplate.

# 28. Revision Notes

0.1.0 Draft for PUB-TASK-B02-002; strengthened by PUB-TASK-B02-002-FIX-01.
