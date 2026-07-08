# Cross-Cutting Specification — Capability

**Spec ID:** B02-XCUT-CAPABILITY  
**Spec Type:** Cross-Cutting Specification  
**Specification Name:** Capability  
**Specification Category:** Cross-Cutting Core System  
**Source Chapter:** B02-CH-19 — Capability Specification  
**Related Chapters:** B02-CH-05 — Core Principles; B02-CH-08 — Ontology and Domain Classification; B02-CH-13 — Core Domain Architecture; B02-CH-26 — AI Capability and Agent Governance Specification; B02-CH-28 — Core MVP Boundary; B02-CH-30 — MVP Execution Matrix  
**Related Appendix:** B02-APP-B — Core Domain Index; B02-APP-C — Core Object Index; B02-APP-D — Core Service Index; B02-APP-G — Agent Index; B02-APP-H — Codex Task Index  
**Related Domain Specs:** core-specs/domains/identity.md; core-specs/domains/permission.md; core-specs/domains/policy.md; core-specs/domains/knowledge.md; core-specs/domains/task.md; core-specs/domains/event.md; core-specs/domains/workflow-contract.md  
**Related Object Specs:** core-specs/objects/capability.md; core-specs/objects/capability-scope.md; core-specs/objects/capability-owner.md; core-specs/objects/capability-contract.md; core-specs/objects/capability-binding.md; core-specs/objects/capability-status.md  
**Related Service Specs:** core-specs/services/capability-registration-service.md; core-specs/services/capability-binding-service.md; core-specs/services/capability-validation-service.md; core-specs/services/capability-access-evaluation-service.md; core-specs/services/capability-reference-validation-service.md  
**Related Event Specs:** core-specs/events/capability-registered.md; core-specs/events/capability-updated.md; core-specs/events/capability-bound.md; core-specs/events/capability-access-evaluated.md; core-specs/events/capability-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/capability/capability-contract.md; core-specs/contracts/capability/capability-scope-contract.md; core-specs/contracts/capability/capability-binding-contract.md; core-specs/contracts/capability/capability-access-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Capability cross-cutting specification defines how MarkOrbit describes, governs and exposes what an actor, service, product, agent or system is able to do.

Capability exists so that Core does not confuse:

```text
identity
permission
policy
role
skill
service
AI agent behavior
product feature
implementation endpoint
```

Capability provides a governed description of possible action.

Permission determines whether a specific actor may perform that action.

Policy determines whether contextual constraints allow the action.

Service performs the action.

Agent may request or recommend the action only under contract.

This specification is cross-cutting because Capability applies across domains rather than belonging to one domain.

---

# 2. Core Meaning

Capability means:

```text
a Core-recognized description of an available action, function, skill or service behavior that may be provided by a person, team, system, service, AI agent or product, subject to permission, policy, contract and execution rules.
```

Capability is not:

```text
Identity
Permission
Policy
Role
User
Agent
Service
API endpoint
Product feature
AI output
Professional truth
Business responsibility
```

Capability answers:

```text
What can be done?
Who or what can provide it?
What scope does it apply to?
Which object, service, workflow or domain may consume it?
What contract governs it?
Is it enabled, disabled, experimental, reserved or deprecated?
What permission and policy checks are required before use?
Can AI access or recommend it?
```

---

# 3. Specification Category

Capability is a Cross-Cutting Core System.

It is not one of the baseline 26 Core Domains.

It may produce:

```text
objects
services
events
contracts
validation rules
Codex tasks
AI agent constraints
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

Capability sits between Core definition and controlled execution.

```text
Identity recognizes actor
        ↓
Capability describes possible action
        ↓
Permission determines allowed action
        ↓
Policy evaluates contextual constraints
        ↓
Contract defines safe usage boundary
        ↓
Service executes
        ↓
Event records outcome
        ↓
