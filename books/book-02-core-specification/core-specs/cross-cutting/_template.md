# Cross-Cutting Specification Template

**Repository:** `book-02-core`  
**Directory:** `core-specs/cross-cutting/`  
**Template ID:** B02-TPL-CROSS-CUTTING  
**Template Type:** Cross-Cutting Specification Template  
**Source Chapters:** B02-CH-19 — Capability Specification; B02-CH-21 — Business Responsibility Specification; B02-CH-26 — AI Capability and Agent Governance Specification; B02-CH-31 — Codex Implementation Roadmap  
**Source Indexes:** indexes/domain-index.md; indexes/object-index.md; indexes/service-index.md; indexes/event-index.md; indexes/api-index.md; indexes/agent-index.md; indexes/codex-task-index.md  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# How to Use This Template

Copy this template to:

```text
core-specs/cross-cutting/{system-name}.md
```

Use lowercase kebab-case filenames.

Examples:

```text
capability.md
business-responsibility.md
policy.md
review-and-approval.md
audit.md
ai-governance.md
specification-governance.md
codex-governance.md
```

This template is for cross-cutting Core specification systems.

Do not use this template to silently create new baseline Core Domains.

The baseline Core Domain Map contains 26 domains.

Capability and Business Responsibility are cross-cutting Core specification systems.

They are not counted as additional baseline Core Domains.

---

# Cross-Cutting Specification — {System Name}

**Spec ID:** B02-XCUT-{SYSTEM-ID}  
**Spec Type:** Cross-Cutting  
**System Name:** {System Name}  
**System Category:** Capability | Business Responsibility | Policy | Review and Approval | Audit | AI Governance | Specification Governance | Codex Governance | Other Cross-Cutting  
**Owning Layer:** Core  
**Source Chapters:** B02-CH-19; B02-CH-21; B02-CH-26; B02-CH-31  
**Source Indexes:** indexes/domain-index.md; indexes/object-index.md; indexes/service-index.md; indexes/event-index.md; indexes/api-index.md; indexes/agent-index.md; indexes/codex-task-index.md  
**Related Domain Specs:** core-specs/domains/{domain}.md  
**Related Object Specs:** core-specs/objects/{object}.md  
**Related Service Specs:** core-specs/services/{service}.md  
**Related Event Specs:** core-specs/events/{event}.md  
**Related Contract Specs:** core-specs/contracts/{contract}.md  
**Related API Specs:** core-specs/api/{api}.md  
**Related Agent Specs:** core-specs/agents/{agent}.md  
**Related Workflow Specs:** core-specs/workflows/{workflow}.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase/Wave:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Wave 0–7  
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred  
**Primary Consumers:** MarkReg | MarkOrbit Lite | Workplace | AI Agents | Codex Implementation | Future Consumers  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Describe why this cross-cutting system exists.

The purpose should answer:

```text
What repeated Core concern does this system govern?
Why does this concern cross multiple domains?
Why should it not be treated as an ordinary baseline Core Domain?
Which objects, services, events, contracts, APIs, agents or workflows depend on it?
```

Example format:

```text
The {System Name} system governs ...
It exists so that ...
It crosses domains because ...
It is not a baseline Core Domain because ...
```

---

# 2. Cross-Cutting Meaning

Define the canonical meaning of this cross-cutting system.

```text
{System Name} means ...
```

The meaning must be governance-oriented and Core-level.

Do not define the system as:

```text
a new Core Domain
a product module
a database table group
a UI section
a reporting category
an implementation helper
```

Preferred definition pattern:

```text
This cross-cutting system defines the shared Core rules for ...
```

---

# 3. System Category

Select one canonical category.

```text
Capability
Business Responsibility
Policy
Review and Approval
Audit
AI Governance
Specification Governance
Codex Governance
Other Cross-Cutting
```

Explain why the category is correct.

```text
This system belongs to {System Category} because ...
```

---

# 4. Architectural Position

Define the architectural position of this system.

Use this structure:

```text
Layer:
    Core

Relationship to Domains:
    cross-cutting over selected baseline Core Domains

Relationship to Objects:
    defines or governs selected objects

Relationship to Services:
    constrains or enables selected services

Relationship to Events:
    requires or emits selected events

Relationship to Contracts:
    requires explicit contracts

Relationship to Products:
    consumed by products but not owned by products

Relationship to Codex:
    implemented only through approved specs and tasks
```

---

# 5. Domain Baseline Rule

State whether this system changes the 26-domain baseline.

Default:

```text
This cross-cutting system does not change the baseline Core Domain Map.
It must not be counted as an additional baseline Core Domain.
```

If a future architecture release changes the domain map, it must be documented outside this template through a formal architecture release.

---

# 6. Scope

Define what is inside this cross-cutting system.

```text
This system includes:
- ...
- ...
- ...
```

The scope should include cross-domain governance, contracts, rules, responsibilities, validation requirements and execution constraints.

It should not include product UI, database implementation, unapproved automation or future marketplace scope.

---

# 7. Boundary

Define the system boundary.

## 7.1 In Boundary

```text
- ...
- ...
```

## 7.2 Out of Boundary

```text
- ...
- ...
```

## 7.3 Boundary Notes

Explain boundary-sensitive distinctions.

Examples:

```text
This system governs ...
This system references ...
This system constrains ...
This system does not own ...
```

---

# 8. Participating Domains

List baseline Core Domains affected by this cross-cutting system.

Source:

```text
indexes/domain-index.md
```

Use this format:

| Domain | Relationship | MVP Scope | Notes |
|--------|--------------|-----------|-------|
| {Domain Name} | governed / enabled / constrained / reviewed / audited / validated | Must / Partial / Reserved / Future | {Notes} |

Only list domains actually affected.

Do not add new domains.

---

# 9. Primary Objects

List Core Objects governed or created by this system.

Source:

```text
indexes/object-index.md
```

Use this format:

| Object | Ownership | Role | MVP Depth | Notes |
|--------|-----------|------|-----------|-------|
| {Object Name} | {Domain/System} | governed / created / referenced / reviewed / audited / validated | {Depth} | {Notes} |

Rules:

```text
- Objects must have an owning domain or explicit cross-cutting system.
- Product ownership is not Core ownership.
- Objects must not be created only for implementation convenience.
```

Detailed object specs belong to:

```text
core-specs/objects/
```

---

# 10. Primary Services

List Core Services governed or required by this system.

Source:

```text
indexes/service-index.md
```

Use this format:

| Service | Owning Domain/System | Role | MVP Depth | Notes |
|---------|----------------------|------|-----------|-------|
| {Service Name} | {Owner} | governed / required / constrained / validation / review / audit | {Depth} | {Notes} |

Rules:

```text
- Services must operate Core meaning.
- Services must have object relationships.
- Mutating services must emit events.
- High-risk services must preserve review and audit rules.
```

Detailed service specs belong to:

```text
core-specs/services/
```

---

# 11. Primary Events

List Core Events governed or emitted by this system.

Source:

```text
indexes/event-index.md
```

Use this format:

| Event | Source Service | Role | MVP Depth | Notes |
|-------|----------------|------|-----------|-------|
| {Event Name} | {Service Name} | emitted / consumed / required / audit / review / validation | {Depth} | {Notes} |

Rules:

```text
- Events must represent meaningful Core change.
- Events must not be logs or UI actions.
- AI and high-risk events must preserve review and audit references.
```

Detailed event specs belong to:

```text
core-specs/events/
```

---

# 12. Primary Contracts

List required contracts.

Contract types may include:

```text
Capability Contract
Business Responsibility Contract
Policy Contract
Review Contract
Approval Contract
Audit Contract
Agent Contract
AI Governance Contract
Codex Task Contract
Validation Contract
Permission Contract
API Contract
Workflow Contract
```

Use this format:

| Contract | Contract Type | Required For | Notes |
|----------|---------------|--------------|-------|
| {Contract Name} | {Type} | {Usage} | {Notes} |

