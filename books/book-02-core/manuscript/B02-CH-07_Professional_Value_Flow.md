# Book 02

# 07 — Professional Value Flow

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-07

**Chapter Title:** Professional Value Flow

**Part:** Part I — Core Foundation

**Chapter Type:** Foundation

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

This chapter defines the Professional Value Flow of the MarkOrbit Core.

Chapter 06 explained how the Professional Operating System becomes the Core Kernel.

This chapter focuses on the value flow that the Core must support.

Professional service work does not begin with software functions.

It begins with reality.

A client has a brand.

A trademark exists or needs to be filed.

A jurisdiction has rules.

A document is required.

An office action is issued.

A foreign agent replies.

A deadline approaches.

A business opportunity appears.

A professional must understand the situation, make judgment, take action, coordinate with others and deliver an experience that clients can trust.

Book 01 described this as a professional value flow:

```text
Reality
        ↓
Facts
        ↓
Understanding
        ↓
Judgment
        ↓
Action
        ↓
Coordination
        ↓
Experience
```

Book 02 must make this flow executable.

This chapter defines how the MarkOrbit Core supports each stage of the flow.

---

# 2. Core Question

This chapter answers one question:

> How does professional value flow through the MarkOrbit Core?

The answer is:

> Professional value flows from reality into Core Objects, from Core Objects into facts, from facts into knowledge-based understanding, from understanding into governed judgment, from judgment into Core Services, from services into coordination, and from coordination into Workplace and product experience.

The Core is not merely a data system.

The Core is the structure through which professional value becomes reusable, traceable and executable.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- the Professional Value Flow;
- the meaning of each stage in the flow;
- how each stage maps to Core architecture;
- how value flow connects Core Objects, Knowledge, AI, Services, Events and Consumption;
- how value flow prevents MarkOrbit from becoming only a CRM, workflow tool or AI application;
- how value flow guides domain, object, service, event and AI specification.

## 3.2 Out of Scope

This chapter does not define:

- detailed product journeys;
- detailed workflow execution;
- UI screens;
- database schemas;
- API endpoints;
- AI prompt templates;
- product pricing;
- operational SOPs;
- deployment details.

Those belong to later chapters, `core-specs/`, product publications or implementation documents.

---

# 4. Professional Value Flow Definition

The Professional Value Flow is defined as follows:

> Professional Value Flow is the structured transformation from external reality into trusted professional experience through facts, understanding, judgment, action and coordination.

The flow is:

```text
Reality
        ↓
Facts
        ↓
Understanding
        ↓
Judgment
        ↓
Action
        ↓
Coordination
        ↓
Experience
```

This flow is not a simple workflow.

It is not a sequence of UI steps.

It is the underlying logic of professional service work.

A workflow may implement part of this flow.

A product may present part of this flow.

An AI agent may assist part of this flow.

But the flow itself belongs to the Professional Operating System and must be supported by the Core.

---

# 5. Why Value Flow Matters

Professional service value is not created by storing information alone.

It is created when information is transformed into professional action.

For example, knowing that a trademark office issued an office action is only a fact.

The value appears when the system helps answer:

- What does this office action mean?
- Which rule or citation is involved?
- What deadline applies?
- What documents are needed?
- Which agent or attorney should handle it?
- What should be explained to the client?
- What action should be taken next?
- Who is responsible?
- What event should be recorded?
- What risk should be monitored?

The Core must support this transformation.

If the Core only stores data, it becomes a database.

If the Core only runs tasks, it becomes a workflow tool.

If the Core only generates text, it becomes an AI assistant.

The MarkOrbit Core must support the entire value flow.

---

# 6. High-Level Mapping

The Professional Value Flow maps to Core architecture as follows:

```text
Reality
        ↓
Core Objects

Facts
        ↓
Data, Records and Events

Understanding
        ↓
Knowledge Model and Knowledge Services

Judgment
        ↓
Rules, Policies, AI Capability and Human Review

Action
        ↓
Core Services and Execution Primitives

Coordination
        ↓
Tasks, Events, Routing, Communication and Workflow Contracts

Experience
        ↓
Workplace and Product Consumption
```

