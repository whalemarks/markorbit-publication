# API Specification — Agent API

**Spec ID:** B02-API-AGENT  
**Spec Type:** API Specification  
**API Name:** Agent API  
**API File:** core-specs/api/agent-api.md  
**Related Domain:** core-specs/domains/agent.md  
**Related Object Specs:** core-specs/objects/agent.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/knowledge.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/communication.md; core-specs/objects/routing.md; core-specs/objects/service-provider.md  
**Related Service Specs:** core-specs/services/agent-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/knowledge-service.md; core-specs/services/task-service.md; core-specs/services/event-service.md; core-specs/services/communication-service.md; core-specs/services/routing-service.md; core-specs/services/service-provider-service.md  
**Related Event Specs:** core-specs/events/agent-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/routing-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/agent-api-contract.md; core-specs/contracts/events/agent-created-payload.md; core-specs/contracts/agents/agent-runtime-contract.md  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 4 — Collaboration / Network Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Agent API exposes governed Agent registration, access, validation and execution-boundary operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and control Agent references without treating Agent as User, Service Provider, human professional, legal decision-maker, autonomous system authority, unrestricted API client, unrestricted knowledge reader or owner of professional truth.

Agent API exists to support:

```text
AI / automation agent registration
agent identity and capability boundary
agent permission and policy evaluation context
agent-to-task execution preparation
agent knowledge access governance
agent communication drafting governance
agent routing support governance
agent event trace access
API-safe agent reference validation
```

Agent API does not authorize autonomous legal work, bypass professional review, create domain truth, override Permission/Policy, replace users or act as service provider by itself.

---

# 2. API Meaning

Agent API means:

```text
a governed interface for operating Agent references and Agent execution boundaries through Agent Service.
```

Agent API does not mean:

```text
User API
Service Provider API
professional decision API
unrestricted AI runtime API
unrestricted tool access API
Knowledge bypass API
Task execution bypass API
Communication sending API
Routing decision API
```

Agent is an execution actor category with governed capabilities.

User is human/account context.

Service Provider is external service-capability context.

Professional truth remains with governed business responsibility and human review where required.

---

# 3. API Boundary

Agent API is responsible for:

```text
Agent create request intake
Agent read/search/list access
Agent update request intake
Agent reference validation
Agent capability exposure under policy
Agent access boundary evaluation
Agent task execution-context preparation
Agent knowledge access request governance
Agent communication draft governance
safe Agent response shaping
Permission/Policy enforcement for Agent operations
Agent-related Event reference exposure where allowed
controlled API errors
```

Agent API is not responsible for:

```text
human user lifecycle ownership
service provider lifecycle ownership
professional legal conclusion
official filing execution
unrestricted automation runtime execution
unrestricted knowledge access
task completion without Task Service
communication delivery without Communication Service
routing selection without Routing Service
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/agent.md
```

Domain rule:

```text
Agent represents governed AI or automation actor context.
Agent is not User, Service Provider, professional truth, unrestricted runtime or autonomous legal authority by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/agent.md
core-specs/objects/user.md
core-specs/objects/organization.md
core-specs/objects/permission.md
core-specs/objects/policy.md
core-specs/objects/knowledge.md
core-specs/objects/task.md
core-specs/objects/event.md
core-specs/objects/communication.md
core-specs/objects/routing.md
core-specs/objects/service-provider.md
```

Object rules:

```text
- Agent API returns agent_reference_id.
- Agent API may reference User, Organization, Permission, Policy, Knowledge, Task, Event, Communication, Routing or Service Provider context but must not create or execute them silently.
- Agent cannot be treated as human professional.
- Agent cannot be treated as Service Provider.
- Agent access must be capability-scoped, permission-scoped, policy-scoped and context-scoped.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/agent-service.md
core-specs/services/user-service.md
core-specs/services/organization-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/knowledge-service.md
core-specs/services/task-service.md
core-specs/services/event-service.md
core-specs/services/communication-service.md
core-specs/services/routing-service.md
core-specs/services/service-provider-service.md
```

Service rules:

```text
- Agent API must invoke Agent Service for Agent behavior.
- Agent API must validate related references through their owning services where required.
- Agent API must invoke Permission Service before protected agent operations.
- Agent API must invoke Policy Service before access, capability, knowledge or execution-boundary operations.
- Agent API must not emit Agent events directly; Agent Service and Event Service govern events.
- Downstream actions must route through owning services.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/agent-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
core-specs/events/task-created.md
core-specs/events/communication-created.md
core-specs/events/routing-evaluated.md
```

Event rules:

