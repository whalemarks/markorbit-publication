# API Specification — Customer API

**Spec ID:** B02-API-CUSTOMER  
**Spec Type:** API Specification  
**API Name:** Customer API  
**API File:** core-specs/api/customer-api.md  
**Related Domain:** core-specs/domains/customer.md  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/organization.md; core-specs/objects/user.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/document.md; core-specs/objects/communication.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/customer-service.md; core-specs/services/organization-service.md; core-specs/services/user-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/document-service.md; core-specs/services/communication-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/customer-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/customer-api-contract.md; core-specs/contracts/events/customer-created-payload.md  
**Related Agent Specs:** core-specs/agents/customer-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Customer API exposes governed Customer relationship operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and link Customer references without treating Customer as Organization, User, Brand owner, Trademark owner, billing account, Order, Matter, legal applicant, decision-maker, communication contact or AI-inferred client identity.

Customer API exists to support:

```text
customer relationship reference creation
customer portfolio context
customer-to-brand/trademark/matter/order preparation
customer contact and organization context separation
policy-controlled customer visibility
business execution context
AI-assisted customer analysis under governance
event trace access
API-safe customer reference validation
```

Customer API does not prove legal ownership, create orders, create matters, approve instructions, define billing obligations or replace human/business confirmation.

---

# 2. API Meaning

Customer API means:

```text
a governed interface for operating Customer relationship references through Customer Service.
```

Customer API does not mean:

```text
Organization API
User API
Brand API
Trademark ownership API
Order API
Matter API
billing API
legal applicant API
communication contact API
AI customer identity API
```

Customer is the business relationship object.

Organization is operating context.

User is account/person context.

Brand/Trademark ownership requires separately governed relationships and evidence.

---

# 3. API Boundary

Customer API is responsible for:

```text
Customer create request intake
Customer read/search/list access
Customer update request intake
Customer reference validation
Customer link request intake where explicitly governed
safe Customer response shaping
Permission/Policy enforcement for Customer operations
Customer-related Event reference exposure where allowed
AI Agent access boundary for Customer operations
controlled API errors
```

Customer API is not responsible for:

```text
Organization lifecycle ownership
User lifecycle ownership
Order creation
Matter creation
billing/payment ownership
legal applicant ownership
Brand/Trademark ownership proof
official registry applicant truth
communication delivery
AI final customer determination
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/customer.md
```

Domain rule:

```text
Customer represents a business relationship context.
Customer is not Organization, User, legal owner, applicant, Order or Matter by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/customer.md
core-specs/objects/organization.md
core-specs/objects/user.md
core-specs/objects/brand.md
core-specs/objects/trademark.md
core-specs/objects/matter.md
core-specs/objects/order.md
core-specs/objects/document.md
core-specs/objects/communication.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Customer API returns customer_reference_id.
- Customer API may reference Organization and User context but must not create them silently unless explicitly defined by a governed operation.
- Customer API may link Brand, Trademark, Matter or Order context but must not create ownership, Matter or Order silently.
- Customer API must not treat Customer as legal applicant or trademark owner.
- Customer API must not expose restricted commercial terms, contact data or strategy by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/customer-service.md
core-specs/services/organization-service.md
core-specs/services/user-service.md
core-specs/services/brand-service.md
core-specs/services/trademark-service.md
core-specs/services/matter-service.md
core-specs/services/order-service.md
core-specs/services/document-service.md
core-specs/services/communication-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Customer API must invoke Customer Service for Customer behavior.
- Customer API must validate related references through their owning services where required.
- Customer API must invoke Permission Service where operation requires authorization.
- Customer API must invoke Policy Service where contextual constraints apply.
- Customer API must not emit Customer events directly; Customer Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/customer-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createCustomer may result in CustomerCreated.
- protected operations may produce PermissionEvaluated and PolicyEvaluated.
- API consumers must not fabricate CustomerCreated.
- CustomerCreated is business relationship trace, not legal ownership, applicant confirmation, Order or Matter creation.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Customer

**Operation Category:** Create  
**Method:** POST  
**Path:** `/customers`  
**Owning Service Operation:** `createCustomer`  
**Permission Required:** `customer:create`  
**Policy Required:** `CustomerCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-inferred  
**Event Behavior:** Service Must Emit CustomerCreated

Meaning:

```text
Create a governed Customer relationship reference.
```

Non-meaning:

```text
does not create Organization automatically
does not create User automatically
does not create Order
does not create Matter
does not prove legal ownership
does not prove applicant authority
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
Customer Service createCustomer
  ↓
Event Service record CustomerCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Customer

**Operation Category:** Read  
**Method:** GET  
**Path:** `/customers/{customer_reference_id}`  
**Owning Service Operation:** `getCustomer`  
**Permission Required:** `customer:read`  
**Policy Required:** `CustomerVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Customer relationship view.
```

Non-meaning:

```text
does not expose restricted commercial terms automatically
does not expose contact details automatically
does not prove legal applicant or ownership status automatically
```

## 8.3 Operation: Search Customers

**Operation Category:** Search  
**Method:** GET  
**Path:** `/customers`  
**Owning Service Operation:** `searchCustomers`  
**Permission Required:** `customer:search`  
**Policy Required:** `CustomerVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Customer references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted customer database access
does not expose restricted contact, commercial or strategy data by default
```

## 8.4 Operation: Update Customer

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/customers/{customer_reference_id}`  
**Owning Service Operation:** `updateCustomer`  
**Permission Required:** `customer:update`  
**Policy Required:** `CustomerUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit CustomerUpdated where event is defined

Meaning:

```text
Update governed Customer metadata, status or relationship context under Customer Service rules.
```

Non-meaning:

```text
does not update Organization or User automatically
does not update legal applicant status automatically
does not update Order or Matter state automatically
does not approve customer instructions
```

## 8.5 Operation: Validate Customer Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/customers/reference/validate`  
**Owning Service Operation:** `validateCustomerReference`  
**Permission Required:** `customer:validate`  
**Policy Required:** `CustomerReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Customer reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not prove legal ownership
does not authorize instruction
does not authorize billing
does not prove contact authority
```

## 8.6 Operation: Link Customer to Object

**Operation Category:** Link  
**Method:** POST  
**Path:** `/customers/{customer_reference_id}/links`  
**Owning Service Operation:** `linkCustomerToObject`  
**Permission Required:** `customer:link`  
**Policy Required:** `CustomerLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit CustomerUpdated or future LinkEvent where defined

Meaning:

```text
Create a governed relationship between Customer and a target Core object.
```

Non-meaning:

```text
does not create target object
does not prove ownership
does not create Order or Matter
does not approve filing instruction
```

## 8.7 Operation: Prepare Customer Intake Context

**Operation Category:** Action  
**Method:** POST  
**Path:** `/customers/{customer_reference_id}/intake-context/prepare`  
**Owning Service Operation:** `prepareCustomerIntakeContext`  
**Permission Required:** `customer:intake:prepare`  
**Policy Required:** `CustomerIntakePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Service May Emit PolicyEvaluated; must not create Order/Matter unless called separately

Meaning:

```text
Prepare a safe customer intake context for downstream Matter or Order creation.
```

Non-meaning:

```text
does not create Matter
does not create Order
does not approve service scope
does not accept customer instruction
```

## 8.8 Operation: List Customer Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/customers/{customer_reference_id}/events`  
**Owning Service Operation:** `listCustomerEvents`  
**Permission Required:** `customer:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Customer-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Customer Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  customer_type: string
  customer_status: string | optional
  customer_display_name: string
  related_organization_reference_id: string | null
  primary_user_reference_id: string | null
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_inferred: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Customer Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  customer_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  customer_status: string | optional
  customer_display_name: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Customer Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  customer_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Customer to Object Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  customer_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  target_object_type: string
  target_object_reference_id: string
  link_type: string
  link_reason: string | null
  request_context: object
```

## 9.5 Prepare Customer Intake Context Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  intended_service_type: string
  target_context:
    brand_reference_id: string | null
    trademark_reference_id: string | null
    jurisdiction_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include unrestricted contact data, payment data, personal secrets or privileged strategy by default.
- Requests must use controlled customer_type, customer_status, source_type, link_type and intended_use values.
- AI-inferred customer data must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Customer Response

```yaml
status: 200
body:
  customer_reference_id: string
  customer_type: string
  customer_status: string
  customer_display_name: string
  related_organization_reference_id: string | null
  primary_user_reference_id: string | null
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

## 10.2 Create Customer Response

```yaml
status: 201
body:
  customer_reference_id: string
  customer_status: string
  review_required: boolean
  related_event_reference_ids:
    - customer_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Customer Reference Validation Response

```yaml
status: 200
body:
  customer_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Customer Intake Context Response

```yaml
status: 200
body:
  customer_reference_id: string
  intake_context_reference_id: string | null
  intended_service_type: string
  safe_summary:
    usable_for_matter_preparation: boolean
    usable_for_order_preparation: boolean
    missing_items: list[string]
    review_required: boolean
  policy_decision_reference_id: string | null
  human_review_required: boolean
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply legal ownership, applicant authority, billing authorization or instruction approval.
- Responses must not expose restricted contact, commercial, payment or strategy fields by default.
- Responses must distinguish Customer references from Organization, User, Matter and Order references.
- Responses must identify review requirements for AI-inferred or AI-prepared content.
```

---

# 11. Controlled Values

## 11.1 customer_type

```text
Individual
Company
AgencyClient
DirectClient
PartnerClient
InternalClient
ProspectiveCustomer
Unknown
```

## 11.2 customer_status

```text
Draft
Active
ReviewRequired
Prospective
Suspended
Inactive
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 source_type

