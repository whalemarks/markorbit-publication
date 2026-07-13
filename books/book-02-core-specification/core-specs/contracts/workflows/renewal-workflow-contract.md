# Renewal Workflow Contract

**Spec ID:** B02-CONTRACT-WORKFLOW-RENEWAL  
**Spec Type:** Workflow Contract Specification  
**Contract Name:** Renewal Workflow Contract  
**Contract File:** core-specs/contracts/workflows/renewal-workflow-contract.md  
**Contract Category:** Workflow  
**Related Workflow Contract Type:** RenewalWorkflow  
**Related Domains:** Trademark; Jurisdiction; Customer; Matter; Order; Document; Evidence; Task; Communication; Notification; Knowledge; Event; Permission; Policy; Agent  
**Related Object Specs:** core-specs/objects/trademark.md; core-specs/objects/jurisdiction.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/task.md; core-specs/objects/communication.md; core-specs/objects/notification.md; core-specs/objects/knowledge.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/trademark-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/task-service.md; core-specs/services/communication-service.md; core-specs/services/notification-service.md; core-specs/services/knowledge-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/trademark-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/customer-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/task-api.md; core-specs/api/communication-api.md; core-specs/api/notification-api.md; core-specs/api/knowledge-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/agent-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/notification-created.md; core-specs/events/matter-created.md; core-specs/events/order-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/workflow-agent.md; core-specs/agents/knowledge-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Workflow Contract Version:** v0.1.0  
**MVP Phase:** Phase 5 — Post-Registration / Portfolio Expansion  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Renewal Workflow Contract defines the governed execution pattern for identifying, preparing, reviewing and coordinating trademark renewal work.

It standardizes:

```text
renewal workflow trigger
trademark renewal target context
jurisdiction renewal rule context
deadline and grace-period context
customer confirmation context
matter/order preparation boundary
document and evidence preparation boundary
communication and notification preparation
task plan creation
human review checkpoints
permission and policy checks
AI assistance boundaries
idempotency behavior
safe error behavior
Codex implementation rules
```

This Workflow Contract does not file renewal applications by itself, certify deadline accuracy without review, approve customer instruction, approve payment, send external communications, or replace Trademark Service, Jurisdiction Service, Matter Service, Order Service, Document Service, Communication Service, Notification Service or Task Service.

---

# 2. Core Lock

```text
Renewal Workflow coordinates governed post-registration renewal preparation.
Trademark Service owns Trademark behavior and renewal-related trademark state.
Jurisdiction and Knowledge Services provide governed rule context, not professional truth by themselves.
Matter and Order Services own business execution context.
Document and Evidence Services own renewal documents and use/evidence records.
Task Service owns active Task creation.
Communication and Notification Services own communication and attention signals.
Permission and Policy govern every protected step.
AI may summarize, calculate candidates and draft, but must not certify deadlines, approve renewal strategy or submit renewals.
Events preserve trace.
```

---

# 3. Contract Meaning

This contract means:

```text
a reusable governed workflow pattern for preparing trademark renewal execution in MarkOrbit.
```

This contract does not mean:

```text
official renewal filing
deadline certification
legal advice approval
customer instruction approval
payment approval
provider selection
communication sending
task completion
permission grant
policy approval
event emitter
renewal filing portal
```

---

# 4. Workflow Boundary

This Workflow Contract is responsible for:

```text
defining renewal workflow trigger
defining trademark renewal target context
defining renewal deadline and grace-period preparation
defining renewal workflow steps
defining required services
defining task plan shape
defining customer communication and notification boundary
defining renewal document/evidence preparation boundary
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
official renewal submission
payment execution
deadline legal certification without review
provider selection
creating active Tasks outside Task Service
sending Communications outside Communication Service
emitting Events directly
evaluating Permission or Policy internally
rendering UI
```

---

# 5. Trigger Context

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

Supported trigger sources:

```text
RenewalWindowDetected
DeadlineMonitorDetected
ManualStaffEntry
CustomerRenewalRequest
PortfolioReview
ImportedRenewalRecord
NotificationAcknowledged
WorkflowContinuation
AgentPrepared
Unknown
```

Trigger rules:

```text
- Triggering renewal workflow is not renewal filing approval.
- Trademark reference must be validated by Trademark Service.
- Jurisdiction context must be validated before deadline preparation.
- Deadline monitor output is a signal and must be reviewed before customer-facing use.
- Agent-prepared trigger must still pass Permission and Policy checks.
- Applying workflow requires idempotency_key.
```

---

# 6. Target Object Context

Renewal Workflow may target:

```text
Trademark
Matter
Order
Customer
Notification
```

Canonical target shape:

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
- Trademark reference must be validated by Trademark Service.
- Matter and Order references must be validated by owning services where provided.
- Customer reference must be validated by Customer Service where provided.
- Target trademark status and renewal eligibility must be revalidated before protected transitions.
```

---

# 7. Required Services

This workflow may require:

```text
Workflow Contract Service
Trademark Service
Jurisdiction Service
Knowledge Service
Customer Service
Matter Service
Order Service
Document Service
Evidence Service
Communication Service
Notification Service
Task Service
Event Service
Permission Service
Policy Service
Agent Service
```

Service boundary rules:

```text
- Workflow Contract Service owns preview and apply behavior.
- Trademark Service owns renewal-related trademark state.
- Jurisdiction Service owns jurisdiction reference context.
- Knowledge Service provides governed source-grounded renewal rule references.
- Matter and Order Services own business execution state.
- Document Service owns renewal document records.
- Evidence Service owns use/evidence records where renewal requires evidence.
- Communication Service owns customer/provider communication drafts.
- Notification Service owns internal attention signals.
- Task Service owns active Task creation.
- Event Service owns Event trace.
- Permission Service owns Permission evaluation.
- Policy Service owns Policy evaluation.
- Agent Service governs AI capability use.
```

---

# 8. Required References

Canonical references:

```yaml
references:
  workflow_contract_reference_id: string
  workflow_application_reference_id: string | null
  trademark_reference_id: string
  customer_reference_id: string | null
  matter_reference_id: string | null
  order_reference_id: string | null
  jurisdiction_reference_id: string | null
  renewal_rule_reference_ids:
    - string
  document_reference_ids:
    - string
  evidence_reference_ids:
    - string
  communication_reference_id: string | null
  notification_reference_ids:
    - string
  task_reference_ids:
    - string
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

# 9. Workflow Applicability Rules

Applicability must check:

```text
target trademark status
registration date or renewal basis
jurisdiction renewal rules
renewal window status
grace period status
customer relationship context
matter/order readiness
required documents
required use/evidence where applicable
workflow contract status and version
required permissions
policy restrictions
human review prerequisites
```

Applicability result shape:

```yaml
applicability:
  applicable: boolean
  applicability_status: string
  renewal_window_status: string | null
  deadline_risk_level: string | null
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
NotYetInRenewalWindow
GracePeriodOnly
DeadlineExpired
PermissionDenied
PolicyRestricted
RequiresHumanReview
StateInvalid
VersionUnsupported
Unknown
```

---

# 10. Workflow Step Contract

