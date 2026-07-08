# Object Specification — Classification

**Spec ID:** B02-OBJ-CLASSIFICATION  
**Spec Type:** Object  
**Object Name:** Classification  
**Owning Domain:** Classification  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/classification.md  
**Related Object Specs:** core-specs/objects/trademark.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification-class.md; core-specs/objects/goods-services-item.md; core-specs/objects/classification-scheme.md; core-specs/objects/classification-status.md; core-specs/objects/classification-recommendation.md  
**Related Service Specs:** core-specs/services/classification-registration-service.md; core-specs/services/classification-item-service.md; core-specs/services/classification-scheme-service.md; core-specs/services/classification-validation-service.md; core-specs/services/classification-recommendation-service.md; core-specs/services/classification-reference-validation-service.md  
**Related Event Specs:** core-specs/events/classification-created.md; core-specs/events/classification-updated.md; core-specs/events/classification-item-added.md; core-specs/events/classification-item-removed.md; core-specs/events/classification-validated.md; core-specs/events/classification-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/classification/classification-contract.md; core-specs/contracts/classification/classification-class-contract.md; core-specs/contracts/classification/goods-services-item-contract.md; core-specs/contracts/classification/classification-scheme-contract.md; core-specs/contracts/classification/classification-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Classification object defines the Core-recognized goods/services scope used for trademark planning, filing, prosecution, maintenance, evidence review and professional analysis.

It exists so that Trademark, Brand, Jurisdiction, Matter, Order, Document, Evidence, Knowledge, AI Agents, Services, APIs and product consumers can consistently reference classes, goods/services items, classification schemes, item status and professional review state.

Classification is required before:

```text
trademark goods/services planning
Nice class reference
local classification reference
jurisdiction-specific item validation
filing scope preparation
office action response scope analysis
renewal/use declaration goods scope review
evidence-to-goods/services matching
AI classification recommendation
client-facing goods/services selection
Codex implementation of classification workflows
```

---

# 2. Core Meaning

Classification means:

```text
a Core-recognized professional goods/services scope for trademark protection, consisting of class references, goods/services items, scheme references, jurisdiction context, status and review/validation state.
```

Classification is not:

```text
class number alone
product category alone
customer product list
raw official acceptable item only
AI recommendation
approved filing scope by default
trademark itself
brand itself
legal conclusion
```

Classification answers:

```text
Which goods or services are being claimed, planned, reviewed or filed?
Which class or classes apply?
Which classification scheme applies?
Which jurisdiction context affects item wording or limits?
Which trademark or brand does the scope relate to?
Has the scope been drafted, recommended, reviewed, approved, rejected or filed?
Which Knowledge, Document or Evidence references support it?
What audit trace is required?
```

---

# 3. Object Category

Classification is a Professional Object owned by the Classification Domain.

It is the professional goods/services scope layer for trademark work.

It may link to Trademark and Jurisdiction, but it must not replace Trademark, Jurisdiction or legal strategy.

---

# 4. Architectural Position

Classification sits between Trademark and professional execution.

```text
Brand captures commercial identity
        ↓
Trademark defines legal/procedural protection object
        ↓
Jurisdiction defines where protection/procedure applies
        ↓
Classification defines goods/services scope
        ↓
Matter executes professional work
        ↓
Document and Evidence support procedure
```

Classification defines professional scope.

It does not file application by itself.

It does not decide registrability by itself.

---

# 5. Scope

The Classification object includes:

```text
classification id
classification scheme reference
jurisdiction reference
trademark reference
brand reference
class references
goods/services item references
classification status
recommendation reference
review status
source reference
knowledge reference
document reference
evidence reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
classification id
classification scheme
jurisdiction reference
trademark reference
brand reference
class numbers/references
goods/services items
status
review status
source reference
knowledge reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Classification ID. |
| classification_scheme | enum/string | Yes | Yes | Nice, Local, Custom, Madrid, USPTO ID Manual, CN Similar Group, Unknown. |
| jurisdiction_reference_id | string | No | Yes | Jurisdiction context where applicable. |
| trademark_reference_id | string | No | Yes | Related Trademark reference. |
| brand_reference_id | string | No | Yes | Related Brand reference. |
| class_references | array | Yes | Yes | Controlled class references or numbers. |
| goods_services_items | array | Yes | Yes | Goods/services item references or embedded item structures. |
| status | enum | Yes | Yes | Controlled Classification status. |
| review_status | enum | Yes | Yes | Controlled professional review state. |
| recommendation_reference_id | string | No | Partial | AI/system recommendation reference. |
| source_reference | string | No | Yes | Intake/import/official/source reference. |
| knowledge_reference_ids | array | No | Yes | Related Knowledge references. |
| document_reference_ids | array | No | Partial | Related Document references. |
| evidence_reference_ids | array | No | Partial | Related Evidence references. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 classification_scheme

MVP controlled values:

```text
Nice
Local
Madrid
USPTO_ID_Manual
CN_Similar_Group
Custom
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
Recommended
ReviewRequired
Approved
Rejected
Filed
Amended
Archived
DeletedReferenceOnly
```

## 7.3 review_status

MVP controlled values:

```text
Unreviewed
AIRecommended
HumanReviewed
ApprovedForFiling
Rejected
NeedsRevision
FiledScope
```

## 7.4 item_type

Suggested controlled values:

```text
Goods
Services
ClassHeading
CustomItem
OfficialAcceptableItem
LocalStandardItem
Unknown
```

---

# 8. Object Rules

## 8.1 Classification Requires Class and Item Scope

Every Classification must contain:

```text
class reference
goods/services item reference
classification scheme
status
```

A class number alone is not complete Classification.

## 8.2 Classification Requires Scheme Context

Every Classification must identify the classification scheme.

Nice class number, local subclass, official acceptable wording and custom wording must be distinguishable.

## 8.3 Classification May Be Jurisdiction-Specific

Classification can be affected by jurisdiction rules, official wording requirements, class limits, subclass systems, local practice and fee structures.

Jurisdiction context should be linked where relevant.

## 8.4 AI Recommendation Is Not Approved Scope

AI or system recommendation must be distinguished from reviewed or approved filing scope.

Professional review is required for filing-ready classification where risk or client-facing commitment exists.

## 8.5 Classification Does Not Replace Trademark

Classification defines goods/services scope.

Trademark remains the legal/procedural protection object.

## 8.6 Classification Must Be Auditable

Classification-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
classification creation
class change
goods/services item addition
goods/services item deletion
item wording update
scheme update
jurisdiction context update
AI recommendation
human review
approval for filing
filed scope confirmation
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Trademark | Classification may belong to Trademark | Trademark remains protection object. |
| Brand | Classification may support Brand strategy | Brand remains commercial identity. |
| Jurisdiction | Classification may be jurisdiction-specific | Jurisdiction remains where procedure applies. |
| Knowledge | Knowledge may support item selection | Knowledge does not approve scope. |
| Document | Documents may contain classification wording | Document remains artifact. |
| Evidence | Evidence may support use for items | Evidence remains proof layer. |
| Matter | Matter may execute classification work | Matter remains execution container. |
| Order | Order may request classification service | Order remains commercial request. |
| Policy | Policy may constrain item limits/review | Policy remains contextual rule. |
| AI Output | AI may recommend Classification | AI Output is not approved scope. |
| Audit Record | Audit may reference Classification | Audit remains accountability system. |

---

# 10. Lifecycle

Classification lifecycle states:

```text
Draft
Recommended
ReviewRequired
Approved
Rejected
Filed
Amended
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → Recommended
Draft → ReviewRequired
Recommended → ReviewRequired
ReviewRequired → Approved
ReviewRequired → Rejected
Approved → Filed
Filed → Amended
Approved → Archived
Rejected → Archived
Filed → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Recommended → Filed without approval
AIRecommended → ApprovedForFiling without human review where required
Archived → Filed without restoration/review
DeletedReferenceOnly → Active state
```

---

# 11. Service Usage

Classification object is created and managed through:

```text
Classification Registration Service
Classification Item Service
Classification Scheme Service
Classification Validation Service
Classification Review Service
Classification Recommendation Service
Classification Reference Validation Service
Classification Audit Reference Service
```

Service rules:

```text
- Services must validate classification_scheme.
- Services must require class references and goods/services items.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- AI recommendation service must mark recommendation as AI/system generated.
- Validation service must not turn recommendation into approval.
- Services must not create Trademark unless Trademark service is invoked.
```

---

# 12. Event Usage

Classification object emits or participates in:

```text
ClassificationCreated
ClassificationUpdated
ClassificationStatusChanged
ClassificationItemAdded
ClassificationItemRemoved
ClassificationItemUpdated
ClassificationSchemeUpdated
ClassificationRecommended
ClassificationReviewRequired
ClassificationApproved
ClassificationRejected
ClassificationFiled
ClassificationReferenceValidated
```

Event rules:

```text
- Classification events must reference Classification ID.
- Item events must preserve item reference and class reference.
- Recommendation events must identify AI/system/human source.
- Approval events must preserve reviewer where allowed.
- Events must not expose protected client product data unnecessarily.
```

---

# 13. API Usage

Potential Phase 2 APIs:

```text
POST /classifications
GET /classifications/{id}
PATCH /classifications/{id}
POST /classifications/{id}/status
POST /classifications/{id}/items
DELETE /classifications/{id}/items/{itemId}
POST /classifications/{id}/validate
POST /classifications/{id}/recommend
POST /classifications/reference/validate
```

API rules:

```text
- APIs must invoke Classification Services.
- APIs must distinguish recommendation from approved scope.
- APIs must not file applications directly.
- APIs must not create Trademark unless Trademark service is invoked.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Classification only under governed Agent Contracts.

