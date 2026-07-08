# API Specification — Service Network API

**Spec ID:** B02-API-SERVICE-NETWORK  
**Spec Type:** API Specification  
**API Name:** Service Network API  
**API File:** core-specs/api/service-network-api.md  
**Related Domain:** core-specs/domains/service-network.md  
**Related Object Specs:** core-specs/objects/service-network.md; core-specs/objects/service-provider.md; core-specs/objects/partner.md; core-specs/objects/routing.md; core-specs/objects/jurisdiction.md; core-specs/objects/capability.md; core-specs/objects/organization.md; core-specs/objects/communication.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/service-network-service.md; core-specs/services/service-provider-service.md; core-specs/services/partner-service.md; core-specs/services/routing-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/communication-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/service-network-linked.md; core-specs/events/service-provider-created.md; core-specs/events/partner-created.md; core-specs/events/routing-evaluated.md; core-specs/events/routing-selected.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/service-network-api-contract.md; core-specs/contracts/events/service-network-linked-payload.md  
**Related Agent Specs:** core-specs/agents/service-network-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 5 — Network Expansion Reserved  
**MVP Depth:** Reserved / Later Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Service Network API exposes governed Service Network creation, membership, linkage, visibility and routing-support operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate, link and evaluate Service Network references without treating Service Network as Service Provider, Partner, selected route, order assignment, payment settlement, commission settlement, legal authority, contract approval, operational marketplace or AI-approved provider network.

Service Network API exists to support:

```text
service network reference creation
provider and partner network organization
jurisdiction/service capability network context
network membership preparation and governance
routing candidate pool preparation
partner / service-provider network linkage
network communication preparation
policy-controlled network visibility
AI-assisted network analysis under governance
event trace access
API-safe service network reference validation
```

Service Network API does not select providers by itself, assign orders, approve contracts, authorize payment, approve commissions, prove legal authority or replace network governance.

---

# 2. API Meaning

Service Network API means:

```text
a governed interface for operating Service Network references and membership context through Service Network Service.
```

Service Network API does not mean:

```text
Service Provider API
Partner API
Routing API
Order assignment API
payment API
commission settlement API
legal authority API
marketplace transaction API
AI network approval API
```

Service Network organizes network relationships.

Service Provider owns external service-capability context.

Partner owns collaboration relationship context.

Routing evaluates and selects service candidates.

Order and Matter own execution context.

---

# 3. API Boundary

Service Network API is responsible for:

```text
Service Network create request intake
Service Network read/search/list access
Service Network update request intake
Service Network reference validation
Service Provider and Partner link request intake
network membership visibility governance
network routing-scope preparation
network qualification / health review request intake
network communication preparation
safe Service Network response shaping
Permission/Policy enforcement for Service Network operations
Service Network-related Event reference exposure where allowed
AI Agent access boundary for Service Network operations
controlled API errors
```

Service Network API is not responsible for:

```text
Service Provider lifecycle ownership
Partner lifecycle ownership
Routing selection
Order assignment
Task execution
payment or commission settlement
contract execution
legal authority verification by itself
communication delivery
professional decision approval
AI final network or provider approval
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/service-network.md
```

Domain rule:

```text
Service Network organizes governed service relationship networks.
Service Network is not Service Provider, Partner, Routing selection, Order assignment, payment, commission settlement, contract approval, legal authority or professional truth by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/service-network.md
core-specs/objects/service-provider.md
core-specs/objects/partner.md
core-specs/objects/routing.md
core-specs/objects/jurisdiction.md
core-specs/objects/capability.md
core-specs/objects/organization.md
core-specs/objects/communication.md
core-specs/objects/order.md
core-specs/objects/matter.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Service Network API returns service_network_reference_id.
- Service Network API may reference Service Provider, Partner, Routing, Jurisdiction, Capability, Organization, Communication, Order and Matter context but must not create or execute them silently.
- Service Network link is not provider selection.
- Service Network membership is not payment, contract or legal authority approval.
- Service Network visibility must be policy-filtered and context-specific.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/service-network-service.md
core-specs/services/service-provider-service.md
core-specs/services/partner-service.md
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
- Service Network API must invoke Service Network Service for Service Network behavior.
- Service Network API must validate related references through their owning services where required.
- Service Network API must invoke Permission Service before protected operations.
- Service Network API must invoke Policy Service before visibility, link, qualification and routing-scope operations.
- Service Network API must not emit ServiceNetworkLinked directly; Service Network Service and Event Service govern events.
- Routing selection must route through Routing Service.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/service-network-linked.md
core-specs/events/service-provider-created.md
core-specs/events/partner-created.md
core-specs/events/routing-evaluated.md
core-specs/events/routing-selected.md
core-specs/events/communication-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- linkServiceNetworkMember may result in ServiceNetworkLinked.
- routing evaluation must use Routing Service and may result in RoutingEvaluated.
- routing selection must use Routing Service and may result in RoutingSelected.
- network communication must use Communication Service and may result in CommunicationCreated.
- API consumers must not fabricate ServiceNetworkLinked.
- ServiceNetworkLinked is network relationship trace, not provider selection, order assignment, payment, commission, legal authority or contract approval.
```

