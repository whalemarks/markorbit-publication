# Book 02

# 27 — Core Consumption Specification

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-27  
**Chapter Title:** Core Consumption Specification  
**Part:** Part III — Core Specification System  
**Chapter Type:** Specification  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-03 — Core Position
- B02-CH-04 — Core Boundary
- B02-CH-05 — Core Principles
- B02-CH-17 — Core Contract Architecture
- B02-CH-22 — Domain Specification
- B02-CH-23 — Object Specification
- B02-CH-24 — Service Specification
- B02-CH-25 — Event Specification
- B02-CH-26 — AI Capability and Agent Governance Specification
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines how the MarkOrbit Core may be consumed.

The Core is not useful if it is only defined.

The Core becomes useful when products, Workplaces, services, integrations, AI agents, reporting systems and Codex tasks consume it correctly.

However, consumption is also where architecture usually fragments.

A product may consume a Core Object and redefine its meaning.

A Workplace may consume a Task and hide workflow rules inside UI.

An AI agent may consume Knowledge and produce output without review.

An external integration may read internal data without a contract.

Codex may consume manuscript language and generate implementation that expands MVP scope.

Therefore, this chapter establishes the rules, contract requirements and acceptance criteria for Core Consumption.

The purpose of Core Consumption Specification is to ensure that all consumers use the Core without redefining it.

---

# 2. Core Question

This chapter answers one question:

> How can products, Workplaces, AI agents, services, integrations, reporting systems and Codex consume the Core safely?

The answer is:

> They must consume Core through approved Objects, Services, Events, Contracts, APIs, Agent Contracts, Workflow Contracts and Codex task specifications, without redefining Core meaning, bypassing governance or expanding deferred scope.

---

# 3. Core Consumption Definition

Core Consumption defines how an authorized consumer reads, invokes, subscribes to, extends or implements Core specifications.

A Core Consumer may consume:

```text
Core Domains
Core Objects
Core Services
Core Events
Core Contracts
Core APIs
Core Knowledge
Core Workflow Contracts
Core Agent Contracts
Core Consumption Contracts
Codex Task Contracts
```

A Core Consumer shall not redefine:

```text
Core meaning
domain ownership
object lifecycle
service responsibility
event semantics
permission rules
AI governance
workflow state rules
MVP boundary
deferred scope
```

The canonical rule is:

```text
Consume, do not redefine.
Contract before consumption.
```

---

# 4. Core Consumption Statement

Book 02 uses the following statement:

```text
Core Consumption defines how products, Workplaces, AI agents, services, integrations and Codex consume Core without redefining Core meaning.
```

This statement contains five constraints:

```text
1. Consumption must be explicit.
2. Consumption must be contract-bound.
3. Consumption must respect ownership.
4. Consumption must preserve Core semantics.
5. Consumption must follow MVP and deferred-scope boundaries.
```

---

# 5. Consumption Principles

Core Consumption follows eight principles.

```text
C1 — Consume, Do Not Redefine
C2 — Contract Before Consumption
C3 — Read and Write Boundaries Must Be Explicit
C4 — Services Mediate State Change
C5 — Events Communicate Meaningful Change
C6 — AI Requires Agent Contract
C7 — Codex Requires Source Specifications
C8 — Future Consumers Do Not Expand MVP Scope Automatically
```

These principles apply to all consumers.

---

# 6. Consumer Categories

Book 02 recognizes seven consumer categories.

```text
Product Consumer
Workplace Consumer
AI Agent Consumer
Internal Service Consumer
External Integration Consumer
Data / Reporting Consumer
Codex Implementation Consumer
```

Each category has different rules.

---

# 7. Product Consumer

A Product Consumer is a product that uses Core to deliver user-facing functionality.

Examples:

```text
MarkReg
MarkOrbit Lite
Partner Center
Client Portal
Service Platform
Brand Asset Vault
Opportunity Engine
MGSN product surfaces
```

