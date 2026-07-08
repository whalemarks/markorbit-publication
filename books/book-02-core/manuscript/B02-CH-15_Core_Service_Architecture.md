# Book 02

# 15 — Core Service Architecture

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-15

**Chapter Title:** Core Service Architecture

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

This chapter defines the Core Service Architecture of MarkOrbit.

Chapter 13 defined Core Domains.

Chapter 14 defined Core Objects.

This chapter defines Core Services.

Domains own responsibility.

Objects represent stable things.

Services expose reusable capabilities.

A professional operating system cannot be built only from objects.

Objects must be acted on.

Knowledge must be retrieved.

Documents must be generated.

Classification must be recommended.

Matters must be created.

Orders must be converted.

Agents must be matched.

Opportunities must be discovered.

Events must be published.

Permissions must be evaluated.

AI capabilities must operate under governance.

Core Services are the reusable capabilities that make the Core executable.

This chapter defines how Core Services are identified, owned, structured, governed, contracted and consumed.

---

# 2. Core Question

This chapter answers one question:

> How shall MarkOrbit define and govern Core Services?

The answer is:

> A Core Service is a reusable, governed capability owned by a Core Domain that acts on Core Objects, applies knowledge or policy, produces traceable results, and is consumed through explicit contracts by products, Workplaces, AI agents or other services.

A Core Service is not a product button.

A Core Service is not a UI action.

A Core Service is not an isolated function.

A Core Service is a governed capability of the Core.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- Core Service definition;
- service responsibility;
- service ownership;
- service categories;
- service inputs and outputs;
- service context;
- service permissions;
- service side effects;
- service events;
- service contracts;
- service AI usage;
- service composition;
- service quality;
- service failure handling;
- service specification structure;
- service inclusion and exclusion rules;
- service review questions;
- service anti-patterns;
- service mapping to `core-specs/services/`;
- service mapping to Codex implementation tasks.

## 3.2 Out of Scope

This chapter does not define:

- complete service contracts for every Core Service;
- API endpoint details;
- runtime microservice topology;
- programming language functions;
- product UI actions;
- product-specific workflows;
- production AI prompts;
- vendor-specific implementation;
- deployment architecture.

Detailed Core Service specifications belong in:

```text
core-specs/services/
```

---

# 4. Core Service Definition

A Core Service is:

> a reusable, governed capability owned by a Core Domain that acts on Core Objects, applies knowledge or policy, produces traceable results, and is consumed through explicit contracts by products, Workplaces, AI agents or other services.

This definition contains seven parts.

## 4.1 Reusable

A Core Service should be useful beyond one isolated product screen.

## 4.2 Governed

A Core Service must respect permission, policy, context, audit and risk rules.

## 4.3 Capability

A Core Service represents what the Core can do.

It is more than a technical function.

## 4.4 Domain-Owned

A Core Service must have a primary owning Core Domain.

## 4.5 Object-Aware

A Core Service acts on, creates, updates, reads or relates Core Objects.

## 4.6 Traceable

A Core Service should produce events, logs, records or audit traces where meaningful.

## 4.7 Contract-Consumable

A Core Service should be consumed through explicit contracts.

---

# 5. What a Core Service Is Not

A Core Service is not:

- a product button;
- a UI action;
- a screen behavior;
- a product-specific workflow step;
- an isolated helper function;
- a vendor API wrapper without Core meaning;
- a prompt template;
- a background script with no domain responsibility;
- a database query alone;
- a report export function;
- a one-product-only feature.

For example:

- `Trademark Search Service` may be a Core Service.
- `MarkReg Search Button` is product UI.
- `Classification Recommendation Service` may be a Core Service.
- `Lite Class Selection Step` is a product feature.
- `Agent Matching Service` may be a Core Service.
- `MGSN Agent Card Recommendation` is product experience.
- `Document Generation Service` may be a Core Service.
- `Generate POA Button` is product UI.

---

# 6. Service Architecture Position

Core Services sit inside the Core Kernel.

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

Domains own services.

Objects are acted on by services.

Services may emit events.

Contracts expose services.

Products, Workplaces and AI agents consume services.

This position makes Core Services the primary executable capabilities of the MarkOrbit Core.

---

# 7. Service Responsibility

Every Core Service must answer:

> What reusable capability does this service provide?

