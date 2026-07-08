# API Contract — Permission API

**Spec ID:** B02-CONTRACT-API-PERMISSION  
**Spec Type:** API Contract Specification  
**Contract Name:** Permission API Contract  
**Contract File:** core-specs/contracts/api/permission-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/permission-api.md  
**Related Domain:** Permission  
**Related Object Specs:** core-specs/objects/permission.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/agent.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/permission-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/agent-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/permission-api.md; core-specs/api/user-api.md; core-specs/api/organization-api.md; core-specs/api/agent-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Permission API Contract defines the implementation-facing request and response contract for Permission API operations in MarkOrbit Core.

It standardizes how clients evaluate, read, search, validate and reference Permission decisions through governed API boundaries without bypassing Permission Service, Policy Service or Event Service.

This contract governs:

```text
Permission API versioning
Permission evaluation request
Permission evaluation response
Permission decision read response
Permission decision search/list response
Permission key validation
Permission reference validation
Actor, Agent and Organization context
Target object context
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Permission API Contract does not grant permissions by itself, define authentication, implement role models, replace Permission Service, replace Policy Service, or expose permission internals.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Permission Service through governed API boundaries.
```

This contract does not mean:

```text
permission grant
role assignment engine
authentication contract
authorization implementation by itself
policy decision
human approval
business approval
event emitter
debug endpoint
```

Core rule:

```text
Permission API receives governed permission requests.
Permission Service owns Permission evaluation.
Permission decisions do not bypass Policy.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
permission evaluation payload
permission decision reference shape
permission key validation shape
actor/agent/target context
safe decision result shape
pagination shape for list/search
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
assigning permissions
creating user roles
authenticating actors
evaluating policy
executing protected operations
emitting events directly
exposing permission rule internals
database schema design
UI rendering
```

---

# 4. Related Owning Spec

Owning API spec:

```text
core-specs/api/permission-api.md
```

Owning service spec:

```text
core-specs/services/permission-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Permission API and Permission Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Permission
```

Related objects:

```text
User
Organization
Agent
Policy
Event
```

Reference rules:

```text
- permission_decision_reference_id identifies a Permission evaluation decision.
- actor_reference_id identifies the actor requesting or being evaluated.
- agent_reference_id identifies Agent context where applicable.
- target_object_type and target_object_reference_id identify the protected target.
- Permission result does not imply Policy allowance.
```

---

# 6. Required References

Common API context:

```yaml
api_context:
  api_version: v1
  contract_version: v0.1.0
  correlation_id: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
```

Permission evaluation context:

```yaml
permission_context:
  actor_reference_id: string | null
  actor_type: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  agent_registry_key: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  intended_operation: string
  required_permission_keys: list[string]
```

Rules:

```text
- intended_operation is required for permission evaluation.
- required_permission_keys must contain at least one key.
- actor_reference_id or governed system/agent context is required.
- organization_reference_id is required for organization-scoped evaluation.
- agent_reference_id and agent_registry_key are required for Agent operations.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/permissions/evaluate
GET    /v1/permissions/decisions/{permission_decision_reference_id}
GET    /v1/permissions/decisions
POST   /v1/permissions/validate-key
POST   /v1/permissions/validate-decision-reference
```

Endpoint ownership:

```text
API layer validates request contract.
Permission Service executes evaluation and decision retrieval.
Policy Service may govern visibility of decision details.
Event Service records PermissionEvaluated from Permission Service.
```

---

# 8. Evaluate Permission Request Contract

Endpoint:

```text
POST /v1/permissions/evaluate
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null

payload:
  actor:
    actor_type: string
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
    required_permission_keys:
      - string
```

Rules:

```text
- required_permission_keys are required.
- Permission keys must follow Permission Context Contract.
- Agent capability does not equal permission.
- Request must not contain permission rule internals.
```

---

