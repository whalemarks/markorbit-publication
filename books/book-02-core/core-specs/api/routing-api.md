# API Specification — Routing API

**Spec ID:** B02-API-ROUTING  
**Spec Type:** API Specification  
**API Name:** Routing API  
**API File:** core-specs/api/routing-api.md  
**Related Domain:** core-specs/domains/routing.md  
**Related Object Specs:** core-specs/objects/routing.md; core-specs/objects/service-provider.md; core-specs/objects/agent.md; core-specs/objects/partner.md; core-specs/objects/service-network.md; core-specs/objects/jurisdiction.md; core-specs/objects/capability.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/task.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/routing-service.md; core-specs/services/service-provider-service.md; core-specs/services/agent-service.md; core-specs/services/partner-service.md; core-specs/services/service-network-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/task-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/routing-evaluated.md; core-specs/events/routing-selected.md; core-specs/events/service-provider-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/routing-api-contract.md; core-specs/contracts/events/routing-evaluated-payload.md; core-specs/contracts/events/routing-selected-payload.md  
**Related Agent Specs:** core-specs/agents/routing-agent.md; core-specs/agents/service-provider-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 4 — Collaboration / Network Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Routing API exposes governed Routing evaluation, candidate comparison and selection operations for MarkOrbit Core.

It allows authorized consumers to create routing evaluations, read routing results, validate routing references, select routing outcomes and prepare downstream order/matter/task context without treating Routing as Service Provider truth, payment authorization, legal representation, contract approval, order assignment, task execution, professional conclusion or AI autonomous vendor selection.

Routing API exists to support:

```text
provider candidate evaluation
jurisdiction and service capability matching
order/matter routing preparation
service-provider comparison
policy-controlled routing visibility
routing decision trace
AI-assisted routing recommendation under governance
event trace access
API-safe routing reference validation
```

Routing API does not create Service Providers, prove legal authority, approve contracts, authorize payments, assign work by itself or replace human/vendor governance.

---

# 2. API Meaning

Routing API means:

```text
a governed interface for evaluating and selecting service route candidates through Routing Service.
```

Routing API does not mean:

```text
Service Provider API
Partner API
Service Network API
Order assignment API
payment API
vendor contract API
legal representative API
professional truth API
AI autonomous selection API
```

Routing evaluates candidates.

Service Provider owns provider reference and capability context.

Order and Matter own service execution context.

Task owns actionable work.

RoutingSelected is a governed selection trace, not payment, contract or legal authority by itself.

---

# 3. API Boundary

Routing API is responsible for:

```text
Routing evaluation request intake
Routing read/search/list access
Routing reference validation
Routing candidate comparison
Routing selection request intake
Routing selection explanation
downstream preparation for Order/Matter/Task where explicitly governed
safe Routing response shaping
Permission/Policy enforcement for Routing operations
Routing-related Event reference exposure where allowed
AI Agent access boundary for Routing operations
controlled API errors
```

Routing API is not responsible for:

```text
Service Provider lifecycle ownership
Partner lifecycle ownership
Service Network lifecycle ownership
payment or settlement
contract approval
legal authority verification by itself
Order assignment by itself
Task execution
Communication delivery
professional decision approval
AI final selection without review where required
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/routing.md
```

Domain rule:

```text
Routing evaluates and selects service route candidates.
Routing is not Service Provider, Partner, payment, contract, legal authority, Order assignment or Task execution by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/routing.md
core-specs/objects/service-provider.md
core-specs/objects/agent.md
core-specs/objects/partner.md
core-specs/objects/service-network.md
core-specs/objects/jurisdiction.md
core-specs/objects/capability.md
core-specs/objects/order.md
core-specs/objects/matter.md
core-specs/objects/task.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Routing API returns routing_reference_id or routing_selection_reference_id.
- Routing API may reference Service Provider, Partner, Service Network, Jurisdiction, Order, Matter and Task context but must not create or execute them silently.
- Routing evaluation is not routing selection.
- Routing selection is not contract approval, payment authorization or legal authority confirmation.
- Routing candidate data must be policy-filtered and context-specific.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/routing-service.md
core-specs/services/service-provider-service.md
core-specs/services/agent-service.md
core-specs/services/partner-service.md
core-specs/services/service-network-service.md
core-specs/services/jurisdiction-service.md
core-specs/services/order-service.md
core-specs/services/matter-service.md
core-specs/services/task-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Routing API must invoke Routing Service for Routing behavior.
- Routing API must validate Service Provider, Jurisdiction, Order, Matter and Task references through their owning services where required.
- Routing API must invoke Permission Service before protected operations.
- Routing API must invoke Policy Service before evaluation, visibility and selection operations.
- Routing API must not emit RoutingEvaluated or RoutingSelected directly; Routing Service and Event Service govern events.
- Downstream Order, Matter and Task operations must route through their owning services.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/routing-evaluated.md
core-specs/events/routing-selected.md
core-specs/events/service-provider-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- evaluateRouting may result in RoutingEvaluated.
- selectRouting may result in RoutingSelected.
- API consumers must not fabricate RoutingEvaluated or RoutingSelected.
- RoutingEvaluated is candidate assessment trace, not selection.
- RoutingSelected is selection trace, not payment, contract, legal authority or execution completion.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Evaluate Routing

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/routing/evaluations`  
**Owning Service Operation:** `evaluateRouting`  
**Permission Required:** `routing:evaluate`  
**Policy Required:** `RoutingEvaluationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Service Must Emit RoutingEvaluated

Meaning:

```text
Evaluate route candidates for a target service context.
```

Non-meaning:

```text
does not select route
does not assign Order
does not approve payment
does not approve contract
does not prove legal authority
does not create Service Provider
does not grant Permission
```

Expected service call:

```text
API
  ↓
Permission Service evaluatePermission
  ↓
Policy Service evaluatePolicy
  ↓
Routing Service evaluateRouting
  ↓
Event Service record RoutingEvaluated
  ↓
Safe API response
```

## 8.2 Operation: Get Routing Evaluation

**Operation Category:** Read  
**Method:** GET  
**Path:** `/routing/evaluations/{routing_reference_id}`  
**Owning Service Operation:** `getRoutingEvaluation`  
**Permission Required:** `routing:read`  
**Policy Required:** `RoutingVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Routing evaluation view.
```

Non-meaning:

```text
does not expose provider pricing or private notes automatically
does not expose restricted candidate scoring automatically
does not indicate final route selection unless selection exists
```

## 8.3 Operation: Search Routing Evaluations

**Operation Category:** Search  
**Method:** GET  
**Path:** `/routing/evaluations`  
**Owning Service Operation:** `searchRoutingEvaluations`  
**Permission Required:** `routing:search`  
**Policy Required:** `RoutingVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Routing evaluation references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted routing history access
does not expose restricted provider, pricing, strategy or performance data by default
```

## 8.4 Operation: Validate Routing Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/routing/reference/validate`  
**Owning Service Operation:** `validateRoutingReference`  
**Permission Required:** `routing:validate`  
**Policy Required:** `RoutingReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Routing reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not authorize selection
does not assign order
does not approve provider engagement
does not authorize payment
```

## 8.5 Operation: List Routing Candidates

**Operation Category:** Read  
**Method:** GET  
**Path:** `/routing/evaluations/{routing_reference_id}/candidates`  
**Owning Service Operation:** `listRoutingCandidates`  
**Permission Required:** `routing:candidates:read`  
**Policy Required:** `RoutingCandidateVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe candidate summaries for a Routing evaluation.
```

Non-meaning:

```text
does not expose restricted provider terms automatically
does not select candidate
does not guarantee provider availability
```

## 8.6 Operation: Explain Routing Evaluation

