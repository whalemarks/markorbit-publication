# Controlled State Value Specification — Matter Status Values



Spec ID: B02-CSV-MATTER-STATUS

Spec Type: Controlled State Value Specification

Parent Object: Matter

Owning Domain: Matter

Owning Service: Matter Service

Parent Field: Matter.status

Legacy Object ID: OBJ-MAT-002 — Reclassified

Status: Draft

Version: 0.1.0

MVP Phase: Phase 3

MVP Depth: Must Implement

Owner: MarkOrbit Publications Editorial Board



# 1. Purpose

Defines legal values, semantics, transitions and governance for `Matter.status`.

# 2. Classification

This is a Controlled State Value Specification owned by the parent object. It is not an independent Core Object, aggregate root, repository, table, source of truth or UI list.

# 3. Parent Ownership

Matter owns state truth. Matter Service is the only mutation authority.

# 4. Parent Field

`Matter.status` consumes these exact values.

# 5. Canonical Values

```text

Draft

Open

InProgress

WaitingForCustomer

WaitingForAgent

WaitingForOffice

ReviewRequired

Blocked

Completed

Cancelled

Archived

DeletedReferenceOnly

```

# 6. Value Semantics

| Canonical value | Core meaning | State category | Initial allowed | Active / inactive | Terminal behavior | Reopenable | Official-source-sensitive | Human-review-sensitive | Typical entry condition | Typical exit condition | Event expectation |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Draft | Record is being prepared and is not ready for committed execution. | Internal Planning State | Yes | Active | Non-terminal | Yes | No | No | Enter when record is being prepared and is not ready for committed execution. | Exit only through an allowed transition with owning-Service validation. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| Open | Parent is active and available for work but may not yet be actively performed. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when parent is active and available for work but may not yet be actively performed. | Exit only through an allowed transition with owning-Service validation. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| InProgress | Work or fulfillment related to the parent is actively underway. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when work or fulfillment related to the parent is actively underway. | Exit only through an allowed transition with owning-Service validation. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| WaitingForCustomer | Parent remains active but requires customer input or response. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when parent remains active but requires customer input or response. | Exit only through an allowed transition with owning-Service validation. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| WaitingForAgent | Matter waits for agent/provider action and remains active. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when matter waits for agent/provider action and remains active. | Exit only through an allowed transition with owning-Service validation. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| WaitingForOffice | Matter remains active while waiting for official-office response or procedural occurrence; this does not establish an official outcome. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when matter remains active while waiting for official-office response or procedural occurrence; this does not establish an official outcome. | Exit only through an allowed transition with owning-Service validation. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| ReviewRequired | Governance hold for source conflict, uncertain mapping, legal ambiguity or required professional decision; not an official result. | Governance State | No | Active | Non-terminal | Yes | No | Yes | Enter when governance hold for source conflict, uncertain mapping, legal ambiguity or required professional decision; not an official result. | Exit only through an allowed transition with owning-Service validation. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| Blocked | Progress is halted by a blocker that must be resolved or reviewed. | Governance State | No | Active | Non-terminal | Yes | No | No | Enter when progress is halted by a blocker that must be resolved or reviewed. | Exit only through an allowed transition with owning-Service validation. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| Completed | Parent-level work is complete according to its own completion criteria. | Inactive State | No | Inactive | Non-terminal | Guarded | No | Guarded | Enter when parent-level work is complete according to its own completion criteria. | Exit only through an allowed transition with owning-Service validation. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| Cancelled | Cancellation outcome or governed cancellation has been recorded. | Inactive State | No | Inactive | Non-terminal | Guarded | No | Yes | Enter when cancellation outcome or governed cancellation has been recorded. | Exit only through an allowed transition with owning-Service validation. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| Archived | Inactive archival state retained for history and ordinary reporting. | Archival / Reference-Only State | No | Inactive | Terminal | Guarded | No | Guarded | Enter when inactive archival state retained for history and ordinary reporting. | No ordinary exit; restoration is deferred governance. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

