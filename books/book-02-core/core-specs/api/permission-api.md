# API Specification — Permission API

**Spec ID:** B02-API-PERMISSION  
**Spec Type:** API Specification  
**API Name:** Permission API  
**API File:** core-specs/api/permission-api.md  
**Related Domain:** core-specs/domains/permission.md  
**Related Object Specs:** core-specs/objects/permission.md; core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/permission-service.md; core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/permission-api-contract.md; core-specs/contracts/events/permission-evaluated-payload.md  
**Related Agent Specs:** core-specs/agents/permission-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Permission API exposes governed permission evaluation operations for MarkOrbit Core.

It allows authorized consumers to evaluate whether an actor may perform an action on a target context without treating Permission as Policy, User role, Organization membership, workflow approval, business responsibility, legal authority or AI authorization by itself.

Permission API exists to support:

```text
action authorization decision
actor/action/resource evaluation
user and identity access control
organization-scoped operation guard
API operation protection
event access protection
AI Agent action boundary
audit trace for permission decisions
```

Permission API does not create professional truth, approve business decisions, evaluate contextual policy constraints or bypass workflow gates.

---

# 2. API Meaning

Permission API means:

```text
a governed interface for evaluating whether an actor is allowed to perform a requested action in a specific context.
```

Permission API does not mean:

```text
Policy API
role management API
User API
Organization membership API
business responsibility API
workflow approval API
legal authority API
AI authority API
```

Permission determines allowed action.

Policy evaluates contextual constraints.

They must remain separate.

---

# 3. API Boundary

Permission API is responsible for:

```text
permission evaluation request intake
actor/action/target reference validation
permission decision generation through Permission Service
safe permission decision response shaping
permission evaluation event reference exposure
AI Agent action boundary support
controlled API errors
```

Permission API is not responsible for:

```text
Policy ownership
business responsibility ownership
workflow execution
Task assignment
professional decision approval
legal representative authority
role assignment lifecycle unless separately specified
User or Organization creation
AI reasoning truth
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/permission.md
```

Domain rule:

```text
Permission determines whether an actor may perform an action.
Permission is not Policy, workflow approval, business responsibility or professional truth.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/permission.md
core-specs/objects/identity.md
core-specs/objects/user.md
core-specs/objects/organization.md
core-specs/objects/policy.md
core-specs/objects/event.md
```

Object rules:

```text
- Permission API returns permission_decision_reference_id where decisions are recorded.
- Permission API must reference actor, action and target context.
- Permission API must not create User, Identity or Organization silently.
- Permission API must not treat User existence or Organization membership as permission decision by itself.
- Permission API must not treat Policy decision as Permission decision.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/permission-service.md
core-specs/services/identity-service.md
core-specs/services/user-service.md
core-specs/services/organization-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Permission API must invoke Permission Service for permission behavior.
- Permission API may validate Identity/User/Organization references through their owning services.
- Permission API may call Policy Service only when a combined guard endpoint explicitly requires Policy evaluation.
- Permission API must not emit PermissionEvaluated directly; Permission Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- evaluatePermission must result in PermissionEvaluated where decision recording is required.
- combined guard operations may also result in PolicyEvaluated.
- API consumers must not fabricate PermissionEvaluated.
- PermissionEvaluated is decision trace, not access token.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Evaluate Permission

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/permissions/evaluate`  
**Owning Service Operation:** `evaluatePermission`  
**Permission Required:** `permission:evaluate` or system-internal guard authority  
**Policy Required:** `PermissionEvaluationPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service Must Emit PermissionEvaluated where audit required

Meaning:

```text
Evaluate whether an actor may perform a requested action on a target context.
```

Non-meaning:

```text
does not evaluate Policy constraints by itself
does not grant a permanent permission
does not create role assignment
does not approve workflow
does not prove professional authority
```

Expected service call:

```text
API
  ↓
Identity/User/Organization reference validation where required
  ↓
Permission Service evaluatePermission
  ↓
Event Service record PermissionEvaluated where required
  ↓
