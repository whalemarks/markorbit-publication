# API Specification — Identity API

**Spec ID:** B02-API-IDENTITY  
**Spec Type:** API Specification  
**API Name:** Identity API  
**API File:** core-specs/api/identity-api.md  
**Related Domain:** core-specs/domains/identity.md  
**Related Object Specs:** core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/identity-created.md; core-specs/events/identity-updated.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/identity-api-contract.md; core-specs/contracts/events/identity-created-payload.md; core-specs/contracts/events/identity-updated-payload.md  
**Related Agent Specs:** core-specs/agents/identity-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Identity API exposes governed Identity reference operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, validate and search Identity references without treating Identity as authentication credentials, User account, Organization membership, Permission grant or Policy approval.

Identity API exists to support:

```text
stable actor reference creation
actor reference lookup
identity status review
identity reference validation
user identity linkage preparation
permission evaluation context
policy evaluation context
event trace access
AI-safe actor reference handling
```

Identity API does not authenticate users, issue tokens, manage passwords or grant access.

---

# 2. API Meaning

Identity API means:

```text
a governed interface for accessing and operating Identity references through Identity Service.
```

Identity API does not mean:

```text
login API
credential API
token API
User API
Organization membership API
Permission API
Policy API
approval API
account provisioning API
AI authority API
```

Identity is a stable actor reference.

Authentication and access control are separate concerns.

---

# 3. API Boundary

Identity API is responsible for:

```text
Identity create request intake
Identity read/search/list access
Identity update request intake
Identity reference validation
safe Identity response shaping
Permission/Policy enforcement for Identity operations
Identity-related Event reference exposure where allowed
AI Agent access boundary for Identity operations
controlled API errors
```

Identity API is not responsible for:

```text
password management
session management
token issuance
multi-factor authentication
User account lifecycle
Organization membership lifecycle
Permission grant
Policy evaluation ownership
business role assignment
AI Agent authorization by itself
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/identity.md
```

Domain rule:

```text
Identity recognizes actor references.
Identity does not authenticate credentials.
Identity does not grant Permission or evaluate Policy.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/identity.md
core-specs/objects/user.md
core-specs/objects/organization.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Identity API returns identity_reference_id.
- Identity API may reference User or Organization context but must not create them silently.
- Identity API must not expose credential material.
- Identity API must not treat Identity as Permission.
- Identity API must not treat Identity status as Policy approval.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/identity-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Identity API must invoke Identity Service for Identity behavior.
- Identity API must invoke Permission Service where operation requires authorization.
- Identity API must invoke Policy Service where contextual constraints apply.
- Identity API must not emit Identity events directly; Identity Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/identity-created.md
core-specs/events/identity-updated.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createIdentity may result in IdentityCreated.
- updateIdentity may result in IdentityUpdated.
- protected operations may produce PermissionEvaluated and PolicyEvaluated.
- API consumers must not fabricate IdentityCreated or IdentityUpdated.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Identity

**Operation Category:** Create  
**Method:** POST  
**Path:** `/identities`  
**Owning Service Operation:** `createIdentity`  
**Permission Required:** `identity:create`  
**Policy Required:** `IdentityCreationPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service Must Emit IdentityCreated

Meaning:

```text
Create a governed Identity reference.
```

Non-meaning:

```text
does not create User
does not authenticate credentials
does not create Organization membership
does not grant Permission
does not approve Policy
```

Expected service call:

```text
API
  ↓
Permission Service evaluatePermission
  ↓
Policy Service evaluatePolicy where required
  ↓
Identity Service createIdentity
  ↓
Event Service record IdentityCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Identity

**Operation Category:** Read  
**Method:** GET  
**Path:** `/identities/{identity_reference_id}`  
**Owning Service Operation:** `getIdentity`  
**Permission Required:** `identity:read`  
**Policy Required:** `IdentityVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Identity reference view.
```

Non-meaning:

```text
does not expose credentials
does not expose authentication state beyond governed Identity state
does not expose linked restricted User/Organization details automatically
```

## 8.3 Operation: Search Identities

**Operation Category:** Search  
**Method:** GET  
**Path:** `/identities`  
**Owning Service Operation:** `searchIdentities`  
**Permission Required:** `identity:search`  
**Policy Required:** `IdentityVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Identity references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted directory access
does not expose private actor data by default
```

## 8.4 Operation: Update Identity

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/identities/{identity_reference_id}`  
**Owning Service Operation:** `updateIdentity`  
**Permission Required:** `identity:update`  
**Policy Required:** `IdentityUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service Must Emit IdentityUpdated

Meaning:

```text
Update governed Identity metadata or status under Identity Service rules.
```

Non-meaning:

```text
does not update credentials
does not update User account automatically
does not update Organization membership automatically
does not grant Permission
```

## 8.5 Operation: Validate Identity Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/identities/reference/validate`  
**Owning Service Operation:** `validateIdentityReference`  
**Permission Required:** `identity:validate`  
**Policy Required:** `IdentityReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that an Identity reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not authenticate actor
does not authorize action
does not grant access to target object
```