| DeletedReferenceOnly | Terminal tombstone/reference-only state with no normal business transition. | Archival / Reference-Only State | No | Inactive | Terminal | No | No | Yes | Enter when terminal tombstone/reference-only state with no normal business transition. | No ordinary business exit. | `MatterStatusChanged` with prior status, next status, actor, reason and audit context. |

# 7. State Categories

Internal Planning State; Official / Procedural Normalized State; Maintenance State; Governance State; Inactive State; Archival / Reference-Only State.

# 8. Initial State Rules

`Draft` is the normal initial state unless governed import validation permits another existing-source state.

# 9. Terminal and Inactive State Rules

`Archived` is terminal archival for ordinary flow. `DeletedReferenceOnly` is terminal reference/tombstone state.

# 10. Transition Model

```text

Draft -> Open

Draft -> Cancelled

Draft -> Archived

Open -> InProgress

Open -> WaitingForCustomer

Open -> WaitingForAgent

Open -> WaitingForOffice

Open -> ReviewRequired

Open -> Blocked

Open -> Completed

Open -> Cancelled

InProgress -> WaitingForCustomer

InProgress -> WaitingForAgent

InProgress -> WaitingForOffice

InProgress -> ReviewRequired

InProgress -> Blocked

InProgress -> Completed

InProgress -> Cancelled

WaitingForCustomer -> InProgress

WaitingForCustomer -> ReviewRequired

WaitingForCustomer -> Blocked

WaitingForCustomer -> Cancelled

WaitingForAgent -> InProgress

WaitingForAgent -> ReviewRequired

WaitingForAgent -> Blocked

WaitingForAgent -> Cancelled

WaitingForOffice -> InProgress

WaitingForOffice -> ReviewRequired

WaitingForOffice -> Blocked

WaitingForOffice -> Cancelled

ReviewRequired -> InProgress

ReviewRequired -> WaitingForCustomer

ReviewRequired -> WaitingForAgent

ReviewRequired -> WaitingForOffice

ReviewRequired -> Blocked

ReviewRequired -> Completed

ReviewRequired -> Cancelled

Blocked -> InProgress

Blocked -> ReviewRequired

Blocked -> Cancelled

Completed -> Archived

Cancelled -> Archived

```

# 11. Transition Validation

Unlisted transitions return `InvalidTransition` unless a stricter applicable Workflow Contract also validates the route. Validate current status, requested status, actor, permission, policy, guards, idempotency and event trace.

# 12. Owning Service Mutation Authority

Only Matter Service mutates `Matter.status` and must preserve previous status, next status, actor, reason, source and audit context.

# 13. Permission and Policy

Permission and Policy are mandatory for sensitive, terminal, reopening, cancellation, completion, archival or externally sourced transitions.

# 14. Human Review

Leaving `ReviewRequired` requires a review outcome. Leaving `Blocked` requires blocker resolution. Workflow-linked Matter transitions must also satisfy the applicable Workflow Contract. Human Review governs professional judgment, exception handling and sensitive cancellation/completion decisions.

# 15. Event Requirements

Each mutation produces or requires `MatterStatusChanged` with previous/next status and reason semantics.

# 16. API and Contract Consumption

API requests cannot define states or bypass transition validation. Contracts consume this spec and may constrain but not expand state truth.

# 17. AI Boundary

AI may explain, summarize or recommend for review only; AI cannot create values, mutate status, approve, cancel, complete, archive or execute protected action.

# 18. Product Consumption

Product UI consumes these values and may render labels; UI text is not canonical state definition.

# 19. Source and Official-Status Boundary

`WaitingForOffice` does not establish an official result. `Completed` is Matter container completion and does not imply that a Trademark registered or any legal right succeeded.

# 20. Compatibility and Versioning

Legacy Object ID is historical/reclassified metadata only and must not be used as a new Spec ID.

# 21. Failure and Reason Semantics

Failures include InvalidState, InvalidTransition, PermissionRequired, PolicyRequired, ReviewRequired, ApprovalRequired and Blocked. Reasons must be auditable.

# 22. Valid Examples

Valid: `Draft -> Open` through Matter Service with event trace.

# 23. Invalid Examples

Invalid: Product UI directly changes `Matter.status` or invents a new state.

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
