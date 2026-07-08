# Customer Intake Workflow

**Spec ID:** B02-WORKFLOW-CUSTOMER-INTAKE  
**Spec Type:** Workflow Specification  
**Spec File:** core-specs/workflows/customer-intake-workflow.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Workflow Index:** core-specs/workflows/index.md  
**Related Workflow Contract:** core-specs/contracts/workflows/customer-intake-workflow-contract.md  
**Related API Contracts:** customer-api-contract; brand-api-contract; matter-api-contract; order-api-contract; document-api-contract; task-api-contract; communication-api-contract; event-api-contract  
**Related Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Codex Task:** codex-tasks/TASK-008-workflow-validator-scaffold.md; codex-tasks/TASK-010-mvp-execution-spine.md  
**Status:** Draft  
**Version:** 0.1.0  
**Workflow ID:** customer-intake-workflow  
**Workflow Contract Version:** v0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** Level 2/3 — MVP Workflow Validator and Execution Spine  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Customer Intake Workflow defines the first professional intake process in MarkOrbit Core.

It coordinates the creation and preparation of:

```text
Customer
Brand
Matter
Order
Document references
Task plan
Communication draft where applicable
Event trace
```

This workflow proves the first part of the MVP execution spine:

```text
Customer
↓
Brand
↓
Matter / Order
↓
Document
↓
Task
↓
Communication
↓
Event
↓
Permission / Policy
↓
Tests
```

Customer Intake Workflow does not replace professional judgment.

It structures intake, validates required information, prepares next actions, and routes ownership to the correct Core services.

---

# 2. Core Lock

```text
Customer Intake Workflow coordinates intake.
Customer Service owns Customer state.
Brand Service owns Brand state.
Matter Service owns Matter state.
Order Service owns Order state.
Document Service owns Document references.
Task Service creates active Tasks.
Communication Service owns Communication drafts.
Event Service preserves trace.
Workflow preview has no side effects.
Workflow apply requires Idempotency.
Workflow layer does not own domain behavior.
Workflow layer must not create active Tasks directly.
Workflow layer must not emit Events directly.
Workflow layer must not send Communications directly.
Permission and Policy govern protected intake behavior.
AI may summarize or suggest but must not decide or execute.
Human Review gates protected professional or external-facing actions.
Codex implements validators and scoped MVP coordination only.
```

---

# 3. Workflow Position

Customer Intake Workflow is the first workflow in the MVP workflow set.

It is upstream of:

```text
trademark-application-workflow
communication-review-workflow
```

It provides:

```text
customer context
brand context
initial matter context
order context
document references
initial task plan
optional communication draft
```

It does not provide:

```text
final trademark filing readiness
final goods/services classification
official filing submission
external message sending
provider final selection
payment execution
```

---

# 4. Workflow Category

```text
MVP Category: Must Build Now
Implementation Depth: Level 2/3
Execution Mode: Preview + Apply
Production Side Effects: Scoped, service-owned only
External Side Effects: Not allowed in MVP
AI Use: Draft/Summary/Suggestion only
Human Review: Required for protected professional/external-facing actions
```

---

# 5. Related Services

Customer Intake Workflow coordinates these services:

```text
Customer Service
Brand Service
Matter Service
Order Service
Document Service
Task Service
Communication Service
Event Service
Permission Service
Policy Service
```

Optional or future services:

```text
Knowledge Service
Notification Service
Opportunity Service
Routing Service
```

These are not production-required in the MVP intake workflow.

---

# 6. Ownership Rules

| Area | Owner |
|---|---|
| Customer state | Customer Service |
| Brand state | Brand Service |
| Matter state | Matter Service |
| Order state | Order Service |
| Document metadata/reference | Document Service |
| Active Task | Task Service |
| Communication draft/review/send state | Communication Service |
| Event trace | Event Service / owning service integration |
| Permission evaluation | Permission Service |
| Policy evaluation | Policy Service |
| Workflow coordination | Customer Intake Workflow |
| Workflow contract validation | Workflow Contract validator |

Workflow must not claim ownership over service-owned state.

---

# 7. Inputs

Customer Intake Workflow input may include:

```yaml
workflow_id: customer-intake-workflow
workflow_contract_version: v0.1.0
operation: preview | apply
actor_reference_id: usr_...
organization_reference_id: org_...
customer_input:
  customer_name: string
  customer_type: individual | company | agency | unknown
  contact_name: string | null
  contact_email: string | null
  contact_phone: string | null
  country_or_region: string | null
brand_input:
  brand_name: string | null
  brand_language: string | null
  logo_document_reference_id: doc_... | null
  brand_owner_name: string | null
matter_input:
  matter_type: trademark_application | consultation | monitoring | renewal | unknown
  target_jurisdictions: list
  business_description: string | null
  goods_services_description: string | null
order_input:
  requested_service_scope: string | null
  budget_note: string | null
  urgency: normal | urgent | unknown
document_inputs:
  uploaded_document_reference_ids: list
communication_input:
  initial_message: string | null
ai_context:
  optional
human_review_reference_id: string | null
idempotency_key: string | required for apply
correlation_id: string | null
```

