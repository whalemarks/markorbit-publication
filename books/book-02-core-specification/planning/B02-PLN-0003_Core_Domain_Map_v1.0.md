# Book 02

# B02-PLN-0003 — Core Domain Map v1.0

**Document ID:** B02-PLN-0003

**Title:** Core Domain Map v1.0

**Version:** 1.0.0

**Status:** Canonical Draft

**Category:** Planning

**Owner:** MarkOrbit Publications Editorial Board

**Applies To:** Book 02 — *MarkOrbit Core Specification*

**Related Documents:**

- Book 01 — *The Operating System for Global Brand Services*
- Book 02 TOC v1.2 — Frozen
- B02-PLN-0001 — Core Positioning
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- B02-EDT-0001 — Editorial Protocol and Chapter Writing Template
- MAC — MarkOrbit Architecture Canon
- MAG — MarkOrbit Architecture Governance
- MAS — MarkOrbit Architecture Specifications

---

# 1. Purpose

This document defines the Core Domain Map of the MarkOrbit Core.

Its purpose is to identify the stable executable business boundaries that Book 02 shall recognize, specify and later map into `core-specs/`.

This document does not define detailed domain specifications.

It does not define product features.

It does not define database schemas.

It does not define UI modules.

It establishes the domain structure that allows the MarkOrbit Core to become executable without turning Book 02 into a product PRD.

Detailed domain specifications shall be written under:

```text
core-specs/domains/
```

---

# 2. Domain Map Statement

The MarkOrbit Core shall be organized around stable Core Domains.

A Core Domain is an executable business boundary.

A Core Domain is not merely:

- a database table;
- a UI page;
- a product feature;
- an internal module;
- an AI prompt;
- a workflow screen.

A Core Domain owns a stable professional or system responsibility that can be reused by multiple products.

The purpose of this domain map is to prevent MarkReg, MarkOrbit Lite, MGSN and future products from creating isolated definitions for the same business reality.

---

# 3. Relationship to Book 02

Book 02 manuscript defines the architecture of Core Domains.

This planning document identifies the initial Core Domain Map.

`core-specs/domains/` shall contain detailed executable domain specifications.

The relationship is:

```text
Book 02 Manuscript
    defines Domain Architecture

B02-PLN-0003
    defines Core Domain Map

core-specs/domains/
    defines detailed executable domain specifications
```

---

# 4. Relationship to Architecture Blueprint

This document follows the architectural chain defined in B02-PLN-0002.

```text
Canonical Models
        ↓
Core Domains
        ↓
Core Objects
        ↓
Core Services
        ↓
Execution Primitives
        ↓
Core Contracts
        ↓
Core Consumption
```

Core Domains are the bridge between architecture and software implementation.

They translate the Core from conceptual architecture into executable business boundaries.

---

# 5. Domain Design Principles

## Principle 1 — Domain Before Feature

Domains shall be defined before product features.

A product feature may consume a domain.

A product feature shall not define a domain independently.

## Principle 2 — Reality Before Software

A domain shall represent a stable professional, business, system or collaboration reality.

It shall not be introduced merely because a software module needs a name.

## Principle 3 — One Domain, One Primary Responsibility

Each domain shall own one primary responsibility.

A domain may collaborate with other domains.

It shall not absorb unrelated responsibilities.

## Principle 4 — Core Before Product

A domain belongs to Core only if it can be reused across products or is necessary to preserve shared meaning.

Product-specific domains shall not enter the Core Domain Map.

## Principle 5 — Contract Before Integration

Domain interaction shall be governed through explicit objects, services, events and contracts.

Informal data sharing between products shall not define domain boundaries.

## Principle 6 — Governance Before Automation

Domains that involve AI, routing, professional judgment or client communication shall be governed by identity, permission, knowledge, event and human review rules.

---

# 6. Domain Classification

MarkOrbit Core Domains are classified into four categories.

```text
Foundation Domains
        ↓
Professional Domains
        ↓
Business Execution Domains
        ↓
Collaboration Network Domains
```

Each category owns a distinct architectural role.

---

# 7. Foundation Domains

