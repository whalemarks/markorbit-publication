# Domain Specification — Service Provider

**Spec ID:** B02-DOM-SERVICE-PROVIDER  
**Spec Type:** Domain  
**Domain Name:** Service Provider  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/service-provider.md; core-specs/objects/service-provider-profile.md; core-specs/objects/service-provider-contact.md; core-specs/objects/service-provider-capability.md; core-specs/objects/service-provider-jurisdiction-scope.md; core-specs/objects/service-provider-status.md; core-specs/objects/service-provider-commercial-reference.md  
**Related Service Specs:** core-specs/services/service-provider-registration-service.md; core-specs/services/service-provider-contact-service.md; core-specs/services/service-provider-capability-service.md; core-specs/services/service-provider-jurisdiction-scope-service.md; core-specs/services/service-provider-status-service.md; core-specs/services/service-provider-reference-validation-service.md  
**Related Event Specs:** core-specs/events/service-provider-created.md; core-specs/events/service-provider-updated.md; core-specs/events/service-provider-contact-linked.md; core-specs/events/service-provider-capability-updated.md; core-specs/events/service-provider-jurisdiction-scope-updated.md; core-specs/events/service-provider-status-changed.md; core-specs/events/service-provider-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/service-provider/service-provider-contract.md; core-specs/contracts/service-provider/service-provider-profile-contract.md; core-specs/contracts/service-provider/service-provider-contact-contract.md; core-specs/contracts/service-provider/service-provider-capability-contract.md; core-specs/contracts/service-provider/service-provider-jurisdiction-scope-contract.md; core-specs/contracts/service-provider/service-provider-commercial-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Execution Extension Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Service Provider Domain defines the Core meaning of an external or internal provider that can deliver, support or participate in trademark-related services in MarkOrbit.

It exists so that Agents, Routing, Orders, Matters, Communications, Documents, Evidence, Tasks, Partner workflows, AI Agents and product consumers can consistently reference provider identity, provider contacts, service capabilities, jurisdiction scope, status and commercial reference boundaries.

Service Provider is required before:

```text
provider profile management
service capability mapping
provider contact management
provider jurisdiction scope reference
agent-provider relationship handling
routing input preparation
service procurement planning
provider communication tracking
provider matter participation
provider commercial reference
AI provider recommendation support
Codex implementation of collaboration workflows
```

The Service Provider Domain is a Collaboration Network Domain because MarkOrbit’s service network must connect internal execution with external capability providers.

---

# 2. Core Meaning

Service Provider means:

```text
a Core-recognized provider entity that may offer one or more service capabilities, operate in one or more jurisdictions, maintain contacts and participate in service delivery, routing, communication or matter execution.
```

Service Provider is not merely:

```text
an Agent
a Partner
a Customer
a User
an Organization
a contact person
a vendor invoice account
a price list
a routing decision
a marketplace listing
a matter participant only
a communication thread
```

Service Provider answers:

```text
Who or what provider entity can support service delivery?
Which service capabilities are known?
Which jurisdictions or service scopes apply?
Which contacts and communication channels are associated with it?
Is the provider active, inactive, review-required or do-not-use?
How does it relate to Agents, Routing, Matters, Orders and Communication?
What source, commercial reference or audit trace supports the provider profile?
```

---

# 3. Domain Category

Service Provider is a Collaboration Network Domain.

Collaboration Network Domains provide the Core basis for:

```text
external capability reference
provider profile management
service capability mapping
jurisdiction support mapping
routing inputs
collaboration network growth
procurement preparation
provider communication
AI-assisted provider recommendation
service network expansion
```

Service Provider is broader than Agent.

An Agent may be linked to a Service Provider, but not every Service Provider is an Agent.

---

# 4. Architectural Position

Service Provider sits in the Collaboration Network Core between provider identity/capability and routing.

```text
Jurisdiction defines where service applies
        ↓
Service Provider defines provider entity and capability
        ↓
Agent may represent trademark-specific collaborator role
        ↓
Routing selects provider or agent
        ↓
Communication carries instructions and replies
        ↓
Matter and Task coordinate execution
```

Service Provider provides capability and commercial profile context.

Agent provides trademark collaborator role.

Routing makes selection decisions.

Communication handles messages.

Matter executes work.

---

# 5. Scope

The Service Provider Domain includes:

```text
service provider definition
provider profile
provider type
provider status
provider contact
provider service capability
provider jurisdiction scope
provider commercial reference boundary
provider agent relationship boundary
provider routing eligibility reference
provider communication reference boundary
provider matter participation boundary
provider document/evidence participation boundary
provider reference validation
provider audit reference
provider event emission
provider use by AI Agents, Services, Workflows, APIs and Codex tasks
```

Phase 4 implementation should focus on:

```text
Service Provider
Service Provider Profile
Service Provider Contact
Service Provider Status
Service Provider Capability
Service Provider Jurisdiction Scope
Service Provider Commercial Reference
Service Provider Registration Service
Service Provider Contact Service
Service Provider Capability Service
Service Provider Jurisdiction Scope Service
Service Provider Status Service
Service Provider Reference Validation Service
ServiceProviderCreated event
ServiceProviderContactLinked event
ServiceProviderCapabilityUpdated event
ServiceProviderJurisdictionScopeUpdated event
ServiceProviderStatusChanged event
ServiceProviderReferenceValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

The Service Provider Domain owns:

```text
Core Service Provider definition
provider profile
provider type
provider status
provider contact boundary
provider service capability
provider jurisdiction scope
provider commercial reference boundary
provider relationship to Agent
provider routing eligibility reference
provider communication reference boundary
provider matter participation boundary
provider reference validation
provider event emission
provider reference used by collaboration workflows and products
```

## 6.2 Out of Boundary

The Service Provider Domain does not own:

```text
Agent trademark collaborator role meaning
Partner relationship lifecycle
Customer lifecycle
User account lifecycle
Organization tenant meaning
Routing selection logic
Communication message lifecycle
Matter execution lifecycle
Order commercial lifecycle
payment or settlement lifecycle
procurement marketplace
provider contract legal management
advanced performance analytics
official filing automation
```

Those responsibilities belong to:

```text
Agent Domain
Partner Domain
Customer Domain
User Domain
Organization Domain
Routing Domain
Communication Domain
Matter Domain
Order Domain
Finance/Product implementation
Product implementation
External integration implementation
```

## 6.3 Boundary Notes

Service Provider is the provider entity and capability profile.

Agent is a trademark-specific collaborator role.

Routing selects among eligible providers or agents.

Partner is a cooperation or channel relationship.

Service Provider must not be overloaded into all external-party meanings.

---

# 7. Domain Rules

## 7.1 Service Provider Requires Capability or Explicit Pending Capability

Every Service Provider should have at least one service capability or explicit capability-pending status.

A provider without service capability is not routing-ready.

## 7.2 Service Provider Requires Contact Boundary

A Service Provider must have at least one contact reference or explicit contact-pending status before external communication.

Service Provider Contact is not a User unless linked through User/Identity rules.

## 7.3 Service Provider Does Not Equal Agent

An Agent may be linked to Service Provider.

Service Provider is broader and may include law firms, vendors, consultants, search providers, translation providers, document providers or technical providers.

Agent owns trademark-specific agent role.

## 7.4 Service Provider Does Not Own Routing

Service Provider may provide eligibility and capability data.

Routing Domain owns selection, ranking, fallback and route decision logic.

## 7.5 Commercial References Are Not Finance Lifecycle

Service Provider may contain commercial reference such as standard fee note, quote reference, payment term note or procurement note.

It must not own payment, invoice, settlement or accounting lifecycle.

## 7.6 Service Provider Must Be Auditable

Service Provider-sensitive actions must preserve audit trace.

Audit-sensitive service provider actions include:

```text
provider creation
provider profile update
provider contact update
capability update
jurisdiction scope update
status change
commercial reference update
agent relationship linking
routing eligibility change
matter participation involving provider
external communication to provider
AI provider recommendation
provider deactivation
```

---

# 8. Primary Objects

The Service Provider Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Service Provider | Service Provider | Partial Implement | Core provider entity capable of supporting service delivery. |
| Service Provider Profile | Service Provider | Partial Implement | Profile fields describing provider identity and background. |
| Service Provider Type | Service Provider | Partial Implement | Controlled type of provider. |
| Service Provider Status | Service Provider | Partial Implement | Controlled usability status. |
| Service Provider Contact | Service Provider / Communication | Partial Implement | Contact reference for provider communication. |
| Service Provider Capability | Service Provider | Partial Implement | Services the provider can support. |
| Service Provider Jurisdiction Scope | Service Provider / Jurisdiction | Partial Implement | Jurisdictions supported by provider. |
| Service Provider Commercial Reference | Service Provider / Order / Finance | Partial Implement | Quote, fee, term or commercial note boundary. |
| Service Provider Agent Link | Service Provider / Agent | Partial Implement | Relationship between provider and Agent role. |
| Service Provider Routing Eligibility Reference | Service Provider / Routing | Partial Implement | Eligibility input used by Routing. |
| Service Provider Performance Reference | Service Provider / Reporting | Deferred | Performance or reliability reference, not full analytics. |
| Service Provider Audit Reference | Service Provider / Audit | Partial Implement | Audit reference for provider-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Agent | Agent | Agent may be linked to Service Provider. |
| Jurisdiction | Jurisdiction | Provider may support one or more jurisdictions. |
| Routing | Routing | Routing may select provider. |
| Communication | Communication | Provider participates in communication. |
| Matter | Matter | Provider may participate in execution. |
| Order | Order | Provider may support service fulfillment through Matter. |
| Partner | Partner | Provider may also be a partner in broader cooperation. |
| Document | Document | Provider may provide or request Documents. |
| Evidence | Evidence | Provider may provide or request Evidence. |
| Task | Task | Provider follow-up may create Tasks. |
| Knowledge Reference | Knowledge | Provider rules/notes may cite Knowledge. |
| AI Output | AI Governance | AI may recommend or summarize providers. |
| Audit Record | Audit | Audit records provider-sensitive actions. |

---

# 9. Primary Services

The Service Provider Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Service Provider Registration Service | Service Provider | Partial Implement | Create a Core Service Provider. |
| Service Provider Update Service | Service Provider | Partial Implement | Update controlled provider fields. |
| Service Provider Contact Service | Service Provider / Communication | Partial Implement | Link or update provider contacts. |
| Service Provider Capability Service | Service Provider | Partial Implement | Link or update provider service capabilities. |
| Service Provider Jurisdiction Scope Service | Service Provider / Jurisdiction | Partial Implement | Link or update jurisdiction scope. |
| Service Provider Status Service | Service Provider | Partial Implement | Update provider status through governed rules. |
| Service Provider Commercial Reference Service | Service Provider / Order / Finance | Partial Implement | Link quote, fee or term reference without owning finance lifecycle. |
| Service Provider Agent Link Service | Service Provider / Agent | Partial Implement | Link provider to Agent role where applicable. |
| Service Provider Routing Eligibility Service | Service Provider / Routing | Partial Implement | Produce routing eligibility reference. |
| Service Provider Reference Validation Service | Service Provider | Partial Implement | Validate provider references used by other domains. |
| Service Provider Audit Reference Service | Service Provider / Audit | Partial Implement | Produce provider audit reference for governed actions. |

Service rules:

```text
- Mutating Service Provider services must emit events.
- Service Provider services must not own Routing decision logic.
- Service Provider services must not own Communication message lifecycle.
- Service Provider services must not own Matter or Order lifecycle.
- Commercial references must not become payment or settlement lifecycle.
- AI-generated provider recommendations must be draft/review-required.
```

---

# 10. Primary Events

The Service Provider Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| ServiceProviderCreated | Service Provider Registration Service | Partial Implement | Service Provider has been created. |
| ServiceProviderUpdated | Service Provider Update Service | Partial Implement | Controlled provider fields have changed. |
| ServiceProviderStatusChanged | Service Provider Status Service | Partial Implement | Provider Status has changed. |
| ServiceProviderContactLinked | Service Provider Contact Service | Partial Implement | Provider Contact has been linked. |
| ServiceProviderContactUpdated | Service Provider Contact Service | Partial Implement | Provider Contact has changed. |
| ServiceProviderCapabilityUpdated | Service Provider Capability Service | Partial Implement | Provider service capability has changed. |
| ServiceProviderJurisdictionScopeUpdated | Service Provider Jurisdiction Scope Service | Partial Implement | Provider jurisdiction scope has changed. |
| ServiceProviderCommercialReferenceUpdated | Service Provider Commercial Reference Service | Partial Implement | Provider commercial reference has changed. |
| ServiceProviderAgentLinked | Service Provider Agent Link Service | Partial Implement | Provider has been linked to Agent role. |
| ServiceProviderRoutingEligibilityUpdated | Service Provider Routing Eligibility Service | Partial Implement | Routing eligibility reference has changed. |
| ServiceProviderReferenceValidated | Service Provider Reference Validation Service | Partial Implement | Provider reference has been validated for governed use. |
| ServiceProviderReviewRequired | Service Provider Update / Capability Service | Partial Implement | Provider information requires review. |

Event rules:

```text
- Service Provider events must reference Service Provider.
- Contact events must not expose sensitive contact details unnecessarily.
- Jurisdiction scope events must reference Jurisdiction.
- Capability events must reference service capability and source where applicable.
- Commercial reference events must not imply payment or settlement.
- Routing eligibility events must not represent final routing decision.
```

---

# 11. Primary Contracts

Service Provider requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Service Provider Contract | Service Provider Contract | Partial Implement | Defines provider fields, type, status, capability and jurisdiction references. |
| Service Provider Profile Contract | Service Provider Contract | Partial Implement | Defines provider identity, background and profile references. |
| Service Provider Contact Contract | Service Provider / Communication Contract | Partial Implement | Defines contact reference and allowed use. |
| Service Provider Capability Contract | Service Provider Contract | Partial Implement | Defines supported service capabilities. |
| Service Provider Jurisdiction Scope Contract | Service Provider / Jurisdiction Contract | Partial Implement | Defines supported jurisdictions and scope status. |
| Service Provider Commercial Reference Contract | Service Provider / Order / Finance Contract | Partial Implement | Defines quote, fee or term reference boundary. |
| Service Provider Agent Link Contract | Service Provider / Agent Contract | Partial Implement | Defines relationship to Agent role. |
| Service Provider Routing Eligibility Contract | Service Provider / Routing Contract | Partial Implement | Defines eligibility input for Routing, not final selection. |
| Service Provider Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for provider-sensitive actions. |

Contract rules:

```text
- Service Provider Contract must not redefine Agent.
- Capability Contract must define source-aware service capability.
- Commercial Reference Contract must not define payment or settlement lifecycle.
- Routing Eligibility Contract must not make final routing decision.
```

---

# 12. Relationships to Other Domains

## 12.1 Agent

Agent may be linked to Service Provider.

Agent owns trademark collaborator role.

Service Provider owns broader provider profile and capability.

## 12.2 Jurisdiction

Service Provider may support one or more jurisdictions.

Jurisdiction owns where procedure applies.

## 12.3 Routing

Routing uses provider scope, capability, status and eligibility to select provider.

Routing owns selection logic.

## 12.4 Communication

Communication records messages with Service Provider.

Communication owns thread and message lifecycle.

## 12.5 Matter

Service Provider may participate in Matter execution.

Matter owns professional execution container.

## 12.6 Order

Order may require provider service through Matter.

Order owns commercial service request.

## 12.7 Partner

A Service Provider may also have partner relationship characteristics.

Partner Domain owns cooperation/channel relationship lifecycle.

## 12.8 Document and Evidence

Service Provider may provide, request or review Documents and Evidence.

Document and Evidence retain their own meanings.

## 12.9 Task

Provider follow-up may create Tasks.

Task owns actionable work unit.

## 12.10 AI Governance

AI may recommend providers, summarize provider history or flag capability gaps, but must not make final routing or procurement decisions where review is required.

## 12.11 Audit

Audit records should include Service Provider references for provider-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Service Provider only under governed Agent Contracts.

Allowed AI use:

```text
summarize provider profile
identify missing provider capability
identify missing provider contact information
suggest possible providers for routing review
compare provider service capabilities
draft provider instruction or follow-up message
summarize provider communication history if authorized
flag provider status, jurisdiction or capability mismatch
```

AI must not:

```text
make final routing or procurement decision without governed service and review
create Service Provider without authorized service
invent provider capability
invent provider contact details
send instructions to Service Provider without Communication service and review where required
mark provider active without review/source
override provider status
alter commercial references without authorized service
expose confidential provider/customer/matter data outside authorized scope
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Service Provider Object Access Rule
Service Provider Service Access Rule
Service Provider Event Access Rule
Jurisdiction / Agent / Routing Access Rules
Communication Rule
Permission Rule
Policy Rule
Review Rule
Audit Rule
Human Review Rule for routing, procurement and external instructions
```

---

# 14. Workflow Usage

Service Provider participates in collaboration workflows.

Service Provider-sensitive workflows may include:

```text
service-provider-registration-workflow.md
service-provider-contact-review-workflow.md
service-provider-capability-review-workflow.md
service-provider-jurisdiction-scope-review-workflow.md
service-provider-agent-link-workflow.md
service-provider-routing-eligibility-workflow.md
service-provider-instruction-communication-workflow.md
ai-service-provider-recommendation-review-workflow.md
```

Workflow rules:

```text
- Service Provider workflows must reference Workflow Contracts.
- Provider capability and jurisdiction scope should be reviewable.
- Routing decisions must use Routing service, not Service Provider service.
- External instructions to Service Provider must use Communication service.
- Commercial references must not trigger payment or settlement lifecycle.
- AI-generated recommendations must remain draft/review-required where routing or procurement affects execution.
```

---

# 15. API Usage

Service Provider APIs expose provider creation, contacts, jurisdiction scope, capabilities, status and reference validation through governed services.

Potential Phase 4 APIs:

```text
POST /service-providers
GET /service-providers/{id}
PATCH /service-providers/{id}
POST /service-providers/{id}/contacts
POST /service-providers/{id}/capabilities
POST /service-providers/{id}/jurisdiction-scopes
POST /service-providers/{id}/status
POST /service-providers/{id}/commercial-references
POST /service-providers/{id}/agent-links
POST /service-providers/reference/validate
```

Potential partial/deferred APIs:

```text
POST /service-providers/{id}/routing-eligibility
GET /service-providers/{id}/performance-reference
GET /service-providers/{id}/audit-reference
POST /service-providers/{id}/ai-summary
```

API rules:

```text
- APIs must invoke Service Provider Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not perform Routing selection directly.
- APIs must not send Communication messages directly.
- APIs must not mutate payment, invoice or settlement lifecycle.
- APIs must not expose confidential provider or matter data without Permission and Policy.
- Mutating APIs must emit or cause service-level events.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

