# Domain Specification — Classification

**Spec ID:** B02-DOM-CLASSIFICATION  
**Spec Type:** Domain  
**Domain Name:** Classification  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/classification.md; core-specs/objects/class-reference.md; core-specs/objects/goods-services-item.md; core-specs/objects/goods-services-set.md; core-specs/objects/classification-suggestion.md; core-specs/objects/classification-review-record.md; core-specs/objects/classification-source-reference.md  
**Related Service Specs:** core-specs/services/classification-reference-service.md; core-specs/services/goods-services-normalization-service.md; core-specs/services/classification-suggestion-service.md; core-specs/services/classification-review-service.md; core-specs/services/classification-jurisdiction-scope-service.md; core-specs/services/classification-reference-validation-service.md  
**Related Event Specs:** core-specs/events/classification-reference-created.md; core-specs/events/goods-services-item-created.md; core-specs/events/goods-services-set-updated.md; core-specs/events/classification-suggestion-created.md; core-specs/events/classification-review-required.md; core-specs/events/classification-review-approved.md; core-specs/events/classification-review-rejected.md; core-specs/events/classification-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/classification/classification-contract.md; core-specs/contracts/classification/class-reference-contract.md; core-specs/contracts/classification/goods-services-item-contract.md; core-specs/contracts/classification/goods-services-set-contract.md; core-specs/contracts/classification/classification-suggestion-contract.md; core-specs/contracts/classification/classification-review-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Classification Domain defines the Core meaning of trademark classification, class references, goods/services items, goods/services sets, classification suggestions and professional classification review in MarkOrbit.

It exists so that Brand, Trademark, Jurisdiction, Document, Evidence, Matter, Order, AI Agents and product consumers can consistently handle the professional question:

```text
Which goods or services should this trademark cover, and how should they be classified?
```

Classification is required before:

```text
trademark intake
goods/services recommendation
Nice class reference
jurisdiction-specific goods/services review
filing scope planning
official goods/services drafting
class-based fee estimation
document drafting
evidence preparation
AI classification assistance
professional classification review
client-facing filing proposal
Codex implementation of trademark intake and review workflows
```

The Classification Domain is a Professional Domain because goods/services and class scope directly affect trademark filing strategy, cost, protection scope and professional risk.

---

# 2. Core Meaning

Classification means:

```text
a governed Core professional structure for representing, suggesting, reviewing and validating trademark goods/services items, classes and class-related scope, including jurisdiction-sensitive classification constraints and source references.
```

Classification is not merely:

```text
a Nice class number
a product category
a product taxonomy
an e-commerce category
a price tier
a filing package
a text input field
an AI-generated list
a goods/services translation
a legal conclusion by itself
```

Classification answers:

```text
What goods or services are being claimed or considered?
Which class or classes may apply?
What source supports the class reference?
Which jurisdiction constraints apply?
Is this goods/services wording approved, suggested, draft, rejected or review-required?
Which professional user reviewed it?
Can the goods/services scope be used for trademark filing, quote, document or client proposal?
```

---

# 3. Domain Category

Classification is a Professional Domain.

Professional Domains provide the Core basis for:

```text
goods/services understanding
class scope management
Nice class reference
jurisdiction-specific classification constraints
trademark filing scope
filing fee basis
AI-assisted class suggestion
professional review
client-facing explanation
```

Classification supports Brand and Trademark and is constrained by Jurisdiction.

---

# 4. Architectural Position

Classification sits beside Trademark and Jurisdiction in the Professional Core.

```text
Brand defines the commercial identity
        ↓
Trademark defines the protection record or intended protection
        ↓
Jurisdiction defines where protection applies
        ↓
Classification defines goods/services and class scope
        ↓
Document and Evidence support filing and prosecution
        ↓
Matter, Order and Workflow execute the service
```

Classification is the professional bridge between what the brand does and what the trademark filing should cover.

Classification does not replace Brand.

Classification does not replace Trademark.

Classification does not replace Jurisdiction.

---

# 5. Scope

The Classification Domain includes:

```text
classification definition
class reference
Nice class reference boundary
goods/services item
goods/services set
goods/services wording
goods/services source reference
goods/services status
classification suggestion
classification review record
classification jurisdiction scope
classification source reference
classification translation boundary
classification audit reference
classification event emission
classification use by AI Agents, Services, Workflows, APIs and Codex tasks
```

MVP implementation should focus on:

```text
Classification
Class Reference
Goods/Services Item
Goods/Services Set
Classification Suggestion
Classification Review Record
Classification Source Reference
Classification Reference Service
Goods/Services Normalization Service
Classification Suggestion Service
Classification Review Service
Classification Reference Validation Service
ClassificationReferenceCreated event
GoodsServicesItemCreated event
GoodsServicesSetUpdated event
ClassificationSuggestionCreated event
ClassificationReviewRequired event
ClassificationReviewApproved event
ClassificationReviewRejected event
```

---

# 6. Boundary

## 6.1 In Boundary

The Classification Domain owns:

```text
Core Classification definition
class reference
goods/services item meaning
goods/services set meaning
classification suggestion boundary
classification review boundary
classification status
classification source reference
classification jurisdiction scope reference
classification validation
classification event emission
classification reference used by professional workflows and products
```

## 6.2 Out of Boundary

The Classification Domain does not own:

```text
Brand commercial identity
Trademark lifecycle
Jurisdiction legal rule definition
official Nice database ingestion as infrastructure
official filing submission automation
document file lifecycle
evidence proof lifecycle
translation management as full system
fee calculation engine
matter lifecycle
order lifecycle
AI model behavior
final legal filing decision without review
product UI class selection wizard
e-commerce product taxonomy
```

Those responsibilities belong to:

```text
Brand Domain
Trademark Domain
Jurisdiction Domain
Document Domain
Evidence Domain
Matter Domain
Order Domain
Knowledge Domain
AI Governance
Workflow Contract system
Product implementation
External integration implementation
```

## 6.3 Boundary Notes

Classification owns goods/services and class meaning.

Jurisdiction owns where the classification applies and may reference jurisdiction-specific constraints.

Knowledge owns source-aware classification guidance.

AI Governance owns AI classification assistant behavior and review controls.

Document owns generated filing documents.

Order owns commercial quote and fee presentation.

---

# 7. Domain Rules

## 7.1 Classification Requires Goods/Services Meaning

Classification must represent actual goods/services meaning, not only a class number.

A class number without goods/services wording is insufficient for professional trademark filing scope.

## 7.2 Classification Must Preserve Original Wording

Original user-provided or source-provided goods/services wording must be preserved when normalization, translation or professional revision occurs.

MVP should support:

```text
original wording
normalized wording
reviewed wording
jurisdiction-specific wording
source reference
status
```

## 7.3 Classification Must Distinguish Suggestion from Approved Scope

AI or system suggestions must not be treated as approved filing scope.

Classification outputs must distinguish:

```text
Draft
Suggested
ReviewRequired
Reviewed
Approved
Rejected
Superseded
```

## 7.4 Classification Is Jurisdiction-Sensitive

Some jurisdictions impose goods/services limitations, class count rules, subclass practices, item count limits, official wording preferences or extra fees.

Jurisdiction-specific constraints must be represented through Jurisdiction and Knowledge references, not hard-coded assumptions.

## 7.5 Classification Must Be Reviewable

Professional review is required before classification suggestions become filing-ready or client-facing final recommendations.

High-risk classification decisions must create review records.

## 7.6 Classification Must Be Auditable

Classification-sensitive actions must preserve audit trace.

Audit-sensitive classification actions include:

```text
goods/services creation
goods/services normalization
class assignment
classification suggestion
classification review approval
classification review rejection
jurisdiction-specific wording update
class-based fee basis update
AI classification recommendation
client-facing class proposal generation
```

---

# 8. Primary Objects

