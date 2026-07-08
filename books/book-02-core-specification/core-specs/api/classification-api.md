# API Specification — Classification API

**Spec ID:** B02-API-CLASSIFICATION  
**Spec Type:** API Specification  
**API Name:** Classification API  
**API File:** core-specs/api/classification-api.md  
**Related Domain:** core-specs/domains/classification.md  
**Related Object Specs:** core-specs/objects/classification.md; core-specs/objects/trademark.md; core-specs/objects/jurisdiction.md; core-specs/objects/knowledge.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/classification-service.md; core-specs/services/trademark-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/knowledge-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/classification-created.md; core-specs/events/trademark-created.md; core-specs/events/jurisdiction-linked.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/classification-api-contract.md; core-specs/contracts/events/classification-created-payload.md  
**Related Agent Specs:** core-specs/agents/classification-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Classification API exposes governed Classification operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and suggest Classification references without treating Classification as Trademark filing, official goods/services acceptance, legal registrability conclusion, jurisdiction rule approval, evidence of use, document package, fee quote or AI professional decision.

Classification API exists to support:

```text
goods/services classification preparation
Nice class and local class context
trademark-to-classification preparation
jurisdiction-specific classification context
classification knowledge retrieval
matter/order preparation
AI-assisted classification suggestion under governance
policy-controlled classification visibility
event trace access
API-safe classification reference validation
```

Classification API does not file applications, guarantee office acceptance, prove use, decide registrability, calculate official fees or replace professional review.

---

# 2. API Meaning

Classification API means:

```text
a governed interface for operating Classification references through Classification Service.
```

Classification API does not mean:

```text
Trademark filing API
official goods/services approval API
Jurisdiction API
Knowledge API
Evidence API
Document API
Fee API
registrability opinion API
AI classification approval API
```

Classification organizes goods/services and class references.

It is not final legal acceptance or filing instruction by itself.

---

# 3. API Boundary

Classification API is responsible for:

```text
Classification create request intake
Classification read/search/list access
Classification update request intake
Classification reference validation
Classification suggestion request intake where explicitly governed
Trademark/Jurisdiction context validation where applicable
safe Classification response shaping
Permission/Policy enforcement for Classification operations
Classification-related Event reference exposure where allowed
AI Agent access boundary for Classification operations
controlled API errors
```

Classification API is not responsible for:

```text
Trademark filing execution
Order lifecycle ownership
Matter lifecycle ownership
official office acceptance
jurisdiction rule ownership
fee calculation
evidence sufficiency
document lifecycle ownership
professional legal conclusion by itself
AI final classification decision
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/classification.md
```

Domain rule:

```text
Classification provides governed goods/services and class context.
Classification is not filing execution, official acceptance, Evidence, fee calculation or legal conclusion by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/classification.md
core-specs/objects/trademark.md
core-specs/objects/jurisdiction.md
core-specs/objects/knowledge.md
core-specs/objects/document.md
core-specs/objects/evidence.md
core-specs/objects/matter.md
core-specs/objects/order.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Classification API returns classification_reference_id.
- Classification API may reference Trademark, Jurisdiction, Knowledge, Matter or Order context but must not create them silently.
- Classification API must not treat Classification as office-approved goods/services.
- Classification API must not treat classification suggestion as professional approval.
- Classification API must not expose restricted customer filing strategy or local rule notes by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/classification-service.md
core-specs/services/trademark-service.md
core-specs/services/jurisdiction-service.md
core-specs/services/knowledge-service.md
core-specs/services/document-service.md
core-specs/services/evidence-service.md
core-specs/services/matter-service.md
core-specs/services/order-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Classification API must invoke Classification Service for Classification behavior.
- Classification API must validate related references through their owning services where required.
- Classification API must invoke Permission Service where operation requires authorization.
- Classification API must invoke Policy Service where contextual constraints apply.
- Classification API must not emit Classification events directly; Classification Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/classification-created.md
core-specs/events/trademark-created.md
core-specs/events/jurisdiction-linked.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createClassification may result in ClassificationCreated.
- protected operations may produce PermissionEvaluated and PolicyEvaluated.
- API consumers must not fabricate ClassificationCreated.
- ClassificationCreated is classification reference trace, not filing, office acceptance or professional approval.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Classification

**Operation Category:** Create  
**Method:** POST  
**Path:** `/classifications`  
**Owning Service Operation:** `createClassification`  
**Permission Required:** `classification:create`  
**Policy Required:** `ClassificationCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated  
**Event Behavior:** Service Must Emit ClassificationCreated

