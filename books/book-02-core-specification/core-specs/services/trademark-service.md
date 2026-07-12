# Service Specification — Trademark Service

**Spec ID:** B02-SVC-TRADEMARK-SERVICE  
**Spec Type:** Service  
**Service Name:** Trademark Service  
**Owning Domain:** Trademark  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/trademark.md  
**Related Object Specs:** core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification.md; core-specs/objects/document.md; core-specs/objects/evidence.md  
**Related Service Specs:** core-specs/services/brand-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/classification-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/matter-service.md  
**Related Event Specs:** core-specs/events/trademark-created.md; core-specs/events/trademark-updated.md; core-specs/events/trademark-status-changed.md; core-specs/events/trademark-brand-linked.md; core-specs/events/trademark-classification-linked.md; core-specs/events/trademark-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/trademark/trademark-contract.md; core-specs/contracts/trademark/trademark-reference-contract.md; core-specs/contracts/trademark/trademark-brand-link-contract.md; core-specs/contracts/trademark/trademark-classification-contract.md; core-specs/contracts/trademark/trademark-status-contract.md; core-specs/contracts/trademark/trademark-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Trademark Service defines the Core service boundary for creating, updating, validating, linking and managing Trademark objects.

It exists so that Brand, Jurisdiction, Classification, Matter, Order, Document, Evidence, Knowledge, AI Agents, APIs and product consumers can consistently reference legal/procedural trademark protection objects without confusing Trademark with Brand, Matter, Order, Document, Evidence, official registry raw data or AI legal conclusion.

Trademark Service is required before:

```text
trademark record creation
trademark intake
brand-to-trademark linkage
jurisdiction-specific trademark planning
classification linkage
application/registration reference management
trademark status tracking
document/evidence linkage
matter creation based on trademark context
AI-assisted trademark summary and planning
audit trace for trademark-sensitive actions
```

---

# 2. Core Meaning

Trademark Service means:

```text
the Core service that manages legal/procedural trademark protection objects and their governed relationships to brands, jurisdictions, classifications, documents, evidence and professional execution.
```

Trademark Service does not mean:

```text
Brand Service
Matter Service
Order Service
official registry integration by itself
trademark filing engine by itself
legal opinion engine
registrability decision engine
document management service
evidence review service
AI legal conclusion service
```

Trademark Service answers:

```text
Does this Trademark exist?
Which Brand does it protect or relate to?
Which Jurisdiction applies?
Which Classification scope is linked?
Which application or registration references exist?
What controlled status applies?
Which Documents, Evidence or Matters reference it?
Can another domain safely reference this Trademark?
```

---

# 3. Service Category

Trademark Service is a Professional Core Service.

It manages legal/procedural trademark protection objects.

It does not replace Brand.

It does not execute full prosecution workflow.

It does not make final legal conclusions.

---

# 4. Architectural Position

Trademark Service sits after Brand Service and before Matter execution.

```text
Customer provides demand context
        ↓
Brand Service manages commercial identity
        ↓
Trademark Service manages legal/procedural protection object
        ↓
Jurisdiction Service defines where protection applies
        ↓
Classification Service defines goods/services scope
        ↓
Matter Service executes professional work
        ↓
Document and Evidence Services support execution
```

Trademark is the protection object.

Matter executes work.

Document and Evidence support procedure.

---

# 5. Scope

Trademark Service includes:

```text
trademark creation
trademark update
trademark status management
trademark brand linkage
trademark jurisdiction linkage
trademark classification linkage
trademark document linkage
trademark evidence linkage
official reference management
trademark reference validation
trademark audit trace
trademark event emission
```

MVP scope includes:

```text
create trademark
get trademark
update trademark metadata
change trademark status
link trademark to brand
link trademark to jurisdiction
link trademark to classification
link trademark to document
link trademark to evidence
validate trademark reference
emit trademark events
```

Deferred scope includes:

```text
official registry sync engine
automated trademark filing
full prosecution workflow
deadline engine
fee engine
registrability scoring
advanced similarity search
substantive legal opinion automation
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createTrademark | Create Trademark object | Yes | TrademarkCreated |
| getTrademark | Retrieve Trademark by ID | Yes | No |
| updateTrademark | Update governed Trademark metadata | Yes | TrademarkUpdated |
| changeTrademarkStatus | Change Trademark lifecycle status | Yes | TrademarkStatusChanged |
| linkTrademarkBrand | Link Trademark to Brand | Yes | TrademarkBrandLinked |
| unlinkTrademarkBrand | Remove Brand link | Partial | TrademarkBrandUnlinked |
| linkTrademarkJurisdiction | Link Trademark to Jurisdiction | Yes | TrademarkJurisdictionLinked |
| linkTrademarkClassification | Link Trademark to Classification | Yes | TrademarkClassificationLinked |
| unlinkTrademarkClassification | Remove Classification link | Partial | TrademarkClassificationUnlinked |
| linkTrademarkDocument | Link Trademark to Document | Yes | TrademarkDocumentLinked |
| linkTrademarkEvidence | Link Trademark to Evidence | Partial | TrademarkEvidenceLinked |
| updateOfficialReference | Update application/registration/source reference | Yes | TrademarkOfficialReferenceUpdated |
| validateTrademarkReference | Validate whether Trademark can be referenced | Yes | TrademarkReferenceValidated |
| archiveTrademark | Archive Trademark reference | Partial | TrademarkArchived |

---

# 7. Inputs

Trademark Service accepts:

```text
trademark_type
mark_representation
status
brand_reference_id
jurisdiction_reference_id
classification_reference_ids
owner_reference_id
application_number
registration_number
official_reference
document_reference_ids
evidence_reference_ids
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
trademark_type
mark_representation
jurisdiction_reference_id
status
source_reference
actor_context
```

Required for brand linkage:

```text
trademark_reference_id
brand_reference_id
link_type
actor_context
```

Required for classification linkage:

```text
trademark_reference_id
classification_reference_id
link_type
actor_context
```

Required for validation:

```text
trademark_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Trademark Service returns:

```text
Trademark object
Trademark reference
Trademark validation result
Trademark status result
Trademark brand link result
Trademark classification link result
Trademark document/evidence link result
Trademark official reference result
Trademark event reference
error result
```

Validation output must include:

```text
is_valid
trademark_reference_id
status
jurisdiction_reference_id
brand_reference_hint where applicable
classification_reference_hint where applicable
reason_code
policy_hint where applicable
```

Validation output must not expose unnecessary confidential customer, trademark or evidence data.

---

# 9. Controlled Values

## 9.1 trademark_type

```text
Word
Device
Combined
Slogan
Sound
Color
ThreeDimensional
Series
Unknown
```

## 9.2 status

Consumed canonical values from [Trademark Status Values](../controlled-state-values/trademark-status-values.md):

```text
Draft
Planned
PendingFiling
Filed
UnderExamination
Published
Opposed
Registered
Refused
Abandoned
Cancelled
Expired
Invalidated
RenewalDue
ReviewRequired
Archived
DeletedReferenceOnly
```

The Controlled State Value Specification [Trademark Status Values](../controlled-state-values/trademark-status-values.md) is the canonical source for legal Trademark status values and transition semantics. Trademark owns current state truth. Trademark Service validates and performs mutation. The Service must not define an alternate active status list.

## 9.3 brand_link_type

```text
PrimaryBrand
RelatedBrand
HistoricalBrand
DisputedBrand
Unknown
```

## 9.4 classification_link_type

```text
PlannedScope
FiledScope
RegisteredScope
AmendedScope
RenewalScope
EvidenceScope
Unknown
```

## 9.5 validation_result

