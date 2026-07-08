# Book 02

# 29 — MVP Domain Priority

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-29  
**Chapter Title:** MVP Domain Priority  
**Part:** Part IV — Core Execution Boundary  
**Chapter Type:** Execution  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-03 — Core Position
- B02-CH-04 — Core Boundary
- B02-CH-05 — Core Principles
- B02-CH-08 — Ontology and Domain Classification
- B02-CH-13 — Core Domain Architecture
- B02-CH-22 — Domain Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-28 — Core MVP Boundary
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines the MVP priority of MarkOrbit Core Domains.

Chapter 28 defined the Core MVP boundary.

This chapter defines which domains must be implemented first, which domains require partial implementation, which domains should be reserved and which domains must remain deferred.

The purpose of MVP Domain Priority is not to rank domains by importance in the long-term vision.

It is to sequence executable Core construction.

A domain may be strategically important but not MVP-critical.

A domain may be small but foundational.

A domain may be required for future products but should not be implemented deeply in the first kernel.

Therefore, this chapter defines priority according to execution dependency, consumer need, risk, governance and MVP readiness.

---

# 2. Core Question

This chapter answers one question:

> Which Core Domains and cross-cutting systems must be implemented, partially implemented, reserved or deferred in the first executable MarkOrbit Core?

The answer is:

> MVP priority starts from identity, permission and knowledge foundations, then professional trademark objects, then business execution primitives, then limited collaboration and growth domains, while keeping full network, marketplace, analytics and advanced automation outside the MVP.

---

# 3. MVP Priority Statement

Book 02 uses the following MVP priority statement:

```text
MVP priority is determined by executable dependency, not by strategic attractiveness.
```

This means:

```text
Foundational identity comes before product experience.
Knowledge comes before AI recommendation.
Trademark and jurisdiction come before order execution.
Order and matter come before task workflow.
Task and event come before Workplace coordination.
Agent and routing remain partial until execution needs are proven.
Service Network and full marketplace remain reserved.
```

The Core MVP must support first execution without absorbing the whole future platform.

---

# 4. Priority Dimensions

MVP priority is evaluated through eight dimensions.

```text
1. Foundation Dependency
2. Professional Dependency
3. Execution Dependency
4. Consumer Dependency
5. AI Governance Dependency
6. Risk and Review Dependency
7. Network Dependency
8. Future Scope Risk
```

## 4.1 Foundation Dependency

Does the domain enable identity, permission, organization or knowledge?

If yes, it likely belongs early.

## 4.2 Professional Dependency

Does the domain define trademark professional meaning required by MarkReg or Lite?

If yes, it likely belongs early.

## 4.3 Execution Dependency

Does the domain enable order, matter, task, event or workflow execution?

If yes, it likely belongs early.

## 4.4 Consumer Dependency

Is the domain required by MVP Consumers?

MVP Consumers are:

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

## 4.5 AI Governance Dependency

Does AI need this domain to operate safely?

If yes, the domain may need at least partial MVP support.

## 4.6 Risk and Review Dependency

Does the domain require review, audit or responsibility control?

If yes, its governance structures may need to be implemented early.

## 4.7 Network Dependency

Does the domain support agent, service provider, routing or communication?

If yes, it may be partial or reserved depending on MVP need.

## 4.8 Future Scope Risk

Could the domain pull in full future product scope too early?

If yes, it should be Reserved Boundary or Deferred.

---

# 5. MVP Depth Types

Book 02 uses four MVP depth types.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## 5.1 Must Implement

A domain or system is Must Implement when the first executable Core cannot operate without it.

Must Implement items require:

```text
canonical specification
baseline objects
baseline services
baseline events where applicable
permission or policy rules where applicable
tests
acceptance criteria
Codex implementation tasks
```

## 5.2 Partial Implement

A domain or system is Partial Implement when the MVP needs a controlled subset but not the full future design.

Partial Implement items require:

```text
clear scope
reserved future boundary
minimal objects or contracts
limited services where needed
explicit deferred scope
acceptance criteria
```

## 5.3 Reserved Boundary

A domain is Reserved Boundary when the architecture must recognize it, but MVP should not implement it deeply.

Reserved Boundary items require:

```text
name reserved
meaning reserved
relationship reserved
future scope described
implementation blocked unless approved
```