Meaning:

```text
Create a governed Classification reference.
```

Non-meaning:

```text
does not file application
does not create Trademark
does not create Matter or Order
does not prove office acceptance
does not approve registrability
does not prove use
does not calculate final fees
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
Classification Service createClassification
  ↓
Event Service record ClassificationCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Classification

**Operation Category:** Read  
**Method:** GET  
**Path:** `/classifications/{classification_reference_id}`  
**Owning Service Operation:** `getClassification`  
**Permission Required:** `classification:read`  
**Policy Required:** `ClassificationVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Classification reference view.
```

Non-meaning:

```text
does not expose restricted filing strategy automatically
does not expose full local rule notes automatically
does not assert office acceptance automatically
```

## 8.3 Operation: Search Classifications

**Operation Category:** Search  
**Method:** GET  
**Path:** `/classifications`  
**Owning Service Operation:** `searchClassifications`  
**Permission Required:** `classification:search`  
**Policy Required:** `ClassificationVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Classification references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted classification corpus access
does not expose restricted customer/strategy/local rule data by default
```

## 8.4 Operation: Update Classification

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/classifications/{classification_reference_id}`  
**Owning Service Operation:** `updateClassification`  
**Permission Required:** `classification:update`  
**Policy Required:** `ClassificationUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit ClassificationUpdated where event is defined

Meaning:

```text
Update governed Classification metadata, wording, class or status under Classification Service rules.
```

Non-meaning:

```text
does not update Trademark, Matter or Order state automatically
does not approve office acceptance
does not update evidence or document records automatically
does not approve professional conclusions
```

## 8.5 Operation: Validate Classification Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/classifications/reference/validate`  
**Owning Service Operation:** `validateClassificationReference`  
**Permission Required:** `classification:validate`  
**Policy Required:** `ClassificationReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Classification reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not verify office acceptance
does not approve filing
does not prove registrability
does not prove use
```

## 8.6 Operation: Suggest Classification

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/classifications/suggest`  
**Owning Service Operation:** `suggestClassification`  
**Permission Required:** `classification:suggest`  
**Policy Required:** `ClassificationSuggestionPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit ClassificationCreated unless createClassification succeeds separately

Meaning:

```text
Generate governed classification suggestions for review using provided trademark, jurisdiction, goods/services and knowledge context.
```

Non-meaning:

```text
does not create Classification automatically
does not approve suggested wording
does not guarantee local acceptance
does not replace professional review
```

## 8.7 Operation: Link Classification to Trademark

**Operation Category:** Link  
**Method:** POST  
**Path:** `/classifications/{classification_reference_id}/trademarks/{trademark_reference_id}`  
**Owning Service Operation:** `linkClassificationToTrademark`  
**Permission Required:** `classification:trademark:link`  
**Policy Required:** `ClassificationTrademarkLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit ClassificationCreated or future LinkEvent where defined

Meaning:

```text
Create a governed relationship reference between Classification and Trademark.
```

Non-meaning:

```text
does not file application
does not approve goods/services
does not create Order or Matter
does not guarantee classification acceptance
```

## 8.8 Operation: Retrieve Classification Knowledge

**Operation Category:** Action  
**Method:** POST  
**Path:** `/classifications/knowledge/retrieve`  
**Owning Service Operation:** `retrieveClassificationKnowledge`  
**Permission Required:** `classification:knowledge:retrieve`  
**Policy Required:** `ClassificationKnowledgeAccessPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service May Emit PolicyEvaluated

Meaning:

```text
Retrieve policy-filtered Knowledge Records relevant to classification context.
```

Non-meaning:

```text
does not guarantee current official truth
does not provide legal opinion
does not bypass Knowledge policy
does not remove human review where required
```

## 8.9 Operation: List Classification Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/classifications/{classification_reference_id}/events`  
**Owning Service Operation:** `listClassificationEvents`  
**Permission Required:** `classification:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Classification-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Classification Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  classification_type: string
  classification_status: string | optional
  class_system: string
  class_number: string | null
  goods_services_text: string
  normalized_text: string | null
  trademark_reference_id: string | null
  jurisdiction_reference_id: string | null
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_generated: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Classification Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  classification_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  classification_status: string | optional
  class_number: string | optional
  goods_services_text: string | optional
  normalized_text: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Classification Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  classification_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Suggest Classification Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  trademark_reference_id: string | null
  jurisdiction_reference_id: string | null
  goods_services_description: string
  preferred_class_system: string | null
  suggestion_purpose: string
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.5 Link Classification to Trademark Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  classification_reference_id: string
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
- Requests must not include confidential filing strategy, pricing assumptions, raw document content or evidence content by default.
- Requests must use controlled classification_type, classification_status, class_system, source_type and link_type values.
- AI-generated classification suggestions must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Classification Response

```yaml
status: 200
body:
  classification_reference_id: string
  classification_type: string
  classification_status: string
  class_system: string
  class_number: string | null
  goods_services_text: string
  normalized_text: string | null
  trademark_reference_id: string | null
  jurisdiction_reference_id: string | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Classification Response

```yaml
status: 201
body:
  classification_reference_id: string
  classification_status: string
  review_required: boolean
  related_event_reference_ids:
    - classification_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Suggest Classification Response

```yaml
status: 200
body:
  suggestion_reference_id: string | null
  suggestions:
    - class_system: string
      class_number: string | null
      goods_services_text: string
      confidence_level: string
      review_required: boolean
      safe_reason: string | null
  policy_decision_reference_id: string | null
  human_review_required: boolean
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.4 Classification Reference Validation Response

```yaml
status: 200
body:
  classification_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply filing, office acceptance, use proof, fee calculation or registrability.
- Responses must not expose restricted strategy/local rule/document/evidence fields by default.
- Responses must distinguish Classification references from Trademark, Matter and Order references.
- Responses must identify review requirements for AI-created or AI-suggested content.
```

---

# 11. Controlled Values

## 11.1 classification_type

```text
Goods
Services
GoodsAndServices
Heading
CustomWording
LocalStandardItem
NiceItem
Translation
Other
Unknown
```

## 11.2 classification_status

```text
Draft
Active
ReviewRequired
Suggested
AcceptedInternal
RejectedInternal
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 class_system

```text
Nice
Local
USAcceptableID
ChinaStandard
EUIPOHarmonized
Madrid
Custom
Unknown
```

## 11.4 source_type

```text
ProfessionalInput
CustomerInput
TrademarkDerived
JurisdictionDerived
KnowledgeDerived
DocumentDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.5 link_type

```text
PrimaryClassification
AlternativeClassification
LocalAdaptation
Translation
HistoricalClassification
DraftClassification
Unknown
```

## 11.6 suggestion_purpose

```text
InitialFiling
GoodsServicesExpansion
LocalAdaptation
Translation
OfficeActionResponse
RenewalReview
PortfolioReview
AIAssistedWorkflow
Unknown
```

## 11.7 confidence_level

```text
Low
Medium
High
Unknown
```

