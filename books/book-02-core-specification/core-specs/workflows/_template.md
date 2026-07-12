# Workflow Specification Template

**Repository:** `book-02-core`  
**Directory:** `core-specs/workflows/`  
**Template ID:** B02-TPL-WORKFLOW  
**Template Type:** Workflow Specification Template  
**Source Chapters:** B02-CH-16 — Core Execution Primitives; B02-CH-17 — Core Contract Architecture; B02-CH-27 — Core Consumption Specification  
**Source Indexes:** indexes/object-index.md; indexes/service-index.md; indexes/event-index.md  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# How to Use This Template

Copy this template to the appropriate workflow category directory.

Recommended locations:

```text
core-specs/workflows/business-execution/{workflow-name}.md
core-specs/workflows/professional-review/{workflow-name}.md
core-specs/workflows/ai-governance/{workflow-name}.md
core-specs/workflows/routing/{workflow-name}.md
core-specs/workflows/communication/{workflow-name}.md
core-specs/workflows/codex/{workflow-name}.md
core-specs/workflows/validation/{workflow-name}.md
```

Use lowercase kebab-case filenames.

Examples:

```text
order-to-matter-conversion-workflow.md
classification-review-workflow.md
document-review-workflow.md
ai-output-review-workflow.md
routing-review-workflow.md
codex-task-acceptance-workflow.md
```

This template is for Core Workflow Specifications only.

Do not use this template for:

```text
product screen flows
wizards
kanban boards
UI checklists
chat flows
form flows
sales pipeline screens
background jobs without Core workflow meaning
```

A workflow may later be represented by UI, task boards, notifications or automation jobs, but those artifacts do not define the Core Workflow.

---

# Workflow Specification — {Workflow Name}

**Spec ID:** B02-WF-{WORKFLOW-ID}  
**Spec Type:** Workflow  
**Workflow Name:** {Workflow Name}  
**Workflow Category:** Business Execution | Professional Review | AI Governance | Routing | Communication | Codex | Validation | Reserved Boundary  
**Owning Domain/System:** {Domain or Cross-Cutting System}  
**Source Chapters:** B02-CH-16; B02-CH-17; B02-CH-27  
**Source Indexes:** indexes/object-index.md; indexes/service-index.md; indexes/event-index.md  
**Related Contract Specs:** core-specs/contracts/{contract}.md  
**Related Object Specs:** core-specs/objects/{object}.md  
**Related Service Specs:** core-specs/services/{service}.md  
**Related Event Specs:** core-specs/events/{event}.md  
**Related Agent Specs:** core-specs/agents/{agent}.md  
**Related API Specs:** core-specs/api/{api}.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase/Wave:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Wave 0–7  
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred  
**Primary Consumers:** Workplace | MarkReg | MarkOrbit Lite | AI Agents | Codex Implementation | Future Consumers  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Describe why this Core Workflow exists.

The purpose should answer:

```text
What execution process does this workflow coordinate?
Which Core Objects, Services, Events, Reviews, Approvals or Responsibility Assignments depend on it?
Why must this execution process be governed by Core rather than only by a product UI?
```

Example format:

```text
The {Workflow Name} coordinates ...
It exists so that ...
It is required by ...
```

---

# 2. Workflow Meaning

Define the canonical meaning of this workflow.

```text
{Workflow Name} means ...
```

The meaning must be execution-oriented and Core-level.

Do not define the workflow as:

```text
a product page
a wizard
a kanban column
a checklist UI
a button sequence
a chat flow
a background worker
```

Preferred definition pattern:

```text
This workflow defines the governed Core execution path for ...
```

---

# 3. Workflow Category

Select one canonical category.

```text
Business Execution Workflow
Professional Review Workflow
AI Governance Workflow
Routing Workflow
Communication Workflow
Codex Workflow
Validation Workflow
Reserved Boundary Workflow
```

Explain why the category is correct.

```text
This workflow belongs to {Workflow Category} because ...
```

