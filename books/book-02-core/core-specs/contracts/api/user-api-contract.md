# API Contract — User API

**Spec ID:** B02-CONTRACT-API-USER  
**Spec Type:** API Contract Specification  
**Contract Name:** User API Contract  
**Contract File:** core-specs/contracts/api/user-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/user-api.md  
**Related Domain:** User  
**Related Object Specs:** core-specs/objects/user.md; core-specs/objects/identity.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/user-service.md; core-specs/services/identity-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/user-api.md; core-specs/api/identity-api.md; core-specs/api/organization-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/user-created.md; core-specs/events/user-updated.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

User API Contract defines the implementation-facing request and response contract for User API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate and reference User records through governed API boundaries without bypassing User Service, Identity Service, Organization Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
User API versioning
User create request
User update request
User read response
User search/list response
User reference validation
User identity linkage
User organization linkage
Permission and Policy context
Idempotency behavior
Audit context
Event trace references
Error behavior
Codex implementation rules
```

User API Contract does not define authentication, login sessions, passwords, MFA, product role UI, professional authority, permission grants or policy approvals by itself.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming User Service through governed API boundaries.
```

This contract does not mean:

```text
authentication system
login credential store
password contract
MFA contract
role model by itself
permission grant
policy approval
organization membership approval
event emitter
UI form
```

Core rule:

```text
User API receives governed requests.
User Service owns User behavior.
Identity and Organization references are validated by owning services.
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
User reference fields
Identity and Organization linkage fields
pagination shape for list/search
permission/policy context requirements
idempotency requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
User lifecycle ownership outside User Service
authentication credential handling
password reset flow
MFA setup flow
Permission evaluation logic
Policy evaluation logic
Event emission implementation
database schema design
UI rendering
```

---

# 4. Related Owning Spec

Owning API spec:

```text
core-specs/api/user-api.md
```

Owning service spec:

```text
core-specs/services/user-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken User API and User Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
User
```

Related objects:

```text
Identity
Organization
Permission
Policy
Event
Agent
```

Reference rules:

```text
- user_reference_id identifies User.
- identity_reference_id links User to Identity where User Service allows.
- organization_reference_id scopes or links User to Organization where User Service allows.
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

User target context:

```yaml
target:
  user_reference_id: string | null
  target_object_type: User
  target_object_reference_id: string | null
```

Rules:

```text
- user_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- organization_reference_id is required where operation is organization-scoped.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/users
GET    /v1/users/{user_reference_id}
PATCH  /v1/users/{user_reference_id}
GET    /v1/users
POST   /v1/users/validate-reference
```

Endpoint ownership:

```text
API layer validates request contract.
User Service executes behavior.
Identity Service validates identity_reference_id where needed.
Organization Service validates organization_reference_id where needed.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Event Service records emitted events from owning services.
```

---

# 8. Create User Request Contract

Endpoint:

```text
POST /v1/users
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
    - user:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - user:create:policy
  policy_decision_reference_id: string | null

payload:
  user_type: string
  user_status: string | null
  identity_reference_id: string | null
  organization_reference_ids:
    - string
  display_name_safe: string
  email_safe: string | null
  locale: string | null
  timezone: string | null
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- user_type and display_name_safe are required.
- identity_reference_id must be validated through Identity Service where provided.
- organization_reference_ids must be validated through Organization Service where provided.
- email_safe is not authentication credential proof.
- User Service assigns user_reference_id.
```

---

# 9. Create User Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  user_reference_id: string
  user_type: string
  user_status: string
  identity_reference_id: string | null
  organization_reference_ids:
    - string
  display_name_safe: string
  email_safe: string | null
  locale: string | null
  timezone: string | null
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
- UserCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate UserCreated event.
```

---

# 10. Read User Contract

Endpoint:

```text
GET /v1/users/{user_reference_id}
```

Path parameters:

```yaml
user_reference_id: string
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  user_reference_id: string
  user_type: string
  user_status: string
  identity_reference_id: string | null
  organization_reference_ids:
    - string
  display_name_safe: string
  email_safe: string | null
  locale: string | null
  timezone: string | null
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
- Read must evaluate user:read permission.
- Policy may downgrade response to metadata-only.
- Restricted fields must be omitted by default.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update User Contract

Endpoint:

```text
PATCH /v1/users/{user_reference_id}
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
  user_status: string | null
  display_name_safe: string | null
  email_safe: string | null
  locale: string | null
  timezone: string | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - user:update
policy_context:
  required_policy_scopes:
    - user:update:policy
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  user_reference_id: string
  user_status: string
  display_name_safe: string | null
  email_safe: string | null
  locale: string | null
  timezone: string | null
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through User Service.
- User status transitions must follow User Service rules.
- Restricted metadata must not be patched through metadata_safe_patch.
- UserUpdated event reference may be returned where policy allows it.
```

---

# 12. Search/List User Contract

Endpoint:

```text
GET /v1/users
```

Query parameters:

```yaml
user_type: string | null
user_status: string | null
organization_reference_id: string | null
identity_reference_id: string | null
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
    - user_reference_id: string
      user_type: string
      user_status: string
      identity_reference_id: string | null
      display_name_safe: string
      email_safe: string | null
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
- Search must not reveal restricted User existence.
- safe_query must not be treated as unrestricted search.
```

---

# 13. Validate User Reference Contract

Endpoint:

```text
POST /v1/users/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  user_reference_id: string
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
  user_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full User.
- Validation status must follow Reference Contract.
- Policy may hide safe_label.
```

---

# 14. Controlled Values

## 14.1 user_type

```text
PlatformAdmin
TenantAdmin
ProfessionalUser
OperationsUser
FinanceUser
PartnerUser
CustomerUser
ServiceProviderUser
SystemUser
Unknown
```

## 14.2 user_status

```text
Draft
Invited
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
email_safe
user_status
user_type
```

---

# 15. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] user_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] user_type is controlled.
[ ] user_status is controlled where provided.
[ ] identity_reference_id is validated where provided.
[ ] organization_reference_ids are validated where provided.
[ ] email_safe is safe and not treated as credential proof.
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
user:create
user:read
user:search
user:update
user:validate
```

Rules:

```text
- User API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 17. Policy Rules

Required policy scopes may include:

```text
user:create:policy
user:read:policy
user:search:policy
user:update:policy
user:reference:policy
user:visibility:policy
cross-organization:user
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
POST /v1/users requires idempotency_key.
PATCH /v1/users/{user_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
```

Events:

```text
UserCreated may be emitted by User Service after successful creation.
UserUpdated may be emitted by User Service after successful update.
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
IdentityReferenceInvalid
OrganizationReferenceInvalid
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
cite User API Spec
cite User Service Spec
cite this User API Contract
use Reference Contract for user_reference_id
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use Idempotency Contract for create
use Versioning Contract for version validation
route all behavior through User Service
invoke Identity Service for identity_reference_id validation
invoke Organization Service for organization_reference_ids validation
invoke Permission Service before protected behavior
invoke Policy Service before exposing fields
return safe errors only
write tests for create/read/update/search/validate-reference
write tests for identity reference validation
write tests for organization reference validation
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create User directly in API layer
query database directly from API contract implementation
use generic id where user_reference_id is required
expose database IDs
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
treat email_safe as authentication credential proof
treat User as Identity or Organization
```

---

# 22. Acceptance Criteria

This User API Contract is accepted only if:

```text
[ ] It defines User API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites User API and Service specs.
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
| 0.1.0 | Draft | Initial User API Contract. Defines governed create, read, update, search and validate-reference payloads, Identity/Organization linkage, Permission/Policy context, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
