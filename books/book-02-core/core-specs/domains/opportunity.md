# Domain Specification — Opportunity

**Spec ID:** B02-DOM-OPPORTUNITY  
**Spec Type:** Domain  
**Domain Name:** Opportunity  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/opportunity.md; core-specs/objects/opportunity-source.md; core-specs/objects/opportunity-signal.md; core-specs/objects/opportunity-status.md; core-specs/objects/opportunity-score.md; core-specs/objects/opportunity-recommendation.md; core-specs/objects/opportunity-conversion-record.md  
**Related Service Specs:** core-specs/services/opportunity-registration-service.md; core-specs/services/opportunity-signal-service.md; core-specs/services/opportunity-scoring-service.md; core-specs/services/opportunity-recommendation-service.md; core-specs/services/opportunity-conversion-service.md; core-specs/services/opportunity-reference-validation-service.md  
**Related Event Specs:** core-specs/events/opportunity-created.md; core-specs/events/opportunity-updated.md; core-specs/events/opportunity-signal-linked.md; core-specs/events/opportunity-score-updated.md; core-specs/events/opportunity-recommendation-created.md; core-specs/events/opportunity-converted-to-customer.md; core-specs/events/opportunity-converted-to-order.md; core-specs/events/opportunity-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/opportunity/opportunity-contract.md; core-specs/contracts/opportunity/opportunity-source-contract.md; core-specs/contracts/opportunity/opportunity-signal-contract.md; core-specs/contracts/opportunity/opportunity-score-contract.md; core-specs/contracts/opportunity/opportunity-recommendation-contract.md; core-specs/contracts/opportunity/opportunity-conversion-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Execution Extension Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Opportunity Domain defines the Core meaning of a potential business need, service lead or commercial chance in MarkOrbit.

It exists so that Customers, Brands, Trademarks, Jurisdictions, Classifications, Orders, Matters, Communications, AI Agents and product consumers can consistently refer to signals that may become service requests, customer relationships, orders or professional matters.

Opportunity is required before:

```text
lead intake
business opportunity generation
trademark portfolio opportunity discovery
potential customer follow-up
brand protection gap identification
jurisdiction expansion recommendation
classification gap recommendation
renewal or maintenance opportunity detection
agent or partner referral handling
AI opportunity recommendation
opportunity-to-customer conversion
opportunity-to-order conversion
Codex implementation of opportunity workflows
```

The Opportunity Domain is a Business Execution Domain because it supports the pre-order business process that may lead to Customer, Order and Matter execution.

---

# 2. Core Meaning

Opportunity means:

```text
a Core-recognized potential service need or commercial chance, supported by source, signal, context, status, recommendation and conversion rules, that may later become Customer, Order or Matter activity.
```

Opportunity is not merely:

```text
a Customer
an Order
a Matter
a marketing lead list
a sales note
an AI guess
a trademark record
a brand risk
a task
a campaign
a price quote
a communication thread
```

Opportunity answers:

```text
What potential service need has been identified?
Where did the signal come from?
Which Brand, Trademark, Jurisdiction, Classification, Customer or Communication context supports it?
Is the opportunity draft, review-required, qualified, rejected, converted or archived?
What recommendation or next action is suggested?
Can it be converted into Customer, Order or Matter through governed services?
What evidence, source or AI trace supports the opportunity?
```

---

# 3. Domain Category

Opportunity is a Business Execution Domain.

Business Execution Domains provide the Core basis for:

```text
lead handling
service opportunity recognition
pre-order business context
AI-assisted commercial recommendation
customer development workflow
order conversion
matter planning
business pipeline traceability
```

Opportunity precedes Order and Matter but does not replace them.

---

# 4. Architectural Position

Opportunity sits before Order in the Business Execution Core, but its implementation priority is Phase 4.

```text
Professional Core provides Brand, Trademark, Jurisdiction and Classification context
        ↓
Opportunity identifies potential service need
        ↓
Customer provides demand-side party context
        ↓
Order confirms commercial service request
        ↓
Matter executes professional work
        ↓
Workflow, Task, Event and Notification coordinate execution
```

Opportunity is a pre-order business signal.

Order is a commercial commitment.

Matter is professional execution.

Opportunity must not silently become Order or Matter.

---

# 5. Scope

The Opportunity Domain includes:

```text
opportunity definition
opportunity source
opportunity signal
opportunity status
opportunity context
opportunity score boundary
opportunity recommendation
opportunity qualification boundary
opportunity relationship to Customer
opportunity relationship to Brand
opportunity relationship to Trademark
opportunity relationship to Jurisdiction
opportunity relationship to Classification
opportunity relationship to Communication
opportunity conversion to Customer
opportunity conversion to Order
opportunity conversion to Matter boundary
opportunity reference validation
opportunity audit reference
opportunity event emission
opportunity use by AI Agents, Services, Workflows, APIs and Codex tasks
```

MVP / Phase 4 implementation should focus on:

```text
Opportunity
Opportunity Source
Opportunity Signal
Opportunity Status
Opportunity Recommendation
Opportunity Conversion Record
Opportunity Registration Service
Opportunity Signal Service
Opportunity Recommendation Service
Opportunity Conversion Service
Opportunity Reference Validation Service
OpportunityCreated event
OpportunitySignalLinked event
OpportunityRecommendationCreated event
OpportunityConvertedToCustomer event
OpportunityConvertedToOrder event
OpportunityReferenceValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

The Opportunity Domain owns:

```text
Core Opportunity definition
opportunity source
opportunity signal
opportunity status
opportunity recommendation boundary
opportunity qualification boundary
opportunity conversion boundary
opportunity relationship to Customer, Brand and Trademark
opportunity relationship to Jurisdiction and Classification
opportunity reference validation
opportunity event emission
opportunity reference used by business development workflows and products
```

## 6.2 Out of Boundary

The Opportunity Domain does not own:

```text
Customer lifecycle
Order commercial commitment
Matter professional execution
payment lifecycle
pricing engine
marketing automation platform
CRM campaign management
advertising attribution
Brand commercial identity
Trademark lifecycle
Jurisdiction rule meaning
Classification goods/services meaning
Communication message lifecycle
AI model scoring logic as final truth
automatic sales decision
```

Those responsibilities belong to:

```text
Customer Domain
Order Domain
Matter Domain
Brand Domain
Trademark Domain
Jurisdiction Domain
Classification Domain
Communication Domain
AI Governance
Policy system
Product implementation
External integration implementation
```

## 6.3 Boundary Notes

Opportunity may be generated from professional data, communication, AI analysis, partner referral or manual input.

Opportunity is not a confirmed commercial request.

Opportunity must be qualified and converted through governed services before becoming Order or Matter.

AI may suggest Opportunities, but AI suggestions are not automatically qualified opportunities.

---

# 7. Domain Rules

## 7.1 Opportunity Requires Source

Every Opportunity must have an Opportunity Source or explicit source-exemption reason.

Source may include:

```text
ManualInput
CustomerInquiry
CommunicationSignal
TrademarkPortfolioSignal
BrandProtectionGap
JurisdictionExpansionSignal
ClassificationGapSignal
RenewalSignal
AgentReferral
PartnerReferral
AIRecommendation
ImportedLead
```

## 7.2 Opportunity Requires Signal or Context

An Opportunity must be supported by a signal or context.

A free-text sales idea without source or context is not implementation-ready.

## 7.3 Opportunity Does Not Equal Customer

Opportunity may reference or create a Customer through conversion.

It must not be treated as Customer until converted or linked through Customer service.

## 7.4 Opportunity Does Not Equal Order

Opportunity may convert into Order.

It does not represent confirmed commercial service scope.

## 7.5 Opportunity Recommendation Must Be Reviewable

AI-generated or system-generated Opportunity Recommendations must be reviewable.

High-risk recommendations, client-facing recommendations or pricing-related recommendations must require human review.

## 7.6 Opportunity Must Be Auditable

Opportunity-sensitive actions must preserve audit trace.

Audit-sensitive opportunity actions include:

```text
opportunity creation
signal linking
score update
recommendation creation
qualification status change
conversion to customer
conversion to order
conversion to matter boundary
AI opportunity recommendation
opportunity rejection
opportunity archival
```

---

# 8. Primary Objects

The Opportunity Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Opportunity | Opportunity | Partial Implement | Core-recognized potential service need or commercial chance. |
| Opportunity Source | Opportunity | Partial Implement | Source from which opportunity was identified. |
| Opportunity Signal | Opportunity | Partial Implement | Signal or trigger supporting the opportunity. |
| Opportunity Status | Opportunity | Partial Implement | Controlled status of opportunity lifecycle. |
| Opportunity Context | Opportunity | Partial Implement | Context linking opportunity to professional and business objects. |
| Opportunity Score | Opportunity / AI Governance | Deferred | Scoring reference, not final sales truth. |
| Opportunity Recommendation | Opportunity / AI Governance | Partial Implement | Suggested next action or commercial recommendation. |
| Opportunity Qualification Record | Opportunity / Review and Approval | Partial Implement | Review result for qualification. |
| Opportunity Conversion Record | Opportunity / Customer / Order / Matter | Partial Implement | Record of conversion into Customer, Order or Matter. |
| Opportunity Audit Reference | Opportunity / Audit | Partial Implement | Audit reference for opportunity-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Customer | Customer | Opportunity may link to or convert into Customer. |
| Order | Order | Opportunity may convert into Order. |
| Matter | Matter | Matter should usually be created from Order, not directly from Opportunity. |
| Brand | Brand | Opportunity may relate to Brand protection need. |
| Trademark | Trademark | Opportunity may relate to Trademark lifecycle or portfolio gap. |
| Jurisdiction | Jurisdiction | Opportunity may suggest jurisdiction expansion. |
| Classification | Classification | Opportunity may identify classification gap or recommendation. |
| Communication | Communication | Opportunity may originate from customer inquiry or message signal. |
| Knowledge Reference | Knowledge | Opportunity rules or recommendation may cite Knowledge. |
| AI Output | AI Governance | AI may generate opportunity recommendation. |
| Audit Record | Audit | Audit records opportunity-sensitive actions. |

---

# 9. Primary Services

The Opportunity Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Opportunity Registration Service | Opportunity | Partial Implement | Create a Core Opportunity. |
| Opportunity Update Service | Opportunity | Partial Implement | Update controlled Opportunity fields. |
| Opportunity Source Service | Opportunity | Partial Implement | Link or validate Opportunity Source. |
| Opportunity Signal Service | Opportunity | Partial Implement | Link signals to Opportunity. |
| Opportunity Recommendation Service | Opportunity / AI Governance | Partial Implement | Create recommendation or suggested next action. |
| Opportunity Qualification Service | Opportunity / Review and Approval | Partial Implement | Qualify, reject or mark Opportunity as review-required. |
| Opportunity Conversion Service | Opportunity / Customer / Order | Partial Implement | Convert Opportunity to Customer or Order through governed rules. |
| Opportunity Scoring Service | Opportunity / AI Governance | Deferred | Produce scoring reference, not final decision. |
| Opportunity Reference Validation Service | Opportunity | Partial Implement | Validate Opportunity references used by other domains. |
| Opportunity Audit Reference Service | Opportunity / Audit | Partial Implement | Produce opportunity audit reference for governed actions. |

Service rules:

```text
- Mutating Opportunity services must emit events.
- Opportunity services must not create Order without Order service.
- Opportunity services must not create Matter directly in MVP.
- AI-generated recommendations must be marked as Suggested or ReviewRequired.
- Opportunity conversion must preserve source, signal and actor trace.
- Scoring must not be treated as final commercial decision.
```

---

# 10. Primary Events

The Opportunity Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| OpportunityCreated | Opportunity Registration Service | Partial Implement | A Core Opportunity has been created. |
| OpportunityUpdated | Opportunity Update Service | Partial Implement | Controlled Opportunity fields have changed. |
| OpportunitySourceLinked | Opportunity Source Service | Partial Implement | Source has been linked to Opportunity. |
| OpportunitySignalLinked | Opportunity Signal Service | Partial Implement | Signal has been linked to Opportunity. |
| OpportunityStatusChanged | Opportunity Qualification Service / Update Service | Partial Implement | Opportunity status has changed. |
| OpportunityRecommendationCreated | Opportunity Recommendation Service | Partial Implement | Recommendation has been created. |
| OpportunityScoreUpdated | Opportunity Scoring Service | Deferred | Score reference has changed. |
| OpportunityQualificationRequired | Opportunity Recommendation Service | Partial Implement | Opportunity requires qualification review. |
| OpportunityQualified | Opportunity Qualification Service | Partial Implement | Opportunity has been qualified for next action. |
| OpportunityRejected | Opportunity Qualification Service | Partial Implement | Opportunity has been rejected. |
| OpportunityConvertedToCustomer | Opportunity Conversion Service | Partial Implement | Opportunity has been converted or linked to Customer. |
| OpportunityConvertedToOrder | Opportunity Conversion Service / Order Service | Partial Implement | Opportunity has been converted into Order. |
| OpportunityReferenceValidated | Opportunity Reference Validation Service | Partial Implement | Opportunity reference has been validated for governed use. |
| OpportunityArchived | Opportunity Update Service | Deferred | Opportunity has been archived. |

Event rules:

```text
- Opportunity events must reference Opportunity.
- Conversion events must reference created or linked Customer/Order.
- Recommendation events must distinguish AI, system and human source.
- Score events must not imply final qualification.
- Opportunity events must not expose confidential customer or trademark details unnecessarily.
```

---

# 11. Primary Contracts

Opportunity requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Opportunity Contract | Opportunity Contract | Partial Implement | Defines Opportunity fields, status, source, signal and context. |
| Opportunity Source Contract | Opportunity Contract | Partial Implement | Defines source type, reference and validation rules. |
| Opportunity Signal Contract | Opportunity Contract | Partial Implement | Defines signal type, evidence/context and source trace. |
| Opportunity Recommendation Contract | Opportunity / AI Contract | Partial Implement | Defines recommendation source, output status and review requirement. |
| Opportunity Qualification Contract | Opportunity / Review Contract | Partial Implement | Defines qualification, rejection and review-required behavior. |
| Opportunity Conversion Contract | Opportunity / Customer / Order Contract | Partial Implement | Defines conversion into Customer or Order through governed services. |
| Opportunity Score Contract | Opportunity / AI Contract | Deferred | Defines scoring fields and non-final decision boundary. |
| Opportunity Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for opportunity-sensitive actions. |

Contract rules:

```text
- Opportunity Contract must not define Order commercial commitment.
- Opportunity Conversion Contract must use Customer and Order services where conversion occurs.
- Recommendation Contract must distinguish suggestion from qualified opportunity.
- Score Contract must not be used as final sales decision.
```

---

# 12. Relationships to Other Domains

## 12.1 Customer

Opportunity may link to or convert into Customer.

Customer owns demand-side party meaning.

Opportunity owns potential need meaning.

## 12.2 Order

Opportunity may convert into Order when commercial scope is confirmed.

Order owns commercial service request meaning.

## 12.3 Matter

Matter should normally be created from Order.

Opportunity should not directly create Matter in MVP.

## 12.4 Brand

Opportunity may identify Brand protection gaps, new filing needs or brand expansion needs.

Brand owns commercial identity.

## 12.5 Trademark

Opportunity may arise from Trademark status, deadline, goods/services gap, jurisdiction gap, renewal need or portfolio analysis.

Trademark owns protection-record meaning.

## 12.6 Jurisdiction

Opportunity may recommend jurisdiction expansion or jurisdiction-specific service need.

Jurisdiction owns where procedure applies.

## 12.7 Classification

Opportunity may identify class gap, goods/services expansion or filing package recommendation.

Classification owns goods/services and class meaning.

## 12.8 Communication

Opportunity may originate from customer inquiry, email, chat or agent communication.

Communication owns message lifecycle.

## 12.9 Knowledge

Knowledge may support recommendation rules and opportunity explanation.

Opportunity does not define Knowledge validity.

## 12.10 AI Governance

AI may generate opportunity recommendations, but must not qualify or convert high-risk opportunities without review and governed services.

## 12.11 Audit

Audit records should include Opportunity references for opportunity-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Opportunity only under governed Agent Contracts.

Allowed AI use:

```text
identify potential opportunity signals
summarize opportunity context
suggest missing customer or brand information
recommend possible next action
flag jurisdiction or classification gaps
prepare draft sales or service note
compare opportunity with existing Customer, Order or Matter references
suggest whether human qualification is required
```

AI must not:

```text
create qualified Opportunity without authorized service and review rules
convert Opportunity to Order without governed Order service
create Matter directly from Opportunity in MVP
assign final commercial value or priority as truth
send sales communication externally without review where required
invent opportunity source
use confidential trademark or customer data outside authorized scope
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Opportunity Object Access Rule
Opportunity Service Access Rule
Opportunity Event Access Rule
Customer / Brand / Trademark Access Rules
Policy Rule
Review Rule
Audit Rule
Human Review Rule for commercial or external outputs
```

---

# 14. Workflow Usage

Opportunity participates in pre-order business workflows.

Opportunity-sensitive workflows may include:

```text
opportunity-intake-workflow.md
opportunity-signal-review-workflow.md
opportunity-qualification-workflow.md
opportunity-recommendation-review-workflow.md
opportunity-to-customer-conversion-workflow.md
opportunity-to-order-conversion-workflow.md
ai-opportunity-recommendation-review-workflow.md
trademark-portfolio-opportunity-workflow.md
```

Workflow rules:

```text
- Opportunity workflows must reference Workflow Contracts.
- AI-generated opportunities must be reviewable before external or commercial action.
- Opportunity-to-Order conversion must use Order services.
- Opportunity-to-Customer conversion must use Customer services.
- Direct Opportunity-to-Matter conversion is deferred unless later approved.
- Opportunity rejection and archival must preserve source and signal trace.
```

---

# 15. API Usage

Opportunity APIs expose opportunity creation, source, signal, recommendation, qualification and conversion through governed services.

Potential Phase 4 APIs:

```text
POST /opportunities
GET /opportunities/{id}
PATCH /opportunities/{id}
POST /opportunities/{id}/sources
POST /opportunities/{id}/signals
POST /opportunities/{id}/recommendations
POST /opportunities/{id}/qualification
POST /opportunities/{id}/convert-to-customer
POST /opportunities/{id}/convert-to-order
POST /opportunities/reference/validate
```

Deferred APIs:

```text
POST /opportunities/{id}/score
GET /opportunities/{id}/audit-reference
POST /opportunities/{id}/archive
POST /opportunities/batch-detect
```

API rules:

```text
- APIs must invoke Opportunity Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not create Order without Order service.
- APIs must not create Matter directly in MVP.
- Mutating APIs must emit or cause service-level events.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