## 5.4 Deferred

A feature or system is Deferred when it is outside MVP and should not be implemented.

Deferred items require:

```text
explicit exclusion
reason for deferral
future trigger condition
prohibited implementation note
```

---

# 6. Baseline Domain Count Rule

The canonical baseline Core Domain Map contains 26 domains.

This chapter does not change the domain count.

Capability and Business Responsibility are included in MVP priority because they affect implementation sequencing.

However, they are cross-cutting Core specification systems.

They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.

Canonical clarification:

```text
26 baseline domains remain canonical.
Capability and Business Responsibility are cross-cutting systems.
MVP priority may schedule cross-cutting systems without changing the domain map.
```

---

# 7. MVP Priority Phases

MVP Domain Priority is organized into five phases.

```text
Phase 1 — Foundation Core
Phase 2 — Professional Core
Phase 3 — Business Execution Core
Phase 4 — Collaboration and Growth Baseline
Phase 5 — Reserved Network and Future Expansion
```

These phases define sequencing, not publication order.

---

# 8. Phase 1 — Foundation Core

Phase 1 establishes identity, authority and knowledge foundations.

## 8.1 Phase 1 Purpose

Phase 1 answers:

```text
Who can act?
For which organization?
Under what permission?
Using what knowledge?
Under what governance?
```

## 8.2 Phase 1 Domains

```text
Identity
Organization
User
Permission
Knowledge
```

## 8.3 Phase 1 Partial Systems

```text
Policy
Capability
Business Responsibility
```

Policy is a baseline domain but may be partial in MVP.

Capability and Business Responsibility are cross-cutting systems.

## 8.4 Phase 1 Priority

| Item | Type | MVP Depth | Rationale |
|------|------|-----------|-----------|
| Identity | Domain | Must Implement | Required for human, system and AI actor identity. |
| Organization | Domain | Must Implement | Required for customer, provider and internal structure. |
| User | Domain | Must Implement | Required for human operation and permission. |
| Permission | Domain | Must Implement | Required before access, service invocation and AI usage. |
| Knowledge | Domain | Must Implement | Required for professional guidance and AI authorization. |
| Policy | Domain | Partial Implement | Needed for baseline constraints, but full policy engine can wait. |
| Capability | Cross-Cutting System | Partial Implement | Needed for AI, routing and service readiness, but not full matching engine. |
| Business Responsibility | Cross-Cutting System | Partial Implement | Needed for ownership, review and accountability, but not full business attribution. |

## 8.5 Phase 1 Deferred Scope

Do not implement in Phase 1:

```text
full enterprise IAM suite
complex role marketplace
full policy rule engine
advanced capability scoring
full responsibility accounting
advanced knowledge automation
full AI knowledge validation pipeline
```

---

# 9. Phase 2 — Professional Core

Phase 2 establishes trademark and brand professional meaning.

## 9.1 Phase 2 Purpose

Phase 2 answers:

```text
What professional objects are being operated?
What jurisdiction rules apply?
What classification rules apply?
What documents are required?
What evidence may be needed?
```

## 9.2 Phase 2 Domains

```text
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
```

## 9.3 Phase 2 Priority

| Item | Type | MVP Depth | Rationale |
|------|------|-----------|-----------|
| Brand | Domain | Must Implement | Required to connect customer intent to trademark assets. |
| Trademark | Domain | Must Implement | Central professional object for MarkReg and Lite. |
| Jurisdiction | Domain | Must Implement | Required for country/office rules and document requirements. |
| Classification | Domain | Must Implement | Required for goods/services recommendation and filing scope. |
| Document | Domain | Must Implement | Required for POA, application materials and official documents. |
| Evidence | Domain | Partial Implement | Required as reserved professional proof structure, but full evidence system can wait. |

## 9.4 Phase 2 Deferred Scope

Do not implement in Phase 2:

```text
full global jurisdiction rule engine
complete Nice and local classification automation
full document assembly platform
advanced evidence scoring
full brand asset vault
full trademark portfolio analytics
```

---

# 10. Phase 3 — Business Execution Core

Phase 3 turns professional meaning into executable work.

## 10.1 Phase 3 Purpose

Phase 3 answers:

```text
Who is the customer?
What has been ordered?
What matter should be executed?
What work must be assigned?
What event has occurred?
What notification is needed?
What workflow governs the work?
```

