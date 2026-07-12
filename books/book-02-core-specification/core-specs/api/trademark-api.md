# API Specification — Trademark API

**Spec ID:** B02-API-TRADEMARK  
**Spec Type:** API Specification  
**API Name:** Trademark API  
**API File:** core-specs/api/trademark-api.md  
**Related Domain:** core-specs/domains/trademark.md  
**Related Object Specs:** core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/classification-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/trademark-created.md; core-specs/events/jurisdiction-linked.md; core-specs/events/classification-created.md; core-specs/events/document-created.md; core-specs/events/evidence-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/trademark-api-contract.md; core-specs/contracts/events/trademark-created-payload.md  
**Related Agent Specs:** core-specs/agents/trademark-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Trademark API exposes governed Trademark professional-object operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and link Trademark references without treating Trademark as Brand, filing order, Matter, official registry record, legal right, registrability approval, use evidence, document package, customer ownership proof or AI legal conclusion.

Trademark API exists to support:

```text
trademark professional object creation
brand-to-trademark protection context
jurisdiction and classification preparation
document and evidence linkage preparation
matter/order preparation
trademark lifecycle reference
AI-assisted trademark analysis under governance
policy-controlled trademark visibility
event trace access
API-safe trademark reference validation
```

Trademark API does not file applications, determine registrability, prove ownership, prove use, replace official registry status or replace professional review.

---

# 2. API Meaning

Trademark API means:

```text
a governed interface for operating Trademark professional-object references through Trademark Service.
```

Trademark API does not mean:

```text
Brand API
Order API
Matter API
official registry API
legal right API
registrability opinion API
Evidence API
Document API
filing API
AI legal conclusion API
```

Trademark is the legal/professional protection object.

Brand is the commercial identity reference.

Order and Matter own execution context.

The API must preserve these boundaries.

---

# 3. API Boundary

Trademark API is responsible for:

```text
Trademark create request intake
Trademark read/search/list access
Trademark update request intake
Trademark reference validation
Trademark-to-Brand link request intake where explicitly defined
Trademark-to-Jurisdiction and Classification preparation where explicitly defined
safe Trademark response shaping
Permission/Policy enforcement for Trademark operations
Trademark-related Event reference exposure where allowed
AI Agent access boundary for Trademark operations
controlled API errors
```

Trademark API is not responsible for:

```text
application filing execution
Order lifecycle ownership
Matter lifecycle ownership
official registry synchronization truth
evidence sufficiency
document lifecycle ownership
customer ownership determination
fee/pricing/payment ownership
professional legal conclusion by itself
AI final legal decision
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/trademark.md
```

Domain rule:

```text
Trademark represents the legal/professional protection object.
Trademark is not Brand, Order, Matter, official registry truth, Evidence or legal conclusion by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/trademark.md
core-specs/objects/brand.md
core-specs/objects/jurisdiction.md
core-specs/objects/classification.md
core-specs/objects/document.md
core-specs/objects/evidence.md
core-specs/objects/customer.md
core-specs/objects/matter.md
core-specs/objects/order.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Trademark API returns trademark_reference_id.
- Trademark API may reference Brand, Customer, Jurisdiction, Classification, Document or Evidence context but must not create them silently unless explicitly defined by governed operation.
- Trademark API must not treat Trademark as official registry status by default.
- Trademark API must not treat Trademark as ownership proof or use proof.
- Trademark API must not expose restricted filing strategy, customer data, document content or evidence content by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/trademark-service.md
core-specs/services/brand-service.md
core-specs/services/jurisdiction-service.md
core-specs/services/classification-service.md
core-specs/services/document-service.md
core-specs/services/evidence-service.md
core-specs/services/customer-service.md
core-specs/services/matter-service.md
core-specs/services/order-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Trademark API must invoke Trademark Service for Trademark behavior.
- Trademark API must validate related references through their owning services where required.
- Trademark API must invoke Permission Service where operation requires authorization.
- Trademark API must invoke Policy Service where contextual constraints apply.
- Trademark API must not emit Trademark events directly; Trademark Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/trademark-created.md
core-specs/events/jurisdiction-linked.md
core-specs/events/classification-created.md
core-specs/events/document-created.md
core-specs/events/evidence-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createTrademark may result in TrademarkCreated.
- linkTrademarkJurisdiction may result in JurisdictionLinked where governed by related service.
- classification preparation must use Classification Service and related events.
- document/evidence linkage must use Document/Evidence services and related events.
- API consumers must not fabricate TrademarkCreated.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Trademark

**Operation Category:** Create  
**Method:** POST  
**Path:** `/trademarks`  
**Owning Service Operation:** `createTrademark`  
**Permission Required:** `trademark:create`  
**Policy Required:** `TrademarkCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated  
**Event Behavior:** Service Must Emit TrademarkCreated

