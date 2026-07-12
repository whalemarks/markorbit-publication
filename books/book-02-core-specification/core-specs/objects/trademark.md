# Object Specification — Trademark

**Spec ID:** B02-OBJ-TRADEMARK  
**Spec Type:** Object  
**Object Name:** Trademark  
**Owning Domain:** Trademark  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/trademark.md  
**Related Object Specs:** core-specs/objects/brand.md; core-specs/objects/trademark-application.md; core-specs/objects/trademark-registration.md; core-specs/objects/trademark-owner-reference.md; core-specs/objects/trademark-mark-representation.md; core-specs/objects/trademark-goods-services-reference.md
**Related Service Specs:** core-specs/services/trademark-registration-service.md; core-specs/services/trademark-status-service.md; core-specs/services/trademark-owner-reference-service.md; core-specs/services/trademark-brand-link-service.md; core-specs/services/trademark-classification-reference-service.md; core-specs/services/trademark-reference-validation-service.md  
**Related Event Specs:** core-specs/events/trademark-created.md; core-specs/events/trademark-updated.md; core-specs/events/trademark-status-changed.md; core-specs/events/trademark-brand-linked.md; core-specs/events/trademark-owner-linked.md; core-specs/events/trademark-classification-linked.md; core-specs/events/trademark-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/trademark/trademark-contract.md; core-specs/contracts/trademark/trademark-application-contract.md; core-specs/contracts/trademark/trademark-registration-contract.md; core-specs/contracts/trademark/trademark-status-contract.md; core-specs/contracts/trademark/trademark-brand-link-contract.md; core-specs/contracts/trademark/trademark-classification-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Trademark object defines the Core-recognized legal/procedural protection object used to represent a trademark application, registration, filing target, protection record or managed trademark asset in MarkOrbit.

It exists so that Brand, Jurisdiction, Classification, Matter, Order, Document, Evidence, Customer, AI Agents, Services, APIs and product consumers can consistently reference trademark protection without confusing it with commercial brand identity, filing matter, official document, evidence material or order request.

Trademark is required before:

```text
trademark intake
trademark record management
application and registration tracking
jurisdiction-specific filing planning
classification and goods/services linkage
matter creation
document preparation
evidence collection
deadline and status management
renewal/change/assignment/opposition workflows
AI trademark analysis
client-facing trademark workspace
```

---

# 2. Core Meaning

Trademark means:

```text
a Core-recognized legal or procedural protection object for a mark, application, registration or managed trademark record, connected to jurisdiction, classification, owner, status, documents, evidence and professional execution context.
```

Trademark is not:

```text
Brand
Customer
Matter
Order
Document
Evidence
Jurisdiction
Classification
Official database raw record
Legal opinion
Final professional conclusion
AI output
```

Trademark answers:

```text
Which mark is being protected or managed?
Which Brand does it relate to?
Which jurisdiction applies?
Which classes, goods and services apply?
Who is the applicant, registrant or owner reference?
What application or registration references exist?
What status and lifecycle apply?
Which matters, documents and evidence support the record?
What audit trace is required?
```

---

# 3. Object Category

Trademark is a Professional Object owned by the Trademark Domain.

It is the legal/procedural protection object.

Brand is the commercial identity object.

Matter is the professional execution container.

Order is the commercial service request.

Trademark must preserve these boundaries.

---

# 4. Architectural Position

Trademark sits after Brand and before Matter execution.

```text
Brand captures commercial identity
        ↓
Trademark defines legal/procedural protection object
        ↓
Jurisdiction defines where protection applies
        ↓
Classification defines goods/services scope
        ↓
Matter executes professional work
        ↓
Document and Evidence support procedure
```

Trademark provides professional protection context.

It does not execute work by itself.

---

# 5. Scope

The Trademark object includes:

