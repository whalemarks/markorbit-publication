# Book 02

# 04 — Core Boundary

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-04  
**Chapter Title:** Core Boundary  
**Part:** Part I — Core Foundation  
**Chapter Type:** Foundation  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-PLN-0001 — Core Positioning
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines the boundary of the MarkOrbit Core.

Chapter 03 positioned the Core in the MarkOrbit ecosystem. This chapter defines what belongs inside the Core and what must remain outside it.

A Core without boundaries becomes a platform monolith.

A Core with unclear boundaries becomes a source of conflict between products, Workplaces, AI agents, services, data models and implementation teams.

A Core that owns too much slows product development.

A Core that owns too little allows each product to redefine professional meaning.

Therefore, this chapter establishes the boundary rules that govern every later chapter, appendix, `core-specs/` file and Codex task.

The Core boundary answers:

```text
What does Core own?
What does Core provide?
What does Core govern?
What does Core not own?
What must products own?
What must Workplace own?
What must AI never own?
What must Codex never invent?
What belongs to future books or implementation?
```

---

# 2. Core Question

This chapter answers one question:

> Where does the MarkOrbit Core stop?

The answer is:

> The MarkOrbit Core stops at shared professional meaning, execution primitives, governance rules and consumption contracts. It does not extend into product experience, commercial policy, full workflow operation, vendor-specific implementation, autonomous AI judgment or future marketplace execution.

The Core is a kernel.

It is not the whole platform.

---

# 3. Boundary Statement

The MarkOrbit Core owns the shared foundation required for the MarkOrbit ecosystem to operate consistently.

The Core owns:

```text
canonical professional meaning
baseline domain classification
Core Object meaning
Core Service responsibility
Core Event semantics
Core Contract types
Core Execution Primitives
Identity and permission foundations
Knowledge governance
AI capability governance
Core consumption rules
MVP execution boundaries
Codex implementation constraints
```

The Core does not own:

```text
product user interfaces
product-specific user journeys
commercial pricing packages
sales tactics
full workplace experience
complete global service marketplace
vendor-specific integrations
deployment architecture
production prompt libraries
full data warehouse implementation
final professional judgment without human responsibility
```

The Core defines what must be shared.

Other layers define how shared capabilities are experienced, operated, sold, deployed or extended.

---

# 4. Boundary Principle

Book 02 uses the following boundary principle.

```text
Core owns shared meaning.
Business owns commercial responsibility.
Workplace owns operating experience.
Products own user-facing delivery.
Network owns collaboration operation.
AI assists under governance.
Codex implements approved specifications.
Infrastructure runs the system.
```

This principle prevents the Core from becoming:

```text
a product PRD
a UI system
a pricing system
a workflow app
an AI prompt library
a database schema package
a deployment guide
a vendor integration manual
```

The Core must remain small enough to be stable and large enough to prevent fragmentation.

---

# 5. Core Boundary Map

The Core boundary can be mapped as follows.

```text
Professional OS
    defines why professional work operates
        ↓
Core
    defines shared meaning, primitives, contracts and governance
        ↓
Appendices / Indexes
    stabilize terms and specification lists
        ↓
core-specs/
    defines executable domain, object, service, event, contract, API, agent and workflow specs
        ↓
Codex Tasks
    implement approved specs under task contracts
        ↓
Implementation
    realizes specs in code, data, APIs, tests and infrastructure
        ↓
Products / Workplace / Network
    deliver user-facing and operational experience
```

The Core must not collapse these layers into one document.

---

# 6. Core Owns

The Core owns the following areas.

## 6.1 Canonical Meaning

The Core defines stable meanings for shared professional concepts.

Examples:

```text
Identity
Organization
User
Permission
Knowledge
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
Customer
Order
Matter
Task
Event
Workflow Contract
Agent
Service Provider
Routing
Communication
```

Products may display these concepts differently. They shall not redefine their Core meaning.

## 6.2 Domain Classification

The Core owns the baseline domain map.

The canonical baseline domain map contains 26 domains grouped into:

```text
Foundation Domains
Professional Domains
Business Execution Domains
Collaboration Network Domains
```