Meaning:

```text
Create a governed Trademark professional-object reference.
```

Non-meaning:

```text
does not file an application
does not create Order
does not create Matter
does not prove ownership
does not prove use
does not approve registrability
does not create official registry record
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
Trademark Service createTrademark
  ↓
Event Service record TrademarkCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Trademark

**Operation Category:** Read  
**Method:** GET  
**Path:** `/trademarks/{trademark_reference_id}`  
**Owning Service Operation:** `getTrademark`  
**Permission Required:** `trademark:read`  
**Policy Required:** `TrademarkVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Trademark professional-object view.
```

Non-meaning:

```text
does not expose restricted filing strategy automatically
does not expose customer ownership details automatically
does not expose document/evidence content automatically
does not assert current official registry truth automatically
```

## 8.3 Operation: Search Trademarks

**Operation Category:** Search  
**Method:** GET  
**Path:** `/trademarks`  
**Owning Service Operation:** `searchTrademarks`  
**Permission Required:** `trademark:search`  
**Policy Required:** `TrademarkVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Trademark references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted portfolio access
does not expose restricted legal/customer/strategy data by default
```

## 8.4 Operation: Update Trademark

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/trademarks/{trademark_reference_id}`  
**Owning Service Operation:** `updateTrademark`  
**Permission Required:** `trademark:update`  
**Policy Required:** `TrademarkUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit TrademarkUpdated where event is defined

Meaning:

```text
Update governed Trademark metadata or status under Trademark Service rules.
```

Non-meaning:

```text
does not update Brand automatically
does not update official registry status automatically
does not update Matter/Order state automatically
does not update Document or Evidence records automatically
does not approve professional conclusions
```

## 8.5 Operation: Validate Trademark Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/trademarks/reference/validate`  
**Owning Service Operation:** `validateTrademarkReference`  
**Permission Required:** `trademark:validate`  
**Policy Required:** `TrademarkReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Trademark reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not validate registrability
does not prove ownership or use
does not authorize filing
does not verify official registry status
```

## 8.6 Operation: Link Trademark to Brand

**Operation Category:** Link  
**Method:** POST  
**Path:** `/trademarks/{trademark_reference_id}/brands/{brand_reference_id}`  
**Owning Service Operation:** `linkTrademarkToBrand`  
**Permission Required:** `trademark:brand:link`  
**Policy Required:** `TrademarkBrandLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where suggested by AI  
**Event Behavior:** Service May Emit TrademarkUpdated or a future LinkEvent where defined

Meaning:

```text
Create a governed relationship reference between Trademark and Brand.
```

Non-meaning:

```text
does not create Brand
does not prove ownership
does not approve trademark protection strategy
does not file trademark
```

## 8.7 Operation: Link Trademark to Jurisdiction

**Operation Category:** Link  
**Method:** POST  
**Path:** `/trademarks/{trademark_reference_id}/jurisdictions/{jurisdiction_reference_id}`  
**Owning Service Operation:** `linkTrademarkToJurisdiction`  
**Permission Required:** `trademark:jurisdiction:link`  
**Policy Required:** `TrademarkJurisdictionLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where suggested by AI  
**Event Behavior:** Service May Emit JurisdictionLinked through governed behavior

Meaning:

```text
Create or request a governed relationship between Trademark and Jurisdiction context.
```

