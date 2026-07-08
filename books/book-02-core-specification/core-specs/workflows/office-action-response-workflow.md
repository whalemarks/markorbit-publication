# Office Action Response Workflow

**Spec ID:** B02-WORKFLOW-OFFICE-ACTION-RESPONSE  
**Spec Type:** Workflow Specification  
**Spec File:** core-specs/workflows/office-action-response-workflow.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Workflow Index:** core-specs/workflows/index.md  
**Related Workflow Contract:** core-specs/contracts/workflows/office-action-response-workflow-contract.md  
**Related API Contracts:** trademark-api-contract; jurisdiction-api-contract; classification-api-contract; document-api-contract; evidence-api-contract; matter-api-contract; task-api-contract; communication-api-contract; event-api-contract  
**Related Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Codex Task:** codex-tasks/TASK-008-workflow-validator-scaffold.md  
**Status:** Draft  
**Version:** 0.1.0  
**Workflow ID:** office-action-response-workflow  
**Workflow Contract Version:** v0.1.0  
**MVP Category:** Stub Now  
**Implementation Depth:** Level 1/2 — Preview / Validation Stub  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Office Action Response Workflow defines the future professional workflow for preparing responses to trademark office actions, refusals, notices, examination opinions, objections and similar official communications.

In MVP, this workflow is a safe stub.

It may validate request shape, references and governance boundaries, and may produce preview-only preparation plans.

It must not submit official responses, certify legal arguments, finalize legal strategy or create production filing actions.

---

# 2. Core Lock

```text
Office Action Response Workflow coordinates response preparation.
It is Stub Now in MVP.
Workflow preview has no side effects.
Workflow apply is not production-enabled in MVP.
Trademark Service owns Trademark state.
Jurisdiction Service owns jurisdiction-specific reference behavior.
Classification Service owns classification behavior.
Document Service owns official notice and response document references.
Evidence Service owns evidence references.
Matter Service owns Matter state.
Task Service creates active Tasks only when explicitly allowed by MVP scope.
Communication Service owns communication drafts.
Event Service preserves trace.
Workflow layer must not submit official responses.
Workflow layer must not certify legal arguments.
AI may summarize office actions and suggest response gaps but must not define professional truth.
Human Review gates all professional conclusions.
Codex implements validation and preview-only boundaries only.
```

---

# 3. Workflow Position

Office Action Response Workflow is downstream of:

```text
trademark-application-workflow
```

It may involve:

```text
trademark record
official notice document
office action deadline context
classification objections
absolute/relative refusal issues
evidence of use or distinctiveness
response draft
professional review tasks
foreign associate or attorney communication
```

In MVP, it is not part of the executable spine.

It exists to preserve future architecture and prevent ad hoc implementation later.

---

# 4. Workflow Category

```text
MVP Category: Stub Now
Implementation Depth: Level 1/2
Execution Mode: Preview / Validation Stub
Apply Behavior: Not production-enabled in MVP
Official Response Filing: Not allowed in MVP
External Side Effects: Not allowed in MVP
AI Use: Summary / gap suggestion / draft outline only
Human Review: Required for all professional conclusions
```

---

# 5. Related Services

Future full workflow may coordinate:

```text
Trademark Service
Jurisdiction Service
Classification Service
Document Service
Evidence Service
Matter Service
Order Service
Task Service
Communication Service
Event Service
Permission Service
Policy Service
Knowledge Service
Routing Service
Service Provider Service
```

MVP stub may only require:

```text
reference validation
Permission/Policy validation
AI Context validation where AI-assisted
safe preview output
safe NotImplemented for apply
safe Errors
Versioning validation
```

---

# 6. Ownership Rules

| Area | Owner |
|---|---|
| Trademark state | Trademark Service |
| Jurisdiction rules/reference | Jurisdiction Service |
| Classification state | Classification Service |
| Official notice document reference | Document Service |
| Response draft document reference | Document Service |
| Evidence reference | Evidence Service |
| Matter state | Matter Service |
| Order/commercial scope | Order Service |
| Active Task | Task Service |
| Communication draft/send state | Communication Service |
| Event trace | Event Service / owning service integration |
| Permission evaluation | Permission Service |
| Policy evaluation | Policy Service |
| Workflow coordination | Office Action Response Workflow |

Workflow must not own official legal response behavior.