# 9. Evaluate Permission Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  permission_decision_reference_id: string
  permission_decision: string
  allowed: boolean
  conditional: boolean
  decision_reason_safe: string | null
  evaluated_at: datetime
  expires_at: datetime | null
  required_permission_keys:
    - string
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Response must not expose permission rule internals.
- PermissionEvaluated event reference may be included where policy allows it.
- allowed = true does not bypass Policy Service.
- conditional = true must be resolved by owning service before protected behavior continues unless explicitly allowed.
```

---

# 10. Read Permission Decision Contract

Endpoint:

```text
GET /v1/permissions/decisions/{permission_decision_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  permission_decision_reference_id: string
  actor_type: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  intended_operation: string
  required_permission_keys:
    - string
  permission_decision: string
  decision_reason_safe: string | null
  evaluated_at: datetime
  expires_at: datetime | null
  restricted_fields_omitted: boolean
policy_context:
  policy_decision_reference_id: string | null
```

Rules:

```text
- Read must be visibility-governed.
- Policy may redact actor, target, reason or key details.
- Permission decision read must not expose internal rule graph.
```

---

# 11. Search/List Permission Decisions Contract

Endpoint:

```text
GET /v1/permissions/decisions
```

Query parameters:

```yaml
actor_reference_id: string | null
organization_reference_id: string | null
agent_reference_id: string | null
target_object_type: string | null
target_object_reference_id: string | null
permission_decision: string | null
intended_operation: string | null
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
    - permission_decision_reference_id: string
      actor_type: string | null
      actor_reference_id: string | null
      target_object_type: string | null
      target_object_reference_id: string | null
      intended_operation: string
      permission_decision: string
      evaluated_at: datetime
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
- Search must not reveal restricted Permission decision existence.
```

---

# 12. Validate Permission Key Contract

Endpoint:

```text
POST /v1/permissions/validate-key
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  permission_key: string
  intended_operation: string | null
  target_object_type: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  permission_key: string
  valid: boolean
  validation_status: string
  safe_reason: string | null
```

Rules:

```text
- Permission key validation does not evaluate whether actor has permission.
- Valid key only means key shape and registry are acceptable.
```

---

# 13. Validate Permission Decision Reference Contract

Endpoint:

```text
POST /v1/permissions/validate-decision-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  permission_decision_reference_id: string
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
  permission_decision_reference_id: string
  valid: boolean
  validation_status: string
  permission_decision: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid decision reference does not imply it is reusable for a different target/operation.
- Decision freshness and context matching must be checked.
- Policy may hide decision detail.
```

---

# 14. Controlled Values

## 14.1 actor_type

```text
User
Agent
System
Integration
Service
Unknown
```

## 14.2 operation_category

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

## 14.3 permission_decision

```text
Allowed
Denied
Conditional
NotEvaluated
Expired
Invalid
Unknown
```

## 14.4 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
ContextMismatch
Expired
Unknown
```

## 14.5 sort.field

```text
evaluated_at
permission_decision
intended_operation
actor_reference_id
target_object_type
```

---

# 15. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] required_permission_keys are present for evaluation.
[ ] permission keys follow Permission Context Contract.
[ ] actor or governed system/agent context is present.
[ ] target object reference follows Reference Contract.
[ ] permission_decision_reference_id is valid where required.
[ ] permission_decision is controlled where provided.
[ ] pagination follows Pagination Contract.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 16. Permission Rules

Permission API access may itself require:

```text
permission:evaluate
permission:decision:read
permission:decision:search
permission:key:validate
permission:decision:validate
```

Rules:

```text
- Permission API must not grant permission.
- Permission Service evaluates requested permission.
- Access to decision history may require separate permission.
- PermissionDenied must stop protected behavior.
```

---

# 17. Policy Rules

Required policy scopes may include:

```text
permission:evaluate:policy
permission:decision:read:policy
permission:decision:search:policy
permission:decision:visibility:policy
permission:internals:restricted
cross-organization:permission
```

Rules:

```text
- Policy Service governs visibility of decision details.
- Policy may redact actor/target/reason/key details.
- Policy may return NotFound where existence disclosure is restricted.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 18. Event Rules

Events:

```text
PermissionEvaluated may be emitted by Permission Service after evaluation.
API layer must not emit PermissionEvaluated directly.
```

Rules:

```text
- Event references are audit trace, not commands.
- Event payload must not expose permission internals by default.
- Permission evaluation event emission must be idempotency-safe where applicable.
```

---

# 19. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
PermissionKeyInvalid
PermissionDecisionInvalid
PermissionDecisionExpired
PermissionDecisionReferenceInvalid
PermissionContextMismatch
ReferenceInvalid
ReferenceNotFound
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
- Errors must not expose permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 20. Versioning Rules

Version fields:

```yaml
api_version: v1
contract_version: v0.1.0
schema_version: v0.1.0
```

Rules:

```text
- Unsupported API or contract versions must fail closed.
- Breaking changes require contract version bump.
- Response payloads must preserve version fields.
```

---

# 21. Codex Implementation Notes

Codex must:

```text
cite Permission API Spec
cite Permission Service Spec
cite this Permission API Contract
use Permission Context Contract for evaluation payloads
use Reference Contract for target references
use Error Contract for errors
use Pagination Contract for list/search
use Policy Context Contract before exposing decision details
use Versioning Contract for version validation
route all evaluation through Permission Service
invoke Policy Service before exposing decision history
return safe errors only
write tests for evaluate/read/search/validate-key/validate-decision-reference
write tests for invalid permission key
write tests for denied decision
write tests for conditional decision
write tests for expired decision reference
write tests that API does not emit PermissionEvaluated directly
write tests for PolicyRestricted visibility
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
evaluate permission in API layer directly
query database directly from API contract implementation
expose permission rule internals
skip Policy checks for decision visibility
emit PermissionEvaluated directly from controller/API handler
treat Permission Allowed as Policy Allowed
reuse permission decision for incompatible target/operation
return unrestricted total_count by default
```

---

# 22. Acceptance Criteria

This Permission API Contract is accepted only if:

```text
[ ] It defines Permission API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Permission API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines evaluate request/response.
[ ] It defines read decision contract.
[ ] It defines search/list decision contract.
[ ] It defines validate-key contract.
[ ] It defines validate-decision-reference contract.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 23. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Permission API Contract. Defines governed permission evaluation, decision reading/searching, key validation, decision reference validation, visibility policy, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
