# Domain Specification — Brand

**Spec ID:** B02-DOM-BRAND  
**Spec Type:** Domain  
**Domain Name:** Brand  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/brand.md; core-specs/objects/brand-asset.md; core-specs/objects/brand-owner-reference.md; core-specs/objects/brand-name.md; core-specs/objects/brand-status.md; core-specs/objects/brand-usage-context.md  
**Related Service Specs:** core-specs/services/brand-registration-service.md; core-specs/services/brand-asset-registration-service.md; core-specs/services/brand-owner-reference-service.md; core-specs/services/brand-reference-validation-service.md; core-specs/services/brand-usage-context-service.md  
**Related Event Specs:** core-specs/events/brand-created.md; core-specs/events/brand-updated.md; core-specs/events/brand-asset-linked.md; core-specs/events/brand-owner-linked.md; core-specs/events/brand-status-changed.md; core-specs/events/brand-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/brand/brand-contract.md; core-specs/contracts/brand/brand-asset-contract.md; core-specs/contracts/brand/brand-owner-reference-contract.md; core-specs/contracts/brand/brand-usage-context-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Brand Domain defines the Core meaning of a commercial, professional or organizational brand identity in MarkOrbit.

It exists so that trademarks, documents, evidence, matters, orders, classifications, jurisdictions, AI recommendations, product intake and professional workflows can refer to the brand being protected, managed or analyzed.

Brand is required before:

```text
trademark intake
trademark record creation
brand-owner reference
logo or word mark asset handling
goods and services recommendation
classification assistance
jurisdiction filing strategy
document drafting
evidence collection
brand portfolio management
opportunity generation
AI brand analysis
```

The Brand Domain is a Professional Domain because it represents the client-side commercial subject that professional trademark services are meant to protect.

---

# 2. Core Meaning

Brand means:

```text
a Core-recognized commercial or organizational identity that may be represented by names, signs, logos, visual assets, usage contexts and ownership references, and may be connected to trademark protection, professional service execution and product consumption.
```

Brand is not merely:

```text
a trademark application
a trademark registration
a logo file
a company name
a product name
a customer record
a marketing campaign
a design asset folder
a social media account
a product listing
an opportunity lead
```

Brand answers:

```text
What commercial identity is being protected or managed?
Which names, signs or assets represent it?
Who appears to own or use it?
Which trademarks, matters, orders, documents and evidence relate to it?
What usage context is relevant to professional judgment?
Can AI, services and workflows reference it consistently?
```

---

# 3. Domain Category

Brand is a Professional Domain.

Professional Domains provide the Core basis for:

```text
brand identity understanding
trademark professional work
jurisdiction-specific filing strategy
classification and goods/services reasoning
document and evidence preparation
client-facing professional explanation
AI-assisted professional recommendation
matter and order context
```

Brand is the professional subject before Trademark, Document, Evidence and Matter execution.

---

# 4. Architectural Position

Brand sits at the entry point of the Professional Core.

```text
Foundation Core provides actor, organization, permission, policy and knowledge
        ↓
Brand defines the commercial identity being protected
        ↓
Trademark represents legal protection records and applications
        ↓
Jurisdiction and Classification define filing context
        ↓
Document and Evidence support professional execution
        ↓
Matter, Order and Workflow operate the service
```

Brand provides commercial/professional context.

Trademark provides legal/procedural protection records.

Brand does not replace Trademark.

Trademark does not replace Brand.

---

# 5. Scope

The Brand Domain includes:

```text
brand definition
brand name
brand sign reference
brand asset boundary
brand owner reference boundary
brand usage context
brand status
brand-to-trademark relationship boundary
brand-to-document relationship boundary
brand-to-evidence relationship boundary
brand reference validation
brand audit reference
brand event emission
brand use by AI Agents, Services, Workflows, APIs and Codex tasks
```

MVP implementation should focus on:

```text
Brand
Brand Name
Brand Asset
Brand Owner Reference
Brand Status
Brand Usage Context
Brand Registration Service
Brand Asset Registration Service
Brand Owner Reference Service
Brand Reference Validation Service
BrandCreated event
BrandAssetLinked event
BrandOwnerLinked event
BrandReferenceValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

The Brand Domain owns:

```text
Core Brand definition
brand name reference
brand sign reference
brand asset reference
brand owner reference boundary
brand status
brand usage context
brand reference validation
brand relationship to trademarks
brand relationship to documents and evidence
brand event emission
brand reference used by professional workflows and products
```

## 6.2 Out of Boundary

The Brand Domain does not own:

```text
trademark application lifecycle
trademark registration status
official filing data
jurisdiction legal rules
Nice classification structure
goods/services official taxonomy
document file lifecycle
evidence proof lifecycle
customer lifecycle
order lifecycle
matter lifecycle
opportunity scoring
brand valuation
marketing strategy
brand design service
logo generation
product listing scraping
social media monitoring
public brand reputation analytics
```

Those responsibilities belong to:

```text
Trademark Domain
Jurisdiction Domain
Classification Domain
Document Domain
Evidence Domain
Customer Domain
Order Domain
Matter Domain
Opportunity Domain
Product implementation
External integration implementation
```

## 6.3 Boundary Notes

Brand is the commercial identity.

Trademark is the legal/procedural protection object.

Brand Asset is a reference to a brand-related sign or material.

Document owns formal files.

Evidence owns proof.

Customer owns commercial relationship.

Matter owns professional service execution.

---

# 7. Domain Rules

## 7.1 Brand Must Be Product-Neutral

Brand must not be defined by a single product's UI, intake form or campaign structure.

Products may collect Brand information, but they must consume the Core Brand model.

## 7.2 Brand Must Support Multiple Representations

A Brand may have:

```text
word name
stylized name
logo
device mark
slogan
Chinese name
English name
transliteration
series mark
product line mark
visual asset reference
```

MVP does not need full brand asset management, but must allow stable references.

## 7.3 Brand Does Not Equal Trademark

A Brand may have zero, one or many related Trademarks.

A Trademark may protect one representation of a Brand.

Trademark status must not be stored as Brand status.

## 7.4 Brand Requires Ownership or Usage Context

Brand should include a Brand Owner Reference or explicit unknown/undetermined ownership status.

Ownership reference does not equal verified legal ownership unless supported by Evidence or official Trademark records.

## 7.5 Brand Must Preserve Professional Context

Brand should support usage context required for professional reasoning.

Usage context may include:

```text
products or services
markets
jurisdictions
online channels
industry
business model
intended filing purpose
existing trademark portfolio
known risk notes
```

MVP may store this as structured baseline context rather than full analytics.

## 7.6 Brand Must Be Auditable

Brand-sensitive actions must preserve audit trace.

Audit-sensitive brand actions include:

```text
brand creation
brand owner reference change
brand asset linking
brand-to-trademark linking
brand status change
AI-generated brand recommendation
classification suggestion based on brand context
jurisdiction strategy based on brand context
```

---

# 8. Primary Objects

The Brand Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Brand | Brand | Must Implement | Core-recognized commercial or organizational brand identity. |
| Brand Name | Brand | Must Implement | Name, word element or textual representation of a Brand. |
| Brand Asset | Brand / Document | Must Implement | Reference to logo, sign, visual material or brand-related asset. |
| Brand Owner Reference | Brand / Customer / Organization | Must Implement | Reference to apparent or declared owner/user of a Brand. |
| Brand Status | Brand | Must Implement | Controlled status indicating Brand usability in Core execution. |
| Brand Usage Context | Brand | Must Implement | Professional context describing how the Brand is used or intended to be used. |
| Brand-Trademark Link | Brand / Trademark | Must Implement | Relationship between Brand and Trademark records. |
| Brand Reference | Brand | Must Implement | Portable reference to Brand used by Services, Events, APIs and Workflows. |
| Brand Audit Reference | Brand / Audit | Partial Implement | Audit reference for brand-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Trademark | Trademark | Trademark may protect a Brand representation. |
| Jurisdiction | Jurisdiction | Brand protection may be planned by jurisdiction. |
| Classification | Classification | Brand usage context supports classification reasoning. |
| Document | Document | Brand assets or application materials may be documents. |
| Evidence | Evidence | Brand use evidence may support ownership or use claims. |
| Customer | Customer | Customer may be owner, applicant or service buyer for Brand. |
| Organization | Organization | Organization may own or manage Brand. |
| Matter | Matter | Matter may be opened for Brand-related service. |
| Order | Order | Order may include Brand-related service request. |
| AI Output | AI Governance | AI may generate brand analysis or recommendations. |
| Knowledge Reference | Knowledge | Brand guidance may cite approved knowledge. |
| Audit Record | Audit | Audit records brand-sensitive actions. |

---

# 9. Primary Services

The Brand Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Brand Registration Service | Brand | Must Implement | Create a Core Brand record. |
| Brand Update Service | Brand | Must Implement | Update controlled Brand fields through governed rules. |
| Brand Asset Registration Service | Brand / Document | Must Implement | Link logo, sign or visual asset reference to Brand. |
| Brand Owner Reference Service | Brand | Must Implement | Create or update declared owner/user reference. |
| Brand Usage Context Service | Brand | Must Implement | Create or update professional usage context. |
| Brand Reference Validation Service | Brand | Must Implement | Validate Brand references used by other domains. |
| Brand-Trademark Link Service | Brand / Trademark | Must Implement | Link Brand to Trademark records. |
| Brand Status Service | Brand | Must Implement | Update Brand status through governed rules. |
| Brand Audit Reference Service | Brand / Audit | Partial Implement | Produce brand audit reference for governed actions. |

Service rules:

```text
- Mutating Brand services must emit events.
- Brand services must not create official Trademark records directly.
- Brand services must not verify legal ownership without Evidence or official records.
- Brand services must not perform classification final judgment.
- Brand services must preserve ownership and usage-context audit trace.
```

---

# 10. Primary Events

The Brand Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| BrandCreated | Brand Registration Service | Must Implement | A Core Brand has been created. |
| BrandUpdated | Brand Update Service | Must Implement | Controlled Brand fields have changed. |
| BrandStatusChanged | Brand Status Service | Must Implement | Brand status has changed. |
| BrandAssetLinked | Brand Asset Registration Service | Must Implement | Brand asset reference has been linked to Brand. |
| BrandOwnerLinked | Brand Owner Reference Service | Must Implement | Owner/user reference has been linked to Brand. |
| BrandUsageContextUpdated | Brand Usage Context Service | Must Implement | Brand usage context has changed. |
| BrandTrademarkLinked | Brand-Trademark Link Service | Must Implement | Brand has been linked to a Trademark record. |
| BrandReferenceValidated | Brand Reference Validation Service | Must Implement | Brand reference has been validated for governed use. |
| BrandOwnershipReviewRequired | Brand Owner Reference Service | Partial Implement | Brand ownership reference requires review or evidence. |
| BrandAssetReviewRequired | Brand Asset Registration Service | Partial Implement | Brand asset requires review before use. |

Event rules:

```text
- Brand events must reference Brand.
- Owner-linked events must distinguish declared ownership from verified ownership.
- Asset-linked events must reference Document or asset reference where applicable.
- Brand events must not expose confidential client materials unnecessarily.
- Review-required events must reference review reason where applicable.
```

---

# 11. Primary Contracts

Brand requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Brand Contract | Brand Contract | Must Implement | Defines Brand fields, status, names and reference behavior. |
| Brand Name Contract | Brand Contract | Must Implement | Defines textual representation and language/script fields. |
| Brand Asset Contract | Brand / Document Contract | Must Implement | Defines asset reference, asset type and source boundary. |
| Brand Owner Reference Contract | Brand / Customer / Organization Contract | Must Implement | Defines declared owner/user reference and verification boundary. |
| Brand Usage Context Contract | Brand Contract | Must Implement | Defines usage context fields used by professional services and AI. |
| Brand-Trademark Link Contract | Brand / Trademark Contract | Must Implement | Defines relationship between Brand and Trademark records. |
| Brand Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for brand-sensitive actions. |

Contract rules:

```text
- Brand Contract must not define Trademark official status.
- Brand Owner Reference Contract must distinguish declared and verified ownership.
- Brand Asset Contract must reference Document or asset source where applicable.
- Brand Usage Context Contract must be reusable by Classification, Jurisdiction, AI and Workflow specs.
```

---

# 12. Relationships to Other Domains

## 12.1 Trademark

Trademark represents legal or procedural trademark protection.

Brand represents commercial identity.

A Brand may link to multiple Trademark records.

## 12.2 Jurisdiction

Jurisdiction defines country, region or office context.

Brand protection strategy may be jurisdiction-scoped.

## 12.3 Classification

Classification uses Brand Usage Context to support goods/services and class recommendations.

Brand does not define final classification.

## 12.4 Document

Document owns formal file lifecycle.

Brand assets may reference Document.

## 12.5 Evidence

Evidence supports proof of use, ownership, reputation or priority.

Brand ownership and use claims may require Evidence.

## 12.6 Customer

Customer may be applicant, owner, buyer or service requester.

Brand does not define customer lifecycle.

## 12.7 Organization

Organization may own, manage or operate a Brand.

Organization does not replace Brand.

## 12.8 Matter and Order

Matter and Order may be opened for Brand-related service.

Brand does not define Matter or Order lifecycle.

## 12.9 Knowledge

Knowledge may provide brand strategy guidance, classification references or jurisdiction references.

Brand does not define Knowledge validity.

## 12.10 AI Governance

AI may assist with brand understanding, class suggestion or filing strategy, but must not replace professional judgment.

## 12.11 Audit

Audit records should include Brand references for brand-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Brand only under governed Agent Contracts.

Allowed AI use:

```text
summarize Brand information
identify missing Brand usage context
suggest possible goods/services based on Brand context
suggest possible jurisdictions based on stated business context
flag possible owner-reference gaps
generate draft intake questions
compare Brand Name with existing Trademark references if authorized
prepare review notes for professional user
```

AI must not:

```text
determine legal ownership as final
make final trademark availability decision
make final classification decision
make final filing strategy decision without review
create Trademark application record without authorized service
treat logo generation as Brand governance
infer confidential business facts beyond approved data
use unauthorized external brand data
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Brand Object Access Rule
Brand Service Access Rule
Brand Event Access Rule
Policy Rule
Review Rule
Audit Rule
Human Review Rule for professional recommendations
```

---

# 14. Workflow Usage

Brand participates in professional workflows.

Brand-sensitive workflows may include:

```text
brand-intake-workflow.md
brand-asset-review-workflow.md
brand-owner-reference-review-workflow.md
brand-to-trademark-link-workflow.md
classification-recommendation-workflow.md
jurisdiction-strategy-workflow.md
trademark-intake-workflow.md
```

Workflow rules:

```text
- Brand workflows must reference Workflow Contracts.
- Brand owner reference changes should be auditable.
- Brand asset review should be required when assets are used in official or client-facing output.
- AI-generated brand recommendations must require review before professional use.
- Brand workflows must not create official filing records without Trademark/Matter services.
```

---

# 15. API Usage

Brand APIs expose brand creation, update, asset linking, owner reference and usage context through governed services.

Potential MVP APIs:

```text
POST /brands
GET /brands/{id}
PATCH /brands/{id}
POST /brands/{id}/assets
POST /brands/{id}/owner-references
POST /brands/{id}/usage-context
POST /brands/{id}/trademark-links
POST /brands/reference/validate
```

Potential partial APIs:

```text
POST /brands/{id}/status
POST /brands/{id}/owner-review
GET /brands/{id}/audit-reference
```

API rules:

```text
- APIs must invoke Brand Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not create official Trademark application lifecycle directly.
- APIs must not expose confidential brand assets without Permission and Policy.
- Mutating APIs must emit or cause service-level events.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

