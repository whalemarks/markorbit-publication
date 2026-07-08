# API Specification — Opportunity API

**Spec ID:** B02-API-OPPORTUNITY  
**Spec Type:** API Specification  
**API Name:** Opportunity API  
**API File:** core-specs/api/opportunity-api.md  
**Related Domain:** core-specs/domains/opportunity.md  
**Related Object Specs:** core-specs/objects/opportunity.md; core-specs/objects/customer.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification.md; core-specs/objects/communication.md; core-specs/objects/document.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/opportunity-service.md; core-specs/services/customer-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/classification-service.md; core-specs/services/communication-service.md; core-specs/services/document-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/order-created.md; core-specs/events/customer-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/opportunity-api-contract.md  
**Related Agent Specs:** core-specs/agents/opportunity-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 4 — Collaboration / Growth Core  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Opportunity API exposes governed Opportunity operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate, score and prepare Opportunity references without treating Opportunity as Customer, confirmed instruction, Order, payment, legal mandate, Matter, filing decision, routing decision, sales contract or AI-approved commercial transaction.

Opportunity API exists to support:

```text
potential business opportunity context
lead-to-customer preparation
customer demand discovery
brand/trademark/jurisdiction opportunity context
communication-derived opportunity context
order preparation
sales and service intake separation
policy-controlled opportunity visibility
AI-assisted opportunity analysis under governance
event trace access
API-safe opportunity reference validation
```

Opportunity API does not create Customer automatically, confirm service scope, create Order automatically, settle payment, approve legal instruction or replace business confirmation.

---

# 2. API Meaning

Opportunity API means:

```text
a governed interface for operating potential business opportunity context through Opportunity Service.
```

Opportunity API does not mean:

```text
Customer API
Order API
Matter API
Payment API
Sales contract API
legal instruction API
Routing API
Communication API
AI deal approval API
```

Opportunity is pre-order commercial context.

Customer is business relationship context.

Order is confirmed commercial service context.

Matter is professional case context.

---

# 3. API Boundary

Opportunity API is responsible for:

```text
Opportunity create request intake
Opportunity read/search/list access
Opportunity update request intake
Opportunity reference validation
Opportunity scoring and qualification request intake where explicitly governed
Opportunity-to-object link request intake where explicitly governed
Order preparation from Opportunity
safe Opportunity response shaping
Permission/Policy enforcement for Opportunity operations
Opportunity-related Event reference exposure where allowed
AI Agent access boundary for Opportunity operations
controlled API errors
```

Opportunity API is not responsible for:

```text
Customer lifecycle ownership
Order creation unless explicit governed operation is called
Matter creation
payment or invoice ownership
legal instruction approval
official filing execution
service provider routing
communication delivery
professional conclusion
AI final commercial decision
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/opportunity.md
```

Domain rule:

```text
Opportunity represents potential business demand.
Opportunity is not Customer, Order, Matter, payment, instruction approval or legal mandate by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/opportunity.md
core-specs/objects/customer.md
core-specs/objects/order.md
core-specs/objects/matter.md
core-specs/objects/brand.md
core-specs/objects/trademark.md
core-specs/objects/jurisdiction.md
core-specs/objects/classification.md
core-specs/objects/communication.md
core-specs/objects/document.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Opportunity API returns opportunity_reference_id.
- Opportunity API may reference Customer, Brand, Trademark, Jurisdiction, Classification, Communication, Document, Order or Matter context but must not create them silently unless explicitly defined by a governed operation.
- Opportunity API must not treat Opportunity as Customer confirmation.
- Opportunity API must not treat Opportunity as Order or paid service.
- Opportunity API must not expose restricted sales strategy, customer data, pricing assumptions or communication content by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/opportunity-service.md
core-specs/services/customer-service.md
core-specs/services/order-service.md
core-specs/services/matter-service.md
core-specs/services/brand-service.md
core-specs/services/trademark-service.md
core-specs/services/jurisdiction-service.md
core-specs/services/classification-service.md
core-specs/services/communication-service.md
core-specs/services/document-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Opportunity API must invoke Opportunity Service for Opportunity behavior.
- Opportunity API must validate related references through their owning services where required.
- Opportunity API must invoke Permission Service where operation requires authorization.
- Opportunity API must invoke Policy Service where contextual constraints apply.
- Opportunity API must not emit Opportunity events directly; Opportunity Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/customer-created.md
core-specs/events/order-created.md
core-specs/events/communication-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- Opportunity operations may reference CustomerCreated, OrderCreated and CommunicationCreated events.
- createOrderFromOpportunity must use Order Service and may result in OrderCreated.
- createCustomerFromOpportunity must use Customer Service and may result in CustomerCreated.
- API consumers must not fabricate downstream events.
- Opportunity state changes are not confirmed Order or Customer creation unless owning service creates them.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Opportunity

**Operation Category:** Create  
**Method:** POST  
**Path:** `/opportunities`  
**Owning Service Operation:** `createOpportunity`  
**Permission Required:** `opportunity:create`  
**Policy Required:** `OpportunityCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-inferred  
**Event Behavior:** Service May Emit OpportunityCreated where event is defined