The Classification Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Classification | Classification | Must Implement | Core professional structure for class and goods/services scope. |
| Class Reference | Classification | Must Implement | Reference to class number or class system entry. |
| Goods/Services Item | Classification | Must Implement | Individual goods or services wording item. |
| Goods/Services Set | Classification | Must Implement | Group of goods/services items associated with Brand, Trademark, Order or Matter. |
| Goods/Services Status | Classification | Must Implement | Controlled status for wording or item usability. |
| Classification Suggestion | Classification / AI Governance | Must Implement | Draft recommendation for class or goods/services scope. |
| Classification Review Record | Classification / Review and Approval | Must Implement | Professional review record for classification output. |
| Classification Source Reference | Classification / Knowledge | Must Implement | Source reference supporting classification guidance or wording. |
| Classification Jurisdiction Scope | Classification / Jurisdiction | Must Implement | Jurisdiction-sensitive applicability of classification wording. |
| Classification Audit Reference | Classification / Audit | Partial Implement | Audit reference for classification-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Brand | Brand | Brand usage context supports classification. |
| Trademark | Trademark | Trademark goods/services reference Classification. |
| Jurisdiction | Jurisdiction | Jurisdiction constrains classification use. |
| Document | Document | Filing documents may use approved classification wording. |
| Evidence | Evidence | Evidence may support use of goods/services. |
| Knowledge Reference | Knowledge | Classification guidance must cite source where applicable. |
| AI Output | AI Governance | AI may create classification suggestions. |
| Review Record | Review and Approval | Professional review approves or rejects classification output. |
| Order | Order | Class count may affect pricing and service scope. |
| Matter | Matter | Classification review may be a matter task. |
| Audit Record | Audit | Audit records classification-sensitive actions. |

---

# 9. Primary Services

The Classification Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Classification Reference Service | Classification | Must Implement | Create, resolve and validate Classification and Class References. |
| Goods/Services Item Service | Classification | Must Implement | Create or update goods/services items. |
| Goods/Services Set Service | Classification | Must Implement | Create or update goods/services sets. |
| Goods/Services Normalization Service | Classification | Must Implement | Normalize wording while preserving original wording and trace. |
| Classification Suggestion Service | Classification / AI Governance | Must Implement | Create draft classification suggestions. |
| Classification Review Service | Classification / Review and Approval | Must Implement | Review, approve or reject classification suggestions or wording. |
| Classification Jurisdiction Scope Service | Classification / Jurisdiction | Must Implement | Validate jurisdiction-sensitive classification applicability. |
| Classification Source Reference Service | Classification / Knowledge | Must Implement | Link classification output to source references. |
| Classification Reference Validation Service | Classification | Must Implement | Validate classification references used by other domains. |
| Classification Audit Reference Service | Classification / Audit | Partial Implement | Produce classification audit reference for governed actions. |

Service rules:

```text
- Mutating Classification services must emit events.
- Suggestion services must mark outputs as Draft, Suggested or ReviewRequired.
- Review service must create or update review records.
- Normalization service must preserve original wording.
- Jurisdiction scope service must not invent legal rules without source.
- AI-assisted classification must require Agent Contract and audit.
```

---

# 10. Primary Events

The Classification Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| ClassificationReferenceCreated | Classification Reference Service | Must Implement | A Classification or Class Reference has been created. |
| ClassificationReferenceValidated | Classification Reference Validation Service | Must Implement | Classification reference has been validated for governed use. |
| GoodsServicesItemCreated | Goods/Services Item Service | Must Implement | Goods/services item has been created. |
| GoodsServicesItemUpdated | Goods/Services Item Service | Must Implement | Goods/services item wording or status has changed. |
| GoodsServicesSetCreated | Goods/Services Set Service | Must Implement | Goods/services set has been created. |
| GoodsServicesSetUpdated | Goods/Services Set Service | Must Implement | Goods/services set has changed. |
| GoodsServicesNormalized | Goods/Services Normalization Service | Must Implement | Wording has been normalized with trace to original. |
| ClassificationSuggestionCreated | Classification Suggestion Service | Must Implement | Draft classification suggestion has been created. |
| ClassificationReviewRequired | Classification Suggestion Service / Review Service | Must Implement | Classification output requires professional review. |
| ClassificationReviewApproved | Classification Review Service | Must Implement | Classification output has been approved. |
| ClassificationReviewRejected | Classification Review Service | Must Implement | Classification output has been rejected. |
| ClassificationJurisdictionScopeValidated | Classification Jurisdiction Scope Service | Must Implement | Jurisdiction-sensitive classification scope has been validated. |
| ClassificationSourceLinked | Classification Source Reference Service | Partial Implement | Source reference has been linked to classification output. |