A service responsibility statement should be short and stable.

Examples:

- Identity Resolution Service resolves and links identities.
- Permission Evaluation Service determines whether an action is allowed.
- Knowledge Retrieval Service retrieves authorized knowledge.
- Trademark Search Service searches normalized trademark records.
- Jurisdiction Requirement Service retrieves filing requirements.
- Classification Recommendation Service recommends goods and services.
- Document Generation Service generates professional documents from governed templates and context.
- Evidence Packaging Service organizes evidence into a reviewable package.
- Matter Creation Service creates professional matters.
- Order-to-Matter Conversion Service converts paid or confirmed orders into matters.
- Opportunity Discovery Service identifies potential business opportunities.
- Agent Matching Service matches agents to jurisdiction, service and matter context.
- Routing Decision Service recommends or records routing decisions.
- Event Publishing Service publishes meaningful events.

A service without stable reusable responsibility should not become a Core Service.

---

# 8. Service Ownership

Every Core Service shall have one primary owning Core Domain.

Ownership means responsibility for service meaning and rules.

A service may use multiple domains, but primary ownership must be clear.

Examples:

```text
Trademark Search Service
    Primary owner: Trademark Domain
    Uses: Jurisdiction, Classification, Knowledge

Order-to-Matter Conversion Service
    Primary owner: Order Domain
    Uses: Customer, Matter, Task, Event

Agent Matching Service
    Primary owner: Agent Domain or Routing Domain
    Uses: Jurisdiction, Service Provider, Service Network, Matter

Classification Recommendation Service
    Primary owner: Classification Domain
    Uses: Knowledge, Jurisdiction, Trademark, Brand
```

A consuming product does not own the service.

A product may call, display or compose the service.

---

# 9. Service Categories

Book 02 recognizes eight practical Core Service categories.

```text
1. Identity and Permission Services
2. Knowledge Services
3. Professional Services
4. Business Execution Services
5. Execution and Event Services
6. Collaboration Network Services
7. AI-Assisted Services
8. Contract and Consumption Services
```

These categories help organize service architecture.

They do not replace domain ownership.

---

# 10. Identity and Permission Services

Identity and Permission Services provide access, identity and authorization foundations.

Examples include:

- Identity Resolution Service;
- Organization Lookup Service;
- User Context Service;
- Role Assignment Service;
- Permission Evaluation Service;
- Policy Evaluation Service;
- Access Audit Service.

These services support:

- login context;
- object access;
- action authorization;
- business responsibility;
- AI governance;
- product consumption.

They are usually foundational and must be implemented early.

---

# 11. Knowledge Services

Knowledge Services make professional knowledge executable.

Examples include:

- Knowledge Retrieval Service;
- Knowledge Validation Service;
- Jurisdiction Rule Lookup Service;
- Filing Requirement Retrieval Service;
- Classification Rule Retrieval Service;
- Evidence Standard Retrieval Service;
- Document Template Retrieval Service;
- Knowledge Gap Detection Service.

These services support:

- professional understanding;
- AI grounding;
- classification recommendation;
- filing guidance;
- document generation;
- evidence review;
- opportunity discovery.

Knowledge Services must distinguish authorized, validated, stale, inferred and unverified knowledge.

---

# 12. Professional Services

Professional Services act on professional domains.

Examples include:

- Brand Portfolio Mapping Service;
- Trademark Search Service;
- Trademark Status Normalization Service;
- Trademark Lifecycle Tracking Service;
- Jurisdiction Lookup Service;
- Classification Recommendation Service;
- Goods/Services Validation Service;
- Document Generation Service;
- Document Parsing Service;
- Evidence Packaging Service;
- Evidence Review Assistance Service.

These services distinguish MarkOrbit from generic SaaS tools.

They must preserve professional meaning and knowledge dependency.

---

# 13. Business Execution Services

Business Execution Services transform professional value into executable business work.

Examples include:

- Customer Context Service;
- Matter Creation Service;
- Matter Status Update Service;
- Matter Responsibility Assignment Service;
- Order Creation Service;
- Quote Generation Support Service;
- Order-to-Matter Conversion Service;
- Opportunity Discovery Service;
- Opportunity Scoring Service;
- Opportunity Assignment Service;
- Review Assignment Service.