API details belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

## 16.1 MVP Consumers

```text
Workplace
MarkReg
MarkOrbit Lite
AI Agents
Codex Implementation
Validation tools
```

## 16.2 Partial Consumers

```text
Client Portal
Partner Center
Service Platform
Brand Asset Vault baseline
Opportunity Engine baseline
Reporting consumers
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Brand transaction products
Brand valuation products
Brand monitoring products
Public education products
```

Product rule:

```text
Products consume Brand.
Products do not redefine Brand.
```

---

# 17. MVP Scope

Brand is a Phase 2 / Wave 2 Must Implement domain.

MVP includes:

```text
Brand
Brand Name
Brand Asset
Brand Owner Reference
Brand Status
Brand Usage Context
Brand-Trademark Link
Brand Reference
Brand Registration Service
Brand Update Service
Brand Asset Registration Service
Brand Owner Reference Service
Brand Usage Context Service
Brand Reference Validation Service
Brand-Trademark Link Service
BrandCreated event
BrandUpdated event
BrandAssetLinked event
BrandOwnerLinked event
BrandUsageContextUpdated event
BrandTrademarkLinked event
BrandReferenceValidated event
basic brand metadata validation
source traceability to Trademark, Classification, Jurisdiction, Document, Evidence and AI systems
```

