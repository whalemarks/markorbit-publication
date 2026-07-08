# API Specification — Partner API

**Spec ID:** B02-API-PARTNER  
**Spec Type:** API Specification  
**API Name:** Partner API  
**API File:** core-specs/api/partner-api.md  
**Related Domain:** core-specs/domains/partner.md  
**Related Object Specs:** core-specs/objects/partner.md; core-specs/objects/organization.md; core-specs/objects/customer.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/service-provider.md; core-specs/objects/service-network.md; core-specs/objects/routing.md; core-specs/objects/communication.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/partner-service.md; core-specs/services/organization-service.md; core-specs/services/customer-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/service-provider-service.md; core-specs/services/service-network-service.md; core-specs/services/routing-service.md; core-specs/services/communication-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/partner-created.md; core-specs/events/service-network-linked.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/partner-api-contract.md; core-specs/contracts/events/partner-created-payload.md  
**Related Agent Specs:** core-specs/agents/partner-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 5 — Network Expansion Reserved  
**MVP Depth:** Reserved / Later Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Partner API exposes governed Partner registration, relationship, visibility and collaboration-context operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate, qualify and link Partner references without treating Partner as Customer, Service Provider, Agent, Service Network membership, routing selection, order ownership, payment obligation, commission settlement, legal representative, professional truth source or AI-approved business relationship.

Partner API exists to support:

```text
partner relationship reference creation
agency / channel / business collaborator context
partner organization linkage
partner customer/order/matter context
partner qualification and review
service-network relationship preparation
partner communication preparation
policy-controlled partner visibility
AI-assisted partner analysis under governance
event trace access
API-safe partner reference validation
```

Partner API does not create financial settlement, approve commissions, select providers, assign orders, prove legal authority, create Service Network membership automatically or replace business relationship governance.

---

# 2. API Meaning

Partner API means:

```text
a governed interface for operating Partner relationship references through Partner Service.
```

Partner API does not mean:

```text
Customer API
Service Provider API
Agent API
Service Network API
Routing API
payment API
commission settlement API
legal representative API
business contract API
AI partner approval API
```

Partner represents a business collaboration relationship.

Customer represents demand-side business/customer context.

Service Provider represents external service-capability context.

Service Network organizes provider/partner network relationships.

Routing evaluates and selects service routes.

---

# 3. API Boundary

Partner API is responsible for:

```text
Partner create request intake
Partner read/search/list access
Partner update request intake
Partner reference validation
Partner qualification request intake
Partner-to-organization relationship context
Partner-to-service-network link preparation
Partner communication preparation
safe Partner response shaping
Permission/Policy enforcement for Partner operations
Partner-related Event reference exposure where allowed
AI Agent access boundary for Partner operations
controlled API errors
```

Partner API is not responsible for:

```text
Customer lifecycle ownership
Service Provider lifecycle ownership
Service Network lifecycle ownership
Routing selection
Order ownership transfer
payment or commission settlement
contract execution
legal authority verification by itself
communication delivery
professional decision approval
AI final partner approval
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/partner.md
```

Domain rule:

```text
Partner represents governed business collaboration relationship context.
Partner is not Customer, Service Provider, Agent, Service Network membership, Routing selection, payment, commission settlement, legal authority or professional truth by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/partner.md
core-specs/objects/organization.md
core-specs/objects/customer.md
core-specs/objects/order.md
core-specs/objects/matter.md
core-specs/objects/service-provider.md
core-specs/objects/service-network.md
core-specs/objects/routing.md
core-specs/objects/communication.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Partner API returns partner_reference_id.
- Partner API may reference Organization, Customer, Order, Matter, Service Provider, Service Network, Routing and Communication context but must not create or execute them silently.
- Partner must not be treated as Customer or Service Provider by default.
- Partner must not be treated as network member unless Service Network link exists.
- Partner financial, commission, contract and private contact fields are restricted by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/partner-service.md
core-specs/services/organization-service.md
core-specs/services/customer-service.md
core-specs/services/order-service.md
core-specs/services/matter-service.md
core-specs/services/service-provider-service.md
core-specs/services/service-network-service.md
core-specs/services/routing-service.md
core-specs/services/communication-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Partner API must invoke Partner Service for Partner behavior.
- Partner API must validate related references through their owning services where required.
- Partner API must invoke Permission Service before protected operations.
- Partner API must invoke Policy Service before visibility, qualification, network-link and communication operations.
- Partner API must not emit PartnerCreated directly; Partner Service and Event Service govern events.
- Service Network linking must route through Service Network Service where actual membership or link is created.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/partner-created.md
core-specs/events/service-network-linked.md
core-specs/events/communication-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createPartner may result in PartnerCreated.
- service-network linking must use Service Network Service and may result in ServiceNetworkLinked.
- partner communication must use Communication Service and may result in CommunicationCreated.
- API consumers must not fabricate PartnerCreated.
- PartnerCreated is relationship reference trace, not contract approval, commission settlement, customer creation, service provider creation or network membership by itself.
```