These services must preserve business responsibility.

They should not become sales package logic unless a product document owns that commercialization.

---

# 14. Execution and Event Services

Execution and Event Services make work traceable and coordinated.

Examples include:

- Task Creation Service;
- Task Assignment Service;
- Task Completion Service;
- Event Publishing Service;
- Event Subscription Service;
- Notification Dispatch Service;
- Workflow Contract Activation Service;
- State Transition Service;
- Timeline Recording Service.

These services support coordination.

They do not own workflow execution experience.

Workplace operates workflows.

Products display workflows.

Core Services provide primitives and contracts.

---

# 15. Collaboration Network Services

Collaboration Network Services support multi-party professional collaboration.

Examples include:

- Partner Lookup Service;
- Agent Search Service;
- Agent Capability Matching Service;
- Service Provider Search Service;
- Service Network Coverage Service;
- Routing Decision Service;
- Communication Linking Service;
- Conversation Threading Service;
- Reliability Scoring Support Service;
- Trust Record Update Service.

These services provide the Core foundation for MGSN.

Book 06 may define product-level network operation and commercialization.

Book 02 defines the shared service capabilities.

---

# 16. AI-Assisted Services

AI-Assisted Services are Core Services that use AI under governance.

Examples include:

- AI Classification Recommendation;
- AI Document Draft Assistance;
- AI Evidence Review Assistance;
- AI Trademark Status Summary;
- AI Office Action Summary;
- AI Opportunity Discovery;
- AI Agent Matching Assistance;
- AI Communication Summary;
- AI Client Explanation Drafting.

AI-Assisted Services must declare:

- Core Capability;
- owning domain;
- knowledge sources;
- input objects;
- output type;
- permission boundary;
- risk level;
- human review requirement;
- audit requirement;
- related events.

AI-Assisted Services are not free-form chat.

They are governed Core capabilities.

---

# 17. Contract and Consumption Services

Contract and Consumption Services support safe consumption of Core capabilities.

Examples include:

- API Contract Validation Service;
- Event Contract Validation Service;
- Agent Contract Enforcement Service;
- Consumption Permission Service;
- Data Export Service;
- Product View Composition Service;
- Contract Version Compatibility Service.

These services help ensure products, Workplaces, agents and integrations consume Core consistently.

They belong close to the Integration Contracts Layer.

---

# 18. Service Input

Every Core Service shall define input.

Input may include:

- Core Objects;
- object IDs;
- user identity;
- organization context;
- permission context;
- knowledge context;
- jurisdiction;
- service type;
- product context;
- workflow context;
- AI context;
- external reference;
- uploaded document;
- communication record.

Input must not be ambiguous.

A service should not rely on hidden product state.

Input should be explicit enough to support audit, testing and Codex implementation.

---

# 19. Service Output

Every Core Service shall define output.

Output may include:

- Core Object;
- updated object state;
- recommendation result;
- generated document;
- validation result;
- routing decision;
- task;
- event;
- notification;
- audit record;
- AI-assisted draft;
- error result;
- review requirement.

Output should distinguish:

- final result;
- draft result;
- recommendation;
- warning;
- failure;
- partial result;
- human-review-required result.

This distinction is especially important for AI-assisted services.

---

# 20. Service Context

Every meaningful Core Service should define context.

Context may include:

- acting user;
- organization;
- customer;
- matter;
- jurisdiction;
- trademark;
- document;
- knowledge source;
- workflow state;
- product consumer;
- risk level;
- time;
- source system;
- AI model or agent;
- human review requirement.

Context prevents services from acting blindly.

A service without context may produce technically correct but professionally unsafe results.

---

# 21. Service Permission

Core Services shall respect permission and policy.

Permission questions include:

- who may invoke the service;
- which object may be accessed;
- which action may be performed;
- whether AI may be used;
- whether external sharing is allowed;
- whether review is required;
- whether output may update Core Objects;
- whether event publication is allowed.

Permission should not be enforced only in product UI.

Permission belongs to the Core and Integration Contracts.

---

# 22. Service Side Effects

Some Core Services are read-only.

Some create or modify state.

Some publish events.

Some trigger tasks.

Some create AI output.

Some create review requirements.

Each service must declare side effects.

Examples:

```text
Knowledge Retrieval Service
    Side effect: usually none or access log

Matter Creation Service
    Side effect: creates Matter, emits MatterCreated, may create initial Tasks

Order-to-Matter Conversion Service
    Side effect: updates Order, creates Matter, emits OrderConvertedToMatter and MatterCreated

AI Document Draft Assistance
    Side effect: creates Draft Output, may create Review Task, emits AIDraftGenerated

Routing Decision Service
    Side effect: creates Routing Decision, may assign Agent, emits RoutingDecisionMade
```

Side effects must be explicit for audit and testing.

---

# 23. Service Events

Core Services may publish events.

Events make service outcomes visible.

A service should publish an event when:

- a Core Object is created;
- object state changes meaningfully;
- responsibility changes;
- AI output is generated for professional use;
- routing decision is made;
- document is generated or verified;
- evidence package is created;
- task is assigned or completed;
- opportunity is created;
- notification is dispatched.

Events should not be treated as optional logs.

They are part of coordination and audit.

---

# 24. Service Contracts

Core Services must be consumed through contracts.

A Service Contract may define:

- service name;
- owning domain;
- capability description;
- input;
- output;
- permission;
- policy;
- context;
- side effects;
- events;
- error behavior;
- version;
- AI usage;
- review requirement;
- consumer limitations.

Service Contracts may be represented through:

- API Contracts;
- Agent Contracts;
- Workflow Contracts;
- Event Contracts;
- Consumption Contracts.

Products should not call services informally.

AI agents should not use services outside Agent Contracts.

---

# 25. Service Composition

Core Services may compose other services.

Example:

```text
Guided Filing Preparation
    uses:
        Identity Resolution
        Customer Context
        Brand Portfolio Mapping
        Jurisdiction Lookup
        Classification Recommendation
        Filing Requirement Retrieval
        Document Checklist Generation
        Quote Support
        Order Creation
```

Composition must preserve service ownership.

A composed service should not absorb the responsibilities of all services it calls.

If a composition becomes product-specific, it may belong to Workplace or Product rather than Core.

The Core may define reusable service orchestration only when it represents shared capability.

---

# 26. Service Quality

Service quality should be defined where relevant.

Quality dimensions may include:

- accuracy;
- completeness;
- source authority;
- freshness;
- consistency;
- latency;
- explainability;
- auditability;
- permission correctness;
- review compliance;
- AI confidence;
- fallback behavior.

Quality is especially important for:

- knowledge retrieval;
- classification recommendation;
- evidence review assistance;
- opportunity scoring;
- routing decision;
- deadline calculation;
- AI-assisted drafting.

A service that produces professional output should define quality expectations.

---

# 27. Service Failure Handling

Every Core Service should define failure behavior.

Failure types may include:

- missing input;
- invalid permission;
- stale knowledge;
- incomplete object context;
- external source unavailable;
- AI confidence too low;
- conflicting records;
- duplicate object detected;
- contract violation;
- human review required;
- downstream service failure.

Failure output should be explicit.

A service should not silently return misleading results.

For professional services, failure may be safer than uncertain success.

---

# 28. Service Idempotency and Safety

Some Core Services should be idempotent or safety-controlled.

Examples:

- identity linking should avoid duplicate links;
- order-to-matter conversion should not create duplicate matters;
- event publishing should avoid duplicate events;
- notification dispatch should prevent duplicate alerts where necessary;
- document generation may allow multiple versions but should track them;
- AI draft generation may create versions but should not overwrite approved content.

Service safety should be specified when repeated calls may cause risk.

---

# 29. Service and Core Objects

Core Services act on Core Objects.

A service should declare:

- objects read;
- objects created;
- objects updated;
- objects linked;
- objects archived;
- objects versioned;
- object quality requirements;
- object permission requirements.

Examples:

```text
Matter Creation Service
    Reads: Customer, Trademark, Order
    Creates: Matter
    Links: Document, Task
    Emits: MatterCreated

Evidence Packaging Service
    Reads: Evidence, Document, Trademark, Goods/Services Item
    Creates: Evidence Package
    Emits: EvidencePackageCreated
```

A service that acts on objects must preserve object ownership.

---

# 30. Service and Knowledge

Many Core Services depend on Knowledge.

Examples:

- filing requirement retrieval depends on jurisdiction knowledge;
- classification recommendation depends on classification rules and goods/services knowledge;
- document generation depends on document templates and jurisdiction requirements;
- evidence review assistance depends on evidence standards;
- opportunity discovery depends on business rules and trademark lifecycle knowledge;
- routing depends on agent capability knowledge and policy.

Services should declare knowledge dependencies.

A knowledge-dependent service should respond differently when knowledge is missing, stale or unverified.

---

# 31. Service and Business Responsibility

Services may affect business responsibility.

Examples:

- Matter Creation assigns responsibility.
- Order Conversion transfers order responsibility into matter responsibility.
- Opportunity Assignment creates ownership.
- Routing Decision may assign an agent.
- AI Draft Generation may require review authority.
- Permission Evaluation determines who may act.

Services that affect responsibility must declare:

- responsibility owner;
- authorization requirement;
- review requirement;
- audit requirement;
- event output.

Business responsibility should not be hidden in service implementation.

---

# 32. Service and AI Capability

A Core Service may use AI.

But AI usage must be governed.

A service using AI shall declare:

- AI role;
- whether AI is optional or required;
- knowledge sources;
- input objects;
- allowed output;
- risk level;
- confidence handling;
- human review requirement;
- event recording;
- audit storage;
- prohibited actions.

Examples:

```text
AI Classification Recommendation Service
    AI Role: recommendation support
    Human Review: required before final filing selection

AI Evidence Review Assistance Service
    AI Role: sufficiency analysis support
    Human Review: required for final legal conclusion

AI Communication Summary Service
    AI Role: summarization
    Human Review: optional unless used for client advice
```

AI shall not silently mutate critical Core Objects.

---

# 33. Service and Products

Products consume Core Services.

A product may:

- call a Core Service;
- present service output;
- request service execution;
- compose services into a user journey;
- use AI-assisted service output;
- show service events and results.

A product shall not:

- redefine service meaning;
- bypass service contracts;
- call services without permission;
- hide service side effects;
- treat AI recommendations as approved conclusions without review;
- create duplicate local service implementations where Core exists.

Products own experience.

Core Services own reusable capability.

---

# 34. Service and Workplace

Workplace composes and operates work using Core Services.

Workplace may:

- invoke services based on workflow state;
- create tasks through services;
- respond to events;
- coordinate review;
- surface service outputs;
- combine human and AI work.

Workplace shall not redefine Core Service meaning.

Workplace operates service-based work.

Core defines service capability and contracts.

---

# 35. Service and `core-specs/`

Detailed service specifications belong in:

```text
core-specs/services/
```

Service specs should reference:

```text
core-specs/domains/
core-specs/objects/
core-specs/events/
core-specs/api/
core-specs/agents/
core-specs/workflows/
core-specs/contracts/
```

A service spec should not exist without a domain owner.

A service spec should not hide AI usage.

A service spec should not omit permission and failure behavior when professional risk exists.

---

# 36. Service Specification Structure

Every detailed Core Service specification shall follow a standard structure.

```text
# Service Name

1. Service Purpose
2. Owning Domain
3. Service Category
4. Capability Description
5. Canonical Model Dependencies
6. In Scope
7. Out of Scope
8. Input
9. Output
10. Context Requirements
11. Permission and Policy Requirements
12. Knowledge Dependencies
13. Objects Read
14. Objects Created or Updated
15. Side Effects
16. Events Published
17. Events Consumed
18. Contracts
19. AI Usage
20. Human Review Requirements
21. Failure Behavior
22. Idempotency and Safety
23. Quality Requirements
24. Product Consumers
25. Workflow / Execution Usage
26. MVP Priority
27. Acceptance Criteria
28. Revision Notes
```

This structure belongs to:

```text
core-specs/services/
```

---

# 37. Service Inclusion Test

A concept may become a Core Service only if it satisfies most of the following conditions:

1. It represents a reusable capability.
2. It has a primary owning Core Domain.
3. It acts on or retrieves Core Objects, Knowledge, Policy or Events.
4. It may be consumed by more than one product, Workplace, AI agent or service.
5. It requires permission, policy, audit or governance.
6. It produces meaningful output or side effects.
7. It may publish or consume Events.
8. It should be exposed through explicit contracts.
9. It supports the Professional Value Flow.
10. Fragmentation would occur if each product implemented it separately.

