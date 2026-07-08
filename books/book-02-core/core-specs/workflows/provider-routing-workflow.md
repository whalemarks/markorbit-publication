# Provider Routing Workflow

**Spec ID:** B02-WORKFLOW-PROVIDER-ROUTING  
**Spec Type:** Workflow Specification  
**Spec File:** core-specs/workflows/provider-routing-workflow.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Workflow Index:** core-specs/workflows/index.md  
**Related Workflow Contract:** core-specs/contracts/workflows/provider-routing-workflow-contract.md  
**Related API Contracts:** routing-api-contract; partner-api-contract; service-provider-api-contract; service-network-api-contract; matter-api-contract; order-api-contract; task-api-contract; communication-api-contract; event-api-contract  
**Related Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Codex Task:** codex-tasks/TASK-008-workflow-validator-scaffold.md  
**Status:** Draft  
**Version:** 0.1.0  
**Workflow ID:** provider-routing-workflow  
**Workflow Contract Version:** v0.1.0  
**MVP Category:** Stub Now  
**Implementation Depth:** Level 1/2 — Preview / Validation Stub  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Provider Routing Workflow defines the future workflow for preparing service provider routing decisions.

It may help identify possible providers, routing constraints, missing provider information and review requirements.

In MVP, this workflow is a safe stub.

It must not perform final provider selection, dispatch instructions, create commercial commitments or contact providers automatically.

---

# 2. Core Lock

```text
Provider Routing Workflow coordinates routing preparation.
It is Stub Now in MVP.
Routing Service owns routing behavior.
Partner Service owns Partner state.
Service Provider Service owns Service Provider state.
Service Network Service owns Service Network state.
Matter Service owns Matter state.
Order Service owns Order state.
Task Service creates active Tasks only when explicitly allowed by MVP scope.
Communication Service owns Communication drafts.
Event Service preserves trace.
Workflow preview has no side effects.
Workflow apply is not production-enabled in MVP.
Routing preview does not equal final provider selection.
AI may suggest provider candidates but must not select final provider.
Human Review gates provider selection and external provider engagement.
Codex implements validation and preview-only boundaries only.
```

---

# 3. Workflow Position

Provider Routing Workflow may be used after:

```text
customer-intake-workflow
trademark-application-workflow
office-action-response-workflow
renewal-workflow
assignment-workflow
evidence-review-workflow
```

It supports future routing needs for:

```text
jurisdiction-specific local associate selection
service provider matching
provider quote comparison
service network routing
provider capacity review
commercial terms review
provider communication preparation
```

In MVP, it is not part of the executable spine.

It exists to preserve routing architecture and prevent premature provider automation.

---

# 4. Workflow Category

```text
MVP Category: Stub Now
Implementation Depth: Level 1/2
Execution Mode: Preview / Validation Stub
Apply Behavior: Not production-enabled in MVP
Provider Final Selection: Not allowed in MVP
External Provider Engagement: Not allowed in MVP
Commercial Commitment: Not allowed in MVP
AI Use: Candidate preview / gap summary only
Human Review: Required for provider final selection
```

---

# 5. Related Services

Future full workflow may coordinate:

```text
Routing Service
Partner Service
Service Provider Service
Service Network Service
Jurisdiction Service
Matter Service
Order Service
Task Service
Communication Service
Event Service
Permission Service
Policy Service
Knowledge Service
```

MVP stub may only require:

```text
reference validation
Permission/Policy validation
safe routing candidate preview
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
| Routing logic and routing preview | Routing Service |
| Partner state | Partner Service |
| Service Provider state | Service Provider Service |
| Service Network state | Service Network Service |
| Jurisdiction references | Jurisdiction Service |
| Matter state | Matter Service |
| Order state | Order Service |
| Active Task | Task Service |
| Communication draft/send state | Communication Service |
| Event trace | Event Service / owning service integration |
| Permission evaluation | Permission Service |
| Policy evaluation | Policy Service |
| Workflow coordination | Provider Routing Workflow |

Workflow must not own provider selection or service network state.

---

# 7. Inputs

```yaml
workflow_id: provider-routing-workflow
workflow_contract_version: v0.1.0
operation: preview | apply
actor_reference_id: usr_...
organization_reference_id: org_...
matter_reference_id: mat_... | null
order_reference_id: ord_... | null
routing_input:
  target_jurisdiction: string | null
  service_type: trademark_application | office_action_response | renewal | assignment | search | opposition | unknown
  language_requirement: string | null
  urgency: normal | urgent | unknown
  budget_note: string | null
  preferred_provider_reference_ids: list
  excluded_provider_reference_ids: list
  required_capabilities: list
  client_constraints: list