Foundation Domains provide the common structural base of the Core.

They are consumed by most other domains.

They evolve slowly.

| Domain | Primary Responsibility |
|--------|------------------------|
| Identity | Persistent identity across persons, organizations, users, agents, providers and workplaces |
| Organization | Participating organizations and organizational relationships |
| User | Human users, memberships, roles and assignments |
| Permission | Access control, authorization and responsibility boundaries |
| Policy | Formal rules governing business, workflow, routing and governance behavior |
| Knowledge | Professional knowledge assets, sources, links, validation and retrieval |

---

# 8. Professional Domains

Professional Domains represent the subject matter of international trademark and global brand services.

They distinguish MarkOrbit from generic CRM, generic workflow systems and generic AI platforms.

| Domain | Primary Responsibility |
|--------|------------------------|
| Brand | Brand assets, brand ownership context and brand portfolio meaning |
| Trademark | Trademark records, trademark lifecycle and trademark portfolio data |
| Jurisdiction | Countries, regions, offices, local requirements and legal filing environments |
| Classification | Classes, goods/services items, local classification rules and item recommendations |
| Document | Legal, procedural and operational documents |
| Evidence | Use evidence, supporting materials and evidence packages |

---

# 9. Business Execution Domains

Business Execution Domains transform professional knowledge into operational work.

They do not define product UI or Workplace experience.

They define Core-level business execution objects, primitives and contracts.

| Domain | Primary Responsibility |
|--------|------------------------|
| Customer | Customer account, customer relationship and client-side business context |
| Matter | Professional service matters as the central execution unit of work |
| Order | Commercial orders, service items, quotes and order-to-matter conversion |
| Opportunity | Business opportunities generated from data, events and professional context |
| Workflow Contract | Reusable workflow definitions, workflow contracts and workflow interoperability rules |
| Task | Assignable execution units and task responsibility |
| Event | Domain events, lifecycle events and event streams |
| Notification | Core-level reminders, alerts and delivery records |

---

# 10. Collaboration Network Domains

Collaboration Network Domains enable cooperation among internal users, clients, partners, agents and global service providers.

They provide the Core foundation for MGSN, but detailed network architecture belongs to Book 06.

| Domain | Primary Responsibility |
|--------|------------------------|
| Partner | Partner agencies and business collaborators |
| Agent | Professional agents and service representatives |
| Service Provider | External service providers, offerings, coverage and capacity |
| Service Network | Core-level network nodes, membership, trust and capability exchange |
| Routing | Routing decisions for work, opportunities and service requests |
| Communication | Structured communication records, messages, conversations and threads |

---

# 11. Complete Core Domain Map

The canonical Core Domain Map v1.0 contains the following 26 domains.

```text
Foundation Domains
    ├── Identity
    ├── Organization
    ├── User
    ├── Permission
    ├── Policy
    └── Knowledge

Professional Domains
    ├── Brand
    ├── Trademark
    ├── Jurisdiction
    ├── Classification
    ├── Document
    └── Evidence

Business Execution Domains
    ├── Customer
    ├── Matter
    ├── Order
    ├── Opportunity
    ├── Workflow Contract
    ├── Task
    ├── Event
    └── Notification

Collaboration Network Domains
    ├── Partner
    ├── Agent
    ├── Service Provider
    ├── Service Network
    ├── Routing
    └── Communication
```

---

# 12. Domain Boundary Rules

## Rule 1 — Domain Boundaries Are Core Boundaries

A Core Domain defines a shared boundary for all products.

A product shall not create a conflicting domain meaning.

## Rule 2 — Domain Ownership Is Singular

Each Core Domain shall have one primary responsibility.

A domain may collaborate with other domains, but it shall not own their responsibilities.

## Rule 3 — Domain Details Belong in core-specs

The manuscript explains the domain architecture.

Detailed domain specifications belong in:

```text
core-specs/domains/
```

## Rule 4 — Workflow Execution Is Not a Core Domain Responsibility

The Core may define Workflow Contract as a domain.

The Core shall not own product-specific workflow execution.

Workplace owns operational workflow composition.

