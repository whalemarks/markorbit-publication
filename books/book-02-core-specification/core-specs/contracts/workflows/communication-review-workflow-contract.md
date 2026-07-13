# Communication Review Workflow Contract

**Spec ID:** B02-CONTRACT-WORKFLOW-COMMUNICATION-REVIEW  
**Spec Type:** Workflow Contract Specification  
**Contract Name:** Communication Review Workflow Contract  
**Contract File:** core-specs/contracts/workflows/communication-review-workflow-contract.md  
**Contract Category:** Workflow  
**Related Workflow Contract Type:** CommunicationReviewWorkflow  
**Related Domains:** Communication; Document; Task; Matter; Order; Customer; Service Provider; Partner; Event; Permission; Policy; Agent  
**Related Object Specs:** core-specs/objects/communication.md; core-specs/objects/document.md; core-specs/objects/task.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/customer.md; core-specs/objects/service-provider.md; core-specs/objects/partner.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/communication-service.md; core-specs/services/document-service.md; core-specs/services/task-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/customer-service.md; core-specs/services/service-provider-service.md; core-specs/services/partner-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/communication-api.md; core-specs/api/document-api.md; core-specs/api/task-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/customer-api.md; core-specs/api/service-provider-api.md; core-specs/api/partner-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/agent-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/communication-created.md; core-specs/events/task-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/communication-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/task-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Workflow Contract Version:** v0.1.0  
**MVP Phase:** Phase 4 — Collaboration Network / Communication Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Communication Review Workflow Contract defines the governed execution pattern for drafting, reviewing, approving and preparing communications for internal, customer-facing, provider-facing or partner-facing use.

It standardizes:

```text
communication review trigger
communication target context
source matter/order/customer/provider/partner context
document attachment context
AI-assisted draft boundary
human review checkpoints
approval and revision loop
send-preparation boundary
follow-up task plan creation
permission and policy checks
idempotency behavior
safe error behavior
Codex implementation rules
```

This Workflow Contract does not silently send external communications, approve legal advice, bind the organization, complete tasks, close matters/orders, replace Communication Service, evaluate Permission/Policy, or authorize AI output as final communication.

---

# 2. Core Lock

```text
Communication Review Workflow coordinates governed communication preparation and review.
Communication Service owns Communication behavior.
Document Service owns attachments and source documents.
Task Service owns active Task creation.
Matter, Order, Customer, Service Provider and Partner Services own linked business context.
Permission and Policy govern every protected step.
Communication Agent may draft and summarize, but must not approve or send.
External delivery requires explicit governed send process and human review where required.
Events preserve trace.
```

---

# 3. Contract Meaning

This contract means:

```text
a reusable governed workflow pattern for moving communication from draft or request state to reviewed, approved and send-ready state.
```

This contract does not mean:

```text
external message delivery
legal notice approval
professional truth approval
customer consent
task completion
matter completion
order completion
provider engagement approval
permission grant
policy approval
event emitter
inbox UI
```

---

# 4. Workflow Boundary

This Workflow Contract is responsible for:

```text
defining communication review trigger
defining communication target context
defining review workflow steps
defining required services
defining draft preparation boundary
defining review and approval boundary
defining send-preparation boundary
defining follow-up task plan shape
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
external delivery provider internals
sending communications outside Communication Service
approving legal/professional truth
creating active Tasks outside Task Service
closing linked Matter or Order
binding customer/provider/partner engagement
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
ManualDraftCreated
AIDraftPrepared
CustomerIntakeRequiresReply
MatterRequiresCommunication
OrderRequiresCommunication
ProviderRoutingSelected
OfficeActionResponseNeedsCustomerConfirmation
TaskRequiresCommunication
ImportedMessage
WorkflowContinuation
Unknown
```

Trigger rules:

```text
- Triggering communication review is not communication approval.
- Existing Communication reference must be validated by Communication Service where provided.
- Linked Matter, Order, Customer, Service Provider or Partner references must be validated by owning services where provided.
- AI-prepared draft must still pass Permission, Policy and Human Review checks.
- Applying workflow requires idempotency_key.
```

