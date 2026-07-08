# API Contract — Routing API

**Spec ID:** B02-CONTRACT-API-ROUTING  
**Spec Type:** API Contract Specification  
**Contract Name:** Routing API Contract  
**Contract File:** core-specs/contracts/api/routing-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/routing-api.md  
**Related Domain:** Routing  
**Related Object Specs:** core-specs/objects/routing.md; core-specs/objects/service-provider.md; core-specs/objects/service-network.md; core-specs/objects/partner.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/jurisdiction.md; core-specs/objects/communication.md; core-specs/objects/document.md; core-specs/objects/agent.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/routing-service.md; core-specs/services/service-provider-service.md; core-specs/services/service-network-service.md; core-specs/services/partner-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/communication-service.md; core-specs/services/document-service.md; core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/routing-api.md; core-specs/api/service-provider-api.md; core-specs/api/service-network-api.md; core-specs/api/partner-api.md; core-specs/api/order-api.md; core-specs/api/matter-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/communication-api.md; core-specs/api/document-api.md; core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/routing-evaluated.md; core-specs/events/routing-selected.md; core-specs/events/service-provider-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/routing-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 4 — Collaboration Network Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Routing API Contract defines the implementation-facing request and response contract for Routing API operations in MarkOrbit Core.

It standardizes how clients create, read, search, validate, evaluate, compare, prepare recommendation and select Routing records through governed API boundaries without bypassing Routing Service, Service Provider Service, Service Network Service, Partner Service, Permission Service, Policy Service, Human Review rules or Event Service.

This contract governs:

```text
Routing API versioning
Routing evaluation request
Routing evaluation response
Routing read response
Routing search/list response
Routing reference validation
Candidate provider context
Routing comparison context
Routing recommendation preparation
Routing selection request/response
Order and Matter target context
Jurisdiction and service scope context
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Routing API Contract does not select providers silently, approve engagement, approve payment, create supplier contracts, send communications, create legal authority, replace Routing Service, evaluate Permission/Policy, or authorize AI output as final routing decision.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Routing Service through governed API boundaries.
```

This contract does not mean:

```text
provider selection by itself
engagement approval
payment approval
supplier contract
legal authority certification
external communication delivery
service provider lifecycle ownership
permission grant
policy approval
event emitter
vendor marketplace UI
```

Core rule:

```text
Routing API receives governed routing requests.
Routing Service owns routing evaluation and selection.
Service Provider, Service Network, Partner, Order, Matter and Jurisdiction references are validated by owning services.
Permission and Policy govern access.
Routing Agent may compare and recommend, but must not select.
Routing selection requires explicit governed decision and trace.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Routing reference fields
routing target fields
candidate provider fields
comparison and scoring fields
recommendation preparation fields
selection fields
pagination shape for list/search
permission/policy context requirements
AI and human-review context requirements
idempotency requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
Service Provider lifecycle ownership
provider engagement approval
contract execution
payment approval
external communication sending
order/matter lifecycle completion
Permission evaluation logic
Policy evaluation logic
Event emission implementation
database schema design
UI rendering
```

---

# 4. Related Owning Spec

Owning API spec:

```text
core-specs/api/routing-api.md
```

Owning service spec:

```text
core-specs/services/routing-service.md
```

Related agent boundary:

```text
core-specs/agents/routing-agent.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Routing API, Routing Service or Routing Agent responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Routing
```

Related objects:

```text
ServiceProvider
ServiceNetwork
Partner
Order
Matter
Jurisdiction
Communication
Document
Agent
Permission
Policy
Event
```

Reference rules:

```text
- routing_reference_id identifies Routing evaluation or selection record.
- service_provider_reference_id identifies candidate or selected provider and must be validated by Service Provider Service.
- order_reference_id and matter_reference_id must be validated by owning services where provided.
- jurisdiction_reference_id must be validated by Jurisdiction Service where provided.
- routing evaluation does not equal routing selection.
- routing recommendation does not equal routing selection.
- RoutingSelected requires explicit governed selection.
```

---

# 6. Required References