This mapping guides the rest of Book 02.

Every Core Domain, Object, Service, Event and AI Capability should support one or more stages of the value flow.

---

# 7. Stage 1 — Reality

## 7.1 Definition

Reality is what exists or happens outside the system.

Reality includes the real-world entities, relationships, documents, events, deadlines, requests, decisions and communications that professional work must respond to.

Examples include:

- a brand created by a client;
- a trademark that has been filed;
- a trademark application that needs to be prepared;
- a trademark office issuing an office action;
- a customer requesting a quote;
- a foreign agent sending an email;
- a renewal deadline approaching;
- a power of attorney being signed;
- a document being uploaded;
- a payment being received;
- an opposition being filed;
- a business opportunity appearing.

Reality exists whether or not MarkOrbit records it.

The first responsibility of the Core is to represent relevant reality accurately.

## 7.2 Core Responsibility

The Core does not create reality.

The Core represents reality.

Reality enters the Core through:

- Core Objects;
- Data Records;
- Documents;
- Evidence;
- Communication;
- Events;
- User input;
- Integrations;
- AI-assisted extraction;
- Manual review.

The Core must decide which parts of reality require stable representation.

Not every detail becomes a Core Object.

But if a reality must be shared, referenced, audited, linked, executed or consumed by products, it should be represented in the Core.

## 7.3 Example

A client sends an email asking whether a trademark can be filed in the United States and the European Union.

This real-world request may create or update:

- Customer;
- Brand;
- Trademark;
- Jurisdiction;
- Communication;
- Opportunity;
- Order;
- Matter.

The email itself is not the full value.

It is an entry point into the value flow.

---

# 8. Stage 2 — Facts

## 8.1 Definition

Facts are recorded observations about reality.

A fact is something the system can record, reference and verify.

Examples include:

- a customer requested a quote on a certain date;
- a trademark was filed in a jurisdiction;
- a document was received;
- a deadline is due;
- a status changed;
- an agent replied;
- a payment was linked;
- a task was completed;
- an evidence package was uploaded;
- a matter was assigned.

Facts are not yet understanding.

They are recorded signals.

## 8.2 Core Responsibility

The Core turns reality into facts through:

- structured data;
- object records;
- document metadata;
- event logs;
- communication records;
- status records;
- task records;
- audit trails.

Facts must be reliable.

They should have:

- source;
- timestamp;
- related object;
- responsible identity;
- status;
- audit context where necessary.

## 8.3 Fact Quality

Not all recorded information has the same quality.

The Core should distinguish:

- confirmed facts;
- imported data;
- user-submitted data;
- AI-extracted data;
- inferred facts;
- unverified information;
- historical records;
- authoritative records.

This distinction is important because later stages depend on fact quality.

A professional judgment based on unverified facts should be treated differently from one based on confirmed official records.

## 8.4 Example

If an imported trademark record says that a mark is registered, the Core should know:

- where the data came from;
- when it was imported;
- whether it was normalized;
- whether it has been verified;
- which Trademark object it belongs to;
- whether any status event was created.

Facts become valuable when they are structured and traceable.

---

# 9. Stage 3 — Understanding

## 9.1 Definition

Understanding is the interpretation of facts through knowledge.

A fact says what happened.

Understanding explains what it means.

For example:

- a trademark status changed;
- an office action was issued;
- a deadline is approaching;
- a customer requested multiple jurisdictions;
- a class item may be too broad;
- an evidence document may not support claimed goods;
- an agent has not replied for several weeks.

Understanding requires knowledge.

Without knowledge, the system can record facts but cannot explain them.

## 9.2 Core Responsibility

The Core supports understanding through:

- Knowledge Model;
- Knowledge Assets;
- Knowledge Sources;
- Knowledge Relationships;
- Knowledge Validation;
- Knowledge Retrieval Services;
- Jurisdiction Rules;
- Classification Rules;
- Policy Rules;
- Historical Practice;
- AI-assisted interpretation.

Understanding should not depend only on AI language generation.

It should be grounded in authorized knowledge sources.

## 9.3 Knowledge Connection

To support understanding, facts must connect to knowledge.

Examples:

- Trademark status connects to lifecycle knowledge.
- Jurisdiction connects to filing requirements.
- Classification item connects to class rules and local practice.
- Evidence connects to use requirement standards.
- Office action connects to response strategy knowledge.
- Agent response delay connects to service reliability rules.
- Customer portfolio connects to opportunity rules.

The Core must make these connections explicit.

## 9.4 Example

Fact:

> A U.S. trademark registration is approaching a Section 8 deadline.

Understanding:

> The registration requires continued-use declaration or acceptable excusable non-use handling. Evidence may be required. Missing the deadline may affect the registration.

This understanding depends on jurisdiction knowledge, trademark lifecycle knowledge, evidence knowledge and deadline rules.

---

# 10. Stage 4 — Judgment

## 10.1 Definition

Judgment is the professional evaluation of what should be concluded or recommended.

Understanding explains meaning.

Judgment determines what should be done or advised.

Examples include:

- whether a trademark filing strategy is suitable;
- whether goods/services are acceptable;
- whether evidence is sufficient;
- whether an office action can be responded to;
- whether an agent should be selected;
- whether a matter should be escalated;
- whether an opportunity is worth pursuing;
- whether AI output can be trusted;
- whether human review is required.

Judgment is where professional responsibility becomes visible.

## 10.2 Core Responsibility

The Core does not replace professional judgment.

It supports judgment.

The Core supports judgment through:

- structured facts;
- authorized knowledge;
- policies;
- rules;
- risk levels;
- AI Capability;
- recommendation services;
- human review requirements;
- audit records.

The Core should help professionals make better judgments.

It should not silently make high-risk judgments without review.

## 10.3 AI and Judgment

AI may assist judgment.

AI may:

- summarize relevant facts;
- retrieve applicable knowledge;
- compare options;
- generate recommended actions;
- identify risks;
- draft explanations;
- propose routing decisions.

But AI shall not define professional truth.

For high-risk professional actions, human review remains required.

## 10.4 Judgment Traceability

Professional judgment should be traceable where it affects rights, obligations, deadlines, client advice or business responsibility.

Traceability may include:

- who made the judgment;
- what facts were considered;
- what knowledge sources were used;
- what AI assistance was used;
- what risk level applied;
- whether human review occurred;
- what decision was made;
- what action followed.

This traceability supports accountability and learning.

---

# 11. Stage 5 — Action

## 11.1 Definition

Action is the execution of a professional decision or system-supported next step.

Examples include:

- creating a matter;
- generating a quote;
- filing an application;
- requesting documents;
- assigning a task;
- generating a draft;
- sending a notification;
- routing work to an agent;
- creating an order;
- updating a trademark status;
- creating an opportunity;
- closing a matter.

Action turns judgment into execution.

## 11.2 Core Responsibility

The Core supports action through:

- Core Services;
- Execution Primitives;
- Task creation;
- Event publication;
- Workflow Contracts;
- Routing;
- Notification;
- Permission checks;
- Policy evaluation;
- AI-assisted execution.

A Core Service should define:

- input;
- output;
- context;
- permission;
- side effect;
- event;
- failure handling;
- consumer.

This ensures action is not hidden inside product-specific behavior.

## 11.3 Action Quality

A professional action should be:

- authorized;
- contextual;
- traceable;
- reversible where possible;
- audited where necessary;
- connected to objects and events;
- consistent with Core Contracts.

Actions that affect legal rights, deadlines, official filings or client advice require stronger governance.

## 11.4 Example

Judgment:

> The client should file in the U.S. and EU for Classes 9 and 35.

Actions may include:

- create Order;
- create Matter;
- generate quote;
- recommend goods/services;
- request POA;
- assign task;
- route to agent;
- publish MatterCreated and TaskAssigned events.

The Core provides the services and primitives.

Products deliver the user experience.

---

# 12. Stage 6 — Coordination

## 12.1 Definition

Coordination is the organization of action across people, systems, products, agents and time.

Professional service work is rarely individual.

It usually involves:

- client;
- sales;
- process team;
- attorney;
- foreign agent;
- service provider;
- finance;
- AI assistant;
- product system;
- external office;
- deadlines.

