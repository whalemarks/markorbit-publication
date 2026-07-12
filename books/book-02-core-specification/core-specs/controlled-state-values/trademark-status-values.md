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

Defines legal values, semantics, transitions and governance for `Trademark.status`.

# 2. Classification

This is a Controlled State Value Specification owned by the parent object. It is not an independent Core Object, aggregate root, repository, table, source of truth or UI list.

# 3. Parent Ownership

Trademark owns state truth. Trademark Service is the only mutation authority.

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

| Draft | Record is being prepared and is not ready for committed execution. | Internal Planning State | Yes | Active | Non-terminal | Yes | No | No | Enter when record is being prepared and is not ready for committed execution. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Planned | Internal plan exists but filing has not been requested. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when internal plan exists but filing has not been requested. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| PendingFiling | Filing preparation is ready for validation before filed evidence exists. | Internal Planning State | No | Active | Non-terminal | Yes | No | No | Enter when filing preparation is ready for validation before filed evidence exists. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Filed | A normalized filing state has been validated from source evidence. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | No | Enter when a normalized filing state has been validated from source evidence. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| UnderExamination | Official examination is understood to be pending or active from validated source context. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | No | Enter when official examination is understood to be pending or active from validated source context. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Published | Publication/opposition-window state has been normalized from source context. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | No | Enter when publication/opposition-window state has been normalized from source context. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Opposed | Opposition or contested procedure has been normalized from source context. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | No | Enter when opposition or contested procedure has been normalized from source context. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Registered | Registration/protection has been normalized from validated official or professional source context; later exits may be maintenance-related. | Official / Procedural Normalized State | No | Active | Non-terminal | Yes | Yes | Guarded | Enter when registration/protection has been normalized from validated official or professional source context; later exits may be maintenance-related. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Refused | Refusal outcome has been normalized and is inactive unless reviewed or abandoned. | Inactive State | No | Inactive | Non-terminal | Guarded | Yes | Yes | Enter when refusal outcome has been normalized and is inactive unless reviewed or abandoned. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Abandoned | Application or record is no longer actively pursued. | Inactive State | No | Inactive | Non-terminal | Guarded | No | No | Enter when application or record is no longer actively pursued. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Cancelled | Cancellation outcome or governed cancellation has been recorded. | Inactive State | No | Inactive | Non-terminal | Guarded | Yes | Yes | Enter when cancellation outcome or governed cancellation has been recorded. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Expired | Protection period has lapsed based on validated maintenance/source context. | Inactive State | No | Inactive | Non-terminal | Guarded | Yes | No | Enter when protection period has lapsed based on validated maintenance/source context. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Invalidated | Invalidity outcome has been normalized from authoritative or reviewed context. | Inactive State | No | Inactive | Non-terminal | Guarded | Yes | Yes | Enter when invalidity outcome has been normalized from authoritative or reviewed context. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| RenewalDue | Registered record requires maintenance attention before expiry or loss. | Maintenance State | No | Active | Non-terminal | Yes | Yes | Guarded | Enter when registered record requires maintenance attention before expiry or loss. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| ReviewRequired | Governance hold for source conflict, uncertain mapping, legal ambiguity or required professional decision; not an official result. | Governance State | No | Active | Non-terminal | Yes | No | Yes | Enter when governance hold for source conflict, uncertain mapping, legal ambiguity or required professional decision; not an official result. | Exit only through an allowed transition with owning-Service validation. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| Archived | Inactive archival state retained for history and ordinary reporting. | Archival / Reference-Only State | No | Inactive | Terminal | Guarded | No | Guarded | Enter when inactive archival state retained for history and ordinary reporting. | No ordinary exit; restoration is deferred governance. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

| DeletedReferenceOnly | Terminal tombstone/reference-only state with no normal business transition. | Archival / Reference-Only State | No | Inactive | Terminal | No | No | Yes | Enter when terminal tombstone/reference-only state with no normal business transition. | No ordinary business exit. | `TrademarkStatusChanged` with prior status, next status, actor, reason and audit context. |

# 7. State Categories

```text
Internal Planning State
Official / Procedural Normalized State
Maintenance State
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

Unlisted transitions return `InvalidTransition` unless a stricter applicable Workflow Contract also validates the route. Validate current status, requested status, actor, permission, policy, guards, idempotency and event trace.

# 12. Owning Service Mutation Authority

Only Trademark Service mutates `Trademark.status` and must preserve previous status, next status, actor, reason, source and audit context.

# 13. Permission and Policy

Permission and Policy are mandatory for sensitive, terminal, reopening, cancellation, completion, archival or externally sourced transitions.

# 14. Human Review

Leaving `ReviewRequired` requires a Human Review outcome. Official/procedural uncertainty, source conflicts, ambiguous jurisdictional interpretation, refusal/cancellation/invalidity interpretation, or unsupported transition requests require Human Review. `ReviewRequired` is not an alternative official lifecycle result and cannot be used as a back door around invalid transitions.

# 15. Event Requirements

Each mutation produces or requires `TrademarkStatusChanged` with previous/next status and reason semantics.

# 16. API and Contract Consumption

API requests cannot define states or bypass transition validation. Contracts consume this spec and may constrain but not expand state truth.

# 17. AI Boundary

AI may explain, summarize or recommend for review only; AI cannot create values, mutate status, approve, cancel, complete, archive or execute protected action.

# 18. Product Consumption

Product UI consumes these values and may render labels; UI text is not canonical state definition.

# 19. Source and Official-Status Boundary

Trademark.status is a MarkOrbit normalized state. It is not automatically the verbatim official-office status. Entering official/procedural normalized or inactive official-outcome states requires source reference, source timestamp or version, normalization evidence, jurisdiction context, validation result and Human Review when needed.

# 20. Compatibility and Versioning

Legacy Object ID is historical/reclassified metadata only and must not be used as a new Spec ID.

# 21. Failure and Reason Semantics

Failures include InvalidState, InvalidTransition, PermissionRequired, PolicyRequired, ReviewRequired, ApprovalRequired and Blocked. Reasons must be auditable.

# 22. Valid Examples

Valid: `Draft -> Planned` through Trademark Service with event trace.

# 23. Invalid Examples

Invalid: Product UI directly changes `Trademark.status` or invents a new state.

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