```text
ProfessionalInput
CustomerInput
PartnerInput
CommunicationDerived
OrderDerived
MatterDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.4 link_type

```text
PrimaryCustomer
RelatedCustomer
ApplicantCandidate
BrandOwnerCandidate
TrademarkOwnerCandidate
BillingCandidate
InstructionSource
HistoricalCustomer
ReferenceOnly
Unknown
```

## 11.5 intended_service_type

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

## 11.6 validation_status

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

## 11.7 intended_use

```text
MatterPreparation
OrderPreparation
BrandContext
TrademarkContext
DocumentContext
CommunicationContext
BillingPreparation
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
customer:create
customer:read
customer:search
customer:update
customer:validate
customer:link
customer:intake:prepare
customer:event:read
```

Rules:

```text
- Customer read/search must be permission-controlled.
- Customer creation must not imply legal ownership, applicant authority or billing authorization.
- Customer validation must not authorize instruction, billing or ownership claim.
- Customer-to-object linking requires separate permission.
- Customer intake preparation requires separate permission.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
CustomerCreationPolicy
CustomerUpdatePolicy
CustomerVisibilityPolicy
CustomerReferencePolicy
CustomerLinkPolicy
CustomerIntakePolicy
EventVisibilityPolicy
AIAgentCustomerAccessPolicy
RestrictedCustomerDataPolicy
CrossOrganizationCustomerPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Customer fields.
- Policy may require human review for AI-inferred Customer data.
- Policy may restrict cross-organization Customer lookup.
- Policy may restrict contact details, commercial terms, payment/billing data and privileged strategy.
- Policy may restrict customer-linked Brand/Trademark details.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Customer: Restricted / HumanReviewRequired where AI-inferred
Get Customer: Restricted
Search Customers: Restricted
Update Customer: Restricted / HumanReviewRequired where sensitive
Validate Customer Reference: Allowed under contract
Link Customer to Object: Restricted / HumanReviewRequired where AI-suggested
Prepare Customer Intake Context: Restricted / HumanReviewRequired
List Customer Events: Restricted
```

AI Agents may:

```text
summarize safe Customer metadata
flag duplicate or conflicting Customer records
validate Customer references for authorized actions
suggest Customer-to-object links for human review
prepare intake context draft for human review
identify missing customer intake items
```

AI Agents must not:

```text
fabricate Customer
fabricate CustomerCreated events
treat AI-inferred Customer as confirmed customer
treat Customer as legal owner or applicant
approve customer instructions
authorize billing or payment
create Matter or Order silently
bypass Permission or Policy
expose restricted contact/commercial data
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

Customer API may expose:

```text
CustomerCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Customer events directly.
- CustomerCreated must not be treated as Organization creation, User creation, Order creation, Matter creation, ownership proof or billing authorization.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] customer_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] related_organization_reference_id is valid where provided.
[ ] primary_user_reference_id is valid where provided.
[ ] target_object_type and target_object_reference_id are valid for link operation.
[ ] customer_type is controlled.
[ ] customer_status is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] intended_service_type is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted contact/commercial/billing/strategy fields are omitted or allowed.
[ ] AI-inferred customer data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] CustomerCreated is emitted after createCustomer succeeds.
[ ] Intake preparation does not create Matter or Order automatically.
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
CustomerReferenceInvalid
OrganizationReferenceInvalid
UserReferenceInvalid
TargetObjectReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedCustomerData
BillingDataRestricted
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
- Errors must not expose restricted Customer data.
- Errors must not expose contact details, payment/billing data or privileged strategy.
- Errors must not expose unrelated Organization/User data.
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
- customer_type, customer_status, source_type and link_type changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI customer-intake behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Customer API spec
cite Customer Service Specification
cite Customer Object Specification
cite CustomerCreated Event Specification
cite Organization/User/Brand/Trademark/Matter/Order specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid customer_reference_id
write tests for invalid organization/user/target references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Customer creation does not create Organization or User silently
write tests that Customer creation does not create Order or Matter
write tests that Customer validation does not prove ownership, instruction or billing authority
write tests for AI Agent Contract and human review requirement
write tests for CustomerCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Customer Service
allow UI to emit CustomerCreated directly
treat Customer as Organization or User
treat Customer as legal owner or applicant
treat Customer as billing authorization
treat AI-inferred Customer as confirmed business fact
create Matter or Order silently from Customer operations
expose restricted contact/commercial/billing data for convenience
allow AI to fabricate Customer references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Customer API purpose.
[ ] It defines Customer API meaning.
[ ] It defines Customer API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, link, intake preparation and event-list operations.
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
| 0.1.0 | Draft | Initial Customer API specification. Defines governed Customer relationship interface and separates Customer API from Organization, User, Order, Matter, ownership proof, applicant authority, billing authorization and AI-inferred customer truth. |

---

**End of API Specification**