## 11.8 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Deprecated
ContextMismatch
Unknown
```

## 11.9 intended_use

```text
TrademarkPreparation
MatterPreparation
OrderPreparation
JurisdictionPreparation
FilingDraft
OfficeActionResponse
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
classification:create
classification:read
classification:search
classification:update
classification:validate
classification:suggest
classification:trademark:link
classification:knowledge:retrieve
classification:event:read
```

Rules:

```text
- Classification read/search must be permission-controlled.
- Classification creation must not imply office acceptance.
- Classification validation must not authorize filing or registrability claim.
- Classification suggestion requires separate permission.
- Classification-to-Trademark linking requires separate permission.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
ClassificationCreationPolicy
ClassificationUpdatePolicy
ClassificationVisibilityPolicy
ClassificationReferencePolicy
ClassificationSuggestionPolicy
ClassificationTrademarkLinkPolicy
ClassificationKnowledgeAccessPolicy
EventVisibilityPolicy
AIAgentClassificationAccessPolicy
RestrictedClassificationStrategyPolicy
CrossOrganizationClassificationPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Classification fields.
- Policy may require human review for AI-generated or AI-suggested Classification content.
- Policy may restrict cross-organization Classification lookup.
- Policy may restrict local rule, customer strategy and filing strategy fields.
- Policy may restrict full Knowledge content and return safe summaries only.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Classification: Restricted / HumanReviewRequired where AI-generated
Get Classification: Restricted
Search Classifications: Restricted
Update Classification: Restricted / HumanReviewRequired where sensitive
Validate Classification Reference: Allowed under contract
Suggest Classification: Restricted / HumanReviewRequired
Link Classification to Trademark: Restricted / HumanReviewRequired where AI-suggested
Retrieve Classification Knowledge: Restricted
List Classification Events: Restricted
```

AI Agents may:

```text
suggest goods/services wording
summarize safe Classification metadata
flag possible class conflicts or missing jurisdiction context
validate Classification references for authorized actions
suggest local adaptation for human review
retrieve authorized Classification Knowledge
```

AI Agents must not:

```text
fabricate Classification
fabricate ClassificationCreated events
treat AI suggestion as approved Classification
treat Classification as office acceptance
approve registrability
prove use or filing eligibility
calculate final fees unless governed by separate fee logic
bypass Permission or Policy
expose restricted classification strategy
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

Classification API may expose:

```text
ClassificationCreated
TrademarkCreated
JurisdictionLinked
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Classification events directly.
- ClassificationCreated must not be treated as filing, office acceptance, fee approval or professional conclusion.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] classification_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] trademark_reference_id is valid where provided.
[ ] jurisdiction_reference_id is valid where provided.
[ ] classification_type is controlled.
[ ] classification_status is controlled.
[ ] class_system is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] suggestion_purpose is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted classification/strategy/local rule/document/evidence fields are omitted or allowed.
[ ] AI-generated or AI-suggested content is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] ClassificationCreated is emitted after createClassification succeeds.
[ ] Suggestion operation does not create Classification unless createClassification is called separately.
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
ClassificationReferenceInvalid
TrademarkReferenceInvalid
JurisdictionReferenceInvalid
KnowledgeReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedClassificationStrategy
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
- Errors must not expose restricted classification strategy.
- Errors must not expose local rule internals, pricing assumptions or customer confidential data.
- Errors must not expose restricted Knowledge, Document or Evidence content.
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
- classification_type, classification_status, class_system and suggestion_purpose changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI classification operation behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Classification API spec
cite Classification Service Specification
cite Classification Object Specification
cite ClassificationCreated Event Specification
cite Trademark/Jurisdiction/Knowledge specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe summaries by default
write tests for invalid classification_reference_id
write tests for invalid trademark/jurisdiction references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Classification creation does not file application
write tests that Classification suggestion does not create Classification automatically
write tests that Classification validation does not prove office acceptance or registrability
write tests for AI Agent Contract and human review requirement
write tests for ClassificationCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Classification Service
allow UI to emit ClassificationCreated directly
treat Classification as filing execution
treat Classification as office acceptance
treat Classification as final fee calculation
treat AI classification suggestion as approved professional conclusion
create Trademark, Matter or Order silently from Classification operations
expose restricted classification/customer strategy for convenience
allow AI to fabricate Classification references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Classification API purpose.
[ ] It defines Classification API meaning.
[ ] It defines Classification API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, suggest, link, knowledge retrieval and event-list operations.
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
| 0.1.0 | Draft | Initial Classification API specification. Defines governed Classification interface and separates Classification API from filing, office acceptance, registrability, Evidence, Document, fee calculation and AI professional decision. |

---

**End of API Specification**
