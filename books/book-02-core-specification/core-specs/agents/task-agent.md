# Agent Specification — Task Agent

**Spec ID:** B02-AGENT-TASK  
**Spec Type:** Specialized Agent Specification  
**Agent Spec Name:** Task Agent  
**Agent Spec File:** core-specs/agents/task-agent.md  
**Registry Key:** task-agent  
**Related Agent Governance:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Related Core Domains:** Task; Agent; Permission; Policy; Event; Workflow Contract; Matter; Order; Communication; Notification; Knowledge  
**Related Object Specs:** core-specs/objects/task.md; core-specs/objects/agent.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md; core-specs/objects/workflow-contract.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/communication.md; core-specs/objects/notification.md; core-specs/objects/knowledge.md  
**Related Service Specs:** core-specs/services/task-service.md; core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/communication-service.md; core-specs/services/notification-service.md; core-specs/services/knowledge-service.md  
**Related API Specs:** core-specs/api/task-api.md; core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/communication-api.md; core-specs/api/notification-api.md; core-specs/api/knowledge-api.md  
**Related Event Specs:** core-specs/events/task-created.md; core-specs/events/workflow-contract-applied.md; core-specs/events/communication-created.md; core-specs/events/notification-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Task Agent defines the governed AI Agent pattern for assisting Task planning, task-context review, task draft preparation, assignment suggestions, checklist preparation and completion-draft support in MarkOrbit Core.

It exists to help professionals and systems organize work without allowing AI to become task owner, workflow executor, professional approver, filing submitter, communication sender, customer-instruction approver or silent domain-state mutator.

Task Agent supports:

```text
task summary assistance
task gap detection
task checklist preparation
task draft preparation
task assignment suggestion
task next-step suggestion
task completion draft preparation
workflow-derived task plan review
task-to-communication draft preparation
task-to-notification preparation
event trace review
```

Task Agent does not complete professional work, approve legal conclusions, send communications, file applications, mutate Matter/Order state or execute tasks outside Task Service.

---

# 2. Agent Meaning

Task Agent means:

```text
a governed AI Agent that assists with Task planning and task-action preparation through Task Service boundaries.
```

Task Agent does not mean:

```text
task executor
workflow runtime
professional reviewer
legal decision maker
filing submitter
communication sender
notification delivery engine
order assignee authority
matter owner
permission grantor
policy bypasser
```

Task Agent may help answer:

```text
What tasks are missing?
What task should be prepared next?
What inputs are required before this task can proceed?
Who might be an appropriate assignee candidate?
What should a completion draft include?
What related events or workflow steps explain this task?
```

Task Agent must not claim:

```text
The task is completed unless Task Service records completion.
The professional output is approved.
The filing has been submitted.
The customer instruction is accepted.
The communication has been sent.
The workflow is finished.
```

---

# 3. Registry Position

Registry entry:

```text
task-agent
```

Required registry constraints:

```text
agent_type: TaskAgent
agent_role: TaskPlanningAssistant
default_data_access_scope: SafeSummaryOnly
default_execution_mode: PrepareOnly
```

Allowed capabilities:

```text
Read
Summarize
Suggest
PrepareTask
ValidateReference
ExplainTrace
```

Restricted capabilities:

```text
CreateObject
UpdateObject
CompleteTask
SendCommunication
ApplyWorkflow
AccessRestrictedContent
```

Registry rule:

```text
Task Agent may be considered for task planning and task-action preparation.
Permission and Policy decide whether it may prepare, suggest or request specific Task operations in context.
```

---

# 4. Agent Boundary

Task Agent is responsible for:

```text
task query preparation
task reference validation request
safe task summary generation
missing input detection
task checklist preparation
task draft preparation
assignment suggestion preparation
next-step suggestion preparation
completion draft preparation
workflow-derived task plan review
task event trace explanation
```

Task Agent is not responsible for:

```text
Task object lifecycle ownership
Task creation without Task Service
Task assignment without Task Service
Task start/complete state transition without Task Service
workflow application
Matter or Order lifecycle ownership
Communication creation or delivery
Notification delivery
professional approval
official filing
permission grant
policy evaluation
```

---

# 5. Governance Lock

Task Agent must obey:

```text
Task Agent may read, summarize, suggest and prepare only within Permission and Policy limits.
Task Agent output is task-planning assistance, not task execution.
Task Agent must not silently create, assign, start, complete or close Tasks.
Task Agent must not treat AI-prepared completion draft as professional approval.
Task Agent must route downstream Task actions through Task Service.
```

