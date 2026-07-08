# Service Specification — Evidence Service

**Spec ID:** B02-SVC-EVIDENCE-SERVICE  
**Spec Type:** Service  
**Service Name:** Evidence Service  
**Owning Domain:** Evidence  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/evidence.md  
**Related Object Specs:** core-specs/objects/evidence.md; core-specs/objects/document.md; core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/matter.md; core-specs/objects/classification.md  
**Related Service Specs:** core-specs/services/document-service.md; core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/classification-service.md; core-specs/services/matter-service.md; core-specs/services/knowledge-service.md  
**Related Event Specs:** core-specs/events/evidence-created.md; core-specs/events/evidence-updated.md; core-specs/events/evidence-status-changed.md; core-specs/events/evidence-source-linked.md; core-specs/events/evidence-claim-linked.md; core-specs/events/evidence-reviewed.md; core-specs/events/evidence-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/evidence/evidence-contract.md; core-specs/contracts/evidence/evidence-reference-contract.md; core-specs/contracts/evidence/evidence-source-contract.md; core-specs/contracts/evidence/evidence-claim-contract.md; core-specs/contracts/evidence/evidence-review-contract.md; core-specs/contracts/evidence/evidence-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Evidence Service defines the Core service boundary for creating, updating, validating, reviewing, linking and managing Evidence objects.

It exists so that Trademark, Brand, Classification, Document, Matter, Order, Knowledge, AI Agents, APIs and product consumers can consistently reference proof materials and proof purposes without confusing Evidence with Document, raw file, screenshot, Communication attachment, Knowledge, AI extraction or professional conclusion.

Evidence Service is required before:

```text
use evidence registration
proof-of-use material handling
ownership evidence registration
priority evidence handling
distinctiveness evidence handling
opposition/cancellation evidence handling
goods/services evidence mapping
document-to-evidence linkage
evidence review and approval
AI-assisted evidence extraction and summary
audit trace for evidence-sensitive actions
```

---

# 2. Core Meaning

Evidence Service means:

```text
the Core service that manages proof-layer records, including source, purpose, claim relationship, review state, status, scope, version and governed lifecycle.
```

Evidence Service does not mean:

```text
Document Service
file storage service
screenshot repository
Knowledge Service
legal conclusion service
official truth service
AI proof validator by itself
litigation management system
```

Evidence Service answers:

```text
Does this Evidence exist?
What claim, purpose or issue does it support?
Which source Document, file, Communication or external source supports it?
Which Brand, Trademark, Classification, Matter or Jurisdiction does it relate to?
Has it been reviewed, approved, rejected or marked insufficient?
Can another domain safely reference this Evidence?
What audit trace is required?
```

---

# 3. Service Category

Evidence Service is a Professional Core Service.

It manages the proof layer.

It does not manage raw file storage.

It does not replace Document or Knowledge.

It does not make final legal conclusions.

---

# 4. Architectural Position

Evidence Service sits after source artifacts and before professional proof use.

```text
Document / File / Screenshot / Communication source exists
        ↓
Evidence Service registers proof purpose and source
        ↓
Review determines sufficiency or usability
        ↓
Matter / Trademark / Classification consume Evidence reference
        ↓
Professional judgment determines legal argument or submission
        ↓
Event and Audit preserve trace
```

Document is artifact.

Evidence is proof.

Knowledge is governed reference.

Professional judgment decides use.

---

# 5. Scope

Evidence Service includes:

```text
evidence creation
evidence update
evidence status management
evidence source linkage
evidence claim linkage
evidence review management
evidence scope linkage
evidence document linkage
evidence trademark/brand/classification linkage
evidence reference validation
evidence audit trace
evidence event emission
```

MVP scope includes:

```text
create evidence
get evidence
update evidence metadata
change evidence status
link evidence source
link evidence to document
link evidence to trademark
link evidence to brand
link evidence to classification
record evidence review
validate evidence reference
emit evidence events
```

Deferred scope includes:

```text
full evidence bundle management
litigation evidence chronology
automatic evidence sufficiency scoring
advanced OCR/extraction pipeline
forensic authenticity verification
automatic proof-of-use decisioning
jurisdiction-specific evidence rule engine
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createEvidence | Create Evidence object | Yes | EvidenceCreated |
| getEvidence | Retrieve Evidence by ID | Yes | No |
| updateEvidence | Update governed metadata | Yes | EvidenceUpdated |
| changeEvidenceStatus | Change Evidence lifecycle status | Yes | EvidenceStatusChanged |
| linkEvidenceSource | Link source Document/file/Communication/source | Yes | EvidenceSourceLinked |
| unlinkEvidenceSource | Remove source link | Partial | EvidenceSourceUnlinked |
| linkEvidenceClaim | Link Evidence to claim/purpose/issue | Yes | EvidenceClaimLinked |
| linkEvidenceDocument | Link Evidence to Document | Yes | EvidenceDocumentLinked |
| linkEvidenceTrademark | Link Evidence to Trademark | Yes | EvidenceTrademarkLinked |
| linkEvidenceBrand | Link Evidence to Brand | Partial | EvidenceBrandLinked |
| linkEvidenceClassification | Link Evidence to Classification item/scope | Partial | EvidenceClassificationLinked |
| reviewEvidence | Record evidence review result | Yes | EvidenceReviewed |
| requireEvidenceReview | Mark review required | Yes | EvidenceReviewRequired |
| validateEvidenceReference | Validate whether Evidence can be referenced | Yes | EvidenceReferenceValidated |
| archiveEvidence | Archive Evidence reference | Partial | EvidenceArchived |

---

# 7. Inputs

Evidence Service accepts:

```text
evidence_type
evidence_purpose
claim_reference
status
review_status
source_type
source_reference_id
document_reference_id
trademark_reference_id
brand_reference_id
classification_reference_id
classification_item_reference_id
matter_reference_id
jurisdiction_reference_id
date_range_reference
language_reference
confidentiality_level
metadata
actor_context
request_context
```

Required for creation:

```text
evidence_type
evidence_purpose
source_type
source_reference_id
status
review_status
actor_context
```

Required for source linkage:

```text
evidence_reference_id
source_type
source_reference_id
actor_context
```

Required for review:

```text
evidence_reference_id
review_status
review_note_reference
actor_context
```

Required for validation:

```text
evidence_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Evidence Service returns:

```text
Evidence object
Evidence reference
Evidence validation result
Evidence source link result
Evidence claim link result
Evidence review result
Evidence status result
Evidence event reference
error result
```

Validation output must include:

```text
is_valid
evidence_reference_id
evidence_type
evidence_purpose
status
review_status
source_type
reason_code
review_required
sufficiency_hint where applicable
confidentiality_hint where applicable
policy_hint where applicable
```

Validation output must not expose restricted evidence content, confidential customer material or sensitive proof strategy unnecessarily.

---

# 9. Controlled Values

## 9.1 evidence_type

```text
UseEvidence
OwnershipEvidence
PriorityEvidence
DistinctivenessEvidence
SalesEvidence
AdvertisingEvidence
WebsiteEvidence
MarketplaceEvidence
SocialMediaEvidence
OfficialRecordEvidence
CorrespondenceEvidence
Other
Unknown
```

## 9.2 evidence_purpose

```text
ProofOfUse
OwnershipProof
PriorityProof
DistinctivenessProof
OppositionSupport
CancellationSupport
OfficeActionResponseSupport
ClassificationSupport
RenewalSupport
AssignmentSupport
ChangeSupport
GeneralReference
Unknown
```

## 9.3 status

```text
Draft
Collected
ReviewRequired
Reviewed
ApprovedForUse
Insufficient
Rejected
Submitted
Archived
DeletedReferenceOnly
```

## 9.4 review_status

```text
Unreviewed
AIReviewedDraft
HumanReviewed
ApprovedForUse
Insufficient
Rejected
NeedsSupplement
```

