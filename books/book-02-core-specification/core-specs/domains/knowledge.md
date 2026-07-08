# Domain Specification — Knowledge

**Spec ID:** B02-DOM-KNOWLEDGE  
**Spec Type:** Domain  
**Domain Name:** Knowledge  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/knowledge-item.md; core-specs/objects/knowledge-source.md; core-specs/objects/knowledge-reference.md; core-specs/objects/knowledge-collection.md; core-specs/objects/knowledge-version.md; core-specs/objects/knowledge-citation.md; core-specs/objects/knowledge-status.md  
**Related Service Specs:** core-specs/services/knowledge-registration-service.md; core-specs/services/knowledge-reference-service.md; core-specs/services/knowledge-source-validation-service.md; core-specs/services/knowledge-retrieval-service.md; core-specs/services/knowledge-versioning-service.md; core-specs/services/knowledge-citation-validation-service.md  
**Related Event Specs:** core-specs/events/knowledge-item-created.md; core-specs/events/knowledge-item-updated.md; core-specs/events/knowledge-source-linked.md; core-specs/events/knowledge-reference-created.md; core-specs/events/knowledge-version-created.md; core-specs/events/knowledge-citation-validated.md; core-specs/events/knowledge-item-deprecated.md  
**Related Contract Specs:** core-specs/contracts/knowledge/knowledge-item-contract.md; core-specs/contracts/knowledge/knowledge-source-contract.md; core-specs/contracts/knowledge/knowledge-reference-contract.md; core-specs/contracts/knowledge/knowledge-version-contract.md; core-specs/contracts/knowledge/knowledge-citation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Knowledge Domain defines the Core meaning of governed knowledge used by MarkOrbit.

It exists so that professional judgment, AI assistance, service execution, workflow review, Codex implementation, product guidance and audit records can refer to reliable, source-aware and version-aware knowledge.

Knowledge is required before:

```text
AI Agent reasoning
professional recommendation support
classification guidance
jurisdiction guidance
document drafting guidance
workflow explanation
Codex implementation traceability
policy interpretation support
review support
client-facing guidance
```

The Knowledge Domain is a Foundation Domain because MarkOrbit must distinguish governed knowledge from unverified text, casual notes, AI output and product content.

---

# 2. Core Meaning

Knowledge means:

```text
a governed Core information asset that has source, meaning, scope, status, version and reference rules, and may be used to support professional execution, AI assistance, product guidance or Codex implementation.
```

Knowledge is not merely:

```text
a document file
a web page
a prompt
a chat message
an AI answer
a product article
a marketing post
a legal conclusion
a user note
a database row
a vector embedding
```

Knowledge answers:

```text
What information asset is being used?
Where did it come from?
What does it mean inside Core?
What scope does it apply to?
Which version is valid?
Can it be cited by AI, services, workflows or Codex?
Is it approved, draft, deprecated or superseded?
What human review is required before use?
```

---

# 3. Domain Category

Knowledge is a Foundation Domain.

Foundation Domains provide the minimum Core basis for:

```text
source-aware reasoning
professional reference
AI grounding
Codex source traceability
domain guidance
controlled interpretation
knowledge reuse
version control
citation
auditability
```

Knowledge must be implemented before AI Agents and Codex tasks can safely consume professional or architecture references.

---

# 4. Architectural Position

Knowledge sits beside Identity, Organization, User, Permission and Policy as a foundational control layer.

```text
Identity recognizes the actor
        ↓
Organization provides operating context
        ↓
User represents the account
        ↓
Permission determines allowed action
        ↓
Policy evaluates contextual constraints
        ↓
Knowledge provides governed reference
        ↓
Services, Workflows, AI Agents and Codex use approved references
        ↓
Events and Audit preserve trace
```

Knowledge supports execution.

Knowledge does not replace professional judgment.

Knowledge does not define Domain ownership unless formalized in approved specs.

Knowledge does not authorize action.

That belongs to Permission and Policy.

---

# 5. Scope

The Knowledge Domain includes:

```text
knowledge item definition
knowledge source definition
knowledge reference
knowledge collection boundary
knowledge status
knowledge version
knowledge citation
knowledge source validation
knowledge retrieval boundary
knowledge use by AI Agents
knowledge use by Codex tasks
knowledge use by product consumers
knowledge audit reference
knowledge event emission
```

MVP implementation should focus on:

```text
Knowledge Item
Knowledge Source
Knowledge Reference
Knowledge Status
Knowledge Version
Knowledge Citation
Knowledge Registration Service
Knowledge Reference Service
Knowledge Source Validation Service
Knowledge Retrieval Service
KnowledgeItemCreated event
KnowledgeReferenceCreated event
KnowledgeSourceLinked event
KnowledgeVersionCreated event
basic source traceability validation
```