Audit preserves trace
```

Capability describes what may be available.

It does not grant access.

It does not execute action.

It does not replace professional judgment.

---

# 5. Scope

Capability includes:

```text
capability definition
capability type
capability scope
capability owner
capability provider
capability consumer
capability binding
capability contract reference
capability permission requirement
capability policy requirement
capability AI access boundary
capability service reference
capability workflow reference
capability status
capability validation
capability event emission
capability use by Codex tasks
```

MVP / Phase 1 partial implementation should focus on:

```text
Capability
Capability Scope
Capability Status
Capability Contract Reference
Capability Binding
Capability Registration Service
Capability Binding Service
Capability Validation Service
Capability Reference Validation Service
CapabilityRegistered event
CapabilityBound event
CapabilityReferenceValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

Capability owns:

```text
Core capability definition
capability type
capability scope
capability provider reference
capability consumer reference
capability binding
capability status
capability contract reference
capability access evaluation boundary
capability reference validation
capability event emission
```

## 6.2 Out of Boundary

Capability does not own:

```text
actor identity
user account lifecycle
permission grant
policy rule definition
business responsibility assignment
professional truth
service implementation details
API endpoint implementation
workflow state transition
AI agent final decision
product feature design
```

Those responsibilities belong to:

```text
Identity Domain
User Domain
Permission Domain
Policy Domain
Business Responsibility cross-cutting system
Professional Domains
Service Architecture
API specs
Workflow Contract Domain
AI Governance
Product implementation
```

## 6.3 Boundary Notes

Capability is descriptive and contractual.

Permission is authorizing.

Policy is contextual.

Service is executing.

Agent is governed consumer or provider.

Product is consuming interface.

---

# 7. Core Rules

## 7.1 Capability Must Not Grant Permission

A capability describes what can be done.

It does not mean the actor is allowed to do it.

```text
Capability = can provide / can perform in principle
Permission = may perform now
Policy = may perform under this context
```

## 7.2 Capability Must Be Scoped

Every Capability must define scope.

Scope may include:

```text
domain
object
service
workflow
jurisdiction
product
agent
data access level
operation type
```

Unscoped capabilities are prohibited.

## 7.3 Capability Must Have Provider or Owner

Every Capability should identify a provider or owner.

Provider may be:

```text
User
Team
Organization
Service
AI Agent
System Actor
Service Provider
Agent
Product
```

## 7.4 Capability Must Have Contract Reference

A Capability that can be consumed by services, workflows, APIs, agents or products must reference a Capability Contract.

Capability without contract is not implementation-ready.

## 7.5 AI Capability Must Be Explicit

AI-related capabilities must be explicitly marked.

AI may not infer access to a capability because a tool, endpoint or service exists.

AI capability requires:

```text
Agent identity
Agent contract
Capability binding
Permission check
Policy check
Review rule where required
Audit rule
```

## 7.6 Capability Must Be Auditable

Capability-sensitive actions must preserve audit trace.

Audit-sensitive capability actions include:

```text
capability creation
capability update
capability binding
capability unbinding
capability status change
capability access evaluation
AI capability invocation
capability deprecation
capability override
```

---

# 8. Primary Objects

Capability governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Capability | Capability | Partial Implement | Core description of available action or function. |
| Capability Type | Capability | Partial Implement | Controlled type of capability. |
| Capability Scope | Capability | Partial Implement | Scope where capability applies. |
| Capability Owner | Capability / Identity / Organization | Partial Implement | Owner of capability definition. |
| Capability Provider | Capability | Partial Implement | Actor, service, system or agent able to provide capability. |
| Capability Consumer | Capability | Partial Implement | Actor, service, product or agent that may consume capability. |
| Capability Binding | Capability | Partial Implement | Binding between capability and provider/consumer/context. |
| Capability Contract Reference | Capability / Contract | Partial Implement | Contract governing capability usage. |
| Capability Status | Capability | Partial Implement | Controlled lifecycle status. |
| Capability Audit Reference | Capability / Audit | Partial Implement | Audit reference for capability-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning System | Relationship |
|--------|---------------|--------------|
| Identity | Identity Domain | Capability may bind to recognized actor. |
| Permission | Permission Domain | Permission determines allowed use. |
| Policy | Policy Domain | Policy determines contextual constraints. |
| Knowledge | Knowledge Domain | Capability may depend on governed knowledge. |
| Service | Service Architecture | Capability may be exposed by service. |
| Workflow Contract | Workflow Contract Domain | Workflow may require capability. |
| AI Agent | AI Governance | Agent may provide or consume capability. |
| Task | Task Domain | Task may require capability. |
| Event | Event Domain | Capability changes emit events. |
| Audit Record | Audit | Audit records capability-sensitive actions. |