Allowed AI use:

```text
suggest class candidates
suggest goods/services items
normalize item wording
map product descriptions to candidate items
identify item/class mismatch
flag jurisdiction-specific wording issues
compare classification with evidence
prepare classification draft for human review
```

AI must not:

```text
mark scope approved for filing without professional review
file applications directly
represent recommendation as official acceptable wording without source
ignore jurisdiction limits
delete goods/services items without governed service
make final legal strategy decision
```

AI Classification use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Classification Access Rule
Jurisdiction Rule
Trademark Access Rule where applicable
Audit Rule
Human Review Rule for filing-ready scope
```

---

# 15. Validation Rules

Classification object must pass:

```text
[ ] id is present and immutable.
[ ] classification_scheme is controlled.
[ ] class_references are present.
[ ] goods_services_items are present.
[ ] status is controlled.
[ ] review_status is controlled.
[ ] Class number alone is not complete Classification.
[ ] AI recommendation is not approved filing scope.
[ ] Jurisdiction-specific requirements are referenceable.
[ ] Classification does not replace Trademark.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite classification domain spec
cite trademark and jurisdiction object specs
preserve Classification / Trademark boundary
preserve Classification / Jurisdiction boundary
preserve Classification / AI Recommendation boundary
implement only MVP fields unless task says otherwise
write tests for required classification_scheme
write tests for required class_references
write tests for required goods_services_items
write tests for controlled status
write tests for controlled review_status
write tests preventing class number alone as complete classification
write tests preventing AI recommendation from becoming approved scope
write tests for event emission on mutation
```

Codex must not:

```text
invent full legal classification engine in MVP
treat class number as complete filing scope
treat AI recommendation as approved scope
file applications from Classification service
ignore jurisdiction context where required
treat official wording reference as automatically approved for all jurisdictions
allow product UI to redefine Classification status
```

---

# 17. Acceptance Criteria

This Classification Object Specification is accepted only if:

```text
[ ] It defines Classification purpose.
[ ] It defines Classification Core meaning.
[ ] It identifies Classification as Professional Object.
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
| 0.1.0 | Draft | Initial Classification object specification. Establishes Classification as professional goods/services scope object, separates it from class number alone, Trademark, Jurisdiction and AI recommendation, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