**Operation Category:** Read  
**Method:** POST  
**Path:** `/routing/evaluations/{routing_reference_id}/explain`  
**Owning Service Operation:** `explainRoutingEvaluation`  
**Permission Required:** `routing:explain`  
**Policy Required:** `RoutingExplanationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where used for decisioning  
**Event Behavior:** May emit PolicyEvaluated; read only

Meaning:

```text
Generate a safe explanation of Routing evaluation result.
```

Non-meaning:

```text
does not create selection
does not reveal restricted scoring formulas by default
does not approve final selection
does not replace human review where required
```

## 8.7 Operation: Select Routing Candidate

**Operation Category:** Action  
**Method:** POST  
**Path:** `/routing/evaluations/{routing_reference_id}/select`  
**Owning Service Operation:** `selectRoutingCandidate`  
**Permission Required:** `routing:select`  
**Policy Required:** `RoutingSelectionPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-recommended  
**Event Behavior:** Service Must Emit RoutingSelected

Meaning:

```text
Create a governed Routing selection from a prior or current Routing evaluation.
```

Non-meaning:

```text
does not assign Order automatically
does not approve payment
does not approve contract
does not prove legal authority
does not create Communication automatically
does not complete workflow
```

## 8.8 Operation: Prepare Order Assignment from Routing

**Operation Category:** Action  
**Method:** POST  
**Path:** `/routing/selections/{routing_selection_reference_id}/order-assignment/prepare`  
**Owning Service Operation:** `prepareOrderAssignmentFromRouting`  
**Permission Required:** `routing:order-assignment:prepare`  
**Policy Required:** `RoutingOrderAssignmentPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired  
**Event Behavior:** Must route through Order Service if Order state is changed

Meaning:

```text
Prepare a governed Order assignment or provider engagement context from Routing selection.
```

Non-meaning:

```text
does not assign Order unless Order Service accepts it
does not approve payment
does not approve contract
does not start service work
```

## 8.9 Operation: Prepare Provider Communication from Routing

**Operation Category:** Action  
**Method:** POST  
**Path:** `/routing/selections/{routing_selection_reference_id}/communications/prepare`  
**Owning Service Operation:** `prepareProviderCommunicationFromRouting`  
**Permission Required:** `routing:communication:prepare`  
**Policy Required:** `RoutingCommunicationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Must route through Communication Service if Communication is created

Meaning:

```text
Prepare governed Communication draft or request based on Routing selection.
```

Non-meaning:

```text
does not create Communication unless Communication Service accepts it
does not send message
does not create contract
does not approve provider engagement
```

## 8.10 Operation: List Routing Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/routing/evaluations/{routing_reference_id}/events`  
**Owning Service Operation:** `listRoutingEvents`  
**Permission Required:** `routing:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Routing-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Evaluate Routing Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  routing_type: string
  routing_status: string | optional
  routing_purpose: string
  target_context:
    order_reference_id: string | null
    matter_reference_id: string | null
    task_reference_id: string | null
    jurisdiction_reference_id: string | null
    service_type: string | null
  candidate_scope:
    service_provider_reference_ids: list[string]
    service_network_reference_id: string | null
    include_preferred_only: boolean | null
  evaluation_mode: string
  source_type: string
  request_context: object
  ai_context:
    ai_assisted: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Validate Routing Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  routing_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.3 Explain Routing Evaluation Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  explanation_purpose: string
  explanation_depth: string
  include_restricted_scoring: boolean
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.4 Select Routing Candidate Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
path_parameters:
  routing_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  selected_service_provider_reference_id: string
  selection_mode: string
  selection_reason: string | null
  human_review_reference_id: string | null
  request_context: object
```

## 9.5 Prepare Order Assignment from Routing Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  order_reference_id: string
  assignment_mode: string
  service_provider_reference_id: string | null
  request_context: object