MVP should support:

```text
word brand intake
logo or asset reference
declared owner reference
basic product/service usage context
basic jurisdiction interest context
brand-to-trademark relationship
AI-assisted intake support with human review
```

MVP does not require full brand asset vault, valuation, monitoring or transaction platform.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full Brand Asset Vault
advanced logo version management
brand valuation engine
brand transaction marketplace
brand monitoring platform
social media brand monitoring
product listing scraping
brand reputation analytics
automatic brand similarity scoring
brand portfolio optimization engine
brand licensing management
public brand profile pages
advanced brand design workflow
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Brand should use stable immutable ID.
Brand Name should support language/script where possible.
Brand Asset should reference asset source or Document rather than store file meaning directly.
Brand Owner Reference should distinguish declared, inferred, verified and unknown states.
Brand Usage Context should be structured enough to support classification and jurisdiction recommendations.
Brand-Trademark Link should not imply trademark ownership unless supported by Trademark records.
AI-generated brand analysis should produce draft/recommendation output status.
```

Suggested Brand Status values:

```text
Draft
Active
ReviewRequired
Suspended
Archived
Merged
Superseded
DeletedReferenceOnly
```

MVP controlled Brand Status values:

```text
Draft
Active
Archived
```

Suggested Brand Owner Reference Status values:

```text
Declared
VerificationRequired
EvidenceRequired
VerifiedByTrademarkRecord
Disputed
Unknown
```

MVP controlled Brand Owner Reference Status values:

```text
Declared
EvidenceRequired
Unknown
```

Suggested Brand Asset Type values:

```text
Word
Logo
Device
StylizedWord
Slogan
CombinedMark
ProductImage
PackagingImage
DocumentReference
```

MVP controlled Brand Asset Type values:

```text
Word
Logo
Device
StylizedWord
CombinedMark
DocumentReference
```

Do not treat Brand Asset Vault as MVP Core.

---

# 20. Codex Implementation Notes

Codex may implement Brand only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Brand / Trademark boundary
preserve Brand / Document / Evidence boundaries
preserve Brand / Customer / Organization boundary
implement only MVP scope unless task says otherwise
write tests for brand creation
write tests for brand asset linking
write tests for owner reference linking
write tests for brand usage context
write tests for brand-to-trademark link
write tests preventing Trademark status from being stored as Brand status
write tests preventing full Brand Asset Vault implementation in MVP
```