---

# 6. Boundary

## 6.1 In Boundary

The Knowledge Domain owns:

```text
Core knowledge definition
knowledge source reference
knowledge status
knowledge version boundary
knowledge reference rules
knowledge citation rules
knowledge source validation
knowledge retrieval boundary
knowledge deprecation boundary
knowledge event emission
knowledge reference used by AI Agents, Services, Workflows, APIs and Codex tasks
```

## 6.2 Out of Boundary

The Knowledge Domain does not own:

```text
official legal truth
professional final judgment
document file lifecycle
evidence lifecycle
customer communication lifecycle
marketing content publishing
training course publishing
AI model behavior
AI Agent capability authorization
vector database infrastructure
search engine implementation
document OCR implementation
web crawling implementation
product content UI
external legal database integration
```

Those responsibilities belong to:

```text
Document Domain
Evidence Domain
Communication Domain
AI Governance
Agent specs
Professional domains
Product implementation
Infrastructure implementation
External integration implementation
```

## 6.3 Boundary Notes

Knowledge is the governed reference layer.

Document is a file or formal artifact layer.

Evidence is proof used for professional or legal reasoning.

AI Output is machine-generated output requiring governance.

Knowledge may be derived from documents or evidence, but it does not replace them.

---

# 7. Domain Rules

## 7.1 Knowledge Requires Source

Every Knowledge Item must have at least one Knowledge Source or an explicit source-exemption reason.

Source-exempt knowledge must be marked and reviewed.

## 7.2 Knowledge Requires Status

Every Knowledge Item must have controlled status.

Uncontrolled text must not be consumed as approved Core Knowledge.

## 7.3 Knowledge Requires Version Awareness

Knowledge used by AI Agents, Services, Workflows, APIs or Codex must reference version or effective status.

Outdated or deprecated knowledge must not be used without explicit policy allowance.

## 7.4 Knowledge Does Not Replace Professional Judgment

Knowledge may support professional execution.

It must not automatically decide legal strategy, filing decision, classification conclusion, risk conclusion or official response.

## 7.5 Knowledge Must Be Citable

AI-assisted outputs, professional notes, Codex tasks and review records should cite Knowledge References where knowledge affects reasoning or output.

## 7.6 Knowledge Must Be Product-Neutral

Products may consume Knowledge.

Products must not redefine Knowledge meaning or create ungoverned product-only knowledge for governed execution.

---

# 8. Primary Objects

The Knowledge Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Knowledge Item | Knowledge | Must Implement | Governed Core information asset. |
| Knowledge Source | Knowledge | Must Implement | Source reference from which knowledge is derived or supported. |
| Knowledge Reference | Knowledge | Must Implement | Stable reference to a Knowledge Item or specific version. |
| Knowledge Collection | Knowledge | Partial Implement | Curated grouping of related Knowledge Items. |
| Knowledge Version | Knowledge | Must Implement | Version record of a Knowledge Item. |
| Knowledge Citation | Knowledge | Must Implement | Citation reference used by AI, services, workflows, products or Codex. |
| Knowledge Status | Knowledge | Must Implement | Controlled status indicating usability of knowledge. |
| Knowledge Scope | Knowledge / Policy | Partial Implement | Jurisdiction, domain, product, workflow or use scope of knowledge. |
| Knowledge Audit Reference | Knowledge / Audit | Partial Implement | Audit reference for knowledge-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Document | Document | Knowledge may reference or be derived from documents. |
| Evidence | Evidence | Knowledge may reference evidence but does not replace evidence. |
| Jurisdiction | Jurisdiction | Knowledge may be scoped by jurisdiction. |
| Classification | Classification | Knowledge may support classification guidance. |
| Trademark | Trademark | Knowledge may support trademark status explanation. |
| Policy Evaluation Context | Policy | Policy may control knowledge use. |
| AI Output | AI Governance | AI Output may cite Knowledge References. |
| Agent Contract | AI Governance | Agent access to Knowledge must be authorized. |
| Codex Task | Codex Governance | Codex tasks must cite approved Knowledge or specs where relevant. |
| Audit Record | Audit | Audit may record knowledge references used. |

---

# 9. Primary Services