```

## 9.6 Prepare Provider Communication from Routing Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  communication_type: string
  draft_purpose: string
  target_context:
    order_reference_id: string | null
    matter_reference_id: string | null
    service_provider_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include unrestricted provider pricing, bank data, private contacts, contract secrets or internal scoring details by default.
- Requests must use controlled routing_type, routing_status, routing_purpose, evaluation_mode, selection_mode, assignment_mode and source_type values.
- AI-assisted routing data must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Routing Evaluation Response

```yaml
status: 200
body:
  routing_reference_id: string
  routing_type: string
  routing_status: string
  routing_purpose: string
  target_context:
    order_reference_id: string | null
    matter_reference_id: string | null
    task_reference_id: string | null
    jurisdiction_reference_id: string | null
    service_type: string | null
  candidate_summary:
    candidate_count: integer
    recommended_candidate_reference_id: string | null
    requires_human_review: boolean
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    evaluation_summary: string | null
  related_event_reference_ids:
    - routing_evaluated_event_id
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Routing Candidate Response

```yaml
status: 200
body:
  routing_reference_id: string
  candidates:
    - service_provider_reference_id: string
      candidate_status: string
      safe_score_band: string | null
      safe_reason: string | null
      review_required: boolean
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.3 Routing Reference Validation Response

```yaml
status: 200
body:
  routing_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Routing Explanation Response

```yaml
status: 200
body:
  routing_reference_id: string
  explanation_reference_id: string | null
  safe_explanation: string
  gaps_or_warnings: list[string]
  human_review_required: boolean
  restricted_fields_omitted: boolean
  policy_decision_reference_id: string | null
  correlation_id: string | null
```

## 10.5 Routing Selection Response

```yaml
status: 201
body:
  routing_reference_id: string
  routing_selection_reference_id: string
  selected_service_provider_reference_id: string
  selection_status: string
  review_required: boolean
  related_event_reference_ids:
    - routing_selected_event_id
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Downstream Preparation Response

```yaml
status: 200
body:
  routing_selection_reference_id: string
  preparation_reference_id: string | null
  preparation_status: string
  downstream_service_required: string | null
  missing_items: list[string]
  review_required: boolean
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply Order assignment, payment, contract approval, legal authority, Communication sending or service execution.
- Responses must not expose restricted scoring, provider pricing, private contacts, bank data, contracts or internal strategy by default.
- Responses must distinguish Routing Evaluation, Routing Selection, Service Provider, Order, Matter and Task references.
- Responses must identify review requirements for AI-assisted routing recommendations.
```

---

# 11. Controlled Values

## 11.1 routing_type

```text
ServiceProviderRouting
JurisdictionRouting
TaskRouting
OrderRouting
MatterRouting
CommunicationRouting
InternalRouting
Unknown
```

## 11.2 routing_status

```text
Draft
Evaluated
ReviewRequired
Selected
Rejected
Expired
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 routing_purpose

```text
OrderProviderSelection
MatterProviderSelection
JurisdictionProviderSelection
TaskAssigneeSupport
CommunicationTargetSupport
ServiceNetworkSelection
AIAssistedRouting
Unknown
```

## 11.4 evaluation_mode

```text
Preview
AIAssistedDraft
HumanReview
FinalEvaluation
Unknown
```

## 11.5 selection_mode

```text
Preview
HumanSelected
PolicySelected
AIAssistedRecommendationAccepted
SystemSelected
Unknown
```

## 11.6 assignment_mode

```text
Preview
PrepareOnly
RequestOrderAssignment
Unknown
```

## 11.7 candidate_status

```text
Candidate
Recommended
NotRecommended
Restricted
Unavailable
ReviewRequired
Unknown
```

## 11.8 safe_score_band

```text
Low
Medium
High
NotDisclosed
Unknown
```

## 11.9 selection_status

```text
Selected
Rejected
PolicyRestricted
PermissionDenied
ReviewRequired
Unknown
```

