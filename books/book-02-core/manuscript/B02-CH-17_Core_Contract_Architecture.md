# Book 02

# 17 — Core Contract Architecture

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-17

**Chapter Title:** Core Contract Architecture

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

This chapter defines the Core Contract Architecture of MarkOrbit.

Chapter 13 defined Core Domains.

Chapter 14 defined Core Objects.

Chapter 15 defined Core Services.

Chapter 16 defined Core Execution Primitives.

This chapter defines the contracts that allow all of those Core assets to be consumed safely and consistently.

A professional operating system cannot rely on informal integration.

If products, Workplaces, AI agents, services and implementations access Core assets without contracts, the Core will fragment.

A product may interpret a Trademark differently.

An AI agent may use unauthorized knowledge.

A workflow may mutate state incorrectly.

An API may expose sensitive data.

An event may be consumed with the wrong meaning.

A product may bypass permission rules.

A service may change behavior without downstream awareness.

Core Contracts prevent these failures.

They define how Core meaning is exposed, consumed, validated, versioned, governed and evolved.

The purpose of this chapter is to define the contract architecture that protects the Core while allowing products and implementations to move quickly.

---

# 2. Core Question

This chapter answers one question:

> How shall MarkOrbit define contracts so that Core Domains, Objects, Services, Events, AI Capabilities, Workflows and Products can interoperate without redefining shared meaning?

The answer is:

> MarkOrbit shall use explicit Data, API, Event, Agent, Workflow and Consumption Contracts to govern how Core assets are exposed, consumed, executed, automated and evolved.

The contract principle is:

```text
No Core consumption without contract.
```

This does not mean every internal helper requires a heavy contract.

It means any product, Workplace, AI agent, integration or service that consumes shared Core meaning must do so through explicit contract rules.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- Core Contract definition;
- contract responsibility;
- contract categories;
- Data Contract;
- API Contract;
- Event Contract;
- Agent Contract;
- Workflow Contract;
- Consumption Contract;
- contract ownership;
- contract versioning;
- contract validation;
- contract governance;
- contract relationship to domains, objects, services, events, AI and products;
- contract specification structure;
- inclusion and exclusion rules;
- review questions;
- anti-patterns;
- MVP contract priority;
- Codex implementation rules.

## 3.2 Out of Scope

This chapter does not define:

- complete API endpoint list;
- complete event payload list;
- full OpenAPI specification;
- runtime gateway design;
- external partner legal agreements;
- commercial service contracts;
- product terms of service;
- deployment infrastructure;
- vendor-specific integration details;
- production AI prompts;
- implementation code.

Detailed contract specifications belong in:

```text
core-specs/contracts/
core-specs/api/
core-specs/events/
core-specs/agents/
core-specs/workflows/
```

---

# 4. Core Contract Definition

A Core Contract is:

> an explicit, versioned and governed agreement that defines how a Core asset may be exposed, consumed, executed, integrated, automated or extended without changing its shared meaning.

This definition contains seven parts.

## 4.1 Explicit

A Core Contract must be documented.

It cannot be hidden in code, UI assumptions or prompt behavior.

## 4.2 Versioned

A Core Contract must support change without uncontrolled breakage.

## 4.3 Governed

A Core Contract must respect permission, policy, audit, risk and human review rules.

## 4.4 Agreement

A Core Contract defines expectations between provider and consumer.

## 4.5 Core Asset

A Core Contract may apply to objects, services, events, workflows, AI agents or products.

## 4.6 Consumption

A Core Contract defines how downstream systems consume Core.

## 4.7 Meaning Protection

A Core Contract protects shared Core meaning from being reinterpreted by consumers.

---

# 5. What a Core Contract Is Not

A Core Contract is not:

- a commercial sales contract;
- a client engagement agreement;
- a legal service agreement;
- a product pricing package;
- a marketing promise;
- a UI design rule;
- a database schema alone;
- an informal API convention;
- a prompt instruction;
- a product workflow description;
- a vendor-specific SDK wrapper;
- an implementation comment.

For example:

- `Trademark API Contract` may be a Core Contract.
- `Trademark search page behavior` is product design.
- `MatterCreated Event Contract` may be a Core Contract.
- `Activity feed display row` is product UI.
- `Classification Agent Contract` may be a Core Contract.
- `classification prompt template` is implementation detail.
- `Workflow Contract` may be Core.
- `MarkReg filing wizard` is product experience.

---

# 6. Contract Architecture Position

Core Contracts sit inside the Core Kernel.

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

Core Contracts are the boundary between Core assets and Core consumers.

They protect:

- domain meaning;
- object semantics;
- service behavior;
- event interpretation;
- workflow interoperability;
- AI governance;
- product consumption.

Without contracts, Core assets may exist but will be consumed inconsistently.

---

# 7. Contract Responsibility

Every Core Contract must answer:

> What Core asset is being consumed, by whom, under what rules, with what meaning, permission, version and expected behavior?

