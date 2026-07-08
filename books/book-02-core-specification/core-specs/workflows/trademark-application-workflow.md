# Trademark Application Workflow

**Spec ID:** B02-WORKFLOW-TRADEMARK-APPLICATION  
**Spec Type:** Workflow Specification  
**Spec File:** core-specs/workflows/trademark-application-workflow.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Workflow Index:** core-specs/workflows/index.md  
**Related Workflow Contract:** core-specs/contracts/workflows/trademark-application-workflow-contract.md  
**Related API Contracts:** trademark-api-contract; brand-api-contract; jurisdiction-api-contract; classification-api-contract; document-api-contract; evidence-api-contract; matter-api-contract; order-api-contract; task-api-contract; event-api-contract  
**Related Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Codex Task:** codex-tasks/TASK-008-workflow-validator-scaffold.md; codex-tasks/TASK-010-mvp-execution-spine.md  
**Status:** Draft  
**Version:** 0.1.0  
**Workflow ID:** trademark-application-workflow  
**Workflow Contract Version:** v0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** Level 2/3 — MVP Workflow Validator and Execution Spine  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Trademark Application Workflow defines the MVP professional preparation workflow for a trademark application matter.

It coordinates:

```text
Trademark record preparation
Brand context
Jurisdiction selection context
Classification preparation
Document references
Evidence references
Matter and Order context
Task plan
Event trace
Permission / Policy governance
AI-assisted suggestions
Human Review gates
```

This workflow does not submit official applications.

It prepares a governed application workspace and the next professional tasks required before official filing.

---

# 2. Core Lock

```text
Trademark Application Workflow coordinates application preparation.
Trademark Service owns Trademark state.
Brand Service owns Brand state.
Jurisdiction Service owns Jurisdiction reference behavior.
Classification Service owns Classification behavior.
Document Service owns Document references.
Evidence Service owns Evidence references.
Matter Service owns Matter state.
Order Service owns Order state.
Task Service creates active Tasks.
Event Service preserves trace.
Workflow preview has no side effects.
Workflow apply requires Idempotency.
Workflow layer does not own domain behavior.
Workflow layer must not create active Tasks directly.
Workflow layer must not emit Events directly.
Workflow layer must not submit official filings.
AI may suggest classifications or gaps but must not certify professional truth.
Human Review gates protected professional conclusions.
Codex implements scoped MVP coordination only.
```

---

# 3. Workflow Position

Trademark Application Workflow is downstream of:

```text
customer-intake-workflow
```

It may be followed by:

```text
communication-review-workflow
office-action-response-workflow
provider-routing-workflow
evidence-review-workflow
```

In MVP, it proves the middle section of the execution spine:

```text
Brand / Trademark
↓
Matter / Order
↓
Document / Evidence
↓
Workflow Contract
↓
Task
↓
Event
↓
Permission / Policy
↓
Tests
```

---

# 4. Workflow Category

```text
MVP Category: Must Build Now
Implementation Depth: Level 2/3
Execution Mode: Preview + Apply
Official Filing: Not allowed in MVP
External Side Effects: Not allowed in MVP
AI Use: Suggestion / gap summary / draft only
Human Review: Required for professional finalization gates
```

---

# 5. Related Services

Trademark Application Workflow coordinates:

```text
Trademark Service
Brand Service
Jurisdiction Service
Classification Service
Document Service
Evidence Service
Matter Service
Order Service
Task Service
Event Service
Permission Service
Policy Service
```

Optional or future services:

```text
Knowledge Service
Routing Service
Service Provider Service
Notification Service
```

These are not production execution requirements in MVP.

---

# 6. Ownership Rules

| Area | Owner |
|---|---|
| Trademark state | Trademark Service |
| Brand state | Brand Service |
| Jurisdiction reference | Jurisdiction Service |
| Classification state/suggestions/finalization boundary | Classification Service |
| Document metadata/reference | Document Service |
| Evidence metadata/reference | Evidence Service |
| Matter state | Matter Service |
| Order state | Order Service |
| Active Task | Task Service |
| Event trace | Event Service / owning service integration |
| Permission evaluation | Permission Service |
| Policy evaluation | Policy Service |
| Workflow coordination | Trademark Application Workflow |

