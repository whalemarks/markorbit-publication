# API Specification — Service Provider API

**Spec ID:** B02-API-SERVICE-PROVIDER  
**Spec Type:** API Specification  
**API Name:** Service Provider API  
**API File:** core-specs/api/service-provider-api.md  
**Related Domain:** core-specs/domains/service-provider.md  
**Related Object Specs:** core-specs/objects/service-provider.md; core-specs/objects/agent.md; core-specs/objects/partner.md; core-specs/objects/service-network.md; core-specs/objects/routing.md; core-specs/objects/jurisdiction.md; core-specs/objects/capability.md; core-specs/objects/communication.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/service-provider-service.md; core-specs/services/agent-service.md; core-specs/services/partner-service.md; core-specs/services/service-network-service.md; core-specs/services/routing-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/communication-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/service-provider-created.md; core-specs/events/routing-evaluated.md; core-specs/events/routing-selected.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/service-provider-api-contract.md; core-specs/contracts/events/service-provider-created-payload.md  
**Related Agent Specs:** core-specs/agents/service-provider-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 4 — Collaboration / Network Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Service Provider API exposes governed Service Provider registration, qualification, capability, visibility and routing-support operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate, qualify and evaluate Service Provider references without treating Service Provider as Agent, Partner, Customer, selected route, confirmed engagement, order assignee, legal representative, payment recipient, professional truth source or AI-approved provider.

Service Provider API exists to support:

```text
external provider reference creation
jurisdiction and service capability context
provider qualification and review
provider communication context
routing candidate preparation
service-network linkage preparation
policy-controlled provider visibility
AI-assisted provider analysis under governance
event trace access
API-safe service provider reference validation
```

Service Provider API does not select routes by itself, create engagements, assign orders, authorize payment, prove local legal authority or replace professional/vendor review.

---

# 2. API Meaning

Service Provider API means:

```text
a governed interface for operating Service Provider references through Service Provider Service.
```

Service Provider API does not mean:

```text
Agent API
Partner API
Routing API
Order assignment API
payment API
legal representative API
vendor contract API
professional truth API
AI provider approval API
```

Service Provider represents an external service-capability context.

Routing evaluates and selects candidates.

Partner represents business collaboration relationship where applicable.

Agent represents AI/automation actor context.

---

# 3. API Boundary

Service Provider API is responsible for:

```text
Service Provider create request intake
Service Provider read/search/list access
Service Provider update request intake
Service Provider reference validation
Provider capability and jurisdiction context exposure
Provider qualification request intake
Provider routing-candidate preparation
Provider communication preparation
safe Service Provider response shaping
Permission/Policy enforcement for Service Provider operations
Service Provider-related Event reference exposure where allowed
AI Agent access boundary for Service Provider operations
controlled API errors
```

Service Provider API is not responsible for:

```text
routing selection
order assignment
payment or settlement
partner lifecycle ownership
agent lifecycle ownership
official legal authority verification by itself
service contract execution
communication delivery
professional decision approval
AI final provider selection
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/service-provider.md
```

Domain rule:

```text
Service Provider represents external service-capability context.
Service Provider is not Agent, Partner, Routing selection, Order assignment, payment recipient, legal representative or professional truth by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/service-provider.md
core-specs/objects/agent.md
core-specs/objects/partner.md
core-specs/objects/service-network.md
core-specs/objects/routing.md
core-specs/objects/jurisdiction.md
core-specs/objects/capability.md
core-specs/objects/communication.md
core-specs/objects/order.md
core-specs/objects/matter.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Service Provider API returns service_provider_reference_id.
- Service Provider API may reference Agent, Partner, Service Network, Routing, Jurisdiction, Communication, Order or Matter context but must not create or execute them silently.
- Service Provider must not be treated as selected route.
- Service Provider must not be treated as legal representative or payment recipient without separate governed contract/state.
- Service Provider capability must be policy-filtered and context-specific.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/service-provider-service.md
core-specs/services/agent-service.md
core-specs/services/partner-service.md
core-specs/services/service-network-service.md
core-specs/services/routing-service.md
core-specs/services/jurisdiction-service.md
core-specs/services/communication-service.md
core-specs/services/order-service.md
core-specs/services/matter-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Service Provider API must invoke Service Provider Service for Service Provider behavior.
- Service Provider API must validate related references through their owning services where required.
- Service Provider API must invoke Permission Service before protected operations.
- Service Provider API must invoke Policy Service before visibility, qualification, capability and routing-support operations.
- Service Provider API must not emit ServiceProviderCreated directly; Service Provider Service and Event Service govern events.
- Routing selection must route through Routing Service.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/service-provider-created.md
core-specs/events/routing-evaluated.md
core-specs/events/routing-selected.md
core-specs/events/communication-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createServiceProvider may result in ServiceProviderCreated.
- routing evaluation must use Routing Service and may result in RoutingEvaluated.
- routing selection must use Routing Service and may result in RoutingSelected.
- provider communication must use Communication Service and may result in CommunicationCreated.
- API consumers must not fabricate ServiceProviderCreated.
- ServiceProviderCreated is provider reference trace, not routing selection, order assignment, legal authority or payment approval.
```