---

# 8. API Operations

## 8.1 Operation: Create Partner

**Operation Category:** Create  
**Method:** POST  
**Path:** `/partners`  
**Owning Service Operation:** `createPartner`  
**Permission Required:** `partner:create`  
**Policy Required:** `PartnerCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-inferred  
**Event Behavior:** Service Must Emit PartnerCreated

Meaning:

```text
Create a governed Partner relationship reference.
```

Non-meaning:

```text
does not create Customer
does not create Service Provider
does not create Service Network membership
does not approve contract
does not settle commission
does not authorize payment
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
Partner Service createPartner
  ↓
Event Service record PartnerCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Partner

**Operation Category:** Read  
**Method:** GET  
**Path:** `/partners/{partner_reference_id}`  
**Owning Service Operation:** `getPartner`  
**Permission Required:** `partner:read`  
**Policy Required:** `PartnerVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Partner view.
```

Non-meaning:

```text
does not expose private contacts automatically
does not expose commission terms automatically
does not expose contract terms automatically
does not authorize collaboration action
```

## 8.3 Operation: Search Partners

**Operation Category:** Search  
**Method:** GET  
**Path:** `/partners`  
**Owning Service Operation:** `searchPartners`  
**Permission Required:** `partner:search`  
**Policy Required:** `PartnerVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Partner references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted partner database access
does not expose restricted contacts, commissions, contracts, performance notes or strategy data by default
```

## 8.4 Operation: Update Partner

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/partners/{partner_reference_id}`  
**Owning Service Operation:** `updatePartner`  
**Permission Required:** `partner:update`  
**Policy Required:** `PartnerUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit PartnerUpdated where event is defined

Meaning:

```text
Update governed Partner metadata, relationship status, qualification context or safe summary under Partner Service rules.
```

Non-meaning:

```text
does not update contract automatically
does not update commission settlement automatically
does not update Customer, Order or Service Provider state automatically
does not create Service Network membership automatically
```

## 8.5 Operation: Validate Partner Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/partners/reference/validate`  
**Owning Service Operation:** `validatePartnerReference`  
**Permission Required:** `partner:validate`  
**Policy Required:** `PartnerReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Partner reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not authorize order sharing
does not authorize commission settlement
does not prove contract status
does not prove service-network membership
```

## 8.6 Operation: Qualify Partner

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/partners/{partner_reference_id}/qualify`  
**Owning Service Operation:** `qualifyPartner`  
**Permission Required:** `partner:qualify`  
**Policy Required:** `PartnerQualificationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit ServiceNetworkLinked

Meaning:

```text
Create or update a governed qualification assessment for a Partner.
```

Non-meaning:

```text
does not approve contract
does not settle commission
does not create network membership
does not assign orders
does not replace business review
```

## 8.7 Operation: Link Partner to Organization