Workflow must not claim ownership over service-owned state.

---

# 7. Inputs

```yaml
workflow_id: trademark-application-workflow
workflow_contract_version: v0.1.0
operation: preview | apply
actor_reference_id: usr_...
organization_reference_id: org_...
customer_reference_id: cus_... | null
brand_reference_id: brd_... | null
trademark_input:
  trademark_name: string | null
  mark_type: word | device | combined | slogan | sound | unknown
  mark_text: string | null
  logo_document_reference_id: doc_... | null
  applicant_name: string | null
  applicant_country_or_region: string | null
jurisdiction_input:
  target_jurisdictions: list
  filing_basis: string | null
classification_input:
  goods_services_description: string | null
  preferred_classes: list | null
  preferred_items: list | null
document_inputs:
  uploaded_document_reference_ids: list
evidence_inputs:
  evidence_reference_ids: list
matter_reference_id: mat_... | null
order_reference_id: ord_... | null
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
At least one trademark signal is required.
At least one target jurisdiction or jurisdiction question is required.
idempotency_key is not required.
```

For apply:

```text
workflow_id is required.
workflow_contract_version is required.
actor_reference_id is required.
organization_reference_id is required.
brand_reference_id or brand creation input is required.
trademark_input.mark_type is required.
trademark_input.mark_text or logo_document_reference_id is required depending on mark_type.
target_jurisdictions are required.
matter_reference_id or matter creation context is required.
idempotency_key is required.
Permission/Policy context is required.
Human Review may be required for classification finalization or filing readiness gates.
```

---

# 9. Outputs

Preview output:

```yaml
workflow_id: trademark-application-workflow
operation: preview
status: preview_ready | missing_required_inputs | blocked | review_required
trademark_preview:
  create_trademark: boolean
  missing_trademark_fields: list
jurisdiction_preview:
  target_jurisdictions: list
  missing_jurisdiction_fields: list
classification_preview:
  suggested_classes: list
  suggested_items: list
  missing_goods_services_fields: list
  human_review_required: boolean
document_preview:
  accepted_document_references: list
  rejected_document_references: list
evidence_preview:
  accepted_evidence_references: list
  missing_evidence_items: list
task_plan:
  planned_tasks: list
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
workflow_id: trademark-application-workflow
operation: apply
status: applied | blocked | review_required | failed
trademark_reference_id: tm_... | null
brand_reference_id: brd_... | null
matter_reference_id: mat_... | null
order_reference_id: ord_... | null
document_reference_ids: list
evidence_reference_ids: list
task_reference_ids: list
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
check Permission/Policy
identify missing trademark fields
identify missing applicant fields
identify missing jurisdiction fields
prepare class suggestions
prepare goods/services gap list
prepare document/evidence gap list
prepare task plan
prepare AI-assisted intake summary
show HumanReviewRequired
show policy omissions
return warnings
```

Preview must not:

```text
create Trademark
create Brand
create Matter
create Order
create Document
create Evidence
create active Task
emit Event
submit official filing
finalize classification
certify registrability
certify filing readiness
select provider finally
send Communication
```

---

# 11. Apply Behavior

Apply coordinates service-owned state changes.

Apply may coordinate:

```text
Trademark Service creates or updates Trademark.
Brand Service links or creates Brand where scoped.
Jurisdiction Service validates jurisdiction references.
Classification Service records draft or review-required classification state.
Document Service validates/attaches document references.
Evidence Service validates/attaches evidence references.
Matter Service creates or updates Matter.
Order Service updates application-related order context.
Task Service creates active Tasks.
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
submit official filing
send official instructions
finalize professional classification without Human Review
certify registrability
certify evidence sufficiency
certify official deadline
create active Tasks directly from workflow layer
emit Events directly from workflow layer
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
idempotency_key for apply
correlation_id
```

## 12.2 Step 2 — Permission / Policy Precheck

Checks:

```text
trademark application preparation permission
brand/trademark data access
document/evidence access
matter/order access
classification suggestion permission
AI source policy
cross-organization policy
```

## 12.3 Step 3 — Brand and Trademark Context

Coordinates Brand Service and Trademark Service.