---

# 9. Primary Services

Capability requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Capability Registration Service | Capability | Partial Implement | Register Core Capability. |
| Capability Update Service | Capability | Partial Implement | Update controlled capability fields. |
| Capability Binding Service | Capability | Partial Implement | Bind capability to provider, consumer or context. |
| Capability Status Service | Capability | Partial Implement | Update capability status through governed rules. |
| Capability Validation Service | Capability | Partial Implement | Validate scope, contract and status. |
| Capability Access Evaluation Service | Capability / Permission / Policy | Partial Implement | Evaluate whether capability may be invoked in context. |
| Capability Contract Reference Service | Capability / Contract | Partial Implement | Link capability to governing contract. |
| Capability Reference Validation Service | Capability | Partial Implement | Validate capability reference used by other specs. |
| Capability Audit Reference Service | Capability / Audit | Partial Implement | Produce audit reference for capability-sensitive actions. |

Service rules:

```text
- Mutating Capability services must emit events.
- Capability Access Evaluation must not bypass Permission or Policy.
- Capability Binding must require scope and contract.
- AI capability access must require Agent Contract.
- Capability services must not implement business service logic directly.
```

---

# 10. Primary Events

Capability emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| CapabilityRegistered | Capability Registration Service | Partial Implement | Capability has been registered. |
| CapabilityUpdated | Capability Update Service | Partial Implement | Controlled capability fields have changed. |
| CapabilityStatusChanged | Capability Status Service | Partial Implement | Capability status has changed. |
| CapabilityBound | Capability Binding Service | Partial Implement | Capability has been bound to provider, consumer or context. |
| CapabilityUnbound | Capability Binding Service | Partial Implement | Capability binding has been removed. |
| CapabilityValidated | Capability Validation Service | Partial Implement | Capability has passed validation. |
| CapabilityValidationFailed | Capability Validation Service | Partial Implement | Capability validation failed. |
| CapabilityAccessEvaluated | Capability Access Evaluation Service | Partial Implement | Capability access has been evaluated. |
| CapabilityReferenceValidated | Capability Reference Validation Service | Partial Implement | Capability reference has been validated for governed use. |
| CapabilityReviewRequired | Capability Validation / Status Service | Partial Implement | Capability requires review. |

Event rules:

```text
- Capability events must reference Capability.
- Binding events must reference provider/consumer/context.
- Access evaluation events must not expose protected context unnecessarily.
- AI capability events must identify AI agent source where applicable.
```

---

# 11. Primary Contracts

Capability requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Capability Contract | Capability Contract | Partial Implement | Defines capability identity, type, scope, status and references. |
| Capability Scope Contract | Capability Contract | Partial Implement | Defines valid scope boundary. |
| Capability Binding Contract | Capability Contract | Partial Implement | Defines provider/consumer/context binding. |
| Capability Access Contract | Capability / Permission / Policy Contract | Partial Implement | Defines access evaluation requirements. |
| Capability AI Usage Contract | Capability / AI Contract | Partial Implement | Defines AI consumption or provision boundary. |
| Capability Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for capability-sensitive actions. |

Contract rules:

```text
- Capability Contract must not grant Permission.
- Capability Access Contract must require Permission and Policy where applicable.
- Capability AI Usage Contract must reference Agent Contract.
- Capability Scope Contract must prevent unscoped capability.
```

---

# 12. Relationships to Domains

## 12.1 Identity

Capability may bind to an Identity or actor reference.

Identity recognizes actor.

Capability describes what may be provided or consumed.

## 12.2 Permission

Permission determines whether a capability may be used by actor.

Capability does not grant Permission.

## 12.3 Policy

Policy determines contextual constraints for capability use.

Capability does not define Policy rules.

## 12.4 Knowledge

Knowledge may support a capability.

Capability does not replace professional knowledge or truth.

## 12.5 Workflow Contract

Workflow may require certain capabilities for transitions or tasks.

Workflow owns transition structure.