Coordination ensures that action is assigned, tracked, communicated and completed.

## 12.2 Core Responsibility

The Core supports coordination through:

- Task;
- Event;
- Notification;
- Routing;
- Communication;
- Workflow Contract;
- Permission;
- Policy;
- Matter Timeline;
- Service Network;
- Agent Matching.

The Core does not own workflow execution.

Workplace operates workflows.

Products deliver coordination experience.

But the Core must provide the primitives and contracts that allow coordination to be consistent across products.

## 12.3 Coordination Risks

Without Core-supported coordination:

- tasks may be missed;
- deadlines may be lost;
- agent replies may be buried in email;
- customers may not receive updates;
- opportunities may not be followed;
- documents may not be linked to matters;
- AI agents may act without context;
- product systems may diverge.

Events, tasks and contracts reduce these risks.

## 12.4 Example

A foreign agent has not replied after receiving original filing documents.

The Core may support:

- Communication record;
- Matter timeline;
- Task escalation;
- Notification;
- Agent reliability update;
- Routing review;
- Event publication.

The product may show this as a warning, dashboard item or follow-up workflow.

The Core provides the coordination foundation.

---

# 13. Stage 7 — Experience

## 13.1 Definition

Experience is how professional value is delivered to users, clients, partners and service providers.

Experience includes:

- clarity;
- confidence;
- guidance;
- status visibility;
- next-step understanding;
- trust;
- reduced complexity;
- timely communication;
- professional consistency.

Experience is delivered through Workplace and products.

But experience depends on the Core.

## 13.2 Core Responsibility

The Core does not define final user experience.

It defines what experience can be built from.

The Core provides:

- shared objects;
- trustworthy facts;
- knowledge-backed understanding;
- governed judgment support;
- reusable services;
- events and tasks;
- workflow contracts;
- consumption rules;
- AI governance.

Products transform these into user experience.

## 13.3 Product Examples

MarkReg may transform Core value into:

- trademark filing dashboard;
- matter status page;
- document checklist;
- agent coordination workflow.

MarkOrbit Lite may transform Core value into:

- guided brand consultation;
- AI-assisted filing recommendation;
- opportunity follow-up;
- simplified order process.

MGSN may transform Core value into:

- agent directory;
- service provider routing;
- network trust display;
- communication workspace.

The product experience differs.

The Core meaning remains shared.

---

# 14. Value Flow Is Not Workflow

Professional Value Flow must not be confused with workflow.

Workflow is an operational arrangement of steps.

Professional Value Flow is the underlying transformation of value.

For example, a trademark filing workflow may include:

- intake;
- class selection;
- document request;
- quote;
- payment;
- filing;
- reporting.

But the value flow underneath includes:

- reality: client needs trademark protection;
- facts: brand, jurisdiction, goods, owner information;
- understanding: filing requirements and classification implications;
- judgment: recommended filing strategy;
- action: order, matter and document generation;
- coordination: tasks, agent routing and status updates;
- experience: client clarity and confidence.

A workflow may change.

The value flow remains.

This is why the Core should not be designed around one workflow.

It should be designed around value flow and reusable execution structure.

---

# 15. Value Flow Is Not Funnel

Professional Value Flow must also not be confused with a marketing funnel.

A funnel focuses on conversion.

Professional Value Flow focuses on transformation of professional work.

Opportunity generation may be part of the Core.

Sales conversion may be part of a product or business process.

But professional value is broader than sales.

It includes:

- accurate representation;
- trusted knowledge;
- responsible judgment;
- traceable action;
- coordinated execution;
- reliable experience.

Therefore, Opportunity is one Core Domain.

It does not replace the entire value flow.

---

# 16. Value Flow Is Not AI Conversation

Professional Value Flow must also not be reduced to AI conversation.

AI may provide an interface.

AI may ask questions, summarize facts, recommend options and draft documents.

But the value flow cannot depend only on conversation.

Behind a good AI interaction, the Core still needs:

- identity;
- object context;
- knowledge sources;
- service contracts;
- event history;
- task state;
- permission;
- human review;
- consumption rules.

An AI answer without Core context may be fluent but unreliable.