provider_context:
  partner_reference_id: par_... | null
  service_network_reference_id: snw_... | null
  service_provider_reference_ids: list
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
service_type is required.
target_jurisdiction is required unless matter/order supplies it.
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
apply must not select final provider.
apply must not contact provider.
apply must not create commercial commitment.
```

---

# 9. Outputs

Preview output:

```yaml
workflow_id: provider-routing-workflow
workflow_contract_version: v0.1.0
operation: preview
status: preview_ready | missing_required_inputs | blocked | review_required | not_implemented
routing_preview:
  candidate_provider_references: list
  missing_routing_fields: list
  routing_factors: list
  excluded_candidates: list
  provider_visibility_limited: boolean
  final_selection_made: false
provider_review:
  human_review_required: true
  commercial_terms_review_required: true
task_plan:
  planned_tasks: list
communication_preview:
  provider_contact_draft_needed: boolean
  draft_summary: string | null
ai_output:
  candidate_summary: string | null
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
workflow_id: provider-routing-workflow
operation: apply
status: not_implemented
error:
  code: StateInvalid
  message: apply is not production-enabled for provider routing in MVP
  retryable: false
```

---

# 10. Preview Behavior

Preview may:

```text
validate request shape
validate matter/order references
validate provider references
check Permission/Policy
identify missing routing fields
prepare candidate provider preview
prepare routing factor explanation
prepare provider data gap list
prepare commercial review warning
prepare task plan preview
prepare provider contact draft summary
show HumanReviewRequired
show policy omissions
return safe warnings
```

Preview must not:

```text
select final provider
create provider engagement
create commercial commitment
create active Task
create Communication
send provider message
emit Event
execute payment
dispatch filing instruction
```

---

# 11. Apply Behavior

In MVP, apply is not production-enabled.

Apply must:

```text
return controlled safe not-implemented response
perform no side effects
not select final provider
not create active Tasks
not create Communications
not emit Events
not send provider message
not create provider commitment
```

Future apply must require:

```text
idempotency_key
Permission/Policy
Human Review
safe Errors
Versioning
routing ownership through Routing Service
provider state through Service Provider Service
communication through Communication Service
event trace through Event Service or owning service integration
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
service_type
target_jurisdiction
matter/order references
provider references
correlation_id
```

## 12.2 Step 2 — Permission / Policy Precheck

Checks:

```text
routing preview permission
provider data visibility
partner/service network visibility
matter/order visibility
commercial terms visibility
AI source use policy
cross-organization/provider relationship policy
```

## 12.3 Step 3 — Routing Context Preview

May identify:

```text
service type
target jurisdiction
language requirement
urgency
required capabilities
preferred/excluded providers
provider data gaps
commercial review needs
```

## 12.4 Step 4 — Candidate Preview

May prepare:

```text
candidate provider list
candidate match factors
candidate missing data
excluded provider reasons where visible
policy-limited fields
human review requirement
```

This does not select final provider.

## 12.5 Step 5 — Task Plan Preview

May prepare planned tasks:

```text
review provider candidates
confirm provider availability
request provider quote
review commercial terms
prepare provider instruction draft
obtain human approval
```

Task plan is not active Task in MVP stub.

## 12.6 Step 6 — Communication Preview

May prepare:

```text
provider inquiry draft summary
provider quote request outline
internal routing note
client approval question
```

No communication is created or sent in MVP stub unless separately coordinated through Communication Service in a later phase.

## 12.7 Step 7 — AI-Assisted Routing Summary

AI may prepare:

```text
candidate comparison summary
provider data gap list
routing factor explanation
risk flags
question list for provider review
```

AI must not:

```text
select final provider
engage provider
approve commercial terms
send provider inquiry
commit order
emit Events
```

## 12.8 Step 8 — Return Safe Preview

Returns:

```text
candidate preview
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
routing:preview
partner:read
service_provider:read
service_network:read
matter:read
order:read
communication:draft
event:read
```

Future apply may require:

```text
routing:select
service_provider:engage
communication:create
task:create
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
provider:data:visible
provider:commercial_terms:visible
partner:data:visible
service_network:data:visible
matter:data:visible
order:data:visible
cross_organization:allowed
ai_source:allowed
event:trace:visible
```

Rules:

```text
PolicyRestrictedBlock blocks workflow preview.
PolicyRestrictedRedact redacts provider/commercial fields and sets restricted_fields_omitted.
PolicyRequiresHumanReview marks review required.
PolicyNonDisclosureNotFound hides provider/source existence where required.
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
no duplicate provider engagement
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
provider-routing-previewed
provider-routing-applied
provider-candidates-prepared
provider-selected
provider-instruction-draft-created
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
Provider commercial data must not leak in Event payload.
```

---

# 17. Task Plan Rules

MVP task plan may include:

```yaml
planned_task_type: review_provider_candidates
subject_reference_id: mat_...
required_owner_role: routing_manager
priority: normal
human_review_required: true
policy_restrictions:
  - provider_commercial_terms_restricted
