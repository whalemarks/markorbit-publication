# Renewal Workflow

**Spec ID:** B02-WORKFLOW-RENEWAL  
**Spec Type:** Workflow Specification  
**Spec File:** core-specs/workflows/renewal-workflow.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Workflow Index:** core-specs/workflows/index.md  
**Related Workflow Contract:** core-specs/contracts/workflows/renewal-workflow-contract.md  
**Related API Contracts:** trademark-api-contract; jurisdiction-api-contract; document-api-contract; evidence-api-contract; matter-api-contract; order-api-contract; task-api-contract; communication-api-contract; event-api-contract  
**Related Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Codex Task:** codex-tasks/TASK-008-workflow-validator-scaffold.md  
**Status:** Draft  
**Version:** 0.1.0  
**Workflow ID:** renewal-workflow  
**Workflow Contract Version:** v0.1.0  
**MVP Category:** Stub Now  
**Implementation Depth:** Level 1/2 — Preview / Validation Stub  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Renewal Workflow defines the future professional workflow for preparing trademark renewal matters.

It may help identify renewal windows, required documents, required evidence, missing owner/applicant data, task plans and client communication needs.

In MVP, this workflow is a safe stub.

It must not file renewals, certify official deadlines, execute payments, send external communications or create production official filing actions.

---

# 2. Core Lock

```text
Renewal Workflow coordinates renewal preparation.
It is Stub Now in MVP.
Workflow preview has no side effects.
Workflow apply is not production-enabled in MVP.
Trademark Service owns Trademark state.
Jurisdiction Service owns jurisdiction reference behavior.
Document Service owns renewal document references.
Evidence Service owns evidence references.
Matter Service owns Matter state.
Order Service owns Order state.
Task Service creates active Tasks only when explicitly allowed by MVP scope.
Communication Service owns Communication drafts.
Event Service preserves trace.
Workflow layer must not file renewals.
Workflow layer must not certify official deadlines.
Workflow layer must not execute payments.
AI may summarize renewal gaps but must not define professional truth.
Human Review gates renewal readiness and deadline confirmation.
Codex implements validation and preview-only boundaries only.
```

---

# 3. Workflow Position

Renewal Workflow may be used after a trademark record exists.

It may involve:

```text
registered trademark record
registration date
expiry date
renewal window
grace period
owner/applicant information
use evidence where applicable
POA or authorization document
renewal fee/order scope
client communication
provider routing
```

In MVP, it is not part of the executable spine.

It exists to preserve future lifecycle-management architecture.

---

# 4. Workflow Category

```text
MVP Category: Stub Now
Implementation Depth: Level 1/2
Execution Mode: Preview / Validation Stub
Apply Behavior: Not production-enabled in MVP
Official Renewal Filing: Not allowed in MVP
Payment Execution: Not allowed in MVP
External Side Effects: Not allowed in MVP
AI Use: Summary / gap suggestion / draft only
Human Review: Required for deadline and renewal readiness conclusions
```

---

# 5. Related Services

Future full workflow may coordinate:

```text
Trademark Service
Jurisdiction Service
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
Notification Service
```

MVP stub may only require:

```text
reference validation
Permission/Policy validation
safe renewal preview
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
| Trademark lifecycle state | Trademark Service |
| Jurisdiction renewal reference behavior | Jurisdiction Service |
| Renewal document reference | Document Service |
| Use evidence reference | Evidence Service |
| Matter state | Matter Service |
| Order/commercial scope | Order Service |
| Active Task | Task Service |
| Communication draft/send state | Communication Service |
| Event trace | Event Service / owning service integration |
| Permission evaluation | Permission Service |
| Policy evaluation | Policy Service |
| Workflow coordination | Renewal Workflow |

Workflow must not own trademark lifecycle state or official renewal filing behavior.

---

# 7. Inputs

```yaml
workflow_id: renewal-workflow
workflow_contract_version: v0.1.0
operation: preview | apply
actor_reference_id: usr_...
organization_reference_id: org_...
trademark_reference_id: tm_...
matter_reference_id: mat_... | null
order_reference_id: ord_... | null
renewal_input:
  registration_number: string | null
  registration_date: string | null
  expiry_date: string | null
  jurisdiction: string | null
  owner_name: string | null
  renewal_window_start: string | null
  renewal_deadline: string | null
  grace_period_deadline: string | null
  use_evidence_required: boolean | null