The Core also recognizes cross-cutting specification systems such as Capability and Business Responsibility.

These cross-cutting systems may produce executable specs, but they do not silently change the baseline domain count.

## 6.3 Core Objects

The Core owns the meaning and lifecycle of Core Objects.

A Core Object is not merely a database table.

A Core Object defines:

```text
identity
meaning
owning domain
relationships
lifecycle
state
permissions
audit requirements
service usage
event relationships
AI usage boundaries
product consumption boundaries
```

## 6.4 Core Services

The Core owns service responsibility.

A Core Service is a governed capability that operates Core meaning.

A Core Service is not merely a helper function, UI button or controller method.

The Core defines:

```text
service purpose
owning domain
inputs
outputs
objects read
objects created or updated
side effects
events emitted
permission rules
policy rules
failure behavior
AI usage
human review rules
```

## 6.5 Core Events

The Core owns event semantics.

A Core Event is a meaningful change in Core state or professional execution.

A Core Event is not merely:

```text
a log line
a UI click
an activity feed row
a queue message
an analytics ping
```

The Core defines source domain, trigger, payload contract, related objects, actor or source, downstream consumers, audit rules, retention and replay rules.

## 6.6 Core Contracts

The Core owns contract types and consumption boundaries.

Core Contracts include:

```text
Data Contract
API Contract
Event Contract
Agent Contract
Workflow Contract
Consumption Contract
```

Contracts protect the Core from uncontrolled use.

## 6.7 Execution Primitives

The Core owns baseline execution primitives.

```text
Identity
Context
State
Task
Event
Workflow Contract
Review
Notification
Audit
```

Workplace and products may operate or display these primitives. They shall not redefine them.

## 6.8 AI Governance

The Core owns AI governance.

The Core defines:

```text
AI Agent Identity
Agent Contract
Authorized Knowledge
Allowed Object Access
Permission and Policy
Risk Level
Human Review
AI Events
AI Audit
Failure Behavior
Product Consumer Binding
```

AI may assist execution. AI shall not become ungoverned authority.

## 6.9 Consumption Rules

The Core owns consumption rules.

Every product, Workplace, AI agent, integration or Codex task must consume Core through defined boundaries.

The rule is:

```text
Consume, do not redefine.
Contract before consumption.
```

---

# 7. Core Does Not Own

The Core deliberately does not own the following areas.

## 7.1 Product User Interface

Core does not own pages, forms, menus, dashboards, navigation, visual design, interaction copy, onboarding screens or customer-facing layouts.

Products own UI. Core defines the meaning that UI consumes.

## 7.2 Product-Specific User Journeys

Core does not own each product’s detailed user journey.

MarkOrbit Lite may design a simplified guided intake flow. MarkReg may design professional case operation views. MGSN may design agent collaboration workflows.

These product journeys must consume Core, not redefine it.

## 7.3 Commercial Pricing and Packaging

Core does not own pricing packages, discount rules, margin policy, sales commission, partner rebate, payment strategy or commercial campaign design.

Core may support Order, Service, Capability and Responsibility structures. Commercial policy belongs to business and product layers.

## 7.4 Full Workplace Experience

Core does not own complete Workplace experience.

Core owns primitives such as Task, Event, Matter, Workflow Contract and Review.

Workplace owns work queues, review screens, assignment experience, operational dashboards, collaboration views and human work coordination experience.

## 7.5 Full Network Marketplace

Core does not own the full global service marketplace.

Core may define Partner, Agent, Service Provider, Service Network, Routing and Communication foundations.

Book 06 defines full MGSN operation.

## 7.6 Vendor-Specific Integrations

Core does not own vendor-specific implementation details.

Examples include email providers, payment providers, CRM connectors, cloud vendors, AI model providers and trademark office data connectors.

Core may define integration contracts. Implementations may adapt to vendors.

## 7.7 Production Prompt Library

Core does not own production prompts.

Core owns AI Agent Contracts and governance.

Prompt libraries may belong to AI implementation or product layers, but must conform to Agent Contracts.

## 7.8 Deployment Architecture

Core does not own infrastructure deployment design.