A contract responsibility statement should identify:

- provider;
- consumer;
- asset exposed;
- allowed usage;
- prohibited usage;
- input or payload;
- output or result;
- permission;
- policy;
- version;
- failure behavior;
- audit requirement;
- review requirement where relevant.

A contract without a clear responsibility should not be accepted into Core architecture.

---

# 8. Contract Categories

Book 02 defines six Core Contract categories.

```text
1. Data Contract
2. API Contract
3. Event Contract
4. Agent Contract
5. Workflow Contract
6. Consumption Contract
```

These categories are related but not identical.

They answer different consumption questions.

| Contract Type | Primary Question |
|---------------|------------------|
| Data Contract | What does the data mean and how may it be represented? |
| API Contract | How may services and objects be accessed or changed? |
| Event Contract | What happened and how may consumers interpret it? |
| Agent Contract | What may an AI agent do, using which context and knowledge? |
| Workflow Contract | What execution structure may Workplace and products rely on? |
| Consumption Contract | How may a product, Workplace or downstream system consume Core? |

---

# 9. Data Contract

## 9.1 Definition

A Data Contract defines the meaning, structure, ownership, sensitivity, quality and consumption rules of Core data.

It answers:

> What does this data represent, where does it come from, and how may it be used?

## 9.2 Responsibility

Data Contracts are responsible for:

- object meaning;
- field meaning;
- source and provenance;
- data quality;
- data sensitivity;
- required fields;
- optional fields;
- derived fields;
- read/write permissions;
- versioning;
- validation rules;
- retention rules.

## 9.3 Examples

Examples include:

```text
Trademark Data Contract
Customer Data Contract
Matter Data Contract
Document Data Contract
Agent Data Contract
Knowledge Source Data Contract
Routing Decision Data Contract
```

## 9.4 Boundary

A Data Contract is not the same as a database schema.

A database schema implements a Data Contract.

The Data Contract defines meaning.

## 9.5 Core Use

Data Contracts support:

- database implementation;
- API design;
- event payload design;
- product consumption;
- AI context access;
- audit;
- migration;
- data import and normalization.

---

# 10. API Contract

## 10.1 Definition

An API Contract defines how Core Objects and Core Services may be accessed, invoked or modified by authorized consumers.

It answers:

> How may a consumer call the Core safely?

## 10.2 Responsibility

API Contracts are responsible for:

- endpoint or operation name;
- service or object exposed;
- input;
- output;
- permissions;
- policy checks;
- context requirements;
- validation;
- side effects;
- event publication;
- error behavior;
- idempotency;
- rate or usage limits where relevant;
- version compatibility.

## 10.3 Examples

Examples include:

```text
Trademark Search API Contract
Matter Creation API Contract
Order-to-Matter Conversion API Contract
Classification Recommendation API Contract
Document Generation API Contract
Agent Matching API Contract
Routing Decision API Contract
Knowledge Retrieval API Contract
```

## 10.4 Boundary

An API Contract is not only an HTTP route.

It is a consumption agreement.

The same contract may be implemented through REST, RPC, internal service call, queue command or future interface.

Book 02 defines the contract meaning.

Implementation chooses the protocol.

---

# 11. Event Contract

## 11.1 Definition

An Event Contract defines the meaning, payload, source, trigger, consumers and lifecycle rules of a Core Event.

It answers:

> What happened, what does it mean, and how may consumers react?

## 11.2 Responsibility

Event Contracts are responsible for:

- event name;
- event meaning;
- source domain;
- trigger;
- related Core Objects;
- payload structure;
- payload version;
- actor and timestamp;
- correlation and causation;
- consumers;
- replay rules;
- retention;
- audit;
- sensitivity;
- compatibility.

## 11.3 Examples

Examples include:

```text
MatterCreated Event Contract
OrderConvertedToMatter Event Contract
TaskAssigned Event Contract
TrademarkStatusChanged Event Contract
DocumentUploaded Event Contract
RoutingDecisionMade Event Contract
AIRecommendationReviewRequired Event Contract
```

## 11.4 Boundary

An Event Contract is not a log format.

It is not a product activity feed item.

It is a semantic change contract.

Products may show events in activity feeds.

But the Event Contract defines meaning.

---

# 12. Agent Contract

## 12.1 Definition

An Agent Contract defines what an AI agent or automated agent may do, what knowledge it may use, what objects it may access, what services it may call, and what review or audit is required.

It answers:

> What is this agent allowed to do under Core governance?

## 12.2 Responsibility

Agent Contracts are responsible for:

- agent identity;
- agent purpose;
- allowed capabilities;
- prohibited capabilities;
- authorized knowledge sources;
- accessible objects;
- allowed services;
- permission boundary;
- risk level;
- human review requirement;
- output type;
- event recording;
- audit requirement;
- failure behavior;
- escalation behavior;
- version.

## 12.3 Examples

Examples include:

```text
Classification Assistant Agent Contract
Document Draft Assistant Agent Contract
Evidence Review Assistant Agent Contract
Trademark Status Summary Agent Contract
Opportunity Discovery Agent Contract
Routing Assistant Agent Contract
Communication Summary Agent Contract
```

## 12.4 Boundary

An Agent Contract is not a prompt.

A prompt may implement part of an Agent Contract.

But the contract defines governance.

AI agents shall not operate only through prompt instructions.

They must operate under Core identity, knowledge, permission, context, audit and review rules.

---

# 13. Workflow Contract

## 13.1 Definition

A Workflow Contract defines the reusable execution structure for a professional work pattern.

It answers:

> What states, transitions, tasks, events, permissions and review rules may Workplace and products rely on?

Workflow Contract was introduced in Chapter 16 as an execution primitive.

In this chapter, it is also treated as a contract type because it governs interoperability.

## 13.2 Responsibility

Workflow Contracts are responsible for:

- workflow type;
- owning domain;
- related Core Objects;
- allowed states;
- allowed transitions;
- required tasks;
- optional tasks;
- event triggers;
- service calls;
- permission rules;
- policy rules;
- AI usage;
- human review;
- notification rules;
- product consumption rules;
- version.

## 13.3 Examples

Examples include:

```text
Trademark Filing Matter Workflow Contract
Order-to-Matter Conversion Workflow Contract
Document Review Workflow Contract
Evidence Review Workflow Contract
AI Recommendation Review Workflow Contract
Agent Routing Workflow Contract
```

## 13.4 Boundary

A Workflow Contract is not the product workflow experience.

It does not define the visual wizard, screen layout, task board or operational SOP.

It defines the execution contract that Workplace and products consume.

---

# 14. Consumption Contract

## 14.1 Definition

A Consumption Contract defines how a downstream consumer may use Core assets without redefining them.

It answers:

> What may this product, Workplace, AI agent, service or integration consume from Core, and under what limitations?

## 14.2 Responsibility

Consumption Contracts are responsible for:

- consumer identity;
- Core assets consumed;
- allowed read behavior;
- allowed write behavior;
- allowed service calls;
- event subscriptions;
- AI capability usage;
- product-specific extensions;
- prohibited redefinition;
- permission model;
- audit requirements;
- compatibility expectations.

## 14.3 Examples

Examples include:

```text
MarkReg Core Consumption Contract
Lite Core Consumption Contract
MGSN Core Consumption Contract
Workplace Core Consumption Contract
Brand Asset Vault Consumption Contract
Opportunity Engine Consumption Contract
```

## 14.4 Boundary

A Consumption Contract is not a product PRD.

It does not define product features in detail.

It defines how the product consumes Core.

Products may specialize experience.

They shall not redefine Core meaning.

---

# 15. Contract Ownership

Every Core Contract shall have an owner.

Ownership means responsibility for contract meaning, versioning and compatibility.

Contract ownership may be assigned by:

- owning domain;
- owning service;
- owning event source;
- owning agent specification;
- owning workflow contract;
- Core architecture governance.

Examples:

```text
Trademark API Contract
    Owner: Trademark Domain

MatterCreated Event Contract
    Owner: Matter Domain + Event Domain

Classification Assistant Agent Contract
    Owner: Classification Domain + AI Governance

Order-to-Matter Conversion Workflow Contract
    Owner: Order Domain + Workflow Contract Domain

Lite Consumption Contract
    Owner: Core Consumption Specification + Lite Product Specification
```

Contract consumers do not own contract meaning.

They consume it.

---

# 16. Contract Provider and Consumer

Every Core Contract shall identify provider and consumer.

## 16.1 Provider

The provider owns or exposes the Core asset.

Examples:

- Trademark Domain provides Trademark Data Contract.
- Matter Service provides Matter Creation API Contract.
- Event Domain provides Event Contract.
- AI Governance provides Agent Contract.
- Workflow Contract Domain provides Workflow Contract.

## 16.2 Consumer

The consumer uses the Core asset.

Examples:

- MarkReg consumes Trademark Search API.
- Lite consumes Classification Recommendation Service.
- MGSN consumes Agent Matching Service.
- Workplace consumes Task and Workflow Contracts.
- AI agents consume Knowledge and Core Objects under Agent Contracts.

A contract should be clear about who consumes what.

---

# 17. Contract Input and Output

Contracts should define input and output where applicable.

## 17.1 Input

Input may include:

- object ID;
- service parameters;
- actor identity;
- organization context;
- permission context;
- product consumer;
- related Core Objects;
- knowledge sources;
- workflow state;
- AI context;
- request metadata.

## 17.2 Output

Output may include:

- object data;
- created or updated object;
- recommendation;
- validation result;
- event;
- task;
- notification;
- error;
- review requirement;
- audit record.

Input and output must preserve Core meaning.

They should not be product-specific unless the contract is explicitly a product consumption contract.

