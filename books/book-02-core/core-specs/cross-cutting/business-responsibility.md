# Cross-Cutting Specification — Business Responsibility

**Spec ID:** B02-XCUT-BUSINESS-RESPONSIBILITY  
**Spec Type:** Cross-Cutting Specification  
**Specification Name:** Business Responsibility  
**Specification Category:** Cross-Cutting Core System  
**Source Chapter:** B02-CH-21 — Business Responsibility Specification  
**Related Chapters:** B02-CH-05 — Core Principles; B02-CH-08 — Ontology and Domain Classification; B02-CH-11 — Responsibility Flow; B02-CH-13 — Core Domain Architecture; B02-CH-16 — Core Execution Primitives; B02-CH-28 — Core MVP Boundary; B02-CH-30 — MVP Execution Matrix  
**Related Appendix:** B02-APP-B — Core Domain Index; B02-APP-C — Core Object Index; B02-APP-D — Core Service Index; B02-APP-E — Event Index; B02-APP-H — Codex Task Index  
**Related Domain Specs:** core-specs/domains/identity.md; core-specs/domains/organization.md; core-specs/domains/user.md; core-specs/domains/permission.md; core-specs/domains/policy.md; core-specs/domains/customer.md; core-specs/domains/order.md; core-specs/domains/matter.md; core-specs/domains/task.md; core-specs/domains/workflow-contract.md; core-specs/domains/event.md  
**Related Object Specs:** core-specs/objects/business-responsibility.md; core-specs/objects/responsibility-assignment.md; core-specs/objects/responsibility-role.md; core-specs/objects/responsibility-scope.md; core-specs/objects/responsibility-status.md; core-specs/objects/responsibility-handoff.md; core-specs/objects/responsibility-review-reference.md  
**Related Service Specs:** core-specs/services/responsibility-assignment-service.md; core-specs/services/responsibility-handoff-service.md; core-specs/services/responsibility-validation-service.md; core-specs/services/responsibility-review-service.md; core-specs/services/responsibility-reference-validation-service.md  
**Related Event Specs:** core-specs/events/responsibility-assigned.md; core-specs/events/responsibility-updated.md; core-specs/events/responsibility-handoff-requested.md; core-specs/events/responsibility-handoff-completed.md; core-specs/events/responsibility-review-required.md; core-specs/events/responsibility-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/business-responsibility/business-responsibility-contract.md; core-specs/contracts/business-responsibility/responsibility-assignment-contract.md; core-specs/contracts/business-responsibility/responsibility-scope-contract.md; core-specs/contracts/business-responsibility/responsibility-handoff-contract.md; core-specs/contracts/business-responsibility/responsibility-review-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Business Responsibility cross-cutting specification defines how MarkOrbit records, assigns, transfers, reviews and audits responsibility for business and professional execution.

Business Responsibility exists so that Core does not confuse:

```text
identity
permission
role
task assignee
matter owner
workflow participant
AI agent capability
organization structure
product UI ownership
```

Business Responsibility provides a governed responsibility layer across domains.

It answers who is responsible for an action, decision, review, handoff, communication or execution outcome, without redefining the underlying domain.

This specification is cross-cutting because responsibility can apply to Customers, Orders, Matters, Tasks, Workflows, Documents, Evidence, Communications, Agents, Service Providers and AI actions.

---

# 2. Core Meaning

Business Responsibility means:

```text
a Core-recognized accountability relationship that assigns a responsible actor, role, team, system or agent to a defined business or professional scope, with status, handoff, review and audit rules.
```

Business Responsibility is not:

```text
Identity
User
Permission
Policy
Capability
Task
Matter
Workflow
Organization chart
job title
UI owner field
AI authority
professional truth
```

Business Responsibility answers:

```text
Who is accountable?
For what scope?
Under which role?
For which object, workflow, task, matter or decision?
Is the responsibility active, pending, transferred, completed or revoked?
Can it be handed off?
Does it require review or approval?
What audit trace is required?
Can AI be assigned, assist or only recommend?
```

---

# 3. Specification Category

Business Responsibility is a Cross-Cutting Core System.

It is not one of the baseline 26 Core Domains.

It may produce:

```text
objects
services
events
contracts
validation rules
Codex tasks
AI governance constraints
```

But it must not silently change the baseline Core Domain Map.

The baseline Core Domain Map remains:

```text
26 Core Domains
+ Capability as cross-cutting system
+ Business Responsibility as cross-cutting system
```

---

# 4. Architectural Position

Business Responsibility sits between actor recognition, work execution and audit.

```text
Identity recognizes actor
        ↓
Permission determines allowed action
        ↓
Policy evaluates contextual constraints
        ↓
Business Responsibility assigns accountability
        ↓
Workflow coordinates state
        ↓
Task executes work
        ↓
Event records changes
        ↓
Audit preserves accountable trace
```

Business Responsibility assigns accountability.

It does not grant permission.

It does not execute work.

It does not replace workflow or task.

---

# 5. Scope

Business Responsibility includes:

```text
responsibility definition
responsibility role
responsibility scope
responsibility actor reference
responsibility assignment
responsibility status
responsibility handoff
responsibility review reference
responsibility escalation boundary
responsibility relationship to task
responsibility relationship to matter
responsibility relationship to workflow
responsibility relationship to order
responsibility relationship to communication
responsibility AI assignment boundary
responsibility validation
responsibility event emission
responsibility use by Codex tasks
```

MVP / Phase 3 partial implementation should focus on:

```text
Business Responsibility
Responsibility Role
Responsibility Scope
Responsibility Assignment
Responsibility Status
Responsibility Handoff
Responsibility Assignment Service
Responsibility Handoff Service
Responsibility Validation Service
Responsibility Reference Validation Service
ResponsibilityAssigned event
ResponsibilityUpdated event
ResponsibilityHandoffRequested event
ResponsibilityHandoffCompleted event
ResponsibilityReviewRequired event
ResponsibilityReferenceValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

Business Responsibility owns:

```text
Core responsibility definition
responsibility role
responsibility scope
responsibility actor reference
responsibility assignment
responsibility status
responsibility handoff boundary
responsibility review reference
responsibility escalation boundary
responsibility validation
responsibility event emission
```

## 6.2 Out of Boundary

Business Responsibility does not own:

```text
actor identity
user account lifecycle
permission grant
policy rule definition
capability definition
task lifecycle
matter lifecycle
workflow state transition
order lifecycle
communication message lifecycle
organization HR structure
employment contract
performance evaluation
AI agent autonomy
```

Those responsibilities belong to:

```text
Identity Domain
User Domain
Permission Domain
Policy Domain
Capability cross-cutting system
Task Domain
Matter Domain
Workflow Contract Domain
Order Domain
Communication Domain
Organization Domain
AI Governance
Product implementation
```

## 6.3 Boundary Notes

Business Responsibility is accountability.

Permission is authorization.

Capability is ability.

Task is work unit.

Workflow is process structure.

Matter is execution container.

Business Responsibility can link to these but must not absorb their meanings.

---

# 7. Core Rules

## 7.1 Responsibility Must Have Scope

Every Responsibility Assignment must define scope.

Scope may include:

```text
domain
object
matter
order
task
workflow
communication
document
evidence
jurisdiction
time window
action type
review type
```

Unscoped responsibility is prohibited.

## 7.2 Responsibility Must Have Actor or Role

Every Responsibility Assignment must identify an actor, role, team, system or explicitly pending assignment rule.

Responsible actor may include:

```text
User
Team
Organization Unit
System Actor
AI Agent
External Participant Reference
```

AI responsibility requires explicit Agent Contract and review constraints.

## 7.3 Responsibility Does Not Grant Permission

A responsibility assignment does not grant the actor permission to perform an action.

Permission and Policy must still be evaluated.

## 7.4 Responsibility Does Not Execute Work

Business Responsibility identifies accountability.

Task, Workflow, Matter or Service performs execution through governed services.

## 7.5 Responsibility Handoff Must Be Traceable

Responsibility handoff must preserve:

```text
source responsible actor
target responsible actor
handoff reason
scope
approval or review requirement
time
actor initiating handoff
status
```

## 7.6 Responsibility Must Be Auditable

Responsibility-sensitive actions must preserve audit trace.

Audit-sensitive responsibility actions include:

```text
responsibility assignment
responsibility update
responsibility handoff request
responsibility handoff approval
responsibility handoff completion
responsibility escalation
responsibility review requirement
AI responsibility recommendation
responsibility override
responsibility closure
```

---

# 8. Primary Objects

Business Responsibility governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Business Responsibility | Business Responsibility | Partial Implement | Core accountability relationship. |
| Responsibility Role | Business Responsibility | Partial Implement | Controlled role defining nature of responsibility. |
| Responsibility Scope | Business Responsibility | Partial Implement | Scope where responsibility applies. |
| Responsibility Assignment | Business Responsibility | Partial Implement | Assignment of responsibility to actor, role, team, system or agent. |
| Responsibility Status | Business Responsibility | Partial Implement | Controlled lifecycle status. |
| Responsibility Handoff | Business Responsibility | Partial Implement | Transfer or reassignment of responsibility. |
| Responsibility Review Reference | Business Responsibility / Review | Partial Implement | Review requirement or decision reference. |
| Responsibility Escalation Reference | Business Responsibility / Workflow | Deferred | Escalation rule or escalation event reference. |
| Responsibility Audit Reference | Business Responsibility / Audit | Partial Implement | Audit reference for responsibility-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning System | Relationship |
|--------|---------------|--------------|
| Identity | Identity Domain | Responsible actor must be recognized. |
| User | User Domain | User may be responsible actor. |
| Organization | Organization Domain | Responsibility may be scoped to organization/team. |
| Permission | Permission Domain | Permission still required for action. |
| Policy | Policy Domain | Policy constraints still apply. |
| Capability | Capability cross-cutting system | Responsible actor may require capability. |
| Matter | Matter Domain | Matter may have owner/reviewer responsibility. |
| Order | Order Domain | Order may have commercial owner responsibility. |
| Task | Task Domain | Task may have assignee responsibility. |
| Workflow Contract | Workflow Contract Domain | Workflow may require responsibility guards. |
| Communication | Communication Domain | Communication may have owner/reviewer responsibility. |
| AI Agent | AI Governance | AI may assist or be assigned under contract. |
| Event | Event Domain | Responsibility changes emit events. |
| Audit Record | Audit | Audit records responsibility-sensitive actions. |

---

# 9. Primary Services

Business Responsibility requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Responsibility Assignment Service | Business Responsibility | Partial Implement | Assign responsibility to actor, role, team, system or agent. |
| Responsibility Update Service | Business Responsibility | Partial Implement | Update controlled responsibility fields. |
| Responsibility Status Service | Business Responsibility | Partial Implement | Update Responsibility Status through governed rules. |
| Responsibility Handoff Service | Business Responsibility | Partial Implement | Request, approve or complete handoff. |
| Responsibility Validation Service | Business Responsibility | Partial Implement | Validate scope, actor, role and status. |
| Responsibility Review Service | Business Responsibility / Review | Partial Implement | Create or resolve responsibility review requirement. |
| Responsibility Escalation Service | Business Responsibility / Workflow | Deferred | Escalate unhandled or blocked responsibility. |
| Responsibility Reference Validation Service | Business Responsibility | Partial Implement | Validate responsibility references used by other specs. |
| Responsibility Audit Reference Service | Business Responsibility / Audit | Partial Implement | Produce audit reference for responsibility-sensitive actions. |

Service rules:

```text
- Mutating Responsibility services must emit events.
- Responsibility Assignment must not grant Permission.
- Responsibility services must not execute Task, Matter or Workflow directly.
- AI responsibility assignment must require Agent Contract.
- Handoff must preserve source, target, scope and reason.
```

---

# 10. Primary Events

Business Responsibility emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| ResponsibilityAssigned | Responsibility Assignment Service | Partial Implement | Responsibility has been assigned. |
| ResponsibilityUpdated | Responsibility Update Service | Partial Implement | Controlled responsibility fields have changed. |
| ResponsibilityStatusChanged | Responsibility Status Service | Partial Implement | Responsibility status has changed. |
| ResponsibilityHandoffRequested | Responsibility Handoff Service | Partial Implement | Handoff has been requested. |
| ResponsibilityHandoffApproved | Responsibility Handoff Service / Review Service | Partial Implement | Handoff has been approved. |
| ResponsibilityHandoffRejected | Responsibility Handoff Service / Review Service | Partial Implement | Handoff has been rejected. |
| ResponsibilityHandoffCompleted | Responsibility Handoff Service | Partial Implement | Handoff has been completed. |
| ResponsibilityReviewRequired | Responsibility Review Service | Partial Implement | Responsibility requires review. |
| ResponsibilityEscalationRequested | Responsibility Escalation Service | Deferred | Escalation has been requested. |
| ResponsibilityReferenceValidated | Responsibility Reference Validation Service | Partial Implement | Responsibility reference has been validated for governed use. |

Event rules:

```text
- Responsibility events must reference Responsibility Assignment.
- Handoff events must reference source and target responsible actor where allowed.
- Review events must reference review requirement without exposing confidential content unnecessarily.
- AI responsibility events must identify AI source where applicable.
```

---

# 11. Primary Contracts

Business Responsibility requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Business Responsibility Contract | Responsibility Contract | Partial Implement | Defines responsibility identity, role, scope, actor and status. |
| Responsibility Role Contract | Responsibility Contract | Partial Implement | Defines controlled responsibility roles. |
| Responsibility Scope Contract | Responsibility Contract | Partial Implement | Defines valid responsibility scope boundary. |
| Responsibility Assignment Contract | Responsibility Contract | Partial Implement | Defines assignment actor, role, scope and source. |
| Responsibility Handoff Contract | Responsibility Contract | Partial Implement | Defines handoff source, target, reason, approval and status. |
| Responsibility Review Contract | Responsibility / Review Contract | Partial Implement | Defines review requirement and resolution boundary. |
| Responsibility Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for responsibility-sensitive actions. |

Contract rules:

```text
- Responsibility Contract must not grant Permission.
- Responsibility Scope Contract must prevent unscoped responsibility.
- Responsibility Handoff Contract must preserve source and target trace.
- Responsibility Assignment Contract must distinguish human, team, system and AI responsibility.
```

---

# 12. Relationships to Domains

## 12.1 Identity and User

Responsibility may be assigned to recognized actors.

Identity recognizes actor.

User represents account.

Responsibility assigns accountability.

## 12.2 Permission

Permission determines whether the responsible actor may perform actions.

Responsibility does not grant Permission.

## 12.3 Policy

Policy determines contextual constraints.

Responsibility must respect Policy.

## 12.4 Capability

Capability describes possible action.

Responsibility may require capability, but capability does not equal accountability.

## 12.5 Matter

Matter may have matter owner, professional reviewer, process owner or communication owner responsibilities.

Matter owns execution container.

## 12.6 Order

Order may have commercial owner, order reviewer or conversion owner responsibilities.

Order owns commercial service request.

## 12.7 Task

Task assignment may create or reference Responsibility Assignment.

Task owns work unit lifecycle.

## 12.8 Workflow Contract

Workflow may require responsibility guards, review roles or handoff rules.

Workflow owns transition structure.

## 12.9 Communication

Communication may require drafter, reviewer, sender or response-owner responsibility.

Communication owns message lifecycle.

## 12.10 AI Governance

AI may assist responsibility assignment or be assigned limited responsibility under Agent Contract.

AI cannot become final professional accountability by default.

## 12.11 Audit

Audit records should include Responsibility references for accountability-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Business Responsibility only under governed Agent Contracts.

Allowed AI use:

```text
suggest responsibility assignment
identify missing responsible actor
summarize responsibility coverage
flag unowned Matter, Task or Communication
recommend handoff review
draft responsibility handoff note
detect responsibility-scope mismatch
identify AI actions that require human responsible owner
```

AI must not:

```text
assign itself final responsibility without Agent Contract
grant permission through responsibility
override existing responsible actor without governed service
complete responsibility handoff without required review
assume professional accountability for legal conclusions by default
hide responsibility gap
execute Task, Matter or Workflow directly through responsibility
```

AI responsibility usage requires:

```text
Agent Identity
Agent Contract
Capability Binding where applicable
Permission Rule
Policy Rule
Review Rule
Audit Rule
Human Responsible Owner for high-risk professional work
```

---

# 14. Workflow Usage

Business Responsibility participates in workflows as assignment, guard, review and handoff mechanism.

Responsibility-sensitive workflows may include:

```text
responsibility-assignment-workflow.md
matter-owner-assignment-workflow.md
task-assignee-responsibility-workflow.md
communication-review-responsibility-workflow.md
responsibility-handoff-workflow.md
responsibility-review-workflow.md
ai-responsibility-recommendation-review-workflow.md
responsibility-escalation-workflow.md
```

Workflow rules:

```text
- Responsibility workflows must reference Workflow Contracts.
- Responsibility assignment must validate actor, role and scope.
- Responsibility handoff must be traceable.
- Responsibility gaps should trigger review or escalation where required.
- AI responsibility suggestions must be reviewable where high-risk.
- Responsibility does not mutate Task, Matter or Workflow directly.
```

---

# 15. API Usage

Business Responsibility APIs expose assignment, handoff, validation and review through governed services.

Potential Phase 3 APIs:

```text
POST /responsibilities
GET /responsibilities/{id}
PATCH /responsibilities/{id}
POST /responsibilities/{id}/status
POST /responsibilities/{id}/handoff/request
POST /responsibilities/{id}/handoff/approve
POST /responsibilities/{id}/handoff/complete
POST /responsibilities/{id}/validate
POST /responsibilities/reference/validate
```

Potential partial APIs:

```text
POST /responsibilities/{id}/review
POST /responsibilities/{id}/escalate
GET /responsibilities/{id}/audit-reference
POST /responsibilities/{id}/ai-recommendation
```

API rules:

```text
- APIs must invoke Responsibility Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not grant Permission.
- APIs must not execute Task, Matter or Workflow directly.
- Mutating APIs must emit or cause service-level events.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

