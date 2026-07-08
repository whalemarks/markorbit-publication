# Book 02

# 05 — Core Principles

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-05  
**Chapter Title:** Core Principles  
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

This chapter defines the Core Principles of MarkOrbit.

Chapter 03 defined the position of the Core.

Chapter 04 defined the boundary of the Core.

This chapter defines the principles that govern how the Core should be designed, specified, consumed, implemented and evolved.

Principles are not slogans.

In Book 02, principles are architecture constraints.

They determine:

```text
what Core may define
what Core must not own
how products consume Core
how AI is governed
how Codex implements
how domains are classified
how objects are specified
how services operate
how events represent change
how contracts protect boundaries
how MVP scope is controlled
how future extensions are governed
```

Without principles, the Core becomes a collection of features.

With principles, the Core becomes a stable kernel.

---

# 2. Core Question

This chapter answers one question:

> What principles must govern the MarkOrbit Core so that it remains stable, reusable, professional and executable?

The answer is:

> The MarkOrbit Core must be governed by principles that keep professional meaning above implementation, shared architecture above products, contracts before consumption, governance before automation and specifications before Codex execution.

---

# 3. Core Principle Statement

The Core Principles are summarized as follows:

```text
Principles define.
Core provides.
Business owns.
Execution coordinates.
Integration connects.
Products consume.
AI assists under governance.
Codex implements approved specifications.
```

This statement is the governing logic of Book 02.

It means:

```text
Principles define the architecture.
Core provides shared primitives and contracts.
Business owns commercial and professional responsibility.
Execution coordinates work through tasks, events, states and workflows.
Integration connects external systems through contracts.
Products consume Core to deliver experiences.
AI assists through governed Agent Contracts.
Codex implements only approved specifications.
```

No later layer may reverse this order.

---

# 4. Principle System

Book 02 uses thirteen Core Principles.

```text
P1 — Core Before Product
P2 — Meaning Before Data
P3 — Boundary Before Detail
P4 — Domain Before Object
P5 — Object Before Service
P6 — Service Before Automation
P7 — Event Before Coordination
P8 — Contract Before Consumption
P9 — Governance Before AI
P10 — Responsibility Before Delegation
P11 — Appendix Before core-specs
P12 — Specification Before Codex
P13 — MVP Before Expansion
```

These principles apply to:

```text
manuscript chapters
appendices
indexes
core-specs/
Codex tasks
implementation
product books
AI agents
workflow design
integration design
```

---

# 5. P1 — Core Before Product

## Principle

```text
Core meaning must be defined before product experience consumes it.
```

## Explanation

Products may differ in interface, audience, workflow, pricing, packaging and delivery.

But they should share the same Core meanings.

For example:

```text
MarkReg may show a Matter in a professional case dashboard.
MarkOrbit Lite may hide Matter behind a simplified client journey.
Workplace may show Matter in a work queue.
MGSN may use Matter for network collaboration.
```

The product experience differs.

The Core meaning of Matter remains stable.

## Required Behavior

Products must consume Core through:

```text
Core Objects
Core Services
Core Events
Core Contracts
Core Consumption Contracts
```

## Prohibited Behavior

Products must not redefine:

```text
Trademark
Customer
Order
Matter
Task
Event
Document
Agent
Routing
AI Output
```

## Execution Implication

Before a product feature is implemented, check whether it needs:

```text
a Core Object
a Core Service
a Core Event
a Core Contract
a Core Consumption rule
```

---

# 6. P2 — Meaning Before Data

## Principle

```text
Core meaning must be defined before data structures become authoritative.
```

## Explanation

A database table stores information.

A Core Object defines professional meaning.

The Core must not be reduced to schemas.

For example:

```text
a trademark row is data
a Trademark Object is Core meaning
a Trademark Service governs use
a Trademark Event records meaningful change
a Trademark Contract governs consumption
```

## Required Behavior

Object specifications must define:

```text
owning domain
meaning
identity
lifecycle
relationships
state
permissions
audit
events
product consumers
```

before implementation treats the object as authoritative.