Capability owns action availability description.

## 12.6 Task

Task may require a capability to execute.

Task owns work unit lifecycle.

## 12.7 Event

Capability changes and access evaluations may emit Events.

Event owns signal meaning.

## 12.8 AI Governance

AI capability must be explicit and contract-governed.

AI cannot infer capability from model ability alone.

## 12.9 Product Consumers

Products consume capability definitions to expose features, but product UI does not define Core Capability.

---

# 13. AI Agent Usage

AI Agents may use Capability only under governed Agent Contracts.

Allowed AI use:

```text
list capabilities available to an agent if authorized
evaluate missing capability references in specs
recommend capability binding for review
summarize capability scope
flag unscoped or overbroad capability
suggest review requirement for high-risk capability
```

AI must not:

```text
grant itself capability
infer capability from available tool alone
invoke capability without permission and policy checks
bind capability without authorized service
override capability status
treat model ability as professional authority
execute high-risk capability without review where required
```

AI capability usage requires:

```text
Agent Identity
Agent Contract
Capability Binding
Permission Rule
Policy Rule
Review Rule
Audit Rule
Human Review Rule for high-risk action
```

---

# 14. Workflow Usage

Capability participates in workflows as requirement, guard or binding.

Capability-sensitive workflows may include:

```text
capability-registration-workflow.md
capability-binding-workflow.md
capability-access-evaluation-workflow.md
ai-capability-review-workflow.md
capability-deprecation-workflow.md
workflow-capability-guard-workflow.md
```

Workflow rules:

```text
- Capability workflows must reference Workflow Contracts.
- Capability binding must be reviewable where high-risk.
- Capability access evaluation must not bypass Permission or Policy.
- AI capability access must be traceable.
- Deprecated capabilities must not be used by new Codex tasks unless explicitly approved.
```

---

# 15. API Usage

Capability APIs expose registration, binding, validation and access evaluation through governed services.

Potential Phase 1 APIs:

```text
POST /capabilities
GET /capabilities/{id}
PATCH /capabilities/{id}
POST /capabilities/{id}/bindings
POST /capabilities/{id}/validate
POST /capabilities/{id}/access/evaluate
POST /capabilities/reference/validate
```

Potential partial APIs:

```text
POST /capabilities/{id}/status
GET /capabilities/{id}/audit-reference
POST /capabilities/{id}/ai-review
```

API rules:

```text
- APIs must invoke Capability Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not grant Permission.
- APIs must not execute business service logic directly.
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
Developer tools
Agent governance tools
Workflow tools
```

## 16.3 Future Consumers

```text
Marketplace
Service Network
External integrations
Capability catalog
Automation products
AI orchestration products
```

Product rule:

```text
Products consume Capability.
Products do not redefine Capability.
```

---

# 17. MVP Scope

Capability is a Phase 1 / Wave 1 Partial Implement cross-cutting system.

MVP includes:

```text
Capability
Capability Type
Capability Scope
Capability Status
Capability Contract Reference
Capability Binding
Capability Registration Service
Capability Binding Service
Capability Validation Service
Capability Reference Validation Service
CapabilityRegistered event
CapabilityBound event
CapabilityValidated event
CapabilityValidationFailed event
CapabilityReferenceValidated event
basic capability metadata validation
source traceability to Identity, Permission, Policy, Workflow, Task, Service and AI systems
```

MVP should support:

```text
basic capability registration
basic capability scope
basic capability binding
basic status
basic contract reference
basic AI capability boundary
Codex validation against unscoped or unauthorized capability use
```

MVP does not require full capability marketplace, advanced capability discovery, autonomous AI capability orchestration or external capability exchange.

---

# 18. Deferred Scope

Deferred scope includes:

```text
capability marketplace
capability catalog UI
advanced capability discovery
automatic capability inference
cross-tenant capability exchange
dynamic capability pricing
autonomous AI capability orchestration
capability performance analytics
capability recommendation engine
external capability provider marketplace
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Capability should use stable immutable ID.
Capability Scope should be required.
Capability Status should use controlled values.
Capability Binding should reference provider, consumer and context.
Capability Contract Reference should be required for executable or AI-facing capability.
Capability Access Evaluation should call Permission and Policy evaluation.
Capability must not be treated as endpoint access alone.
AI-generated capability suggestions should remain draft/recommendation output until reviewed where needed.
```

