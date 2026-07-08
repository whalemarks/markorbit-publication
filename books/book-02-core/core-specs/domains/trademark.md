# Domain Specification — Trademark

**Spec ID:** B02-DOM-TRADEMARK  
**Spec Type:** Domain  
**Domain Name:** Trademark  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/trademark.md; core-specs/objects/trademark-application.md; core-specs/objects/trademark-registration.md; core-specs/objects/trademark-status.md; core-specs/objects/trademark-owner-reference.md; core-specs/objects/trademark-goods-services.md; core-specs/objects/trademark-jurisdiction-reference.md; core-specs/objects/trademark-deadline-reference.md  
**Related Service Specs:** core-specs/services/trademark-record-service.md; core-specs/services/trademark-status-service.md; core-specs/services/trademark-owner-reference-service.md; core-specs/services/trademark-goods-services-service.md; core-specs/services/trademark-jurisdiction-link-service.md; core-specs/services/trademark-brand-link-service.md; core-specs/services/trademark-reference-validation-service.md  
**Related Event Specs:** core-specs/events/trademark-record-created.md; core-specs/events/trademark-status-updated.md; core-specs/events/trademark-owner-linked.md; core-specs/events/trademark-goods-services-updated.md; core-specs/events/trademark-jurisdiction-linked.md; core-specs/events/trademark-brand-linked.md; core-specs/events/trademark-reference-validated.md; core-specs/events/trademark-deadline-detected.md  
**Related Contract Specs:** core-specs/contracts/trademark/trademark-contract.md; core-specs/contracts/trademark/trademark-application-contract.md; core-specs/contracts/trademark/trademark-registration-contract.md; core-specs/contracts/trademark/trademark-status-contract.md; core-specs/contracts/trademark/trademark-goods-services-contract.md; core-specs/contracts/trademark/trademark-owner-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Trademark Domain defines the Core meaning of trademark protection records in MarkOrbit.

It exists so that brands, jurisdictions, classifications, documents, evidence, matters, orders, workflows, AI assistance and product consumers can consistently refer to trademark applications, registrations, statuses, goods/services, ownership references and lifecycle-sensitive professional work.

Trademark is required before:

```text
trademark intake
trademark application management
trademark status explanation
goods/services review
jurisdiction filing context
deadline awareness
document drafting
evidence preparation
matter lifecycle execution
order fulfillment
AI trademark summary
client-facing trademark portfolio view
Codex implementation of professional trademark workflows
```

The Trademark Domain is a Professional Domain because it represents the legal/procedural protection object around which international trademark services are performed.

---

# 2. Core Meaning

Trademark means:

```text
a Core-recognized trademark protection record or intended protection record that may represent an application, registration, designation, filing, status, jurisdiction, owner reference, goods/services scope and relationship to a Brand.
```

Trademark is not merely:

```text
a Brand
a logo file
a mark image
a filing order
a matter
a document
an evidence item
a customer request
an official database row
a product intake form
a deadline reminder
a legal conclusion
```

Trademark answers:

```text
Which trademark protection record or intended record is being managed?
Which Brand does it relate to?
Which jurisdiction or office applies?
What mark representation is involved?
What goods/services are covered?
What status is known or asserted?
Which owner/applicant reference is involved?
Which documents, evidence, matters, orders and deadlines relate to it?
What professional work is required?
```

---

# 3. Domain Category

Trademark is a Professional Domain.

Professional Domains provide the Core basis for:

```text
trademark record management
application and registration reference
jurisdiction-specific protection context
goods/services and class relationship
status tracking and explanation
official record linkage
deadline awareness
document and evidence preparation
matter and order execution
AI-assisted professional support
```

Trademark depends on Brand, Jurisdiction, Classification, Document and Evidence to support professional execution.

---

# 4. Architectural Position

Trademark sits after Brand in the Professional Core.

```text
Brand defines the commercial identity
        ↓
Trademark defines the legal/procedural protection record
        ↓
Jurisdiction defines where protection applies
        ↓
Classification defines goods/services and class context
        ↓
Document and Evidence support filing, prosecution and maintenance
        ↓
Matter, Order and Workflow execute professional service
```

Trademark provides protection-record context.

Brand provides commercial identity context.

Trademark does not replace Matter or Order.

Matter and Order operate services involving Trademark.

---

# 5. Scope

The Trademark Domain includes:

```text
trademark record definition
trademark application boundary
trademark registration boundary
trademark status
trademark owner/applicant reference boundary
trademark goods/services reference
trademark class reference
trademark jurisdiction reference
trademark office/reference number boundary
trademark filing/registration date reference
trademark deadline reference boundary
trademark-to-brand relationship
trademark-to-document relationship
trademark-to-evidence relationship
trademark reference validation
trademark audit reference
trademark event emission
trademark use by AI Agents, Services, Workflows, APIs and Codex tasks
```

MVP implementation should focus on:

```text
Trademark
Trademark Application
Trademark Registration
Trademark Status
Trademark Owner Reference
Trademark Goods/Services
Trademark Jurisdiction Reference
Trademark-Brand Link
Trademark Record Service
Trademark Status Service
Trademark Goods/Services Service
Trademark Reference Validation Service
TrademarkRecordCreated event
TrademarkStatusUpdated event
TrademarkGoodsServicesUpdated event
TrademarkBrandLinked event
TrademarkReferenceValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

The Trademark Domain owns:

```text
Core Trademark definition
trademark application reference
trademark registration reference
trademark status reference
trademark owner/applicant reference boundary
trademark goods/services relationship
trademark jurisdiction relationship
trademark-to-brand relationship
trademark filing and registration date references
trademark official number references
trademark deadline reference boundary
trademark reference validation
trademark event emission
trademark reference used by professional workflows and products
```

## 6.2 Out of Boundary

The Trademark Domain does not own:

```text
Brand commercial identity
official trademark office data source ingestion
jurisdiction legal rule definition
Nice classification taxonomy
document file lifecycle
evidence proof lifecycle
matter lifecycle
order lifecycle
task lifecycle
deadline calculation engine as full system
official filing submission automation
legal strategy final judgment
opposition/cancellation litigation workflow
trademark valuation
trademark transaction marketplace
monitoring/surveillance platform
```

Those responsibilities belong to:

```text
Brand Domain
Jurisdiction Domain
Classification Domain
Document Domain
Evidence Domain
Matter Domain
Order Domain
Task Domain
Workflow Contract system
Official data connectors or later integrations
Product implementation
External integration implementation
```

## 6.3 Boundary Notes

Trademark records may include official references, but official registry ingestion is not the meaning of Trademark.

Trademark status may be imported, manually maintained or reviewed, but official status truth and local legal interpretation require source and review.

Trademark deadlines may be referenced in Trademark, but deadline calculation and reminder execution are separate service/workflow responsibilities.

---

# 7. Domain Rules

## 7.1 Trademark Must Link to Brand Where Possible

A Trademark should relate to at least one Brand or explicit unknown/unlinked Brand state.

Trademark is the protection object.

Brand is the commercial identity.

## 7.2 Trademark Must Be Jurisdiction-Aware

Every Trademark record must reference a Jurisdiction or explicit pending/unknown jurisdiction state.

A trademark without jurisdiction context cannot support professional filing or status reasoning.

## 7.3 Trademark Must Preserve Status Source

Trademark status should distinguish:

```text
official status
agent-reported status
client-provided status
internal workflow status
AI-summarized status
unknown status
```

AI-summarized status must not replace official or professionally reviewed status.

## 7.4 Trademark Must Preserve Goods/Services Scope

Goods/services must be represented as professional scope.

Where classification applies, goods/services should link to Classification.

Trademark goods/services text must not be silently normalized without trace.

## 7.5 Trademark Must Distinguish Application and Registration

Application and registration are related but distinct lifecycle concepts.

Registration fields must not be assumed for pending applications.

Application filing date and registration date must be separately represented.

## 7.6 Trademark Must Be Auditable

Trademark-sensitive actions must preserve audit trace.

Audit-sensitive trademark actions include:

```text
trademark record creation
status update
owner/applicant reference change
goods/services update
class update
jurisdiction reference update
official number update
brand link update
deadline reference update
AI trademark summary
professional status explanation
document generation using trademark data
```

---

# 8. Primary Objects

The Trademark Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Trademark | Trademark | Must Implement | Core-recognized trademark protection record or intended protection record. |
| Trademark Application | Trademark | Must Implement | Application-side record, including filing reference and application status. |
| Trademark Registration | Trademark | Must Implement | Registration-side record, including registration reference and maintenance context. |
| Trademark Status | Trademark | Must Implement | Controlled professional status or mapped official status reference. |
| Trademark Owner Reference | Trademark / Customer / Organization | Must Implement | Owner/applicant reference associated with Trademark. |
| Trademark Goods/Services | Trademark / Classification | Must Implement | Goods/services scope associated with Trademark. |
| Trademark Jurisdiction Reference | Trademark / Jurisdiction | Must Implement | Jurisdiction or office context for Trademark. |
| Trademark Class Reference | Trademark / Classification | Must Implement | Class reference associated with goods/services. |
| Trademark-Brand Link | Trademark / Brand | Must Implement | Relationship between Trademark and Brand. |
| Trademark Deadline Reference | Trademark / Workflow | Partial Implement | Deadline reference associated with Trademark lifecycle. |
| Trademark Source Reference | Trademark / Knowledge / Document | Partial Implement | Source reference supporting trademark data. |
| Trademark Audit Reference | Trademark / Audit | Partial Implement | Audit reference for trademark-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Brand | Brand | Trademark may protect a Brand representation. |
| Jurisdiction | Jurisdiction | Trademark must be jurisdiction-aware. |
| Classification | Classification | Trademark goods/services may be class-scoped. |
| Document | Document | Trademark may reference documents and official notices. |
| Evidence | Evidence | Trademark use or ownership may require evidence. |
| Customer | Customer | Customer may be applicant, owner, requester or buyer. |
| Matter | Matter | Trademark-related professional work is executed through Matter. |
| Order | Order | Trademark-related service request is commercialized through Order. |
| Task | Task | Trademark work may create tasks. |
| AI Output | AI Governance | AI may summarize or recommend around Trademark. |
| Knowledge Reference | Knowledge | Trademark guidance may cite approved knowledge. |
| Audit Record | Audit | Audit records trademark-sensitive actions. |

---

# 9. Primary Services

The Trademark Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Trademark Record Service | Trademark | Must Implement | Create or update Core Trademark record. |
| Trademark Application Service | Trademark | Must Implement | Create or update application-side trademark fields. |
| Trademark Registration Service | Trademark | Partial Implement | Create or update registration-side trademark fields. |
| Trademark Status Service | Trademark | Must Implement | Update or map Trademark Status through governed rules. |
| Trademark Owner Reference Service | Trademark | Must Implement | Create or update owner/applicant reference. |
| Trademark Goods/Services Service | Trademark / Classification | Must Implement | Create or update goods/services and class references. |
| Trademark Jurisdiction Link Service | Trademark / Jurisdiction | Must Implement | Link Trademark to Jurisdiction or office reference. |
| Trademark Brand Link Service | Trademark / Brand | Must Implement | Link Trademark to Brand. |
| Trademark Deadline Reference Service | Trademark / Workflow | Partial Implement | Register or validate trademark deadline references. |
| Trademark Reference Validation Service | Trademark | Must Implement | Validate Trademark references used by other domains. |
| Trademark Audit Reference Service | Trademark / Audit | Partial Implement | Produce trademark audit reference for governed actions. |

Service rules:

```text
- Mutating Trademark services must emit events.
- Trademark services must not define Brand meaning.
- Trademark services must not define Jurisdiction legal rules.
- Trademark services must not define Classification taxonomy.
- Trademark status changes must preserve source and audit trace.
- AI-generated summaries must not update Trademark Status directly without governed service and review.
```

---

# 10. Primary Events

The Trademark Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| TrademarkRecordCreated | Trademark Record Service | Must Implement | A Core Trademark record has been created. |
| TrademarkRecordUpdated | Trademark Record Service | Must Implement | Controlled Trademark fields have changed. |
| TrademarkApplicationCreated | Trademark Application Service | Must Implement | Application-side Trademark record has been created. |
| TrademarkRegistrationLinked | Trademark Registration Service | Partial Implement | Registration reference has been linked to Trademark. |
| TrademarkStatusUpdated | Trademark Status Service | Must Implement | Trademark status has been updated or mapped. |
| TrademarkOwnerLinked | Trademark Owner Reference Service | Must Implement | Owner/applicant reference has been linked to Trademark. |
| TrademarkGoodsServicesUpdated | Trademark Goods/Services Service | Must Implement | Goods/services scope has changed. |
| TrademarkClassLinked | Trademark Goods/Services Service | Must Implement | Class reference has been linked to Trademark. |
| TrademarkJurisdictionLinked | Trademark Jurisdiction Link Service | Must Implement | Jurisdiction reference has been linked to Trademark. |
| TrademarkBrandLinked | Trademark Brand Link Service | Must Implement | Brand has been linked to Trademark. |
| TrademarkReferenceValidated | Trademark Reference Validation Service | Must Implement | Trademark reference has been validated for governed use. |
| TrademarkDeadlineDetected | Trademark Deadline Reference Service | Partial Implement | Potential trademark deadline reference has been detected. |
| TrademarkReviewRequired | Trademark Status Service / Goods/Services Service | Partial Implement | Trademark data or change requires professional review. |

Event rules:

```text
- Trademark events must reference Trademark.
- Status events must include status source or status source type.
- Goods/services events must preserve previous and updated text references where applicable.
- Jurisdiction events must reference Jurisdiction.
- Review-required events must include review reason.
- Trademark events must not imply official truth without source.
```

---

# 11. Primary Contracts

Trademark requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Trademark Contract | Trademark Contract | Must Implement | Defines Trademark fields, status, references and relationship behavior. |
| Trademark Application Contract | Trademark Contract | Must Implement | Defines application number, filing date, applicant and status fields. |
| Trademark Registration Contract | Trademark Contract | Partial Implement | Defines registration number, registration date and maintenance context. |
| Trademark Status Contract | Trademark Contract | Must Implement | Defines status value, status source, mapping and review boundary. |
| Trademark Owner Reference Contract | Trademark / Customer / Organization Contract | Must Implement | Defines applicant/owner reference and verification boundary. |
| Trademark Goods/Services Contract | Trademark / Classification Contract | Must Implement | Defines goods/services text, class reference and amendment boundary. |
| Trademark Jurisdiction Reference Contract | Trademark / Jurisdiction Contract | Must Implement | Defines jurisdiction or office reference for Trademark. |
| Trademark-Brand Link Contract | Trademark / Brand Contract | Must Implement | Defines relationship between Trademark and Brand. |
| Trademark Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for trademark-sensitive actions. |

Contract rules:

```text
- Trademark Status Contract must distinguish official, agent-reported, internal and AI-summarized status.
- Trademark Application and Registration Contracts must not collapse into one uncontrolled lifecycle object.
- Trademark Goods/Services Contract must preserve original text and normalized/reference text where applicable.
- Trademark contracts must not define filing automation or official submission rules.
```

---

# 12. Relationships to Other Domains

## 12.1 Brand

Brand represents commercial identity.

Trademark represents legal/procedural protection.

Trademark should link to Brand where possible.

## 12.2 Jurisdiction

Jurisdiction defines where Trademark protection applies.

Trademark must be jurisdiction-aware.

## 12.3 Classification

Classification defines goods/services and class context.

Trademark goods/services may reference Classification.

## 12.4 Document

Document owns official notices, certificates, filings, POAs and other files.

Trademark may reference Documents.

## 12.5 Evidence

Evidence supports use, ownership, reputation or response arguments.

Trademark may require Evidence for professional tasks.

## 12.6 Customer

Customer may be applicant, owner, requester or buyer.

Trademark does not define customer lifecycle.

## 12.7 Matter and Order

Matter executes professional trademark work.

Order commercializes service request.

Trademark does not define Matter or Order lifecycle.

## 12.8 Task and Workflow

Trademark-related execution creates tasks and workflow transitions.

Trademark does not define task lifecycle or workflow state model.

## 12.9 Knowledge

Knowledge supports trademark guidance, status explanation, jurisdiction notes and professional reasoning.

Trademark does not define Knowledge validity.

## 12.10 AI Governance

AI may summarize Trademark status or recommend next steps, but must not replace professional review.

## 12.11 Audit

Audit records should include Trademark references for trademark-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Trademark only under governed Agent Contracts.

Allowed AI use:

```text
summarize Trademark record
explain known status with source and uncertainty
identify missing trademark fields
suggest whether professional review is required
prepare draft status notes
suggest goods/services clarification questions
compare Brand and Trademark references if authorized
prepare client-facing summary draft for review
flag potential deadline references for human confirmation
```

AI must not:

```text
declare official trademark status without source
make final legal conclusion
make final registrability or availability decision
file or submit official applications
update Trademark Status directly without governed service
delete or amend goods/services without review
treat unofficial source as official without label
calculate legal deadline as final without review where high-risk
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Trademark Object Access Rule
Trademark Service Access Rule
Trademark Event Access Rule
Jurisdiction and Classification Scope Rule
Policy Rule
Review Rule
Audit Rule
Human Review Rule for professional conclusions
```

---

# 14. Workflow Usage

Trademark participates in professional workflows.

Trademark-sensitive workflows may include:

```text
trademark-intake-workflow.md
trademark-record-review-workflow.md
trademark-status-review-workflow.md
trademark-goods-services-review-workflow.md
trademark-owner-reference-review-workflow.md
trademark-document-preparation-workflow.md
trademark-deadline-review-workflow.md
ai-trademark-summary-review-workflow.md
```

Workflow rules:

```text
- Trademark workflows must reference Workflow Contracts.
- Trademark status updates should preserve source and review trace.
- Goods/services amendments must be auditable.
- AI-generated trademark summaries must require review before professional use.
- Deadline-related workflows must distinguish detected, calculated, confirmed and approved deadlines.
- Trademark workflows must not submit official filings in MVP.
```

---

# 15. API Usage

Trademark APIs expose trademark records, status, owner references, goods/services, jurisdiction links and brand links through governed services.

Potential MVP APIs:

```text
POST /trademarks
GET /trademarks/{id}
PATCH /trademarks/{id}
POST /trademarks/{id}/applications
POST /trademarks/{id}/status
POST /trademarks/{id}/owners
POST /trademarks/{id}/goods-services
POST /trademarks/{id}/jurisdiction
POST /trademarks/{id}/brand-links
POST /trademarks/reference/validate
```

Potential partial APIs:

```text
POST /trademarks/{id}/registrations
POST /trademarks/{id}/deadline-references
POST /trademarks/{id}/review
GET /trademarks/{id}/audit-reference
```

API rules:

```text
- APIs must invoke Trademark Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not submit official filings in MVP.
- APIs must not expose confidential trademark documents without Permission and Policy.
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
Reporting consumers
Opportunity Engine baseline
Brand Asset Vault baseline
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Trademark monitoring products
Trademark transaction products
Portfolio analytics products
Official connector products
```

Product rule:

```text
Products consume Trademark.
Products do not redefine Trademark.
```

---

# 17. MVP Scope

Trademark is a Phase 2 / Wave 2 Must Implement domain.

MVP includes:

```text
Trademark
Trademark Application
Trademark Registration boundary
Trademark Status
Trademark Owner Reference
Trademark Goods/Services
Trademark Jurisdiction Reference
Trademark Class Reference
Trademark-Brand Link
Trademark Reference
Trademark Record Service
Trademark Application Service
Trademark Status Service
Trademark Owner Reference Service
Trademark Goods/Services Service
Trademark Jurisdiction Link Service
Trademark Brand Link Service
Trademark Reference Validation Service
TrademarkRecordCreated event
TrademarkRecordUpdated event
TrademarkApplicationCreated event
TrademarkStatusUpdated event
TrademarkOwnerLinked event
TrademarkGoodsServicesUpdated event
TrademarkClassLinked event
TrademarkJurisdictionLinked event
TrademarkBrandLinked event
TrademarkReferenceValidated event
basic trademark metadata validation
source traceability to Brand, Jurisdiction, Classification, Document, Evidence and AI systems
```

MVP should support:

```text
basic trademark intake
basic application record
basic registration reference boundary
basic status tracking
basic goods/services and class references
basic jurisdiction context
basic brand relationship
basic owner/applicant reference
AI-assisted trademark status summary with human review
```

MVP does not require official filing automation, full official registry connectors or full deadline calculation engine.

---

# 18. Deferred Scope

Deferred scope includes:

```text
official filing submission automation
full trademark office data ingestion
automatic office-action response generation
full opposition/cancellation workflow
legal deadline calculation engine
global renewal automation
full trademark portfolio analytics
trademark valuation engine
trademark transaction marketplace
watching/monitoring platform
automatic similarity/conflict search engine
automatic official document retrieval
cross-jurisdiction status normalization engine
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Trademark should use stable immutable ID.
Trademark should link to Brand where possible.
Trademark should reference Jurisdiction using approved Jurisdiction specs.
Trademark goods/services should preserve original text.
Trademark Status should use controlled values and status source.
Application and Registration fields should be distinct.
Trademark owner reference should distinguish declared, official, agent-reported and unknown states.
Deadline references should be treated as references until confirmed by deadline-specific workflow or service.
AI-generated summaries should produce draft/recommendation output status and require review for professional use.
```

Suggested Trademark Record Status values:

```text
Draft
Intake
ApplicationPlanned
ApplicationFiled
UnderExamination
OfficeActionIssued
Published
Opposed
Allowed
Registered
RenewalDue
Renewed
Cancelled
Expired
Abandoned
Refused
Suspended
Unknown
Archived
```

MVP controlled status values:

```text
Draft
ApplicationFiled
UnderExamination
OfficeActionIssued
Published
Registered
Refused
Abandoned
Expired
Unknown
Archived
```

Suggested Status Source Type values:

```text
OfficialRecord
AgentReport
ClientProvided
InternalWorkflow
AISummarized
ManualReview
Unknown
```

MVP controlled source types:

```text
OfficialRecord
AgentReport
ClientProvided
InternalWorkflow
ManualReview
Unknown
```

Do not treat AI-summarized status as official status.

---

# 20. Codex Implementation Notes

Codex may implement Trademark only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Trademark / Brand boundary
preserve Trademark / Jurisdiction / Classification boundaries
preserve Trademark / Document / Evidence boundaries
preserve Trademark / Matter / Order boundaries
implement only MVP scope unless task says otherwise
write tests for trademark record creation
write tests for application record creation
write tests for status update with source
write tests for goods/services update
write tests for jurisdiction link
write tests for brand link
write tests preventing official filing automation in MVP
write tests preventing AI-summarized status from replacing official status
```