## Prohibited Behavior

Do not let:

```text
database schema
spreadsheet fields
DTO shape
API response shape
legacy data import
```

define Core meaning.

## Execution Implication

`core-specs/objects/` must precede final database authority.

---

# 7. P3 — Boundary Before Detail

## Principle

```text
The Core boundary must be clear before detailed specifications are created.
```

## Explanation

Details are dangerous when the boundary is unclear.

A detailed object field may accidentally encode product logic.

A service may accidentally own pricing.

An event may become an analytics log.

An AI agent may become a professional decision maker.

Boundary must come first.

## Required Behavior

Before writing detailed specs, confirm:

```text
what Core owns
what product owns
what Workplace owns
what AI may do
what Codex may implement
what remains deferred
```

## Prohibited Behavior

Do not create detailed specs that blur:

```text
Core vs Product
Core vs Workplace
Core vs AI
Core vs Codex
Core vs Business Policy
Core vs Vendor Integration
Core vs Reporting
```

## Execution Implication

Chapter 04 and Appendix A/B must be considered before generating detailed `core-specs/`.

---

# 8. P4 — Domain Before Object

## Principle

```text
Every Core Object must belong to an owning domain or an explicitly defined cross-cutting system.
```

## Explanation

Objects without domain ownership become unstable.

If no domain owns an object, no one governs its meaning, lifecycle, permissions, services or events.

## Required Behavior

Every Core Object must declare:

```text
owning domain
or cross-cutting specification system
object purpose
relationships
lifecycle
events
services
contracts
```

Examples:

```text
Trademark belongs to Trademark Domain.
Matter belongs to Matter Domain.
Task belongs to Task Domain.
Agent Contract belongs to AI Governance / Contract system.
Capability belongs to the cross-cutting Capability system.
Responsibility Assignment belongs to the cross-cutting Business Responsibility system.
```

## Prohibited Behavior

Do not create:

```text
floating objects
product-local duplicates
unowned AI output objects
database-only objects
```

## Execution Implication

Appendix C — Core Object Index must map each object to an owning domain or cross-cutting system.

---

# 9. P5 — Object Before Service

## Principle

```text
Services must operate defined Core Objects and meanings.
```

## Explanation

A Core Service is not a random function.

It is a governed capability that reads, creates, updates, validates, routes, converts, reviews or publishes Core meaning.

## Required Behavior

Before a service is implemented, define:

```text
objects read
objects created
objects updated
permission rules
policy rules
events emitted
failure behavior
human review requirement
AI usage boundary
```

## Prohibited Behavior

Do not create services that:

```text
mutate unknown objects
hide state changes
bypass ownership
combine unrelated domains
duplicate product logic
```

## Execution Implication

Appendix D — Core Service Index must map services to objects, events and contracts.

---

# 10. P6 — Service Before Automation

## Principle

```text
Automation must call governed services instead of bypassing Core rules.
```

## Explanation

Automation can improve speed.

But automation without service governance creates invisible risk.

Examples of automation include:

```text
AI classification
document generation
order-to-matter conversion
routing recommendation
notification dispatch
status synchronization
evidence packaging
Codex implementation
```

These must operate through Core Services.

## Required Behavior

Automation must respect:

```text
permission
policy
service contract
event side effects
review requirement
audit requirement
failure behavior
```

## Prohibited Behavior

Do not allow automation to:

```text
write Core Objects directly
bypass human review
skip event emission
ignore permissions
operate without audit
```

## Execution Implication

AI and workflow automation must be attached to Core Services, Agent Contracts or Workflow Contracts.

---

# 11. P7 — Event Before Coordination

## Principle

```text
Meaningful changes must become Core Events before they coordinate downstream behavior.
```

## Explanation

Coordination depends on shared awareness.

If meaningful changes are hidden inside services, UI or data updates, downstream systems cannot reliably respond.

## Required Behavior

Meaningful changes should emit events such as:

```text
TrademarkCreated
TrademarkStatusChanged
CustomerCreated
OrderCreated
OrderConfirmed
OrderConvertedToMatter
MatterCreated
MatterStatusChanged
TaskCreated
TaskAssigned
TaskCompleted
DocumentUploaded
DocumentGenerated
ReviewRequired
ReviewApproved
ReviewRejected
AIRecommendationGenerated
AIRecommendationReviewRequired
RoutingDecisionMade
CommunicationLinked
OpportunityCreated
```

## Prohibited Behavior

Do not treat Events as:

```text
logs
analytics pings
UI clicks
activity feed rows
queue messages without semantic contract
```

## Execution Implication

Appendix E — Event Index must become canonical before event infrastructure expands.

---

# 12. P8 — Contract Before Consumption

## Principle

```text
No consumer should consume Core without a contract.
```

## Explanation

Core consumption without contracts creates fragmentation.

Consumers include:

```text
products
Workplace
AI agents
internal services
external integrations
reporting systems
Codex tasks
```

## Required Behavior

Core consumption must be governed by:

```text
Data Contract
API Contract
Event Contract
Agent Contract
Workflow Contract
Consumption Contract
```

## Prohibited Behavior

Consumers must not:

```text
read internal data directly without contract
write Core state directly
reinterpret object status
redefine event meaning
invoke AI without Agent Contract
consume private fields as public API
```

## Execution Implication

Appendix F and Appendix H must define consumption and Codex task boundaries before implementation.

---

# 13. P9 — Governance Before AI

## Principle

```text
AI must be governed before it is used.
```

## Explanation

AI can assist professional work, but it must not become unbounded authority.

AI is not the Core.

AI is not above the Core.

AI is not a substitute for professional responsibility.

## Required Behavior

AI execution requires:

```text
AI Agent Identity
Agent Contract
Authorized Knowledge
Allowed Object Access
Structured Context
Permission
Policy
Risk Level
Human Review
AI Events
AI Audit
Failure Behavior
Product Consumer Binding
```

## Prohibited Behavior

Do not implement:

```text
prompt-only AI
AI without identity
AI without Agent Contract
AI output without review status
AI mutation without service/event/audit
AI decision without responsibility
```

## Execution Implication

Appendix C must index AI execution objects.

Appendix G must index AI agents.

Chapter 26 and `core-specs/agents/` must govern all AI usage.

---

# 14. P10 — Responsibility Before Delegation

## Principle

```text
Work may be delegated only after responsibility is defined.
```

## Explanation

MarkOrbit work involves professional judgment, client commitments, foreign agents, AI assistance, internal teams and network collaboration.

Delegation without responsibility causes operational and legal risk.

## Required Behavior

Before work is assigned, routed, automated or delegated, define:

```text
owner
assignee
reviewer
approver
responsibility boundary
audit requirement
escalation path
```

Responsibility applies to:

```text
Order
Matter
Task
AI Output
Routing Decision
Document Draft
Evidence Review
Opportunity Follow-up
Communication
```

## Prohibited Behavior

Do not delegate work to:

```text
AI without review responsibility
external agents without routing/responsibility record
internal users without task ownership
services without audit
```

## Execution Implication

Business Responsibility must be treated as a cross-cutting Core specification system.

---

# 15. P11 — Appendix Before core-specs

## Principle

```text
Appendices must stabilize terminology and indexes before detailed core-specs are generated.
```

## Explanation

The manuscript defines architecture.

Appendices stabilize canonical lists.

`core-specs/` defines executable details.

Skipping appendices creates inconsistent specs.

## Required Behavior

Generate appendices in this order:

```text
Appendix A — Glossary
Appendix B — Core Domain Index
Appendix C — Core Object Index
Appendix D — Core Service Index
Appendix E — Event Index
Appendix F — API Index
Appendix G — Agent Index
Appendix H — Codex Task Index
```

## Prohibited Behavior

Do not generate detailed `core-specs/` before appendices A–H are complete.

## Execution Implication

Round 3 and Round 4 review gates must remain active until appendices are complete.

---

# 16. P12 — Specification Before Codex

## Principle