## 10.2 Phase 3 Domains

```text
Customer
Order
Matter
Workflow Contract
Task
Event
Notification
```

## 10.3 Phase 3 Partial Domains

```text
Opportunity
```

## 10.4 Phase 3 Priority

| Item | Type | MVP Depth | Rationale |
|------|------|-----------|-----------|
| Customer | Domain | Must Implement | Required for service relationship and order context. |
| Order | Domain | Must Implement | Required for intake and service request commitment. |
| Matter | Domain | Must Implement | Required for managed professional execution. |
| Workflow Contract | Domain | Must Implement | Required to govern execution states and transitions. |
| Task | Domain | Must Implement | Required for work assignment and Workplace operation. |
| Event | Domain | Must Implement | Required for meaningful change and coordination. |
| Notification | Domain | Partial Implement | Required for baseline work alerts, but not full notification platform. |
| Opportunity | Domain | Partial Implement | Needed for baseline opportunity signals, but not full opportunity engine. |

## 10.5 Phase 3 Deferred Scope

Do not implement in Phase 3:

```text
full CRM system
full sales pipeline
full opportunity scoring engine
advanced notification preference center
complex workflow designer
full BPM platform
full revenue attribution
```

---

# 11. Phase 4 — Collaboration and Growth Baseline

Phase 4 introduces controlled external collaboration and growth primitives.

## 11.1 Phase 4 Purpose

Phase 4 answers:

```text
Which agent or provider may help?
How is work routed?
How is communication linked?
What limited opportunity or network support is needed?
```

## 11.2 Phase 4 Domains

```text
Agent
Service Provider
Routing
Communication
Opportunity
```

Opportunity appears in Phase 3 as partial execution signal and Phase 4 as growth baseline.

This does not duplicate the domain.

It reflects phased implementation depth.

## 11.3 Phase 4 Priority

| Item | Type | MVP Depth | Rationale |
|------|------|-----------|-----------|
| Agent | Domain | Partial Implement | Needed for foreign associate context and routing baseline. |
| Service Provider | Domain | Partial Implement | Needed for provider context but not full provider platform. |
| Routing | Domain | Partial Implement | Needed for controlled assignment/recommendation, not full optimization. |
| Communication | Domain | Partial Implement | Needed to link emails/messages to matters and agents. |
| Opportunity | Domain | Partial Implement | Needed for baseline signals, not full commercial engine. |

## 11.4 Phase 4 Deferred Scope

Do not implement in Phase 4:

```text
full provider marketplace
advanced routing optimization
provider ranking and scoring
full communication center
external agent portal
full opportunity automation
```

---

# 12. Phase 5 — Reserved Network and Future Expansion

Phase 5 reserves future architecture without implementing full future scope.

## 12.1 Phase 5 Purpose

Phase 5 answers:

```text
What future domains must be recognized now but not built deeply in MVP?
```

## 12.2 Phase 5 Domains

```text
Partner
Service Network
```

## 12.3 Phase 5 Priority

| Item | Type | MVP Depth | Rationale |
|------|------|-----------|-----------|
| Partner | Domain | Reserved Boundary | Needed for future partner architecture, not MVP execution. |
| Service Network | Domain | Reserved Boundary | Needed for MGSN, but full network operation is outside MVP. |

## 12.4 Phase 5 Deferred Scope

Do not implement in Phase 5 during Core MVP:

```text
full Mark Global Service Network marketplace
partner self-service portal
provider ranking
provider trust scoring
cross-border network settlement
public service exchange
full agent marketplace
```

---

# 13. Complete MVP Priority Table

The following table summarizes MVP priority.

