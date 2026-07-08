# API Contract — Service Network API

**Spec ID:** B02-CONTRACT-API-SERVICE-NETWORK  
**Spec Type:** API Contract Specification  
**Contract Name:** Service Network API Contract  
**Contract File:** core-specs/contracts/api/service-network-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/service-network-api.md  
**Related Domain:** Service Network  
**Related Object Specs:** core-specs/objects/service-network.md; core-specs/objects/service-provider.md; core-specs/objects/partner.md; core-specs/objects/routing.md; core-specs/objects/jurisdiction.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/communication.md; core-specs/objects/document.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/service-network-service.md; core-specs/services/service-provider-service.md; core-specs/services/partner-service.md; core-specs/services/routing-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/communication-service.md; core-specs/services/document-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/service-network-api.md; core-specs/api/service-provider-api.md; core-specs/api/partner-api.md; core-specs/api/routing-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/order-api.md; core-specs/api/matter-api.md; core-specs/api/communication-api.md; core-specs/api/document-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/service-network-linked.md; core-specs/events/service-provider-created.md; core-specs/events/partner-created.md; core-specs/events/routing-evaluated.md; core-specs/events/routing-selected.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/routing-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
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

Service Network API Contract defines the implementation-facing request and response contract for Service Network API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, link, qualify and prepare Service Network records through governed API boundaries without bypassing Service Network Service, Service Provider Service, Partner Service, Routing Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Service Network API versioning
Service Network create request
Service Network update request
Service Network read response
Service Network search/list response
Service Network reference validation
Service Provider linkage
Partner linkage
Jurisdiction and service scope coverage
Network qualification preparation
Network routing context preparation
Network communication preparation
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Service Network API Contract does not approve network membership by itself, select providers, approve partner agreements, approve payment, create legal authority, send communications, replace Routing Service, replace Service Network Service, evaluate Permission/Policy, or authorize AI output as final network decision.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Service Network Service through governed API boundaries.
```

This contract does not mean:

```text
provider selection
network membership approval by itself
partnership agreement approval
supplier contract approval
payment approval
legal authority certification
external communication delivery
routing decision
permission grant
policy approval
event emitter
network portal UI
```

Core rule:

```text
Service Network API receives governed network requests.
Service Network Service owns Service Network behavior.
Service Provider, Partner, Jurisdiction, Order, Matter and Routing references are validated by owning services.
Permission and Policy govern access.
Network use requires governed routing and business process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Service Network reference fields
provider and partner membership fields
jurisdiction coverage fields
service scope fields
qualification preparation fields
routing context preparation fields
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
Service Network lifecycle ownership outside Service Network Service
provider routing selection
partner agreement execution
supplier contract execution
payment/revenue-share execution
external message delivery
legal authority certification
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
core-specs/api/service-network-api.md
```

Owning service spec:

```text
core-specs/services/service-network-service.md
```

Related network/routing boundaries:

```text
core-specs/services/service-provider-service.md
core-specs/services/partner-service.md
core-specs/services/routing-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Service Network API, Service Network Service, Service Provider Service, Partner Service or Routing Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
ServiceNetwork
```

Related objects:

```text
ServiceProvider
Partner
Routing
Jurisdiction
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
- service_network_reference_id identifies Service Network.
- service_provider_reference_ids identify network providers and must be validated by Service Provider Service.
- partner_reference_ids identify network partners and must be validated by Partner Service.
- jurisdiction_reference_ids describe network coverage and must be validated by Jurisdiction Service.
- routing_reference_id is owned by Routing Service and must not be selected by Service Network API.
- Service Network membership does not prove legal authority, contract approval, payment approval or provider selection by itself.
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

Service Network target context:

```yaml
target:
  service_network_reference_id: string | null
  target_object_type: ServiceNetwork
  target_object_reference_id: string | null
```

Rules:

```text
- service_network_reference_id is required for read/update/validate/link operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- linked provider, partner, jurisdiction and document references must be validated where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/service-networks
GET    /v1/service-networks/{service_network_reference_id}
PATCH  /v1/service-networks/{service_network_reference_id}
GET    /v1/service-networks
POST   /v1/service-networks/validate-reference
POST   /v1/service-networks/{service_network_reference_id}/link-members
POST   /v1/service-networks/{service_network_reference_id}/link-coverage
POST   /v1/service-networks/{service_network_reference_id}/prepare-qualification
POST   /v1/service-networks/{service_network_reference_id}/prepare-routing-context
POST   /v1/service-networks/{service_network_reference_id}/prepare-communication
```