---

# 4. Owning Domain or System

State the primary owner.

```text
Primary Owner: {Domain or Cross-Cutting System}
Owner Type: Baseline Core Domain | Cross-Cutting Core Specification System | AI Governance | Codex Task System | Specification Governance
```

Ownership rules:

```text
- Every workflow must have one primary owner.
- Cross-domain workflows must declare primary ownership.
- Product ownership is not Core workflow ownership.
- Cross-cutting ownership must be explicit.
```

Related domains or systems:

```text
- ...
- ...
```

---

# 5. Participants

List workflow participants.

Use this format:

| Participant | Participant Type | Role | Required | Notes |
|-------------|------------------|------|----------|-------|
| {Participant Name} | Human / System / AI Agent / Product / Service / External Actor | {Role} | Yes / No | {Notes} |

Participant types may include:

```text
Human Actor
Internal User
Reviewer
Approver
AI Agent
System Agent
Core Service
Product Consumer
External Professional Agent
Codex Agent
Validation Agent
```

---

# 6. Scope

Define what is inside this workflow.

```text
This workflow includes:
- ...
- ...
- ...
```

The scope should include governed execution, Core state movement, task creation, review, approval, responsibility, event mapping and failure behavior.

It should not include product screen design or physical workflow engine configuration.

---

# 7. Boundary

Define workflow boundary.

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
This workflow coordinates ...
This workflow invokes ...
This workflow emits ...
This workflow does not own ...
```

---

# 8. Workflow Contract

Reference the required Workflow Contract.

Detailed contract specs belong to:

```text
core-specs/contracts/workflow/
```

## 8.1 Workflow Contract Reference

```text
Workflow Contract: {Contract Name}
Contract File: core-specs/contracts/workflow/{contract-name}.md
```

## 8.2 Contract Requirements

The Workflow Contract must define:

```text
state model
allowed transitions
required services
required events
required tasks
review requirements
approval requirements
responsibility assignment
failure behavior
audit requirements
```

A workflow without a Workflow Contract is not implementation-ready.

---

# 9. State Model

Define the workflow state model.

Use controlled state names.

## 9.1 State List

Use this format:

| State | Meaning | Entry Condition | Exit Condition | Blocking Rules |
|-------|---------|-----------------|----------------|----------------|
| {State Name} | {Meaning} | {Entry Condition} | {Exit Condition} | {Blocking Rules} |

## 9.2 State Rules

```text
- States must be controlled.
- States must not be product UI labels only.
- States must map to Core Objects, Services and Events.
- State changes must occur through governed Core Services.
```

## 9.3 No-State Reason

If this workflow does not require a state model, state:

```text
This workflow does not require an independent state model because ...
```

---

# 10. Transition Rules

Define allowed transitions.

Use this format:

| From State | To State | Trigger | Service Invoked | Permission | Policy | Review | Approval | Events Emitted |
|------------|----------|---------|-----------------|------------|--------|--------|----------|----------------|
| {From} | {To} | {Trigger} | {Service} | {Permission} | {Policy} | Yes / No | Yes / No | {Events} |

Rules:

```text
- Transitions must be performed through governed Core Services.
- Product UI must not change workflow state directly.
- AI Agents must not approve or complete transitions outside Agent Contract and review rules.
- Transitions that affect professional responsibility must produce audit traces.
```

---

# 11. Task Rules

Define task behavior.

Use this format:

| Task | Created By Service | Assigned To | Completion Rule | Review Required | Events |
|------|--------------------|-------------|-----------------|-----------------|--------|
| {Task Name} | {Service} | {Owner} | {Rule} | Yes / No | {Events} |

Task rules should define:

```text
task type
task owner
task creation service
task assignment service
task completion service
task review service
deadline or due rule if applicable
failure behavior
```

Task-related objects:

```text
Task
Task Assignment
Task Status
Review Record
Approval Record
Responsibility Assignment
```

---

# 12. Review Rules

Define review requirements.

Use this structure:

```text
Review Required: Yes / No