The Knowledge Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Knowledge Registration Service | Knowledge | Must Implement | Register a new Knowledge Item with source and status. |
| Knowledge Reference Service | Knowledge | Must Implement | Create, resolve or validate Knowledge References. |
| Knowledge Source Validation Service | Knowledge | Must Implement | Validate source presence, source type and source usability. |
| Knowledge Retrieval Service | Knowledge | Must Implement | Retrieve approved knowledge for authorized consumers. |
| Knowledge Versioning Service | Knowledge | Must Implement | Create and resolve Knowledge Versions. |
| Knowledge Citation Validation Service | Knowledge | Must Implement | Validate citation references used by AI, services or Codex. |
| Knowledge Deprecation Service | Knowledge | Partial Implement | Mark knowledge deprecated, superseded or unusable. |
| Knowledge Collection Service | Knowledge | Partial Implement | Manage curated collections. |
| Knowledge Audit Reference Service | Knowledge / Audit | Partial Implement | Produce audit references for knowledge-sensitive actions. |

Service rules:

```text
- Mutating Knowledge services must emit events.
- Knowledge Retrieval Service must respect Permission and Policy where applicable.
- AI Agents must not retrieve unauthorized knowledge.
- Knowledge Registration must preserve source reference.
- Knowledge Citation Validation must fail when citation source is missing or deprecated.
```

---

# 10. Primary Events

The Knowledge Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| KnowledgeItemCreated | Knowledge Registration Service | Must Implement | A Knowledge Item has been created. |
| KnowledgeItemUpdated | Knowledge Registration Service / Knowledge Versioning Service | Partial Implement | Knowledge controlled fields or content reference changed. |
| KnowledgeSourceLinked | Knowledge Source Validation Service | Must Implement | A source has been linked to a Knowledge Item. |
| KnowledgeSourceValidated | Knowledge Source Validation Service | Must Implement | Knowledge source was validated for use. |
| KnowledgeReferenceCreated | Knowledge Reference Service | Must Implement | A stable Knowledge Reference has been created. |
| KnowledgeReferenceResolved | Knowledge Reference Service | Partial Implement | A Knowledge Reference has been resolved. |
| KnowledgeVersionCreated | Knowledge Versioning Service | Must Implement | A new Knowledge Version has been created. |
| KnowledgeCitationValidated | Knowledge Citation Validation Service | Must Implement | Citation reference has been validated. |
| KnowledgeItemDeprecated | Knowledge Deprecation Service | Partial Implement | Knowledge Item has been marked deprecated. |
| KnowledgeItemSuperseded | Knowledge Deprecation Service / Versioning Service | Partial Implement | Knowledge Item has been superseded by another item or version. |

Event rules:

```text
- Knowledge events must reference Knowledge Item or Knowledge Reference.
- Source events must reference Knowledge Source.
- Deprecation and supersession events must be auditable.
- Knowledge events must not expose protected or confidential source content unnecessarily.
```

---

# 11. Primary Contracts

Knowledge requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Knowledge Item Contract | Knowledge Contract | Must Implement | Defines Knowledge Item fields, status, scope and source references. |
| Knowledge Source Contract | Knowledge Contract | Must Implement | Defines source type, source reference and validation fields. |
| Knowledge Reference Contract | Knowledge Contract | Must Implement | Defines stable reference behavior for knowledge consumption. |
| Knowledge Version Contract | Knowledge Contract | Must Implement | Defines version behavior, effective status and supersession. |
| Knowledge Citation Contract | Knowledge Contract | Must Implement | Defines citation requirements for AI, services, workflows and Codex. |
| Knowledge Retrieval Contract | Knowledge / API Contract | Partial Implement | Defines retrieval constraints for consumers. |
| Knowledge Audit Contract | Audit Contract | Partial Implement | Defines audit fields for knowledge-sensitive actions. |

Contract rules:

```text
- Knowledge Item Contract must include source reference or source-exemption rule.
- Knowledge Reference Contract must be reusable by AI Agents, Codex tasks, Services and Workflows.
- Knowledge Citation Contract must support source traceability.
- Knowledge contracts must not define professional final judgment.
```

---

# 12. Relationships to Other Domains

## 12.1 Document

Document owns file or formal document lifecycle.

Knowledge may reference Document as source.

Knowledge does not replace Document.

## 12.2 Evidence

Evidence owns proof used for professional or legal support.

Knowledge may cite Evidence but does not replace Evidence.

## 12.3 Jurisdiction

Knowledge may be jurisdiction-scoped.

Jurisdiction owns official jurisdiction structure and country/region meaning.

## 12.4 Classification

Knowledge may support classification guidance.

Classification owns Nice class, goods/services and classification reasoning objects.

## 12.5 Trademark

Knowledge may support trademark status explanation or lifecycle guidance.

Trademark owns trademark record meaning.

## 12.6 Policy

Policy governs whether knowledge may be used, exposed, retrieved or cited.