## 7.1 Product May Own

Products may own:

```text
screens
forms
navigation
copywriting
onboarding
product-specific journey
presentation logic
product dashboards
product packaging
commercial experience
```

## 7.2 Product Must Consume

Products must consume:

```text
Core Objects
Core Services
Core Events
Core APIs
Core Contracts
Core Knowledge
Core Workflow Contracts
AI Agent Contracts
```

## 7.3 Product Must Not Redefine

Products must not redefine:

```text
Customer
Trademark
Jurisdiction
Classification
Document
Order
Matter
Task
Event
Agent
AI Output
Review
Workflow Contract
```

## 7.4 Product Consumption Contract

A product requires a Core Consumption Contract when it:

```text
reads Core Objects
writes or mutates Core state
invokes Core Services
subscribes to Core Events
uses AI agents
exposes Core data to users
exports Core data
creates workflow actions
```

---

# 8. Workplace Consumer

A Workplace Consumer operates professional work.

Workplace is a special consumer because it coordinates human execution.

Workplace may consume:

```text
Identity
User
Permission
Matter
Task
Event
Workflow Contract
Review
Business Responsibility
Notification
AI Output
Audit
```

Workplace may own:

```text
queues
task boards
review screens
daily work view
assignment experience
operational dashboards
collaboration panels
```

Workplace must not redefine:

```text
Task meaning
Matter lifecycle
Event semantics
Review requirement
Workflow states
Responsibility rules
AI output review status
```

Workplace consumption must be governed by:

```text
Workflow Contract
Task Service Contract
Event Subscription Contract
Permission Rules
Responsibility Rules
AI Review Rules
```

---

# 9. AI Agent Consumer

An AI Agent Consumer is a governed AI actor that consumes Core context and produces controlled outputs.

AI agents may consume:

```text
authorized Knowledge
allowed Core Objects
structured Context
approved Service outputs
Workflow state
Document text
Classification data
Trademark status data
communication context
```

AI agents may produce:

```text
AI Output
AI Recommendation
AI Summary
AI Draft
AI Classification Suggestion
AI Routing Suggestion
AI Review Note
Codex Implementation Suggestion
```

AI agents require:

```text
AI Agent Identity
Agent Contract
Authorized Knowledge
Allowed Object Access
Allowed Services
Prohibited Capabilities
Risk Level
Human Review Rule
Event Rules
Audit Rules
Failure Behavior
Product Consumer Binding
```

AI agents must not:

```text
own professional truth
bypass review
mutate Core state directly
access unauthorized knowledge
invent domain meanings
create unapproved workflow states
expand MVP scope
```

The rule is:

```text
No Agent Contract, no AI Core consumption.
```

---

# 10. Internal Service Consumer

An Internal Service Consumer is a platform service that consumes Core to perform internal operations.

Examples:

```text
classification service
document generation service
order conversion service
task assignment service
event publishing service
notification service
routing service
knowledge retrieval service
audit service
```

Internal services may consume Core Objects and emit Events, but they must do so through Service Specifications.

Internal services must declare:

```text
owning domain or cross-cutting system
objects read
objects created or updated
events emitted
contracts required
permission and policy requirements
failure behavior
idempotency rules
audit rules
```

Internal services must not become hidden owners of Core meaning.

---

# 11. External Integration Consumer

An External Integration Consumer connects MarkOrbit with external systems.

Examples:

```text
trademark office data connector
email connector
calendar connector
payment connector
document signing connector
cloud storage connector
foreign agent system connector
AI model provider connector
CRM connector
```

External integrations may consume or provide data through contracts.

They must not directly define Core meaning.

External integrations require:

```text
Integration Contract
API Contract
Data Contract
Permission Rule
Event Side Effect Rule
Audit Rule
Error Handling Rule
Vendor Mapping Rule
```

External integrations must not:

```text
write Core state without service mediation
expose private fields
reinterpret object status
bypass permission
create vendor-specific Core semantics
```

Vendor-specific behavior belongs to implementation adapters, not Core meaning.

---

# 12. Data / Reporting Consumer

A Data or Reporting Consumer uses Core data, Events or audit records to produce analysis.

Examples:

```text
operational dashboards
business reports
case statistics
agent performance reports
workflow analytics
deadline reports
customer portfolio reports
AI usage reports
```

Reporting may consume:

```text
Core Events
Data Contracts
Audit Records
Object snapshots
Service outputs
Status histories
```

Reporting must not redefine:

```text
object meaning
event meaning
status vocabulary
workflow state
professional judgment
```

If reporting requires a new status, field or event, it must request Core governance review.

Reporting consumes Core.

Reporting does not define Core.

---

# 13. Codex Implementation Consumer

Codex is a special Core Consumer.

Codex consumes specifications and produces implementation artifacts.

Codex may consume:

```text
Book 02 manuscript
Appendices
indexes/
core-specs/
MVP Execution Matrix
Codex Task Index
Codex Task files
```

Codex may produce:

```text
repository scaffolds
domain spec templates
object spec templates
service code
event code
contract tests
fixtures
documentation
implementation notes
```

Codex must not invent:

```text
Core domains
Core object meanings
service responsibilities
event semantics
AI authority
product ownership boundaries
workflow states
deferred features
```

Every Codex task must include:

```text
source specifications
dependencies
scope
out-of-scope items
expected output
tests required
acceptance criteria
prohibited overreach
status
```

The rule is:

```text
Codex consumes approved specifications.
Codex does not define Core architecture.
```

---

# 14. Consumer Priority Classification

Consumers are classified by MVP readiness.

## 14.1 MVP Consumers

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

MVP Consumers shape the first executable Core kernel.

## 14.2 Partial Consumers

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

Partial Consumers require reserved or partial Core support but shall not pull full future product scope into MVP.

## 14.3 Future Consumers

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

Future Consumers may be supported by future Core extensions.

They do not define MVP scope.

---

# 15. Consumption Modes

A consumer may consume Core through different modes.

```text
Read
Write
Invoke
Subscribe
Publish
Extend
Export
Implement
```

## 15.1 Read

The consumer reads Core data or context.

Requires:

```text
Data Contract
Permission Rule
Field Exposure Rule
Audit Rule where needed
```

## 15.2 Write

The consumer creates or updates Core state.

Requires:

```text
Service Specification
Permission Rule
Policy Rule
Validation Rule
Event Rule
Audit Rule
```

## 15.3 Invoke

The consumer calls a Core Service or AI Agent.

Requires:

```text
Service Contract
API Contract where exposed
Agent Contract where AI is involved
Failure Behavior
Review Rule where required
```

## 15.4 Subscribe

The consumer listens to Core Events.

Requires:

```text
Event Contract
Subscription Rule
Payload Exposure Rule
Permission Rule
Retention Rule
```

## 15.5 Publish

The consumer publishes a Core Event.

Requires:

```text
source domain authority
event specification
payload contract
audit rule
idempotency rule
```

## 15.6 Extend

The consumer requests new Core capability.

Requires:

```text
architecture issue
boundary review
spec update
appendix/index update
core-specs update
Codex task where approved
```

## 15.7 Export

The consumer exports Core data outside the platform.

Requires:

```text
Export Contract
Permission Rule
Privacy Rule
Data Scope Rule
Audit Rule
```

## 15.8 Implement

Codex or engineering implements Core specs.

Requires:

```text
Codex Task
source specs
tests
acceptance criteria
review
```

---

# 16. Consumption Contract Types

Core Consumption may require multiple contract types.

```text
Data Contract
API Contract
Event Contract
Agent Contract
Workflow Contract
Consumption Contract
Integration Contract
Export Contract
Codex Task Contract
```

