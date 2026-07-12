# Customer Intake Workflow Contract

**Spec ID:** B02-CONTRACT-WORKFLOW-CUSTOMER-INTAKE  
**Spec Type:** Workflow Contract Specification  
**Contract Name:** Customer Intake Workflow Contract  
**Contract File:** core-specs/contracts/workflows/customer-intake-workflow-contract.md  
**Contract Category:** Workflow  
**Related Workflow Contract Type:** CustomerIntakeWorkflow  
**Related Domains:** Customer; Opportunity; Matter; Order; Brand; Trademark; Document; Communication; Task; Event; Permission; Policy; Agent  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/opportunity.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/document.md; core-specs/objects/communication.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/customer-service.md; core-specs/services/opportunity-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/document-service.md; core-specs/services/communication-service.md; core-specs/services/task-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/customer-api.md; core-specs/api/opportunity-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/brand-api.md; core-specs/api/trademark-api.md; core-specs/api/document-api.md; core-specs/api/communication-api.md; core-specs/api/task-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/agent-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/customer-created.md; core-specs/events/opportunity-created.md; core-specs/events/matter-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/workflow-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Workflow Contract Version:** v0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Customer Intake Workflow Contract defines the governed execution pattern for receiving, structuring, validating and preparing a customer request before it becomes a qualified Opportunity, Matter, Order or follow-up Task.

It standardizes:

```text
customer inquiry trigger
customer identity/contact context
business request capture
brand/trademark/document intake
opportunity preparation
matter/order draft preparation boundary
communication draft preparation
task plan creation
human review checkpoints
permission and policy checks
AI assistance boundaries
idempotency behavior
safe error behavior
Codex implementation rules
```

This Workflow Contract does not approve customer engagement, create legal advice, guarantee order conversion, submit filings, select providers, send external communications, or replace Customer Service, Opportunity Service, Matter Service, Order Service, Communication Service or Task Service.

---

# 2. Core Lock

```text
Customer Intake Workflow coordinates governed intake.
Customer Service owns Customer behavior.
Opportunity Service owns Opportunity behavior.
Matter and Order Services own conversion behavior.
Task Service owns active Task creation.
Communication Service owns Communication behavior.
Permission and Policy govern every protected step.
AI may summarize, classify and draft, but must not approve engagement or create professional truth.
Events preserve trace.
```

---

# 3. Contract Meaning

This contract means:

```text
a reusable governed workflow pattern for converting customer request signals into structured intake records, safe drafts, task plans and review-ready business context.
```

This contract does not mean:

```text
customer contract approval
payment approval
legal advice
trademark availability opinion
order creation by itself
matter creation by itself
communication sending
provider selection
permission grant
policy approval
event emitter
UI intake form
```

---

# 4. Workflow Boundary

This Workflow Contract is responsible for:

```text
defining intake trigger
defining customer/request target context
defining intake workflow steps
defining required services
defining task plan shape
defining draft communication boundary
defining opportunity preparation boundary
defining matter/order conversion boundary
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
creating Customer outside Customer Service
creating Opportunity outside Opportunity Service
creating Matter outside Matter Service
creating Order outside Order Service
creating active Tasks outside Task Service
sending Communications outside Communication Service
deciding legal/professional truth
selecting providers
approving payment
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
ManualStaffEntry
WebsiteInquiry
PortalSubmission
WechatInquiry
EmailInquiry
ImportedLead
PartnerReferral
ExistingCustomerRequest
AgentPrepared
Unknown
```

Trigger rules:

```text
- Triggering customer intake is not customer engagement approval.
- Imported lead must be marked as imported source and may require review.
- Partner referral must validate Partner reference where provided.
- Agent-prepared intake must still pass Permission and Policy checks.
- Applying intake workflow requires idempotency_key.
```

---

# 6. Target Object Context

Customer Intake may target:

```text
Customer
Opportunity
Communication
ImportedRecord
UnknownLead
```

Canonical target shape:

```yaml
target_context:
  target_object_type: string
  target_object_reference_id: string | null
  target_object_status_at_start: string | null
  target_object_owner_service: string
  target_object_visibility: string | null
```

Rules:

```text
- Existing Customer reference must be validated by Customer Service.
- Existing Opportunity reference must be validated by Opportunity Service.
- Existing Communication reference must be validated by Communication Service.
- UnknownLead may be used before a Customer record exists, but conversion must route through Customer Service.
- Target status must be revalidated before conversion to Matter or Order.
```

---

# 7. Required Services

