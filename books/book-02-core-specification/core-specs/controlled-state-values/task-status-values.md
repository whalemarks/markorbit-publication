# Controlled State Value Specification — Task Status Values



Spec ID: B02-CSV-TASK-STATUS

Spec Type: Controlled State Value Specification

Parent Object: Task

Owning Domain: Task

Owning Service: Task Service

Parent Field: Task.status

Legacy Object ID: OBJ-TSK-003 — Reclassified

Status: Draft

Version: 0.1.0

MVP Phase: Phase 3

MVP Depth: Must Implement

Owner: MarkOrbit Publications Editorial Board



# 1. Purpose

Defines legal values, semantics, transitions and governance for `Task.status`.

# 2. Classification

This is a Controlled State Value Specification owned by the parent object. It is not an independent Core Object, aggregate root, repository, table, source of truth or UI list.

# 3. Parent Ownership

Task owns state truth. Task Service is the only mutation authority.

# 4. Parent Field

`Task.status` consumes these exact values.

# 5. Canonical Values

```text

Draft

Open

Assigned

InProgress

Waiting

Blocked

ReviewRequired

Completed

Cancelled

Archived

DeletedReferenceOnly

```

# 6. Value Semantics

| Canonical value | Core meaning | State category | Initial allowed | Active / inactive | Terminal behavior | Reopenable | Official-source-sensitive | Human-review-sensitive | Typical entry condition | Typical exit condition | Event expectation |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Draft | Record is being prepared and is not ready for committed execution. | Internal Planning State | Yes | Active | Non-terminal | Yes | No | No | Enter when record is being prepared and is not ready for committed execution. | Exit only through an allowed transition with owning-Service validation. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

| Open | Parent is active and available for work but may not yet be actively performed. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when parent is active and available for work but may not yet be actively performed. | Exit only through an allowed transition with owning-Service validation. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

| Assigned | Task has valid assignee and responsibility context, but active performance may not have started. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when task has valid assignee and responsibility context, but active performance may not have started. | Exit only through an allowed transition with owning-Service validation. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

| InProgress | Work or fulfillment related to the parent is actively underway. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when work or fulfillment related to the parent is actively underway. | Exit only through an allowed transition with owning-Service validation. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

| Waiting | Task remains active but is waiting on input, dependency or timing. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when task remains active but is waiting on input, dependency or timing. | Exit only through an allowed transition with owning-Service validation. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

| Blocked | Progress is halted by a blocker that must be resolved or reviewed. | Governance State | No | Active | Non-terminal | Yes | No | No | Enter when progress is halted by a blocker that must be resolved or reviewed. | Exit only through an allowed transition with owning-Service validation. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

| ReviewRequired | Governance hold for source conflict, uncertain mapping, legal ambiguity or required professional decision; not an official result. | Governance State | No | Active | Non-terminal | Yes | No | Yes | Enter when governance hold for source conflict, uncertain mapping, legal ambiguity or required professional decision; not an official result. | Exit only through an allowed transition with owning-Service validation. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

| Completed | Parent-level work is complete according to its own completion criteria. | Inactive State | No | Inactive | Non-terminal | Guarded | No | Guarded | Enter when parent-level work is complete according to its own completion criteria. | Exit only through an allowed transition with owning-Service validation. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

| Cancelled | Cancellation outcome or governed cancellation has been recorded. | Inactive State | No | Inactive | Non-terminal | Guarded | No | Yes | Enter when cancellation outcome or governed cancellation has been recorded. | Exit only through an allowed transition with owning-Service validation. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

| Archived | Inactive archival state retained for history and ordinary reporting. | Archival / Reference-Only State | No | Inactive | Terminal | Guarded | No | Guarded | Enter when inactive archival state retained for history and ordinary reporting. | No ordinary exit; restoration is deferred governance. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