Review Trigger:
- ...

Review Owner:
- ...

Review Object:
- Review Record
- Approval Record
- Responsibility Assignment

Review Statuses:
- ReviewRequired
- ReviewApproved
- ReviewRejected
- Superseded

Review Events:
- ReviewRequired
- ReviewApproved
- ReviewRejected

Blocking Behavior:
- none
- blocks external use
- blocks state transition
- blocks final output
- advisory only
```

Professional or high-risk workflows must define review rules.

---

# 13. Approval Rules

Define approval requirements.

Use this structure:

```text
Approval Required: Yes / No

Approval Trigger:
- ...

Approver Role:
- ...

Approval Object:
- Approval Record

Approval Service:
- ...

Approval Events:
- ReviewApproved
- WorkflowTransitionApproved
- ...

Rejection Events:
- ReviewRejected
- WorkflowTransitionRejected
- ...

Post-Approval Transition:
- ...

Post-Rejection Transition:
- ...
```

Approval is a Core responsibility action.

It is not a UI checkbox.

---

# 14. Responsibility Rules

Define responsibility assignment.

Use this structure:

```text
Responsibility Required: Yes / No

Responsibility Objects:
- Responsibility Assignment
- Task Assignment
- Review Record
- Approval Record

Responsible Actor Types:
- ...

Assignment Rules:
- ...

Escalation Rules:
- ...

Responsibility Events:
- ResponsibilityAssigned
- TaskAssigned
- ReviewRequired
```

A workflow that affects professional execution must not proceed without accountable ownership.

---

# 15. Service Usage

List Core Services used by this workflow.

Source:

```text
indexes/service-index.md
```

Use this format:

| Service | Workflow Role | Invoked At | Required | Notes |
|---------|---------------|------------|----------|-------|
| {Service Name} | transition / task / review / approval / event / validation / notification | {State or Transition} | Yes / No | {Notes} |

Detailed service specs belong to:

```text
core-specs/services/
```

---

# 16. Event Mapping

Map workflow events.

Source:

```text
indexes/event-index.md
```

Use this format:

| Event | Emitted By | Trigger Point | State Impact | Consumers | Audit Required |
|-------|------------|---------------|--------------|-----------|----------------|
| {Event Name} | {Service} | {State/Transition} | {Impact} | {Consumers} | Yes / No |

Workflow event mapping must preserve:

```text
source service
trigger point
workflow state affected
consumer service
audit requirement
review requirement
```

---

# 17. Object Usage

List Core Objects used by this workflow.

Source:

```text
indexes/object-index.md
```

Use this format:

| Object | Workflow Role | State Impact | Notes |
|--------|---------------|--------------|-------|
| {Object Name} | input / output / state object / task object / review object / approval object / event reference | {Impact} | {Notes} |

Common workflow objects:

```text
Workflow Contract
Workflow State
Workflow Transition
Task
Task Assignment
Task Status
Matter
Order
Review Record
Approval Record
Responsibility Assignment
AI Output
AI Recommendation
Codex Task
Validation Report
```

---

# 18. API Usage

Define API usage.

```text
API usage:
    none / internal / product / agent / admin / integration
```

Related APIs:

```text
- ...
```

Rules:

```text
- Workflow APIs must reference Workflow Contracts and Services.
- Workflow APIs must not skip required review.
- Workflow APIs must not create unapproved workflow states.
- Workflow APIs must not mutate Matter or Order status outside governed services.
```

If no API usage is required, state:

```text
This workflow does not require MVP API exposure.
```

---

# 19. AI Agent Usage

Define AI Agent usage.

## 19.1 AI Assistance

```text
AI usage:
    none / optional / required / prohibited