An AI answer grounded in Core can become a professional capability.

---

# 17. Value Flow and Core Domains

The Professional Value Flow maps to Core Domain categories.

| Value Flow Stage | Primary Domain Categories |
|------------------|---------------------------|
| Reality | Professional Domains, Collaboration Network Domains |
| Facts | Foundation Domains, Professional Domains, Event Domain |
| Understanding | Knowledge, Jurisdiction, Classification, Policy |
| Judgment | Knowledge, Policy, AI Capability, Business Responsibility |
| Action | Matter, Order, Document, Evidence, Core Services |
| Coordination | Task, Event, Notification, Routing, Communication |
| Experience | Workplace, Product Consumption, Service Network |

This mapping is not exclusive.

Many domains support more than one stage.

For example, Trademark supports Reality, Facts, Understanding, Judgment and Action.

Matter supports Action, Coordination and Experience.

Knowledge supports Understanding and Judgment.

Event supports Facts, Coordination and Audit.

---

# 18. Value Flow and Core Objects

Core Objects represent value flow anchors.

Examples:

- Brand anchors real-world brand identity.
- Trademark anchors legal protection.
- Customer anchors client context.
- Matter anchors professional work.
- Order anchors commercial execution.
- Document anchors professional evidence or procedure.
- Event anchors change.
- Task anchors responsibility.
- Opportunity anchors business potential.
- Agent anchors professional collaboration.
- Communication anchors interaction history.

Each Core Object should be evaluated by asking:

> Which part of the Professional Value Flow does this object support?

If an object does not support the value flow, it may not belong to Core.

---

# 19. Value Flow and Core Services

Core Services move value forward.

Examples:

- Search Service helps move from facts to understanding.
- Knowledge Retrieval Service helps move from facts to understanding.
- Classification Recommendation Service helps move from understanding to judgment.
- Matter Creation Service helps move from judgment to action.
- Document Generation Service helps move from action to coordination.
- Routing Service helps move from action to coordination.
- Notification Service helps coordination reach experience.
- Opportunity Scoring Service helps facts and understanding become business action.

A Core Service should not exist only because a product needs a button.

It should exist because it moves professional value forward in a reusable way.

---

# 20. Value Flow and Events

Events make value flow visible.

Without events, value flow becomes hidden.

Events can record:

- a fact has entered the system;
- an object has changed state;
- a judgment has been made;
- an action has been performed;
- coordination is required;
- a risk has appeared;
- an experience-relevant update is available.

Examples:

- `TrademarkStatusChanged`
- `MatterCreated`
- `OrderConvertedToMatter`
- `DocumentUploaded`
- `EvidencePackageGenerated`
- `TaskAssigned`
- `AgentReplyReceived`
- `OpportunityCreated`
- `RoutingDecisionMade`
- `NotificationDelivered`

Events allow the Core to support audit, automation, AI monitoring, notification and cross-product coordination.

---

# 21. Value Flow and AI Capability

AI Capability should be evaluated by its role in the value flow.

AI may assist:

- Reality to Facts through extraction and classification;
- Facts to Understanding through summarization and knowledge retrieval;
- Understanding to Judgment through recommendation and risk analysis;
- Judgment to Action through drafting and next-step generation;
- Action to Coordination through task suggestions and routing support;
- Coordination to Experience through communication drafting and status explanation.

AI shall not bypass the flow.

AI shall not replace facts with hallucination.

AI shall not replace knowledge with plausible language.

AI shall not replace professional judgment in high-risk matters.

AI shall move value forward only under Core governance.

---

# 22. Value Flow and Human Review

Human review appears especially at the Judgment and Action stages.

Human review is required when:

- legal rights may be affected;
- official filings may be submitted;
- deadlines may be missed;
- evidence sufficiency is uncertain;
- client advice is high-risk;
- AI output is uncertain;
- policy requires approval;
- financial or contractual responsibility is involved.

The Core should not treat human review as a manual inconvenience.

Human review is part of professional value creation.

The Core must represent review through tasks, events, permissions and audit records where necessary.

---

# 23. Value Flow and Business Responsibility

Professional value flow also contains business responsibility.

