# Assignment Workflow Contract

**Spec ID:** B02-CONTRACT-WORKFLOW-ASSIGNMENT  
**Spec Type:** Workflow Contract Specification  
**Contract Name:** Assignment Workflow Contract  
**Contract File:** core-specs/contracts/workflows/assignment-workflow-contract.md  
**Contract Category:** Workflow  
**Related Workflow Contract Type:** AssignmentWorkflow  
**Related Domains:** Trademark; Customer; Matter; Order; Document; Evidence; Communication; Task; Jurisdiction; Knowledge; Event; Permission; Policy; Agent  
**Related Object Specs:** core-specs/objects/trademark.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/communication.md; core-specs/objects/task.md; core-specs/objects/jurisdiction.md; core-specs/objects/knowledge.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/trademark-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/communication-service.md; core-specs/services/task-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/knowledge-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/trademark-api.md; core-specs/api/customer-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/communication-api.md; core-specs/api/task-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/knowledge-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/agent-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/matter-created.md; core-specs/events/order-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
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

Assignment Workflow Contract defines the governed execution pattern for preparing, reviewing and coordinating trademark ownership assignment work.

It standardizes:

```text
assignment workflow trigger
trademark ownership-change target context
assignor and assignee context
jurisdiction assignment rule context
matter/order preparation boundary
assignment document preparation
supporting evidence preparation
customer confirmation communication
task plan creation
human review checkpoints
permission and policy checks
AI assistance boundaries
idempotency behavior
safe error behavior
Codex implementation rules
```

This Workflow Contract does not record assignment at an official office by itself, approve ownership transfer, certify authority, approve signatures, approve payment, send external communications, or replace Trademark Service, Document Service, Matter Service, Order Service, Communication Service or Task Service.

---

# 2. Core Lock

```text
Assignment Workflow coordinates governed ownership-change preparation.
Trademark Service owns Trademark behavior and trademark ownership state.
Customer, Matter and Order Services own business execution context.
Jurisdiction and Knowledge Services provide governed rule context, not professional truth by themselves.
Document and Evidence Services own assignment documents and supporting evidence records.
Task Service owns active Task creation.
Communication Service owns Communication behavior.
Permission and Policy govern every protected step.
AI may summarize, compare and draft, but must not certify authority, approve transfer or record assignment.
Events preserve trace.
```

---

# 3. Contract Meaning

This contract means:

```text
a reusable governed workflow pattern for preparing trademark assignment execution in MarkOrbit.
```

This contract does not mean:

```text
official assignment recordal
ownership transfer approval
signature authority certification
legal advice approval
customer instruction approval
payment approval
provider selection
communication sending
task completion
permission grant
policy approval
event emitter
assignment filing portal
```

---

# 4. Workflow Boundary

This Workflow Contract is responsible for:

```text
defining assignment workflow trigger
defining trademark assignment target context
defining assignor and assignee preparation
defining jurisdiction rule preparation
defining assignment workflow steps
defining required services
defining task plan shape
defining assignment document/evidence preparation boundary
defining customer communication boundary
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
official assignment submission
legal ownership transfer by itself
signature authority certification without review
payment execution
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
CustomerAssignmentRequest
PortfolioOwnershipChangeDetected
ManualStaffEntry
ImportedAssignmentRecord
MatterCreated
OrderCreated
DocumentUploaded
WorkflowContinuation
AgentPrepared
Unknown
```

Trigger rules:

```text
- Triggering assignment workflow is not transfer approval.
- Trademark reference must be validated by Trademark Service.
- Assignor and assignee context must be reviewed before customer-facing or official-facing use.
- Uploaded assignment documents must be validated by Document Service.
- Agent-prepared trigger must still pass Permission and Policy checks.
- Applying workflow requires idempotency_key.
```

---

# 6. Target Object Context

Assignment Workflow may target:

```text
Trademark
Matter
Order
Customer
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
- Trademark reference must be validated by Trademark Service.
- Matter and Order references must be validated by owning services where provided.
- Customer references for assignor/assignee must be validated by Customer Service where represented as Customers.
- Document references must be validated by Document Service where used as assignment instruments or supporting documents.
- Target status and ownership context must be revalidated before protected transitions.
```

---

# 7. Required Services

This workflow may require:

```text
Workflow Contract Service
Trademark Service
Customer Service
Matter Service
Order Service
Jurisdiction Service
Knowledge Service
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
- Trademark Service owns trademark ownership state and assignment-related trademark context.
- Customer Service owns customer/party context where assignor or assignee is represented as Customer.
- Matter and Order Services own business execution state.
- Jurisdiction Service owns jurisdiction reference context.
- Knowledge Service provides governed source-grounded assignment rule references.
- Document Service owns assignment instruments and supporting documents.
- Evidence Service owns authority/use/evidence support records where applicable.
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
  trademark_reference_id: string
  assignor_customer_reference_id: string | null
  assignee_customer_reference_id: string | null
  matter_reference_id: string | null
  order_reference_id: string | null
  jurisdiction_reference_id: string | null
  assignment_rule_reference_ids:
    - string
  assignment_document_reference_ids:
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
target trademark status
current ownership context
assignor context availability
assignee context availability
jurisdiction assignment rule context
matter/order readiness
required documents
signature/authority evidence where applicable
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
  ownership_context_status: string | null
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
OwnershipContextMissing
PartyContextMissing
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

Canonical assignment workflow steps:

```yaml
steps:
  - step_key: validate-assignment-target
    step_title_safe: Validate Assignment Target
    step_type: Review
    step_required: true
    owning_service: Trademark Service
    target_object_type: Trademark
    target_object_reference_id: trademark_reference_id
    input_contract_refs:
      - core-specs/contracts/api/trademark-api-contract.md
      - core-specs/contracts/api/jurisdiction-api-contract.md
    output_contract_refs:
      - core-specs/contracts/workflows/assignment-workflow-contract.md
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

  - step_key: retrieve-assignment-rules
    step_title_safe: Retrieve Assignment Rules
    step_type: Review
    step_required: true
    owning_service: Knowledge Service
    target_object_type: Knowledge
    target_object_reference_id: assignment_rule_reference_ids
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

  - step_key: validate-party-context
    step_title_safe: Validate Assignor and Assignee Context
    step_type: Review
    step_required: true
    owning_service: Customer Service
    target_object_type: Customer
    target_object_reference_id: assignor_customer_reference_id
    input_contract_refs:
      - core-specs/contracts/api/customer-api-contract.md
    output_contract_refs:
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - customer:read
      - customer:validate
    policy_scopes:
      - customer:read:policy
      - customer:reference:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: prepare-assignment-matter-order
    step_title_safe: Prepare Assignment Matter or Order
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

  - step_key: prepare-assignment-documents
    step_title_safe: Prepare Assignment Documents
    step_type: PrepareDocument
    step_required: true
    owning_service: Document Service
    target_object_type: Document
    target_object_reference_id: assignment_document_reference_ids
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

  - step_key: prepare-authority-evidence
    step_title_safe: Prepare Authority and Supporting Evidence
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

  - step_key: prepare-customer-assignment-communication
    step_title_safe: Prepare Assignment Communication
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

  - step_key: create-assignment-tasks
    step_title_safe: Create Assignment Tasks
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

  - step_key: review-assignment-readiness
    step_title_safe: Review Assignment Readiness
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
      task_title_safe: Review assignment target and ownership context
      task_description_safe: Confirm trademark, current ownership, assignor, assignee and jurisdiction assignment requirements.
      target_object_type: Trademark
      target_object_reference_id: trademark_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: validate-assignment-target
      human_review_required: true

    - task_type: DocumentPreparationTask
      task_title_safe: Prepare assignment documents
      task_description_safe: Prepare assignment agreement, POA or recordal documents.
      target_object_type: Document
      target_object_reference_id: null
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-assignment-documents
      human_review_required: true

    - task_type: EvidenceCollectionTask
      task_title_safe: Collect authority evidence
      task_description_safe: Collect signature authority or supporting evidence if required.
      target_object_type: Evidence
      target_object_reference_id: null
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-authority-evidence
      human_review_required: true

    - task_type: CustomerConfirmationTask
      task_title_safe: Confirm assignment instruction
      task_description_safe: Confirm assignor/assignee information, documents and customer instruction.
      target_object_type: Communication
      target_object_reference_id: communication_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-customer-assignment-communication
      human_review_required: true

    - task_type: InternalApprovalTask
      task_title_safe: Approve assignment readiness
      task_description_safe: Review whether assignment package is ready for governed recordal/submission process.
      target_object_type: Matter
      target_object_reference_id: matter_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: review-assignment-readiness
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
- TaskCreated may only be emitted by Task Service.
- Official assignment recordal events are outside this workflow unless a governed filing/recordal service exists.
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
customer:read
customer:validate
jurisdiction:read
knowledge:read
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
customer:read:policy
customer:reference:policy
jurisdiction:read:policy
knowledge:read:policy
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
task:create:policy
cross-organization:workflow
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may block, redact, downgrade or require human review.
- Party identity, assignment documents, authority evidence, customer communications, commercial terms and private notes may be redacted.
- Workflow output must disclose policy omissions where applicable.
- PolicyRestricted must stop protected action or return safe partial output.
```

---

# 16. AI Assistance Rules

Allowed AI roles:

```text
summarize assignment request
compare current owner and proposed assignee context
retrieve governed assignment rule references
identify missing party or document information
prepare assignment checklist
prepare assignment document outline
prepare customer confirmation draft
prepare authority/evidence gap summary
prepare follow-up task plan
```

AI must not:

```text
certify ownership transfer authority
approve assignment agreement
approve signature authority
record assignment
approve customer instruction
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
  - checkpoint_key: confirm-ownership-context
    checkpoint_title_safe: Confirm Ownership Context
    required: true
    required_before_step_key: prepare-assignment-documents
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: confirm-party-authority
    checkpoint_title_safe: Confirm Assignor and Assignee Authority
    required: true
    required_before_step_key: review-assignment-readiness
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-assignment-documents
    checkpoint_title_safe: Approve Assignment Documents
    required: true
    required_before_step_key: review-assignment-readiness
    reviewer_role: FilingReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-assignment-communication
    checkpoint_title_safe: Approve Assignment Communication
    required: true
    required_before_step_key: prepare-customer-assignment-communication
    reviewer_role: CommunicationReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-assignment-readiness
    checkpoint_title_safe: Approve Assignment Readiness
    required: true
    required_before_step_key: review-assignment-readiness
    reviewer_role: TrademarkProfessional
    review_output_contract_ref: core-specs/contracts/common/human-review.md