```

Allowed AI assistance:

```text
AI may:
- summarize workflow progress
- suggest next task
- identify overdue tasks
- flag missing review
- explain workflow state
- prepare review notes
```

## 19.2 Prohibited AI Behavior

```text
AI must not:
- skip required review
- approve its own output
- complete professional tasks without human responsibility
- create unapproved workflow states
- mutate Core state outside governed services
```

## 19.3 Required AI Governance

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

If AI is not relevant, state:

```text
This workflow does not require MVP AI usage.
```

---

# 20. Notification Usage

Define notification usage.

```text
Notification usage:
    none / optional / required
```

Notification rules:

```text
Notification Trigger:
- ...

Source Event:
- ...

Recipient Rule:
- ...

Permission Scope:
- ...

Message Sensitivity:
- ...

Review Dependency:
- ...

Audit Requirement:
- ...

Failure Behavior:
- ...
```

Notification channel implementation does not belong here.

---

# 21. Failure Behavior

Define failure behavior.

Use this format:

| Failure Type | Result | State Impact | Event Emitted | Audit Required | Retry Rule | Escalation |
|--------------|--------|--------------|---------------|----------------|------------|------------|
| invalid state transition | ... | ... | ... | ... | ... | ... |
| missing required task | ... | ... | ... | ... | ... | ... |
| missing review | ... | ... | ... | ... | ... | ... |
| review rejected | ... | ... | ... | ... | ... | ... |
| approval rejected | ... | ... | ... | ... | ... | ... |
| permission failure | ... | ... | ... | ... | ... | ... |
| policy failure | ... | ... | ... | ... | ... | ... |
| AI governance failure | ... | ... | ... | ... | ... | ... |
| missing responsibility owner | ... | ... | ... | ... | ... | ... |
| service failure | ... | ... | ... | ... | ... | ... |
| event publication failure | ... | ... | ... | ... | ... | ... |
| notification failure | ... | ... | ... | ... | ... | ... |
| idempotency conflict | ... | ... | ... | ... | ... | ... |

Add workflow-specific failure types as needed.

---

# 22. Idempotency and Safety

Define idempotency and safety behavior.

This is required for workflows that create or mutate Core state.

Use this structure:

```text
Idempotency required: Yes / No

Idempotency Rule:
- ...

Duplicate Transition Handling:
- ...

Duplicate Task Handling:
- ...

Safe Retry Behavior:
- ...

State Conflict Behavior:
- ...

Event Duplication Prevention:
- ...

