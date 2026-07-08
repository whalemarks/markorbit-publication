# Agent Specification — Workflow Agent

**Spec ID:** B02-AGENT-WORKFLOW  
**Spec Type:** Specialized Agent Specification  
**Agent Spec Name:** Workflow Agent  
**Agent Spec File:** core-specs/agents/workflow-agent.md  
**Registry Key:** workflow-agent  
**Related Agent Governance:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Related Core Domains:** Workflow Contract; Task; Agent; Permission; Policy; Event; Matter; Order; Knowledge; Communication; Notification  
**Related Object Specs:** core-specs/objects/workflow-contract.md; core-specs/objects/task.md; core-specs/objects/agent.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/knowledge.md; core-specs/objects/communication.md; core-specs/objects/notification.md  
**Related Service Specs:** core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md; core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/knowledge-service.md; core-specs/services/communication-service.md; core-specs/services/notification-service.md  
**Related API Specs:** core-specs/api/workflow-contract-api.md; core-specs/api/task-api.md; core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/knowledge-api.md; core-specs/api/communication-api.md; core-specs/api/notification-api.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/notification-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Workflow Agent defines the governed AI Agent pattern for assisting Workflow Contract review, workflow application preview, task-plan preparation, gap detection, trace explanation and workflow-to-task preparation in MarkOrbit Core.

It exists to help professionals and systems understand and prepare workflow execution without allowing AI to become workflow runtime authority, silent task creator, professional approver, deadline owner, filing submitter, communication sender or uncontrolled domain-state mutator.

Workflow Agent supports:

```text
workflow contract summary
workflow application preview
workflow step explanation
workflow gap detection
task-plan preparation
workflow-to-task draft preparation
workflow trace explanation
workflow readiness review
missing input checklist
safe workflow recommendation
```

Workflow Agent does not apply workflows, create active tasks, complete workflow steps, approve professional output or mutate Matter/Order state outside governed services.

---

# 2. Agent Meaning

Workflow Agent means:

```text
a governed AI Agent that assists with Workflow Contract interpretation and workflow-action preparation through Workflow Contract Service boundaries.
```

Workflow Agent does not mean:

```text
workflow runtime engine
task execution engine
professional reviewer
legal decision maker
filing submitter
communication sender
deadline authority
order state authority
matter state authority
permission grantor
policy bypasser
```

Workflow Agent may help answer:

```text
What workflow contract applies?
What tasks may be prepared?
What workflow inputs are missing?
What step should be reviewed next?
What trace explains this workflow state?
What human review is required?
```

Workflow Agent must not claim:

```text
The workflow has been applied unless Workflow Contract Service records it.
The tasks have been created unless Task Service records them.
The workflow is complete.
The professional output is approved.
The filing has been submitted.
```

---

# 3. Registry Position

Registry entry:

```text
workflow-agent
```

Required registry constraints:

```text
agent_type: WorkflowAgent
agent_role: WorkflowSupportAssistant
default_data_access_scope: SafeSummaryOnly
default_execution_mode: PrepareOnly
```

Allowed capabilities:

```text
Read
Summarize
Suggest
PrepareWorkflow
PrepareTask
ValidateReference
ExplainTrace
```

Restricted capabilities:

```text
ApplyWorkflow
CreateObject
UpdateObject
CompleteTask
SendCommunication
AccessRestrictedContent
```

Registry rule:

```text
Workflow Agent may be considered for workflow interpretation, preview and preparation.
Permission and Policy decide whether it may prepare or request specific workflow operations in context.
```

---

# 4. Agent Boundary

Workflow Agent is responsible for:

```text
workflow contract query preparation
workflow contract reference validation request
safe workflow contract summary
workflow application preview preparation
workflow gap detection
workflow readiness checklist preparation
task-plan draft preparation
workflow trace explanation
workflow-to-task preparation
workflow-related notification/communication draft context
```

Workflow Agent is not responsible for:

```text
Workflow Contract lifecycle ownership
Workflow Contract application without Workflow Contract Service
active Task creation without Task Service
Task completion
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

Workflow Agent must obey:

```text
Workflow Agent may read, summarize, suggest and prepare only within Permission and Policy limits.
Workflow Agent output is workflow-preparation assistance, not workflow execution.
Workflow Agent must not silently apply Workflow Contracts, create active Tasks, complete Tasks or close workflow states.
Workflow Agent must not treat AI-prepared workflow plan as professional approval.
Workflow Agent must route workflow application through Workflow Contract Service and task creation through Task Service.
```

This lock applies to all Workflow Agent implementations.

---

# 6. Agent Identity Requirements

Every Workflow Agent operation must include:

```yaml
agent_reference_id: string
agent_registry_key: workflow-agent
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
- Agent Contract is required for protected workflow actions.
- Suspended, revoked, archived or unknown agents must not perform Workflow operations.
- Agent must not borrow human User identity.
```

---

# 7. Capability Rules

Allowed operations:

```text
summarizeWorkflowContract
searchWorkflowContractsSafely
validateWorkflowContractReference
prepareWorkflowApplicationPreview
identifyWorkflowGaps
prepareWorkflowTaskPlan
prepareWorkflowReadinessChecklist
prepareWorkflowNotificationDraft
prepareWorkflowCommunicationDraft
explainWorkflowTrace
```

Disallowed operations:

```text
applyWorkflowSilently
createActiveTasksSilently
completeWorkflowSilently
completeTaskSilently
approveWorkflowOutput
closeMatter
completeOrder
sendCommunication
deliverNotification
submitFiling
```

Capability rule:

```text
Workflow Agent may prepare workflow context and plans; Workflow Contract Service owns workflow application and Task Service owns Task creation/state.
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
- Workflow internal rules may be summarized safely but restricted execution logic may require policy.
- Matter strategy, customer instructions, document content and evidence content require separate policy.
- Prompt/context construction must use evaluated access scope.
```

Disallowed default fields:

```text
privileged workflow notes
customer private instructions
unredacted document content
raw evidence packages
payment data
provider pricing
internal scoring or routing logic
filing credentials
restricted automation rules
```

---

# 9. Permission Rules

Required permissions may include:

```text
agent:workflow:prepare
workflow-contract:read
workflow-contract:search
workflow-contract:validate
workflow-contract:apply
workflow-contract:preview
task:create
task:read
matter:read
order:read
event:read
communication:draft:prepare
notification:create
knowledge:read
```

Rules:

```text
- Agent-level permission is required.
- Workflow Contract-domain permission is required.
- Related Task/Matter/Order/Event permission is required where those records are referenced.
- Applying workflow requires explicit permission and policy.
- Permission must be evaluated against actor, agent, organization, target context and intended use.
- PermissionDenied stops the operation.
```

---

# 10. Policy Rules

Required policies may include:

```text
AIAgentWorkflowPolicy
WorkflowContractVisibilityPolicy
WorkflowContractReferencePolicy
WorkflowApplicationPolicy
WorkflowPreviewPolicy
WorkflowTaskCreationPolicy
TaskCreationPolicy
RestrictedWorkflowDataPolicy
CrossOrganizationWorkflowPolicy
AIAgentHumanReviewPolicy
```

Rules:

```text
- Policy controls whether Workflow Agent may preview or prepare workflow application.
- Policy may require human review before workflow application or active task creation.
- Policy may restrict workflow details, internal execution logic, matter strategy and customer instructions.
- Policy may restrict cross-organization or cross-matter workflow access.
- PolicyRestricted stops or downgrades the operation.
```

---

# 11. Request Patterns

## 11.1 Workflow Application Preview Request

```yaml
operation: prepareWorkflowApplicationPreview
agent_reference_id: string
agent_registry_key: workflow-agent
actor_reference_id: string | null
organization_reference_id: string | null
workflow_contract_reference_id: string
workflow_application_purpose: string
target_context:
  matter_reference_id: string | null
  order_reference_id: string | null
  task_reference_id: string | null
input_context:
  known_inputs: list[object]
  known_task_reference_ids: list[string]
data_access_requested: string
correlation_id: string | null
```

## 11.2 Workflow Gap Review Request

```yaml
operation: identifyWorkflowGaps
agent_reference_id: string
workflow_contract_reference_id: string
target_context:
  matter_reference_id: string | null
  order_reference_id: string | null
known_task_reference_ids: list[string]
gap_purpose: string
correlation_id: string | null
```

## 11.3 Workflow Task Plan Request

```yaml
operation: prepareWorkflowTaskPlan
agent_reference_id: string
workflow_contract_reference_id: string
task_plan_purpose: string
target_context:
  matter_reference_id: string | null
  order_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

