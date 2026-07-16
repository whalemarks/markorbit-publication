# MarkOrbit Orbital Professional Operating Architecture vNext.1

## Status

- **Version:** vNext.1
- **Status:** Active Canon — ready for Owner activation on merge
- **Effective authority:** Repository-level MarkOrbit architecture governance
- **Supersedes:** `MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.md` as the active working Canon
- **Accepted amendment basis:** `MO-ADR-WSP-001` and `MO-ARCH-AMEND-001`

This Canon is not a final public edition, a Book 02 semantic amendment, an implementation authorization, a production deployment approval or an External Protected Action authorization.

Book 02 remains the Frozen Core Specification Baseline v0.1. Semantic changes to that baseline continue to require the established Change Proposal process.

## 1. Canonical Meaning of MarkOrbit

MarkOrbit is the operating system for global brand professional services.

```text
Each in its own orbit.
Connected by capability.
Evolving together.
```

```text
各行其道
→ each Organization operates through its own accountable Workplace

彼此牵引
→ Workplaces consume shared capability and connect through governed interfaces

共同演进
→ evidence and outcomes improve Products, networks and shared capabilities
```

`Orbital` remains the primary architecture metaphor. `Federated`, `networked` and `platform-managed` may describe particular governance characteristics but do not replace Orbital as the total architecture language.

## 2. Constitutional Spine

```text
Industry and Professional Philosophy
                ↓
MarkOrbit Operating System
                ↓
MarkOrbit Core
                ↓
MarkOrbit Execution System
                ↓
Organization Workplace / Independent Orbit
                ↓
Product Installations and Operating Models
                ↓
Managed Networks and External Projections
                ↓
Ecosystem Learning and Evolution
```

The spine expresses authority and responsibility, not one physical deployment stack.

- Core defines shared semantic authority, controlled contracts and reusable capabilities.
- Execution governs coordinated work, review, failure, audit and formal mutation paths.
- Workplace is the Organization-scoped business-sovereignty and accountability boundary.
- Products operate through Workplace-scoped Product Installations.
- Managed networks, including MGSN, remain distinct from the Workplace connections that access them.
- Ecosystem learning must preserve source, permission, rights, candidate status and professional responsibility.

## 3. Five Authority Dimensions

The word `owner` must not collapse different forms of authority.

### 3.1 Business sovereignty

Who controls the customer relationship, internal business context, private pricing, internal knowledge, operating preferences and accountable commercial responsibility.

Default authority: the relevant Organization through its Workplace.

### 3.2 Semantic authority

Who defines the controlled meaning of objects, fields, states, terms and contracts.

Default authority: Core, accepted Specifications and the architecture authority chain.

### 3.3 Formal-state authority

Who may create or mutate formal business facts.

Default authority: the applicable Owning Service operating through governed Execution.

### 3.4 Physical custody

Who stores, transmits, processes, backs up or technically administers data.

Physical custody may belong to the platform or an authorized infrastructure provider without transferring business sovereignty.

### 3.5 Legal and source authority

Who holds legal rights, privacy authority, evidentiary authority, official-source authority or professional responsibility.

This may belong to a customer, Organization, provider, professional, government office or other source authority depending on the record.

```text
Physical custody
≠ business sovereignty

Semantic authority
≠ concrete-record commercial ownership

Formal-state authority
≠ customer-relationship ownership

Workplace sovereignty
≠ unrestricted mutation authority
```

## 4. Organization and Workplace

### 4.1 Organization

An Organization is the accountable legal, commercial, professional or administrative participant.

Examples include:

- trademark agencies;
- law firms;
- independent professional practices;
- enterprise brand or legal departments;
- MarkReg self-operated entities;
- provider Organizations;
- platform operating entities.

An Organization may operate one or more Workplaces where legitimate separation is required.

### 4.2 Workplace

> **Workplace is the Organization-scoped business-sovereignty, accountability, permission, Product-operation and projection boundary.**

A Workplace may contain or govern access to:

- Organization identity and membership;
- users, roles and permissions;
- Customer and Contact context;
- private relationships;
- internal service catalog and customer-facing pricing;
- internal cost, margin and commercial policy;
- private Documents, Evidence and Knowledge;
- professional decisions, approvals and reviews;
- business history and organizational memory;
- Product Installations and entitlements;
- authorized external projections;
- audit and accountability context.

Workplace is not merely:

- a navigation shell;
- a generic employee dashboard;
- a theme around platform-owned business records;
- a separately deployed codebase by default;
- authority to bypass Core or Owning Services.

### 4.3 Concrete business records