This lock applies to all Task Agent implementations.

---

# 6. Agent Identity Requirements

Every Task Agent operation must include:

```yaml
agent_reference_id: string
agent_registry_key: task-agent
agent_contract_reference_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
target_context:
  target_object_type: string | null
  target_object_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Agent identity must be validated through Agent Service.
- Agent status must be Active or explicitly allowed.
- Agent Contract is required for protected task actions.
- Suspended, revoked, archived or unknown agents must not perform Task operations.
- Agent must not borrow human User identity.
```

---

# 7. Capability Rules

Allowed operations:

```text
summarizeTask
searchTasksSafely
validateTaskReference
identifyTaskGaps
prepareTaskDraft
prepareAssignmentSuggestion
prepareNextStepSuggestion
prepareCompletionDraft
prepareTaskNotificationDraft
prepareTaskCommunicationDraft
explainTaskTrace
```

Disallowed operations:

```text
createActiveTaskSilently
assignTaskSilently
startTaskSilently
completeTaskSilently
approveTaskOutput
closeMatter
completeOrder
applyWorkflow
sendCommunication
deliverNotification
submitFiling
```

Capability rule:

```text
Task Agent may prepare action context; Task Service owns Task creation, assignment and state transition.
```

---

# 8. Data Access Rules

Default data access:

```text
SafeSummaryOnly
```

Allowed data access scopes:

```text
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
```

Restricted data access scopes:

```text
RestrictedContentWithHumanApproval
AccessRawDocument
AccessEvidence
AccessPricing
AccessPrivateContact
AccessFinancialData
```

Rules:

```text
- SafeSummaryOnly is the default.
- Policy may downgrade access to MetadataOnly or NoAccess.
- Task internal notes are restricted by default.
- Matter strategy, customer instructions, document content and evidence content require separate policy.
- Prompt/context construction must use evaluated access scope.
```

Disallowed default fields:

```text
privileged task notes
customer private instructions
unredacted document content
raw evidence packages
payment data
private contact details
provider pricing
internal scoring or routing logic
filing credentials
```

---

# 9. Permission Rules

Required permissions may include:

```text
agent:task:prepare-action
task:read
task:search
task:validate
task:create
task:update
task:assign
task:start
task:complete
task:notification:prepare
task:communication:prepare
workflow-contract:read
matter:read
order:read
event:read
```

Rules:

```text
- Agent-level permission is required.
- Task-domain permission is required.
- Related Matter/Order/Workflow/Event permission is required where those records are referenced.
- State-changing Task operations require explicit permission.
- Permission must be evaluated against actor, agent, organization, target context and intended use.
- PermissionDenied stops the operation.
```

---

# 10. Policy Rules

Required policies may include:

```text
AIAgentTaskActionPolicy
TaskVisibilityPolicy
TaskReferencePolicy
TaskCreationPolicy
TaskAssignmentPolicy
TaskStateTransitionPolicy
TaskCompletionPolicy
TaskNotificationPolicy
TaskCommunicationPolicy
RestrictedTaskDataPolicy
CrossOrganizationTaskPolicy
AIAgentHumanReviewPolicy
```

Rules:

```text
- Policy controls whether Task Agent may prepare or request Task actions.
- Policy may require human review before task creation, assignment or completion.
- Policy may restrict task details, internal notes, matter strategy and customer instructions.
- Policy may restrict cross-organization or cross-matter task access.
- PolicyRestricted stops or downgrades the operation.
```

---

# 11. Request Patterns

## 11.1 Task Planning Request

```yaml
operation: prepareTaskDraft
agent_reference_id: string
agent_registry_key: task-agent
actor_reference_id: string | null
organization_reference_id: string | null
task_planning_purpose: string
target_context:
  matter_reference_id: string | null
  order_reference_id: string | null
  workflow_contract_reference_id: string | null
  workflow_application_reference_id: string | null
candidate_task_context:
  task_type: string | null
  title: string | null
  safe_summary: string | null
data_access_requested: string
correlation_id: string | null
```

## 11.2 Task Gap Review Request

```yaml
operation: identifyTaskGaps
agent_reference_id: string
target_context:
  matter_reference_id: string | null
  order_reference_id: string | null
  workflow_contract_reference_id: string | null
known_task_reference_ids: list[string]
gap_purpose: string
correlation_id: string | null
```