## 11.4 Workflow Trace Explanation Request

```yaml
operation: explainWorkflowTrace
agent_reference_id: string
workflow_application_reference_id: string | null
workflow_contract_reference_id: string | null
event_reference_ids: list[string]
explanation_purpose: string
correlation_id: string | null
```

---

# 12. Response Patterns

## 12.1 Workflow Application Preview Response

```yaml
agent_reference_id: string
workflow_preview_reference_id: string | null
workflow_contract_reference_id: string
preparation_status: string
safe_preview:
  applicable: boolean
  application_summary: string | null
  expected_task_count: integer | null
  expected_task_types: list[string]
  blocked_items: list[string]
  missing_inputs: list[string]
source_scope: string
policy_omissions: list[string]
human_review_required: boolean
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.2 Workflow Gap Response

```yaml
agent_reference_id: string
gap_review_reference_id: string | null
safe_gap_summary:
  missing_workflow_inputs: list[string]
  missing_task_types: list[string]
  blocked_step_reasons: list[string]
  suggested_next_steps: list[string]
source_task_reference_ids: list[string]
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.3 Workflow Task Plan Response

```yaml
agent_reference_id: string
task_plan_reference_id: string | null
workflow_contract_reference_id: string
safe_task_plan:
  task_plan_summary: string | null
  task_drafts:
    - task_type: string
      title: string
      safe_summary: string | null
      required_inputs: list[string]
      suggested_sequence: integer | null
preparation_status: string
human_review_required: boolean
restricted_fields_omitted: boolean
downstream_service_required: string | null
correlation_id: string | null
```

## 12.4 Workflow Trace Explanation Response

```yaml
agent_reference_id: string
trace_explanation_reference_id: string | null
safe_explanation: string
source_event_reference_ids: list[string]
missing_context: list[string]
policy_omissions: list[string]
confidence_level: string
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

Response rules:

```text
- Responses must mark AI-generated output.
- Responses must not imply Workflow application or Task creation.
- Responses must disclose missing context and policy omissions.
- Responses must not expose restricted fields by default.
- Responses must identify required downstream service.
```

---

# 13. Controlled Values

## 13.1 workflow_application_purpose

```text
MatterWorkflowPreview
OrderWorkflowPreview
TaskPlanPreparation
WorkflowReadinessReview
QualityCheck
AIAssistedWorkflow
Unknown
```

## 13.2 gap_purpose

```text
WorkflowCoverage
MatterReadiness
OrderReadiness
TaskReadiness
DeadlineReview
QualityReview
AIAssistedReview
Unknown
```

## 13.3 task_plan_purpose

```text
InitialTaskPlan
WorkflowTaskBreakdown
TaskGenerationPreview
OperationalChecklist
HumanReviewPreparation
AIAssistedTaskPlan
Unknown
```

## 13.4 explanation_purpose

```text
InternalReview
AuditReview
UserSupport
WorkflowDebugging
ProfessionalReview
AIAssistedExplanation
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

## 13.6 source_scope

```text
WorkflowContractOnly
WorkflowApplication
MatterContext
OrderContext
TaskContext
EventTrace
PolicyFilteredContext
Unknown
```

## 13.7 confidence_level