---

# 8. API Operations

## 8.1 Operation: Create Service Provider

**Operation Category:** Create  
**Method:** POST  
**Path:** `/service-providers`  
**Owning Service Operation:** `createServiceProvider`  
**Permission Required:** `service-provider:create`  
**Policy Required:** `ServiceProviderCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-inferred  
**Event Behavior:** Service Must Emit ServiceProviderCreated

Meaning:

```text
Create a governed Service Provider reference.
```

Non-meaning:

```text
does not create Partner
does not create Agent
does not select route
does not assign Order
does not approve payment
does not prove legal authority
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
Service Provider Service createServiceProvider
  ↓
Event Service record ServiceProviderCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Service Provider

**Operation Category:** Read  
**Method:** GET  
**Path:** `/service-providers/{service_provider_reference_id}`  
**Owning Service Operation:** `getServiceProvider`  
**Permission Required:** `service-provider:read`  
**Policy Required:** `ServiceProviderVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Service Provider view.
```

Non-meaning:

```text
does not expose commercial terms automatically
does not expose bank/payment details automatically
does not expose private contacts automatically
does not authorize engagement or order assignment
```

## 8.3 Operation: Search Service Providers

**Operation Category:** Search  
**Method:** GET  
**Path:** `/service-providers`  
**Owning Service Operation:** `searchServiceProviders`  
**Permission Required:** `service-provider:search`  
**Policy Required:** `ServiceProviderVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Service Provider references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted provider database access
does not expose restricted pricing, contacts, agreements, performance notes or strategy data by default
```

## 8.4 Operation: Update Service Provider

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/service-providers/{service_provider_reference_id}`  
**Owning Service Operation:** `updateServiceProvider`  
**Permission Required:** `service-provider:update`  
**Policy Required:** `ServiceProviderUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit ServiceProviderUpdated where event is defined

Meaning:

```text
Update governed Service Provider metadata, status, capability or qualification context under Service Provider Service rules.
```

Non-meaning:

```text
does not update Partner relationship automatically
does not update Routing selection automatically
does not assign Order
does not approve payment or contract
```

## 8.5 Operation: Validate Service Provider Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/service-providers/reference/validate`  
**Owning Service Operation:** `validateServiceProviderReference`  
**Permission Required:** `service-provider:validate`  
**Policy Required:** `ServiceProviderReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Service Provider reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not authorize routing selection
does not authorize order assignment
does not prove legal authority
does not authorize payment
```

## 8.6 Operation: List Service Provider Capabilities

**Operation Category:** Read  
**Method:** GET  
**Path:** `/service-providers/{service_provider_reference_id}/capabilities`  
**Owning Service Operation:** `listServiceProviderCapabilities`  
**Permission Required:** `service-provider:capability:read`  
**Policy Required:** `ServiceProviderCapabilityVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe capabilities associated with a Service Provider.
```

Non-meaning:

```text
does not guarantee capability availability
does not approve provider selection
does not expose restricted pricing or contract terms by default
```

## 8.7 Operation: Qualify Service Provider

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/service-providers/{service_provider_reference_id}/qualify`  
**Owning Service Operation:** `qualifyServiceProvider`  
**Permission Required:** `service-provider:qualify`  
**Policy Required:** `ServiceProviderQualificationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit RoutingSelected

Meaning:

```text
Create or update a governed qualification assessment for a Service Provider.
```

Non-meaning:

```text
does not select provider
does not assign order
does not approve contract
does not prove legal authority
does not replace professional/vendor review
```

