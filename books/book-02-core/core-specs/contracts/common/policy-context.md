# Common Contract — Policy Context

**Spec ID:** B02-CONTRACT-COMMON-POLICY-CONTEXT  
**Spec Type:** Common Contract Specification  
**Contract Name:** Policy Context Contract  
**Contract File:** core-specs/contracts/common/policy-context.md  
**Contract Category:** Common  
**Related Owning Spec:** core-specs/contracts/README.md  
**Related Domain:** Policy  
**Related Object Specs:** core-specs/objects/policy.md; core-specs/objects/permission.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/agent.md; all Core object specifications where policy-gated behavior exists  
**Related Service Specs:** core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/agent-service.md; all Core service specifications where policy-controlled operations exist  
**Related API Specs:** core-specs/api/policy-api.md; all Core API specifications where policy-controlled operations exist  
**Related Event Specs:** core-specs/events/policy-evaluated.md; core-specs/events/permission-evaluated.md  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md; core-specs/agents/knowledge-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/audit-agent.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Policy Context Contract defines the canonical policy context shape used across MarkOrbit Core.

It standardizes how APIs, services, workflows, agents and validators represent contextual policy evaluation, policy scope, policy decision result, data visibility, allowed/downgraded behavior, restricted-field omission, human-review requirement and policy decision trace before a protected operation continues.

This contract governs:

```text
policy evaluation context
policy scope
actor and organization context
agent context
target object context
intended operation
data access scope
field visibility
policy decision result
policy decision reference
policy restrictions
policy-required human review
safe policy errors
Codex implementation rules
```

Policy Context Contract does not grant permission, evaluate permission, implement policy logic by itself, replace Policy Service, replace Permission Service or define product-specific business policy text.

---

# 2. Contract Meaning

This contract means:

```text
a common Core agreement for carrying policy-evaluation context and policy-decision trace.
```

This contract does not mean:

```text
policy engine
business rule implementation
permission grant
role model
human approval
legal conclusion
professional standard itself
product settings screen
```

Core rule:

```text
Policy context requests or records contextual policy evaluation.
Permission Service decides whether an actor may act.
Policy Service decides whether context allows or restricts the action.
Valid policy context is not policy approval by itself.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
policy context field names
policy scope shape
target object context
data access scope shape
policy decision reference shape
policy result shape
restricted field omission shape
policy-required human review shape
safe policy error linkage
Codex validation expectations
```

This contract is not responsible for:

```text
authenticating users
granting permissions
assigning roles
implementing policy rules
executing protected operations
creating events directly
approving professional action
choosing product UX
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
core-specs/contracts/common/permission-context.md
```

Owning rule:

```text
Policy Context Contract defines the shape of policy context and decision trace. It must not be treated as Policy Service implementation or policy approval by itself.
```

---

# 5. Related Core Objects

Primary related objects:

```text
Policy
Permission
User
Organization
Agent
Event
```

Applies to policy-controlled operations across:

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
- Policy object/domain owns policy structure.
- Policy Service owns policy evaluation.
- Related domain services decide whether policy evaluation is required.
- Permission Service must not be replaced by Policy Context.
```

---

# 6. Required References

Policy context shape:

```yaml
policy_context:
  policy_context_reference_id: string | null
  policy_decision_reference_id: string | null
  permission_decision_reference_id: string | null
  actor_reference_id: string | null
  actor_type: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  agent_registry_key: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  intended_operation: string
  required_policy_scopes: list[string]
  requested_data_access_scope: string | null
  evaluated_data_access_scope: string | null
  policy_decision: string | null
  restriction_mode: string | null
  restricted_fields_omitted: boolean
  human_review_required: boolean | null
  decision_reason_safe: string | null
  evaluated_at: datetime | null
  correlation_id: string | null
```

Rules:

```text
- intended_operation is required for policy-controlled operations.
- required_policy_scopes is required when policy evaluation is needed.
- actor or governed agent/system context is required.
- organization_reference_id is required for organization-scoped policy.
- agent_reference_id and agent_registry_key are required for agent-assisted protected operations.
- policy_decision_reference_id is required where prior policy evaluation is relied on.
```

---

# 7. Contract Shape

Canonical policy context shape:

```yaml
policy_context:
  policy_context_reference_id: string | null
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
    required_policy_scopes: list[string]
  access:
    requested_data_access_scope: string | null
    evaluated_data_access_scope: string | null
    restricted_fields_omitted: boolean
    omitted_field_groups: list[string]
  decision:
    policy_decision_reference_id: string | null
    policy_decision: string | null
    restriction_mode: string | null
    decision_reason_safe: string | null
    evaluated_at: datetime | null
  governance:
    permission_decision_reference_id: string | null
    human_review_required: boolean | null
    human_review_reference_id: string | null
  trace:
    correlation_id: string | null
    event_reference_ids: list[string]