---

# 6. Target Object Context

Communication Review Workflow may target:

```text
Communication
Matter
Order
Customer
ServiceProvider
Partner
Task
Document
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
- Communication reference must be validated by Communication Service where target is Communication.
- Matter and Order references must be validated by owning services where provided.
- Customer, Service Provider and Partner references must be validated by owning services where provided.
- Document references must be validated by Document Service where used as source or attachment.
- Target status must be revalidated before approval and send-preparation.
```

---

# 7. Required Services

This workflow may require:

```text
Workflow Contract Service
Communication Service
Document Service
Task Service
Matter Service
Order Service
Customer Service
Service Provider Service
Partner Service
Event Service
Permission Service
Policy Service
Agent Service
```

Service boundary rules:

```text
- Workflow Contract Service owns preview and apply behavior.
- Communication Service owns draft creation, review, approval and send-preparation behavior.
- Document Service owns source document and attachment references.
- Task Service owns active Task creation.
- Matter and Order Services own business execution state.
- Customer, Service Provider and Partner Services own relationship and contact context.
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
  communication_reference_id: string | null
  matter_reference_id: string | null
  order_reference_id: string | null
  customer_reference_id: string | null
  service_provider_reference_id: string | null
  partner_reference_id: string | null
  task_reference_id: string | null
  source_document_reference_ids:
    - string
  attachment_document_reference_ids:
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
target object type and status
communication status
communication type and channel
recipient context availability
source object visibility
attachment/document availability
AI draft status where applicable
human review requirements
workflow contract status and version
required permissions
policy restrictions
```

Applicability result shape:

```yaml
applicability:
  applicable: boolean
  applicability_status: string
  missing_context_safe:
    - string
  communication_risk_level: string | null
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

Canonical communication review steps:

```yaml
steps:
  - step_key: validate-communication-context
    step_title_safe: Validate Communication Context
    step_type: Review
    step_required: true
    owning_service: Communication Service
    target_object_type: Communication
    target_object_reference_id: communication_reference_id
    input_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
      - core-specs/contracts/api/matter-api-contract.md
      - core-specs/contracts/api/order-api-contract.md
    output_contract_refs:
      - core-specs/contracts/workflows/communication-review-workflow-contract.md
    permission_keys:
      - communication:read
      - matter:read
      - order:read
    policy_scopes:
      - communication:read:policy
      - matter:read:policy
      - order:read:policy
    human_review_required: false
    ai_assistance_allowed: false
    events_expected:
      - WorkflowContractApplied
    failure_behavior: StopWorkflow

  - step_key: validate-recipients-and-channel
    step_title_safe: Validate Recipients and Channel
    step_type: Review
    step_required: true
    owning_service: Communication Service
    target_object_type: Communication
    target_object_reference_id: communication_reference_id
    input_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
      - core-specs/contracts/api/customer-api-contract.md
      - core-specs/contracts/api/service-provider-api-contract.md
      - core-specs/contracts/api/partner-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
    permission_keys:
      - communication:read
      - customer:read
      - service-provider:read
      - partner:read
    policy_scopes:
      - communication:read:policy
      - communication:recipient:visibility:policy
      - customer:read:policy
      - service-provider:read:policy
      - partner:read:policy
    human_review_required: true
    ai_assistance_allowed: false
    events_expected: []
    failure_behavior: RequireReview

  - step_key: validate-source-documents
    step_title_safe: Validate Source Documents and Attachments
    step_type: PrepareDocument
    step_required: false
    owning_service: Document Service
    target_object_type: Document
    target_object_reference_id: source_document_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/document-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/document-api-contract.md
    permission_keys:
      - document:read
      - document:validate
    policy_scopes:
      - document:visibility:policy
      - document:reference:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: prepare-or-update-draft
    step_title_safe: Prepare or Update Communication Draft
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
      - communication:update
      - communication:draft:prepare
    policy_scopes:
      - communication:create:policy
      - communication:update:policy
      - communication:draft:prepare:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected:
      - CommunicationCreated
    failure_behavior: RequireReview

  - step_key: review-communication-content
    step_title_safe: Review Communication Content
    step_type: InternalApproval
    step_required: true
    owning_service: Communication Service
    target_object_type: Communication
    target_object_reference_id: communication_reference_id
    input_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
      - core-specs/contracts/common/human-review.md
    output_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - communication:review
    policy_scopes:
      - communication:review:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: resolve-revisions
    step_title_safe: Resolve Requested Revisions
    step_type: Review
    step_required: false
    owning_service: Communication Service
    target_object_type: Communication
    target_object_reference_id: communication_reference_id
    input_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
    permission_keys:
      - communication:update
      - communication:draft:prepare
    policy_scopes:
      - communication:update:policy
      - communication:draft:prepare:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: approve-communication
    step_title_safe: Approve Communication
    step_type: InternalApproval
    step_required: true
    owning_service: Communication Service
    target_object_type: Communication
    target_object_reference_id: communication_reference_id
    input_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
      - core-specs/contracts/common/human-review.md
    output_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
    permission_keys:
      - communication:approve
    policy_scopes:
      - communication:approve:policy
    human_review_required: true
    ai_assistance_allowed: false
    events_expected: []
    failure_behavior: RequireReview

  - step_key: prepare-send
    step_title_safe: Prepare Send
    step_type: ExternalCommunication
    step_required: false
    owning_service: Communication Service
    target_object_type: Communication
    target_object_reference_id: communication_reference_id
    input_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
    permission_keys:
      - communication:send:prepare
    policy_scopes:
      - communication:send:prepare:policy
    human_review_required: true
    ai_assistance_allowed: false
    events_expected: []
    failure_behavior: RequireReview

  - step_key: create-follow-up-tasks
    step_title_safe: Create Follow-up Tasks
    step_type: TaskGroup
    step_required: false
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
```

---

# 12. Task Creation Rules

Suggested task plan:

```yaml
task_plan:
  proposed_tasks:
    - task_type: ReviewTask
      task_title_safe: Review communication recipients and channel
      task_description_safe: Confirm recipients, channel and linked business context before communication approval.
      target_object_type: Communication
      target_object_reference_id: communication_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: validate-recipients-and-channel
      human_review_required: true

    - task_type: ReviewTask
      task_title_safe: Review communication content
      task_description_safe: Review communication wording, attachments and policy omissions.
      target_object_type: Communication
      target_object_reference_id: communication_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: review-communication-content
      human_review_required: true

    - task_type: InternalApprovalTask
      task_title_safe: Approve communication for send-preparation
      task_description_safe: Approve communication before governed send-preparation.
      target_object_type: Communication
      target_object_reference_id: communication_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: approve-communication
      human_review_required: true

    - task_type: FollowUpTask
      task_title_safe: Follow up after communication review
      task_description_safe: Track next action after communication approval or send-preparation.
      target_object_type: Communication
      target_object_reference_id: communication_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: create-follow-up-tasks
      human_review_required: false
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
CommunicationCreated
TaskCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Events are emitted by owning services.
- Workflow Contract must not emit events directly.
- CommunicationCreated may only be emitted by Communication Service.
- Communication review/approval/send-preparation events may be reserved for later if event specs exist.
- TaskCreated may only be emitted by Task Service.
- External delivery events are outside this workflow unless Communication Service owns a governed delivery handoff.
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

# 14. Permission Rules

Required permission keys:

```text
workflow-contract:preview
workflow-contract:apply
communication:create
communication:read
communication:update
communication:draft:prepare
communication:review
communication:approve
communication:send:prepare
customer:read
service-provider:read
partner:read
matter:read
order:read
document:read
document:validate
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
communication:create:policy
communication:read:policy
communication:update:policy
communication:draft:prepare:policy
communication:review:policy
communication:approve:policy
communication:send:prepare:policy
communication:recipient:visibility:policy
customer:read:policy
service-provider:read:policy
partner:read:policy
matter:read:policy
order:read:policy
document:visibility:policy
document:reference:policy
task:create:policy
cross-organization:workflow
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may block, redact, downgrade or require human review.
- Communication body, recipients, addresses, attachments, source context and commercial terms may be redacted.
- Workflow output must disclose policy omissions where applicable.
- PolicyRestricted must stop protected action or return safe partial output.
```