## 8.8 Operation: Prepare Routing Candidate

**Operation Category:** Action  
**Method:** POST  
**Path:** `/service-providers/{service_provider_reference_id}/routing-candidate/prepare`  
**Owning Service Operation:** `prepareServiceProviderRoutingCandidate`  
**Permission Required:** `service-provider:routing-candidate:prepare`  
**Policy Required:** `ServiceProviderRoutingCandidatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Must route through Routing Service for RoutingEvaluated/Selected where applicable

Meaning:

```text
Prepare a Service Provider as a governed routing candidate for a target service context.
```

Non-meaning:

```text
does not evaluate all routing candidates
does not select route
does not assign Order
does not create service engagement
```

## 8.9 Operation: Prepare Provider Communication

**Operation Category:** Action  
**Method:** POST  
**Path:** `/service-providers/{service_provider_reference_id}/communications/prepare`  
**Owning Service Operation:** `prepareServiceProviderCommunication`  
**Permission Required:** `service-provider:communication:prepare`  
**Policy Required:** `ServiceProviderCommunicationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Must route through Communication Service if Communication is created

Meaning:

```text
Prepare governed Communication draft or request with a Service Provider.
```

Non-meaning:

```text
does not create Communication unless Communication Service accepts it
does not send message
does not approve external wording
does not create engagement
```

## 8.10 Operation: Link Service Provider to Network

**Operation Category:** Link  
**Method:** POST  
**Path:** `/service-providers/{service_provider_reference_id}/service-networks/{service_network_reference_id}/link`  
**Owning Service Operation:** `linkServiceProviderToNetwork`  
**Permission Required:** `service-provider:service-network:link`  
**Policy Required:** `ServiceProviderNetworkLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Must route through Service Network Service where network link event is defined

Meaning:

```text
Create a governed relationship between Service Provider and Service Network.
```

Non-meaning:

```text
does not approve service engagement
does not create Partner automatically
does not select route
does not assign Order
```

## 8.11 Operation: List Service Provider Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/service-providers/{service_provider_reference_id}/events`  
**Owning Service Operation:** `listServiceProviderEvents`  
**Permission Required:** `service-provider:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Service Provider-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Service Provider Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  service_provider_type: string
  service_provider_status: string | optional
  provider_name: string
  provider_region: string | null
  primary_jurisdiction_reference_id: string | null
  capability_profile_reference_id: string | null
  qualification_status: string | optional
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_inferred: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Service Provider Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  service_provider_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  service_provider_status: string | optional
  provider_name: string | optional
  capability_profile_reference_id: string | optional
  qualification_status: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Service Provider Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  service_provider_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Qualify Service Provider Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  qualification_mode: string
  qualification_purpose: string
  target_context:
    jurisdiction_reference_id: string | null
    service_type: string | null
    matter_reference_id: string | null
    order_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.5 Prepare Routing Candidate Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  routing_purpose: string
  target_context:
    jurisdiction_reference_id: string | null
    service_type: string | null
    matter_reference_id: string | null
    order_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.6 Prepare Provider Communication Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  draft_purpose: string
  communication_type: string
  target_context:
    matter_reference_id: string | null
    order_reference_id: string | null
    routing_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.7 Link Service Provider to Network Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  service_provider_reference_id: string
  service_network_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  link_type: string
  link_reason: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include bank data, private contacts, contract secrets, credentials or restricted performance notes by default.
- Requests must use controlled service_provider_type, service_provider_status, qualification_status, source_type, qualification_mode, routing_purpose and link_type values.
- AI-inferred provider data must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Service Provider Response

```yaml
status: 200
body:
  service_provider_reference_id: string
  service_provider_type: string
  service_provider_status: string
  provider_name: string
  provider_region: string | null
  primary_jurisdiction_reference_id: string | null
  capability_profile_reference_id: string | null
  qualification_status: string
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    capability_summary: string | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Service Provider Response

```yaml
status: 201
body:
  service_provider_reference_id: string
  service_provider_status: string
  qualification_status: string
  review_required: boolean
  related_event_reference_ids:
    - service_provider_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Service Provider Reference Validation Response

```yaml
status: 200
body:
  service_provider_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Service Provider Capability Response