Non-meaning:

```text
does not file in that jurisdiction
does not verify local availability
does not approve filing strategy
does not create official application
```

## 8.8 Operation: List Trademark Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/trademarks/{trademark_reference_id}/events`  
**Owning Service Operation:** `listTrademarkEvents`  
**Permission Required:** `trademark:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Trademark-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Trademark Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  trademark_type: string
  trademark_status: string | optional
  mark_text: string | null
  mark_image_document_reference_id: string | null
  brand_reference_id: string | null
  customer_reference_id: string | null
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_generated: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Trademark Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  trademark_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  trademark_status: string | optional
  mark_text: string | optional
  mark_image_document_reference_id: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Trademark Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  trademark_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Trademark to Brand Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  trademark_reference_id: string
  brand_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  link_type: string
  link_reason: string | null
  request_context: object
```

## 9.5 Link Trademark to Jurisdiction Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  trademark_reference_id: string
  jurisdiction_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  jurisdiction_link_type: string
  intended_service_type: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include confidential filing strategy, ownership proof, raw document content or evidence content by default.
- Requests must use controlled trademark_type, trademark_status, source_type and link_type values.
- AI-generated trademark suggestions must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Trademark Response

```yaml
status: 200
body:
  trademark_reference_id: string
  trademark_type: string
  trademark_status: string
  mark_text: string | null
  mark_image_document_reference_id: string | null
  brand_reference_id: string | null
  customer_reference_id: string | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
  related_jurisdiction_reference_ids: list[string]
  related_classification_reference_ids: list[string]
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Trademark Response

```yaml
status: 201
body:
  trademark_reference_id: string
  trademark_status: string
  review_required: boolean
  related_event_reference_ids:
    - trademark_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Trademark Reference Validation Response

```yaml
status: 200
body:
  trademark_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply filing, ownership proof, use proof, legal right or registrability.
- Responses must not expose restricted customer/strategy/document/evidence fields by default.
- Responses must distinguish Trademark references from Brand, Order and Matter references.
- Responses must identify review requirements for AI-created or AI-suggested content.
```

---

# 11. Controlled Values

## 11.1 trademark_type

```text
WordMark
DeviceMark
CompositeMark
ThreeDimensionalMark
ColorMark
SoundMark
MotionMark
CertificationMark
CollectiveMark
ServiceMark
Other
Unknown
```

## 11.2 trademark_status

```text
Draft
Active
ReviewRequired
PendingJurisdictionLink
PendingClassification
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 source_type

```text
ProfessionalInput
CustomerInput
BrandDerived
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
PrimaryBrand
RelatedBrand
VariantBrand
HistoricalBrand
DraftBrand
Unknown
```

## 11.5 jurisdiction_link_type

```text
TargetJurisdiction
ExistingRegistrationJurisdiction
PriorityJurisdiction
MadridDesignation
MonitoringJurisdiction
ReferenceJurisdiction
Unknown
```

## 11.6 intended_service_type

```text
Search
Filing
Renewal
OfficeAction
Opposition
Cancellation
Recordal
Monitoring
PortfolioManagement
Unknown
```

## 11.7 validation_status

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

## 11.8 intended_use

```text
PortfolioReference
BrandProtection
MatterPreparation
OrderPreparation
JurisdictionPreparation
ClassificationPreparation
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
trademark:create
trademark:read
trademark:search
trademark:update
trademark:validate
trademark:brand:link
trademark:jurisdiction:link
trademark:event:read
```

Rules:

```text
- Trademark read/search must be permission-controlled.
- Trademark creation must not imply filing or registrability approval.
- Trademark validation must not authorize filing or ownership claim.
- Trademark-to-Brand and Trademark-to-Jurisdiction linking require separate permissions.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
TrademarkCreationPolicy
TrademarkUpdatePolicy
TrademarkVisibilityPolicy
TrademarkReferencePolicy
TrademarkBrandLinkPolicy
TrademarkJurisdictionLinkPolicy
EventVisibilityPolicy
AIAgentTrademarkAccessPolicy
RestrictedTrademarkStrategyPolicy
CrossOrganizationTrademarkPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Trademark fields.
- Policy may require human review for AI-generated Trademark content.
- Policy may restrict cross-organization Trademark lookup.
- Policy may restrict customer-linked Trademark details.
- Policy may restrict jurisdiction strategy fields.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Trademark: Restricted / HumanReviewRequired where AI-generated
Get Trademark: Restricted
Search Trademarks: Restricted
Update Trademark: Restricted / HumanReviewRequired where sensitive
Validate Trademark Reference: Allowed under contract
Link Trademark to Brand: Restricted / HumanReviewRequired where AI-suggested
Link Trademark to Jurisdiction: Restricted / HumanReviewRequired where AI-suggested
List Trademark Events: Restricted
```

AI Agents may:

```text
suggest trademark normalization
summarize safe Trademark metadata
flag possible duplicate or variant Trademark references
validate Trademark references for authorized actions
suggest Brand/Jurisdiction links for human review
prepare preliminary analysis using authorized Knowledge
```

AI Agents must not:

```text
fabricate Trademark
fabricate TrademarkCreated events
treat AI-generated Trademark as approved professional object
treat Trademark as filed application or legal right
approve registrability
prove ownership or use
bypass Permission or Policy
expose restricted filing strategy or customer data
```

AI access requires:

```text
agent_identity_reference_id
agent_contract_reference_id where required
authorized_knowledge_reference_id where applicable
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 15. Event Access Rules

