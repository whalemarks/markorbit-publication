# Communication Review Workflow

**Spec ID:** B02-WORKFLOW-COMMUNICATION-REVIEW  
**Spec Type:** Workflow Specification  
**Spec File:** core-specs/workflows/communication-review-workflow.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Workflow Index:** core-specs/workflows/index.md  
**Related Workflow Contract:** core-specs/contracts/workflows/communication-review-workflow-contract.md  
**Related API Contracts:** communication-api-contract; task-api-contract; event-api-contract; customer-api-contract; matter-api-contract; order-api-contract; trademark-api-contract  
**Related Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Codex Task:** codex-tasks/TASK-008-workflow-validator-scaffold.md; codex-tasks/TASK-010-mvp-execution-spine.md  
**Status:** Draft  
**Version:** 0.1.0  
**Workflow ID:** communication-review-workflow  
**Workflow Contract Version:** v0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** Level 2/3 — MVP Workflow Validator and Execution Spine  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Communication Review Workflow defines the governed review process for professional and external-facing communications in MarkOrbit Core.

It coordinates:

```text
Communication draft review
AI-assisted draft safety
Policy redaction
Human Review gate
Task handoff
Event trace
Permission / Policy governance
```

This workflow proves the communication section of the MVP execution spine:

```text
Communication
↓
Human Review
↓
Task
↓
Event
↓
Permission / Policy
↓
Tests
```

Communication Review Workflow does not send external communications directly in MVP.

It prepares, reviews and gates communications so that Communication Service remains the owner of communication state.

---

# 2. Core Lock

```text
Communication Review Workflow coordinates communication review.
Communication Service owns Communication state.
Task Service creates active Tasks.
Event Service preserves trace.
Workflow preview has no side effects.
Workflow apply requires Idempotency.
Workflow layer does not own Communication behavior.
Workflow layer must not send Communications directly.
Workflow layer must not create active Tasks directly.
Workflow layer must not emit Events directly.
AI may draft or suggest but must not approve or send.
Human Review gates external-facing or professional communication.
Permission and Policy govern communication content and visibility.
Codex implements scoped MVP review coordination only.
```

---

# 3. Workflow Position

Communication Review Workflow may be invoked after:

```text
customer-intake-workflow
trademark-application-workflow
office-action-response-workflow
provider-routing-workflow
renewal-workflow
assignment-workflow
evidence-review-workflow
```

In MVP, it is one of the three Must Build Now workflows.

It supports:

```text
intake confirmation draft
missing information request
internal review note
client-facing status explanation
provider inquiry draft preview
professional communication review
```

It does not support direct external sending in MVP.

---

# 4. Workflow Category

```text
MVP Category: Must Build Now
Implementation Depth: Level 2/3
Execution Mode: Preview + Apply
External Send: Not allowed directly by workflow
AI Use: Draft / suggest / flag only
Human Review: Required for external-facing or professional communication approval
Production Side Effects: Scoped, service-owned only
```

---

# 5. Related Services

Communication Review Workflow coordinates:

```text
Communication Service
Task Service
Event Service
Permission Service
Policy Service
```

Depending on subject context, it may validate references against:

```text
Customer Service
Matter Service
Order Service
Trademark Service
Document Service
Evidence Service
Service Provider Service
Partner Service
```

The workflow does not own those subject records.

---

# 6. Ownership Rules

| Area | Owner |
|---|---|
| Communication draft | Communication Service |
| Communication review status | Communication Service |
| Communication send status | Communication Service |
| Active Task | Task Service |
| Event trace | Event Service / owning service integration |
| Subject records | Their owning services |
| Permission evaluation | Permission Service |
| Policy evaluation | Policy Service |
| Workflow coordination | Communication Review Workflow |
| Human Review record | Human Review Contract / owning review mechanism |

Workflow must not own Communication state.

---

# 7. Inputs