---

# 16. AI Assistance Rules

Allowed AI roles:

```text
summarize linked business context
summarize source documents visible under policy
prepare communication draft
revise communication draft
identify missing recipient or attachment context
prepare review checklist
prepare follow-up task plan
```

AI must not:

```text
approve communication
send communication
bind the organization
create legal/professional truth
decide customer consent
complete tasks
close Matter or Order
select providers
approve payment
bypass Permission or Policy
```

AI output context shape:

```yaml
ai_output_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: CommunicationAgent | null
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
```

---

# 17. Human Review Rules

Human review checkpoints:

```yaml
human_review_checkpoints:
  - checkpoint_key: review-recipients
    checkpoint_title_safe: Review Recipients and Channel
    required: true
    required_before_step_key: prepare-or-update-draft
    reviewer_role: CommunicationReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: review-content
    checkpoint_title_safe: Review Communication Content
    required: true
    required_before_step_key: approve-communication
    reviewer_role: CommunicationReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-communication
    checkpoint_title_safe: Approve Communication
    required: true
    required_before_step_key: prepare-send
    reviewer_role: AuthorizedApprover
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-send-preparation
    checkpoint_title_safe: Approve Send Preparation
    required: true
    required_before_step_key: prepare-send
    reviewer_role: AuthorizedSender
    review_output_contract_ref: core-specs/contracts/common/human-review.md
```

Rules:

```text
- Human Review records accountable professional/business review.
- Human Review does not send communication by itself.
- Communication Service decides whether review satisfies approval or send-preparation requirements.
- Human review must gate external-facing, customer-facing, provider-facing and legal-risk communication.
```

---

# 18. Idempotency Rules

Idempotency requirements:

```text
Preview:
  idempotency_key normally not required unless result is persisted.

Apply:
  idempotency_key required.

Communication creation/update:
  must be duplicate-safe.

Review and approval:
  may require idempotency_key where owning service marks the operation duplicate-sensitive.

Task creation:
  must be duplicate-safe.

Send-preparation:
  must be duplicate-safe and must not silently deliver externally.
```

Rules:

```text
- Duplicate apply must not duplicate Communication, Tasks or Events.
- Duplicate approval must not duplicate approval trace.
- Duplicate send-preparation must not duplicate delivery handoff.
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
CommunicationReferenceInvalid
CustomerReferenceInvalid
ServiceProviderReferenceInvalid
PartnerReferenceInvalid
MatterReferenceInvalid
OrderReferenceInvalid
DocumentReferenceInvalid
RecipientReferenceInvalid
ChannelInvalid
AttachmentReferenceInvalid
ReviewInvalid
ApprovalInvalid
SendPreparationBlocked
TaskCreationFailed
PermissionDenied
PolicyRestricted
HumanReviewRequired
StateInvalid
InsufficientCommunicationContext
SentCommunicationImmutable
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
- Errors must not expose restricted communication body, recipient addresses, attachments, private notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 20. Versioning Rules

Version fields:

```yaml
workflow_contract_version: v0.1.0
contract_version: v0.1.0
schema_version: v0.1.0
communication_review_version: v0.1.0
```

Rules:

```text
- Breaking changes require version bump.
- Workflow application must record workflow_contract_version used.
- Review/approval state must remain traceable.
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
    target_object_type: Communication | Matter | Order | Customer | ServiceProvider | Partner | Task | Document
    target_object_reference_id: string
  include_task_plan: boolean
  include_ai_summary: boolean
  include_review_checklist: boolean
  include_send_readiness_preview: boolean
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
  communication_summary_safe: string | null
  review_checklist_safe:
    - string
  send_readiness_preview_safe: string | null
  missing_context_safe:
    - string
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Preview does not apply workflow.
- Preview does not create, approve or send Communication.
- Preview does not create active Tasks.
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
    target_object_type: Communication | Matter | Order | Customer | ServiceProvider | Partner | Task | Document
    target_object_reference_id: string
  apply_scope: string
  create_communication_if_missing: boolean
  prepare_or_update_draft: boolean
  request_review: boolean
  approve_if_review_satisfied: boolean
  prepare_send: boolean
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
  communication_reference_id: string | null
  review_status: string | null
  approval_status: string | null
  send_preparation_status: string | null
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
- Communication creation/update/review/approval/send-preparation must route through Communication Service.
- Active Task creation must route through Task Service.
- Send-preparation must not silently deliver externally.
- External delivery must be separately governed by Communication Service if supported.
```

---

# 23. Controlled Values

## 23.1 apply_scope

```text
PreviewOnly
ValidateContext
PrepareDraft
RequestReview
ResolveRevisions
ApproveCommunication
PrepareSend
PrepareTasks
FullCommunicationReview
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