## 16.1 Data Contract

Defines what data may be read or exported.

## 16.2 API Contract

Defines the API surface, input, output, permissions and side effects.

## 16.3 Event Contract

Defines event payload, timing, consumers and retention.

## 16.4 Agent Contract

Defines what an AI Agent may do.

## 16.5 Workflow Contract

Defines states, transitions, roles and review requirements.

## 16.6 Consumption Contract

Defines how a product or Workplace consumes Core.

## 16.7 Integration Contract

Defines how an external system exchanges data or actions.

## 16.8 Export Contract

Defines controlled external data export.

## 16.9 Codex Task Contract

Defines how Codex implements approved specs.

---

# 17. Core Consumption Specification Template

Each Core Consumption Specification should follow this template.

```text
# Core Consumption Specification

1. Consumer Identity
2. Consumer Type
3. Consumer Priority Classification
4. Consumption Purpose
5. Core Domains Consumed
6. Core Objects Consumed
7. Core Services Invoked
8. Core Events Subscribed To
9. Core Events Published
10. Contracts Required
11. Permissions Required
12. Policy Requirements
13. Knowledge Access
14. AI Usage
15. Workflow Usage
16. Read Boundary
17. Write Boundary
18. Export Boundary
19. Data Exposure Rules
20. Audit Requirements
21. Failure Behavior
22. Deferred Scope
23. Prohibited Redefinitions
24. Acceptance Criteria
25. Revision Notes
```

This template should be used for product, Workplace, AI, integration and Codex consumption planning.

---

# 18. Read Boundary

Read boundary defines what a consumer may see.

A read boundary must specify:

```text
objects readable
fields readable
context readable
events readable
knowledge readable
documents readable
AI outputs readable
permission required
redaction rules
audit requirements
```

A consumer must not assume access to internal fields merely because a Core Object exists.

---

# 19. Write Boundary

Write boundary defines what a consumer may change.

A write boundary must specify:

```text
objects writable
allowed state transitions
services required for mutation
events emitted
review requirement
permission required
policy required
audit requirement
failure behavior
```

A consumer must not write Core state directly without a governed service.

---

# 20. AI Consumption Boundary

AI consumption requires special control.

An AI Agent may only consume Core under an Agent Contract.

The Agent Contract must define:

```text
authorized knowledge
allowed objects
allowed services
allowed tools
allowed outputs
prohibited outputs
risk level
human review requirement
audit rule
events emitted
failure behavior
```

AI output must have a status.

Example statuses:

```text
Draft
Recommendation
ReviewRequired
ReviewApproved
ReviewRejected
Expired
Superseded
```

AI-generated output is not professional truth until approved where review is required.

---

# 21. Workflow Consumption Boundary

Workflow consumption must use Workflow Contracts.

A product or Workplace may present workflow experience, but workflow state rules must be Core-governed.

Workflow consumption must define:

```text
workflow contract
allowed states
allowed transitions
actors
responsibility
review points
events
notifications
failure handling
audit
```

Workflow rules must not be hidden inside UI.

---

# 22. API Consumption Boundary

API consumption must use API Contracts.

An API is not simply a route.

An API is a governed exposure of Core Services, Core Objects or Core Events.

API consumption must define:

```text
API name
owning domain/service
consumer
input contract
output contract
permission requirement
policy requirement
event side effects
rate or usage constraints where needed
audit requirement
MVP status
```

Appendix F must define the API Index before `core-specs/api/` is expanded.

---

# 23. Event Consumption Boundary

Event consumption must use Event Contracts.

Consumers may subscribe to events only when they are authorized.

Event consumption must define:

```text
event name
source domain
payload fields exposed
consumer
purpose
permission
downstream action
idempotency
retention
replay rule
audit
```

Consumers must not reinterpret event meaning.

---

# 24. Knowledge Consumption Boundary

Knowledge consumption must be governed.