---

# 7. Inputs

```yaml
workflow_id: office-action-response-workflow
workflow_contract_version: v0.1.0
operation: preview | apply
actor_reference_id: usr_...
organization_reference_id: org_...
trademark_reference_id: tm_...
matter_reference_id: mat_... | null
office_action_input:
  office_action_document_reference_id: doc_...
  office_action_type: refusal | objection | notice | requirement | unknown
  issuing_office: string | null
  issue_date: string | null
  response_deadline: string | null
  refusal_basis: list | null
  cited_marks: list | null
  affected_classes: list | null
  affected_items: list | null
response_preparation_input:
  proposed_strategy_note: string | null
  draft_response_document_reference_id: doc_... | null
  evidence_reference_ids: list
  communication_needed: boolean
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
trademark_reference_id is required.
office_action_document_reference_id is required where office action is attached.
office_action_type may be unknown.
idempotency_key is not required for preview.
Permission/Policy context is required.
```

For MVP apply:

```text
apply is not production-enabled in MVP.
apply must return safe NotImplemented or equivalent controlled response.
apply must not mutate state.
apply must not create active Tasks.
apply must not emit Events.
apply must not submit official response.
```

---

# 9. Outputs

Preview output:

```yaml
workflow_id: office-action-response-workflow
workflow_contract_version: v0.1.0
operation: preview
status: preview_ready | missing_required_inputs | blocked | review_required | not_implemented
office_action_preview:
  office_action_type: string
  detected_issue_categories: list
  missing_notice_fields: list
  deadline_present: boolean
  deadline_certified: false
response_preparation_preview:
  possible_response_paths: list
  required_professional_review: true
  required_documents: list
  evidence_gaps: list
  cited_mark_references: list
task_plan:
  planned_tasks: list
communication_preview:
  draft_needed: boolean
  draft_summary: string | null
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
workflow_id: office-action-response-workflow
operation: apply
status: not_implemented
error:
  code: StateInvalid
  message: apply is not production-enabled for this workflow in MVP
  retryable: false
```

---

# 10. Preview Behavior

Preview may:

```text
validate request shape
validate trademark reference
validate office action document reference
check Permission/Policy
identify missing office action fields
summarize notice type
identify possible issue categories
prepare response preparation checklist
prepare document/evidence gap list
prepare task plan preview
prepare communication draft summary
mark HumanReviewRequired
show policy omissions
return safe warnings
```

Preview must not:

```text
mutate Trademark
create Matter
create active Task
create Communication
emit Event
submit official response
certify response deadline
certify legal strategy
certify refusal overcome probability
certify evidence sufficiency
select final attorney/provider
send official instruction
```

---

# 11. Apply Behavior

In MVP, apply is not production-enabled.

Apply must:

```text
return controlled safe not-implemented response
perform no side effects
not create active Tasks
not create Communications
not emit Events
not submit official response
not certify legal conclusions
```

Future apply may coordinate:

```text
Matter Service
Document Service
Evidence Service
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
trademark_reference_id
office_action_document_reference_id
correlation_id
```

## 12.2 Step 2 — Permission / Policy Precheck

Checks:

```text
trademark data access
office action document access
matter access where supplied
evidence access
AI source use policy
cross-organization policy
event trace visibility where referenced
```

## 12.3 Step 3 — Office Action Context Preview

May identify:

```text
office action type
issuing office
issue date presence
deadline presence
affected classes/items
cited marks
formal requirements
substantive refusal categories
missing notice metadata
```

This does not certify official deadline or legal basis.

## 12.4 Step 4 — Response Preparation Preview

May identify:

```text
possible response paths
required documents
required evidence
required arguments
required local attorney/professional review
missing client information
communication needs
```

This does not finalize legal strategy.

## 12.5 Step 5 — Task Plan Preview

May prepare planned tasks:

```text
review office action
confirm deadline with professional
analyze cited marks
collect evidence
prepare response draft
review response draft
prepare client communication
confirm filing instructions
```

Task plan is not active Task in MVP stub.

## 12.6 Step 6 — AI-Assisted Summary

AI may prepare:

```text
plain-language office action summary
issue category guess
missing information checklist
evidence gap list
draft response outline
client question list
```

AI must not:

```text
certify legal basis
certify official deadline
certify success probability
finalize response strategy
submit response
send communication
emit Events
```