If a concept fails this test, it may be a product function, UI action, implementation helper or vendor wrapper rather than a Core Service.

---

# 38. Service Exclusion Test

A concept shall be excluded from Core Service status if it is primarily:

- a product button action;
- a UI interaction;
- a product-specific workflow step;
- a local helper function;
- a vendor API wrapper without Core meaning;
- a report export;
- a prompt template;
- a one-product-only behavior;
- a temporary script;
- a cache operation;
- a direct database query with no domain responsibility.

Excluded services may still exist in implementation or products.

They should not be promoted to Core Service status.

---

# 39. Service Naming Rules

Core Service names shall be stable and capability-oriented.

## Rule 1 — Use capability names

Correct:

```text
Trademark Search Service
Classification Recommendation Service
Matter Creation Service
Routing Decision Service
Knowledge Retrieval Service
```

Incorrect:

```text
Search Button Handler
Class Wizard Step Function
Matter Modal Submit
Route Card Click
```

## Rule 2 — Avoid vendor names

Correct:

```text
AI Document Draft Assistance Service
```

Incorrect:

```text
OpenAI POA Prompt Function
```

## Rule 3 — Avoid database operation names

Correct:

```text
Agent Matching Service
```

Incorrect:

```text
QueryAgentTableByCountry
```

Service names should remain meaningful across products and technologies.

---

# 40. Service Boundary Rules

Every Core Service shall define boundaries.

A boundary statement should answer:

- what capability the service provides;
- what it does not provide;
- which domain owns it;
- which objects it reads or changes;
- which knowledge it requires;
- which events it emits;
- which contracts expose it;
- which products consume it;
- whether AI is involved;
- whether human review is required.

Examples:

## 40.1 Classification Recommendation vs Filing Decision

Classification Recommendation Service may recommend classes and goods/services.

It does not make final filing decisions without human or product approval.

## 40.2 Evidence Review Assistance vs Legal Conclusion

Evidence Review Assistance Service may assist sufficiency review.

It does not issue final legal conclusion autonomously.

## 40.3 Agent Matching vs Assignment Approval

Agent Matching Service may recommend agents.

Business Responsibility determines who approves assignment.

## 40.4 Document Generation vs Official Submission

Document Generation Service may generate documents.

Official submission belongs to product workflow, human review or authorized filing process.

---

# 41. Service Extension Rule

New Core Services may be added only through governed extension.

A service extension proposal shall include:

- proposed service name;
- owning domain;
- service category;
- capability description;
- reason existing services are insufficient;
- input;
- output;
- context;
- permissions;
- objects involved;
- knowledge dependencies;
- side effects;
- events;
- contracts;
- AI usage;
- human review;
- product consumers;
- MVP relevance;
- acceptance criteria.

No product may add a Core Service directly.

A product may request service review.

---

# 42. Service Versioning Rule

Core Services may evolve.

Changes requiring review include:

- service responsibility change;
- input or output semantic change;
- permission change;
- policy change;
- side effect change;
- event change;
- contract change;
- AI usage change;
- human review change;
- failure behavior change;
- quality requirement change.

Minor implementation changes that preserve contract behavior may not require semantic version change.

Contract-affecting changes require versioning.

---

# 43. Service Review Questions

When reviewing a Core Service, reviewers shall ask:

1. What reusable capability does this service provide?
2. Which Core Domain owns it?
3. Which service category does it belong to?
4. Which Canonical Models does it depend on?
5. What input does it require?
6. What output does it produce?
7. What context is required?
8. What permissions and policies apply?
9. What knowledge does it depend on?
10. What objects does it read, create or update?
11. What side effects does it have?
12. What events does it publish or consume?
13. What contracts expose it?
14. Does it use AI?
15. Is human review required?
16. What failure behavior applies?
17. Is it idempotent or safety-controlled?
18. Which products or Workplaces consume it?
19. Would products fragment if this service did not exist?
20. Can Codex implement it from approved specifications?

---

# 44. Service Anti-Patterns

## 44.1 Button Service

A product button handler is promoted to Core Service.

Correction:

```text
Product buttons call Core Services.
They do not define them.
```

## 44.2 Function Service

A local helper function becomes a Core Service without domain responsibility.

Correction:

```text
Core Services must represent reusable capability.
```