document_inputs:
  uploaded_document_reference_ids: list
evidence_inputs:
  evidence_reference_ids: list
communication_input:
  client_reminder_needed: boolean
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
trademark_reference_id is required.
jurisdiction or trademark jurisdiction reference is required.
expiry_date or renewal deadline signal is recommended but not certified.
Permission/Policy context is required.
idempotency_key is not required for preview.
```

For MVP apply:

```text
apply is not production-enabled in MVP.
apply must return safe NotImplemented or equivalent controlled response.
apply must not mutate state.
apply must not create active Tasks.
apply must not create Communication.
apply must not emit Events.
apply must not file renewal.
apply must not execute payment.
apply must not certify deadline.
```

---

# 9. Outputs

Preview output:

```yaml
workflow_id: renewal-workflow
workflow_contract_version: v0.1.0
operation: preview
status: preview_ready | missing_required_inputs | blocked | review_required | not_implemented
renewal_preview:
  trademark_reference_id: tm_...
  jurisdiction: string | null
  renewal_window_present: boolean
  deadline_present: boolean
  deadline_certified: false
  grace_period_present: boolean
  renewal_readiness_certified: false
  missing_renewal_fields: list
document_preview:
  accepted_document_references: list
  missing_documents: list
evidence_preview:
  accepted_evidence_references: list
  missing_evidence_items: list
task_plan:
  planned_tasks: list
communication_preview:
  client_reminder_draft_needed: boolean
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
workflow_id: renewal-workflow
operation: apply
status: not_implemented
error:
  code: StateInvalid
  message: apply is not production-enabled for renewal workflow in MVP
  retryable: false
```

---

# 10. Preview Behavior

Preview may:

```text
validate request shape
validate trademark reference
validate jurisdiction reference
check Permission/Policy
identify missing renewal fields
identify document gaps
identify evidence gaps
prepare renewal readiness checklist
prepare client reminder draft summary
prepare provider instruction draft summary
prepare task plan preview
mark HumanReviewRequired
show policy omissions
return safe warnings
```

Preview must not:

```text
mutate Trademark
create Matter
create Order
create active Task
create Communication
emit Event
file renewal
execute payment
certify renewal deadline
certify grace period deadline
certify renewal readiness
send reminder
engage provider
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
not file renewal
not execute payment
not certify deadlines
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
trademark_reference_id
jurisdiction
correlation_id
```

## 12.2 Step 2 — Permission / Policy Precheck

Checks:

```text
trademark data access
renewal preview permission
document/evidence access
matter/order access where supplied
AI source use policy
cross-organization policy
event trace visibility where referenced
```

## 12.3 Step 3 — Renewal Context Preview

May identify:

```text
registration number
registration date
expiry date presence
renewal window presence
grace period presence
jurisdiction-specific requirements
owner data gaps
commercial scope gaps
```

This does not certify deadline or renewal eligibility.

## 12.4 Step 4 — Document and Evidence Gap Preview

May identify:

```text
POA or authorization document need
owner identity/company document need
use evidence need
certificate copy need
translation/legalization need
provider-specific document requirement
```

This does not certify official sufficiency.

## 12.5 Step 5 — Task Plan Preview

May prepare planned tasks:

```text
verify renewal deadline
confirm owner information
collect renewal documents
collect use evidence
confirm renewal instruction
prepare client reminder
prepare provider instruction
review renewal readiness
```

Task plan is not active Task in MVP stub.

## 12.6 Step 6 — Communication Preview

May prepare:

```text
client renewal reminder outline
missing document request outline
provider renewal instruction outline
internal renewal review note
```

No communication is created or sent in MVP stub unless separately coordinated through Communication Service in a later phase.

## 12.7 Step 7 — AI-Assisted Renewal Summary

AI may prepare:

```text
renewal gap summary
document checklist
client reminder draft outline
provider instruction draft outline
risk flags
```

AI must not:

```text
certify deadline
certify renewal eligibility
certify use evidence sufficiency
file renewal
approve payment
send reminder
emit Events
```

## 12.8 Step 8 — Return Safe Preview

Returns:

```text
renewal preview
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
trademark:renewal:preview
document:read
evidence:read
matter:read
order:read
communication:draft
event:read
```

Future apply may require:

```text
trademark:renewal:prepare
trademark:renewal:file
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
renewal:data:visible
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
no duplicate renewal filing instruction
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
renewal-previewed
renewal-preparation-started
renewal-document-attached
renewal-evidence-attached
renewal-instruction-draft-created
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
Renewal deadline data must not leak through restricted Event payload.
```

---

# 17. Task Plan Rules

MVP task plan may include:

```yaml
planned_task_type: verify_renewal_deadline
subject_reference_id: tm_...
required_owner_role: trademark_professional
priority: urgent
human_review_required: true
policy_restrictions: []
source_step: renewal-preview
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
client renewal reminder outline
client missing document request outline
provider renewal instruction outline
internal renewal review note
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
renewal gap summary
renewal checklist
client reminder outline
document/evidence gap list
risk flags
```

Forbidden AI outputs:

```text
deadline certification
grace period certification
renewal eligibility certification
use evidence sufficiency certification
official renewal instruction approval
payment approval
external reminder send
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
renewal deadline confirmation
grace period confirmation
renewal eligibility conclusion
use evidence sufficiency conclusion
client-facing renewal reminder approval
provider renewal instruction approval
payment/fee confirmation where future scoped
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
renewal deadline assumptions
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

