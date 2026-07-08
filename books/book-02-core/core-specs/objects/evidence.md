# Object Specification — Evidence

**Spec ID:** B02-OBJ-EVIDENCE  
**Spec Type:** Object  
**Object Name:** Evidence  
**Owning Domain:** Evidence  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/evidence.md  
**Related Object Specs:** core-specs/objects/document.md; core-specs/objects/evidence-source.md; core-specs/objects/evidence-purpose.md; core-specs/objects/evidence-status.md; core-specs/objects/evidence-review-reference.md; core-specs/objects/evidence-claim-link.md; core-specs/objects/evidence-use-reference.md  
**Related Service Specs:** core-specs/services/evidence-registration-service.md; core-specs/services/evidence-source-service.md; core-specs/services/evidence-review-service.md; core-specs/services/evidence-validation-service.md; core-specs/services/evidence-document-link-service.md; core-specs/services/evidence-reference-validation-service.md  
**Related Event Specs:** core-specs/events/evidence-created.md; core-specs/events/evidence-updated.md; core-specs/events/evidence-source-linked.md; core-specs/events/evidence-document-linked.md; core-specs/events/evidence-review-required.md; core-specs/events/evidence-validated.md; core-specs/events/evidence-status-changed.md; core-specs/events/evidence-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/evidence/evidence-contract.md; core-specs/contracts/evidence/evidence-source-contract.md; core-specs/contracts/evidence/evidence-purpose-contract.md; core-specs/contracts/evidence/evidence-review-contract.md; core-specs/contracts/evidence/evidence-document-link-contract.md; core-specs/contracts/evidence/evidence-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Evidence object defines the Core-recognized proof material used to support trademark use, ownership, priority, distinctiveness, reputation, response arguments, opposition, cancellation, renewal, declaration, enforcement or other professional claims.

It exists so that Trademark, Document, Matter, Order, Classification, Jurisdiction, Knowledge, Communication, AI Agents, Services, APIs and product consumers can consistently reference proof materials without confusing them with raw files, documents, knowledge references, AI outputs or unreviewed screenshots.

Evidence is required before:

```text
use evidence collection
ownership proof review
priority proof handling
office action response support
opposition/cancellation proof package
renewal or declaration use evidence review
evidence-to-goods/services matching
evidence-to-jurisdiction matching
document-to-evidence registration
AI evidence extraction or review support
professional evidence package preparation
```

---

# 2. Core Meaning

Evidence means:

```text
a Core-recognized proof object with defined source, purpose, claim relationship, review state, status and governed links to documents, trademarks, goods/services, jurisdiction and professional matters.
```

Evidence is not:

```text
raw uploaded file
Document
Knowledge
Communication
AI Output
screenshot by itself
marketing material by itself
legal conclusion
professional final decision
claim itself
```

Evidence answers:

```text
What fact, claim, use or legal/procedural point does this material support?
Where did the material come from?
Which Document, file, communication or source supports it?
Which Trademark, Brand, Classification, Jurisdiction or Matter does it relate to?
Has it been reviewed, accepted, rejected or marked insufficient?
Can AI extract or summarize it?
What audit trace is required?
```

---

# 3. Object Category

Evidence is a Professional Object owned by the Evidence Domain.

It is the proof layer.

Document is the artifact layer.

Knowledge is the governed reference layer.

Communication is the message/conversation layer.

Evidence may link to these objects, but it must not be collapsed into any of them.

---

# 4. Architectural Position

Evidence sits after Document and before professional argument or filing package.

```text
Document / Communication / Source provides material
        ↓
Evidence registers proof purpose and source
        ↓
Review determines professional sufficiency
        ↓
Matter uses Evidence in procedure or argument
        ↓
Event and Audit preserve trace
```

Evidence defines proof purpose.

It does not prove automatically.

It does not become final legal argument by itself.

---

# 5. Scope

The Evidence object includes:

```text
evidence id
evidence type
evidence purpose
evidence status
evidence review status
evidence source reference
document reference
file reference
claim reference
trademark reference
brand reference
classification reference
goods/services item reference
jurisdiction reference
matter reference
order reference
date range/use date reference
source reliability reference
language reference
translation reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
evidence id
evidence type
evidence purpose
evidence status
review status
source reference
document reference
trademark reference
brand reference
classification reference
jurisdiction reference
matter reference
claim reference
date/use reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Evidence ID. |
| evidence_type | enum | Yes | Yes | Controlled evidence type. |
| evidence_purpose | enum | Yes | Yes | Purpose or claim category. |
| status | enum | Yes | Yes | Controlled Evidence status. |
| review_status | enum | Yes | Yes | Controlled professional review state. |
| source_reference_id | string | Yes | Yes | Evidence source reference is required. |
| document_reference_id | string | No | Yes | Related Document reference where applicable. |
| file_reference_id | string | No | Partial | File reference where not represented by Document. |
| claim_reference_id | string | No | Yes | Claim/fact/procedural point supported. |
| trademark_reference_id | string | No | Yes | Related Trademark reference. |
| brand_reference_id | string | No | Yes | Related Brand reference. |
| classification_reference_id | string | No | Yes | Related Classification reference. |
| goods_services_item_references | array | No | Yes | Related goods/services item references. |
| jurisdiction_reference_id | string | No | Yes | Jurisdiction context where applicable. |
| matter_reference_id | string | No | Yes | Related Matter reference. |
| order_reference_id | string | No | Partial | Related Order reference. |
| evidence_date | date | No | Yes | Evidence date where known. |
| date_range_start | date | No | Partial | Start date for use period where applicable. |
| date_range_end | date | No | Partial | End date for use period where applicable. |
| source_reliability | enum | No | Partial | Reliability indicator. |
| language_reference | string | No | Partial | Evidence language reference. |
| translation_reference_id | string | No | Partial | Translation Document reference where applicable. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 evidence_type

MVP controlled values:

```text
UseEvidence
OwnershipEvidence
PriorityEvidence
DistinctivenessEvidence
ReputationEvidence
SalesEvidence
AdvertisingEvidence
OnlineUseEvidence
PackagingEvidence
ProductEvidence
OfficialRecordEvidence
CommunicationEvidence
Other
Unknown
```

## 7.2 evidence_purpose

MVP controlled values:

```text
ProofOfUse
ProofOfOwnership
ProofOfPriority
ProofOfDistinctiveness
ProofOfReputation
ProofOfGoodsServicesUse
ProofOfJurisdictionUse
ResponseSupport
OppositionSupport
CancellationSupport
RenewalSupport
DeclarationSupport
GeneralSupport
Unknown
```

## 7.3 status

MVP controlled values:

```text
Draft
Collected
ReviewRequired
Reviewed
Accepted
Rejected
Insufficient
Filed
Archived
DeletedReferenceOnly
```

## 7.4 review_status

MVP controlled values:

```text
Unreviewed
AIReviewedDraft
HumanReviewed
AcceptedForUse
Rejected
NeedsMoreEvidence
NeedsTranslation
NeedsSourceVerification
```

## 7.5 source_reliability

Suggested controlled values:

```text
Official
ClientProvided
AgentProvided
PublicWeb
Marketplace
SocialMedia
InternalRecord
ThirdPartyReport
Unknown
```

---

# 8. Object Rules

## 8.1 Evidence Requires Source

Every Evidence object must reference a source.

A file, screenshot or document without source context is not Core-valid Evidence.

## 8.2 Evidence Requires Purpose

Every Evidence object must define evidence purpose or claim relationship.

Material without proof purpose remains Document or raw material, not Evidence.

## 8.3 Evidence Is Not Document Automatically

Document may support Evidence.

A Document becomes Evidence only through Evidence Registration Service with purpose, source and review context.

## 8.4 Evidence Is Not Knowledge

Evidence supports factual/procedural proof.

Knowledge provides governed reference.

Evidence must not be used as generalized Knowledge without Knowledge registration and validation.

## 8.5 AI Review Is Not Professional Acceptance

AI may extract, summarize or flag Evidence.

AI review does not equal professional acceptance.

## 8.6 Evidence Must Preserve Claim Link

Evidence should identify what claim, fact, goods/services item, use date, ownership point or procedural argument it supports.

## 8.7 Evidence Must Be Auditable

Evidence-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
evidence creation
source linking
document linking
purpose update
claim link update
goods/services link update
review
acceptance/rejection
translation link
filing use
AI evidence extraction
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Document | Evidence may link to Document | Document remains artifact. |
| Trademark | Evidence may support Trademark | Trademark remains protection object. |
| Brand | Evidence may support Brand use or identity | Brand remains commercial identity. |
| Classification | Evidence may support goods/services use | Classification remains scope object. |
| Goods/Services Item | Evidence may link to item | Item remains classification element. |
| Jurisdiction | Evidence may be jurisdiction-specific | Jurisdiction remains procedural context. |
| Matter | Evidence may be used in Matter | Matter remains execution container. |
| Order | Evidence may support Order fulfillment | Order remains commercial request. |
| Communication | Evidence may be derived from communication | Communication remains message lifecycle. |
| Knowledge | Knowledge may guide evidence review | Knowledge remains reference. |
| Policy | Policy may constrain evidence use | Policy remains contextual rule. |
| AI Output | AI may extract/summarize Evidence | AI Output is not accepted evidence. |
| Audit Record | Audit may reference Evidence | Audit remains accountability system. |

---

# 10. Lifecycle

Evidence lifecycle states:

```text
Draft
Collected
ReviewRequired
Reviewed
Accepted
Rejected
Insufficient
Filed
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → Collected
Collected → ReviewRequired
ReviewRequired → Reviewed
Reviewed → Accepted
Reviewed → Rejected
Reviewed → Insufficient
Insufficient → ReviewRequired
Accepted → Filed
Accepted → Archived
Rejected → Archived
Filed → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Collected → Accepted without review where policy requires review
AIReviewedDraft → AcceptedForUse without human review where required
Rejected → Filed without new review
Archived → Filed without restoration/review
DeletedReferenceOnly → Active state
```

---

# 11. Service Usage

Evidence object is created and managed through:

```text
Evidence Registration Service
Evidence Source Service
Evidence Document Link Service
Evidence Review Service
Evidence Validation Service
Evidence Claim Link Service
Evidence Translation Link Service
Evidence Reference Validation Service
Evidence Audit Reference Service
```

Service rules:

```text
- Services must validate evidence_type.
- Services must validate evidence_purpose.
- Services must require source_reference_id.
- Services must validate status and review_status.
- Services must emit events for mutating actions.
- Services must not convert Document into Evidence without explicit registration.
- AI extraction must remain draft/review-required until reviewed where required.
```

---

# 12. Event Usage

Evidence object emits or participates in:

```text
EvidenceCreated
EvidenceUpdated
EvidenceSourceLinked
EvidenceDocumentLinked
EvidenceClaimLinked
EvidenceGoodsServicesLinked
EvidenceReviewRequired
EvidenceReviewed
EvidenceAccepted
EvidenceRejected
EvidenceMarkedInsufficient
EvidenceFiled
EvidenceArchived
EvidenceReferenceValidated
```

Event rules:

```text
- Evidence events must reference Evidence ID.
- Source events must preserve source reference.
- Review events must preserve reviewer/source where allowed.
- Claim link events must reference claim or purpose.
- AI-generated extraction events must identify AI source.
- Events must not expose protected evidence content unnecessarily.
```

---

# 13. API Usage

Potential Phase 2 APIs:

```text
POST /evidence
GET /evidence/{id}
PATCH /evidence/{id}
POST /evidence/{id}/sources
POST /evidence/{id}/documents
POST /evidence/{id}/claims
POST /evidence/{id}/goods-services
POST /evidence/{id}/review
POST /evidence/{id}/status
POST /evidence/reference/validate
```

API rules:

```text
- APIs must invoke Evidence Services.
- APIs must require source and purpose.
- APIs must not treat Document or file upload as accepted Evidence.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Evidence only under governed Agent Contracts.

