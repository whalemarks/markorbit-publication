# API Contract — Organization API

**Spec ID:** B02-CONTRACT-API-ORGANIZATION  
**Spec Type:** API Contract Specification  
**Contract Name:** Organization API Contract  
**Contract File:** core-specs/contracts/api/organization-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/organization-api.md  
**Related Domain:** Organization  
**Related Object Specs:** core-specs/objects/organization.md; core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/organization-service.md; core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/organization-api.md; core-specs/api/identity-api.md; core-specs/api/user-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/organization-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
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

Organization API Contract defines the implementation-facing request and response contract for Organization API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate and reference Organization records through governed API boundaries without bypassing Organization Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Organization API versioning
Organization create request
Organization update request
Organization read response
Organization search/list response
Organization reference validation
Organization membership/reference context
Permission and Policy context
Idempotency behavior
Audit context
Event trace references
Error behavior
Codex implementation rules
```

Organization API Contract does not define Organization domain truth by itself, create Organization records directly, evaluate Permission/Policy, replace Organization Service, or define product UI forms.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Organization Service through governed API boundaries.
```

This contract does not mean:

```text
database schema
company registration proof
legal entity verification by itself
tenant model by itself
user membership system by itself
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Organization API receives governed requests.
Organization Service owns Organization behavior.
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
Organization reference fields
pagination shape for list/search
permission/policy context requirements
idempotency requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
Organization lifecycle ownership
Organization object semantic rules beyond contract shape
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
core-specs/api/organization-api.md
```

Owning service spec:

```text
core-specs/services/organization-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Organization API and Organization Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Organization
```

Related objects:

```text
Identity
User
Permission
Policy
Event
Agent
```

Reference rules:

```text
- organization_reference_id identifies Organization.
- identity_reference_id may link Organization to Identity where Organization Service allows.
- user_reference_id may be used for member/admin context but must not replace Organization.
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

Organization target context:

```yaml
target:
  organization_reference_id: string | null
  target_object_type: Organization
  target_object_reference_id: string | null
```

Rules:

```text
- organization_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- organization_reference_id may be both target and scope; owning contract must distinguish target organization from acting organization where needed.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/organizations
GET    /v1/organizations/{organization_reference_id}
PATCH  /v1/organizations/{organization_reference_id}
GET    /v1/organizations
POST   /v1/organizations/validate-reference
```

Endpoint ownership:

```text
API layer validates request contract.
Organization Service executes behavior.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Event Service records emitted events from owning services.
```

---

# 8. Create Organization Request Contract

Endpoint:

```text
POST /v1/organizations
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string
actor_reference_id: string | null

permission_context:
  required_permission_keys:
    - organization:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - organization:create:policy
  policy_decision_reference_id: string | null

payload:
  organization_type: string
  organization_status: string | null
  display_name_safe: string
  identity_reference_id: string | null
  parent_organization_reference_id: string | null
  external_references:
    - external_system: string
      external_reference_id: string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- organization_type and display_name_safe are required.
- identity_reference_id must be validated through Identity Service where provided.
- parent_organization_reference_id must be validated through Organization Service where provided.
- external_reference_id must not be used as Core organization_reference_id.
- Organization Service assigns organization_reference_id.
```

---

# 9. Create Organization Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  organization_reference_id: string
  organization_type: string
  organization_status: string
  display_name_safe: string
  identity_reference_id: string | null
  parent_organization_reference_id: string | null
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
- OrganizationCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate OrganizationCreated event.
```

---

# 10. Read Organization Contract

Endpoint:

```text
GET /v1/organizations/{organization_reference_id}
```

Path parameters:

```yaml
organization_reference_id: string
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  organization_reference_id: string
  organization_type: string
  organization_status: string
  display_name_safe: string
  identity_reference_id: string | null
  parent_organization_reference_id: string | null
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
- Read must evaluate organization:read permission.
- Policy may downgrade response to metadata-only.
- Restricted fields must be omitted by default.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Organization Contract

Endpoint:

```text
PATCH /v1/organizations/{organization_reference_id}
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
payload:
  organization_status: string | null
  display_name_safe: string | null
  parent_organization_reference_id: string | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - organization:update
policy_context:
  required_policy_scopes:
    - organization:update:policy
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  organization_reference_id: string
  organization_status: string
  display_name_safe: string | null
  parent_organization_reference_id: string | null
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Organization Service.
- Organization status transitions must follow Organization Service rules.
- Parent organization changes must be validated and must not create cycles.
- Restricted metadata must not be patched through metadata_safe_patch.
```

---

# 12. Search/List Organization Contract

Endpoint:

```text
GET /v1/organizations
```

Query parameters:

```yaml
organization_type: string | null
organization_status: string | null
parent_organization_reference_id: string | null
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
    - organization_reference_id: string
      organization_type: string
      organization_status: string
      display_name_safe: string
      parent_organization_reference_id: string | null
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
- Search must not reveal restricted Organization existence.
- safe_query must not be treated as unrestricted search.
```

---

# 13. Validate Organization Reference Contract

Endpoint:

```text
POST /v1/organizations/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  organization_reference_id: string
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
  organization_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Organization.
- Validation status must follow Reference Contract.
- Policy may hide safe_label.
```

---

# 14. Controlled Values

## 14.1 organization_type

```text
PlatformOwner
Tenant
Partner
CustomerOrganization
ServiceProviderOrganization
InternalTeam
ExternalOrganization
SystemOrganization
Unknown
```

## 14.2 organization_status

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
organization_status
organization_type
```

---

# 15. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] organization_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] organization_type is controlled.
[ ] organization_status is controlled where provided.
[ ] identity_reference_id is validated where provided.
[ ] parent_organization_reference_id is validated where provided.
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
organization:create
organization:read
organization:search
organization:update
organization:validate
```

Rules:

```text
- Organization API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 17. Policy Rules

Required policy scopes may include:

```text
organization:create:policy
organization:read:policy
organization:search:policy
organization:update:policy
organization:reference:policy
organization:visibility:policy
cross-organization:organization
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
POST /v1/organizations requires idempotency_key.
PATCH /v1/organizations/{organization_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
```

Events:

```text
OrganizationCreated may be emitted by Organization Service after successful creation.
OrganizationUpdated may be reserved for later if event spec exists.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
- API response must not claim OrganizationUpdated event unless the event spec exists and service emits it.
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
ParentOrganizationInvalid
OrganizationCycleRejected
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
cite Organization API Spec
cite Organization Service Spec
cite this Organization API Contract
use Reference Contract for organization_reference_id
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use Idempotency Contract for create
use Versioning Contract for version validation
route all behavior through Organization Service
invoke Permission Service before protected behavior
invoke Policy Service before exposing fields
return safe errors only
write tests for create/read/update/search/validate-reference
write tests for parent organization validation
write tests for organization cycle rejection
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Organization directly in API layer
query database directly from API contract implementation
use generic id where organization_reference_id is required
expose database IDs
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
treat external_reference_id as Core organization_reference_id
treat Organization as User or Identity
```

---

# 22. Acceptance Criteria

This Organization API Contract is accepted only if:

```text
[ ] It defines Organization API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Organization API and Service specs.
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
| 0.1.0 | Draft | Initial Organization API Contract. Defines governed create, read, update, search and validate-reference payloads, Permission/Policy context, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
