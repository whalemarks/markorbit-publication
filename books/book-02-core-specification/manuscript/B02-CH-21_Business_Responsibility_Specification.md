# Book 02

# 21 — Business Responsibility Specification

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-21

**Chapter Title:** Business Responsibility Specification

**Part:** Part III — Core Specification System

**Chapter Type:** Specification

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

This chapter defines the Business Responsibility Specification of the MarkOrbit Core.

Chapter 18 defined Identity.

Chapter 19 defined Capability.

Chapter 20 defined Knowledge.

This chapter defines Business Responsibility.

Business Responsibility is the layer that answers:

> Who owns, authorizes, approves, delegates, executes, reviews, receives value, bears risk and remains accountable?

Professional service systems often fail not because data is missing, but because responsibility is unclear.

A trademark matter may have customer owner, sales owner, matter owner, process operator, foreign agent, reviewer, finance approver and client contact.

An AI agent may draft a recommendation, but a human must review it.

An order may be paid, but responsibility must transfer into a matter.

A routing decision may assign a foreign agent, but someone must approve or accept the risk.

An opportunity may be detected, but someone must own follow-up.

A document may be generated, but someone must verify whether it is correct.

Business Responsibility makes these accountability structures explicit.

Without Business Responsibility, MarkOrbit would become a data platform, workflow tool or AI assistant without professional accountability.

This chapter defines how responsibility is represented, governed, executed and audited in the Core.

---

# 2. Core Question

This chapter answers one question:

> How shall MarkOrbit define, assign, govern, execute and audit business responsibility across customers, orders, matters, opportunities, tasks, AI output, routing, agents, service providers and products?

The answer is:

> MarkOrbit shall define Business Responsibility as a governed Core structure that links Identity, Capability, Knowledge, Permission, Policy, Objects, Services, Events, Tasks, Workflow Contracts and Product Consumption to explicit ownership, authorization, delegation, review, accountability and value responsibility.

Business Responsibility is not pricing.

Business Responsibility is not sales commission.

Business Responsibility is not organization chart.

Business Responsibility is not a product dashboard.

Business Responsibility is architectural accountability.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- Business Responsibility purpose;
- Business Responsibility Model application;
- responsibility ontology;
- responsibility object types;
- responsibility ownership types;
- customer responsibility;
- order responsibility;
- matter responsibility;
- opportunity responsibility;
- task responsibility;
- review responsibility;
- AI output responsibility;
- routing responsibility;
- agent and service provider responsibility;
- delegation;
- authorization;
- approval;
- escalation;
- responsibility transfer;
- responsibility lifecycle;
- responsibility events;
- responsibility services;
- responsibility contracts;
- product consumption;
- MVP boundary;
- `core-specs/` requirements;
- Codex implementation rules.

## 3.2 Out of Scope

This chapter does not define:

- product pricing plans;
- commission schedules;
- sales incentive schemes;
- HR job descriptions;
- internal department structure;
- company org chart;
- product commercial packages;
- client engagement contracts;
- detailed operational SOPs;
- full workflow operation;
- complete API endpoint design;
- database schema;
- implementation code.

Those belong to product business documents, operating manuals, legal documents or implementation specs.

---

# 4. Business Responsibility Definition

In the MarkOrbit Core, Business Responsibility means:

> the governed assignment of ownership, authorization, delegation, execution, review, approval, escalation, value relationship and accountability for Core professional and business actions.

This definition includes:

- who owns a customer;
- who owns an opportunity;
- who owns an order;
- who owns a matter;
- who may act;
- who may approve;
- who must review;
- who may delegate;
- who is assigned;
- who bears responsibility for risk;
- who is accountable for AI-assisted output;
- who is responsible for external agent routing;
- who receives value or business attribution.

Business Responsibility connects professional execution to accountability.

---

# 5. Business Responsibility Specification Position

Business Responsibility Specification belongs to Part III because it turns the Business Responsibility Model into concrete Core specification rules.

It is connected to Part II as follows:

```text
Canonical Models
    Business Responsibility Model

Core Domains
    Customer
    Matter
    Order
    Opportunity
    Permission
    Policy
    Task
    Event
    Routing
    Communication
    Agent
    Service Provider
    AI Capability and Agent Governance

Core Objects
    Responsibility Assignment
    Responsibility Owner
    Review Authority
    Delegation
    Approval Record
    Escalation Record
    Responsibility Transfer
    Responsibility Audit Record

Core Services
    Responsibility Assignment Service
    Review Assignment Service
    Approval Service
    Delegation Service
    Escalation Service
    Responsibility Transfer Service
    Responsibility Audit Service

Execution Primitives
    ResponsibilityAssigned
    ResponsibilityTransferred
    ReviewRequired
    ReviewApproved
    ReviewRejected
    EscalationTriggered

Core Contracts
    Responsibility Data Contract
    Responsibility API Contract
    Responsibility Event Contract
    Workflow Contract
    Agent Contract
    Consumption Contract
```

Business Responsibility is not a single product feature.

It is a Core specification that affects execution across the ecosystem.

---

# 6. Business Responsibility Principles

The Business Responsibility Specification is governed by the following principles.

## Principle 1 — Responsibility Before Automation

Automation must not execute high-risk professional actions without responsibility assignment.

## Principle 2 — Responsibility Before AI Autonomy

AI may assist, but responsibility remains with human, business or domain owners.

## Principle 3 — Ownership Must Be Explicit

Customer, order, matter, opportunity, task, review and routing responsibility must not remain hidden.

## Principle 4 — Authorization Must Be Governed

The right to act must depend on identity, role, permission, policy, context and risk.

## Principle 5 — Delegation Must Be Traceable

Delegated responsibility must preserve who delegated, to whom, under what scope and when.

## Principle 6 — Review Must Be Represented

High-risk actions require review structures, not informal memory.

## Principle 7 — Responsibility Transfer Must Be Evented

When responsibility moves from order to matter, from sales to process, or from AI to human review, the change must be observable.

## Principle 8 — Product Experience Must Not Redefine Responsibility

Products may display responsibility, but Core defines its meaning.

---

# 7. Responsibility Ontology

Business Responsibility belongs primarily to System Ontology and Execution Ontology.

## 7.1 System Ontology

Responsibility is a system concept because it governs ownership, authorization, review and accountability.

## 7.2 Execution Ontology

Responsibility becomes executable through tasks, events, states, workflow contracts and service actions.

## 7.3 Reality Ontology

Responsibility reflects real business and professional accountability among people and organizations.

## 7.4 Collaboration Ontology

Responsibility extends to agents, service providers, partners and external collaboration.

Business Responsibility therefore connects multiple ontology layers.

---

# 8. Responsibility Domain Relationships

Business Responsibility is related to many Core Domains.

| Domain | Responsibility Relationship |
|--------|-----------------------------|
| Identity | responsibility owner and actor identity |
| User | internal user responsibility |
| Organization | organization-level responsibility |
| Permission | authorization depends on responsibility |
| Policy | policy defines responsibility rules |
| Customer | customer owner and relationship responsibility |
| Order | order owner, payer, converter and approver |
| Matter | matter owner, executor, reviewer and agent assignee |
| Opportunity | opportunity owner and follow-up responsibility |
| Task | task assignee and responsible owner |
| Event | responsibility changes become events |
| Notification | responsibility triggers awareness |
| Agent | external professional responsibility |
| Service Provider | provider responsibility |
| Routing | routing approval and assignment responsibility |
| Communication | responsible communicator and recipient |
| AI Capability | AI output review and accountability |

No domain should redefine responsibility independently.

Domains consume this specification.

---

# 9. Responsibility Object Types

The Business Responsibility Specification recognizes the following object types.

```text
Responsibility Assignment
Responsibility Owner
Responsibility Role
Authorization Rule
Delegation Record
Approval Record
Review Requirement
Review Assignment
Review Result
Escalation Rule
Escalation Record
Responsibility Transfer
Accountability Record
Value Attribution
Responsibility Audit Record
```

Not all objects require separate database tables.

But their meanings must be preserved in detailed specifications.

---

# 10. Responsibility Assignment

## 10.1 Definition

Responsibility Assignment is:

> the structured assignment of responsibility for a Core Object, action, decision, task, review, workflow or outcome to an Identity, Role, Organization, Agent, Service Provider or AI-governed actor.

## 10.2 Purpose

Responsibility Assignment provides:

- ownership;
- accountability;
- authorization context;
- task assignment;
- review assignment;
- escalation path;
- audit trace;
- product visibility;
- AI governance.

## 10.3 Minimum Attributes

A minimal Responsibility Assignment should include:

```text
responsibility_assignment_id
responsibility_type
related_object_type
related_object_id
owner_identity_id
owner_role
assigned_by
assignment_scope
status
created_at
updated_at
```

This is a semantic baseline, not a final database schema.

Detailed fields belong in `core-specs/objects/responsibility-assignment.md`.

---

# 11. Responsibility Ownership Types

Book 02 recognizes multiple responsibility ownership types.

```text
1. Semantic Responsibility
2. Business Ownership
3. Execution Responsibility
4. Review Responsibility
5. Authorization Responsibility
6. Delegated Responsibility
7. External Service Responsibility
8. AI Output Responsibility
9. Value Attribution Responsibility
10. Audit Responsibility
```

Each type must be distinguished.

Mixing responsibility types creates professional risk.

---

# 12. Semantic Responsibility

Semantic Responsibility means ownership of Core meaning.

Examples:

- Trademark Domain owns trademark meaning.
- Matter Domain owns matter meaning.
- Agent Domain owns agent meaning.
- Knowledge Domain owns knowledge meaning.

Semantic Responsibility belongs to Core architecture.

Products shall not own semantic responsibility.

---

# 13. Business Ownership

Business Ownership means ownership of business relationship, opportunity, order, matter or customer value.

Examples:

- customer owner;
- opportunity owner;
- order owner;
- matter business owner;
- partner owner;
- account owner.

Business Ownership supports:

- follow-up;
- reporting;
- authorization;
- escalation;
- product visibility;
- value attribution.

Business Ownership is not the same as execution assignment.

A sales owner may own the customer, while a process operator executes the matter.

---

# 14. Execution Responsibility

Execution Responsibility means responsibility for performing work.

Examples:

- task assignee;
- matter operator;
- document preparer;
- filing processor;
- agent coordinator;
- service provider assignee;
- workflow operator.

Execution Responsibility is represented through Tasks, Workflow Contracts and Events.

Execution Responsibility should be visible and traceable.

---

# 15. Review Responsibility

Review Responsibility means responsibility for reviewing, approving, rejecting or escalating an output or decision.

Examples:

- review AI classification recommendation;
- approve evidence sufficiency analysis;
- review document draft;
- approve client-facing advice;
- approve routing decision;
- approve official filing submission;
- review identity merge.

Review Responsibility is especially important for AI-assisted and high-risk professional work.

---

# 16. Authorization Responsibility

Authorization Responsibility means the authority to permit action.

Examples:

- approve order conversion;
- authorize agent assignment;
- permit external document sharing;
- approve quote;
- allow AI access to sensitive objects;
- permit state transition;
- override risk warning.

Authorization depends on Identity, Role, Permission, Policy and Context.

Authorization must not live only in product UI.

---

# 17. Delegated Responsibility

Delegated Responsibility means responsibility assigned by one responsible actor to another.

Examples:

- matter owner delegates document preparation to process user;
- internal reviewer delegates translation check to service provider;
- agent coordinator assigns work to foreign agent;
- product workflow assigns AI draft review to reviewer.

Delegation should record:

- delegator;
- delegatee;
- scope;
- time;
- reason;
- acceptance status where relevant;
- audit.

Delegation does not erase original accountability unless responsibility transfer rules say so.

---

# 18. External Service Responsibility

External Service Responsibility means responsibility assigned to an agent, service provider or external collaborator.

Examples:

- foreign agent responsible for filing;
- service provider responsible for translation;
- local counsel responsible for legal opinion;
- provider responsible for certificate scan;
- agent responsible for deadline response.

External responsibility must link to:

- Agent Identity;
- Service Provider Identity;
- Capability;
- Matter;
- Task;
- Communication;
- Routing Decision;
- Contract;
- Event.

External responsibility is not merely a note in email.

---

# 19. AI Output Responsibility

AI Output Responsibility means responsibility for AI-assisted output.

AI may generate:

- recommendation;
- draft;
- summary;
- classification result;
- routing suggestion;
- opportunity signal;
- evidence analysis;
- client explanation.

But responsibility must define:

- requesting user;
- AI agent identity;
- owning domain;
- reviewer;
- approval status;
- output risk;
- whether output may be shown to client;
- whether output may update Core Objects;
- audit record.

AI output without responsibility is not acceptable for professional Core execution.

---

# 20. Value Attribution Responsibility