Meaning:

```text
Create a governed Opportunity potential-demand context.
```

Non-meaning:

```text
does not create Customer automatically
does not create Order
does not create Matter
does not approve service scope
does not accept legal instruction
does not settle payment
does not grant Permission
```

Expected service call:

```text
API
  ↓
Permission Service evaluatePermission
  ↓
Policy Service evaluatePolicy where required
  ↓
Opportunity Service createOpportunity
  ↓
Event Service record event where applicable
  ↓
Safe API response
```

## 8.2 Operation: Get Opportunity

**Operation Category:** Read  
**Method:** GET  
**Path:** `/opportunities/{opportunity_reference_id}`  
**Owning Service Operation:** `getOpportunity`  
**Permission Required:** `opportunity:read`  
**Policy Required:** `OpportunityVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Opportunity view.
```

Non-meaning:

```text
does not expose restricted sales strategy automatically
does not expose customer contact details automatically
does not expose communication content automatically
does not assert confirmed order or instruction automatically
```

## 8.3 Operation: Search Opportunities

**Operation Category:** Search  
**Method:** GET  
**Path:** `/opportunities`  
**Owning Service Operation:** `searchOpportunities`  
**Permission Required:** `opportunity:search`  
**Policy Required:** `OpportunityVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Opportunity references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted sales pipeline access
does not expose restricted commercial, customer, communication or pricing data by default
```

## 8.4 Operation: Update Opportunity

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/opportunities/{opportunity_reference_id}`  
**Owning Service Operation:** `updateOpportunity`  
**Permission Required:** `opportunity:update`  
**Policy Required:** `OpportunityUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit OpportunityUpdated where event is defined

Meaning:

```text
Update governed Opportunity metadata, status, qualification or context under Opportunity Service rules.
```

Non-meaning:

```text
does not create Customer, Order or Matter automatically
does not approve commercial terms automatically
does not approve legal instruction
does not settle payment
```

## 8.5 Operation: Validate Opportunity Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/opportunities/reference/validate`  
**Owning Service Operation:** `validateOpportunityReference`  
**Permission Required:** `opportunity:validate`  
**Policy Required:** `OpportunityReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that an Opportunity reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not prove customer confirmation
does not authorize order creation
does not approve pricing
does not prove legal instruction
```

## 8.6 Operation: Link Opportunity to Object

**Operation Category:** Link  
**Method:** POST  
**Path:** `/opportunities/{opportunity_reference_id}/links`  
**Owning Service Operation:** `linkOpportunityToObject`  
**Permission Required:** `opportunity:link`  
**Policy Required:** `OpportunityLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit OpportunityUpdated or future LinkEvent where defined

Meaning:

```text
Create a governed relationship between Opportunity and a target Core object.
```

Non-meaning:

```text
does not create target object
does not create Customer
does not create Order or Matter
does not approve commercial transaction
```

## 8.7 Operation: Qualify Opportunity

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/opportunities/{opportunity_reference_id}/qualify`  
**Owning Service Operation:** `qualifyOpportunity`  
**Permission Required:** `opportunity:qualify`  
**Policy Required:** `OpportunityQualificationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Service May Emit PolicyEvaluated; must not create Customer/Order automatically

Meaning:

```text
Generate or record a governed qualification result for an Opportunity.
```

Non-meaning:

```text
does not confirm customer
does not create order
does not approve pricing or service scope
does not replace human sales/business review
```

## 8.8 Operation: Prepare Order from Opportunity

**Operation Category:** Action  
**Method:** POST  
**Path:** `/opportunities/{opportunity_reference_id}/orders/prepare`  
**Owning Service Operation:** `prepareOrderFromOpportunity`  
**Permission Required:** `opportunity:order:prepare`  
**Policy Required:** `OpportunityOrderPreparationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit OrderCreated unless Order Service creates Order

