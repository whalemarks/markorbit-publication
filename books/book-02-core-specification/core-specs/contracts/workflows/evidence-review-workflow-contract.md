# Evidence Review Workflow Contract

**Spec ID:** B02-CONTRACT-WORKFLOW-EVIDENCE-REVIEW  
**Spec Type:** Workflow Contract Specification  
**Contract Name:** Evidence Review Workflow Contract  
**Contract File:** core-specs/contracts/workflows/evidence-review-workflow-contract.md  
**Contract Category:** Workflow  
**Related Workflow Contract Type:** EvidenceReviewWorkflow  
**Related Domains:** Evidence; Document; Trademark; Brand; Customer; Matter; Order; Jurisdiction; Classification; Knowledge; Communication; Task; Event; Permission; Policy; Agent  
**Related Object Specs:** core-specs/objects/evidence.md; core-specs/objects/document.md; core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification.md; core-specs/objects/knowledge.md; core-specs/objects/communication.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/evidence-service.md; core-specs/services/document-service.md; core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/classification-service.md; core-specs/services/knowledge-service.md; core-specs/services/communication-service.md; core-specs/services/task-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/evidence-api.md; core-specs/api/document-api.md; core-specs/api/trademark-api.md; core-specs/api/brand-api.md; core-specs/api/customer-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/classification-api.md; core-specs/api/knowledge-api.md; core-specs/api/communication-api.md; core-specs/api/task-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/agent-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/workflow-agent.md; core-specs/agents/knowledge-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Workflow Contract Version:** v0.1.0  
**MVP Phase:** Phase 5 — Evidence / Professional Review Expansion  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Evidence Review Workflow Contract defines the governed execution pattern for collecting, structuring, validating, reviewing and preparing evidence for trademark-related professional work.

It standardizes:

```text
evidence review trigger
evidence target context
trademark / brand / customer / matter / order context
document and attachment context
jurisdiction and issue-context reference
classification and goods/services linkage
evidence sufficiency preparation
evidence gap analysis
customer evidence request preparation
task plan creation
human review checkpoints
permission and policy checks
AI assistance boundaries
idempotency behavior
safe error behavior
Codex implementation rules
```

This Workflow Contract does not determine legal sufficiency by itself, certify use, authenticate documents, approve evidence for filing, submit evidence to an official office, send external communications, or replace Evidence Service, Document Service, Trademark Service, Communication Service or Task Service.

---

# 2. Core Lock

```text
Evidence Review Workflow coordinates governed evidence preparation and review.
Evidence Service owns Evidence behavior.
Document Service owns source documents and attachments.
Trademark, Brand, Customer, Matter and Order Services own linked business and professional context.
Jurisdiction, Classification and Knowledge Services provide governed reference context, not professional truth by themselves.
Task Service owns active Task creation.
Communication Service owns Communication behavior.
Permission and Policy govern every protected step.
AI may summarize, classify and identify gaps, but must not decide evidence sufficiency or professional truth.
Events preserve trace.
```

---

# 3. Contract Meaning

This contract means:

```text
a reusable governed workflow pattern for preparing evidence review and evidence-readiness context in MarkOrbit.
```

This contract does not mean:

```text
evidence legal sufficiency decision
document authentication
use certification
official evidence filing
legal advice approval
customer instruction approval
communication sending
task completion
permission grant
policy approval
event emitter
evidence portal UI
```

---

# 4. Workflow Boundary

This Workflow Contract is responsible for:

```text
defining evidence review workflow trigger
defining evidence target context
defining evidence review steps
defining required services
defining source document and attachment boundary
defining evidence gap analysis boundary
defining evidence sufficiency preparation boundary
defining customer communication boundary
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
official evidence submission
legal sufficiency approval by itself
document authentication without review
use certification without review
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
EvidenceUploaded
CustomerEvidenceSubmitted
OfficeActionRequiresEvidence
RenewalRequiresEvidence
UseDeclarationRequiresEvidence
OppositionRequiresEvidence
CancellationRequiresEvidence
ManualStaffEntry
ImportedEvidenceRecord
WorkflowContinuation
AgentPrepared
Unknown
```

Trigger rules:

```text
- Triggering evidence review is not evidence approval.
- Evidence reference must be validated by Evidence Service where provided.
- Source documents must be validated by Document Service where provided.
- Trademark, Matter and Order references must be validated where provided.
- AI-prepared evidence summaries must still pass Permission, Policy and Human Review checks.
- Applying workflow requires idempotency_key.
```

---

# 6. Target Object Context

Evidence Review Workflow may target:

```text
Evidence
Document
Trademark
Matter
Order
Customer
Brand
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
- Evidence reference must be validated by Evidence Service.
- Document reference must be validated by Document Service.
- Trademark reference must be validated by Trademark Service where provided.
- Matter and Order references must be validated by owning services where provided.
- Target status and visibility must be revalidated before protected transitions.
```

---

# 7. Required Services

This workflow may require:

```text
Workflow Contract Service
Evidence Service
Document Service
Trademark Service
Brand Service
Customer Service
Matter Service
Order Service
Jurisdiction Service
Classification Service
Knowledge Service
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
- Evidence Service owns evidence creation, linkage, status and review preparation behavior.
- Document Service owns source documents and attachments.
- Trademark and Brand Services own linked professional context.
- Customer, Matter and Order Services own relationship and business execution state.
- Jurisdiction, Classification and Knowledge Services provide governed reference context.
- Communication Service owns customer/provider communication drafts.
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
  evidence_reference_ids:
    - string
  source_document_reference_ids:
    - string
  attachment_document_reference_ids:
    - string
  trademark_reference_id: string | null
  brand_reference_id: string | null
  customer_reference_id: string | null
  matter_reference_id: string | null
  order_reference_id: string | null
  jurisdiction_reference_id: string | null
  classification_reference_ids:
    - string
  knowledge_reference_ids:
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
evidence type and source context
source document availability
trademark / matter / order context
jurisdiction and issue context
classification / goods-services linkage where applicable
required evidence categories
minimum visible context
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
  evidence_context_status: string | null
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
EvidenceMissing
DocumentMissing
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

Canonical evidence review steps:

```yaml
steps:
  - step_key: validate-evidence-target
    step_title_safe: Validate Evidence Target
    step_type: Review
    step_required: true
    owning_service: Evidence Service
    target_object_type: Evidence
    target_object_reference_id: evidence_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/evidence-api-contract.md
      - core-specs/contracts/api/document-api-contract.md
    output_contract_refs:
      - core-specs/contracts/workflows/evidence-review-workflow-contract.md
    permission_keys:
      - evidence:read
      - evidence:validate
      - document:read
    policy_scopes:
      - evidence:visibility:policy
      - evidence:reference:policy
      - document:visibility:policy
    human_review_required: false
    ai_assistance_allowed: false
    events_expected:
      - WorkflowContractApplied
    failure_behavior: StopWorkflow

  - step_key: validate-linked-context
    step_title_safe: Validate Linked Trademark and Business Context
    step_type: Review
    step_required: true
    owning_service: Trademark Service
    target_object_type: Trademark
    target_object_reference_id: trademark_reference_id
    input_contract_refs:
      - core-specs/contracts/api/trademark-api-contract.md
      - core-specs/contracts/api/matter-api-contract.md
      - core-specs/contracts/api/order-api-contract.md
    output_contract_refs:
      - core-specs/contracts/workflows/evidence-review-workflow-contract.md
    permission_keys:
      - trademark:read
      - matter:read
      - order:read
    policy_scopes:
      - trademark:read:policy
      - matter:read:policy
      - order:read:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: retrieve-evidence-rules
    step_title_safe: Retrieve Evidence Rule Context
    step_type: Review
    step_required: false
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

  - step_key: classify-evidence
    step_title_safe: Classify Evidence
    step_type: CollectEvidence
    step_required: true
    owning_service: Evidence Service
    target_object_type: Evidence
    target_object_reference_id: evidence_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/evidence-api-contract.md
      - core-specs/contracts/api/classification-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/evidence-api-contract.md
    permission_keys:
      - evidence:update
      - classification:read
    policy_scopes:
      - evidence:update:policy
      - classification:read:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: validate-source-documents
    step_title_safe: Validate Source Documents
    step_type: PrepareDocument
    step_required: true
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
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: prepare-evidence-gap-analysis
    step_title_safe: Prepare Evidence Gap Analysis
    step_type: CollectEvidence
    step_required: true
    owning_service: Evidence Service
    target_object_type: Evidence
    target_object_reference_id: evidence_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/evidence-api-contract.md
      - core-specs/contracts/api/knowledge-api-contract.md
    output_contract_refs:
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - evidence:read
      - evidence:update
      - knowledge:read
    policy_scopes:
      - evidence:visibility:policy
      - evidence:update:policy
      - knowledge:read:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: prepare-customer-evidence-request
    step_title_safe: Prepare Customer Evidence Request
    step_type: ExternalCommunication
    step_required: false
    owning_service: Communication Service
    target_object_type: Communication
    target_object_reference_id: communication_reference_id
    input_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
      - core-specs/contracts/api/evidence-api-contract.md
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

  - step_key: create-evidence-review-tasks
    step_title_safe: Create Evidence Review Tasks
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

  - step_key: review-evidence-readiness
    step_title_safe: Review Evidence Readiness
    step_type: InternalApproval
    step_required: true
    owning_service: Evidence Service
    target_object_type: Evidence
    target_object_reference_id: evidence_reference_ids
    input_contract_refs:
      - core-specs/contracts/common/human-review.md
      - core-specs/contracts/api/evidence-api-contract.md
    output_contract_refs:
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - evidence:update
    policy_scopes:
      - evidence:update:policy
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
    - task_type: EvidenceReviewTask
      task_title_safe: Review evidence source and context
      task_description_safe: Review evidence source documents, linked trademark/matter/order context and evidence purpose.
      target_object_type: Evidence
      target_object_reference_id: null
      assignee_user_reference_id: null
      due_date: null
      source_step_key: validate-evidence-target
      human_review_required: true

    - task_type: EvidenceCollectionTask
      task_title_safe: Collect missing evidence
      task_description_safe: Collect missing use evidence, supporting documents or customer confirmations.
      target_object_type: Evidence
      target_object_reference_id: null
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-evidence-gap-analysis
      human_review_required: true

    - task_type: CustomerConfirmationTask
      task_title_safe: Request evidence from customer
      task_description_safe: Prepare and review customer-facing evidence request.
      target_object_type: Communication
      target_object_reference_id: communication_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-customer-evidence-request
      human_review_required: true

    - task_type: InternalApprovalTask
      task_title_safe: Approve evidence readiness
      task_description_safe: Review whether evidence package is ready for governed professional or filing process.
      target_object_type: Evidence
      target_object_reference_id: null
      assignee_user_reference_id: null
      due_date: null
      source_step_key: review-evidence-readiness
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
- Evidence review/sufficiency events are reserved for later if event specs exist.
- Official evidence submission events are outside this workflow unless a governed filing/submission service exists.
- Event references are audit trace, not commands.
- Idempotent replay must not duplicate Events.
```

---

# 14. Permission Rules

Required permission keys:

```text
workflow-contract:preview
workflow-contract:apply
evidence:create
evidence:read
evidence:update
evidence:validate
document:read
document:validate
trademark:read
brand:read
customer:read
matter:read
order:read
jurisdiction:read
classification:read
knowledge:read
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
evidence:create:policy
evidence:visibility:policy
evidence:update:policy
evidence:reference:policy
document:visibility:policy
document:reference:policy
trademark:read:policy
brand:read:policy
customer:read:policy
matter:read:policy
order:read:policy
jurisdiction:read:policy
classification:read:policy
knowledge:read:policy
communication:create:policy
communication:draft:prepare:policy
task:create:policy
cross-organization:workflow
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may block, redact, downgrade or require human review.
- Evidence content, source documents, customer data, use records, commercial terms and private notes may be redacted.
- Workflow output must disclose policy omissions where applicable.
- PolicyRestricted must stop protected action or return safe partial output.
```

---

# 16. AI Assistance Rules

Allowed AI roles:

```text
summarize visible evidence
extract dates and use references from visible documents
classify evidence type
map evidence to goods/services candidates
identify missing source documents
prepare evidence gap analysis
prepare customer evidence request draft
prepare evidence review checklist
prepare follow-up task plan
```

AI must not:

```text
decide legal evidence sufficiency
authenticate documents
certify use
approve evidence for filing
submit evidence
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
  - checkpoint_key: review-source-documents
    checkpoint_title_safe: Review Source Documents
    required: true
    required_before_step_key: prepare-evidence-gap-analysis
    reviewer_role: EvidenceReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: review-evidence-classification
    checkpoint_title_safe: Review Evidence Classification
    required: true
    required_before_step_key: review-evidence-readiness
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: review-evidence-gap-analysis
    checkpoint_title_safe: Review Evidence Gap Analysis
    required: true
    required_before_step_key: prepare-customer-evidence-request
    reviewer_role: EvidenceReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-customer-evidence-request
    checkpoint_title_safe: Approve Customer Evidence Request
    required: true
    required_before_step_key: prepare-customer-evidence-request
    reviewer_role: CommunicationReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-evidence-readiness
    checkpoint_title_safe: Approve Evidence Readiness
    required: true
    required_before_step_key: review-evidence-readiness
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md
```

Rules:

```text
- Human Review records accountable professional/business review.
- Human Review does not certify evidence sufficiency or submit evidence by itself.
- Evidence Service and downstream filing/professional services decide whether review satisfies execution requirements.
- Human review must gate source document review, evidence classification, gap analysis, customer evidence request and evidence readiness.
```

---

# 18. Idempotency Rules

Idempotency requirements:

```text
Preview:
  idempotency_key normally not required unless result is persisted.

