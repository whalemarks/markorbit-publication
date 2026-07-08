# API Specification — Document API

**Spec ID:** B02-API-DOCUMENT  
**Spec Type:** API Specification  
**API Name:** Document API  
**API File:** core-specs/api/document-api.md  
**Related Domain:** core-specs/domains/document.md  
**Related Object Specs:** core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/communication.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/communication-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/document-created.md; core-specs/events/evidence-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/document-api-contract.md; core-specs/contracts/events/document-created-payload.md  
**Related Agent Specs:** core-specs/agents/document-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Document API exposes governed Document reference and file-metadata operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and link Document references without treating Document as Evidence, legal proof, filing package approval, official submission, communication delivery, customer instruction, professional conclusion or AI-extracted truth.

Document API exists to support:

```text
document reference creation
file metadata and storage reference management
document-to-trademark/brand/customer/matter/order context
document-to-evidence preparation
communication attachment registration
policy-controlled document visibility
AI-assisted document extraction under governance
event trace access
API-safe document reference validation
```

Document API does not prove facts, establish evidentiary sufficiency, file documents with offices, approve document content or replace professional review.

---

# 2. API Meaning

Document API means:

```text
a governed interface for operating Document references through Document Service.
```

Document API does not mean:

```text
Evidence API
official filing API
Communication API
Matter API
Order API
legal proof API
document approval API
storage implementation API
AI extraction truth API
```

Document is an artifact/reference layer.

Evidence is the proof layer.

Submission, filing and professional approval are owned by separate processes and services.

---

# 3. API Boundary

Document API is responsible for:

```text
Document create request intake
Document read/search/list access
Document update request intake
Document reference validation
Document link request intake where explicitly governed
safe Document response shaping
Permission/Policy enforcement for Document operations
Document-related Event reference exposure where allowed
AI Agent access boundary for Document operations
controlled API errors
```

Document API is not responsible for:

```text
Evidence sufficiency
official filing execution
communication delivery
professional document approval
customer instruction acceptance
matter/order workflow execution
storage provider implementation details
OCR/extraction truth by itself
AI final professional conclusion
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/document.md
```

Domain rule:

```text
Document manages artifacts and file references.
Document is not Evidence, official submission, professional approval or legal proof by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/document.md
core-specs/objects/evidence.md
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
- Document API returns document_reference_id.
- Document API may reference Trademark, Brand, Customer, Matter, Order or Communication context but must not create them silently.
- Document API must not treat Document as Evidence automatically.
- Document API must not treat file upload as filing, approval or proof.
- Document API must not expose restricted raw file content by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/document-service.md
core-specs/services/evidence-service.md
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
- Document API must invoke Document Service for Document behavior.
- Document API must validate related references through their owning services where required.
- Document API must invoke Permission Service where operation requires authorization.
- Document API must invoke Policy Service where contextual constraints apply.
- Document API must not emit Document events directly; Document Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/document-created.md
core-specs/events/evidence-created.md
core-specs/events/communication-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createDocument may result in DocumentCreated.
- createEvidenceFromDocument must use Evidence Service and may result in EvidenceCreated.
- communication attachment context must use Communication Service where applicable.
- API consumers must not fabricate DocumentCreated.
- DocumentCreated is artifact reference trace, not proof, filing or approval.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Document

**Operation Category:** Create  
**Method:** POST  
**Path:** `/documents`  
**Owning Service Operation:** `createDocument`  
**Permission Required:** `document:create`  
**Policy Required:** `DocumentCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated metadata  
**Event Behavior:** Service Must Emit DocumentCreated

Meaning:

```text
Create a governed Document reference and metadata record.
```

Non-meaning:

```text
does not create Evidence
does not file document
does not approve document content
does not prove legal fact
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
Document Service createDocument
  ↓
Event Service record DocumentCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Document

**Operation Category:** Read  
**Method:** GET  
**Path:** `/documents/{document_reference_id}`  
**Owning Service Operation:** `getDocument`  
**Permission Required:** `document:read`  
**Policy Required:** `DocumentVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Document reference and metadata view.
```

Non-meaning:

```text
does not expose raw file content automatically
does not expose restricted customer/matter strategy automatically
does not prove evidence sufficiency automatically
```

## 8.3 Operation: Search Documents

**Operation Category:** Search  
**Method:** GET  
**Path:** `/documents`  
**Owning Service Operation:** `searchDocuments`  
**Permission Required:** `document:search`  
**Policy Required:** `DocumentVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Document references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted file repository access
does not expose restricted raw content by default
```

## 8.4 Operation: Update Document

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/documents/{document_reference_id}`  
**Owning Service Operation:** `updateDocument`  
**Permission Required:** `document:update`  
**Policy Required:** `DocumentUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit DocumentUpdated where event is defined

Meaning:

```text
Update governed Document metadata, status or linkage under Document Service rules.
```

Non-meaning:

```text
does not update Evidence automatically
does not approve document content
does not change Matter or Order status automatically
does not rewrite audit/event history
```

## 8.5 Operation: Validate Document Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/documents/reference/validate`  
**Owning Service Operation:** `validateDocumentReference`  
**Permission Required:** `document:validate`  
**Policy Required:** `DocumentReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Document reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not verify evidence sufficiency
does not approve document for filing
does not authorize raw file access
```