```

Minimal downstream reliance shape:

```yaml
policy_context:
  policy_decision_reference_id: string | null
  required_policy_scopes: list[string]
  policy_decision: string | null
  evaluated_data_access_scope: string | null
  restricted_fields_omitted: boolean
  human_review_required: boolean | null
```

Rules:

```text
- Full shape is required for policy evaluation request/response.
- Minimal shape may be used only to reference a completed decision where owning service permits it.
- Policy decision must be fresh enough for the operation where freshness policy applies.
- Policy context may reference permission_decision_reference_id but must not replace Permission Context.
```

---

# 8. Field Rules

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| policy_context_reference_id | string | No | Yes | Optional context reference. |
| policy_decision_reference_id | string | Contextual | Yes | Required when relying on existing policy decision. |
| permission_decision_reference_id | string | Contextual | Yes | Required where policy evaluation depends on permission decision. |
| actor_type | string | Contextual | Yes | Must use controlled value. |
| actor_reference_id | string | Contextual | Yes | Required unless governed system/agent context is allowed. |
| organization_reference_id | string | Contextual | Yes | Required for organization-scoped policy. |
| agent_reference_id | string | Contextual | Yes | Required for governed Agent operations. |
| agent_registry_key | string | Contextual | Yes | Required where Agent Registry applies. |
| target_object_type | string | Contextual | Yes | Must follow Reference Contract. |
| target_object_reference_id | string | Contextual | Yes | Must match target_object_type. |
| intended_operation | string | Yes | No | Must identify policy-controlled operation. |
| required_policy_scopes | list[string] | Yes for policy-controlled operation | No | Must contain at least one scope where policy applies. |
| requested_data_access_scope | string | Contextual | Yes | Requested scope before policy evaluation. |
| evaluated_data_access_scope | string | Contextual | Yes | Final allowed/downgraded scope after policy evaluation. |
| policy_decision | string | Contextual | Yes | Must use controlled value where provided. |
| restriction_mode | string | Contextual | Yes | Must use controlled value where provided. |
| restricted_fields_omitted | boolean | Yes where safe response returned | No | True when fields are omitted by policy. |
| human_review_required | boolean | Contextual | Yes | Must be explicit where policy requires review. |
| decision_reason_safe | string | No | Yes | Must not expose policy internals. |
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

## 9.3 policy_decision

```text
Allowed
Denied
Restricted
Downgraded
RequiresHumanReview
NotEvaluated
Expired
Invalid
Unknown
```

## 9.4 restriction_mode

```text
Allow
Deny
Redact
OmitFields
DowngradeAccess
RequireHumanReview
ReturnNotFound
ReturnEmpty
Escalate
Unknown
```

## 9.5 data_access_scope

```text
NoAccess
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContentWithHumanApproval
Unknown
```

## 9.6 omitted_field_group

```text
PrivateContact
Pricing
FinancialData
RawDocument
RawEvidence
PrivilegedNotes
PolicyInternals
PermissionInternals
ProviderTerms
CustomerPrivateInstructions
AgentPromptContext
SystemInternal
Unknown
```

## 9.7 policy_scope pattern

```text
<domain>:<policy-purpose>
<domain>:<operation>:policy
agent:<agent-domain>:policy
data-visibility:<scope>
cross-organization:<scope>
```

Examples:

```text
communication:send:policy
communication:draft:policy
task:completion:policy
routing:selection:policy
workflow:application:policy
document:visibility:policy
evidence:visibility:policy
agent:communication:policy
data-visibility:restricted-content
cross-organization:communication
```

Rules:

```text
- Policy scopes must be lowercase kebab-case or colon-separated controlled scopes.
- Policy scopes must be defined by owning Policy/API/Service specs.
- Unknown is not valid for production policy decisions.
```

---

# 10. Validation Rules

Validation checklist:

```text
[ ] intended_operation is present.
[ ] required_policy_scopes are present for policy-controlled operation.
[ ] actor_type is controlled where provided.
[ ] actor_reference_id or governed agent/system context is present.
[ ] organization_reference_id is present for organization-scoped policy.
[ ] agent_reference_id and agent_registry_key are present for Agent operations.
[ ] target object reference follows Reference Contract.
[ ] required_policy_scopes follow policy scope pattern.
[ ] requested_data_access_scope is controlled where provided.
[ ] evaluated_data_access_scope is controlled where provided.
[ ] policy_decision is controlled where provided.
[ ] restriction_mode is controlled where provided.
[ ] restricted_fields_omitted is set correctly.
[ ] omitted_field_groups are controlled where provided.
[ ] human_review_required is explicit where policy requires review.
[ ] policy_decision_reference_id is valid where relied on.
[ ] evaluated_at is present where decision is completed.
[ ] policy decision freshness satisfies operation requirement where applicable.
[ ] decision_reason_safe does not expose policy internals.
```

---

# 11. Permission Rules

Policy is not permission.

Rules:

```text
- Permission Service must evaluate whether actor may attempt the operation.
- Policy Service evaluates whether context allows, restricts, redacts or downgrades the operation.
- Policy Context may reference permission_decision_reference_id.
- Permission Allowed does not bypass policy.
- PermissionDenied must stop before policy-controlled protected behavior proceeds.
```

Required sequence:

```text
operation request
↓
Permission Context / Permission Service
↓
Policy Context / Policy Service
↓
owning service behavior
↓
event/audit trace
```

---

# 12. Policy Rules

This contract carries policy context but does not evaluate policy.

Rules:

```text
- Policy Service must evaluate required_policy_scopes.
- A populated policy_context is not proof of policy allowance unless policy_decision permits it and decision reference is valid.
- Denied, Expired, Invalid or NotEvaluated must stop protected behavior.
- Restricted or Downgraded must be enforced by owning service.
- RequiresHumanReview must require Human Review Contract before downstream use.
- Owning service must confirm required_policy_scopes match intended operation.
```

Policy evaluation flow:

```text
build policy_context
↓
Policy Service evaluates required_policy_scopes
↓
policy_decision_reference_id returned
↓
owning service enforces decision
↓
Event Service records trace where applicable
```

---

# 13. AI Agent Rules

Agent-assisted policy context must include:

```yaml
agent:
  agent_reference_id: string
  agent_registry_key: string
  agent_contract_reference_id: string | null
