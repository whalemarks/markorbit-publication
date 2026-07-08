# API Specification — Brand API

**Spec ID:** B02-API-BRAND  
**Spec Type:** API Specification  
**API Name:** Brand API  
**API File:** core-specs/api/brand-api.md  
**Related Domain:** core-specs/domains/brand.md  
**Related Object Specs:** core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/customer.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/knowledge.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/customer-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/knowledge-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/brand-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/brand-api-contract.md; core-specs/contracts/events/brand-created-payload.md  
**Related Agent Specs:** core-specs/agents/brand-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Brand API exposes governed Brand reference operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and link Brand references without treating Brand as Trademark, Customer, commercial owner, filing instruction, legal right, evidence of use, registrability conclusion, product SKU, marketing campaign or AI-generated brand decision.

Brand API exists to support:

```text
brand asset reference creation
brand portfolio context
brand-to-trademark preparation
brand ownership/context review
brand name and mark element organization
document/evidence linkage preparation
AI-assisted brand analysis under governance
policy-controlled brand visibility
event trace access
API-safe brand reference validation
```

Brand API does not determine trademark registrability, create trademark applications, prove ownership, prove use or replace professional review.

---

# 2. API Meaning

Brand API means:

```text
a governed interface for operating Brand references through Brand Service.
```

Brand API does not mean:

```text
Trademark API
Customer API
Ownership API
Evidence API
Document API
filing instruction API
legal right API
registrability opinion API
marketing CMS API
AI brand approval API
```

Brand is a commercial/brand asset reference.

Trademark is the legal/professional protection object.

The API must preserve this distinction.

---

# 3. API Boundary

Brand API is responsible for:

```text
Brand create request intake
Brand read/search/list access
Brand update request intake
Brand reference validation
Brand-to-related-object link request intake where explicitly defined
safe Brand response shaping
Permission/Policy enforcement for Brand operations
Brand-related Event reference exposure where allowed
AI Agent access boundary for Brand operations
controlled API errors
```

Brand API is not responsible for:

```text
Trademark lifecycle ownership
Customer ownership determination
Document lifecycle ownership
Evidence sufficiency
registrability/legal conclusion
filing decision
goods/services classification
market/marketing campaign execution
AI creative approval by itself
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/brand.md
```

Domain rule:

```text
Brand organizes commercial identity and brand asset references.
Brand is not Trademark, Customer, Evidence, legal right or professional conclusion.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/brand.md
core-specs/objects/trademark.md
core-specs/objects/customer.md
core-specs/objects/document.md
core-specs/objects/evidence.md
core-specs/objects/knowledge.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Brand API returns brand_reference_id.
- Brand API may reference Trademark, Customer, Document or Evidence context but must not create them silently.
- Brand API must not treat Brand as ownership proof.
- Brand API must not treat Brand as legal right or trademark application.
- Brand API must not expose restricted brand strategy or customer data by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/brand-service.md
core-specs/services/trademark-service.md
core-specs/services/customer-service.md
core-specs/services/document-service.md
core-specs/services/evidence-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Brand API must invoke Brand Service for Brand behavior.
- Brand API must validate related references through their owning services where required.
- Brand API must invoke Permission Service where operation requires authorization.
- Brand API must invoke Policy Service where contextual constraints apply.
- Brand API must not emit Brand events directly; Brand Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/brand-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createBrand may result in BrandCreated.
- protected operations may produce PermissionEvaluated and PolicyEvaluated.
- API consumers must not fabricate BrandCreated.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Brand

**Operation Category:** Create  
**Method:** POST  
**Path:** `/brands`  
**Owning Service Operation:** `createBrand`  
**Permission Required:** `brand:create`  
**Policy Required:** `BrandCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated  
**Event Behavior:** Service Must Emit BrandCreated

Meaning:

```text
Create a governed Brand reference.
```

Non-meaning:

```text
does not create Trademark
does not create Customer
does not prove ownership
does not prove use
does not establish legal right
does not approve registrability
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
Brand Service createBrand
  ↓
Event Service record BrandCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Brand

**Operation Category:** Read  
**Method:** GET  
**Path:** `/brands/{brand_reference_id}`  
**Owning Service Operation:** `getBrand`  
**Permission Required:** `brand:read`  
**Policy Required:** `BrandVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Brand reference view.
```

Non-meaning:

```text
does not expose restricted brand strategy automatically
does not expose customer ownership details automatically
does not expose evidence or document content automatically
```

## 8.3 Operation: Search Brands

**Operation Category:** Search  
**Method:** GET  
**Path:** `/brands`  
**Owning Service Operation:** `searchBrands`  
**Permission Required:** `brand:search`  
**Policy Required:** `BrandVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Brand references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted brand portfolio access
does not expose restricted customer/strategy data by default
```

## 8.4 Operation: Update Brand

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/brands/{brand_reference_id}`  
**Owning Service Operation:** `updateBrand`  
**Permission Required:** `brand:update`  
**Policy Required:** `BrandUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit BrandUpdated where event is defined

Meaning:

```text
Update governed Brand metadata or status under Brand Service rules.
```

Non-meaning:

```text
does not update Trademark automatically
does not update Customer ownership automatically
does not update Document or Evidence records automatically
does not approve professional conclusions
```

## 8.5 Operation: Validate Brand Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/brands/reference/validate`  
**Owning Service Operation:** `validateBrandReference`  
**Permission Required:** `brand:validate`  
**Policy Required:** `BrandReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Brand reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not validate trademark registrability
does not prove ownership or use
does not authorize filing or commercial action
```

## 8.6 Operation: Link Brand to Trademark

**Operation Category:** Link  
**Method:** POST  
**Path:** `/brands/{brand_reference_id}/trademarks/{trademark_reference_id}`  
**Owning Service Operation:** `linkBrandToTrademark`  
**Permission Required:** `brand:trademark:link`  
**Policy Required:** `BrandTrademarkLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where suggested by AI  
**Event Behavior:** Service May Emit BrandUpdated or a future LinkEvent where defined

Meaning:

```text
Create a governed relationship reference between Brand and Trademark.
```

Non-meaning:

```text
does not create Trademark
does not file Trademark
does not approve protection strategy
does not prove ownership
```

## 8.7 Operation: List Brand Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/brands/{brand_reference_id}/events`  
**Owning Service Operation:** `listBrandEvents`  
**Permission Required:** `brand:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Brand-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Brand Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  brand_type: string
  brand_status: string | optional
  brand_name: string
  brand_language: string | null
  brand_script: string | null
  customer_reference_id: string | null
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_generated: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Brand Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  brand_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  brand_status: string | optional
  brand_name: string | optional
  brand_language: string | optional
  brand_script: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Brand Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  brand_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Brand to Trademark Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  brand_reference_id: string
  trademark_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  link_type: string
  link_reason: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include confidential strategy, ownership proof, raw document content or evidence content by default.
- Requests must use controlled brand_type, brand_status, source_type and link_type values.
- AI-generated brand suggestions must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Brand Response

```yaml
status: 200
body:
  brand_reference_id: string
  brand_type: string
  brand_status: string
  brand_name: string
  brand_language: string | null
  brand_script: string | null
  customer_reference_id: string | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
  related_trademark_reference_ids: list[string]
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Brand Response

```yaml
status: 201
body:
  brand_reference_id: string
  brand_status: string
  review_required: boolean
  related_event_reference_ids:
    - brand_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Brand Reference Validation Response

```yaml
status: 200
body:
  brand_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply trademark filing, ownership proof or registrability.
- Responses must not expose restricted customer/strategy fields by default.
- Responses must distinguish Brand references from Trademark references.
- Responses must identify review requirements for AI-created or AI-suggested content.
```

---

# 11. Controlled Values

## 11.1 brand_type

```text
WordBrand
LogoBrand
CompositeBrand
ProductBrand
ServiceBrand
SeriesBrand
CompanyBrand
PersonalBrand
Unknown
```

## 11.2 brand_status

```text
Draft
Active
ReviewRequired
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 source_type