| Priority | Item | Category | Type | MVP Depth | Primary Consumers |
|----------|------|----------|------|-----------|-------------------|
| 01 | Identity | Foundation | Domain | Must Implement | All consumers |
| 02 | Organization | Foundation | Domain | Must Implement | MarkReg, Lite, Workplace |
| 03 | User | Foundation | Domain | Must Implement | Workplace, MarkReg, Codex |
| 04 | Permission | Foundation | Domain | Must Implement | All consumers |
| 05 | Knowledge | Foundation | Domain | Must Implement | Lite, MarkReg, AI Agents |
| 06 | Policy | Foundation | Domain | Partial Implement | Permission, AI, Workflow |
| 07 | Capability | Cross-Cutting | System | Partial Implement | AI, Routing, MGSN baseline |
| 08 | Business Responsibility | Cross-Cutting | System | Partial Implement | Workplace, AI, Task, Matter |
| 09 | Brand | Professional | Domain | Must Implement | Lite, MarkReg |
| 10 | Trademark | Professional | Domain | Must Implement | Lite, MarkReg, Workplace |
| 11 | Jurisdiction | Professional | Domain | Must Implement | Lite, MarkReg, AI Agents |
| 12 | Classification | Professional | Domain | Must Implement | Lite, MarkReg, AI Agents |
| 13 | Document | Professional | Domain | Must Implement | MarkReg, Lite, Workplace |
| 14 | Evidence | Professional | Domain | Partial Implement | MarkReg, AI Agents |
| 15 | Customer | Business Execution | Domain | Must Implement | Lite, MarkReg, Workplace |
| 16 | Order | Business Execution | Domain | Must Implement | Lite, MarkReg |
| 17 | Matter | Business Execution | Domain | Must Implement | MarkReg, Workplace |
| 18 | Workflow Contract | Business Execution | Domain | Must Implement | Workplace, Codex |
| 19 | Task | Business Execution | Domain | Must Implement | Workplace, MarkReg |
| 20 | Event | Business Execution | Domain | Must Implement | All execution consumers |
| 21 | Notification | Business Execution | Domain | Partial Implement | Workplace, MarkReg |
| 22 | Opportunity | Business Execution | Domain | Partial Implement | Lite, Growth baseline |
| 23 | Agent | Collaboration Network | Domain | Partial Implement | MarkReg, MGSN baseline |
| 24 | Service Provider | Collaboration Network | Domain | Partial Implement | MGSN baseline, Routing |
| 25 | Routing | Collaboration Network | Domain | Partial Implement | MarkReg, MGSN baseline, AI |
| 26 | Communication | Collaboration Network | Domain | Partial Implement | MarkReg, Workplace, Agents |
| 27 | Partner | Collaboration Network | Domain | Reserved Boundary | Future Partner Center, MGSN |
| 28 | Service Network | Collaboration Network | Domain | Reserved Boundary | Future MGSN |

Note:

```text
The table has 28 priority rows because it includes 26 baseline domains plus 2 cross-cutting systems.
The baseline domain count remains 26.
Capability and Business Responsibility are not additional baseline domains.
```

---

# 14. Must Implement Baseline

The Must Implement baseline is:

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
Customer
Order
Matter
Workflow Contract
Task
Event
```

These are required for the first executable Core.

They must produce:

```text
domain specs
object specs
service specs where applicable
event specs where applicable
contracts where applicable
acceptance criteria
Codex tasks
```

---

# 15. Partial Implement Baseline

The Partial Implement baseline is:

```text
Policy
Capability
Business Responsibility
Evidence
Notification
Opportunity
Agent
Service Provider
Routing
Communication
```

These are required, but not at full depth.

Each partial item must define:

```text
minimal MVP scope
explicit future scope
objects required now
services required now
events required now
contracts required now
what remains deferred
```

---

# 16. Reserved Boundary Baseline

The Reserved Boundary baseline is:

```text
Partner
Service Network
```

These are recognized but not deeply implemented.

They must define:

```text
canonical meaning
future relationship to MGSN
minimal references if needed
prohibited MVP implementation
future activation conditions
```

---

# 17. Deferred Baseline

The Deferred baseline includes advanced future systems and features.

```text
full MGSN marketplace
partner self-service portal
client portal full experience
service provider marketplace
provider ranking and trust scoring
advanced routing optimization
full opportunity scoring
full brand asset vault
advanced analytics and BI
full external integration platform
full policy rule engine
full workflow designer
full AI autonomy
```

Deferred scope must not enter MVP unless an architecture release changes the boundary.

---

# 18. Priority Dependency Chain

MVP priority follows this dependency chain.

```text
Identity / Organization / User
        ↓
Permission / Policy
        ↓
Knowledge
        ↓
Brand / Trademark / Jurisdiction / Classification / Document
        ↓
Customer / Order / Matter
        ↓
Workflow Contract / Task / Event / Notification
        ↓