Event rules:

```text
- Classification events must reference Classification or Goods/Services object.
- Suggestion events must distinguish AI/system suggestion from professional review.
- Review events must reference reviewer or review record.
- Normalization events must preserve original and normalized wording references.
- Jurisdiction-scope events must reference Jurisdiction.
```

---

# 11. Primary Contracts

Classification requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Classification Contract | Classification Contract | Must Implement | Defines Classification fields, class references, scope and status. |
| Class Reference Contract | Classification Contract | Must Implement | Defines class number/system reference and source boundary. |
| Goods/Services Item Contract | Classification Contract | Must Implement | Defines wording, language, source, status and review fields. |
| Goods/Services Set Contract | Classification Contract | Must Implement | Defines grouped goods/services items and class relationships. |
| Classification Suggestion Contract | Classification / AI Contract | Must Implement | Defines suggestion source, confidence boundary, output status and review requirement. |
| Classification Review Contract | Classification / Review Contract | Must Implement | Defines review input, reviewer, decision and result status. |
| Classification Jurisdiction Scope Contract | Classification / Jurisdiction Contract | Must Implement | Defines jurisdiction-specific scope or constraint references. |
| Classification Source Reference Contract | Classification / Knowledge Contract | Must Implement | Defines source reference behavior for classification guidance. |
| Classification Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for classification-sensitive actions. |

Contract rules:

```text
- Goods/Services Item Contract must preserve original wording.
- Classification Suggestion Contract must not represent approved filing scope.
- Review Contract must distinguish approved, rejected and review-required output.
- Jurisdiction Scope Contract must reference Jurisdiction and source where applicable.
```

---

# 12. Relationships to Other Domains

## 12.1 Brand

Brand Usage Context supports classification.

Classification may use brand products, services, markets and channels to suggest classes and wording.

## 12.2 Trademark

Trademark Goods/Services should reference Classification objects.

Classification defines goods/services scope, while Trademark defines the protection record.

## 12.3 Jurisdiction

Jurisdiction may constrain classification wording, class count, official terms, subclass practices or fee implications.

Classification must be jurisdiction-aware when used for filing strategy.

## 12.4 Document

Document may use approved goods/services wording for filings, POAs, instructions or client proposals.

Classification does not own document lifecycle.

## 12.5 Evidence

Evidence may support claimed use for goods/services.

Classification does not own proof lifecycle.

## 12.6 Knowledge

Knowledge provides source-aware classification references and guidance.

Classification suggestions should cite Knowledge where applicable.

## 12.7 Order

Class count and goods/services scope may affect quotes or order scope.

Classification does not own pricing.

## 12.8 Matter

Classification review may be a professional matter task.

Matter owns execution lifecycle.

## 12.9 AI Governance

AI may create classification suggestions but cannot approve them as final filing scope.

AI output requires Agent Contract, review and audit.

## 12.10 Audit

Audit records should include classification references for classification-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Classification only under governed Agent Contracts.

Allowed AI use:

```text
suggest possible classes based on Brand Usage Context
draft goods/services wording
normalize user-provided goods/services wording
identify missing goods/services information
flag jurisdiction-specific wording risk
prepare classification review notes
compare suggested goods/services with approved Knowledge references
summarize classification rationale with citations
```

AI must not:

```text
approve classification output as final filing scope
make final legal classification decision without human review
invent official wording without source label
silently delete user-provided goods/services wording
ignore jurisdiction-specific constraints
treat high-confidence AI output as reviewed output
submit official filings
change Trademark goods/services without governed service and review
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Classification Object Access Rule
Classification Service Access Rule
Classification Event Access Rule
Jurisdiction Scope Rule
Knowledge Citation Rule
Policy Rule
Review Rule
Audit Rule
Human Review Rule for filing-ready output
```