## Rule 5 — Network Detail Belongs to Book 06

The Core may define Service Network as a domain.

Detailed global collaboration network architecture belongs to Book 06.

## Rule 6 — Product Experience Belongs to Products

A Core Domain may be consumed by multiple products.

Product-specific screens, journeys and experiences shall not define Core Domain boundaries.

---

# 13. Domain Cards

This section defines the initial responsibility cards for each Core Domain.

These cards are planning-level definitions.

They are not replacements for detailed domain specifications.

---

## 13.1 Identity Domain

**Responsibility:** Defines persistent identity across the ecosystem.

**Primary Objects:**

- Identity
- Person
- Organization Identity
- Workplace Identity
- Service Identity

**Core Services:**

- Identity Resolution
- Identity Matching
- Identity Verification
- Identity Relationship Mapping

**Primary Consumers:**

- Organization
- User
- Permission
- Partner
- Agent
- Service Provider
- Service Network

**Detailed Spec Location:**

```text
core-specs/domains/identity.md
```

---

## 13.2 Organization Domain

**Responsibility:** Defines organizations participating in the ecosystem.

**Primary Objects:**

- Organization
- Organization Profile
- Organization Relationship
- Organization Role

**Core Services:**

- Organization Registry
- Organization Classification
- Organization Relationship Management
- Organization Search

**Primary Consumers:**

- Customer
- Partner
- Agent
- Service Provider
- Permission

**Detailed Spec Location:**

```text
core-specs/domains/organization.md
```

---

## 13.3 User Domain

**Responsibility:** Defines human users and their participation in Workplaces and products.

**Primary Objects:**

- User
- User Profile
- Membership
- Assignment
- User Context

**Core Services:**

- User Registration
- User Context Resolution
- User Assignment
- Membership Management

**Primary Consumers:**

- Permission
- Task
- Workflow Contract
- Communication
- Notification

**Detailed Spec Location:**

```text
core-specs/domains/user.md
```

---

## 13.4 Permission Domain

**Responsibility:** Controls access, authorization and responsibility boundaries.

**Primary Objects:**

- Role
- Permission
- Access Policy
- Authorization Context
- Permission Decision

**Core Services:**

- Permission Evaluation
- Role Assignment
- Access Control
- Authorization Audit

**Primary Consumers:**

- All Core Domains

**Detailed Spec Location:**

```text
core-specs/domains/permission.md
```

---

## 13.5 Policy Domain

**Responsibility:** Defines formal rules governing business, workflow, routing and governance behavior.

**Primary Objects:**

- Policy
- Policy Rule
- Policy Scope
- Policy Decision
- Policy Version

**Core Services:**

- Policy Evaluation
- Policy Validation
- Policy Versioning
- Policy Application

**Primary Consumers:**

- Matter
- Order
- Routing
- Workflow Contract
- AI Capability
- Core Consumption

**Detailed Spec Location:**

```text
core-specs/domains/policy.md
```

---

## 13.6 Knowledge Domain

**Responsibility:** Stores and organizes reusable professional knowledge.

**Primary Objects:**

- Knowledge Asset
- Knowledge Source
- Knowledge Node
- Knowledge Relationship
- Knowledge Version

**Core Services:**

- Knowledge Retrieval
- Knowledge Classification
- Knowledge Validation
- Knowledge Linking
- Knowledge Update

**Primary Consumers:**

- Trademark
- Brand
- Jurisdiction
- Classification
- Document
- Evidence
- AI Capability

**Detailed Spec Location:**

```text
core-specs/domains/knowledge.md
```

---

## 13.7 Brand Domain

**Responsibility:** Defines brand assets and brand ownership context.

**Primary Objects:**

- Brand
- Brand Asset
- Logo
- Product Line
- Brand Owner
- Brand Portfolio

**Core Services:**

- Brand Asset Management
- Brand Portfolio Mapping
- Brand Conflict Context
- Brand Opportunity Discovery

**Primary Consumers:**

- Trademark
- Opportunity
- Customer
- Brand Asset Vault
- MarkOrbit Lite

**Detailed Spec Location:**