Each step must follow:

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
- step_key must be stable and unique.
- owning_service must be explicit.
- Step must not mutate a domain object outside its owning service.
- Step must not create active tasks except through Task Service.
- Step must not emit events directly.
```

---

# 11. Workflow Step List

Canonical renewal workflow steps:

```yaml
steps:
  - step_key: validate-renewal-target
    step_title_safe: Validate Renewal Target
    step_type: Review
    step_required: true
    owning_service: Trademark Service
    target_object_type: Trademark
    target_object_reference_id: trademark_reference_id
    input_contract_refs:
      - core-specs/contracts/api/trademark-api-contract.md
      - core-specs/contracts/api/jurisdiction-api-contract.md
    output_contract_refs:
      - core-specs/contracts/workflows/renewal-workflow-contract.md
    permission_keys:
      - trademark:read
      - trademark:validate
    policy_scopes:
      - trademark:read:policy
      - trademark:reference:policy
    human_review_required: false
    ai_assistance_allowed: false
    events_expected:
      - WorkflowContractApplied
    failure_behavior: StopWorkflow

  - step_key: retrieve-renewal-rules
    step_title_safe: Retrieve Renewal Rules
    step_type: Review
    step_required: true
    owning_service: Knowledge Service
    target_object_type: Knowledge
    target_object_reference_id: renewal_rule_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/knowledge-api-contract.md
      - core-specs/contracts/api/jurisdiction-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/knowledge-api-contract.md
    permission_keys:
      - knowledge:read
      - jurisdiction:read
    policy_scopes:
      - knowledge:read:policy
      - jurisdiction:read:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: prepare-deadline-summary
    step_title_safe: Prepare Renewal Deadline Summary
    step_type: StatusCheck
    step_required: true
    owning_service: Trademark Service
    target_object_type: Trademark
    target_object_reference_id: trademark_reference_id
    input_contract_refs:
      - core-specs/contracts/api/trademark-api-contract.md
      - core-specs/contracts/api/knowledge-api-contract.md
    output_contract_refs:
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - trademark:read
      - trademark:update
      - knowledge:read
    policy_scopes:
      - trademark:read:policy
      - trademark:update:policy
      - knowledge:read:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: validate-customer-renewal-context
    step_title_safe: Validate Customer Renewal Context
    step_type: CustomerConfirmation
    step_required: true
    owning_service: Customer Service
    target_object_type: Customer
    target_object_reference_id: customer_reference_id
    input_contract_refs:
      - core-specs/contracts/api/customer-api-contract.md
      - core-specs/contracts/api/trademark-api-contract.md
    output_contract_refs:
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - customer:read
      - trademark:read
    policy_scopes:
      - customer:read:policy
      - trademark:read:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: prepare-renewal-matter-order
    step_title_safe: Prepare Renewal Matter or Order
    step_type: InternalApproval
    step_required: false
    owning_service: Matter Service
    target_object_type: Matter
    target_object_reference_id: matter_reference_id
    input_contract_refs:
      - core-specs/contracts/api/matter-api-contract.md
      - core-specs/contracts/api/order-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/matter-api-contract.md
      - core-specs/contracts/api/order-api-contract.md
    permission_keys:
      - matter:create
      - matter:update
      - order:create
      - order:update
    policy_scopes:
      - matter:create:policy
      - matter:update:policy
      - order:create:policy
      - order:update:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected:
      - MatterCreated
      - OrderCreated
    failure_behavior: RequireReview

  - step_key: prepare-renewal-documents
    step_title_safe: Prepare Renewal Documents
    step_type: PrepareDocument
    step_required: true
    owning_service: Document Service
    target_object_type: Document
    target_object_reference_id: document_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/document-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/document-api-contract.md
    permission_keys:
      - document:create
      - document:update
      - document:read
    policy_scopes:
      - document:create:policy
      - document:update:policy
      - document:visibility:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: prepare-use-evidence
    step_title_safe: Prepare Use or Evidence Context
    step_type: CollectEvidence
    step_required: false
    owning_service: Evidence Service
    target_object_type: Evidence
    target_object_reference_id: evidence_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/evidence-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/evidence-api-contract.md
    permission_keys:
      - evidence:create
      - evidence:update
      - evidence:read
    policy_scopes:
      - evidence:create:policy
      - evidence:update:policy
      - evidence:visibility:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: prepare-customer-renewal-communication
    step_title_safe: Prepare Customer Renewal Communication
    step_type: ExternalCommunication
    step_required: true
    owning_service: Communication Service
    target_object_type: Communication
    target_object_reference_id: communication_reference_id
    input_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
    permission_keys:
      - communication:create
      - communication:draft:prepare
    policy_scopes:
      - communication:create:policy
      - communication:draft:prepare:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected:
      - CommunicationCreated
    failure_behavior: SafePartial

  - step_key: create-renewal-notifications
    step_title_safe: Create Renewal Notifications
    step_type: StatusCheck
    step_required: false
    owning_service: Notification Service
    target_object_type: Notification
    target_object_reference_id: notification_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/notification-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/notification-api-contract.md
    permission_keys:
      - notification:create
    policy_scopes:
      - notification:create:policy
    human_review_required: false
    ai_assistance_allowed: false
    events_expected:
      - NotificationCreated
    failure_behavior: SafePartial

  - step_key: create-renewal-tasks
    step_title_safe: Create Renewal Tasks
    step_type: TaskGroup
    step_required: true
    owning_service: Task Service
    target_object_type: Task
    target_object_reference_id: task_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/task-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/task-api-contract.md
    permission_keys:
      - task:create
    policy_scopes:
      - task:create:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected:
      - TaskCreated
    failure_behavior: SafePartial

  - step_key: review-renewal-readiness
    step_title_safe: Review Renewal Readiness
    step_type: InternalApproval
    step_required: true
    owning_service: Matter Service
    target_object_type: Matter
    target_object_reference_id: matter_reference_id
    input_contract_refs:
      - core-specs/contracts/common/human-review.md
      - core-specs/contracts/api/matter-api-contract.md
    output_contract_refs:
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - matter:update
    policy_scopes:
      - matter:update:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview
```

---

# 12. Task Creation Rules

Suggested task plan:

```yaml
task_plan:
  proposed_tasks:
    - task_type: StatusCheckTask
      task_title_safe: Review renewal deadline and eligibility
      task_description_safe: Confirm renewal window, grace period and deadline risk.
      target_object_type: Trademark
      target_object_reference_id: trademark_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-deadline-summary
      human_review_required: true

    - task_type: CustomerConfirmationTask
      task_title_safe: Confirm renewal instruction with customer
      task_description_safe: Confirm customer renewal instruction, fees, documents and any use/evidence requirements.
      target_object_type: Customer
      target_object_reference_id: customer_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-customer-renewal-communication
      human_review_required: true

    - task_type: DocumentPreparationTask
      task_title_safe: Prepare renewal documents
      task_description_safe: Prepare renewal forms, POA or supporting documents.
      target_object_type: Document
      target_object_reference_id: null
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-renewal-documents
      human_review_required: true

    - task_type: InternalApprovalTask
      task_title_safe: Approve renewal readiness
      task_description_safe: Review whether renewal package is ready for governed filing/payment process.
      target_object_type: Matter
      target_object_reference_id: matter_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: review-renewal-readiness
      human_review_required: true
```

Rules:

```text
- Task plans are proposals until Task Service creates active Tasks.
- Active Task creation must route through Task Service.
- Workflow preview must never create active Tasks.
- Workflow apply may request Task Service to create Tasks.
- Duplicate workflow apply must not duplicate Tasks.
```

---

# 13. Event Rules

Expected events may include:

```text
WorkflowContractApplied
MatterCreated
OrderCreated
CommunicationCreated
NotificationCreated
TaskCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Events are emitted by owning services.
- Workflow Contract must not emit events directly.
- MatterCreated may only be emitted by Matter Service.
- OrderCreated may only be emitted by Order Service.
- CommunicationCreated may only be emitted by Communication Service.
- NotificationCreated may only be emitted by Notification Service.
- TaskCreated may only be emitted by Task Service.
- Official renewal filing/payment events are outside this workflow unless governed filing/payment services exist.
- Event references are audit trace, not commands.
- Idempotent replay must not duplicate Events.
```

---

# 14. Permission Rules

Required permission keys:

```text
workflow-contract:preview
workflow-contract:apply
trademark:read
trademark:validate
trademark:update
jurisdiction:read
knowledge:read
customer:read
matter:create
matter:update
order:create
order:update
document:create
document:update
document:read
evidence:create
evidence:update
evidence:read
communication:create
communication:draft:prepare
notification:create
task:create
```

Rules:

```text
- Permission Service evaluates permission.
- Workflow Contract must not grant permission.
- Each protected step must define required permission keys.
- PermissionDenied must stop or downgrade workflow behavior.
```

---

# 15. Policy Rules

Required policy scopes:

```text
workflow-contract:preview:policy
workflow-contract:apply:policy
trademark:read:policy
trademark:reference:policy
trademark:update:policy
jurisdiction:read:policy
knowledge:read:policy
customer:read:policy
matter:create:policy
matter:update:policy
order:create:policy
order:update:policy
document:create:policy
document:update:policy
document:visibility:policy
evidence:create:policy
evidence:update:policy
evidence:visibility:policy
communication:create:policy
communication:draft:prepare:policy
notification:create:policy
task:create:policy
cross-organization:workflow
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may block, redact, downgrade or require human review.
- Customer contacts, renewal deadlines, documents, evidence, commercial terms and private notes may be redacted.
- Workflow output must disclose policy omissions where applicable.
- PolicyRestricted must stop protected action or return safe partial output.
```

---

# 16. AI Assistance Rules

Allowed AI roles:

```text
summarize trademark renewal context
retrieve governed renewal rule references
prepare deadline candidate summary
identify missing renewal information
prepare renewal checklist
prepare customer renewal communication draft
prepare use/evidence gap summary
prepare follow-up task plan
```

AI must not:

```text
certify renewal deadline accuracy
approve renewal eligibility
approve customer instruction
submit renewal filing
approve payment
send customer/provider communication
complete tasks
select providers
create legal advice
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

