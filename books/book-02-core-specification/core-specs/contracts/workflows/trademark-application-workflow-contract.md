# Trademark Application Workflow Contract

**Spec ID:** B02-CONTRACT-WORKFLOW-TRADEMARK-APPLICATION  
**Spec Type:** Workflow Contract Specification  
**Contract Name:** Trademark Application Workflow Contract  
**Contract File:** core-specs/contracts/workflows/trademark-application-workflow-contract.md  
**Contract Category:** Workflow  
**Related Workflow Contract Type:** TrademarkApplicationWorkflow  
**Related Domains:** Trademark; Brand; Jurisdiction; Classification; Document; Evidence; Customer; Matter; Order; Task; Communication; Event; Permission; Policy; Agent  
**Related Object Specs:** core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/task.md; core-specs/objects/communication.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/classification-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/task-service.md; core-specs/services/communication-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/trademark-api.md; core-specs/api/brand-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/classification-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/customer-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/task-api.md; core-specs/api/communication-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/agent-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/trademark-created.md; core-specs/events/matter-created.md; core-specs/events/order-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/workflow-agent.md; core-specs/agents/knowledge-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
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

Trademark Application Workflow Contract defines the governed execution pattern for preparing, reviewing and coordinating a trademark application matter from structured intake to filing-ready execution context.

It standardizes:

```text
application workflow trigger
customer / matter / order context
brand and trademark context
jurisdiction context
classification and goods/services context
document and evidence preparation
application checklist preparation
task plan creation
communication draft preparation
human review checkpoints
permission and policy checks
AI assistance boundaries
idempotency behavior
safe error behavior
Codex implementation rules
```

This Workflow Contract does not submit official trademark applications by itself, approve legal filing strategy, guarantee registrability, select providers, approve payment, send external communications, or replace Trademark Service, Classification Service, Document Service, Matter Service, Order Service, Communication Service or Task Service.

---

# 2. Core Lock

```text
Trademark Application Workflow coordinates governed application preparation.
Trademark Service owns Trademark behavior.
Brand, Jurisdiction, Classification, Document and Evidence Services own their domain facts.
Matter and Order Services own business execution context.
Task Service owns active Task creation.
Communication Service owns Communication behavior.
Permission and Policy govern every protected step.
AI may suggest, summarize and draft, but must not decide registrability, filing strategy or professional truth.
Events preserve trace.
```

---

# 3. Contract Meaning

This contract means:

```text
a reusable governed workflow pattern for preparing trademark application execution in MarkOrbit.
```

This contract does not mean:

```text
official filing submission
registrability opinion
legal advice approval
classification final approval
customer instruction approval
payment approval
provider selection
communication sending
task completion
permission grant
policy approval
event emitter
filing form UI
```

---

# 4. Workflow Boundary

This Workflow Contract is responsible for:

```text
defining application workflow trigger
defining application target context
defining application workflow steps
defining required services
defining task plan shape
defining document/evidence preparation boundary
defining classification preparation boundary
defining communication preparation boundary
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
official office submission
provider selection
payment approval
legal conclusion approval
classification final approval outside professional review
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
CustomerIntakeConverted
MatterCreated
OrderCreated
ManualStaffEntry
PortalApplicationRequest
ImportedApplicationRecord
PartnerReferral
AgentPrepared
Unknown
```

Trigger rules:

```text
- Triggering trademark application workflow is not filing approval.
- Matter or Order reference must be validated where provided.
- Customer instruction context must be visible and policy-allowed before customer-facing output.
- Agent-prepared trigger must still pass Permission and Policy checks.
- Applying workflow requires idempotency_key.
```

---

# 6. Target Object Context

Trademark Application Workflow may target:

```text
Matter
Order
Trademark
Customer
Opportunity
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
- Matter reference must be validated by Matter Service where target is Matter.
- Order reference must be validated by Order Service where target is Order.
- Trademark reference must be validated by Trademark Service where target is Trademark.
- Target status must be revalidated before protected transitions.
- Workflow applicability must be evaluated before task creation.
```

---

# 7. Required Services

This workflow may require:

```text
Workflow Contract Service
Customer Service
Matter Service
Order Service
Brand Service
Trademark Service
Jurisdiction Service
Classification Service
Document Service
Evidence Service
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
- Trademark Service owns Trademark creation/update.
- Brand Service owns Brand reference and brand context.
- Jurisdiction Service owns jurisdiction rules/reference context.
- Classification Service owns classification suggestion/validation behavior.
- Document Service owns document creation/linkage.
- Evidence Service owns evidence linkage and sufficiency preparation.
- Matter and Order Services own business execution state.
- Task Service owns active Task creation.
- Communication Service owns draft creation, review and send-preparation.
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
  matter_reference_id: string | null
  order_reference_id: string | null
  brand_reference_id: string | null
  trademark_reference_id: string | null
  jurisdiction_reference_id: string | null
  classification_reference_ids:
    - string
  document_reference_ids:
    - string
  evidence_reference_ids:
    - string
  communication_reference_id: string | null
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
target object type and status
customer instruction availability
brand/trademark context availability
jurisdiction context availability
classification context availability
required document status
required evidence status where applicable
matter/order execution readiness
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

Canonical trademark application steps:

```yaml
steps:
  - step_key: validate-business-context
    step_title_safe: Validate Business Context
    step_type: Review
    step_required: true
    owning_service: Matter Service
    target_object_type: Matter
    target_object_reference_id: matter_reference_id
    input_contract_refs:
      - core-specs/contracts/api/matter-api-contract.md
      - core-specs/contracts/api/order-api-contract.md
    output_contract_refs:
      - core-specs/contracts/workflows/trademark-application-workflow-contract.md
    permission_keys:
      - matter:read
      - order:read
    policy_scopes:
      - matter:read:policy
      - order:read:policy
    human_review_required: false
    ai_assistance_allowed: false
    events_expected:
      - WorkflowContractApplied
    failure_behavior: StopWorkflow

  - step_key: validate-customer-instruction
    step_title_safe: Validate Customer Instruction
    step_type: CustomerConfirmation
    step_required: true
    owning_service: Customer Service
    target_object_type: Customer
    target_object_reference_id: customer_reference_id
    input_contract_refs:
      - core-specs/contracts/api/customer-api-contract.md
      - core-specs/contracts/api/document-api-contract.md
    output_contract_refs:
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - customer:read
      - document:read
    policy_scopes:
      - customer:read:policy
      - document:visibility:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: prepare-brand-context
    step_title_safe: Prepare Brand Context
    step_type: Intake
    step_required: true
    owning_service: Brand Service
    target_object_type: Brand
    target_object_reference_id: brand_reference_id
    input_contract_refs:
      - core-specs/contracts/api/brand-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/brand-api-contract.md
    permission_keys:
      - brand:read
      - brand:update
    policy_scopes:
      - brand:read:policy
      - brand:update:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: prepare-trademark-record
    step_title_safe: Prepare Trademark Record
    step_type: FilingPreparation
    step_required: true
    owning_service: Trademark Service
    target_object_type: Trademark
    target_object_reference_id: trademark_reference_id
    input_contract_refs:
      - core-specs/contracts/api/trademark-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/trademark-api-contract.md
    permission_keys:
      - trademark:create
      - trademark:update
      - trademark:validate
    policy_scopes:
      - trademark:create:policy
      - trademark:update:policy
      - trademark:reference:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected:
      - TrademarkCreated
    failure_behavior: RequireReview

  - step_key: validate-jurisdiction-context
    step_title_safe: Validate Jurisdiction Context
    step_type: Review
    step_required: true
    owning_service: Jurisdiction Service
    target_object_type: Jurisdiction
    target_object_reference_id: jurisdiction_reference_id
    input_contract_refs:
      - core-specs/contracts/api/jurisdiction-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/jurisdiction-api-contract.md
    permission_keys:
      - jurisdiction:read
      - jurisdiction:validate
    policy_scopes:
      - jurisdiction:read:policy
      - jurisdiction:reference:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: StopWorkflow

  - step_key: prepare-classification
    step_title_safe: Prepare Classification and Goods Services
    step_type: Review
    step_required: true
    owning_service: Classification Service
    target_object_type: Classification
    target_object_reference_id: classification_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/classification-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/classification-api-contract.md
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - classification:read
      - classification:update
      - classification:suggestion:prepare
    policy_scopes:
      - classification:read:policy
      - classification:update:policy
      - classification:suggestion:prepare:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: prepare-application-documents
    step_title_safe: Prepare Application Documents
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

  - step_key: prepare-evidence-context
    step_title_safe: Prepare Evidence Context
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

  - step_key: prepare-application-communication
    step_title_safe: Prepare Application Communication
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

  - step_key: create-application-tasks
    step_title_safe: Create Application Tasks
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

  - step_key: review-filing-readiness
    step_title_safe: Review Filing Readiness
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
    - task_type: ReviewTask
      task_title_safe: Review trademark application context
      task_description_safe: Review customer instruction, mark information, jurisdiction and service scope.
      target_object_type: Matter
      target_object_reference_id: matter_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: validate-customer-instruction
      human_review_required: true

    - task_type: ClassificationTask
      task_title_safe: Review classification and goods services
      task_description_safe: Review proposed classes and goods/services before application preparation.
      target_object_type: Trademark
      target_object_reference_id: trademark_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-classification
      human_review_required: true

    - task_type: DocumentPreparationTask
      task_title_safe: Prepare application documents
      task_description_safe: Prepare application form, POA or required filing documents.
      target_object_type: Document
      target_object_reference_id: null
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-application-documents
      human_review_required: true

    - task_type: InternalApprovalTask
      task_title_safe: Confirm filing readiness
      task_description_safe: Confirm application package is ready for governed filing process.
      target_object_type: Matter
      target_object_reference_id: matter_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: review-filing-readiness
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
TrademarkCreated
MatterCreated
OrderCreated
CommunicationCreated
TaskCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Events are emitted by owning services.
- Workflow Contract must not emit events directly.
- TrademarkCreated may only be emitted by Trademark Service.
- MatterCreated may only be emitted by Matter Service.
- OrderCreated may only be emitted by Order Service.
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
customer:read
matter:read
matter:update
order:read
brand:read
brand:update
trademark:create
trademark:update
trademark:validate
jurisdiction:read
jurisdiction:validate
classification:read
classification:update
classification:suggestion:prepare
document:create
document:update
document:read
evidence:create
evidence:update
evidence:read
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
customer:read:policy
matter:read:policy
matter:update:policy
order:read:policy
brand:read:policy
brand:update:policy
trademark:create:policy
trademark:update:policy
trademark:reference:policy
jurisdiction:read:policy
jurisdiction:reference:policy
classification:read:policy
classification:update:policy
classification:suggestion:prepare:policy
document:create:policy
document:update:policy
document:visibility:policy
evidence:create:policy
evidence:update:policy
evidence:visibility:policy
communication:create:policy
communication:draft:prepare:policy
task:create:policy
cross-organization:workflow
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may block, redact, downgrade or require human review.
- Customer instruction, communication content, filing documents and evidence may be redacted.
- Workflow output must disclose policy omissions where applicable.
- PolicyRestricted must stop protected action or return safe partial output.
```

---

# 16. AI Assistance Rules

Allowed AI roles:

```text
summarize customer filing request
identify missing application information
suggest classification candidates
summarize jurisdiction requirements from governed knowledge
prepare document checklist
prepare customer confirmation draft
prepare filing readiness checklist
prepare follow-up task plan
```

AI must not:

```text
decide trademark registrability
approve classification final wording
approve filing strategy
submit official filing
send customer/provider communication
complete tasks
select providers
approve payment
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
  - checkpoint_key: review-customer-instruction
    checkpoint_title_safe: Review Customer Filing Instruction
    required: true
    required_before_step_key: prepare-trademark-record
    reviewer_role: IntakeReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-classification
    checkpoint_title_safe: Approve Classification and Goods Services
    required: true
    required_before_step_key: review-filing-readiness
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-application-documents
    checkpoint_title_safe: Approve Application Documents
    required: true
    required_before_step_key: review-filing-readiness
    reviewer_role: FilingReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-customer-communication
    checkpoint_title_safe: Approve Customer Communication
    required: true
    required_before_step_key: prepare-application-communication
    reviewer_role: CommunicationReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-filing-readiness
    checkpoint_title_safe: Approve Filing Readiness
    required: true
    required_before_step_key: review-filing-readiness
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md
```

Rules:

```text
- Human Review records accountable professional/business review.
- Human Review does not submit filing by itself.
- Matter, Order and downstream filing services decide whether review satisfies execution requirements.
- Human review must gate classification, application documents, customer-facing communication and filing readiness.
```

---

# 18. Idempotency Rules

Idempotency requirements:

```text
Preview:
  idempotency_key normally not required unless result is persisted.