```text
core-specs/domains/brand.md
```

---

## 13.8 Trademark Domain

**Responsibility:** Defines trademark records and trademark lifecycle.

**Primary Objects:**

- Trademark
- Trademark Application
- Trademark Registration
- Trademark Status
- Trademark Lifecycle Event
- Trademark Portfolio

**Core Services:**

- Trademark Search
- Trademark Lifecycle Tracking
- Trademark Status Normalization
- Trademark Portfolio Management

**Primary Consumers:**

- Brand
- Matter
- Opportunity
- Document
- Evidence
- MarkReg
- MarkOrbit Lite

**Detailed Spec Location:**

```text
core-specs/domains/trademark.md
```

---

## 13.9 Jurisdiction Domain

**Responsibility:** Defines countries, regions, offices, local requirements and filing environments.

**Primary Objects:**

- Jurisdiction
- Trademark Office
- Local Rule
- Filing Requirement
- Deadline Rule

**Core Services:**

- Jurisdiction Lookup
- Filing Requirement Retrieval
- Deadline Calculation
- Local Rule Validation

**Primary Consumers:**

- Trademark
- Classification
- Matter
- Order
- Routing
- AI Capability

**Detailed Spec Location:**

```text
core-specs/domains/jurisdiction.md
```

---

## 13.10 Classification Domain

**Responsibility:** Defines goods, services, classes and classification logic.

**Primary Objects:**

- Class
- Goods Service Item
- Classification Rule
- Similar Group
- Recommended Item

**Core Services:**

- Classification Search
- Goods Recommendation
- Similar Group Analysis
- Classification Validation

**Primary Consumers:**

- Trademark
- Matter
- Order
- AI Capability
- MarkOrbit Lite

**Detailed Spec Location:**

```text
core-specs/domains/classification.md
```

---

## 13.11 Document Domain

**Responsibility:** Manages legal, procedural and operational documents.

**Primary Objects:**

- Document
- Document Template
- Document Version
- Document Attachment
- Document Package

**Core Services:**

- Document Generation
- Document Parsing
- Document Storage
- Document Review
- Document Packaging

**Primary Consumers:**

- Matter
- Order
- Evidence
- Communication
- MarkReg
- MGSN

**Detailed Spec Location:**

```text
core-specs/domains/document.md
```

---

## 13.12 Evidence Domain

**Responsibility:** Manages use evidence and supporting materials.

**Primary Objects:**

- Evidence
- Evidence Source
- Evidence Package
- Evidence Review
- Evidence Metadata

**Core Services:**

- Evidence Intake
- Evidence Classification
- Evidence Packaging
- Evidence Review

**Primary Consumers:**

- Trademark
- Matter
- Document
- AI Capability
- Brand Asset Vault

**Detailed Spec Location:**

```text
core-specs/domains/evidence.md
```

---

## 13.13 Customer Domain

**Responsibility:** Defines customer accounts, customer relationships and client-side business context.

**Primary Objects:**

- Customer
- Customer Account
- Customer Contact
- Customer Relationship
- Customer Context

**Core Services:**

- Customer Registry
- Customer Context Resolution
- Customer Relationship Management
- Customer Opportunity Context

**Primary Consumers:**

- Brand
- Trademark
- Order
- Opportunity
- Communication
- MarkReg
- MarkOrbit Lite

**Detailed Spec Location:**

```text
core-specs/domains/customer.md
```

---

## 13.14 Matter Domain

**Responsibility:** Defines professional service matters as the central execution unit of work.

**Primary Objects:**

- Matter
- Matter Type
- Matter Status
- Matter Timeline
- Matter Assignment

**Core Services:**

- Matter Creation
- Matter Tracking
- Matter Assignment
- Matter Status Management
- Matter Closure

**Primary Consumers:**

- Workflow Contract
- Task
- Event
- Document
- Agent
- MarkReg

**Detailed Spec Location:**

```text
core-specs/domains/matter.md
```

---

## 13.15 Order Domain

**Responsibility:** Defines commercial orders and service purchases.

**Primary Objects:**

- Order
- Order Item
- Service Product
- Price Quote
- Payment Record

