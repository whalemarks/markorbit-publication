# Book 02

# 16 — Core Execution Primitives

**Subtitle:** Events, Tasks, State, Context and Workflow Contracts

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-16

**Chapter Title:** Core Execution Primitives

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

This chapter defines the Core Execution Primitives of MarkOrbit.

Chapter 13 defined Core Domains.

Chapter 14 defined Core Objects.

Chapter 15 defined Core Services.

This chapter defines the primitives that allow Core Objects and Core Services to participate in traceable execution.

A professional operating system cannot rely only on data and services.

Professional work moves.

It changes state.

It creates responsibility.

It triggers follow-up.

It requires review.

It coordinates people, systems, products, AI agents and external service providers.

It must remember what happened and why.

Core Execution Primitives make this possible.

The main execution primitives are:

```text
Events
Tasks
State
Context
Workflow Contracts
```

These primitives are not product workflows.

They are not UI flows.

They are not operational SOPs.

They are the shared execution foundation that Workplace and products consume.

The purpose of this chapter is to define how execution becomes visible, traceable, governable and interoperable without moving workflow operation into the Core.

---

# 2. Core Question

This chapter answers one question:

> What execution primitives must the MarkOrbit Core provide so that professional work can be coordinated without making the Core responsible for product workflow execution?

The answer is:

> The Core shall provide Events, Tasks, State, Context and Workflow Contracts as governed execution primitives, while Workplace operates workflows and products deliver workflow experience.

The boundary is:

```text
Core
    provides execution primitives and workflow contracts

Workplace
    operates professional work and workflow composition

Products
    deliver workflow experience and user-facing interaction
```

This boundary is mandatory.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- Core Execution Primitive definition;
- Event Primitive;
- Task Primitive;
- State Primitive;
- Context Primitive;
- Workflow Contract;
- Notification relationship;
- execution responsibility;
- execution boundary;
- relationship to Core Domains, Objects and Services;
- relationship to Workplace;
- relationship to Products;
- relationship to AI;
- relationship to `core-specs/`;
- execution specification structures;
- inclusion and exclusion rules;
- review questions;
- anti-patterns;
- MVP execution priority;
- Codex implementation rules.

## 3.2 Out of Scope

This chapter does not define:

- full product workflow implementation;
- Workplace UI;
- task board design;
- workflow engine runtime;
- all event payloads;
- all task schemas;
- product-specific notification screens;
- operational SOPs;
- detailed API endpoints;
- deployment architecture;
- vendor-specific implementation;
- production AI prompts.

Detailed executable specifications belong in:

```text
core-specs/events/
core-specs/workflows/
core-specs/services/
core-specs/api/
core-specs/agents/
core-specs/contracts/
```

---

# 4. Core Execution Primitive Definition

A Core Execution Primitive is:

> a shared, governed and reusable execution structure that allows Core work to become observable, stateful, assignable, contextual, contract-based and interoperable.

This definition contains six parts.

## 4.1 Shared

The primitive is not product-specific.

It may be consumed by multiple products, Workplaces, services or AI agents.

## 4.2 Governed

The primitive must respect identity, permission, policy, audit and responsibility rules.

## 4.3 Reusable

The primitive should support repeated patterns of professional execution.

## 4.4 Observable

Execution should not be hidden inside product code.

Important changes should be visible.

## 4.5 Stateful

Professional work has status, lifecycle and transitions.

## 4.6 Interoperable

Work should coordinate across products, services, agents and Workplaces through contracts.

---

# 5. Execution Primitive Overview

Book 02 defines five primary Core Execution Primitives.

```text
1. Event
2. Task
3. State
4. Context
5. Workflow Contract
```

A related structure, Notification, is also discussed because it depends on Events and Tasks.

The relationship is:

```text
Context
    provides the execution situation

State
    defines current lifecycle condition

Event
    records meaningful change

Task
    assigns responsibility for action

Workflow Contract
    defines allowed coordination structure

Notification
    delivers execution awareness
```

Together, these primitives make professional execution traceable.

---

# 6. What Core Execution Primitives Are Not

Core Execution Primitives are not:

- product workflow screens;
- task board UI;
- kanban columns;
- product wizard steps;
- operational SOPs;
- human management rules;
- full workflow engine implementation;
- deployment queues;
- background job scripts;
- one-product-only status fields;
- AI prompt sequences;
- chat messages alone.

For example:

- `Task` may be a Core Execution Primitive.
- `MarkReg Task Board` is a product or Workplace view.
- `MatterCreated` may be a Core Event.
- `Activity Feed Row` is product UI.
- `Workflow Contract` may be Core.
- `Lite Filing Wizard` is product experience.
- `State` may be Core.
- `Step 3 highlighted in UI` is product presentation.

---

# 7. Primitive 1 — Event

## 7.1 Definition

An Event is:

> a record of meaningful change that occurred in the Core and may be used for audit, coordination, automation, notification, AI monitoring or product synchronization.

Events answer:

> What happened?

Events make change visible.

They are the memory of execution.

## 7.2 Event Responsibility

Events are responsible for:

- recording meaningful change;
- preserving source and time;
- identifying related objects;
- supporting audit;
- triggering downstream coordination;
- enabling notification;
- enabling automation;
- supporting AI monitoring;
- synchronizing products.

## 7.3 Event Examples

Examples include:

```text
IdentityLinked
KnowledgeSourceValidated
TrademarkStatusChanged
DocumentUploaded
EvidencePackageCreated
MatterCreated
MatterStatusChanged
MatterOwnerAssigned
OrderPaid
OrderConvertedToMatter
OpportunityCreated
TaskAssigned
TaskCompleted
RoutingDecisionMade
AgentReplyReceived
NotificationDelivered
AIDraftGenerated
AIRecommendationReviewRequired
```

## 7.4 Event Is Not a Log Line

An Event is not an unstructured log line.

A log may describe system behavior.

An Event represents meaningful domain change.

Events should be typed, structured and owned.

## 7.5 Event Ownership

Every Event shall have:

- source domain;
- event name;
- event meaning;
- triggering action;
- related Core Object;
- timestamp;
- actor or system source;
- payload contract;
- consumers;
- audit rule.

Example:

```text
Event:
    MatterCreated

Source Domain:
    Matter

Related Object:
    Matter

Triggered By:
    Matter Creation Service or Order-to-Matter Conversion Service

Consumers:
    Task Service, Notification Service, Workplace, MarkReg
```

---

# 8. Event Naming

Event names should be stable and semantic.

Recommended pattern:

```text
Noun + Past Tense Verb
```

Examples:

```text
MatterCreated
TaskAssigned
DocumentUploaded
TrademarkStatusChanged
OrderConvertedToMatter
RoutingDecisionMade
```

Avoid product-specific names.

Incorrect:

```text
MarkRegButtonClicked
LiteWizardStepFinished
DashboardRowUpdated
EmailCardOpened
```

Events should describe Core meaning, not UI behavior.

---

# 9. Event Payload

An Event payload should include only what is needed for consumption, coordination and audit.

Typical payload fields may include:

- event ID;
- event type;
- source domain;
- source service;
- related object ID;
- related object type;
- actor identity;
- organization context;
- timestamp;
- previous state where relevant;
- new state where relevant;
- reason or trigger;
- correlation ID;
- causation ID;
- risk level where relevant;
- review requirement where relevant;
- payload version.

Events should not expose sensitive data unnecessarily.

Payload design belongs to:

```text
core-specs/events/
```

---

# 10. Event Consumption

Events may be consumed by:

- Core Services;
- Workflow Contracts;
- Task Service;
- Notification Service;
- AI monitoring agents;
- audit systems;
- product dashboards;
- Workplace views;
- opportunity detection services;
- external integrations where authorized.

Consumers shall not reinterpret Event meaning.

They consume Event Contracts.

---

# 11. Primitive 2 — Task

## 11.1 Definition

A Task is:

> an assignable unit of responsibility that requires action, review, follow-up, confirmation or completion within a professional execution context.

Tasks answer:

> Who needs to do what, by when, and under what context?

Tasks make responsibility visible.

## 11.2 Task Responsibility

