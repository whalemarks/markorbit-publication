# API Specification — User API

**Spec ID:** B02-API-USER  
**Spec Type:** API Specification  
**API Name:** User API  
**API File:** core-specs/api/user-api.md  
**Related Domain:** core-specs/domains/user.md  
**Related Object Specs:** core-specs/objects/user.md; core-specs/objects/identity.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/user-service.md; core-specs/services/identity-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/user-created.md; core-specs/events/user-updated.md; core-specs/events/identity-created.md; core-specs/events/identity-updated.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/user-api-contract.md; core-specs/contracts/events/user-created-payload.md; core-specs/contracts/events/user-updated-payload.md  
**Related Agent Specs:** core-specs/agents/user-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

User API exposes governed User account participant operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search and validate User references without treating User as Identity, authentication credential, Organization, Organization membership, Permission grant, Policy approval or business role authorization.

User API exists to support:

```text
account participant creation
identity-to-user linkage
user profile safe lookup
user status review
organization participant preparation
permission evaluation subject context
policy evaluation subject context
event trace access
AI-safe user reference handling
```

User API does not authenticate users, issue tokens, manage passwords, grant permissions or define business authority.

---

# 2. API Meaning

User API means:

```text
a governed interface for operating User account participant references through User Service.
```

User API does not mean:

```text
login API
credential API
Identity API
Organization membership API
Permission API
Policy API
role assignment API
approval API
employee HR API
AI authority API
```

A User must reference Identity.

A User is an account participant, not an authorization decision.

---

# 3. API Boundary

User API is responsible for:

```text
User create request intake
User read/search/list access
User update request intake
User reference validation
Identity reference requirement enforcement
safe User response shaping
Permission/Policy enforcement for User operations
User-related Event reference exposure where allowed
AI Agent access boundary for User operations
controlled API errors
```

User API is not responsible for:

```text
authentication
password/session/token management
Identity creation unless explicitly delegated through Identity Service
Organization creation
Organization membership lifecycle
Permission grant
Policy evaluation ownership
business role assignment
task assignment
customer/contact authority
AI Agent authorization by itself
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/user.md
```

Domain rule:

```text
User represents account participant.
User must reference Identity.
User is not authentication, Permission, Policy or Organization membership.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/user.md
core-specs/objects/identity.md
core-specs/objects/organization.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- User API returns user_reference_id.
- User API requires identity_reference_id for User creation.
- User API may reference Organization context but must not create membership silently.
- User API must not expose credential material.
- User API must not treat User existence as Permission.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/user-service.md
core-specs/services/identity-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- User API must invoke User Service for User behavior.
- User API must validate Identity reference through Identity Service where required.
- User API must invoke Permission Service where operation requires authorization.
- User API must invoke Policy Service where contextual constraints apply.
- User API must not emit User events directly; User Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/user-created.md
core-specs/events/user-updated.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createUser may result in UserCreated.
- updateUser may result in UserUpdated.
- protected operations may produce PermissionEvaluated and PolicyEvaluated.
- API consumers must not fabricate UserCreated or UserUpdated.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create User

**Operation Category:** Create  
**Method:** POST  
**Path:** `/users`  
**Owning Service Operation:** `createUser`  
**Permission Required:** `user:create`  
**Policy Required:** `UserCreationPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service Must Emit UserCreated

Meaning:

```text
Create a governed User account participant reference linked to an existing Identity.
```

Non-meaning:

```text
does not create Identity automatically unless explicitly delegated and governed
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
Identity Service validateIdentityReference
  ↓
User Service createUser
  ↓
Event Service record UserCreated
  ↓
Safe API response
```

## 8.2 Operation: Get User

**Operation Category:** Read  
**Method:** GET  
**Path:** `/users/{user_reference_id}`  
**Owning Service Operation:** `getUser`  
**Permission Required:** `user:read`  
**Policy Required:** `UserVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe User account participant view.
```

Non-meaning:

```text
does not expose credentials
does not expose restricted identity data automatically
does not expose organization membership or role authority automatically
```

## 8.3 Operation: Search Users

**Operation Category:** Search  
**Method:** GET  
**Path:** `/users`  
**Owning Service Operation:** `searchUsers`  
**Permission Required:** `user:search`  
**Policy Required:** `UserVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search User references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted directory access
does not expose private account participant data by default
```

## 8.4 Operation: Update User

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/users/{user_reference_id}`  
**Owning Service Operation:** `updateUser`  
**Permission Required:** `user:update`  
**Policy Required:** `UserUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service Must Emit UserUpdated

Meaning:

```text
Update governed User metadata or status under User Service rules.
```

Non-meaning:

```text
does not update Identity automatically
does not update credentials
does not update Organization membership
does not grant Permission
```

## 8.5 Operation: Validate User Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/users/reference/validate`  
**Owning Service Operation:** `validateUserReference`  
**Permission Required:** `user:validate`  
**Policy Required:** `UserReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a User reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not authenticate User
does not authorize action
does not prove Organization membership
does not grant access to target object
```