Detailed contract specs belong to:

```text
core-specs/contracts/
```

---

# 13. API Usage

Define API usage.

```text
API usage:
    none / internal / product / agent / admin / integration / validation
```

Related APIs:

```text
- ...
```

API rules:

```text
- APIs must reference approved services and contracts.
- APIs must not define Core meaning.
- High-risk APIs require permission, policy, review and audit.
- Agent APIs require Agent Contract authorization.
```

If no API usage is required, state:

```text
This cross-cutting system does not require MVP API exposure.
```

---

# 14. AI Agent Usage

Define AI Agent usage.

## 14.1 AI Assistance

```text
AI usage:
    none / optional / required / prohibited
```

Allowed AI assistance:

```text
AI may:
- ...
- ...
```

Prohibited AI behavior:

```text
AI must not:
- ...
- ...
```

## 14.2 Required AI Governance

If AI is used, define:

```text
AI Agent required: Yes / No
Agent Contract required: Yes / No
Authorized Knowledge required: Yes / No
Human Review required: Yes / No
AI Audit Record required: Yes / No
Related AI Events:
    - ...
```

AI must not replace professional responsibility.

---

# 15. Workflow Usage

Define workflow usage.

```text
Workflow usage:
    none / review / approval / responsibility / audit / validation / Codex acceptance / AI output review
```

Related workflows:

```text
- ...
```

Workflow rules:

```text
- Workflow must operate through Core Objects, Services, Events and Contracts.
- Workflow must not define Core meaning.
- Workflow must preserve review, approval and responsibility rules.
```

If no workflow usage is required, state:

```text
This cross-cutting system does not require MVP workflow execution.
```

---

# 16. Policy Rules

Define policy rules if this system governs policy.

Use this structure:

```text
Applicable Policies:
- ...

Policy Source:
- ...

Policy Evaluation Point:
- before object access
- before service invocation
- before mutation
- before AI use
- before external exposure
- before review or approval
- before Codex task acceptance

Policy Violation Behavior:
- result:
- event emitted:
- audit required:
- review required:
```

If policy is not relevant, state:

```text
This cross-cutting system does not define policy rules.
```

---

# 17. Review and Approval Rules

Define review and approval rules if applicable.

Use this structure:

```text
Review Required: Yes / No
Approval Required: Yes / No

Review Trigger:
- ...

Review Owner:
- ...

Approval Owner:
- ...

Review Objects:
- Review Record
- Approval Record
- Responsibility Assignment

Review Events:
- ReviewRequired
- ReviewApproved
- ReviewRejected

Blocking Behavior:
- none
- blocks external use
- blocks state transition
- blocks final output
- blocks Codex acceptance
- advisory only
```

If review is not relevant, state:

```text
This cross-cutting system does not require MVP review or approval behavior.
```

---

# 18. Audit Rules

Define audit rules.

Use this structure:

```text
Audit Required: Yes / No

Audit Trigger:
- ...

Audit Objects:
- AI Audit Record
- Event Audit Reference
- Review Record
- Approval Record
- Validation Report

Audit Content:
- actor identity
- system name
- objects accessed
- services invoked
- policy context
- review status
- output reference
- event IDs
- timestamp
```

Audit is required when this system affects:

```text
professional judgment
legal or business state
AI output
recommendation
review or approval
responsibility assignment
permission or policy
Codex task acceptance
prohibited overreach detection
```

---

# 19. Governance Rules

Define governance rules for this cross-cutting system.

Use this structure:

```text
Governance Owner:
- ...

Governance Inputs:
- ...

Governance Outputs:
- ...

Governance Events:
- ...

Governance Review:
- ...

Governance Audit:
- ...

Governance Failure Behavior:
- ...
```

Governance rules must prevent silent expansion of Core scope.

---

# 20. MVP Scope

Define MVP scope.

```text
MVP includes:
- ...
- ...
```

## 20.1 MVP Phase or Wave

```text
Phase/Wave: {Phase or Wave}
```

## 20.2 MVP Depth