Capability / Business Responsibility
        ↓
Agent / Service Provider / Routing / Communication / Opportunity
        ↓
Partner / Service Network
```

Capability and Business Responsibility are shown in the chain because they influence execution and governance across multiple domains.

They are not baseline domains.

---

# 19. Consumer-Driven Priority

MVP priority is also driven by first consumers.

## 19.1 MarkReg Priority

MarkReg requires:

```text
Customer
Trademark
Jurisdiction
Classification
Document
Evidence partial
Order
Matter
Workflow Contract
Task
Event
Agent partial
Communication partial
AI Governance partial
```

## 19.2 MarkOrbit Lite Priority

Lite requires:

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
AI Governance partial
```

## 19.3 Workplace Priority

Workplace requires:

```text
Identity
User
Permission
Matter
Task
Event
Workflow Contract
Business Responsibility partial
Notification partial
AI Output review partial
```

## 19.4 AI Agent Priority

AI Agents require:

```text
Identity
Permission
Knowledge
Policy partial
Capability partial
Business Responsibility partial
Agent Contract
AI Output
AI Audit
Human Review rules
```

## 19.5 Codex Priority

Codex requires:

```text
Appendices
indexes
core-specs templates
MVP Execution Matrix
Codex Task Index
acceptance criteria
prohibited overreach
```

Codex does not define domain priority.

Codex implements approved priority.

---

# 20. AI Priority Rules

AI-related domains and systems must be sequenced carefully.

AI cannot be implemented safely before:

```text
Identity
Permission
Knowledge
Policy baseline
Capability baseline
Business Responsibility baseline
Object access rules
Agent Contract
AI Output status
AI Audit rules
Human Review rules
```

AI MVP may include:

```text
classification assistance
document drafting assistance
trademark status summary
communication summary
routing suggestion
opportunity signal suggestion
Codex implementation assistance
```

AI MVP must not include:

```text
autonomous professional decision
unreviewed legal advice
state mutation without service
unbounded knowledge access
agent selection without review when risk requires it
client-facing professional conclusion without responsibility
```

---

# 21. Domain Priority and Appendix B

Appendix B — Core Domain Index must preserve this priority model.

Appendix B must include for each domain:

```text
domain name
domain category
purpose
MVP phase
MVP depth
primary consumers
primary objects
primary services
primary events
contracts
AI usage
deferred scope
```

Appendix B must also include the clarification:

```text
The canonical baseline Core Domain Map contains 26 domains.
Capability and Business Responsibility are cross-cutting Core specification systems.
They are included in MVP priority sequencing but are not counted as additional baseline domains.
```

---

# 22. Domain Priority and Appendix H

Appendix H — Codex Task Index must convert MVP priority into Codex task sequence.

Codex task generation should follow this order:

```text
Wave 0 — Repository and Spec Scaffold
Wave 1 — Foundation Core
Wave 2 — Professional Core
Wave 3 — Business Execution Core
Wave 4 — AI Governance and Review
Wave 5 — Product Consumption Baseline
Wave 6 — Growth Core Baseline
Wave 7 — Validation, Hardening and Release
```

Priority decisions in this chapter must be reflected in:

```text
Codex task dependencies
source specs
expected outputs
out-of-scope warnings
acceptance criteria
```

---

# 23. Domain Priority Anti-Patterns

The following priority anti-patterns are prohibited.

## 23.1 Product Pulls Future Domain Forward

A future product requests a full domain implementation before MVP requires it.

Correction:

```text
Use Partial Implement, Reserved Boundary or Deferred classification.
```

## 23.2 AI Pulls Governance Too Late

AI features are implemented before Agent Contract, review and audit.

Correction:

```text
Implement governance baseline before AI capability expansion.
```

## 23.3 Network Marketplace Enters MVP

MGSN marketplace features enter Core MVP before Partner and Service Network are ready.

Correction:

```text
Keep Partner and Service Network as Reserved Boundary.
```

## 23.4 Data Import Becomes Domain Priority

Available data determines domain sequence.

Correction:

```text
Domain priority follows Core dependency, not data availability.
```

## 23.5 Codex Implements Out of Sequence

Codex builds services before domains, objects and indexes are stable.

Correction:

```text
Follow Appendix H, execution matrix and source specs.
```