```text
- createAgent may result in AgentCreated.
- protected agent operations may produce PermissionEvaluated and PolicyEvaluated.
- agent-prepared tasks must route through Task Service and may result in TaskCreated.
- agent-prepared communications must route through Communication Service and may result in CommunicationCreated.
- API consumers must not fabricate AgentCreated.
- AgentCreated is actor registration trace, not authorization for unrestricted actions.
```

---

# 8. API Operations

## 8.1 Operation: Create Agent

**Operation Category:** Create  
**Method:** POST  
**Path:** `/agents`  
**Owning Service Operation:** `createAgent`  
**Permission Required:** `agent:create`  
**Policy Required:** `AgentCreationPolicy`  
**AI Agent Access:** Not Allowed to self-create unless governed system bootstrap  
**Event Behavior:** Service Must Emit AgentCreated

Meaning:

```text
Create a governed Agent reference.
```

Non-meaning:

```text
does not grant unrestricted permissions
does not create User
does not create Service Provider
does not approve professional authority
does not allow autonomous filing
does not bypass Policy
```

Expected service call:

```text
API
  ↓
Permission Service evaluatePermission
  ↓
Policy Service evaluatePolicy
  ↓
Agent Service createAgent
  ↓
Event Service record AgentCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Agent

**Operation Category:** Read  
**Method:** GET  
**Path:** `/agents/{agent_reference_id}`  
**Owning Service Operation:** `getAgent`  
**Permission Required:** `agent:read`  
**Policy Required:** `AgentVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Agent view.
```

Non-meaning:

```text
does not expose credentials
does not expose full prompts or tools automatically
does not expose restricted capability policy
does not grant execution permission
```

## 8.3 Operation: Search Agents

**Operation Category:** Search  
**Method:** GET  
**Path:** `/agents`  
**Owning Service Operation:** `searchAgents`  
**Permission Required:** `agent:search`  
**Policy Required:** `AgentVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Agent references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted agent registry access
does not expose credentials, prompts, runtime secrets or restricted tools by default
```

## 8.4 Operation: Update Agent

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/agents/{agent_reference_id}`  
**Owning Service Operation:** `updateAgent`  
**Permission Required:** `agent:update`  
**Policy Required:** `AgentUpdatePolicy`  
**AI Agent Access:** Not Allowed for self-modifying authority unless explicitly governed  
**Event Behavior:** Service May Emit AgentUpdated where event is defined

Meaning:

```text
Update governed Agent metadata, status, capability boundary or lifecycle state under Agent Service rules.
```

Non-meaning:

```text
does not grant unrestricted tools
does not mutate Permission/Policy directly
does not approve autonomous execution
does not rewrite historical actions
```

## 8.5 Operation: Validate Agent Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/agents/reference/validate`  
**Owning Service Operation:** `validateAgentReference`  
**Permission Required:** `agent:validate`  
**Policy Required:** `AgentReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that an Agent reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not grant capability
does not authorize tool use
does not authorize knowledge access
does not authorize professional decision
```

## 8.6 Operation: Evaluate Agent Access

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/agents/{agent_reference_id}/access/evaluate`  
**Owning Service Operation:** `evaluateAgentAccess`  
**Permission Required:** `agent:access:evaluate`  
**Policy Required:** `AIAgentAccessPolicy`  
**AI Agent Access:** Allowed for self-check only under contract  
**Event Behavior:** Must route through Permission/Policy evaluation; may emit PermissionEvaluated and PolicyEvaluated

Meaning:

```text
Evaluate whether an Agent may perform a requested action in a specific context.
```

Non-meaning:

```text
does not execute the requested action
does not grant permanent permission
does not bypass downstream service policy
does not approve professional result
```

## 8.7 Operation: List Agent Capabilities

**Operation Category:** Read  
**Method:** GET  
**Path:** `/agents/{agent_reference_id}/capabilities`  
**Owning Service Operation:** `listAgentCapabilities`  
**Permission Required:** `agent:capability:read`  
**Policy Required:** `AgentCapabilityVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe capability boundaries available to an Agent.
```

Non-meaning:

```text
does not expose internal prompts or secrets
does not authorize capability execution
does not expose restricted tools by default
```

## 8.8 Operation: Prepare Agent Task Action

**Operation Category:** Action  
**Method:** POST  
**Path:** `/agents/{agent_reference_id}/tasks/prepare-action`  
**Owning Service Operation:** `prepareAgentTaskAction`  
**Permission Required:** `agent:task:prepare-action`  
**Policy Required:** `AgentTaskActionPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where action impacts business state  
**Event Behavior:** Must not emit TaskCreated unless Task Service creates Task

Meaning:

```text
Prepare a governed Task action request or draft using Agent context.
```

Non-meaning:

```text
does not create Task automatically
does not complete Task
does not execute work
does not approve professional output
```

## 8.9 Operation: Prepare Agent Communication Draft

**Operation Category:** Action  
**Method:** POST  
**Path:** `/agents/{agent_reference_id}/communications/prepare-draft`  
**Owning Service Operation:** `prepareAgentCommunicationDraft`  
**Permission Required:** `agent:communication:prepare-draft`  
**Policy Required:** `AgentCommunicationDraftPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired  
**Event Behavior:** Must not emit CommunicationCreated unless Communication Service creates Communication

Meaning:

```text
Prepare a governed Communication draft using Agent context.
```

Non-meaning:

```text
does not create Communication automatically
does not send message
does not approve external wording
does not create legal notice
```

## 8.10 Operation: Request Agent Knowledge Access

**Operation Category:** Action  
**Method:** POST  
**Path:** `/agents/{agent_reference_id}/knowledge/access-request`  
**Owning Service Operation:** `requestAgentKnowledgeAccess`  
**Permission Required:** `agent:knowledge:request-access`  
**Policy Required:** `AgentKnowledgeAccessPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** May emit PermissionEvaluated and PolicyEvaluated

Meaning:

```text
Request policy-filtered Knowledge access for a governed Agent operation.
```

Non-meaning:

```text
does not expose all Knowledge
does not bypass Knowledge policy
does not turn retrieved Knowledge into professional truth
does not allow unrestricted retrieval
```

## 8.11 Operation: List Agent Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/agents/{agent_reference_id}/events`  
**Owning Service Operation:** `listAgentEvents`  
**Permission Required:** `agent:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Agent-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Agent Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  agent_type: string
  agent_status: string | optional
  agent_name: string
  agent_purpose: string
  owner_user_reference_id: string | null
  owner_organization_reference_id: string | null
  capability_profile_reference_id: string | null
  runtime_profile_reference_id: string | null
  governance_profile_reference_id: string | null
  source_type: string
  safe_summary: string | null
  request_context: object
```

## 9.2 Update Agent Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  agent_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  agent_status: string | optional
  agent_name: string | optional
  agent_purpose: string | optional
  capability_profile_reference_id: string | optional
  governance_profile_reference_id: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Agent Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  agent_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Evaluate Agent Access Request

```yaml
body:
  actor_reference_id: string | null
  organization_reference_id: string | null
  requested_action: string
  target_object_type: string | null
  target_object_reference_id: string | null
  capability_required: string | null
  data_access_scope: string
  execution_mode: string
  request_context: object
```

## 9.5 Prepare Agent Task Action Request

```yaml
body:
  actor_reference_id: string | null
  organization_reference_id: string | null
  task_reference_id: string | null
  action_purpose: string
  requested_task_action: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
  human_review_required: boolean | null
  request_context: object
```

## 9.6 Prepare Agent Communication Draft Request

```yaml
body:
  actor_reference_id: string | null
  organization_reference_id: string | null
  draft_purpose: string
  communication_type: string
  subject_object_type: string | null
  subject_object_reference_id: string | null
  recipient_context:
    recipient_type: string | null
    recipient_reference_id: string | null
  human_review_required: boolean | null
  request_context: object
```

## 9.7 Request Agent Knowledge Access Request

```yaml
body:
  actor_reference_id: string | null
  organization_reference_id: string | null
  retrieval_purpose: string
  knowledge_scope: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include credentials, prompts, secrets, raw restricted documents or unrestricted Knowledge content by default.
- Requests must use controlled agent_type, agent_status, agent_purpose, source_type, execution_mode, data_access_scope and retrieval_purpose values.
- Agent self-requests must include agent_reference_id and must be governed by Agent Contract.
- Requested actions must be evaluated before downstream execution.
```

---

# 10. Response Contracts

## 10.1 Agent Response

```yaml
status: 200
body:
  agent_reference_id: string
  agent_type: string
  agent_status: string
  agent_name: string
  agent_purpose: string
  owner_user_reference_id: string | null
  owner_organization_reference_id: string | null
  capability_profile_reference_id: string | null
  governance_profile_reference_id: string | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    capability_summary: string | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Agent Response

```yaml
status: 201
body:
  agent_reference_id: string
  agent_status: string
  review_required: boolean
  related_event_reference_ids:
    - agent_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Agent Reference Validation Response

```yaml
status: 200
body:
  agent_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Agent Access Evaluation Response

```yaml
status: 200
body:
  agent_reference_id: string
  allowed: boolean
  access_decision: string
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
  allowed_capabilities: list[string]
  restricted_capabilities: list[string]
  human_review_required: boolean
  safe_reason: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.5 Agent Action Preparation Response