Renewal Workflow MVP does not implement:

```text
official renewal filing
deadline certification
grace period certification
renewal eligibility certification
use evidence sufficiency certification
payment execution
provider final selection
external communication send
production task creation
production event emission
official portal integration
full renewal docketing engine
full notification delivery
full AI renewal agent
```

---

# 24. Forbidden Shortcuts

Codex must not:

```text
turn preview into production apply
file renewal
certify renewal deadline
certify grace period deadline
certify renewal eligibility
certify evidence sufficiency
execute payment
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
preview_valid_request_returns_renewal_preparation_plan
preview_missing_required_inputs_returns_missing_inputs
preview_has_no_side_effects
preview_permission_denied_blocks
preview_policy_restricted_blocks
preview_policy_redacts_output
preview_policy_nondisclosure_returns_notfound
preview_human_review_required_for_deadline_confirmation
apply_returns_not_implemented_in_mvp
apply_has_no_side_effects_in_mvp
workflow_does_not_emit_events_directly
workflow_does_not_create_active_tasks_directly
workflow_does_not_file_renewal
workflow_does_not_execute_payment
ai_deadline_certification_blocked
ai_renewal_eligibility_certification_blocked
event_reference_is_trace_only
version_unsupported_fails_closed
safe_errors_no_database_id_or_stack_trace
restricted_data_not_leaked
```

---

# 26. Acceptance Criteria

Renewal Workflow is accepted only if:

```text
[ ] Workflow purpose is clear.
[ ] Workflow category is Stub Now.
[ ] Related workflow contract exists.
[ ] Preview behavior is side-effect free.
[ ] Apply is not production-enabled in MVP.
[ ] Official renewal filing is explicitly out of scope.
[ ] Deadline certification is explicitly forbidden.
[ ] Payment execution is explicitly forbidden.
[ ] Evidence sufficiency certification is explicitly forbidden.
[ ] Task plan is not active Task.
[ ] Workflow does not emit Events directly.
[ ] Workflow does not send Communication directly.
[ ] Permission/Policy checks are defined.
[ ] AI output remains draft/suggestion/non-final.
[ ] Human Review gates renewal professional conclusions.
[ ] Safe Error behavior is defined.
[ ] Versioning behavior is defined.
[ ] Forbidden shortcuts are explicit.
[ ] Required tests are defined.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Renewal Workflow. Defines Stub Now renewal preview/validation behavior, future coordination scope, ownership, inputs/outputs, side-effect-free preview, apply disabled in MVP, deadline/payment/filing boundaries, Permission/Policy, AI/Human Review, Event/Task/Communication boundaries, errors, versioning, out-of-scope, forbidden shortcuts and tests. |

---

**End of Renewal Workflow**
