# Workflow Contracts — README

**Spec ID:** B02-CONTRACT-WORKFLOW-README  
**Spec Type:** Workflow Contract Index / README  
**Contract File:** core-specs/contracts/workflows/README.md  
**Contract Category:** Workflow Contracts  
**Related Core Specs:** core-specs/contracts/README.md; core-specs/contracts/template.md; core-specs/contracts/api/README.md; core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Related Core Domains:** Workflow Contract; Task; Event; Matter; Order; Customer; Trademark; Document; Evidence; Communication; Routing; Service Provider; Service Network; Partner; Permission; Policy; Agent  
**Related Service Specs:** core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md; core-specs/services/event-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/communication-service.md; core-specs/services/routing-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md  
**Related API Specs:** core-specs/api/workflow-contract-api.md; core-specs/api/task-api.md; core-specs/api/event-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/communication-api.md; core-specs/api/routing-api.md  
**Related Agent Specs:** core-specs/agents/workflow-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This README defines the purpose, boundary, file structure, naming rules and implementation expectations for MarkOrbit Workflow Contracts.

Workflow Contracts describe governed, reusable execution patterns for professional trademark and business-service workflows. They connect Core primitives such as Matter, Order, Task, Event, Communication, Document, Evidence, Routing and AI Agent preparation without allowing any one workflow file to bypass owning services.

Workflow Contracts are not generic BPM diagrams. They are Core execution contracts.

They define:

```text
workflow purpose
workflow trigger context
workflow target object context
workflow step contract
task creation boundary
event trace expectations
human review checkpoints
permission and policy checkpoints
AI assistance boundary
idempotency expectations
error handling expectations
Codex implementation expectations
acceptance criteria
```

---

# 2. Core Lock

```text
Workflow Contracts define governed execution patterns.
Workflow Contract Service owns workflow contract behavior.
Task Service owns active task creation.
Owning domain services own domain state.
Permission and Policy govern every workflow action.
AI may prepare, summarize and suggest, but must not execute protected actions.
Events preserve trace.
```

This lock applies to every file under:

```text
core-specs/contracts/workflows/
```

---

# 3. What Workflow Contracts Are

Workflow Contracts are canonical execution specifications for repeatable processes.

Examples:

```text
customer intake workflow
trademark application workflow
office action response workflow
renewal workflow
assignment workflow
evidence review workflow
provider routing workflow
communication review workflow
```

Each Workflow Contract must define:

```text
who or what may trigger it
which target object it applies to
which services must be invoked
which tasks may be created
which events may be emitted
which decisions require human review
which AI assistance is allowed
which policy restrictions may block or redact workflow behavior
```

---

# 4. What Workflow Contracts Are Not

Workflow Contracts are not:

```text
UI flowcharts
generic BPMN diagrams
database schemas
service implementations
permission grants
policy approvals
task execution engines
AI autonomous execution plans
legal opinions
professional truth
payment approvals
external delivery mechanisms
```

A workflow can coordinate behavior, but it does not own the professional truth of the underlying domain object.

---

# 5. Architectural Position

Workflow Contracts sit between Core API/Service contracts and execution primitives.

Canonical position:

```text
Principles define
↓
Core provides
↓
Business owns
↓
Workflow Contracts coordinate
↓
Tasks execute
↓
Events preserve trace
↓
Products consume
```

Workflow Contracts depend on:

```text
Common Contracts
API Contracts
Service Specs
Object Specs
Event Specs
Agent Specs
Permission / Policy
Human Review
Idempotency
Versioning
```

Workflow Contracts must not bypass:

```text
owning domain services
Permission Service
Policy Service
Task Service
Event Service
Human Review requirements
AI Agent Governance
```

---

# 6. Workflow Contract File Naming

Workflow contract files use:

```text
core-specs/contracts/workflows/{workflow-name}-workflow-contract.md
```

Examples:

```text
core-specs/contracts/workflows/customer-intake-workflow-contract.md
core-specs/contracts/workflows/trademark-application-workflow-contract.md
core-specs/contracts/workflows/office-action-response-workflow-contract.md
core-specs/contracts/workflows/renewal-workflow-contract.md
core-specs/contracts/workflows/assignment-workflow-contract.md
core-specs/contracts/workflows/evidence-review-workflow-contract.md
core-specs/contracts/workflows/provider-routing-workflow-contract.md
core-specs/contracts/workflows/communication-review-workflow-contract.md
```