# 17. Human Review Rules

Human review checkpoints:

```yaml
human_review_checkpoints:
  - checkpoint_key: confirm-renewal-deadline
    checkpoint_title_safe: Confirm Renewal Deadline
    required: true
    required_before_step_key: prepare-customer-renewal-communication
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: confirm-customer-renewal-instruction
    checkpoint_title_safe: Confirm Customer Renewal Instruction
    required: true
    required_before_step_key: prepare-renewal-matter-order
    reviewer_role: BusinessReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-renewal-documents
    checkpoint_title_safe: Approve Renewal Documents
    required: true
    required_before_step_key: review-renewal-readiness
    reviewer_role: FilingReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-renewal-communication
    checkpoint_title_safe: Approve Renewal Communication
    required: true
    required_before_step_key: prepare-customer-renewal-communication
    reviewer_role: CommunicationReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-renewal-readiness
    checkpoint_title_safe: Approve Renewal Readiness
    required: true
    required_before_step_key: review-renewal-readiness
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md
```

Rules:

```text
- Human Review records accountable professional/business review.
- Human Review does not file renewal or approve payment by itself.
- Matter, Order and downstream filing/payment services decide whether review satisfies execution requirements.
- Human review must gate deadline confirmation, customer instruction, documents, communication and renewal readiness.
```

---

# 18. Idempotency Rules

Idempotency requirements:

```text
Preview:
  idempotency_key normally not required unless result is persisted.

Apply:
  idempotency_key required.

Matter/Order creation:
  must be duplicate-safe.

Document creation:
  must be duplicate-safe where generated.

Notification creation:
  must be duplicate-safe.

Task creation:
  must be duplicate-safe.

Communication creation:
  must be duplicate-safe.
```

Rules:

```text
- Duplicate apply must not duplicate Matter, Order, Documents, Notifications, Tasks, Communications or Events.
- Owning services define semantic equality.
- Idempotency conflicts must fail safe.
```