Endpoint ownership:

```text
API layer validates request contract.
Service Network Service executes Service Network behavior.
Service Provider, Partner, Jurisdiction, Order, Matter, Routing and Document services validate references where applicable.
Communication Service owns Communication creation/sending.
Routing Service owns routing evaluation and selection.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted preparation where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Service Network Request Contract

Endpoint:

```text
POST /v1/service-networks
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
    - service-network:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - service-network:create:policy
  policy_decision_reference_id: string | null

payload:
  service_network_type: string
  service_network_status: string | null
  network_name_safe: string
  network_display_name_safe: string | null
  jurisdiction_reference_ids:
    - string
  service_scope_keys:
    - string
  service_provider_reference_ids:
    - string
  partner_reference_ids:
    - string
  document_reference_ids:
    - string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- service_network_type and network_name_safe are required.
- jurisdiction_reference_ids must be validated by Jurisdiction Service where provided.
- service_provider_reference_ids must be validated by Service Provider Service where provided.
- partner_reference_ids must be validated by Partner Service where provided.
- document_reference_ids must be validated by Document Service where provided.
- Service Network Service assigns service_network_reference_id.
```

---

# 9. Create Service Network Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  service_network_reference_id: string
  service_network_type: string
  service_network_status: string
  network_name_safe: string
  network_display_name_safe: string | null
  jurisdiction_reference_ids_visible:
    - string
  service_scope_keys_visible:
    - string
  service_provider_reference_ids_visible:
    - string
  partner_reference_ids_visible:
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
- ServiceNetworkLinked event reference may be included only where service emits it and policy allows it.
- Replayed idempotent response must not duplicate events.
```

---

# 10. Read Service Network Contract

Endpoint:

```text
GET /v1/service-networks/{service_network_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  service_network_reference_id: string
  service_network_type: string
  service_network_status: string
  network_name_safe: string
  network_display_name_safe: string | null
  jurisdiction_reference_ids_visible:
    - string
  service_scope_keys_visible:
    - string
  service_provider_reference_ids_visible:
    - string
  partner_reference_ids_visible:
    - string
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
- Read must evaluate service-network:read permission.
- Policy may redact provider members, partner members, documents, commercial details, qualification status or coverage details.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Service Network Contract

Endpoint:

```text
PATCH /v1/service-networks/{service_network_reference_id}
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
  service_network_status: string | null
  network_name_safe: string | null
  network_display_name_safe: string | null
  service_scope_keys_patch:
    - string
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - service-network:update
policy_context:
  required_policy_scopes:
    - service-network:update:policy
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
  service_network_reference_id: string
  service_network_status: string
  network_name_safe: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Update must route through Service Network Service.
- Coverage, scope or membership-impacting changes may require human review.
- Restricted agreement, commercial or qualification metadata must not be patched unless policy allows it.
```

---

# 12. Search/List Service Network Contract

Endpoint:

```text
GET /v1/service-networks
```

Query parameters:

```yaml
service_network_type: string | null
service_network_status: string | null
jurisdiction_reference_id: string | null
service_scope_key: string | null
service_provider_reference_id: string | null
partner_reference_id: string | null
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
    - service_network_reference_id: string
      service_network_type: string
      service_network_status: string
      network_name_safe: string
      network_display_name_safe: string | null
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
- Search must not reveal restricted Service Network existence or restricted member/commercial details.
- safe_query must not search private notes or protected network terms without policy allowance.
```

---

# 13. Validate Service Network Reference Contract

Endpoint:

```text
POST /v1/service-networks/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  service_network_reference_id: string
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
  service_network_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  service_network_type: string | null
  service_network_status: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Service Network.