A business opportunity becomes valuable only when responsibility is clear.

Questions include:

- Who owns the customer?
- Who owns the opportunity?
- Who is authorized to quote?
- Who is responsible for the matter?
- Who may assign an agent?
- Who may approve an AI-generated draft?
- Who may send client advice?
- Who may close the matter?
- Who is accountable for failure?

Business responsibility connects judgment, action and coordination.

This is why Book 02 includes Business Responsibility Specification.

It is not about pricing packages.

It is about responsibility ownership in professional execution.

---

# 24. Value Flow and Product Consumption

Products consume the Core at different stages of value flow.

MarkReg may focus on:

- action;
- coordination;
- official filing;
- document handling;
- matter status;
- professional execution.

MarkOrbit Lite may focus on:

- guided understanding;
- AI-assisted judgment;
- opportunity conversion;
- simplified action.

MGSN may focus on:

- coordination;
- routing;
- agent and service provider collaboration;
- network trust.

Brand Asset Vault may focus on:

- reality representation;
- facts;
- professional memory;
- asset continuity.

Opportunity Engine may focus on:

- facts;
- understanding;
- business judgment;
- opportunity action.

Different products consume different parts of the flow.

But all should depend on the same Core.

---

# 25. Value Flow and MVP

The Core MVP should implement enough of the value flow to become useful.

A Core MVP should not only store objects.

It should support a minimal chain:

```text
Reality
        ↓
Facts
        ↓
Understanding
        ↓
Action
        ↓
Coordination
```

For example, an MVP chain may include:

- Customer;
- Brand;
- Trademark;
- Jurisdiction;
- Classification;
- Knowledge;
- Order;
- Matter;
- Task;
- Event;
- Document.

This creates a minimal executable skeleton.

The MVP may not yet complete all opportunity, routing, network and AI capabilities.

But it should preserve the value flow.

If MVP implementation breaks the flow, later expansion will become difficult.

---

# 26. Value Flow Integrity

Value Flow Integrity means that each stage of the value flow remains connected to the next stage.

The Core should avoid disconnected fragments.

Examples of broken value flow:

- data imported but not linked to Core Objects;
- objects created but no events recorded;
- knowledge stored but not retrievable by services;
- AI recommendations generated without knowledge source;
- tasks assigned without related matter context;
- documents uploaded without lifecycle connection;
- opportunities created without customer or trademark context;
- notifications sent without event history;
- product UI shows status without Core event source.

A healthy Core preserves the chain.

```text
Reality → Facts → Understanding → Judgment → Action → Coordination → Experience
```

---

# 27. Value Flow Review Questions

When reviewing a domain, object, service, event, AI capability or product consumption rule, reviewers should ask:

1. Which stage of the Professional Value Flow does this support?
2. What reality does it represent?
3. What facts does it record?
4. What knowledge does it require?
5. What understanding does it produce?
6. What judgment does it support?
7. What action does it enable?
8. What coordination does it require?
9. What experience does it support?
10. What events make the flow visible?
11. What human review is required?
12. What product consumes this value?
13. What would break if this stage were missing?

These questions shall guide later specification review.

---

# 28. Value Flow Anti-Patterns

## 28.1 Data Without Meaning

Data is stored, but no Core Object or domain meaning exists.

Result:

- hard to reuse;
- hard to govern;
- hard to connect to products.

## 28.2 Knowledge Without Execution

Knowledge exists as documents or notes but cannot be used by services or AI.

Result:

- knowledge remains passive;
- professionals still rely on memory;
- AI lacks authorized sources.

## 28.3 AI Without Facts

AI responds without reliable facts or object context.

Result:

- plausible but unsafe output;
- inconsistent advice;
- weak auditability.

## 28.4 Action Without Judgment

The system performs actions without understanding or review.

Result:

- operational risk;
- professional responsibility unclear;
- client trust may be damaged.

## 28.5 Workflow Without Value Flow

A workflow moves tasks forward but does not preserve knowledge, judgment, audit or experience.

Result:

- process exists but professional value is weak.

## 28.6 Experience Without Core

A product looks smooth but does not consume shared Core Objects, Services or Events.

