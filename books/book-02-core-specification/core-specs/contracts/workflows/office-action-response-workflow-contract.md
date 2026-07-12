# Office Action Response Workflow Contract

**Spec ID:** B02-CONTRACT-WORKFLOW-OFFICE-ACTION-RESPONSE  
**Spec Type:** Workflow Contract Specification  
**Contract Name:** Office Action Response Workflow Contract  
**Contract File:** core-specs/contracts/workflows/office-action-response-workflow-contract.md  
**Contract Category:** Workflow  
**Related Workflow Contract Type:** OfficeActionResponseWorkflow  
**Related Domains:** Trademark; Jurisdiction; Classification; Document; Evidence; Customer; Matter; Order; Task; Communication; Knowledge; Event; Permission; Policy; Agent  
**Related Object Specs:** core-specs/objects/trademark.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/task.md; core-specs/objects/communication.md; core-specs/objects/knowledge.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/trademark-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/classification-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/task-service.md; core-specs/services/communication-service.md; core-specs/services/knowledge-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/trademark-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/classification-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/customer-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/task-api.md; core-specs/api/communication-api.md; core-specs/api/knowledge-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/agent-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
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

Office Action Response Workflow Contract defines the governed execution pattern for receiving, analyzing, preparing, reviewing and coordinating a response to an official trademark office action or examination notice.

It standardizes:

```text
office action workflow trigger
official document and deadline context
trademark / matter / order context
jurisdiction and legal-ground context
classification amendment context
evidence preparation context
response strategy preparation
customer confirmation communication
task plan creation
human review checkpoints
permission and policy checks
AI assistance boundaries
idempotency behavior
safe error behavior
Codex implementation rules
```

This Workflow Contract does not submit an official response by itself, decide legal strategy, guarantee acceptance, approve amendments, send external communications, select providers, approve payment, or replace Trademark Service, Document Service, Evidence Service, Communication Service, Matter Service, Order Service or Task Service.

---

# 2. Core Lock

```text
Office Action Response Workflow coordinates governed response preparation.
Trademark Service owns Trademark behavior.
Document and Evidence Services own official-document and evidence records.
Knowledge Service may provide source-grounded reference, not professional truth.
Matter and Order Services own business execution context.
Task Service owns active Task creation.
Communication Service owns Communication behavior.
Permission and Policy govern every protected step.
AI may summarize, classify and draft, but must not decide legal strategy or submit responses.
Events preserve trace.
```

---

# 3. Contract Meaning

This contract means:

```text
a reusable governed workflow pattern for preparing office action response execution in MarkOrbit.
```

This contract does not mean:

```text
official response submission
legal opinion approval
office action final judgment
amendment approval
customer instruction approval
payment approval
provider selection
communication sending
task completion
permission grant
policy approval
event emitter
official filing portal
```

---

# 4. Workflow Boundary

This Workflow Contract is responsible for:

```text
defining office action workflow trigger
defining target trademark/matter/order context
defining official document intake and deadline context
defining response workflow steps
defining required services
defining task plan shape
defining evidence/document preparation boundary
defining communication preparation boundary
defining response strategy preparation boundary
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
legal conclusion approval
customer instruction approval
provider selection
payment approval
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
OfficialDocumentReceived
StatusMonitorDetected
ManualStaffEntry
CustomerUploadedNotice
AgentUploadedNotice
PartnerForwardedNotice
ImportedOfficeActionRecord
WorkflowContinuation
AgentPrepared
Unknown
```

Trigger rules:

```text
- Triggering response workflow is not response approval.
- Official document reference must be validated by Document Service where provided.
- Trademark and Matter references must be validated where provided.
- Deadline context must be treated as high-risk and review-sensitive.
- Agent-prepared trigger must still pass Permission and Policy checks.
- Applying workflow requires idempotency_key.
```

---

# 6. Target Object Context

Office Action Response Workflow may target:

```text
Trademark
Matter
Order
Document
Communication
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
- Matter reference must be validated by Matter Service where provided.
- Order reference must be validated by Order Service where provided.
- Official document reference must be validated by Document Service.
- Target status and deadline context must be revalidated before protected transitions.
```

---

# 7. Required Services

This workflow may require:

```text
Workflow Contract Service
Trademark Service
Jurisdiction Service
Classification Service
Document Service
Evidence Service
Customer Service
Matter Service
Order Service
Communication Service
Task Service
Knowledge Service
Event Service
Permission Service
Policy Service
Agent Service
```

Service boundary rules:

```text
- Workflow Contract Service owns preview and apply behavior.
- Trademark Service owns Trademark state and official status context.
- Document Service owns office action document and response document records.
- Evidence Service owns evidence linkage and sufficiency preparation.
- Knowledge Service provides governed source-grounded references.
- Classification Service owns goods/services amendment preparation.
- Matter and Order Services own business execution state.
- Communication Service owns customer/provider communication drafts and send-preparation.
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
  matter_reference_id: string | null
  order_reference_id: string | null
  trademark_reference_id: string
  jurisdiction_reference_id: string | null
  official_document_reference_id: string | null
  response_document_reference_ids:
    - string
  evidence_reference_ids:
    - string
  classification_reference_ids:
    - string
  communication_reference_id: string | null
  task_reference_ids:
    - string
  knowledge_reference_ids:
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
official document availability
deadline availability and urgency
trademark status context
jurisdiction context
office action issue type
response scope
customer instruction status
required document/evidence availability
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
  deadline_risk_level: string | null
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
```

Controlled applicability status:

```text
Applicable
NotApplicable
InsufficientContext
DeadlineMissing
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

Canonical office action response steps:

```yaml
steps:
  - step_key: validate-response-context
    step_title_safe: Validate Response Context
    step_type: Review
    step_required: true
    owning_service: Matter Service
    target_object_type: Matter
    target_object_reference_id: matter_reference_id
    input_contract_refs:
      - core-specs/contracts/api/matter-api-contract.md
      - core-specs/contracts/api/order-api-contract.md
      - core-specs/contracts/api/trademark-api-contract.md
    output_contract_refs:
      - core-specs/contracts/workflows/office-action-response-workflow-contract.md
    permission_keys:
      - matter:read
      - order:read
      - trademark:read
    policy_scopes:
      - matter:read:policy
      - order:read:policy
      - trademark:read:policy
    human_review_required: false
    ai_assistance_allowed: false
    events_expected:
      - WorkflowContractApplied
    failure_behavior: StopWorkflow

  - step_key: ingest-official-document
    step_title_safe: Ingest Official Office Action Document
    step_type: PrepareDocument
    step_required: true
    owning_service: Document Service
    target_object_type: Document
    target_object_reference_id: official_document_reference_id
    input_contract_refs:
      - core-specs/contracts/api/document-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/document-api-contract.md
    permission_keys:
      - document:create
      - document:read
      - document:update
    policy_scopes:
      - document:create:policy
      - document:visibility:policy
      - document:update:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: extract-deadline-and-issues
    step_title_safe: Extract Deadline and Issues
    step_type: Review
    step_required: true
    owning_service: Trademark Service
    target_object_type: Trademark
    target_object_reference_id: trademark_reference_id
    input_contract_refs:
      - core-specs/contracts/api/trademark-api-contract.md
      - core-specs/contracts/api/document-api-contract.md
    output_contract_refs:
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - trademark:update
      - document:read
    policy_scopes:
      - trademark:update:policy
      - document:visibility:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: retrieve-jurisdiction-knowledge
    step_title_safe: Retrieve Jurisdiction Knowledge
    step_type: Review
    step_required: true
    owning_service: Knowledge Service
    target_object_type: Knowledge
    target_object_reference_id: knowledge_reference_ids
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

  - step_key: prepare-response-strategy
    step_title_safe: Prepare Response Strategy
    step_type: InternalApproval
    step_required: true
    owning_service: Matter Service
    target_object_type: Matter
    target_object_reference_id: matter_reference_id
    input_contract_refs:
      - core-specs/contracts/api/matter-api-contract.md
      - core-specs/contracts/api/trademark-api-contract.md
      - core-specs/contracts/api/knowledge-api-contract.md
    output_contract_refs:
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - matter:update
      - trademark:read
      - knowledge:read
    policy_scopes:
      - matter:update:policy
      - trademark:read:policy
      - knowledge:read:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: prepare-classification-amendment
    step_title_safe: Prepare Classification Amendment
    step_type: Review
    step_required: false
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
    failure_behavior: SafePartial

  - step_key: prepare-evidence-package
    step_title_safe: Prepare Evidence Package
    step_type: CollectEvidence
    step_required: false
    owning_service: Evidence Service
    target_object_type: Evidence
    target_object_reference_id: evidence_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/evidence-api-contract.md
      - core-specs/contracts/api/document-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/evidence-api-contract.md
    permission_keys:
      - evidence:create
      - evidence:update
      - evidence:read
      - document:read
    policy_scopes:
      - evidence:create:policy
      - evidence:update:policy
      - evidence:visibility:policy
      - document:visibility:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: prepare-response-documents
    step_title_safe: Prepare Response Documents
    step_type: PrepareDocument
    step_required: true
    owning_service: Document Service
    target_object_type: Document
    target_object_reference_id: response_document_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/document-api-contract.md
      - core-specs/contracts/api/evidence-api-contract.md
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

  - step_key: prepare-customer-confirmation
    step_title_safe: Prepare Customer Confirmation
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

  - step_key: create-response-tasks
    step_title_safe: Create Response Tasks
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

  - step_key: review-response-readiness
    step_title_safe: Review Response Readiness
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
      task_title_safe: Review office action document
      task_description_safe: Review official document, deadline, issue type and required response scope.
      target_object_type: Document
      target_object_reference_id: official_document_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: ingest-official-document
      human_review_required: true

    - task_type: EvidenceCollectionTask
      task_title_safe: Collect response evidence
      task_description_safe: Collect evidence required for response if applicable.
      target_object_type: Evidence
      target_object_reference_id: null
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-evidence-package
      human_review_required: true

    - task_type: DocumentPreparationTask
      task_title_safe: Prepare office action response document
      task_description_safe: Prepare response draft and supporting documents for review.
      target_object_type: Document
      target_object_reference_id: null
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-response-documents
      human_review_required: true

    - task_type: CustomerConfirmationTask
      task_title_safe: Confirm response instructions with customer
      task_description_safe: Confirm customer consent, amendments or evidence before response execution.
      target_object_type: Communication
      target_object_reference_id: communication_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-customer-confirmation
      human_review_required: true

    - task_type: InternalApprovalTask
      task_title_safe: Approve response readiness
      task_description_safe: Review whether response package is ready for governed submission process.
      target_object_type: Matter
      target_object_reference_id: matter_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: review-response-readiness
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
- TaskCreated may only be emitted by Task Service.
- Official response submission events are outside this workflow unless a governed filing/submission service exists.
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
trademark:read
trademark:update
jurisdiction:read
knowledge:read
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
trademark:read:policy
trademark:update:policy
jurisdiction:read:policy
knowledge:read:policy
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
- Official documents, customer communications, response drafts, evidence and private strategy notes may be redacted.
- Workflow output must disclose policy omissions where applicable.
- PolicyRestricted must stop protected action or return safe partial output.
```

---

# 16. AI Assistance Rules

Allowed AI roles:

```text
summarize official document
extract deadline candidates
identify issue categories
retrieve jurisdiction reference material
summarize visible knowledge sources
suggest response checklist
suggest classification amendment candidates
summarize evidence gaps
prepare response document outline
prepare customer confirmation draft
prepare follow-up task plan
```

AI must not:

```text
decide legal strategy
approve response arguments
approve goods/services amendment final wording
certify deadline accuracy without review
submit official response
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
  - checkpoint_key: review-official-document
    checkpoint_title_safe: Review Official Office Action Document
    required: true
    required_before_step_key: extract-deadline-and-issues
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: confirm-deadline-and-issues
    checkpoint_title_safe: Confirm Deadline and Issues
    required: true
    required_before_step_key: prepare-response-strategy
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-response-strategy
    checkpoint_title_safe: Approve Response Strategy
    required: true
    required_before_step_key: prepare-response-documents
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-classification-amendment
    checkpoint_title_safe: Approve Classification Amendment
    required: true
    required_before_step_key: prepare-response-documents
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-response-documents
    checkpoint_title_safe: Approve Response Documents
    required: true
    required_before_step_key: review-response-readiness
    reviewer_role: FilingReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-customer-confirmation
    checkpoint_title_safe: Approve Customer Confirmation
    required: true
    required_before_step_key: prepare-customer-confirmation
    reviewer_role: CommunicationReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-response-readiness
    checkpoint_title_safe: Approve Response Readiness
    required: true
    required_before_step_key: review-response-readiness
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md
```

Rules:

```text
- Human Review records accountable professional/business review.
- Human Review does not submit response by itself.
- Matter, Order and downstream filing/submission services decide whether review satisfies execution requirements.
- Human review must gate deadline confirmation, legal strategy, response documents, customer communication and response readiness.
```

---

# 18. Idempotency Rules

Idempotency requirements:

```text
Preview:
  idempotency_key normally not required unless result is persisted.