```yaml
workflow_id: communication-review-workflow
workflow_contract_version: v0.1.0
operation: preview | apply
actor_reference_id: usr_...
organization_reference_id: org_...
communication_input:
  communication_reference_id: com_... | null
  draft_text: string | null
  communication_type: internal_note | client_email | provider_email | official_instruction | unknown
  channel: email | internal | portal | phone_note | unknown
  audience_type: internal | customer | partner | provider | official | unknown
  subject_reference_id: string | null
  subject_reference_type: customer | trademark | matter | order | document | evidence | provider | unknown
review_input:
  requested_action: prepare_review | request_changes | mark_reviewed | approve_for_send | reject | unknown
  reviewer_note: string | null
  risk_flags: list
  required_review_role: string | null
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
communication_reference_id or draft_text is required.
communication_type is required.
audience_type is required.
idempotency_key is not required.
Permission/Policy context is required.
```

For apply:

```text
workflow_id is required.
workflow_contract_version is required.
actor_reference_id is required.
organization_reference_id is required.
communication_reference_id is required unless creating draft through Communication Service is explicitly scoped.
requested_action is required.
idempotency_key is required.
Permission/Policy context is required.
Human Review is required for approve_for_send where protected.
```

---

# 9. Outputs

Preview output:

```yaml
workflow_id: communication-review-workflow
workflow_contract_version: v0.1.0
operation: preview
status: preview_ready | missing_required_inputs | blocked | review_required
communication_preview:
  communication_reference_id: com_... | null
  draft_available: boolean
  audience_type: string
  communication_type: string
  policy_restricted_content_found: boolean
  restricted_fields_omitted: boolean
review_preview:
  allowed_review_actions: list
  human_review_required: boolean
  required_review_role: string | null
  risk_flags: list
  missing_review_inputs: list
task_plan:
  planned_tasks: list
ai_output:
  suggested_revision: string | null
  risk_summary: string | null
  non_final: true
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
workflow_id: communication-review-workflow
workflow_contract_version: v0.1.0
operation: apply
status: applied | blocked | review_required | failed
communication_reference_id: com_... | null
communication_status: draft | review_requested | changes_requested | reviewed | approved_for_send | rejected | null
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
validate communication reference
validate subject reference
check Permission/Policy
identify restricted content
identify missing review inputs
prepare review action options
prepare task plan
prepare AI-assisted revision suggestion
prepare AI-assisted risk summary
show HumanReviewRequired
show policy omissions
return warnings
```

Preview must not:

```text
create Communication
update Communication
approve Communication
send Communication
create active Task
emit Event
mutate subject record
execute external communication
```

---

# 11. Apply Behavior

Apply coordinates Communication Service and related services.

Apply may coordinate:

```text
Communication Service creates draft where scoped.
Communication Service updates review status.
Communication Service records reviewer note.
Task Service creates active follow-up Tasks.
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
send Communication directly from workflow layer
approve external send without Human Review where required
create active Tasks directly from workflow layer
emit Events directly from workflow layer
mutate subject records directly
treat AI draft as approval
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
communication_reference_id or draft_text
communication_type
audience_type
idempotency_key for apply
correlation_id
```

## 12.2 Step 2 — Permission / Policy Precheck

Checks:

```text
actor may read or review Communication
actor may create draft where scoped
actor may approve for send where protected
actor may access subject reference
Policy allows content visibility
Policy allows recipient/audience visibility
Policy allows AI source use where AI-assisted
```

## 12.3 Step 3 — Communication Content Assessment

Coordinates Communication Service.

Determines:

```text
draft availability
draft type
audience type
subject linkage
restricted content flags
missing content
channel requirements
review requirements
```

## 12.4 Step 4 — Review Requirement Assessment

Determines:

```text
required review role
human review requirement
policy restrictions
professional risk flags
external-facing risk
official-instruction risk
```

## 12.5 Step 5 — AI-Assisted Draft Review

AI may prepare:

```text
suggested revision
tone improvement
risk flag summary
missing information list
policy omission disclosure
```

AI must not:

```text
approve draft
send communication
certify legal correctness
certify client instruction
certify official filing readiness
change Communication status
emit Events
```

## 12.6 Step 6 — Task Plan Preparation

Possible planned tasks:

```text
revise communication
obtain client confirmation
obtain professional review
confirm recipient
attach missing document
prepare communication send review
```

Task plan is not active Task.

## 12.7 Step 7 — Apply Through Owning Services

On apply, workflow coordinates service calls.

Expected service-owned effects:

```text
Communication review status updated
reviewer note recorded
draft created where scoped
active follow-up Tasks created by Task Service
Event trace recorded
```

## 12.8 Step 8 — Return Safe Result

Returns:

```text
communication reference
communication review status
task references
event references
policy redaction status
human review status
idempotency replay status
safe warnings/errors
```

---

# 13. Review Actions

Supported review actions in MVP:

```text
prepare_review
request_changes
mark_reviewed
approve_for_send
reject
```

Action rules:

```text
prepare_review may only prepare review context.
request_changes may update review status through Communication Service.
mark_reviewed may mark reviewed through Communication Service.
approve_for_send requires Permission/Policy and Human Review where protected.
reject may update review status through Communication Service.
```

Not allowed directly by workflow:

```text
send
external_dispatch
official_submission
provider_instruction_send
payment_instruction_send
```

---

# 14. Permission Requirements

Required permissions may include:

```text
communication:read
communication:draft
communication:review
communication:approve
communication:send_request
task:create
event:read
customer:read
matter:read
order:read
trademark:read
document:read
evidence:read
provider:read
```

Rules:

```text
PermissionDenied blocks protected action.
UnknownPermission fails closed.
MissingPermissionContext fails closed.
PermissionAllowed does not bypass Policy.
```

---

# 15. Policy Requirements

Required policy scopes may include:

```text
communication:content:visible
communication:recipient:visible
communication:review_note:visible
customer:data:visible
matter:data:visible
order:data:visible
trademark:data:visible
document:metadata:visible
evidence:metadata:visible
provider:data:visible
provider:commercial_terms:visible
ai_source:allowed
cross_organization:allowed
event:trace:visible
```

Rules:

```text
PolicyRestrictedBlock blocks workflow step.
PolicyRestrictedRedact redacts content and sets restricted_fields_omitted.
PolicyRequiresHumanReview returns HumanReviewRequired unless valid review exists.
PolicyNonDisclosureNotFound hides object/source existence.
UnknownPolicy fails closed where policy-controlled.
```

---

# 16. Idempotency

Apply must require idempotency.

Rules:

```text
idempotency_key is required for apply.
Same key + same semantic request replays safely.
Same key + different semantic request returns IdempotencyConflict.
Replay creates no duplicate Communication draft.
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
communication_reference_id
normalized draft_text where applicable
requested_action
reviewer_note
workflow_contract_version
```

---

# 17. Event Trace

Expected event types may include:

```text
communication-review-previewed
communication-review-applied
communication-draft-created
communication-review-requested
communication-changes-requested
communication-reviewed
communication-approved-for-send
communication-rejected
task-created
permission-evaluated
policy-evaluated
```

Rules:

```text
Workflow does not emit Events directly.
Communication Service or Event Service integration records Communication Events.
Task Service records Task Events.
event_reference_ids are trace only.
event_reference_ids are not commands.
Event visibility follows Permission/Policy.
Event payloads must not leak restricted communication content.
```

---

# 18. Task Plan and Active Task Rules

Possible planned tasks:

```yaml
planned_task_type: revise_communication
subject_reference_id: com_...
required_owner_role: communication_reviewer
priority: normal
human_review_required: true
policy_restrictions:
  - communication_content_restricted
source_step: communication-review
```

Rules:

```text
Task plan is not active Task.
Task Service creates active Tasks during apply.
Workflow layer cannot create active Tasks directly.
AI suggestions cannot become active Tasks directly.
Task subject references must not reveal hidden objects.
```

---

# 19. Communication Send Boundary

MVP workflow may approve or mark review status only where allowed.

It must not:

```text
send external email
send provider instruction
send official instruction
dispatch portal message
trigger external notification
```

External send, when implemented later, must be:

```text
owned by Communication Service
Permission/Policy governed
Human Review gated
Idempotency protected
Event traced
safe-error controlled
versioned
```

---

# 20. AI Context

Allowed AI outputs:

```text
draft revision
tone adjustment suggestion
risk flag summary
missing information list
policy omission explanation
recipient clarity suggestion
```

Forbidden AI outputs:

```text
approval
send decision
legal correctness certification
official instruction approval
client authorization certification
provider engagement decision
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
client-facing communication approval
provider-facing communication approval
official instruction approval
communication containing legal/professional conclusion
communication using restricted data
cross-organization communication
approve_for_send action
```

Rules:

```text
Human Review does not execute downstream send action by itself.
Human Review does not bypass Permission.
Human Review does not bypass Policy.
Communication Service determines whether review satisfies status transition.
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
restricted communication content
hidden recipients
restricted customer data
restricted provider commercial terms
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

Communication Review Workflow MVP does not implement:

```text
external email sending
official portal messaging
provider instruction dispatch
payment notice dispatch
notification delivery
SMS/WhatsApp/WeChat sending
full communication center
full template engine
full AI legal writing agent
automatic legal approval
automatic client authorization
```

---

# 25. Forbidden Shortcuts

Codex must not:

```text
send Communication directly from workflow layer
approve external send without required Human Review
create active Task directly from workflow layer
emit Events directly from workflow layer
mutate subject records directly
skip Permission/Policy
skip Idempotency for apply
treat AI output as approval
treat Human Review as automatic send
treat preview as apply
accept unsupported versions silently
return unsafe errors
```

---

# 26. Test Requirements

Required tests:

```text
preview_valid_request_returns_review_plan
preview_missing_required_inputs_returns_missing_inputs
preview_has_no_side_effects
apply_requires_idempotency_key
apply_same_key_same_request_replays_safely
apply_same_key_different_request_conflicts
apply_permission_denied_blocks
apply_policy_restricted_blocks
apply_policy_redacts_content
apply_policy_nondisclosure_returns_notfound
apply_human_review_required_for_approve_for_send
apply_creates_active_tasks_only_through_task_service
workflow_does_not_emit_events_directly
workflow_does_not_send_communication_directly
communication_service_owns_status_transition
ai_draft_is_non_final
ai_approval_or_send_blocked
event_reference_is_trace_only
version_unsupported_fails_closed
safe_errors_no_database_id_or_stack_trace
restricted_communication_content_not_leaked
```

---

# 27. Acceptance Criteria

Communication Review Workflow is accepted only if:

```text
[ ] Workflow purpose is clear.
[ ] Workflow category is Must Build Now.
[ ] Related workflow contract exists.
[ ] Preview behavior is side-effect free.
[ ] Apply behavior requires Idempotency.
[ ] Communication Service owns Communication state.
[ ] Workflow does not send Communication directly.
[ ] Workflow does not emit Events directly.
[ ] Workflow does not create active Tasks directly.
[ ] Task Service creates active Tasks.
[ ] Permission/Policy checks are defined.
[ ] AI output remains draft/suggestion/non-final.
[ ] Human Review gates external-facing/professional communication.
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
| 0.1.0 | Draft | Initial Communication Review Workflow. Defines MVP communication review coordination, inputs/outputs, preview/apply behavior, Communication Service ownership, send boundary, Permission/Policy, Idempotency, Event trace, Task/AI/Human Review rules, errors, versioning, out-of-scope, forbidden shortcuts and tests. |

---

**End of Communication Review Workflow**