```

Rules:

```text
- Agent capability does not equal policy allowance.
- Agent Registry eligibility does not equal policy allowance.
- Agent must not fabricate policy_decision_reference_id.
- Agent must not claim policy is Allowed unless Policy Service provided valid decision.
- AI output must disclose policy_omissions, restricted_fields_omitted and human_review_required.
- AI prompt/context construction must use evaluated_data_access_scope.
```

---

# 14. Event Rules

Policy evaluation may produce:

```text
PolicyEvaluated
```

Rules:

```text
- Policy Context does not emit events directly.
- Policy Service owns PolicyEvaluated event emission.
- Event payload must not expose restricted policy internals by default.
- policy_decision_reference_id may be included in downstream audit context where policy allows.
```

---

# 15. Error Rules

Controlled policy context errors:

```text
PolicyContextInvalid
PolicyScopeInvalid
PolicyDecisionInvalid
PolicyDecisionExpired
PolicyDecisionReferenceInvalid
PolicyRestricted
PolicyContextMismatch
DataAccessScopeInvalid
DataAccessScopeExceeded
RestrictedFieldViolation
PolicyRequiresHumanReview
PolicyReturnNotFound
PolicyReturnEmpty
AgentPolicyRestricted
CrossOrganizationPolicyRestricted
```

Safe error shape:

```yaml
error:
  code: string
  category: Policy | Validation | Reference | Agent | HumanReview
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Errors must not expose policy internals.
- Errors must not expose restricted object existence where policy forbids it.
- PolicyRestricted must stop or downgrade protected behavior.
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
- Adding policy_decision values requires revision notes.
- Adding restriction_mode values requires revision notes.
- Changing policy scope pattern is breaking.
- Renaming policy context fields is breaking.
- Changing meaning of Downgraded or RequiresHumanReview is breaking unless versioned.
```

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this Policy Context Contract before implementing policy-controlled operations
build policy_context before protected service behavior
invoke Permission Service before Policy Service where permission applies
invoke Policy Service for evaluation
validate required_policy_scopes
validate actor/agent/organization references
preserve policy_decision_reference_id
preserve correlation_id
use Error Contract for policy errors
use Reference Contract for target references
use AI Context Contract for AI-assisted policy behavior
use Human Review Contract where policy requires review
enforce evaluated_data_access_scope
omit restricted fields when policy requires
write tests for missing required_policy_scopes
write tests for invalid policy scope
write tests for PolicyRestricted
write tests for Downgraded
write tests for RequiresHumanReview
write tests for DataAccessScopeExceeded
write tests for restricted_fields_omitted
write tests that Permission Allowed does not bypass Policy
```

Codex must not:

```text
treat policy_context as policy approval without Policy Service decision
treat Agent Registry eligibility as policy allowance
skip Permission evaluation where permission applies
expose policy internals in errors
fabricate policy_decision_reference_id
reuse policy decision for incompatible target/operation/context
allow unrestricted data access after downgrade
allow AI prompt/context to exceed evaluated_data_access_scope
emit PolicyEvaluated directly from API contract
```

---

# 18. Acceptance Criteria

This Policy Context Contract is accepted only if:

```text
[ ] It defines policy context purpose.
[ ] It defines policy context meaning.
[ ] It defines policy context boundary.
[ ] It cites related owning spec and common contracts.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines canonical policy context shape.
[ ] It defines minimal downstream reliance shape.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines policy scope pattern.
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
| 0.1.0 | Draft | Initial common Policy Context Contract. Defines policy context shape, policy scope pattern, access-scope control, restriction modes, decision trace, validation, relationship to Permission, AI Agent rules, event rules, errors and Codex implementation notes. |

---

**End of Common Contract**
