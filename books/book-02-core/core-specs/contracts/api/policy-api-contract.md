# API Contract — Policy API

**Spec ID:** B02-CONTRACT-API-POLICY  
**Spec Type:** API Contract Specification  
**Contract Name:** Policy API Contract  
**Contract File:** core-specs/contracts/api/policy-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/policy-api.md  
**Related Domain:** Policy  
**Related Object Specs:** core-specs/objects/policy.md; core-specs/objects/permission.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/agent.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/agent-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/policy-api.md; core-specs/api/permission-api.md; core-specs/api/user-api.md; core-specs/api/organization-api.md; core-specs/api/agent-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/policy-evaluated.md; core-specs/events/permission-evaluated.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Policy API Contract defines the implementation-facing request and response contract for Policy API operations in MarkOrbit Core.

It standardizes how clients evaluate, read, search, validate and reference Policy decisions through governed API boundaries without bypassing Policy Service, Permission Service or Event Service.

This contract governs:

```text
Policy API versioning
Policy evaluation request
Policy evaluation response
Policy decision read response
Policy decision search/list response
Policy scope validation
Policy decision reference validation
Permission decision dependency
Actor, Agent and Organization context
Target object context
Data access scope and restriction mode
Human-review requirement
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Policy API Contract does not grant permissions, define business policy logic by itself, implement policy rules in the API layer, replace Policy Service, replace Permission Service, or expose policy internals.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Policy Service through governed API boundaries.
```

This contract does not mean:

```text
policy engine implementation
permission grant
role assignment
business approval
human review completion
legal conclusion
professional standard itself
event emitter
debug endpoint
```

Core rule:

```text
Policy API receives governed policy requests.
Policy Service owns Policy evaluation.
Permission approval does not bypass Policy.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
policy evaluation payload
policy decision reference shape
policy scope validation shape
actor/agent/target context
data access scope response
restriction mode response
human-review requirement response
pagination shape for list/search
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
implementing policy rules
assigning permissions
authenticating actors
executing protected operations
performing human review
emitting events directly
exposing policy rule internals
database schema design
UI rendering
```

---

# 4. Related Owning Spec

Owning API spec:

```text
core-specs/api/policy-api.md
```

Owning service spec:

```text
core-specs/services/policy-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Policy API and Policy Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Policy
```

Related objects:

```text
Permission
User
Organization
Agent
Event
HumanReview
```

Reference rules:

```text
- policy_decision_reference_id identifies a Policy evaluation decision.
- permission_decision_reference_id may be referenced where policy evaluation depends on prior permission evaluation.
- actor_reference_id identifies the actor requesting or being evaluated.
- agent_reference_id identifies Agent context where applicable.
- target_object_type and target_object_reference_id identify the protected target.
- Policy decision does not grant permission.
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

Policy evaluation context:

```yaml
policy_context:
  actor_reference_id: string | null
  actor_type: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  agent_registry_key: string | null
  permission_decision_reference_id: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  intended_operation: string
  required_policy_scopes: list[string]
  requested_data_access_scope: string | null
```

Rules:

```text
- intended_operation is required for policy evaluation.
- required_policy_scopes must contain at least one scope.
- actor_reference_id or governed system/agent context is required.
- organization_reference_id is required for organization-scoped evaluation.
- agent_reference_id and agent_registry_key are required for Agent operations.
- permission_decision_reference_id is required where Policy Service requires prior Permission evaluation.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/policies/evaluate
GET    /v1/policies/decisions/{policy_decision_reference_id}
GET    /v1/policies/decisions
POST   /v1/policies/validate-scope
POST   /v1/policies/validate-decision-reference
```

Endpoint ownership:

```text
API layer validates request contract.
Policy Service executes evaluation and decision retrieval.
Permission Service owns Permission decision validation where required.
Event Service records PolicyEvaluated from Policy Service.
```

---

# 8. Evaluate Policy Request Contract

Endpoint:

```text
POST /v1/policies/evaluate
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
    required_policy_scopes:
      - string
  access:
    requested_data_access_scope: string | null
  governance:
    permission_decision_reference_id: string | null
