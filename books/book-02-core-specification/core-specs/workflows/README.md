# core-specs/workflows/

**Repository:** `book-02-core`  
**Directory:** `core-specs/workflows/`  
**Document:** `core-specs/workflows/README.md`  
**Book:** Book 02 — MarkOrbit Core Specification  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Directory Purpose

The `core-specs/workflows/` directory contains detailed Workflow Specification files for MarkOrbit Core.

A Workflow is a governed execution contract that coordinates Core Objects, Services, Events, Tasks, Reviews, Approvals and Responsibility Assignments.

This directory exists to define workflow execution without turning Core into product UI.

Workflows specify how Core meaning moves through professional execution.

They do not define screen flows, user journeys or product-specific interaction design.

Workflow specifications may be consumed by:

```text
Workplace
MarkReg
MarkOrbit Lite
AI Agents
Task systems
Review systems
Notification systems
Codex tasks
validation scripts
```

---

# 2. Canonical Workflow Rule

Book 02 uses the following canonical rule:

```text
Workflow coordinates execution.
Workflow does not define Core meaning.
Workflow must operate through Core Objects, Services, Events and Contracts.
```

Therefore:

```text
No Workflow Contract, no executable workflow.
No state model, no workflow.
No transition rules, no workflow.
No task and review rules, no professional execution.
No event mapping, no workflow trace.
No responsibility assignment, no accountable workflow.
```

---

# 3. Workflow Is Not UI Flow

A Core Workflow is not automatically:

```text
a product page
a wizard
a checklist UI
a kanban board
a status label
a chat flow
a form flow
a sales pipeline screen
a background job
```

A workflow may later be represented by those artifacts, but those artifacts do not define the Core Workflow.

Core workflow meaning comes first.

Product experience comes later.

---

# 4. Directory Boundary

## 4.1 workflows/ Owns

This directory owns:

```text
Workflow Specification files
workflow purpose
workflow ownership
workflow scope
workflow boundary
workflow participants
workflow states
workflow transitions
workflow tasks
workflow review rules
workflow approval rules
workflow responsibility rules
workflow service usage
workflow event mapping
workflow contract references
workflow AI usage
workflow notification usage
workflow failure behavior
workflow acceptance criteria
```

## 4.2 workflows/ Does Not Own

This directory does not own:

```text
Core Domain meaning
Core Object canonical meaning
Core Service responsibility
Core Event semantics
API endpoint design
AI Agent Contract definition
product UI
screen flow
database schema
background worker implementation
notification channel implementation
Codex implementation code
```

Those belong to other specification layers.

---

# 5. Source Chain

Every Workflow Specification file must cite its source chain.

Required source chain:

```text
B02-CH-16 — Core Execution Primitives
B02-CH-17 — Core Contract Architecture
B02-CH-27 — Core Consumption Specification
indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
core-specs/workflows/{workflow-name}.md
codex-tasks/{task}.md
```

Related sources may include:

```text
indexes/api-index.md
indexes/agent-index.md
indexes/codex-task-index.md
core-specs/contracts/
core-specs/services/
core-specs/events/
core-specs/agents/
B02-CH-28 — Core MVP Boundary
B02-CH-29 — MVP Domain Priority
B02-CH-30 — MVP Execution Matrix
B02-CH-31 — Codex Implementation Roadmap
```

---

# 6. Required Workflow Spec Groups

Workflow Specification files should be grouped by responsibility.

Expected directory structure:

```text
core-specs/workflows/README.md
core-specs/workflows/_template.md

core-specs/workflows/business-execution/
core-specs/workflows/professional-review/
core-specs/workflows/ai-governance/
core-specs/workflows/routing/
core-specs/workflows/communication/
core-specs/workflows/codex/
core-specs/workflows/validation/
```

Each subdirectory should contain workflow specs for the corresponding category.

---

# 7. Workflow Categories

This directory uses the following workflow categories.

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

A spec must use one canonical category.

---

# 8. Workflow Spec Metadata

Each Workflow Specification file must begin with metadata.

```text
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
**Status:** Draft
**Version:** 0.1.0
**MVP Phase/Wave:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Wave 0–7
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred
**Owner:** MarkOrbit Publications Editorial Board
```

---

# 9. Workflow Spec Required Sections