Common API context:

```yaml
api_context:
  api_version: v1
  contract_version: v0.1.0
  correlation_id: string | null
  idempotency_key: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
```

Routing target context:

```yaml
target:
  routing_reference_id: string | null
  target_object_type: Routing
  target_object_reference_id: string | null
```

Rules:

```text
- routing_reference_id is required for read/validate/select-from-existing operations.
- idempotency_key is required for evaluate and select operations where a Routing record is created.
- actor_reference_id or governed system/agent context is required for protected operations.
- target and candidate references must be validated by owning services where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/routing/evaluate
GET    /v1/routing/{routing_reference_id}
GET    /v1/routing
POST   /v1/routing/validate-reference
POST   /v1/routing/{routing_reference_id}/compare-candidates
POST   /v1/routing/{routing_reference_id}/prepare-recommendation
POST   /v1/routing/{routing_reference_id}/select
POST   /v1/routing/prepare-provider-query
```

Endpoint ownership:

```text
API layer validates request contract.
Routing Service executes Routing evaluation and selection behavior.
Service Provider, Service Network, Partner, Order, Matter, Jurisdiction and Document services validate references where applicable.
Agent Service governs Routing Agent context.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Event Service records events emitted by owning services.
API layer must not select provider without Routing Service.
```

---

# 8. Evaluate Routing Request Contract

Endpoint:

```text
POST /v1/routing/evaluate
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string
actor_reference_id: string | null
organization_reference_id: string | null

permission_context:
  required_permission_keys:
    - routing:evaluate
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - routing:evaluate:policy
  policy_decision_reference_id: string | null

payload:
  routing_type: string
  routing_purpose: string
  target_context:
    order_reference_id: string | null
    matter_reference_id: string | null
    jurisdiction_reference_id: string | null
    service_scope_key: string | null
  candidate_constraints:
    service_provider_reference_ids:
      - string
    service_network_reference_ids:
      - string
    partner_reference_ids:
      - string
    language_codes:
      - string
  evaluation_criteria:
    - criterion_key: string
      weight: number | null
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- routing_type and routing_purpose are required.
- target_context must include enough context for Routing Service to evaluate.
- candidate references must be validated by owning services where provided.
- evaluation_criteria must be controlled.
- Routing Service assigns routing_reference_id.
```

---

# 9. Evaluate Routing Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  routing_reference_id: string
  routing_type: string
  routing_status: string
  routing_purpose: string
  candidate_results_visible:
    - service_provider_reference_id: string
      match_status: string
      score_band: string | null
      match_summary_safe: string | null
      restricted_fields_omitted: boolean
  recommended_service_provider_reference_id: string | null
  recommendation_basis_safe: string | null
  human_review_required: boolean
  created_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
idempotency_result:
  idempotency_key: string
  idempotency_status: string
  replayed: boolean