API details belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

## 16.1 Phase 4 Consumers

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
Partner Center
Service Platform
Routing baseline
Communication tools
Reporting consumers
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Provider procurement products
Provider performance analytics
Partner settlement products
Advanced routing products
```

Product rule:

```text
Products consume Service Provider.
Products do not redefine Service Provider.
```

---

# 17. MVP Scope

Service Provider is a Phase 4 / Wave 4 Partial Implement domain.

Phase 4 includes:

```text
Service Provider
Service Provider Profile
Service Provider Type
Service Provider Status
Service Provider Contact
Service Provider Capability
Service Provider Jurisdiction Scope
Service Provider Commercial Reference
Service Provider Agent Link
Service Provider Routing Eligibility Reference
Service Provider Registration Service
Service Provider Update Service
Service Provider Contact Service
Service Provider Capability Service
Service Provider Jurisdiction Scope Service
Service Provider Status Service
Service Provider Commercial Reference Service
Service Provider Agent Link Service
Service Provider Reference Validation Service
ServiceProviderCreated event
ServiceProviderUpdated event
ServiceProviderStatusChanged event
ServiceProviderContactLinked event
ServiceProviderContactUpdated event
ServiceProviderCapabilityUpdated event
ServiceProviderJurisdictionScopeUpdated event
ServiceProviderCommercialReferenceUpdated event
ServiceProviderAgentLinked event
ServiceProviderReferenceValidated event
basic provider metadata validation
source traceability to Agent, Jurisdiction, Routing, Communication, Matter, Order, Document, Evidence and AI systems
```

Phase 4 should support:

```text
basic provider profile
basic contact reference
basic capability reference
basic jurisdiction scope
basic status
basic commercial reference
agent link
routing eligibility reference
AI-assisted provider summary/recommendation with human review
```

Phase 4 does not require provider marketplace, settlement lifecycle, performance analytics or automated procurement.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full provider marketplace
provider performance analytics
automated provider ranking
procurement bidding
provider settlement system
contract management
provider onboarding portal
provider SLA scoring
external provider database synchronization
automatic routing optimization
risk-based provider selection
provider self-service portal
revenue sharing and settlement engine
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Service Provider should use stable immutable ID.
Service Provider Contact should not automatically become User.
Service Provider Capability should be controlled and source-aware.
Service Provider Jurisdiction Scope should reference Jurisdiction.
Service Provider Commercial Reference should preserve quote/fee/term reference but not finance lifecycle.
Service Provider Status should use controlled values.
Routing eligibility should remain reference-level until Routing decides.
Performance analytics should remain deferred unless explicitly approved.
AI-generated provider recommendations should remain draft/recommendation output until reviewed where needed.
```