## 9.5 source_type

```text
Document
File
Screenshot
Communication
OfficialSource
Website
Marketplace
ClientProvided
AgentProvided
AIExtractionDraft
Unknown
```

## 9.6 validation_result

```text
Valid
Invalid
NotFound
ReviewRequired
Insufficient
Rejected
Archived
ConfidentialityRestricted
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Evidence Requires Source and Purpose

Evidence creation must require:

```text
source_type
source_reference_id
evidence_purpose
```

A file, screenshot or Document is not Evidence unless proof purpose and source are registered.

## 10.2 Evidence Is Not Document

Evidence may reference Document.

Document Service owns artifact lifecycle.

Evidence Service owns proof purpose and proof relationship.

## 10.3 Evidence Is Not Knowledge

Evidence may support Knowledge or legal argument.

Knowledge Service owns governed reference knowledge.

## 10.4 Evidence Is Not Professional Conclusion

Evidence may be approved for use.

Whether evidence is legally sufficient or strategically persuasive requires professional review where applicable.

## 10.5 AI Extraction Is Not Approved Evidence

AI may extract, summarize or classify candidate evidence.

AI output becomes Evidence only through Evidence Service and review where required.

## 10.6 Evidence Must Preserve Claim Relationship

Evidence must identify what claim, purpose, issue, item, class, mark, jurisdiction or matter it supports where applicable.

## 10.7 Evidence Changes Must Be Auditable

Evidence-sensitive operations must preserve actor, source, request context, review status, version/source trace and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Document Service | Evidence may reference Document | Document owns artifact lifecycle. |
| Trademark Service | Evidence may support Trademark | Trademark owns protection object. |
| Brand Service | Evidence may support Brand use/ownership | Brand owns commercial identity. |
| Classification Service | Evidence may support item scope | Classification owns goods/services scope. |
| Matter Service | Evidence may support Matter work | Matter owns execution container. |
| Order Service | Evidence may support Order request | Order owns commercial request. |
| Knowledge Service | Evidence may support Knowledge | Knowledge owns governed reference. |
| Policy Service | Controls access/confidentiality | Policy owns contextual constraints. |
| AI Agent Governance | AI may extract/summarize | Agent Contract governs AI use. |
| Audit Service | Records Evidence-sensitive action | Audit owns accountability trail. |
| Event Service | Records Evidence events | Event records occurrence. |

---

# 12. Event Usage

Evidence Service emits:

```text
EvidenceCreated
EvidenceUpdated
EvidenceStatusChanged
EvidenceSourceLinked
EvidenceSourceUnlinked
EvidenceClaimLinked
EvidenceDocumentLinked
EvidenceTrademarkLinked
EvidenceBrandLinked
EvidenceClassificationLinked
EvidenceReviewRequired
EvidenceReviewed
EvidenceApprovedForUse
EvidenceMarkedInsufficient
EvidenceRejected
EvidenceSubmitted
EvidenceArchived
EvidenceReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Source link events must reference source type and source ID.
- Review events must preserve reviewer/source where allowed.
- Insufficient or rejected evidence events must preserve reason code where allowed.
- AI extraction/review events must identify AI source where applicable.
- Events must not expose restricted evidence content unnecessarily.
```

---

# 13. API Usage

Potential Phase 2 APIs:

```text
POST /evidence
GET /evidence/{id}
PATCH /evidence/{id}
POST /evidence/{id}/status
POST /evidence/{id}/sources
DELETE /evidence/{id}/sources/{sourceId}
POST /evidence/{id}/claims
POST /evidence/{id}/documents
POST /evidence/{id}/trademarks
POST /evidence/{id}/brands
POST /evidence/{id}/classifications
POST /evidence/{id}/review
POST /evidence/reference/validate
```

API rules:

```text
- APIs must invoke Evidence Service operations.
- APIs must not treat raw files, screenshots or Documents as Evidence automatically.
- APIs must not mark AI extraction as approved Evidence automatically.
- APIs must not make final legal sufficiency conclusion.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Evidence Service only under governed Agent Contracts.