```text
Low
Medium
High
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

Human review is required when Workflow Agent output may be used for:

```text
workflow application
active task creation
task assignment
task completion
professional work output
official filing preparation
external communication
customer instruction handling
payment or order impact
evidence sufficiency
document finalization
cross-organization disclosure
restricted workflow logic use
```

Human review is not required for:

```text
safe internal workflow summary
safe metadata lookup
non-state-changing preview
gap checklist preparation where no restricted content is exposed
trace explanation from visible events
```

Rules:

```text
- Human review requirement must be included in output.
- Human review must be explicit before workflow application where required.
- Human review reference must be passed to Workflow Contract Service or Task Service where required.
```

---

# 15. Event and Audit Rules

Workflow Agent operations must be traceable.

Trace must include:

```yaml
agent_registry_key: workflow-agent
agent_reference_id: string
operation: string
workflow_contract_reference_id: string | null
workflow_application_reference_id: string | null
matter_reference_id: string | null
order_reference_id: string | null
task_reference_ids: list[string]
event_reference_ids: list[string]
data_access_scope: string
execution_mode: string
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Workflow Agent must not emit domain events directly.
- Event Service owns event recording.
- WorkflowContractApplied must only be emitted after Workflow Contract Service applies workflow.
- TaskCreated must only be emitted after Task Service creates Tasks.
- Workflow trace must distinguish AI preview from actual application.
```

---

# 16. Relationship to Workflow Contract Service

Workflow Agent must use Workflow Contract Service for:

```text
getWorkflowContract
searchWorkflowContracts
validateWorkflowContractReference
previewWorkflowApplication
applyWorkflowContract
explainWorkflowApplication
```

Rules:

```text
- Workflow Agent must not query or mutate workflow contract store directly.
- Workflow Contract Service applies Workflow Contract domain rules.
- Permission and Policy are evaluated before protected Workflow operations.
- Workflow Agent may transform safe results into previews, task plans or explanations.
```

---

# 17. Relationship to Task Service

Workflow Agent may prepare downstream task drafts.

Allowed:

```text
prepare workflow task plan
prepare missing task checklist
prepare task draft context
prepare sequencing suggestion
```

Rules:

```text
- Task creation must route through Task Service.
- Task assignment must route through Task Service.
- Task completion must route through Task Service.
- Workflow Agent output must not be treated as active Task or completed Task.
```

---

# 18. Relationship to Knowledge, Communication and Notification Services

Workflow Agent may use related services only through governed access.

Rules:

```text
- Knowledge Service owns Knowledge access.
- Communication Service owns Communication creation.
- Notification Service owns Notification creation.
- Workflow Agent may prepare context, but downstream services own action.
- Workflow Agent must not send messages or notifications directly.
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
WorkflowReferenceInvalid
WorkflowApplicationInvalid
TaskReferenceInvalid
MatterReferenceInvalid
OrderReferenceInvalid
TargetContextInvalid
CrossOrganizationRestricted
DownstreamServiceRequired
```

Rules:

```text
- Rejections must be safe to display.
- Rejections must not reveal hidden Workflow logic.
- Rejections must not expose policy internals.
- Rejections may recommend the next governed step.
```

---

# 20. Codex Implementation Notes

Codex must:

```text
cite AI Agent Governance
cite Agent Registry
cite this Workflow Agent spec
cite Workflow Contract Service Specification
cite Workflow Contract Object Specification
cite Workflow Contract API Specification
cite Task Service Specification where task drafts are prepared
cite Permission and Policy specs
validate agent_registry_key = workflow-agent
validate agent status
validate capability eligibility
invoke Permission Service before protected workflow access
invoke Policy Service before workflow context access
use SafeSummaryOnly by default
mark AI-generated workflow previews and task plans
preserve workflow/matter/order/task/event references in output
disclose missing context and policy omissions
route workflow application through Workflow Contract Service
route Task creation/assignment/completion through Task Service
route Notification preparation through Notification Service
route Communication preparation through Communication Service
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for AgentContractRequired
write tests for HumanReviewRequired
write tests for restricted data omission
write tests for invalid Workflow Contract reference
write tests that Workflow Agent cannot apply workflows directly
write tests that Workflow Agent cannot silently create active Tasks
write tests that Workflow Agent cannot complete Tasks or send Communications
```

Codex must not:

```text
query Workflow database directly
bypass Workflow Contract Service
bypass Task Service
bypass Permission or Policy
pass unrestricted workflow/matter/order context into prompts
treat AI preview as applied Workflow
treat AI task plan as created Tasks
approve professional workflow output
create communications or notifications directly
emit domain events directly
```

---

# 21. Acceptance Criteria

This Workflow Agent Specification is accepted only if:

```text
[ ] It defines Workflow Agent purpose.
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
[ ] It defines relationship to Workflow Contract Service.
[ ] It defines relationship to Task Service.
[ ] It defines relationship to Knowledge, Communication and Notification Services.
[ ] It defines error and rejection rules.
[ ] It defines Codex implementation notes.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Workflow Agent specification. Defines governed workflow preview, workflow gap detection, task-plan preparation and trace explanation rules under AI Agent Governance and Agent Registry. |

---

**End of Agent Specification**
