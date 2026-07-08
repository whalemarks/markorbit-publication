# Common Contract — Permission Context

**Spec ID:** B02-CONTRACT-COMMON-PERMISSION-CONTEXT  
**Spec Type:** Common Contract Specification  
**Contract Name:** Permission Context Contract  
**Contract File:** core-specs/contracts/common/permission-context.md  
**Contract Category:** Common  
**Related Owning Spec:** core-specs/contracts/README.md  
**Related Domain:** Permission  
**Related Object Specs:** core-specs/objects/permission.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/agent.md; all Core object specifications where permission-gated operations exist  
**Related Service Specs:** core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md; all Core service specifications where protected operations exist  
**Related API Specs:** core-specs/api/permission-api.md; all Core API specifications where protected operations exist  
**Related Event Specs:** core-specs/events/permission-evaluated.md  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Permission Context Contract defines the canonical permission context shape used across MarkOrbit Core.

It standardizes how APIs, services, workflows, agents and validators represent the actor, organization, agent, target object, intended operation, required permission keys, permission decision result and permission decision trace before a protected operation continues.

This contract governs:

```text
permission evaluation context
actor reference
organization reference
agent reference
target object reference
intended operation
required permission keys
permission decision result
permission decision reference
permission denial handling
permission trace
permission-related safe errors
Codex implementation rules
```

Permission Context Contract does not grant permission, evaluate permission by itself, replace Permission Service, replace Policy Service or define product roles.

---

# 2. Contract Meaning

This contract means:

```text
a common Core agreement for carrying permission-evaluation context and permission-decision trace.
```

This contract does not mean:

```text
permission engine
role model
access-control implementation
policy evaluation
business approval
human review
authentication token
product role design
```

Core rule:

```text
Permission context requests or records permission evaluation.
Permission Service decides permission.
Policy Service decides contextual restrictions.
Valid permission context is not permission approval by itself.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
permission context field names
actor/organization/agent target context
required permission key shape
permission decision reference shape
permission result shape
permission denial trace
safe permission error linkage
Codex validation expectations
```

This contract is not responsible for:

```text
authenticating users
granting roles
assigning permissions
evaluating permission rules
evaluating policies
executing protected operations
creating events directly
approving professional action
```

---

# 4. Related Owning Spec

Owning spec:

```text
core-specs/contracts/README.md
```

Related common contracts:

```text
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/common/policy-context.md
```

Owning rule:

```text
Permission Context Contract defines the shape of permission context and decision trace. It must not be treated as Permission Service implementation or permission approval by itself.
```

---

# 5. Related Core Objects

Primary related objects:

```text
Permission
User
Organization
Agent
Policy
Event
```

Applies to protected operations across:

```text
Identity
Organization
User
Permission
Policy
Knowledge
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
Customer
Matter
Order
Opportunity
WorkflowContract
Task
Event
Notification
Communication
Agent
ServiceProvider
Routing
Partner
ServiceNetwork
```

Rules:

```text
- Permission object/domain owns permission structure.
- Permission Service owns permission evaluation.
- Related domain services decide whether an operation requires permission.
- Policy Service may further restrict an operation after permission allows it.
```

---

# 6. Required References

Permission context shape:

```yaml
permission_context:
  permission_context_reference_id: string | null
  permission_decision_reference_id: string | null
  actor_reference_id: string | null
  actor_type: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  agent_registry_key: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  intended_operation: string
  required_permission_keys: list[string]
  permission_decision: string | null
  decision_reason_safe: string | null
  evaluated_at: datetime | null
  correlation_id: string | null
```

Rules:

```text
- intended_operation is required for protected operations.
- required_permission_keys is required when permission evaluation is needed.
- actor_reference_id or governed agent/system context is required.
- organization_reference_id is required for organization-scoped operations.
- agent_reference_id and agent_registry_key are required for agent-assisted protected operations.
- permission_decision_reference_id is required where prior permission evaluation is relied on.
```

---

# 7. Contract Shape

Canonical permission context shape:

```yaml
permission_context:
  permission_context_reference_id: string | null
  actor:
    actor_type: string | null
    actor_reference_id: string | null
    organization_reference_id: string | null
  agent:
    agent_reference_id: string | null
    agent_registry_key: string | null
    agent_contract_reference_id: string | null
  target:
    target_object_type: string | null
    target_object_reference_id: string | null
  operation:
    intended_operation: string
    operation_category: string | null
    required_permission_keys: list[string]
  decision:
    permission_decision_reference_id: string | null
    permission_decision: string | null
    decision_reason_safe: string | null
    evaluated_at: datetime | null
  trace:
    correlation_id: string | null
    event_reference_ids: list[string]
```

Minimal downstream reliance shape:

```yaml
permission_context:
  permission_decision_reference_id: string | null
  required_permission_keys: list[string]
  permission_decision: string | null
```

Rules:

```text
- Full shape is required for permission evaluation request/response.
- Minimal shape may be used only to reference a completed decision where owning service permits it.
- Permission decision must be fresh enough for the operation where freshness policy applies.
- Permission context must not include policy decision fields except by reference to Policy Context.
```

---

# 8. Field Rules

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| permission_context_reference_id | string | No | Yes | Optional context reference. |
| permission_decision_reference_id | string | Contextual | Yes | Required when relying on existing permission decision. |
| actor_type | string | Contextual | Yes | Must use controlled value. |
| actor_reference_id | string | Contextual | Yes | Required unless governed system/agent context is allowed. |
| organization_reference_id | string | Contextual | Yes | Required for organization-scoped permission. |
| agent_reference_id | string | Contextual | Yes | Required for governed Agent operations. |
| agent_registry_key | string | Contextual | Yes | Required where Agent Registry applies. |
| target_object_type | string | Contextual | Yes | Must follow Reference Contract. |
| target_object_reference_id | string | Contextual | Yes | Must match target_object_type. |
| intended_operation | string | Yes | No | Must identify protected operation. |
| operation_category | string | Contextual | Yes | Must use controlled value where provided. |
| required_permission_keys | list[string] | Yes for protected operation | No | Must contain at least one key where permission check applies. |
| permission_decision | string | Contextual | Yes | Must use controlled value where provided. |
| decision_reason_safe | string | No | Yes | Must not expose permission internals. |
| evaluated_at | datetime | Contextual | Yes | Required where decision is completed. |
| correlation_id | string | No | Yes | Must be preserved where provided. |

---

# 9. Controlled Values

## 9.1 actor_type

```text
User
Agent
System
Integration
Service
Unknown
```

## 9.2 operation_category

```text
Create
Read
Search
Update
Delete
Validate
Evaluate
Apply
Prepare
Draft
Review
Approve
Reject
Link
Unlink
Assign
TransitionState
Send
Select
Export
Import
AgentAction
WorkflowAction
SystemAction
Unknown
```

## 9.3 permission_decision

```text
Allowed
Denied
Conditional
NotEvaluated
Expired
Invalid
Unknown
```

## 9.4 permission_key pattern

```text
<domain>:<operation>
<domain>:<object>:<operation>
agent:<agent-domain>:<operation>
data-scope:<scope>
```

Examples:

```text
task:read
task:create
communication:draft:prepare
communication:send
routing:evaluate
routing:select
agent:communication:prepare-draft
document:read
evidence:read
```

Rules:

```text
- Permission keys must be lowercase kebab-case or colon-separated controlled keys.
- Permission keys must be defined by owning Permission/API/Service specs.
- Wildcard permissions are not allowed in public contracts unless explicitly governed.
```

---

# 10. Validation Rules

Validation checklist:

```text
[ ] intended_operation is present.
[ ] required_permission_keys are present for protected operation.
[ ] actor_type is controlled where provided.
[ ] actor_reference_id or governed agent/system context is present.
[ ] organization_reference_id is present for organization-scoped operations.
[ ] agent_reference_id and agent_registry_key are present for Agent operations.
[ ] target object reference follows Reference Contract.
[ ] required_permission_keys follow permission key pattern.
[ ] permission_decision is controlled where provided.
[ ] permission_decision_reference_id is valid where relied on.
[ ] evaluated_at is present where decision is completed.
[ ] permission decision freshness satisfies operation requirement where applicable.
[ ] decision_reason_safe does not expose permission internals.
```

---

# 11. Permission Rules

This contract carries permission context but does not grant permission.

Rules:

```text
- Permission Service must evaluate permission.
- A populated permission_context is not proof of permission unless permission_decision = Allowed and decision reference is valid.
- Conditional permission must be resolved before protected operation continues unless owning service explicitly accepts conditional behavior.
- Denied, Expired, Invalid or NotEvaluated must stop protected behavior.
- Owning service must confirm required permission keys match intended operation.
```

Permission evaluation flow:

```text
operation request
↓
build permission_context
↓
Permission Service evaluates required_permission_keys
↓
permission decision reference returned
↓
Policy Service evaluates contextual restrictions
↓
owning service continues, rejects or downgrades
```

---

# 12. Policy Rules

Permission is not policy.

Rules:

```text
- Permission Allowed does not mean Policy Allowed.
- Policy Context must be evaluated separately where policy applies.
- Policy may restrict, downgrade or block an operation even after permission allows it.
- Permission context must not include hidden policy internals.
```

Common policies related to permission context:

```text
PermissionDecisionVisibilityPolicy
CrossOrganizationPermissionPolicy
AgentPermissionPolicy
RestrictedPermissionTracePolicy
PermissionDecisionFreshnessPolicy
```

---

# 13. AI Agent Rules

Agent-assisted permission context must include:

```yaml
agent:
  agent_reference_id: string
  agent_registry_key: string
  agent_contract_reference_id: string | null
```

Rules:

```text
- Agent capability does not equal permission.
- Agent Registry eligibility does not equal permission.
- Agent must not fabricate permission_decision_reference_id.
- Agent must not claim permission is Allowed unless Permission Service provided valid decision.
- AI output must disclose PermissionDenied where operation is blocked.
```

---

# 14. Event Rules

Permission evaluation may produce:

```text
PermissionEvaluated
```

Rules:

```text
- Permission Context does not emit events directly.
- Permission Service owns PermissionEvaluated event emission.
- Event payload must not expose restricted permission internals by default.
- permission_decision_reference_id may be included in downstream audit context where policy allows.
```

---

# 15. Error Rules

Controlled permission context errors:

```text
PermissionContextInvalid
PermissionKeyInvalid
PermissionDecisionInvalid
PermissionDecisionExpired
PermissionDecisionReferenceInvalid
PermissionDenied
PermissionContextMismatch
ActorReferenceInvalid
AgentPermissionDenied
OrganizationPermissionDenied
TargetPermissionDenied
```

Safe error shape:

```yaml
error:
  code: string
  category: Permission | Validation | Reference | Agent
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Errors must not expose permission internals.
- Errors must not expose restricted object existence where policy forbids it.
- PermissionDenied must stop protected behavior.
```

---

# 16. Versioning Rules

Contract version:

```text
v0.1.0
```

Rules:

```text
- Adding operation_category values requires revision notes.
- Adding permission_decision values requires revision notes.
- Changing permission key pattern is breaking.
- Renaming permission context fields is breaking.
- Changing meaning of Conditional is breaking unless versioned.
```

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this Permission Context Contract before implementing protected operations
build permission_context before protected service behavior
invoke Permission Service for evaluation
validate required_permission_keys
validate actor/agent/organization references
preserve permission_decision_reference_id
preserve correlation_id
use Error Contract for permission errors
use Reference Contract for target references
invoke Policy Service separately after permission where policy applies
write tests for missing required_permission_keys
write tests for invalid permission key
write tests for PermissionDenied
write tests for Conditional permission
write tests for expired permission decision
write tests for Agent capability not equal permission
write tests that permission allowed does not bypass policy
```

Codex must not:

```text
treat permission_context as permission grant without Permission Service decision
treat Agent Registry eligibility as permission
skip Policy evaluation after permission
expose permission internals in errors
fabricate permission_decision_reference_id
reuse permission decision for incompatible target/operation
allow wildcard permission without governed specification
emit PermissionEvaluated directly from API contract
```

---

# 18. Acceptance Criteria

This Permission Context Contract is accepted only if:

```text
[ ] It defines permission context purpose.
[ ] It defines permission context meaning.
[ ] It defines permission context boundary.
[ ] It cites related owning spec and common contracts.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines canonical permission context shape.
[ ] It defines minimal downstream reliance shape.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent rules.
[ ] It defines Event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial common Permission Context Contract. Defines permission context shape, required references, permission key pattern, decision trace, validation, relationship to Policy, AI Agent rules, event rules, errors and Codex implementation notes. |

---

**End of Common Contract**