Every Workflow Specification must include the following sections.

```text
1. Purpose
2. Workflow Meaning
3. Workflow Category
4. Owning Domain or System
5. Participants
6. Scope
7. Boundary
8. Workflow Contract
9. State Model
10. Transition Rules
11. Task Rules
12. Review Rules
13. Approval Rules
14. Responsibility Rules
15. Service Usage
16. Event Mapping
17. Object Usage
18. API Usage
19. AI Agent Usage
20. Notification Usage
21. Failure Behavior
22. Idempotency and Safety
23. Product Consumers
24. MVP Scope
25. Deferred Scope
26. Data and Implementation Notes
27. Codex Implementation Notes
28. Validation Rules
29. Prohibited Overreach
30. Acceptance Criteria
31. Revision Notes
```

---

# 10. Workflow Ownership Rules

## 10.1 Every Workflow Must Have an Owner

Each workflow must have one primary owner.

The owner must be either:

```text
one of the 26 baseline Core Domains
or an explicitly declared cross-cutting Core specification system
or AI Governance
or Codex Task System
or Specification Governance
```

## 10.2 Workflow Ownership Is Not Product Ownership

Products may consume workflow specs, but products do not own Core Workflow meaning.

The following are consumers, not Core Workflow owners:

```text
Workplace
MarkReg
MarkOrbit Lite
MGSN
Partner Center
Client Portal
Service Platform
```

## 10.3 Cross-Domain Workflows Must Declare Primary Ownership

A workflow may coordinate multiple domains, but it must still have one primary owner.

Example:

```text
Order-to-Matter Conversion Workflow
    Primary Owner: Order
    Related Domain: Matter
```

---

# 11. Workflow Contract Rules

Every workflow must reference a Workflow Contract.

Workflow Contracts define:

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

Workflow Contract specs belong to:

```text
core-specs/contracts/workflow/
```

A workflow without a contract is not implementation-ready.

---

# 12. State Model Rules

Every executable workflow must define a state model.

State model must include:

```text
state name
state meaning
entry condition
exit condition
allowed transitions
blocking rules
review requirements
responsibility owner
events emitted
```

State names must be controlled.

Workflow specs must not allow arbitrary UI-defined states.

---

# 13. Transition Rules

Each workflow must define transition rules.

Transition rules must include:

```text
from state
to state
trigger
service invoked
permission required
policy required
review required
approval required
events emitted
failure behavior
audit requirement
```

Transitions must be performed through governed Core Services.

Product UI must not change workflow state directly.

---

# 14. Task Rules

Workflow task rules must define:

```text
task type
task owner
task creation service
task assignment service
task completion service
task review service
task events
deadline or due rule if applicable
failure behavior
```

Task-related objects include:

```text
Task
Task Assignment
Task Status
Review Record
Approval Record
Responsibility Assignment
```

---

# 15. Review Rules

Professional or high-risk workflows must define review rules.

Review rules must include:

```text
review trigger
review owner
review object
review status
blocking behavior
review events
approval requirement
rejection behavior
audit requirement
```

Review-sensitive workflows include:

```text
classification-review-workflow.md
document-review-workflow.md
evidence-review-workflow.md
ai-output-review-workflow.md
routing-review-workflow.md
codex-task-acceptance-workflow.md
```

---

# 16. Approval Rules

Approval rules must define:

```text
approval trigger
approver role
approval object
approval status
approval service
approval events
rejection events
post-approval transition
post-rejection transition
audit requirement
```

Approval is not a UI checkbox.

Approval is a Core responsibility action.

---

# 17. Responsibility Rules

Workflows must define responsibility assignment.

Responsibility rules should reference:

```text
Responsibility Assignment
Review Record
Approval Record
Task Assignment
Business Responsibility cross-cutting system
Permission
Policy
```

A workflow that affects professional execution must not proceed without accountable ownership.

---

# 18. Service Usage Rules

Workflow specs must list services used.

Use service types such as:

```text
workflow transition validation service
task creation service
task assignment service
task completion service
task review service
order-to-matter conversion service
classification review service
document validation service
AI output registration service
review assignment service
approval service
event publication service
notification dispatch service
```

Detailed service specs belong to:

```text
core-specs/services/
```

---

# 19. Event Mapping Rules

Workflow specs must map events.