Tasks are responsible for:

- assigning work;
- linking work to Core Objects;
- tracking status;
- supporting deadline and priority;
- preserving accountability;
- triggering notifications;
- enabling workflow operation;
- supporting human review;
- coordinating human and AI work.

## 11.3 Task Examples

Examples include:

```text
Review AI classification recommendation
Request signed POA
Upload evidence
Check agent reply
Prepare filing documents
Approve office action response draft
Confirm order conversion
Review routing decision
Send client status update
Validate imported trademark data
```

## 11.4 Task Is Not a To-Do Widget

A Task is not merely a UI checklist item.

A product may display tasks as a checklist, board or timeline.

The Core Task represents responsibility and execution context.

## 11.5 Task Ownership

Every Task shall have:

- task ID;
- source domain or service;
- related Core Object;
- task type;
- task title;
- assignee;
- responsible owner;
- status;
- priority;
- due date where relevant;
- context;
- required action;
- completion condition;
- event triggers;
- audit rule.

---

# 12. Task Lifecycle

A Core Task should have a lifecycle.

Baseline lifecycle:

```text
Created
Assigned
In Progress
Blocked
Completed
Cancelled
```

Additional states may be added by Task specification or Workflow Contract.

Task lifecycle should not be defined by product UI alone.

Task state changes should emit events where meaningful:

```text
TaskAssigned
TaskStarted
TaskBlocked
TaskCompleted
TaskCancelled
```

---

# 13. Task Assignment

Task assignment defines responsibility.

A Task may be assigned to:

- user;
- role;
- team;
- organization;
- agent;
- service provider;
- AI agent under governance;
- review authority;
- system queue.

Assignment should identify:

- assignee;
- assigning actor;
- assignment reason;
- due date;
- responsibility owner;
- review requirement;
- escalation rule where applicable.

Assignment is not only operational convenience.

It is part of professional accountability.

---

# 14. Primitive 3 — State

## 14.1 Definition

State is:

> the current lifecycle condition of a Core Object, Task, Workflow Contract or execution process.

State answers:

> What condition is this thing currently in?

State makes lifecycle visible and governable.

## 14.2 State Responsibility

State is responsible for:

- expressing lifecycle condition;
- enabling valid transitions;
- supporting status visibility;
- triggering events;
- enabling workflow contracts;
- supporting audit;
- enabling product status display;
- supporting AI and automation context.

## 14.3 State Examples

Examples include:

```text
Matter Status:
    Draft
    Active
    Waiting for Client
    Waiting for Agent
    Under Review
    Completed
    Closed

Order Status:
    Created
    Quoted
    Confirmed
    Paid
    Converted to Matter
    Cancelled

Document Status:
    Requested
    Uploaded
    Verified
    Rejected
    Submitted

Task Status:
    Created
    Assigned
    In Progress
    Blocked
    Completed
```

## 14.4 State Is Not Product Label

A product may display a state label differently.

But Core State meaning must remain stable.

For example, a product may display `Waiting for Agent` as “代理处理中”.

But the underlying state meaning remains Core.

## 14.5 State Transitions

State should change through governed transitions.

A transition should define:

- source state;
- target state;
- allowed trigger;
- required permission;
- required context;
- required service;
- event emitted;
- audit requirement;
- review requirement where applicable.

State should not be mutated informally by product UI or direct database update.

---

# 15. Primitive 4 — Context

## 15.1 Definition

Context is:

> the structured execution situation required to interpret, authorize, perform or review an action.

Context answers:

> Under what situation is this action or decision being made?

Context prevents services, tasks, AI agents and workflows from acting blindly.

## 15.2 Context Responsibility

Context is responsible for carrying:

- actor identity;
- organization context;
- customer context;
- matter context;
- jurisdiction context;
- trademark context;
- document context;
- knowledge context;
- permission context;
- product context;
- workflow context;
- AI context;
- risk context;
- time context;
- source context.

## 15.3 Context Examples

Examples:

```text
A classification recommendation context:
    User
    Customer
    Brand
    Trademark
    Jurisdiction
    Goods/Services text
    Knowledge source
    Product consumer
    Risk level
    Review requirement

A routing decision context:
    Matter
    Jurisdiction
    Service type
    Agent capability
    Service provider coverage
    Policy
    Business responsibility
    Communication history
```

## 15.4 Context Is Not Prompt Text

Context may be used by AI prompts.

But Context is not a prompt.

Context is structured Core information.

AI prompts may consume Context under Agent Contracts.

They do not define Context.

## 15.5 Context Quality

Context should indicate quality where relevant:

- complete;
- incomplete;
- stale;
- inferred;
- AI-extracted;
- human-verified;
- official-source-based;
- conflicting;
- review-required.

Context quality affects service output and AI confidence.

---

# 16. Primitive 5 — Workflow Contract

## 16.1 Definition

A Workflow Contract is:

> a Core-defined execution contract that specifies allowed states, transitions, required tasks, events, permissions and review conditions for a reusable work pattern.

Workflow Contract answers:

> What execution structure may Workplace and products rely on?

A Workflow Contract is not workflow execution.

It defines the contract for workflow execution.

## 16.2 Workflow Contract Responsibility

Workflow Contracts are responsible for:

- defining reusable work pattern structure;
- defining allowed states;
- defining allowed transitions;
- defining required tasks;
- defining event triggers;
- defining permission requirements;
- defining review requirements;
- defining product consumption boundaries;
- preserving interoperability across products and Workplaces.

## 16.3 Workflow Contract Examples

Examples include:

```text
Trademark Filing Matter Workflow Contract
Office Action Response Workflow Contract
Trademark Renewal Workflow Contract
Document Review Workflow Contract
Evidence Review Workflow Contract
Agent Routing Workflow Contract
Order-to-Matter Conversion Workflow Contract
AI Recommendation Review Workflow Contract
```

## 16.4 Workflow Contract Is Not Workflow UI

A Workflow Contract does not define:

- screen layout;
- wizard steps;
- product copy;
- task board columns;
- daily operation procedure;
- team management style.

Those belong to Workplace or products.

## 16.5 Workflow Contract Elements

A Workflow Contract may define:

- contract ID;
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
- human review requirements;
- notification rules;
- product consumption rules;
- version;
- acceptance criteria.

Detailed specifications belong to:

```text
core-specs/workflows/
```

---

# 17. Notification Relationship

Notification is closely related to execution primitives.

A Notification is:

> a delivered awareness signal triggered by an Event, Task, State change, deadline, policy rule or workflow condition.

Notification answers:

> Who needs to know something?

Notification is not the same as Event.

Event records what happened.

Notification delivers awareness.

Notification may be triggered by:

- Event;
- Task;
- State change;
- deadline;
- policy rule;
- workflow condition;
- AI review requirement;
- communication update.

Notification belongs to the Notification Domain and consumes Events and Tasks.

---

# 18. Execution Primitive Relationships

Execution primitives are connected.

```text
Context
    informs
Service Action

Service Action
    changes
State

State Change
    emits
Event

Event
    may create
Task

Task
    may trigger
Notification

Workflow Contract
    governs
allowed states, tasks, events and transitions
```

Another view:

```text
Workflow Contract
    defines execution structure

Context
    provides situation

Task
    assigns responsibility

State
    shows lifecycle condition

Event
    records meaningful change

Notification
    delivers awareness
```

These primitives should be designed as a system.

---

# 19. Execution Boundary with Workplace

The Core / Workplace boundary is critical.

```text
Core
    defines execution primitives and workflow contracts

Workplace
    operates workflow execution and work composition
```

Book 02 may define:

- Event structure;
- Task structure;
- State structure;
- Context structure;
- Workflow Contract structure;
- Notification Contract structure.

Book 03 may define:

- Workspace;
- work views;
- task board;
- workflow operation;
- collaboration surfaces;
- human-AI co-working experience;
- operational composition.

Products may define:

- product-specific workflow experience;
- forms;
- dashboards;
- status displays;
- user journeys.

This boundary prevents Book 02 from becoming an operations manual.

---

# 20. Execution Boundary with Products

Products consume execution primitives.

A product may:

- display tasks;
- show events;
- display state;
- provide workflow interactions;
- request service execution;
- surface notifications;
- invoke AI-assisted execution;
- show context-specific next steps.

A product shall not:

- redefine Event meaning;
- redefine Task responsibility;
- mutate State outside allowed transitions;
- redefine Workflow Contract;
- hide meaningful changes from Events;
- bypass permission and policy;
- treat UI steps as Core workflow contract.

Products deliver experience.

Core defines execution meaning.

---

# 21. Execution Boundary with AI

AI may assist execution.

AI may:

- summarize events;
- recommend tasks;
- draft communication;
- analyze evidence;
- recommend classification;
- identify opportunity;
- suggest routing;
- detect context gaps;
- generate review notes.

AI shall not:

- own professional responsibility;
- define Workflow Contracts;
- mutate critical State silently;
- create high-risk Tasks without authorization;
- emit authoritative Events without governed service;
- bypass human review;
- operate without Context;
- use unauthorized Knowledge.

AI-assisted execution must be governed through Agent Contracts and Core Services.

---

# 22. Execution Boundary with Implementation

Implementation realizes execution primitives.

Implementation may include:

- event store;
- task tables;
- state fields;
- context objects;
- workflow contract records;
- notification infrastructure;
- queues;
- background jobs;
- event handlers.

But implementation does not define primitive meaning.

Meaning is defined by Book 02 and `core-specs/`.

For example:

- a queue system may deliver events;
- it does not define what `MatterCreated` means;
- a task table may store task records;
- it does not define professional responsibility by itself.

---

# 23. Event Specification Structure

Every detailed Event specification shall follow a standard structure.

```text
# Event Name

1. Event Purpose
2. Source Domain
3. Event Type
4. Trigger
5. Related Core Objects
6. Actor / Source
7. Payload Contract
8. Previous State / New State
9. Context Requirements
10. Permission and Policy Requirements
11. Events Consumed or Caused By
12. Downstream Consumers
13. Notification Rules
14. AI Usage
15. Audit Requirements
16. Retention Rules
17. Version
18. Acceptance Criteria
19. Revision Notes
```

This structure belongs to:

```text
core-specs/events/
```

---

# 24. Task Specification Structure

Every detailed Task specification shall follow a standard structure.

```text
# Task Type

1. Task Purpose
2. Source Domain
3. Related Core Objects
4. Task Category
5. Creation Trigger
6. Assignee Rules
7. Responsibility Owner
8. Required Context
9. Status Lifecycle
10. Completion Criteria
11. Permission and Policy Requirements
12. Events Published
13. Notification Rules
14. AI Usage
15. Human Review Requirements
16. Escalation Rules
17. Audit Requirements
18. Product Consumers
19. Acceptance Criteria
20. Revision Notes
```

This structure belongs to:

```text
core-specs/workflows/
core-specs/tasks/
```

If the repository does not use `core-specs/tasks/`, Task specifications may be placed under `core-specs/workflows/` or `core-specs/events/` depending on implementation organization.

---

# 25. State Specification Structure

Every detailed State specification shall follow a standard structure.

```text
# State Model Name

1. State Model Purpose
2. Owning Domain
3. Related Core Object
4. State List
5. State Meaning
6. Allowed Transitions
7. Transition Triggers
8. Required Permissions
9. Required Context
10. Events Published
11. Review Requirements
12. Product Display Rules
13. AI Usage
14. Audit Requirements
15. Version
16. Acceptance Criteria
17. Revision Notes
```

This structure belongs to:

```text
core-specs/workflows/
core-specs/objects/
```

depending on whether the state is workflow-level or object-level.

---

# 26. Context Specification Structure

Every detailed Context specification shall follow a standard structure.

```text
# Context Name

1. Context Purpose
2. Owning Domain
3. Related Core Objects
4. Required Context Fields
5. Optional Context Fields
6. Context Source
7. Context Quality Rules
8. Permission and Policy Rules
9. Knowledge Dependencies
10. AI Usage
11. Event Relationships
12. Task Relationships
13. Product Consumers
14. Validation Rules
15. Acceptance Criteria
16. Revision Notes
```

