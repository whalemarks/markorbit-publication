# Book 02

# 12 — Canonical Models

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-12

**Chapter Title:** Canonical Models

**Part:** Part II — Core Kernel Architecture

**Chapter Type:** Architecture

**Status:** Draft

**Version:** 0.1.0

**Owner:** MarkOrbit Publications Editorial Board

**Related Planning Documents:**

- B02-PLN-0001 — Core Positioning
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- B02-EDT-0001 — Editorial Protocol and Chapter Writing Template

---

# 1. Chapter Purpose

This chapter defines the Canonical Models of the MarkOrbit Core.

Chapter 09 introduced Canonical Models as the first component of the Core Kernel.

Chapter 10 defined the architecture layers.

Chapter 11 defined the responsibility flow.

This chapter now defines the foundational models that give Core Domains their conceptual structure.

Canonical Models are not product models.

They are not database models.

They are not UI models.

They are not implementation frameworks.

Canonical Models define the stable conceptual patterns that appear across multiple Core Domains.

They prevent domains from being designed as isolated objects.

For example:

- Identity appears in User, Organization, Customer, Partner, Agent and Service Provider.
- Capability appears in Core Services, AI Capability, Agent Capability and Service Provider capability.
- Knowledge appears in jurisdiction rules, classification rules, evidence rules, document templates and AI reasoning.
- Business Responsibility appears in customer ownership, matter responsibility, order conversion, opportunity ownership and human review.
- Workplace appears in tasks, context, workflow contracts and professional work operation.
- Network appears in partner, agent, service provider, routing and communication.

The purpose of this chapter is to define these models before detailed domain architecture begins.

---

# 2. Core Question

This chapter answers one question:

> What canonical models must the MarkOrbit Core define before domains, objects, services and contracts can be specified consistently?

The answer is:

> The MarkOrbit Core requires six Canonical Models: Identity, Capability, Knowledge, Business Responsibility, Workplace and Network.

These models provide the conceptual structure for Core Domains, Core Objects, Core Services, Execution Primitives, Core Contracts and Core Consumption.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- what a Canonical Model is;
- why Canonical Models are necessary;
- the six official Canonical Models;
- the responsibility of each model;
- the relationship between Canonical Models and Core Domains;
- the relationship between Canonical Models and Core Objects;
- the relationship between Canonical Models and Core Services;
- the relationship between Canonical Models and AI governance;
- how Canonical Models guide `core-specs/` and Codex implementation.

## 3.2 Out of Scope

This chapter does not define:

- full domain specifications;
- complete object field definitions;
- database schemas;
- API endpoint details;
- UI models;
- product navigation models;
- product-specific workflow models;
- production AI prompts;
- implementation code.

Those belong to later chapters, `core-specs/`, product publications or implementation documents.

---

# 4. Canonical Model Definition

A Canonical Model is:

> a stable conceptual model that defines a recurring Core pattern shared across multiple domains, objects, services, contracts and products.

A Canonical Model answers:

- What is the general pattern?
- Which domains use it?
- Which objects express it?
- Which services depend on it?
- Which events may involve it?
- Which contracts expose it?
- Which products consume it?
- Which governance rules protect it?

A Canonical Model is more abstract than a Core Domain.

A Core Domain owns a specific responsibility.

A Canonical Model defines a recurring structure across domains.

---

# 5. Why Canonical Models Matter

Without Canonical Models, domains may be internally clear but externally inconsistent.

For example:

- User may define identity one way.
- Customer may define identity another way.
- Agent may define identity as contact information.
- Service Provider may define identity as marketplace account.
- Partner may define identity as business relationship.

This creates fragmented identity.

The same problem can happen with capability, knowledge, responsibility, workplace context and network participation.

Canonical Models prevent this by providing shared conceptual patterns before domain-level design.

They allow domains to specialize while preserving structural consistency.

---

# 6. Official Canonical Models

Book 02 defines six Canonical Models.