## 8.6 Operation: List User Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/users/{user_reference_id}/events`  
**Owning Service Operation:** `listUserEvents`  
**Permission Required:** `user:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe User-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create User Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  identity_reference_id: string
  user_type: string
  user_status: string | optional
  display_reference: string | null
  source_type: string
  request_context: object
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update User Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  user_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  user_status: string | optional
  display_reference: string | optional
  source_type: string | optional
  request_context: object
```

## 9.3 Validate User Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  user_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

Request rules:

```text
- Requests must not include passwords, tokens, secrets or raw credential material.
- User creation must include identity_reference_id.
- Requests must use controlled user_type and user_status values.
- Requests must include actor_reference_id for protected operations.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 User Response

```yaml
status: 200
body:
  user_reference_id: string
  identity_reference_id: string
  user_type: string
  user_status: string
  safe_summary:
    display_reference: string | null
    source_type: string
    created_at: datetime
    updated_at: datetime | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create User Response

```yaml
status: 201
body:
  user_reference_id: string
  identity_reference_id: string
  user_status: string
  related_event_reference_ids:
    - user_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Validation Response

```yaml
status: 200
body:
  user_reference_id: string
  identity_reference_id: string | null
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
- Responses must hide restricted Identity/Organization data unless separately authorized.
```

---

# 11. Controlled Values

## 11.1 user_type

```text
HumanUser
SystemUser
AIAgentUser
ExternalUser
ServiceUser
Unknown
```

## 11.2 user_status

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
IdentityMissing
PolicyRestricted
PermissionDenied
ContextMismatch
Unknown
```

## 11.5 intended_use

```text
AccountParticipant
OrganizationMembershipPreparation
PermissionEvaluation
PolicyEvaluation
TaskAssignmentCandidate
CommunicationRecipient
AuditReference
AIAgentAction
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
user:create
user:read
user:search
user:update
user:validate
user:event:read
```

Rules:

```text
- User read/search must be permission-controlled.
- User creation must not imply Permission grant.
- User validation must not be used as authorization decision.
- User existence must not be treated as Organization membership.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
UserCreationPolicy
UserUpdatePolicy
UserVisibilityPolicy
UserReferencePolicy
EventVisibilityPolicy
AIAgentUserAccessPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive User fields.
- Policy may require human review for AI-created or AI-updated User references.
- Policy may restrict cross-organization User lookup.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create User: Restricted
Get User: Restricted
Search Users: Restricted
Update User: Restricted / HumanReviewRequired where sensitive
Validate User Reference: Allowed under contract
List User Events: Restricted
```

AI Agents may:

```text
validate user references for authorized actions
summarize safe User metadata
prepare draft User creation/update requests where allowed
flag missing Identity references
flag invalid User references
```

AI Agents must not:

```text
fabricate User
fabricate UserCreated or UserUpdated events
create User without Identity reference
create User without Agent Contract where required
treat User as authentication
treat User as Permission grant
treat User as Organization membership
expose restricted User data
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

User API may expose:

```text
UserCreated
UserUpdated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create User events directly.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] user_reference_id is present where required.
[ ] identity_reference_id is present for createUser.
[ ] identity_reference_id is valid.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] user_type is controlled.
[ ] user_status is controlled.
[ ] source_type is controlled.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] No credential material is included.
[ ] Restricted fields are omitted or allowed.
[ ] AI Agent Contract is present where required.
[ ] UserCreated is emitted after createUser succeeds.
[ ] UserUpdated is emitted after updateUser succeeds.
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
UserReferenceInvalid
IdentityReferenceMissing
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
- Errors must not expose restricted User fields.
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
- user_type and user_status changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this User API spec
cite User Service Specification
cite User Object Specification
cite Identity Service and Identity Object specs
cite UserCreated and UserUpdated Event Specifications
cite Permission and Policy specs before protected operations
implement request validation before service invocation
validate identity_reference_id before createUser
enforce Permission and Policy before protected operations
return safe responses by default
write tests for credential material rejection
write tests for missing identity_reference_id
write tests for invalid user_reference_id
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for UserCreated event after successful create
write tests for UserUpdated event after successful update
write tests for AI Agent Contract requirement
```

Codex must not:

```text
implement login or token issuance in User API
write directly to database bypassing User Service
allow UI to emit UserCreated or UserUpdated directly
treat User as Identity
treat User as Organization membership
treat User as Permission
treat User validation as authentication
expose credentials or secrets
allow AI to fabricate User references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines User API purpose.
[ ] It defines User API meaning.
[ ] It defines User API boundary.
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
| 0.1.0 | Draft | Initial User API specification. Defines governed User account participant interface and separates User API from Identity, authentication, Organization membership, Permission, Policy and AI authority. |

---

**End of API Specification**
