# MO-ADR-WSP-001 — Workplace Sovereignty, Product Installation, Projection and Managed Network Boundaries

## 1. Decision Metadata

| Field | Value |
| --- | --- |
| Decision ID | `MO-ADR-WSP-001` |
| Status | Proposed for Owner Acceptance |
| Decision type | Platform Constitution / Architecture Canon Candidate |
| Scope | Core, Execution, Workplace, MarkReg, Lite, Sites, MGSN and future Workplace Products |
| Authority | Repository-level architecture governance after explicit Owner acceptance |
| Backward treatment | Does not silently rewrite frozen Books; creates controlled next-version and Product inputs |
| Implementation authority | None |
| External protected-action authority | None |

## 2. Decision Summary

MarkOrbit adopts the following architecture candidate:

> **Workplace is the Organization-scoped business-sovereignty, accountability and Product operating boundary.**

A Workplace carries the concrete business context through which an Organization owns or controls its customers, relationships, business records, private knowledge, people, permissions, Product Installations, projections and operating responsibility.

MarkOrbit Core provides shared semantics, governed capabilities, rules, Packs, AI, security, audit, identifiers, algorithms, connectors and Execution infrastructure. Core does not become the business owner of every concrete Customer, Order, Matter, Document or relationship merely because it defines their schemas or processes them.

Products operate through explicit Workplace-scoped installations or equivalent governed Product relationships.

MarkReg self-operated business is itself an Organization and Workplace. It does not receive automatic access to Partner Workplace data.

Sites is a Workplace public projection Product.

Lite is a lightweight Workplace Product that may also expose a client-facing projection; it is not only a client portal.

A Workplace connects to MGSN through governed MGSN connection, demand, supply and Return projections. The platform owns or governs the MGSN network, admitted provider supply, procurement, routing, funds, fulfillment and platform Trust. A Workplace does not own the underlying MGSN provider pool merely because it participates in the network.

## 3. Problem Statement

The current architecture baseline correctly states that each Organization Workplace is an independent Orbit and retains its clients, data, knowledge, pricing, rules and relationships.

However, the baseline remains ambiguous in four areas:

1. Workplace is described primarily as a unified operating environment or platform shell rather than a concrete business-sovereignty and accountability boundary.
2. Core semantic authority is not sufficiently distinguished from concrete-record business ownership.
3. Product access is described without a fully explicit Product Installation and Workplace-scoped configuration model.
4. MGSN is described as connecting Workplaces through private-first network relationships, which can be misread as Workplace ownership of network supply, routing and provider resources.

This ambiguity can cause:

- Partner distrust about customer appropriation;
- incorrect global Customer or Matter pools;
- silent access by the MarkReg self-operated team;
- Product records without a clear business boundary;
- Lite being reduced to either a shell or a client portal;
- MGSN being treated either as a peer-to-peer network or as a platform that owns Partner business;
- confusion between business ownership, formal state authority, physical custody and semantic authority;
- invalid cross-Workplace data access;
- weak portability and exit guarantees.

## 4. Constitutional Definitions

### 4.1 Organization

An `Organization` is a legal, professional, commercial or managed operating entity.

Examples include:

- trademark agencies;
- law firms;
- enterprise IP departments;
- brand-service firms;
- provider organizations;
- MarkReg self-operated business;
- regional or white-label operating entities.

An Organization may have one or more Workplaces.

```text
Organization 1 → N Workplaces
```

MVP may default to one Workplace, but the architecture must not hard-code one-to-one identity.

### 4.2 Workplace

A `Workplace` is:

> **an Organization-scoped business-sovereignty, accountability, permission, Product-operation and projection boundary.**

It is not merely:

- a dashboard;
- an employee collaboration surface;
- a navigation shell;
- a folder of organizational context;
- a tenant label.

A Workplace carries or governs:

- concrete customer and relationship context;
- business records;
- people, memberships and roles;
- private knowledge and preferences;
- business policies and pricing;
- formal Product access;
- Product Installations and configurations;
- internal review and approvals;
- external projections;
- audit and accountability context;
- export and continuity rights.

### 4.3 Core

MarkOrbit Core is the shared semantics, capability and governance plane.

Core may own or govern:

- controlled type and state definitions;
- identifiers;
- Jurisdiction Packs;
- Rules and Sources;
- taxonomies and ontologies;
- capability definitions;
- algorithm versions;
- permission and audit protocols;
- connector registries;
- conformance definitions;
- shared execution contracts.

Core does not automatically own the business relationship or concrete business instance represented using those definitions.

### 4.4 Product Installation

A `Product Installation` is the governed relationship by which a Product is enabled for a Workplace.

It must identify at least:

```text
product_installation_id
workplace_id
product_type
status
edition_or_entitlement
configuration_version
enabled_capabilities
data_access_scope
projection_scope
activated_at
deactivated_at
audit_reference
```

Installation is a logical Product and governance relationship. It does not require separate code, database or deployment for each Workplace.

### 4.5 Projection

A `Projection` is a purpose-limited representation or interaction surface through which a Workplace exposes authorized context to a customer, the public, another Product, MGSN or another Workplace.

Projection:

- does not silently change business ownership;
- does not automatically transfer formal state authority;
- does not create unrestricted recipient access;
- must identify purpose, scope, recipient, duration and revocation where applicable.

### 4.6 Handoff and Return

A `Handoff` is a governed transfer of a bounded responsibility package to another Product, Owning Service, Workplace or managed network participant.

A `Return` is the governed response carrying acceptance, result, evidence, exception, remaining responsibility and source state.

Projection may support discovery or visibility; Handoff and Return govern collaboration continuity.

## 5. Five Separate Authority Dimensions

The word `owner` must not collapse five different dimensions.

| Dimension | Meaning | Typical authority |
| --- | --- | --- |
| Business sovereignty | Who controls and is accountable for the commercial relationship and business context | Workplace / Organization |
| Semantic authority | Who defines the accepted meaning of a record or state | Core / accepted specification |
| Formal state authority | Who may create or mutate formal business facts | Owning Service under Execution governance |
| Physical custody | Where data is hosted or processed | MarkOrbit infrastructure or authorized provider |
| Legal/source authority | Who has statutory, contractual, privacy, evidence or official authority | data subject, Organization, provider, regulator, official office or contract |

Therefore:

```text
Core defines Customer semantics
≠ Core owns every Customer relationship

Workplace controls Matter business context
≠ Workplace may mutate every Matter state outside Owning Service rules

Platform stores data
≠ platform owns the business

Provider produces evidence
≠ provider owns the originating customer relationship
```

## 6. Workplace Sovereignty Principles

### 6.1 Business Sovereignty

Concrete business records and relationships are scoped to the Workplace that creates, receives, manages or is contractually responsible for them, subject to source, legal and official rights.

Candidate record families include:

- Customer and Contact;
- Lead or Opportunity context where Product-owned;
- Applicant and Trademark context;
- Quote and commercial acceptance;
- Order and Matter;
- Documents and Communications;
- Payments, internal cost and margin;
- internal Deadline and reminders;
- Professional Decision and Approval;
- private Knowledge and Memory;
- Product configuration;
- external-route history;
- MGSN request and Return projections.

### 6.2 Storage Is Not Ownership

```text
physical custody
≠ business sovereignty
```

### 6.3 Capability without Appropriation

Core or a Product may calculate, classify, recommend, validate, render, transmit or execute within authority without appropriating the source business relationship or result.

### 6.4 Default Isolation

All access is Workplace-scoped by default.

Cross-Workplace access requires:

- purpose;
- source Workplace;
- recipient;
- record and field scope;
- permission scope;
- effective and expiry time;
- revocation policy;
- audit reference.

### 6.5 Projection by Authorization

Sites, Lite client views, MGSN connections and cross-Workplace interactions expose only authorized projections.

### 6.6 Portable Sovereignty

A Workplace must be able to export the concrete business records, content and configurations it owns or controls, subject to:

- official or legal retention;
- third-party rights;
- privacy restrictions;
- platform-derived confidential data;
- security and anti-abuse controls.

Portable sovereignty does not require export of:

- the full MGSN provider pool;
- confidential platform procurement terms;
- platform routing logic;
- platform-private Trust;
- other Workplaces' private data;
- restricted shared algorithms.

### 6.7 No Hidden Platform Appropriation

The platform must not:

- create an unauthorized global Partner customer pool;
- use Partner customers for MarkReg self-operated marketing without authorization;
- merge Customer records across Workplaces merely by identity similarity;
- treat Product installation as consent to transfer business ownership;
- use one Workplace's private context for another Workplace's recommendation without a governed basis;
- silently widen AI training or network projection rights.

## 7. Product Architecture Decisions

### 7.1 MarkReg

MarkReg is a trademark lifecycle Product installed or enabled in a Workplace.

The Workplace carries the business relationship and accountable operating context. MarkReg and its Owning Services govern formal lifecycle state under accepted specifications.

### 7.2 MarkReg Self-operated Workplace

MarkReg self-operated business is represented as:

```text
MarkReg Self-operated Organization
→ MarkReg Self-operated Workplace
→ MarkReg Product Installation
```

It owns or controls its own customers, Orders, Matters, Communications, Payments, provider procurement and margins.

It has no default access to Partner Workplace data.

### 7.3 Lite

Lite is:

> a lightweight Workplace Product and operating experience for independent professionals and small teams.

Lite may also provide a client-facing projection for:

- guided intake;
- file upload;
- customer confirmation;
- payment initiation;
- status viewing;
- communication and follow-up.

Therefore:

```text
Lite
≠ only a client portal

Lite
≠ an unscoped platform customer-acquisition surface
```

Lite-created business context remains bound to an identified Workplace and Product route.

### 7.4 Sites

Sites is a Workplace public-brand and content projection Product.

Sites content and configuration remain Workplace-scoped. Sites does not become the authoritative Customer, Order, Matter or Payment service.

Dynamic actions must use Workplace-scoped Product or Core interfaces.

### 7.5 MGSN Connection versus MGSN Network

A Workplace may hold:

- MGSN connection configuration;
- authorized demand projections;
- admitted supply projections;
- private route preferences and history;
- Relationship Provenance visible to that Workplace;
- MGSN Return projections.

The platform owns or governs:

- the MGSN network hub;
- participant admission;
- provider supply portfolio;
- Capability Profiles and verification;
- procurement and negotiated terms;
- matching and routing;
- funds and settlement controls;
- fulfillment, exception and replacement;
- platform Trust and network operating evidence;
- controlled network interfaces.

Therefore:

```text
Workplace participates in MGSN
≠ Workplace owns MGSN resources

Workplace has provider history
≠ Workplace owns the platform provider pool

MGSN connection
≠ participant-to-participant network edge
```

## 8. Managed Network and Cross-Workplace Collaboration

### 8.1 Hub-mediated topology

```text
Originating Workplace
→ authorized demand projection
→ MGSN
→ controlled provider instruction
→ Execution Provider Workplace
→ governed Return
→ Originating Workplace
```

### 8.2 Originating Workplace

The Originating Workplace owns or controls the originating Customer relationship, commercial service context and Matter responsibility unless a separate accepted service agreement says otherwise.

### 8.3 Execution Provider Workplace

The Execution Provider Workplace owns or controls its people, methods, professional responsibility, provider-side records and accepted delivery obligations.

It does not automatically obtain the originating end-client relationship.

### 8.4 No undisclosed rebrokering

MGSN-managed work must not use undisclosed or ungoverned rebrokering.

Where legal or operational execution requires additional entities:

- material participants must be disclosed to the platform;
- responsibility must be mapped;
- required user disclosure and approval must occur;
- data scope must remain minimal;
- funds and evidence must remain traceable.

### 8.5 Platform control and Workplace sovereignty are complementary

```text
Workplace sovereignty
protects the participant's business

MGSN governance
protects the managed network and fulfillment
```

Neither one cancels the other.

## 9. AI, Data and Permission Boundaries

AI and algorithms inherit Workplace and purpose boundaries.

An AI runtime must not:

- read another Workplace's private context without authority;
- use MarkReg self-operated access to view Partner customers;
- enlarge a Sites, Lite or MGSN projection automatically;
- convert a Candidate into formal state without Owning Service authority;
- treat model processing as ownership transfer;
- expose platform provider or procurement data beyond policy.

Each material AI call should preserve:

- calling Workplace;
- purpose;
- Product Installation;
- Capability and model version;
- source and rule version;
- input/output summary;
- permission context;
- audit reference.

## 10. Distribution Boundary

Distribution is separate from Workplace sovereignty and MGSN execution routing.