This workflow may require:

```text
Workflow Contract Service
Customer Service
Opportunity Service
Matter Service
Order Service
Brand Service
Trademark Service
Document Service
Communication Service
Task Service
Event Service
Permission Service
Policy Service
Agent Service
```

Service boundary rules:

```text
- Workflow Contract Service owns preview and apply behavior.
- Customer Service owns Customer creation/update.
- Opportunity Service owns Opportunity creation/update.
- Matter Service owns Matter creation/update.
- Order Service owns Order creation/update.
- Communication Service owns draft creation, review and send-preparation.
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
  customer_reference_id: string | null
  opportunity_reference_id: string | null
  matter_reference_id: string | null
  order_reference_id: string | null
  brand_reference_id: string | null
  trademark_reference_id: string | null
  communication_reference_id: string | null
  document_reference_ids:
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
intake source validity
customer/contact context availability
requested service category
brand/trademark context availability
document attachment availability where applicable
target object status
workflow contract status
required permissions
policy restrictions
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

Canonical customer intake steps:

```yaml
steps:
  - step_key: capture-intake-source
    step_title_safe: Capture Intake Source
    step_type: Intake
    step_required: true
    owning_service: Workflow Contract Service
    target_object_type: UnknownLead
    target_object_reference_id: null
    input_contract_refs:
      - core-specs/contracts/common/audit-context.md
    output_contract_refs:
      - core-specs/contracts/workflows/customer-intake-workflow-contract.md
    permission_keys:
      - workflow-contract:apply
    policy_scopes:
      - workflow-contract:apply:policy
    human_review_required: false
    ai_assistance_allowed: false
    events_expected:
      - WorkflowContractApplied
    failure_behavior: StopWorkflow

  - step_key: validate-or-create-customer
    step_title_safe: Validate or Create Customer
    step_type: Intake
    step_required: true
    owning_service: Customer Service
    target_object_type: Customer
    target_object_reference_id: customer_reference_id
    input_contract_refs:
      - core-specs/contracts/api/customer-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/customer-api-contract.md
    permission_keys:
      - customer:create
      - customer:update
      - customer:validate
    policy_scopes:
      - customer:create:policy
      - customer:update:policy
      - customer:reference:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected:
      - CustomerCreated
    failure_behavior: RequireReview

  - step_key: collect-brand-trademark-context
    step_title_safe: Collect Brand and Trademark Context
    step_type: Intake
    step_required: true
    owning_service: Brand Service
    target_object_type: Brand
    target_object_reference_id: brand_reference_id
    input_contract_refs:
      - core-specs/contracts/api/brand-api-contract.md
      - core-specs/contracts/api/trademark-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/brand-api-contract.md
      - core-specs/contracts/api/trademark-api-contract.md
    permission_keys:
      - brand:create
      - brand:update
      - trademark:create
      - trademark:update
    policy_scopes:
      - brand:create:policy
      - brand:update:policy
      - trademark:create:policy
      - trademark:update:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: attach-documents
    step_title_safe: Attach Intake Documents
    step_type: PrepareDocument
    step_required: false
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
    policy_scopes:
      - document:create:policy
      - document:update:policy
      - document:visibility:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: prepare-opportunity
    step_title_safe: Prepare Opportunity
    step_type: Review
    step_required: true
    owning_service: Opportunity Service
    target_object_type: Opportunity
    target_object_reference_id: opportunity_reference_id
    input_contract_refs:
      - core-specs/contracts/api/opportunity-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/opportunity-api-contract.md
    permission_keys:
      - opportunity:create
      - opportunity:update
      - opportunity:qualification:prepare
    policy_scopes:
      - opportunity:create:policy
      - opportunity:update:policy
      - opportunity:qualification:prepare:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected:
      - OpportunityCreated
    failure_behavior: RequireReview

  - step_key: prepare-intake-communication
    step_title_safe: Prepare Intake Communication
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

  - step_key: prepare-follow-up-tasks
    step_title_safe: Prepare Follow-up Tasks
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

  - step_key: prepare-conversion-draft
    step_title_safe: Prepare Matter or Order Conversion Draft
    step_type: InternalApproval
    step_required: false
    owning_service: Opportunity Service
    target_object_type: Opportunity
    target_object_reference_id: opportunity_reference_id
    input_contract_refs:
      - core-specs/contracts/api/opportunity-api-contract.md
      - core-specs/contracts/api/matter-api-contract.md
      - core-specs/contracts/api/order-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/opportunity-api-contract.md
    permission_keys:
      - opportunity:conversion:prepare
    policy_scopes:
      - opportunity:conversion:prepare:policy
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
    - task_type: IntakeTask
      task_title_safe: Review customer intake
      task_description_safe: Review customer request, identity, brand/trademark context and missing materials.
      target_object_type: Opportunity
      target_object_reference_id: opportunity_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-opportunity
      human_review_required: true

    - task_type: CustomerConfirmationTask
      task_title_safe: Confirm missing customer information
      task_description_safe: Confirm missing fields or documents with customer.
      target_object_type: Customer
      target_object_reference_id: customer_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-intake-communication
      human_review_required: false

    - task_type: InternalApprovalTask
      task_title_safe: Approve conversion to matter or order
      task_description_safe: Review whether intake is ready to convert to Matter or Order.
      target_object_type: Opportunity
      target_object_reference_id: opportunity_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-conversion-draft
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
CustomerCreated
OpportunityCreated
CommunicationCreated
TaskCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Events are emitted by owning services.
- Workflow Contract must not emit events directly.
- CustomerCreated may only be emitted by Customer Service.
- OpportunityCreated may only be emitted by Opportunity Service.
- CommunicationCreated may only be emitted by Communication Service.
- TaskCreated may only be emitted by Task Service.
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
customer:create
customer:update
customer:validate
brand:create
brand:update
trademark:create
trademark:update
document:create
document:update
opportunity:create
opportunity:update
opportunity:qualification:prepare
opportunity:conversion:prepare
communication:create
communication:draft:prepare
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
customer:create:policy
customer:update:policy
customer:reference:policy
brand:create:policy
brand:update:policy
trademark:create:policy
trademark:update:policy
document:create:policy
document:update:policy
document:visibility:policy
opportunity:create:policy
opportunity:update:policy
opportunity:qualification:prepare:policy
opportunity:conversion:prepare:policy
communication:create:policy
communication:draft:prepare:policy
task:create:policy
cross-organization:workflow
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may block, redact, downgrade or require human review.
- Customer contact, communication content, commercial terms and private notes may be redacted.
- Workflow output must disclose policy omissions where applicable.
- PolicyRestricted must stop protected action or return safe partial output.
```

---

# 16. AI Assistance Rules

Allowed AI roles:

```text
summarize customer request
extract missing intake fields
summarize brand/trademark context
suggest opportunity type
prepare intake checklist
prepare customer confirmation draft
prepare follow-up task plan
prepare conversion readiness summary
```

AI must not:

```text
approve customer engagement
create legal advice
decide trademark registrability
create Matter or Order by itself
send customer communication
complete tasks
select providers
approve payment
submit filing
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
  - checkpoint_key: review-intake-summary
    checkpoint_title_safe: Review Intake Summary
    required: true
    required_before_step_key: prepare-conversion-draft
    reviewer_role: IntakeReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: review-customer-communication
    checkpoint_title_safe: Review Customer Communication
    required: true
    required_before_step_key: prepare-intake-communication
    reviewer_role: CommunicationReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-conversion-draft
    checkpoint_title_safe: Approve Conversion Draft
    required: true
    required_before_step_key: prepare-conversion-draft
    reviewer_role: BusinessReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md