Knowledge does not define policy logic.

## 12.7 AI Governance

AI Agents require authorized Knowledge access.

AI Output should cite Knowledge References when knowledge supports the output.

## 12.8 Workflow Contract

Workflows may require knowledge references for review, recommendation, explanation or Codex acceptance.

Knowledge does not define workflow states.

## 12.9 Codex Governance

Codex tasks may reference Knowledge only when approved sources and specs allow it.

Codex must not implement from ungoverned knowledge.

## 12.10 Audit

Audit records may include Knowledge References used in high-risk output, review or decision support.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Knowledge only under governed Agent Contracts.

Allowed AI use:

```text
retrieve authorized Knowledge Items
cite Knowledge References in generated output
summarize approved Knowledge for user or professional review
identify missing source references
flag deprecated or superseded knowledge
compare requested output against approved knowledge scope
support Codex task source traceability
```

AI must not:

```text
treat unverified text as approved Knowledge
invent source references
hide missing citations
use deprecated knowledge as current without warning
replace professional judgment with knowledge retrieval
perform legal conclusion without review
create official filing advice solely from knowledge snippets
retrieve unauthorized knowledge
train or fine-tune outside approved data governance
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Knowledge Object Access Rule
Knowledge Service Access Rule
Knowledge Event Access Rule
Citation Rule
Policy Rule
Audit Rule
Human Review Rule where high-risk
```

---

# 14. Workflow Usage

Knowledge participates in workflows but does not own most workflows.

Knowledge-sensitive workflows may include:

```text
knowledge-registration-workflow.md
knowledge-source-review-workflow.md
knowledge-deprecation-review-workflow.md
knowledge-citation-validation-workflow.md
ai-knowledge-use-review-workflow.md
codex-source-traceability-workflow.md
```

Workflow rules:

```text
- Knowledge workflows must reference Workflow Contracts.
- Knowledge source validation must be auditable.
- Deprecated knowledge use must trigger warning or block according to Policy.
- AI knowledge use must preserve citations and audit references.
- Codex tasks must not use unapproved knowledge as source specification.
```

---

# 15. API Usage

Knowledge APIs expose registration, reference, retrieval, citation and versioning through governed services.

Potential MVP APIs:

```text
POST /knowledge/items
GET /knowledge/items/{id}
POST /knowledge/sources/validate
POST /knowledge/references
POST /knowledge/references/resolve
POST /knowledge/citations/validate
GET /knowledge/versions/{id}
```

Potential partial APIs:

```text
POST /knowledge/collections
GET /knowledge/collections/{id}
POST /knowledge/items/{id}/deprecate
POST /knowledge/items/{id}/supersede
GET /knowledge/search
```

API rules:

```text
- APIs must invoke Knowledge Services.
- APIs must preserve Identity, User, Organization and Policy context where required.
- APIs must not expose unauthorized knowledge.
- APIs must not expose confidential source content unnecessarily.
- Mutating APIs must emit or cause service-level events.
- Retrieval APIs must respect status, version and scope.
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
Reporting consumers
Training content consumers
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Advanced analytics
Knowledge marketplace
Public education products
```

Product rule:

```text
Products consume Knowledge.
Products do not redefine Knowledge.
```

---

# 17. MVP Scope

Knowledge is a Phase 1 / Wave 1 Must Implement domain.

MVP includes:

```text
Knowledge Item
Knowledge Source
Knowledge Reference
Knowledge Version
Knowledge Citation
Knowledge Status
Knowledge Registration Service
Knowledge Reference Service
Knowledge Source Validation Service
Knowledge Retrieval Service
Knowledge Versioning Service
Knowledge Citation Validation Service
KnowledgeItemCreated event
KnowledgeSourceLinked event
KnowledgeSourceValidated event
KnowledgeReferenceCreated event
KnowledgeVersionCreated event
KnowledgeCitationValidated event
basic knowledge metadata validation
source traceability to AI Agent, Codex, Workflow, Policy and Product Consumption systems
```

MVP should support:

```text
architecture knowledge reference
domain/spec knowledge reference
professional guidance knowledge reference
AI authorized knowledge access
Codex source traceability
basic citation validation
basic deprecated/superseded warning boundary
```