```text
Canonical Models
    ├── Identity Model
    ├── Capability Model
    ├── Knowledge Model
    ├── Business Responsibility Model
    ├── Workplace Model
    └── Network Model
```

These six models are sufficient for the initial Core architecture.

Future models may be added only through architectural review.

---

# 7. Model 1 — Identity Model

## 7.1 Definition

The Identity Model defines how the Core represents actors, organizations, roles, accounts and identity-linked entities.

It answers:

> Who or what is represented, recognized, authorized or related in the system?

Identity is not only login.

Identity is the foundation for responsibility, permission, relationship, audit, communication and network collaboration.

## 7.2 Primary Concepts

The Identity Model includes:

- Person;
- Organization;
- User;
- Customer;
- Partner;
- Agent;
- Service Provider;
- Role;
- Account;
- Contact Point;
- Identity Link;
- Identity Verification;
- Identity Relationship.

## 7.3 Related Core Domains

The Identity Model informs:

- Identity;
- Organization;
- User;
- Permission;
- Customer;
- Partner;
- Agent;
- Service Provider;
- Communication.

## 7.4 Core Responsibility

The Core shall provide a shared identity structure so that all products can recognize and relate actors consistently.

For example:

- a foreign associate may be an Agent;
- the same legal entity may also be a Service Provider;
- a Chinese agency may be a Partner;
- a company may be a Customer;
- a person may be a User and also a contact person for a Customer.

Without a shared Identity Model, these entities may be duplicated or misunderstood.

## 7.5 Exclusions

The Identity Model does not define:

- product login UI;
- onboarding screens;
- commercial membership plans;
- contact management page design;
- external KYC vendor implementation;
- authentication infrastructure details.

Those belong to product or implementation documents.

## 7.6 Example

A person named “Anthony” may appear as:

- email sender;
- attorney contact;
- agent representative;
- matter participant;
- service provider staff.

The Identity Model determines whether these appearances should be linked to one identity or treated separately.

---

# 8. Model 2 — Capability Model

## 8.1 Definition

The Capability Model defines how the Core represents what the system, a service, an AI agent, a person, an agent or a service provider can do.

It answers:

> What capability exists, who or what provides it, under what conditions, and how may it be consumed?

Capability is broader than function.

A function may be product-specific.

A capability is reusable and governable.

## 8.2 Primary Concepts

The Capability Model includes:

- Core Capability;
- Core Service;
- AI Capability;
- Agent Capability;
- Service Provider Capability;
- Human Capability;
- Capability Scope;
- Capability Condition;
- Capability Permission;
- Capability Risk Level;
- Capability Output;
- Capability Consumer.

## 8.3 Related Core Domains

The Capability Model informs:

- Knowledge;
- Permission;
- Policy;
- Classification;
- Document;
- Evidence;
- Matter;
- Opportunity;
- Agent;
- Service Provider;
- Routing;
- AI Capability and Agent Governance Specification.

## 8.4 Core Responsibility

The Core shall define reusable capabilities and the conditions under which they may be used.

Examples include:

- filing requirement retrieval;
- goods and services recommendation;
- trademark search;
- document generation;
- evidence packaging;
- agent matching;
- routing decision;
- opportunity discovery;
- AI-assisted drafting.

A capability may be executed by:

- a Core Service;
- an AI agent;
- a human professional;
- a workflow step;
- a service provider;
- a product feature.

The capability itself must remain governed by the Core if it is reusable and shared.

## 8.5 Exclusions

The Capability Model does not define:

- product buttons;
- UI actions;
- production prompts;
- vendor-specific LLM calls;
- internal implementation functions that have no shared meaning;
- product-only feature behavior.

## 8.6 Example

“Classification Recommendation” is a capability.

It may be consumed by:

- MarkReg filing workflow;
- Lite guided consultation;
- AI classification assistant;
- opportunity analysis;
- client intake tool.

The product interface may vary.

The capability definition should remain shared.

---

# 9. Model 3 — Knowledge Model