Determines:

```text
existing brand reference
new brand requirement
mark type
mark text/logo requirements
applicant information gaps
trademark record creation plan
```

## 12.4 Step 4 — Jurisdiction Context

Coordinates Jurisdiction Service.

Determines:

```text
target jurisdictions
jurisdiction-specific input gaps
country/region reference validity
future direct/Madrid route questions
```

This does not finalize route strategy.

## 12.5 Step 5 — Classification Preparation

Coordinates Classification Service.

May prepare:

```text
suggested Nice classes
suggested goods/services items
missing product/service descriptions
jurisdiction-specific item constraints
professional review requirement
```

This does not finalize classification unless reviewed through owning service rules.

## 12.6 Step 6 — Document and Evidence Preparation

Coordinates Document Service and Evidence Service.

Validates:

```text
logo files
applicant documents
priority documents where applicable
use evidence where applicable
authorization documents where applicable
```

This does not certify official sufficiency.

## 12.7 Step 7 — Matter and Order Alignment

Coordinates Matter Service and Order Service.

Determines:

```text
application matter context
order service scope
jurisdiction/class count basis
missing commercial confirmation
professional task requirements
```

This does not execute payment.

## 12.8 Step 8 — Task Plan Preparation

Possible planned tasks:

```text
confirm applicant name
confirm mark type
confirm target jurisdictions
confirm goods/services
professional classification review
collect logo file
collect POA/applicant documents
prepare filing instruction draft
review filing readiness
```

Task plan is not active Task.

## 12.9 Step 9 — AI-Assisted Preparation

AI may prepare:

```text
application summary
classification suggestion
missing information list
document/evidence gap summary
draft next questions
risk flags
```

AI must not:

```text
finalize classification
certify registrability
certify filing readiness
certify official deadline
submit application
select final provider
emit Events
```

## 12.10 Step 10 — Apply Through Owning Services

Expected service-owned effects:

```text
Trademark created/updated
Brand linked/created
Matter created/updated
Order aligned
Document references attached
Evidence references attached
Task Service creates active Tasks
Event trace recorded
```

## 12.11 Step 11 — Return Safe Result

Returns:

```text
created/linked references
task references
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
trademark:prepare
trademark:create
trademark:read
brand:read
brand:create
jurisdiction:read
classification:suggest
classification:review
document:read
document:attach
evidence:read
evidence:attach
matter:read
matter:create
order:read
order:update
task:create
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
trademark:data:visible
brand:data:visible
classification:source:visible
document:metadata:visible
evidence:metadata:visible
matter:data:visible
order:data:visible
event:trace:visible
ai_source:allowed
cross_organization:allowed
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
Replay creates no duplicate Trademark.
Replay creates no duplicate Matter.
Replay creates no duplicate Order.
Replay creates no duplicate active Task.
Replay creates no duplicate Event.
Replay does not leak policy-hidden prior result.
```

Semantic request includes:

```text
workflow_id
operation
actor_reference_id
organization_reference_id
brand_reference_id
normalized trademark_input
normalized jurisdiction_input
normalized classification_input
normalized document_inputs
normalized evidence_inputs
workflow_contract_version
```

---

# 16. Event Trace

Expected event types may include:

```text
trademark-application-previewed
trademark-application-applied
trademark-created
brand-linked
classification-suggestion-prepared
document-attached
evidence-attached
matter-created
order-updated
task-created
permission-evaluated
policy-evaluated
```

Rules:

```text
Workflow does not emit Events directly.
Owning services or Event Service integration record Events.
event_reference_ids are trace only.
event_reference_ids are not commands.
Event visibility follows Permission/Policy.
Event payloads must not leak restricted application data.
```

---

# 17. Task Plan and Active Task Rules

Possible planned tasks:

```yaml
planned_task_type: review_classification
subject_reference_id: tm_...
required_owner_role: trademark_professional
priority: normal
human_review_required: true
policy_restrictions: []
source_step: classification-preparation
```

Rules:

```text
Task plan is not active Task.
Only Task Service creates active Tasks.
Task plan must preserve policy restrictions.
Task plan must use public references.
Workflow layer cannot create active Tasks directly.
```