```text
Codex must implement specifications, not invent architecture.
```

## Explanation

Codex can accelerate implementation.

It can also accelerate architecture drift if given ambiguous instructions.

## Required Behavior

Every Codex task must reference:

```text
source specs
MVP execution matrix row
dependencies
in scope
out of scope
implementation instructions
tests required
acceptance criteria
prohibited overreach
```

## Prohibited Behavior

Codex must not invent:

```text
Core domains
Core object meanings
service responsibilities
event semantics
AI authority
product scope
deferred features
```

## Execution Implication

Appendix H and `indexes/codex-task-index.md` must exist before Codex Wave 0 implementation tasks.

---

# 17. P13 — MVP Before Expansion

## Principle

```text
The first executable Core must be smaller than the full MarkOrbit vision.
```

## Explanation

The Core MVP is the first executable kernel.

It should support first consumers without overbuilding future systems.

## Required Behavior

Use four depth types:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

First consumers:

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

Partial consumers:

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

Future consumers:

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

## Prohibited Behavior

Do not build:

```text
full global marketplace
full provider ranking
full opportunity scoring
full brand asset vault
full analytics suite
full external integration platform
full AI autonomy
```

inside Core MVP.

## Execution Implication

Chapter 28–31 and Appendix H must protect MVP scope.

---

# 18. Principle Dependency Flow

The principles follow a dependency order.

```text
Core Before Product
        ↓
Meaning Before Data
        ↓
Boundary Before Detail
        ↓
Domain Before Object
        ↓
Object Before Service
        ↓
Service Before Automation
        ↓
Event Before Coordination
        ↓
Contract Before Consumption
        ↓
Governance Before AI
        ↓
Responsibility Before Delegation
        ↓
Appendix Before core-specs
        ↓
Specification Before Codex
        ↓
MVP Before Expansion
```

This flow should guide rewrite, appendices, `core-specs/` generation and Codex task design.

---

# 19. Principle-to-Artifact Mapping

| Principle | Main Artifact Impact |
|----------|----------------------|
| Core Before Product | Core Consumption Contracts |
| Meaning Before Data | Object Specifications |
| Boundary Before Detail | Boundary chapters and appendices |
| Domain Before Object | Domain Index and Object Index |
| Object Before Service | Service Specifications |
| Service Before Automation | Workflow and AI integration |
| Event Before Coordination | Event Index and Event Contracts |
| Contract Before Consumption | Data/API/Event/Agent/Consumption Contracts |
| Governance Before AI | Agent Index and Agent Contracts |
| Responsibility Before Delegation | Business Responsibility specs |
| Appendix Before core-specs | Appendices A–H |
| Specification Before Codex | Codex Task Index |
| MVP Before Expansion | MVP Boundary and Execution Matrix |

---

# 20. Principle-to-Consumer Mapping

## 20.1 Products

Products must follow:

```text
Core Before Product
Contract Before Consumption
MVP Before Expansion
```

## 20.2 Workplace

Workplace must follow:

```text
Boundary Before Detail
Event Before Coordination
Responsibility Before Delegation
```

## 20.3 AI Agents

AI agents must follow:

```text
Governance Before AI
Responsibility Before Delegation
Service Before Automation
```

## 20.4 Codex

Codex must follow:

```text
Appendix Before core-specs
Specification Before Codex
MVP Before Expansion
```

## 20.5 Integrations

Integrations must follow:

```text
Contract Before Consumption
Meaning Before Data
Event Before Coordination
```

---

# 21. Principle Enforcement

Principles must be enforced through documents and gates.

## 21.1 Manuscript Enforcement

Chapters must not contradict the principles.

## 21.2 Appendix Enforcement

Appendices must convert principles into canonical indexes.

## 21.3 core-specs Enforcement

Detailed specs must include fields and acceptance criteria that reflect the principles.

## 21.4 Codex Enforcement

Codex tasks must include prohibited overreach and acceptance criteria.

## 21.5 Review Enforcement

Architecture review must reject outputs that violate Core Principles.

---

# 22. Common Principle Violations