Concrete Customer, Order, Matter, Payment, Communication and related records operate in an explicit Workplace business context.

The relevant Workplace normally holds business sovereignty and commercial accountability for the records it originates or manages. The applicable Core semantics and Owning Services still govern their formal meaning and mutation.

## 5. Product Installation

A Product participates in an Organization through a Workplace-scoped Product Installation.

```text
Organization
→ Workplace
→ Product Installation
→ enabled capabilities, configuration,
  entitlement, permissions and projection scope
```

A Product Installation may define:

- Product identity and edition;
- lifecycle status;
- enabled capabilities;
- data-access scope;
- role and permission mappings;
- configuration version;
- projection scope;
- integration and connector policy;
- audit reference;
- activation and retirement context.

```text
Product Installation
≠ separate source-code deployment
≠ separate database by necessity
≠ ownership of every record the Product displays
```

A shared multi-tenant implementation may support many Product Installations while preserving Workplace isolation and authority.

## 6. Product Projection, Handoff and Return

### 6.1 Product Projection

A Product Projection exposes a purpose-limited view or interaction surface derived from an authorized Workplace or Product context.

Examples include:

- a client-facing Lite experience;
- a Sites public page;
- an MGSN Capability Need projection;
- a provider-facing instruction view.

A Projection does not automatically transfer business sovereignty or formal-state authority.

### 6.2 Handoff

A Handoff transfers typed context from one Product, service or Workplace boundary toward another authorized destination.

A Handoff must preserve:

- source authority;
- destination authority;
- purpose;
- permission;
- minimum required context;
- version and provenance;
- pending, accepted, rejected and unknown states.

### 6.3 Return

A Return brings typed outcome, Evidence or status projection back to the originating context.

```text
Return received
≠ Return accepted as formal truth

Delivered data
≠ destination ownership transfer
```

The destination must validate the Return under its own authority and Owning Service rules.

## 7. Core and Execution Boundaries

### 7.1 Core

Core provides shared:

- controlled semantics;
- identifiers and contracts;
- Jurisdiction Packs, Rules and Sources;
- Capability definitions;
- validation and fixture expectations;
- security and identity primitives;
- audit and Event contracts;
- Handoff and Return contracts;
- approved shared infrastructure boundaries.

Core may define the meaning of Customer, Order, Matter, Task, Opportunity, Document, Evidence and related concepts without becoming the commercial owner of every concrete record.

### 7.2 Execution

Execution governs:

- Workflow coordination;
- Task and step state;
- review and approval;
- protected-action boundaries;
- retry and duplicate safety;
- failure and unknown outcome handling;
- audit and Event evidence;
- invocation of Owning Services.

AI Agents, Assistants, Products and Workplaces do not silently replace Owning Service authority.

## 8. Product Locks

### 8.1 MarkReg

MarkReg is the flagship international trademark lifecycle Product.

```text
Organization
→ Workplace
→ MarkReg Installation
→ trademark lifecycle capabilities
```

MarkReg self-operated business must operate through an isolated self-operated Organization and Workplace. Platform operation does not grant default access to Partner Workplace business records.

MarkReg may operate as a full Product experience and may be launched or embedded from Lite or another Workplace surface, but its formal lifecycle states remain governed by the relevant Owning Services.

### 8.2 MarkOrbit Lite

Lite is a lightweight Workplace Product for independent trademark professionals and small teams.

```text
Lite Workplace experience
├── professional operating experience
└── optional client-facing projection
```

Lite may support Today, growth, Customer context, Opportunities, professional work products, Cases, Memory, Assets and cross-Product handoffs.

It may also provide Intake, upload, decision confirmation, status viewing and other client-facing interactions. These projections do not reduce Lite to a client portal.

```text
Lite
≠ smaller MarkReg
≠ content-only tool
≠ client portal only
```

### 8.3 Sites

Sites is a Workplace public-brand and content projection Product.

It may govern domain, brand, design system, pages, content, cases, FAQs, service pages, widgets and publication versions.

Sites is not the Owning Service for Customer, Order, Matter, Payment or professional decisions. Dynamic Intake and Lead flows must enter an explicit Workplace and Product route.

### 8.4 MGSN Connection / Gateway

An MGSN Connection or Gateway is the Workplace-scoped interface through which authorized demand, supply, instruction and Return projections enter or leave MGSN.

The Connection may hold:

- participation configuration;
- permission and disclosure policy;
- private preferences;
- external-route declarations;
- relationship provenance view;
- demand and supply projections;
- returned results and Evidence.

It does not own the MGSN provider pool, procurement terms, routing logic, platform Trust or funds system.

### 8.5 MGSN Network