```text
ProfessionalInput
CustomerInput
DocumentDerived
EvidenceDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.4 link_type

```text
PrimaryTrademark
RelatedTrademark
VariantTrademark
DefensiveTrademark
HistoricalTrademark
DraftTrademark
Unknown
```

## 11.5 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
ContextMismatch
Unknown
```

## 11.6 intended_use

```text
PortfolioReference
TrademarkPreparation
MatterPreparation
OrderPreparation
DocumentLink
EvidenceLink
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
brand:create
brand:read
brand:search
brand:update
brand:validate
brand:trademark:link
brand:event:read
```

Rules:

```text
- Brand read/search must be permission-controlled.
- Brand creation must not imply Trademark creation.
- Brand validation must not authorize filing or ownership claim.
- Brand-to-Trademark linking requires separate permission.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
BrandCreationPolicy
BrandUpdatePolicy
BrandVisibilityPolicy
BrandReferencePolicy
BrandTrademarkLinkPolicy
EventVisibilityPolicy
AIAgentBrandAccessPolicy
RestrictedBrandStrategyPolicy
CrossOrganizationBrandPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Brand fields.
- Policy may require human review for AI-generated Brand content.
- Policy may restrict cross-organization Brand lookup.
- Policy may restrict customer-linked Brand details.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Brand: Restricted / HumanReviewRequired where AI-generated
Get Brand: Restricted
Search Brands: Restricted
Update Brand: Restricted / HumanReviewRequired where sensitive
Validate Brand Reference: Allowed under contract
Link Brand to Trademark: Restricted / HumanReviewRequired where AI-suggested
List Brand Events: Restricted
```

AI Agents may:

```text
suggest brand normalization
summarize safe Brand metadata
flag possible duplicate or variant Brand references
validate Brand references for authorized actions
suggest Brand-to-Trademark links for human review
```

AI Agents must not:

```text
fabricate Brand
fabricate BrandCreated events
treat AI-generated Brand as approved brand asset
treat Brand as Trademark or legal right
approve registrability
prove ownership or use
bypass Permission or Policy
expose restricted brand strategy or customer data
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

Brand API may expose:

```text
BrandCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Brand events directly.
- BrandCreated must not be treated as TrademarkCreated or ownership proof.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] brand_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] customer_reference_id is valid where provided.
[ ] trademark_reference_id is valid for link operation.
[ ] brand_type is controlled.
[ ] brand_status is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted brand/customer/strategy fields are omitted or allowed.
[ ] AI-generated content is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] BrandCreated is emitted after createBrand succeeds.
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
BrandReferenceInvalid
CustomerReferenceInvalid
TrademarkReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedBrandStrategy
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
- Errors must not expose restricted brand strategy.
- Errors must not expose customer confidential data.
- Errors must not expose document/evidence content.
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
- brand_type, brand_status and link_type changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI brand operation behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Brand API spec
cite Brand Service Specification
cite Brand Object Specification
cite BrandCreated Event Specification
cite Trademark/Customer specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe summaries by default
write tests for invalid brand_reference_id
write tests for invalid trademark/customer references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Brand creation does not create Trademark
write tests that Brand validation does not prove ownership or registrability
write tests for AI Agent Contract requirement
write tests for BrandCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Brand Service
allow UI to emit BrandCreated directly
treat Brand as Trademark
treat Brand as Customer
treat Brand as ownership proof
treat Brand as evidence of use
treat AI-generated Brand as approved professional conclusion
expose restricted brand/customer strategy for convenience
allow AI to fabricate Brand references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Brand API purpose.
[ ] It defines Brand API meaning.
[ ] It defines Brand API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, link and event-list operations.
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
| 0.1.0 | Draft | Initial Brand API specification. Defines governed Brand reference interface and separates Brand API from Trademark, Customer, ownership proof, Evidence, filing instruction, registrability conclusion and AI brand approval. |

---

**End of API Specification**