```yaml
status: 200
body:
  service_provider_reference_id: string
  safe_capabilities:
    - capability_reference_id: string | null
      service_type: string
      jurisdiction_reference_id: string | null
      capability_status: string
      safe_summary: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.5 Service Provider Qualification Response

```yaml
status: 200
body:
  service_provider_reference_id: string
  qualification_reference_id: string | null
  qualification_status: string
  safe_summary:
    qualified: boolean
    risk_summary: string | null
    missing_items: list[string]
    review_required: boolean
  confidence_level: string
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Routing Candidate Preparation Response

```yaml
status: 200
body:
  service_provider_reference_id: string
  routing_candidate_reference_id: string | null
  usable_for_routing_evaluation: boolean
  missing_items: list[string]
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply Routing selection, Order assignment, payment approval, legal authority or engagement creation.
- Responses must not expose restricted contacts, pricing, bank details, agreements, performance notes or internal strategy by default.
- Responses must distinguish Service Provider references from Partner, Agent, Routing and Service Network references.
- Responses must identify review requirements for AI-inferred or AI-assisted provider data.
```

---

# 11. Controlled Values

## 11.1 service_provider_type

```text
ForeignAssociate
LocalTrademarkAgent
LawFirm
TranslationProvider
SearchProvider
FilingProvider
RenewalProvider
RecordalProvider
Consultant
InternalProvider
Unknown
```

## 11.2 service_provider_status

```text
Draft
Active
ReviewRequired
Preferred
Suspended
Inactive
Blacklisted
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 qualification_status

```text
Unqualified
Qualified
NeedsReview
Preferred
Restricted
Rejected
Expired
Unknown
```

## 11.4 source_type

```text
ProfessionalInput
PartnerInput
CommunicationDerived
RoutingDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.5 qualification_mode

```text
Preview
AIAssistedDraft
HumanReview
FinalQualification
Unknown
```

## 11.6 qualification_purpose

```text
GeneralReview
JurisdictionCapability
ServiceCapability
RoutingPreparation
OrderPreparation
MatterPreparation
NetworkAdmission
Unknown
```

## 11.7 routing_purpose

```text
CandidatePreparation
FeeComparison
JurisdictionMatch
ServiceCapabilityMatch
RiskReview
UrgencyReview
AIAssistedRouting
Unknown
```

## 11.8 link_type

```text
NetworkMember
PreferredProvider
BackupProvider
RestrictedProvider
HistoricalProvider
ReferenceOnly
Unknown
```

## 11.9 capability_status

```text
Active
ReviewRequired
Restricted
Deprecated
Unknown
```

## 11.10 confidence_level

```text
Low
Medium
High
Unknown
```

## 11.11 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Suspended
Restricted
ContextMismatch
Unknown
```

## 11.12 intended_use

```text
RoutingPreparation
OrderPreparation
MatterPreparation
CommunicationPreparation
ServiceNetworkLink
CapabilityReview
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
service-provider:create
service-provider:read
service-provider:search
service-provider:update
service-provider:validate
service-provider:capability:read
service-provider:qualify
service-provider:routing-candidate:prepare
service-provider:communication:prepare
service-provider:service-network:link
service-provider:event:read
```

Rules:

```text
- Service Provider read/search must be permission-controlled.
- Service Provider creation must not imply routing selection or engagement.
- Service Provider validation must not authorize routing selection, order assignment or payment.
- Qualification, capability access, routing candidate preparation and network linking require separate permissions.
- Downstream Routing, Communication and Service Network operations require their owning permissions.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
ServiceProviderCreationPolicy
ServiceProviderUpdatePolicy
ServiceProviderVisibilityPolicy
ServiceProviderReferencePolicy
ServiceProviderCapabilityVisibilityPolicy
ServiceProviderQualificationPolicy
ServiceProviderRoutingCandidatePolicy
ServiceProviderCommunicationPolicy
ServiceProviderNetworkLinkPolicy
EventVisibilityPolicy
AIAgentServiceProviderAccessPolicy
RestrictedServiceProviderDataPolicy
CrossOrganizationServiceProviderPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Service Provider fields.
- Policy may require human review for AI-inferred provider records and AI-assisted qualification.
- Policy may restrict cross-organization Service Provider lookup.
- Policy may restrict private contacts, pricing, bank data, contracts, performance notes and internal strategy.
- Policy may restrict provider qualification, routing candidate preparation and network linking.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Service Provider: Restricted / HumanReviewRequired where AI-inferred
Get Service Provider: Restricted
Search Service Providers: Restricted
Update Service Provider: Restricted / HumanReviewRequired where sensitive
Validate Service Provider Reference: Allowed under contract
List Service Provider Capabilities: Restricted
Qualify Service Provider: Restricted / HumanReviewRequired
Prepare Routing Candidate: Restricted / HumanReviewRequired
Prepare Provider Communication: Restricted / HumanReviewRequired where AI-drafted
Link Service Provider to Network: Restricted / HumanReviewRequired where AI-suggested
List Service Provider Events: Restricted
```

AI Agents may:

```text
summarize safe Service Provider metadata
flag missing capability or qualification context
validate Service Provider references for authorized actions
prepare qualification draft for human review
prepare routing candidate draft for human review
prepare provider Communication draft for human review
suggest Service Network link for human review
```

AI Agents must not:

```text
fabricate Service Provider
fabricate ServiceProviderCreated events
treat AI-inferred provider data as confirmed vendor truth
select route or assign order
approve payment or contract
treat provider as legal representative without governed proof
send provider communication directly
bypass Permission or Policy
expose restricted contacts, pricing, contracts or bank data
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