```yaml
status: 200
body:
  agent_reference_id: string
  prepared_action_reference_id: string | null
  preparation_status: string
  downstream_service_required: string | null
  human_review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Agent Knowledge Access Response

```yaml
status: 200
body:
  agent_reference_id: string
  knowledge_access_reference_id: string | null
  access_decision: string
  safe_knowledge_summaries: list[object]
  human_review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not expose credentials, prompts, runtime secrets or unrestricted tool definitions.
- Responses must not imply professional authority, legal conclusion, task completion, communication delivery or filing.
- Responses must distinguish Agent references from User and Service Provider references.
- Responses must identify review requirements for Agent-prepared actions.
```

---

# 11. Controlled Values

## 11.1 agent_type

```text
AIAgent
AutomationAgent
IntegrationAgent
WorkflowAgent
KnowledgeAgent
CommunicationAgent
RoutingAgent
SystemAgent
Unknown
```

## 11.2 agent_status

```text
Draft
Active
ReviewRequired
Suspended
Revoked
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 agent_purpose

```text
ClassificationAssistance
DocumentReview
EvidenceReview
IntakeAssistance
TaskPlanning
CommunicationDrafting
KnowledgeRetrieval
RoutingSupport
WorkflowSupport
AuditSupport
Unknown
```

## 11.4 source_type

```text
ProfessionalInput
SystemConfigured
OrganizationConfigured
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.5 execution_mode

```text
ReadOnly
DraftOnly
SuggestOnly
PrepareOnly
HumanReviewRequired
SystemApproved
NotAllowed
Unknown
```

## 11.6 data_access_scope

```text
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContent
NoAccess
Unknown
```

## 11.7 requested_task_action

```text
Summarize
PrepareDraft
SuggestNextStep
ValidateReference
PrepareCompletionDraft
RequestHumanReview
Unknown
```

## 11.8 access_decision

```text
Allowed
Denied
PolicyRestricted
PermissionDenied
HumanReviewRequired
ContractRequired
Unknown
```

## 11.9 preparation_status

```text
Prepared
Rejected
PolicyRestricted
PermissionDenied
HumanReviewRequired
DownstreamServiceRequired
Unknown
```

## 11.10 retrieval_purpose

```text
Read
Summarize
Draft
Recommend
Validate
Explain
AIAssistedWorkflow
Unknown
```

## 11.11 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Suspended
Revoked
ContextMismatch
Unknown
```

## 11.12 intended_use

```text
KnowledgeAccess
TaskPreparation
CommunicationDrafting
RoutingSupport
WorkflowSupport
AuditReference
AIAgentAction
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
agent:create
agent:read
agent:search
agent:update
agent:validate
agent:access:evaluate
agent:capability:read
agent:task:prepare-action
agent:communication:prepare-draft
agent:knowledge:request-access
agent:event:read
```

Rules:

```text
- Agent read/search must be permission-controlled.
- Agent creation must not grant unrestricted authority.
- Agent validation must not authorize execution.
- Agent access evaluation must be performed before downstream agent action.
- Agent knowledge access must be permission-controlled and policy-filtered.
- Downstream Task, Communication, Routing and Knowledge operations require their owning permissions.
- API must return PermissionDenied when actor or agent lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
AgentCreationPolicy
AgentUpdatePolicy
AgentVisibilityPolicy
AgentReferencePolicy
AIAgentAccessPolicy
AgentCapabilityVisibilityPolicy
AgentTaskActionPolicy
AgentCommunicationDraftPolicy
AgentKnowledgeAccessPolicy
EventVisibilityPolicy
RestrictedAgentDataPolicy
CrossOrganizationAgentPolicy
AgentSelfModificationPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Agent fields.
- Policy must restrict credentials, prompts, runtime settings, tools and system instructions.
- Policy may require human review for Agent-prepared actions.
- Policy may restrict cross-organization Agent lookup.
- Policy may restrict self-modification and self-authorization.
- Policy must restrict Knowledge access by scope and purpose.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Agent: Not Allowed except governed system bootstrap
Get Agent: Restricted
Search Agents: Restricted
Update Agent: Not Allowed for self-authority changes
Validate Agent Reference: Allowed under contract
Evaluate Agent Access: Allowed for self-check under contract
List Agent Capabilities: Restricted
Prepare Agent Task Action: Restricted / HumanReviewRequired
Prepare Agent Communication Draft: Restricted / HumanReviewRequired
Request Agent Knowledge Access: Restricted
List Agent Events: Restricted
```

