# Provider Routing Workflow Contract

**Spec ID:** B02-CONTRACT-WORKFLOW-PROVIDER-ROUTING  
**Spec Type:** Workflow Contract Specification  
**Contract Name:** Provider Routing Workflow Contract  
**Contract File:** core-specs/contracts/workflows/provider-routing-workflow-contract.md  
**Contract Category:** Workflow  
**Related Workflow Contract Type:** ProviderRoutingWorkflow  
**Related Domains:** Routing; Service Provider; Service Network; Partner; Jurisdiction; Matter; Order; Communication; Document; Task; Event; Permission; Policy; Agent  
**Related Object Specs:** core-specs/objects/routing.md; core-specs/objects/service-provider.md; core-specs/objects/service-network.md; core-specs/objects/partner.md; core-specs/objects/jurisdiction.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/communication.md; core-specs/objects/document.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/routing-service.md; core-specs/services/service-provider-service.md; core-specs/services/service-network-service.md; core-specs/services/partner-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/communication-service.md; core-specs/services/document-service.md; core-specs/services/task-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/routing-api.md; core-specs/api/service-provider-api.md; core-specs/api/service-network-api.md; core-specs/api/partner-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/communication-api.md; core-specs/api/document-api.md; core-specs/api/task-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/agent-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/routing-evaluated.md; core-specs/events/routing-selected.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/routing-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Workflow Contract Version:** v0.1.0  
**MVP Phase:** Phase 4 — Collaboration Network Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Provider Routing Workflow Contract defines the governed execution pattern for preparing, evaluating, comparing, reviewing and selecting service providers for a Matter, Order, jurisdiction or service-scope need.

It standardizes:

```text
provider routing trigger
matter / order / jurisdiction target context
service scope context
service provider candidate discovery
service network and partner constraints
routing evaluation
candidate comparison
recommendation preparation
human-reviewed provider selection
communication draft preparation
task plan creation
permission and policy checks
AI assistance boundaries
idempotency behavior
safe error behavior
Codex implementation rules
```

This Workflow Contract does not select providers silently, approve engagement, approve payment, create supplier contracts, certify provider authority, send external communications, or replace Routing Service, Service Provider Service, Service Network Service, Partner Service, Communication Service or Task Service.

---

# 2. Core Lock

```text
Provider Routing Workflow coordinates governed provider routing.
Routing Service owns routing evaluation and selection.
Service Provider, Service Network, Partner and Jurisdiction Services own their domain facts.
Matter and Order Services own business execution context.
Task Service owns active Task creation.
Communication Service owns Communication behavior.
Permission and Policy govern every protected step.
Routing Agent may compare and recommend, but must not select.
Provider selection requires explicit governed human/service decision and trace.
Events preserve trace.
```

---

# 3. Contract Meaning

This contract means:

```text
a reusable governed workflow pattern for preparing provider routing evaluation, comparison, recommendation and selection in MarkOrbit.
```

This contract does not mean:

```text
provider selection by itself
supplier engagement approval
contract approval
payment approval
legal authority certification
communication sending
task completion
permission grant
policy approval
event emitter
provider marketplace UI
```

---

# 4. Workflow Boundary

This Workflow Contract is responsible for:

```text
defining provider routing workflow trigger
defining routing target context
defining routing workflow steps
defining required services
defining candidate discovery and validation boundary
defining routing evaluation boundary
defining recommendation preparation boundary
defining provider selection boundary
defining communication preparation boundary
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
provider engagement approval
supplier contract execution
payment execution
official filing delegation approval
legal authority certification
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
MatterRequiresProvider
OrderRequiresProvider
JurisdictionSelected
ServiceScopeSelected
ManualStaffEntry
PartnerReferral
WorkflowContinuation
AgentPrepared
Unknown
```

Trigger rules:

```text
- Triggering provider routing is not provider selection.
- Matter or Order reference must be validated where provided.
- Jurisdiction and service scope context must be validated before evaluation.
- Agent-prepared trigger must still pass Permission and Policy checks.
- Applying workflow requires idempotency_key.
```

---

# 6. Target Object Context

Provider Routing Workflow may target:

```text
Matter
Order
Jurisdiction
Routing
ServiceProvider
ServiceNetwork
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
- Jurisdiction reference must be validated by Jurisdiction Service where target is Jurisdiction.
- Existing Routing reference must be validated by Routing Service where target is Routing.
- Target status must be revalidated before selection.
```

---

# 7. Required Services

This workflow may require:

```text
Workflow Contract Service
Routing Service
Service Provider Service
Service Network Service
Partner Service
Jurisdiction Service
Matter Service
Order Service
Communication Service
Document Service
Task Service
Event Service
Permission Service
Policy Service
Agent Service
```

Service boundary rules:

```text
- Workflow Contract Service owns preview and apply behavior.
- Routing Service owns routing evaluation and provider selection.
- Service Provider Service owns provider records and capability context.
- Service Network Service owns network membership and coverage context.
- Partner Service owns partner relationship context.
- Jurisdiction Service owns jurisdiction reference context.
- Matter and Order Services own business execution state.
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
  routing_reference_id: string | null
  matter_reference_id: string | null
  order_reference_id: string | null
  jurisdiction_reference_id: string | null
  service_scope_key: string | null
  candidate_service_provider_reference_ids:
    - string
  selected_service_provider_reference_id: string | null
  service_network_reference_ids:
    - string
  partner_reference_ids:
    - string
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
target object type and status
matter/order routing need
jurisdiction context
service scope context
available provider/network/partner context
provider visibility and policy restrictions
routing contract status and version
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
  candidate_visibility_status: string | null
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
```

Controlled applicability status:

```text
Applicable
NotApplicable
InsufficientContext
NoVisibleCandidates
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

Canonical provider routing steps:

```yaml
steps:
  - step_key: validate-routing-context
    step_title_safe: Validate Routing Context
    step_type: Review
    step_required: true
    owning_service: Routing Service
    target_object_type: Routing
    target_object_reference_id: routing_reference_id
    input_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
      - core-specs/contracts/api/matter-api-contract.md
      - core-specs/contracts/api/order-api-contract.md
    output_contract_refs:
      - core-specs/contracts/workflows/provider-routing-workflow-contract.md
    permission_keys:
      - routing:evaluate
      - matter:read
      - order:read
    policy_scopes:
      - routing:evaluate:policy
      - matter:read:policy
      - order:read:policy
    human_review_required: false
    ai_assistance_allowed: false
    events_expected:
      - WorkflowContractApplied
    failure_behavior: StopWorkflow

  - step_key: validate-jurisdiction-and-scope
    step_title_safe: Validate Jurisdiction and Service Scope
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

  - step_key: prepare-provider-query
    step_title_safe: Prepare Provider Query
    step_type: ProviderRouting
    step_required: true
    owning_service: Routing Service
    target_object_type: Routing
    target_object_reference_id: routing_reference_id
    input_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
      - core-specs/contracts/api/service-network-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
    permission_keys:
      - routing:provider-query:prepare
    policy_scopes:
      - routing:provider-query:prepare:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: validate-candidate-providers
    step_title_safe: Validate Candidate Providers
    step_type: ProviderRouting
    step_required: true
    owning_service: Service Provider Service
    target_object_type: ServiceProvider
    target_object_reference_id: candidate_service_provider_reference_ids
    input_contract_refs:
      - core-specs/contracts/api/service-provider-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/service-provider-api-contract.md
    permission_keys:
      - service-provider:read
      - service-provider:validate
    policy_scopes:
      - service-provider:read:policy
      - service-provider:reference:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: evaluate-routing
    step_title_safe: Evaluate Routing
    step_type: ProviderRouting
    step_required: true
    owning_service: Routing Service
    target_object_type: Routing
    target_object_reference_id: routing_reference_id
    input_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
    permission_keys:
      - routing:evaluate
    policy_scopes:
      - routing:evaluate:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected:
      - RoutingEvaluated
    failure_behavior: RequireReview

  - step_key: compare-candidates
    step_title_safe: Compare Candidate Providers
    step_type: ProviderRouting
    step_required: true
    owning_service: Routing Service
    target_object_type: Routing
    target_object_reference_id: routing_reference_id
    input_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
      - core-specs/contracts/api/service-provider-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
    permission_keys:
      - routing:candidates:compare
    policy_scopes:
      - routing:candidates:compare:policy
    human_review_required: false
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: SafePartial

  - step_key: prepare-routing-recommendation
    step_title_safe: Prepare Routing Recommendation
    step_type: ProviderRouting
    step_required: true
    owning_service: Routing Service
    target_object_type: Routing
    target_object_reference_id: routing_reference_id
    input_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
    output_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
      - core-specs/contracts/common/human-review.md
    permission_keys:
      - routing:recommendation:prepare
    policy_scopes:
      - routing:recommendation:prepare:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected: []
    failure_behavior: RequireReview

  - step_key: approve-provider-selection
    step_title_safe: Approve Provider Selection
    step_type: InternalApproval
    step_required: true
    owning_service: Routing Service
    target_object_type: Routing
    target_object_reference_id: routing_reference_id
    input_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
      - core-specs/contracts/common/human-review.md
    output_contract_refs:
      - core-specs/contracts/api/routing-api-contract.md
    permission_keys:
      - routing:select
    policy_scopes:
      - routing:select:policy
    human_review_required: true
    ai_assistance_allowed: true
    events_expected:
      - RoutingSelected
    failure_behavior: RequireReview

  - step_key: prepare-provider-communication
    step_title_safe: Prepare Provider Communication
    step_type: ExternalCommunication
    step_required: false
    owning_service: Communication Service
    target_object_type: Communication
    target_object_reference_id: communication_reference_id
    input_contract_refs:
      - core-specs/contracts/api/communication-api-contract.md
      - core-specs/contracts/api/service-provider-api-contract.md
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

  - step_key: create-routing-tasks
    step_title_safe: Create Routing Tasks
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
```

---

# 12. Task Creation Rules

Suggested task plan:

```yaml
task_plan:
  proposed_tasks:
    - task_type: ProviderRoutingTask
      task_title_safe: Review provider routing context
      task_description_safe: Review jurisdiction, service scope, matter/order context and candidate constraints.
      target_object_type: Routing
      target_object_reference_id: routing_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: validate-routing-context
      human_review_required: true

    - task_type: ReviewTask
      task_title_safe: Compare candidate providers
      task_description_safe: Review candidate provider suitability, restrictions and routing recommendation.
      target_object_type: Routing
      target_object_reference_id: routing_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: compare-candidates
      human_review_required: true

    - task_type: InternalApprovalTask
      task_title_safe: Approve selected provider
      task_description_safe: Approve provider selection before engagement or communication.
      target_object_type: Routing
      target_object_reference_id: routing_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: approve-provider-selection
      human_review_required: true

    - task_type: ExternalCommunicationTask
      task_title_safe: Prepare provider instruction message
      task_description_safe: Prepare provider communication draft after provider selection is approved.
      target_object_type: Communication
      target_object_reference_id: communication_reference_id
      assignee_user_reference_id: null
      due_date: null
      source_step_key: prepare-provider-communication
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
RoutingEvaluated
RoutingSelected
CommunicationCreated
TaskCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Events are emitted by owning services.
- Workflow Contract must not emit events directly.
- RoutingEvaluated and RoutingSelected may only be emitted by Routing Service.
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
routing:evaluate
routing:read
routing:provider-query:prepare
routing:candidates:compare
routing:recommendation:prepare
routing:select
service-provider:read
service-provider:validate
service-network:read
partner:read
jurisdiction:read
jurisdiction:validate
matter:read
order:read
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
routing:evaluate:policy
routing:read:policy
routing:provider-query:prepare:policy
routing:candidates:compare:policy
routing:recommendation:prepare:policy
routing:select:policy
routing:candidate:visibility:policy
routing:commercial-terms:visibility:policy
service-provider:read:policy
service-provider:reference:policy
service-network:read:policy
partner:read:policy
jurisdiction:read:policy
jurisdiction:reference:policy
matter:read:policy
order:read:policy
communication:create:policy
communication:draft:prepare:policy
task:create:policy
cross-organization:workflow
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may block, redact, downgrade or require human review.
- Provider contacts, commercial terms, score bands, candidate lists and private relationship notes may be redacted.
- Workflow output must disclose policy omissions where applicable.
- PolicyRestricted must stop protected action or return safe partial output.
```

---

# 16. AI Assistance Rules

Allowed AI roles:

```text
summarize routing context
identify missing routing fields
prepare provider query filters
summarize candidate provider profiles
compare visible candidates
prepare routing recommendation summary
prepare provider communication draft
prepare follow-up task plan
```

AI must not:

```text
select service provider
approve provider engagement
approve supplier contract
approve payment
certify provider authority
send provider communication
complete tasks
submit filings
decide professional truth
bypass Permission or Policy
```

AI output context shape:

```yaml
ai_output_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: RoutingAgent | null
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
```

---

# 17. Human Review Rules

Human review checkpoints:

```yaml
human_review_checkpoints:
  - checkpoint_key: review-routing-context
    checkpoint_title_safe: Review Routing Context
    required: true
    required_before_step_key: evaluate-routing
    reviewer_role: RoutingReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: review-routing-recommendation
    checkpoint_title_safe: Review Routing Recommendation
    required: true
    required_before_step_key: approve-provider-selection
    reviewer_role: RoutingReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-provider-selection
    checkpoint_title_safe: Approve Provider Selection
    required: true
    required_before_step_key: approve-provider-selection
    reviewer_role: BusinessReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md

  - checkpoint_key: approve-provider-communication
    checkpoint_title_safe: Approve Provider Communication
    required: true
    required_before_step_key: prepare-provider-communication
    reviewer_role: CommunicationReviewer
    review_output_contract_ref: core-specs/contracts/common/human-review.md