Trademark API may expose:

```text
TrademarkCreated
JurisdictionLinked
ClassificationCreated
DocumentCreated
EvidenceCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Trademark events directly.
- TrademarkCreated must not be treated as official filing, registration, ownership proof or use proof.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] trademark_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] brand_reference_id is valid where provided.
[ ] customer_reference_id is valid where provided.
[ ] jurisdiction_reference_id is valid for link operation.
[ ] mark_image_document_reference_id is valid where provided.
[ ] trademark_type is controlled.
[ ] trademark_status is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] jurisdiction_link_type is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted trademark/customer/strategy/document/evidence fields are omitted or allowed.
[ ] AI-generated content is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] TrademarkCreated is emitted after createTrademark succeeds.
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
TrademarkReferenceInvalid
BrandReferenceInvalid
CustomerReferenceInvalid
JurisdictionReferenceInvalid
DocumentReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedTrademarkStrategy
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
- Errors must not expose restricted filing strategy.
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
- trademark_type, trademark_status and jurisdiction_link_type changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI trademark operation behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Trademark API spec
cite Trademark Service Specification
cite Trademark Object Specification
cite TrademarkCreated Event Specification
cite Brand/Jurisdiction/Classification/Document/Evidence specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe summaries by default
write tests for invalid trademark_reference_id
write tests for invalid brand/customer/jurisdiction/document references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Trademark creation does not create Order or Matter
write tests that Trademark creation does not file application
write tests that Trademark validation does not prove ownership, use or registrability
write tests for AI Agent Contract requirement
write tests for TrademarkCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Trademark Service
allow UI to emit TrademarkCreated directly
treat Trademark as Brand
treat Trademark as Order or Matter
treat Trademark as official registry truth
treat Trademark as ownership proof or use proof
treat AI-generated Trademark as approved legal/professional conclusion
expose restricted filing/customer strategy for convenience
allow AI to fabricate Trademark references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Trademark API purpose.
[ ] It defines Trademark API meaning.
[ ] It defines Trademark API boundary.
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
| 0.1.0 | Draft | Initial Trademark API specification. Defines governed Trademark professional-object interface and separates Trademark API from Brand, Order, Matter, official registry truth, filing, ownership proof, Evidence, registrability conclusion and AI legal decision. |

---

**End of API Specification**


## PUB-TASK-B02-002 State and Workflow Reference

API requests cannot define canonical status or workflow states. API calls route to the owning Service, invalid transitions cannot be bypassed through PATCH, and workflow transition validation returns decision, reason and review/permission/policy requirements without directly performing domain mutation. This task adds no endpoint and changes no endpoint path.