---

# 14. Workflow Usage

Classification participates in professional workflows.

Classification-sensitive workflows may include:

```text
classification-suggestion-workflow.md
classification-review-workflow.md
goods-services-normalization-workflow.md
jurisdiction-classification-review-workflow.md
trademark-goods-services-review-workflow.md
ai-classification-output-review-workflow.md
client-classification-confirmation-workflow.md
```

Workflow rules:

```text
- Classification workflows must reference Workflow Contracts.
- AI-generated suggestions must require review before filing-ready use.
- Normalized wording must preserve original wording trace.
- Jurisdiction-sensitive classification must cite source or require review.
- Classification approval must create review record and audit reference.
```

---

# 15. API Usage

Classification APIs expose class references, goods/services items, suggestions and review through governed services.

Potential MVP APIs:

```text
POST /classifications
GET /classifications/{id}
POST /classifications/class-references
POST /classifications/goods-services/items
POST /classifications/goods-services/sets
POST /classifications/goods-services/normalize
POST /classifications/suggestions
POST /classifications/reviews
POST /classifications/jurisdiction-scope/validate
POST /classifications/reference/validate
```

Potential partial APIs:

```text
POST /classifications/source-references
GET /classifications/{id}/audit-reference
POST /classifications/suggestions/{id}/review-required
```

API rules:

```text
- APIs must invoke Classification Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not expose AI suggestions as approved filing scope.
- APIs must not submit official filings.
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
Opportunity Engine baseline
Reporting consumers
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Official filing connectors
Classification analytics
Trademark portfolio optimization products
Public self-service filing assistant
```

Product rule:

```text
Products consume Classification.
Products do not redefine Classification.
```

---

# 17. MVP Scope

Classification is a Phase 2 / Wave 2 Must Implement domain.

MVP includes:

```text
Classification
Class Reference
Goods/Services Item
Goods/Services Set
Goods/Services Status
Classification Suggestion
Classification Review Record
Classification Source Reference
Classification Jurisdiction Scope
Classification Reference Service
Goods/Services Item Service
Goods/Services Set Service
Goods/Services Normalization Service
Classification Suggestion Service
Classification Review Service
Classification Jurisdiction Scope Service
Classification Reference Validation Service
ClassificationReferenceCreated event
GoodsServicesItemCreated event
GoodsServicesItemUpdated event
GoodsServicesSetCreated event
GoodsServicesSetUpdated event
GoodsServicesNormalized event
ClassificationSuggestionCreated event
ClassificationReviewRequired event
ClassificationReviewApproved event
ClassificationReviewRejected event
ClassificationJurisdictionScopeValidated event
basic classification metadata validation
source traceability to Brand, Trademark, Jurisdiction, Knowledge and AI systems
```

MVP should support:

```text
basic class reference
basic goods/services item
basic goods/services set
AI-assisted classification suggestion
professional review approval/rejection
jurisdiction-sensitive validation boundary
original wording preservation
classification source reference
```