AI Agents may:

```text
validate their own reference under contract
request access evaluation before action
request policy-filtered Knowledge access
prepare Task action drafts for human review
prepare Communication drafts for human review
summarize safe Agent metadata where allowed
```

AI Agents must not:

```text
create themselves
grant themselves permissions
modify their own authority
fabricate AgentCreated events
bypass Permission or Policy
act as human professional
act as Service Provider
treat retrieved Knowledge as final professional truth
complete Tasks or send Communications directly through Agent API
expose credentials, prompts or restricted tool settings
```

AI access requires:

```text
agent_identity_reference_id
agent_contract_reference_id
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 15. Event Access Rules

Agent API may expose:

```text
AgentCreated
PermissionEvaluated
PolicyEvaluated
TaskCreated
CommunicationCreated
RoutingEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Agent events directly.
- AgentCreated must not be treated as permission grant, professional authority or autonomous runtime approval.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] agent_reference_id is present where required.
[ ] actor_reference_id is present for protected human/system operations.
[ ] organization_reference_id is valid where provided.
[ ] owner_user_reference_id is valid where provided.
[ ] owner_organization_reference_id is valid where provided.
[ ] capability_profile_reference_id is valid where provided.
[ ] governance_profile_reference_id is valid where provided.
[ ] target_object_type and target_object_reference_id are valid where provided.
[ ] agent_type is controlled.
[ ] agent_status is controlled.
[ ] agent_purpose is controlled.
[ ] source_type is controlled.
[ ] execution_mode is controlled.
[ ] data_access_scope is controlled.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted credentials/prompts/tools/runtime fields are omitted or allowed.
[ ] Agent Contract is present where required.
[ ] AgentCreated is emitted after createAgent succeeds.
[ ] Access evaluation does not execute downstream action.
[ ] Knowledge access is policy-filtered.
[ ] Task and Communication preparation do not create or send downstream objects automatically.
[ ] Response shape is safe.
```

---

# 17. Error Handling

Controlled errors:

```text
BadRequest
Unauthorized
PermissionDenied
PolicyRestricted
NotFound
AgentReferenceInvalid
UserReferenceInvalid
OrganizationReferenceInvalid
CapabilityProfileInvalid
GovernanceProfileInvalid
TargetContextInvalid
AgentContractRequired
SelfModificationRestricted
AccessDenied
KnowledgeAccessRestricted
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedAgentData
HumanReviewRequired
EventEmissionFailed
InternalError
```

Error response:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Error rules:

```text
- Errors must not expose restricted Agent data.
- Errors must not expose credentials, prompts, runtime settings, tools or system instructions.
- Errors must not expose unrelated User, Organization, Knowledge, Task or Communication details.
- Errors must not expose permission or policy internals.
- Errors must be safe for product/API consumers.
```

---

# 18. Versioning Rules

API version:

```text
v0.1.0
```

Versioning rules:

```text
- Breaking changes require new version or explicit migration rule.
- agent_type, agent_status, agent_purpose, execution_mode and data_access_scope changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI Agent access and execution-boundary behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Agent API spec
cite Agent Service Specification
cite Agent Object Specification
cite AgentCreated Event Specification
cite AI Agent Governance Specification
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid agent_reference_id
write tests for invalid owner/user/organization/profile references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Agent creation does not grant unrestricted authority
write tests that Agent validation does not authorize execution
write tests that Agent cannot self-modify authority without policy
write tests that Knowledge access is policy-filtered
write tests that Task/Communication preparation does not execute downstream action
write tests for Agent Contract and human review requirement
write tests for AgentCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Agent Service
allow UI to emit AgentCreated directly
treat Agent as User
treat Agent as Service Provider
treat Agent as human professional or final legal authority
grant permissions from Agent API directly
expose credentials, prompts, tools or runtime secrets for convenience
allow AI to fabricate Agent references or events
allow AI to bypass Permission, Policy, Knowledge, Task or Communication services
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Agent API purpose.
[ ] It defines Agent API meaning.
[ ] It defines Agent API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, access evaluation, capability listing, task preparation, communication draft preparation, knowledge access and event-list operations.
[ ] It defines request contracts.
[ ] It defines response contracts.
[ ] It defines controlled values.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent access rules.
[ ] It defines Event access rules.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It defines versioning rules.
[ ] It includes Codex implementation notes.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Agent API specification. Defines governed Agent registration and execution-boundary interface and separates Agent API from User, Service Provider, professional authority, unrestricted runtime, Knowledge bypass, Task execution and AI autonomous action. |

---

**End of API Specification**