---

# 8. Required Input Rules

For preview:

```text
workflow_id is required.
workflow_contract_version is required.
actor_reference_id is required.
organization_reference_id is required.
At least one customer or brand signal is required.
idempotency_key is not required.
```

For apply:

```text
workflow_id is required.
workflow_contract_version is required.
actor_reference_id is required.
organization_reference_id is required.
customer_input.customer_name is required unless existing customer_reference_id is supplied.
brand_input.brand_name or brand_input.logo_document_reference_id is required if creating Brand.
matter_input.matter_type is required.
order_input.requested_service_scope is required if creating Order.
idempotency_key is required.
Permission/Policy context is required.
Human Review may be required depending on policy.
```

---

# 9. Outputs

Preview output:

```yaml
workflow_id: customer-intake-workflow
workflow_contract_version: v0.1.0
operation: preview
status: preview_ready | missing_required_inputs | blocked | review_required
customer_preview:
  create_customer: boolean
  existing_customer_candidates: list
brand_preview:
  create_brand: boolean
  missing_brand_fields: list
matter_preview:
  create_matter: boolean
  matter_type: string
order_preview:
  create_order: boolean
  order_scope_summary: string | null
document_preview:
  accepted_document_references: list
  rejected_document_references: list
task_plan:
  planned_tasks: list
communication_preview:
  draft_needed: boolean
  draft_summary: string | null
ai_output:
  summary: string | null
  suggestions: list
policy:
  restricted_fields_omitted: boolean
  policy_omissions_disclosed: boolean
human_review:
  human_review_required: boolean
warnings: list
errors: list
```

Apply output:

```yaml
workflow_id: customer-intake-workflow
workflow_contract_version: v0.1.0
operation: apply
status: applied | blocked | review_required | failed
customer_reference_id: cus_... | null
brand_reference_id: brd_... | null
matter_reference_id: mat_... | null
order_reference_id: ord_... | null
document_reference_ids: list
task_reference_ids: list
communication_reference_id: com_... | null
event_reference_ids: list
idempotency:
  replayed: boolean
  idempotency_key: string
policy:
  restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean
correlation_id: string | null
```

---

# 10. Preview Behavior

Preview is side-effect free.

Preview may:

```text
validate request shape
validate references
check Permission/Policy where protected
identify missing customer fields
identify missing brand fields
identify missing matter/order fields
prepare task plan
prepare intake summary
prepare optional communication draft summary
identify document reference issues
show HumanReviewRequired
show policy omissions
return warnings
```

Preview must not:

```text
create Customer
create Brand
create Matter
create Order
create Document
create active Task
create Communication
emit Event
send Communication
submit official filing
select provider finally
execute payment
```

---

# 11. Apply Behavior

Apply coordinates service-owned state changes.

Apply may coordinate:

```text
Customer Service creates or updates Customer.
Brand Service creates or updates Brand.
Matter Service creates Matter.
Order Service creates Order.
Document Service validates/attaches document references.
Task Service creates active Tasks.
Communication Service creates draft Communication where needed.
Event Service or owning service integration records trace.
```

Apply must:

```text
require idempotency_key
check Permission/Policy
validate Human Review where required
preserve AI Context where AI-assisted
use safe Errors
preserve workflow_contract_version
return event_reference_ids as trace only
```

Apply must not:

```text
create service-owned objects directly
create active Tasks directly from workflow layer
emit Events directly from workflow layer
send Communications directly
submit official trademark filing
certify filing readiness
certify registrability
certify evidence sufficiency
```

---

# 12. Workflow Steps

## 12.1 Step 1 — Validate Workflow Request

Validates:

```text
workflow_id
workflow_contract_version
operation
actor_reference_id
organization_reference_id
input shape
correlation_id
idempotency_key for apply
```

Failure examples:

```text
ValidationFailed
VersionUnsupported
IdempotencyKeyRequired
```

## 12.2 Step 2 — Permission / Policy Precheck

Checks:

```text
actor may perform customer intake
actor may access organization context
actor may create customer/brand/matter/order
actor may access uploaded document references
policy allows source and output visibility
```

Failure examples:

```text
PermissionDenied
PolicyRestricted
HumanReviewRequired
NotFound for non-disclosure
```

## 12.3 Step 3 — Customer Intake Assessment

Coordinates Customer Service.

Determines:

```text
new customer
existing customer candidate
missing customer fields
customer duplicate risk
customer data visibility restrictions
```

## 12.4 Step 4 — Brand Intake Assessment

Coordinates Brand Service.