```text
Valid
Invalid
NotFound
Inactive
Archived
ReviewRequired
JurisdictionRequired
ClassificationRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Trademark Requires Mark Representation and Jurisdiction

Trademark creation must require mark representation and jurisdiction reference.

A trademark without mark representation or jurisdiction context is not Core-valid unless explicitly represented as draft/pending with governed exception.

## 10.2 Trademark Is Not Brand

Trademark Service may link to Brand.

Brand Service owns commercial identity.

## 10.3 Trademark Is Not Matter or Order

Trademark Service manages protection objects.

Matter Service executes professional work.

Order Service records commercial service requests.

## 10.4 Trademark Is Not Official Registry Raw Data

Official references may update or support Trademark.

Raw official data must be normalized, sourced and validated before becoming governed Trademark fields.

## 10.5 Trademark Does Not Own Classification Logic

Trademark may link to Classification.

Classification Service owns goods/services scope.

## 10.6 Trademark Does Not Convert Documents or Evidence

Trademark may link Document and Evidence references.

Document and Evidence lifecycle remain owned by their services.

## 10.7 AI Analysis Is Not Final Legal Conclusion

AI may summarize, extract or recommend.

Final registrability, infringement, ownership or strategy conclusions require professional review where applicable.

## 10.8 Trademark Changes Must Be Auditable

Trademark-sensitive operations must preserve actor, source, request context and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Brand Service | Trademark may link to Brand | Brand owns commercial identity. |
| Jurisdiction Service | Trademark must reference Jurisdiction | Jurisdiction owns where context. |
| Classification Service | Trademark may link Classification | Classification owns goods/services scope. |
| Matter Service | Matter may execute Trademark work | Matter owns execution container. |
| Order Service | Order may request Trademark service | Order owns commercial request. |
| Document Service | Trademark may link Documents | Document owns artifact lifecycle. |
| Evidence Service | Trademark may link Evidence | Evidence owns proof layer. |
| Knowledge Service | May provide trademark guidance | Knowledge owns governed reference. |
| AI Agent Governance | AI may summarize/recommend | Agent Contract governs AI use. |
| Audit Service | Records Trademark-sensitive action | Audit owns accountability trail. |
| Event Service | Records Trademark events | Event records occurrence. |

---

# 12. Event Usage

Trademark Service emits:

```text
TrademarkCreated
TrademarkUpdated
TrademarkStatusChanged
TrademarkBrandLinked
TrademarkBrandUnlinked
TrademarkJurisdictionLinked
TrademarkClassificationLinked
TrademarkClassificationUnlinked
TrademarkDocumentLinked
TrademarkEvidenceLinked
TrademarkOfficialReferenceUpdated
TrademarkArchived
TrademarkReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Validation events may be emitted where audit requires.
- Events must reference Trademark ID.
- Brand link events must reference Brand ID.
- Jurisdiction link events must reference Jurisdiction ID.
- Classification link events must reference Classification ID.
- Official reference events must preserve source reference.
- Events must not expose confidential evidence or document content unnecessarily.
```

---

# 13. API Usage

Potential Phase 2 APIs:

```text
POST /trademarks
GET /trademarks/{id}
PATCH /trademarks/{id}
POST /trademarks/{id}/status
POST /trademarks/{id}/brands
DELETE /trademarks/{id}/brands/{brandId}
POST /trademarks/{id}/jurisdiction
POST /trademarks/{id}/classifications
DELETE /trademarks/{id}/classifications/{classificationId}
POST /trademarks/{id}/documents
POST /trademarks/{id}/evidence
POST /trademarks/{id}/official-reference
POST /trademarks/reference/validate
```

API rules:

```text
- APIs must invoke Trademark Service operations.
- APIs must not create Brand unless Brand Service is invoked.
- APIs must not create Classification unless Classification Service is invoked.
- APIs must not create Matter or Order directly.
- APIs must not convert official raw data directly into approved fields without validation.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Trademark Service only under governed Agent Contracts.

Allowed AI use:

```text
summarize Trademark profile
identify missing Brand, Jurisdiction or Classification links
extract application/registration references for review
suggest status mapping for review
identify document/evidence gaps
draft trademark intake notes
flag Brand / Trademark boundary mismatch
suggest matter creation readiness for review
```

AI must not:

```text
create Trademark without authorized service
make final registrability conclusion
make final infringement or ownership conclusion
change official status without authorized source/service
treat raw registry data as approved Trademark automatically
create Matter or Order directly
convert Documents or Evidence automatically
alter Trademark status without authorized service
```

AI Trademark use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Trademark Access Rule
Brand Access Rule where applicable
Jurisdiction Rule
Classification Rule
Audit Rule
Human Review Rule for legal/professional conclusions and status changes
```

---

# 15. Validation Rules

Trademark Service must enforce:

```text
[ ] trademark_type is controlled.
[ ] status is controlled.
[ ] createTrademark requires mark_representation unless governed draft exception applies.
[ ] createTrademark requires jurisdiction_reference_id.
[ ] createTrademark produces stable immutable Trademark ID.
[ ] updateTrademark does not mutate immutable ID.
[ ] changeTrademarkStatus follows allowed lifecycle.
[ ] linkTrademarkBrand references valid Brand.
[ ] linkTrademarkJurisdiction references valid Jurisdiction.
[ ] linkTrademarkClassification references valid Classification.
[ ] validateTrademarkReference rejects missing, archived or deleted-reference trademarks where not allowed.
[ ] Trademark Service does not create Brand/Classification/Matter/Order directly.
[ ] Trademark Service does not convert raw official data automatically.
[ ] Trademark Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Trademark Service should return controlled errors:

```text
TrademarkNotFound
InvalidTrademarkType
InvalidTrademarkStatus
InvalidTrademarkTransition
InvalidTrademarkReference
MarkRepresentationRequired
JurisdictionRequired
InvalidJurisdictionReference
BrandNotFound
InvalidBrandReference
ClassificationNotFound
InvalidClassificationReference
DocumentNotFound
EvidenceNotFound
InvalidOfficialReference
PermissionRequired
PolicyRestricted
ReviewRequired
AuditContextMissing
UnknownTrademarkError
```

Errors must be safe for product display and API consumption.

Sensitive trademark, customer, document or evidence information must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite trademark domain spec
cite trademark object spec
cite brand, jurisdiction and classification specs where relevant
preserve Trademark / Brand boundary
preserve Trademark / Matter boundary
preserve Trademark / Order boundary
preserve Trademark / Classification boundary
preserve Trademark / Document / Evidence boundaries
implement only Phase 2 MVP operations unless task says otherwise
write tests for createTrademark requiring mark_representation
write tests for createTrademark requiring jurisdiction_reference_id
write tests for controlled trademark_type
write tests for controlled status
write tests preventing Trademark Service from creating Brand directly
write tests preventing Trademark Service from creating Matter/Order directly
write tests preventing raw official data from becoming approved Trademark automatically
write tests for event emission on mutation
```

Codex must not:

```text
invent full trademark prosecution engine in Phase 2
treat Trademark as Brand
treat Trademark as Matter or Order
implement official registry sync unless explicitly tasked
implement registrability or infringement decision engine
convert official raw data into approved fields without validation
convert Documents/Evidence automatically
allow AI to make final legal conclusion
allow product UI to redefine Trademark status
```

---

# 18. Acceptance Criteria

This Trademark Service Specification is accepted only if:

```text
[ ] It defines Trademark Service purpose.
[ ] It defines Trademark Service Core meaning.
[ ] It identifies Trademark Service as Professional Core Service.
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
| 0.1.0 | Draft | Initial Trademark Service specification. Establishes Trademark Service as legal/procedural protection object service, separates it from Brand, Matter, Order, Classification, Document, Evidence, official registry raw data and AI legal conclusions, and defines Phase 2 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