**Core Services:**

- Order Creation
- Quote Generation
- Order Tracking
- Payment Linking
- Order-to-Matter Conversion

**Primary Consumers:**

- Customer
- Matter
- Opportunity
- MarkReg
- MarkOrbit Lite

**Detailed Spec Location:**

```text
core-specs/domains/order.md
```

---

## 13.16 Opportunity Domain

**Responsibility:** Defines business opportunities generated from data, events and professional context.

**Primary Objects:**

- Opportunity
- Opportunity Source
- Opportunity Score
- Opportunity Recommendation
- Opportunity Assignment

**Core Services:**

- Opportunity Discovery
- Opportunity Scoring
- Opportunity Routing
- Opportunity Conversion
- Opportunity Follow-up

**Primary Consumers:**

- Customer
- Brand
- Trademark
- Order
- Routing
- Notification
- Opportunity Engine

**Detailed Spec Location:**

```text
core-specs/domains/opportunity.md
```

---

## 13.17 Workflow Contract Domain

**Responsibility:** Defines reusable workflow contracts and workflow interoperability rules.

**Primary Objects:**

- Workflow Contract
- Workflow Definition
- Workflow Step
- Workflow State
- Workflow Transition

**Core Services:**

- Workflow Contract Definition
- Workflow Validation
- Workflow State Rule Management
- Workflow Interoperability Support

**Primary Consumers:**

- Matter
- Task
- Event
- Book 03 Workplace
- MarkReg
- MarkOrbit Lite

**Boundary Note:**

Core defines workflow contracts.

Workplace operates workflows.

Products deliver workflow experience.

**Detailed Spec Location:**

```text
core-specs/domains/workflow-contract.md
```

---

## 13.18 Task Domain

**Responsibility:** Defines assignable execution units.

**Primary Objects:**

- Task
- Assignment
- Task Status
- Task Dependency
- Task Result

**Core Services:**

- Task Creation
- Task Assignment
- Task Tracking
- Task Completion
- Task Escalation

**Primary Consumers:**

- Workflow Contract
- Matter
- Event
- Notification
- Workplace
- Products

**Detailed Spec Location:**

```text
core-specs/domains/task.md
```

---

## 13.19 Event Domain

**Responsibility:** Defines system and business events.

**Primary Objects:**

- Event
- Event Type
- Event Source
- Event Payload
- Event Stream

**Core Services:**

- Event Publishing
- Event Subscription
- Event Routing
- Event Logging
- Event Replay

**Primary Consumers:**

- All execution domains
- Notification
- Opportunity
- AI Capability
- Products

**Detailed Spec Location:**

```text
core-specs/domains/event.md
```

---

## 13.20 Notification Domain

**Responsibility:** Defines Core-level reminders, alerts and delivery records.

**Primary Objects:**

- Notification
- Reminder
- Alert
- Channel
- Delivery Log

**Core Services:**

- Notification Dispatch
- Reminder Scheduling
- Alert Generation
- Delivery Tracking

**Primary Consumers:**

- Event
- Task
- Opportunity
- Communication
- Products

**Detailed Spec Location:**

```text
core-specs/domains/notification.md
```

---

## 13.21 Partner Domain

**Responsibility:** Defines partner agencies and business collaborators.

**Primary Objects:**

- Partner
- Partner Contact
- Partner Account
- Partner Relationship
- Partner Tier

**Core Services:**

- Partner Registry
- Partner Matching
- Partner Performance Tracking
- Partner Communication Support

**Primary Consumers:**

- Customer
- Order
- Opportunity
- MGSN
- MarkReg

**Detailed Spec Location:**

```text
core-specs/domains/partner.md
```

---

## 13.22 Agent Domain

**Responsibility:** Defines professional agents and service representatives.

**Primary Objects:**

- Agent
- Agent Contact
- Agent Capability
- Agent Jurisdiction
- Agent Rating

**Core Services:**

- Agent Registry
- Agent Search
- Agent Capability Matching
- Agent Reliability Scoring

**Primary Consumers:**