## 9.1 Definition

The Knowledge Model defines how professional knowledge is represented, governed, validated, retrieved and applied by the Core.

It answers:

> What knowledge does the Core trust, how is it structured, and how is it used by services, humans and AI?

Knowledge is not only text.

It includes rules, sources, relationships, templates, jurisdiction requirements, classification logic, evidence standards, procedural experience and validated practice.

## 9.2 Primary Concepts

The Knowledge Model includes:

- Knowledge Source;
- Knowledge Asset;
- Knowledge Node;
- Knowledge Relationship;
- Knowledge Rule;
- Knowledge Version;
- Knowledge Authority;
- Knowledge Validation;
- Knowledge Retrieval;
- Knowledge Application;
- Knowledge Gap;
- Knowledge Risk.

## 9.3 Related Core Domains

The Knowledge Model informs:

- Knowledge;
- Jurisdiction;
- Classification;
- Document;
- Evidence;
- Trademark;
- Policy;
- AI Capability and Agent Governance;
- Opportunity;
- Routing.

## 9.4 Core Responsibility

The Core shall make professional knowledge executable.

This means knowledge should be connected to:

- domains;
- objects;
- services;
- events;
- AI capabilities;
- workflow contracts;
- product consumption.

For example:

- jurisdiction knowledge supports filing requirement retrieval;
- classification knowledge supports goods recommendation;
- evidence knowledge supports use review;
- document knowledge supports document generation;
- agent knowledge supports routing;
- policy knowledge supports permission and review.

## 9.5 Exclusions

The Knowledge Model does not define:

- a generic article library only;
- unvalidated internal notes as authoritative rules;
- AI hallucinated knowledge;
- product help pages;
- marketing copy;
- unofficial prompts as knowledge sources.

## 9.6 Example

A country rule about power of attorney requirements should not exist only as a static article.

It should be usable by:

- filing requirement service;
- document checklist;
- AI consultation;
- matter setup;
- client guidance;
- Codex tests where relevant.

---

# 10. Model 4 — Business Responsibility Model

## 10.1 Definition

The Business Responsibility Model defines ownership, accountability, authorization, delegation and value responsibility in professional service execution.

It answers:

> Who is responsible for what, who may act, who must review, who owns value, and who bears risk?

This model is necessary because professional work is not only data processing.

It involves responsibility.

## 10.2 Primary Concepts

The Business Responsibility Model includes:

- Responsibility Owner;
- Customer Owner;
- Matter Owner;
- Order Owner;
- Opportunity Owner;
- Review Authority;
- Executor;
- Delegation;
- Authorization;
- Approval;
- Escalation;
- Responsibility Transfer;
- Value Relationship;
- Risk Responsibility;
- Audit Responsibility.

## 10.3 Related Core Domains

The Business Responsibility Model informs:

- Customer;
- Matter;
- Order;
- Opportunity;
- Permission;
- Policy;
- Task;
- Event;
- Routing;
- Communication;
- AI Capability and Agent Governance.

## 10.4 Core Responsibility

The Core shall make business and professional responsibility explicit where it affects execution, permission, review, audit or value creation.

Examples include:

- who owns a customer relationship;
- who may approve a quote;
- who is responsible for a matter;
- who must review AI output;
- who is authorized to assign an agent;
- who receives opportunity follow-up;
- who is accountable for deadline-sensitive work.

## 10.5 Exclusions

The Business Responsibility Model does not define:

- product pricing packages;
- sales scripts;
- commission schedules;
- promotional policies;
- membership tiers;
- marketing campaigns;
- revenue targets.

Those belong to product business documents or operating documents.

## 10.6 Example

When an AI agent drafts a response to an office action, the Business Responsibility Model determines:

- who requested the draft;
- who is responsible for review;
- who may approve final advice;
- whether the output may be sent to a client;
- what audit record is required.

---

# 11. Model 5 — Workplace Model

## 11.1 Definition

The Workplace Model defines how Core work context is represented for operation by Workplace and products.

