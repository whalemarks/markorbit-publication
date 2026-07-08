# API Contract — Identity API

**Spec ID:** B02-CONTRACT-API-IDENTITY  
**Spec Type:** API Contract Specification  
**Contract Name:** Identity API Contract  
**Contract File:** core-specs/contracts/api/identity-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/identity-api.md  
**Related Domain:** Identity  
**Related Object Specs:** core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/identity-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/identity-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/identity-created.md; core-specs/events/identity-updated.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Common Contracts:** references.md; errors.md; pagination.md; audit-context.md; permission-context.md; policy-context.md; idempotency.md; versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Identity API Contract defines the implementation-facing request and response contract for Identity API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search and validate Identity records through governed API boundaries without bypassing Identity Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Identity API versioning
Identity create/read/update/search/validate-reference payloads
Identity reference shape
Permission and Policy context
Idempotency behavior
Audit context
Event trace references
Safe errors
Codex implementation rules
```

Identity API Contract does not define Identity domain truth by itself, create Identity records directly, evaluate Permission/Policy, replace Identity Service, or define product UI forms.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Identity Service through governed API boundaries.
```

This contract does not mean:

```text
database schema
authentication system
login session
user profile
organization profile
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Identity API receives governed requests.
Identity Service owns Identity behavior.
Permission and Policy govern access.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Identity reference fields
pagination shape for list/search
permission/policy context requirements
idempotency requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
Identity lifecycle ownership
Permission evaluation logic
Policy evaluation logic
Event emission implementation
authentication implementation
database schema design
UI rendering
```

---

# 4. Related Owning Spec

Owning API spec:

```text
core-specs/api/identity-api.md
```

Owning service spec:

```text
core-specs/services/identity-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Identity API and Identity Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Identity
```

Related objects:

```text
User
Organization
Permission
Policy
Event
Agent
```

Reference rules:

```text
- identity_reference_id identifies Identity.
- user_reference_id identifies User but must not replace Identity.
- organization_reference_id scopes access where required.
- Permission/Policy decision references must not be treated as approval unless validated by owning services.
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

Rules:

```text
- identity_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- organization_reference_id is required where operation is organization-scoped.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/identities
GET    /v1/identities/{identity_reference_id}
PATCH  /v1/identities/{identity_reference_id}
GET    /v1/identities
POST   /v1/identities/validate-reference
```

Endpoint ownership:

```text
API layer validates request contract.
Identity Service executes behavior.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Event Service records events from owning services.
```


---

# 8. Create Identity Request Contract

Endpoint:

```text
POST /v1/identities
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
    - identity:create
  permission_decision_reference_id: string | null
policy_context:
  required_policy_scopes:
    - identity:create:policy
  policy_decision_reference_id: string | null
payload:
  identity_type: string
  identity_status: string | null
  display_name_safe: string | null
  external_references:
    - external_system: string
      external_reference_id: string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- identity_type is required.
- display_name_safe must not contain restricted private data unless policy allows it.
- external_reference_id must not be used as Core identity_reference_id.
- Identity Service assigns identity_reference_id.
```

---

# 9. Create Identity Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  identity_reference_id: string
  identity_type: string
  identity_status: string
  display_name_safe: string | null
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
- Response must not expose database IDs.
- identity-created event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate IdentityCreated event.
```

---

# 10. Read Identity Contract

Endpoint:

```text
GET /v1/identities/{identity_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  identity_reference_id: string
  identity_type: string
  identity_status: string
  display_name_safe: string | null
  external_references_visible: list[object]
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
- Read must evaluate identity:read permission.
- Policy may downgrade response to metadata-only.
- Restricted fields must be omitted by default.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Identity Contract

Endpoint:

```text
PATCH /v1/identities/{identity_reference_id}
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
  identity_status: string | null
  display_name_safe: string | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - identity:update
policy_context:
  required_policy_scopes:
    - identity:update:policy
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  identity_reference_id: string
  identity_status: string
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Identity Service.
- Identity status transitions must follow Identity Service rules.
- Restricted metadata must not be patched through metadata_safe_patch.
- IdentityUpdated event reference may be returned where policy allows it.
```

---

# 12. Search/List Identity Contract

Endpoint:

```text
GET /v1/identities
```

Query parameters:

```yaml
identity_type: string | null
identity_status: string | null
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
    - identity_reference_id: string
      identity_type: string
      identity_status: string
      display_name_safe: string | null
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
- Search must not reveal restricted Identity existence.
- safe_query must not be treated as unrestricted search.
```


---

# 13. Validate Identity Reference Contract

Endpoint:

```text
POST /v1/identities/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  identity_reference_id: string
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
  identity_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Identity.
- Validation status must follow Reference Contract.
- Policy may hide safe_label.
```

---

# 14. Controlled Values

## 14.1 identity_type

```text
Person
Organization
System
Agent
Integration
Unknown
```

## 14.2 identity_status

```text
Draft
Active
Suspended
Archived
DeletedReferenceOnly
Unknown
```

## 14.3 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 14.4 sort.field

```text
created_at
updated_at
display_name_safe
identity_status
identity_type
```

---

# 15. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] identity_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] identity_type is controlled.
[ ] identity_status is controlled where provided.
[ ] external references do not replace Core reference IDs.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 16. Permission Rules

Required permission keys:

```text
identity:create
identity:read
identity:search
identity:update
identity:validate
```

Rules:

```text
- Identity API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 17. Policy Rules

Required policy scopes may include:

```text
identity:create:policy
identity:read:policy
identity:search:policy
identity:update:policy
identity:reference:policy
identity:visibility:policy
cross-organization:identity
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact fields, omit total_count, return NotFound or require review.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 18. Idempotency and Event Rules

Idempotency:

```text
POST /v1/identities requires idempotency_key.
PATCH /v1/identities/{identity_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
```

Events:

```text
IdentityCreated may be emitted by Identity Service after successful creation.
IdentityUpdated may be emitted by Identity Service after successful update.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
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
ReferenceInvalid
ReferenceNotFound
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
- Errors must not expose database IDs, permission internals or policy internals.
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
cite Identity API Spec
cite Identity Service Spec
cite this Identity API Contract
use Reference Contract for identity_reference_id
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use Idempotency Contract for create
use Versioning Contract for version validation
route all behavior through Identity Service
invoke Permission Service before protected behavior
invoke Policy Service before exposing fields
return safe errors only
write tests for create/read/update/search/validate-reference
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Identity directly in API layer
query database directly from API contract implementation
use generic id where identity_reference_id is required
expose database IDs
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
treat external_reference_id as Core identity_reference_id
```

---

# 22. Acceptance Criteria

This Identity API Contract is accepted only if:

```text
[ ] It defines Identity API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Identity API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines idempotency and event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 23. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Identity API Contract. Defines governed create, read, update, search and validate-reference payloads, Permission/Policy context, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