```

Rules:

```text
- Human Review records accountable business/professional review.
- Human Review does not select provider by itself.
- Routing Service decides whether review satisfies selection requirements.
- Human review must gate routing recommendation, provider selection and external provider communication.
```

---

# 18. Idempotency Rules

Idempotency requirements:

```text
Preview:
  idempotency_key normally not required unless result is persisted.

Apply:
  idempotency_key required.

Routing evaluation:
  must be duplicate-safe.

Routing selection:
  requires idempotency_key and must be duplicate-safe.

Task creation:
  must be duplicate-safe.

Communication creation:
  must be duplicate-safe.
```

Rules:

```text
- Duplicate apply must not duplicate Routing records, selections, Tasks, Communications or Events.
- Duplicate selection must not duplicate RoutingSelected events.
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
RoutingReferenceInvalid
ServiceProviderReferenceInvalid
ServiceNetworkReferenceInvalid
PartnerReferenceInvalid
JurisdictionReferenceInvalid
MatterReferenceInvalid
OrderReferenceInvalid
CommunicationReferenceInvalid
TaskCreationFailed
NoVisibleCandidates
CandidateSetInvalid
RoutingEvaluationUnavailable
RoutingRecommendationUnavailable
RoutingSelectionInvalid
PermissionDenied
PolicyRestricted
HumanReviewRequired
StateInvalid
InsufficientRoutingContext
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
- Errors must not expose restricted provider data, commercial terms, private relationship notes, candidate scoring internals, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 20. Versioning Rules

Version fields:

```yaml
workflow_contract_version: v0.1.0
contract_version: v0.1.0
schema_version: v0.1.0
routing_evaluation_version: v0.1.0
```

Rules:

```text
- Breaking changes require version bump.
- Workflow application must record workflow_contract_version used.
- Routing selection must record routing_evaluation_version where selection relies on evaluation.
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
    target_object_type: Matter | Order | Jurisdiction | Routing | ServiceProvider | ServiceNetwork
    target_object_reference_id: string
  include_task_plan: boolean
  include_ai_summary: boolean
  include_candidate_summary: boolean
  include_recommendation_preview: boolean
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
  routing_context_summary_safe: string | null
  candidate_summary_safe: string | null
  recommendation_preview_safe: string | null
  missing_context_safe:
    - string
  policy_omissions_disclosed: boolean
  human_review_required: boolean | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Preview does not apply workflow.
- Preview does not evaluate or select routing unless routed through explicit preview-only Routing Service behavior.
- Preview does not create Communications or active Tasks.
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
    target_object_type: Matter | Order | Jurisdiction | Routing | ServiceProvider | ServiceNetwork
    target_object_reference_id: string
  apply_scope: string
  create_tasks: boolean
  evaluate_routing: boolean
  prepare_recommendation: boolean
  select_provider: boolean
  prepare_provider_communication: boolean
  selected_service_provider_reference_id: string | null
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
  routing_reference_id: string | null
  candidate_service_provider_reference_ids:
    - string
  recommended_service_provider_reference_id: string | null
  selected_service_provider_reference_id: string | null
  communication_reference_id: string | null
  created_task_reference_ids:
    - string
  selection_status: string | null
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
- Routing evaluation and selection must route through Routing Service.
- Provider references must be validated by Service Provider Service.
- Active Task creation must route through Task Service.
- Communication draft creation must route through Communication Service.
- Provider selection requires explicit select_provider flag and human/service review requirements.
```