```

Rules:

```text
- Human Review records accountable professional/business review.
- Human Review does not record assignment or approve payment by itself.
- Matter, Order and downstream filing/recordal services decide whether review satisfies execution requirements.
- Human review must gate ownership context, party authority, documents, customer communication and assignment readiness.
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

Evidence linkage:
  must be duplicate-safe.

Task creation:
  must be duplicate-safe.

Communication creation:
  must be duplicate-safe.
```

Rules:

```text
- Duplicate apply must not duplicate Matter, Order, Documents, Evidence links, Tasks, Communications or Events.
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
CustomerReferenceInvalid
AssignorReferenceInvalid
AssigneeReferenceInvalid
JurisdictionReferenceInvalid
MatterReferenceInvalid
OrderReferenceInvalid
DocumentReferenceInvalid
EvidenceReferenceInvalid
CommunicationReferenceInvalid
TaskCreationFailed
OwnershipContextMissing
PartyContextMissing
AuthorityEvidenceMissing
PermissionDenied
PolicyRestricted
HumanReviewRequired
StateInvalid
InsufficientAssignmentContext
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
- Errors must not expose restricted party data, assignment documents, evidence, commercial terms, private notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 20. Versioning Rules

Version fields:

```yaml
workflow_contract_version: v0.1.0
contract_version: v0.1.0
schema_version: v0.1.0
assignment_rule_version: v0.1.0
```

Rules:

```text
- Breaking changes require version bump.
- Workflow application must record workflow_contract_version used.
- Assignment rule version/source context must be recorded where available.
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
    target_object_type: Trademark | Matter | Order | Customer | Document
    target_object_reference_id: string
  include_task_plan: boolean
  include_ai_summary: boolean
  include_party_summary: boolean
  include_assignment_checklist: boolean
  permission_context: object
  policy_context: object
```

Workflow preview response shape:

```yaml
preview_response:
  preview_status: string
  applicable: boolean
  ownership_context_status: string | null
  proposed_steps_visible:
    - step_key: string
      step_title_safe: string
      step_type: string
  proposed_task_plan_safe: object | null
  assignment_summary_safe: string | null
  party_summary_safe: string | null
  assignment_checklist_safe:
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
- Preview does not create Matter, Order, Documents, Evidence, Communications or active Tasks.
- Preview does not approve ownership transfer.
- Preview does not record assignment.
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
    target_object_type: Trademark | Matter | Order | Customer | Document
    target_object_reference_id: string
  apply_scope: string
  create_tasks: boolean
  create_matter_or_order_if_missing: boolean
  prepare_documents: boolean
  prepare_evidence_context: boolean
  prepare_customer_communication: boolean
  prepare_assignment_readiness_review: boolean
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
  assignment_document_reference_ids:
    - string
  evidence_reference_ids:
    - string
  communication_reference_id: string | null
  created_task_reference_ids:
    - string
  assignment_readiness_status: string | null
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
- Active Task creation must route through Task Service.
- Communication draft creation must route through Communication Service.
- Official assignment recordal must not happen in this workflow contract.
```

---

# 23. Controlled Values

## 23.1 apply_scope

```text
PreviewOnly
PreparePartyContext
PrepareMatterOrder
PrepareDocuments
PrepareEvidence
PrepareCommunication
PrepareTasks
PrepareAssignmentReadiness
FullAssignmentPreparation
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

## 23.4 assignment_type

```text
FullAssignment
PartialAssignment
Merger
NameChangeRelated
SecurityInterest
RecordalCorrection
Other
Unknown
```

## 23.5 ownership_context_status

```text
Confirmed
PartiallyConfirmed
Unconfirmed
ConflictDetected
PolicyRestricted
Unknown
```

## 23.6 assignment_readiness_status

```text
NotReady
PartiallyReady
ReadyForProfessionalReview
ReadyForCustomerConfirmation
ReadyForRecordalProcess
PolicyRestricted
RequiresHumanReview
Unknown
```

---

# 24. Codex Implementation Notes

Codex must:

```text
cite this Assignment Workflow Contract
cite Workflow Contracts README
cite Workflow Contract API Contract
cite Workflow Contract Service Spec
cite Trademark API and Trademark Service
cite Customer API and Customer Service
cite Jurisdiction API and Jurisdiction Service
cite Knowledge API and Knowledge Service
cite Matter API and Matter Service
cite Order API and Order Service
cite Document API and Document Service
cite Evidence API and Evidence Service
cite Communication API and Communication Service
cite Task API and Task Service
cite Event API and Event Service
use Reference Contract for all references
use Error Contract for errors
use Permission Context Contract before protected steps
use Policy Context Contract before policy-controlled steps
use AI Context Contract for AI-assisted steps
use Human Review Contract for ownership/authority/document/communication/readiness checkpoints
use Idempotency Contract for apply operations
use Versioning Contract for workflow versioning
write preview tests
write apply tests
write duplicate apply tests
write tests that preview creates no Matter, Order, Documents, Evidence, Communication or Tasks
write tests that apply does not duplicate Matter/Order/Documents/Evidence/Tasks/Communication
write tests that AI cannot certify authority or approve assignment
write tests that human review gates ownership context, party authority, documents, communication and assignment readiness
write tests that official assignment recordal is not performed by this workflow
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
treat workflow contract as implementation code
update Trademark ownership outside Trademark Service
create Matter or Order outside owning services
create Documents outside Document Service
create Evidence outside Evidence Service
create tasks outside Task Service
send communication outside Communication Service
record official assignment from this workflow
emit events directly from workflow code
mutate target object outside owning service
skip Permission or Policy checks
allow AI to certify authority, approve transfer, record assignment or create legal advice
hide human-review requirements
overwrite historical workflow versions silently
```

---

# 25. Acceptance Criteria

This Assignment Workflow Contract is accepted only if:

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
| 0.1.0 | Draft | Initial Assignment Workflow Contract. Defines governed assignment target validation, rule retrieval, assignor/assignee context, matter/order preparation, assignment documents, authority evidence, customer communication, task plan, assignment readiness review, Permission/Policy context, AI and human review rules, idempotency, events, errors, versioning and Codex implementation expectations. |

---

**End of Assignment Workflow Contract**


## PUB-TASK-B02-003 Component Contract References

State definitions conform to `components/workflow-state-definition-contract.md` (`B02-CONTRACT-WORKFLOW-STATE-DEFINITION`). Transition definitions conform to `components/workflow-transition-definition-contract.md` (`B02-CONTRACT-WORKFLOW-TRANSITION-DEFINITION`). Workflow Contract validates and routes only; it does not perform target object mutation or authorize protected external action.