Review Duplication Prevention:
- ...
```

If idempotency is not relevant, state:

```text
This workflow does not mutate Core state and does not require idempotency beyond standard request tracing.
```

---

# 23. Product Consumers

Classify product consumers.

## 23.1 MVP Consumers

```text
- Workplace
- MarkReg
- MarkOrbit Lite
- AI Agents
- Codex Implementation
```

## 23.2 Partial Consumers

```text
- MGSN
- Opportunity Engine baseline
- Brand Asset Vault baseline
```

## 23.3 Future Consumers

```text
- Partner Center
- Client Portal
- Service Platform
- External Integrations
- Reporting Consumers
```

Only list consumers that actually consume this workflow.

Products may consume workflows.

Products must not redefine Core Workflow meaning.

---

# 24. MVP Scope

Define MVP scope for this workflow.

```text
MVP includes:
- ...
- ...
```

## 24.1 MVP Phase or Wave

```text
Phase/Wave: {Phase or Wave}
```

## 24.2 MVP Depth

```text
Depth: Must Implement | Partial Implement | Reserved Boundary | Deferred
```

## 24.3 MVP Acceptance Summary

```text
MVP acceptance requires:
- ...
- ...
```

---

# 25. Deferred Scope

Define what is explicitly deferred.

```text
Deferred:
- ...
- ...
```

Deferred scope must not be implemented by Codex unless a later approved task changes scope.

Reserved workflows must not be production-enabled in MVP.

---

# 26. Data and Implementation Notes

Provide implementation-facing notes without defining product UI or physical workflow engine configuration.

Allowed notes:

```text
workflow must use controlled states
workflow must emit events for transitions
workflow must preserve review records
workflow must preserve responsibility assignment
workflow must be idempotent for state transitions
workflow must audit high-risk transitions
workflow must prevent duplicate task creation
workflow must enforce permission and policy before transition
```

Prohibited notes:

```text
UI screen design
kanban board layout
controller implementation
background worker code
physical database schema
vendor-specific workflow engine configuration
undocumented shortcut around Core Services
```

---

# 27. Codex Implementation Notes

Define how Codex may implement this workflow.

Codex must:

```text
- cite this workflow spec
- cite related contract, service, event and object specs
- preserve workflow state model
- preserve transition rules
- preserve review and approval rules
- preserve responsibility rules
- preserve event mapping
- preserve MVP depth
- preserve deferred scope
- write tests
- follow prohibited-overreach rules
```

Codex must not:

```text
- create workflows without Workflow Contracts
- create states outside the workflow spec
- create transitions outside services
- skip review or approval requirements
- complete tasks without responsibility assignment
- implement reserved workflows as MVP
- turn workflow specs into product UI
```

Related Codex Tasks:

```text
- B02-CX-W{wave}-{sequence} — {Task Title}
```

---

# 28. Validation Rules

This Workflow Specification must pass the following checks.

```text
[ ] Workflow name matches approved index or approved workflow list.
[ ] Workflow category is defined.
[ ] Owning domain or system is defined.
[ ] Workflow Contract is referenced.
[ ] Participants are defined.
[ ] Scope and boundary are defined.
[ ] State model is defined.
[ ] Transition rules are defined.
[ ] Task rules are defined.
[ ] Review rules are defined or explicitly not required.
[ ] Approval rules are defined or explicitly not required.
[ ] Responsibility rules are defined.
[ ] Service usage is listed.
[ ] Event mapping is listed.
[ ] Object usage is listed.
[ ] API usage is defined or explicitly not required.
[ ] AI Agent usage is defined or explicitly not required.
[ ] Notification usage is defined or explicitly not required.
[ ] Failure behavior is defined.
[ ] Idempotency and safety are defined.
[ ] Product consumers are classified.
[ ] MVP scope is defined.
[ ] Deferred scope is defined.
[ ] Codex implementation notes are included.
[ ] Prohibited overreach is defined.
```

---

# 29. Prohibited Overreach

This workflow spec must not be used to:

```text
treat product UI flows as Core Workflows
create workflows without Workflow Contracts
create arbitrary workflow states
create transitions outside Core Services
skip required review
skip required approval
skip responsibility assignment
allow AI to approve its own output
allow product UI to mutate workflow state directly
implement reserved future workflows as MVP
define screen layouts
define physical workflow engine configuration
define database schema
```

Add workflow-specific prohibited overreach:

```text
- ...
- ...
```

---

# 30. Acceptance Criteria

This Workflow Specification is accepted only if:

```text
[ ] It defines the workflow purpose.
[ ] It defines workflow meaning.
[ ] It identifies workflow category.
[ ] It identifies owning domain or system.
[ ] It defines participants.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It references Workflow Contract.
[ ] It defines state model.
[ ] It defines transition rules.
[ ] It defines task rules.
[ ] It defines review rules.
[ ] It defines approval rules.
[ ] It defines responsibility rules.
[ ] It lists service usage.
[ ] It maps events.
[ ] It lists object usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines notification usage.
[ ] It defines failure behavior.
[ ] It defines idempotency and safety.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes data and implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 31. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial workflow specification created from B02-TPL-WORKFLOW. |

---

**End of Workflow Specification**


## PUB-TASK-B02-002 Component Governance Reference

Workflow state models must consume `core-specs/workflows/components/workflow-state-definition.md`. Transition rules must consume `core-specs/workflows/components/workflow-transition-definition.md`. Free-text transitions cannot bypass terminal, guard, review, approval, event or failure semantics. Workflow Contracts do not own domain mutation and do not authorize protected external action.