---

# 19. Error Rules

Controlled workflow errors:

```text
WorkflowReferenceInvalid
WorkflowNotApplicable
WorkflowPreviewUnavailable
WorkflowApplyConflict
TargetReferenceInvalid
TrademarkReferenceInvalid
JurisdictionReferenceInvalid
CustomerReferenceInvalid
MatterReferenceInvalid
OrderReferenceInvalid
DocumentReferenceInvalid
EvidenceReferenceInvalid
CommunicationReferenceInvalid
NotificationReferenceInvalid
TaskCreationFailed
RenewalDeadlineMissing
RenewalWindowNotOpen
GracePeriodOnly
RenewalDeadlineExpired
PermissionDenied
PolicyRestricted
HumanReviewRequired
StateInvalid
InsufficientRenewalContext
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
- Errors must not expose restricted customer data, renewal commercial terms, documents, evidence, private notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 20. Versioning Rules

Version fields:

```yaml
workflow_contract_version: v0.1.0
contract_version: v0.1.0
schema_version: v0.1.0
renewal_rule_version: v0.1.0
```

Rules:

```text
- Breaking changes require version bump.
- Workflow application must record workflow_contract_version used.
- Renewal rule version/source context must be recorded where available.
- Historical workflow applications must remain traceable.
- Deprecated workflow versions must not be silently rewritten.
```

---

# 21. Preview Contract

Workflow preview request shape:

```yaml
preview_request:
  workflow_contract_reference_id: string
  target_context:
    target_object_type: Trademark | Matter | Order | Customer | Notification
    target_object_reference_id: string
  include_task_plan: boolean
  include_ai_summary: boolean
  include_deadline_summary: boolean
  include_renewal_checklist: boolean
  permission_context: object
  policy_context: object
```

Workflow preview response shape:

```yaml
preview_response:
  preview_status: string
  applicable: boolean
  renewal_window_status: string | null
  deadline_risk_level: string | null
  proposed_steps_visible:
    - step_key: string
      step_title_safe: string
      step_type: string
  proposed_task_plan_safe: object | null
  renewal_summary_safe: string | null
  deadline_summary_safe: string | null
  renewal_checklist_safe:
    - string
  missing_context_safe:
    - string
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Preview does not apply workflow.
- Preview does not create Matter, Order, Documents, Notifications, Communications or active Tasks.
- Preview does not certify deadline accuracy.
- Preview does not submit renewal filing or payment.
- Preview does not emit domain Events directly.
```

---

# 22. Apply Contract

Workflow apply request shape:

```yaml
apply_request:
  workflow_contract_reference_id: string
  idempotency_key: string
  target_context:
    target_object_type: Trademark | Matter | Order | Customer | Notification
    target_object_reference_id: string
  apply_scope: string
  create_tasks: boolean
  create_matter_or_order_if_missing: boolean
  prepare_documents: boolean
  prepare_evidence_context: boolean
  prepare_customer_communication: boolean
  create_notifications: boolean
  prepare_renewal_readiness_review: boolean
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
  trademark_reference_id: string
  matter_reference_id: string | null
  order_reference_id: string | null
  document_reference_ids:
    - string
  evidence_reference_ids:
    - string
  communication_reference_id: string | null
  notification_reference_ids:
    - string
  created_task_reference_ids:
    - string
  renewal_readiness_status: string | null
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
- Trademark update must route through Trademark Service.
- Matter/Order creation must route through Matter/Order Service.
- Document preparation must route through Document Service.
- Evidence preparation must route through Evidence Service.
- Notification creation must route through Notification Service.
- Active Task creation must route through Task Service.
- Communication draft creation must route through Communication Service.
- Official renewal filing/payment must not happen in this workflow contract.
```

---

# 23. Controlled Values

## 23.1 apply_scope

```text
PreviewOnly
PrepareDeadlineSummary
PrepareMatterOrder
PrepareDocuments
PrepareEvidence
PrepareCommunication
PrepareNotifications
PrepareTasks
PrepareRenewalReadiness
FullRenewalPreparation
Unknown
```

## 23.2 application_status

```text
Applied
PartiallyApplied
NotApplied
PolicyRestricted
PermissionDenied
RequiresHumanReview
Conflict
Error
Unknown
```

## 23.3 preview_status

```text
Completed
Partial
NotApplicable
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 23.4 renewal_window_status

