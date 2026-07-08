# API Contract — Agent API

**Spec ID:** B02-CONTRACT-API-AGENT  
**Spec Type:** API Contract Specification  
**Contract Name:** Agent API Contract  
**Contract File:** core-specs/contracts/api/agent-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/agent-api.md  
**Related Domain:** Agent  
**Related Object Specs:** core-specs/objects/agent.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/knowledge.md; core-specs/objects/task.md; core-specs/objects/workflow-contract.md; core-specs/objects/communication.md; core-specs/objects/routing.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/agent-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/knowledge-service.md; core-specs/services/task-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/communication-service.md; core-specs/services/routing-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/knowledge-api.md; core-specs/api/task-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/communication-api.md; core-specs/api/routing-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/agent-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md; core-specs/agents/knowledge-agent.md; core-specs/agents/task-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/audit-agent.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 4 — Collaboration Network / AI Governance Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Agent API Contract defines the implementation-facing request and response contract for Agent API operations in MarkOrbit Core.

It standardizes how clients register, read, update, search, validate, activate, suspend, evaluate and invoke governed Agent capabilities through API boundaries without bypassing Agent Service, Agent Registry, Permission Service, Policy Service, Human Review rules or Event Service.

This contract governs:

```text
Agent API versioning
Agent create/register request
Agent update request
Agent read response
Agent search/list response
Agent reference validation
Agent registry key validation
Agent capability evaluation
Agent invocation preparation
Agent activation and suspension
AI context creation and disclosure
Permission and Policy context
Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Agent API Contract does not grant permissions, execute downstream domain actions by itself, bypass owning services, approve professional truth, silently mutate domain state, send communications, select providers, complete tasks or replace human review where required.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Agent Service through governed API boundaries.
```

This contract does not mean:

```text
unrestricted AI execution interface
permission grant
policy approval
professional truth generator
downstream service bypass
workflow executor by itself
communication sender
provider selector
task completer
legal conclusion
debug prompt endpoint
```

Core rule:

```text
Agent API receives governed agent requests.
Agent Service owns Agent identity and registry behavior.
Permission and Policy govern every capability use.
Agents may prepare, draft, summarize, suggest and validate only within their governed scope.
Downstream actions must route through owning services.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Agent reference fields
Agent registry fields
capability declaration fields
capability evaluation fields
safe invocation preparation fields
AI context fields
human-review fields
pagination shape for list/search
permission/policy context requirements
idempotency requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
LLM provider internals
prompt runtime implementation
tool execution internals
downstream domain execution
permission evaluation logic
policy evaluation logic
human review decision logic
event emission implementation outside owning services
database schema design
UI rendering
```

---

# 4. Related Owning Spec

Owning API spec:

```text
core-specs/api/agent-api.md
```

Owning service spec:

```text
core-specs/services/agent-service.md
```

Owning agent governance specs:

```text
core-specs/agents/ai-agent-governance.md
core-specs/agents/agent-registry.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Agent API, Agent Service, Agent Registry or AI Agent Governance boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Agent
```

Related objects:

```text
User
Organization
Permission
Policy
Knowledge
Task
WorkflowContract
Communication
Routing
Event
```

Reference rules:

```text
- agent_reference_id identifies Agent.
- agent_registry_key identifies declared Agent type/capability family.
- actor_reference_id identifies the requesting actor and must not be replaced by agent_reference_id.
- permission_decision_reference_id and policy_decision_reference_id must be validated before capability use.
- ai_context_reference_id identifies AI assistance context and does not authorize downstream execution.
- Downstream target references must be validated by their owning services.
```

---

# 6. Required References

Common API context:

```yaml
api_context:
  api_version: v1
  contract_version: v0.1.0
  correlation_id: string | null
  idempotency_key: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
```

Agent target context:

```yaml
target:
  agent_reference_id: string | null
  target_object_type: Agent
  target_object_reference_id: string | null
```

Rules:

```text
- agent_reference_id is required for read/update/activate/suspend/validate-by-reference operations.
- agent_registry_key is required for registry validation and capability evaluation.
- idempotency_key is required for create/register operations.
- actor_reference_id or governed system context is required for protected operations.
- Permission and Policy decisions are required before capability use.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/agents
GET    /v1/agents/{agent_reference_id}
PATCH  /v1/agents/{agent_reference_id}
GET    /v1/agents
POST   /v1/agents/validate-reference
POST   /v1/agents/validate-registry-key
POST   /v1/agents/{agent_reference_id}/evaluate-capability
POST   /v1/agents/{agent_reference_id}/prepare-invocation
POST   /v1/agents/{agent_reference_id}/activate
POST   /v1/agents/{agent_reference_id}/suspend
```

Endpoint ownership:

```text
API layer validates request contract.
Agent Service executes Agent behavior.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Downstream owning services execute downstream domain actions.
Event Service records events emitted by owning services.
API layer must not execute downstream actions directly.
```

---

# 8. Create/Register Agent Request Contract

Endpoint:

```text
POST /v1/agents
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string
actor_reference_id: string | null
organization_reference_id: string | null

permission_context:
  required_permission_keys:
    - agent:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - agent:create:policy
  policy_decision_reference_id: string | null

payload:
  agent_registry_key: string
  agent_name_safe: string
  agent_status: string | null
  agent_type: string
  owning_service_reference: string | null
  allowed_capability_keys:
    - string
  allowed_target_object_types:
    - string
  data_access_scope_default: string | null
  human_review_default_required: boolean
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- agent_registry_key, agent_name_safe and agent_type are required.
- agent_registry_key must be validated against Agent Registry.
- allowed_capability_keys must not exceed Agent Registry declaration.
- data_access_scope_default must not exceed Policy allowance.
- Agent Service assigns agent_reference_id.
```

---

# 9. Create/Register Agent Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  agent_reference_id: string
  agent_registry_key: string
  agent_name_safe: string
  agent_type: string
  agent_status: string
  allowed_capability_keys:
    - string
  allowed_target_object_types:
    - string
  data_access_scope_default: string | null
  human_review_default_required: boolean
  created_at: datetime
  updated_at: datetime | null
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
idempotency_result:
  idempotency_key: string
  idempotency_status: string
  replayed: boolean