A later Distribution Product or governance record may define:

- Relationship Referral;
- Traffic Affiliate;
- attribution;
- campaign conversion;
- commission rules;
- statements and payouts.

The following must remain distinct:

```text
Distribution attribution
≠ Customer business ownership

Commission
≠ MGSN provider fee

Referral
≠ MGSN execution routing
```

## 11. Conformance Requirements

A conforming architecture or implementation must demonstrate:

### Workplace

1. Concrete private business records carry an explicit Workplace boundary.
2. Access checks use authenticated user, Organization, Workplace, Product role, capability and record scope.
3. MarkReg self-operated and Partner Workplaces are isolated.
4. One Organization may support multiple Workplaces.
5. Workplace-controlled business records and configurations are exportable subject to restrictions.

### Core and Owning Services

6. Core semantic authority is separate from concrete business ownership.
7. Formal state changes occur through accepted Owning Services and Execution rules.
8. Product convenience does not bypass formal authority.

### Products

9. Product Installations are Workplace-scoped and auditable.
10. Sites public outputs remain connected to a Workplace.
11. Lite business context remains connected to an identified Workplace.
12. Lite is not reduced to only a client portal.

### MGSN

13. Workplace-owned connection and projection records are separate from platform-owned network resources.
14. Participants do not receive unrestricted provider-pool export or peer-to-peer graph ownership.
15. MGSN Handoff and Return remain auditable.
16. Managed provider procurement, funds and fulfillment are platform-governed.
17. Material execution participants are disclosed and responsibility-mapped.

### AI and data

18. AI does not leak context across Workplaces.
19. Projection expansion requires authorization.
20. Physical hosting is not represented as business ownership.

## 12. Impact on Existing Authority

### Architecture Canon

If accepted, this ADR requires a controlled Canon amendment to:

- upgrade the Workplace definition;
- add Product Installation and Projection;
- clarify business ownership versus semantic and formal state authority;
- replace peer-network implications in the MGSN statement;
- distinguish MGSN connection from platform MGSN network.

### Book 02

Book 02 remains frozen. Any semantic change requires the existing Change Proposal process.

This ADR should initially clarify instance ownership and Product/Workplace boundaries without silently adding Core types.

### Book 03

Execution must consume Workplace and Product context while preserving Owning Service authority and governed cross-Workplace Handoff.

### Book 04

Book 04 requires a next-version correction because Workplace is currently described too lightly as an operating environment and shell.

### Book 05

Book 05 RC1 remains frozen. A future edition should state that MarkReg operates inside a Workplace and that MarkReg self-operated business is its own Workplace.

### Book 06

Book 06 remains valid where Lite is a lightweight Workplace Product. Client-facing projection language may be added later but must not replace Lite's operating identity.

### Book 07

Book 07 Charter work must pause until this ADR is accepted or revised. The Charter must inherit Originating Workplace, Execution Provider Workplace and MGSN connection/network distinctions.

## 13. Explicit Non-decisions

This ADR does not decide:

- exact database tenancy architecture;
- physical database-per-Workplace deployment;
- final ProductInstallation schema;
- funds custody entity;
- legal title to personal data;
- final Distribution commercial model;
- final MGSN Charter;
- final Sites implementation;
- private deployment obligations;
- public provider discovery;
- automatic provider appointment;
- any external protected action.

## 14. Owner Decision Candidate

Owner acceptance would accept the following architecture direction:

```text
Workplace is the Organization-scoped
business-sovereignty and accountability boundary.

Core owns shared semantics and capabilities,
not every concrete business relationship.

Owning Services retain formal state authority.

Products operate through Workplace-scoped installations.

MarkReg self-operated business is one isolated Workplace.

Lite is a lightweight Workplace Product
with optional client-facing projections.

Sites is a Workplace public projection Product.

Workplaces connect to MGSN through controlled projections.
The platform owns and governs MGSN network resources.

Projection does not silently change ownership.
Handoff and Return govern cross-boundary collaboration.
```

Owner acceptance would authorize preparation of:

- Canon Amendment Candidate;
- Book 04 next-version correction plan;
- Book 07 Charter reconciliation;
- downstream Product specification corrections.

Owner acceptance would not authorize implementation, production deployment, payment custody, provider appointment or external protected action.
