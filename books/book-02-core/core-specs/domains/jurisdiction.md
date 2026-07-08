# Domain Specification — Jurisdiction

**Spec ID:** B02-DOM-JURISDICTION  
**Spec Type:** Domain  
**Domain Name:** Jurisdiction  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/jurisdiction.md; core-specs/objects/jurisdiction-office.md; core-specs/objects/jurisdiction-rule-reference.md; core-specs/objects/jurisdiction-service-scope.md; core-specs/objects/jurisdiction-deadline-rule-reference.md; core-specs/objects/jurisdiction-fee-reference.md  
**Related Service Specs:** core-specs/services/jurisdiction-reference-service.md; core-specs/services/jurisdiction-office-service.md; core-specs/services/jurisdiction-rule-reference-service.md; core-specs/services/jurisdiction-scope-validation-service.md; core-specs/services/jurisdiction-fee-reference-service.md; core-specs/services/jurisdiction-deadline-reference-service.md  
**Related Event Specs:** core-specs/events/jurisdiction-created.md; core-specs/events/jurisdiction-updated.md; core-specs/events/jurisdiction-office-linked.md; core-specs/events/jurisdiction-rule-reference-linked.md; core-specs/events/jurisdiction-scope-validated.md; core-specs/events/jurisdiction-fee-reference-updated.md; core-specs/events/jurisdiction-deadline-reference-linked.md  
**Related Contract Specs:** core-specs/contracts/jurisdiction/jurisdiction-contract.md; core-specs/contracts/jurisdiction/jurisdiction-office-contract.md; core-specs/contracts/jurisdiction/jurisdiction-rule-reference-contract.md; core-specs/contracts/jurisdiction/jurisdiction-service-scope-contract.md; core-specs/contracts/jurisdiction/jurisdiction-fee-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Jurisdiction Domain defines the Core meaning of a country, region, office, treaty route or legal/procedural territory in which trademark-related professional services are planned, filed, managed, reviewed or explained.

It exists so that Brands, Trademarks, Classifications, Documents, Evidence, Matters, Orders, Workflows, AI Agents and product consumers can consistently refer to where a trademark action applies.

Jurisdiction is required before:

```text
trademark filing planning
country or region recommendation
office route selection
goods/services limitation review
fee reference
deadline reference
document requirement reference
Power of Attorney requirement reference
local agent routing
status explanation
client quote generation
AI filing strategy recommendation
Codex implementation of professional trademark workflows
```

The Jurisdiction Domain is a Professional Domain because international trademark services depend on country, region, office and route-specific professional context.

---

# 2. Core Meaning

Jurisdiction means:

```text
a Core-recognized country, region, office, treaty route or procedural territory that defines where trademark protection, filing, examination, registration, maintenance, enforcement or service execution applies.
```

Jurisdiction is not merely:

```text
a country name
a billing region
a shipping destination
a language
a currency
a local agent
a filing product
a price list
a legal memo
a government website
a product market
a customer location
```

Jurisdiction answers:

```text
Where does the trademark action apply?
Which office or route is relevant?
Which professional requirements may be jurisdiction-specific?
Which classification, document, fee, deadline or agent rules may apply?
Which products and services may consume this jurisdiction reference?
What source supports the jurisdiction rule or requirement?
```

---

# 3. Domain Category

Jurisdiction is a Professional Domain.

Professional Domains provide the Core basis for:

```text
country/region trademark service context
office and route selection
filing requirement reference
classification and goods/services constraints
deadline and fee reference
document requirement reference
local agent routing
client quote and product configuration
AI-assisted filing strategy
professional review
```

Jurisdiction supports Trademark, Classification, Document, Evidence, Order, Matter and Routing domains.

---

# 4. Architectural Position

Jurisdiction sits beside Trademark and Classification in the Professional Core.

```text
Brand defines the commercial identity
        ↓
Trademark defines the protection record or intended protection
        ↓
Jurisdiction defines where protection or procedure applies
        ↓
Classification defines goods/services and class context
        ↓
Document and Evidence support jurisdiction-specific requirements
        ↓
Matter, Order, Routing and Workflow execute the service
```

Jurisdiction defines where professional rules apply.

It does not define the final legal rule itself unless represented as governed Knowledge or rule references.

It does not replace Trademark.

It does not replace Classification.

---

# 5. Scope

The Jurisdiction Domain includes:

```text
jurisdiction definition
jurisdiction type
jurisdiction office reference
jurisdiction route reference
jurisdiction service scope
jurisdiction rule reference
jurisdiction document requirement reference
jurisdiction deadline reference boundary
jurisdiction fee reference boundary
jurisdiction classification constraint reference
jurisdiction agent/routing reference boundary
jurisdiction status
jurisdiction source reference
jurisdiction audit reference
jurisdiction event emission
jurisdiction use by AI Agents, Services, Workflows, APIs and Codex tasks
```

MVP implementation should focus on:

```text
Jurisdiction
Jurisdiction Office
Jurisdiction Type
Jurisdiction Status
Jurisdiction Service Scope
Jurisdiction Rule Reference
Jurisdiction Reference Service
Jurisdiction Office Service
Jurisdiction Rule Reference Service
Jurisdiction Scope Validation Service
JurisdictionCreated event
JurisdictionOfficeLinked event
JurisdictionRuleReferenceLinked event
JurisdictionScopeValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

The Jurisdiction Domain owns:

```text
Core Jurisdiction definition
jurisdiction country/region/office reference
jurisdiction type
jurisdiction status
jurisdiction office relationship
jurisdiction route boundary
jurisdiction professional service scope boundary
jurisdiction rule reference boundary
jurisdiction deadline reference boundary
jurisdiction fee reference boundary
jurisdiction source reference
jurisdiction reference validation
jurisdiction event emission
jurisdiction reference used by professional workflows and products
```

## 6.2 Out of Boundary

The Jurisdiction Domain does not own:

```text
full legal rule engine
official law text ingestion
treaty interpretation as legal conclusion
official filing submission automation
classification taxonomy
document file lifecycle
evidence proof lifecycle
fee calculation engine as full product
currency exchange rate service
local agent commercial relationship
routing decision engine
customer market strategy
country risk analytics
official deadline calculation as final legal advice
```

Those responsibilities belong to:

```text
Knowledge Domain
Classification Domain
Document Domain
Evidence Domain
Agent Domain
Service Provider Domain
Routing Domain
Order Domain
Matter Domain
Workflow Contract system
Finance/Product implementation
External integration implementation
```

## 6.3 Boundary Notes

Jurisdiction provides professional location and office context.

Knowledge may contain governed rule references.

Classification applies goods/services and class rules.

Document defines files and requirement artifacts.

Routing chooses agents or service providers.

Fee and deadline references may be linked to Jurisdiction, but full fee engine and legal deadline engine are separate implementation concerns.

---

# 7. Domain Rules

## 7.1 Jurisdiction Must Be Stable

Jurisdiction must have a stable Core ID.

Display names, country names, local names, ISO codes or office labels must not replace Core Jurisdiction IDs.

## 7.2 Jurisdiction Must Distinguish Country, Region, Office and Route

Jurisdiction may represent:

```text
country
region
territory
trademark office
regional office
international route
Madrid designation context
special administrative region
multi-country office route
```

MVP should support country/region and office references.

## 7.3 Jurisdiction Rule References Require Source

Jurisdiction-specific requirements must reference Knowledge, official sources, professional notes, agent reports or approved internal sources.

Unsupported rule assertions must be marked as unverified or review-required.

## 7.4 Jurisdiction Does Not Make Final Legal Decisions

Jurisdiction may provide rule references and constraints.

Final legal strategy, filing decision, deadline confirmation or office-response strategy requires professional review where high-risk.

## 7.5 Jurisdiction Must Support Product-Neutral Consumption

Products may consume Jurisdiction.

Products must not redefine Jurisdiction as pricing region, sales region or UI dropdown only.

## 7.6 Jurisdiction Must Be Auditable

Jurisdiction-sensitive actions must preserve audit trace.

Audit-sensitive jurisdiction actions include:

```text
jurisdiction creation
office reference update
route reference update
rule reference update
document requirement reference update
deadline reference update
fee reference update
AI jurisdiction recommendation
agent routing recommendation
filing strategy recommendation
```

---

# 8. Primary Objects

The Jurisdiction Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Jurisdiction | Jurisdiction | Must Implement | Core-recognized country, region, office route or procedural territory. |
| Jurisdiction Office | Jurisdiction | Must Implement | Trademark office or authority reference associated with Jurisdiction. |
| Jurisdiction Type | Jurisdiction | Must Implement | Controlled classification of jurisdiction kind. |
| Jurisdiction Status | Jurisdiction | Must Implement | Controlled status indicating whether jurisdiction may be used. |
| Jurisdiction Rule Reference | Jurisdiction / Knowledge | Must Implement | Source-aware reference to jurisdiction-specific professional rule or requirement. |
| Jurisdiction Service Scope | Jurisdiction | Must Implement | Service types supported or recognized for the jurisdiction. |
| Jurisdiction Deadline Rule Reference | Jurisdiction / Workflow / Knowledge | Partial Implement | Reference to deadline-related rule, not final deadline calculation. |
| Jurisdiction Fee Reference | Jurisdiction / Order / Finance | Partial Implement | Reference to fee basis or price-related rule, not full pricing engine. |
| Jurisdiction Document Requirement Reference | Jurisdiction / Document / Knowledge | Partial Implement | Reference to required or recommended documents. |
| Jurisdiction Classification Constraint Reference | Jurisdiction / Classification | Partial Implement | Reference to jurisdiction-specific classification constraints. |
| Jurisdiction Audit Reference | Jurisdiction / Audit | Partial Implement | Audit reference for jurisdiction-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Trademark | Trademark | Trademark must reference Jurisdiction. |
| Brand | Brand | Brand protection may be jurisdiction-scoped. |
| Classification | Classification | Goods/services constraints may be jurisdiction-specific. |
| Document | Document | Document requirements may be jurisdiction-specific. |
| Evidence | Evidence | Evidence requirements may be jurisdiction-specific. |
| Knowledge Reference | Knowledge | Rule references require source-aware knowledge. |
| Agent | Agent | Local agent relationship may be jurisdiction-specific. |
| Service Provider | Service Provider | Providers may support jurisdictions. |
| Routing | Routing | Routing may use jurisdiction to select agent/provider. |
| Order | Order | Quote and service scope may reference Jurisdiction. |
| Matter | Matter | Matter execution may be jurisdiction-specific. |
| Audit Record | Audit | Audit records jurisdiction-sensitive actions. |

---

# 9. Primary Services

The Jurisdiction Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Jurisdiction Reference Service | Jurisdiction | Must Implement | Create, resolve and validate Jurisdiction references. |
| Jurisdiction Office Service | Jurisdiction | Must Implement | Link or update trademark office references. |
| Jurisdiction Rule Reference Service | Jurisdiction / Knowledge | Must Implement | Link jurisdiction-specific rule references to Knowledge sources. |
| Jurisdiction Scope Validation Service | Jurisdiction | Must Implement | Validate whether an action applies to the selected Jurisdiction. |
| Jurisdiction Service Scope Service | Jurisdiction | Must Implement | Manage supported service scopes for a Jurisdiction. |
| Jurisdiction Deadline Reference Service | Jurisdiction / Workflow | Partial Implement | Register deadline rule references without final deadline calculation. |
| Jurisdiction Fee Reference Service | Jurisdiction / Order | Partial Implement | Register fee references or pricing basis without full pricing engine. |
| Jurisdiction Document Requirement Service | Jurisdiction / Document | Partial Implement | Register document requirement references. |
| Jurisdiction Audit Reference Service | Jurisdiction / Audit | Partial Implement | Produce jurisdiction audit reference for governed actions. |

Service rules:

```text
- Mutating Jurisdiction services must emit events.
- Jurisdiction services must not implement official filing automation.
- Jurisdiction services must not define full legal rule engine.
- Jurisdiction rule references must cite Knowledge or approved sources.
- Fee and deadline services in MVP must remain reference-level unless separately approved.
```

---

# 10. Primary Events

The Jurisdiction Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| JurisdictionCreated | Jurisdiction Reference Service | Must Implement | A Core Jurisdiction has been created. |
| JurisdictionUpdated | Jurisdiction Reference Service | Must Implement | Controlled Jurisdiction fields have changed. |
| JurisdictionStatusChanged | Jurisdiction Reference Service | Must Implement | Jurisdiction status has changed. |
| JurisdictionOfficeLinked | Jurisdiction Office Service | Must Implement | Office reference has been linked to Jurisdiction. |
| JurisdictionRuleReferenceLinked | Jurisdiction Rule Reference Service | Must Implement | Rule reference has been linked to Jurisdiction. |
| JurisdictionScopeValidated | Jurisdiction Scope Validation Service | Must Implement | Jurisdiction applicability has been validated. |
| JurisdictionServiceScopeUpdated | Jurisdiction Service Scope Service | Must Implement | Supported service scope has changed. |
| JurisdictionDeadlineReferenceLinked | Jurisdiction Deadline Reference Service | Partial Implement | Deadline rule reference has been linked. |
| JurisdictionFeeReferenceUpdated | Jurisdiction Fee Reference Service | Partial Implement | Fee reference or pricing basis has changed. |
| JurisdictionDocumentRequirementLinked | Jurisdiction Document Requirement Service | Partial Implement | Document requirement reference has been linked. |
| JurisdictionReviewRequired | Jurisdiction Rule Reference Service | Partial Implement | Jurisdiction rule or reference requires professional review. |

Event rules:

```text
- Jurisdiction events must reference Jurisdiction.
- Rule reference events must reference Knowledge or source.
- Fee and deadline reference events must not imply final quote or final legal deadline.
- Review-required events must include review reason.
- Jurisdiction events must preserve audit context for rule-sensitive changes.
```

---

# 11. Primary Contracts

Jurisdiction requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Jurisdiction Contract | Jurisdiction Contract | Must Implement | Defines Jurisdiction fields, type, status and reference behavior. |
| Jurisdiction Office Contract | Jurisdiction Contract | Must Implement | Defines office reference, office name and relationship to Jurisdiction. |
| Jurisdiction Rule Reference Contract | Jurisdiction / Knowledge Contract | Must Implement | Defines source-aware rule reference behavior. |
| Jurisdiction Service Scope Contract | Jurisdiction Contract | Must Implement | Defines supported professional service scopes. |
| Jurisdiction Deadline Reference Contract | Jurisdiction / Workflow Contract | Partial Implement | Defines deadline rule reference boundary. |
| Jurisdiction Fee Reference Contract | Jurisdiction / Order Contract | Partial Implement | Defines fee reference boundary and source. |
| Jurisdiction Document Requirement Contract | Jurisdiction / Document Contract | Partial Implement | Defines document requirement reference behavior. |
| Jurisdiction Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for jurisdiction-sensitive actions. |

Contract rules:

```text
- Jurisdiction Contract must not collapse country, office and route into uncontrolled text.
- Rule Reference Contract must require source or review-required status.
- Deadline Reference Contract must not represent final legal deadline without review.
- Fee Reference Contract must not become a full pricing engine in MVP.
```

---

# 12. Relationships to Other Domains

## 12.1 Trademark

Trademark must be jurisdiction-aware.

Jurisdiction defines where a trademark record or intended protection applies.

## 12.2 Brand

Brand protection strategy may be jurisdiction-scoped.

Brand does not define jurisdiction.

## 12.3 Classification

Classification requirements and goods/services limits may vary by jurisdiction.

Jurisdiction references classification constraints but does not own classification taxonomy.

## 12.4 Document

Document requirements may be jurisdiction-specific.

Jurisdiction references document requirements but does not own document lifecycle.

## 12.5 Evidence

Evidence requirements may be jurisdiction-specific.

Jurisdiction references evidence requirements but does not own proof lifecycle.

## 12.6 Knowledge

Jurisdiction rules and requirements should be backed by Knowledge References.

Knowledge owns source-aware governed information.

## 12.7 Agent and Service Provider

Local agents and service providers may be associated with jurisdictions.

Jurisdiction does not own commercial agent relationship or qualification.

## 12.8 Routing

Routing may use Jurisdiction to select agent or service provider.

Routing owns selection logic.

## 12.9 Order and Matter

Order and Matter use Jurisdiction to define service scope and execution context.

Jurisdiction does not define commercial or execution lifecycle.

## 12.10 AI Governance

AI may recommend jurisdictions or summarize jurisdiction requirements, but must cite knowledge and require review for professional decisions.

## 12.11 Audit

Audit records should include Jurisdiction references for jurisdiction-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Jurisdiction only under governed Agent Contracts.

Allowed AI use:

```text
suggest potentially relevant jurisdictions based on declared business context
summarize jurisdiction-specific requirements with citations
identify missing jurisdiction in trademark intake
flag jurisdiction-specific document or goods/services issues
prepare draft filing strategy notes for professional review
compare jurisdiction service scope if authorized
prepare jurisdiction-based client explanation draft
```

AI must not:

```text
make final jurisdiction filing decision without review
state jurisdiction legal requirements without source
calculate legal deadline as final without approved deadline workflow
generate final official fee quote without approved pricing/fee service
select local agent as final without Routing and review where required
treat market interest as confirmed filing need
bypass Knowledge citation requirements
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Jurisdiction Object Access Rule
Jurisdiction Service Access Rule
Jurisdiction Event Access Rule
Knowledge Citation Rule
Policy Rule
Review Rule
Audit Rule
Human Review Rule for professional recommendations
```

---

# 14. Workflow Usage

Jurisdiction participates in professional workflows.

Jurisdiction-sensitive workflows may include:

```text
jurisdiction-selection-workflow.md
jurisdiction-requirement-review-workflow.md
jurisdiction-document-requirement-workflow.md
jurisdiction-fee-reference-review-workflow.md
jurisdiction-deadline-reference-review-workflow.md
agent-routing-by-jurisdiction-workflow.md
trademark-filing-strategy-workflow.md
ai-jurisdiction-recommendation-review-workflow.md
```

Workflow rules:

```text
- Jurisdiction workflows must reference Workflow Contracts.
- Jurisdiction recommendations should be reviewed before professional use.
- Rule references must cite Knowledge or approved source.
- Fee and deadline references must be review-sensitive if used externally.
- Jurisdiction workflows must not submit official filings in MVP.
```

---

# 15. API Usage

Jurisdiction APIs expose jurisdiction references, office references, service scopes and rule references through governed services.

Potential MVP APIs:

```text
POST /jurisdictions
GET /jurisdictions/{id}
PATCH /jurisdictions/{id}
POST /jurisdictions/{id}/offices
POST /jurisdictions/{id}/rule-references
POST /jurisdictions/{id}/service-scopes
POST /jurisdictions/scope/validate
POST /jurisdictions/reference/resolve
```

Potential partial APIs:

```text
POST /jurisdictions/{id}/fee-references
POST /jurisdictions/{id}/deadline-references
POST /jurisdictions/{id}/document-requirements
GET /jurisdictions/{id}/audit-reference
```

API rules:

```text
- APIs must invoke Jurisdiction Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not expose unsupported rule assertions as approved rules.
- APIs must not provide final deadline or final fee unless approved by related services and review.
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
Routing baseline
Opportunity Engine baseline
Reporting consumers
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Official connector products
Global fee engine
Global deadline engine
Advanced strategy products
```

Product rule:

```text
Products consume Jurisdiction.
Products do not redefine Jurisdiction.
```

---

# 17. MVP Scope

Jurisdiction is a Phase 2 / Wave 2 Must Implement domain.

MVP includes:

```text
Jurisdiction
Jurisdiction Office
Jurisdiction Type
Jurisdiction Status
Jurisdiction Rule Reference
Jurisdiction Service Scope
Jurisdiction Reference Service
Jurisdiction Office Service
Jurisdiction Rule Reference Service
Jurisdiction Scope Validation Service
Jurisdiction Service Scope Service
JurisdictionCreated event
JurisdictionUpdated event
JurisdictionOfficeLinked event
JurisdictionRuleReferenceLinked event
JurisdictionScopeValidated event
JurisdictionServiceScopeUpdated event
basic jurisdiction metadata validation
source traceability to Trademark, Classification, Document, Evidence, Knowledge, Routing and AI systems
```

MVP should support:

```text
country/region reference
office reference
basic jurisdiction type
basic trademark service scope
basic rule reference with source
basic jurisdiction validation
AI-assisted jurisdiction notes with human review
```

MVP does not require full legal rule engine, full fee engine, full deadline engine or official filing connector.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full legal rule engine
official law ingestion
jurisdiction treaty interpretation engine
full official filing connectors
global fee calculation engine
currency exchange integration
legal deadline calculation engine
local agent automatic selection engine
jurisdiction risk analytics
country market intelligence
cross-jurisdiction strategy optimizer
automatic document requirement updater
official office API synchronization
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Jurisdiction should use stable immutable ID.
Jurisdiction should support canonical name, display name and local name where applicable.
Jurisdiction Type should use controlled values.
Jurisdiction Office should be separately referenceable.
Jurisdiction Rule Reference should cite Knowledge or approved source.
Fee and deadline references should remain references unless approved services implement final calculation.
AI jurisdiction recommendations should produce draft/recommendation output status and require review for professional use.
```

