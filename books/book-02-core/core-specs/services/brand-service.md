# Service Specification — Brand Service

**Spec ID:** B02-SVC-BRAND-SERVICE  
**Spec Type:** Service  
**Service Name:** Brand Service  
**Owning Domain:** Brand  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/brand.md  
**Related Object Specs:** core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/customer.md; core-specs/objects/document.md; core-specs/objects/evidence.md  
**Related Service Specs:** core-specs/services/trademark-service.md; core-specs/services/customer-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/knowledge-service.md  
**Related Event Specs:** core-specs/events/brand-created.md; core-specs/events/brand-updated.md; core-specs/events/brand-status-changed.md; core-specs/events/brand-trademark-linked.md; core-specs/events/brand-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/brand/brand-contract.md; core-specs/contracts/brand/brand-reference-contract.md; core-specs/contracts/brand/brand-trademark-link-contract.md; core-specs/contracts/brand/brand-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Brand Service defines the Core service boundary for creating, updating, validating, linking and managing Brand objects.

It exists so that Trademark, Customer, Matter, Order, Document, Evidence, Knowledge, AI Agents, APIs and product consumers can consistently reference commercial identity without confusing Brand with Trademark, Customer, company name, product category, document asset or AI-generated naming suggestion.

Brand Service is required before:

```text
brand intake
brand profile management
brand-to-customer linkage
brand-to-trademark linkage
brand asset reference governance
brand protection planning
multi-jurisdiction trademark strategy
AI-assisted brand summary
AI-assisted trademark planning
audit trace for brand-sensitive actions
```

---

# 2. Core Meaning

Brand Service means:

```text
the Core service that manages commercial identity references and their governed relationships to customers, trademarks, documents, evidence and professional execution.
```

Brand Service does not mean:

```text
Trademark Service
Customer Service
marketing campaign system
logo design tool
brand strategy engine
company registry service
AI naming generator
legal rights determination service
```

Brand Service answers:

```text
Does this Brand exist?
Who or what does this Brand relate to?
Which Customer owns or manages it?
Which Trademarks protect or relate to it?
Which assets, Documents or Evidence reference it?
Is the Brand active, draft, review-required or archived?
Can another domain safely reference this Brand?
```

---

# 3. Service Category

Brand Service is a Professional Core Service.

It manages commercial identity.

It does not determine trademark rights.

It does not execute trademark procedures.

It does not replace professional brand/trademark judgment.

---

# 4. Architectural Position

Brand Service sits before Trademark Service in professional architecture.

```text
Customer provides demand context
        ↓
Brand Service manages commercial identity
        ↓
Trademark Service manages legal/procedural protection object
        ↓
Jurisdiction and Classification define protection scope
        ↓
Matter executes professional work
        ↓
Document and Evidence support execution
```

Brand is commercial identity.

Trademark is legal/procedural protection object.

Matter executes work.

---

# 5. Scope

Brand Service includes:

```text
brand creation
brand update
brand status management
brand customer linkage
brand trademark linkage
brand document/evidence linkage
brand reference validation
brand audit trace
brand event emission
```

MVP scope includes:

```text
create brand
get brand
update brand metadata
change brand status
link brand to customer
link brand to trademark
validate brand reference
emit brand events
```

Deferred scope includes:

```text
brand valuation
brand strategy scoring
logo generation
marketing campaign management
brand monitoring engine
brand portfolio optimization
advanced similarity analysis
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createBrand | Create Brand object | Yes | BrandCreated |
| getBrand | Retrieve Brand by ID | Yes | No |
| updateBrand | Update governed Brand metadata | Yes | BrandUpdated |
| changeBrandStatus | Change Brand lifecycle status | Yes | BrandStatusChanged |
| linkBrandCustomer | Link Brand to Customer | Yes | BrandCustomerLinked |
| unlinkBrandCustomer | Remove Customer link | Partial | BrandCustomerUnlinked |
| linkBrandTrademark | Link Brand to Trademark | Yes | BrandTrademarkLinked |
| unlinkBrandTrademark | Remove Trademark link | Partial | BrandTrademarkUnlinked |
| validateBrandReference | Validate whether Brand can be referenced | Yes | BrandReferenceValidated |
| archiveBrand | Archive Brand reference | Partial | BrandArchived |

---

# 7. Inputs

Brand Service accepts:

```text
brand_type
brand_name_reference
brand_display_reference
status
customer_reference_id
trademark_reference_id
document_reference_ids
evidence_reference_ids
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
brand_type
brand_name_reference
status
source_reference
actor_context
```

Required for customer linkage:

```text
brand_reference_id
customer_reference_id
link_type
actor_context
```

Required for trademark linkage:

```text
brand_reference_id
trademark_reference_id
link_type
actor_context
```

Required for validation:

```text
brand_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Brand Service returns:

```text
Brand object
Brand reference
Brand validation result
Brand customer link result
Brand trademark link result
Brand status result
Brand event reference
error result
```

Validation output must include:

```text
is_valid
brand_reference_id
status
reason_code
customer_reference_hint where applicable
trademark_reference_hint where applicable
policy_hint where applicable
```

Validation output must not expose unnecessary confidential customer or brand data.

---

# 9. Controlled Values

## 9.1 brand_type

```text
ProductBrand
ServiceBrand
CompanyBrand
PersonalBrand
SeriesBrand
HouseBrand
SubBrand
Unknown
```

## 9.2 status

```text
Draft
Active
ReviewRequired
Inactive
Archived
DeletedReferenceOnly
```

## 9.3 customer_link_type

```text
Owner
Applicant
Manager
AgencyClient
Representative
InterestedParty
Unknown
```

## 9.4 trademark_link_type

```text
PrimaryProtection
RelatedProtection
PlannedProtection
HistoricalProtection
DisputedProtection
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
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Brand Represents Commercial Identity

Brand Service manages the commercial identity layer.

It must not treat Brand as legal/procedural trademark protection.

## 10.2 Brand Is Not Trademark

Brand may be linked to Trademark.

Trademark Service owns legal/procedural protection objects.

## 10.3 Brand Is Not Customer

Brand may be owned, managed or requested by Customer.

Customer Service owns demand-side commercial party context.

## 10.4 Brand Asset Is Not Document Automatically

A logo, file or attachment may reference Brand.

It becomes Document only through Document Service.

## 10.5 Brand Material Is Not Evidence Automatically

Brand usage material may support Evidence.

It becomes Evidence only through Evidence Service with source and purpose.

## 10.6 AI Suggestions Are Not Approved Brand Records

AI may suggest names, summaries or brand relationships.

Brand creation, update and linkage must use Brand Service.

## 10.7 Brand Changes Must Be Auditable

Brand-sensitive operations must preserve actor, source, request context and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Customer Service | Brand may link to Customer | Customer owns demand-side party. |
| Trademark Service | Brand may link to Trademark | Trademark owns protection object. |
| Document Service | Brand may link Documents | Document owns artifact lifecycle. |
| Evidence Service | Brand may link Evidence | Evidence owns proof layer. |
| Knowledge Service | May provide brand guidance | Knowledge owns governed reference. |
| Matter Service | Matter may reference Brand | Matter owns execution container. |
| Order Service | Order may reference Brand | Order owns commercial request. |
| AI Agent Governance | AI may summarize/suggest | Agent Contract governs AI use. |
| Audit Service | Records Brand-sensitive action | Audit owns accountability trail. |
| Event Service | Records Brand events | Event records occurrence. |

---

# 12. Event Usage

Brand Service emits:

```text
BrandCreated
BrandUpdated
BrandStatusChanged
BrandCustomerLinked
BrandCustomerUnlinked
BrandTrademarkLinked
BrandTrademarkUnlinked
BrandArchived
BrandReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Validation events may be emitted where audit requires.
- Events must reference Brand ID.
- Customer link events must reference Customer ID.
- Trademark link events must reference Trademark ID.
- Events must not expose confidential brand or customer metadata unnecessarily.
```

---

# 13. API Usage

Potential Phase 2 APIs:

```text
POST /brands
GET /brands/{id}
PATCH /brands/{id}
POST /brands/{id}/status
POST /brands/{id}/customers
DELETE /brands/{id}/customers/{customerId}
POST /brands/{id}/trademarks
DELETE /brands/{id}/trademarks/{trademarkId}
POST /brands/reference/validate
```

API rules:

```text
- APIs must invoke Brand Service operations.
- APIs must not create Trademark unless Trademark Service is invoked.
- APIs must not create Customer unless Customer Service is invoked.
- APIs must not convert assets into Documents or Evidence automatically.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Brand Service only under governed Agent Contracts.