## 8.6 Operation: List Identity Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/identities/{identity_reference_id}/events`  
**Owning Service Operation:** `listIdentityEvents`  
**Permission Required:** `identity:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Identity-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Identity Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  identity_type: string
  identity_status: string | optional
  external_reference: string | null
  source_type: string
  request_context: object
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Identity Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  identity_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  identity_status: string | optional
  display_reference: string | optional
  external_reference: string | optional
  request_context: object
```

## 9.3 Validate Identity Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  identity_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

Request rules:

```text
- Requests must not include passwords, tokens, secrets or raw credential material.
- Requests must use controlled identity_type and identity_status values.
- Requests must include actor_reference_id for protected operations.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Identity Response

```yaml
status: 200
body:
  identity_reference_id: string
  identity_type: string
  identity_status: string
  safe_summary:
    display_reference: string | null
    source_type: string
    created_at: datetime
    updated_at: datetime | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Identity Response

```yaml
status: 201
body:
  identity_reference_id: string
  identity_status: string
  related_event_reference_ids:
    - identity_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Validation Response

```yaml
status: 200
body:
  identity_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

Response rules:

```text
- Responses must not include credential material.
- Responses must not imply authentication success.
- Responses must not imply Permission grant.
- Responses must hide restricted linked User/Organization data unless separately authorized.
```

---

# 11. Controlled Values

## 11.1 identity_type

```text
HumanActor
SystemActor
AIAgentActor
ExternalActor
ServiceActor
Unknown
```

## 11.2 identity_status

```text
Draft
Active
Suspended
Revoked
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 source_type

```text
ProfessionalInput
SystemProcess
UserProvisioning
AIAgentProvisioning
ExternalIntegration
Migration
APIRequest
Unknown
```

## 11.4 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ContextMismatch
Unknown
```

## 11.5 intended_use

```text
ActorReference
UserLink
OrganizationLink
PermissionEvaluation
PolicyEvaluation
AIAgentAction
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
identity:create
identity:read
identity:search
identity:update
identity:validate
identity:event:read
```

Rules:

```text
- Identity read/search must be permission-controlled.
- Identity creation must not imply Permission grant.
- Identity validation must not be used as authorization decision.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
IdentityCreationPolicy
IdentityUpdatePolicy
IdentityVisibilityPolicy
IdentityReferencePolicy
EventVisibilityPolicy
AIAgentIdentityAccessPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Identity fields.
- Policy may require human review for AI-created Identity references.
- Policy may restrict cross-organization Identity lookup.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Identity: Restricted
Get Identity: Restricted
Search Identities: Restricted
Update Identity: Restricted / HumanReviewRequired where sensitive
Validate Identity Reference: Allowed under contract
List Identity Events: Restricted
```

AI Agents may:

```text
validate identity references for authorized actions
summarize safe Identity metadata
prepare draft Identity creation requests where allowed
flag missing or invalid Identity references
```

AI Agents must not:

```text
fabricate Identity
fabricate IdentityCreated or IdentityUpdated events
create Identity without Agent Contract where required
treat Identity as authentication
treat Identity as Permission grant
expose restricted Identity data
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

Identity API may expose:

```text
IdentityCreated
IdentityUpdated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Identity events directly.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] identity_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] identity_type is controlled.
[ ] identity_status is controlled.
[ ] source_type is controlled.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] No credential material is included.
[ ] Restricted fields are omitted or allowed.
[ ] AI Agent Contract is present where required.
[ ] IdentityCreated is emitted after createIdentity succeeds.
[ ] IdentityUpdated is emitted after updateIdentity succeeds.
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
IdentityReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
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
- Errors must not expose credentials.
- Errors must not expose restricted Identity fields.
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
- identity_type and identity_status changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Identity API spec
cite Identity Service Specification
cite Identity Object Specification
cite IdentityCreated and IdentityUpdated Event Specifications
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe responses by default
write tests for credential material rejection
write tests for invalid identity_reference_id
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for IdentityCreated event after successful create
write tests for IdentityUpdated event after successful update
write tests for AI Agent Contract requirement
```

Codex must not:

```text
implement login or token issuance in Identity API
write directly to database bypassing Identity Service
allow UI to emit IdentityCreated or IdentityUpdated directly
treat Identity as User
treat Identity as Permission
treat Identity validation as authentication
expose credentials or secrets
allow AI to fabricate Identity references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Identity API purpose.
[ ] It defines Identity API meaning.
[ ] It defines Identity API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate and event-list operations.
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
| 0.1.0 | Draft | Initial Identity API specification. Defines governed Identity reference interface and separates Identity API from authentication, User, Organization membership, Permission, Policy and AI authority. |

---

**End of API Specification**