Apply:
  idempotency_key required.

Evidence creation/update:
  must be duplicate-safe.

Document linkage:
  must be duplicate-safe.

Task creation:
  must be duplicate-safe.

Communication creation:
  must be duplicate-safe.
```

Rules:

```text
- Duplicate apply must not duplicate Evidence records, Document links, Tasks, Communications or Events.
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
EvidenceReferenceInvalid
DocumentReferenceInvalid
TrademarkReferenceInvalid
BrandReferenceInvalid
CustomerReferenceInvalid
MatterReferenceInvalid
OrderReferenceInvalid
JurisdictionReferenceInvalid
ClassificationReferenceInvalid
KnowledgeReferenceInvalid
CommunicationReferenceInvalid
TaskCreationFailed
EvidenceMissing
DocumentMissing
EvidenceContextInsufficient
EvidencePolicyRestricted
PermissionDenied
PolicyRestricted
HumanReviewRequired
StateInvalid
InsufficientEvidenceContext
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
- Errors must not expose restricted evidence content, source documents, customer data, private notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 20. Versioning Rules

Version fields:

```yaml
workflow_contract_version: v0.1.0
contract_version: v0.1.0
schema_version: v0.1.0
evidence_review_version: v0.1.0
```

Rules:

```text
- Breaking changes require version bump.
- Workflow application must record workflow_contract_version used.
- Evidence review version/source context must be recorded where available.
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
    target_object_type: Evidence | Document | Trademark | Matter | Order | Customer | Brand
    target_object_reference_id: string
  include_task_plan: boolean
  include_ai_summary: boolean
  include_gap_analysis_preview: boolean
  include_evidence_checklist: boolean
  permission_context: object
  policy_context: object
```