API details belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

## 16.1 MVP Consumers

```text
Workplace
MarkReg
MarkOrbit Lite
AI Agents
Codex Implementation
Validation tools
```

## 16.2 Partial Consumers

```text
Admin tools
Workflow tools
Task workbench
Matter workbench
Communication review tools
```

## 16.3 Future Consumers

```text
Service Network
Partner Center
Service Platform
Performance reporting
Workload analytics
Advanced responsibility governance
```

Product rule:

```text
Products consume Business Responsibility.
Products do not redefine Business Responsibility.
```

---

# 17. MVP Scope

Business Responsibility is a Phase 3 / Wave 3 Partial Implement cross-cutting system.

MVP includes:

```text
Business Responsibility
Responsibility Role
Responsibility Scope
Responsibility Assignment
Responsibility Status
Responsibility Handoff
Responsibility Assignment Service
Responsibility Update Service
Responsibility Status Service
Responsibility Handoff Service
Responsibility Validation Service
Responsibility Reference Validation Service
ResponsibilityAssigned event
ResponsibilityUpdated event
ResponsibilityStatusChanged event
ResponsibilityHandoffRequested event
ResponsibilityHandoffCompleted event
ResponsibilityReviewRequired event
ResponsibilityReferenceValidated event
basic responsibility metadata validation
source traceability to Identity, User, Permission, Policy, Capability, Matter, Order, Task, Workflow, Communication and AI systems
```