It does not define cloud provider, container strategy, CI/CD pipeline, runtime environment, scaling policy, observability stack or secrets management implementation.

## 7.9 Full Data Warehouse

Core does not own full analytics or data warehouse implementation.

Core defines object meaning, event semantics and contracts.

Reporting and analytics may consume Core data through approved contracts.

## 7.10 Final Professional Judgment Without Responsibility

Core does not automate final professional judgment without responsibility.

AI may assist. Services may recommend. Workflows may route.

But professional judgment must remain tied to responsibility, review and audit where required.

---

# 8. Boundary with Book 01 — Professional OS

Book 01 defines professional operating philosophy.

Book 02 does not redefine that philosophy.

The boundary is:

```text
Book 01 explains professional value.
Book 02 defines the Core structure that makes professional value executable.
```

Book 01 owns professional worldview, value flow, judgment logic and professional operating philosophy.

Book 02 owns Core domains, objects, services, events, contracts, execution primitives, AI governance and MVP boundary.

---

# 9. Boundary with Book 03 — Workplace Framework

Book 03 defines Workplace.

The boundary is:

```text
Core provides execution primitives.
Workplace operates professional work.
```

Core owns Task meaning, Event semantics, Matter meaning, Workflow Contract structure, Review requirement, Notification baseline, Business Responsibility rules, AI Output governance and Audit baseline.

Workplace owns queue design, task boards, review interface, daily work views, operational dashboards, coordination experience and human-in-the-loop workflow experience.

Workplace can request Core extensions through governance. Workplace cannot redefine Task, Event, Matter, Review or Workflow Contract.

---

# 10. Boundary with Product Books

Products consume Core. They may extend experience and product-specific workflows. They must not redefine Core meaning.

## 10.1 MarkReg Boundary

MarkReg may own:

```text
case operation views
trademark service workflows
document preparation screens
status tracking pages
agent communication experience
professional case dashboard
```

Core owns Trademark, Jurisdiction, Classification, Document, Evidence, Customer, Order, Matter, Task, Event, Workflow Contract, Agent, Communication and AI Governance.

## 10.2 MarkOrbit Lite Boundary

Lite may own:

```text
guided intake experience
AI-assisted question flow
client-friendly recommendation presentation
simplified order journey
payment or submission experience
```

Core owns Customer, Brand, Trademark, Jurisdiction, Classification, Knowledge, Document Requirement, Order, AI Agent Contract, Review rules and Consumption Contract.

## 10.3 MGSN Boundary

MGSN may own:

```text
network membership design
provider marketplace experience
service exchange mechanism
agent cooperation process
global network trust model
```

Core owns Partner, Agent, Service Provider, Capability, Routing, Communication, Service Network baseline and Consumption Contracts.

In the Core MVP, MGSN should remain partial or reserved unless explicitly approved.

---

# 11. Boundary with Appendices

Appendices are part of Book 02 but have a different role from manuscript chapters.

Manuscript chapters define architecture meaning.

Appendices stabilize reference lists.

Appendices shall include:

```text
Glossary
Core Domain Index
Core Object Index
Core Service Index
Event Index
API Index
Agent Index
Codex Task Index
```

The boundary is:

```text
Manuscript explains.
Appendices canonize.
core-specs/ executes.
```

Appendices must be completed before detailed `core-specs/` generation.

---

# 12. Boundary with core-specs/

`core-specs/` is the executable specification layer.

The boundary is:

```text
Book 02 defines architecture and rules.
core-specs/ defines file-level executable specifications.
```

Book 02 owns what a Domain, Object, Service, Event and Contract mean; what AI governance requires; how Core is consumed; and what MVP boundary applies.

`core-specs/` owns domain spec files, object spec files, service spec files, event spec files, contract spec files, API spec files, agent spec files, workflow spec files, field-level definitions, payload contracts and testable acceptance criteria.

`core-specs/` may detail the Core. It may not redefine Core meaning.

---

# 13. Boundary with Codex

Codex implements approved tasks.

Codex does not define architecture.

The boundary is:

```text
Book 02 and core-specs/ define.
Codex implements.
```

