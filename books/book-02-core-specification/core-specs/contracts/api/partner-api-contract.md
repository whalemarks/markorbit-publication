# API Contract — Partner API

**Spec ID:** B02-CONTRACT-API-PARTNER  
**Spec Type:** API Contract Specification  
**Contract Name:** Partner API Contract  
**Contract File:** core-specs/contracts/api/partner-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/partner-api.md  
**Related Domain:** Partner  
**Related Object Specs:** core-specs/objects/partner.md; core-specs/objects/customer.md; core-specs/objects/service-provider.md; core-specs/objects/service-network.md; core-specs/objects/routing.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/communication.md; core-specs/objects/document.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/partner-service.md; core-specs/services/customer-service.md; core-specs/services/service-provider-service.md; core-specs/services/service-network-service.md; core-specs/services/routing-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/communication-service.md; core-specs/services/document-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/partner-api.md; core-specs/api/customer-api.md; core-specs/api/service-provider-api.md; core-specs/api/service-network-api.md; core-specs/api/routing-api.md; core-specs/api/order-api.md; core-specs/api/matter-api.md; core-specs/api/communication-api.md; core-specs/api/document-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/partner-created.md; core-specs/events/service-network-linked.md; core-specs/events/routing-evaluated.md; core-specs/events/routing-selected.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/routing-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/task-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 5 — Partner / Network Expansion  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Partner API Contract defines the implementation-facing request and response contract for Partner API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, link and prepare Partner records through governed API boundaries without bypassing Partner Service, Service Network Service, Service Provider Service, Routing Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Partner API versioning
Partner create request
Partner update request
Partner read response
Partner search/list response
Partner reference validation
Partner relationship context
Partner service scope context
Partner customer/order/matter linkage
Partner service network linkage
Partner communication preparation
Partner routing context
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Partner API Contract does not approve partnership agreements, select providers, approve payment, create legal authority, create customer consent, send communications, replace Partner Service, evaluate Permission/Policy, or authorize AI output as final partnership decision.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Partner Service through governed API boundaries.
```

This contract does not mean:

```text
partnership agreement approval
revenue-share approval
legal representation
provider selection
payment approval
customer consent
external communication delivery
service network membership approval by itself
permission grant
policy approval
event emitter
partner portal UI
```

Core rule:

```text
Partner API receives governed partner requests.
Partner Service owns Partner behavior.
Service Network, Service Provider, Customer, Order, Matter and Routing references are validated by owning services.
Permission and Policy govern access.
Partner relationship use requires governed business process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Partner reference fields
partner relationship fields
partner service scope fields
network and provider link fields
customer/order/matter link fields
communication preparation fields
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
Partner lifecycle ownership outside Partner Service
partnership agreement execution
payment/revenue-share execution
provider routing selection
service network membership approval by itself
external message delivery
customer consent proof
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
core-specs/api/partner-api.md
```

Owning service spec:

```text
core-specs/services/partner-service.md
```

Related network/routing boundaries:

```text
core-specs/services/service-network-service.md
core-specs/services/routing-service.md
core-specs/services/service-provider-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Partner API, Partner Service, Service Network Service, Routing Service or Service Provider Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Partner
```

Related objects:

```text
Customer
ServiceProvider
ServiceNetwork
Routing
Order
Matter
Communication
Document
Permission
Policy
Event
Agent
```

Reference rules:

```text
- partner_reference_id identifies Partner.
- customer_reference_id may identify a customer-side partner relationship and must be validated by Customer Service.
- service_provider_reference_id may identify provider-side partner relationship and must be validated by Service Provider Service.
- service_network_reference_id must be validated by Service Network Service.
- routing_reference_id is owned by Routing Service and must not be selected by Partner API.
- Partner record does not prove contract authority, revenue-share approval or customer consent by itself.
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

Partner target context:

```yaml
target:
  partner_reference_id: string | null
  target_object_type: Partner
  target_object_reference_id: string | null
```

Rules:

```text
- partner_reference_id is required for read/update/validate/link operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- linked customer, provider, network, order, matter and document references must be validated where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/partners
GET    /v1/partners/{partner_reference_id}
PATCH  /v1/partners/{partner_reference_id}
GET    /v1/partners
POST   /v1/partners/validate-reference
POST   /v1/partners/{partner_reference_id}/link-relationships
POST   /v1/partners/{partner_reference_id}/link-network
POST   /v1/partners/{partner_reference_id}/prepare-communication
POST   /v1/partners/{partner_reference_id}/prepare-routing-context
```