- Valid reference does not imply network membership approval or routing selection.
- Validation status must follow Reference Contract.
- Policy may hide safe_label, type or status.
```

---

# 14. Link Members Contract

Endpoint:

```text
POST /v1/service-networks/{service_network_reference_id}/link-members
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  member_links:
    - member_object_type: string
      member_object_reference_id: string
      membership_role: string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - service-network:member:link
policy_context:
  required_policy_scopes:
    - service-network:member:link:policy
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
  service_network_reference_id: string
  member_links_visible:
    - member_object_type: string
      member_object_reference_id: string
      membership_role: string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Link operation must route through Service Network Service.
- Service Provider and Partner references must be validated by owning services.
- Membership linkage does not approve contracts, routing selection, payment or engagement by itself.
- Human review may be required for membership expansion or removal.
```

---

# 15. Link Coverage Contract

Endpoint:

```text
POST /v1/service-networks/{service_network_reference_id}/link-coverage
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
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - service-network:coverage:link
policy_context:
  required_policy_scopes:
    - service-network:coverage:link:policy
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
  service_network_reference_id: string
  jurisdiction_reference_ids_visible:
    - string
  service_scope_keys_visible:
    - string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operation must route through Service Network Service.
- Jurisdiction references must be validated by Jurisdiction Service.
- Coverage linkage does not prove local legal authority, service availability or provider selection by itself.
```

---

# 16. Prepare Qualification Contract

Endpoint:

```text
POST /v1/service-networks/{service_network_reference_id}/prepare-qualification
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
    - service-network:qualification:prepare
policy_context:
  required_policy_scopes:
    - service-network:qualification:prepare:policy
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
    service_scope_key: string | null
  include_member_context: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  qualification_preparation_status: string
  network_summary_safe: string | null
  capability_match_summary_safe: string | null
  member_context_summary_safe: string | null
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
- Qualification preparation is assistance, not network membership approval or routing selection.
- Routing evaluation and selection must route through Routing Service.
- AI must not certify network capability or legal authority.
- Human review may be required before routing/selection or external use.
```

---

# 17. Prepare Routing Context Contract

Endpoint:

```text
POST /v1/service-networks/{service_network_reference_id}/prepare-routing-context
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
    - service-network:routing-context:prepare
policy_context:
  required_policy_scopes:
    - service-network:routing-context:prepare:policy
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
  include_provider_candidates: boolean
  include_partner_constraints: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  routing_context_preparation_status: string
  network_routing_context_safe: object | null
  suggested_candidate_filters_safe: object | null
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
- Provider candidates may be omitted or redacted by policy.
- Human review may be required before routing-sensitive use.
```

---

# 18. Prepare Communication Contract

Endpoint:

```text
POST /v1/service-networks/{service_network_reference_id}/prepare-communication
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
    - service-network:communication:prepare
policy_context:
  required_policy_scopes:
    - service-network:communication:prepare:policy
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
- Human review may be required before external network communication.
```

---

# 19. Controlled Values

## 19.1 service_network_type

```text
GlobalAgentNetwork
RegionalAgentNetwork
JurisdictionNetwork
ServiceScopeNetwork
PartnerNetwork
InternalNetwork
AdHocNetwork
Other
Unknown
```

## 19.2 service_network_status

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

## 19.3 membership_role

```text
PrimaryProvider
BackupProvider
PreferredProvider
RestrictedProvider
PartnerMember
NetworkManager
Observer
Unknown
```

## 19.4 member_object_type

```text
ServiceProvider
Partner
InternalOrganization
Unknown
```

## 19.5 service_scope_key

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

## 19.6 qualification_status

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

## 19.7 qualification_preparation_status

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

## 19.8 routing_context_preparation_status

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

## 19.9 communication_preparation_status

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

## 19.10 validation_status

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

## 19.11 sort.field

```text
created_at
updated_at
network_name_safe
service_network_status
service_network_type
qualification_status
```

---

# 20. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] service_network_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] service_network_type is controlled.
[ ] service_network_status is controlled where provided.
[ ] service_scope_keys are controlled where provided.
[ ] jurisdiction_reference_ids are validated where provided.
[ ] service_provider_reference_ids are validated where provided.
[ ] partner_reference_ids are validated where provided.
[ ] member links are validated where provided.
[ ] document references are validated where provided.
[ ] AI Context is present for AI-assisted qualification/routing/communication preparation.
[ ] Human Review Context is present where policy requires review.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 21. Permission Rules

Required permission keys:

```text
service-network:create
service-network:read
service-network:search
service-network:update
service-network:validate
service-network:member:link
service-network:coverage:link
service-network:qualification:prepare
service-network:routing-context:prepare
service-network:communication:prepare
```

Rules:

```text
- Service Network API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 22. Policy Rules