MVP does not require official Nice database ingestion, full auto-classification engine or official filing automation.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full Nice database ingestion
multi-jurisdiction official wording database
automatic subclass engine
automatic fee optimization by class/item count
full auto-classification engine
AI-only filing scope approval
official filing connector integration
e-commerce product taxonomy importer
large-scale product listing classifier
class similarity analytics
conflict risk scoring by classification
multi-language professional translation workflow
public self-service classification wizard
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Classification should use stable immutable ID.
Goods/Services Item should preserve original wording.
Normalized wording must not overwrite original wording.
Classification Suggestion should have source and output status.
Review-approved wording should reference review record.
Class Reference should be controlled and source-aware.
Jurisdiction scope should reference Jurisdiction and source where applicable.
AI suggestions should produce draft/recommendation output status.
```

Suggested Goods/Services Status values:

```text
Draft
Suggested
ReviewRequired
Reviewed
Approved
Rejected
Superseded
Archived
```

MVP controlled Goods/Services Status values:

```text
Draft
Suggested
ReviewRequired
Approved
Rejected
```

Suggested Classification Suggestion Source values:

```text
HumanDraft
AIRecommendation
KnowledgeReference
OfficialReference
AgentReport
ClientProvided
InternalTemplate
```

MVP controlled suggestion source values:

```text
HumanDraft
AIRecommendation
KnowledgeReference
OfficialReference
ClientProvided
InternalTemplate
```

Suggested Review Decision values:

```text
Approved
Rejected
NeedsRevision
EscalationRequired
```

MVP controlled review decision values:

```text
Approved
Rejected
NeedsRevision
```

Do not treat a class number alone as complete professional classification.

---

# 20. Codex Implementation Notes

Codex may implement Classification only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Classification / Brand / Trademark boundaries
preserve Classification / Jurisdiction boundary
preserve Classification / Knowledge boundary
preserve Classification / AI Governance boundary
implement only MVP scope unless task says otherwise
write tests for goods/services item creation
write tests for original wording preservation
write tests for goods/services normalization
write tests for classification suggestion output status
write tests for professional review approval and rejection
write tests preventing AI suggestions from being treated as approved filing scope
write tests preventing official filing automation in MVP
```

Codex must not:

```text
invent official classification rules without source
invent full Nice database ingestion in MVP
invent full auto-classification engine in MVP
treat AI suggestion as final professional output
overwrite original goods/services wording
implement official filing connector inside Classification MVP
turn e-commerce product taxonomy into Core Classification
create pricing or fee engine inside Classification
```

---

# 21. Validation Rules

Classification Domain must pass the following checks.

```text
[ ] Classification is classified as Professional Domain.
[ ] Classification is counted within the 26 baseline Core Domains.
[ ] Classification does not change the baseline Core Domain Map.
[ ] Classification has MVP Phase 2 / Wave 2 classification.
[ ] Classification has MVP Depth = Must Implement.
[ ] Classification defines Core meaning.
[ ] Classification boundary excludes Brand meaning.
[ ] Classification boundary excludes Trademark lifecycle.
[ ] Classification boundary excludes Jurisdiction legal rule definition.
[ ] Classification boundary excludes Document and Evidence lifecycle.
[ ] Classification boundary excludes official filing automation.
[ ] Classification owns Classification object.
[ ] Classification defines Class Reference.
[ ] Classification defines Goods/Services Item.
[ ] Classification defines Goods/Services Set.
[ ] Classification defines Classification Suggestion.
[ ] Classification defines Classification Review Record.
[ ] Classification lists primary services.
[ ] Mutating Classification services emit events.
[ ] Classification lists primary events.
[ ] Classification defines contract requirements.
[ ] Classification defines AI Agent usage constraints.
[ ] Classification defines workflow usage constraints.
[ ] Classification defines API usage constraints.
[ ] Classification defines product consumers.
[ ] Classification defines MVP and deferred scope.
[ ] Classification defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Classification into Brand
turn Classification into Trademark lifecycle
turn Classification into Jurisdiction legal rule engine
turn Classification into official filing automation
turn Classification into fee engine
turn Classification into e-commerce product taxonomy
treat class number alone as complete filing scope
treat AI suggestion as approved professional output
overwrite original goods/services wording without trace
invent official wording without source
ignore jurisdiction-specific constraints
implement full auto-classification engine in MVP
allow Codex to define new classification architecture
```

---

# 23. Acceptance Criteria

This Classification Domain Specification is accepted only if:

```text
[ ] It defines Classification purpose.
[ ] It defines Classification Core meaning.
[ ] It identifies Classification as Professional Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Brand, Trademark, Jurisdiction, Document, Evidence, Knowledge, Order, Matter, AI Governance and Audit.
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
| 0.1.0 | Draft | Initial Classification Domain specification. Establishes Classification as Phase 2 Professional Domain, defines Class Reference, Goods/Services Item, Goods/Services Set, Classification Suggestion, Review Record, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