---

# 8. API Operations

## 8.1 Operation: Create Service Network

**Operation Category:** Create  
**Method:** POST  
**Path:** `/service-networks`  
**Owning Service Operation:** `createServiceNetwork`  
**Permission Required:** `service-network:create`  
**Policy Required:** `ServiceNetworkCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-inferred  
**Event Behavior:** Service May Emit ServiceNetworkCreated where event is defined

Meaning:

```text
Create a governed Service Network reference.
```

Non-meaning:

```text
does not create Service Provider
does not create Partner
does not create membership automatically
does not select route
does not assign Order
does not approve payment or commission
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
Service Network Service createServiceNetwork
  ↓
Event Service record event where applicable
  ↓
Safe API response
```

## 8.2 Operation: Get Service Network

**Operation Category:** Read  
**Method:** GET  
**Path:** `/service-networks/{service_network_reference_id}`  
**Owning Service Operation:** `getServiceNetwork`  
**Permission Required:** `service-network:read`  
**Policy Required:** `ServiceNetworkVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Service Network view.
```

Non-meaning:

```text
does not expose private member terms automatically
does not expose internal scoring or routing strategy automatically
does not authorize network operations automatically
```

## 8.3 Operation: Search Service Networks

**Operation Category:** Search  
**Method:** GET  
**Path:** `/service-networks`  
**Owning Service Operation:** `searchServiceNetworks`  
**Permission Required:** `service-network:search`  
**Policy Required:** `ServiceNetworkVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Service Network references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted network directory access
does not expose restricted membership, pricing, commissions, contracts, scoring or strategy data by default
```

## 8.4 Operation: Update Service Network

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/service-networks/{service_network_reference_id}`  
**Owning Service Operation:** `updateServiceNetwork`  
**Permission Required:** `service-network:update`  
**Policy Required:** `ServiceNetworkUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit ServiceNetworkUpdated where event is defined

Meaning:

```text
Update governed Service Network metadata, status, scope or safe summary under Service Network Service rules.
```

Non-meaning:

```text
does not update member status automatically
does not approve contract or commission automatically
does not select providers or assign orders
```

## 8.5 Operation: Validate Service Network Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/service-networks/reference/validate`  
**Owning Service Operation:** `validateServiceNetworkReference`  
**Permission Required:** `service-network:validate`  
**Policy Required:** `ServiceNetworkReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Service Network reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not authorize membership
does not authorize routing selection
does not authorize order assignment
does not prove provider or partner qualification
```

## 8.6 Operation: Link Service Network Member

**Operation Category:** Link  
**Method:** POST  
**Path:** `/service-networks/{service_network_reference_id}/members/link`  
**Owning Service Operation:** `linkServiceNetworkMember`  
**Permission Required:** `service-network:member:link`  
**Policy Required:** `ServiceNetworkMemberLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service Must Emit ServiceNetworkLinked

Meaning:

```text
Create a governed relationship between Service Network and Service Provider, Partner or Organization member.
```

Non-meaning:

```text
does not select route
does not assign order
does not approve contract
does not approve commission or payment
does not prove legal authority
```

## 8.7 Operation: List Service Network Members

**Operation Category:** Read  
**Method:** GET  
**Path:** `/service-networks/{service_network_reference_id}/members`  
**Owning Service Operation:** `listServiceNetworkMembers`  
**Permission Required:** `service-network:member:read`  
**Policy Required:** `ServiceNetworkMemberVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Service Network member references.
```

Non-meaning:

```text
does not expose restricted member terms automatically
does not prove member availability
does not select member for work
```

## 8.8 Operation: Evaluate Service Network Health

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/service-networks/{service_network_reference_id}/health/evaluate`  
**Owning Service Operation:** `evaluateServiceNetworkHealth`  
**Permission Required:** `service-network:health:evaluate`  
**Policy Required:** `ServiceNetworkHealthPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** May emit PolicyEvaluated; must not select route

Meaning:

```text
Generate a governed health or readiness assessment for a Service Network.
```

Non-meaning:

```text
does not remove or approve members
does not select providers
does not approve contracts or commissions
does not replace governance review
```

## 8.9 Operation: Prepare Routing Scope from Service Network

**Operation Category:** Action  
**Method:** POST  
**Path:** `/service-networks/{service_network_reference_id}/routing-scope/prepare`  
**Owning Service Operation:** `prepareRoutingScopeFromServiceNetwork`  
**Permission Required:** `service-network:routing-scope:prepare`  
**Policy Required:** `ServiceNetworkRoutingScopePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Must route through Routing Service if Routing evaluation is created

