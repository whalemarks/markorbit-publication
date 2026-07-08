# API Specification — Policy API

**Spec ID:** B02-API-POLICY  
**Spec Type:** API Specification  
**API Name:** Policy API  
**API File:** core-specs/api/policy-api.md  
**Related Domain:** core-specs/domains/policy.md  
**Related Object Specs:** core-specs/objects/policy.md; core-specs/objects/permission.md; core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/policy-evaluated.md; core-specs/events/permission-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/policy-api-contract.md; core-specs/contracts/events/policy-evaluated-payload.md  
**Related Agent Specs:** core-specs/agents/policy-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Policy API exposes governed contextual policy evaluation operations for MarkOrbit Core.

It allows authorized consumers to evaluate whether contextual constraints are satisfied for a requested action, object, field, visibility, AI use, integration, event access, export or workflow-sensitive operation without treating Policy as Permission, role, User membership, business approval, legal conclusion or professional truth.

Policy API exists to support:

```text
contextual constraint evaluation
field and object visibility control
confidentiality and data exposure control
AI Agent access control
event payload visibility control
cross-organization access guard
integration/export guard
audit trace for policy decisions
```

Policy API does not decide whether an actor has permission to act.

Permission determines allowed action.

Policy evaluates contextual constraints.

---

# 2. API Meaning

Policy API means:

```text
a governed interface for evaluating contextual constraints through Policy Service.
```

Policy API does not mean:

```text
Permission API
role management API
User API
Organization membership API
workflow approval API
business responsibility API
professional legal conclusion API
AI truth API
```

Policy may restrict or shape an allowed action.

Policy must not be treated as Permission grant.

---

# 3. API Boundary

Policy API is responsible for:

```text
policy evaluation request intake
context validation
policy scope validation
safe policy decision response shaping
restricted field and visibility decision support
AI Agent context boundary support
policy evaluation event reference exposure
controlled API errors
```

Policy API is not responsible for:

```text
Permission ownership
role assignment
User or Organization creation
workflow execution
Task assignment
business responsibility ownership
professional decision approval
legal representative authority
database authorization by itself
AI reasoning truth
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/policy.md
```

Domain rule:

```text
Policy evaluates contextual constraints.
Policy is not Permission, workflow approval, business responsibility or professional truth.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/policy.md
core-specs/objects/permission.md
core-specs/objects/identity.md
core-specs/objects/user.md
core-specs/objects/organization.md
core-specs/objects/event.md
```

Object rules:

```text
- Policy API returns policy_decision_reference_id where decisions are recorded.
- Policy API must reference policy_scope and target context.
- Policy API must not create User, Identity, Organization or Permission records silently.
- Policy API must not treat Permission decision as Policy decision.
- Policy API must not expose restricted policy internals by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/policy-service.md
core-specs/services/permission-service.md
core-specs/services/identity-service.md
core-specs/services/user-service.md
core-specs/services/organization-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Policy API must invoke Policy Service for policy behavior.
- Policy API may validate Identity/User/Organization references through their owning services.
- Policy API may accept Permission decision reference as context but must not replace Permission Service.
- Policy API must not emit PolicyEvaluated directly; Policy Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/policy-evaluated.md
core-specs/events/permission-evaluated.md
```

Event rules:

```text
- evaluatePolicy must result in PolicyEvaluated where decision recording is required.
- combined guard operations may also reference PermissionEvaluated.
- API consumers must not fabricate PolicyEvaluated.
- PolicyEvaluated is decision trace, not Permission grant.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Evaluate Policy

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/policies/evaluate`  
**Owning Service Operation:** `evaluatePolicy`  
**Permission Required:** `policy:evaluate` or system-internal guard authority  
**Policy Required:** `PolicyEvaluationAccessPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service Must Emit PolicyEvaluated where audit required

Meaning:

```text
Evaluate whether contextual policy constraints are satisfied for a requested context.
```

Non-meaning:

```text
does not grant Permission
does not create role assignment
does not approve workflow
does not approve business responsibility
does not prove professional legal conclusion
```

Expected service call:

```text
API
  ↓
Permission guard where required to call policy endpoint
  ↓
Context/reference validation
  ↓
Policy Service evaluatePolicy
  ↓
Event Service record PolicyEvaluated where required
  ↓