Safe API response
```

## 8.2 Operation: Evaluate Access Guard

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/permissions/guard`  
**Owning Service Operation:** `evaluateAccessGuard`  
**Permission Required:** system-internal or `permission:guard:evaluate`  
**Policy Required:** `AccessGuardPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service May Emit PermissionEvaluated and PolicyEvaluated

Meaning:

```text
Evaluate Permission and, where required, Policy as a combined access guard for API operations.
```

Non-meaning:

```text
does not merge Permission and Policy concepts
does not grant permanent access
does not approve professional/business decision
```

## 8.3 Operation: Validate Permission Decision Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/permissions/decisions/reference/validate`  
**Owning Service Operation:** `validatePermissionDecisionReference`  
**Permission Required:** `permission:decision:validate`  
**Policy Required:** `PermissionDecisionVisibilityPolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a permission decision reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not re-authorize by itself
does not extend decision validity
does not bypass current evaluation requirements
```

## 8.4 Operation: Get Permission Decision

**Operation Category:** Read  
**Method:** GET  
**Path:** `/permissions/decisions/{permission_decision_reference_id}`  
**Owning Service Operation:** `getPermissionDecision`  
**Permission Required:** `permission:decision:read`  
**Policy Required:** `PermissionDecisionVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe view of a Permission decision trace.
```

Non-meaning:

```text
does not expose restricted rule internals
does not expose unrelated actor/resource data
does not act as current authorization decision unless still valid and explicitly allowed
```

## 8.5 Operation: List Permission Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/permissions/decisions/{permission_decision_reference_id}/events`  
**Owning Service Operation:** `listPermissionDecisionEvents`  
**Permission Required:** `permission:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Permission-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not replay Permission decision as command
```

---

# 9. Request Contracts

## 9.1 Evaluate Permission Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
body:
  actor_reference_id: string
  actor_type: string
  organization_reference_id: string | null
  action_key: string
  target_object_type: string
  target_object_reference_id: string | null
  request_context:
    source_api: string | null
    operation_category: string | null
    request_ip: string | null
    integration_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Evaluate Access Guard Request

```yaml
headers:
  X-Correlation-ID: string | optional
body:
  actor_reference_id: string
  actor_type: string
  organization_reference_id: string | null
  action_key: string
  target_object_type: string
  target_object_reference_id: string | null
  policy_scope: string | null
  request_context: object
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.3 Validate Permission Decision Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  permission_decision_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

Request rules:

```text
- Requests must include actor_reference_id, action_key and target context.
- Requests must use controlled actor_type and target_object_type values.
- Requests must not include restricted rule internals or secrets.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Permission Evaluation Response

```yaml
status: 200
body:
  permission_decision_reference_id: string
  actor_reference_id: string
  action_key: string
  target_object_type: string
  target_object_reference_id: string | null
  decision: string
  decision_status: string
  reason_code: string
  expires_at: datetime | null
  safe_summary:
    allowed: boolean
    restriction_summary: string | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Access Guard Response

```yaml
status: 200
body:
  permission_decision_reference_id: string
  policy_decision_reference_id: string | null
  allowed: boolean
  blocked_by: string | null
  permission_decision: string
  policy_decision: string | null
  safe_summary: object
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.3 Permission Decision Reference Validation Response

