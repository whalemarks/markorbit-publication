# Workflow Contract Template

**Spec ID:** B02-CONTRACT-WORKFLOW-TEMPLATE  
**Spec Type:** Workflow Contract Template  
**Contract File:** core-specs/contracts/workflows/template.md  
**Contract Category:** Workflow Contracts  
**Template Version:** v0.1.0  
**Contract Version:** v0.1.0  
**Status:** Draft  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 0. How to Use This Template

Use this template for every file under:

```text
core-specs/contracts/workflows/
```

Target file naming:

```text
core-specs/contracts/workflows/{workflow-name}-workflow-contract.md
```

This template must be copied and completed, not referenced as a final contract by itself.

Core rule:

```text
Workflow Contracts define governed execution patterns.
Workflow Contract Service owns workflow contract behavior.
Task Service owns active task creation.
Owning domain services own domain state.
Permission and Policy govern every workflow action.
AI may prepare, summarize and suggest, but must not execute protected actions.
Events preserve trace.
```

---

# 1. Metadata

```yaml
spec_id: B02-CONTRACT-WORKFLOW-{WORKFLOW-NAME}
spec_type: Workflow Contract Specification
contract_name: "{Workflow Name} Workflow Contract"
contract_file: "core-specs/contracts/workflows/{workflow-name}-workflow-contract.md"
contract_category: Workflow
related_workflow_contract_type: "{WorkflowContractType}"
related_domains:
  - "{DomainName}"
related_object_specs:
  - "core-specs/objects/{object}.md"
related_service_specs:
  - "core-specs/services/{service}-service.md"
related_api_specs:
  - "core-specs/api/{api}-api.md"
related_event_specs:
  - "core-specs/events/{event}.md"
related_agent_specs:
  - "core-specs/agents/{agent}.md"
related_common_contracts:
  - "core-specs/contracts/common/references.md"
  - "core-specs/contracts/common/errors.md"
  - "core-specs/contracts/common/pagination.md"
  - "core-specs/contracts/common/audit-context.md"
  - "core-specs/contracts/common/permission-context.md"
  - "core-specs/contracts/common/policy-context.md"
  - "core-specs/contracts/common/ai-context.md"
  - "core-specs/contracts/common/human-review.md"
  - "core-specs/contracts/common/idempotency.md"
  - "core-specs/contracts/common/versioning.md"
status: Draft
version: 0.1.0
contract_version: v0.1.0
workflow_contract_version: v0.1.0
mvp_phase: "{Phase}"
mvp_depth: "{Must Implement | Should Implement | Could Implement}"
owner: MarkOrbit Publications Editorial Board
```

---

# 2. Purpose

This Workflow Contract defines the governed execution pattern for:

```text
{workflow purpose}
```

It standardizes:

```text
trigger context
target object context
workflow applicability
workflow steps
task creation plan
event trace expectations
permission checks
policy checks
AI assistance boundaries
human review checkpoints
idempotency behavior
safe error behavior
Codex implementation rules
```

This Workflow Contract does not execute domain behavior by itself, complete tasks, send communications, select providers, approve payments, submit filings or replace owning services.

---

# 3. Core Lock

```text
{Workflow Name} Workflow Contract coordinates governed execution.
Workflow Contract Service owns workflow contract behavior.
Task Service owns active Task creation.
Owning domain services own domain state.
Permission and Policy govern every protected step.
AI may prepare, summarize and suggest only within governed scope.
Human review gates professional or external-impact actions where required.
Events preserve trace.
```

---

# 4. Contract Meaning

This contract means:

```text
a reusable governed workflow pattern for {workflow name}.
```

This contract does not mean:

```text
implementation code
database schema
UI flow
permission grant
policy approval
professional truth
task completion
communication sending
provider selection
payment approval
event emitter
```

---

# 5. Workflow Boundary

This Workflow Contract is responsible for:

```text
defining workflow trigger
defining target object context
defining workflow steps
defining required services
defining task plan shape
defining event expectations
defining permission and policy checks
defining AI assistance scope
defining human review checkpoints
defining idempotency rules
defining safe errors
defining Codex implementation expectations
```

This Workflow Contract is not responsible for:

```text
executing domain state mutation outside owning service
creating active tasks outside Task Service
sending communications outside Communication Service
selecting providers outside Routing Service
emitting events directly
evaluating Permission or Policy internally
storing implementation data
rendering UI
```

---

# 6. Trigger Context

Canonical trigger shape:

```yaml
trigger_context:
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

Trigger rules:

```text
- Triggering a workflow is not permission approval.
- Event-driven trigger must validate source event visibility and relevance.
- Agent-prepared trigger must still pass Permission and Policy checks.
- Scheduled trigger must evaluate current Policy before action.
- Apply operations require idempotency_key.
```

---

# 7. Target Object Context

Canonical target shape:

```yaml
target_context:
  target_object_type: string
  target_object_reference_id: string
  target_object_status_at_start: string | null
  target_object_owner_service: string
  target_object_visibility: string | null
