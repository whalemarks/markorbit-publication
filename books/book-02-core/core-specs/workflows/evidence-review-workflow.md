# Evidence Review Workflow

**Spec ID:** B02-WORKFLOW-EVIDENCE-REVIEW  
**Spec Type:** Workflow Specification  
**Spec File:** core-specs/workflows/evidence-review-workflow.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Workflow Index:** core-specs/workflows/index.md  
**Related Workflow Contract:** core-specs/contracts/workflows/evidence-review-workflow-contract.md  
**Related API Contracts:** evidence-api-contract; document-api-contract; trademark-api-contract; matter-api-contract; order-api-contract; task-api-contract; communication-api-contract; event-api-contract  
**Related Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Codex Task:** codex-tasks/TASK-008-workflow-validator-scaffold.md  
**Status:** Draft  
**Version:** 0.1.0  
**Workflow ID:** evidence-review-workflow  
**Workflow Contract Version:** v0.1.0  
**MVP Category:** Stub Now  
**Implementation Depth:** Level 1/2 — Preview / Validation Stub  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Evidence Review Workflow defines the future professional workflow for reviewing trademark-related evidence.

It may support evidence preparation for:

```text
use evidence
office action response evidence
distinctiveness evidence
renewal / declaration evidence
opposition or cancellation evidence
assignment support evidence
marketplace or enforcement evidence
```

In MVP, this workflow is a safe stub.

It may validate evidence references, identify missing evidence fields, prepare evidence gap summaries and produce task plan previews.

It must not certify evidence sufficiency, legal admissibility, official acceptability or case outcome.

---

# 2. Core Lock

```text
Evidence Review Workflow coordinates evidence review preparation.
It is Stub Now in MVP.
Workflow preview has no side effects.
Workflow apply is not production-enabled in MVP.
Evidence Service owns Evidence state.
Document Service owns evidence document references.
Trademark Service owns Trademark state.
Matter Service owns Matter state.
Order Service owns Order state.
Task Service creates active Tasks only when explicitly allowed by MVP scope.
Communication Service owns Communication drafts.
Event Service preserves trace.
Workflow layer must not certify evidence sufficiency.
Workflow layer must not certify legal admissibility.
Workflow layer must not submit evidence officially.
AI may summarize evidence gaps but must not define professional truth.
Human Review gates all evidence sufficiency and professional conclusions.
Codex implements validation and preview-only boundaries only.
```

---

# 3. Workflow Position

Evidence Review Workflow may be used by:

```text
trademark-application-workflow
office-action-response-workflow
renewal-workflow
assignment-workflow
opposition/cancellation future workflows
enforcement future workflows
```

It may involve:

```text
evidence document references
use screenshots
sales records
website pages
advertising materials
marketplace listings
declaration documents
translation documents
notarization/legalization requirements
date/source/authenticity review
jurisdiction-specific evidence requirements
```

In MVP, it is not part of the executable spine.

It exists to preserve evidence-governance architecture and prevent AI or workflow shortcuts from certifying legal sufficiency.

---

# 4. Workflow Category

```text
MVP Category: Stub Now
Implementation Depth: Level 1/2
Execution Mode: Preview / Validation Stub
Apply Behavior: Not production-enabled in MVP
Evidence Sufficiency Certification: Not allowed in MVP
Official Submission: Not allowed in MVP
External Side Effects: Not allowed in MVP
AI Use: Summary / gap suggestion / draft only
Human Review: Required for sufficiency, admissibility and official-readiness conclusions
```

---

# 5. Related Services

Future full workflow may coordinate:

```text
Evidence Service
Document Service
Trademark Service
Matter Service
Order Service
Task Service
Communication Service
Event Service
Permission Service
Policy Service
Knowledge Service
Jurisdiction Service
Classification Service
Routing Service
Service Provider Service
```

MVP stub may only require:

```text
reference validation
Permission/Policy validation
safe evidence preview
AI Context validation where AI-assisted
Human Review requirement declaration
safe NotImplemented for apply
safe Errors
Versioning validation
```

---

# 6. Ownership Rules

| Area | Owner |
|---|---|
| Evidence state | Evidence Service |
| Evidence document metadata/reference | Document Service |
| Trademark state | Trademark Service |
| Matter state | Matter Service |
| Order/commercial scope | Order Service |
| Active Task | Task Service |
| Communication draft/send state | Communication Service |
| Event trace | Event Service / owning service integration |
| Permission evaluation | Permission Service |
| Policy evaluation | Policy Service |
| Workflow coordination | Evidence Review Workflow |
| Professional sufficiency conclusion | Human professional review / owning service gate |

Workflow must not own Evidence state or professional sufficiency conclusion.

---

# 7. Inputs

```yaml
workflow_id: evidence-review-workflow
workflow_contract_version: v0.1.0
operation: preview | apply
actor_reference_id: usr_...
organization_reference_id: org_...
evidence_reference_ids: list
document_reference_ids: list
trademark_reference_id: tm_... | null
matter_reference_id: mat_... | null
order_reference_id: ord_... | null
evidence_review_input:
  evidence_purpose: use_evidence | distinctiveness | office_action_response | renewal | declaration | opposition | cancellation | enforcement | assignment | unknown
  target_jurisdiction: string | null
  target_classes: list | null
  target_goods_services: list | null
  relevant_period_start: string | null
  relevant_period_end: string | null
  source_channel: website | marketplace | invoice | advertisement | social_media | declaration | unknown
  review_questions: list
  client_notes: string | null
document_inputs:
  uploaded_document_reference_ids: list
  translation_document_reference_ids: list
  notarization_document_reference_ids: list
communication_input:
  client_request_needed: boolean
  professional_review_needed: boolean
ai_context:
  optional
human_review_reference_id: string | null
idempotency_key: string | required only if apply becomes enabled in later phase
correlation_id: string | null
```

---

# 8. Required Input Rules

For MVP preview:

```text
workflow_id is required.
workflow_contract_version is required.
actor_reference_id is required.
organization_reference_id is required.
At least one evidence_reference_id or document_reference_id is required.
evidence_purpose is required or may be unknown with missing-input warning.
target_jurisdiction is recommended where evidence is jurisdiction-specific.
Permission/Policy context is required.
idempotency_key is not required for preview.
```

For MVP apply:

```text
apply is not production-enabled in MVP.
apply must return safe NotImplemented or equivalent controlled response.
apply must not mutate Evidence state.
apply must not create active Tasks.
apply must not create Communication.
apply must not emit Events.
apply must not certify evidence sufficiency.
apply must not submit evidence officially.
```

---

# 9. Outputs

Preview output:

```yaml
workflow_id: evidence-review-workflow
workflow_contract_version: v0.1.0
operation: preview
status: preview_ready | missing_required_inputs | blocked | review_required | not_implemented
evidence_preview:
  evidence_reference_ids: list
  document_reference_ids: list
  evidence_purpose: string
  target_jurisdiction: string | null
  evidence_sufficiency_certified: false
  legal_admissibility_certified: false
  official_readiness_certified: false
  missing_evidence_fields: list
  evidence_gap_items: list
document_preview:
  accepted_document_references: list
  rejected_document_references: list
  missing_documents: list
  translation_review_required: boolean
  notarization_review_required: boolean
task_plan:
  planned_tasks: list
communication_preview:
  client_request_draft_needed: boolean
  professional_review_note_needed: boolean
ai_output:
  summary: string | null
  gap_suggestions: list
  non_final: true
policy:
  restricted_fields_omitted: boolean
  policy_omissions_disclosed: boolean
human_review:
  human_review_required: true
warnings: list
errors: list
```

Apply output in MVP:

```yaml
workflow_id: evidence-review-workflow
operation: apply
status: not_implemented
error:
  code: StateInvalid
  message: apply is not production-enabled for evidence review workflow in MVP
  retryable: false
```