## 44.3 Vendor Wrapper Service

A vendor API wrapper is treated as a Core Service.

Correction:

```text
Vendor wrappers belong to implementation.
Core Service defines capability independent of vendor.
```

## 44.4 AI Prompt Service

A prompt becomes the service definition.

Correction:

```text
AI capability and service contract define the service.
Prompt implementation is downstream.
```

## 44.5 Hidden Side Effect Service

A service updates objects or publishes events without declaring side effects.

Correction:

```text
Side effects must be explicit.
```

## 44.6 Ungoverned Recommendation Service

A service provides professional recommendations without knowledge, permission, audit or review.

Correction:

```text
Professional recommendation services require governance.
```

---

# 45. Baseline Core Service Inventory

The initial Core Service inventory shall be derived from the Core Domain Map and Execution Matrix.

A baseline inventory includes, but is not limited to:

```text
Identity and Permission Services
    Identity Resolution
    Organization Lookup
    User Context
    Permission Evaluation
    Policy Evaluation

Knowledge Services
    Knowledge Retrieval
    Knowledge Validation
    Jurisdiction Rule Lookup
    Filing Requirement Retrieval
    Classification Rule Retrieval
    Document Template Retrieval

Professional Services
    Brand Portfolio Mapping
    Trademark Search
    Trademark Status Normalization
    Trademark Lifecycle Tracking
    Jurisdiction Lookup
    Classification Recommendation
    Goods/Services Validation
    Document Generation
    Document Parsing
    Evidence Packaging

Business Execution Services
    Customer Context
    Matter Creation
    Matter Status Update
    Matter Responsibility Assignment
    Order Creation
    Order-to-Matter Conversion
    Opportunity Discovery
    Opportunity Scoring
    Review Assignment

Execution and Event Services
    Task Creation
    Task Assignment
    Task Completion
    Event Publishing
    Event Subscription
    Notification Dispatch
    Workflow Contract Activation
    State Transition
    Timeline Recording

Collaboration Network Services
    Partner Lookup
    Agent Search
    Agent Capability Matching
    Service Provider Search
    Service Network Coverage
    Routing Decision
    Communication Linking
    Conversation Threading
    Reliability Scoring Support

AI-Assisted Services
    AI Classification Recommendation
    AI Document Draft Assistance
    AI Evidence Review Assistance
    AI Trademark Status Summary
    AI Opportunity Discovery
    AI Routing Assistance
    AI Communication Summary
```

The full service inventory shall be maintained in:

```text
Appendix D — Core Service Index
core-specs/services/
```

---

# 46. Service and MVP Priority

Services should be implemented according to Core MVP priorities.

A minimal MVP service set may include:

```text
Phase 1 — Foundation Core
    Identity Resolution
    User Context
    Permission Evaluation
    Knowledge Retrieval

Phase 2 — Professional Core
    Brand Portfolio Mapping
    Trademark Search
    Jurisdiction Lookup
    Classification Recommendation
    Document Generation

Phase 3 — Business Execution Core
    Customer Context
    Matter Creation
    Order Creation
    Order-to-Matter Conversion
    Task Creation
    Event Publishing

Phase 4 — Growth Core
    Opportunity Discovery
    Notification Dispatch
    Evidence Packaging
    Agent Search
    Routing Decision

Phase 5 — Network Core
    Partner Lookup
    Service Provider Search
    Service Network Coverage
    Communication Linking
```

The MVP should prioritize services that make the Core executable.

It should not implement isolated product functions before shared Core Services.

---

# 47. Service and Codex

Codex tasks shall implement services from approved service specifications.

A Codex service task should include:

- service name;
- owning domain;
- service category;
- input and output;
- context;
- permissions and policies;
- objects read or changed;
- knowledge dependencies;
- side effects;
- events;
- contracts;
- AI usage restrictions;
- human review requirements;
- failure behavior;
- idempotency and safety;
- tests;
- acceptance criteria;
- prohibited overreach.

Codex shall not invent Core Service meaning from product-level prompts.

---

# 48. Core Service Rules

The following rules are established by this chapter.

## Rule 1 — Core Services SHALL expose reusable capabilities

A service shall not be a product button or local helper function.

## Rule 2 — Core Services SHALL have one primary owning domain