Apply:
  idempotency_key required.

Document creation:
  must be duplicate-safe.

Evidence linkage:
  must be duplicate-safe.

Task creation:
  must be duplicate-safe.

Communication creation:
  must be duplicate-safe.
```

Rules:

```text
- Duplicate apply must not duplicate Documents, Evidence links, Tasks, Communications or Events.
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
TrademarkReferenceInvalid
JurisdictionReferenceInvalid
KnowledgeReferenceInvalid
OfficialDocumentReferenceInvalid
ClassificationReferenceInvalid
EvidenceReferenceInvalid
ResponseDocumentReferenceInvalid
CommunicationReferenceInvalid
TaskCreationFailed
DeadlineMissing
DeadlineExpired
PermissionDenied
PolicyRestricted
HumanReviewRequired
StateInvalid
InsufficientResponseContext
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
- Errors must not expose restricted customer data, official documents, response drafts, evidence, legal strategy notes, policy internals or permission internals.
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
    target_object_type: Trademark | Matter | Order | Document | Communication
    target_object_reference_id: string
  include_task_plan: boolean
  include_ai_summary: boolean
  include_deadline_summary: boolean
  include_response_checklist: boolean
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
  office_action_summary_safe: string | null
  deadline_summary_safe: string | null
  response_checklist_safe:
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
- Preview does not create Documents, Evidence, Communications or active Tasks.
- Preview does not submit official response.
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
    target_object_type: Trademark | Matter | Order | Document | Communication
    target_object_reference_id: string
  apply_scope: string
  create_tasks: boolean
  ingest_official_document: boolean
  prepare_response_documents: boolean
  prepare_evidence_package: boolean
  prepare_customer_communication: boolean
  prepare_response_readiness_review: boolean
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
  official_document_reference_id: string | null
  response_document_reference_ids:
    - string
  evidence_reference_ids:
    - string
  classification_reference_ids:
    - string
  communication_reference_id: string | null
  created_task_reference_ids:
    - string
  response_readiness_status: string | null
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
- Document creation/update must route through Document Service.
- Evidence preparation must route through Evidence Service.
- Classification amendment preparation must route through Classification Service.
- Active Task creation must route through Task Service.
- Communication draft creation must route through Communication Service.
- Official response submission must not happen in this workflow contract.
```

---

# 23. Controlled Values

## 23.1 apply_scope

```text
PreviewOnly
IngestOfficialDocument
PrepareIssueSummary
PrepareResponseStrategy
PrepareClassificationAmendment
PrepareEvidencePackage
PrepareResponseDocuments
PrepareTasks
PrepareCustomerCommunication
PrepareResponseReadiness
FullResponsePreparation
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