Value Attribution Responsibility means responsibility for business value relationship.

Examples:

- opportunity owner;
- customer source;
- partner attribution;
- sales attribution;
- matter conversion attribution;
- service provider contribution;
- AI-assisted opportunity source.

Value Attribution supports reporting and business management.

It is not the same as commission scheme.

Commission and commercial formulas belong to business documents.

Core only defines attribution structure where needed.

---

# 21. Audit Responsibility

Audit Responsibility means responsibility for preserving traceability.

Examples:

- who changed a status;
- who approved a document;
- who reviewed AI output;
- who assigned an agent;
- who merged identities;
- who invoked a high-risk capability;
- who overrode a policy warning.

Audit Responsibility supports governance, learning and dispute handling.

---

# 22. Responsibility Lifecycle

Responsibility should have lifecycle.

Baseline lifecycle may include:

```text
Proposed
Assigned
Accepted
Active
Delegated
Under Review
Approved
Rejected
Escalated
Transferred
Completed
Cancelled
Archived
```

Not all responsibility types need every state.

Lifecycle should be adapted by object type and workflow contract.

State changes may publish responsibility events.

---

# 23. Responsibility Transfer

Responsibility Transfer is the structured movement of responsibility from one owner, stage or object to another.

Examples:

```text
Opportunity → Order
Order → Matter
Sales Owner → Matter Owner
AI Draft → Human Reviewer
Task Assignee → Escalation Owner
Internal Team → External Agent
Agent → Service Provider
```

Responsibility Transfer should define:

- source responsibility;
- target responsibility;
- trigger;
- required permission;
- required acceptance;
- event;
- audit record;
- rollback or correction rule.

Responsibility Transfer is critical for order-to-matter conversion and AI review.

---

# 24. Responsibility Delegation

Delegation assigns work without necessarily transferring final accountability.

Examples:

- matter owner delegates document preparation;
- review authority delegates initial check;
- agent coordinator delegates follow-up task;
- partner delegates client communication to internal user.

Delegation should distinguish:

```text
delegated execution
delegated review
delegated communication
delegated authority
delegated monitoring
```

Delegation rules should define whether final responsibility remains with the delegator.

---

# 25. Authorization

Authorization determines whether an identity may perform an action.

Authorization may depend on:

- identity;
- role;
- organization;
- product access;
- object relationship;
- customer ownership;
- matter ownership;
- task assignment;
- capability;
- policy;
- risk level;
- verification status;
- workflow state.

Authorization should be evaluated through Permission and Policy domains.

Business Responsibility provides context for authorization.

---

# 26. Approval

Approval is a responsibility decision that permits an output, action, transfer or state change.

Approval may apply to:

- quote;
- order conversion;
- AI output;
- document draft;
- evidence review;
- routing decision;
- official filing;
- client communication;
- identity merge;
- policy override.

Approval should record:

- approver;
- object;
- decision;
- time;
- basis;
- conditions;
- related events;
- audit record.

Approval should not be hidden in informal messages.

---

# 27. Escalation

Escalation is the transfer or elevation of responsibility due to risk, delay, blockage or policy.

Escalation triggers may include:

- overdue task;
- agent not replying;
- high-risk AI output;
- missing knowledge;
- document rejected;
- deadline approaching;
- permission denied;
- provider reliability warning;
- customer complaint;
- policy conflict.

Escalation should create:

- escalation event;
- escalation task;
- new responsibility owner;
- notification;
- audit record.

Escalation rules belong to Workflow Contracts or Policy.

---

# 28. Customer Responsibility

Customer Responsibility defines who owns and manages customer relationship.

It may include:

- customer owner;
- account owner;
- partner owner;
- customer contact;
- client communication responsibility;
- opportunity follow-up owner;
- service history owner.

Customer Responsibility supports:

- order creation;
- matter creation;
- opportunity conversion;
- communication routing;
- product access;
- client status updates.

Customer Responsibility is not just CRM assignment.

It affects professional service execution.

---

# 29. Order Responsibility

Order Responsibility defines who owns order creation, confirmation, payment tracking, conversion and cancellation.

It may include:

- order owner;
- quote approver;
- payer relationship;
- payment verifier;
- conversion approver;
- refund approver;
- order-to-matter responsible user.

Order Responsibility connects commercial transaction to professional execution.

Order-to-Matter conversion must produce responsibility transfer.

