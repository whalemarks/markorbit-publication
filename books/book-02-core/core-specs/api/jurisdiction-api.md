# API Specification — Jurisdiction API

**Spec ID:** B02-API-JURISDICTION  
**Spec Type:** API Specification  
**API Name:** Jurisdiction API  
**API File:** core-specs/api/jurisdiction-api.md  
**Related Domain:** core-specs/domains/jurisdiction.md  
**Related Object Specs:** core-specs/objects/jurisdiction.md; core-specs/objects/trademark.md; core-specs/objects/classification.md; core-specs/objects/knowledge.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/routing.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/jurisdiction-service.md; core-specs/services/trademark-service.md; core-specs/services/classification-service.md; core-specs/services/knowledge-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/routing-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/jurisdiction-linked.md; core-specs/events/trademark-created.md; core-specs/events/classification-created.md; core-specs/events/document-created.md; core-specs/events/evidence-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/jurisdiction-api-contract.md; core-specs/contracts/events/jurisdiction-linked-payload.md  
**Related Agent Specs:** core-specs/agents/jurisdiction-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Jurisdiction API exposes governed Jurisdiction reference and linkage operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and link Jurisdiction references without treating Jurisdiction as Trademark filing, official registry record, local counsel selection, routing selection, legal availability, classification approval, fee quotation, deadline calculation or AI legal conclusion.

Jurisdiction API exists to support:

```text
jurisdiction reference management
trademark-to-jurisdiction preparation
country/region legal context
classification and local rule preparation
jurisdiction-specific knowledge lookup
matter/order jurisdiction context
routing candidate context
policy-controlled jurisdiction visibility
event trace access
API-safe jurisdiction reference validation
```

Jurisdiction API does not file applications, decide registrability, select agents, prove official status, quote fees or replace local professional review.

---

# 2. API Meaning

Jurisdiction API means:

```text
a governed interface for operating Jurisdiction references and jurisdiction links through Jurisdiction Service.
```

Jurisdiction API does not mean:

```text
Trademark filing API
official registry API
Classification API
Routing API
Agent API
Service Provider API
Fee API
Deadline API
legal opinion API
AI jurisdiction decision API
```

Jurisdiction defines country/region/legal-office context.

Execution, routing, filing, pricing and professional decisions are owned by separate services.

---

# 3. API Boundary

Jurisdiction API is responsible for:

```text
Jurisdiction create request intake
Jurisdiction read/search/list access
Jurisdiction update request intake
Jurisdiction reference validation
Trademark-to-Jurisdiction link request intake where explicitly defined
safe Jurisdiction response shaping
Permission/Policy enforcement for Jurisdiction operations
Jurisdiction-related Event reference exposure where allowed
AI Agent access boundary for Jurisdiction operations
controlled API errors
```

Jurisdiction API is not responsible for:

```text
Trademark filing execution
Order lifecycle ownership
Matter lifecycle ownership
Routing selection
Agent or Service Provider selection
Classification lifecycle ownership
fee quotation
deadline calculation
official registry synchronization truth
professional legal conclusion
AI final jurisdiction decision
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/jurisdiction.md
```

Domain rule:

```text
Jurisdiction provides governed country/region/legal-office context.
Jurisdiction is not filing execution, routing selection, official registry truth or legal conclusion by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/jurisdiction.md
core-specs/objects/trademark.md
core-specs/objects/classification.md
core-specs/objects/knowledge.md
core-specs/objects/document.md
core-specs/objects/evidence.md
core-specs/objects/matter.md
core-specs/objects/order.md
core-specs/objects/routing.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Jurisdiction API returns jurisdiction_reference_id.
- Jurisdiction API may reference Trademark, Classification, Knowledge, Matter, Order or Routing context but must not create them silently unless explicitly defined by governed operation.
- Jurisdiction API must not treat Jurisdiction as official application or registration.
- Jurisdiction API must not treat jurisdiction link as filing instruction.
- Jurisdiction API must not expose restricted filing strategy, local counsel notes or pricing assumptions by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/jurisdiction-service.md
core-specs/services/trademark-service.md
core-specs/services/classification-service.md
core-specs/services/knowledge-service.md
core-specs/services/matter-service.md
core-specs/services/order-service.md
core-specs/services/routing-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Jurisdiction API must invoke Jurisdiction Service for Jurisdiction behavior.
- Jurisdiction API must validate related references through their owning services where required.
- Jurisdiction API must invoke Permission Service where operation requires authorization.
- Jurisdiction API must invoke Policy Service where contextual constraints apply.
- Jurisdiction API must not emit Jurisdiction events directly; Jurisdiction Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/jurisdiction-linked.md
core-specs/events/trademark-created.md
core-specs/events/classification-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- linkJurisdiction may result in JurisdictionLinked.
- protected operations may produce PermissionEvaluated and PolicyEvaluated.
- API consumers must not fabricate JurisdictionLinked.
- JurisdictionLinked is relationship/link trace, not filing execution.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Jurisdiction

**Operation Category:** Create  
**Method:** POST  
**Path:** `/jurisdictions`  
**Owning Service Operation:** `createJurisdiction`  
**Permission Required:** `jurisdiction:create`  
**Policy Required:** `JurisdictionCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated  
**Event Behavior:** Service May Emit JurisdictionCreated where event is defined