Rules:

```text
- File names must be lowercase.
- Words must be separated by hyphens.
- File names must end with -workflow-contract.md.
- Each file must identify its owning Workflow Contract type.
- Each file must cite related API, Service, Object, Event and Agent specs.
```

---

# 7. Required Workflow Contract Sections

Each Workflow Contract must include:

```text
1. Purpose
2. Core Lock
3. Contract Meaning
4. Workflow Boundary
5. Trigger Context
6. Target Object Context
7. Required Services
8. Required References
9. Workflow Step Contract
10. Task Creation Rules
11. Event Rules
12. Permission Rules
13. Policy Rules
14. AI Assistance Rules
15. Human Review Rules
16. Idempotency Rules
17. Error Rules
18. Versioning Rules
19. Codex Implementation Notes
20. Acceptance Criteria
21. Revision Notes
```

Optional sections may include:

```text
Workflow State Matrix
Workflow Transition Matrix
Workflow Payload Examples
Workflow Test Fixtures
Human Review Checkpoint Table
AI Output Contract
```

---

# 8. Workflow Step Contract

Every workflow step must define:

```yaml
step_key: string
step_title_safe: string
step_type: string
step_required: boolean
owning_service: string
target_object_type: string | null
target_object_reference_id: string | null
input_contract_refs:
  - string
output_contract_refs:
  - string
permission_keys:
  - string
policy_scopes:
  - string
human_review_required: boolean
ai_assistance_allowed: boolean
events_expected:
  - string
failure_behavior: string
```

Rules:

```text
- step_key must be stable and unique within the workflow.
- step_type must use controlled values from Workflow Contract API Contract where applicable.
- owning_service must be explicit.
- No step may mutate a domain object outside its owning service.
- No step may create active tasks except through Task Service.
- No step may emit events directly from the workflow file.
```

---

# 9. Workflow Trigger Context

Workflow triggers must identify:

```yaml
trigger_type: string
trigger_source: string
triggered_by_actor_reference_id: string | null
triggered_by_agent_reference_id: string | null
triggered_by_event_reference_id: string | null
correlation_id: string | null
idempotency_key: string | null
```

Allowed trigger types:

```text
Manual
APIRequest
EventDriven
SystemScheduled
WorkflowContinuation
AgentPrepared
ImportedRecord
Unknown
```

Rules:

```text
- Triggering a workflow is not permission approval.
- Event-driven workflow must validate source event visibility and relevance.
- Agent-prepared workflow must still pass Permission and Policy checks.
- Scheduled workflow must still evaluate current Policy before action.
```

---

# 10. Target Object Context

Target object context must define what the workflow applies to.

Canonical shape:

```yaml
target_context:
  target_object_type: string
  target_object_reference_id: string
  target_object_status_at_start: string | null
  target_object_owner_service: string
  target_object_visibility: string | null
```

Rules:

```text
- Target reference must be validated by owning service.
- Workflow applicability must be evaluated before task creation.
- Policy may block or downgrade workflow output.
- Target status may change during workflow; workflow must revalidate before protected transitions.
```

---

# 11. Task Creation Rules

Workflow Contracts may define task plans.

They must not create tasks directly.

Task creation rules:

```text
- Task plans are proposals until Task Service creates active Tasks.
- Active Task creation must route through Task Service.
- TaskCreated events may only be emitted by Task Service.
- Workflow preview must never create active Tasks.
- Workflow application may request task creation through Task Service.
- Duplicate workflow application must not duplicate Tasks.
```

Canonical task plan shape:

```yaml
task_plan:
  proposed_tasks:
    - task_type: string
      task_title_safe: string
      target_object_type: string
      target_object_reference_id: string
      assignee_user_reference_id: string | null
      due_date: date | null
      source_step_key: string
      human_review_required: boolean
```

---

# 12. Event Rules

Workflow Contracts may reference Events, but must not emit them directly.

Rules:

```text
- Events are emitted by owning services.
- WorkflowContractApplied may be emitted by Workflow Contract Service.
- TaskCreated may be emitted by Task Service.
- CommunicationCreated may be emitted by Communication Service.
- RoutingEvaluated and RoutingSelected may be emitted by Routing Service.
- Event references are audit trace, not commands.
- Idempotent replay must not duplicate Events.
```