Endpoint ownership:

```text
API layer validates request contract.
Partner Service executes Partner behavior.
Customer, Service Provider, Service Network, Order, Matter, Document and Routing services validate references where applicable.
Communication Service owns Communication creation/sending.
Routing Service owns routing evaluation and selection.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted preparation where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Partner Request Contract

Endpoint:

```text
POST /v1/partners
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
    - partner:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - partner:create:policy
  policy_decision_reference_id: string | null

payload:
  partner_type: string
  partner_status: string | null
  partner_name_safe: string
  partner_display_name_safe: string | null
  partner_level: string | null
  customer_reference_id: string | null
  service_provider_reference_id: string | null
  service_network_reference_ids:
    - string
  contact_name_safe: string | null
  contact_email_safe: string | null
  contact_phone_safe: string | null
  partner_scope_keys:
    - string
  document_reference_ids:
    - string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- partner_type and partner_name_safe are required.
- customer_reference_id must be validated by Customer Service where provided.
- service_provider_reference_id must be validated by Service Provider Service where provided.
- service_network_reference_ids must be validated by Service Network Service where provided.
- document_reference_ids must be validated by Document Service where provided.
- Partner Service assigns partner_reference_id.
```

---

# 9. Create Partner Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  partner_reference_id: string
  partner_type: string
  partner_status: string
  partner_name_safe: string
  partner_display_name_safe: string | null
  partner_level: string | null
  customer_reference_id: string | null
  service_provider_reference_id: string | null
  service_network_reference_ids_visible:
    - string
  partner_scope_keys_visible:
    - string
  created_at: datetime
  updated_at: datetime | null
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
- Response must not expose database IDs.
- PartnerCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate PartnerCreated event.
```

---

# 10. Read Partner Contract

Endpoint:

```text
GET /v1/partners/{partner_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  partner_reference_id: string
  partner_type: string
  partner_status: string
  partner_name_safe: string
  partner_display_name_safe: string | null
  partner_level: string | null
  customer_reference_id: string | null
  service_provider_reference_id: string | null
  service_network_reference_ids_visible:
    - string
  contact_name_visible: string | null
  contact_email_visible: string | null
  contact_phone_visible: string | null
  partner_scope_keys_visible:
    - string
  document_reference_ids_visible:
    - string
  relationship_status: string | null
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
- Read must evaluate partner:read permission.
- Policy may redact contacts, relationship details, commercial terms, documents, network links or scope keys.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Partner Contract

Endpoint:

```text
PATCH /v1/partners/{partner_reference_id}
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  partner_status: string | null
  partner_name_safe: string | null
  partner_display_name_safe: string | null
  partner_level: string | null
  contact_name_safe: string | null
  contact_email_safe: string | null
  contact_phone_safe: string | null
  partner_scope_keys_patch:
    - string
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - partner:update
policy_context:
  required_policy_scopes:
    - partner:update:policy
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
  partner_reference_id: string
  partner_status: string
  partner_name_safe: string
  partner_level: string | null
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Update must route through Partner Service.
- Relationship, scope, level or commercial-impacting updates may require human review.
- Restricted contact, agreement or commercial metadata must not be patched unless policy allows it.
```

---

# 12. Search/List Partner Contract

Endpoint:

```text
GET /v1/partners
```

Query parameters:

```yaml
partner_type: string | null
partner_status: string | null
partner_level: string | null
customer_reference_id: string | null
service_provider_reference_id: string | null
service_network_reference_id: string | null
partner_scope_key: string | null
relationship_status: string | null
safe_query: string | null
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
    - partner_reference_id: string
      partner_type: string
      partner_status: string
      partner_name_safe: string
      partner_level: string | null
      relationship_status: string | null
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
- Search must not reveal restricted Partner existence or restricted commercial terms.
- safe_query must not search private notes or protected contact details without policy allowance.
```

---

# 13. Validate Partner Reference Contract

Endpoint:

```text
POST /v1/partners/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  partner_reference_id: string
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
  partner_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  partner_type: string | null
  partner_status: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Partner.