Meaning:

```text
Create a governed Jurisdiction reference.
```

Non-meaning:

```text
does not create Trademark
does not file application
does not create Matter or Order
does not select Agent or Service Provider
does not approve local legal strategy
does not quote fees
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
Jurisdiction Service createJurisdiction
  ↓
Event Service record event where applicable
  ↓
Safe API response
```

## 8.2 Operation: Get Jurisdiction

**Operation Category:** Read  
**Method:** GET  
**Path:** `/jurisdictions/{jurisdiction_reference_id}`  
**Owning Service Operation:** `getJurisdiction`  
**Permission Required:** `jurisdiction:read`  
**Policy Required:** `JurisdictionVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Jurisdiction reference view.
```

Non-meaning:

```text
does not expose restricted local strategy automatically
does not expose local counsel or provider preference automatically
does not assert current official office rule truth automatically
```

## 8.3 Operation: Search Jurisdictions

**Operation Category:** Search  
**Method:** GET  
**Path:** `/jurisdictions`  
**Owning Service Operation:** `searchJurisdictions`  
**Permission Required:** `jurisdiction:search`  
**Policy Required:** `JurisdictionVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Jurisdiction references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted internal strategy access
does not expose restricted jurisdiction rules or pricing assumptions by default
```

## 8.4 Operation: Update Jurisdiction

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/jurisdictions/{jurisdiction_reference_id}`  
**Owning Service Operation:** `updateJurisdiction`  
**Permission Required:** `jurisdiction:update`  
**Policy Required:** `JurisdictionUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit JurisdictionUpdated where event is defined

Meaning:

```text
Update governed Jurisdiction metadata or status under Jurisdiction Service rules.
```

Non-meaning:

```text
does not update Trademark, Matter, Order or Routing objects automatically
does not update official registry status automatically
does not update fees or deadlines automatically
does not approve local professional conclusions
```

## 8.5 Operation: Validate Jurisdiction Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/jurisdictions/reference/validate`  
**Owning Service Operation:** `validateJurisdictionReference`  
**Permission Required:** `jurisdiction:validate`  
**Policy Required:** `JurisdictionReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Jurisdiction reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not verify filing availability
does not approve filing strategy
does not select provider
does not verify official registry data
```

## 8.6 Operation: Link Jurisdiction to Trademark

**Operation Category:** Link  
**Method:** POST  
**Path:** `/jurisdictions/{jurisdiction_reference_id}/trademarks/{trademark_reference_id}`  
**Owning Service Operation:** `linkJurisdictionToTrademark`  
**Permission Required:** `jurisdiction:trademark:link`  
**Policy Required:** `JurisdictionTrademarkLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service Must Emit JurisdictionLinked

Meaning:

```text
Create a governed relationship reference between Jurisdiction and Trademark.
```

Non-meaning:

```text
does not file application
does not create Order or Matter
does not approve local filing strategy
does not select local counsel
does not verify local availability
```

## 8.7 Operation: Retrieve Jurisdiction Knowledge

**Operation Category:** Action  
**Method:** POST  
**Path:** `/jurisdictions/{jurisdiction_reference_id}/knowledge/retrieve`  
**Owning Service Operation:** `retrieveJurisdictionKnowledge`  
**Permission Required:** `jurisdiction:knowledge:retrieve`  
**Policy Required:** `JurisdictionKnowledgeAccessPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service May Emit PolicyEvaluated

Meaning:

```text
Retrieve policy-filtered Knowledge Records relevant to a Jurisdiction context.
```

Non-meaning:

```text
does not guarantee current official truth
does not provide legal opinion
does not bypass Knowledge policy
does not remove human review where required
```

## 8.8 Operation: List Jurisdiction Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/jurisdictions/{jurisdiction_reference_id}/events`  
**Owning Service Operation:** `listJurisdictionEvents`  
**Permission Required:** `jurisdiction:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Jurisdiction-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Jurisdiction Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  jurisdiction_code: string
  jurisdiction_type: string
  jurisdiction_status: string | optional
  display_name: string
  parent_jurisdiction_reference_id: string | null
  office_reference: string | null
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_generated: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Jurisdiction Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  jurisdiction_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  jurisdiction_status: string | optional
  display_name: string | optional
  office_reference: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Jurisdiction Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  jurisdiction_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Jurisdiction to Trademark Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  jurisdiction_reference_id: string
  trademark_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  link_type: string
  intended_service_type: string | null
  link_reason: string | null
  request_context: object
```

## 9.5 Retrieve Jurisdiction Knowledge Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  agent_identity_reference_id: string | null
  agent_contract_reference_id: string | null
  retrieval_purpose: string
  filters:
    knowledge_type: list[string]
    language_codes: list[string]
    max_results: integer
```

Request rules:

```text
- Requests must not include confidential filing strategy, pricing assumptions, local counsel notes or restricted knowledge content by default.
- Requests must use controlled jurisdiction_type, jurisdiction_status, source_type, link_type and intended_service_type values.
- AI-generated jurisdiction suggestions must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Jurisdiction Response

```yaml
status: 200
body:
  jurisdiction_reference_id: string
  jurisdiction_code: string
  jurisdiction_type: string
  jurisdiction_status: string
  display_name: string
  parent_jurisdiction_reference_id: string | null
  office_reference: string | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
  related_trademark_reference_ids: list[string]
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Jurisdiction Response

```yaml
status: 201
body:
  jurisdiction_reference_id: string
  jurisdiction_code: string
  jurisdiction_status: string
  review_required: boolean
  related_event_reference_ids: list[string]
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Jurisdiction Reference Validation Response

```yaml
status: 200
body:
  jurisdiction_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Jurisdiction Knowledge Retrieval Response

```yaml
status: 200
body:
  jurisdiction_reference_id: string
  authorized_knowledge_reference_id: string | null
  retrieved_records:
    - knowledge_record_reference_id: string
      safe_summary: object
      allowed_content_scope: string
  policy_decision_reference_id: string | null
  human_review_required: boolean
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply filing, local availability, provider selection, fee quote or legal conclusion.
- Responses must not expose restricted local strategy, provider preference or pricing assumptions by default.
- Responses must distinguish Jurisdiction references from Trademark, Matter, Order and Routing references.
- Responses must identify review requirements for AI-created or AI-suggested content.
```

---

# 11. Controlled Values

## 11.1 jurisdiction_type

```text
Country
Region
IntergovernmentalOffice
Territory
StateProvince
SpecialAdministrativeRegion
CustomsUnion
TreatySystem
Other
Unknown
```

## 11.2 jurisdiction_status

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
OfficialSource
KnowledgeDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.4 link_type

```text
TargetJurisdiction
ExistingRegistrationJurisdiction
PriorityJurisdiction
MadridDesignation
MonitoringJurisdiction
ReferenceJurisdiction
Unknown
```

## 11.5 intended_service_type

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
Routing
Unknown
```

## 11.6 retrieval_purpose

```text
Read
Summarize
Draft
Recommend
Validate
Classify
Explain
AIAssistedWorkflow
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
Deprecated
ContextMismatch
Unknown
```

## 11.8 intended_use

```text
TrademarkPreparation
MatterPreparation
OrderPreparation
ClassificationPreparation
RoutingContext
KnowledgeRetrieval
Monitoring
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
jurisdiction:create
jurisdiction:read
jurisdiction:search
jurisdiction:update
jurisdiction:validate
jurisdiction:trademark:link
jurisdiction:knowledge:retrieve
jurisdiction:event:read
```

Rules:

```text
- Jurisdiction read/search must be permission-controlled.
- Jurisdiction creation must not imply filing availability or legal approval.
- Jurisdiction validation must not authorize filing or routing.
- Jurisdiction-to-Trademark linking requires separate permission.
- Jurisdiction Knowledge retrieval requires Knowledge and Policy controls.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
JurisdictionCreationPolicy
JurisdictionUpdatePolicy
JurisdictionVisibilityPolicy
JurisdictionReferencePolicy
JurisdictionTrademarkLinkPolicy
JurisdictionKnowledgeAccessPolicy
EventVisibilityPolicy
AIAgentJurisdictionAccessPolicy
RestrictedJurisdictionStrategyPolicy
CrossOrganizationJurisdictionPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Jurisdiction fields.
- Policy may require human review for AI-generated Jurisdiction content.
- Policy may restrict cross-organization Jurisdiction lookup.
- Policy may restrict local counsel, pricing, deadline and strategy fields.
- Policy may restrict full Knowledge content and return safe summaries only.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Jurisdiction: Restricted / HumanReviewRequired where AI-generated
Get Jurisdiction: Restricted
Search Jurisdictions: Restricted
Update Jurisdiction: Restricted / HumanReviewRequired where sensitive
Validate Jurisdiction Reference: Allowed under contract
Link Jurisdiction to Trademark: Restricted / HumanReviewRequired where AI-suggested
Retrieve Jurisdiction Knowledge: Restricted
List Jurisdiction Events: Restricted
```

AI Agents may:

```text
suggest jurisdiction normalization
summarize safe Jurisdiction metadata
flag deprecated or conflicting Jurisdiction references
validate Jurisdiction references for authorized actions
suggest Trademark-to-Jurisdiction links for human review
retrieve authorized Jurisdiction Knowledge
```

AI Agents must not:

```text
fabricate Jurisdiction
fabricate JurisdictionLinked events
treat AI-generated Jurisdiction as approved professional object
treat Jurisdiction as filing or legal conclusion
select provider or routing candidate
approve filing availability
quote official fees or deadlines unless governed by separate source and review
bypass Permission or Policy
expose restricted jurisdiction strategy
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

Jurisdiction API may expose:

```text
JurisdictionLinked
TrademarkCreated
ClassificationCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Jurisdiction events directly.
- JurisdictionLinked must not be treated as filing, routing selection or local availability approval.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] jurisdiction_reference_id is present where required.
[ ] jurisdiction_code is present for create operation.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] parent_jurisdiction_reference_id is valid where provided.
[ ] trademark_reference_id is valid for link operation.
[ ] jurisdiction_type is controlled.
[ ] jurisdiction_status is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] intended_service_type is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted jurisdiction/strategy/provider/pricing fields are omitted or allowed.
[ ] AI-generated content is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] JurisdictionLinked is emitted after successful governed link operation.
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
JurisdictionReferenceInvalid
ParentJurisdictionReferenceInvalid
TrademarkReferenceInvalid
KnowledgeReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedJurisdictionStrategy
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
- Errors must not expose restricted jurisdiction strategy.
- Errors must not expose provider preference, local counsel notes or pricing assumptions.
- Errors must not expose restricted Knowledge content.
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
- jurisdiction_type, jurisdiction_status, link_type and intended_service_type changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI jurisdiction operation behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Jurisdiction API spec
cite Jurisdiction Service Specification
cite Jurisdiction Object Specification
cite JurisdictionLinked Event Specification
cite Trademark/Classification/Knowledge/Routing specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe summaries by default
write tests for invalid jurisdiction_reference_id
write tests for invalid trademark/parent jurisdiction references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Jurisdiction creation does not create Trademark, Order or Matter
write tests that Jurisdiction link does not file application
write tests that Jurisdiction validation does not approve filing, routing or legal availability
write tests for AI Agent Contract requirement
write tests for JurisdictionLinked event after successful link
```

Codex must not:

```text
write directly to database bypassing Jurisdiction Service
allow UI to emit JurisdictionLinked directly
treat Jurisdiction as filing execution
treat Jurisdiction as Routing selection
treat Jurisdiction as official registry truth
treat Jurisdiction as legal availability approval
treat AI-generated Jurisdiction analysis as approved professional conclusion
expose restricted jurisdiction/provider/pricing strategy for convenience
allow AI to fabricate Jurisdiction references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Jurisdiction API purpose.
[ ] It defines Jurisdiction API meaning.
[ ] It defines Jurisdiction API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, link, knowledge retrieval and event-list operations.
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
| 0.1.0 | Draft | Initial Jurisdiction API specification. Defines governed Jurisdiction reference and linkage interface and separates Jurisdiction API from filing, official registry truth, routing selection, provider selection, fee/deadline decision and AI legal conclusion. |

---

**End of API Specification**