---

# 18. Contract Permission and Policy

Contracts must define permission and policy requirements.

Questions include:

- who may call this contract;
- which product may consume it;
- which object may be accessed;
- which fields may be visible;
- which actions may be performed;
- whether AI may use the output;
- whether external sharing is allowed;
- whether human review is required;
- whether audit is required;
- which policy rules apply.

Permission should not live only in UI.

Policy should not live only in product logic.

Contracts should enforce both.

---

# 19. Contract Versioning

Contracts must support versioning.

Versioning is required when changes affect consumers.

Contract changes may include:

- field meaning change;
- input requirement change;
- output structure change;
- permission change;
- policy change;
- event payload change;
- service side effect change;
- AI usage change;
- review requirement change;
- error behavior change;
- deprecation;
- removal.

Versioning should distinguish:

- patch changes;
- backward-compatible minor changes;
- breaking major changes.

The exact versioning scheme may be defined in `core-specs/contracts/`.

Book 02 requires the principle.

---

# 20. Contract Compatibility

Contract compatibility protects downstream consumers.

Before changing a contract, reviewers should identify:

- affected products;
- affected Workplaces;
- affected AI agents;
- affected services;
- affected event consumers;
- affected tests;
- affected Codex tasks;
- migration requirements;
- deprecation period;
- fallback behavior.

Compatibility review prevents local changes from breaking the ecosystem.

---

# 21. Contract Validation

Contracts should be validated where possible.

Validation may include:

- schema validation;
- permission validation;
- policy validation;
- event payload validation;
- API request validation;
- agent context validation;
- workflow transition validation;
- data quality validation;
- AI output validation;
- human review validation.

Validation may occur at:

- design time;
- test time;
- runtime;
- review time;
- Codex task acceptance.

A contract that cannot be validated may still exist, but validation should be added where professional or system risk is significant.

---

# 22. Contract Failure Behavior

Contracts must define failure behavior.

Failure types may include:

- invalid input;
- missing permission;
- policy denial;
- stale data;
- incompatible version;
- missing required context;
- knowledge unavailable;
- AI confidence too low;
- review required;
- service unavailable;
- event delivery failure;
- workflow transition invalid.

Failure should be explicit.

Silent failure is unacceptable for professional execution.

---

# 23. Contract Auditability

Contracts should define audit requirements.

Audit may be required when:

- legal rights may be affected;
- official filing status may change;
- deadline-sensitive actions occur;
- client advice is generated;
- AI output is used professionally;
- permission is elevated;
- data is shared externally;
- routing decision assigns external service provider;
- order converts to matter;
- payment or business responsibility changes.

Audit should record:

- actor;
- consumer;
- contract used;
- input summary;
- output summary;
- timestamp;
- permission result;
- policy result;
- related objects;
- related events;
- review record where applicable.

---

# 24. Contract and Core Domains

Contracts expose domains safely.

A domain may define multiple contracts.

Examples:

```text
Trademark Domain
    Trademark Data Contract
    Trademark Search API Contract
    TrademarkStatusChanged Event Contract

Matter Domain
    Matter Data Contract
    Matter Creation API Contract
    MatterCreated Event Contract
    Matter Workflow Contract

Agent Domain
    Agent Data Contract
    Agent Search API Contract
    Agent Capability Contract
    Agent Matching Contract
```

A contract should not redefine the domain.

It exposes or protects domain meaning.

---

# 25. Contract and Core Objects

Contracts define how Core Objects are represented and consumed.

Examples:

- Data Contract defines object fields and meaning.
- API Contract defines how objects are read or changed.
- Event Contract references object identity and state changes.
- Agent Contract defines which objects AI may access.
- Workflow Contract defines object state transitions.
- Consumption Contract defines product-level object usage.

Object meaning comes from Core Object Architecture.

Contracts expose that meaning safely.

---

# 26. Contract and Core Services

Contracts define how Core Services are invoked and consumed.

A service contract should define:

- service purpose;
- owning domain;
- input;
- output;
- context;
- permission;
- policy;
- side effects;
- events;
- failure behavior;
- AI usage;
- human review;
- version.

A product should not call a service without understanding these rules.

An AI agent should not invoke a service outside its Agent Contract.

---

# 27. Contract and Events

Event Contracts define how events are published and consumed.

They should include:

- event source;
- trigger;
- related objects;
- payload;
- version;
- consumers;
- retention;
- replay;
- sensitivity;
- audit;
- compatibility.

Event consumers shall not assume extra meaning beyond the Event Contract.

Products may display events.

They shall not redefine them.

---

# 28. Contract and AI Capability

AI Capability requires Agent Contracts.

Agent Contracts protect:

- knowledge usage;
- object access;
- service invocation;
- output risk;
- human review;
- auditability;
- permission;
- product consumption.

AI without contract creates governance risk.

For example:

```text
AI Classification Assistant
    must know:
        allowed knowledge sources
        allowed input objects
        output type
        review requirement
        event output
        prohibited actions
```

A prompt is not enough.

---

# 29. Contract and Workflow

Workflow Contracts govern execution interoperability.

They define the structure that Workplace and products rely on.

A Workflow Contract may reference:

- objects;
- states;
- transitions;
- tasks;
- events;
- services;
- permissions;
- policies;
- AI usage;
- review requirements;
- notification rules;
- product consumers.

Workflow Contracts prevent product workflows from creating incompatible state logic.

---

# 30. Contract and Product Consumption

Products consume Core through Consumption Contracts and other Core Contracts.

A product consumption contract should define:

- product name;
- Core Domains consumed;
- Core Objects consumed;
- Core Services called;
- Core Events subscribed;
- AI Capabilities used;
- Workflow Contracts consumed;
- product-specific extensions allowed;
- prohibited Core redefinitions;
- permission model;
- audit rules;
- compatibility obligations.

Examples:

```text
MarkReg Consumption Contract
Lite Consumption Contract
MGSN Consumption Contract
```

This allows product specialization without Core fragmentation.

---

# 31. Contract and Workplace Consumption

Workplace consumes:

- Task;
- Event;
- State;
- Context;
- Workflow Contract;
- Notification;
- Core Objects;
- Core Services.

A Workplace Consumption Contract should define:

- what Core work items are visible;
- how tasks are operated;
- how events are displayed;
- how workflow contracts are consumed;
- how AI assistance is invoked;
- how human review is enforced;
- how permissions are applied.

Book 03 defines Workplace Framework.

Book 02 defines the Core contracts Workplace consumes.

---

# 32. Contract and Codex

Codex tasks must reference contracts.

A Codex task should not say only:

> Build trademark search.

It should reference:

- Trademark Domain;
- Trademark Object;
- Trademark Search Service;
- Trademark API Contract;
- Data Contract;
- permission rule;
- tests;
- acceptance criteria.

A Codex task for AI should reference:

- Agent Contract;
- Knowledge sources;
- permitted objects;
- risk level;
- review requirement;
- event outputs.

Contracts make Codex implementation reliable.

Without contracts, Codex may create locally correct but architecturally inconsistent code.

---

# 33. Contract Specification Structures

Detailed contract specifications shall use standard structures.

## 33.1 Data Contract Structure

```text
# Data Contract Name

1. Contract Purpose
2. Owning Domain
3. Related Core Object
4. Field Semantics
5. Required Fields
6. Optional Fields
7. Source and Provenance
8. Data Quality Rules
9. Sensitivity and Privacy Rules
10. Permission Rules
11. Validation Rules
12. Versioning Rules
13. Consumers
14. Acceptance Criteria
15. Revision Notes
```

## 33.2 API Contract Structure

```text
# API Contract Name

1. Contract Purpose
2. Owning Domain / Service
3. Operation Name
4. Input
5. Output
6. Context Requirements
7. Permission and Policy Requirements
8. Side Effects
9. Events Published
10. Error and Failure Behavior
11. Idempotency and Safety
12. Versioning
13. Consumers
14. Acceptance Criteria
15. Revision Notes
```

## 33.3 Event Contract Structure

```text
# Event Contract Name

1. Contract Purpose
2. Source Domain
3. Event Meaning
4. Trigger
5. Payload
6. Related Core Objects
7. Actor and Source
8. Correlation and Causation
9. Consumers
10. Replay and Retention
11. Sensitivity
12. Versioning
13. Acceptance Criteria
14. Revision Notes
```

## 33.4 Agent Contract Structure

```text
# Agent Contract Name

1. Contract Purpose
2. Agent Identity
3. Owning Domain
4. Allowed Capabilities
5. Prohibited Capabilities
6. Authorized Knowledge Sources
7. Accessible Core Objects
8. Allowed Core Services
9. Context Requirements
10. Permission and Policy Requirements
11. Output Types
12. Risk Level
13. Human Review Requirements
14. Events Published
15. Audit Requirements
16. Failure and Escalation
17. Versioning
18. Product Consumers
19. Acceptance Criteria
20. Revision Notes
```

## 33.5 Workflow Contract Structure

```text
# Workflow Contract Name

1. Contract Purpose
2. Owning Domain
3. Related Core Objects
4. States
5. Transitions
6. Required Tasks
7. Optional Tasks
8. Events Published
9. Events Consumed
10. Services Used
11. Context Requirements
12. Permission and Policy Requirements
13. AI Usage
14. Human Review Requirements
15. Notification Rules
16. Product / Workplace Consumers
17. Versioning
18. Acceptance Criteria
19. Revision Notes
```

## 33.6 Consumption Contract Structure

