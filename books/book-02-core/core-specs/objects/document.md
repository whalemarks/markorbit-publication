# Object Specification — Document

**Spec ID:** B02-OBJ-DOCUMENT  
**Spec Type:** Object  
**Object Name:** Document  
**Owning Domain:** Document  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/document.md  
**Related Object Specs:** core-specs/objects/document-file-reference.md; core-specs/objects/document-type.md; core-specs/objects/document-status.md; core-specs/objects/document-owner-reference.md; core-specs/objects/document-version.md; core-specs/objects/document-review-reference.md; core-specs/objects/evidence.md  
**Related Service Specs:** core-specs/services/document-registration-service.md; core-specs/services/document-file-reference-service.md; core-specs/services/document-version-service.md; core-specs/services/document-review-service.md; core-specs/services/document-status-service.md; core-specs/services/document-reference-validation-service.md  
**Related Event Specs:** core-specs/events/document-created.md; core-specs/events/document-updated.md; core-specs/events/document-file-linked.md; core-specs/events/document-version-created.md; core-specs/events/document-review-required.md; core-specs/events/document-status-changed.md; core-specs/events/document-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/document/document-contract.md; core-specs/contracts/document/document-file-reference-contract.md; core-specs/contracts/document/document-version-contract.md; core-specs/contracts/document/document-review-contract.md; core-specs/contracts/document/document-evidence-link-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Document object defines the Core-recognized professional artifact used to support trademark work, business execution, communication, filing preparation, official correspondence, client instructions, agent instructions and procedural records.

It exists so that Trademark, Brand, Jurisdiction, Classification, Evidence, Matter, Order, Customer, Communication, AI Agents, Services, APIs and product consumers can consistently reference documents without confusing them with raw uploaded files, evidence proof, knowledge sources, communication messages or AI-generated output.

Document is required before:

```text
document intake
file attachment governance
POA handling
application form handling
official notice handling
certificate handling
office action document handling
client instruction document handling
agent instruction document handling
document version tracking
document review workflow
document-to-evidence conversion
AI document summary or drafting support
```

---

# 2. Core Meaning

Document means:

```text
a Core-recognized professional artifact or file-backed record with type, status, source, version, owner/reference context, review state and governed relationships to trademark execution.
```

Document is not:

```text
raw uploaded file only
Evidence
Knowledge
Communication
AI Output
Trademark
Matter
Order
official truth by itself
legal conclusion
```

Document answers:

```text
What professional artifact is being referenced?
Which file or source supports it?
Which type of document is it?
Which Trademark, Matter, Order, Customer, Jurisdiction or Communication does it relate to?
Which version and status apply?
Has it been reviewed, accepted, rejected or archived?
Can it become Evidence?
Can AI summarize, classify or draft it?
What audit trace is required?
```

---

# 3. Object Category

Document is a Professional Object owned by the Document Domain.

It is the professional artifact layer.

It may reference files, communications, trademarks, matters or evidence, but it must not absorb their meanings.

Evidence is the proof layer.

Knowledge is the governed reference layer.

Communication is the message/conversation layer.

---

# 4. Architectural Position

Document sits between professional work and supporting materials.

```text
Trademark / Matter creates need
        ↓
Document captures artifact or formal material
        ↓
Review determines professional usability
        ↓
Evidence may register proof purpose where needed
        ↓
Workflow and Task coordinate handling
        ↓
Event and Audit preserve trace
```

Document manages artifact identity and lifecycle.

It does not prove facts by itself.

It does not become Evidence automatically.

---

# 5. Scope

The Document object includes:

```text
document id
document type
document title/reference
document status
document file reference
document source reference
document version
document owner/reference context
document review status
document language reference
document jurisdiction reference
document trademark reference
document matter reference
document order reference
document communication reference
document evidence link reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
document id
document type
title/reference
status
file reference
source reference
version reference
review status
jurisdiction reference
trademark reference
matter reference
order reference
communication reference
evidence link reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Document ID. |
| document_type | enum | Yes | Yes | Controlled document type. |
| title_reference | string | Yes | Yes | Human-readable title/reference. |
| status | enum | Yes | Yes | Controlled Document status. |
| review_status | enum | Yes | Yes | Controlled professional review state. |
| file_reference_id | string | No | Yes | File/blob/storage reference; not Document by itself. |
| source_reference | string | No | Yes | Intake/import/official/source reference. |
| version_reference | string | No | Yes | Version identifier/reference. |
| parent_document_id | string | No | Partial | Parent/original document reference. |
| jurisdiction_reference_id | string | No | Yes | Jurisdiction context where applicable. |
| trademark_reference_id | string | No | Yes | Related Trademark reference. |
| brand_reference_id | string | No | Partial | Related Brand reference. |
| matter_reference_id | string | No | Yes | Related Matter reference. |
| order_reference_id | string | No | Yes | Related Order reference. |
| customer_reference_id | string | No | Partial | Related Customer reference. |
| communication_reference_id | string | No | Yes | Related Communication reference. |
| evidence_reference_ids | array | No | Partial | Evidence links where registered. |
| language_reference | string | No | Partial | Document language reference. |
| confidentiality_level | enum | No | Partial | Data handling level. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 document_type

MVP controlled values:

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

## 7.2 status

MVP controlled values:

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

## 7.3 review_status

MVP controlled values:

```text
Unreviewed
ReviewRequired
HumanReviewed
AIReviewedDraft
ApprovedForUse
Rejected
NeedsRevision
```

## 7.4 confidentiality_level

Suggested controlled values:

```text
Public
Internal
Confidential
HighlyConfidential
Restricted
Unknown
```

---

# 8. Object Rules

## 8.1 Document Requires Type and Title

Every Document must define:

```text
document_type
title_reference
status
review_status
```

A file without these fields is not a Core Document.

## 8.2 File Reference Is Not Document by Itself

A raw uploaded file becomes a Document only through Document Registration Service.

Storage path, attachment or image upload alone is not a governed Document.

## 8.3 Document Is Not Evidence Automatically

A Document may support Evidence.

It becomes Evidence only when registered with proof purpose, source and review through Evidence services.

## 8.4 Document Is Not Knowledge Automatically

A Document may contain knowledge.

It becomes Knowledge only when registered, scoped, sourced and validated through Knowledge services.

## 8.5 Document Review Must Be Explicit

Professional use of Document should distinguish:

```text
received
review-required
reviewed
approved-for-use
rejected
filed/issued
```

## 8.6 Document Must Be Version-Aware

Documents that may affect filing, response, ownership, evidence or official record must preserve version references.

## 8.7 Document Must Be Auditable

Document-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
document creation
file linking
document type update
document status change
document review
document approval/rejection
document version creation
document evidence link
document deletion/reference archival
AI document summary or drafting
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Trademark | Document may support Trademark | Trademark remains protection object. |
| Brand | Document may reference Brand | Brand remains commercial identity. |
| Jurisdiction | Document may be jurisdiction-specific | Jurisdiction remains procedural context. |
| Classification | Document may contain goods/services wording | Classification owns scope. |
| Evidence | Document may become evidence through service | Evidence remains proof layer. |
| Knowledge | Document may support Knowledge extraction | Knowledge remains governed reference. |
| Matter | Document may belong to Matter | Matter remains execution container. |
| Order | Document may support Order fulfillment | Order remains commercial service request. |
| Customer | Document may be provided by Customer | Customer remains demand-side party. |
| Communication | Document may be attached to Communication | Communication remains message lifecycle. |
| Task | Task may request/review Document | Task remains work unit. |
| AI Output | AI may draft/summarize Document | AI Output is not approved Document by default. |
| Audit Record | Audit may reference Document | Audit remains accountability system. |

---

# 10. Lifecycle

Document lifecycle states:

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

Lifecycle rules:

```text
Draft → Uploaded
Received → ReviewRequired
Uploaded → ReviewRequired
ReviewRequired → Reviewed
Reviewed → Approved
Reviewed → Rejected
Approved → Filed
Approved → Issued
Rejected → Archived
Filed → Archived
Issued → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Uploaded → Approved without review where policy requires review
Rejected → Filed without revision/review
Archived → Filed without restoration/review
DeletedReferenceOnly → Active state
```

---

# 11. Service Usage

Document object is created and managed through:

```text
Document Registration Service
Document File Reference Service
Document Version Service
Document Review Service
Document Status Service
Document Evidence Link Service
Document Reference Validation Service
Document Audit Reference Service
```

Service rules:

```text
- Services must validate document_type.
- Services must validate status and review_status.
- Services must validate file reference where file-backed.
- Services must emit events for mutating actions.
- Services must not convert Document into Evidence without Evidence service.
- Services must not convert Document into Knowledge without Knowledge service.
- AI-generated drafts must remain Draft or ReviewRequired until reviewed.
```

---

# 12. Event Usage

Document object emits or participates in:

```text
DocumentCreated
DocumentUpdated
DocumentFileLinked
DocumentVersionCreated
DocumentStatusChanged
DocumentReviewRequired
DocumentReviewed
DocumentApproved
DocumentRejected
DocumentFiled
DocumentIssued
DocumentEvidenceLinked
DocumentArchived
DocumentReferenceValidated
```

Event rules:

```text
- Document events must reference Document ID.
- File events must reference file reference, not expose raw file content unnecessarily.
- Review events must preserve reviewer/source where allowed.
- Evidence link events must reference Evidence ID.
- AI-generated document events must identify AI source.
```

---

# 13. API Usage

Potential Phase 2 APIs:

```text
POST /documents
GET /documents/{id}
PATCH /documents/{id}
POST /documents/{id}/files
POST /documents/{id}/versions
POST /documents/{id}/review
POST /documents/{id}/status
POST /documents/{id}/evidence-links
POST /documents/reference/validate
```

API rules:

```text
- APIs must invoke Document Services.
- APIs must not treat raw file upload as approved Document.
- APIs must not convert Document into Evidence or Knowledge directly.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Document only under governed Agent Contracts.

