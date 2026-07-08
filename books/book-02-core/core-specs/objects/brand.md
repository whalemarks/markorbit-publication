# Object Specification — Brand

**Spec ID:** B02-OBJ-BRAND  
**Spec Type:** Object  
**Object Name:** Brand  
**Owning Domain:** Brand  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/brand.md  
**Related Object Specs:** core-specs/objects/brand-profile.md; core-specs/objects/brand-name.md; core-specs/objects/brand-owner-reference.md; core-specs/objects/brand-status.md; core-specs/objects/brand-asset-reference.md; core-specs/objects/trademark.md  
**Related Service Specs:** core-specs/services/brand-registration-service.md; core-specs/services/brand-profile-service.md; core-specs/services/brand-owner-reference-service.md; core-specs/services/brand-asset-reference-service.md; core-specs/services/brand-reference-validation-service.md  
**Related Event Specs:** core-specs/events/brand-created.md; core-specs/events/brand-updated.md; core-specs/events/brand-owner-linked.md; core-specs/events/brand-asset-linked.md; core-specs/events/brand-status-changed.md; core-specs/events/brand-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/brand/brand-contract.md; core-specs/contracts/brand/brand-profile-contract.md; core-specs/contracts/brand/brand-owner-reference-contract.md; core-specs/contracts/brand/brand-asset-reference-contract.md; core-specs/contracts/brand/brand-trademark-link-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Brand object defines the Core-recognized commercial identity that may be protected, managed, analyzed, searched, filed, commercialized or connected to trademarks.

It exists so that Trademark, Customer, Matter, Order, Opportunity, Classification, Document, Evidence, AI Agents, Services, APIs and product consumers can consistently reference the brand concept without confusing it with trademark application records, legal rights, customer accounts, products or marketing copy.

Brand is required before:

```text
brand intake
trademark planning
brand-trademark relationship
brand owner reference
brand asset management
multi-jurisdiction filing strategy
classification recommendation
document preparation
evidence collection
opportunity generation
AI brand analysis
client-facing brand workspace
```

---

# 2. Core Meaning

Brand means:

```text
a Core-recognized commercial identity, name, sign, logo, expression or business-facing brand concept that may be associated with one or more trademark protection objects.
```

Brand is not:

```text
Trademark
Trademark Application
Trademark Registration
Customer
Organization
Product
Document
Evidence
Marketing Campaign
Legal Right by itself
Official Filing Record
```

Brand answers:

```text
What commercial identity is being protected or managed?
Who is associated with the brand?
Which brand names, logos or assets exist?
Which trademarks relate to the brand?
Which jurisdictions, classes, goods/services or matters may involve it?
What status, source and audit trace apply?
```

---

# 3. Object Category

Brand is a Professional Object owned by the Brand Domain.

It is the commercial identity layer.

It may link to Trademark, but it must not replace Trademark.

Trademark is the legal/procedural protection object.

Brand is the business/commercial identity object.

---

# 4. Architectural Position

Brand sits before Trademark in professional value flow.

```text
Customer expresses commercial need
        ↓
Brand captures commercial identity
        ↓
Trademark protects Brand in legal/procedural systems
        ↓
Classification defines goods/services scope
        ↓
Matter executes professional work
        ↓
Document and Evidence support procedure
```

Brand provides meaning and context.

Trademark provides legal/procedural protection object.

---

# 5. Scope

The Brand object includes:

```text
brand id
brand type
brand name/reference
brand status
brand owner reference
brand profile reference
brand asset reference
brand language/script reference
brand market/use reference
brand trademark relationship
brand customer relationship
brand source reference
brand notes boundary
created time
updated time
audit metadata
```

MVP scope includes:

```text
brand id
brand type
brand name/reference
brand status
brand owner reference
brand customer reference
brand asset reference
brand trademark link reference
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Brand ID. |
| brand_type | enum | Yes | Yes | Word, Logo, Combined, Slogan, Series, TradeName, ProductLine, Unknown. |
| name_reference | string | Yes | Yes | Primary brand name or display reference. |
| normalized_name | string | No | Yes | Normalized text for search/matching. |
| status | enum | Yes | Yes | Controlled Brand status. |
| owner_reference_id | string | No | Yes | Brand owner reference; may link Customer/Organization/Identity. |
| customer_reference_id | string | No | Yes | Customer relationship reference where applicable. |
| profile_reference_id | string | No | Partial | Brand profile reference. |
| asset_references | array | No | Yes | Logo/image/file references; not automatically Document or Evidence. |
| trademark_references | array | No | Yes | Related Trademark references. |
| language_reference | string | No | Partial | Language/script note. |
| market_reference | string | No | Deferred | Market/use context reference. |
| source_reference | string | No | Yes | Intake/import/source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 brand_type

MVP controlled values:

```text
Word
Logo
Combined
Slogan
Series
TradeName
ProductLine
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
Active
ReviewRequired
Archived
DeletedReferenceOnly
```

## 7.3 asset_reference_type

Suggested controlled values:

```text
Logo
WordmarkImage
PackagingImage
ProductImage
StorefrontImage
MarketingImage
Other
```

Asset references do not automatically become Documents or Evidence.

---

# 8. Object Rules

## 8.1 Brand Requires Name or Asset Reference

Every Brand must have at least one of:

```text
name_reference
asset_reference
```

A Brand without name or asset reference is not Core-valid.

## 8.2 Brand Does Not Equal Trademark

Brand is commercial identity.

Trademark is legal/procedural protection object.

A Brand may have zero, one or many Trademark references.

A Trademark may protect one Brand or be associated with multiple Brand contexts where governed.

## 8.3 Brand Does Not Prove Ownership

Brand owner reference is a business/professional reference.

It is not legal ownership proof by itself.

Legal ownership proof must be handled through Document/Evidence where required.

## 8.4 Brand Assets Are Not Documents or Evidence Automatically

Logo images, packaging images and marketing files attached to Brand are asset references.

They become Documents or Evidence only through governed Document or Evidence services.

## 8.5 Brand Must Support Professional Context

Brand should support trademark planning, jurisdiction strategy, classification, document preparation and evidence review.

## 8.6 Brand Must Be Auditable

Brand-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
brand creation
brand name update
brand owner reference update
brand asset linking
brand trademark link
brand status change
brand archival
AI brand analysis
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Customer | Brand may be linked to Customer | Customer remains demand-side party. |
| Organization | Brand owner may reference Organization | Organization is not legal ownership proof. |
| Trademark | Brand may link to Trademark | Trademark remains legal/procedural object. |
| Classification | Brand may guide class/goods planning | Classification owns goods/services scope. |
| Jurisdiction | Brand may be planned by jurisdiction | Jurisdiction remains where protection applies. |
| Document | Brand assets may become Documents through service | Brand does not own Document lifecycle. |
| Evidence | Brand use material may become Evidence through service | Brand does not own Evidence proof status. |
| Matter | Matter may be opened for Brand | Matter remains execution container. |
| Order | Order may request service for Brand | Order remains commercial service request. |
| Opportunity | Opportunity may be generated from Brand | Opportunity remains potential service need. |
| AI Output | AI may analyze Brand | AI Output is not Brand truth. |
| Audit Record | Audit may reference Brand | Audit remains accountability system. |

---

# 10. Lifecycle

Brand lifecycle states:

```text
Draft
Active
ReviewRequired
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → Active
Draft → ReviewRequired
ReviewRequired → Active
Active → ReviewRequired
Active → Archived
Draft → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Archived → Active without restoration service and review
DeletedReferenceOnly → Active
Active → DeletedReferenceOnly without archival or governed deletion
```

---

# 11. Service Usage

Brand object is created and managed through:

```text
Brand Registration Service
Brand Profile Service
Brand Owner Reference Service
Brand Asset Reference Service
Brand Trademark Link Service
Brand Status Service
Brand Reference Validation Service
Brand Audit Reference Service
```

Service rules:

```text
- Services must validate brand_type.
- Services must require name or asset reference.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not create Trademark directly unless Trademark service is invoked.
- Services must not convert assets into Document or Evidence directly.
```

---

# 12. Event Usage

Brand object emits or participates in:

```text
BrandCreated
BrandUpdated
BrandStatusChanged
BrandOwnerLinked
BrandAssetLinked
BrandTrademarkLinked
BrandArchived
BrandReferenceValidated
```

Event rules:

```text
- Brand events must reference Brand ID.
- Name update events should preserve previous and new reference where allowed.
- Asset events must reference asset reference only.
- Trademark link events must reference Trademark ID.
- Events must not expose protected assets unnecessarily.
```

---

# 13. API Usage

Potential Phase 2 APIs:

```text
POST /brands
GET /brands/{id}
PATCH /brands/{id}
POST /brands/{id}/status
POST /brands/{id}/assets
POST /brands/{id}/trademarks
POST /brands/reference/validate
```

API rules:

```text
- APIs must invoke Brand Services.
- APIs must not create Trademark unless Trademark service is invoked.
- APIs must not convert asset references into Document or Evidence.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract.
```

---

# 14. AI Agent Usage

AI Agents may use Brand only under governed Agent Contracts.

Allowed AI use:

```text
summarize brand profile
normalize brand name
identify possible brand type
suggest trademark planning questions
suggest classification starting points
flag missing brand owner reference
flag brand/trademark boundary mismatch
generate brand intake notes for review
```

AI must not:

```text
treat Brand as legal right
create Trademark directly from Brand without governed service
prove ownership from brand owner reference
convert brand assets into Evidence automatically
make final registrability or infringement conclusion
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
Trademark Access Rule where applicable
Audit Rule
Human Review Rule for professional conclusions
```

---

# 15. Validation Rules

Brand object must pass:

```text
[ ] id is present and immutable.
[ ] brand_type is controlled.
[ ] status is controlled.
[ ] name_reference or asset_reference is present.
[ ] Brand does not equal Trademark.
[ ] Brand owner reference is not legal proof by itself.
[ ] Brand assets do not become Document or Evidence automatically.
[ ] Trademark links reference valid Trademark objects.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite brand domain spec
preserve Brand / Trademark boundary
preserve Brand / Customer boundary
preserve Brand / Document / Evidence boundaries
implement only MVP fields unless task says otherwise
write tests for required name_reference or asset_reference
write tests for controlled brand_type
write tests for controlled status
write tests preventing Brand from becoming Trademark
write tests preventing asset references from becoming Document/Evidence automatically
write tests for Brand-Trademark link integrity
write tests for event emission on mutation
```

Codex must not:

```text
invent brand marketing system inside Brand object
treat Brand as legal right
create Trademark automatically from Brand
treat uploaded logo as Evidence automatically
treat owner reference as legal proof
allow AI to make final legal conclusions from Brand alone
allow product UI to redefine Brand status
```

---

# 17. Acceptance Criteria

This Brand Object Specification is accepted only if:

```text
[ ] It defines Brand purpose.
[ ] It defines Brand Core meaning.
[ ] It identifies Brand as Professional Object.
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
| 0.1.0 | Draft | Initial Brand object specification. Establishes Brand as commercial identity object, separates Brand from Trademark, Customer, Document and Evidence, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
