# API Contract — Service Provider API

**Spec ID:** B02-CONTRACT-API-SERVICE-PROVIDER  
**Spec Type:** API Contract Specification  
**Contract Name:** Service Provider API Contract  
**Contract File:** core-specs/contracts/api/service-provider-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/service-provider-api.md  
**Related Domain:** Service Provider  
**Related Object Specs:** core-specs/objects/service-provider.md; core-specs/objects/agent.md; core-specs/objects/routing.md; core-specs/objects/service-network.md; core-specs/objects/partner.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/jurisdiction.md; core-specs/objects/communication.md; core-specs/objects/document.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/service-provider-service.md; core-specs/services/agent-service.md; core-specs/services/routing-service.md; core-specs/services/service-network-service.md; core-specs/services/partner-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/communication-service.md; core-specs/services/document-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/service-provider-api.md; core-specs/api/agent-api.md; core-specs/api/routing-api.md; core-specs/api/service-network-api.md; core-specs/api/partner-api.md; core-specs/api/order-api.md; core-specs/api/matter-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/communication-api.md; core-specs/api/document-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/service-provider-created.md; core-specs/events/routing-evaluated.md; core-specs/events/routing-selected.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
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

Service Provider API Contract defines the implementation-facing request and response contract for Service Provider API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, qualify, link and prepare Service Provider records through governed API boundaries without bypassing Service Provider Service, Routing Service, Service Network Service, Partner Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Service Provider API versioning
Service Provider create request
Service Provider update request
Service Provider read response
Service Provider search/list response
Service Provider reference validation
Provider capability and coverage context
Provider jurisdiction and service scope context
Provider qualification preparation
Provider communication preparation
Routing and selection boundary
Service Network linkage
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Service Provider API Contract does not select providers by itself, approve engagement, approve payment, create legal authority, send communications, replace Routing Service, replace Service Provider Service, evaluate Permission/Policy, or authorize AI output as final provider decision.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Service Provider Service through governed API boundaries.
```

This contract does not mean:

```text
provider selection approval
supplier contract approval
payment approval
legal authority verification by itself
routing decision
service network membership approval by itself
external communication delivery
permission grant
policy approval
event emitter
vendor portal UI
```

Core rule:

```text
Service Provider API receives governed provider requests.
Service Provider Service owns Service Provider behavior.
Routing Service owns routing evaluation and selection.
Service Network and Partner references are validated by owning services.
Permission and Policy govern access.
Provider engagement requires governed business process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Service Provider reference fields
provider capability fields
jurisdiction and service coverage fields
qualification preparation fields
communication preparation fields
relationship link fields
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
Service Provider lifecycle ownership outside Service Provider Service
provider routing selection
contract approval
payment approval
legal authority certification
external message delivery
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
core-specs/api/service-provider-api.md
```

Owning service spec:

```text
core-specs/services/service-provider-service.md
```

Related routing boundary:

```text
core-specs/services/routing-service.md
core-specs/agents/routing-agent.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Service Provider API, Service Provider Service, Routing Service or Routing Agent responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
ServiceProvider
```

Related objects:

```text
Agent
Routing
ServiceNetwork
Partner
Order
Matter
Jurisdiction
Communication
Document
Permission
Policy
Event
```

Reference rules:

```text
- service_provider_reference_id identifies Service Provider.
- jurisdiction_reference_ids describe coverage and must be validated by Jurisdiction Service where provided.
- service_network_reference_id must be validated by Service Network Service where provided.
- partner_reference_id must be validated by Partner Service where provided.
- routing_reference_id is owned by Routing Service and must not be created or selected by this API contract alone.
- Service Provider record does not prove legal authority, contract approval or payment approval by itself.
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

Service Provider target context:

```yaml
target:
  service_provider_reference_id: string | null
  target_object_type: ServiceProvider
  target_object_reference_id: string | null
```

Rules:

```text
- service_provider_reference_id is required for read/update/validate/qualify/link operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- linked jurisdiction, partner, service network and document references must be validated where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/service-providers
GET    /v1/service-providers/{service_provider_reference_id}
PATCH  /v1/service-providers/{service_provider_reference_id}
GET    /v1/service-providers
POST   /v1/service-providers/validate-reference
POST   /v1/service-providers/{service_provider_reference_id}/link-coverage
POST   /v1/service-providers/{service_provider_reference_id}/link-network
POST   /v1/service-providers/{service_provider_reference_id}/prepare-qualification
POST   /v1/service-providers/{service_provider_reference_id}/prepare-communication
```

Endpoint ownership:

```text
API layer validates request contract.
Service Provider Service executes Service Provider behavior.
Jurisdiction, Partner, Service Network, Document and Communication services validate references where applicable.
Routing Service owns routing evaluation and selection.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted qualification/communication preparation where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Service Provider Request Contract

Endpoint:

```text
POST /v1/service-providers
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
    - service-provider:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - service-provider:create:policy
  policy_decision_reference_id: string | null

payload:
  service_provider_type: string
  service_provider_status: string | null
  provider_name_safe: string
  provider_display_name_safe: string | null
  contact_name_safe: string | null
  contact_email_safe: string | null
  contact_phone_safe: string | null
  jurisdiction_reference_ids:
    - string
  service_scope_keys:
    - string
  language_codes:
    - string
  service_network_reference_ids:
    - string
  partner_reference_id: string | null
  document_reference_ids:
    - string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- service_provider_type and provider_name_safe are required.
- jurisdiction_reference_ids must be validated by Jurisdiction Service where provided.
- service_network_reference_ids must be validated by Service Network Service where provided.
- partner_reference_id must be validated by Partner Service where provided.
- contact fields are safe contact fields and do not prove authority.
- Service Provider Service assigns service_provider_reference_id.
```

---

# 9. Create Service Provider Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  service_provider_reference_id: string
  service_provider_type: string
  service_provider_status: string
  provider_name_safe: string
  provider_display_name_safe: string | null
  jurisdiction_reference_ids_visible:
    - string
  service_scope_keys_visible:
    - string
  service_network_reference_ids_visible:
    - string
  partner_reference_id: string | null
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
- ServiceProviderCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate ServiceProviderCreated event.
```

---

# 10. Read Service Provider Contract

Endpoint:

```text
GET /v1/service-providers/{service_provider_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  service_provider_reference_id: string
  service_provider_type: string
  service_provider_status: string
  provider_name_safe: string
  provider_display_name_safe: string | null
  contact_name_visible: string | null
  contact_email_visible: string | null
  contact_phone_visible: string | null
  jurisdiction_reference_ids_visible:
    - string
  service_scope_keys_visible:
    - string
  language_codes_visible:
    - string
  service_network_reference_ids_visible:
    - string
  partner_reference_id: string | null
  document_reference_ids_visible:
    - string
  qualification_status: string | null
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
- Read must evaluate service-provider:read permission.
- Policy may redact contact fields, qualification details, document references, commercial terms or coverage details.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Service Provider Contract

Endpoint:

```text
PATCH /v1/service-providers/{service_provider_reference_id}
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
  service_provider_status: string | null
  provider_name_safe: string | null
  provider_display_name_safe: string | null
  contact_name_safe: string | null
  contact_email_safe: string | null
  contact_phone_safe: string | null
  service_scope_keys_patch:
    - string
  language_codes_patch:
    - string
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - service-provider:update
policy_context:
  required_policy_scopes:
    - service-provider:update:policy
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
  service_provider_reference_id: string
  service_provider_status: string
  provider_name_safe: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Update must route through Service Provider Service.