- Valid reference does not imply partnership approval, routing selection or engagement authority.
- Validation status must follow Reference Contract.
- Policy may hide safe_label, type or status.
```

---

# 14. Link Relationships Contract

Endpoint:

```text
POST /v1/partners/{partner_reference_id}/link-relationships
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  relationship_links:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - partner:relationship:link
policy_context:
  required_policy_scopes:
    - partner:relationship:link:policy
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
  partner_reference_id: string
  relationship_links_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operation must route through Partner Service.
- Linked target references must be validated by owning services.
- Link operation does not mutate linked object lifecycle directly.
- Human review may be required where relationship affects responsibility or commercial terms.
```

---

# 15. Link Network Contract

Endpoint:

```text
POST /v1/partners/{partner_reference_id}/link-network
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  service_network_reference_ids:
    - string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - partner:network:link
policy_context:
  required_policy_scopes:
    - partner:network:link:policy
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
  partner_reference_id: string
  service_network_reference_ids_visible:
    - string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operation must route through Partner Service.
- Service Network references must be validated by Service Network Service.
- Network linkage does not approve membership, routing selection, payment or engagement by itself unless owning services confirm.
```

---

# 16. Prepare Communication Contract

Endpoint:

```text
POST /v1/partners/{partner_reference_id}/prepare-communication
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
    - partner:communication:prepare
policy_context:
  required_policy_scopes:
    - partner:communication:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  communication_purpose: string
  target_context:
    order_reference_id: string | null
    matter_reference_id: string | null
    routing_reference_id: string | null
  requested_channel: string | null
  include_draft: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  communication_preparation_status: string
  draft_subject_safe: string | null
  draft_body_safe: string | null
  communication_payload_hint_safe: object | null
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Communication preparation is assistance, not sending.
- Creating/sending Communication must route through Communication Service.
- Human review may be required before external partner communication.
```

---

# 17. Prepare Routing Context Contract

Endpoint:

```text
POST /v1/partners/{partner_reference_id}/prepare-routing-context
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
    - partner:routing-context:prepare
policy_context:
  required_policy_scopes:
    - partner:routing-context:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  routing_purpose: string
  target_context:
    order_reference_id: string | null
    matter_reference_id: string | null
    jurisdiction_reference_id: string | null
    service_scope_key: string | null
  include_network_context: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  routing_context_preparation_status: string
  partner_routing_context_safe: object | null
  suggested_constraints_safe: object | null
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
- Routing context preparation is assistance, not routing evaluation or selection.
- Routing evaluation/selection must route through Routing Service.
- AI must not select partner/provider.
- Human review may be required before routing-sensitive use.
```

---

# 18. Controlled Values

## 18.1 partner_type

```text
AgencyPartner
ReferralPartner
ServicePartner
NetworkPartner
ChannelPartner
TechnologyPartner
InternalPartner
Other
Unknown
```

## 18.2 partner_status

```text
Draft
Active
UnderReview
Suspended
Inactive
Archived
DeletedReferenceOnly
Unknown
```

## 18.3 partner_level

```text
Unknown
Standard
Preferred
Strategic
Restricted
Internal
```

## 18.4 partner_scope_key

```text
customer.referral
order.intake
service.delivery
provider.network
routing.support
communication.support
technology.integration
marketing.cooperation
unknown
```

## 18.5 relationship_status

```text
Unknown
Prospective
Active
Paused
Disputed
Terminated
Archived
```

## 18.6 relationship_type

```text
CustomerRelation
ServiceProviderRelation
ServiceNetworkRelation
ReferralRelation
OrderRelation
MatterRelation
RoutingRelation
CommunicationRelation
DocumentRelation
HistoricalReference
Unknown
```

## 18.7 target_object_type

```text
Customer
ServiceProvider
ServiceNetwork
Order
Matter
Routing
Communication
Document
Unknown
```

## 18.8 communication_preparation_status

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

## 18.9 routing_context_preparation_status

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

## 18.10 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
Suspended
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 18.11 sort.field

```text
created_at
updated_at
partner_name_safe
partner_status
partner_type
partner_level
relationship_status
```

---

# 19. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] partner_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] partner_type is controlled.
[ ] partner_status is controlled where provided.
[ ] partner_level is controlled where provided.
[ ] partner_scope_keys are controlled where provided.
[ ] customer_reference_id is validated where provided.
[ ] service_provider_reference_id is validated where provided.
[ ] service_network_reference_ids are validated where provided.
[ ] relationship links are validated where provided.
[ ] document references are validated where provided.
[ ] AI Context is present for AI-assisted communication/routing preparation.
[ ] Human Review Context is present where policy requires review.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 20. Permission Rules

Required permission keys:

```text
partner:create
partner:read
partner:search
partner:update
partner:validate
partner:relationship:link
partner:network:link
partner:communication:prepare
partner:routing-context:prepare
```

Rules:

```text
- Partner API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 21. Policy Rules