- Matter
- Routing
- Service Provider
- MGSN
- MarkReg

**Detailed Spec Location:**

```text
core-specs/domains/agent.md
```

---

## 13.23 Service Provider Domain

**Responsibility:** Defines external service providers participating in the ecosystem.

**Primary Objects:**

- Service Provider
- Service Offering
- Provider Price
- Provider Coverage
- Provider Capacity

**Core Services:**

- Provider Registry
- Provider Matching
- Provider Quote Retrieval
- Provider Evaluation

**Primary Consumers:**

- Service Network
- Routing
- Agent
- MGSN

**Detailed Spec Location:**

```text
core-specs/domains/service-provider.md
```

---

## 13.24 Service Network Domain

**Responsibility:** Defines the Core-level global collaboration network foundation.

**Primary Objects:**

- Service Network
- Network Node
- Membership
- Trust Record
- Capability Exchange

**Core Services:**

- Network Discovery
- Membership Management
- Trust Evaluation
- Capability Exchange

**Primary Consumers:**

- Book 06 MGSN
- Routing
- Partner
- Agent
- Service Provider

**Boundary Note:**

Core defines the network foundation.

Book 06 defines detailed network architecture.

**Detailed Spec Location:**

```text
core-specs/domains/service-network.md
```

---

## 13.25 Routing Domain

**Responsibility:** Routes work, opportunities and service requests to appropriate participants.

**Primary Objects:**

- Route
- Routing Rule
- Routing Decision
- Routing Candidate
- Routing History

**Core Services:**

- Work Routing
- Opportunity Routing
- Service Provider Routing
- Routing Explanation
- Routing Optimization

**Primary Consumers:**

- Matter
- Opportunity
- Agent
- Service Provider
- Service Network
- MGSN

**Detailed Spec Location:**

```text
core-specs/domains/routing.md
```

---

## 13.26 Communication Domain

**Responsibility:** Manages structured communication records between participants.

**Primary Objects:**

- Conversation
- Message
- Thread
- Communication Participant
- Communication Log

**Core Services:**

- Message Capture
- Email Drafting Support
- Conversation Linking
- Communication Search
- Communication Summarization

**Primary Consumers:**

- Customer
- Partner
- Agent
- Service Provider
- Matter
- MGSN
- MarkReg

**Detailed Spec Location:**

```text
core-specs/domains/communication.md
```

---

# 14. Domain Dependency Map

The initial domain dependency map is directional.

```text
Identity
    ↓
Organization
    ↓
User / Customer / Partner / Agent / Service Provider
    ↓
Permission / Policy

Knowledge
    ↓
Brand / Trademark / Jurisdiction / Classification
    ↓
Document / Evidence
    ↓
Matter / Order / Opportunity

Matter
    ↓
Workflow Contract
    ↓
Task
    ↓
Event
    ↓
Notification

Partner / Agent / Service Provider
    ↓
Service Network
    ↓
Routing
    ↓
Communication
```

Dependencies shall not create circular ownership.

A domain may consume another domain.

A domain shall not redefine another domain.

---

# 15. Product Consumption Map

| Product / Publication | Primary Consumed Domains |
|-----------------------|--------------------------|
| Book 03 — Workplace Framework | Workflow Contract, Task, Event, Notification, Context, Core Services |
| Book 04 — MarkReg | Trademark, Matter, Order, Document, Evidence, Agent, Task, Event |
| Book 05 — MarkOrbit Lite | Brand, Trademark, Customer, Opportunity, Classification, Knowledge, Order |
| Book 06 — MGSN | Partner, Agent, Service Provider, Service Network, Routing, Communication |
| Brand Asset Vault | Brand, Trademark, Document, Evidence, Knowledge |
| Opportunity Engine | Opportunity, Customer, Trademark, Brand, Knowledge, Routing, Notification |

This map defines consumption, not ownership.

Products consume domains.

Products shall not redefine domains.

---

# 16. MVP Domain Priority

The MVP shall implement domains in phases.

The purpose is to establish an executable Core skeleton before expanding into full ecosystem capability.

## Phase 1 — Foundation Core