```text
# Consumption Contract Name

1. Contract Purpose
2. Consumer
3. Core Domains Consumed
4. Core Objects Consumed
5. Core Services Consumed
6. Core Events Subscribed
7. Workflow Contracts Consumed
8. AI Capabilities Used
9. Allowed Product Extensions
10. Prohibited Redefinitions
11. Permission and Policy Requirements
12. Audit Requirements
13. Compatibility Rules
14. Versioning
15. Acceptance Criteria
16. Revision Notes
```

These structures belong in:

```text
core-specs/contracts/
core-specs/api/
core-specs/events/
core-specs/agents/
core-specs/workflows/
```

---

# 34. Contract Inclusion Test

A concept requires a Core Contract if it satisfies most of the following conditions:

1. It exposes Core meaning to a consumer.
2. It is consumed by a product, Workplace, AI agent, integration or service.
3. It involves Core Objects, Core Services, Events or Workflow Contracts.
4. It requires permission, policy, audit or review.
5. It affects professional or business responsibility.
6. It may change state or trigger execution.
7. It may be versioned independently.
8. It may affect multiple consumers.
9. It may create fragmentation if left informal.
10. It can be specified and validated.

If a concept fails this test, it may be an internal implementation detail rather than a Core Contract.

---

# 35. Contract Exclusion Test

A concept shall be excluded from Core Contract status if it is primarily:

- commercial sales agreement;
- product pricing package;
- UI behavior;
- product copy;
- one-time implementation detail;
- vendor SDK wrapper;
- local helper function interface;
- internal debug log;
- prompt instruction;
- temporary workflow note;
- operational SOP.

Excluded contracts may still exist outside Core.

They should not be treated as Core Contracts.

---

# 36. Contract Naming Rules

Core Contract names shall be stable and semantic.

## 36.1 Data Contract Names

Correct:

```text
Trademark Data Contract
Matter Data Contract
Agent Data Contract
```

Incorrect:

```text
Trademark Table Schema
Matter Grid Fields
Agent CSV Format
```

## 36.2 API Contract Names

Correct:

```text
Trademark Search API Contract
Matter Creation API Contract
```

Incorrect:

```text
Search Button Endpoint
Submit Modal API
```

## 36.3 Event Contract Names

Correct:

```text
MatterCreated Event Contract
TaskAssigned Event Contract
```

Incorrect:

```text
Activity Feed Log
Dashboard Update Event
```

## 36.4 Agent Contract Names

Correct:

```text
Classification Assistant Agent Contract
Document Draft Assistant Agent Contract
```

Incorrect:

```text
GPT Prompt V3
Class Chatbot Script
```

## 36.5 Consumption Contract Names

Correct:

```text
MarkReg Core Consumption Contract
Lite Core Consumption Contract
MGSN Core Consumption Contract
```

Incorrect:

```text
MarkReg Feature Plan
Lite Screen Design
MGSN User Flow
```

---

# 37. Contract Boundary Rules

Every Core Contract shall define boundaries.

A boundary statement should answer:

- what the contract exposes;
- what it does not expose;
- who provides it;
- who consumes it;
- what is allowed;
- what is prohibited;
- what permissions apply;
- what version applies;
- what failure behavior applies;
- what review is required.

Examples:

## 37.1 API Contract Boundary

A Classification Recommendation API Contract exposes recommendation capability.

It does not approve final filing strategy.

## 37.2 Agent Contract Boundary

A Document Draft Assistant Agent Contract allows draft generation.

It does not allow official submission without review.

## 37.3 Workflow Contract Boundary

A Trademark Filing Workflow Contract defines states and tasks.

It does not define MarkReg screen sequence.

## 37.4 Consumption Contract Boundary

Lite may consume Trademark and Classification.

It may not redefine Trademark or Classification semantics.

---

# 38. Contract Extension Rule

New Core Contracts may be added only through governed extension.

A contract extension proposal shall include:

- contract name;
- contract type;
- owning domain or service;
- provider;
- consumers;
- Core assets exposed;
- reason existing contracts are insufficient;
- input or payload;
- output or behavior;
- permission and policy;
- versioning;
- failure behavior;
- audit;
- AI usage if relevant;
- human review if relevant;
- acceptance criteria.

No product may create Core Contract meaning independently.

Products may request contract review.

---

# 39. Contract Versioning Rule

Contract semantic changes must be versioned.

Breaking changes require compatibility review.

A breaking change may include:

- required field removal;
- field meaning change;
- output type change;
- event meaning change;
- permission rule change;
- service side effect change;
- AI capability expansion;
- human review removal;
- workflow state change;
- consumer limitation change.

Consumers should be notified through governance process.

Contract versioning protects the ecosystem.

---

# 40. Contract Review Questions

When reviewing a Core Contract, reviewers shall ask:

1. What Core asset does this contract expose?
2. Who owns the contract?
3. Who provides it?
4. Who consumes it?
5. What meaning must be preserved?
6. What input, payload or object structure applies?
7. What output or behavior applies?
8. What permission and policy rules apply?
9. What side effects exist?
10. What events are published or consumed?
11. Does AI use this contract?
12. Is human review required?
13. What failure behavior applies?
14. What versioning and compatibility rules apply?
15. What audit is required?
16. Which products or Workplaces are affected?
17. Would consumers fragment without this contract?
18. Can Codex implement and test it from the contract spec?