Event trace shape:

```yaml
audit_context:
  correlation_id: string | null
  causation_event_reference_id: string | null
  event_reference_ids:
    - string
```

---

# 13. Permission Rules

Every Workflow Contract must declare required permission keys.

Common keys:

```text
workflow-contract:preview
workflow-contract:apply
task:create
task:assign
task:status:transition
communication:draft:prepare
communication:review
communication:approve
routing:evaluate
routing:select
matter:update
order:update
document:read
evidence:read
```

Rules:

```text
- Permission Service evaluates permission.
- Workflow Contract must not grant permission.
- Each protected step must define required permission keys.
- PermissionDenied must stop or downgrade workflow behavior.
```

---

# 14. Policy Rules

Every Workflow Contract must declare required policy scopes.

Common scopes:

```text
workflow-contract:preview:policy
workflow-contract:apply:policy
task:create:policy
task:status:transition:policy
communication:draft:prepare:policy
communication:approve:policy
routing:evaluate:policy
routing:select:policy
matter:update:policy
order:update:policy
document:visibility:policy
evidence:visibility:policy
cross-organization:workflow
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may block, redact, downgrade or require human review.
- Workflow output must disclose policy omissions where applicable.
- PolicyRestricted must stop protected action or return safe partial output.
```

---

# 15. AI Assistance Rules

AI may assist workflows only inside governed boundaries.

Allowed AI roles:

```text
summarize context
prepare task plan
prepare communication draft
prepare routing comparison
prepare evidence summary
prepare checklist
identify missing context
explain visible event trace
```

AI must not:

```text
apply workflow by itself
create active tasks by itself
complete tasks
approve communications
send communications
select service providers
approve payments
submit filings
decide legal/professional truth
bypass Permission or Policy
```

AI output must include:

```yaml
ai_output_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
```

---

# 16. Human Review Rules

Human review must be required when workflow output may affect:

```text
professional conclusions
customer-facing communication
external communication
provider selection
payment-impacting decisions
filing/submission decisions
task completion
matter/order status closure
legal-risk decisions
```

Rules:

```text
- Human Review records accountable professional review.
- Human Review does not execute downstream action by itself.
- Owning services decide whether review satisfies action requirements.
- Workflow Contract must explicitly declare review checkpoints.
```

Review checkpoint shape:

```yaml
human_review_checkpoint:
  checkpoint_key: string
  checkpoint_title_safe: string
  required: boolean
  required_before_step_key: string | null
  reviewer_role: string | null
  review_output_contract_ref: string | null
```

---

# 17. Idempotency Rules

Workflow Contracts must define idempotency for:

```text
workflow application
task creation
routing evaluation
routing selection
communication creation
status transition
```

Rules:

```text
- Preview operations normally do not require idempotency unless persisted.
- Apply operations require idempotency_key.
- Duplicate apply must not duplicate tasks, events, communications or selections.
- Owning services define semantic equality.
```

---

# 18. Error Rules

Workflow Contract errors must follow Error Contract.

Common errors:

```text
WorkflowReferenceInvalid
WorkflowNotApplicable
WorkflowPreviewUnavailable
WorkflowApplyConflict
TargetReferenceInvalid
TaskCreationFailed
PermissionDenied
PolicyRestricted
HumanReviewRequired
StateInvalid
IdempotencyKeyRequired
IdempotencyConflict
VersionUnsupported
InternalError
```

Rules:

```text
- Errors must be safe.
- Errors must not expose restricted target data, private workflow notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 19. Versioning Rules

Every Workflow Contract must include:

```yaml
workflow_contract_version: v0.1.0
contract_version: v0.1.0
schema_version: v0.1.0
```

Rules:

```text
- Breaking changes require version bump.
- Workflow application must record workflow_contract_version used.
- Historical workflow applications must remain traceable.
- Deprecated workflow versions must not be silently rewritten.
```

---

# 20. Initial Workflow Contract Index

Recommended initial workflow contracts:

```text
core-specs/contracts/workflows/customer-intake-workflow-contract.md
core-specs/contracts/workflows/trademark-application-workflow-contract.md
core-specs/contracts/workflows/office-action-response-workflow-contract.md
core-specs/contracts/workflows/renewal-workflow-contract.md
core-specs/contracts/workflows/assignment-workflow-contract.md
core-specs/contracts/workflows/evidence-review-workflow-contract.md
core-specs/contracts/workflows/provider-routing-workflow-contract.md
core-specs/contracts/workflows/communication-review-workflow-contract.md
```

MVP priority:

```text
Must Implement:
  customer-intake-workflow-contract.md
  trademark-application-workflow-contract.md
  office-action-response-workflow-contract.md
  provider-routing-workflow-contract.md
  communication-review-workflow-contract.md