Allowed AI use:

```text
summarize Brand profile
identify missing Customer link
identify missing Trademark protection link
suggest Brand-Trademark relationship for review
draft brand intake notes
flag Brand / Trademark boundary mismatch
suggest protection planning questions
```

AI must not:

```text
create Brand without authorized service
treat AI-generated name as approved Brand
treat Brand as Trademark
make final registrability or ownership conclusion
convert brand asset into Document automatically
convert brand material into Evidence automatically
alter Brand status without authorized service
```

AI Brand use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Brand Access Rule
Customer Access Rule where applicable
Trademark Access Rule where applicable
Audit Rule
Human Review Rule for professional conclusions or external commitments
```

---

# 15. Validation Rules

Brand Service must enforce:

```text
[ ] brand_type is controlled.
[ ] status is controlled.
[ ] createBrand requires brand_name_reference.
[ ] createBrand produces stable immutable Brand ID.
[ ] updateBrand does not mutate immutable ID.
[ ] changeBrandStatus follows allowed lifecycle.
[ ] linkBrandCustomer references valid Customer where required.
[ ] linkBrandTrademark references valid Trademark.
[ ] validateBrandReference rejects missing, inactive, archived or deleted-reference brands where not allowed.
[ ] Brand Service does not create Trademark directly.
[ ] Brand Service does not convert assets into Documents/Evidence automatically.
[ ] Brand Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Brand Service should return controlled errors:

```text
BrandNotFound
InvalidBrandType
InvalidBrandStatus
InvalidBrandTransition
InvalidBrandReference
BrandNameRequired
CustomerNotFound
InvalidCustomerReference
TrademarkNotFound
InvalidTrademarkReference
DuplicateBrandCustomerLink
DuplicateBrandTrademarkLink
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownBrandError
```

Errors must be safe for product display and API consumption.

Sensitive brand/customer information must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite brand domain spec
cite brand object spec
cite trademark service/object specs where relevant
preserve Brand / Trademark boundary
preserve Brand / Customer boundary
preserve Brand / Document boundary
preserve Brand / Evidence boundary
implement only Phase 2 MVP operations unless task says otherwise
write tests for createBrand requiring brand_name_reference
write tests for controlled brand_type
write tests for controlled status
write tests preventing Brand Service from creating Trademark directly
write tests preventing Brand Service from creating Customer directly
write tests preventing brand asset from becoming Document automatically
write tests preventing brand material from becoming Evidence automatically
write tests for event emission on mutation
```

Codex must not:

```text
invent full brand strategy system in Phase 2
treat Brand as Trademark
treat Brand as Customer
generate approved Brand from AI suggestion
implement logo design or brand valuation inside Brand Service
convert assets into Documents/Evidence automatically
allow AI to make final ownership or registrability conclusion
allow product UI to redefine Brand status
```

---

# 18. Acceptance Criteria

This Brand Service Specification is accepted only if:

```text
[ ] It defines Brand Service purpose.
[ ] It defines Brand Service Core meaning.
[ ] It identifies Brand Service as Professional Core Service.
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
| 0.1.0 | Draft | Initial Brand Service specification. Establishes Brand Service as commercial identity service, separates Brand from Trademark, Customer, Document and Evidence, and defines Phase 2 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