Meaning:

```text
Prepare a governed Order draft context from Opportunity context.
```

Non-meaning:

```text
does not create Order automatically
does not accept commercial terms
does not create Matter
does not settle payment
```

## 8.9 Operation: Create Customer from Opportunity

**Operation Category:** Action  
**Method:** POST  
**Path:** `/opportunities/{opportunity_reference_id}/customers/create`  
**Owning Service Operation:** `createCustomerFromOpportunity`  
**Permission Required:** `opportunity:customer:create`  
**Policy Required:** `OpportunityCustomerCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-inferred  
**Event Behavior:** Must route through Customer Service; may emit CustomerCreated

Meaning:

```text
Create a governed Customer relationship from an approved Opportunity context.
```

Non-meaning:

```text
does not create Order
does not prove legal ownership
does not approve service instruction
does not authorize billing
```

## 8.10 Operation: Create Order from Opportunity

**Operation Category:** Action  
**Method:** POST  
**Path:** `/opportunities/{opportunity_reference_id}/orders/create`  
**Owning Service Operation:** `createOrderFromOpportunity`  
**Permission Required:** `opportunity:order:create`  
**Policy Required:** `OpportunityOrderCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Must route through Order Service; may emit OrderCreated

Meaning:

```text
Create a governed Order from an approved Opportunity context.
```

Non-meaning:

```text
does not settle payment
does not create Matter unless Order workflow explicitly does so
does not file application
does not approve professional conclusion
```

## 8.11 Operation: List Opportunity Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/opportunities/{opportunity_reference_id}/events`  
**Owning Service Operation:** `listOpportunityEvents`  
**Permission Required:** `opportunity:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Opportunity-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Opportunity Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  opportunity_type: string
  opportunity_status: string | optional
  qualification_status: string | optional
  customer_reference_id: string | null
  communication_reference_id: string | null
  brand_reference_id: string | null
  trademark_reference_id: string | null
  jurisdiction_reference_id: string | null
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_inferred: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Opportunity Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  opportunity_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  opportunity_status: string | optional
  qualification_status: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Opportunity Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  opportunity_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Opportunity to Object Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  opportunity_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  target_object_type: string
  target_object_reference_id: string
  link_type: string
  link_reason: string | null
  request_context: object
```

## 9.5 Qualify Opportunity Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  qualification_mode: string
  qualification_inputs:
    service_need_summary: string | null
    estimated_value_band: string | null
    urgency_level: string | null
    required_jurisdictions: list[string]
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.6 Prepare Order from Opportunity Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  intended_service_type: string
  customer_reference_id: string | null
  target_context:
    brand_reference_id: string | null
    trademark_reference_id: string | null
    jurisdiction_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.7 Create Customer from Opportunity Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
path_parameters:
  opportunity_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  customer_creation_mode: string
  request_context: object
```

## 9.8 Create Order from Opportunity Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
path_parameters:
  opportunity_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  order_creation_mode: string
  customer_reference_id: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include unrestricted contact data, payment data, pricing secrets, privileged notes or full communication content by default.
- Requests must use controlled opportunity_type, opportunity_status, qualification_status, source_type, link_type and creation_mode values.
- AI-inferred opportunity data must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Opportunity Response

```yaml
status: 200
body:
  opportunity_reference_id: string
  opportunity_type: string
  opportunity_status: string
  qualification_status: string
  customer_reference_id: string | null
  communication_reference_id: string | null
  brand_reference_id: string | null
  trademark_reference_id: string | null
  jurisdiction_reference_id: string | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    demand_summary: string | null
  linked_object_references:
    - target_object_type: string
      target_object_reference_id: string
      link_type: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Opportunity Response