Consumers may use Knowledge Sources and Knowledge Assets only according to their authorized scope.

Knowledge consumption must define:

```text
knowledge source
knowledge asset type
consumer
purpose
retrieval method
validation status
AI authorization
jurisdiction scope
update rule
review requirement
```

AI may not treat unvalidated generated content as validated knowledge.

---

# 25. Product-Specific Consumption Examples

## 25.1 MarkReg

MarkReg may consume:

```text
Customer
Trademark
Jurisdiction
Classification
Document
Evidence
Order
Matter
Workflow Contract
Task
Event
Agent
Communication
AI Governance
```

Required contracts:

```text
MarkReg Core Consumption Contract
Matter Workflow Contract
Document Data Contract
Event Subscription Contract
Agent Communication Contract
AI Agent Contracts where AI is used
```

## 25.2 MarkOrbit Lite

Lite may consume:

```text
Identity
Customer
Brand
Trademark
Jurisdiction
Classification
Knowledge
Document
Order
AI Governance
```

Required contracts:

```text
Lite Core Consumption Contract
Guided Intake Consumption Contract
Classification Recommendation API Contract
Document Requirement Contract
AI Consultation Agent Contract
```

## 25.3 Workplace

Workplace may consume:

```text
Matter
Task
Event
Workflow Contract
Review
Notification
Business Responsibility
AI Output
Audit
```

Required contracts:

```text
Workplace Core Consumption Contract
Task Service Contract
Workflow Contract
Review Contract
Event Subscription Contract
AI Review Contract
```

## 25.4 MGSN

MGSN may consume:

```text
Partner
Agent
Service Provider
Service Network
Routing
Communication
Capability
Business Responsibility
```

MGSN is partial or reserved in MVP.

Required contracts:

```text
MGSN Core Consumption Contract
Routing Contract
Agent Contract
Service Provider Contract
Network Communication Contract
```

---

# 26. Prohibited Consumption Patterns

The following consumption patterns are prohibited.

## 26.1 Product Redefines Core Meaning

A product creates its own meaning for Matter, Task, Event or Trademark.

Correction:

```text
Use Core Object and Core Service specifications.
```

## 26.2 Direct Database Consumption

A consumer reads tables directly and bypasses contracts.

Correction:

```text
Use Data Contract or API Contract.
```

## 26.3 Direct State Mutation

A product or integration changes Core state without a service.

Correction:

```text
Use governed Core Service.
```

## 26.4 Event Reinterpretation

A consumer treats an event as meaning something different from its Event Specification.

Correction:

```text
Use Event Contract and source-domain definition.
```

## 26.5 Prompt-Only AI Consumption

AI consumes Core context without Agent Contract.

Correction:

```text
Define AI Agent Identity and Agent Contract.
```

## 26.6 Hidden Workflow Rules

Workflow logic is embedded inside UI.

Correction:

```text
Use Workflow Contract.
```

## 26.7 Codex Overreach

Codex creates architecture beyond approved specs.

Correction:

```text
Use Codex Task Contract and prohibited-overreach section.
```

## 26.8 Future Scope Leakage

Future products pull advanced features into MVP.

Correction:

```text
Use MVP / Partial / Future classification.
```

---

# 27. Consumption Governance

Consumption governance is required when a consumer:

```text
requests new Core access
requests write authority
requests AI access
requests event subscription
requests data export
requests external integration
requests new API surface
requests future product expansion
```

Governance process:

```text
Consumption need identified
        ↓
Consumer type and priority classified
        ↓
Read/write/invoke/export boundaries defined
        ↓
Required contracts identified
        ↓
Security, permission and policy reviewed
        ↓
AI/review/audit rules defined where needed
        ↓
Appendix/index updated
        ↓
core-specs updated
        ↓
Codex task generated if approved
```

---

# 28. Relationship to Appendix F and Appendix H

Appendix F — API Index must define API consumption surfaces.

