# API Specification — Evidence API

**Spec ID:** B02-API-EVIDENCE  
**Spec Type:** API Specification  
**API Name:** Evidence API  
**API File:** core-specs/api/evidence-api.md  
**Related Domain:** core-specs/domains/evidence.md  
**Related Object Specs:** core-specs/objects/evidence.md; core-specs/objects/document.md; core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/communication.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/evidence-service.md; core-specs/services/document-service.md; core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/communication-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/evidence-created.md; core-specs/events/document-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/evidence-api-contract.md; core-specs/contracts/events/evidence-created-payload.md  
**Related Agent Specs:** core-specs/agents/evidence-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Evidence API exposes governed Evidence reference and proof-context operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and link Evidence references without treating Evidence as Document, raw file, official filing, legal sufficiency, use acceptance, ownership proof, litigation proof, professional conclusion or AI-extracted truth.

Evidence API exists to support:

```text
evidence reference creation
proof material organization
document-to-evidence transformation under governance
trademark use and ownership support context
matter/order evidence preparation
communication-derived evidence preparation
policy-controlled evidence visibility
AI-assisted evidence extraction and review
event trace access
API-safe evidence reference validation
```

Evidence API does not prove legal sufficiency by itself, submit evidence officially, approve evidence for use or replace professional review.

---

# 2. API Meaning

Evidence API means:

```text
a governed interface for operating Evidence references through Evidence Service.
```

Evidence API does not mean:

```text
Document API
official filing API
legal proof API
professional opinion API
Matter API
Order API
Communication API
raw file storage API
AI extraction truth API
```

Evidence is the proof layer.

Document is the artifact layer.

Professional sufficiency and official acceptance are separate decisions.

---

# 3. API Boundary

Evidence API is responsible for:

```text
Evidence create request intake
Evidence read/search/list access
Evidence update request intake
Evidence reference validation
Evidence link request intake where explicitly governed
safe Evidence response shaping
Permission/Policy enforcement for Evidence operations
Evidence-related Event reference exposure where allowed
AI Agent access boundary for Evidence operations
controlled API errors
```

Evidence API is not responsible for:

```text
Document storage lifecycle
official filing execution
professional sufficiency approval
office acceptance
litigation decision
customer instruction acceptance
matter/order workflow execution
AI final proof conclusion
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/evidence.md
```

Domain rule:

```text
Evidence organizes proof-context references.
Evidence is not Document, filing, official acceptance or legal sufficiency by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/evidence.md
core-specs/objects/document.md
core-specs/objects/trademark.md
core-specs/objects/brand.md
core-specs/objects/customer.md
core-specs/objects/matter.md
core-specs/objects/order.md
core-specs/objects/communication.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Evidence API returns evidence_reference_id.
- Evidence API may reference Document, Trademark, Brand, Customer, Matter, Order or Communication context but must not create them silently.
- Evidence API must not treat Document as Evidence automatically.
- Evidence API must not treat Evidence creation as professional sufficiency approval.
- Evidence API must not expose restricted raw proof content by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/evidence-service.md
core-specs/services/document-service.md
core-specs/services/trademark-service.md
core-specs/services/brand-service.md
core-specs/services/customer-service.md
core-specs/services/matter-service.md
core-specs/services/order-service.md
core-specs/services/communication-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Evidence API must invoke Evidence Service for Evidence behavior.
- Evidence API must validate related references through their owning services where required.
- Evidence API must invoke Permission Service where operation requires authorization.
- Evidence API must invoke Policy Service where contextual constraints apply.
- Evidence API must not emit Evidence events directly; Evidence Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/evidence-created.md
core-specs/events/document-created.md
core-specs/events/communication-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createEvidence may result in EvidenceCreated.
- Document-created events do not create Evidence automatically.
- Communication-created events do not create Evidence automatically.
- API consumers must not fabricate EvidenceCreated.
- EvidenceCreated is proof-context reference trace, not legal sufficiency or official acceptance.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Evidence

**Operation Category:** Create  
**Method:** POST  
**Path:** `/evidence`  
**Owning Service Operation:** `createEvidence`  
**Permission Required:** `evidence:create`  
**Policy Required:** `EvidenceCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated analysis  
**Event Behavior:** Service Must Emit EvidenceCreated

Meaning:

```text
Create a governed Evidence reference and proof-context record.
```

Non-meaning:

```text
does not create Document
does not file evidence
does not approve sufficiency
does not prove ownership
does not prove use
does not create Matter or Order
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
Evidence Service createEvidence
  ↓
Event Service record EvidenceCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Evidence

**Operation Category:** Read  
**Method:** GET  
**Path:** `/evidence/{evidence_reference_id}`  
**Owning Service Operation:** `getEvidence`  
**Permission Required:** `evidence:read`  
**Policy Required:** `EvidenceVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Evidence reference and proof-context view.
```

Non-meaning:

```text
does not expose raw proof content automatically
does not expose restricted customer/matter strategy automatically
does not prove sufficiency automatically
```

## 8.3 Operation: Search Evidence

**Operation Category:** Search  
**Method:** GET  
**Path:** `/evidence`  
**Owning Service Operation:** `searchEvidence`  
**Permission Required:** `evidence:search`  
**Policy Required:** `EvidenceVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Evidence references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted proof repository access
does not expose restricted evidence content by default
```

## 8.4 Operation: Update Evidence

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/evidence/{evidence_reference_id}`  
**Owning Service Operation:** `updateEvidence`  
**Permission Required:** `evidence:update`  
**Policy Required:** `EvidenceUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit EvidenceUpdated where event is defined

Meaning:

```text
Update governed Evidence metadata, status or linkage under Evidence Service rules.
```

Non-meaning:

```text
does not update Document automatically
does not approve evidence sufficiency
does not change Matter or Order status automatically
does not rewrite audit/event history
```

## 8.5 Operation: Validate Evidence Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/evidence/reference/validate`  
**Owning Service Operation:** `validateEvidenceReference`  
**Permission Required:** `evidence:validate`  
**Policy Required:** `EvidenceReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that an Evidence reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not verify legal sufficiency
does not approve evidence for filing
does not authorize raw proof access
```

## 8.6 Operation: Link Evidence to Object

**Operation Category:** Link  
**Method:** POST  
**Path:** `/evidence/{evidence_reference_id}/links`  
**Owning Service Operation:** `linkEvidenceToObject`  
**Permission Required:** `evidence:link`  
**Policy Required:** `EvidenceLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit EvidenceUpdated or future LinkEvent where defined

Meaning:

```text
Create a governed relationship between Evidence and a target Core object.
```

Non-meaning:

```text
does not create target object
does not approve evidence use
does not file or submit evidence
does not prove sufficiency
```

## 8.7 Operation: Assess Evidence Sufficiency

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/evidence/{evidence_reference_id}/sufficiency/assess`  
**Owning Service Operation:** `assessEvidenceSufficiency`  
**Permission Required:** `evidence:sufficiency:assess`  
**Policy Required:** `EvidenceSufficiencyAssessmentPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired  
**Event Behavior:** Service May Emit PolicyEvaluated; must not change Evidence status unless explicitly updated by governed operation

Meaning:

```text
Produce a governed assessment draft or professional review record about possible evidence sufficiency.
```

Non-meaning:

```text
does not approve sufficiency automatically
does not guarantee office acceptance
does not prove legal fact
does not replace professional review
```

## 8.8 Operation: Prepare Evidence from Document

**Operation Category:** Create  
**Method:** POST  
**Path:** `/evidence/from-document`  
**Owning Service Operation:** `createEvidenceFromDocument`  
**Permission Required:** `evidence:create:from-document`  
**Policy Required:** `EvidenceFromDocumentPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Service Must Emit EvidenceCreated if created

Meaning:

```text
Create Evidence through Evidence Service using a governed Document reference as source.
```

Non-meaning:

```text
does not make all Documents Evidence
does not approve sufficiency
does not file evidence
does not prove ownership or use
```

## 8.9 Operation: List Evidence Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/evidence/{evidence_reference_id}/events`  
**Owning Service Operation:** `listEvidenceEvents`  
**Permission Required:** `evidence:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Evidence-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Evidence Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  evidence_type: string
  evidence_status: string | optional
  evidence_purpose: string
  source_type: string
  source_document_reference_id: string | null
  source_communication_reference_id: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_generated_analysis: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Evidence Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  evidence_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  evidence_status: string | optional
  evidence_type: string | optional
  evidence_purpose: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Evidence Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  evidence_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Evidence to Object Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  evidence_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  target_object_type: string
  target_object_reference_id: string
  link_type: string
  link_reason: string | null
  request_context: object
```