Safe API response
```

## 8.2 Operation: Evaluate Visibility Policy

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/policies/visibility/evaluate`  
**Owning Service Operation:** `evaluateVisibilityPolicy`  
**Permission Required:** `policy:visibility:evaluate`  
**Policy Required:** `VisibilityPolicyEvaluationAccessPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service May Emit PolicyEvaluated

Meaning:

```text
Evaluate object, field or event payload visibility for a given actor/context.
```

Non-meaning:

```text
does not authorize the underlying action by itself
does not expose restricted fields automatically
does not override Permission denial
```

## 8.3 Operation: Evaluate AI Access Policy

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/policies/ai-access/evaluate`  
**Owning Service Operation:** `evaluateAIAccessPolicy`  
**Permission Required:** `policy:ai:evaluate`  
**Policy Required:** `AIAgentPolicyEvaluationAccessPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service Must Emit PolicyEvaluated where audit required

Meaning:

```text
Evaluate whether an AI Agent may access, summarize, draft, recommend or invoke an operation in a given context.
```

Non-meaning:

```text
does not authorize AI action without Permission where Permission is required
does not make AI output professional truth
does not remove human review requirement where required
```

## 8.4 Operation: Validate Policy Decision Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/policies/decisions/reference/validate`  
**Owning Service Operation:** `validatePolicyDecisionReference`  
**Permission Required:** `policy:decision:validate`  
**Policy Required:** `PolicyDecisionVisibilityPolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a policy decision reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not re-evaluate current policy
does not extend decision validity
does not grant Permission
```

## 8.5 Operation: Get Policy Decision

**Operation Category:** Read  
**Method:** GET  
**Path:** `/policies/decisions/{policy_decision_reference_id}`  
**Owning Service Operation:** `getPolicyDecision`  
**Permission Required:** `policy:decision:read`  
**Policy Required:** `PolicyDecisionVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe view of a Policy decision trace.
```

Non-meaning:

```text
does not expose restricted policy internals
does not expose unrelated actor/resource data
does not act as current contextual approval unless still valid and explicitly allowed
```

## 8.6 Operation: List Policy Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/policies/decisions/{policy_decision_reference_id}/events`  
**Owning Service Operation:** `listPolicyDecisionEvents`  
**Permission Required:** `policy:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Policy-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not replay Policy decision as command
```

---

# 9. Request Contracts

## 9.1 Evaluate Policy Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
body:
  actor_reference_id: string
  actor_type: string
  organization_reference_id: string | null
  policy_scope: string
  policy_context_type: string
  target_object_type: string
  target_object_reference_id: string | null
  permission_decision_reference_id: string | null
  request_context:
    source_api: string | null
    operation_category: string | null
    requested_fields: list[string]
    integration_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Evaluate Visibility Policy Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  target_object_type: string
  target_object_reference_id: string | null
  requested_visibility:
    fields: list[string]
    include_events: boolean
    include_restricted_payload: boolean
  request_context: object
```

## 9.3 Evaluate AI Access Policy Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  agent_identity_reference_id: string
  agent_contract_reference_id: string | null
  ai_action_type: string
  target_object_type: string
  target_object_reference_id: string | null
  requested_data_scope: string
  human_review_context:
    review_required: boolean | null
    review_reference_id: string | null
```

## 9.4 Validate Policy Decision Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  policy_decision_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

Request rules:

```text
- Requests must include policy_scope and target context.
- Requests must use controlled actor_type, policy_context_type and target_object_type values.
- Requests must not include restricted policy rule internals or secrets.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Policy Evaluation Response

```yaml
status: 200
body:
  policy_decision_reference_id: string
  actor_reference_id: string
  policy_scope: string
  policy_context_type: string
  target_object_type: string
  target_object_reference_id: string | null
  decision: string
  decision_status: string
  reason_code: string
  expires_at: datetime | null
  safe_summary:
    allowed_by_policy: boolean
    restriction_summary: string | null
    fields_allowed: list[string]
    fields_restricted: list[string]
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 AI Access Policy Response

```yaml
status: 200
body:
  policy_decision_reference_id: string
  agent_identity_reference_id: string
  ai_action_type: string
  decision: string
  human_review_required: boolean
  allowed_data_scope: string
  restricted_data_scope: string | null
  reason_code: string
  safe_summary: object
  related_event_reference_ids: list[string]
  correlation_id: string | null
```

## 10.3 Policy Decision Reference Validation Response

```yaml
status: 200
body:
  policy_decision_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

Response rules:

```text
- Responses must not expose restricted policy rule internals by default.
- Responses must not expose restricted object fields unless policy allows.
- Responses must not imply Permission grant.
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

## 11.2 policy_context_type

```text
Visibility
Confidentiality
DataAccess
EventAccess
AIAccess
IntegrationAccess
Export
Retention
CrossOrganization
WorkflowGuard
FieldAccess
Unknown
```

## 11.3 decision

```text
Allowed
Restricted
Denied
ReviewRequired
NotApplicable
Unknown
```

## 11.4 decision_status

```text
Evaluated
Valid
Expired
Revoked
Superseded
PolicyRestricted
Error
Unknown
```

## 11.5 target_object_type

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

## 11.6 ai_action_type

```text
Read
Summarize
Draft
Recommend
Classify
Extract
Validate
InvokeAPI
CreateRecord
UpdateRecord
ObserveEvent
Unknown
```

## 11.7 intended_use