## 11.10 preparation_status

```text
Prepared
Rejected
PolicyRestricted
PermissionDenied
ReviewRequired
DownstreamServiceRequired
Unknown
```

## 11.11 explanation_purpose

```text
InternalReview
ClientSupport
ProviderComparison
AuditReview
AIAssistedExplanation
Unknown
```

## 11.12 explanation_depth

```text
Summary
DetailedSafe
RestrictedInternal
Unknown
```

## 11.13 source_type

```text
ProfessionalInput
OrderDerived
MatterDerived
TaskDerived
ServiceProviderDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.14 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Expired
ContextMismatch
Unknown
```

## 11.15 intended_use

```text
OrderPreparation
MatterPreparation
TaskPreparation
ProviderSelection
CommunicationPreparation
AuditReference
AIAgentAnalysis
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
routing:evaluate
routing:read
routing:search
routing:validate
routing:candidates:read
routing:explain
routing:select
routing:order-assignment:prepare
routing:communication:prepare
routing:event:read
```

Rules:

```text
- Routing read/search must be permission-controlled.
- Routing evaluation must not imply selection.
- Routing validation must not authorize selection or assignment.
- Candidate visibility, explanation and selection require separate permissions.
- Order assignment and Communication preparation require downstream permissions and policies.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
RoutingEvaluationPolicy
RoutingVisibilityPolicy
RoutingReferencePolicy
RoutingCandidateVisibilityPolicy
RoutingExplanationPolicy
RoutingSelectionPolicy
RoutingOrderAssignmentPolicy
RoutingCommunicationPolicy
EventVisibilityPolicy
AIAgentRoutingAccessPolicy
RestrictedRoutingDataPolicy
CrossOrganizationRoutingPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Routing fields.
- Policy may require human review for AI-assisted routing recommendations.
- Policy may restrict cross-organization Routing lookup.
- Policy may restrict provider pricing, private contacts, scoring formulas, performance notes, contracts and internal strategy.
- Policy may restrict selection, order assignment preparation and provider communication preparation.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Evaluate Routing: Restricted / HumanReviewRequired where AI-assisted
Get Routing Evaluation: Restricted
Search Routing Evaluations: Restricted
Validate Routing Reference: Allowed under contract
List Routing Candidates: Restricted
Explain Routing Evaluation: Restricted / HumanReviewRequired where used for decisioning
Select Routing Candidate: Restricted / HumanReviewRequired
Prepare Order Assignment from Routing: Restricted / HumanReviewRequired
Prepare Provider Communication from Routing: Restricted / HumanReviewRequired where AI-drafted
List Routing Events: Restricted
```

AI Agents may:

```text
summarize safe Routing metadata
prepare Routing evaluation drafts for human review
flag missing candidate or service context
validate Routing references for authorized actions
explain Routing evaluation using safe fields
recommend candidate for human review
prepare downstream assignment or communication drafts for human review
```

AI Agents must not:

```text
fabricate Routing
fabricate RoutingEvaluated or RoutingSelected events
select provider without governed permission and review where required
assign Order or Task directly
approve payment or contract
treat provider as legal representative without governed proof
send provider Communication directly
bypass Permission or Policy
expose restricted scoring, pricing, contacts, contracts or bank data
```

AI access requires:

```text
agent_identity_reference_id
agent_contract_reference_id where required
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 15. Event Access Rules

Routing API may expose:

```text
RoutingEvaluated
RoutingSelected
ServiceProviderCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Routing events directly.
- RoutingEvaluated must not be treated as RoutingSelected.
- RoutingSelected must not be treated as payment authorization, contract approval, legal authority, Order assignment or Task execution.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] routing_reference_id is present where required.
[ ] routing_selection_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] order_reference_id is valid where provided.
[ ] matter_reference_id is valid where provided.
[ ] task_reference_id is valid where provided.
[ ] jurisdiction_reference_id is valid where provided.
[ ] service_provider_reference_ids are valid where provided.
[ ] selected_service_provider_reference_id is valid for selection.
[ ] routing_type is controlled.
[ ] routing_status is controlled.
[ ] routing_purpose is controlled.
[ ] evaluation_mode is controlled.
[ ] selection_mode is controlled where applicable.
[ ] assignment_mode is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted routing/provider/pricing/scoring/contact/contract fields are omitted or allowed.
[ ] AI-assisted routing data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] RoutingEvaluated is emitted after evaluateRouting succeeds.
[ ] RoutingSelected is emitted after selectRoutingCandidate succeeds.
[ ] Evaluation does not select candidate.
[ ] Selection does not assign Order or authorize payment.
[ ] Order assignment preparation routes through Order Service where state changes are required.
[ ] Communication preparation routes through Communication Service if Communication is created.
[ ] Response shape is safe.
```

---

# 17. Error Handling

Controlled errors:

```text
BadRequest
Unauthorized
PermissionDenied
PolicyRestricted
NotFound
RoutingReferenceInvalid
RoutingSelectionReferenceInvalid
OrderReferenceInvalid
MatterReferenceInvalid
TaskReferenceInvalid
JurisdictionReferenceInvalid
ServiceProviderReferenceInvalid
CandidateInvalid
SelectionInvalid
EvaluationInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedRoutingData
AgentContractRequired
HumanReviewRequired
EventEmissionFailed
InternalError
```

Error response:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Error rules:

```text
- Errors must not expose restricted Routing data.
- Errors must not expose provider pricing, contacts, bank data, contracts, scoring formulas or internal strategy.
- Errors must not expose unrelated Service Provider, Order, Matter or Task details.
- Errors must not expose permission or policy internals.
- Errors must be safe for product/API consumers.
```

---

# 18. Versioning Rules

API version:

```text
v0.1.0
```

Versioning rules:

```text
- Breaking changes require new version or explicit migration rule.
- routing_type, routing_status, routing_purpose, evaluation_mode, selection_mode, candidate_status and selection_status changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI routing recommendation behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Routing API spec
cite Routing Service Specification
cite Routing Object Specification
cite RoutingEvaluated and RoutingSelected Event Specifications
cite Service Provider/Order/Matter/Task/Communication specs where downstream operations are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata and safe candidate summaries by default
write tests for invalid routing_reference_id
write tests for invalid service_provider/order/matter/task references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that evaluation does not select candidate
write tests that selection does not assign Order or authorize payment
write tests that restricted scoring and pricing fields are omitted
write tests that Order assignment preparation routes through Order Service where required
write tests that Communication preparation routes through Communication Service
write tests for AI Agent Contract and human review requirement
write tests for RoutingEvaluated and RoutingSelected events after successful operations
```

Codex must not:

```text
write directly to database bypassing Routing Service
allow UI to emit RoutingEvaluated or RoutingSelected directly
treat Routing as Service Provider
treat Routing evaluation as selection
treat Routing selection as payment, contract, legal authority or Order assignment
assign Order or Task through Routing API directly
expose provider pricing, contacts, bank data, contracts or scoring internals for convenience
allow AI to fabricate Routing references or events
allow AI to select provider without governed review where required
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Routing API purpose.
[ ] It defines Routing API meaning.
[ ] It defines Routing API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines evaluate, read, search, validate, candidate-list, explanation, selection, order-assignment preparation, communication preparation and event-list operations.
[ ] It defines request contracts.
[ ] It defines response contracts.
[ ] It defines controlled values.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent access rules.
[ ] It defines Event access rules.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It defines versioning rules.
[ ] It includes Codex implementation notes.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Routing API specification. Defines governed Routing evaluation/selection interface and separates Routing API from Service Provider truth, payment, contract approval, legal authority, Order assignment, Task execution and AI autonomous provider selection. |

---

**End of API Specification**