Meaning:

```text
Prepare a governed Routing candidate scope from Service Network membership.
```

Non-meaning:

```text
does not evaluate routing automatically unless Routing Service accepts it
does not select provider
does not assign order
does not approve payment or contract
```

## 8.10 Operation: Prepare Service Network Communication

**Operation Category:** Action  
**Method:** POST  
**Path:** `/service-networks/{service_network_reference_id}/communications/prepare`  
**Owning Service Operation:** `prepareServiceNetworkCommunication`  
**Permission Required:** `service-network:communication:prepare`  
**Policy Required:** `ServiceNetworkCommunicationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Must route through Communication Service if Communication is created

Meaning:

```text
Prepare governed Communication draft or request involving Service Network context.
```

Non-meaning:

```text
does not create Communication unless Communication Service accepts it
does not send message
does not approve external wording
does not create member obligations
```

## 8.11 Operation: List Service Network Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/service-networks/{service_network_reference_id}/events`  
**Owning Service Operation:** `listServiceNetworkEvents`  
**Permission Required:** `service-network:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Service Network-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Service Network Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  service_network_type: string
  service_network_status: string | optional
  service_network_name: string
  network_scope: string
  primary_jurisdiction_reference_id: string | null
  safe_summary: string | null
  source_type: string
  request_context: object
  ai_context:
    ai_inferred: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Service Network Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  service_network_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  service_network_status: string | optional
  service_network_name: string | optional
  network_scope: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Service Network Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  service_network_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Service Network Member Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
path_parameters:
  service_network_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  member_type: string
  member_reference_id: string
  link_type: string
  link_status: string | optional
  link_reason: string | null
  request_context: object
  ai_context:
    ai_suggested: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.5 Evaluate Service Network Health Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  health_evaluation_purpose: string
  evaluation_mode: string
  target_context:
    jurisdiction_reference_id: string | null
    service_type: string | null
    order_reference_id: string | null
    matter_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.6 Prepare Routing Scope Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  routing_scope_purpose: string
  target_context:
    jurisdiction_reference_id: string | null
    service_type: string | null
    order_reference_id: string | null
    matter_reference_id: string | null
  include_member_types: list[string]
  candidate_filter_mode: string
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.7 Prepare Service Network Communication Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  draft_purpose: string
  communication_type: string
  target_context:
    member_type: string | null
    member_reference_id: string | null
    order_reference_id: string | null
    matter_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include bank data, commission terms, private contacts, contract secrets, credentials, restricted scores or performance notes by default.
- Requests must use controlled service_network_type, service_network_status, network_scope, member_type, link_type, link_status, source_type, evaluation_mode and routing_scope_purpose values.
- AI-inferred or AI-suggested network data must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Service Network Response

```yaml
status: 200
body:
  service_network_reference_id: string
  service_network_type: string
  service_network_status: string
  service_network_name: string
  network_scope: string
  primary_jurisdiction_reference_id: string | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    network_summary: string | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Service Network Response

```yaml
status: 201
body:
  service_network_reference_id: string
  service_network_status: string
  review_required: boolean
  related_event_reference_ids: list[string]
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Service Network Reference Validation Response

```yaml
status: 200
body:
  service_network_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Service Network Member Link Response

```yaml
status: 201
body:
  service_network_reference_id: string
  service_network_link_reference_id: string
  member_type: string
  member_reference_id: string
  link_type: string
  link_status: string
  review_required: boolean
  related_event_reference_ids:
    - service_network_linked_event_id
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.5 Service Network Members Response

```yaml
status: 200
body:
  service_network_reference_id: string
  members:
    - service_network_link_reference_id: string
      member_type: string
      member_reference_id: string
      link_type: string
      link_status: string
      safe_summary: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Health Evaluation / Routing Scope Response