```

Rules:

```text
- Human Review records accountable professional/business review.
- Human Review does not create Matter or Order by itself.
- Matter and Order Services decide whether review satisfies conversion requirements.
- Human review must gate customer-facing communication and conversion readiness.
```

---

# 18. Idempotency Rules

Idempotency requirements:

```text
Preview:
  idempotency_key normally not required unless result is persisted.

Apply:
  idempotency_key required.

Customer creation:
  must be duplicate-safe.

Opportunity creation:
  must be duplicate-safe.

Task creation:
  must be duplicate-safe.

Communication creation:
  must be duplicate-safe.
```

Rules:

```text
- Duplicate apply must not duplicate Customer, Opportunity, Tasks, Communications or Events.
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
CustomerReferenceInvalid
OpportunityReferenceInvalid
BrandReferenceInvalid
TrademarkReferenceInvalid
DocumentReferenceInvalid
CommunicationReferenceInvalid
TaskCreationFailed
PermissionDenied
PolicyRestricted
HumanReviewRequired
StateInvalid
InsufficientIntakeContext
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
- Errors must not expose restricted customer data, private communication content, commercial terms, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 20. Versioning Rules

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

# 21. Preview Contract

Workflow preview request shape:

```yaml
preview_request:
  workflow_contract_reference_id: string
  target_context:
    target_object_type: Customer | Opportunity | Communication | ImportedRecord | UnknownLead
    target_object_reference_id: string | null
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
  intake_summary_safe: string | null
  missing_context_safe:
    - string
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Preview does not apply workflow.
- Preview does not create Customer, Opportunity, Matter, Order, Communication or active Tasks.
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
    target_object_type: Customer | Opportunity | Communication | ImportedRecord | UnknownLead
    target_object_reference_id: string | null
  apply_scope: string
  create_tasks: boolean
  create_customer_if_missing: boolean
  create_opportunity_if_missing: boolean
  prepare_communication_draft: boolean
  prepare_conversion_draft: boolean
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
  customer_reference_id: string | null
  opportunity_reference_id: string | null
  created_task_reference_ids:
    - string
  communication_reference_id: string | null
  conversion_draft_status: string | null
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
- Customer creation must route through Customer Service.
- Opportunity creation must route through Opportunity Service.
- Active Task creation must route through Task Service.
- Communication draft creation must route through Communication Service.
- Matter or Order creation must not happen in this workflow unless explicitly routed through Matter/Order Service and review gates are satisfied.
```