Event mapping must define:

```text
event name
emitted by service
trigger point
workflow state affected
consumer service
audit requirement
review requirement
```

Workflow-related event examples:

```text
WorkflowContractCreated
WorkflowTransitionRequested
WorkflowTransitionApproved
WorkflowTransitionRejected
TaskCreated
TaskAssigned
TaskCompleted
TaskReviewRequired
ReviewRequired
ReviewApproved
ReviewRejected
OrderConvertedToMatter
MatterCreated
AIReviewRequired
CodexTaskAccepted
```

---

# 20. Object Usage Rules

Workflow specs must list Core Objects used.

Common workflow objects include:

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

Object meaning belongs to:

```text
core-specs/objects/
```

Workflow specs reference object usage and state interaction.

---

# 21. API Usage Rules

Workflow APIs must reference Workflow Contracts and Services.

Workflow APIs may:

```text
create tasks
assign tasks
request transitions
approve transitions
reject transitions
mark review required
record approval
record rejection
publish workflow events
```

Workflow APIs must not:

```text
skip required review
create unapproved workflow states
complete professional tasks without responsibility record
mutate Matter or Order status outside governed services
```

---

# 22. AI Agent Usage Rules

AI Agents may assist workflow but must not own professional responsibility.

AI workflow assistance may include:

```text
summarize workflow progress
suggest next task
identify overdue tasks
flag missing review
explain workflow state
prepare review notes
```

AI Agents must not:

```text
skip required review
approve their own output
complete professional tasks without human responsibility
create unapproved workflow states
mutate Core state outside governed services
```