```yaml
status: 200
body:
  service_network_reference_id: string
  preparation_reference_id: string | null
  evaluation_reference_id: string | null
  preparation_status: string
  safe_summary:
    usable: boolean
    candidate_count: integer | null
    missing_items: list[string]
    warnings: list[string]
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply Routing selection, Order assignment, payment authorization, commission settlement, contract approval, legal authority or service execution.
- Responses must not expose restricted contacts, commission terms, bank details, agreements, performance notes, scoring or internal strategy by default.
- Responses must distinguish Service Network references from Service Provider, Partner, Routing, Order and Matter references.
- Responses must identify review requirements for AI-inferred or AI-assisted network data.
```

---

# 11. Controlled Values

## 11.1 service_network_type

```text
GlobalServiceNetwork
RegionalServiceNetwork
JurisdictionServiceNetwork
TrademarkServiceNetwork
PartnerNetwork
ProviderNetwork
InternalNetwork
Unknown
```

## 11.2 service_network_status

```text
Draft
Active
ReviewRequired
Suspended
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 network_scope

```text
Global
Regional
Jurisdiction
ServiceType
PartnerGroup
ProviderGroup
Internal
Unknown
```

## 11.4 member_type

```text
ServiceProvider
Partner
Organization
InternalTeam
Unknown
```

## 11.5 link_type

```text
NetworkMember
PreferredMember
BackupMember
RestrictedMember
RegionalMember
JurisdictionMember
ServiceTypeMember
ReferenceOnly
Unknown
```

## 11.6 link_status

```text
Draft
Active
ReviewRequired
Suspended
Restricted
Expired
Archived
Unknown
```

## 11.7 source_type

```text
ProfessionalInput
PartnerDerived
ServiceProviderDerived
RoutingDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.8 evaluation_mode

```text
Preview
AIAssistedDraft
HumanReview
FinalEvaluation
Unknown
```

## 11.9 health_evaluation_purpose

```text
NetworkReadiness
CoverageReview
RiskReview
JurisdictionCoverage
ServiceCoverage
RoutingPreparation
AIAssistedReview
Unknown
```

## 11.10 routing_scope_purpose

```text
CandidatePoolPreparation
JurisdictionRouting
ServiceProviderRouting
OrderRouting
MatterRouting
AIAssistedRouting
Unknown
```

## 11.11 candidate_filter_mode

```text
PreferredOnly
ActiveOnly
IncludeBackup
IncludeRestrictedForReview
AllVisible
Unknown
```

## 11.12 preparation_status

```text
Prepared
Rejected
PolicyRestricted
PermissionDenied
ReviewRequired
DownstreamServiceRequired
Unknown
```

## 11.13 validation_status

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

## 11.14 intended_use

```text
MemberLink
RoutingScopePreparation
NetworkHealthReview
CommunicationPreparation
OrderPreparation
MatterPreparation
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
service-network:create
service-network:read
service-network:search
service-network:update
service-network:validate
service-network:member:link
service-network:member:read
service-network:health:evaluate
service-network:routing-scope:prepare
service-network:communication:prepare
service-network:event:read
```

Rules:

```text
- Service Network read/search must be permission-controlled.
- Service Network creation must not imply membership, provider selection or routing selection.
- Service Network validation must not authorize membership or routing.
- Member linking, member listing, health evaluation, routing-scope preparation and communication preparation require separate permissions.
- Downstream Routing and Communication operations require their owning permissions.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
ServiceNetworkCreationPolicy
ServiceNetworkUpdatePolicy
ServiceNetworkVisibilityPolicy
ServiceNetworkReferencePolicy
ServiceNetworkMemberLinkPolicy
ServiceNetworkMemberVisibilityPolicy
ServiceNetworkHealthPolicy
ServiceNetworkRoutingScopePolicy
ServiceNetworkCommunicationPolicy
EventVisibilityPolicy
AIAgentServiceNetworkAccessPolicy
RestrictedServiceNetworkDataPolicy
CrossOrganizationServiceNetworkPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Service Network fields.
- Policy may require human review for AI-inferred network records and AI-assisted link/routing-scope operations.
- Policy may restrict cross-organization Service Network lookup.
- Policy may restrict member lists, private contacts, commission terms, bank data, contracts, performance notes, scoring and internal strategy.
- Policy may restrict member linking, routing-scope preparation and network communication preparation.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Service Network: Restricted / HumanReviewRequired where AI-inferred
Get Service Network: Restricted
Search Service Networks: Restricted
Update Service Network: Restricted / HumanReviewRequired where sensitive
Validate Service Network Reference: Allowed under contract
Link Service Network Member: Restricted / HumanReviewRequired where AI-suggested
List Service Network Members: Restricted
Evaluate Service Network Health: Restricted / HumanReviewRequired
Prepare Routing Scope from Service Network: Restricted / HumanReviewRequired
Prepare Service Network Communication: Restricted / HumanReviewRequired where AI-drafted
List Service Network Events: Restricted
```