source_step: routing-preview
```

Rules:

```text
Task plan is not active Task.
MVP stub does not create active Task.
Future active Tasks must be created only by Task Service.
AI candidate suggestions cannot become active Tasks directly.
```

---

# 18. Communication Rules

Preview may prepare:

```text
provider quote request outline
provider availability inquiry outline
internal routing note
client provider approval question
```

Rules:

```text
Communication draft is not sent.
MVP stub does not create Communication unless separately allowed by Communication Service.
External provider message requires Communication Review Workflow and Human Review.
AI draft remains draft/suggestion/non-final.
```

---

# 19. AI Context

Allowed AI outputs:

```text
candidate comparison summary
provider data gap list
routing factor explanation
question list
risk flags
```

Forbidden AI outputs:

```text
final provider selection
provider engagement
commercial approval
provider ranking as final decision
automatic dispatch
payment approval
communication send
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
final provider selection
provider engagement
commercial term approval
provider instruction approval
client-facing provider recommendation
cross-organization restricted provider data use
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
restricted provider data
provider commercial terms
partner relationship internals
service network internals
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

Provider Routing Workflow MVP does not implement:

```text
final provider selection
provider engagement
provider instruction sending
commercial commitment
payment execution
provider marketplace settlement
provider contract management
automatic provider ranking as final decision
production task creation
production event emission
external communication send
full provider scoring engine
full routing automation engine
full AI routing agent
```

---

# 24. Forbidden Shortcuts

Codex must not:

```text
turn preview into production apply
select final provider
engage provider
approve commercial terms
create active Task directly from workflow layer
emit Events directly from workflow layer
send Communication directly from workflow layer
skip Permission/Policy
treat AI output as final provider decision
treat Human Review record as automatic provider engagement
accept unsupported versions silently
return unsafe errors
```

---

# 25. Test Requirements

Required tests:

```text
preview_valid_request_returns_candidate_preview
preview_missing_required_inputs_returns_missing_inputs
preview_has_no_side_effects
preview_permission_denied_blocks
preview_policy_restricted_blocks
preview_policy_redacts_provider_fields
preview_policy_nondisclosure_hides_provider
preview_human_review_required_for_final_selection
apply_returns_not_implemented_in_mvp
apply_has_no_side_effects_in_mvp
workflow_does_not_emit_events_directly
workflow_does_not_create_active_tasks_directly
workflow_does_not_select_final_provider
workflow_does_not_send_provider_communication
ai_candidate_summary_is_non_final
ai_final_provider_selection_blocked
event_reference_is_trace_only
version_unsupported_fails_closed
safe_errors_no_database_id_or_stack_trace
restricted_provider_data_not_leaked
```

---

# 26. Acceptance Criteria

Provider Routing Workflow is accepted only if:

```text
[ ] Workflow purpose is clear.
[ ] Workflow category is Stub Now.
[ ] Related workflow contract exists.
[ ] Preview behavior is side-effect free.
[ ] Apply is not production-enabled in MVP.
[ ] Final provider selection is explicitly out of scope.
[ ] Provider engagement is explicitly forbidden.
[ ] Commercial commitment is explicitly forbidden.
[ ] Task plan is not active Task.
[ ] Workflow does not emit Events directly.
[ ] Workflow does not send Communication directly.
[ ] Permission/Policy checks are defined.
[ ] Provider/commercial data policy restrictions are preserved.
[ ] AI output remains draft/suggestion/non-final.
[ ] Human Review gates provider selection.
[ ] Safe Error behavior is defined.
[ ] Versioning behavior is defined.
[ ] Forbidden shortcuts are explicit.
[ ] Required tests are defined.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Provider Routing Workflow. Defines Stub Now routing preview/validation behavior, future coordination scope, ownership, inputs/outputs, side-effect-free preview, apply disabled in MVP, provider final selection boundary, Permission/Policy, AI/Human Review, Event/Task/Communication boundaries, errors, versioning, out-of-scope, forbidden shortcuts and tests. |

---

**End of Provider Routing Workflow**