It answers:

> What work context must the Core provide so that Workplace can operate professional work?

Workplace Model is included as a Canonical Model because the Core must provide objects, tasks, events, context and contracts that Workplace consumes.

However, Workplace operation itself belongs to Book 03.

## 11.2 Primary Concepts

The Workplace Model includes:

- Workspace Context;
- Work Item;
- Task;
- Event;
- State;
- Context;
- Assignment;
- Notification;
- Workflow Contract;
- Work View;
- Work Relationship;
- Human-AI Collaboration Context;
- Work History.

## 11.3 Related Core Domains

The Workplace Model informs:

- Matter;
- Workflow Contract;
- Task;
- Event;
- Notification;
- Communication;
- Permission;
- Policy;
- AI Capability and Agent Governance.

## 11.4 Core Responsibility

The Core shall provide the primitives and contracts that allow Workplace to operate work.

Core provides:

- task structure;
- event structure;
- state structure;
- context structure;
- workflow contracts;
- notification contracts;
- responsibility links;
- consumption rules.

Workplace operates:

- work composition;
- workflow surfaces;
- task boards;
- collaboration experience;
- human-AI co-working experience;
- operational views.

## 11.5 Exclusions

The Workplace Model does not define:

- Workplace UI;
- task board layout;
- product-specific work views;
- daily operating SOPs;
- team management process;
- full workflow execution experience.

Those belong to Book 03 or product documents.

## 11.6 Example

The Core may define a Task as a Core execution primitive.

Book 03 may define how tasks are displayed and operated in Workplace.

MarkReg may show filing-related tasks.

Lite may show simplified client-facing next steps.

The Task meaning remains Core.

---

# 12. Model 6 — Network Model

## 12.1 Definition

The Network Model defines how the Core represents professional collaboration among partners, agents, service providers and service networks.

It answers:

> How does MarkOrbit represent and govern multi-party professional collaboration?

The Network Model is necessary because MarkOrbit is not only an internal operating system.

It also connects global trademark service participants.

## 12.2 Primary Concepts

The Network Model includes:

- Partner;
- Agent;
- Service Provider;
- Service Network;
- Network Node;
- Jurisdiction Coverage;
- Service Coverage;
- Capability Coverage;
- Trust Record;
- Reliability Record;
- Routing Rule;
- Routing Decision;
- Communication Channel;
- Collaboration Context;
- Network Participation.

## 12.3 Related Core Domains

The Network Model informs:

- Partner;
- Agent;
- Service Provider;
- Service Network;
- Routing;
- Communication;
- Jurisdiction;
- Matter;
- Task;
- Event;
- Policy;
- Permission.

## 12.4 Core Responsibility

The Core shall define shared network concepts and collaboration foundations.

It may define:

- who an Agent is;
- what a Service Provider is;
- what capability coverage means;
- what routing decision means;
- how communication is linked to matters;
- how service network participation is represented;
- how trust or reliability records may be structured.

Book 06 defines the detailed Mark Global Service Network product and business model.

## 12.5 Exclusions

The Network Model does not define:

- MGSN product UI;
- network marketplace pages;
- provider subscription plans;
- commercial membership packages;
- network sales policy;
- detailed marketplace operation.

Those belong to Book 06 or product business documents.

## 12.6 Example

A foreign law firm may appear as:

- Agent;
- Service Provider;
- network participant;
- matter assignee;
- communication participant;
- jurisdiction capability provider.

The Network Model allows those roles to be connected without reducing the firm to a simple contact record.

---

# 13. Canonical Model Relationship Map

The six Canonical Models are related.

```text
Identity Model
    supports
Business Responsibility Model
    supports
Workplace Model

Knowledge Model
    supports
Capability Model
    supports
AI Capability and Core Services

Network Model
    uses
Identity Model + Capability Model + Business Responsibility Model
```

A more detailed view:

```text
Identity
    answers who exists

Capability
    answers what can be done

Knowledge
    answers what is known and trusted

Business Responsibility
    answers who owns and approves

Workplace
    answers what work context is required

Network
    answers how external collaboration is structured
```

These models should not be designed independently.

They form the conceptual foundation of the Core Kernel.

---

# 14. Canonical Models and Core Domains

Canonical Models inform Core Domains.

They are not identical to domains.

For example:

| Canonical Model | Related Domains |
|-----------------|----------------|
| Identity Model | Identity, Organization, User, Customer, Partner, Agent, Service Provider |
| Capability Model | Knowledge, Classification, Document, Evidence, Agent, Service Provider, Routing |
| Knowledge Model | Knowledge, Jurisdiction, Classification, Document, Evidence, Policy |
| Business Responsibility Model | Customer, Matter, Order, Opportunity, Permission, Policy, Task |
| Workplace Model | Matter, Workflow Contract, Task, Event, Notification, Communication |
| Network Model | Partner, Agent, Service Provider, Service Network, Routing, Communication |

A domain specification should identify which Canonical Models it depends on.

---

# 15. Canonical Models and Core Objects

Canonical Models inform Core Object design.

Examples:

- Identity Model informs User, Organization, Customer, Partner, Agent and Service Provider objects.
- Capability Model informs Capability, Service, Agent Capability and Service Provider Capability objects.
- Knowledge Model informs Knowledge Asset, Knowledge Source, Knowledge Rule and Knowledge Relationship objects.
- Business Responsibility Model informs Matter Owner, Review Authority and Responsibility Assignment objects.
- Workplace Model informs Task, Event, State, Context and Workflow Contract objects.
- Network Model informs Agent, Service Provider, Route, Communication and Service Network objects.

A Core Object should not be designed only from product needs.

It should be checked against the relevant Canonical Model.

---

# 16. Canonical Models and Core Services

Canonical Models also inform Core Service design.

Examples:

- Identity Model supports Identity Resolution Service.
- Capability Model supports Capability Matching Service.
- Knowledge Model supports Knowledge Retrieval Service.
- Business Responsibility Model supports Permission Evaluation and Review Assignment Services.
- Workplace Model supports Task Creation, Event Publishing and Notification Services.
- Network Model supports Agent Matching, Routing Decision and Communication Services.

A Core Service should declare which Canonical Model or models it relies on.

---

# 17. Canonical Models and Events

Events should preserve Canonical Model meaning.

Examples:

- `IdentityLinked` belongs to Identity logic.
- `CapabilityUpdated` belongs to Capability logic.
- `KnowledgeSourceValidated` belongs to Knowledge logic.
- `MatterOwnerAssigned` belongs to Business Responsibility logic.
- `TaskAssigned` belongs to Workplace / Execution logic.
- `RoutingDecisionMade` belongs to Network logic.

Event naming and payload should not be product-specific.

Events should reflect stable meaning from Canonical Models and Core Domains.

---

# 18. Canonical Models and AI Governance

AI Capability must be governed by Canonical Models.

AI needs:

- Identity Model to know who is acting and who is affected;
- Permission and Business Responsibility to know what is allowed;
- Knowledge Model to know what sources may be used;
- Capability Model to know what the AI may perform;
- Workplace Model to know the task and context;
- Network Model to know collaboration boundaries where external parties are involved.

Without Canonical Models, AI governance becomes prompt-level control only.

That is not sufficient.

AI governance must be architectural.

---

# 19. Canonical Models and Product Consumption

Products consume Canonical Models indirectly through Core Domains, Objects, Services, Events and Contracts.

For example:

- MarkReg consumes Identity through users, agents and matter responsibility.
- Lite consumes Knowledge and Capability through AI-assisted guidance.
- MGSN consumes Network through service provider, routing and communication.
- Brand Asset Vault consumes Identity, Knowledge and Professional Domains through brand and trademark continuity.
- Opportunity Engine consumes Business Responsibility and Knowledge through opportunity detection and follow-up.