| DeletedReferenceOnly | Terminal tombstone/reference-only state with no normal business transition. | Archival / Reference-Only State | No | Inactive | Terminal | No | No | Yes | Enter when terminal tombstone/reference-only state with no normal business transition. | No ordinary business exit. | `TaskStatusChanged` with prior status, next status, actor, reason and audit context. |

# 7. State Categories

```text
Internal Planning State
Governance State
Inactive State
Archival / Reference-Only State
```

# 8. Initial State Rules

`Draft` is the normal initial state unless governed import validation permits another existing-source state.

# 9. Terminal and Inactive State Rules

`Archived` is terminal archival for ordinary flow. `DeletedReferenceOnly` is terminal reference/tombstone state.

# 10. Transition Model

```text

Draft -> Open

Draft -> Assigned

Draft -> Cancelled

Draft -> Archived

Open -> Assigned

Open -> InProgress

Open -> Waiting

Open -> Blocked

Open -> ReviewRequired

Open -> Completed

Open -> Cancelled

Assigned -> InProgress

Assigned -> Waiting

Assigned -> Blocked

Assigned -> ReviewRequired

Assigned -> Completed

Assigned -> Cancelled

InProgress -> Waiting

InProgress -> Blocked

InProgress -> ReviewRequired

InProgress -> Completed

InProgress -> Cancelled

Waiting -> Assigned

Waiting -> InProgress

Waiting -> Blocked

Waiting -> ReviewRequired

Waiting -> Cancelled

Blocked -> Assigned

Blocked -> InProgress

Blocked -> Waiting

Blocked -> ReviewRequired

Blocked -> Cancelled

ReviewRequired -> Assigned

ReviewRequired -> InProgress

ReviewRequired -> Completed

ReviewRequired -> Cancelled

Completed -> Archived

Cancelled -> Archived

Completed -> Open

Cancelled -> Open

```

# 11. Transition Validation

Unlisted transitions return `InvalidTransition` unless a stricter applicable Workflow Contract also validates the route. Validate current status, requested status, actor, permission, policy, guards, idempotency and event trace.

# 12. Owning Service Mutation Authority

Only Task Service mutates `Task.status` and must preserve previous status, next status, actor, reason, source and audit context.

# 13. Permission and Policy

Permission and Policy are mandatory for sensitive, terminal, reopening, cancellation, completion, archival or externally sourced transitions.

# 14. Human Review

Leaving `ReviewRequired` requires a review result. Leaving `Blocked` requires blocker resolution. AI must not automatically complete, cancel, archive or reopen Tasks.

# 15. Event Requirements

Each mutation produces or requires `TaskStatusChanged` with previous/next status and reason semantics.

# 16. API and Contract Consumption

API requests cannot define states or bypass transition validation. Contracts consume this spec and may constrain but not expand state truth.

# 17. AI Boundary

AI may explain, summarize or recommend for review only; AI cannot create values, mutate status, approve, cancel, complete, archive or execute protected action.

# 18. Product Consumption

Product UI consumes these values and may render labels; UI text is not canonical state definition.

# 19. Source and Official-Status Boundary

`Assigned` requires an assignee reference. `Completed` requires completion context. Governed reopen is limited to the explicit reopen operation.

# 20. Compatibility and Versioning

Legacy Object ID is historical/reclassified metadata only and must not be used as a new Spec ID.

# 21. Failure and Reason Semantics

Failures include InvalidState, InvalidTransition, PermissionRequired, PolicyRequired, ReviewRequired, ApprovalRequired and Blocked. Reasons must be auditable.

# 22. Valid Examples

Valid: `Draft -> Open` through Task Service with event trace.

# 23. Invalid Examples

Invalid: Product UI directly changes `Task.status` or invents a new state.

## Governed Reopen Exception

`Completed -> Open` and `Cancelled -> Open` are governed reopen exceptions requiring an explicit governed reopen operation with actor, permission, policy, reopen reason, prior status, new status, audit context, event trace and Workflow Contract validation when applicable. Ordinary `changeTaskStatus` must not silently reopen.

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