```

Rules:

```text
- required_policy_scopes are required.
- Policy scopes must follow Policy Context Contract.
- Permission approval does not equal policy allowance.
- Request must not contain policy rule internals.
- Agent prompt/context must not be included in the request payload.
```

---

# 9. Evaluate Policy Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  policy_decision_reference_id: string
  policy_decision: string
  allowed: boolean
  restricted: boolean
  downgraded: boolean
  restriction_mode: string | null
  requested_data_access_scope: string | null
  evaluated_data_access_scope: string | null
  restricted_fields_omitted: boolean
  omitted_field_groups:
    - string
  human_review_required: boolean
  decision_reason_safe: string | null
  evaluated_at: datetime
  expires_at: datetime | null
  required_policy_scopes:
    - string
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Response must not expose policy rule internals.
- PolicyEvaluated event reference may be included where policy allows it.
- allowed = true does not grant permission.
- restricted/downgraded decision must be enforced by owning service.
- human_review_required must be explicit.
```

---

# 10. Read Policy Decision Contract

Endpoint:

```text
GET /v1/policies/decisions/{policy_decision_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  policy_decision_reference_id: string
  permission_decision_reference_id: string | null
  actor_type: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  intended_operation: string
  required_policy_scopes:
    - string
  policy_decision: string
  restriction_mode: string | null
  evaluated_data_access_scope: string | null
  restricted_fields_omitted: boolean
  omitted_field_groups:
    - string
  human_review_required: boolean | null
  decision_reason_safe: string | null
  evaluated_at: datetime
  expires_at: datetime | null
```

Rules:

```text
- Read must be visibility-governed.
- Policy may redact actor, target, reason, scope, omitted groups or decision details.
- Policy decision read must not expose internal rule graph.
```

---

# 11. Search/List Policy Decisions Contract

Endpoint:

```text
GET /v1/policies/decisions
```

Query parameters:

```yaml
actor_reference_id: string | null
organization_reference_id: string | null
agent_reference_id: string | null
target_object_type: string | null
target_object_reference_id: string | null
policy_decision: string | null
intended_operation: string | null
required_policy_scope: string | null
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
    - policy_decision_reference_id: string
      actor_type: string | null
      actor_reference_id: string | null
      target_object_type: string | null
      target_object_reference_id: string | null
      intended_operation: string
      policy_decision: string
      restriction_mode: string | null
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
- Search must not reveal restricted Policy decision existence.
```

---

# 12. Validate Policy Scope Contract

Endpoint:

```text
POST /v1/policies/validate-scope
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  policy_scope: string
  intended_operation: string | null
  target_object_type: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  policy_scope: string
  valid: boolean
  validation_status: string
  safe_reason: string | null
```

Rules:

```text
- Policy scope validation does not evaluate whether context allows an action.
- Valid scope only means scope shape and registry are acceptable.
```

---

# 13. Validate Policy Decision Reference Contract

Endpoint:

```text
POST /v1/policies/validate-decision-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  policy_decision_reference_id: string
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
  policy_decision_reference_id: string
  valid: boolean
  validation_status: string
  policy_decision: string | null
  evaluated_data_access_scope: string | null
  restricted_fields_omitted: boolean
  human_review_required: boolean | null
```

Rules:

```text
- Valid decision reference does not imply it is reusable for a different target/operation/context.
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

## 14.3 policy_decision

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

## 14.4 restriction_mode

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

## 14.5 data_access_scope

```text
NoAccess
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContentWithHumanApproval
Unknown
```

## 14.6 validation_status

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

## 14.7 sort.field

```text
evaluated_at
policy_decision
restriction_mode
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
[ ] required_policy_scopes are present for evaluation.
[ ] policy scopes follow Policy Context Contract.
[ ] actor or governed system/agent context is present.
[ ] target object reference follows Reference Contract.
[ ] requested_data_access_scope is controlled where provided.
[ ] permission_decision_reference_id is valid where required.
[ ] policy_decision_reference_id is valid where required.
[ ] policy_decision and restriction_mode are controlled where provided.
[ ] human_review_required is explicit in evaluation response.
[ ] pagination follows Pagination Contract.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 16. Permission Rules