```text
Depth: Must Implement | Partial Implement | Reserved Boundary | Deferred
```

## 20.3 MVP Acceptance Summary

```text
MVP acceptance requires:
- ...
- ...
```

---

# 21. Deferred Scope

Define explicitly deferred scope.

```text
Deferred:
- ...
- ...
```

Deferred scope must not be implemented by Codex unless a later approved task changes scope.

Reserved systems or behaviors must not be production-enabled in MVP.

---

# 22. Data and Implementation Notes

Provide implementation-facing notes without defining physical implementation.

Allowed notes:

```text
system requires explicit ownership
system requires controlled status values
system requires source references
system requires audit references
system requires review records
system requires policy evaluation
system requires validation checks
system must preserve MVP depth
```

Prohibited notes:

```text
physical database schema
UI component design
controller implementation
vendor-specific infrastructure
unreviewed automation
undocumented shortcut around Core Services
```

---

# 23. Codex Implementation Notes

Define how Codex may implement this cross-cutting system.

Codex must:

```text
- cite this cross-cutting spec
- cite related indexes
- cite related object, service, event, contract, API, agent or workflow specs
- preserve cross-cutting classification
- preserve the 26-domain baseline
- preserve MVP depth
- preserve deferred scope
- write tests
- follow prohibited-overreach rules
```

Codex must not:

```text
- convert this system into a new baseline Core Domain
- create unapproved domains
- create unowned objects
- create services without contracts
- create AI behavior without Agent Contract
- skip review or audit requirements
- implement deferred scope as MVP
- define architecture through implementation
```

Related Codex Tasks:

```text
- B02-CX-W{wave}-{sequence} — {Task Title}
```

---

# 24. Validation Rules

This Cross-Cutting Specification must pass the following checks.

```text
[ ] System name is defined.
[ ] System category is defined.
[ ] System does not silently change the 26-domain baseline.
[ ] Architectural position is defined.
[ ] Participating domains are listed.
[ ] Primary objects are listed or explicit no-object reason is provided.
[ ] Primary services are listed or explicit no-service reason is provided.
[ ] Primary events are listed or explicit no-event reason is provided.
[ ] Primary contracts are listed.
[ ] API usage is defined or explicitly not required.
[ ] AI Agent usage is defined or explicitly not required.
[ ] Workflow usage is defined or explicitly not required.
[ ] Policy rules are defined or explicitly not relevant.
[ ] Review and approval rules are defined or explicitly not relevant.
[ ] Audit rules are defined.
[ ] Governance rules are defined.
[ ] MVP scope is defined.
[ ] Deferred scope is defined.
[ ] Codex implementation notes are included.
[ ] Prohibited overreach is defined.
```

---

# 25. Prohibited Overreach

This cross-cutting spec must not be used to:

```text
change the 26-domain baseline
silently add a new baseline Core Domain
treat Capability as an ordinary domain
treat Business Responsibility as an ordinary domain
create product modules as cross-cutting systems
create unowned objects
create services without contracts
create events without source services
create AI behavior without Agent Contract
skip professional review
skip audit for high-risk execution
allow Codex to define architecture
implement deferred scope as MVP
define product UI
define physical database schema
```

Add system-specific prohibited overreach:

```text
- ...
- ...
```

---

# 26. Acceptance Criteria

This Cross-Cutting Specification is accepted only if:

```text
[ ] It defines the system purpose.
[ ] It defines cross-cutting meaning.
[ ] It identifies system category.
[ ] It defines architectural position.
[ ] It preserves the 26-domain baseline.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It lists participating domains.
[ ] It lists primary objects or explicit no-object reason.
[ ] It lists primary services or explicit no-service reason.
[ ] It lists primary events or explicit no-event reason.
[ ] It lists primary contracts.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines workflow usage.
[ ] It defines policy rules.
[ ] It defines review and approval rules.
[ ] It defines audit rules.
[ ] It defines governance rules.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes data and implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial cross-cutting specification created from B02-TPL-CROSS-CUTTING. |

---

**End of Cross-Cutting Specification**