```

Rules:

```text
- RoutingEvaluated event reference may be included where policy allows it.
- recommended_service_provider_reference_id is recommendation only.
- Evaluation response must not imply provider selection.
- Replayed idempotent response must not duplicate RoutingEvaluated event.
```

---

# 10. Read Routing Contract

Endpoint:

```text
GET /v1/routing/{routing_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  routing_reference_id: string
  routing_type: string
  routing_status: string
  routing_purpose: string
  target_context_visible:
    order_reference_id: string | null
    matter_reference_id: string | null
    jurisdiction_reference_id: string | null
    service_scope_key: string | null
  candidate_results_visible:
    - service_provider_reference_id: string
      match_status: string
      score_band: string | null
      match_summary_safe: string | null
      restricted_fields_omitted: boolean
  recommended_service_provider_reference_id: string | null
  selected_service_provider_reference_id: string | null
  selection_status: string | null
  selected_at: datetime | null
  metadata_safe: object | null
  created_at: datetime | null
  updated_at: datetime | null
  restricted_fields_omitted: boolean
permission_context:
  permission_decision_reference_id: string | null
policy_context:
  policy_decision_reference_id: string | null
```

Rules:

```text
- Read must evaluate routing:read permission.
- Policy may redact candidate scores, summaries, commercial context, target details or selected provider.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Search/List Routing Contract

Endpoint:

```text
GET /v1/routing
```

Query parameters:

```yaml
routing_type: string | null
routing_status: string | null
selection_status: string | null
order_reference_id: string | null
matter_reference_id: string | null
jurisdiction_reference_id: string | null
service_provider_reference_id: string | null
service_scope_key: string | null
created_after: datetime | null
created_before: datetime | null
pagination:
  cursor: string | null
  limit: integer | null
  sort:
    field: string | null
    direction: Asc | Desc | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  items:
    - routing_reference_id: string
      routing_type: string
      routing_status: string
      routing_purpose: string
      selection_status: string | null
      recommended_service_provider_reference_id: string | null
      selected_service_provider_reference_id: string | null
      created_at: datetime
      restricted_fields_omitted: boolean
  pagination:
    next_cursor: string | null
    previous_cursor: string | null
    limit: integer
    returned_count: integer
    has_more: boolean
    total_count: integer | null
    total_count_omitted: boolean
```

Rules:

```text
- Pagination must follow Pagination Contract.
- total_count must be omitted where policy or security requires it.
- Search must not reveal restricted Routing existence, restricted candidate lists or commercial terms.
```

---

# 12. Validate Routing Reference Contract

Endpoint:

```text
POST /v1/routing/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  routing_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  routing_reference_id: string
  valid: boolean
  validation_status: string
  routing_type: string | null
  routing_status: string | null
  selection_status: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Routing.
- Valid reference does not imply provider selection.
- Validation status must follow Reference Contract.
- Policy may hide routing type, status or selection status.
```

---

# 13. Compare Candidates Contract

Endpoint:

```text
POST /v1/routing/{routing_reference_id}/compare-candidates
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
permission_context:
  required_permission_keys:
    - routing:candidates:compare
policy_context:
  required_policy_scopes:
    - routing:candidates:compare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  service_provider_reference_ids:
    - string
  comparison_scope: string | null
  include_recommendation: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  comparison_status: string
  candidate_comparisons_visible:
    - service_provider_reference_id: string
      comparison_summary_safe: string | null
      score_band: string | null
      strengths_safe:
        - string
      risks_safe:
        - string
      restricted_fields_omitted: boolean
  recommendation_summary_safe: string | null
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Candidate comparison is assistance unless routed through Routing Service decision flow.
- Routing Agent may compare but must not select.
- Policy may redact commercial terms, contacts, scores or risk details.
```

---

# 14. Prepare Recommendation Contract

Endpoint:

```text
POST /v1/routing/{routing_reference_id}/prepare-recommendation
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
permission_context:
  required_permission_keys:
    - routing:recommendation:prepare
policy_context:
  required_policy_scopes:
    - routing:recommendation:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: RoutingAgent | null
payload:
  recommendation_purpose: string
  preferred_service_provider_reference_id: string | null
  include_customer_facing_summary: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  recommendation_preparation_status: string
  recommended_service_provider_reference_id: string | null
  recommendation_basis_safe: string | null
  customer_facing_summary_safe: string | null
  missing_context_safe:
    - string
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Recommendation preparation is assistance, not selection.
- Customer-facing summary may require human review.
- Preferred provider input must be validated but does not force recommendation.
```

---

# 15. Select Routing Contract

Endpoint:

```text
POST /v1/routing/{routing_reference_id}/select
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  selected_service_provider_reference_id: string
  selection_reason_safe: string | null
  selection_scope: string
permission_context:
  required_permission_keys:
    - routing:select
policy_context:
  required_policy_scopes:
    - routing:select:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  routing_reference_id: string
  previous_selection_status: string | null
  selection_status: string
  selected_service_provider_reference_id: string
  selected_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
idempotency_result:
  idempotency_key: string
  idempotency_status: string
  replayed: boolean
```

Rules:

```text
- Select requires idempotency_key.
- Select must route through Routing Service.
- selected_service_provider_reference_id must be validated and must belong to eligible candidate set unless policy/service allows exception.
- Human review may be required for selection.
- RoutingSelected event may be emitted by Routing Service.
- Selection does not approve contract, payment, external communication or filing.
```

---

# 16. Prepare Provider Query Contract

Endpoint:

```text
POST /v1/routing/prepare-provider-query
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
permission_context:
  required_permission_keys:
    - routing:provider-query:prepare
policy_context:
  required_policy_scopes:
    - routing:provider-query:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  query_purpose: string
  target_context:
    order_reference_id: string | null
    matter_reference_id: string | null
    jurisdiction_reference_id: string | null
    service_scope_key: string | null
  include_candidate_filters: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  provider_query_preparation_status: string
  provider_query_filters_safe: object | null
  missing_context_safe:
    - string
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Provider query preparation is assistance, not evaluation or selection.
- Generated filters must remain within Permission and Policy limits.
- Human review may be required before using query for selection-sensitive routing.
```

---

# 17. Controlled Values

## 17.1 routing_type

```text
ProviderRouting
JurisdictionRouting
ServiceScopeRouting
PartnerRouting
NetworkRouting
FallbackRouting
InternalRouting
Unknown
```

## 17.2 routing_status

```text
Draft
Evaluated
PartiallyEvaluated
SelectionPrepared
Selected
Rejected
Expired
Archived
DeletedReferenceOnly
Unknown
```

## 17.3 selection_status

```text
NotSelected
RecommendationPrepared
Selected
Rejected
Superseded
Cancelled
Unknown
```

## 17.4 match_status

```text
Matched
PartiallyMatched
NotMatched
Restricted
Unavailable
Unknown
```

## 17.5 score_band

```text
High
Medium
Low
Unknown
Hidden
```

## 17.6 criterion_key

```text
jurisdictionCoverage
serviceScopeFit
languageFit
networkFit
historicalPerformance
availability
costBand
riskLevel
relationshipFit
manualPriority
unknown
```

## 17.7 service_scope_key

```text
trademark.application
trademark.search
trademark.oa-response
trademark.renewal
trademark.assignment
trademark.change-recordal
trademark.opposition
trademark.cancellation
trademark.evidence
translation
document.legalization
investigation
unknown
```

## 17.8 comparison_status

```text
Completed
Partial
InsufficientContext
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 17.9 recommendation_preparation_status

```text
Completed
Partial
InsufficientContext
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 17.10 provider_query_preparation_status

```text
Completed
Partial
InsufficientContext
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 17.11 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
Expired
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 17.12 sort.field

```text
created_at
updated_at
routing_status
selection_status
routing_type
selected_at
```

---

# 18. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] routing_reference_id is valid where required.
[ ] idempotency_key is present for evaluate and select.
[ ] routing_type is controlled.
[ ] routing_status is controlled where provided.
[ ] target context references are validated where provided.
[ ] candidate provider/network/partner references are validated where provided.
[ ] selected provider is valid and eligible.
[ ] service_scope_key is controlled where provided.
[ ] evaluation criteria are controlled.
[ ] AI Context is present for AI-assisted compare/recommend/query preparation.
[ ] Human Review Context is present where policy requires review.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 19. Permission Rules

Required permission keys:

```text
routing:evaluate
routing:read
routing:search
routing:validate
routing:candidates:compare
routing:recommendation:prepare
routing:select
routing:provider-query:prepare
```

Rules:

```text
- Routing API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 20. Policy Rules

Required policy scopes may include:

```text
routing:evaluate:policy
routing:read:policy
routing:search:policy
routing:reference:policy
routing:candidates:compare:policy
routing:recommendation:prepare:policy
routing:select:policy
routing:provider-query:prepare:policy
routing:candidate:visibility:policy
routing:commercial-terms:visibility:policy
cross-organization:routing
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact candidate providers, score bands, commercial terms, comparison details, recommendation basis, selected provider or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before selection or customer-facing recommendation.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 21. AI and Human Review Rules

AI rules:

```text
- Routing Agent may read, summarize, compare, suggest and prepare only within Permission and Policy limits.
- Routing Agent output is routing assistance, not RoutingSelected.
- AI must not select providers, approve engagement, approve payments, send communications or verify legal authority.
- AI output must disclose candidate basis, source scope, missing context, restricted omissions and human-review requirements.
```

Human review:

```text
- Human review may be required where Routing output is used for provider selection, engagement, contract approval, payment-impacting action, external communication or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 22. Idempotency and Event Rules

Idempotency:

```text
POST /v1/routing/evaluate requires idempotency_key.
POST /v1/routing/{routing_reference_id}/select requires idempotency_key.
Compare/recommend/query preparation endpoints do not normally require idempotency unless result is persisted.
```

Events:

```text
RoutingEvaluated may be emitted by Routing Service after successful evaluation.
RoutingSelected may be emitted by Routing Service after successful selection.
CommunicationCreated may only be emitted by Communication Service.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate RoutingEvaluated or RoutingSelected events.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 23. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
RoutingReferenceInvalid
ServiceProviderReferenceInvalid
ServiceNetworkReferenceInvalid
PartnerReferenceInvalid
OrderReferenceInvalid
MatterReferenceInvalid
JurisdictionReferenceInvalid
ServiceScopeInvalid
CandidateSetInvalid
EvaluationUnavailable
ComparisonUnavailable
RecommendationUnavailable
ProviderQueryPreparationUnavailable
SelectionInvalid
SelectionConflict
HumanReviewRequired
StateInvalid
IdempotencyKeyRequired
IdempotencyConflict
VersionUnsupported
InternalError
```

Safe error shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Errors must not expose database IDs, restricted candidate data, commercial terms, private notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 24. Versioning Rules

Version fields:

```yaml
api_version: v1
contract_version: v0.1.0
schema_version: v0.1.0
routing_evaluation_version: v0.1.0
```

Rules:

```text
- Unsupported API or contract versions must fail closed.
- Routing evaluation version must be recorded where selection relies on evaluation.
- Breaking changes require contract version bump.
- Response payloads must preserve version fields.
```

---

# 25. Codex Implementation Notes

Codex must:

```text
cite Routing API Spec
cite Routing Service Spec
cite Routing Agent Spec
cite Service Provider Service Spec where provider references are used
cite this Routing API Contract
use Reference Contract for routing_reference_id, candidate references and target references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted compare/recommend/query preparation
use Human Review Contract where policy requires review
use Idempotency Contract for evaluate and select
use Versioning Contract for version validation
route all Routing evaluation and selection through Routing Service
invoke Service Provider/Service Network/Partner/Order/Matter/Jurisdiction services for reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing candidates, scores, commercial terms or recommendation basis
return safe errors only
write tests for evaluate/read/search/validate-reference/compare-candidates/prepare-recommendation/select/prepare-provider-query
write tests for candidate reference validation
write tests that recommendation preparation does not select provider
write tests that Routing Agent cannot select provider
write tests that select requires idempotency_key
write tests that duplicate select does not duplicate RoutingSelected event
write tests for human_review_required on selection
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Routing directly in API layer
query database directly from API contract implementation
use generic id where routing_reference_id is required
expose database IDs, restricted candidates, private notes or commercial terms without policy allowance
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
select provider from compare or prepare-recommendation endpoints
approve engagement, contract or payment from Routing API
send communication from Routing API
treat AI recommendation as RoutingSelected
allow AI context to exceed evaluated_data_access_scope
```

---

# 26. Acceptance Criteria

This Routing API Contract is accepted only if:

```text
[ ] It defines Routing API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Routing API, Routing Service and Routing Agent specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines evaluate request/response.
[ ] It defines read contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines compare candidates contract.
[ ] It defines prepare recommendation contract.
[ ] It defines select routing contract.
[ ] It defines prepare provider query contract.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI and Human Review rules.
[ ] It defines idempotency and event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Routing API Contract. Defines governed evaluate, read, search, validate-reference, compare, recommendation preparation, provider query preparation and selection payloads, candidate/reference validation, Routing Agent boundary, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