Required policy scopes may include:

```text
service-network:create:policy
service-network:read:policy
service-network:search:policy
service-network:update:policy
service-network:reference:policy
service-network:visibility:policy
service-network:member:visibility:policy
service-network:member:link:policy
service-network:coverage:link:policy
service-network:qualification:prepare:policy
service-network:routing-context:prepare:policy
service-network:communication:prepare:policy
service-network:commercial-terms:visibility:policy
cross-organization:service-network
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact member lists, provider candidates, partner links, commercial data, agreement terms, documents, summaries or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before network use, membership changes, routing context use or external communication.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 23. AI and Human Review Rules

AI rules:

```text
- AI may summarize Service Network context and prepare qualification, routing context and communication drafts only within Permission and Policy limits.
- AI must not approve network membership, select providers, approve payment, approve engagement, create customer consent or send communications.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Service Network output is used for routing, membership decision, commercial terms, external communication, payment-impacting action or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 24. Idempotency and Event Rules

Idempotency:

```text
POST /v1/service-networks requires idempotency_key.
PATCH /v1/service-networks/{service_network_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Member/coverage link endpoints may require idempotency_key for duplicate-sensitive operations.
Preparation endpoints do not normally require idempotency unless result is persisted.
```

Events:

```text
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

# 25. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
ServiceNetworkReferenceInvalid
ServiceProviderReferenceInvalid
PartnerReferenceInvalid
JurisdictionReferenceInvalid
OrderReferenceInvalid
MatterReferenceInvalid
RoutingReferenceInvalid
DocumentReferenceInvalid
ServiceScopeInvalid
MemberLinkInvalid
CoverageLinkInvalid
QualificationPreparationUnavailable
RoutingContextPreparationUnavailable
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
- Errors must not expose database IDs, restricted network data, member lists, agreement terms, commercial terms, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 26. Versioning Rules

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

# 27. Codex Implementation Notes

Codex must:

```text
cite Service Network API Spec
cite Service Network Service Spec
cite Service Provider Service Spec where member context is used
cite Partner Service Spec where partner context is used
cite Routing Service Spec where routing context is used
cite this Service Network API Contract
use Reference Contract for service_network_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted qualification/routing/communication preparation
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link operations
use Versioning Contract for version validation
route all Service Network mutation through Service Network Service
invoke Service Provider/Partner/Jurisdiction/Order/Matter/Routing/Document services for reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing members, coverage, partner links, commercial terms or summaries
return safe errors only
write tests for create/read/update/search/validate-reference/link-members/link-coverage/prepare-qualification/prepare-routing-context/prepare-communication
write tests for provider/partner/jurisdiction/document reference validation
write tests that routing context preparation does not evaluate or select routing
write tests that communication preparation does not send communication
write tests for member/coverage changes requiring human review
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Service Network directly in API layer
query database directly from API contract implementation
use generic id where service_network_reference_id is required
expose database IDs, private member data, agreement terms or commercial terms without policy allowance
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
select providers from Service Network API
approve network membership, engagement, contracts or payments from this API contract
send external communication from preparation endpoint
treat AI routing context as RoutingSelected
allow AI context to exceed evaluated_data_access_scope
```

---

# 28. Acceptance Criteria

This Service Network API Contract is accepted only if:

```text
[ ] It defines Service Network API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Service Network API and Service specs.
[ ] It defines related Provider, Partner and Routing boundaries.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines link members contract.
[ ] It defines link coverage contract.
[ ] It defines prepare qualification contract.
[ ] It defines prepare routing context contract.
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

# 29. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Service Network API Contract. Defines governed create, read, update, search, validate-reference, member/coverage linkage, qualification preparation, routing-context preparation and communication preparation payloads, linked reference validation, Provider/Partner/Routing boundaries, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