---

# 41. Contract Anti-Patterns

## 41.1 Informal API

A product calls Core data directly without API Contract.

Correction:

```text
Products consume Core through explicit API or Consumption Contracts.
```

## 41.2 Schema as Contract

A database schema is treated as a Data Contract.

Correction:

```text
Data Contract defines meaning.
Schema implements it.
```

## 41.3 Log as Event Contract

Unstructured logs are consumed as Events.

Correction:

```text
Event Contracts define semantic events.
Logs are implementation artifacts.
```

## 41.4 Prompt as Agent Contract

A prompt controls AI behavior without Agent Contract.

Correction:

```text
Agent Contract defines capability, knowledge, permission, risk and review.
Prompt implements part of it.
```

## 41.5 Product Workflow as Workflow Contract

A product wizard defines the workflow contract.

Correction:

```text
Workflow Contract defines reusable execution structure.
Product wizard consumes it.
```

## 41.6 Product PRD as Consumption Contract

A product PRD is treated as the Core consumption rule.

Correction:

```text
Consumption Contract defines Core usage.
PRD defines product features.
```

## 41.7 Breaking Contract Without Versioning

A service output changes and products break.

Correction:

```text
Contract changes require versioning and compatibility review.
```

---

# 42. Baseline Contract Inventory

The initial Core Contract inventory shall include, but is not limited to:

```text
Data Contracts
    Identity Data Contract
    Customer Data Contract
    Trademark Data Contract
    Brand Data Contract
    Matter Data Contract
    Order Data Contract
    Document Data Contract
    Agent Data Contract
    Routing Decision Data Contract

API Contracts
    Identity Resolution API Contract
    Permission Evaluation API Contract
    Knowledge Retrieval API Contract
    Trademark Search API Contract
    Classification Recommendation API Contract
    Document Generation API Contract
    Matter Creation API Contract
    Order-to-Matter Conversion API Contract
    Agent Matching API Contract
    Routing Decision API Contract

Event Contracts
    MatterCreated Event Contract
    OrderConvertedToMatter Event Contract
    TaskAssigned Event Contract
    TrademarkStatusChanged Event Contract
    DocumentUploaded Event Contract
    RoutingDecisionMade Event Contract
    AIRecommendationReviewRequired Event Contract

Agent Contracts
    Classification Assistant Agent Contract
    Document Draft Assistant Agent Contract
    Evidence Review Assistant Agent Contract
    Trademark Status Summary Agent Contract
    Opportunity Discovery Agent Contract
    Routing Assistant Agent Contract
    Communication Summary Agent Contract

Workflow Contracts
    Trademark Filing Matter Workflow Contract
    Office Action Response Workflow Contract
    Document Review Workflow Contract
    Evidence Review Workflow Contract
    Order-to-Matter Conversion Workflow Contract
    AI Recommendation Review Workflow Contract
    Agent Routing Workflow Contract

Consumption Contracts
    Workplace Core Consumption Contract
    MarkReg Core Consumption Contract
    Lite Core Consumption Contract
    MGSN Core Consumption Contract
    Brand Asset Vault Consumption Contract
    Opportunity Engine Consumption Contract
```

The full contract inventory shall be maintained in:

```text
Appendix F — API Index
Appendix G — Agent Index
core-specs/contracts/
core-specs/api/
core-specs/events/
core-specs/agents/
core-specs/workflows/
```

---

# 43. Contract and MVP Priority

The MVP should implement contract coverage in phases.

```text
Phase 1 — Foundation Contracts
    Identity Data Contract
    Permission Evaluation API Contract
    Knowledge Retrieval API Contract
    Basic Consumption Contract

Phase 2 — Professional Contracts
    Trademark Data Contract
    Trademark Search API Contract
    Jurisdiction Lookup API Contract
    Classification Recommendation API Contract
    Document Data Contract

Phase 3 — Business Execution Contracts
    Customer Data Contract
    Matter Data Contract
    Order Data Contract
    Matter Creation API Contract
    Order-to-Matter Conversion API Contract
    MatterCreated Event Contract
    TaskAssigned Event Contract

Phase 4 — Growth Contracts
    Opportunity Data Contract
    Notification Contract
    Evidence Data Contract
    Agent Data Contract
    Routing Decision API Contract
    AI Recommendation Review Agent Contract

Phase 5 — Network Contracts
    Partner Data Contract
    Service Provider Data Contract
    Service Network Contract
    Communication Contract
    MGSN Consumption Contract
```

MVP shall not expose Core assets informally merely to move faster.

A minimal contract is better than no contract.

---

# 44. Contract and Codex

Codex implementation tasks shall reference relevant Core Contracts.