```text
trademark id
mark representation
trademark type
trademark status
brand reference
jurisdiction reference
owner/applicant reference
application reference
registration reference
classification reference
goods/services reference
filing date reference
registration date reference
priority reference
official status reference
matter references
document references
evidence references
source reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
trademark id
mark representation
trademark type
trademark status
brand reference
jurisdiction reference
owner/applicant reference
application number/reference
registration number/reference
classification references
goods/services references
matter references
document references
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Trademark ID. |
| mark_representation | string/object | Yes | Yes | Word, image reference or structured mark representation. |
| trademark_type | enum | Yes | Yes | Word, Device, Combined, Slogan, Sound, Color, 3D, Series, Unknown. |
| status | enum | Yes | Yes | Controlled Trademark status. |
| brand_reference_id | string | No | Yes | Related Brand reference. |
| jurisdiction_reference_id | string | Yes | Yes | Jurisdiction where protection applies. |
| owner_reference_id | string | No | Yes | Applicant/registrant/owner reference. |
| applicant_reference_id | string | No | Yes | Applicant reference where distinct. |
| application_number | string | No | Yes | Official or internal application number/reference. |
| registration_number | string | No | Yes | Official or internal registration number/reference. |
| application_date | date | No | Yes | Filing/application date where known. |
| registration_date | date | No | Yes | Registration date where known. |
| priority_reference | string | No | Partial | Priority reference where applicable. |
| class_references | array | No | Yes | Nice or local class references. |
| goods_services_references | array | No | Yes | Classification/goods/services references. |
| official_status_reference | string | No | Partial | Official status/source reference. |
| matter_references | array | No | Yes | Related Matter references. |
| document_references | array | No | Yes | Related Document references. |
| evidence_references | array | No | Partial | Related Evidence references. |
| source_reference | string | No | Yes | Intake/import/official source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 trademark_type

MVP controlled values:

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

## 7.2 status

Trademark Status is a parent-owned Controlled State Value Specification of Trademark, not an independent identity-bearing Core Object. Only the Trademark owning Service may mutate `status`; each status change requires an Event trace. AI and Product UI may display or summarize allowed status values but must not define new Trademark statuses or directly change them.

MVP controlled values:

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

## 7.3 mark_representation_type

Suggested controlled values:

```text
Text
Image
TextAndImage
StructuredDescription
OfficialImageReference
Unknown
```

---

# 8. Object Rules

## 8.1 Trademark Requires Mark Representation

Every Trademark must have a mark representation or explicit mark-pending status.

A Trademark without mark representation is not filing-ready.

## 8.2 Trademark Requires Jurisdiction

Every Trademark must reference Jurisdiction.

Trademark protection and procedure are jurisdiction-bound.

## 8.3 Trademark Does Not Equal Brand

Trademark protects or represents legal/procedural protection of a mark.

Brand captures commercial identity.

A Brand may have many Trademarks.

A Trademark may be linked to one or more Brand contexts where governed.

## 8.4 Trademark Does Not Equal Matter

Matter executes work involving Trademark.

Trademark remains protection object.

## 8.5 Trademark Does Not Equal Official Database Record

Official database data may source or update Trademark.

Raw official data must be normalized, sourced and validated before Core use.

## 8.6 Trademark Documents and Evidence Are References

Trademark may link to Document and Evidence.

It does not own Document lifecycle or Evidence proof status.

## 8.7 Trademark Must Be Auditable

Trademark-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
trademark creation
mark representation update
jurisdiction update
owner/applicant update
brand linkage
classification linkage
status change
official reference update
document/evidence linkage
AI trademark analysis
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Brand | Trademark may protect Brand | Brand remains commercial identity. |
| Jurisdiction | Trademark must reference Jurisdiction | Jurisdiction defines where procedure applies. |
| Classification | Trademark references classes/goods/services | Classification owns goods/services scope. |
| Customer | Customer may own/request Trademark service | Customer remains demand-side party. |
| Matter | Matter executes work for Trademark | Matter remains execution container. |
| Order | Order may request Trademark service | Order remains commercial service request. |
| Document | Trademark may link to Documents | Document remains artifact. |
| Evidence | Trademark may link to Evidence | Evidence remains proof layer. |
| Knowledge | Knowledge may support analysis | Knowledge does not decide legal status. |
| Policy | Policy may constrain handling | Policy remains contextual rule. |
| AI Output | AI may analyze Trademark | AI Output is not final professional conclusion. |
| Audit Record | Audit may reference Trademark | Audit remains accountability system. |

---

# 10. Lifecycle

Trademark lifecycle states:

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

Lifecycle rules are jurisdiction-sensitive and must remain policy/workflow governed.

General lifecycle examples:

```text
Draft → Planned
Planned → PendingFiling
PendingFiling → Filed
Filed → UnderExamination
UnderExamination → Published
Published → Registered
Published → Opposed
UnderExamination → Refused
Registered → RenewalDue
Registered → Cancelled
Registered → Expired
Refused → Archived
Abandoned → Archived
Expired → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
DeletedReferenceOnly → Active status
Registered → Filed without correction/review
Jurisdiction-specific transition without Workflow Contract or Policy support
Official status overwrite without source reference
```

---

# 11. Service Usage

Trademark object is created and managed through:

```text
Trademark Registration Service
Trademark Update Service
Trademark Status Service
Trademark Brand Link Service
Trademark Owner Reference Service
Trademark Classification Reference Service
Trademark Document Reference Service
Trademark Evidence Reference Service
Trademark Reference Validation Service
Trademark Audit Reference Service
```

Service rules:

```text
- Services must validate trademark_type.
- Services must validate jurisdiction reference.
- Services must validate status transitions through policy/workflow where required.
- Services must emit events for mutating actions.
- Services must not create Brand unless Brand service is invoked.
- Services must not create Matter unless Matter service is invoked.
- Services must not convert official raw records directly into approved Trademark without validation.
```

---

# 12. Event Usage

Trademark object emits or participates in:

```text
TrademarkCreated
TrademarkUpdated
TrademarkStatusChanged
TrademarkBrandLinked
TrademarkOwnerLinked
TrademarkJurisdictionLinked
TrademarkClassificationLinked
TrademarkDocumentLinked
TrademarkEvidenceLinked
TrademarkOfficialReferenceUpdated
TrademarkArchived
TrademarkReferenceValidated
```

Event rules:

```text
- Trademark events must reference Trademark ID.
- Status events must preserve previous and new status.
- Official reference events must preserve source reference.
- Classification events must reference class/goods/services references.
- Events must not expose protected documents or evidence unnecessarily.
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
POST /trademarks/{id}/classifications
POST /trademarks/{id}/documents
POST /trademarks/{id}/evidence
POST /trademarks/reference/validate
```

API rules:

```text
- APIs must invoke Trademark Services.
- APIs must not create Brand unless Brand service is invoked.
- APIs must not create Matter unless Matter service is invoked.
- APIs must not convert Documents or Evidence automatically.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Trademark only under governed Agent Contracts.