AI Agents may:

```text
summarize safe Service Network metadata
flag missing network membership or coverage context
validate Service Network references for authorized actions
suggest member links for human review
prepare network health review draft for human review
prepare routing candidate scope for human review
prepare network Communication draft for human review
```

AI Agents must not:

```text
fabricate Service Network
fabricate ServiceNetworkLinked events
treat AI-inferred network data as confirmed network truth
approve membership without governed review where required
select providers or assign Orders
approve contract, commission or payment
send network Communication directly
bypass Permission or Policy
expose restricted member lists, contacts, commissions, contracts or bank data
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

Service Network API may expose:

```text
ServiceNetworkLinked
ServiceProviderCreated
PartnerCreated
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
- API clients must not create Service Network events directly.
- ServiceNetworkLinked must not be treated as provider selection, Order assignment, payment authorization, commission settlement, contract approval or legal authority.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] service_network_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] primary_jurisdiction_reference_id is valid where provided.
[ ] member_reference_id is valid for the given member_type.
[ ] service_provider_reference_id is valid where provided.
[ ] partner_reference_id is valid where provided.
[ ] order_reference_id is valid where provided.
[ ] matter_reference_id is valid where provided.
[ ] service_network_type is controlled.
[ ] service_network_status is controlled.
[ ] network_scope is controlled.
[ ] member_type is controlled.
[ ] link_type is controlled.
[ ] link_status is controlled.
[ ] source_type is controlled.
[ ] evaluation_mode is controlled where applicable.
[ ] routing_scope_purpose is controlled where applicable.
[ ] candidate_filter_mode is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted network/member/contact/commission/contract/bank/performance fields are omitted or allowed.
[ ] AI-inferred or AI-suggested network data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] ServiceNetworkLinked is emitted after linkServiceNetworkMember succeeds.
[ ] Member link does not select route or assign Order.
[ ] Routing-scope preparation routes through Routing Service where Routing evaluation is created.
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
ServiceNetworkReferenceInvalid
MemberReferenceInvalid
ServiceProviderReferenceInvalid
PartnerReferenceInvalid
OrganizationReferenceInvalid
JurisdictionReferenceInvalid
OrderReferenceInvalid
MatterReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
MemberLinkInvalid
RoutingScopeInvalid
RestrictedFieldViolation
RestrictedServiceNetworkData
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
- Errors must not expose restricted Service Network data.
- Errors must not expose member private contacts, commissions, bank data, contracts, performance notes, scoring or internal strategy.
- Errors must not expose unrelated Service Provider, Partner, Routing, Order or Matter details.
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
- service_network_type, service_network_status, network_scope, member_type, link_type, link_status and preparation_status changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI network health/routing-scope behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Service Network API spec
cite Service Network Service Specification
cite Service Network Object Specification
cite ServiceNetworkLinked Event Specification
cite Service Provider/Partner/Routing/Communication specs where downstream operations are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata and safe member summaries by default
write tests for invalid service_network_reference_id
write tests for invalid member/provider/partner/order/matter references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Service Network creation does not create members automatically
write tests that member linking does not select route or assign Order
write tests that ServiceNetworkLinked is emitted after successful link
write tests that routing-scope preparation does not emit RoutingSelected directly
write tests that Communication preparation routes through Communication Service
write tests for AI Agent Contract and human review requirement
```

Codex must not:

```text
write directly to database bypassing Service Network Service
allow UI to emit ServiceNetworkLinked directly
treat Service Network as Service Provider
treat Service Network as Partner
treat Service Network membership as route selection
treat Service Network membership as payment, commission, contract or legal authority approval
select provider or assign Order through Service Network API
expose member contacts, commissions, bank data, contracts or performance notes for convenience
allow AI to fabricate Service Network references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Service Network API purpose.
[ ] It defines Service Network API meaning.
[ ] It defines Service Network API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, member link, member list, health evaluation, routing-scope preparation, communication preparation and event-list operations.
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
| 0.1.0 | Draft | Initial Service Network API specification. Defines governed Service Network relationship-network interface and separates Service Network API from Service Provider, Partner, Routing selection, Order assignment, payment, commission settlement, contract approval, legal authority and AI network approval. |

---

**End of API Specification**