---

# 23. Controlled Values

## 23.1 apply_scope

```text
PreviewOnly
CreateCustomer
CreateOpportunity
CreateCustomerAndOpportunity
PrepareTasks
PrepareCommunication
PrepareConversionDraft
FullIntakeApply
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

## 23.4 intake_source_type

```text
ManualStaffEntry
WebsiteInquiry
PortalSubmission
WechatInquiry
EmailInquiry
ImportedLead
PartnerReferral
ExistingCustomerRequest
AgentPrepared
Unknown
```

## 23.5 intake_service_category

```text
TrademarkApplication
TrademarkSearch
OfficeActionResponse
Renewal
Assignment
ChangeRecordal
Opposition
PortfolioManagement
Consultation
Other
Unknown
```

---

# 24. Codex Implementation Notes

Codex must:

```text
cite this Customer Intake Workflow Contract
cite Workflow Contracts README
cite Workflow Contract API Contract
cite Workflow Contract Service Spec
cite Customer API and Customer Service
cite Opportunity API and Opportunity Service
cite Matter API and Matter Service where conversion draft is used
cite Order API and Order Service where conversion draft is used
cite Communication API and Communication Service
cite Task API and Task Service
cite Document API and Document Service
cite Event API and Event Service
use Reference Contract for all references
use Error Contract for errors
use Permission Context Contract before protected steps
use Policy Context Contract before policy-controlled steps
use AI Context Contract for AI-assisted steps
use Human Review Contract for communication/conversion checkpoints
use Idempotency Contract for apply operations
use Versioning Contract for workflow versioning
write preview tests
write apply tests
write duplicate apply tests
write tests that preview creates no Customer, Opportunity, Communication or Tasks
write tests that apply does not duplicate Customer/Opportunity/Tasks/Communication
write tests that AI cannot approve engagement or create professional truth
write tests that human review gates communication and conversion draft use
write tests that Matter/Order are not created unless explicitly routed through owning services
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
treat workflow contract as implementation code
create Customer outside Customer Service
create Opportunity outside Opportunity Service
create Matter or Order from workflow directly
create tasks outside Task Service
send communication outside Communication Service
emit events directly from workflow code
mutate target object outside owning service
skip Permission or Policy checks
allow AI to approve engagement, create legal advice, send communications or convert orders
hide human-review requirements
overwrite historical workflow versions silently
```

---

# 25. Acceptance Criteria

This Customer Intake Workflow Contract is accepted only if:

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
| 0.1.0 | Draft | Initial Customer Intake Workflow Contract. Defines governed customer request intake, customer/opportunity preparation, brand/trademark/document context, communication draft boundary, follow-up task plan, conversion draft boundary, Permission/Policy context, AI and human review rules, idempotency, events, errors, versioning and Codex implementation expectations. |

---

**End of Customer Intake Workflow Contract**


## PUB-TASK-B02-003 Component Contract References

State definitions conform to `components/workflow-state-definition-contract.md` (`B02-CONTRACT-WORKFLOW-STATE-DEFINITION`). Transition definitions conform to `components/workflow-transition-definition-contract.md` (`B02-CONTRACT-WORKFLOW-TRANSITION-DEFINITION`). Workflow Contract validates and routes only; it does not perform target object mutation or authorize protected external action.