Determines:

```text
brand name availability within customer context
logo document reference validity
brand owner fields
missing brand fields
brand language notes
```

This does not determine legal registrability.

## 12.5 Step 5 — Matter / Order Preparation

Coordinates Matter Service and Order Service.

Determines:

```text
matter type
target jurisdictions
initial professional context
requested service scope
initial order draft
commercial scope summary
```

This does not execute payment.

## 12.6 Step 6 — Document Reference Validation

Coordinates Document Service.

Validates:

```text
uploaded document references
logo document references
identity/company document references where applicable
policy visibility
document type hints
```

This does not validate official sufficiency.

## 12.7 Step 7 — Task Plan Preparation

Prepares task plan.

Possible planned tasks:

```text
complete customer information
confirm brand owner
confirm target jurisdiction
collect logo file
collect applicant identity/company document
collect goods/services description
prepare trademark application workflow
prepare communication review
```

Task plan is not active Task.

Active Tasks are created only by Task Service during apply.

## 12.8 Step 8 — Communication Draft Preparation

Coordinates Communication Service only if needed.

Possible draft types:

```text
missing-information-request
intake-confirmation-draft
internal-review-note
```

Draft is not sent externally.

External send requires Communication Review Workflow and Human Review where required.

## 12.9 Step 9 — AI-Assisted Summary

AI may prepare:

```text
intake summary
missing information list
suggested next questions
risk flags
task plan suggestion
communication draft suggestion
```

AI must not:

```text
approve intake
certify customer data
certify filing readiness
finalize jurisdiction choice
finalize classification
send communication
create active Tasks
emit Events
```

## 12.10 Step 10 — Apply Through Owning Services

On apply, workflow coordinates service calls.

Expected service-owned effects:

```text
Customer created/updated
Brand created/updated
Matter created
Order created
Document references attached
Task Service creates active Tasks
Communication Service creates draft Communication if required
Event trace recorded
```

## 12.11 Step 11 — Return Safe Result

Returns:

```text
created references
task references
communication draft reference
event references
policy redaction status
human review status
idempotency replay status
safe warnings/errors
```

---

# 13. Permission Requirements

Required permissions may include:

```text
customer:intake
customer:create
customer:read
brand:create
brand:read
matter:create
order:create
document:read
document:attach
task:create
communication:draft
event:read
```

Rules:

```text
PermissionDenied blocks protected action.
UnknownPermission fails closed.
MissingPermissionContext fails closed.
PermissionAllowed does not bypass Policy.
```

---

# 14. Policy Requirements

Required policy scopes may include:

```text
customer:data:visible
brand:data:visible
matter:data:visible
order:data:visible
document:metadata:visible
communication:draft:visible
event:trace:visible
cross_organization:allowed
ai_source:allowed
```

Policy outcomes:

```text
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
PolicyNonDisclosureNotFound
UnknownPolicy
MissingPolicyContext
```

Rules:

```text
PolicyRestrictedBlock blocks workflow step.
PolicyRestrictedRedact redacts output and sets restricted_fields_omitted.
PolicyRequiresHumanReview returns HumanReviewRequired unless valid review exists.
PolicyNonDisclosureNotFound hides object/source existence.
UnknownPolicy fails closed where policy-controlled.
```

---

# 15. Idempotency

Apply must require idempotency.

Rules:

```text
idempotency_key is required for apply.
Same key + same semantic request replays safely.
Same key + different semantic request returns IdempotencyConflict.
Replay creates no duplicate Customer.
Replay creates no duplicate Brand.
Replay creates no duplicate Matter.
Replay creates no duplicate Order.
Replay creates no duplicate active Task.
Replay creates no duplicate Communication.
Replay creates no duplicate Event.
Replay does not leak policy-hidden prior result.
```

Semantic request includes:

```text
workflow_id
operation
actor_reference_id
organization_reference_id
normalized customer_input
normalized brand_input
normalized matter_input
normalized order_input
normalized document_inputs
workflow_contract_version
```

---

# 16. Event Trace

Expected event types may include:

```text
customer-intake-previewed
customer-intake-applied
customer-created
brand-created
matter-created
order-created
document-attached
task-created
communication-draft-created
policy-evaluated
permission-evaluated
```

Rules:

```text
Workflow does not emit Events directly.
Owning services or Event Service integration record Events.
event_reference_ids are trace only.
event_reference_ids are not commands.
Event visibility follows Permission/Policy.
Event payloads must not leak restricted intake data.
```

---

# 17. Task Plan and Active Task Rules

Task plan may include:

```yaml
planned_task_type: collect_missing_information
subject_reference_id: cus_...
required_owner_role: intake_operator
priority: normal
human_review_required: false
policy_restrictions: []
source_step: customer-intake
```

Rules:

```text
Task plan is not active Task.
Task plan does not create work by itself.
Task Service creates active Tasks during apply.
Agent suggestions cannot become active Tasks directly.
Workflow layer cannot create active Tasks directly.
```

---

# 18. Communication Rules

Communication draft may be created for:

```text
missing customer information
intake confirmation
internal handoff
next-step explanation
```

Rules:

```text
Communication Service owns Communication draft.
Workflow does not send Communication.
AI draft is marked draft/suggestion.
External send requires Communication Review Workflow.
External send requires Human Review where protected.
Communication content follows Policy redaction.
```

---

# 19. AI Context

AI assistance is optional.

Allowed AI outputs:

```text
intake summary
missing information list
suggested next questions
draft communication text
task plan suggestion
risk flags
```

Forbidden AI outputs:

```text
final legal advice
final classification
filing readiness certification
registrability certification
deadline certification
customer approval
external send approval
automatic state mutation
event emission
```

AI output must include:

```text
ai_assisted = true
capability_scope
source_scope
policy_omissions_disclosed where applicable
human_review_required where applicable
draft/suggestion/non-final marker
```

---

# 20. Human Review

Human Review may be required for:

```text
cross-organization customer intake
restricted customer data access
external-facing communication draft approval
professional intake confirmation
filing readiness transition
```

Rules:

```text
Human Review does not execute downstream action by itself.
Human Review does not bypass Permission.
Human Review does not bypass Policy.
Owning service determines whether review satisfies gate.
```

---

# 21. Error Handling

Customer Intake Workflow uses Error Contract.

Required controlled errors:

```text
ValidationFailed
ReferenceInvalid
PermissionDenied
PolicyRestricted
HumanReviewRequired
IdempotencyKeyRequired
IdempotencyConflict
VersionUnsupported
StateInvalid
NotFound
Conflict
InternalError
```

Errors must not expose:

```text
database IDs
restricted customer data
restricted document metadata
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
Historical workflow application version is preserved.
Event records preserve version context.
Idempotency fingerprint includes workflow_contract_version.
```

---

# 23. Out of Scope

Customer Intake Workflow does not implement:

```text
official trademark filing
final jurisdiction recommendation
final goods/services classification
final registrability assessment
official deadline certification
payment execution
provider final selection
external communication send
full CRM lifecycle
full opportunity management
full notification delivery
full workflow engine
full AI agent runtime
```

---

# 24. Forbidden Shortcuts

Codex must not:

```text
create Customer directly from workflow layer
create Brand directly from workflow layer
create Matter directly from workflow layer
create Order directly from workflow layer
create active Task directly from workflow layer
emit Events directly from workflow layer
send Communication directly from workflow layer
skip Permission/Policy
skip Idempotency for apply
treat AI output as Human Review
treat preview as apply
accept unsupported versions silently
return unsafe errors
```

---

# 25. Test Requirements

Required tests:

```text
preview_valid_request_returns_plan
preview_missing_required_inputs_returns_missing_inputs
preview_has_no_side_effects
apply_requires_idempotency_key
apply_same_key_same_request_replays_safely
apply_same_key_different_request_conflicts
apply_permission_denied_blocks
apply_policy_restricted_blocks
apply_policy_redacts_output
apply_policy_nondisclosure_returns_notfound
apply_human_review_required
apply_creates_active_tasks_only_through_task_service
workflow_does_not_emit_events_directly
workflow_does_not_send_communication_directly
ai_output_is_non_final
ai_forbidden_action_blocked
event_reference_is_trace_only
version_unsupported_fails_closed
safe_errors_no_database_id_or_stack_trace
restricted_data_not_leaked
```

---

# 26. Acceptance Criteria

Customer Intake Workflow is accepted only if:

```text
[ ] Workflow purpose is clear.
[ ] Workflow category is Must Build Now.
[ ] Related workflow contract exists.
[ ] Preview behavior is side-effect free.
[ ] Apply behavior requires Idempotency.
[ ] Owning service boundaries are preserved.
[ ] Task plan is not active Task.
[ ] Active Tasks are created only through Task Service.
[ ] Communication draft is owned by Communication Service.
[ ] Workflow does not send Communication.
[ ] Workflow does not emit Events directly.
[ ] Permission/Policy checks are defined.
[ ] AI output remains draft/suggestion/non-final.
[ ] Human Review gates are preserved.
[ ] Safe Error behavior is defined.
[ ] Versioning behavior is defined.
[ ] Out-of-scope items are explicit.
[ ] Forbidden shortcuts are explicit.
[ ] Required tests are defined.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Customer Intake Workflow. Defines MVP intake coordination, inputs/outputs, preview/apply behavior, service ownership, Permission/Policy, Idempotency, Event trace, Task/Communication/AI/Human Review rules, errors, versioning, out-of-scope, forbidden shortcuts and tests. |

---

**End of Customer Intake Workflow**