> **MGSN is the platform-owned and platform-governed managed global professional service network.**

MGSN governs:

- provider recruitment and admission;
- provider supply portfolios;
- Capability and qualification projections;
- procurement and package terms;
- matching and routing;
- platform Trust and performance evidence;
- controlled funds and settlement processes;
- fulfillment monitoring;
- correction, replacement, suspension and retirement;
- network interfaces and operating data.

The canonical topology is:

```text
Originating Workplace
→ authorized demand projection
→ MGSN Connection / Gateway
→ platform-owned MGSN Network
→ controlled allocation / instruction
→ Execution Provider Workplace
→ governed Return
→ Originating Workplace
```

Participants may communicate where professional execution requires it, but MGSN-managed work does not create an unrestricted participant-to-participant network graph.

```text
Workplace relationship history
≠ ownership of MGSN supply

MGSN Connection
≠ MGSN Network

User confirmation
≠ automatic provider appointment

Provider access
≠ customer-relationship ownership
```

MGSN is not an open bidding marketplace, free provider directory or lowest-price-only allocation engine.

## 9. External Self-Managed Routes

A Workplace may retain a genuine external self-managed provider route outside MGSN.

The originating Organization remains responsible for negotiation, instruction, payment, follow-up and non-performance. Platform continuity resumes through manually supplied, source-qualified Evidence and status.

External routes do not receive implied MGSN procurement, funds, replacement, fulfillment or provider-verification guarantees.

## 10. Cross-Workplace Collaboration

Cross-Workplace collaboration must preserve distinct authority on both sides.

```text
Originating Workplace permission
≠ Execution Provider Workplace permission

Source approval
≠ destination approval

Technical delivery
≠ unrestricted reuse

AI access in one Workplace
≠ AI access in another Workplace
```

No undisclosed or ungoverned rebrokering is permitted. Where additional local professionals or legal representatives are required, their identity, role, authority, funds and Evidence path must be governed and disclosed to the extent required.

## 11. Portability and Exit

Workplace sovereignty requires governed portability, not unrestricted extraction of platform-owned assets.

A Workplace should be able to export or transfer, subject to rights and policy:

- its concrete business records;
- its Documents and Evidence;
- its private Knowledge and configuration;
- its own relationship history;
- its Product Installation configuration where portable.

Portability does not imply export of:

- the MGSN provider pool;
- confidential procurement terms;
- platform routing models;
- platform Trust records beyond authorized views;
- other participants' private data;
- platform-owned shared capabilities or source code.

## 12. Candidate-before-Canonical Lock

```text
Observation
≠ formal fact

Candidate
≠ approved record

Recommendation
≠ Decision

User confirmation
≠ Human Review where governed review is required

Prepared Action
≠ execution

Handoff sent
≠ destination acceptance

Return received
≠ formal-state mutation

Unknown external outcome
≠ completed, failed or safe to retry
```

Candidates require the applicable validation, governance, professional and Owning Service gates before becoming authoritative.

## 13. Product Loop and Platform Extraction

Product Loop First, Shared Platform Extraction Second remains the governing development principle.

Shared capabilities should be extracted when repeated Product needs demonstrate a stable cross-Product boundary. Architecture convenience alone does not justify a separate service, repository, database or network.

## 14. Publication and Change Governance

Authority hierarchy:

```text
Level 1 — Active Canon and accepted canonical publications
Level 2 — Architecture Specifications and accepted amendments
Level 3 — Product Charters and controlled Product Specifications
Level 4 — Implementation ADRs, contracts and repository decisions
Level 5 — Research, technical radar and POCs
```

Lower levels may not silently redefine higher-level semantics or authority.

Book 02 remains frozen. The Workplace sovereignty amendment is an architecture clarification unless future work changes frozen Core object identity, cardinality, fields, states, transitions, Owning Services or Event/Handoff contracts.

## 15. Current Publication Direction

- Book 04 requires a controlled next-version Workplace sovereignty correction; RC1 remains historical and unchanged.
- Book 05 remains the frozen MarkReg RC1, with future Workplace-installation clarification.
- Book 06 remains the accepted Lite RC1; Lite's client projection is additive and does not replace its operating identity.
- Book 07 defines MGSN and must use the Originating Workplace → MGSN → Execution Provider Workplace model.

## 16. Authority Boundary

This Canon does not authorize:

- unrestricted implementation;
- production deployment;
- payment custody without an approved legal and operational model;
- autonomous provider appointment;
- autonomous professional judgment;
- filing or official submission;
- External Protected Action.

Those actions remain subject to Product, Execution, legal, financial and governance gates.