```yaml
status: 200
body:
  permission_decision_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

Response rules:

```text
- Responses must not expose restricted permission rule internals by default.
- Responses must not expose unrelated actor, user or organization data.
- Responses must not imply Policy pass unless Policy was actually evaluated.
- Responses must distinguish current evaluation result from historical decision trace.
```

---

# 11. Controlled Values

## 11.1 actor_type

```text
Identity
User
System
AIAgent
ExternalIntegration
Unknown
```

## 11.2 decision

```text
Allowed
Denied
Conditional
NotApplicable
Unknown
```

## 11.3 decision_status

```text
Evaluated
Valid
Expired
Revoked
Superseded
PolicyRestricted
PermissionDenied
Error
Unknown
```

## 11.4 target_object_type

```text
Identity
User
Organization
Knowledge
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
Customer
Order
Matter
Task
Event
Notification
Communication
Agent
ServiceProvider
Routing
Partner
ServiceNetwork
API
System
Unknown
```

## 11.5 intended_use

```text
CurrentAuthorization
AuditReference
EventAccess
APIGuard
AIAgentAction
ValidationOnly
Unknown
```

## 11.6 reason_code

```text
PermissionAllowed
PermissionDenied
PermissionConditional
ActorInvalid
ActionInvalid
TargetInvalid
OrganizationContextInvalid
PermissionRuleMissing
DecisionExpired
PolicyRequired
PolicyRestricted
AgentContractRequired
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
permission:evaluate
permission:guard:evaluate
permission:decision:validate
permission:decision:read
permission:event:read
```

Rules:

```text
- Permission evaluation endpoints must be protected against unrestricted probing.
- System-internal guard evaluation may use internal service authority.
- Reading decision traces requires separate permission.
- Permission validation does not authorize the original action.
- Permission decisions must be context-specific and time-sensitive where required.
```

---

# 13. Policy Rules

Policy scopes:

```text
PermissionEvaluationPolicy
AccessGuardPolicy
PermissionDecisionVisibilityPolicy
EventVisibilityPolicy
AIAgentPermissionAccessPolicy
```

Rules:

```text
- Policy may restrict who can evaluate permissions.
- Policy may restrict visibility into decision reasons.
- Policy may require AI Agent Contract for AI-originated permission evaluation.
- Policy may require re-evaluation for stale permission decisions.
- Policy failure must return safe PolicyRestricted error.
```

Permission and Policy separation:

```text
Permission answers: may this actor perform this action?
Policy answers: are contextual constraints satisfied?
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Evaluate Permission: Restricted
Evaluate Access Guard: Restricted
Validate Permission Decision Reference: Allowed under contract
Get Permission Decision: Restricted
List Permission Events: Restricted
```

AI Agents may:

```text
request permission evaluation for authorized planned actions
validate decision references where authorized
summarize safe decision outcome
flag missing actor/action/target context
explain that permission is not policy or professional approval
```

AI Agents must not:

```text
fabricate Permission decision
fabricate PermissionEvaluated event
override Permission result
treat Permission as Policy pass
treat Permission as workflow approval
treat Permission as legal authority
expose restricted permission internals
```

AI access requires:

```text
agent_identity_reference_id
agent_contract_reference_id where required
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 15. Event Access Rules

Permission API may expose:

```text
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Permission events directly.
- PermissionEvaluated must not be treated as permanent access token.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] actor_reference_id is present.
[ ] actor_type is controlled.
[ ] action_key is present.
[ ] target_object_type is controlled.
[ ] target_object_reference_id is valid where required.
[ ] organization_reference_id is valid where provided.
[ ] AI Agent Contract is present where required.
[ ] Permission Service is invoked for permission decision.
[ ] Policy Service is invoked only where required by operation.
[ ] PermissionEvaluated is emitted where audit/event trace is required.
[ ] Restricted permission internals are omitted.
[ ] Response distinguishes Permission from Policy.
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
ActorReferenceInvalid
ActionKeyInvalid
TargetReferenceInvalid
OrganizationReferenceInvalid
PermissionDecisionReferenceInvalid
ValidationFailed
DecisionExpired
RestrictedFieldViolation
AgentContractRequired
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
- Errors must not expose restricted permission rules.
- Errors must not expose policy internals.
- Errors must not expose private actor/resource data.
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
- decision and decision_status changes must be documented.
- Event behavior changes must be documented.
- Permission/Policy interaction changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Permission API spec
cite Permission Service Specification
cite Permission Object Specification
cite PermissionEvaluated Event Specification
cite Policy specs for Access Guard and policy-linked operations
implement request validation before service invocation
validate actor/action/target context
enforce AI Agent Contract where required
return safe responses by default
write tests for invalid actor/action/target references
write tests for PermissionDenied
write tests for PolicyRestricted on guarded operations
write tests for PermissionEvaluated event after required evaluations
write tests that Permission API does not grant permanent permission
write tests that Permission API does not treat Policy as Permission
write tests that restricted permission internals are hidden
```

Codex must not:

```text
write directly to database bypassing Permission Service
allow UI to emit PermissionEvaluated directly
treat User existence as Permission
treat Organization membership as Permission by itself
treat Permission decision as Policy pass
treat Permission decision as workflow approval
expose permission rule internals for convenience
allow AI to fabricate Permission decisions or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Permission API purpose.
[ ] It defines Permission API meaning.
[ ] It defines Permission API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines evaluate, guard, validate, read and event-list operations.
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
| 0.1.0 | Draft | Initial Permission API specification. Defines governed permission evaluation interface and separates Permission API from Policy, User role, Organization membership, workflow approval, business responsibility, legal authority and AI authority. |

---

**End of API Specification**