- Capability and coverage changes may require human review.
- Restricted contact, commercial or qualification metadata must not be patched unless policy allows it.
```

---

# 12. Search/List Service Provider Contract

Endpoint:

```text
GET /v1/service-providers
```

Query parameters:

```yaml
service_provider_type: string | null
service_provider_status: string | null
jurisdiction_reference_id: string | null
service_scope_key: string | null
service_network_reference_id: string | null
partner_reference_id: string | null
language_code: string | null
qualification_status: string | null
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
    - service_provider_reference_id: string
      service_provider_type: string
      service_provider_status: string
      provider_name_safe: string
      jurisdiction_reference_ids_visible:
        - string
      service_scope_keys_visible:
        - string
      qualification_status: string | null
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
- Search must not reveal restricted Service Provider existence or restricted commercial terms.
- safe_query must not search private notes or protected contact details without policy allowance.
```

---

# 13. Validate Service Provider Reference Contract

Endpoint:

```text
POST /v1/service-providers/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  service_provider_reference_id: string
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
  service_provider_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  service_provider_type: string | null
  service_provider_status: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Service Provider.
- Valid reference does not imply provider may be selected.
- Validation status must follow Reference Contract.
- Policy may hide safe_label, type or status.
```

---

# 14. Link Coverage Contract

Endpoint:

```text
POST /v1/service-providers/{service_provider_reference_id}/link-coverage
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  jurisdiction_reference_ids:
    - string
  service_scope_keys:
    - string
  language_codes:
    - string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - service-provider:coverage:link
policy_context:
  required_policy_scopes:
    - service-provider:coverage:link:policy
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
  service_provider_reference_id: string
  jurisdiction_reference_ids_visible:
    - string
  service_scope_keys_visible:
    - string
  language_codes_visible:
    - string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operation must route through Service Provider Service.
- Jurisdiction references must be validated by Jurisdiction Service.
- Coverage linkage does not prove authority, capability or selection approval by itself.
- Human review may be required for coverage expansion.
```

---

# 15. Link Network Contract

Endpoint:

```text
POST /v1/service-providers/{service_provider_reference_id}/link-network
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
  partner_reference_id: string | null
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - service-provider:network:link
policy_context:
  required_policy_scopes:
    - service-provider:network:link:policy
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
  service_provider_reference_id: string
  service_network_reference_ids_visible:
    - string
  partner_reference_id: string | null
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operation must route through Service Provider Service.
- Service Network and Partner references must be validated by owning services.
- Network linkage does not create selection, contract or payment approval by itself.
```

---

# 16. Prepare Qualification Contract

Endpoint:

```text
POST /v1/service-providers/{service_provider_reference_id}/prepare-qualification
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
    - service-provider:qualification:prepare
policy_context:
  required_policy_scopes:
    - service-provider:qualification:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  qualification_purpose: string
  target_context:
    order_reference_id: string | null
    matter_reference_id: string | null
    jurisdiction_reference_id: string | null
  requested_service_scope_key: string | null
  include_routing_context: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  qualification_preparation_status: string
  provider_summary_safe: string | null
  capability_match_summary_safe: string | null
  missing_context_safe:
    - string
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Qualification preparation is assistance, not selection.
- Routing evaluation and selection must route through Routing Service.
- AI must not certify provider capability or legal authority.
- Human review may be required before routing/selection or external use.
```

---

# 17. Prepare Communication Contract

Endpoint:

```text
POST /v1/service-providers/{service_provider_reference_id}/prepare-communication
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
    - service-provider:communication:prepare
policy_context:
  required_policy_scopes:
    - service-provider:communication:prepare:policy
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
- Human review may be required before external communication.
```

---

# 18. Controlled Values

## 18.1 service_provider_type

```text
LawFirm
TrademarkAgency
IndividualAttorney
LocalAssociate
OfficialServiceProvider
TranslationProvider
DocumentProvider
InvestigationProvider
InternalProvider
Other
Unknown
```

## 18.2 service_provider_status

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

## 18.3 service_scope_key

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

## 18.4 qualification_status

```text
Unknown
Unqualified
PreQualified
Qualified
Preferred
Restricted
Suspended
UnderReview
```

## 18.5 qualification_preparation_status

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

## 18.6 communication_preparation_status

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

## 18.7 validation_status

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

## 18.8 sort.field

```text
created_at
updated_at
provider_name_safe
service_provider_status
service_provider_type
qualification_status
```

---

# 19. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] service_provider_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] service_provider_type is controlled.
[ ] service_provider_status is controlled where provided.
[ ] service_scope_keys are controlled where provided.
[ ] jurisdiction_reference_ids are validated where provided.
[ ] service_network_reference_ids are validated where provided.
[ ] partner_reference_id is validated where provided.
[ ] document_reference_ids are validated where provided.
[ ] AI Context is present for AI-assisted qualification/communication preparation.
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
service-provider:create
service-provider:read
service-provider:search
service-provider:update
service-provider:validate
service-provider:coverage:link
service-provider:network:link
service-provider:qualification:prepare
service-provider:communication:prepare
```