Products should not create their own competing canonical models.

They may create product-specific views.

The underlying models remain Core.

---

# 20. Canonical Models and `core-specs/`

Every `core-specs/` file should identify relevant Canonical Models.

Examples:

```text
core-specs/domains/agent.md
    Canonical Models:
        - Identity Model
        - Capability Model
        - Network Model
        - Business Responsibility Model

core-specs/objects/matter.md
    Canonical Models:
        - Business Responsibility Model
        - Workplace Model
        - Knowledge Model

core-specs/services/classification-recommendation.md
    Canonical Models:
        - Knowledge Model
        - Capability Model
        - Business Responsibility Model

core-specs/events/task-assigned.md
    Canonical Models:
        - Workplace Model
        - Business Responsibility Model
```

This keeps specifications connected to the Core Kernel.

---

# 21. Canonical Models and Codex

Codex tasks shall reference Canonical Models where relevant.

A Codex task should not only say:

> Create a table for agents.

It should say:

> Implement Agent according to the Identity Model, Capability Model and Network Model, using the Agent Domain specification, related object specification and acceptance criteria.

This prevents Codex from creating shallow implementation artifacts.

Canonical Models help Codex understand why a concept exists and how it relates to the rest of the Core.

---

# 22. Canonical Model Extension Rule

New Canonical Models may be proposed only when existing models cannot explain a recurring Core pattern.

A proposal for a new Canonical Model must include:

- model name;
- recurring pattern it explains;
- why existing models are insufficient;
- affected Core Domains;
- affected Core Objects;
- affected Core Services;
- affected Events;
- affected Contracts;
- affected AI Capabilities;
- affected products;
- boundary rules;
- acceptance criteria.

New Canonical Models shall not be added merely to satisfy a product feature.

---

# 23. Canonical Model Anti-Patterns

## 23.1 Product Model Becomes Canonical Model

A product-specific model is promoted to Core without review.

Result:

- product experience defines architecture;
- future products inherit unsuitable assumptions.

## 23.2 Database Model Becomes Canonical Model

Tables are treated as conceptual models.

Result:

- implementation defines Core meaning;
- semantic consistency is weak.

## 23.3 AI Prompt Model Becomes Canonical Model

Prompt structures define Core concepts.

Result:

- AI becomes an uncontrolled source of ontology;
- governance weakens.

## 23.4 Isolated Domain Model

Each domain defines identity, capability, knowledge or responsibility independently.

Result:

- cross-domain fragmentation;
- inconsistent product consumption.

## 23.5 Over-Abstract Model

A model is so abstract that it cannot guide domains, objects, services or implementation.

Result:

- architecture becomes decorative;
- Codex and developers cannot use it.

Canonical Models must be abstract enough to guide multiple domains and concrete enough to support execution.

---

# 24. Canonical Model Review Questions

When reviewing a Canonical Model or model usage, reviewers shall ask:

1. What recurring Core pattern does this model explain?
2. Which domains depend on it?
3. Which objects express it?
4. Which services use it?
5. Which events should preserve it?
6. Which contracts expose it?
7. Which AI capabilities require it?
8. Which products consume it?
9. Does it overlap with an existing Canonical Model?
10. Is it too product-specific?
11. Is it too implementation-specific?
12. Can Codex use it to generate more consistent implementation?

---

# 25. Canonical Model Decision Matrix

| Proposed Concept | Canonical Model? | Reason |
|------------------|------------------|--------|
| Identity | Yes | Recurs across users, customers, partners, agents and providers |
| Capability | Yes | Recurs across services, AI, agents and providers |
| Knowledge | Yes | Recurs across rules, documents, classification, jurisdiction and AI |
| Business Responsibility | Yes | Recurs across orders, matters, opportunities, review and authorization |
| Workplace | Yes | Recurs across tasks, events, states, context and work operation |
| Network | Yes | Recurs across partners, agents, providers, routing and communication |
| Trademark | No | Core Domain / Core Object, not a cross-domain model |
| Filing Wizard | No | Product feature |
| Dashboard | No | Product view |
| Database Schema | No | Implementation artifact |
| Prompt Template | No | Agent implementation artifact |
| Pricing Plan | No | Product business document |