Workflow preview response shape:

```yaml
preview_response:
  preview_status: string
  applicable: boolean
  evidence_context_status: string | null
  proposed_steps_visible:
    - step_key: string
      step_title_safe: string
      step_type: string
  proposed_task_plan_safe: object | null
  evidence_summary_safe: string | null
  gap_analysis_preview_safe: string | null
  evidence_checklist_safe:
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
- Preview does not create Evidence, Documents, Communications or active Tasks.
- Preview does not certify evidence sufficiency.
- Preview does not submit evidence.
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
    target_object_type: Evidence | Document | Trademark | Matter | Order | Customer | Brand
    target_object_reference_id: string
  apply_scope: string
  create_tasks: boolean
  classify_evidence: boolean
  validate_documents: boolean
  prepare_gap_analysis: boolean
  prepare_customer_communication: boolean
  prepare_evidence_readiness_review: boolean
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
  evidence_reference_ids:
    - string
  source_document_reference_ids:
    - string
  attachment_document_reference_ids:
    - string
  communication_reference_id: string | null
  created_task_reference_ids:
    - string
  evidence_readiness_status: string | null
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
- Evidence update/linkage must route through Evidence Service.
- Document validation/linkage must route through Document Service.
- Active Task creation must route through Task Service.
- Communication draft creation must route through Communication Service.
- Evidence submission or legal sufficiency approval must not happen in this workflow contract.
```