Service ownership must be explicit.

## Rule 3 — Core Services SHALL define input, output and context

Hidden dependencies are not allowed for meaningful Core Services.

## Rule 4 — Core Services SHALL enforce permission and policy

Permission shall not be UI-only.

## Rule 5 — Core Services SHALL declare side effects

Object changes, event publication, task creation and AI output must be explicit.

## Rule 6 — Core Services SHALL publish events where meaningful

Important changes and outcomes should be observable.

## Rule 7 — Core Services SHALL be consumed through contracts

Products, Workplaces and AI agents shall not consume services informally.

## Rule 8 — AI-Assisted Services SHALL be governed

AI usage requires knowledge, context, permission, risk, audit and review rules.

## Rule 9 — Core Services SHALL define failure behavior

Professional services must not fail silently or return misleading output.

## Rule 10 — Core Service changes SHALL be governed and versioned

Semantic or contract-affecting changes require review.

---

# 49. Specification Output

This chapter produces the following specification output:

- Core Service definition;
- Core Service exclusions;
- service responsibility model;
- service ownership rules;
- service categories;
- service input, output and context rules;
- permission and policy rules;
- side effect rules;
- event rules;
- contract rules;
- service composition rules;
- quality and failure handling rules;
- AI-assisted service rules;
- service-to-object, knowledge, business responsibility, product and Workplace mapping;
- service specification structure;
- inclusion and exclusion tests;
- naming and boundary rules;
- extension and versioning rules;
- review questions;
- anti-patterns;
- baseline Core Service inventory;
- MVP service priority;
- Codex implementation rules.

These outputs guide Chapters 16 and 17 and Part III.

---

# 50. Execution Mapping

This chapter does not directly define API endpoints or implementation code.

It controls how Core Services become executable assets.

| Service Architecture Element | Execution Mapping |
|------------------------------|------------------|
| Service Meaning | service spec and acceptance criteria |
| Owning Domain | domain service ownership |
| Input / Output | service contract and validation |
| Context | request context and execution context |
| Permission / Policy | authorization checks and policy evaluation |
| Knowledge Dependencies | retrieval and validation services |
| Object Interaction | domain models and persistence operations |
| Side Effects | object updates, tasks, events and audit records |
| Events | event specs and event publishing |
| Contracts | API, agent, workflow and consumption contracts |
| AI Usage | agent specs, governance and review workflow |
| Failure Behavior | error contracts and fallback rules |
| Quality Rules | tests, validation and monitoring |
| Product Consumers | product integration and consumption specs |
| MVP Priority | Codex task sequencing |

Implementation shall preserve service meaning, ownership, governance and contracts.

---

# 51. Relationship to core-specs/

This chapter governs `core-specs/services/`.

Every file in `core-specs/services/` shall follow the service specification structure defined in this chapter.

Each service file shall reference related specs:

```text
core-specs/domains/
core-specs/objects/
core-specs/events/
core-specs/api/
core-specs/agents/
core-specs/workflows/
core-specs/contracts/
```

where relevant.

No service spec shall exist without a domain owner.

No product document shall override a Core Service specification.

No implementation task shall create a Core Service without an approved service spec or explicit architecture approval.

---

# 52. Exclusions

This chapter shall not include:

- complete service contracts for every service;
- API endpoint definitions;
- microservice topology;
- database implementation;
- product button behavior;
- product UI;
- product workflows;
- production prompts;
- vendor-specific integrations;
- deployment architecture;
- implementation code.

These belong elsewhere.

---

# 53. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines Core Service clearly.
- It distinguishes Core Services from buttons, UI actions, helper functions, vendor wrappers and prompt templates.
- It defines service ownership by domain.
- It defines service categories.
- It explains input, output, context, permission, policy, side effects, events, contracts, quality and failure behavior.
- It defines AI-assisted service governance.
- It maps services to objects, knowledge, business responsibility, Workplace and products.
- It provides a service specification structure for `core-specs/services/`.
- It defines inclusion, exclusion, naming, boundary, extension and versioning rules.
- It provides review questions and anti-patterns.
- It supports MVP service sequencing.
- It guides Codex implementation.
- It supports Book 02 TOC v1.2.

---

# 54. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 15, defining Core Service Architecture and service governance rules. |

---

**End of Chapter**