Codex may create folders, templates, models, service code, event code, contract tests, fixtures, documentation and implementation notes.

Codex may not invent new Core domains, new Core object meanings, ungoverned AI behavior, unapproved product scope, hidden state changes or deferred marketplace features.

Each Codex task must reference:

```text
source specs
matrix row
dependencies
in scope
out of scope
tests
acceptance criteria
```

---

# 14. Boundary with AI

AI is inside Core governance but outside Core authority.

AI may execute governed capabilities.

AI may not own professional truth, bypass responsibility or mutate Core state without service, permission, event and audit rules.

The boundary is:

```text
Core governs AI.
AI assists execution.
Humans retain responsibility where required.
```

AI must operate through AI Agent Identity, Agent Contract, Authorized Knowledge, Structured Context, Permission and Policy, Risk Level, Human Review, Events, Audit, Failure Behavior and Product Consumption Boundary.

Prompt-only AI is outside the Core boundary.

---

# 15. Boundary with Data

Data storage is not Core by itself.

The Core defines meaning before data structure.

Boundary examples:

```text
Database table
    is implementation.

Core Object
    is shared professional meaning.

DTO
    is transport structure.

Data Contract
    is governed consumption rule.

Event payload
    is change communication contract.
```

Implementation may store Core Objects. Storage shape does not define Core meaning.

---

# 16. Boundary with Knowledge

Knowledge is a Core foundation, but a knowledge base is not the whole Core.

Core owns:

```text
Knowledge Source
Knowledge Asset
Knowledge Rule
Knowledge Validation
Knowledge Retrieval
Knowledge Gap
AI Knowledge Authorization
```

Knowledge systems may store laws, requirements, country rules, classification references, case notes, templates, agent notes and service knowledge.

Core governs how knowledge is used.

AI-generated content is not validated knowledge unless it passes validation rules.

---

# 17. Boundary with Capability

Capability is a cross-cutting Core specification system.

It may describe what can be done, by whom or by what actor.

Capability may apply to human users, internal teams, AI agents, external agents, service providers, products and workflow roles.

Capability is not counted as an additional baseline Core Domain unless a future architecture release changes the domain map.

Capability may produce:

```text
Capability Object
Capability Provider
Capability Scope
Capability Matching Service
Capability Contract
```

The boundary is:

```text
Capability governs what can be performed.
It does not become a product package or commercial offer by itself.
```

---

# 18. Boundary with Business Responsibility

Business Responsibility is a cross-cutting Core specification system.

It defines accountability for work.

It may apply to order ownership, matter ownership, task assignment, review responsibility, AI output approval, opportunity follow-up, routing approval and network responsibility.

Business Responsibility is not the same as sales commission, pricing policy, revenue attribution or commercial package design.

It may produce:

```text
Responsibility Assignment
Review Record
Approval Service
ReviewRequired Event
Responsibility Contract
```

The boundary is:

```text
Business Responsibility governs who is accountable.
Business policy governs how business value is priced, sold or rewarded.
```

---

# 19. Boundary with Network Collaboration

The Core defines network-capable primitives.

It does not operate the full network marketplace.

Core may define Partner, Agent, Service Provider, Service Network baseline, Routing Decision, Communication, Capability, Responsibility and trust-related primitives.

Book 06 may define network membership, provider onboarding, service exchange, agent marketplace, trust scoring, network operations, cooperation rules and commercial network policies.

Core MVP should reserve future network boundaries without overbuilding them.

---

# 20. Boundary with Business Policy

Business policy belongs to business and product governance.

Core may support business policy through objects and services, but it does not decide business strategy.

Core may support Order, Service Type, Capability, Responsibility, Approval, Audit and Policy Rule baseline.

Core does not own price amount, discount strategy, margin strategy, commission allocation, partner rebate formula, marketing campaign rule or sales incentive design.

Business policy may consume Core structures. It does not redefine Core meaning.

---

# 21. Boundary with External Integrations

External integrations consume or provide data and actions through contracts.

Core may define integration boundaries.

Core does not own vendor-specific adapters.

Examples:

```text
Trademark office data connector
Email connector
Calendar connector
Payment connector
Document signing connector
Cloud storage connector
AI model provider connector
CRM connector
```

Core owns what data means, what contract is required, what permission applies, what event is emitted and what audit is needed.

Integration implementation owns vendor API calls, authentication details, retry strategy, provider-specific mapping, rate limit handling and connector-specific errors.

---

# 22. Boundary with Reporting and Analytics

Reporting consumes Core.

Reporting does not define Core.

Core may define objects, events, audit records, state changes and contracted data exports.

Reporting may produce dashboards, metrics, trend analysis, performance reports, operational charts and business intelligence outputs.

Reporting shall not redefine event meaning or object status.

If a reporting need reveals a missing Core event or field, it must return to Core governance.

---

# 23. Boundary with MVP Scope

Core MVP is the first executable kernel.

It is not the full platform.

The MVP boundary uses four depth types:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

The Core MVP should include enough to support first consumers.

First consumers are:

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

Partial consumers include:

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

Future consumers include:

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

Future consumers do not automatically expand MVP scope.

---

# 24. Boundary with Future Architecture

The Core boundary may evolve.

However, Core evolution must be governed.

A future need may come from product implementation, Workplace operation, AI agent behavior, network collaboration, external integration, reporting need, client workflow or business policy.

But a future need does not automatically change the Core.

The change path is:

```text
Need discovered
        ↓
Architecture issue recorded
        ↓
Core boundary reviewed
        ↓
Spec updated if approved
        ↓
Appendix/index updated
        ↓
core-specs/ updated
        ↓
Codex task generated
        ↓
Implementation changed
```

---

# 25. Boundary Rules

The following boundary rules are established.

## Rule 1 — Core owns shared meaning, not all implementation

Core defines reusable professional meaning and governance. Implementation realizes it.

## Rule 2 — Products consume Core, not redefine Core

Product experience may differ. Core meaning must remain stable.

## Rule 3 — Workplace operates Core primitives

Workplace manages execution experience. It does not redefine Task, Event, Matter or Workflow Contract.

## Rule 4 — AI is governed by Core

AI must operate under Agent Contract, permission, review and audit rules.

## Rule 5 — Codex implements approved specifications

Codex must not invent Core meaning or expand scope.

## Rule 6 — Data structure does not define Core Object meaning

Objects must be specified before schemas become authoritative.

## Rule 7 — Events are semantic changes, not logs

Events must represent meaningful Core or execution changes.

## Rule 8 — Contracts precede consumption

Products, integrations, AI agents and Codex tasks require contracts.

## Rule 9 — Appendices precede detailed core-specs/

Glossary and indexes must stabilize terms before executable specs.

## Rule 10 — Deferred scope remains deferred

Deferred features require explicit architecture approval before implementation.

## Rule 11 — Cross-cutting systems must be classified

Capability and Business Responsibility must not silently alter the baseline domain map.

## Rule 12 — Future consumers do not define MVP scope

Future product names must not pull full future architecture into the MVP.

---

# 26. Boundary Anti-Patterns

The following patterns are prohibited.

## 26.1 Product-First Core

A product screen defines the meaning of a Core Object.

Correction:

```text
Core Object meaning must be defined in Book 02 / core-specs/.
```

## 26.2 Database-First Core

A table schema defines Core meaning before Object Specification exists.

Correction:

```text
Object Specification precedes schema authority.
```

## 26.3 Prompt-First AI

A prompt is treated as an AI agent.

Correction:

```text
Agent Contract precedes AI behavior.
```

## 26.4 Eventless State Change

A meaningful state change happens without Event.

Correction:

```text
Core Service must define event side effects.
```

## 26.5 Workflow Hidden in UI

Workflow rules are hard-coded inside product screens.

Correction:

```text
Workflow Contract defines states and transitions.
```

## 26.6 Marketplace Overbuild

Future MGSN marketplace features enter Core MVP without approval.

Correction:

```text
Use Reserved Boundary or Deferred classification.
```

## 26.7 Codex Architecture Drift

Codex invents domains, objects, events or agents.

Correction:

```text
Codex tasks must reference approved specs and matrix rows.
```

## 26.8 Analytics Redefines Events

Reporting defines its own status or event meaning.

Correction:

```text
Reporting consumes Core Events and requests extensions through governance.
```

---

# 27. Specification Output

This chapter produces the following boundary outputs:

```text
Core Ownership Boundary
Core Exclusion Boundary
Book 01 Boundary
Book 03 Workplace Boundary
Product Book Boundary
Appendix Boundary
core-specs Boundary
Codex Boundary
AI Boundary
Data Boundary
Knowledge Boundary
Capability Boundary
Business Responsibility Boundary
Network Boundary
Business Policy Boundary
External Integration Boundary
Reporting Boundary
MVP Boundary
Future Architecture Boundary
Boundary Rules
Boundary Anti-Patterns
```

These outputs govern later chapters and appendices.

---

# 28. Execution Mapping

Boundary decisions map to execution controls.

| Boundary Decision | Execution Control |
|------------------|------------------|
| Core owns meaning | Domain/Object specs required |
| Products consume Core | Consumption Contracts required |
| Workplace operates primitives | Workflow/Task/Event specs required |
| AI governed by Core | Agent Contracts and audit required |
| Data is not Core by itself | Object specs precede schemas |
| Events are semantic | Event specs precede event bus usage |
| API is contract-bound | API Index and API templates required |
| Future scope deferred | MVP depth classification required |
| Codex cannot invent Core | Codex tasks require source specs |
| Appendices before core-specs/ | Glossary and indexes required first |

---

# 29. Relationship to Appendices

This chapter directly informs the appendices.

Appendix A must define boundary terms.

Appendix B must preserve the domain boundary and cross-cutting system clarification.

Appendix C must index objects without confusing objects with database tables.

Appendix D must index services without confusing services with UI actions.

Appendix E must index events without confusing events with logs.

Appendix F must define API surfaces through contracts.

Appendix G must define AI Agent boundaries.

Appendix H must ensure Codex tasks respect Core boundaries.

---

# 30. Relationship to core-specs/

This chapter governs how `core-specs/` should be generated.

`core-specs/` must not include:

```text
product UI definitions
pricing logic
deployment scripts
vendor-specific adapter details
prompt-only agent definitions
unapproved future marketplace scope
```

`core-specs/` should include:

```text
domain specs
object specs
service specs
event specs
contract specs
API specs
agent specs
workflow specs
acceptance criteria
```

---

# 31. Exclusions

This chapter shall not define:

```text
the complete list of object fields
the full list of service inputs and outputs
final event payloads
database schemas
API endpoint routes
UI designs
workflow screens
product pricing
deployment architecture
production prompts
marketplace policies
```

Those belong to later specification, product or implementation documents.

---

# 32. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It clearly defines what Core owns.
[ ] It clearly defines what Core does not own.
[ ] It distinguishes Core from Book 01.
[ ] It distinguishes Core from Book 03 Workplace.
[ ] It distinguishes Core from product books.
[ ] It distinguishes Core from appendices.
[ ] It distinguishes Core from core-specs/.
[ ] It distinguishes Core from Codex.
[ ] It distinguishes Core from AI.
[ ] It distinguishes Core from data storage.
[ ] It distinguishes Core from knowledge base implementation.
[ ] It classifies Capability as cross-cutting.
[ ] It classifies Business Responsibility as cross-cutting.
[ ] It distinguishes Core from network marketplace operation.
[ ] It distinguishes Core from commercial pricing policy.
[ ] It distinguishes Core from external vendor integrations.
[ ] It distinguishes Core from reporting/analytics.
[ ] It preserves MVP / Partial / Future consumer boundaries.
[ ] It states appendices must precede detailed core-specs/.
[ ] It defines clear boundary anti-patterns.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 33. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 04, defining the Core boundary. |
| 0.2.0 | Draft | Second canonical draft rewrite. Strengthened Core ownership/exclusion boundary, cross-cutting systems clarification, product/Workplace/AI/Codex/data/API/network boundaries, MVP scope protection and appendix-before-core-specs rule. |

---

**End of Chapter**