---

# 23. Controlled Values

## 23.1 apply_scope

```text
PreviewOnly
PrepareProviderQuery
EvaluateRouting
CompareCandidates
PrepareRecommendation
SelectProvider
PrepareCommunication
PrepareTasks
FullProviderRouting
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

## 23.4 routing_need_type

```text
NewApplicationProvider
OfficeActionProvider
RenewalProvider
AssignmentProvider
ChangeRecordalProvider
OppositionProvider
EvidenceProvider
TranslationProvider
InvestigationProvider
Other
Unknown
```

## 23.5 candidate_visibility_status

```text
Visible
PartiallyVisible
Hidden
NoVisibleCandidates
PolicyRestricted
PermissionDenied
Unknown
```

## 23.6 selection_status

```text
NotSelected
RecommendationPrepared
Selected
Rejected
Superseded
Cancelled
Unknown
```

---

# 24. Codex Implementation Notes

Codex must:

```text
cite this Provider Routing Workflow Contract
cite Workflow Contracts README
cite Workflow Contract API Contract
cite Workflow Contract Service Spec
cite Routing API and Routing Service
cite Service Provider API and Service Provider Service
cite Service Network API and Service Network Service
cite Partner API and Partner Service
cite Jurisdiction API and Jurisdiction Service
cite Matter API and Matter Service
cite Order API and Order Service
cite Communication API and Communication Service
cite Task API and Task Service
cite Event API and Event Service
cite Routing Agent Spec
use Reference Contract for all references
use Error Contract for errors
use Permission Context Contract before protected steps
use Policy Context Contract before policy-controlled steps
use AI Context Contract for AI-assisted routing comparison/recommendation
use Human Review Contract for recommendation/selection/communication checkpoints
use Idempotency Contract for apply and selection operations
use Versioning Contract for workflow versioning
write preview tests
write apply tests
write duplicate apply tests
write duplicate selection tests
write tests that preview creates no Tasks, Communications or provider selection
write tests that Routing Agent cannot select provider
write tests that recommendation preparation does not select provider
write tests that provider selection requires explicit select_provider and human/service review
write tests that apply does not duplicate RoutingSelected events
write tests that external communication is not sent by this workflow
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
treat workflow contract as implementation code
create Routing outside Routing Service
select provider outside Routing Service
create tasks outside Task Service
send communication outside Communication Service
approve engagement, contract or payment from workflow
emit events directly from workflow code
mutate target object outside owning service
skip Permission or Policy checks
allow AI to select provider, approve engagement, certify authority or send communications
hide human-review requirements
overwrite historical workflow versions silently
```

---

# 25. Acceptance Criteria

This Provider Routing Workflow Contract is accepted only if:

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
| 0.1.0 | Draft | Initial Provider Routing Workflow Contract. Defines governed routing context validation, provider query, candidate validation, routing evaluation, comparison, recommendation, provider selection, provider communication, task plan, Permission/Policy context, Routing Agent boundary, human review, idempotency, events, errors, versioning and Codex implementation expectations. |

---

## Workflow Component Contract Consumption

State Definitions conform to [Workflow State Definition Contract](components/workflow-state-definition-contract.md). Transition Definitions conform to [Workflow Transition Definition Contract](components/workflow-transition-definition-contract.md). Workflow validation does not perform domain mutation; owning Services remain mutation authorities. This reference does not change MVP Depth, does not promote preview-only workflows, does not send Communication Review output, does not submit Trademark Applications, and does not add protected external action.

**End of Provider Routing Workflow Contract**