Codex must not:

```text
invent official filing automation inside Trademark MVP
invent jurisdiction legal rules inside Trademark
invent classification taxonomy inside Trademark
invent legal deadline engine inside Trademark MVP
invent opposition/cancellation litigation workflow in MVP
treat Brand as Trademark
treat Matter or Order as Trademark
allow AI to make final legal status or filing decision
create trademark marketplace or valuation features in MVP
```

---

# 21. Validation Rules

Trademark Domain must pass the following checks.

```text
[ ] Trademark is classified as Professional Domain.
[ ] Trademark is counted within the 26 baseline Core Domains.
[ ] Trademark does not change the baseline Core Domain Map.
[ ] Trademark has MVP Phase 2 / Wave 2 classification.
[ ] Trademark has MVP Depth = Must Implement.
[ ] Trademark defines Core meaning.
[ ] Trademark boundary excludes Brand meaning.
[ ] Trademark boundary excludes Jurisdiction legal rule definition.
[ ] Trademark boundary excludes Classification taxonomy.
[ ] Trademark boundary excludes Document and Evidence lifecycle.
[ ] Trademark boundary excludes Matter and Order lifecycle.
[ ] Trademark boundary excludes official filing automation.
[ ] Trademark owns Trademark object.
[ ] Trademark defines Trademark Application.
[ ] Trademark defines Trademark Registration boundary.
[ ] Trademark defines Trademark Status.
[ ] Trademark defines Trademark Goods/Services.
[ ] Trademark defines Trademark Jurisdiction Reference.
[ ] Trademark defines Trademark-Brand Link.
[ ] Trademark lists primary services.
[ ] Mutating Trademark services emit events.
[ ] Trademark lists primary events.
[ ] Trademark defines contract requirements.
[ ] Trademark defines AI Agent usage constraints.
[ ] Trademark defines workflow usage constraints.
[ ] Trademark defines API usage constraints.
[ ] Trademark defines product consumers.
[ ] Trademark defines MVP and deferred scope.
[ ] Trademark defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Trademark into Brand
turn Trademark into Matter or Order
turn Trademark into Document or Evidence lifecycle
turn Trademark into official filing automation
turn Trademark into legal deadline calculation engine
turn Trademark into opposition/cancellation litigation system
turn Trademark into trademark marketplace
turn Trademark into valuation engine
turn Trademark into monitoring platform
store AI-summarized status as official status
treat unofficial source as official without label
allow AI to make final legal or filing decision
allow product UI to redefine Trademark status
allow Codex to define new trademark architecture
```

---

# 23. Acceptance Criteria

This Trademark Domain Specification is accepted only if:

```text
[ ] It defines Trademark purpose.
[ ] It defines Trademark Core meaning.
[ ] It identifies Trademark as Professional Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Brand, Jurisdiction, Classification, Document, Evidence, Customer, Matter, Order, Task, Knowledge, AI Governance and Audit.
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
| 0.1.0 | Draft | Initial Trademark Domain specification. Establishes Trademark as Phase 2 Professional Domain, defines Trademark, Application, Registration boundary, Status, Owner Reference, Goods/Services, Jurisdiction Reference, Brand Link, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