## 9.5 Assess Evidence Sufficiency Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  assessment_purpose: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.6 Create Evidence From Document Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  document_reference_id: string
  evidence_type: string
  evidence_purpose: string
  target_object_type: string | null
  target_object_reference_id: string | null
  request_context: object
  ai_context:
    ai_assisted: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

Request rules:

```text
- Requests must not include unrestricted raw proof content by default.
- Requests must not include credentials, secrets or privileged strategy.
- Requests must use controlled evidence_type, evidence_status, evidence_purpose, source_type, link_type and intended_use values.
- AI-generated analysis and sufficiency assessment must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Evidence Response

```yaml
status: 200
body:
  evidence_reference_id: string
  evidence_type: string
  evidence_status: string
  evidence_purpose: string
  source_type: string
  source_document_reference_id: string | null
  source_communication_reference_id: string | null
  safe_summary:
    created_at: datetime
    updated_at: datetime | null
    content_summary: string | null
    sufficiency_summary: string | null
  linked_object_references:
    - target_object_type: string
      target_object_reference_id: string
      link_type: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Evidence Response

```yaml
status: 201
body:
  evidence_reference_id: string
  evidence_status: string
  review_required: boolean
  related_event_reference_ids:
    - evidence_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Evidence Reference Validation Response

```yaml
status: 200
body:
  evidence_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Evidence Sufficiency Assessment Response

```yaml
status: 200
body:
  evidence_reference_id: string
  assessment_reference_id: string | null
  assessment_status: string
  safe_summary:
    sufficiency_observation: string | null
    risk_summary: string | null
    missing_items: list[string]
  confidence_level: string
  human_review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply legal sufficiency, office acceptance, ownership proof or use proof unless a governed professional decision says so.
- Responses must not expose raw proof content unless explicitly allowed by Policy.
- Responses must distinguish Evidence references from Document, Matter, Order and Communication references.
- Responses must identify review requirements for AI-assisted assessment.
```

---

# 11. Controlled Values

## 11.1 evidence_type

```text
UseEvidence
OwnershipEvidence
PriorityEvidence
SpecimenEvidence
SalesEvidence
WebsiteEvidence
MarketplaceEvidence
AdvertisingEvidence
CertificateEvidence
CommunicationEvidence
DocumentEvidence
Other
Unknown
```

## 11.2 evidence_status

```text
Draft
Active
ReviewRequired
UnderReview
AcceptedInternal
RejectedInternal
Insufficient
Superseded
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 evidence_purpose

```text
TrademarkUse
OwnershipProof
PriorityClaim
OfficeActionResponse
RenewalDeclaration
Opposition
Cancellation
Recordal
PortfolioReview
InternalReference
Unknown
```

## 11.4 source_type

```text
DocumentDerived
CommunicationDerived
ProfessionalInput
CustomerInput
AgentInput
ServiceProviderInput
SystemGenerated
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.5 link_type

```text
PrimaryEvidence
SupportingEvidence
SourceEvidence
DerivedEvidence
SpecimenEvidence
ReferenceOnly
Unknown
```

## 11.6 assessment_purpose

```text
UseSufficiency
OwnershipSufficiency
SpecimenReview
PriorityReview
OfficeActionSupport
RenewalSupport
OppositionSupport
CancellationSupport
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
Insufficient
Archived
ContextMismatch
Unknown
```

## 11.9 intended_use

```text
TrademarkReference
MatterPreparation
OrderPreparation
FilingPreparation
RenewalSupport
OfficeActionResponse
OppositionSupport
CancellationSupport
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
evidence:create
evidence:read
evidence:search
evidence:update
evidence:validate
evidence:link
evidence:sufficiency:assess
evidence:create:from-document
evidence:event:read
```

Rules:

```text
- Evidence read/search must be permission-controlled.
- Evidence creation must not imply sufficiency approval.
- Evidence validation must not authorize raw proof access or filing use.
- Evidence sufficiency assessment requires separate permission.
- Evidence-from-Document creation requires both Evidence and Document reference permissions where applicable.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
EvidenceCreationPolicy
EvidenceUpdatePolicy
EvidenceVisibilityPolicy
EvidenceReferencePolicy
EvidenceLinkPolicy
EvidenceSufficiencyAssessmentPolicy
EvidenceFromDocumentPolicy
EventVisibilityPolicy
AIAgentEvidenceAccessPolicy
RestrictedEvidenceContentPolicy
CrossOrganizationEvidencePolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Evidence fields and raw proof content.
- Policy may require human review for AI-assisted evidence analysis.
- Policy may restrict cross-organization Evidence lookup.
- Policy may restrict customer, matter, filing strategy and privileged proof material.
- Policy may restrict raw file/proof access even when metadata is visible.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Evidence: Restricted / HumanReviewRequired where AI-generated analysis
Get Evidence: Restricted
Search Evidence: Restricted
Update Evidence: Restricted / HumanReviewRequired where sensitive
Validate Evidence Reference: Allowed under contract
Link Evidence to Object: Restricted / HumanReviewRequired where AI-suggested
Assess Evidence Sufficiency: Restricted / HumanReviewRequired
Create Evidence from Document: Restricted / HumanReviewRequired
List Evidence Events: Restricted
```

AI Agents may:

```text
summarize safe Evidence metadata
extract suggested proof facts where authorized
flag missing evidence type or context
validate Evidence references for authorized actions
suggest Evidence-to-object links for human review
prepare sufficiency assessment draft for human review
```

AI Agents must not:

```text
fabricate Evidence
fabricate EvidenceCreated events
treat Evidence as Document
treat AI assessment as legal sufficiency
treat Evidence as filed or accepted
prove legal facts or use by itself
bypass Permission or Policy
expose restricted raw proof content
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

Evidence API may expose:

```text
EvidenceCreated
DocumentCreated
CommunicationCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Evidence events directly.
- EvidenceCreated must not be treated as DocumentCreated, filing, approval, office acceptance or proof sufficiency.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] evidence_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] source_document_reference_id is valid where provided.
[ ] source_communication_reference_id is valid where provided.
[ ] target_object_type and target_object_reference_id are valid for link operation.
[ ] evidence_type is controlled.
[ ] evidence_status is controlled.
[ ] evidence_purpose is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] assessment_purpose is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted evidence/customer/matter/strategy/raw proof fields are omitted or allowed.
[ ] AI-generated analysis or assessment is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] EvidenceCreated is emitted after createEvidence succeeds.
[ ] Sufficiency assessment does not approve sufficiency automatically.
[ ] Evidence-from-Document operation routes through Evidence Service and does not mutate Document truth.
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
EvidenceReferenceInvalid
DocumentReferenceInvalid
CommunicationReferenceInvalid
SourceObjectReferenceInvalid
TargetObjectReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedEvidenceContent
RawProofAccessRestricted
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
- Errors must not expose restricted Evidence content.
- Errors must not expose raw proof material or privileged strategy.
- Errors must not expose customer/matter confidential content.
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
- evidence_type, evidence_status, evidence_purpose and link_type changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI evidence assessment behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Evidence API spec
cite Evidence Service Specification
cite Evidence Object Specification
cite EvidenceCreated Event Specification
cite Document/Communication/Matter/Order specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid evidence_reference_id
write tests for invalid document/source/target references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Evidence creation does not create Document
write tests that Evidence creation does not file or approve evidence
write tests that sufficiency assessment does not approve sufficiency automatically
write tests for AI Agent Contract and human review requirement
write tests for EvidenceCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Evidence Service
allow UI to emit EvidenceCreated directly
treat Evidence as Document
treat Evidence as filing execution
treat Evidence as legal proof or sufficiency approval
treat AI evidence assessment as verified legal fact
create Matter, Order or Document silently from Evidence operations
expose raw proof content or privileged strategy for convenience
allow AI to fabricate Evidence references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Evidence API purpose.
[ ] It defines Evidence API meaning.
[ ] It defines Evidence API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, link, sufficiency assessment, evidence-from-document and event-list operations.
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
| 0.1.0 | Draft | Initial Evidence API specification. Defines governed Evidence reference interface and separates Evidence API from Document, filing, proof sufficiency, official acceptance, approval and AI evidence truth. |

---

**End of API Specification**