## 23.4 office_action_issue_type

```text
AbsoluteGrounds
RelativeGrounds
Distinctiveness
Descriptiveness
Disclaimer
Classification
IdentificationOfGoodsServices
SpecimenOrUse
FormalDefect
PowerOfAttorney
TranslationTransliteration
MultipleIssues
Other
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

## 23.6 response_readiness_status

```text
NotReady
PartiallyReady
ReadyForProfessionalReview
ReadyForCustomerConfirmation
ReadyForSubmissionProcess
PolicyRestricted
RequiresHumanReview
Unknown
```

---

# 24. Codex Implementation Notes

Codex must:

```text
cite this Office Action Response Workflow Contract
cite Workflow Contracts README
cite Workflow Contract API Contract
cite Workflow Contract Service Spec
cite Trademark API and Trademark Service
cite Jurisdiction API and Jurisdiction Service
cite Classification API and Classification Service
cite Document API and Document Service
cite Evidence API and Evidence Service
cite Knowledge API and Knowledge Service
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
use Human Review Contract for document/deadline/strategy/response/communication checkpoints
use Idempotency Contract for apply operations
use Versioning Contract for workflow versioning
write preview tests
write apply tests
write duplicate apply tests
write tests that preview creates no Documents, Evidence, Communication or Tasks
write tests that apply does not duplicate Documents/Evidence/Tasks/Communication
write tests that AI cannot decide legal strategy or certify deadline accuracy without review
write tests that human review gates deadline, strategy, response documents, communication and response readiness
write tests that official response is not submitted by this workflow
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
treat workflow contract as implementation code
create Documents outside Document Service
create Evidence outside Evidence Service
create Classification amendments outside Classification Service
create tasks outside Task Service
send communication outside Communication Service
submit official office action response from this workflow
emit events directly from workflow code
mutate target object outside owning service
skip Permission or Policy checks
allow AI to decide legal strategy, certify deadline, approve amendments, submit responses or create legal advice
hide human-review requirements
overwrite historical workflow versions silently
```

---

# 25. Acceptance Criteria

This Office Action Response Workflow Contract is accepted only if:

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
| 0.1.0 | Draft | Initial Office Action Response Workflow Contract. Defines governed official document intake, deadline/issue extraction, jurisdiction knowledge retrieval, response strategy preparation, classification amendment, evidence package, response documents, customer confirmation, response task plan, Permission/Policy context, AI and human review rules, idempotency, events, errors, versioning and Codex implementation expectations. |

---

**End of Office Action Response Workflow Contract**


## PUB-TASK-B02-003 Component Contract References

State definitions conform to `components/workflow-state-definition-contract.md` (`B02-CONTRACT-WORKFLOW-STATE-DEFINITION`). Transition definitions conform to `components/workflow-transition-definition-contract.md` (`B02-CONTRACT-WORKFLOW-TRANSITION-DEFINITION`). Workflow Contract validates and routes only; it does not perform target object mutation or authorize protected external action.