API details belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

## 16.1 MVP / Phase 4 Consumers

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
Customer development tools
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
CRM integrations
Marketing automation
Portfolio analytics products
Opportunity intelligence products
```

Product rule:

```text
Products consume Opportunity.
Products do not redefine Opportunity.
```

---

# 17. MVP Scope

Opportunity is a Phase 4 / Wave 4 Partial Implement domain.

MVP / Phase 4 includes:

```text
Opportunity
Opportunity Source
Opportunity Signal
Opportunity Status
Opportunity Context
Opportunity Recommendation
Opportunity Conversion Record
Opportunity Registration Service
Opportunity Update Service
Opportunity Source Service
Opportunity Signal Service
Opportunity Recommendation Service
Opportunity Qualification Service
Opportunity Conversion Service
Opportunity Reference Validation Service
OpportunityCreated event
OpportunityUpdated event
OpportunitySourceLinked event
OpportunitySignalLinked event
OpportunityStatusChanged event
OpportunityRecommendationCreated event
OpportunityQualificationRequired event
OpportunityQualified event
OpportunityRejected event
OpportunityConvertedToCustomer event
OpportunityConvertedToOrder event
OpportunityReferenceValidated event
basic opportunity metadata validation
source traceability to Customer, Brand, Trademark, Jurisdiction, Classification, Communication, Order and AI systems
```

Phase 4 should support:

```text
manual opportunity creation
AI-assisted opportunity suggestion
signal and source reference
qualification / rejection
conversion to Customer
conversion to Order
basic commercial recommendation with human review
```

MVP does not require full CRM pipeline, automated scoring engine, marketing automation or batch opportunity mining platform.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full opportunity scoring engine
automated batch opportunity detection
full CRM pipeline
marketing automation
campaign attribution
customer lifetime value prediction
automatic commercial priority ranking
portfolio-wide gap mining
external CRM synchronization
advertising platform integration
automatic outbound sales communication
opportunity marketplace
advanced opportunity analytics
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Opportunity should use stable immutable ID.
Opportunity Source should be required.
Opportunity Signal should preserve source and context reference.
Opportunity Recommendation should distinguish AI, system and human source.
Opportunity Status should use controlled values.
Opportunity Conversion Record should preserve created or linked Customer/Order references.
Opportunity Score, if present, must be non-final and review-sensitive.
AI-generated opportunity recommendations should remain draft/recommendation output until reviewed where needed.
```