MVP does not require full search engine, vector database or public knowledge publishing platform.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full vector database architecture
semantic search ranking
advanced knowledge graph reasoning
automatic web crawling
automatic OCR pipeline
public knowledge marketplace
paid content publishing
training course platform
auto-generated legal advice engine
external legal database integration
automatic jurisdiction law update ingestion
machine learning-based knowledge validation
full content approval CMS
multi-language public knowledge portal
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Knowledge Item should use stable immutable ID.
Knowledge Reference should be reusable by AI Agents, Services, Workflows, APIs and Codex tasks.
Knowledge Source should record source type, source location and validation status.
Knowledge Version should support supersession and deprecation.
Knowledge Citation should be structured and resolvable.
Knowledge Retrieval should respect Permission and Policy.
AI outputs should preserve citations when knowledge supports reasoning.
Codex tasks should cite core-specs and approved knowledge references, not conversation memory.
```

Suggested Knowledge Status values:

```text
Draft
ReviewRequired
Approved
Active
Deprecated
Superseded
Archived
Rejected
DeletedReferenceOnly
```

MVP controlled Knowledge Status values:

```text
Draft
Active
Deprecated
Superseded
```

Suggested Knowledge Source Type values:

```text
Manuscript
Appendix
Index
CoreSpec
OfficialSource
ProfessionalNote
Document
Evidence
ExternalReference
AcceptedCodexOutput
```

MVP controlled Knowledge Source Type values:

```text
Manuscript
Appendix
Index
CoreSpec
OfficialSource
Document
AcceptedCodexOutput
```

Do not treat vector embeddings as Core Knowledge meaning.

---

# 20. Codex Implementation Notes

Codex may implement Knowledge only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Knowledge / Document / Evidence boundaries
preserve Knowledge / AI Output boundary
preserve Knowledge / Professional Judgment boundary
implement only MVP scope unless task says otherwise
write tests for knowledge item creation
write tests for source validation
write tests for reference creation and resolution
write tests for version creation
write tests for citation validation
write tests preventing unverified text from being treated as approved knowledge
write tests preventing deprecated knowledge from being used as current without policy allowance
```

Codex must not:

```text
invent professional legal conclusions as Knowledge
implement full vector search in MVP
implement web crawler or OCR pipeline as Knowledge MVP
treat AI output as approved Knowledge without review
treat conversation memory as source specification
ignore source traceability
allow public knowledge exposure without Permission and Policy
create product CMS as Core Knowledge
```

---

# 21. Validation Rules

Knowledge Domain must pass the following checks.

```text
[ ] Knowledge is classified as Foundation Domain.
[ ] Knowledge is counted within the 26 baseline Core Domains.
[ ] Knowledge does not change the baseline Core Domain Map.
[ ] Knowledge has MVP Phase 1 / Wave 1 classification.
[ ] Knowledge has MVP Depth = Must Implement.
[ ] Knowledge defines Core meaning.
[ ] Knowledge boundary excludes Document lifecycle.
[ ] Knowledge boundary excludes Evidence lifecycle.
[ ] Knowledge boundary excludes AI Output governance.
[ ] Knowledge boundary excludes professional final judgment.
[ ] Knowledge owns Knowledge Item.
[ ] Knowledge defines Knowledge Source.
[ ] Knowledge defines Knowledge Reference.
[ ] Knowledge defines Knowledge Version.
[ ] Knowledge defines Knowledge Citation.
[ ] Knowledge lists primary services.
[ ] Mutating Knowledge services emit events.
[ ] Knowledge lists primary events.
[ ] Knowledge defines contract requirements.
[ ] Knowledge defines AI Agent usage constraints.
[ ] Knowledge defines workflow usage constraints.
[ ] Knowledge defines API usage constraints.
[ ] Knowledge defines product consumers.
[ ] Knowledge defines MVP and deferred scope.
[ ] Knowledge defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Knowledge into Document lifecycle
turn Knowledge into Evidence lifecycle
turn Knowledge into AI Output governance
turn Knowledge into final professional judgment
turn Knowledge into legal advice automation
turn Knowledge into public CMS
turn Knowledge into vector database architecture
treat prompt text as approved Knowledge
treat AI output as approved Knowledge without review
treat conversation memory as source specification
use deprecated knowledge as current without warning or policy allowance
expose confidential knowledge without Permission and Policy
implement full search/crawling/OCR platform in MVP
allow Codex to define new knowledge architecture
```

---

# 23. Acceptance Criteria

This Knowledge Domain Specification is accepted only if:

```text
[ ] It defines Knowledge purpose.
[ ] It defines Knowledge Core meaning.
[ ] It identifies Knowledge as Foundation Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Document, Evidence, Jurisdiction, Classification, Trademark, Policy, AI Governance, Workflow, Codex Governance and Audit.
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
| 0.1.0 | Draft | Initial Knowledge Domain specification. Establishes Knowledge as Phase 1 Foundation Domain, defines Knowledge Item, Source, Reference, Version, Citation, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