Allowed AI use:

```text
identify candidate evidence from authorized documents
summarize evidence source
classify evidence type for review
map evidence to goods/services items for review
identify missing proof purpose
flag weak or incomplete evidence for review
draft evidence review notes
suggest supplement request
```

AI must not:

```text
approve Evidence for use without governed review where required
treat screenshot/file/document as Evidence automatically
make final legal sufficiency conclusion
fabricate source, date, use, sales or ownership facts
alter evidence source silently
submit Evidence externally without authorized workflow
ignore confidentiality level or policy
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
Trademark/Classification Rule where applicable
Confidentiality Rule
Audit Rule
Human Review Rule for legal sufficiency, submission or external use
```

---

# 15. Validation Rules

Evidence Service must enforce:

```text
[ ] evidence_type is controlled.
[ ] evidence_purpose is controlled.
[ ] status is controlled.
[ ] review_status is controlled.
[ ] source_type is controlled.
[ ] createEvidence requires evidence_purpose.
[ ] createEvidence requires source_type.
[ ] createEvidence requires source_reference_id.
[ ] createEvidence produces stable immutable Evidence ID.
[ ] updateEvidence does not mutate immutable ID.
[ ] changeEvidenceStatus follows allowed lifecycle.
[ ] validateEvidenceReference rejects missing, insufficient, rejected, archived or deleted-reference evidence where not allowed.
[ ] raw files/screenshots/documents do not become Evidence automatically.
[ ] AI extraction does not become approved Evidence automatically.
[ ] Evidence Service does not make final legal sufficiency conclusion.
[ ] Evidence Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Evidence Service should return controlled errors:

```text
EvidenceNotFound
InvalidEvidenceType
InvalidEvidencePurpose
InvalidEvidenceStatus
InvalidReviewStatus
InvalidSourceType
InvalidEvidenceTransition
EvidencePurposeRequired
EvidenceSourceRequired
InvalidSourceReference
DocumentNotFound
TrademarkNotFound
BrandNotFound
ClassificationNotFound
MatterNotFound
ReviewRequired
EvidenceInsufficient
EvidenceRejected
ConfidentialityRestricted
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownEvidenceError
```

Errors must be safe for product display and API consumption.

Restricted evidence content, confidential customer material and proof strategy must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite evidence domain spec
cite evidence object spec
cite document service/object specs where relevant
preserve Evidence / Document boundary
preserve Evidence / Knowledge boundary
preserve Evidence / Professional Conclusion boundary
preserve Evidence / AI Extraction boundary
implement only Phase 2 Partial operations unless task says otherwise
write tests for createEvidence requiring evidence_purpose
write tests for createEvidence requiring source_type
write tests for createEvidence requiring source_reference_id
write tests for controlled evidence_type, evidence_purpose, status and review_status
write tests preventing raw file/screenshot/document from becoming Evidence automatically
write tests preventing AI extraction from becoming approved Evidence
write tests preventing Evidence Service from making final legal sufficiency conclusion
write tests for event emission on mutation
```

Codex must not:

```text
invent full litigation evidence management in Phase 2
treat Document as Evidence automatically
treat screenshot or file upload as Evidence automatically
approve AI-extracted evidence automatically
make final legal sufficiency conclusions
fabricate evidence facts from AI
submit evidence externally from Evidence Service
ignore confidentiality policy
allow product UI to redefine Evidence status
```

---

# 18. Acceptance Criteria

This Evidence Service Specification is accepted only if:

```text
[ ] It defines Evidence Service purpose.
[ ] It defines Evidence Service Core meaning.
[ ] It identifies Evidence Service as Professional Core Service.
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
| 0.1.0 | Draft | Initial Evidence Service specification. Establishes Evidence Service as proof-layer service, separates Evidence from Document, raw files, Knowledge, AI extraction and professional conclusions, and defines Phase 2 Partial operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