## Violation 1 — Product defines Core object meaning

Rejected because it violates Core Before Product.

## Violation 2 — Database field becomes professional truth

Rejected because it violates Meaning Before Data.

## Violation 3 — AI prompt becomes Agent Contract

Rejected because it violates Governance Before AI.

## Violation 4 — Hidden state change without event

Rejected because it violates Event Before Coordination.

## Violation 5 — Product consumes internal model directly

Rejected because it violates Contract Before Consumption.

## Violation 6 — Codex creates unapproved domain

Rejected because it violates Specification Before Codex.

## Violation 7 — Future marketplace built into MVP

Rejected because it violates MVP Before Expansion.

---

# 23. Specification Output

This chapter produces the following specification outputs:

```text
Core Principle Statement
13 Core Principles
Principle dependency flow
Principle-to-artifact mapping
Principle-to-consumer mapping
Principle enforcement rules
Common principle violations
```

These outputs govern all later chapters, appendices and implementation tasks.

---

# 24. Execution Mapping

| Principle | Execution Rule |
|----------|----------------|
| Core Before Product | Product features must consume Core through contracts |
| Meaning Before Data | Object specs precede schema authority |
| Boundary Before Detail | Boundary review precedes detailed specs |
| Domain Before Object | Object Index must declare owning domain/system |
| Object Before Service | Services must declare objects operated |
| Service Before Automation | Automation must call governed services |
| Event Before Coordination | Meaningful state changes emit events |
| Contract Before Consumption | Consumers require contracts |
| Governance Before AI | AI requires Agent Contract and audit |
| Responsibility Before Delegation | Assignment/review requires responsibility |
| Appendix Before core-specs | Appendices A–H precede detailed specs |
| Specification Before Codex | Codex tasks reference specs and matrix rows |
| MVP Before Expansion | Deferred scope remains deferred |

---

# 25. Relationship to Appendices

Appendix A must define all principle-related terms.

Appendix B must protect domain classification.

Appendix C must enforce domain-before-object mapping.

Appendix D must enforce object-before-service mapping.

Appendix E must enforce event-before-coordination mapping.

Appendix F must enforce contract-bound API surfaces.

Appendix G must enforce AI governance.

Appendix H must enforce specification-before-Codex and MVP-before-expansion.

---

# 26. Relationship to core-specs/

`core-specs/` must implement these principles through required fields, templates and acceptance criteria.

Examples:

```text
Domain specs must define scope and exclusions.
Object specs must define owning domain and lifecycle.
Service specs must define side effects and events.
Event specs must define source domain and payload contract.
Contract specs must define consumers and prohibited redefinitions.
Agent specs must define allowed/prohibited capabilities.
Workflow specs must define responsibility and review points.
API specs must define input/output contracts and permissions.
```

---

# 27. Exclusions

This chapter shall not define:

```text
full domain list details
object field schemas
service interface details
event payloads
API routes
product UI requirements
commercial pricing
AI prompt templates
deployment design
Codex task files
```

Those belong to later chapters, appendices, `core-specs/` or implementation documents.

---

# 28. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It states the Core Principle Statement clearly.
[ ] It defines the 13 Core Principles.
[ ] It explains each principle in architecture terms.
[ ] It distinguishes principles from slogans.
[ ] It links principles to appendices.
[ ] It links principles to core-specs/.
[ ] It links principles to Codex.
[ ] It protects Core from product-first drift.
[ ] It protects Core from database-first drift.
[ ] It protects Core from prompt-first AI.
[ ] It protects Core from eventless coordination.
[ ] It protects Core from contractless consumption.
[ ] It protects Core from premature MVP expansion.
[ ] It includes principle-to-artifact mapping.
[ ] It includes principle-to-consumer mapping.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 29. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 05, defining the Core principles. |
| 0.2.0 | Draft | Second canonical draft rewrite. Strengthened the principles into enforceable architecture constraints, added 13-principle system, principle dependency flow, principle-to-artifact mapping and principle enforcement rules. |

---

**End of Chapter**