Rules:

```text
- Service Provider API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 21. Policy Rules

Required policy scopes may include:

```text
service-provider:create:policy
service-provider:read:policy
service-provider:search:policy
service-provider:update:policy
service-provider:reference:policy
service-provider:visibility:policy
service-provider:contact:visibility:policy
service-provider:coverage:link:policy
service-provider:network:link:policy
service-provider:qualification:prepare:policy
service-provider:communication:prepare:policy
service-provider:commercial-terms:visibility:policy
cross-organization:service-provider
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact contacts, pricing/commercial terms, qualification data, documents, network links, summaries or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before provider engagement, routing selection or external communication.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 22. AI and Human Review Rules

AI rules:

```text
- AI may summarize provider context and prepare qualification/communication drafts only within Permission and Policy limits.
- AI must not select providers, approve engagement, certify legal authority, approve payment or send communications.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Service Provider output is used for routing selection, engagement, contract approval, payment-impacting action, external communication or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 23. Idempotency and Event Rules

Idempotency:

```text
POST /v1/service-providers requires idempotency_key.
PATCH /v1/service-providers/{service_provider_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Coverage/network link endpoints may require idempotency_key for duplicate-sensitive operations.
Preparation endpoints do not normally require idempotency unless result is persisted.
```

Events:

```text
ServiceProviderCreated may be emitted by Service Provider Service after successful creation.
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
ServiceProviderReferenceInvalid
JurisdictionReferenceInvalid
ServiceNetworkReferenceInvalid
PartnerReferenceInvalid
DocumentReferenceInvalid
ServiceScopeInvalid
CoverageLinkInvalid
NetworkLinkInvalid
QualificationPreparationUnavailable
CommunicationPreparationUnavailable
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
- Errors must not expose database IDs, restricted provider data, private contacts, commercial terms, policy internals or permission internals.
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
cite Service Provider API Spec
cite Service Provider Service Spec
cite Routing Service Spec where routing context is used
cite this Service Provider API Contract
use Reference Contract for service_provider_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted qualification/communication preparation
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link operations
use Versioning Contract for version validation
route all Service Provider mutation through Service Provider Service
invoke Jurisdiction/Service Network/Partner/Document services for reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing contacts, coverage, qualification data, commercial terms or summaries
return safe errors only
write tests for create/read/update/search/validate-reference/link-coverage/link-network/prepare-qualification/prepare-communication
write tests for jurisdiction/network/partner/document reference validation
write tests that qualification preparation does not select provider
write tests that communication preparation does not send communication
write tests for coverage expansion requiring human review
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Service Provider directly in API layer
query database directly from API contract implementation
use generic id where service_provider_reference_id is required
expose database IDs, private contacts or commercial terms without policy allowance
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
select providers from Service Provider API
approve contracts, engagement or payments from this API contract
send external communication from preparation endpoint
treat AI qualification as legal authority or final provider selection
allow AI context to exceed evaluated_data_access_scope
```

---

# 27. Acceptance Criteria

This Service Provider API Contract is accepted only if:

```text
[ ] It defines Service Provider API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Service Provider API and Service specs.
[ ] It defines related Routing boundary.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines link coverage contract.
[ ] It defines link network contract.
[ ] It defines prepare qualification contract.
[ ] It defines prepare communication contract.
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
| 0.1.0 | Draft | Initial Service Provider API Contract. Defines governed create, read, update, search, validate-reference, coverage/network linkage, qualification preparation and communication preparation payloads, linked reference validation, Routing boundary, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