Result:

- attractive interface;
- fragmented architecture;
- poor long-term scalability.

---

# 29. Value Flow Rules

The following rules are established by this chapter.

## Rule 1 — Core SHALL support the full Professional Value Flow

The Core shall not be reduced to data storage, workflow execution, AI response or product UI.

## Rule 2 — Reality SHALL be represented through Core Objects when shared meaning is required

Relevant professional reality shall become Core Objects when it must be referenced, linked, audited or consumed.

## Rule 3 — Facts SHALL be traceable

Facts shall have source, context and relationship to Core Objects where necessary.

## Rule 4 — Understanding SHALL be grounded in Knowledge

Understanding shall rely on authorized knowledge sources and knowledge services.

## Rule 5 — Judgment SHALL be governed

Judgment support shall use rules, policies, AI governance and human review where appropriate.

## Rule 6 — Action SHALL be executed through Core Services or governed execution primitives

Professional actions shall not be hidden inside product-specific behavior when they represent reusable capabilities.

## Rule 7 — Coordination SHALL be observable

Meaningful coordination shall be represented through tasks, events, notifications, routing, communication or workflow contracts.

## Rule 8 — Experience SHALL consume Core without redefining it

Products may innovate in experience, but shall not redefine Core meaning.

## Rule 9 — AI SHALL move value forward under governance

AI shall support value flow stages only with authorized knowledge, context, permission, audit and review rules.

## Rule 10 — MVP SHALL preserve value flow integrity

MVP implementation shall create a minimal executable chain rather than isolated modules.

---

# 30. Specification Output

This chapter produces the following specification output:

- Professional Value Flow definition;
- stage-by-stage value flow explanation;
- Core architecture mapping;
- domain mapping;
- object mapping;
- service mapping;
- event mapping;
- AI capability mapping;
- product consumption mapping;
- MVP value flow rule;
- value flow integrity rule;
- value flow review questions;
- value flow anti-patterns.

These outputs shall guide all later Book 02 chapters and `core-specs/`.

---

# 31. Execution Mapping

This chapter does not directly define database tables or APIs.

It defines the execution logic that implementation must preserve.

| Value Flow Stage | Execution Mapping |
|------------------|-------------------|
| Reality | Core Objects, documents, communication, integrations |
| Facts | data records, event logs, audit records |
| Understanding | knowledge services, rule retrieval, AI-assisted interpretation |
| Judgment | policies, recommendations, risk levels, human review |
| Action | Core Services, tasks, document generation, routing |
| Coordination | events, workflow contracts, notifications, communication |
| Experience | Workplace and product consumption contracts |

Implementation shall not create isolated assets that break this flow.

---

# 32. Relationship to core-specs/

This chapter governs how `core-specs/` should preserve value flow.

Every detailed specification should identify which stage or stages of the value flow it supports.

In particular:

- Domain specs shall state their value flow responsibility.
- Object specs shall identify the reality or fact they represent.
- Service specs shall state how they move value forward.
- Event specs shall state what change they make visible.
- Agent specs shall state which stage AI assists and what governance applies.
- API specs shall preserve consumption without redefining value flow.
- Workflow specs shall preserve coordination without absorbing product experience.

---

# 33. Exclusions

This chapter shall not include:

- product UI design;
- product user journey details;
- full workflow diagrams;
- detailed database schemas;
- API endpoint definitions;
- production AI prompts;
- product pricing;
- marketing content;
- deployment architecture;
- operational SOPs.

Those belong to later specifications, product publications or implementation documents.

---

# 34. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines Professional Value Flow clearly.
- It maps each stage of the flow to Core architecture.
- It distinguishes value flow from workflow, funnel and AI conversation.
- It explains how Core Domains, Objects, Services, Events and AI Capabilities support the flow.
- It preserves Core / Workplace / Product boundaries.
- It defines value flow integrity.
- It gives review questions and anti-patterns.
- It supports MVP execution without becoming a PRD.
- It supports Book 02 TOC v1.2.
- It does not duplicate Book 01.

---

# 35. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 07, defining the Professional Value Flow of the MarkOrbit Core. |

---

**End of Chapter**