Appendix H — Codex Task Index must define Codex implementation consumption.

This chapter provides the rules that Appendix F and Appendix H must enforce.

Appendix F should include:

```text
API name
owning domain/service
consumer
input contract
output contract
permission requirement
event side effects
MVP status
future status
```

Appendix H should include:

```text
task ID
wave
source specs
consumer
dependencies
expected outputs
tests
acceptance criteria
prohibited overreach
status
```

---

# 29. Relationship to core-specs/

This chapter governs future consumption specs under `core-specs/`.

Expected future files may include:

```text
core-specs/contracts/markreg-core-consumption.md
core-specs/contracts/lite-core-consumption.md
core-specs/contracts/workplace-core-consumption.md
core-specs/contracts/mgsn-core-consumption.md
core-specs/contracts/ai-agent-consumption.md
core-specs/contracts/external-integration-consumption.md
core-specs/api/_template.md
core-specs/agents/_template.md
```

Detailed files should not be generated until appendices and indexes are complete.

---

# 30. Specification Output

This chapter produces the following specification outputs:

```text
Core Consumption Definition
Core Consumption Statement
Consumer Categories
Consumer Priority Classification
Consumption Modes
Consumption Contract Types
Core Consumption Specification Template
Read Boundary Rules
Write Boundary Rules
AI Consumption Boundary
Workflow Consumption Boundary
API Consumption Boundary
Event Consumption Boundary
Knowledge Consumption Boundary
Product-Specific Consumption Examples
Prohibited Consumption Patterns
Consumption Governance Process
Appendix F and Appendix H Requirements
core-specs/ Consumption Readiness
```

---

# 31. Execution Mapping

| Consumption Rule | Execution Impact |
|------------------|------------------|
| Consume, do not redefine | Product contracts required |
| Contract before consumption | Data/API/Event/Agent/Workflow contracts required |
| Read boundary explicit | Field exposure and permission rules required |
| Write boundary explicit | Service-mediated mutation required |
| AI requires Agent Contract | AI agents need identity, risk, review and audit |
| Workflow requires Workflow Contract | UI cannot own workflow state rules |
| API is governed exposure | API Index and API specs required |
| Event consumption requires contract | Event subscribers need authorization |
| Codex consumes specs | Codex tasks need source specs and prohibited overreach |
| Future consumers do not expand MVP | Consumer priority classification required |

---

# 32. Exclusions

This chapter does not define:

```text
final API routes
full object field schemas
full event payload schemas
complete product UI
full external connector implementation
production AI prompts
final data warehouse design
full marketplace consumption model
implementation tickets
```

Those belong to appendices, `core-specs/`, product books or implementation documents.

---

# 33. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It defines Core Consumption clearly.
[ ] It states Consume, do not redefine.
[ ] It states Contract before consumption.
[ ] It defines consumer categories.
[ ] It classifies consumers as MVP / Partial / Future.
[ ] It defines read boundary.
[ ] It defines write boundary.
[ ] It defines AI consumption boundary.
[ ] It defines Workflow consumption boundary.
[ ] It defines API consumption boundary.
[ ] It defines Event consumption boundary.
[ ] It defines Knowledge consumption boundary.
[ ] It provides a Core Consumption Specification Template.
[ ] It includes product-specific consumption examples.
[ ] It defines prohibited consumption patterns.
[ ] It links consumption to Appendix F and Appendix H.
[ ] It prepares future core-specs/contracts/ and core-specs/api/.
[ ] It prevents products, AI and Codex from redefining Core.
[ ] It protects MVP from future-scope leakage.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 34. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 27, defining Core Consumption. |
| 0.2.0 | Draft | Second canonical draft rewrite. Strengthened consumer categories, contract-before-consumption rules, read/write/API/event/AI/workflow/knowledge boundaries, consumer priority classification and Appendix F/H readiness. |

---

**End of Chapter**