AI workflow usage requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Human Review Rule
AI Audit Record
AI Events
```

---

# 23. Notification Usage Rules

Workflow specs may trigger notifications.

Notification usage must define:

```text
notification trigger
source event
recipient rule
permission scope
message sensitivity
review dependency
audit requirement
failure behavior
```

Notification channel implementation does not belong here.

Notification channel implementation belongs to product or infrastructure implementation.

---

# 24. Failure Behavior Rules

Every workflow must define failure behavior.

Failure types may include:

```text
invalid state transition
missing required task
missing review
review rejected
approval rejected
permission failure
policy failure
AI governance failure
missing responsibility owner
service failure
event publication failure
notification failure
idempotency conflict
timeout
```

For each failure type, define:

```text
result
state impact
event emitted if any
audit requirement
retry rule
review or escalation rule
```

---

# 25. Idempotency and Safety Rules

Workflow specs must define idempotency and safety behavior.

Required for:

```text
order-to-matter conversion
task creation
task assignment
workflow transition
review approval
AI output review
Codex task acceptance
event publication
```

Each spec should define:

```text
idempotency key or equivalent rule
duplicate transition handling
duplicate task handling
safe retry behavior
state conflict behavior
event duplication prevention
```

---

# 26. High-Priority Workflow Specs

Initial workflow specs should include:

```text
order-to-matter-conversion-workflow.md
classification-review-workflow.md
document-review-workflow.md
task-review-workflow.md
ai-output-review-workflow.md
routing-review-workflow.md
codex-task-acceptance-workflow.md
```

Additional baseline workflow specs may include:

```text
matter-lifecycle-workflow.md
trademark-status-review-workflow.md
communication-action-item-workflow.md
agent-contract-review-workflow.md
prohibited-overreach-review-workflow.md
spec-consistency-review-workflow.md
```

Reserved or future workflow specs may include:

```text
official-filing-workflow.md
opposition-response-workflow.md
renewal-management-workflow.md
service-provider-marketplace-workflow.md
opportunity-scoring-workflow.md
external-office-integration-workflow.md
```

Reserved workflows must not be production-enabled in MVP.

---

# 27. MVP Depth Rules

Workflow specs must preserve MVP depth from related indexes and specs.

Allowed values:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

A `Reserved Boundary` workflow may be specified at boundary level but should not be production-enabled in MVP.

A `Deferred` workflow should not be implemented without a later approved scope change.

---

# 28. Product Consumer Rules

Workflow specs must classify product consumers.

Consumer categories:

```text
MVP Consumer
Partial Consumer
Future Consumer
```

MVP consumers:

```text
Workplace
MarkReg
MarkOrbit Lite
AI Agents
Codex Implementation
```

Future consumers may include:

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

Products may consume workflows.

Products must not redefine Core Workflow meaning.

---

# 29. Data and Implementation Notes

Workflow specs may include implementation-facing notes.

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

# 30. Codex Implementation Rules

Codex tasks generated from workflow specs must:

```text
cite the workflow spec
cite related contract, service, event and object specs
preserve workflow state model
preserve transition rules
preserve review and approval rules
preserve responsibility rules
preserve event mapping
preserve MVP depth
preserve deferred scope
write tests
follow prohibited-overreach rules
```

Codex must not:

```text
create workflows without Workflow Contracts
create states outside the workflow spec
create transitions outside services
skip review or approval requirements
complete tasks without responsibility assignment
implement reserved workflows as MVP
turn workflow specs into product UI
```

---

# 31. Validation Rules

The `core-specs/workflows/` directory must pass the following checks.

```text
[ ] It contains README.md.
[ ] It contains _template.md before detailed specs.
[ ] Every workflow spec has metadata.
[ ] Every workflow spec has a Workflow Contract reference.
[ ] Every workflow spec defines participants.
[ ] Every workflow spec defines state model.
[ ] Every workflow spec defines transition rules.
[ ] Every workflow spec defines task rules.
[ ] Every review-sensitive workflow defines review rules.
[ ] Every approval-sensitive workflow defines approval rules.
[ ] Every workflow defines responsibility rules.
[ ] Every workflow lists service usage.
[ ] Every workflow maps events.
[ ] Every workflow lists object usage.
[ ] Every workflow defines API usage or explicit no-API reason.
[ ] Every AI-assisted workflow defines Agent Contract and audit requirements.
[ ] Every workflow defines notification usage or explicit no-notification reason.
[ ] Every workflow defines failure behavior.
[ ] Every workflow defines idempotency and safety rules.
[ ] No workflow is only a product UI flow.
[ ] No workflow bypasses Core Services.
[ ] No reserved workflow is production-enabled in MVP.
```

---

# 32. Prohibited Behavior

This directory must not:

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

---

# 33. Acceptance Criteria

The `core-specs/workflows/README.md` file is accepted when:

```text
[ ] It defines the purpose of core-specs/workflows/.
[ ] It defines Workflow as governed execution contract.
[ ] It states workflow coordinates execution but does not define Core meaning.
[ ] It distinguishes Workflow from UI flow.
[ ] It defines directory boundary.
[ ] It defines source chain requirements.
[ ] It defines required workflow spec groups.
[ ] It defines workflow categories.
[ ] It defines required metadata.
[ ] It defines required sections.
[ ] It defines workflow ownership rules.
[ ] It defines Workflow Contract rules.
[ ] It defines state model rules.
[ ] It defines transition rules.
[ ] It defines task rules.
[ ] It defines review rules.
[ ] It defines approval rules.
[ ] It defines responsibility rules.
[ ] It defines service usage rules.
[ ] It defines event mapping rules.
[ ] It defines object usage rules.
[ ] It defines API usage rules.
[ ] It defines AI Agent usage rules.
[ ] It defines notification usage rules.
[ ] It defines failure behavior rules.
[ ] It defines idempotency and safety rules.
[ ] It lists high-priority workflow specs.
[ ] It defines MVP depth rules.
[ ] It defines product consumer rules.
[ ] It defines data and implementation notes.
[ ] It defines Codex implementation rules.
[ ] It defines validation rules.
[ ] It defines prohibited behavior.
```

---

# 34. Next Action

After this README is accepted, generate:

```text
core-specs/workflows/_template.md
```

Do not generate detailed workflow specs before the template exists.

---

# 35. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial README for core-specs/workflows/. Defines directory purpose, workflow boundary, Workflow Contract rules, state/transition/task/review/approval/responsibility rules, AI and notification usage, validation rules and template handoff. |

---

**End of README**


## PUB-TASK-B02-002 Component Governance Reference

Workflow state models must consume `core-specs/workflows/components/workflow-state-definition.md`. Transition rules must consume `core-specs/workflows/components/workflow-transition-definition.md`. Free-text transitions cannot bypass terminal, guard, review, approval, event or failure semantics. Workflow Contracts do not own domain mutation and do not authorize protected external action.