Codex must not:

```text
invent trademark application lifecycle inside Brand
invent classification final decision inside Brand
invent legal ownership verification without Evidence or Trademark records
implement brand valuation or marketplace in MVP
implement social monitoring or scraping in MVP
treat logo generation as Brand Core
treat customer record as Brand
create AI brand recommendations without Agent Contract and review rules
```

---

# 21. Validation Rules

Brand Domain must pass the following checks.

```text
[ ] Brand is classified as Professional Domain.
[ ] Brand is counted within the 26 baseline Core Domains.
[ ] Brand does not change the baseline Core Domain Map.
[ ] Brand has MVP Phase 2 / Wave 2 classification.
[ ] Brand has MVP Depth = Must Implement.
[ ] Brand defines Core meaning.
[ ] Brand boundary excludes Trademark lifecycle.
[ ] Brand boundary excludes Document and Evidence lifecycle.
[ ] Brand boundary excludes Customer lifecycle.
[ ] Brand boundary excludes valuation, monitoring and marketplace scope.
[ ] Brand owns Brand object.
[ ] Brand defines Brand Name.
[ ] Brand defines Brand Asset.
[ ] Brand defines Brand Owner Reference.
[ ] Brand defines Brand Usage Context.
[ ] Brand lists primary services.
[ ] Mutating Brand services emit events.
[ ] Brand lists primary events.
[ ] Brand defines contract requirements.
[ ] Brand defines AI Agent usage constraints.
[ ] Brand defines workflow usage constraints.
[ ] Brand defines API usage constraints.
[ ] Brand defines product consumers.
[ ] Brand defines MVP and deferred scope.
[ ] Brand defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Brand into Trademark
turn Brand into official trademark application lifecycle
turn Brand into Customer
turn Brand into Document
turn Brand into Evidence
turn Brand into marketing campaign management
turn Brand into brand valuation engine
turn Brand into transaction marketplace
turn Brand into social monitoring platform
treat declared ownership as verified ownership without Evidence or official record
allow AI to make final legal ownership or filing decision
implement full Brand Asset Vault in MVP
allow product UI to redefine Brand meaning
allow Codex to define new brand architecture
```

---

# 23. Acceptance Criteria

This Brand Domain Specification is accepted only if:

```text
[ ] It defines Brand purpose.
[ ] It defines Brand Core meaning.
[ ] It identifies Brand as Professional Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Trademark, Jurisdiction, Classification, Document, Evidence, Customer, Organization, Matter, Order, Knowledge, AI Governance and Audit.
[ ] It defines AI Agent usage.
[ ] It defines workflow usage.
[ ] It defines API usage.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Brand Domain specification. Establishes Brand as Phase 2 Professional Domain, defines Brand, Brand Name, Brand Asset, Owner Reference, Usage Context, Brand-Trademark Link, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
