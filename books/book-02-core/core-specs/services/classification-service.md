# Service Specification — Classification Service

**Spec ID:** B02-SVC-CLASSIFICATION-SERVICE  
**Spec Type:** Service  
**Service Name:** Classification Service  
**Owning Domain:** Classification  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/classification.md  
**Related Object Specs:** core-specs/objects/classification.md; core-specs/objects/trademark.md; core-specs/objects/jurisdiction.md; core-specs/objects/brand.md; core-specs/objects/document.md; core-specs/objects/evidence.md  
**Related Service Specs:** core-specs/services/trademark-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/brand-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/knowledge-service.md  
**Related Event Specs:** core-specs/events/classification-created.md; core-specs/events/classification-updated.md; core-specs/events/classification-status-changed.md; core-specs/events/classification-item-added.md; core-specs/events/classification-item-removed.md; core-specs/events/classification-validated.md; core-specs/events/classification-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/classification/classification-contract.md; core-specs/contracts/classification/classification-reference-contract.md; core-specs/contracts/classification/classification-item-contract.md; core-specs/contracts/classification/classification-review-contract.md; core-specs/contracts/classification/classification-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Classification Service defines the Core service boundary for creating, updating, validating, reviewing and managing Classification objects and their goods/services item scope.

It exists so that Trademark, Brand, Jurisdiction, Matter, Order, Document, Evidence, Knowledge, AI Agents, APIs and product consumers can consistently reference trademark classes and goods/services scope without confusing Classification with a class number alone, customer product list, AI recommendation, official acceptable wording or approved filing scope.

Classification Service is required before:

```text
goods/services intake
class and item scope creation
trademark classification planning
jurisdiction-specific item validation
filing scope review
classification approval for filing
classification amendment tracking
evidence-to-goods/services mapping
AI-assisted classification recommendation
audit trace for classification-sensitive actions
```

---

# 2. Core Meaning

Classification Service means:

```text
the Core service that manages professional goods/services scope, including class references, item wording, scheme context, jurisdiction context, review state and validation state.
```

Classification Service does not mean:

```text
Trademark Service
Jurisdiction Service
product catalog service
AI classification engine by itself
official item database by itself
legal strategy engine
filing engine
approved scope by default
```

Classification Service answers:

```text
Does this Classification exist?
Which classes and goods/services items are included?
Which classification scheme applies?
Which Jurisdiction context affects wording or limits?
Which Trademark or Brand does the scope relate to?
Is the scope draft, recommended, review-required, approved, filed or archived?
Can another domain safely reference this Classification?
```

---

# 3. Service Category

Classification Service is a Professional Core Service.

It manages goods/services scope.

It does not file applications.

It does not make final legal strategy decisions.

It does not treat AI recommendations as approved filing scope.

---

# 4. Architectural Position

Classification Service sits after Trademark and Jurisdiction context.

```text
Brand Service manages commercial identity
        ↓
Trademark Service manages protection object
        ↓
Jurisdiction Service defines where protection/procedure applies
        ↓
Classification Service defines goods/services scope
        ↓
Matter Service executes professional work
        ↓
Document and Evidence Services support execution
```

Classification defines scope.

Matter executes work.

AI may recommend, but professional review approves.

---

# 5. Scope

Classification Service includes:

```text
classification creation
classification update
classification status management
classification item addition/removal/update
classification scheme management
jurisdiction context linkage
trademark/brand linkage
classification recommendation reference
classification review and approval
classification validation
classification reference validation
classification audit trace
classification event emission
```

MVP scope includes:

```text
create classification
get classification
update classification metadata
change classification status
add goods/services item
remove goods/services item
update goods/services item
link classification to trademark
link classification to jurisdiction
validate classification reference
validate classification items
mark review required
mark approved for filing
emit classification events
```

Deferred scope includes:

```text
full AI classification engine
official acceptable item sync
jurisdiction-specific subclass engine
fee impact calculation
class limit pricing engine
advanced similarity and risk analysis
automatic approval of AI recommendations
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createClassification | Create Classification object | Yes | ClassificationCreated |
| getClassification | Retrieve Classification by ID | Yes | No |
| updateClassification | Update governed metadata | Yes | ClassificationUpdated |
| changeClassificationStatus | Change Classification lifecycle status | Yes | ClassificationStatusChanged |
| addClassificationItem | Add goods/services item | Yes | ClassificationItemAdded |
| updateClassificationItem | Update item wording/reference | Yes | ClassificationItemUpdated |
| removeClassificationItem | Remove goods/services item | Yes | ClassificationItemRemoved |
| linkClassificationTrademark | Link Classification to Trademark | Yes | ClassificationTrademarkLinked |
| linkClassificationJurisdiction | Link Classification to Jurisdiction | Yes | ClassificationJurisdictionLinked |
| recommendClassification | Register AI/system/human recommendation | Partial | ClassificationRecommended |
| reviewClassification | Record review state | Yes | ClassificationReviewed |
| validateClassification | Validate class/item/scheme consistency | Yes | ClassificationValidated |
| validateClassificationReference | Validate whether Classification can be referenced | Yes | ClassificationReferenceValidated |
| archiveClassification | Archive Classification reference | Partial | ClassificationArchived |

---

# 7. Inputs

Classification Service accepts:

```text
classification_scheme
class_references
goods_services_items
status
review_status
trademark_reference_id
brand_reference_id
jurisdiction_reference_id
recommendation_reference_id
source_reference
knowledge_reference_ids
document_reference_ids
evidence_reference_ids
metadata
actor_context
request_context
```

Required for creation:

```text
classification_scheme
class_references
goods_services_items
status
review_status
source_reference
actor_context
```

Required for item operations:

```text
classification_reference_id
class_reference
goods_services_item
item_type
actor_context
```

Required for review:

```text
classification_reference_id
review_status
review_note_reference
actor_context
```

Required for validation:

```text
classification_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Classification Service returns:

```text
Classification object
Classification reference
Classification item result
Classification review result
Classification validation result
Classification status result
Classification event reference
error result
```

Validation output must include:

```text
is_valid
classification_reference_id
classification_scheme
class_references
item_count
status
review_status
reason_code
review_required
jurisdiction_hint where applicable
policy_hint where applicable
```

Validation output must not expose confidential customer product data unnecessarily.

---

# 9. Controlled Values

## 9.1 classification_scheme

```text
Nice
Local
Madrid
USPTO_ID_Manual
CN_Similar_Group
Custom
Unknown
```

## 9.2 status

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

## 9.3 review_status

```text
Unreviewed
AIRecommended
HumanReviewed
ApprovedForFiling
Rejected
NeedsRevision
FiledScope
```

## 9.4 item_type

```text
Goods
Services
ClassHeading
CustomItem
OfficialAcceptableItem
LocalStandardItem
Unknown
```

## 9.5 validation_result

```text
Valid
Invalid
ReviewRequired
NeedsRevision
MissingClass
MissingItems
SchemeMismatch
JurisdictionReviewRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Classification Requires Scheme, Class and Items

Classification creation must require:

```text
classification_scheme
class_references
goods_services_items
```

A class number alone is not a Core-valid Classification.

## 10.2 Classification Is Not Trademark

Classification may link to Trademark.

Trademark Service owns legal/procedural protection object.

## 10.3 Classification Is Jurisdiction-Aware

Classification may be affected by jurisdiction-specific wording, subclasses, item limits, official practices and filing rules.

Jurisdiction Service and Knowledge Service provide context.

## 10.4 AI Recommendation Is Not Approval

AI/system recommendation must remain distinct from human review and approval for filing.

## 10.5 Official Item Reference Is Not Universal Approval

Official acceptable wording in one source does not automatically approve usage for every jurisdiction or filing context.

## 10.6 Classification Does Not File Applications

Classification Service defines and validates scope.

Matter/Trademark filing workflows execute filing.

## 10.7 Classification Changes Must Be Auditable

Classification-sensitive operations must preserve actor, source, request context, item change trace and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Trademark Service | Classification may link to Trademark | Trademark owns protection object. |
| Brand Service | Classification may support Brand strategy | Brand owns commercial identity. |
| Jurisdiction Service | Provides jurisdiction context | Jurisdiction owns where/procedure context. |
| Knowledge Service | Provides item/scheme guidance | Knowledge owns governed reference. |
| Document Service | Documents may contain item wording | Document owns artifact lifecycle. |
| Evidence Service | Evidence may support item use | Evidence owns proof layer. |
| Matter Service | Matter may execute classification work | Matter owns execution container. |
| Order Service | Order may request classification work | Order owns commercial request. |
| AI Agent Governance | AI may recommend Classification | Agent Contract governs AI use. |
| Audit Service | Records Classification-sensitive action | Audit owns accountability trail. |
| Event Service | Records Classification events | Event records occurrence. |

---

# 12. Event Usage

Classification Service emits:

```text
ClassificationCreated
ClassificationUpdated
ClassificationStatusChanged
ClassificationItemAdded
ClassificationItemUpdated
ClassificationItemRemoved
ClassificationTrademarkLinked
ClassificationJurisdictionLinked
ClassificationRecommended
ClassificationReviewed
ClassificationApproved
ClassificationRejected
ClassificationValidated
ClassificationArchived
ClassificationReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Item events must reference class and item safely.
- Recommendation events must identify AI/system/human source.
- Review and approval events must preserve reviewer/source where allowed.
- Events must not expose confidential customer product details unnecessarily.
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
PATCH /classifications/{id}/items/{itemId}
DELETE /classifications/{id}/items/{itemId}
POST /classifications/{id}/trademark
POST /classifications/{id}/jurisdiction
POST /classifications/{id}/recommend
POST /classifications/{id}/review
POST /classifications/{id}/validate
POST /classifications/reference/validate
```

API rules:

```text
- APIs must invoke Classification Service operations.
- APIs must distinguish recommendation from approved filing scope.
- APIs must not file trademark applications.
- APIs must not create Trademark unless Trademark Service is invoked.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Classification Service only under governed Agent Contracts.