```text
NotYetOpen
Open
GracePeriod
Expired
Unknown
```

## 23.5 deadline_risk_level

```text
Unknown
Low
Normal
High
Critical
Expired
```

## 23.6 renewal_readiness_status

```text
NotReady
PartiallyReady
ReadyForProfessionalReview
ReadyForCustomerConfirmation
ReadyForFilingProcess
PolicyRestricted
RequiresHumanReview
Unknown
```

---

# 24. Codex Implementation Notes

Codex must:

```text
cite this Renewal Workflow Contract
cite Workflow Contracts README
cite Workflow Contract API Contract
cite Workflow Contract Service Spec
cite Trademark API and Trademark Service
cite Jurisdiction API and Jurisdiction Service
cite Knowledge API and Knowledge Service
cite Customer API and Customer Service
cite Matter API and Matter Service
cite Order API and Order Service
cite Document API and Document Service
cite Evidence API and Evidence Service
cite Communication API and Communication Service
cite Notification API and Notification Service
cite Task API and Task Service
cite Event API and Event Service
use Reference Contract for all references
use Error Contract for errors
use Permission Context Contract before protected steps
use Policy Context Contract before policy-controlled steps
use AI Context Contract for AI-assisted steps
use Human Review Contract for deadline/customer-instruction/document/communication/renewal-readiness checkpoints
use Idempotency Contract for apply operations
use Versioning Contract for workflow versioning
write preview tests
write apply tests
write duplicate apply tests
write tests that preview creates no Matter, Order, Documents, Notifications, Communication or Tasks
write tests that apply does not duplicate Matter/Order/Documents/Notifications/Tasks/Communication
write tests that AI cannot certify deadlines or submit renewal
write tests that human review gates deadline, customer instruction, documents, communication and renewal readiness
write tests that official renewal filing/payment is not performed by this workflow
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
treat workflow contract as implementation code
create Trademark updates outside Trademark Service
create Matter or Order outside owning services
create Documents outside Document Service
create Evidence outside Evidence Service
create Notifications outside Notification Service
create tasks outside Task Service
send communication outside Communication Service
submit official renewal filing or payment from this workflow
emit events directly from workflow code
mutate target object outside owning service
skip Permission or Policy checks
allow AI to certify deadline, approve renewal eligibility, submit renewals or create legal advice
hide human-review requirements
overwrite historical workflow versions silently
```

---

# 25. Acceptance Criteria

This Renewal Workflow Contract is accepted only if:

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
[ ] It defines controlled values.
[ ] It defines Codex implementation notes.
```

---

# 26. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Renewal Workflow Contract. Defines governed renewal target validation, renewal rule retrieval, deadline summary, customer renewal context, renewal matter/order preparation, documents/evidence preparation, communication and notification preparation, task plan, renewal readiness review, Permission/Policy context, AI and human review rules, idempotency, events, errors, versioning and Codex implementation expectations. |

---

## Workflow Component Contract Consumption

State Definitions conform to [Workflow State Definition Contract](components/workflow-state-definition-contract.md). Transition Definitions conform to [Workflow Transition Definition Contract](components/workflow-transition-definition-contract.md). Workflow validation does not perform domain mutation; owning Services remain mutation authorities. This reference does not change MVP Depth, does not promote preview-only workflows, does not send Communication Review output, does not submit Trademark Applications, and does not add protected external action.

**End of Renewal Workflow Contract**
