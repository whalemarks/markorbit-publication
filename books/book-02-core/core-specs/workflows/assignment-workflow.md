# Assignment Workflow

**Spec ID:** B02-WORKFLOW-ASSIGNMENT  
**Spec Type:** Workflow Specification  
**Spec File:** core-specs/workflows/assignment-workflow.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Workflow Index:** core-specs/workflows/index.md  
**Related Workflow Contract:** core-specs/contracts/workflows/assignment-workflow-contract.md  
**Related API Contracts:** trademark-api-contract; document-api-contract; evidence-api-contract; matter-api-contract; order-api-contract; task-api-contract; communication-api-contract; event-api-contract  
**Related Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Codex Task:** codex-tasks/TASK-008-workflow-validator-scaffold.md  
**Status:** Draft  
**Version:** 0.1.0  
**Workflow ID:** assignment-workflow  
**Workflow Contract Version:** v0.1.0  
**MVP Category:** Stub Now  
**Implementation Depth:** Level 1/2 — Preview / Validation Stub  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Assignment Workflow defines the future professional workflow for preparing trademark assignment, transfer, owner-change and recordal matters.

It may help identify assignment parties, required documents, signature/legalization requirements, affected trademark records, task plans and communication needs.

In MVP, this workflow is a safe stub.

It must not record assignments with official offices, certify legal effect, execute ownership changes, send external communications or create production official filing actions.

---

# 2. Core Lock

```text
Assignment Workflow coordinates assignment preparation.
It is Stub Now in MVP.
Workflow preview has no side effects.
Workflow apply is not production-enabled in MVP.
Trademark Service owns Trademark state.
Document Service owns assignment document references.
Evidence Service owns supporting evidence references.
Matter Service owns Matter state.
Order Service owns Order state.
Task Service creates active Tasks only when explicitly allowed by MVP scope.
Communication Service owns Communication drafts.
Event Service preserves trace.
Workflow layer must not record assignments officially.
Workflow layer must not mutate trademark owner state in MVP.
Workflow layer must not certify legal effect.
AI may summarize assignment gaps but must not define professional truth.
Human Review gates ownership, legal-effect and filing-readiness conclusions.
Codex implements validation and preview-only boundaries only.
```

---

# 3. Workflow Position

Assignment Workflow may be used after one or more trademark records exist.

It may involve:

```text
trademark record
current owner
new owner
assignment agreement
POA or authorization document
company identity documents
signature/legalization requirements
supporting evidence
recordal jurisdiction
recordal fee/order scope
client communication
provider routing
```

In MVP, it is not part of the executable spine.

It exists to preserve future post-registration and ownership-change architecture.

---

# 4. Workflow Category

```text
MVP Category: Stub Now
Implementation Depth: Level 1/2
Execution Mode: Preview / Validation Stub
Apply Behavior: Not production-enabled in MVP
Official Assignment Recordal: Not allowed in MVP
Ownership Mutation: Not allowed in MVP
External Side Effects: Not allowed in MVP
AI Use: Summary / gap suggestion / draft only
Human Review: Required for ownership and legal-effect conclusions
```

---

# 5. Related Services

Future full workflow may coordinate:

```text
Trademark Service
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
safe assignment preview
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
| Trademark state | Trademark Service |
| Trademark owner state | Trademark Service |
| Assignment document reference | Document Service |
| Supporting evidence reference | Evidence Service |
| Matter state | Matter Service |
| Order/commercial scope | Order Service |
| Active Task | Task Service |
| Communication draft/send state | Communication Service |
| Event trace | Event Service / owning service integration |
| Permission evaluation | Permission Service |
| Policy evaluation | Policy Service |
| Workflow coordination | Assignment Workflow |

Workflow must not own trademark owner state or official assignment recordal behavior.

---

# 7. Inputs

```yaml
workflow_id: assignment-workflow
workflow_contract_version: v0.1.0
operation: preview | apply
actor_reference_id: usr_...
organization_reference_id: org_...
trademark_reference_ids: list
matter_reference_id: mat_... | null
order_reference_id: ord_... | null
assignment_input:
  current_owner_name: string | null
  new_owner_name: string | null
  assignment_type: full_assignment | partial_assignment | merger | name_change | address_change | unknown
  effective_date: string | null
  target_jurisdiction: string | null
  affected_classes: list | null
  affected_goods_services: list | null
document_inputs:
  assignment_agreement_document_reference_id: doc_... | null
  poa_document_reference_id: doc_... | null
  company_document_reference_ids: list
  uploaded_document_reference_ids: list
evidence_inputs:
  evidence_reference_ids: list
