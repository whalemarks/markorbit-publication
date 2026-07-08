# Service Specification — Document Service

**Spec ID:** B02-SVC-DOCUMENT-SERVICE  
**Spec Type:** Service  
**Service Name:** Document Service  
**Owning Domain:** Document  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/document.md  
**Related Object Specs:** core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/trademark.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/communication.md  
**Related Service Specs:** core-specs/services/evidence-service.md; core-specs/services/trademark-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/communication-service.md; core-specs/services/knowledge-service.md  
**Related Event Specs:** core-specs/events/document-created.md; core-specs/events/document-updated.md; core-specs/events/document-status-changed.md; core-specs/events/document-file-linked.md; core-specs/events/document-version-created.md; core-specs/events/document-review-required.md; core-specs/events/document-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/document/document-contract.md; core-specs/contracts/document/document-reference-contract.md; core-specs/contracts/document/document-file-reference-contract.md; core-specs/contracts/document/document-review-contract.md; core-specs/contracts/document/document-evidence-link-contract.md; core-specs/contracts/document/document-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Document Service defines the Core service boundary for creating, updating, validating, reviewing, versioning and linking Document objects.

It exists so that Trademark, Matter, Order, Customer, Communication, Evidence, Knowledge, AI Agents, APIs and product consumers can consistently reference professional artifacts without confusing Document with raw files, attachments, Evidence, Knowledge, Communication content, official truth or AI-generated output.

Document Service is required before:

```text
document intake
file-to-document registration
POA management
application form management
official notice management
certificate management
office action document handling
client instruction document handling
agent instruction document handling
document review and approval
document version tracking
document-to-evidence linkage
AI-assisted document extraction, summary or drafting
audit trace for document-sensitive actions
```

---

# 2. Core Meaning

Document Service means:

```text
the Core service that manages professional artifact records, including file references, document type, status, review state, version, source, relationships and governed lifecycle.
```

Document Service does not mean:

```text
file storage service
Evidence Service
Knowledge Service
Communication Service
official registry truth service
OCR engine
template generation engine
AI drafting engine by itself
```

Document Service answers:

```text
Does this Document exist?
Which file or source supports it?
What document type and status apply?
Which version is current?
Has it been reviewed, approved, rejected or archived?
Which Trademark, Matter, Order, Customer or Communication references it?
Can it be linked to Evidence?
Can another domain safely reference this Document?
```

---

# 3. Service Category

Document Service is a Professional Core Service.

It manages professional artifacts.

It does not manage raw file storage lifecycle by itself.

It does not convert Documents into Evidence or Knowledge automatically.

It does not make final professional conclusions.

---

# 4. Architectural Position

Document Service sits between source files/attachments and professional execution.

```text
File / Attachment / Source material appears
        ↓
Document Service registers governed artifact
        ↓
Review determines professional usability
        ↓
Evidence Service may register proof purpose where needed
        ↓
Matter / Trademark / Order consume Document reference
        ↓
Event and Audit preserve trace
```

Document is the artifact layer.

Evidence is the proof layer.

Knowledge is the governed reference layer.

Communication is the message lifecycle layer.

---

# 5. Scope

Document Service includes:

```text
document creation
document update
document status management
document file reference linkage
document version management
document review management
document relationship linkage
document evidence linkage
document reference validation
document audit trace
document event emission
```

MVP scope includes:

```text
create document
get document
update document metadata
change document status
link file reference
create document version
record review status
link document to trademark
link document to matter/order/communication
link document to evidence reference
validate document reference
emit document events
```

Deferred scope includes:

```text
file storage backend
full document management system
OCR engine
template generation engine
e-signature system
advanced document comparison
automatic evidence conversion
automatic knowledge extraction approval
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createDocument | Create Document object | Yes | DocumentCreated |
| getDocument | Retrieve Document by ID | Yes | No |
| updateDocument | Update governed metadata | Yes | DocumentUpdated |
| changeDocumentStatus | Change Document lifecycle status | Yes | DocumentStatusChanged |
| linkDocumentFile | Link file/storage reference | Yes | DocumentFileLinked |
| createDocumentVersion | Create version reference | Yes | DocumentVersionCreated |
| reviewDocument | Record review result | Yes | DocumentReviewed |
| requireDocumentReview | Mark review required | Yes | DocumentReviewRequired |
| linkDocumentTrademark | Link Document to Trademark | Yes | DocumentTrademarkLinked |
| linkDocumentMatter | Link Document to Matter | Yes | DocumentMatterLinked |
| linkDocumentOrder | Link Document to Order | Partial | DocumentOrderLinked |
| linkDocumentCommunication | Link Document to Communication | Yes | DocumentCommunicationLinked |
| linkDocumentEvidence | Link Document to Evidence reference | Partial | DocumentEvidenceLinked |
| validateDocumentReference | Validate whether Document can be referenced | Yes | DocumentReferenceValidated |
| archiveDocument | Archive Document reference | Partial | DocumentArchived |

---

# 7. Inputs

Document Service accepts:

```text
document_type
title_reference
status
review_status
file_reference_id
source_reference
version_reference
parent_document_id
jurisdiction_reference_id
trademark_reference_id
matter_reference_id
order_reference_id
customer_reference_id
communication_reference_id
evidence_reference_ids
language_reference
confidentiality_level
metadata
actor_context
request_context
```

Required for creation:

```text
document_type
title_reference
status
review_status
source_reference
actor_context
```

Required for file linkage:

```text
document_reference_id
file_reference_id
file_source_reference
actor_context
```

Required for review:

```text
document_reference_id
review_status
review_note_reference
actor_context
```

Required for validation:

```text
document_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Document Service returns:

```text
Document object
Document reference
Document validation result
Document file link result
Document version result
Document review result
Document relationship link result
Document status result
Document event reference
error result
```

Validation output must include:

```text
is_valid
document_reference_id
document_type
status
review_status
version_reference
reason_code
review_required
confidentiality_hint where applicable
policy_hint where applicable
```

Validation output must not expose restricted file content or confidential document material unnecessarily.

---

# 9. Controlled Values

## 9.1 document_type

```text
PowerOfAttorney
ApplicationForm
OfficialNotice
OfficeAction
Certificate
AssignmentDocument
RenewalDocument
ChangeDocument
EvidenceMaterial
ClientInstruction
AgentInstruction
Translation
Draft
Other
Unknown
```

## 9.2 status

```text
Draft
Received
Uploaded
ReviewRequired
Reviewed
Approved
Rejected
Filed
Issued
Archived
DeletedReferenceOnly
```

## 9.3 review_status

```text
Unreviewed
ReviewRequired
HumanReviewed
AIReviewedDraft
ApprovedForUse
Rejected
NeedsRevision
```

## 9.4 confidentiality_level

```text
Public
Internal
Confidential
HighlyConfidential
Restricted
Unknown
```

## 9.5 validation_result

```text
Valid
Invalid
NotFound
ReviewRequired
Rejected
Archived
ConfidentialityRestricted
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Document Requires Type and Title

Document creation must require:

```text
document_type
title_reference
status
review_status
```

A file reference alone is not a Core-valid Document.

## 10.2 File Reference Is Not Document Automatically

Raw uploaded files, attachments and storage paths must become Documents only through Document Service.

## 10.3 Document Is Not Evidence Automatically

Document may link to Evidence.

Evidence Service owns proof purpose, source, claim relationship and evidence review.

## 10.4 Document Is Not Knowledge Automatically

Document may support Knowledge extraction.

Knowledge Service owns governed reference knowledge.

## 10.5 AI Draft or Extraction Is Not Approved Document

AI may draft, summarize or extract.

Document review status must distinguish AI-reviewed draft from human-approved use.

## 10.6 Version-Sensitive Documents Must Preserve Version

Documents affecting filing, ownership, official response, evidence or external communication must preserve version reference where applicable.

## 10.7 Document Changes Must Be Auditable

Document-sensitive operations must preserve actor, source, request context, file reference, version and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Trademark Service | Document may link to Trademark | Trademark owns protection object. |
| Matter Service | Document may belong to Matter | Matter owns execution container. |
| Order Service | Document may support Order | Order owns commercial request. |
| Communication Service | Document may originate from Communication | Communication owns message lifecycle. |
| Evidence Service | Document may support Evidence | Evidence owns proof layer. |
| Knowledge Service | Document may support Knowledge | Knowledge owns governed reference. |
| Policy Service | Controls access/confidentiality | Policy owns contextual constraints. |
| AI Agent Governance | AI may draft/summarize | Agent Contract governs AI use. |
| Audit Service | Records Document-sensitive action | Audit owns accountability trail. |
| Event Service | Records Document events | Event records occurrence. |

---

# 12. Event Usage

Document Service emits:

```text
DocumentCreated
DocumentUpdated
DocumentStatusChanged
DocumentFileLinked
DocumentVersionCreated
DocumentReviewRequired
DocumentReviewed
DocumentApproved
DocumentRejected
DocumentTrademarkLinked
DocumentMatterLinked
DocumentOrderLinked
DocumentCommunicationLinked
DocumentEvidenceLinked
DocumentArchived
DocumentReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- File link events must reference file reference without exposing content unnecessarily.
- Version events must preserve version reference.
- Review events must preserve reviewer/source where allowed.
- Evidence link events must reference registered Evidence ID.
- AI-generated draft/review events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 2 APIs:

```text
POST /documents
GET /documents/{id}
PATCH /documents/{id}
POST /documents/{id}/status
POST /documents/{id}/files
POST /documents/{id}/versions
POST /documents/{id}/review
POST /documents/{id}/trademarks
POST /documents/{id}/matters
POST /documents/{id}/orders
POST /documents/{id}/communications
POST /documents/{id}/evidence
POST /documents/reference/validate
```

API rules:

```text
- APIs must invoke Document Service operations.
- APIs must not treat raw upload as approved Document.
- APIs must not convert Document into Evidence or Knowledge directly.
- APIs must not expose restricted file content.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Document Service only under governed Agent Contracts.

Allowed AI use:

```text
classify document type for review
summarize document content if authorized
extract key fields for review
draft document from template for review
compare document versions
flag missing signature, date or required field
suggest evidence registration from document
suggest knowledge extraction from document
prepare document review notes
```

AI must not:

```text
approve Document for external or filing use without review where required
convert Document into Evidence automatically
convert Document into Knowledge automatically
alter official document content silently
treat OCR/extraction as professional truth
send document externally without Communication service and review
ignore confidentiality level or policy
```

AI Document use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Document Access Rule
Confidentiality Rule
Matter/Trademark Rule where applicable
Audit Rule
Human Review Rule for professional and external use
```

---

# 15. Validation Rules

Document Service must enforce:

```text
[ ] document_type is controlled.
[ ] status is controlled.
[ ] review_status is controlled.
[ ] createDocument requires title_reference.
[ ] createDocument produces stable immutable Document ID.
[ ] updateDocument does not mutate immutable ID.
[ ] changeDocumentStatus follows allowed lifecycle.
[ ] linkDocumentFile references valid file/storage reference.
[ ] validateDocumentReference rejects missing, rejected, archived or deleted-reference documents where not allowed.
[ ] raw file upload does not become approved Document automatically.
[ ] Document Service does not convert Document into Evidence automatically.
[ ] Document Service does not convert Document into Knowledge automatically.
[ ] AI-reviewed draft does not equal approved document.
[ ] Document Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Document Service should return controlled errors:

```text
DocumentNotFound
InvalidDocumentType
InvalidDocumentStatus
InvalidReviewStatus
InvalidDocumentTransition
DocumentTitleRequired
FileReferenceRequired
InvalidFileReference
InvalidVersionReference
ReviewRequired
DocumentRejected
ConfidentialityRestricted
TrademarkNotFound
MatterNotFound
OrderNotFound
CommunicationNotFound
EvidenceNotFound
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownDocumentError
```

Errors must be safe for product display and API consumption.

Restricted file content and confidential document material must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite document domain spec
cite document object spec
cite evidence and knowledge service specs where relevant
preserve Document / File boundary
preserve Document / Evidence boundary
preserve Document / Knowledge boundary
preserve Document / Communication boundary
implement only Phase 2 MVP operations unless task says otherwise
write tests for createDocument requiring document_type
write tests for createDocument requiring title_reference
write tests for controlled status and review_status
write tests preventing file upload from becoming approved Document
write tests preventing Document Service from converting Document into Evidence automatically
write tests preventing Document Service from converting Document into Knowledge automatically
write tests preventing AI-reviewed draft from becoming approved Document
write tests for event emission on mutation
```

Codex must not:

```text
invent full DMS or storage backend in Phase 2
treat file upload as approved Document
treat Document as Evidence
treat Document as Knowledge
allow AI extraction to overwrite official content silently
send external communications from Document Service
ignore confidentiality policy
allow product UI to redefine Document status
```

---

# 18. Acceptance Criteria

This Document Service Specification is accepted only if:

```text
[ ] It defines Document Service purpose.
[ ] It defines Document Service Core meaning.
[ ] It identifies Document Service as Professional Core Service.
[ ] It defines service operations.
[ ] It defines inputs and outputs.
[ ] It defines controlled values.
[ ] It defines service rules.
[ ] It defines relationships.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It includes Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Document Service specification. Establishes Document Service as professional artifact service, separates Document from raw files, Evidence, Knowledge, Communication and AI Output, and defines Phase 2 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