This structure belongs to:

```text
core-specs/workflows/
core-specs/services/
core-specs/agents/
```

depending on consumption.

---

# 27. Workflow Contract Specification Structure

Every detailed Workflow Contract specification shall follow a standard structure.

```text
# Workflow Contract Name

1. Contract Purpose
2. Owning Domain
3. Related Core Objects
4. Workflow Type
5. In Scope
6. Out of Scope
7. States
8. Transitions
9. Required Tasks
10. Optional Tasks
11. Events Published
12. Events Consumed
13. Services Used
14. Context Requirements
15. Permission and Policy Requirements
16. AI Usage
17. Human Review Requirements
18. Notification Rules
19. Product Consumers
20. Workplace Consumption
21. Failure and Escalation Rules
22. Version
23. Acceptance Criteria
24. Revision Notes
```

This structure belongs to:

```text
core-specs/workflows/
```

---

# 28. Execution Inclusion Test

A concept may become a Core Execution Primitive or execution specification only if it satisfies most of the following conditions:

1. It supports traceable professional execution.
2. It is reusable across products, Workplaces, services or AI agents.
3. It involves meaningful state, responsibility, change, context or coordination.
4. It relates to Core Objects or Core Services.
5. It may require permission, policy, audit or review.
6. It may produce or consume Events.
7. It may be represented as a Task, State, Context or Workflow Contract.
8. Fragmentation would occur if each product defined it separately.
9. It supports the Professional Value Flow.
10. It can be specified in `core-specs/`.

If a concept fails this test, it may belong to product workflow, Workplace operation or implementation.

---

# 29. Execution Exclusion Test

A concept shall be excluded from Core Execution Primitive status if it is primarily:

- product UI flow;
- screen step;
- task board column;
- internal team SOP;
- product onboarding sequence;
- one-product-only status label;
- background job script;
- queue configuration;
- prompt sequence;
- chat conversation style;
- report activity row;
- sales follow-up script.

Excluded execution concepts may still be useful.

They should be placed in Book 03, product documents, operations documents or implementation files.

---

# 30. Execution Naming Rules

Execution primitives shall use stable semantic names.

## 30.1 Event Names

Use domain meaning and past tense.

Correct:

```text
MatterCreated
TaskAssigned
DocumentUploaded
RoutingDecisionMade
```

Incorrect:

```text
ButtonClicked
PageSubmitted
Step3Finished
CardOpened
```

## 30.2 Task Names

Use responsibility-oriented names.

Correct:

```text
Review AI Recommendation
Request POA
Verify Document
Follow Up Agent Reply
```

Incorrect:

```text
Click Next
Open Popup
Check Blue Badge
```

## 30.3 State Names

Use lifecycle meaning.

Correct:

```text
Waiting for Agent
Under Review
Completed
Blocked
```

Incorrect:

```text
Yellow Label
Tab 2
Hidden Status
```

## 30.4 Workflow Contract Names

Use reusable professional workflow names.

Correct:

```text
Trademark Filing Matter Workflow Contract
AI Recommendation Review Workflow Contract
```

Incorrect:

```text
Lite Wizard Flow
MarkReg Screen Sequence
```

---

# 31. Execution Review Questions

When reviewing an execution primitive or specification, reviewers shall ask:

1. What execution responsibility does this concept carry?
2. Is it an Event, Task, State, Context, Workflow Contract or Notification?
3. Which Core Domain owns it?
4. Which Core Objects are involved?
5. Which Core Services trigger or consume it?
6. Which permissions and policies apply?
7. Which Business Responsibility is involved?
8. What AI usage is allowed or prohibited?
9. What human review is required?
10. What Events are published or consumed?
11. Which products or Workplaces consume it?
12. Does it preserve the Core / Workplace / Product boundary?
13. Is it too product-specific?
14. Can Codex implement it from approved specifications?

---

# 32. Execution Anti-Patterns

## 32.1 Workflow UI as Core Contract

A product wizard is treated as a Workflow Contract.

Correction:

```text
The wizard is product experience.
The Workflow Contract defines reusable states, tasks and events.
```

## 32.2 Event as Log Line