```yaml
status: 201
body:
  opportunity_reference_id: string
  opportunity_status: string
  qualification_status: string
  review_required: boolean
  related_event_reference_ids: list[string]
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Opportunity Reference Validation Response

```yaml
status: 200
body:
  opportunity_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Opportunity Qualification Response

```yaml
status: 200
body:
  opportunity_reference_id: string
  qualification_reference_id: string | null
  qualification_status: string
  safe_summary:
    qualified: boolean
    risk_summary: string | null
    missing_items: list[string]
    recommended_next_action: string | null
  confidence_level: string
  human_review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.5 Order Preparation Response

```yaml
status: 200
body:
  opportunity_reference_id: string
  order_draft_reference_id: string | null
  usable_for_order_creation: boolean
  missing_items: list[string]
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Customer / Order Creation Response

```yaml
status: 200
body:
  opportunity_reference_id: string
  customer_reference_id: string | null
  order_reference_id: string | null
  creation_status: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply Customer confirmation, Order creation, payment, legal instruction or professional conclusion unless the owning service actually creates the downstream object.
- Responses must not expose restricted sales, pricing, contact, communication or strategy fields by default.
- Responses must distinguish Opportunity references from Customer, Order and Matter references.
- Responses must identify review requirements for AI-inferred or AI-prepared content.
```

---

# 11. Controlled Values

## 11.1 opportunity_type

```text
TrademarkSearchOpportunity
TrademarkFilingOpportunity
RenewalOpportunity
OfficeActionOpportunity
OppositionOpportunity
CancellationOpportunity
RecordalOpportunity
PortfolioOpportunity
ConsultationOpportunity
CrossSellOpportunity
Unknown
```

## 11.2 opportunity_status

```text
Draft
New
ReviewRequired
Qualified
Unqualified
ConvertedToCustomer
ConvertedToOrder
Lost
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 qualification_status

```text
Unqualified
Qualified
NeedsReview
InsufficientInformation
Rejected
Converted
Unknown
```

## 11.4 source_type

```text
ProfessionalInput
CustomerIntake
CommunicationDerived
MarketingDerived
PartnerInput
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.5 link_type

```text
PrimaryOpportunityObject
SupportingObject
SourceObject
RelatedObject
ConversionTarget
ReferenceOnly
Unknown
```

## 11.6 qualification_mode

```text
Preview
AIAssistedDraft
HumanReview
FinalQualification
Unknown
```

## 11.7 customer_creation_mode

```text
Preview
CreateDraftCustomer
CreateActiveCustomer
Unknown
```

## 11.8 order_creation_mode

```text
Preview
CreateDraftOrder
CreatePreparedOrder
CreateConfirmedOrder
Unknown
```

## 11.9 intended_service_type

```text
TrademarkSearch
TrademarkFiling
Renewal
OfficeAction
Opposition
Cancellation
Recordal
PortfolioManagement
Consultation
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
Archived
ContextMismatch
Unknown
```

## 11.12 intended_use

```text
CustomerPreparation
OrderPreparation
MatterPreparation
CommunicationContext
BrandContext
TrademarkContext
SalesPipeline
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
opportunity:create
opportunity:read
opportunity:search
opportunity:update
opportunity:validate
opportunity:link
opportunity:qualify
opportunity:order:prepare
opportunity:customer:create
opportunity:order:create
opportunity:event:read
```

Rules:

```text
- Opportunity read/search must be permission-controlled.
- Opportunity creation must not imply Customer, Order or Matter creation.
- Opportunity validation must not authorize conversion or legal instruction.
- Opportunity qualification requires separate permission.
- Customer/Order creation from Opportunity requires separate permission and downstream service authority.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
OpportunityCreationPolicy
OpportunityUpdatePolicy
OpportunityVisibilityPolicy
OpportunityReferencePolicy
OpportunityLinkPolicy
OpportunityQualificationPolicy
OpportunityOrderPreparationPolicy
OpportunityCustomerCreationPolicy
OpportunityOrderCreationPolicy
EventVisibilityPolicy
AIAgentOpportunityAccessPolicy
RestrictedOpportunityDataPolicy
CrossOrganizationOpportunityPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Opportunity fields.
- Policy may require human review for AI-inferred Opportunity data.
- Policy may restrict cross-organization Opportunity lookup.
- Policy may restrict pricing, contact details, communication content, sales strategy and privileged notes.
- Policy may restrict Customer/Order conversion.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Opportunity: Restricted / HumanReviewRequired where AI-inferred
Get Opportunity: Restricted
Search Opportunities: Restricted
Update Opportunity: Restricted / HumanReviewRequired where sensitive
Validate Opportunity Reference: Allowed under contract
Link Opportunity to Object: Restricted / HumanReviewRequired where AI-suggested
Qualify Opportunity: Restricted / HumanReviewRequired
Prepare Order from Opportunity: Restricted / HumanReviewRequired
Create Customer from Opportunity: Restricted / HumanReviewRequired
Create Order from Opportunity: Restricted / HumanReviewRequired
List Opportunity Events: Restricted
```