MVP should support:

```text
basic responsibility assignment
basic role and scope
basic status
basic handoff
basic responsibility validation
task and matter responsibility reference
AI-assisted responsibility gap detection with human review
```

MVP does not require full HR structure, performance evaluation, workload analytics or autonomous AI responsibility management.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full responsibility governance console
advanced escalation engine
workload and capacity analytics
performance evaluation
SLA responsibility engine
HR system integration
cross-tenant responsibility federation
autonomous AI responsibility management
automatic workload balancing
responsibility-based compensation or settlement
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Business Responsibility should use stable immutable ID.
Responsibility Scope should be required.
Responsibility Role should be controlled.
Responsibility Assignment should reference recognized actor or role.
Responsibility Status should be controlled.
Responsibility Handoff should preserve source, target, reason and status.
Responsibility does not grant Permission.
Responsibility should be linked to Task, Matter, Workflow or Communication where applicable.
AI-generated responsibility recommendations should remain draft/recommendation output until reviewed where needed.
```

Suggested Responsibility Status values:

```text
Draft
Assigned
Active
PendingReview
HandoffRequested
Transferred
Completed
Revoked
Cancelled
Archived
```

MVP controlled Responsibility Status values:

```text
Draft
Assigned
Active
PendingReview
HandoffRequested
Transferred
Completed
Cancelled
Archived
```

Suggested Responsibility Role values:

```text
MatterOwner
OrderOwner
TaskAssignee
ProfessionalReviewer
ProcessOwner
CommunicationOwner
DocumentReviewer
EvidenceReviewer
CustomerContactOwner
AgentContactOwner
ApprovalOwner
AIAssistant
SystemOwner
```

MVP controlled Responsibility Role values:

```text
MatterOwner
OrderOwner
TaskAssignee
ProfessionalReviewer
ProcessOwner
CommunicationOwner
DocumentReviewer
EvidenceReviewer
ApprovalOwner
AIAssistant
SystemOwner
```

Suggested Responsibility Scope Type values:

```text
Domain
Object
Matter
Order
Task
Workflow
Communication
Document
Evidence
Jurisdiction
Action
Review
TimeWindow
```

Do not treat job title or UI owner field as Core Business Responsibility by itself.

---

# 20. Codex Implementation Notes

Codex may implement Business Responsibility only from approved specs.

Codex must:

```text
cite this cross-cutting spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Responsibility / Permission boundary
preserve Responsibility / Policy boundary
preserve Responsibility / Capability boundary
preserve Responsibility / Task boundary
preserve Responsibility / Matter / Workflow boundaries
implement only Phase 3 Partial scope unless task says otherwise
write tests for responsibility assignment
write tests for required scope
write tests for actor or role reference
write tests for responsibility handoff trace
write tests preventing responsibility from granting permission
write tests preventing responsibility from executing tasks or workflow transitions
write tests preventing AI from assuming final professional responsibility by default
```

Codex must not:

```text
turn Business Responsibility into Permission
turn Business Responsibility into Policy
turn Business Responsibility into Capability
turn Business Responsibility into Task
turn Business Responsibility into Workflow
turn Business Responsibility into HR org chart
grant access through Responsibility alone
execute work through Responsibility service
allow AI to self-assign final professional accountability
implement workload analytics in MVP
```

---

# 21. Validation Rules

Business Responsibility must pass the following checks.

```text
[ ] Business Responsibility is classified as Cross-Cutting Core System.
[ ] Business Responsibility is not counted as one of the baseline 26 Core Domains.
[ ] Business Responsibility does not change the baseline Core Domain Map.
[ ] Business Responsibility has MVP Phase 3 / Wave 3 classification.
[ ] Business Responsibility has MVP Depth = Partial Implement.
[ ] Business Responsibility defines Core meaning.
[ ] Business Responsibility boundary excludes Permission grant.
[ ] Business Responsibility boundary excludes Policy rule definition.
[ ] Business Responsibility boundary excludes Capability definition.
[ ] Business Responsibility boundary excludes Task, Matter and Workflow execution.
[ ] Business Responsibility boundary excludes HR performance evaluation.
[ ] Business Responsibility owns Business Responsibility object.
[ ] Business Responsibility defines Responsibility Scope.
[ ] Business Responsibility defines Responsibility Assignment.
[ ] Business Responsibility defines Responsibility Handoff.
[ ] Business Responsibility lists primary services.
[ ] Mutating Responsibility services emit events.
[ ] Business Responsibility lists primary events.
[ ] Business Responsibility defines contract requirements.
[ ] Business Responsibility defines AI Agent usage constraints.
[ ] Business Responsibility defines workflow usage constraints.
[ ] Business Responsibility defines API usage constraints.
[ ] Business Responsibility defines product consumers.
[ ] Business Responsibility defines MVP and deferred scope.
[ ] Business Responsibility defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This specification must not be used to:

```text
turn Business Responsibility into Permission
turn Business Responsibility into Policy
turn Business Responsibility into Capability
turn Business Responsibility into Task
turn Business Responsibility into Matter
turn Business Responsibility into Workflow
turn Business Responsibility into HR system
turn Business Responsibility into performance evaluation
grant access through Responsibility alone
execute work through Responsibility alone
allow AI to self-authorize responsibility
allow AI to become final professional accountable party by default
change baseline 26 Core Domains
allow Codex to define new responsibility architecture
```

---

# 23. Acceptance Criteria

This Business Responsibility Cross-Cutting Specification is accepted only if:

```text
[ ] It defines Business Responsibility purpose.
[ ] It defines Business Responsibility Core meaning.
[ ] It identifies Business Responsibility as Cross-Cutting Core System.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines core rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Identity, User, Permission, Policy, Capability, Matter, Order, Task, Workflow, Communication, AI Governance and Audit.
[ ] It defines AI Agent usage.
[ ] It defines workflow usage.
[ ] It defines API usage.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Business Responsibility cross-cutting specification. Establishes Business Responsibility as Phase 3 Cross-Cutting Core System with Partial Implement depth, defines Responsibility, Role, Scope, Assignment, Handoff, services, events, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Cross-Cutting Specification**