Events are used as unstructured logs.

Correction:

```text
Events must represent meaningful domain change.
```

## 32.3 Task as UI Checklist

A product checklist item is treated as Core Task.

Correction:

```text
Core Task represents responsibility.
UI checklist displays task or product-specific steps.
```

## 32.4 State as Display Label

A product status label becomes Core State.

Correction:

```text
Core State defines lifecycle meaning.
Products may translate or display it differently.
```

## 32.5 Context as Prompt Text

AI prompt content is treated as execution context.

Correction:

```text
Context is structured Core information.
Prompts may consume Context.
```

## 32.6 Hidden Execution

Services update objects without events, tasks or audit.

Correction:

```text
Meaningful changes must be observable.
```

## 32.7 AI Executes Without Review

AI changes professional state or produces final advice without human review.

Correction:

```text
AI execution must follow governance, risk and review rules.
```

---

# 33. Baseline Execution Primitive Inventory

The initial execution primitive inventory includes:

```text
Events
    IdentityLinked
    KnowledgeSourceValidated
    TrademarkStatusChanged
    DocumentUploaded
    EvidencePackageCreated
    MatterCreated
    MatterStatusChanged
    MatterOwnerAssigned
    OrderPaid
    OrderConvertedToMatter
    OpportunityCreated
    TaskAssigned
    TaskCompleted
    RoutingDecisionMade
    AgentReplyReceived
    AIDraftGenerated
    AIRecommendationReviewRequired

Tasks
    Review AI Recommendation
    Request POA
    Verify Document
    Prepare Filing Documents
    Follow Up Agent Reply
    Approve Draft
    Assign Agent
    Review Evidence Package
    Convert Order to Matter
    Send Client Status Update

State Models
    Matter State
    Order State
    Document State
    Task State
    Opportunity State
    Routing Decision State

Contexts
    User Context
    Customer Context
    Matter Context
    Trademark Context
    Jurisdiction Context
    Classification Context
    Document Context
    AI Execution Context
    Routing Context
    Review Context

Workflow Contracts
    Trademark Filing Matter Workflow Contract
    Office Action Response Workflow Contract
    Renewal Workflow Contract
    Document Review Workflow Contract
    Evidence Review Workflow Contract
    Agent Routing Workflow Contract
    Order-to-Matter Conversion Workflow Contract
    AI Recommendation Review Workflow Contract
```

The full inventory shall be maintained in:

```text
Appendix E — Event Index
core-specs/events/
core-specs/workflows/
```

---

# 34. Execution and MVP Priority

The MVP should implement execution primitives in phases.

```text
Phase 1 — Foundation Execution
    User Context
    Permission Context
    Basic Event Structure
    Basic Audit Structure

Phase 2 — Professional Execution
    Trademark Status Event
    Document Uploaded Event
    Document State
    Classification Recommendation Context

Phase 3 — Business Execution
    Matter State
    Order State
    MatterCreated
    OrderConvertedToMatter
    TaskAssigned
    TaskCompleted
    Basic Workflow Contract

Phase 4 — Growth Execution
    OpportunityCreated
    Notification Dispatch
    EvidencePackageCreated
    RoutingDecisionMade
    AIRecommendationReviewRequired

Phase 5 — Network Execution
    AgentReplyReceived
    Communication Linked
    Service Network Routing Events
    Network Collaboration Context
```

MVP shall preserve execution structure even if only a minimal workflow is implemented.

---

# 35. Execution and Codex

Codex tasks shall implement execution primitives from approved specifications.

A Codex execution task should include:

- primitive type;
- name;
- owning domain;
- related objects;
- related services;
- event or task schema;
- state model;
- context requirements;
- workflow contract;
- permissions and policies;
- AI usage;
- human review;
- product consumers;
- tests;
- acceptance criteria;
- prohibited overreach.

Codex shall not invent workflow behavior from product prompts without Core or Workplace specification.

---

# 36. Core Execution Primitive Rules

The following rules are established by this chapter.

## Rule 1 — Core SHALL provide execution primitives

Events, Tasks, State, Context and Workflow Contracts belong to Core as primitives and contracts.