communication_input:
  client_confirmation_needed: boolean
  provider_instruction_needed: boolean
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
At least one trademark_reference_id is required.
assignment_type is required or may be unknown with missing-input warning.
current_owner_name and new_owner_name are recommended but not certified.
target_jurisdiction is required unless derived from trademark reference.
Permission/Policy context is required.
idempotency_key is not required for preview.
```

For MVP apply:

```text
apply is not production-enabled in MVP.
apply must return safe NotImplemented or equivalent controlled response.
apply must not mutate trademark owner state.
apply must not create active Tasks.
apply must not create Communication.
apply must not emit Events.
apply must not file assignment recordal.
apply must not certify legal effect.
```

---

# 9. Outputs

Preview output:

```yaml
workflow_id: assignment-workflow
workflow_contract_version: v0.1.0
operation: preview
status: preview_ready | missing_required_inputs | blocked | review_required | not_implemented
assignment_preview:
  trademark_reference_ids: list
  assignment_type: string
  target_jurisdiction: string | null
  ownership_change_certified: false
  legal_effect_certified: false
  recordal_readiness_certified: false
  missing_assignment_fields: list
document_preview:
  accepted_document_references: list
  missing_documents: list
  legalization_or_notarization_review_required: boolean
evidence_preview:
  accepted_evidence_references: list
  missing_evidence_items: list
task_plan:
  planned_tasks: list
communication_preview:
  client_confirmation_draft_needed: boolean
  provider_instruction_draft_needed: boolean
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
workflow_id: assignment-workflow
operation: apply
status: not_implemented
error:
  code: StateInvalid
  message: apply is not production-enabled for assignment workflow in MVP
  retryable: false
```

---

# 10. Preview Behavior

Preview may:

```text
validate request shape
validate trademark references
validate document references
validate evidence references
check Permission/Policy
identify missing assignment party fields
identify missing document fields
identify notarization/legalization review needs
prepare assignment readiness checklist
prepare client confirmation draft summary
prepare provider instruction draft summary
prepare task plan preview
mark HumanReviewRequired
show policy omissions
return safe warnings
```

Preview must not:

```text
mutate Trademark owner
create Matter
create Order
create active Task
create Communication
emit Event
file assignment recordal
certify legal effect
certify ownership change
certify signature validity
certify notarization/legalization sufficiency
send client/provider communication
engage provider
```

---

# 11. Apply Behavior

In MVP, apply is not production-enabled.

Apply must:

```text
return controlled safe not-implemented response
perform no side effects
not mutate Trademark owner state
not create active Tasks
not create Communications
not emit Events
not file assignment recordal
not certify legal effect
```

Future apply may coordinate:

```text
Trademark Service
Matter Service
Order Service
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
trademark_reference_ids
target_jurisdiction
correlation_id
```

## 12.2 Step 2 — Permission / Policy Precheck

Checks:

```text
trademark data access
assignment preview permission
owner data visibility
document/evidence access
matter/order access where supplied
AI source use policy
cross-organization policy
event trace visibility where referenced
```

## 12.3 Step 3 — Assignment Context Preview

May identify:

```text
current owner presence
new owner presence
assignment type
affected trademarks
affected classes/items
jurisdiction-specific recordal requirements
party data gaps
commercial scope gaps
```

This does not certify legal effect or official recordability.

## 12.4 Step 4 — Document and Evidence Gap Preview

May identify:

```text
assignment agreement requirement
POA requirement
company document requirement
signature requirement
notarization requirement
legalization requirement
translation requirement
supporting evidence requirement
```

This does not certify sufficiency.

## 12.5 Step 5 — Task Plan Preview

May prepare planned tasks:

```text
confirm assignment parties
confirm affected trademarks
collect assignment agreement
collect POA
collect company documents
review notarization/legalization
prepare client confirmation
prepare provider instruction
review recordal readiness
```

Task plan is not active Task in MVP stub.

## 12.6 Step 6 — Communication Preview

May prepare:

```text
client confirmation outline
missing document request outline
provider instruction outline
internal assignment review note
```

No communication is created or sent in MVP stub unless separately coordinated through Communication Service in a later phase.

## 12.7 Step 7 — AI-Assisted Assignment Summary

AI may prepare:

```text
assignment gap summary
document checklist
party information checklist
client question list
provider instruction outline
risk flags
```

AI must not:

```text
certify ownership change
certify legal effect
certify signature validity
certify official recordability
approve assignment
file recordal
send communication
emit Events
```

## 12.8 Step 8 — Return Safe Preview

Returns:

```text
assignment preview
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
trademark:assignment:preview
document:read
evidence:read
matter:read
order:read
communication:draft
event:read
```

Future apply may require:

```text
trademark:assignment:prepare
trademark:assignment:file
trademark:owner:update
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
trademark:data:visible
owner:data:visible
assignment:data:visible
document:metadata:visible
evidence:metadata:visible
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
no duplicate assignment recordal instruction
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
assignment-previewed
assignment-preparation-started
assignment-document-attached
assignment-evidence-attached
assignment-instruction-draft-created
trademark-owner-updated
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
Ownership and party data must not leak through restricted Event payload.
```

---

# 17. Task Plan Rules

MVP task plan may include:

```yaml
planned_task_type: collect_assignment_documents
subject_reference_id: tm_...
required_owner_role: trademark_professional
priority: normal
human_review_required: true
policy_restrictions: []
source_step: assignment-preview
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
client assignment confirmation outline
client missing document request outline
provider assignment instruction outline
internal assignment review note
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
assignment gap summary
document checklist
party information checklist
notarization/legalization issue list
client question list
risk flags
```

Forbidden AI outputs:

```text
ownership change certification
legal effect certification
recordal readiness certification
signature validity certification
notarization/legalization sufficiency certification
assignment approval
official recordal filing
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
assignment party confirmation
ownership change conclusion
legal effect conclusion
document sufficiency conclusion
notarization/legalization conclusion
recordal readiness confirmation
client-facing assignment explanation
provider assignment instruction approval
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
restricted owner data
assignment agreement contents
restricted evidence content
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