## 8.6 Operation: Link Document to Object

**Operation Category:** Link  
**Method:** POST  
**Path:** `/documents/{document_reference_id}/links`  
**Owning Service Operation:** `linkDocumentToObject`  
**Permission Required:** `document:link`  
**Policy Required:** `DocumentLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit DocumentUpdated or future LinkEvent where defined

Meaning:

```text
Create a governed relationship between Document and a target Core object.
```

Non-meaning:

```text
does not create target object
does not create Evidence
does not approve document use
does not file or submit document
```

## 8.7 Operation: Extract Document Metadata

**Operation Category:** Action  
**Method:** POST  
**Path:** `/documents/{document_reference_id}/extract`  
**Owning Service Operation:** `extractDocumentMetadata`  
**Permission Required:** `document:extract`  
**Policy Required:** `DocumentExtractionPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit DocumentCreated

Meaning:

```text
Extract or suggest metadata from Document content under governed AI/automation constraints.
```

Non-meaning:

```text
does not make extracted content verified
does not create Evidence automatically
does not approve document content
does not bypass human review where required
```

## 8.8 Operation: Prepare Evidence from Document

**Operation Category:** Action  
**Method:** POST  
**Path:** `/documents/{document_reference_id}/evidence/prepare`  
**Owning Service Operation:** `prepareEvidenceFromDocument`  
**Permission Required:** `document:evidence:prepare`  
**Policy Required:** `DocumentEvidencePreparationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired  
**Event Behavior:** Must route through Evidence Service for EvidenceCreated if evidence is actually created

Meaning:

```text
Prepare a governed request to create Evidence from a Document reference.
```

Non-meaning:

```text
does not create Evidence unless Evidence Service accepts and creates it
does not prove sufficiency
does not approve use in filing or litigation
```

## 8.9 Operation: List Document Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/documents/{document_reference_id}/events`  
**Owning Service Operation:** `listDocumentEvents`  
**Permission Required:** `document:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Document-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Document Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  document_type: string
  document_status: string | optional
  file_reference_id: string | null
  file_name: string | null
  mime_type: string | null
  file_size_bytes: integer | null
  source_type: string
  source_object_type: string | null
  source_object_reference_id: string | null
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_generated_metadata: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Document Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  document_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  document_status: string | optional
  document_type: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Document Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  document_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Document to Object Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  document_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  target_object_type: string
  target_object_reference_id: string
  link_type: string
  link_reason: string | null
  request_context: object
```

## 9.5 Extract Document Metadata Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  extraction_purpose: string
  requested_fields: list[string]
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include raw file bytes unless the API operation explicitly supports upload handling.
- Requests must not include credentials, secrets or unrestricted raw confidential content by default.
- Requests must use controlled document_type, document_status, source_type, link_type and intended_use values.
- AI-generated metadata and extraction must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Document Response

```yaml
status: 200
body:
  document_reference_id: string
  document_type: string
  document_status: string
  file_reference_id: string | null
  file_name: string | null
  mime_type: string | null
  file_size_bytes: integer | null
  source_type: string
  safe_summary:
    created_at: datetime
    updated_at: datetime | null
    content_summary: string | null
  linked_object_references:
    - target_object_type: string
      target_object_reference_id: string
      link_type: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Document Response

```yaml
status: 201
body:
  document_reference_id: string
  document_status: string
  review_required: boolean
  related_event_reference_ids:
    - document_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Document Reference Validation Response

```yaml
status: 200
body:
  document_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Document Extraction Response

```yaml
status: 200
body:
  document_reference_id: string
  extraction_reference_id: string | null
  extracted_fields:
    - field_name: string
      value_summary: string | null
      confidence_level: string
      review_required: boolean
  policy_decision_reference_id: string | null
  human_review_required: boolean
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply Evidence, filing, approval, legal proof or professional conclusion.
- Responses must not expose raw file content unless explicitly allowed by Policy.
- Responses must distinguish Document references from Evidence, Matter, Order and Communication references.
- Responses must identify review requirements for AI-extracted or AI-generated metadata.
```

---

# 11. Controlled Values

## 11.1 document_type

```text
TrademarkImage
PowerOfAttorney
Certificate
OfficeAction
ApplicationForm
FilingReceipt
RegistrationCertificate
RenewalCertificate
AssignmentDocument
EvidenceMaterial
CommunicationAttachment
Invoice
Translation
InternalNote
Other
Unknown
```

## 11.2 document_status

```text
Draft
Active
ReviewRequired
PendingExtraction
Extracted
ApprovedForUse
Rejected
Superseded
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 source_type