Allowed AI use:

```text
summarize trademark record
normalize mark representation
identify missing jurisdiction or classification reference
suggest filing planning questions
summarize official status if source is available
flag trademark/brand boundary mismatch
flag document/evidence gaps
prepare analysis draft for human review
```

AI must not:

```text
make final registrability decision without professional review
make final infringement or legal risk conclusion
change official status without authorized source and service
create Matter directly from Trademark without governed service
convert raw official data into approved Trademark silently
treat Trademark as Brand
treat Document or Evidence references as automatically reviewed
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
Human Review Rule for professional conclusions
```

---

# 15. Validation Rules

Trademark object must pass:

```text
[ ] id is present and immutable.
[ ] mark_representation is present or mark-pending status is explicit.
[ ] trademark_type is controlled.
[ ] status is controlled.
[ ] jurisdiction_reference_id is present.
[ ] Trademark does not equal Brand.
[ ] Trademark does not equal Matter.
[ ] Trademark does not equal official raw record.
[ ] Document and Evidence references remain references.
[ ] Status transitions are governed by policy/workflow where required.
[ ] Mutating services emit events.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite trademark domain spec
cite brand object spec
preserve Trademark / Brand boundary
preserve Trademark / Matter boundary
preserve Trademark / Order boundary
preserve Trademark / Document / Evidence boundaries
implement only MVP fields unless task says otherwise
write tests for required jurisdiction_reference_id
write tests for required mark representation or explicit pending status
write tests for controlled trademark_type
write tests for controlled status
write tests preventing Trademark from becoming Brand
write tests preventing Trademark from becoming Matter
write tests preventing raw official data from becoming approved Trademark without validation
write tests for event emission on mutation
```

Codex must not:

```text
invent full trademark prosecution engine inside Trademark object
treat Trademark as Brand
create Matter automatically from Trademark
treat official raw record as approved Trademark without validation
treat linked Document/Evidence as reviewed automatically
allow AI to make final legal conclusions from Trademark alone
allow product UI to redefine Trademark status
```

---

# 17. Acceptance Criteria

This Trademark Object Specification is accepted only if:

```text
[ ] It defines Trademark purpose.
[ ] It defines Trademark Core meaning.
[ ] It identifies Trademark as Professional Object.
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
| 0.1.0 | Draft | Initial Trademark object specification. Establishes Trademark as legal/procedural protection object, separates Trademark from Brand, Matter, Order, Document, Evidence and raw official records, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**


## PUB-TASK-B02-002 Controlled State Value Reference

`status` remains parent-owned by this object. Canonical semantics and transition constraints are defined by `core-specs/controlled-state-values/trademark-status-values.md`. This object specification preserves the existing controlled value list and does not restore any legacy status concept as an active Core Object. Product UI and AI may consume but not define or mutate status values.