Assignment Workflow MVP does not implement:

```text
official assignment recordal
trademark owner mutation
legal effect certification
recordal readiness certification
signature validity certification
notarization/legalization sufficiency certification
payment execution
provider final selection
external communication send
production task creation
production event emission
official portal integration
full assignment management engine
full AI assignment agent
```

---

# 24. Forbidden Shortcuts

Codex must not:

```text
turn preview into production apply
file assignment recordal
mutate trademark owner state
certify ownership change
certify legal effect
certify document sufficiency
certify signature validity
certify notarization/legalization sufficiency
create active Task directly from workflow layer
emit Events directly from workflow layer
send Communication directly from workflow layer
skip Permission/Policy
treat AI output as professional conclusion
treat Human Review record as automatic recordal approval
accept unsupported versions silently
return unsafe errors
```

---

# 25. Test Requirements

Required tests:

```text
preview_valid_request_returns_assignment_preparation_plan
preview_missing_required_inputs_returns_missing_inputs
preview_has_no_side_effects
preview_permission_denied_blocks
preview_policy_restricted_blocks
preview_policy_redacts_output
preview_policy_nondisclosure_returns_notfound
preview_human_review_required_for_ownership_conclusion
apply_returns_not_implemented_in_mvp
apply_has_no_side_effects_in_mvp
workflow_does_not_emit_events_directly
workflow_does_not_create_active_tasks_directly
workflow_does_not_mutate_trademark_owner
workflow_does_not_file_assignment_recordal
ai_ownership_certification_blocked
ai_legal_effect_certification_blocked
event_reference_is_trace_only
version_unsupported_fails_closed
safe_errors_no_database_id_or_stack_trace
restricted_owner_data_not_leaked
```

---

# 26. Acceptance Criteria

Assignment Workflow is accepted only if:

```text
[ ] Workflow purpose is clear.
[ ] Workflow category is Stub Now.
[ ] Related workflow contract exists.
[ ] Preview behavior is side-effect free.
[ ] Apply is not production-enabled in MVP.
[ ] Official assignment recordal is explicitly out of scope.
[ ] Trademark owner mutation is explicitly forbidden in MVP.
[ ] Legal effect certification is explicitly forbidden.
[ ] Document/signature/legalization sufficiency certification is explicitly forbidden.
[ ] Task plan is not active Task.
[ ] Workflow does not emit Events directly.
[ ] Workflow does not send Communication directly.
[ ] Permission/Policy checks are defined.
[ ] AI output remains draft/suggestion/non-final.
[ ] Human Review gates assignment professional conclusions.
[ ] Safe Error behavior is defined.
[ ] Versioning behavior is defined.
[ ] Forbidden shortcuts are explicit.
[ ] Required tests are defined.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Assignment Workflow. Defines Stub Now assignment preview/validation behavior, future coordination scope, ownership, inputs/outputs, side-effect-free preview, apply disabled in MVP, owner mutation/recordal/legal-effect boundaries, Permission/Policy, AI/Human Review, Event/Task/Communication boundaries, errors, versioning, out-of-scope, forbidden shortcuts and tests. |

---

**End of Assignment Workflow**