---

# 30. Matter Responsibility

Matter Responsibility defines who owns and executes a professional matter.

It may include:

- matter owner;
- matter operator;
- review authority;
- customer owner;
- agent coordinator;
- external agent assignee;
- service provider assignee;
- deadline owner;
- communication owner;
- escalation owner.

Matter Responsibility is central to MarkOrbit because matters are the main execution unit of professional services.

Matter Responsibility must be represented explicitly.

---

# 31. Opportunity Responsibility

Opportunity Responsibility defines who owns detection, follow-up, scoring, qualification and conversion of opportunities.

It may include:

- opportunity owner;
- source owner;
- customer owner;
- AI discovery source;
- reviewer;
- follow-up assignee;
- conversion owner.

Opportunity Responsibility prevents opportunity signals from becoming unused data.

It also connects AI opportunity discovery to human business action.

---

# 32. Task Responsibility

Task Responsibility defines who must perform a specific action.

It includes:

- assignee;
- responsible owner;
- reviewer where applicable;
- due date;
- escalation owner;
- completion criteria;
- related object;
- related workflow contract.

Task Responsibility is not simply a to-do item.

It is a structured responsibility unit.

---

# 33. Routing Responsibility

Routing Responsibility defines who is responsible for selecting, approving or accepting a routing decision.

Routing may involve:

- matter owner;
- routing service;
- AI routing assistant;
- agent matching service;
- external agent;
- service provider;
- approval authority.

Routing Responsibility should define:

- who may recommend;
- who may approve;
- who is assigned;
- who is accountable for provider risk;
- what event is emitted.

---

# 34. Agent and Service Provider Responsibility

Agent and Service Provider Responsibility defines external professional responsibility.

It may include:

- assigned matter;
- service type;
- jurisdiction;
- document responsibility;
- deadline responsibility;
- communication obligation;
- fee or service arrangement reference;
- reliability tracking;
- escalation pathway.

Book 02 defines responsibility meaning.

Book 06 may define network-level business model and provider operation.

---

# 35. Responsibility and AI

AI requires explicit responsibility rules.

AI may:

- summarize;
- recommend;
- draft;
- classify;
- detect opportunity;
- suggest routing;
- identify gaps;
- prepare review notes.

AI shall not:

- own business responsibility;
- approve high-risk output;
- silently change Core Object state;
- assign external agents without authorization;
- issue final client advice without review;
- bypass knowledge and permission governance.

AI-related responsibility should include:

- AI agent identity;
- requesting user;
- responsible domain;
- reviewer;
- approval status;
- risk level;
- output usage rule;
- audit event.

---

# 36. Responsibility Events

Responsibility-related Events may include:

```text
ResponsibilityAssigned
ResponsibilityAccepted
ResponsibilityDelegated
ResponsibilityTransferred
ResponsibilityCompleted
ResponsibilityCancelled
ReviewRequired
ReviewAssigned
ReviewApproved
ReviewRejected
ApprovalGranted
ApprovalDenied
EscalationTriggered
MatterOwnerAssigned
OpportunityOwnerAssigned
OrderConvertedToMatter
AgentAssigned
AIDraftReviewRequired
AIRecommendationApproved
```

Events should identify:

- source domain;
- related object;
- responsibility type;
- previous owner;
- new owner;
- actor;
- reason;
- risk level;
- review requirement;
- audit record.

Responsibility changes should not remain invisible.

---

# 37. Responsibility Services

Baseline Responsibility Services include:

```text
Responsibility Assignment Service
Responsibility Transfer Service
Delegation Service
Authorization Evaluation Service
Review Assignment Service
Approval Service
Escalation Service
Responsibility Audit Service
Matter Responsibility Service
Opportunity Ownership Service
Order Responsibility Service
AI Output Review Responsibility Service
Routing Responsibility Service
```

## 37.1 Responsibility Assignment Service

Assigns responsibility to identity, role, organization, agent or service provider.

## 37.2 Responsibility Transfer Service

Transfers responsibility between stages or owners.

## 37.3 Review Assignment Service

Creates review responsibility for high-risk output.

## 37.4 Approval Service

Records approval or rejection.

## 37.5 Escalation Service

Creates escalation when risk, delay or blockage appears.

Detailed service specs belong in:

```text
core-specs/services/
```

---

# 38. Responsibility Contracts