```

Rules:

```text
- Response must not expose database IDs, secret keys, prompts or provider credentials.
- AgentCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate AgentCreated event.
```

---

# 10. Read Agent Contract

Endpoint:

```text
GET /v1/agents/{agent_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  agent_reference_id: string
  agent_registry_key: string
  agent_name_safe: string
  agent_type: string
  agent_status: string
  owning_service_reference: string | null
  allowed_capability_keys_visible:
    - string
  allowed_target_object_types_visible:
    - string
  data_access_scope_default: string | null
  human_review_default_required: boolean
  metadata_safe: object | null
  created_at: datetime | null
  updated_at: datetime | null
  restricted_fields_omitted: boolean
permission_context:
  permission_decision_reference_id: string | null
policy_context:
  policy_decision_reference_id: string | null
```

Rules:

```text
- Read must evaluate agent:read permission.
- Policy may redact capability details, owning service, metadata or target types.
- Secret prompts, credentials and provider internals must never be exposed.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Agent Contract

Endpoint:

```text
PATCH /v1/agents/{agent_reference_id}
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  agent_name_safe: string | null
  agent_status: string | null
  owning_service_reference: string | null
  allowed_capability_keys_patch:
    - string
  allowed_target_object_types_patch:
    - string
  data_access_scope_default: string | null
  human_review_default_required: boolean | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - agent:update
policy_context:
  required_policy_scopes:
    - agent:update:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  agent_reference_id: string
  agent_registry_key: string
  agent_status: string
  agent_name_safe: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Update must route through Agent Service.
- Capability expansion must be validated against Agent Registry, Permission and Policy.
- Human review may be required for capability, data scope or target expansion.
- Agent update must not alter downstream service ownership.
```

---

# 12. Search/List Agents Contract

Endpoint:

```text
GET /v1/agents
```

Query parameters:

```yaml
agent_registry_key: string | null
agent_type: string | null
agent_status: string | null
owning_service_reference: string | null
capability_key: string | null
target_object_type: string | null
safe_query: string | null
pagination:
  cursor: string | null
  limit: integer | null
  sort:
    field: string | null
    direction: Asc | Desc | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  items:
    - agent_reference_id: string
      agent_registry_key: string
      agent_name_safe: string
      agent_type: string
      agent_status: string
      owning_service_reference: string | null
      restricted_fields_omitted: boolean
  pagination:
    next_cursor: string | null
    previous_cursor: string | null
    limit: integer
    returned_count: integer
    has_more: boolean
    total_count: integer | null
    total_count_omitted: boolean
```

Rules:

```text
- Pagination must follow Pagination Contract.
- total_count must be omitted where policy or security requires it.
- Search must not reveal restricted Agent existence.
- safe_query must not search secret prompts, credentials or provider internals.
```

---

# 13. Validate Agent Reference Contract

Endpoint:

```text
POST /v1/agents/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  agent_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  agent_reference_id: string
  valid: boolean
  validation_status: string
  agent_registry_key: string | null
  agent_status: string | null
  safe_label: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to use Agent.
- Validation status must follow Reference Contract.
- Policy may hide safe_label, registry key or status.
```

---

# 14. Validate Registry Key Contract

Endpoint:

```text
POST /v1/agents/validate-registry-key
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  agent_registry_key: string
  intended_use: string | null
  requested_capability_key: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  agent_registry_key: string
  valid: boolean
  validation_status: string
  allowed_capability_keys_visible:
    - string
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid registry key only means declared Agent type exists.
- Registry key validation does not grant permission or policy allowance.
- Restricted capability details may be omitted.
```

---

# 15. Evaluate Capability Contract

Endpoint:

```text
POST /v1/agents/{agent_reference_id}/evaluate-capability
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
permission_context:
  required_permission_keys:
    - agent:capability:evaluate
policy_context:
  required_policy_scopes:
    - agent:capability:evaluate:policy
payload:
  requested_capability_key: string
  intended_operation: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
  requested_data_access_scope: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  agent_reference_id: string
  agent_registry_key: string
  requested_capability_key: string
  capability_decision: string
  allowed: boolean
  evaluated_data_access_scope: string | null
  human_review_required: boolean
  missing_requirements_safe:
    - string
  restricted_fields_omitted: boolean
permission_context:
  permission_decision_reference_id: string | null
policy_context:
  policy_decision_reference_id: string | null
```

Rules:

```text
- Capability evaluation does not execute the capability.
- Capability Allowed does not bypass downstream owning service.
- Data access scope must not exceed Policy decision.
- Human review requirement must be explicit.
```

---

# 16. Prepare Invocation Contract

Endpoint:

```text
POST /v1/agents/{agent_reference_id}/prepare-invocation
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
permission_context:
  required_permission_keys:
    - agent:invocation:prepare
policy_context:
  required_policy_scopes:
    - agent:invocation:prepare:policy
ai_context:
  ai_assisted: true
  agent_reference_id: string
  agent_registry_key: string
payload:
  requested_capability_key: string
  invocation_purpose: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
  input_context_safe: object | null
  requested_output_scope: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  invocation_preparation_status: string
  ai_context_reference_id: string | null
  prepared_input_context_safe: object | null
  output_contract_hint_safe: object | null
  missing_context_safe:
    - string
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Prepare invocation is not downstream execution.
- Prepared context must remain within evaluated data access scope.
- Agent output contract must be advisory unless accepted through owning service.
- Human review may be required before downstream use.
```

---

# 17. Activate Agent Contract

Endpoint:

```text
POST /v1/agents/{agent_reference_id}/activate
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  activation_reason_safe: string | null
permission_context:
  required_permission_keys:
    - agent:activate
policy_context:
  required_policy_scopes:
    - agent:activate:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  agent_reference_id: string
  previous_status: string
  current_status: string
  activated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Activation must route through Agent Service.
- Activation does not grant permission or policy allowance.
- Human review may be required for high-risk Agent types.
```

---

# 18. Suspend Agent Contract

Endpoint:

```text
POST /v1/agents/{agent_reference_id}/suspend
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  suspension_reason_safe: string | null
permission_context:
  required_permission_keys:
    - agent:suspend
policy_context:
  required_policy_scopes:
    - agent:suspend:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  agent_reference_id: string
  previous_status: string
  current_status: string
  suspended_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Suspension must route through Agent Service.
- Suspension does not alter historical AI context or Event trace.
- In-flight downstream operations remain owned by their owning services.
```

---

# 19. Controlled Values

## 19.1 agent_type

```text
KnowledgeAgent
TaskAgent
WorkflowAgent
CommunicationAgent
RoutingAgent
AuditAgent
SystemAgent
IntegrationAgent
Other
Unknown
```

## 19.2 agent_status

```text
Draft
Active
Suspended
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 19.3 capability_key

```text
knowledge.retrieve
knowledge.summarize
task.summarize
task.prepareCompletion
workflow.preview
workflow.prepareTaskPlan
communication.prepareDraft
communication.summarize
routing.compare
routing.prepareRecommendation
audit.summarizeTrace
audit.explainEvents
unknown
```

## 19.4 data_access_scope

```text
NoAccess
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContentWithHumanApproval
Unknown
```

## 19.5 capability_decision

```text
Allowed
Denied
Restricted
RequiresHumanReview
NotSupported
NotEvaluated
Unknown
```

## 19.6 invocation_preparation_status

```text
Prepared
Partial
InsufficientContext
PolicyRestricted
PermissionDenied
CapabilityDenied
RequiresHumanReview
Error
Unknown
```

## 19.7 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
Suspended
Deprecated
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 19.8 sort.field

```text
created_at
updated_at
agent_name_safe
agent_status
agent_type
agent_registry_key
owning_service_reference
```

---

# 20. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] agent_reference_id is valid where required.
[ ] agent_registry_key is valid where required.
[ ] idempotency_key is present for create.
[ ] agent_type is controlled.
[ ] agent_status is controlled where provided.
[ ] capability keys are controlled and registry-allowed.
[ ] requested target object type is allowed by Agent Registry.
[ ] data access scope is controlled and policy-allowed.
[ ] AI Context is present for invocation preparation.
[ ] Human Review Context is present where policy requires review.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 21. Permission Rules

Required permission keys:

```text
agent:create
agent:read
agent:search
agent:update
agent:validate
agent:registry-key:validate
agent:capability:evaluate
agent:invocation:prepare
agent:activate
agent:suspend
```

Rules:

```text
- Agent API must not grant permission.
- Permission Service evaluates required permission keys.
- Capability declaration does not equal permission.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 22. Policy Rules

Required policy scopes may include:

```text
agent:create:policy
agent:read:policy
agent:search:policy
agent:update:policy
agent:reference:policy
agent:registry:visibility:policy
agent:capability:evaluate:policy
agent:invocation:prepare:policy
agent:data-access:policy
agent:activate:policy
agent:suspend:policy
cross-organization:agent
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact capability details, registry details, target context, prepared input context or total_count.
- Policy may downgrade data access scope.
- Policy may require human review before invocation or activation.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 23. AI and Human Review Rules

AI rules:

```text
- Agent may operate only within declared Agent Registry capability and evaluated Permission/Policy context.
- AI output is advisory unless accepted through governed human/service process.
- Agent must not silently create, update, complete, approve, send, select, submit, pay or bind.
- Agent must disclose source scope, missing context, policy omissions and human-review requirements.
```

Human review:

```text
- Human review may be required where Agent output is used for professional decision, external communication, workflow application, task completion, provider selection, filing, payment-impacting action or customer-facing output.
- human_review_required must be explicit where policy requires review.
```

---

# 24. Idempotency and Event Rules

Idempotency:

```text
POST /v1/agents requires idempotency_key.
PATCH /v1/agents/{agent_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Activate/suspend endpoints may require idempotency_key for duplicate-sensitive operations.
Capability evaluation and prepare-invocation do not normally require idempotency unless result is persisted.
```

Events:

```text
AgentCreated may be emitted by Agent Service after successful creation.
Agent activation/suspension events may be reserved for later if event specs exist.
Downstream domain events may only be emitted by downstream owning services.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 25. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
AgentReferenceInvalid
AgentRegistryKeyInvalid
AgentCapabilityInvalid
AgentCapabilityDenied
AgentSuspended
AgentDeprecated
DataAccessScopeExceeded
InvocationPreparationUnavailable
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
- Errors must not expose prompts, provider internals, secret configuration, restricted context, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 26. Versioning Rules

Version fields:

```yaml
api_version: v1
contract_version: v0.1.0
schema_version: v0.1.0
agent_registry_version: v0.1.0
```

Rules:

```text
- Unsupported API or contract versions must fail closed.
- Agent Registry version must be recorded for capability evaluation where applicable.
- Breaking changes require contract version bump.
- Response payloads must preserve version fields.
```

---

# 27. Codex Implementation Notes

Codex must:

```text
cite Agent API Spec
cite Agent Service Spec
cite AI Agent Governance Spec
cite Agent Registry Spec
cite this Agent API Contract
use Reference Contract for agent_reference_id and target references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before capability use and context exposure
use AI Context Contract for invocation preparation
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive activation/suspension operations
use Versioning Contract for version validation
route all Agent mutation through Agent Service
invoke Permission Service before protected behavior
invoke Policy Service before exposing capability, data access or prepared context
return safe errors only
write tests for create/read/update/search/validate-reference/validate-registry-key/evaluate-capability/prepare-invocation/activate/suspend
write tests for registry key validation
write tests for unsupported capability
write tests for data access scope downgrade
write tests that prepare-invocation does not execute downstream action
write tests that Agent cannot bypass owning services
write tests for suspended Agent rejection
write tests for human_review_required
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Agent directly in API layer
query database directly from API contract implementation
use generic id where agent_reference_id is required
expose database IDs, secret prompts, credentials, provider internals or restricted context
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
execute downstream domain actions from Agent API
allow Agent to complete tasks, apply workflows, send communications, select providers, submit filings or approve payments
treat AI output as professional truth
allow AI context to exceed evaluated_data_access_scope
```

---

# 28. Acceptance Criteria

This Agent API Contract is accepted only if:

```text
[ ] It defines Agent API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Agent API, Agent Service, AI Agent Governance and Agent Registry specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create/register request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines validate-registry-key contract.
[ ] It defines evaluate capability contract.
[ ] It defines prepare invocation contract.
[ ] It defines activate contract.
[ ] It defines suspend contract.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI and Human Review rules.
[ ] It defines idempotency and event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 29. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Agent API Contract. Defines governed create/register, read, update, search, validate-reference, registry validation, capability evaluation, invocation preparation, activation and suspension payloads, Permission/Policy context, AI and human review, idempotency, event trace, safe errors, versioning and Codex implementation rules. |

---

**End of API Contract**