Policy API access may itself require:

```text
policy:evaluate
policy:decision:read
policy:decision:search
policy:scope:validate
policy:decision:validate
```

Rules:

```text
- Policy API must not grant permission.
- Permission Service may evaluate whether actor may access Policy API functions.
- Permission Allowed does not bypass policy evaluation.
- PermissionDenied must stop protected behavior.
```

---

# 17. Policy Rules

Policy visibility may be policy-controlled.

Required policy scopes may include:

```text
policy:evaluate:policy
policy:decision:read:policy
policy:decision:search:policy
policy:decision:visibility:policy
policy:internals:restricted
cross-organization:policy
```

Rules:

```text
- Policy Service governs visibility of decision details.
- Policy may redact actor/target/reason/scope/restriction details.
- Policy may return NotFound where existence disclosure is restricted.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 18. Human Review and AI Rules

Human review:

```text
Policy evaluation may require human_review_required = true.
Human review must follow Human Review Contract before downstream use where required.
```

AI:

```text
Agent-assisted policy evaluation must include agent_reference_id and agent_registry_key.
AI prompt/context construction must use evaluated_data_access_scope.
Agent must not claim policy is Allowed unless Policy Service returned valid decision.
```

Rules:

```text
- Agent capability does not equal policy allowance.
- Policy decision may restrict AI data scope.
- AI output must disclose policy omissions and restricted field omission where applicable.
```

---

# 19. Event Rules

Events:

```text
PolicyEvaluated may be emitted by Policy Service after evaluation.
API layer must not emit PolicyEvaluated directly.
```

Rules:

```text
- Event references are audit trace, not commands.
- Event payload must not expose policy internals by default.
- Policy evaluation event emission must be idempotency-safe where applicable.
```

---

# 20. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
PolicyScopeInvalid
PolicyDecisionInvalid
PolicyDecisionExpired
PolicyDecisionReferenceInvalid
PolicyContextMismatch
DataAccessScopeInvalid
DataAccessScopeExceeded
RestrictedFieldViolation
PolicyRequiresHumanReview
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
- Errors must not expose policy internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 21. Versioning Rules

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

# 22. Codex Implementation Notes

Codex must:

```text
cite Policy API Spec
cite Policy Service Spec
cite this Policy API Contract
use Policy Context Contract for evaluation payloads
use Permission Context Contract where prior permission decision is required
use Reference Contract for target references
use Error Contract for errors
use Pagination Contract for list/search
use Human Review Contract where policy requires review
use AI Context Contract for agent-assisted policy behavior
use Versioning Contract for version validation
route all evaluation through Policy Service
invoke Permission Service where API access or permission dependency applies
return safe errors only
write tests for evaluate/read/search/validate-scope/validate-decision-reference
write tests for invalid policy scope
write tests for denied/restricted/downgraded decisions
write tests for RequiresHumanReview
write tests for DataAccessScopeExceeded
write tests that API does not emit PolicyEvaluated directly
write tests for decision visibility restriction
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
evaluate policy in API layer directly
query database directly from API contract implementation
expose policy rule internals
skip Permission checks where API access requires them
emit PolicyEvaluated directly from controller/API handler
treat Policy Allowed as Permission Allowed
reuse policy decision for incompatible target/operation/context
return unrestricted total_count by default
allow AI context to exceed evaluated_data_access_scope
```

---

# 23. Acceptance Criteria

This Policy API Contract is accepted only if:

```text
[ ] It defines Policy API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Policy API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines evaluate request/response.
[ ] It defines read decision contract.
[ ] It defines search/list decision contract.
[ ] It defines validate-scope contract.
[ ] It defines validate-decision-reference contract.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines Human Review and AI rules.
[ ] It defines event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Policy API Contract. Defines governed policy evaluation, decision reading/searching, scope validation, decision reference validation, data access scope, restriction mode, human-review requirements, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