Business Responsibility requires several contract types.

## 38.1 Responsibility Data Contract

Defines responsibility assignment, owner, role, status, scope, transfer and audit meaning.

## 38.2 Responsibility API Contract

Defines responsibility assignment, transfer, delegation, review and approval operations.

## 38.3 Responsibility Event Contract

Defines events such as `ResponsibilityAssigned`, `ReviewRequired` and `EscalationTriggered`.

## 38.4 Workflow Contract

Defines how responsibility moves across workflow states, tasks and reviews.

## 38.5 Agent Contract

Defines AI output responsibility and human review requirements.

## 38.6 Consumption Contract

Defines how products display and consume responsibility without redefining it.

Detailed contracts belong to:

```text
core-specs/contracts/
core-specs/api/
core-specs/events/
core-specs/workflows/
core-specs/agents/
```

---

# 39. Responsibility Data Contract Baseline

A baseline Responsibility Data Contract should define:

```text
responsibility_id
responsibility_type
related_object_type
related_object_id
owner_identity_id
owner_role
owner_organization_id
assigned_by
assigned_at
accepted_at
status
scope
delegation_source_id
transfer_source_id
risk_level
review_required
approval_status
escalation_status
created_at
updated_at
audit_reference
```

This is not a final database schema.

It is a semantic baseline.

---

# 40. Responsibility API Surface Baseline

A baseline Responsibility API surface may include:

```text
assignResponsibility
getResponsibility
transferResponsibility
delegateResponsibility
acceptResponsibility
completeResponsibility
cancelResponsibility
requestReview
assignReview
approveReview
rejectReview
triggerEscalation
getResponsibilityHistory
```

These operation names are conceptual.

Implementation may choose REST, RPC, internal service calls or workflow commands.

Meaning must be preserved by API Contracts.

---

# 41. Responsibility AI Usage

AI may assist Business Responsibility, but under governance.

Permitted AI-assisted uses may include:

- suggest task assignee;
- detect missing responsibility;
- summarize responsibility history;
- recommend escalation;
- identify overdue responsibility;
- suggest reviewer based on risk;
- detect conflict between responsibility and permission;
- prepare review notes.

Restricted AI uses include:

- assigning high-risk responsibility without authorization;
- approving professional output;
- transferring responsibility silently;
- overriding human reviewer;
- assigning external agent without policy and human approval where required;
- hiding uncertainty or conflict.

AI may assist responsibility management.

AI does not own responsibility.

---

# 42. Responsibility Product Consumption

Products consume Business Responsibility differently.

## 42.1 MarkReg

Consumes responsibility for:

- matter owner;
- filing operator;
- agent coordinator;
- document reviewer;
- office action reviewer;
- deadline owner;
- external agent assignment.

## 42.2 Lite

Consumes responsibility for:

- customer owner;
- guided consultation owner;
- order owner;
- AI recommendation reviewer;
- client follow-up owner.

## 42.3 MGSN

Consumes responsibility for:

- agent assignment;
- service provider responsibility;
- routing approval;
- network participation responsibility;
- communication responsibility.

## 42.4 Workplace

Consumes responsibility for:

- task assignment;
- review queue;
- escalation;
- workflow responsibility;
- human-AI collaboration.

## 42.5 Opportunity Engine

Consumes responsibility for:

- opportunity owner;
- follow-up assignee;
- conversion owner;
- AI-discovered opportunity review.

Products may display responsibility differently.

They shall not redefine responsibility meaning.

---

# 43. Responsibility MVP Boundary

The Business Responsibility MVP should implement enough to support early Core execution.

MVP should include:

```text
Responsibility Assignment
Responsibility Type
Owner Identity
Role
Status
Matter Owner
Order Owner
Opportunity Owner
Task Assignee
Review Requirement
Review Assignment
Basic Delegation
Basic Transfer
ResponsibilityAssigned Event
ReviewRequired Event
Responsibility Data Contract
Responsibility API Contract
```

MVP may defer:

- advanced value attribution;
- complex escalation matrix;
- full commission attribution;
- advanced responsibility analytics;
- complex multi-party responsibility negotiation;
- full MGSN provider responsibility model;
- advanced AI responsibility optimization.

MVP must not skip responsibility if AI, matters, orders or tasks are implemented.

---

# 44. Responsibility Specification Structure for core-specs/

Recommended files:

```text
core-specs/domains/business-responsibility.md
core-specs/objects/responsibility-assignment.md
core-specs/objects/review-requirement.md
core-specs/objects/delegation-record.md
core-specs/objects/approval-record.md
core-specs/objects/escalation-record.md
core-specs/services/responsibility-assignment.md
core-specs/services/responsibility-transfer.md
core-specs/services/review-assignment.md
core-specs/services/approval.md
core-specs/services/escalation.md
core-specs/events/responsibility-assigned.md
core-specs/events/review-required.md
core-specs/events/review-approved.md
core-specs/events/escalation-triggered.md
core-specs/contracts/responsibility-data-contract.md
core-specs/api/responsibility-api.md
core-specs/agents/responsibility-assistant.md
```

Responsibility should also be referenced by:

```text
core-specs/domains/customer.md
core-specs/domains/order.md
core-specs/domains/matter.md
core-specs/domains/opportunity.md
core-specs/domains/task.md
core-specs/domains/routing.md
core-specs/domains/agent.md
core-specs/domains/service-provider.md
```

---

# 45. Responsibility Specification Template

A detailed Business Responsibility specification should include:

```text
# Business Responsibility Specification

1. Responsibility Purpose
2. Owning Domain
3. Responsibility Type
4. Related Core Object
5. Owner Identity
6. Owner Role
7. Scope
8. Assignment Rules
9. Authorization Rules
10. Delegation Rules
11. Transfer Rules
12. Review Rules
13. Approval Rules
14. Escalation Rules
15. Lifecycle
16. Permission and Policy Requirements
17. AI Usage
18. Events Published
19. Contracts
20. Product Consumers
21. MVP Boundary
22. Acceptance Criteria
23. Revision Notes
```

Detailed object, service, event, API, agent and workflow specs should follow the structures defined in Chapters 14 through 17.

---

# 46. Responsibility Review Questions

When reviewing a responsibility structure, reviewers shall ask:

1. What responsibility type is involved?
2. Which Core Object does it relate to?
3. Who owns the responsibility?
4. Which identity, role or organization is responsible?
5. What scope applies?
6. Who assigned it?
7. Who may accept, reject, delegate or transfer it?
8. What authorization rules apply?
9. Is review required?
10. Who approves the outcome?
11. What happens if responsibility is overdue, blocked or disputed?
12. What events should be emitted?
13. What audit record is required?
14. Does AI assist or produce output?
15. Which product consumes this responsibility?
16. Would fragmentation occur if each product defined responsibility locally?
17. Can Codex implement this from approved specs?

---

# 47. Responsibility Anti-Patterns

## 47.1 Hidden Responsibility

Work is performed but no owner is recorded.

Correction:

```text
Responsibility must be assigned where execution or risk exists.
```

## 47.2 UI Assignment Equals Responsibility

A product field shows an assignee, but no Core responsibility structure exists.

Correction:

```text
Product display consumes Core Responsibility.
It does not define it.
```

## 47.3 AI Owns Responsibility

AI output is treated as final without human or business owner.

Correction:

```text
AI assists.
Human, business or domain responsibility remains explicit.
```

## 47.4 Order Converts Without Transfer

Order becomes matter, but responsibility transfer is not recorded.

Correction:

```text
Order-to-Matter conversion should emit responsibility transfer events.
```

## 47.5 Agent Stored as Text

External responsibility is stored as free text.

Correction:

```text
External responsibility should link to Agent or Service Provider Identity where repeated collaboration exists.
```

## 47.6 Approval Hidden in Email

Approval exists only in communication text.

Correction:

```text
Approval should be structured and auditable where professional risk exists.
```

## 47.7 Product-Local Responsibility

MarkReg, Lite and MGSN define separate responsibility meanings.

Correction:

```text
Shared responsibility belongs to Core.
Products consume it through contracts.
```

---

# 48. Responsibility Rules

The following rules are established by this chapter.

## Rule 1 — Responsibility SHALL be explicit where execution, risk or value exists

Hidden responsibility is not acceptable for professional execution.

## Rule 2 — Responsibility SHALL link to Identity

Responsibility should reference identity, role or organization, not only free text.

## Rule 3 — Responsibility SHALL distinguish ownership, execution, review and authorization

Different responsibility types must not be collapsed.

## Rule 4 — Responsibility SHALL be governed by permission and policy

Authorization cannot be UI-only.