Required policy scopes may include:

```text
partner:create:policy
partner:read:policy
partner:search:policy
partner:update:policy
partner:reference:policy
partner:visibility:policy
partner:contact:visibility:policy
partner:relationship:link:policy
partner:network:link:policy
partner:communication:prepare:policy
partner:routing-context:prepare:policy
partner:commercial-terms:visibility:policy
cross-organization:partner
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact contacts, agreement terms, commercial data, relationship details, network links, summaries or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before partnership use, routing context use or external communication.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 22. AI and Human Review Rules

AI rules:

```text
- AI may summarize Partner context and prepare communication/routing context drafts only within Permission and Policy limits.
- AI must not approve partnerships, select providers, approve payment, approve engagement, create customer consent or send communications.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Partner output is used for routing, partnership decision, commercial terms, external communication, payment-impacting action or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 23. Idempotency and Event Rules

Idempotency:

```text
POST /v1/partners requires idempotency_key.
PATCH /v1/partners/{partner_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Relationship/network link endpoints may require idempotency_key for duplicate-sensitive operations.
Preparation endpoints do not normally require idempotency unless result is persisted.
```

Events:

```text
PartnerCreated may be emitted by Partner Service after successful creation.
ServiceNetworkLinked may be emitted by Service Network Service or owning linking service where event spec applies.
RoutingEvaluated and RoutingSelected may only be emitted by Routing Service.
CommunicationCreated may only be emitted by Communication Service.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 24. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
PartnerReferenceInvalid
CustomerReferenceInvalid
ServiceProviderReferenceInvalid
ServiceNetworkReferenceInvalid
OrderReferenceInvalid
MatterReferenceInvalid
RoutingReferenceInvalid
DocumentReferenceInvalid
PartnerScopeInvalid
RelationshipLinkInvalid
NetworkLinkInvalid
CommunicationPreparationUnavailable
RoutingContextPreparationUnavailable
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
- Errors must not expose database IDs, restricted partner data, private contacts, agreement terms, commercial terms, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 25. Versioning Rules

Version fields:

```yaml
api_version: v1
contract_version: v0.1.0
schema_version: v0.1.0
```

Rules:

```text
- Unsupported API or contract versions must fail closed.
- Breaking changes require contract version bump.
- Response payloads must preserve version fields.
```

---

# 26. Codex Implementation Notes

Codex must:

```text
cite Partner API Spec
cite Partner Service Spec
cite Service Network Service Spec where network context is used
cite Routing Service Spec where routing context is used
cite this Partner API Contract
use Reference Contract for partner_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted communication/routing preparation
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link operations
use Versioning Contract for version validation
route all Partner mutation through Partner Service
invoke Customer/Service Provider/Service Network/Order/Matter/Routing/Document services for reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing contacts, relationship details, network links, commercial terms or summaries
return safe errors only
write tests for create/read/update/search/validate-reference/link-relationships/link-network/prepare-communication/prepare-routing-context
write tests for customer/provider/network/document reference validation
write tests that communication preparation does not send communication
write tests that routing context preparation does not evaluate or select routing
write tests for partnership/commercial updates requiring human review
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Partner directly in API layer
query database directly from API contract implementation
use generic id where partner_reference_id is required
expose database IDs, private contacts, agreement terms or commercial terms without policy allowance
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
select providers from Partner API
approve partnership agreements, engagement or payments from this API contract
send external communication from preparation endpoint
treat AI routing context as RoutingSelected
allow AI context to exceed evaluated_data_access_scope
```

---

# 27. Acceptance Criteria

This Partner API Contract is accepted only if:

```text
[ ] It defines Partner API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Partner API and Service specs.
[ ] It defines related Network and Routing boundaries.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines link relationships contract.
[ ] It defines link network contract.
[ ] It defines prepare communication contract.
[ ] It defines prepare routing context contract.
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

# 28. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Partner API Contract. Defines governed create, read, update, search, validate-reference, relationship/network linkage, communication preparation and routing-context preparation payloads, linked reference validation, Network/Routing boundaries, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