Service Provider API may expose:

```text
ServiceProviderCreated
RoutingEvaluated
RoutingSelected
CommunicationCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Service Provider events directly.
- ServiceProviderCreated must not be treated as route selection, Order assignment, legal authority, contract approval or payment authorization.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] service_provider_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] primary_jurisdiction_reference_id is valid where provided.
[ ] capability_profile_reference_id is valid where provided.
[ ] service_network_reference_id is valid for network link where provided.
[ ] matter_reference_id and order_reference_id are valid where provided.
[ ] service_provider_type is controlled.
[ ] service_provider_status is controlled.
[ ] qualification_status is controlled.
[ ] source_type is controlled.
[ ] qualification_mode is controlled where applicable.
[ ] routing_purpose is controlled where applicable.
[ ] link_type is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted provider/contact/pricing/contract/bank/performance fields are omitted or allowed.
[ ] AI-inferred provider data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] ServiceProviderCreated is emitted after createServiceProvider succeeds.
[ ] Qualification does not select route.
[ ] Routing candidate preparation routes through Routing Service where evaluation/selection is needed.
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
ServiceProviderReferenceInvalid
JurisdictionReferenceInvalid
CapabilityProfileInvalid
ServiceNetworkReferenceInvalid
MatterReferenceInvalid
OrderReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
QualificationRejected
RoutingCandidateInvalid
RestrictedFieldViolation
RestrictedServiceProviderData
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
- Errors must not expose restricted Service Provider data.
- Errors must not expose contacts, pricing, bank data, contracts, performance notes or internal strategy.
- Errors must not expose unrelated Routing, Order, Matter, Partner or Service Network details.
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
- service_provider_type, service_provider_status, qualification_status, capability_status and link_type changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI provider qualification/routing behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Service Provider API spec
cite Service Provider Service Specification
cite Service Provider Object Specification
cite ServiceProviderCreated Event Specification
cite Routing/Communication/Service Network specs where downstream operations are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid service_provider_reference_id
write tests for invalid jurisdiction/capability/network/order/matter references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Service Provider creation does not select route or assign Order
write tests that qualification does not approve legal authority or contract
write tests that routing candidate preparation does not emit RoutingSelected directly
write tests that provider Communication preparation routes through Communication Service
write tests for AI Agent Contract and human review requirement
write tests for ServiceProviderCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Service Provider Service
allow UI to emit ServiceProviderCreated directly
treat Service Provider as Agent
treat Service Provider as Partner
treat Service Provider as selected route
treat Service Provider as legal representative or payment recipient by default
select route or assign Order through Service Provider API
expose contacts, pricing, bank data, contracts or performance notes for convenience
allow AI to fabricate Service Provider references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Service Provider API purpose.
[ ] It defines Service Provider API meaning.
[ ] It defines Service Provider API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, capability listing, qualification, routing-candidate preparation, communication preparation, network linking and event-list operations.
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
| 0.1.0 | Draft | Initial Service Provider API specification. Defines governed Service Provider external capability interface and separates Service Provider API from Agent, Partner, Routing selection, Order assignment, payment, legal authority, engagement and AI provider approval. |

---

**End of API Specification**