Should Implement:
  renewal-workflow-contract.md
  assignment-workflow-contract.md
  evidence-review-workflow-contract.md
```

---

# 21. Cross-Contract Dependency Matrix

```text
Workflow Contract
  depends on Workflow Contract API Contract
  depends on Workflow Contract Service
  depends on Task API Contract
  depends on Task Service
  depends on Event API Contract
  depends on Event Service
  depends on Permission Context
  depends on Policy Context
  depends on Human Review
  depends on AI Context
  depends on Idempotency
  depends on Versioning
```

Domain-specific dependencies:

```text
Customer Intake
  Customer
  Opportunity
  Matter
  Document
  Communication

Trademark Application
  Trademark
  Brand
  Jurisdiction
  Classification
  Document
  Evidence
  Matter
  Order

Office Action Response
  Trademark
  Document
  Evidence
  Matter
  Communication
  Task

Provider Routing
  Service Provider
  Service Network
  Partner
  Routing
  Communication

Communication Review
  Communication
  Document
  Task
  Human Review
```

---

# 22. Codex Implementation Notes

Codex must:

```text
read this README before generating workflow contract files
use Workflow Contract API Contract as payload boundary
use Workflow Contract Service as behavior owner
use Task Service for active task creation
use Event Service for trace retrieval
use Permission Context Contract before protected steps
use Policy Context Contract before policy-controlled steps
use AI Context Contract for AI-assisted steps
use Human Review Contract for review checkpoints
use Idempotency Contract for apply operations
use Versioning Contract for workflow versioning
cite all related object, service, API, event and agent specs
write workflow tests for preview vs apply distinction
write workflow tests that preview creates no active tasks
write workflow tests that apply is idempotent
write workflow tests that AI cannot execute protected actions
write workflow tests that human review gates protected transitions
write workflow tests that PolicyRestricted downgrades or blocks safely
```

Codex must not:

```text
treat workflow contract as implementation code
create tasks outside Task Service
emit events directly from workflow code
mutate target object outside owning service
skip Permission or Policy checks
allow AI to apply workflow, complete tasks, send communications or select providers
hide human-review requirements
overwrite historical workflow versions silently
```

---

# 23. Acceptance Criteria

This README is accepted only if:

```text
[ ] It defines Workflow Contract purpose.
[ ] It defines Core Lock.
[ ] It defines what Workflow Contracts are.
[ ] It defines what Workflow Contracts are not.
[ ] It defines architectural position.
[ ] It defines file naming rules.
[ ] It defines required sections.
[ ] It defines workflow step contract.
[ ] It defines trigger context.
[ ] It defines target object context.
[ ] It defines task creation rules.
[ ] It defines event rules.
[ ] It defines permission rules.
[ ] It defines policy rules.
[ ] It defines AI assistance rules.
[ ] It defines human review rules.
[ ] It defines idempotency rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines initial workflow index.
[ ] It defines dependency matrix.
[ ] It defines Codex implementation notes.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Workflow Contracts README. Defines workflow contract purpose, boundary, naming, required sections, trigger/target/step shape, task/event rules, permission/policy/AI/human review rules, idempotency, error handling, versioning, initial workflow index and Codex implementation expectations. |

---

**End of Workflow Contracts README**


## PUB-TASK-B02-002 Component Governance Reference

Workflow state models must consume `core-specs/workflows/components/workflow-state-definition.md`. Transition rules must consume `core-specs/workflows/components/workflow-transition-definition.md`. Free-text transitions cannot bypass terminal, guard, review, approval, event or failure semantics. Workflow Contracts do not own domain mutation and do not authorize protected external action.