## 23.4 communication_risk_level

```text
Unknown
Low
Normal
High
Critical
```

## 23.5 review_outcome

```text
Approved
RevisionRequested
Rejected
Escalated
NoDecision
Unknown
```

## 23.6 send_readiness_status

```text
NotReady
ReadyForReview
ReadyForSendPreparation
SendPrepared
PolicyRestricted
RequiresHumanReview
Unknown
```

---

# 24. Codex Implementation Notes

Codex must:

```text
cite this Communication Review Workflow Contract
cite Workflow Contracts README
cite Workflow Contract API Contract
cite Workflow Contract Service Spec
cite Communication API and Communication Service
cite Document API and Document Service
cite Task API and Task Service
cite Matter API and Matter Service
cite Order API and Order Service
cite Customer API and Customer Service
cite Service Provider API and Service Provider Service
cite Partner API and Partner Service
cite Event API and Event Service
cite Communication Agent Spec
use Reference Contract for all references
use Error Contract for errors
use Permission Context Contract before protected steps
use Policy Context Contract before policy-controlled steps
use AI Context Contract for AI-assisted draft/revision/checklist steps
use Human Review Contract for recipient/content/approval/send-preparation checkpoints
use Idempotency Contract for apply operations
use Versioning Contract for workflow versioning
write preview tests
write apply tests
write duplicate apply tests
write tests that preview creates no Communication, approval, send-preparation or Tasks
write tests that AI draft does not approve or send
write tests that approval requires governed human/service review
write tests that send-preparation does not silently deliver externally
write tests that sent communication is immutable or revision-controlled
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
treat workflow contract as implementation code
create Communication outside Communication Service
approve or send Communication outside Communication Service
create tasks outside Task Service
emit events directly from workflow code
mutate linked Matter, Order, Customer, Provider or Partner outside owning service
skip Permission or Policy checks
allow AI to approve, send, bind, decide professional truth or complete tasks
hide human-review requirements
overwrite historical workflow versions silently
```

---

# 25. Acceptance Criteria

This Communication Review Workflow Contract is accepted only if:

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
| 0.1.0 | Draft | Initial Communication Review Workflow Contract. Defines governed communication context validation, recipient/channel validation, source/attachment validation, draft preparation, review, revision, approval, send-preparation, follow-up tasks, Permission/Policy context, Communication Agent boundary, human review, idempotency, events, errors, versioning and Codex implementation expectations. |

---

## Workflow Component Contract Consumption

State Definitions conform to [Workflow State Definition Contract](components/workflow-state-definition-contract.md). Transition Definitions conform to [Workflow Transition Definition Contract](components/workflow-transition-definition-contract.md). Workflow validation does not perform domain mutation; owning Services remain mutation authorities. This reference does not change MVP Depth, does not promote preview-only workflows, does not send Communication Review output, does not submit Trademark Applications, and does not add protected external action.

**End of Communication Review Workflow Contract**