Allowed AI use:

```text
suggest class candidates
suggest goods/services items
normalize item wording for review
map customer product descriptions to candidate items
identify item/class mismatch
flag jurisdiction-specific review needs
compare evidence with goods/services items
prepare classification draft for human review
```

AI must not:

```text
mark Classification as ApprovedForFiling without governed review
file applications directly
treat recommendation as official acceptable wording without source
ignore jurisdiction limits or review requirements
delete items without governed service
make final legal strategy decision
alter Classification status without authorized service
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

Classification Service must enforce:

```text
[ ] classification_scheme is controlled.
[ ] status is controlled.
[ ] review_status is controlled.
[ ] createClassification requires class_references.
[ ] createClassification requires goods_services_items.
[ ] createClassification produces stable immutable Classification ID.
[ ] updateClassification does not mutate immutable ID.
[ ] changeClassificationStatus follows allowed lifecycle.
[ ] addClassificationItem requires item type and class reference.
[ ] validateClassification rejects class-number-only scope.
[ ] AI recommendation does not become approved filing scope automatically.
[ ] Classification Service does not file applications.
[ ] Classification Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Classification Service should return controlled errors:

```text
ClassificationNotFound
InvalidClassificationScheme
InvalidClassificationStatus
InvalidReviewStatus
InvalidClassificationTransition
ClassReferenceRequired
GoodsServicesItemsRequired
InvalidItemType
InvalidItemReference
TrademarkNotFound
JurisdictionNotFound
SchemeMismatch
ClassNumberOnlyNotAllowed
AIRecommendationNotApproved
ReviewRequired
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownClassificationError
```

Errors must be safe for product display and API consumption.

Confidential customer product data must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite classification domain spec
cite classification object spec
cite trademark and jurisdiction specs where relevant
preserve Classification / Trademark boundary
preserve Classification / Jurisdiction boundary
preserve Classification / AI Recommendation boundary
preserve Classification / Filing boundary
implement only Phase 2 MVP operations unless task says otherwise
write tests for createClassification requiring classification_scheme
write tests for createClassification requiring class_references
write tests for createClassification requiring goods_services_items
write tests for controlled status and review_status
write tests preventing class-number-only Classification
write tests preventing AI recommendation from becoming ApprovedForFiling
write tests preventing Classification Service from filing applications
write tests for event emission on mutation
```

Codex must not:

```text
invent full classification AI engine in Phase 2
treat class number as complete filing scope
treat AI recommendation as approved filing scope
file applications from Classification Service
create Trademark directly from Classification Service
ignore jurisdiction context where required
treat official wording as universally approved
allow product UI to redefine Classification status
```

---

# 18. Acceptance Criteria

This Classification Service Specification is accepted only if:

```text
[ ] It defines Classification Service purpose.
[ ] It defines Classification Service Core meaning.
[ ] It identifies Classification Service as Professional Core Service.
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
| 0.1.0 | Draft | Initial Classification Service specification. Establishes Classification Service as professional goods/services scope service, separates Classification from class number alone, Trademark, Jurisdiction, AI recommendation and filing execution, and defines Phase 2 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