## 11.3 Assignment Suggestion Request

```yaml
operation: prepareAssignmentSuggestion
agent_reference_id: string
task_reference_id: string
assignment_purpose: string
candidate_assignee_scope:
  assignee_type: string | null
  queue_reference_id: string | null
  role_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

## 11.4 Completion Draft Request

```yaml
operation: prepareCompletionDraft
agent_reference_id: string
task_reference_id: string
completion_purpose: string
input_references:
  document_reference_ids: list[string]
  evidence_reference_ids: list[string]
  communication_reference_ids: list[string]
human_review_reference_id: string | null
correlation_id: string | null
```

---

# 12. Response Patterns

## 12.1 Task Draft Response

```yaml
agent_reference_id: string
task_draft_reference_id: string | null
preparation_status: string
safe_task_draft:
  task_type: string
  title: string
  safe_summary: string | null
  suggested_priority: string | null
  suggested_due_at: datetime | null
  required_inputs: list[string]
  blocked_items: list[string]
source_scope: string
missing_context: list[string]
policy_omissions: list[string]
human_review_required: boolean
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.2 Task Gap Response

```yaml
agent_reference_id: string
gap_review_reference_id: string | null
safe_gap_summary:
  missing_task_types: list[string]
  blocked_task_reasons: list[string]
  suggested_next_steps: list[string]
source_task_reference_ids: list[string]
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.3 Assignment Suggestion Response

```yaml
agent_reference_id: string
assignment_suggestion_reference_id: string | null
task_reference_id: string
safe_assignment_suggestion:
  assignee_type: string | null
  assignee_reference_id: string | null
  safe_reason: string | null
  confidence_level: string
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.4 Completion Draft Response