Suggested Service Provider Status values:

```text
Draft
Active
ReviewRequired
Suspended
Inactive
DoNotUse
Archived
```

Phase 4 controlled Service Provider Status values:

```text
Draft
Active
ReviewRequired
Inactive
DoNotUse
Archived
```

Suggested Service Provider Type values:

```text
TrademarkAgent
LawFirm
SearchProvider
TranslationProvider
DocumentProvider
EvidenceProvider
TechnologyProvider
Consultant
InternalProvider
Other
Unknown
```

Phase 4 controlled Service Provider Type values:

```text
TrademarkAgent
LawFirm
SearchProvider
TranslationProvider
DocumentProvider
EvidenceProvider
Consultant
Other
Unknown
```

Suggested Service Capability values:

```text
TrademarkFiling
TrademarkSearch
OfficeActionResponse
Renewal
Change
Assignment
Opposition
Cancellation
EvidenceReview
DocumentReview
Translation
LegalOpinion
GeneralConsultation
TechnologySupport
```

Do not treat Service Provider as final Routing decision or finance lifecycle.

---

# 20. Codex Implementation Notes

Codex may implement Service Provider only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Service Provider / Agent boundary
preserve Service Provider / Partner boundary
preserve Service Provider / Routing boundary
preserve Service Provider / Communication boundary
preserve Service Provider / Matter / Order boundaries
implement only Phase 4 Partial scope unless task says otherwise
write tests for provider creation
write tests for contact linking
write tests for capability reference
write tests for jurisdiction scope reference
write tests for status control
write tests for commercial reference boundary
write tests preventing Service Provider from making Routing decision
write tests preventing Service Provider Contact from becoming User automatically
write tests preventing commercial reference from becoming payment/settlement lifecycle
```

Codex must not:

```text
invent full provider marketplace in Phase 4 Partial scope
invent performance analytics in MVP
invent settlement or payment lifecycle inside Service Provider
make routing selection inside Service Provider service
send communication directly from Service Provider service
treat contact as User automatically
invent provider capability without source
allow product UI to redefine Service Provider status
```

---

# 21. Validation Rules

Service Provider Domain must pass the following checks.

```text
[ ] Service Provider is classified as Collaboration Network Domain.
[ ] Service Provider is counted within the 26 baseline Core Domains.
[ ] Service Provider does not change the baseline Core Domain Map.
[ ] Service Provider has MVP Phase 4 / Wave 4 classification.
[ ] Service Provider has MVP Depth = Partial Implement.
[ ] Service Provider defines Core meaning.
[ ] Service Provider boundary excludes Agent trademark collaborator role.
[ ] Service Provider boundary excludes Partner relationship lifecycle.
[ ] Service Provider boundary excludes Routing decision logic.
[ ] Service Provider boundary excludes Communication message lifecycle.
[ ] Service Provider boundary excludes Matter and Order lifecycle.
[ ] Service Provider boundary excludes settlement and payment lifecycle.
[ ] Service Provider owns Service Provider object.
[ ] Service Provider defines Service Provider Profile.
[ ] Service Provider defines Service Provider Contact.
[ ] Service Provider defines Service Provider Capability.
[ ] Service Provider defines Service Provider Jurisdiction Scope.
[ ] Service Provider defines Service Provider Commercial Reference.
[ ] Service Provider lists primary services.
[ ] Mutating Service Provider services emit events.
[ ] Service Provider lists primary events.
[ ] Service Provider defines contract requirements.
[ ] Service Provider defines AI Agent usage constraints.
[ ] Service Provider defines workflow usage constraints.
[ ] Service Provider defines API usage constraints.
[ ] Service Provider defines product consumers.
[ ] Service Provider defines MVP and deferred scope.
[ ] Service Provider defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Service Provider into Agent
turn Service Provider into Partner
turn Service Provider into Customer
turn Service Provider into Routing
turn Service Provider into Communication
turn Service Provider into Matter or Order
turn Service Provider into provider marketplace
turn Service Provider into payment or settlement lifecycle
turn Service Provider into performance analytics engine
make final routing decision inside Service Provider
send external communication directly from Service Provider service
treat Service Provider Contact as User automatically
invent provider capability without source
allow AI to make final routing or procurement decision
allow product UI to redefine Service Provider meaning
allow Codex to define new service provider architecture
```

---

# 23. Acceptance Criteria

This Service Provider Domain Specification is accepted only if:

```text
[ ] It defines Service Provider purpose.
[ ] It defines Service Provider Core meaning.
[ ] It identifies Service Provider as Collaboration Network Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Agent, Jurisdiction, Routing, Communication, Matter, Order, Partner, Document, Evidence, Task, AI Governance and Audit.
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
| 0.1.0 | Draft | Initial Service Provider Domain specification. Establishes Service Provider as Phase 4 Collaboration Network Domain with Partial Implement depth, defines Provider Profile, Contact, Capability, Jurisdiction Scope, Commercial Reference, Agent Link, Routing Eligibility Reference, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