---

# 10. Preview Behavior

Preview may:

```text
validate request shape
validate evidence references
validate document references
validate subject trademark/matter/order references
check Permission/Policy
identify missing evidence metadata
identify missing date/source/channel information
identify missing translation/notarization/legalization review needs
prepare evidence gap checklist
prepare client request draft summary
prepare professional review note summary
prepare task plan preview
mark HumanReviewRequired
show policy omissions
return safe warnings
```

Preview must not:

```text
mutate Evidence
create Matter
create Order
create active Task
create Communication
emit Event
certify evidence sufficiency
certify legal admissibility
certify official acceptability
certify use in commerce
certify distinctiveness
certify case outcome
submit evidence officially
send communication
engage provider
```

---

# 11. Apply Behavior

In MVP, apply is not production-enabled.

Apply must:

```text
return controlled safe not-implemented response
perform no side effects
not mutate Evidence state
not create active Tasks
not create Communications
not emit Events
not certify evidence sufficiency
not submit evidence officially
```

Future apply may coordinate:

```text
Evidence Service
Document Service
Matter Service
Order Service
Task Service
Communication Service
Event Service
Permission Service
Policy Service
```

Future apply must still require:

```text
idempotency_key
Permission/Policy
Human Review
safe Errors
Versioning
Event trace through owning services
```

---

# 12. Workflow Steps

## 12.1 Step 1 — Validate Request

Validates:

```text
workflow_id
workflow_contract_version
operation
actor_reference_id
organization_reference_id
evidence_reference_ids
document_reference_ids
target_jurisdiction
correlation_id
```

## 12.2 Step 2 — Permission / Policy Precheck

Checks:

```text
evidence data access
document metadata access
trademark/matter/order access where supplied
AI source use policy
cross-organization policy
event trace visibility where referenced
```

## 12.3 Step 3 — Evidence Context Preview

May identify:

```text
evidence purpose
target jurisdiction
target goods/services/classes
relevant time period
source channel
source reliability questions
evidence metadata gaps
commercial/source restrictions
```

This does not certify sufficiency or admissibility.

## 12.4 Step 4 — Document and Support Gap Preview

May identify:

```text
missing source URL
missing date information
missing translation
missing notarization/legalization review
missing sales/use link
missing trademark display
missing goods/services link
missing applicant/owner link
missing jurisdiction-specific requirement
```

This does not certify official acceptability.

## 12.5 Step 5 — Task Plan Preview

May prepare planned tasks:

```text
collect missing evidence date
collect source URL
collect sales/invoice support
collect trademark-use screenshot
collect translation
review notarization/legalization need
obtain professional evidence review
prepare client evidence request
prepare evidence summary note
```

Task plan is not active Task in MVP stub.

## 12.6 Step 6 — Communication Preview

May prepare:

```text
client evidence request outline
professional review note outline
provider evidence instruction outline
internal evidence gap summary
```

No communication is created or sent in MVP stub unless separately coordinated through Communication Service in a later phase.

## 12.7 Step 7 — AI-Assisted Evidence Summary

AI may prepare:

```text
evidence summary
evidence gap list
date/source/channel summary
goods/services linkage suggestion
risk flags
client question list
```

AI must not:

```text
certify evidence sufficiency
certify legal admissibility
certify official acceptability
certify use in commerce
certify distinctiveness
certify outcome probability
submit evidence
send communication
emit Events
```

## 12.8 Step 8 — Return Safe Preview

Returns:

```text
evidence preview
missing inputs
task plan
AI summary if applicable
HumanReviewRequired
policy omissions
safe warnings/errors
```

---

# 13. Permission Requirements

Required permissions may include:

```text
evidence:read
evidence:review_preview
document:read
trademark:read
matter:read
order:read
communication:draft
event:read
```

Future apply may require:

```text
evidence:update
evidence:review_apply
task:create
communication:create
```

Rules:

```text
PermissionDenied blocks protected preview.
UnknownPermission fails closed.
MissingPermissionContext fails closed.
PermissionAllowed does not bypass Policy.
```

---

# 14. Policy Requirements

Required policy scopes may include:

```text
evidence:data:visible
evidence:content:visible
document:metadata:visible
document:content:visible
trademark:data:visible
matter:data:visible
order:data:visible
ai_source:allowed
cross_organization:allowed
event:trace:visible
```

Rules:

```text
PolicyRestrictedBlock blocks workflow preview.
PolicyRestrictedRedact redacts output and sets restricted_fields_omitted.
PolicyRequiresHumanReview marks review required.
PolicyNonDisclosureNotFound hides object/source existence.
UnknownPolicy fails closed where policy-controlled.
```

---

# 15. Idempotency

MVP preview:

```text
does not require idempotency_key because preview has no side effects.
```

MVP apply:

```text
not production-enabled.
must not create side effects.
```

Future apply must require:

```text
idempotency_key
same key + same semantic request replay safety
same key + different semantic request conflict
no duplicate Tasks
no duplicate Communications
no duplicate Events
no duplicate evidence review result
no policy-hidden replay leakage
```

---

# 16. Event Trace

MVP preview:

```text
does not emit Events.
```

MVP apply:

```text
not production-enabled.
does not emit Events.
```

Future expected event types may include:

```text
evidence-review-previewed
evidence-review-preparation-started
evidence-document-attached
evidence-gap-identified
evidence-review-note-created
task-created
communication-draft-created
permission-evaluated
policy-evaluated
```

Rules:

```text
Workflow does not emit Events directly.
Event references are trace only.
Event references are not commands.
Event visibility follows Permission/Policy.
Evidence content must not leak through restricted Event payload.
```

---

# 17. Task Plan Rules

MVP task plan may include:

```yaml
planned_task_type: collect_missing_evidence
subject_reference_id: evd_...
required_owner_role: evidence_reviewer
priority: normal
human_review_required: true
policy_restrictions:
  - evidence_content_restricted
source_step: evidence-review-preview
```

Rules:

```text
Task plan is not active Task.
MVP stub does not create active Task.
Future active Tasks must be created only by Task Service.
AI task suggestions cannot become active Tasks directly.
```

---

# 18. Communication Rules

Preview may prepare:

```text
client evidence request outline
professional evidence review note outline
provider evidence instruction outline
internal evidence gap summary
```

Rules:

```text
Communication draft is not sent.
MVP stub does not create Communication unless separately allowed by Communication Service.
External send requires Communication Review Workflow and Human Review.
AI draft remains draft/suggestion/non-final.
```

---

# 19. AI Context

Allowed AI outputs:

```text
evidence summary
evidence gap list
document checklist
date/source/channel issue list
goods/services linkage suggestion
client question list
risk flags
```

Forbidden AI outputs:

```text
evidence sufficiency certification
legal admissibility certification
official acceptability certification
use in commerce certification
distinctiveness certification
outcome probability certification
professional conclusion
official submission
external communication send
event emission
state mutation
```

AI output must include:

```text
ai_assisted = true
capability_scope
source_scope
policy_omissions_disclosed where applicable
human_review_required = true
draft/suggestion/non-final marker
```

---

# 20. Human Review

Human Review is required for:

```text
evidence sufficiency conclusion
legal admissibility conclusion
official acceptability conclusion
use in commerce conclusion
distinctiveness conclusion
date/source authenticity conclusion
translation/notarization/legalization conclusion
client-facing evidence explanation
provider evidence instruction approval
```

Rules:

```text
Human Review does not execute downstream action by itself.
Human Review does not bypass Permission.
Human Review does not bypass Policy.
Owning service determines whether review satisfies future gate.
```

---

# 21. Error Handling

Required controlled errors:

```text
ValidationFailed
ReferenceInvalid
PermissionDenied
PolicyRestricted
HumanReviewRequired
VersionUnsupported
StateInvalid
NotFound
Conflict
InternalError
```

If apply is called in MVP:

```text
StateInvalid or NotImplemented-equivalent safe controlled error
```

Errors must not expose:

```text
database IDs
restricted evidence data
evidence document contents
restricted trademark data
client private notes
provider commercial terms
policy internals
permission internals
stack traces
AI prompts
hidden reasoning
```

---

# 22. Versioning

Required versions:

```text
workflow_contract_version
schema_version where applicable
contract_version for related API/service contracts
```

Rules:

```text
Unsupported workflow_contract_version returns VersionUnsupported.
Missing required version fails safely.
Historical future workflow application version must be preserved.
AI output version context must be preserved where recorded.
```

---

# 23. Out of Scope

Evidence Review Workflow MVP does not implement:

```text
evidence sufficiency certification
legal admissibility certification
official acceptability certification
use in commerce certification
distinctiveness certification
case outcome prediction as final conclusion
official evidence submission
production task creation
production event emission
external communication send
provider final selection
payment execution
full evidence management engine
full AI evidence legal reviewer
```

---

# 24. Forbidden Shortcuts

Codex must not:

```text
turn preview into production apply
certify evidence sufficiency
certify legal admissibility
certify official acceptability
certify use in commerce
certify distinctiveness
create active Task directly from workflow layer
emit Events directly from workflow layer
send Communication directly from workflow layer
submit evidence officially
skip Permission/Policy
treat AI output as professional conclusion
treat Human Review record as automatic official submission approval
accept unsupported versions silently
return unsafe errors
```

---

# 25. Test Requirements

Required tests:

```text
preview_valid_request_returns_evidence_review_plan
preview_missing_required_inputs_returns_missing_inputs
preview_has_no_side_effects
preview_permission_denied_blocks
preview_policy_restricted_blocks
preview_policy_redacts_output
preview_policy_nondisclosure_returns_notfound
preview_human_review_required_for_sufficiency_conclusion
apply_returns_not_implemented_in_mvp
apply_has_no_side_effects_in_mvp
workflow_does_not_emit_events_directly
workflow_does_not_create_active_tasks_directly
workflow_does_not_certify_evidence_sufficiency
workflow_does_not_submit_evidence
ai_evidence_sufficiency_certification_blocked
ai_legal_admissibility_certification_blocked
event_reference_is_trace_only
version_unsupported_fails_closed
safe_errors_no_database_id_or_stack_trace
restricted_evidence_data_not_leaked
```

---

# 26. Acceptance Criteria

Evidence Review Workflow is accepted only if:

```text
[ ] Workflow purpose is clear.
[ ] Workflow category is Stub Now.
[ ] Related workflow contract exists.
[ ] Preview behavior is side-effect free.
[ ] Apply is not production-enabled in MVP.
[ ] Evidence sufficiency certification is explicitly forbidden.
[ ] Legal admissibility certification is explicitly forbidden.
[ ] Official evidence submission is explicitly out of scope.
[ ] Task plan is not active Task.
[ ] Workflow does not emit Events directly.
[ ] Workflow does not send Communication directly.
[ ] Permission/Policy checks are defined.
[ ] Evidence content policy restrictions are preserved.
[ ] AI output remains draft/suggestion/non-final.
[ ] Human Review gates evidence professional conclusions.
[ ] Safe Error behavior is defined.
[ ] Versioning behavior is defined.
[ ] Forbidden shortcuts are explicit.
[ ] Required tests are defined.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Evidence Review Workflow. Defines Stub Now evidence preview/validation behavior, future coordination scope, ownership, inputs/outputs, side-effect-free preview, apply disabled in MVP, evidence sufficiency/admissibility/submission boundaries, Permission/Policy, AI/Human Review, Event/Task/Communication boundaries, errors, versioning, out-of-scope, forbidden shortcuts and tests. |

---

**End of Evidence Review Workflow**
