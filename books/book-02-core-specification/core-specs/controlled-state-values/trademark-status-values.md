# Controlled State Value Specification — Trademark Status Values



Spec ID: B02-CSV-TRADEMARK-STATUS

Spec Type: Controlled State Value Specification

Parent Object: Trademark

Owning Domain: Trademark

Owning Service: Trademark Service

Parent Field: Trademark.status

Legacy Object ID: OBJ-TM-003 — Reclassified

Status: Draft

Version: 0.1.0

MVP Phase: Phase 2

MVP Depth: Must Implement

Owner: MarkOrbit Publications Editorial Board



# 1. Purpose

Defines legal values, semantics, transitions and governance for `Trademark.status`. The parent object owns state truth; Trademark Service is the only mutation authority.

# 2. Classification

This is not an independent Core Object, aggregate root, repository, table, source of truth or UI status list.

# 3. Parent Ownership

Trademark owns the state field. The owning Service validates current status, requested status and transition before mutation.

# 4. Parent Field

`Trademark.status` consumes these exact values.

# 5. Canonical Values

```text

Draft

Planned

PendingFiling

Filed

UnderExamination

Published

Opposed

Registered

Refused

Abandoned

Cancelled

Expired

Invalidated

RenewalDue

ReviewRequired

Archived

DeletedReferenceOnly

```

# 6. Value Semantics

| Canonical value | Core meaning | State category | Initial allowed | Active / inactive | Terminal behavior | Reopenable | Official-source-sensitive | Human-review-sensitive | Typical entry condition | Typical exit condition | Event expectation |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Draft | Canonical Trademark lifecycle state `Draft`. | Internal Planning State | Yes | Active | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Planned | Canonical Trademark lifecycle state `Planned`. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| PendingFiling | Canonical Trademark lifecycle state `PendingFiling`. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Filed | Canonical Trademark lifecycle state `Filed`. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| UnderExamination | Canonical Trademark lifecycle state `UnderExamination`. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Published | Canonical Trademark lifecycle state `Published`. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Opposed | Canonical Trademark lifecycle state `Opposed`. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Registered | Canonical Trademark lifecycle state `Registered`. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Refused | Canonical Trademark lifecycle state `Refused`. | Inactive State | No | Inactive | Non-terminal | Yes | No | Yes | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Abandoned | Canonical Trademark lifecycle state `Abandoned`. | Inactive State | No | Inactive | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Cancelled | Canonical Trademark lifecycle state `Cancelled`. | Inactive State | No | Inactive | Non-terminal | Guarded | No | Yes | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Expired | Canonical Trademark lifecycle state `Expired`. | Inactive State | No | Inactive | Non-terminal | Yes | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Invalidated | Canonical Trademark lifecycle state `Invalidated`. | Inactive State | No | Inactive | Non-terminal | Yes | No | Yes | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| RenewalDue | Canonical Trademark lifecycle state `RenewalDue`. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| ReviewRequired | Canonical Trademark lifecycle state `ReviewRequired`. | Governance State | No | Active | Non-terminal | Yes | No | Yes | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| Archived | Canonical Trademark lifecycle state `Archived`. | Archival / Reference-Only State | No | Inactive | Terminal | Guarded | No | No | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

| DeletedReferenceOnly | Canonical Trademark lifecycle state `DeletedReferenceOnly`. | Archival / Reference-Only State | No | Inactive | Terminal | No | No | Yes | Valid owning-service request or source evidence. | Allowed transition, review outcome or archival action. | `TrademarkStatusChanged` with previous and next status. |

# 7. State Categories

Internal Planning State; Official / Procedural Normalized State; Maintenance State; Governance State; Inactive State; Archival / Reference-Only State.

# 8. Initial State Rules

`Draft` is the default initial state unless a governed import contract explicitly validates another initial state.

# 9. Terminal and Inactive State Rules

`Archived` is terminal archival. `DeletedReferenceOnly` is terminal reference/tombstone and does not allow normal business transitions.

# 10. Transition Model

```text

Draft -> Planned

Planned -> Draft

Draft -> PendingFiling

Planned -> PendingFiling

PendingFiling -> Planned

PendingFiling -> Filed

PendingFiling -> ReviewRequired

PendingFiling -> Abandoned

Filed -> UnderExamination

Filed -> Published

Filed -> Opposed

Filed -> Registered

Filed -> Refused

Filed -> Abandoned

Filed -> ReviewRequired

UnderExamination -> Published

UnderExamination -> Opposed

UnderExamination -> Registered

UnderExamination -> Refused

UnderExamination -> Abandoned

UnderExamination -> ReviewRequired

Published -> Opposed

Published -> Registered

Published -> Refused

Published -> Abandoned

Published -> ReviewRequired

Opposed -> Registered

Opposed -> Refused

Opposed -> Abandoned

Opposed -> ReviewRequired

Registered -> RenewalDue

Registered -> Expired

Registered -> Cancelled

Registered -> Invalidated

Registered -> ReviewRequired

RenewalDue -> Registered

RenewalDue -> Expired

RenewalDue -> Cancelled

RenewalDue -> ReviewRequired

Refused -> ReviewRequired

Refused -> Abandoned

Refused -> Archived

Abandoned -> ReviewRequired

Abandoned -> Archived

Cancelled -> ReviewRequired

Cancelled -> Archived

Expired -> ReviewRequired

Expired -> Archived

Invalidated -> ReviewRequired

Invalidated -> Archived

```

# 11. Transition Validation

Default deny: unlisted transitions return `InvalidTransition` unless an applicable Workflow Contract defines a stricter allowed route. Validate current status, requested status, actor, permission, policy, guards, idempotency and event trace.

# 12. Owning Service Mutation Authority

Only Trademark Service mutates `Trademark.status` and must preserve previous status, next status, actor, reason, source and audit context.

# 13. Permission and Policy

Permission and Policy are mandatory for sensitive, terminal, reopening or externally sourced transitions.

# 14. Human Review

Leaving `ReviewRequired` requires Human Review outcome. Sensitive professional decisions require Human Review and may not be automated.

# 15. Event Requirements

Each mutation produces or requires `TrademarkStatusChanged` with previous/next state and reason semantics.

# 16. API and Contract Consumption

API requests cannot define states or bypass transition validation. Contracts consume this spec and may constrain but not expand status truth.

# 17. AI Boundary

AI may explain, summarize or recommend for review only; AI cannot create values, mutate status or approve protected actions.

# 18. Product Consumption

Product UI consumes these values and labels only; UI text is not canonical state definition.

# 19. Source and Official-Status Boundary

Trademark.status is a MarkOrbit normalized state. It is not automatically the verbatim official-office status. Official/procedural entries require source reference, source timestamp/version, normalization evidence, jurisdiction context, validation result and Human Review when needed.

# 20. Compatibility and Versioning

Legacy Object ID is historical only and must not be used as a new Spec ID.

# 21. Failure and Reason Semantics

Failures include InvalidState, InvalidTransition, PermissionRequired, PolicyRequired, ReviewRequired, ApprovalRequired and Blocked. Reasons must be auditable.

# 22. Valid Examples

Valid: `Draft -> Planned` through Trademark Service with event trace.

# 23. Invalid Examples

Invalid: Product UI directly changes `Trademark.status` or invents a new state.

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