Suggested Capability Status values:

```text
Draft
Active
ReviewRequired
Suspended
Deprecated
Disabled
Archived
```

MVP controlled Capability Status values:

```text
Draft
Active
ReviewRequired
Deprecated
Disabled
Archived
```

Suggested Capability Type values:

```text
HumanProfessionalCapability
SystemCapability
ServiceCapability
AIAgentCapability
WorkflowCapability
ProductCapability
IntegrationCapability
KnowledgeCapability
```

MVP controlled Capability Type values:

```text
HumanProfessionalCapability
SystemCapability
ServiceCapability
AIAgentCapability
WorkflowCapability
ProductCapability
IntegrationCapability
```

Suggested Capability Scope Type values:

```text
Domain
Object
Service
Workflow
API
Product
Agent
Jurisdiction
DataAccess
Operation
```

Do not treat a feature flag, endpoint or model skill as Core Capability by itself.

---

# 20. Codex Implementation Notes

Codex may implement Capability only from approved specs.

Codex must:

```text
cite this cross-cutting spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Capability / Permission boundary
preserve Capability / Policy boundary
preserve Capability / Service boundary
preserve Capability / AI Governance boundary
implement only Phase 1 Partial scope unless task says otherwise
write tests for capability registration
write tests for required scope
write tests for capability binding
write tests for capability contract reference
write tests preventing capability from granting permission
write tests preventing AI from inferring capability from tool existence
write tests preventing unscoped capability usage
```

Codex must not:

```text
turn Capability into Permission
turn Capability into Policy
turn Capability into Role
turn Capability into API endpoint
turn Capability into product feature flag only
grant access through Capability alone
allow AI to self-bind capabilities
infer capability from model or tool existence
implement capability marketplace in MVP
```

---

# 21. Validation Rules

Capability must pass the following checks.

```text
[ ] Capability is classified as Cross-Cutting Core System.
[ ] Capability is not counted as one of the baseline 26 Core Domains.
[ ] Capability does not change the baseline Core Domain Map.
[ ] Capability has MVP Phase 1 / Wave 1 classification.
[ ] Capability has MVP Depth = Partial Implement.
[ ] Capability defines Core meaning.
[ ] Capability boundary excludes Permission grant.
[ ] Capability boundary excludes Policy rule definition.
[ ] Capability boundary excludes Service implementation.
[ ] Capability boundary excludes AI final decision.
[ ] Capability owns Capability object.
[ ] Capability defines Capability Scope.
[ ] Capability defines Capability Binding.
[ ] Capability defines Capability Contract Reference.
[ ] Capability lists primary services.
[ ] Mutating Capability services emit events.
[ ] Capability lists primary events.
[ ] Capability defines contract requirements.
[ ] Capability defines AI Agent usage constraints.
[ ] Capability defines workflow usage constraints.
[ ] Capability defines API usage constraints.
[ ] Capability defines product consumers.
[ ] Capability defines MVP and deferred scope.
[ ] Capability defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This specification must not be used to:

```text
turn Capability into Permission
turn Capability into Policy
turn Capability into Role
turn Capability into Service implementation
turn Capability into API endpoint
turn Capability into product feature flag only
turn Capability into AI authority
grant access through Capability alone
allow AI to self-authorize capability
infer capability from model ability or tool existence
change baseline 26 Core Domains
allow Codex to define new capability architecture
```

---

# 23. Acceptance Criteria

This Capability Cross-Cutting Specification is accepted only if:

```text
[ ] It defines Capability purpose.
[ ] It defines Capability Core meaning.
[ ] It identifies Capability as Cross-Cutting Core System.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines core rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Identity, Permission, Policy, Knowledge, Workflow, Task, Event, AI Governance and Product Consumers.
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
| 0.1.0 | Draft | Initial Capability cross-cutting specification. Establishes Capability as Phase 1 Cross-Cutting Core System with Partial Implement depth, defines Capability, Scope, Binding, Contract Reference, services, events, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Cross-Cutting Specification**