---

# 23. Controlled Values

## 23.1 apply_scope

```text
PreviewOnly
ValidateEvidence
ClassifyEvidence
ValidateDocuments
PrepareGapAnalysis
PrepareCommunication
PrepareTasks
PrepareEvidenceReadiness
FullEvidenceReview
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

## 23.4 evidence_context_status

```text
Confirmed
PartiallyConfirmed
Unconfirmed
MissingDocuments
PolicyRestricted
Unknown
```

## 23.5 evidence_type

```text
UseEvidence
OwnershipEvidence
AuthorityEvidence
TranslationEvidence
SpecimenEvidence
MarketplaceEvidence
WebsiteEvidence
SalesEvidence
AdvertisingEvidence
OfficialRecordEvidence
Other
Unknown
```

## 23.6 evidence_readiness_status

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
cite this Evidence Review Workflow Contract
cite Workflow Contracts README
cite Workflow Contract API Contract
cite Workflow Contract Service Spec
cite Evidence API and Evidence Service
cite Document API and Document Service
cite Trademark API and Trademark Service
cite Brand API and Brand Service
cite Customer API and Customer Service
cite Matter API and Matter Service
cite Order API and Order Service
cite Jurisdiction API and Jurisdiction Service
cite Classification API and Classification Service
cite Knowledge API and Knowledge Service
cite Communication API and Communication Service
cite Task API and Task Service
cite Event API and Event Service
use Reference Contract for all references
use Error Contract for errors
use Permission Context Contract before protected steps
use Policy Context Contract before policy-controlled steps
use AI Context Contract for AI-assisted evidence summary/gap/checklist steps
use Human Review Contract for source document/classification/gap/communication/readiness checkpoints
use Idempotency Contract for apply operations
use Versioning Contract for workflow versioning
write preview tests
write apply tests
write duplicate apply tests
write tests that preview creates no Evidence, Documents, Communication or Tasks
write tests that apply does not duplicate Evidence/Document links/Tasks/Communication
write tests that AI cannot decide evidence sufficiency or authenticate documents
write tests that human review gates source documents, evidence classification, gap analysis, communication and evidence readiness
write tests that official evidence submission is not performed by this workflow
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
treat workflow contract as implementation code
create Evidence outside Evidence Service
create Documents outside Document Service
create tasks outside Task Service
send communication outside Communication Service
submit evidence from this workflow
emit events directly from workflow code
mutate target object outside owning service
skip Permission or Policy checks
allow AI to decide evidence sufficiency, authenticate documents, certify use, submit evidence or create legal advice
hide human-review requirements
overwrite historical workflow versions silently
```

---

# 25. Acceptance Criteria

This Evidence Review Workflow Contract is accepted only if:

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
| 0.1.0 | Draft | Initial Evidence Review Workflow Contract. Defines governed evidence target validation, linked context validation, evidence rule retrieval, evidence classification, source document validation, gap analysis, customer evidence request, task plan, evidence readiness review, Permission/Policy context, AI and human review rules, idempotency, events, errors, versioning and Codex implementation expectations. |

---

**End of Evidence Review Workflow Contract**


## PUB-TASK-B02-003 Component Contract References

State definitions conform to `components/workflow-state-definition-contract.md` (`B02-CONTRACT-WORKFLOW-STATE-DEFINITION`). Transition definitions conform to `components/workflow-transition-definition-contract.md` (`B02-CONTRACT-WORKFLOW-TRANSITION-DEFINITION`). Workflow Contract validates and routes only; it does not perform target object mutation or authorize protected external action.