```text
CurrentPolicyCheck
AuditReference
EventAccess
APIGuard
AIAgentAction
VisibilityDecision
ValidationOnly
Unknown
```

## 11.8 reason_code

```text
PolicyAllowed
PolicyRestricted
PolicyDenied
ReviewRequired
ActorInvalid
TargetInvalid
PolicyScopeInvalid
OrganizationContextInvalid
PermissionDecisionRequired
AgentContractRequired
HumanReviewRequired
DecisionExpired
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
policy:evaluate
policy:visibility:evaluate
policy:ai:evaluate
policy:decision:validate
policy:decision:read
policy:event:read
```

Rules:

```text
- Policy evaluation endpoints must be protected against unrestricted probing.
- Policy read operations require separate permission.
- Policy validation does not authorize the original action.
- Permission may be required to call Policy API, but Permission and Policy decisions remain separate.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
PolicyEvaluationAccessPolicy
VisibilityPolicyEvaluationAccessPolicy
AIAgentPolicyEvaluationAccessPolicy
PolicyDecisionVisibilityPolicy
EventVisibilityPolicy
CrossOrganizationPolicy
RestrictedFieldPolicy
DataExportPolicy
```

Rules:

```text
- Policy may restrict who can evaluate policies.
- Policy may restrict visibility into decision reasons.
- Policy may require AI Agent Contract for AI-originated policy evaluation.
- Policy may require human review for certain AI actions.
- Policy may require re-evaluation for stale policy decisions.
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
Evaluate Policy: Restricted
Evaluate Visibility Policy: Restricted
Evaluate AI Access Policy: Restricted
Validate Policy Decision Reference: Allowed under contract
Get Policy Decision: Restricted
List Policy Events: Restricted
```

AI Agents may:

```text
request policy evaluation for authorized planned actions
validate policy decision references where authorized
summarize safe policy outcome
flag missing policy context
explain that policy is not permission or professional approval
```

AI Agents must not:

```text
fabricate Policy decision
fabricate PolicyEvaluated event
override Policy result
treat Policy as Permission grant
treat Policy as workflow approval
treat Policy as professional truth
expose restricted policy internals
bypass human review requirement
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

Policy API may expose:

```text
PolicyEvaluated
PermissionEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Policy events directly.
- PolicyEvaluated must not be treated as Permission grant or permanent approval.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] actor_reference_id is present.
[ ] actor_type is controlled.
[ ] policy_scope is present.
[ ] policy_context_type is controlled.
[ ] target_object_type is controlled.
[ ] target_object_reference_id is valid where required.
[ ] organization_reference_id is valid where provided.
[ ] permission_decision_reference_id is valid where required.
[ ] AI Agent Contract is present where required.
[ ] Policy Service is invoked for policy decision.
[ ] Permission Service is not bypassed where Permission is required.
[ ] PolicyEvaluated is emitted where audit/event trace is required.
[ ] Restricted policy internals are omitted.
[ ] Response distinguishes Policy from Permission.
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
PolicyScopeInvalid
PolicyContextInvalid
TargetReferenceInvalid
OrganizationReferenceInvalid
PermissionDecisionReferenceInvalid
PolicyDecisionReferenceInvalid
ValidationFailed
DecisionExpired
RestrictedFieldViolation
AgentContractRequired
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
- Errors must not expose restricted policy rules.
- Errors must not expose permission internals.
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
- decision, policy_context_type and ai_action_type changes must be documented.
- Event behavior changes must be documented.
- Permission/Policy interaction changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Policy API spec
cite Policy Service Specification
cite Policy Object Specification
cite PolicyEvaluated Event Specification
cite Permission specs for protected and combined operations
implement request validation before service invocation
validate actor/policy/target context
enforce AI Agent Contract where required
return safe responses by default
write tests for invalid actor/policy/target references
write tests for PermissionDenied on protected policy operations
write tests for PolicyRestricted
write tests for PolicyEvaluated event after required evaluations
write tests that Policy API does not grant Permission
write tests that Policy API does not treat Permission as Policy
write tests that restricted policy internals are hidden
write tests that AI human review requirements are enforced
```

Codex must not:

```text
write directly to database bypassing Policy Service
allow UI to emit PolicyEvaluated directly
treat User existence as Policy approval
treat Organization membership as Policy approval by itself
treat Policy decision as Permission grant
treat Policy decision as workflow approval
expose policy rule internals for convenience
allow AI to fabricate Policy decisions or events
bypass human review where policy requires it
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Policy API purpose.
[ ] It defines Policy API meaning.
[ ] It defines Policy API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines evaluate, visibility, AI access, validate, read and event-list operations.
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
| 0.1.0 | Draft | Initial Policy API specification. Defines governed contextual policy evaluation interface and separates Policy API from Permission, User role, Organization membership, workflow approval, business responsibility, legal conclusion and AI truth. |

---

**End of API Specification**