Apply:
  idempotency_key required.

Trademark creation:
  must be duplicate-safe.

Task creation:
  must be duplicate-safe.

Communication creation:
  must be duplicate-safe.

Document creation:
  must be duplicate-safe where generated from workflow.
```

Rules:

```text
- Duplicate apply must not duplicate Trademark, Documents, Tasks, Communications or Events.
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
MatterReferenceInvalid
OrderReferenceInvalid
BrandReferenceInvalid
TrademarkReferenceInvalid
JurisdictionReferenceInvalid
ClassificationReferenceInvalid
DocumentReferenceInvalid
EvidenceReferenceInvalid
CommunicationReferenceInvalid
TaskCreationFailed
PermissionDenied
PolicyRestricted
HumanReviewRequired
StateInvalid
InsufficientApplicationContext
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
- Errors must not expose restricted customer data, filing documents, evidence, private notes, policy internals or permission internals.
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
    target_object_type: Matter | Order | Trademark | Customer | Opportunity
    target_object_reference_id: string
  include_task_plan: boolean
  include_ai_summary: boolean
  include_document_checklist: boolean
  include_classification_summary: boolean
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
  application_readiness_summary_safe: string | null
  classification_summary_safe: string | null
  document_checklist_safe:
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
- Preview does not create Trademark, Documents, Communications or active Tasks.
- Preview does not submit filing.
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
    target_object_type: Matter | Order | Trademark | Customer | Opportunity
    target_object_reference_id: string
  apply_scope: string
  create_tasks: boolean
  create_trademark_if_missing: boolean
  prepare_documents: boolean
  prepare_communication_draft: boolean
  prepare_filing_readiness_review: boolean
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
  trademark_reference_id: string | null
  classification_reference_ids:
    - string
  document_reference_ids:
    - string
  evidence_reference_ids:
    - string
  communication_reference_id: string | null
  created_task_reference_ids:
    - string
  filing_readiness_status: string | null
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
- Trademark creation/update must route through Trademark Service.
- Classification preparation must route through Classification Service.
- Document preparation must route through Document Service.
- Active Task creation must route through Task Service.
- Communication draft creation must route through Communication Service.
- Official filing submission must not happen in this workflow contract.
```

---

# 23. Controlled Values

## 23.1 apply_scope

```text
PreviewOnly
PrepareApplicationContext
PrepareTrademarkRecord
PrepareClassification
PrepareDocuments
PrepareTasks
PrepareCommunication
PrepareFilingReadiness
FullApplicationPreparation
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