**Operation Category:** Link  
**Method:** POST  
**Path:** `/partners/{partner_reference_id}/organizations/{organization_reference_id}/link`  
**Owning Service Operation:** `linkPartnerToOrganization`  
**Permission Required:** `partner:organization:link`  
**Policy Required:** `PartnerOrganizationLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit PartnerUpdated or future link event where defined

Meaning:

```text
Create a governed relationship between Partner and Organization.
```

Non-meaning:

```text
does not merge organizations
does not grant organization permissions
does not create contract
does not authorize commission settlement
```

## 8.8 Operation: Prepare Service Network Link

**Operation Category:** Action  
**Method:** POST  
**Path:** `/partners/{partner_reference_id}/service-networks/{service_network_reference_id}/link/prepare`  
**Owning Service Operation:** `preparePartnerServiceNetworkLink`  
**Permission Required:** `partner:service-network:link:prepare`  
**Policy Required:** `PartnerServiceNetworkLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Must route through Service Network Service if link is created

Meaning:

```text
Prepare a governed Service Network link request for a Partner.
```

Non-meaning:

```text
does not create Service Network link automatically
does not approve membership
does not create Service Provider
does not approve contract or commission
```

## 8.9 Operation: Prepare Partner Communication

**Operation Category:** Action  
**Method:** POST  
**Path:** `/partners/{partner_reference_id}/communications/prepare`  
**Owning Service Operation:** `preparePartnerCommunication`  
**Permission Required:** `partner:communication:prepare`  
**Policy Required:** `PartnerCommunicationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Must route through Communication Service if Communication is created

Meaning:

```text
Prepare governed Communication draft or request with a Partner.
```

Non-meaning:

```text
does not create Communication unless Communication Service accepts it
does not send message
does not approve external wording
does not create contract
```

## 8.10 Operation: Prepare Partner Order Context

**Operation Category:** Action  
**Method:** POST  
**Path:** `/partners/{partner_reference_id}/orders/prepare-context`  
**Owning Service Operation:** `preparePartnerOrderContext`  
**Permission Required:** `partner:order-context:prepare`  
**Policy Required:** `PartnerOrderContextPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Must route through Order Service if Order is created or updated

Meaning:

```text
Prepare governed Order context involving a Partner relationship.
```

Non-meaning:

```text
does not create Order automatically
does not transfer Order ownership
does not approve commission
does not approve customer instruction
```

## 8.11 Operation: List Partner Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/partners/{partner_reference_id}/events`  
**Owning Service Operation:** `listPartnerEvents`  
**Permission Required:** `partner:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Partner-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Partner Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  partner_type: string
  partner_status: string | optional
  partner_name: string
  partner_region: string | null
  partner_organization_reference_id: string | null
  qualification_status: string | optional
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_inferred: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Partner Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  partner_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  partner_status: string | optional
  partner_name: string | optional
  qualification_status: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Partner Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  partner_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Qualify Partner Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  qualification_mode: string
  qualification_purpose: string
  target_context:
    organization_reference_id: string | null
    service_network_reference_id: string | null
    order_reference_id: string | null
    matter_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.5 Link Partner to Organization Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  partner_reference_id: string
  organization_reference_id: string
body:
  actor_reference_id: string
  link_type: string
  link_reason: string | null
  request_context: object
```

## 9.6 Prepare Service Network Link Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  service_network_reference_id: string
  link_type: string
  link_reason: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.7 Prepare Partner Communication Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  draft_purpose: string
  communication_type: string
  target_context:
    order_reference_id: string | null
    matter_reference_id: string | null
    service_network_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.8 Prepare Partner Order Context Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  order_context_purpose: string
  target_context:
    customer_reference_id: string | null
    order_reference_id: string | null
    matter_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include bank data, commission terms, private contacts, contract secrets, credentials or restricted performance notes by default.
- Requests must use controlled partner_type, partner_status, qualification_status, source_type, qualification_mode, link_type, draft_purpose and order_context_purpose values.
- AI-inferred partner data must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Partner Response

```yaml
status: 200
body:
  partner_reference_id: string
  partner_type: string
  partner_status: string
  partner_name: string
  partner_region: string | null
  partner_organization_reference_id: string | null
  qualification_status: string
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    relationship_summary: string | null
  linked_object_references:
    - target_object_type: string
      target_object_reference_id: string
      link_type: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Partner Response

```yaml
status: 201
body:
  partner_reference_id: string
  partner_status: string
  qualification_status: string
  review_required: boolean
  related_event_reference_ids:
    - partner_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Partner Reference Validation Response