## Rule 2 — Core SHALL NOT own workflow execution

Workflow operation belongs to Workplace.

Workflow experience belongs to products.

## Rule 3 — Meaningful change SHOULD produce Events

Important lifecycle, responsibility, status, review, AI or routing changes should be observable.

## Rule 4 — Tasks SHALL represent responsibility

Tasks are not merely UI checklist items.

## Rule 5 — State SHALL be governed

State changes should occur through allowed transitions, services or workflow contracts.

## Rule 6 — Context SHALL be structured

Context is not prompt text or hidden product state.

## Rule 7 — Workflow Contracts SHALL define reusable execution structure

Workflow Contract is not product workflow UI.

## Rule 8 — AI execution SHALL be governed

AI must use authorized context, knowledge, permission and human review where required.

## Rule 9 — Products SHALL consume execution primitives through contracts

Products shall not redefine Event, Task, State or Workflow Contract meanings.

## Rule 10 — Execution changes SHALL be traceable

Important execution changes require event, audit or task trace.

---

# 37. Specification Output

This chapter produces the following specification output:

- Core Execution Primitive definition;
- Event Primitive definition;
- Task Primitive definition;
- State Primitive definition;
- Context Primitive definition;
- Workflow Contract definition;
- Notification relationship;
- execution primitive relationships;
- Core / Workplace / Product boundary rules;
- AI execution boundary;
- Event specification structure;
- Task specification structure;
- State specification structure;
- Context specification structure;
- Workflow Contract specification structure;
- inclusion and exclusion tests;
- naming rules;
- review questions;
- anti-patterns;
- baseline execution primitive inventory;
- MVP execution priority;
- Codex implementation rules.

These outputs guide Chapter 17 and Part III.

---

# 38. Execution Mapping

This chapter directly governs execution asset creation.

| Execution Primitive | Execution Mapping |
|--------------------|------------------|
| Event | event specs, event store, event publishing, event contracts |
| Task | task specs, task model, assignment, task lifecycle |
| State | state models, transition rules, status fields, state events |
| Context | execution context models, service context, AI context |
| Workflow Contract | workflow specs, state machines, task/event relationships |
| Notification | notification triggers, delivery rules, product surfaces |
| AI Execution | agent contracts, review tasks, audit events |
| Product Consumption | workflow views, task boards, status pages, dashboards |

Implementation shall preserve Core execution meanings and boundaries.

---

# 39. Relationship to core-specs/

This chapter governs the following specification folders:

```text
core-specs/events/
core-specs/workflows/
core-specs/services/
core-specs/agents/
core-specs/api/
core-specs/contracts/
```

Every Event spec shall identify source domain and payload contract.

Every Task spec shall identify responsibility and context.

Every State spec shall identify allowed transitions.

Every Context spec shall identify required structured fields.

Every Workflow Contract spec shall identify states, transitions, tasks, events, permissions and product consumers.

No product document shall override Core execution primitive meaning.

No implementation task shall create workflow behavior that violates the Core / Workplace / Product boundary.

---

# 40. Exclusions

This chapter shall not include:

- product workflow UI;
- task board design;
- Workplace interface;
- operational SOPs;
- full workflow engine implementation;
- event infrastructure vendor choice;
- queue topology;
- all event payloads;
- all task schemas;
- API endpoint definitions;
- production prompts;
- deployment architecture.

These belong elsewhere.

---

# 41. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines Core Execution Primitives clearly.
- It defines Events, Tasks, State, Context and Workflow Contracts.
- It distinguishes primitives from product workflow, UI and SOPs.
- It preserves the Core / Workplace / Product boundary.
- It explains how execution primitives relate to domains, objects and services.
- It defines AI execution governance boundaries.
- It provides specification structures for events, tasks, state, context and workflow contracts.
- It defines inclusion, exclusion, naming, review and anti-pattern rules.
- It supports MVP execution sequencing.
- It guides Codex implementation.
- It supports Book 02 TOC v1.2.

---

# 42. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 16, defining Core Execution Primitives: Events, Tasks, State, Context and Workflow Contracts. |

---

**End of Chapter**