A Codex contract task should include:

- contract name;
- contract type;
- owning domain;
- related objects;
- related services;
- related events;
- provider;
- consumer;
- input or payload;
- output or behavior;
- permission and policy;
- version;
- failure behavior;
- audit rules;
- tests;
- acceptance criteria;
- prohibited overreach.

Codex shall not invent API, event, agent or workflow contracts without approved architecture source.

---

# 45. Core Contract Rules

The following rules are established by this chapter.

## Rule 1 — Core consumption SHALL occur through explicit contracts

Products, Workplaces, AI agents, services and integrations shall not consume Core informally.

## Rule 2 — Contracts SHALL preserve Core meaning

Contracts expose Core meaning.

They do not redefine it.

## Rule 3 — Contracts SHALL have ownership

Every contract must identify owner, provider and consumers.

## Rule 4 — Contracts SHALL define permission and policy

Access and action governance must be part of contract design.

## Rule 5 — Contracts SHALL define failure behavior

Professional execution must not fail silently.

## Rule 6 — Contracts SHALL be versioned

Consumer-affecting changes require versioning and compatibility review.

## Rule 7 — Agent Contracts SHALL govern AI

AI agents shall not operate through prompts alone.

## Rule 8 — Workflow Contracts SHALL not become product workflows

Workflow Contract defines execution structure.

Products deliver workflow experience.

## Rule 9 — Consumption Contracts SHALL prevent product redefinition

Products may specialize experience.

They shall not redefine Core semantics.

## Rule 10 — Codex SHALL implement contracts from approved specs

Codex shall not invent contract meaning.

---

# 46. Specification Output

This chapter produces the following specification output:

- Core Contract definition;
- Core Contract exclusions;
- six contract categories;
- Data Contract architecture;
- API Contract architecture;
- Event Contract architecture;
- Agent Contract architecture;
- Workflow Contract architecture;
- Consumption Contract architecture;
- contract ownership rules;
- provider and consumer rules;
- input and output rules;
- permission and policy rules;
- versioning and compatibility rules;
- validation and failure behavior rules;
- auditability rules;
- domain, object, service, event, AI, workflow and product relationships;
- contract specification structures;
- inclusion and exclusion tests;
- naming and boundary rules;
- extension and versioning rules;
- review questions;
- anti-patterns;
- baseline contract inventory;
- MVP contract priority;
- Codex implementation rules.

These outputs complete Part II of Book 02.

---

# 47. Execution Mapping

This chapter directly governs contract execution assets.

| Contract Type | Execution Mapping |
|---------------|------------------|
| Data Contract | schemas, validation, data quality, field meaning, sensitivity |
| API Contract | service interfaces, input/output validation, permissions, error behavior |
| Event Contract | event schema, event store, event publishing, event consumers |
| Agent Contract | AI agent permissions, knowledge access, tools, risk and review |
| Workflow Contract | workflow states, transitions, tasks, events and review requirements |
| Consumption Contract | product integration rules, allowed extensions, prohibited redefinitions |
| Versioning | compatibility checks, migration, deprecation |
| Validation | tests, runtime checks, contract linting |
| Audit | access logs, event logs, review records, contract usage records |

Implementation shall preserve Core contract meaning, governance and compatibility.

---

# 48. Relationship to core-specs/

This chapter governs:

```text
core-specs/contracts/
core-specs/api/
core-specs/events/
core-specs/agents/
core-specs/workflows/
```

Every detailed contract specification shall identify:

- contract type;
- owning domain;
- provider;
- consumers;
- Core assets exposed;
- permission and policy;
- version;
- validation;
- failure behavior;
- audit rule;
- acceptance criteria.

No API, Event, Agent, Workflow or Product Consumption implementation shall be accepted without reference to its relevant contract specification or explicit architecture approval.

---

# 49. Exclusions

This chapter shall not include:

- full OpenAPI files;
- complete event payload catalog;
- complete AI prompt library;
- commercial legal agreements;
- product pricing terms;
- product PRDs;
- UI design;
- vendor integration SDK details;
- deployment topology;
- implementation code.

These belong elsewhere.

---

# 50. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines Core Contract clearly.
- It distinguishes Core Contracts from commercial contracts, UI rules, schemas, logs and prompts.
- It defines six contract categories.
- It explains Data, API, Event, Agent, Workflow and Consumption Contracts.
- It defines contract ownership, provider and consumer.
- It defines permission, policy, versioning, validation, failure and audit rules.
- It maps contracts to domains, objects, services, events, AI, workflow and products.
- It provides contract specification structures.
- It defines inclusion, exclusion, naming, boundary, extension and versioning rules.
- It provides review questions and anti-patterns.
- It supports MVP contract sequencing.
- It guides Codex implementation.
- It completes Part II.
- It supports Book 02 TOC v1.2.

---

# 51. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 17, defining Core Contract Architecture and contract governance rules. |

---

**End of Chapter**