```yaml
status: 200
body:
  partner_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Partner Qualification Response

```yaml
status: 200
body:
  partner_reference_id: string
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

## 10.5 Service Network Link Preparation Response

```yaml
status: 200
body:
  partner_reference_id: string
  service_network_reference_id: string
  network_link_draft_reference_id: string | null
  usable_for_network_link: boolean
  missing_items: list[string]
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Partner Communication / Order Context Preparation Response

```yaml
status: 200
body:
  partner_reference_id: string
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
- Responses must not imply contract approval, commission settlement, payment authorization, Service Network membership, Customer creation, Order creation or Service Provider creation.
- Responses must not expose restricted contacts, commission terms, bank details, agreements, performance notes or internal strategy by default.
- Responses must distinguish Partner references from Customer, Service Provider, Service Network, Routing, Order and Matter references.
- Responses must identify review requirements for AI-inferred or AI-assisted partner data.
```

---

# 11. Controlled Values

## 11.1 partner_type

```text
AgencyPartner
ChannelPartner
ReferralPartner
PlatformPartner
ServicePartner
RegionalPartner
StrategicPartner
InternalPartner
Unknown
```

## 11.2 partner_status

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
OrganizationDerived
CommunicationDerived
ServiceNetworkDerived
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
NetworkAdmission
OrderCollaboration
CustomerReferral
ChannelManagement
RiskReview
Unknown
```

## 11.7 link_type

```text
OrganizationPartner
NetworkMember
PreferredPartner
ReferralPartner
ChannelPartner
RestrictedPartner
HistoricalPartner
ReferenceOnly
Unknown
```

## 11.8 draft_purpose

```text
Onboarding
OrderCoordination
MatterCoordination
NetworkCoordination
PartnerReview
ClientUpdate
InternalReview
AIAssistedDraft
Unknown
```

## 11.9 order_context_purpose

```text
ReferralContext
ChannelContext
JointServiceContext
PartnerManagedOrder
InternalCoordination
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

## 11.11 confidence_level

```text
Low
Medium
High
Unknown
```

## 11.12 validation_status

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

## 11.13 intended_use

```text
OrganizationLink
ServiceNetworkLink
OrderPreparation
MatterPreparation
CommunicationPreparation
PartnerQualification
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
partner:create
partner:read
partner:search
partner:update
partner:validate
partner:qualify
partner:organization:link
partner:service-network:link:prepare
partner:communication:prepare
partner:order-context:prepare
partner:event:read
```

Rules:

```text
- Partner read/search must be permission-controlled.
- Partner creation must not imply contract, commission, payment or network membership.
- Partner validation must not authorize partner-managed order context or commission settlement.
- Qualification, organization link, network link preparation, communication preparation and order-context preparation require separate permissions.
- Downstream Service Network, Communication and Order operations require their owning permissions.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
PartnerCreationPolicy
PartnerUpdatePolicy
PartnerVisibilityPolicy
PartnerReferencePolicy
PartnerQualificationPolicy
PartnerOrganizationLinkPolicy
PartnerServiceNetworkLinkPolicy
PartnerCommunicationPolicy
PartnerOrderContextPolicy
EventVisibilityPolicy
AIAgentPartnerAccessPolicy
RestrictedPartnerDataPolicy
CrossOrganizationPartnerPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Partner fields.
- Policy may require human review for AI-inferred partner records and AI-assisted qualification.
- Policy may restrict cross-organization Partner lookup.
- Policy may restrict private contacts, commission terms, bank data, contracts, performance notes and internal strategy.
- Policy may restrict partner qualification, network link preparation and order-context preparation.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Partner: Restricted / HumanReviewRequired where AI-inferred
Get Partner: Restricted
Search Partners: Restricted
Update Partner: Restricted / HumanReviewRequired where sensitive
Validate Partner Reference: Allowed under contract
Qualify Partner: Restricted / HumanReviewRequired
Link Partner to Organization: Restricted / HumanReviewRequired where AI-suggested
Prepare Service Network Link: Restricted / HumanReviewRequired where AI-suggested
Prepare Partner Communication: Restricted / HumanReviewRequired where AI-drafted
Prepare Partner Order Context: Restricted / HumanReviewRequired
List Partner Events: Restricted
```

AI Agents may:

```text
summarize safe Partner metadata
flag missing partner relationship or qualification context
validate Partner references for authorized actions
prepare qualification draft for human review
prepare Service Network link draft for human review
prepare partner Communication draft for human review
prepare partner Order context draft for human review
```

AI Agents must not:

```text
fabricate Partner
fabricate PartnerCreated events
treat AI-inferred partner data as confirmed business relationship
approve contract, commission or payment
create Service Network membership silently
create Customer, Order or Service Provider silently
send partner Communication directly
bypass Permission or Policy
expose restricted contacts, commissions, contracts or bank data
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