## 12.7 Step 7 — Return Safe Preview

Returns:

```text
preview summary
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
trademark:read
trademark:office_action:preview
document:read
evidence:read
matter:read
classification:read
communication:draft
event:read
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
trademark:data:visible
office_action:document:visible
document:metadata:visible
evidence:metadata:visible
matter:data:visible
classification:data:visible
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
office-action-response-previewed
office-action-response-preparation-started
office-action-document-attached
response-draft-created
evidence-attached
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
```

---

# 17. Task Plan Rules

MVP task plan may include:

```yaml
planned_task_type: review_office_action
subject_reference_id: tm_...
required_owner_role: trademark_professional
priority: urgent
human_review_required: true
policy_restrictions: []
source_step: office-action-preview
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
client question list
draft client explanation summary
internal review note outline
foreign associate instruction draft outline
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
office action summary
issue category suggestion
evidence gap summary
response outline
client question list
risk flags
```

Forbidden AI outputs:

```text
final legal argument
official deadline certification
registrability certification
success probability certification
response sufficiency certification
filing instruction approval
official response submission
provider final selection
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
official deadline confirmation
legal basis confirmation
response strategy
evidence sufficiency conclusion
response draft approval
client-facing legal explanation
foreign associate instruction approval
official filing readiness
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
restricted trademark data
office action document contents
restricted evidence content
legal strategy internals
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

Office Action Response Workflow MVP does not implement:

```text
official response submission
official portal integration
deadline calculation certification
legal argument finalization
refusal overcome probability
evidence sufficiency certification
foreign associate final selection
external communication send
payment execution
production task creation
production event emission
full OA management engine
full AI legal response agent
```

---

# 24. Forbidden Shortcuts

Codex must not:

```text
turn preview into production apply
submit official response
certify official deadline
certify legal argument
certify evidence sufficiency
create active Task directly from workflow layer
emit Events directly from workflow layer
send Communication directly from workflow layer
skip Permission/Policy
treat AI output as professional conclusion
treat Human Review record as automatic filing approval
accept unsupported versions silently
return unsafe errors
```

---

# 25. Test Requirements

Required tests:

```text
preview_valid_request_returns_response_preparation_plan
preview_missing_required_inputs_returns_missing_inputs
preview_has_no_side_effects
preview_permission_denied_blocks
preview_policy_restricted_blocks
preview_policy_redacts_output
preview_policy_nondisclosure_returns_notfound
preview_human_review_required
apply_returns_not_implemented_in_mvp
apply_has_no_side_effects_in_mvp
workflow_does_not_emit_events_directly
workflow_does_not_create_active_tasks_directly
workflow_does_not_submit_official_response
ai_summary_is_non_final
ai_deadline_certification_blocked
ai_legal_strategy_certification_blocked
event_reference_is_trace_only
version_unsupported_fails_closed
safe_errors_no_database_id_or_stack_trace
restricted_data_not_leaked
```

---

# 26. Acceptance Criteria

Office Action Response Workflow is accepted only if:

```text
[ ] Workflow purpose is clear.
[ ] Workflow category is Stub Now.
[ ] Related workflow contract exists.
[ ] Preview behavior is side-effect free.
[ ] Apply is not production-enabled in MVP.
[ ] Official response submission is explicitly out of scope.
[ ] Legal strategy certification is explicitly forbidden.
[ ] Deadline certification is explicitly forbidden.
[ ] Evidence sufficiency certification is explicitly forbidden.
[ ] Task plan is not active Task.
[ ] Workflow does not emit Events directly.
[ ] Workflow does not send Communication directly.
[ ] Permission/Policy checks are defined.
[ ] AI output remains draft/suggestion/non-final.
[ ] Human Review gates are preserved.
[ ] Safe Error behavior is defined.
[ ] Versioning behavior is defined.
[ ] Forbidden shortcuts are explicit.
[ ] Required tests are defined.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Office Action Response Workflow. Defines Stub Now preview/validation behavior, future coordination scope, ownership, inputs/outputs, side-effect-free preview, apply disabled in MVP, Permission/Policy, AI/Human Review, Event/Task/Communication boundaries, errors, versioning, out-of-scope, forbidden shortcuts and tests. |

---

**End of Office Action Response Workflow**