```

Target rules:

```text
- Target reference must be validated by owning service.
- Workflow applicability must be evaluated before task creation.
- Policy may block or downgrade workflow output.
- Target status may change during workflow; workflow must revalidate before protected transitions.
```

---

# 8. Required Services

This workflow may require:

```text
Workflow Contract Service
Task Service
Event Service
Permission Service
Policy Service
Agent Service
{Domain Service}
{Supporting Service}
```

Service boundary rules:

```text
- Workflow Contract Service owns workflow preview and apply behavior.
- Task Service owns active Task creation.
- Event Service owns Event records.
- Permission Service owns Permission evaluation.
- Policy Service owns Policy evaluation.
- Agent Service governs AI capability use.
- Domain services own domain state changes.
```

---

# 9. Required References

Canonical references:

```yaml
references:
  workflow_contract_reference_id: string
  workflow_application_reference_id: string | null
  target_object_type: string
  target_object_reference_id: string
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
  human_review_reference_ids:
    - string
  event_reference_ids:
    - string
```

Rules:

```text
- Reference IDs must follow Reference Contract.
- Database IDs must not be exposed.
- Valid reference does not imply permission.
- Linked references must be validated by owning services.
```

---

# 10. Workflow Applicability Rules

Applicability must check:

```text
target object type
target object status
target object ownership
target object visibility
workflow contract status
workflow contract version
required permissions
policy restrictions
required minimum context
human review prerequisites
```

Applicability result shape:

```yaml
applicability:
  applicable: boolean
  applicability_status: string
  missing_context_safe:
    - string
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
```

Controlled applicability status:

```text
Applicable
NotApplicable
InsufficientContext
PermissionDenied
PolicyRestricted
RequiresHumanReview
StateInvalid
VersionUnsupported
Unknown
```

---

# 11. Workflow Step Contract

Each step must follow this shape:

```yaml
workflow_step:
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

Step rules:

```text
- step_key must be stable and unique within the workflow.
- owning_service must be explicit.
- Step must not mutate a domain object outside its owning service.
- Step must not create active tasks except through Task Service.
- Step must not emit events directly.
- Step failure behavior must be explicit.
```

---

# 12. Workflow Step List

Define steps here:

```yaml
steps:
  - step_key: "{step-key-1}"
    step_title_safe: "{Step Title}"
    step_type: "{StepType}"
    step_required: true
    owning_service: "{Owning Service}"
    target_object_type: "{ObjectType}"
    target_object_reference_id: "{reference_id}"
    input_contract_refs:
      - "{contract-ref}"
    output_contract_refs:
      - "{contract-ref}"
    permission_keys:
      - "{permission:key}"
    policy_scopes:
      - "{policy:scope}"
    human_review_required: false
    ai_assistance_allowed: true
    events_expected:
      - "{EventName}"
    failure_behavior: "StopWorkflow | SkipStep | RequireReview | Retry | SafePartial"
```

---

# 13. Task Creation Rules

Task plan shape:

```yaml
task_plan:
  proposed_tasks:
    - task_type: string
      task_title_safe: string
      task_description_safe: string | null
      target_object_type: string
      target_object_reference_id: string
      assignee_user_reference_id: string | null
      due_date: date | null
      source_step_key: string
      human_review_required: boolean
```

Rules:

```text
- Task plans are proposals until Task Service creates active Tasks.
- Active Task creation must route through Task Service.
- Workflow preview must never create active Tasks.
- Workflow apply may request task creation through Task Service.
- Duplicate workflow apply must not duplicate Tasks.
```

---

# 14. Event Rules

Expected events:

```text
WorkflowContractApplied
TaskCreated
CommunicationCreated
RoutingEvaluated
RoutingSelected
{DomainEvent}
```

Rules:

```text
- Events are emitted by owning services.
- Workflow Contract must not emit events directly.
- Event references are audit trace, not commands.
- Idempotent replay must not duplicate Events.
```

Audit context shape:

```yaml
audit_context:
  correlation_id: string | null
  causation_event_reference_id: string | null
  event_reference_ids:
    - string
```

---

# 15. Permission Rules

Required permission keys:

```text
workflow-contract:preview
workflow-contract:apply
{domain:permission}
```

Rules:

```text
- Permission Service evaluates permission.
- Workflow Contract must not grant permission.
- Each protected step must define required permission keys.
- PermissionDenied must stop or downgrade workflow behavior.
```

---

# 16. Policy Rules

Required policy scopes:

```text
workflow-contract:preview:policy
workflow-contract:apply:policy
{domain:policy}
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

# 17. AI Assistance Rules

Allowed AI roles for this workflow:

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

AI output context shape:

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

# 18. Human Review Rules

Human review checkpoints:

```yaml
human_review_checkpoints:
  - checkpoint_key: "{checkpoint-key}"
    checkpoint_title_safe: "{Checkpoint Title}"
    required: true
    required_before_step_key: "{step-key}"
    reviewer_role: "{Role}"
    review_output_contract_ref: "core-specs/contracts/common/human-review.md"
```

Rules:

```text
- Human Review records accountable professional review.
- Human Review does not execute downstream action by itself.
- Owning services decide whether review satisfies action requirements.
- Human review must gate professional or external-impact actions where required.
```

---

# 19. Idempotency Rules

Idempotency requirements:

```text
Preview:
  idempotency_key normally not required unless result is persisted.

Apply:
  idempotency_key required.

Task creation:
  must be duplicate-safe.

Communication creation:
  must be duplicate-safe.

Routing selection:
  must be duplicate-safe.
```

Rules:

```text
- Duplicate apply must not duplicate tasks, events, communications or selections.
- Owning services define semantic equality.
- Idempotency conflicts must fail safe.
```

---

# 20. Error Rules

Controlled workflow errors:

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

Safe error shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Errors must not expose restricted target data, private workflow notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 21. Versioning Rules

Version fields:

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

# 22. Preview Contract

Workflow preview request shape:

```yaml
preview_request:
  workflow_contract_reference_id: string
  target_context:
    target_object_type: string
    target_object_reference_id: string
  include_task_plan: boolean
  include_ai_summary: boolean
  permission_context: object
  policy_context: object
```

Workflow preview response shape:

```yaml
preview_response:
  preview_status: string
  applicable: boolean
  proposed_steps_visible:
    - step_key: string
      step_title_safe: string
      step_type: string
  proposed_task_plan_safe: object | null
  missing_context_safe:
    - string
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Preview does not apply workflow.
- Preview does not create active Tasks.
- Preview does not emit domain Events directly.
```

---

# 23. Apply Contract

Workflow apply request shape:

```yaml
apply_request:
  workflow_contract_reference_id: string
  idempotency_key: string
  target_context:
    target_object_type: string
    target_object_reference_id: string
  apply_scope: string
  create_tasks: boolean
  permission_context: object
  policy_context: object
  human_review_context: object | null
```

Workflow apply response shape:

```yaml
apply_response:
  workflow_application_reference_id: string
  workflow_contract_reference_id: string
  application_status: string
  created_task_reference_ids:
    - string
  skipped_steps:
    - step_key: string
      reason_safe: string | null
  event_reference_ids:
    - string
  restricted_fields_omitted: boolean
```

Rules:

```text
- Apply requires idempotency_key.
- Apply must route through Workflow Contract Service.
- Active Task creation must route through Task Service.
- Human review may be required before apply or before protected steps.
```

---

# 24. Codex Implementation Notes

Codex must:

```text
cite this workflow contract
cite Workflow Contracts README
cite Workflow Contract API Contract
cite Workflow Contract Service Spec
cite Task API and Task Service where tasks are used
cite Event API and Event Service where events are used
cite all domain owning services used by steps
use Reference Contract for all references
use Error Contract for errors
use Permission Context Contract before protected steps
use Policy Context Contract before policy-controlled steps
use AI Context Contract for AI-assisted steps
use Human Review Contract for review checkpoints
use Idempotency Contract for apply operations
use Versioning Contract for workflow versioning
write preview tests
write apply tests
write idempotency replay tests
write permission denied tests
write policy restricted tests
write human review required tests
write AI boundary tests
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

# 25. Acceptance Criteria

This Workflow Contract is accepted only if:

```text
[ ] It defines metadata.
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines contract meaning.
[ ] It defines workflow boundary.
[ ] It defines trigger context.
[ ] It defines target object context.
[ ] It defines required services.
[ ] It defines required references.
[ ] It defines applicability rules.
[ ] It defines workflow step contract.
[ ] It defines workflow step list.
[ ] It defines task creation rules.
[ ] It defines event rules.
[ ] It defines permission rules.
[ ] It defines policy rules.
[ ] It defines AI assistance rules.
[ ] It defines human review rules.
[ ] It defines idempotency rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines preview contract.
[ ] It defines apply contract.
[ ] It defines Codex implementation notes.
```

---

# 26. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Workflow Contract Template. Defines mandatory workflow contract structure, trigger/target/step shapes, task/event boundaries, permission/policy/AI/human review rules, idempotency, error handling, versioning, preview/apply contracts and Codex implementation expectations. |

---

**End of Workflow Contract Template**