Allowed AI use:

```text
extract candidate evidence facts
summarize evidence material if authorized
suggest evidence purpose
map evidence to goods/services items
identify missing source or date
flag weak or insufficient evidence
suggest translation need
prepare evidence review notes for human review
```

AI must not:

```text
accept Evidence for filing without human review where required
treat screenshot/file as Evidence without source and purpose
alter evidence content silently
invent source, date or use facts
treat AI extraction as professional proof
file evidence directly
ignore confidentiality or data sensitivity
```

AI Evidence use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Evidence Access Rule
Document Access Rule where applicable
Confidentiality Rule
Audit Rule
Human Review Rule for professional use
```

---

# 15. Validation Rules

Evidence object must pass:

```text
[ ] id is present and immutable.
[ ] evidence_type is controlled.
[ ] evidence_purpose is controlled.
[ ] source_reference_id is present.
[ ] status is controlled.
[ ] review_status is controlled.
[ ] Evidence has proof purpose or claim link.
[ ] Evidence does not become Document automatically.
[ ] Document/file does not become Evidence automatically.
[ ] AI review does not equal professional acceptance.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite evidence domain spec
cite document object spec
preserve Evidence / Document boundary
preserve Evidence / Knowledge boundary
preserve Evidence / Communication boundary
preserve Evidence / AI Output boundary
implement only MVP fields unless task says otherwise
write tests for required source_reference_id
write tests for required evidence_purpose
write tests for controlled evidence_type
write tests for controlled status
write tests for controlled review_status
write tests preventing file/document from becoming Evidence automatically
write tests preventing AI review from becoming professional acceptance
write tests for event emission on mutation
```

Codex must not:

```text
invent full evidence litigation system in MVP
treat uploaded file or screenshot as Evidence automatically
accept Evidence without source and purpose
allow AI extraction to overwrite evidence facts silently
treat AI review as human acceptance
file evidence directly from Evidence service
allow product UI to redefine Evidence status
```

---

# 17. Acceptance Criteria

This Evidence Object Specification is accepted only if:

```text
[ ] It defines Evidence purpose.
[ ] It defines Evidence Core meaning.
[ ] It identifies Evidence as Professional Object.
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
| 0.1.0 | Draft | Initial Evidence object specification. Establishes Evidence as proof object, separates Evidence from Document, Knowledge, Communication and AI Output, requires source and purpose, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