```text
ProfessionalUpload
CustomerUpload
AgentUpload
ServiceProviderUpload
CommunicationAttachment
SystemGenerated
DocumentDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.4 link_type

```text
PrimaryDocument
SupportingDocument
Attachment
SourceDocument
DerivedDocument
EvidenceSource
FilingDraft
ReferenceOnly
Unknown
```

## 11.5 extraction_purpose

```text
MetadataExtraction
TextExtraction
ClassificationSupport
EvidencePreparation
FilingPreparation
TranslationSupport
ReviewSupport
AIAssistedWorkflow
Unknown
```

## 11.6 confidence_level

```text
Low
Medium
High
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
Archived
ContextMismatch
Unknown
```

## 11.8 intended_use

```text
TrademarkReference
BrandReference
MatterPreparation
OrderPreparation
EvidencePreparation
FilingPreparation
CommunicationContext
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
document:create
document:read
document:search
document:update
document:validate
document:link
document:extract
document:evidence:prepare
document:event:read
```

Rules:

```text
- Document read/search must be permission-controlled.
- Document creation must not imply approval or evidence creation.
- Document validation must not authorize raw file access or filing use.
- Document extraction requires separate permission.
- Document-to-Evidence preparation requires separate permission.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
DocumentCreationPolicy
DocumentUpdatePolicy
DocumentVisibilityPolicy
DocumentReferencePolicy
DocumentLinkPolicy
DocumentExtractionPolicy
DocumentEvidencePreparationPolicy
EventVisibilityPolicy
AIAgentDocumentAccessPolicy
RestrictedDocumentContentPolicy
CrossOrganizationDocumentPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Document fields and raw file content.
- Policy may require human review for AI-extracted metadata.
- Policy may restrict cross-organization Document lookup.
- Policy may restrict customer, matter, filing strategy and privileged documents.
- Policy may restrict file download even when metadata is visible.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Document: Restricted / HumanReviewRequired where AI-generated metadata
Get Document: Restricted
Search Documents: Restricted
Update Document: Restricted / HumanReviewRequired where sensitive
Validate Document Reference: Allowed under contract
Link Document to Object: Restricted / HumanReviewRequired where AI-suggested
Extract Document Metadata: Restricted / HumanReviewRequired
Prepare Evidence from Document: Restricted / HumanReviewRequired
List Document Events: Restricted
```

AI Agents may:

```text
summarize safe Document metadata
extract suggested metadata where authorized
flag missing document type or context
validate Document references for authorized actions
suggest Document-to-object links for human review
prepare Evidence creation request for human review
```

AI Agents must not:

```text
fabricate Document
fabricate DocumentCreated events
treat Document as Evidence
treat extracted metadata as verified fact
treat Document as filed or approved
prove legal facts or use
bypass Permission or Policy
expose restricted raw file content
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

Document API may expose:

```text
DocumentCreated
EvidenceCreated
CommunicationCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Document events directly.
- DocumentCreated must not be treated as EvidenceCreated, filing, approval or proof.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] document_reference_id is present where required.
[ ] file_reference_id is valid where provided.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] source_object_reference_id is valid where provided.
[ ] target_object_type and target_object_reference_id are valid for link operation.
[ ] document_type is controlled.
[ ] document_status is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] extraction_purpose is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted document/customer/matter/strategy/raw content fields are omitted or allowed.
[ ] AI-generated metadata or extraction is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] DocumentCreated is emitted after createDocument succeeds.
[ ] Extraction operation does not verify extracted fields automatically.
[ ] Evidence preparation does not create Evidence unless Evidence Service creates it.
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
DocumentReferenceInvalid
FileReferenceInvalid
SourceObjectReferenceInvalid
TargetObjectReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedDocumentContent
FileAccessRestricted
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
- Errors must not expose restricted Document content.
- Errors must not expose file storage secrets or signed URLs.
- Errors must not expose customer/matter strategy or privileged content.
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
- document_type, document_status, source_type and link_type changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI extraction behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Document API spec
cite Document Service Specification
cite Document Object Specification
cite DocumentCreated Event Specification
cite Evidence/Communication/Matter/Order specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid document_reference_id
write tests for invalid file/source/target references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Document creation does not create Evidence
write tests that Document creation does not file or approve document
write tests that extraction does not verify content automatically
write tests for AI Agent Contract and human review requirement
write tests for DocumentCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Document Service
allow UI to emit DocumentCreated directly
treat Document as Evidence
treat Document as filing execution
treat Document as legal proof or approval
treat AI extraction as verified fact
create Matter, Order or Evidence silently from Document operations
expose raw file content, storage secrets or signed URLs for convenience
allow AI to fabricate Document references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Document API purpose.
[ ] It defines Document API meaning.
[ ] It defines Document API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, link, extract, evidence preparation and event-list operations.
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
| 0.1.0 | Draft | Initial Document API specification. Defines governed Document reference interface and separates Document API from Evidence, filing, proof, approval, communication delivery and AI extraction truth. |

---

**End of API Specification**