Suggested Jurisdiction Type values:

```text
Country
Region
Territory
TrademarkOffice
RegionalOffice
InternationalRoute
MadridDesignation
SpecialAdministrativeRegion
MultiCountryOffice
```

MVP controlled Jurisdiction Type values:

```text
Country
Region
TrademarkOffice
InternationalRoute
MadridDesignation
```

Suggested Jurisdiction Status values:

```text
Draft
Active
ReviewRequired
Suspended
Deprecated
Superseded
Archived
```

MVP controlled Jurisdiction Status values:

```text
Active
ReviewRequired
Archived
```

Suggested Rule Reference Status values:

```text
Unverified
SourceLinked
ReviewRequired
Approved
Deprecated
Superseded
```

MVP controlled Rule Reference Status values:

```text
SourceLinked
ReviewRequired
Approved
Deprecated
```

Do not treat a country dropdown as Core Jurisdiction meaning.

---

# 20. Codex Implementation Notes

Codex may implement Jurisdiction only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Jurisdiction / Knowledge boundary
preserve Jurisdiction / Classification boundary
preserve Jurisdiction / Document / Evidence boundaries
preserve Jurisdiction / Routing / Agent boundaries
implement only MVP scope unless task says otherwise
write tests for jurisdiction creation
write tests for office linking
write tests for rule reference source requirement
write tests for service scope validation
write tests preventing full legal rule engine implementation in MVP
write tests preventing final fee/deadline calculation without approved service and review
```

Codex must not:

```text
invent legal rules without source
invent classification taxonomy inside Jurisdiction
invent full fee engine in MVP
invent full legal deadline engine in MVP
invent local agent routing engine inside Jurisdiction
implement official filing connector in MVP
treat country name as the only jurisdiction identity
allow AI to make final jurisdiction strategy decision
create product-specific jurisdiction dropdown as Core architecture
```

---

# 21. Validation Rules

Jurisdiction Domain must pass the following checks.

```text
[ ] Jurisdiction is classified as Professional Domain.
[ ] Jurisdiction is counted within the 26 baseline Core Domains.
[ ] Jurisdiction does not change the baseline Core Domain Map.
[ ] Jurisdiction has MVP Phase 2 / Wave 2 classification.
[ ] Jurisdiction has MVP Depth = Must Implement.
[ ] Jurisdiction defines Core meaning.
[ ] Jurisdiction boundary excludes full legal rule engine.
[ ] Jurisdiction boundary excludes Classification taxonomy.
[ ] Jurisdiction boundary excludes Document and Evidence lifecycle.
[ ] Jurisdiction boundary excludes Routing selection logic.
[ ] Jurisdiction boundary excludes full fee and deadline engines.
[ ] Jurisdiction owns Jurisdiction object.
[ ] Jurisdiction defines Jurisdiction Office.
[ ] Jurisdiction defines Jurisdiction Rule Reference.
[ ] Jurisdiction defines Jurisdiction Service Scope.
[ ] Jurisdiction lists primary services.
[ ] Mutating Jurisdiction services emit events.
[ ] Jurisdiction lists primary events.
[ ] Jurisdiction defines contract requirements.
[ ] Jurisdiction defines AI Agent usage constraints.
[ ] Jurisdiction defines workflow usage constraints.
[ ] Jurisdiction defines API usage constraints.
[ ] Jurisdiction defines product consumers.
[ ] Jurisdiction defines MVP and deferred scope.
[ ] Jurisdiction defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Jurisdiction into full legal rule engine
turn Jurisdiction into official law database
turn Jurisdiction into Classification taxonomy
turn Jurisdiction into Routing engine
turn Jurisdiction into Agent relationship management
turn Jurisdiction into fee calculation engine
turn Jurisdiction into legal deadline engine
turn Jurisdiction into customer market strategy
treat country dropdown as Core Jurisdiction
state unsupported rules as approved requirements
allow AI to make final filing jurisdiction decision
implement official filing connector in MVP
allow product UI to redefine Jurisdiction meaning
allow Codex to define new jurisdiction architecture
```

---

# 23. Acceptance Criteria

This Jurisdiction Domain Specification is accepted only if:

```text
[ ] It defines Jurisdiction purpose.
[ ] It defines Jurisdiction Core meaning.
[ ] It identifies Jurisdiction as Professional Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Trademark, Brand, Classification, Document, Evidence, Knowledge, Agent, Service Provider, Routing, Order, Matter, AI Governance and Audit.
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
| 0.1.0 | Draft | Initial Jurisdiction Domain specification. Establishes Jurisdiction as Phase 2 Professional Domain, defines Jurisdiction, Office, Type, Rule Reference, Service Scope, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