Suggested Opportunity Status values:

```text
Draft
Suggested
ReviewRequired
Qualified
Rejected
ConvertedToCustomer
ConvertedToOrder
Deferred
Archived
```

Phase 4 controlled Opportunity Status values:

```text
Draft
Suggested
ReviewRequired
Qualified
Rejected
ConvertedToCustomer
ConvertedToOrder
Archived
```

Suggested Opportunity Source values:

```text
ManualInput
CustomerInquiry
CommunicationSignal
TrademarkPortfolioSignal
BrandProtectionGap
JurisdictionExpansionSignal
ClassificationGapSignal
RenewalSignal
AgentReferral
PartnerReferral
AIRecommendation
ImportedLead
```

Phase 4 controlled Source values:

```text
ManualInput
CustomerInquiry
CommunicationSignal
TrademarkPortfolioSignal
BrandProtectionGap
JurisdictionExpansionSignal
ClassificationGapSignal
AIRecommendation
ImportedLead
```

Suggested Recommendation Status values:

```text
Draft
Suggested
ReviewRequired
Accepted
Rejected
Converted
Superseded
```

Do not treat an AI opportunity suggestion as a qualified sales opportunity.

---

# 20. Codex Implementation Notes

Codex may implement Opportunity only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Opportunity / Customer boundary
preserve Opportunity / Order boundary
preserve Opportunity / Matter boundary
preserve Opportunity / AI Governance boundary
implement only Phase 4 Partial scope unless task says otherwise
write tests for opportunity creation
write tests for source requirement
write tests for signal linking
write tests for recommendation source and status
write tests for qualification and rejection
write tests for conversion through Customer and Order services
write tests preventing direct Matter creation in MVP
write tests preventing AI suggestion from becoming qualified opportunity automatically
```

Codex must not:

```text
invent full CRM pipeline in Opportunity MVP
invent automated scoring engine in MVP
invent marketing automation in Opportunity
create Order without Order service
create Matter directly from Opportunity in MVP
treat AI suggestion as qualified opportunity
send external sales communication without governed Communication and review
expose confidential customer or trademark data without Permission and Policy
allow product UI to redefine Opportunity status
```

---

# 21. Validation Rules

Opportunity Domain must pass the following checks.

```text
[ ] Opportunity is classified as Business Execution Domain.
[ ] Opportunity is counted within the 26 baseline Core Domains.
[ ] Opportunity does not change the baseline Core Domain Map.
[ ] Opportunity has MVP Phase 4 / Wave 4 classification.
[ ] Opportunity has MVP Depth = Partial Implement.
[ ] Opportunity defines Core meaning.
[ ] Opportunity boundary excludes Customer lifecycle.
[ ] Opportunity boundary excludes Order commercial commitment.
[ ] Opportunity boundary excludes Matter professional execution.
[ ] Opportunity boundary excludes full CRM and marketing automation.
[ ] Opportunity boundary excludes final AI scoring decision.
[ ] Opportunity owns Opportunity object.
[ ] Opportunity defines Opportunity Source.
[ ] Opportunity defines Opportunity Signal.
[ ] Opportunity defines Opportunity Recommendation.
[ ] Opportunity defines Opportunity Conversion Record.
[ ] Opportunity lists primary services.
[ ] Mutating Opportunity services emit events.
[ ] Opportunity lists primary events.
[ ] Opportunity defines contract requirements.
[ ] Opportunity defines AI Agent usage constraints.
[ ] Opportunity defines workflow usage constraints.
[ ] Opportunity defines API usage constraints.
[ ] Opportunity defines product consumers.
[ ] Opportunity defines MVP and deferred scope.
[ ] Opportunity defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Opportunity into Customer
turn Opportunity into Order
turn Opportunity into Matter
turn Opportunity into full CRM
turn Opportunity into marketing automation
turn Opportunity into final AI sales decision
turn Opportunity into pricing engine
turn Opportunity into communication sender
create Order without Order service
create Matter directly from Opportunity in MVP
treat AI suggestion as qualified opportunity
treat score as final commercial decision
expose confidential opportunity context without Permission and Policy
allow product UI to redefine Opportunity meaning
allow Codex to define new opportunity architecture
```

---

# 23. Acceptance Criteria

This Opportunity Domain Specification is accepted only if:

```text
[ ] It defines Opportunity purpose.
[ ] It defines Opportunity Core meaning.
[ ] It identifies Opportunity as Business Execution Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Customer, Order, Matter, Brand, Trademark, Jurisdiction, Classification, Communication, Knowledge, AI Governance and Audit.
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
| 0.1.0 | Draft | Initial Opportunity Domain specification. Establishes Opportunity as Business Execution Domain with Phase 4 Partial Implement depth, defines Opportunity, Source, Signal, Recommendation, Qualification and Conversion boundaries, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