## Rule 5 — Responsibility transfer SHALL be traceable

Order-to-matter, AI-to-reviewer and internal-to-external responsibility transfers should be recorded.

## Rule 6 — Review responsibility SHALL be required for high-risk AI or professional output

AI output does not replace review authority.

## Rule 7 — External responsibility SHALL link to Agent or Service Provider where applicable

Repeated external collaboration should not remain unstructured.

## Rule 8 — Responsibility changes SHOULD produce Events

Meaningful responsibility changes must be observable.

## Rule 9 — Products SHALL consume Responsibility through contracts

Products shall not redefine responsibility locally.

## Rule 10 — MVP SHALL include responsibility if matters, tasks, orders or AI are implemented

Execution without responsibility is not acceptable.

---

# 49. Specification Output

This chapter produces the following specification output:

- Business Responsibility definition;
- Business Responsibility principles;
- responsibility ontology;
- domain relationships;
- responsibility object types;
- Responsibility Assignment;
- responsibility ownership types;
- semantic responsibility;
- business ownership;
- execution responsibility;
- review responsibility;
- authorization responsibility;
- delegated responsibility;
- external service responsibility;
- AI output responsibility;
- value attribution responsibility;
- audit responsibility;
- responsibility lifecycle;
- responsibility transfer;
- delegation;
- authorization;
- approval;
- escalation;
- customer responsibility;
- order responsibility;
- matter responsibility;
- opportunity responsibility;
- task responsibility;
- routing responsibility;
- agent and service provider responsibility;
- AI responsibility rules;
- responsibility events;
- responsibility services;
- responsibility contracts;
- Responsibility Data Contract baseline;
- Responsibility API baseline;
- Product Consumption;
- MVP Boundary;
- `core-specs/` file structure;
- review questions;
- anti-patterns;
- Responsibility rules.

These outputs guide detailed specs in `core-specs/`.

---

# 50. Execution Mapping

This chapter controls responsibility-related implementation assets.

| Responsibility Specification Element | Execution Mapping |
|--------------------------------------|------------------|
| Responsibility Assignment | assignment model and persistence |
| Owner Identity | identity link and role mapping |
| Responsibility Type | type enum and business logic |
| Authorization | permission and policy evaluation |
| Delegation | delegation records and events |
| Transfer | transfer service and workflow events |
| Review | review tasks, approval records and audit |
| Escalation | escalation rules, tasks and notifications |
| AI Responsibility | Agent Contract, review assignment and audit |
| External Responsibility | Agent / Service Provider links |
| Events | responsibility event specs and event publishing |
| Contracts | data, API, event, workflow and consumption contracts |
| Product Consumption | MarkReg, Lite, MGSN, Workplace integration |
| MVP | Codex task sequencing |

Implementation shall preserve responsibility meaning, ownership, transfer and auditability.

---

# 51. Relationship to core-specs/

This chapter is the manuscript source for Business Responsibility-related `core-specs/`.

Detailed specs shall be maintained in:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
core-specs/workflows/
```

No product document shall override the Core Business Responsibility Specification.

No implementation task shall create responsibility meaning without reference to approved Responsibility specs or explicit architecture review.

---

# 52. Exclusions

This chapter shall not include:

- product pricing plans;
- commission formulas;
- sales incentive policies;
- HR job descriptions;
- company org chart;
- product dashboard design;
- operational SOPs;
- legal engagement contracts;
- full workflow operation;
- all production API endpoints;
- deployment architecture;
- implementation code.

These belong elsewhere.

---

# 53. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines Business Responsibility clearly as architectural accountability.
- It distinguishes responsibility from pricing, commission, HR roles and product UI.
- It defines responsibility ownership types.
- It connects responsibility to Identity, Permission, Policy, Tasks, Events, AI, Routing and Product Consumption.
- It defines assignment, delegation, authorization, approval, escalation and transfer.
- It defines customer, order, matter, opportunity, task, routing, agent and AI responsibility.
- It defines baseline services, events, contracts and API surface.
- It provides MVP boundary.
- It provides `core-specs/` structure.
- It includes review questions, anti-patterns and rules.
- It supports Book 02 TOC v1.2.
- It supports implementation without becoming company management SOP or product commercial policy.

---

# 54. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 21, defining Business Responsibility Specification for the MarkOrbit Core. |

---

**End of Chapter**