## 23.4 application_service_category

```text
NewTrademarkApplication
AdditionalClassApplication
SeriesApplication
LogoApplication
WordMarkApplication
CombinedMarkApplication
NationalApplication
MadridDesignation
Other
Unknown
```

## 23.5 filing_readiness_status

```text
NotReady
PartiallyReady
ReadyForProfessionalReview
ReadyForFilingProcess
PolicyRestricted
RequiresHumanReview
Unknown
```

---

# 24. Codex Implementation Notes

Codex must:

```text
cite this Trademark Application Workflow Contract
cite Workflow Contracts README
cite Workflow Contract API Contract
cite Workflow Contract Service Spec
cite Trademark API and Trademark Service
cite Brand API and Brand Service
cite Jurisdiction API and Jurisdiction Service
cite Classification API and Classification Service
cite Document API and Document Service
cite Evidence API and Evidence Service
cite Customer API and Customer Service
cite Matter API and Matter Service
cite Order API and Order Service
cite Communication API and Communication Service
cite Task API and Task Service
cite Event API and Event Service
use Reference Contract for all references
use Error Contract for errors
use Permission Context Contract before protected steps
use Policy Context Contract before policy-controlled steps
use AI Context Contract for AI-assisted steps
use Human Review Contract for classification/document/communication/filing-readiness checkpoints
use Idempotency Contract for apply operations
use Versioning Contract for workflow versioning
write preview tests
write apply tests
write duplicate apply tests
write tests that preview creates no Trademark, Document, Communication or Tasks
write tests that apply does not duplicate Trademark/Documents/Tasks/Communication
write tests that AI cannot decide registrability or approve filing strategy
write tests that human review gates classification, documents, communication and filing readiness
write tests that official filing is not submitted by this workflow
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
treat workflow contract as implementation code
create Trademark outside Trademark Service
create Classification outside Classification Service
create Documents outside Document Service
create tasks outside Task Service
send communication outside Communication Service
submit official trademark application from this workflow
emit events directly from workflow code
mutate target object outside owning service
skip Permission or Policy checks
allow AI to decide registrability, approve filing strategy, submit filings or create legal advice
hide human-review requirements
overwrite historical workflow versions silently
```

---

# 25. Acceptance Criteria

This Trademark Application Workflow Contract is accepted only if:

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
| 0.1.0 | Draft | Initial Trademark Application Workflow Contract. Defines governed application preparation, business context validation, trademark/brand/jurisdiction/classification/document/evidence preparation, communication draft boundary, task plan, filing readiness review, Permission/Policy context, AI and human review rules, idempotency, events, errors, versioning and Codex implementation expectations. |

---

**End of Trademark Application Workflow Contract**


## PUB-TASK-B02-003 Component Contract References

State definitions conform to `components/workflow-state-definition-contract.md` (`B02-CONTRACT-WORKFLOW-STATE-DEFINITION`). Transition definitions conform to `components/workflow-transition-definition-contract.md` (`B02-CONTRACT-WORKFLOW-TRANSITION-DEFINITION`). Workflow Contract validates and routes only; it does not perform target object mutation or authorize protected external action.