## 23.6 Cross-Cutting System Becomes Hidden Domain

Capability or Business Responsibility is treated as a new domain without release decision.

Correction:

```text
Keep cross-cutting classification unless architecture release changes baseline map.
```

---

# 24. Priority Governance

MVP priority may change only through architecture governance.

A priority change requires review when it:

```text
changes MVP depth
moves a domain between phases
adds a new Must Implement item
turns Reserved Boundary into implementation scope
moves deferred scope into MVP
changes cross-cutting system classification
adds AI authority
changes consumer priority
```

Priority governance output should include:

```text
change reason
affected domains
affected consumers
affected specs
affected Codex waves
risk assessment
acceptance criteria
release note
```

---

# 25. Specification Output

This chapter produces the following specification outputs:

```text
MVP Priority Statement
Priority Dimensions
MVP Depth Types
Baseline Domain Count Rule
MVP Priority Phases
Phase 1 Foundation Core Priority
Phase 2 Professional Core Priority
Phase 3 Business Execution Core Priority
Phase 4 Collaboration and Growth Baseline Priority
Phase 5 Reserved Network and Future Expansion Priority
Complete MVP Priority Table
Must Implement Baseline
Partial Implement Baseline
Reserved Boundary Baseline
Deferred Baseline
Priority Dependency Chain
Consumer-Driven Priority
AI Priority Rules
Appendix B Requirements
Appendix H Requirements
Domain Priority Anti-Patterns
Priority Governance Rules
```

---

# 26. Execution Mapping

| Priority Decision | Execution Impact |
|------------------|------------------|
| Must Implement | Detailed specs and Codex tasks required |
| Partial Implement | Minimal specs and explicit deferred scope required |
| Reserved Boundary | Name and meaning reserved, implementation blocked |
| Deferred | Explicitly excluded from MVP |
| 26-domain baseline | Appendix B must preserve domain count |
| Cross-cutting systems | Capability and Business Responsibility indexed separately |
| Consumer-driven priority | Product consumption contracts must follow MVP classification |
| AI priority | Agent Contracts and audit precede AI expansion |
| Codex sequencing | Appendix H and Execution Matrix define task order |

---

# 27. Relationship to core-specs/

This chapter governs future `core-specs/` sequencing.

`core-specs/` generation should start with:

```text
Foundation domain specs
Professional domain specs
Business execution domain specs
Cross-cutting system specs or indexes
Partial collaboration domain specs
Reserved boundary notes
```

Detailed `core-specs/` must not begin until:

```text
Appendix A — Glossary is complete
Appendix B — Core Domain Index is complete
Appendix C — Core Object Index is complete
Appendix D — Core Service Index is complete
Appendix E — Event Index is complete
Appendix F — API Index is complete
Appendix G — Agent Index is complete
Appendix H — Codex Task Index is complete
```

---

# 28. Exclusions

This chapter does not define:

```text
complete domain specs
complete object specs
complete service specs
complete event payloads
API routes
product UI
full marketplace behavior
commercial pricing
full AI agent prompts
implementation tickets
```

Those belong to appendices, `core-specs/`, product books or Codex tasks.

---

# 29. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It preserves the 26 baseline Core Domain count.
[ ] It includes Capability and Business Responsibility as cross-cutting systems, not baseline domains.
[ ] It defines MVP priority dimensions.
[ ] It defines MVP depth types.
[ ] It defines Phase 1–5 priority sequencing.
[ ] It identifies Must Implement items.
[ ] It identifies Partial Implement items.
[ ] It identifies Reserved Boundary items.
[ ] It identifies Deferred scope.
[ ] It includes a complete MVP priority table.
[ ] It explains why the table has 28 rows but only 26 baseline domains.
[ ] It defines consumer-driven priority.
[ ] It defines AI priority rules.
[ ] It links priority to Appendix B.
[ ] It links priority to Appendix H.
[ ] It protects MVP from future product scope leakage.
[ ] It prevents Codex from implementing out of sequence.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 30. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 29, defining MVP Domain Priority. |
| 0.2.0 | Draft | Second canonical draft rewrite. Clarified 26-domain baseline versus 28 priority rows, defined MVP depth types, phases, consumer-driven priority, AI priority rules, deferred scope and Appendix B/H readiness. |

---

**End of Chapter**