- Identity
- Organization
- User
- Permission
- Knowledge

## Phase 2 — Professional Core

- Brand
- Trademark
- Jurisdiction
- Classification
- Document

## Phase 3 — Business Execution Core

- Customer
- Matter
- Order
- Workflow Contract
- Task
- Event

## Phase 4 — Growth Core

- Opportunity
- Notification
- Policy
- Evidence
- Agent
- Routing

## Phase 5 — Network Core

- Partner
- Service Provider
- Service Network
- Communication

This priority may evolve through governance.

It shall not be changed ad hoc by product-specific pressure.

---

# 17. Domain Acceptance Criteria

A domain is accepted into the Core only if it satisfies all required criteria.

- It has one primary responsibility.
- It represents a stable professional, business, system or collaboration reality.
- It is reusable by more than one product or necessary for shared Core meaning.
- It has identifiable primary objects.
- It exposes or consumes Core Services.
- It can generate, consume or respond to Events where applicable.
- It has clear product consumers.
- It can be mapped to `core-specs/domains/`.
- It does not duplicate another domain.
- It does not belong exclusively to a single product UI.
- It does not redefine a later publication's responsibility.

---

# 18. Domain Exclusion Criteria

A proposed domain shall be rejected if it is:

- only a UI page;
- only a product feature;
- only a temporary workflow step;
- only a report;
- only a prompt;
- only a database table;
- only a third-party integration;
- only a product package;
- only an operational SOP;
- owned exclusively by one product and not reusable.

Rejected domain candidates may still belong to product specifications, implementation documents or operational documentation.

They shall not enter the Core Domain Map.

---

# 19. Domain Specification Template

Detailed domain specifications shall follow the structure below.

```markdown
# [Domain Name] Domain Specification

**Domain ID:** CORE-DOM-[ID]

**Status:** Draft

**Category:** Foundation / Professional / Business Execution / Collaboration Network

---

# 1. Responsibility

# 2. Scope

## In Scope

## Out of Scope

# 3. Primary Objects

# 4. Core Services

# 5. Events

# 6. Permissions

# 7. Policy Dependencies

# 8. Knowledge Dependencies

# 9. AI Capability Usage

# 10. Product Consumers

# 11. API Surface

# 12. Database Mapping

# 13. Workflow / Execution Usage

# 14. Acceptance Criteria

# 15. Exclusions

# 16. Revision History
```

---

# 20. Repository Mapping

Detailed domain specifications shall be stored as follows.

```text
core-specs/domains/

├── identity.md
├── organization.md
├── user.md
├── permission.md
├── policy.md
├── knowledge.md
├── brand.md
├── trademark.md
├── jurisdiction.md
├── classification.md
├── document.md
├── evidence.md
├── customer.md
├── matter.md
├── order.md
├── opportunity.md
├── workflow-contract.md
├── task.md
├── event.md
├── notification.md
├── partner.md
├── agent.md
├── service-provider.md
├── service-network.md
├── routing.md
└── communication.md
```

---

# 21. Governance Rules

## Rule 1

New Core Domains shall be introduced only through architecture review.

## Rule 2

A new domain shall include a responsibility statement, boundary definition and acceptance criteria.

## Rule 3

A domain shall not be added because a product needs a page or feature.

## Rule 4

Domain removal or consolidation requires review of downstream objects, services, events, APIs, agents and products.

## Rule 5

Domain ownership shall remain stable across products.

---

# 22. Revision Policy

Changes to the Core Domain Map shall be reviewed before they affect Book 02 manuscript or `core-specs/`.

A change is considered material if it:

- adds a Core Domain;
- removes a Core Domain;
- renames a Core Domain;
- changes a domain category;
- changes domain responsibility;
- changes product consumption mapping;
- changes MVP priority.

Material changes require editorial and architecture review.

---

# Revision History

| Version | Status | Description |
|---------|--------|-------------|
| 1.0.0 | Canonical Draft | Rewritten Core Domain Map aligned with Book 02 TOC v1.2, Core Positioning, Architecture Blueprint v2.0 and manuscript/core-specs boundary. |

---

**End of Document**