AI Agents may:

```text
summarize safe Opportunity metadata
flag missing opportunity context items
validate Opportunity references for authorized actions
suggest Opportunity-to-object links for human review
prepare qualification drafts for human review
prepare Customer or Order conversion drafts for human review
```

AI Agents must not:

```text
fabricate Opportunity
fabricate downstream CustomerCreated or OrderCreated events
treat AI-inferred Opportunity as confirmed demand
create Customer or Order silently
approve pricing or service scope
approve legal instruction
settle payment or trigger filing
bypass Permission or Policy
expose restricted sales/contact/communication data
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

Opportunity API may expose:

```text
CustomerCreated
OrderCreated
CommunicationCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create downstream events directly.
- Opportunity conversion events must not be treated as payment, filing, Matter creation or professional conclusion.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] opportunity_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] customer_reference_id is valid where provided.
[ ] communication_reference_id is valid where provided.
[ ] brand_reference_id is valid where provided.
[ ] trademark_reference_id is valid where provided.
[ ] jurisdiction_reference_id is valid where provided.
[ ] target_object_type and target_object_reference_id are valid for link operation.
[ ] opportunity_type is controlled.
[ ] opportunity_status is controlled.
[ ] qualification_status is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] qualification_mode is controlled where applicable.
[ ] customer_creation_mode is controlled where applicable.
[ ] order_creation_mode is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted sales/contact/pricing/communication/strategy fields are omitted or allowed.
[ ] AI-inferred opportunity data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] Opportunity preparation does not create Order automatically.
[ ] Customer creation routes through Customer Service.
[ ] Order creation routes through Order Service.
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
OpportunityReferenceInvalid
CustomerReferenceInvalid
CommunicationReferenceInvalid
BrandReferenceInvalid
TrademarkReferenceInvalid
JurisdictionReferenceInvalid
TargetObjectReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedOpportunityData
ConversionRestricted
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
- Errors must not expose restricted Opportunity data.
- Errors must not expose pricing, contact, communication, customer strategy or privileged notes.
- Errors must not expose unrelated Customer or Order details.
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
- opportunity_type, opportunity_status, qualification_status, source_type, link_type and conversion mode changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI opportunity behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Opportunity API spec
cite Opportunity Service Specification
cite Opportunity Object Specification
cite Customer/Order/Communication specs where downstream references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid opportunity_reference_id
write tests for invalid customer/communication/brand/trademark references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Opportunity creation does not create Customer or Order
write tests that qualification does not convert Opportunity automatically
write tests that Order preparation does not create Order automatically
write tests that Customer creation routes through Customer Service
write tests that Order creation routes through Order Service
write tests for AI Agent Contract and human review requirement
```

Codex must not:

```text
write directly to database bypassing Opportunity Service
fabricate CustomerCreated or OrderCreated events from Opportunity API
treat Opportunity as Customer
treat Opportunity as Order
treat Opportunity as payment or legal instruction
treat AI-inferred Opportunity as confirmed business fact
create Customer, Order or Matter silently from Opportunity operations
expose restricted sales/pricing/contact data for convenience
allow AI to fabricate Opportunity references or downstream events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Opportunity API purpose.
[ ] It defines Opportunity API meaning.
[ ] It defines Opportunity API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, link, qualify, order preparation, customer creation, order creation and event-list operations.
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
| 0.1.0 | Draft | Initial Opportunity API specification. Defines governed Opportunity potential-demand interface and separates Opportunity API from Customer, Order, Matter, payment, legal instruction, sales contract and AI deal approval. |

---

**End of API Specification**