---

# 26. Canonical Model Rules

The following rules are established by this chapter.

## Rule 1 — Canonical Models SHALL define recurring Core patterns

A Canonical Model must explain a pattern used across multiple domains.

## Rule 2 — Canonical Models SHALL precede detailed domain design

Domains should identify their relevant Canonical Models before detailed specification.

## Rule 3 — Products SHALL NOT create competing Canonical Models

Products may create views, but not competing Core models.

## Rule 4 — Canonical Models SHALL guide Core Objects and Services

Objects and services should preserve model meaning.

## Rule 5 — AI SHALL follow Canonical Models

AI capabilities must use Identity, Knowledge, Capability, Responsibility, Workplace and Network rules where relevant.

## Rule 6 — Canonical Models SHALL be implementation-independent

They shall not depend on a specific database, framework, vendor or LLM.

## Rule 7 — Canonical Models SHALL be executable

They must guide domains, objects, services, events, contracts and Codex tasks.

---

# 27. Specification Output

This chapter produces the following specification output:

- Canonical Model definition;
- six official Canonical Models;
- Identity Model;
- Capability Model;
- Knowledge Model;
- Business Responsibility Model;
- Workplace Model;
- Network Model;
- model relationship map;
- model-to-domain mapping;
- model-to-object mapping;
- model-to-service mapping;
- model-to-event mapping;
- AI governance implications;
- product consumption implications;
- `core-specs/` usage rules;
- Codex usage rules;
- extension rule;
- anti-patterns;
- review questions;
- decision matrix;
- Canonical Model rules.

These outputs shall guide Chapters 13 through 17 and Part III.

---

# 28. Execution Mapping

This chapter does not directly define database tables or API endpoints.

It controls how execution assets preserve conceptual consistency.

| Canonical Model | Execution Mapping |
|-----------------|------------------|
| Identity Model | identity tables, organization links, user/customer/agent/provider models |
| Capability Model | service definitions, AI capabilities, agent/provider capability records |
| Knowledge Model | knowledge sources, rules, retrieval services, validation records |
| Business Responsibility Model | owner fields, review authority, delegation, permission and policy rules |
| Workplace Model | task, event, state, context and workflow contract specs |
| Network Model | partner, agent, provider, routing and communication specs |

Implementation shall not create execution assets that conflict with these models.

---

# 29. Relationship to core-specs/

This chapter governs how Canonical Models should appear in `core-specs/`.

Every major domain, object, service, event, agent and workflow specification should include a section titled:

```text
Canonical Model Dependencies
```

That section should list:

- primary Canonical Model;
- secondary Canonical Models;
- model-specific rules;
- model-specific exclusions;
- related consumers.

No detailed specification should define identity, capability, knowledge, responsibility, workplace context or network meaning independently from the Canonical Models.

---

# 30. Exclusions

This chapter shall not include:

- complete domain specs;
- object field schemas;
- database design;
- API endpoint design;
- product UI models;
- product navigation maps;
- product workflows;
- AI prompt templates;
- vendor implementation details;
- deployment architecture.

These belong elsewhere.

---

# 31. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines Canonical Models clearly.
- It identifies the six official Canonical Models.
- It explains why Canonical Models are necessary.
- It distinguishes Canonical Models from domains, objects, tables and product models.
- It defines each model’s responsibility and exclusions.
- It maps Canonical Models to domains, objects, services, events, AI and product consumption.
- It provides rules for `core-specs/` and Codex.
- It prevents product-specific or implementation-specific models from becoming canonical.
- It supports Chapters 13 through 17.
- It supports Book 02 TOC v1.2.

---

# 32. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 12, defining the six Canonical Models of the MarkOrbit Core. |

---

**End of Chapter**