---

# 18. Classification Rules

Classification preparation may include:

```text
suggested classes
suggested goods/services items
missing goods/services descriptions
jurisdiction-specific questions
professional review requirement
```

Classification preparation must not include:

```text
final classification without Human Review
guaranteed acceptance conclusion
official goods/services certification
legal risk certification
registrability certification
```

---

# 19. Document / Evidence Rules

Document and evidence preparation may include:

```text
reference validation
metadata validation
required document gap list
evidence gap list
policy visibility checks
```

It must not include:

```text
official sufficiency certification
court/office evidence conclusion
automatic rejection of evidence as legally insufficient
```

---

# 20. AI Context

Allowed AI outputs:

```text
application summary
classification suggestion
goods/services gap list
document/evidence gap list
draft next questions
risk flags
```

Forbidden AI outputs:

```text
final classification
registrability certification
filing readiness certification
deadline certification
official filing instruction approval
provider final selection
state mutation
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

# 21. Human Review

Human Review may be required for:

```text
final classification
evidence sufficiency conclusion
filing readiness confirmation
external-facing filing instruction
provider final selection if routing appears
cross-organization restricted data use
```

Rules:

```text
Human Review does not execute downstream action by itself.
Human Review does not bypass Permission.
Human Review does not bypass Policy.
Owning service determines whether review satisfies gate.
```

---

# 22. Error Handling

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
restricted trademark data
restricted document metadata
restricted evidence content
classification source restrictions
policy internals
permission internals
stack traces
AI prompts
hidden reasoning
```

---

# 23. Versioning

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

# 24. Out of Scope

Trademark Application Workflow does not implement:

```text
official filing submission
official office communication
final trademark registrability opinion
final deadline certification
final evidence sufficiency certification
final goods/services legal approval without Human Review
payment execution
provider final selection
external communication send
full Madrid route decision engine
full jurisdiction strategy engine
full AI agent runtime
```

---

# 25. Forbidden Shortcuts

Codex must not:

```text
create Trademark directly from workflow layer
finalize Classification directly from workflow layer
create active Task directly from workflow layer
emit Events directly from workflow layer
send Communication directly from workflow layer
submit official filing
skip Permission/Policy
skip Human Review where required
skip Idempotency for apply
treat AI output as professional conclusion
treat preview as apply
accept unsupported versions silently
return unsafe errors
```

---

# 26. Test Requirements

Required tests:

```text
preview_valid_request_returns_application_plan
preview_missing_required_inputs_returns_missing_inputs
preview_has_no_side_effects
apply_requires_idempotency_key
apply_same_key_same_request_replays_safely
apply_same_key_different_request_conflicts
apply_permission_denied_blocks
apply_policy_restricted_blocks
apply_policy_redacts_output
apply_policy_nondisclosure_returns_notfound
apply_human_review_required_for_classification_finalization
apply_creates_active_tasks_only_through_task_service
workflow_does_not_emit_events_directly
workflow_does_not_submit_official_filing
ai_classification_suggestion_is_non_final
ai_forbidden_professional_certification_blocked
event_reference_is_trace_only
version_unsupported_fails_closed
safe_errors_no_database_id_or_stack_trace
restricted_data_not_leaked
```

---

# 27. Acceptance Criteria

Trademark Application Workflow is accepted only if:

```text
[ ] Workflow purpose is clear.
[ ] Workflow category is Must Build Now.
[ ] Related workflow contract exists.
[ ] Preview behavior is side-effect free.
[ ] Apply behavior requires Idempotency.
[ ] Owning service boundaries are preserved.
[ ] Classification finalization is protected.
[ ] Document/Evidence sufficiency is not certified by workflow or AI.
[ ] Task plan is not active Task.
[ ] Active Tasks are created only through Task Service.
[ ] Workflow does not submit official filing.
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

# 28. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Trademark Application Workflow. Defines MVP application preparation coordination, inputs/outputs, preview/apply behavior, service ownership, classification/document/evidence boundaries, Permission/Policy, Idempotency, Event trace, Task/AI/Human Review rules, errors, versioning, out-of-scope, forbidden shortcuts and tests. |

---

**End of Trademark Application Workflow**