```yaml
agent_reference_id: string
completion_draft_reference_id: string | null
task_reference_id: string
safe_completion_draft:
  result_summary: string | null
  required_review_items: list[string]
  missing_inputs: list[string]
  warnings: list[string]
confidence_level: string
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

Response rules:

```text
- Responses must mark AI-generated output.
- Responses must not imply Task execution or completion.
- Responses must disclose missing context and policy omissions.
- Responses must not expose restricted fields by default.
- Responses must identify required downstream service.
```

---

# 13. Controlled Values

## 13.1 task_planning_purpose

```text
MatterPreparation
OrderPreparation
WorkflowPreparation
TaskBreakdown
QualityCheck
FollowUp
AIAssistedPlanning
Unknown
```

## 13.2 gap_purpose

```text
WorkflowCoverage
MatterReadiness
OrderReadiness
DeadlineReview
QualityReview
AIAssistedReview
Unknown
```

## 13.3 assignment_purpose

```text
InitialAssignment
Reassignment
Escalation
QueueBalancing
RoleBasedAssignment
AIAssistedSuggestion
Unknown
```

## 13.4 completion_purpose

```text
CompletionDraft
ReviewDraft
ResultSummary
QualityCheck
AIAssistedCompletionSupport
Unknown
```

## 13.5 preparation_status

```text
Prepared
Rejected
PolicyRestricted
PermissionDenied
HumanReviewRequired
DownstreamServiceRequired
Unknown
```

## 13.6 confidence_level

```text
Low
Medium
High
Unknown
```

## 13.7 source_scope

```text
TaskOnly
MatterContext
OrderContext
WorkflowContext
EventTrace
PolicyFilteredContext
Unknown
```

## 13.8 data_access_requested

```text
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContentWithHumanApproval
Unknown
```

---

# 14. Human Review Rules

Human review is required when Task Agent output may be used for:

```text
active task creation
task assignment with business consequence
task completion
professional work output
official filing preparation
external communication
customer instruction handling
payment or order impact
evidence sufficiency
document finalization
workflow application with active task creation
```

Human review is not required for:

```text
safe internal task summary
safe metadata lookup
non-state-changing gap checklist
reference validation where no restricted content is exposed
```

Rules:

```text
- Human review requirement must be included in output.
- Human review must be explicit where required.
- Human review reference must be passed to Task Service where required.
```

---

# 15. Event and Audit Rules

Task Agent operations must be traceable.

Trace must include:

```yaml
agent_registry_key: task-agent
agent_reference_id: string
operation: string
task_reference_id: string | null
matter_reference_id: string | null
order_reference_id: string | null
workflow_contract_reference_id: string | null
data_access_scope: string
execution_mode: string
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Task Agent must not emit domain events directly.
- Event Service owns event recording.
- TaskCreated must only be emitted after Task Service creates Task.
- Task completion trace must distinguish AI draft from actual completion.
```

---

# 16. Relationship to Task Service

Task Agent must use Task Service for:

```text
getTask
searchTasks
validateTaskReference
createTask
assignTask
startTask
completeTask
prepareTaskNotification
prepareTaskCommunication
```

Rules:

```text
- Task Agent must not query or mutate task store directly.
- Task Service applies Task domain rules.
- Permission and Policy are evaluated before protected Task operations.
- Task Agent may transform safe results into drafts or suggestions.
```

---

# 17. Relationship to Workflow Contract Service

Task Agent may use Workflow Contract context only through governed service access.

Rules:

```text
- Workflow Contract Service owns workflow application.
- Task Agent may review task plan coverage.
- Task Agent may suggest missing tasks.
- Task Agent must not apply workflow by itself.
- Task Agent must not create active tasks from workflow without Task Service and required review.
```

---

# 18. Relationship to Communication and Notification Services

Task Agent may prepare downstream drafts.

Allowed:

```text
prepare task notification draft
prepare task communication draft
prepare follow-up checklist
prepare reminder context
```

Rules:

```text
- Notification creation must route through Notification Service.
- Communication creation must route through Communication Service.
- Task Agent output must not be treated as sent communication or delivered notification.
```

---

# 19. Error and Rejection Rules

Controlled rejection reasons:

```text
PermissionDenied
PolicyRestricted
AgentSuspended
AgentRevoked
AgentContractRequired
CapabilityNotAllowed
HumanReviewRequired
RestrictedDataRequested
TaskReferenceInvalid
MatterReferenceInvalid
OrderReferenceInvalid
WorkflowReferenceInvalid
TargetContextInvalid
CrossOrganizationRestricted
DownstreamServiceRequired
```

Rules:

```text
- Rejections must be safe to display.
- Rejections must not reveal hidden Task data.
- Rejections must not expose policy internals.
- Rejections may recommend the next governed step.
```

---

# 20. Codex Implementation Notes

Codex must:

```text
cite AI Agent Governance
cite Agent Registry
cite this Task Agent spec
cite Task Service Specification
cite Task Object Specification
cite Task API Specification
cite Permission and Policy specs
validate agent_registry_key = task-agent
validate agent status
validate capability eligibility
invoke Permission Service before protected task access
invoke Policy Service before task context access
use SafeSummaryOnly by default
mark AI-generated task drafts and suggestions
preserve source task/matter/order/workflow references in output
disclose missing context and policy omissions
route Task creation/assignment/start/complete through Task Service
route Notification preparation through Notification Service
route Communication preparation through Communication Service
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for AgentContractRequired
write tests for HumanReviewRequired
write tests for restricted data omission
write tests for invalid Task reference
write tests that Task Agent cannot silently create active Tasks
write tests that Task Agent cannot complete Tasks directly
write tests that Task Agent cannot send Communication or Notification
```

Codex must not:

```text
query Task database directly
bypass Task Service
bypass Permission or Policy
pass unrestricted Task/Matter/Order context into prompts
treat AI task draft as created Task
treat AI completion draft as completed Task
approve professional output
create communications or notifications directly
emit domain events directly
```

---

# 21. Acceptance Criteria

This Task Agent Specification is accepted only if:

```text
[ ] It defines Task Agent purpose.
[ ] It defines Agent meaning.
[ ] It defines registry position.
[ ] It defines Agent boundary.
[ ] It defines governance lock.
[ ] It defines identity requirements.
[ ] It defines capability rules.
[ ] It defines data access rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines request patterns.
[ ] It defines response patterns.
[ ] It defines controlled values.
[ ] It defines human review rules.
[ ] It defines event and audit rules.
[ ] It defines relationship to Task Service.
[ ] It defines relationship to Workflow Contract Service.
[ ] It defines relationship to Communication and Notification Services.
[ ] It defines error and rejection rules.
[ ] It defines Codex implementation notes.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Task Agent specification. Defines governed Task planning, gap detection, assignment suggestion, completion draft and downstream preparation rules under AI Agent Governance and Agent Registry. |

---

**End of Agent Specification**