Partner API may expose:

```text
PartnerCreated
ServiceNetworkLinked
CommunicationCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Partner events directly.
- PartnerCreated must not be treated as contract approval, commission settlement, Customer creation, Service Provider creation or Service Network membership.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] partner_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] partner_organization_reference_id is valid where provided.
[ ] service_network_reference_id is valid where provided.
[ ] customer_reference_id is valid where provided.
[ ] order_reference_id is valid where provided.
[ ] matter_reference_id is valid where provided.
[ ] partner_type is controlled.
[ ] partner_status is controlled.
[ ] qualification_status is controlled.
[ ] source_type is controlled.
[ ] qualification_mode is controlled where applicable.
[ ] qualification_purpose is controlled where applicable.
[ ] link_type is controlled where applicable.
[ ] draft_purpose is controlled where applicable.
[ ] order_context_purpose is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted partner/contact/commission/contract/bank/performance fields are omitted or allowed.
[ ] AI-inferred partner data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] PartnerCreated is emitted after createPartner succeeds.
[ ] Qualification does not approve contract or commission.
[ ] Network link preparation does not create Service Network link automatically.
[ ] Communication preparation routes through Communication Service if Communication is created.
[ ] Order context preparation routes through Order Service if Order is created or updated.
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
PartnerReferenceInvalid
OrganizationReferenceInvalid
ServiceNetworkReferenceInvalid
CustomerReferenceInvalid
OrderReferenceInvalid
MatterReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
QualificationRejected
NetworkLinkInvalid
RestrictedFieldViolation
RestrictedPartnerData
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
- Errors must not expose restricted Partner data.
- Errors must not expose contacts, commissions, bank data, contracts, performance notes or internal strategy.
- Errors must not expose unrelated Customer, Order, Matter, Service Provider or Service Network details.
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
- partner_type, partner_status, qualification_status, link_type and preparation_status changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI partner qualification/link behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Partner API spec
cite Partner Service Specification
cite Partner Object Specification
cite PartnerCreated Event Specification
cite Organization/Service Network/Communication/Order specs where downstream operations are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid partner_reference_id
write tests for invalid organization/network/customer/order/matter references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Partner creation does not create Customer, Service Provider or Service Network membership
write tests that Partner creation does not approve commission, contract or payment
write tests that network link preparation does not emit ServiceNetworkLinked directly
write tests that Communication preparation routes through Communication Service
write tests that Order context preparation routes through Order Service where required
write tests for AI Agent Contract and human review requirement
write tests for PartnerCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Partner Service
allow UI to emit PartnerCreated directly
treat Partner as Customer
treat Partner as Service Provider
treat Partner as Service Network member without governed link
treat Partner as commission settlement or payment authority
create Customer, Order, Service Provider or Service Network membership through Partner API silently
expose contacts, commissions, bank data, contracts or performance notes for convenience
allow AI to fabricate Partner references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Partner API purpose.
[ ] It defines Partner API meaning.
[ ] It defines Partner API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, qualification, organization link, service-network link preparation, communication preparation, order context preparation and event-list operations.
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
| 0.1.0 | Draft | Initial Partner API specification. Defines governed Partner business-collaboration interface and separates Partner API from Customer, Service Provider, Service Network membership, Routing, payment, commission settlement, legal authority and AI partner approval. |

---

**End of API Specification**