Allowed AI use:

```text
classify document type for review
summarize document content if authorized
extract key fields for review
draft document from template
compare document versions
flag missing signature or date
suggest evidence registration from document
suggest knowledge extraction from document
```

AI must not:

```text
approve Document for use without review where required
convert Document into Evidence automatically
convert Document into Knowledge automatically
alter official document content silently
treat OCR/extraction as professional truth
send document externally without Communication service and review
ignore confidentiality level
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
Audit Rule
Human Review Rule for professional and external use
```

---

# 15. Validation Rules

Document object must pass:

```text
[ ] id is present and immutable.
[ ] document_type is controlled.
[ ] title_reference is present.
[ ] status is controlled.
[ ] review_status is controlled.
[ ] Raw file reference alone is not Document.
[ ] Document does not become Evidence automatically.
[ ] Document does not become Knowledge automatically.
[ ] Version-sensitive documents preserve version reference.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite document domain spec
preserve Document / Evidence boundary
preserve Document / Knowledge boundary
preserve Document / Communication boundary
preserve Document / AI Output boundary
implement only MVP fields unless task says otherwise
write tests for required document_type
write tests for required title_reference
write tests for controlled status
write tests for controlled review_status
write tests preventing file upload from becoming approved Document
write tests preventing Document from becoming Evidence automatically
write tests preventing Document from becoming Knowledge automatically
write tests for event emission on mutation
```

Codex must not:

```text
invent full document management system in MVP
treat raw file upload as approved Document
treat Document as Evidence automatically
treat Document as Knowledge automatically
allow AI extraction to overwrite official content silently
ignore confidentiality level
allow product UI to redefine Document status
```

---

# 17. Acceptance Criteria

This Document Object Specification is accepted only if:

```text
[ ] It defines Document purpose.
[ ] It defines Document Core meaning.
[ ] It identifies Document as Professional Object.
[ ] It defines fields.
[ ] It defines controlled values.
[ ] It defines object rules.
[ ] It defines relationships.
[ ] It defines lifecycle.
[ ] It defines service usage.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It includes Codex implementation notes.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Document object specification. Establishes Document as professional artifact object, separates Document from raw files, Evidence, Knowledge, Communication and AI Output, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
