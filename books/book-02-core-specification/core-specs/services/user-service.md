# Service Specification — User Service

**Spec ID:** B02-SVC-USER-SERVICE  
**Spec Type:** Service  
**Service Name:** User Service  
**Owning Domain:** User  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-18 — Identity Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/user.md  
**Related Object Specs:** core-specs/objects/user.md; core-specs/objects/identity.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/identity-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/user-created.md; core-specs/events/user-updated.md; core-specs/events/user-status-changed.md; core-specs/events/user-identity-linked.md; core-specs/events/user-organization-linked.md; core-specs/events/user-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/user/user-contract.md; core-specs/contracts/user/user-reference-contract.md; core-specs/contracts/user/user-identity-link-contract.md; core-specs/contracts/user/user-organization-link-contract.md; core-specs/contracts/user/user-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

User Service defines the Core service boundary for creating, updating, validating, linking and managing User objects.

It exists so that Identity, Organization, Permission, Policy, Audit, Task, Communication, AI Agents, APIs and product consumers can consistently reference account participants without confusing User with Identity, Organization, Customer, Partner, Agent, Service Provider or authentication implementation.

User Service is required before:

```text
account participant creation
user-to-identity linkage
user-to-organization linkage
portal or workplace participant reference
task assignment
communication participant reference
permission subject evaluation
policy context evaluation
audit actor attribution
AI-assisted user-context handling
```

---

# 2. Core Meaning

User Service means:

```text
the Core service that manages MarkOrbit account participants and their governed links to Identity, Organization and related access contexts.
```

User Service does not mean:

```text
authentication provider
password service
permission engine
policy engine
organization tenant service
customer contact service
agent contact service
full HR/profile system
```

User Service answers:

```text
Does this User exist?
Which Identity does this User reference?
Which Organization contexts may this User be linked to?
Is this User active, suspended, invited, archived or reference-only?
Can another domain safely reference this User?
Can this User be assigned to a Task or Communication context?
```

---

# 3. Service Category

User Service is a Foundation Core Service.

It manages account participant references.

It does not authenticate credentials.

It does not grant permission.

It does not determine policy outcome.

---

# 4. Architectural Position

User Service sits above Identity Service and beside Organization Service.

```text
Identity Service recognizes actor reference
        ↓
User Service manages account participant
        ↓
Organization Service provides operating context
        ↓
Permission Service determines allowed action
        ↓
Policy Service evaluates contextual constraints
        ↓
Audit records actor trace
```

User represents account participant.

Identity recognizes actor.

Permission grants allowed action.

Policy constrains action.

---

# 5. Scope

User Service includes:

```text
user creation
user update
user status management
user identity linkage
user organization linkage
user reference validation
user resolution
user audit trace
user event emission
```

MVP scope includes:

```text
create user
get user
update user profile metadata
change user status
link user to identity
link user to organization
validate user reference
resolve user from identity
emit user events
```

Deferred scope includes:

```text
password login
OAuth/SAML login
multi-factor authentication
advanced user preferences
HR profile management
full contact-center profile
social login
device/session management
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createUser | Create User object | Yes | UserCreated |
| getUser | Retrieve User by ID | Yes | No |
| updateUser | Update governed User metadata | Yes | UserUpdated |
| changeUserStatus | Change User lifecycle status | Yes | UserStatusChanged |
| linkUserIdentity | Link User to Identity | Yes | UserIdentityLinked |
| unlinkUserIdentity | Remove governed Identity link | Partial | UserIdentityUnlinked |
| linkUserOrganization | Link User to Organization context | Yes | UserOrganizationLinked |
| unlinkUserOrganization | Remove Organization link | Partial | UserOrganizationUnlinked |
| validateUserReference | Validate whether User can be referenced | Yes | UserReferenceValidated |
| resolveUserByIdentity | Resolve User from Identity reference | Yes | No |
| archiveUser | Archive User reference | Partial | UserArchived |

---

# 7. Inputs

User Service accepts:

```text
user_type
display_name_reference
identity_reference_id
organization_reference_ids
status
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
user_type
display_name_reference
identity_reference_id
status
source_reference
actor_context
```

Required for validation:

```text
user_reference_id
requesting_domain
requesting_service
actor_context
```

Required for organization linkage:

```text
user_reference_id
organization_reference_id
link_type
actor_context
```

---

# 8. Outputs

User Service returns:

```text
User object
User reference
User validation result
User identity link result
User organization link result
User status result
User event reference
error result
```

Validation output must include:

```text
is_valid
user_reference_id
identity_reference_id
status
reason_code
organization_context_hint where applicable
policy_hint where applicable
```

Validation output must not expose unnecessary personal or confidential data.

---

# 9. Controlled Values

## 9.1 user_type

```text
InternalUser
ExternalUser
CustomerPortalUser
AgentPortalUser
ServiceProviderPortalUser
SystemLinkedUser
Unknown
```

## 9.2 status

```text
Draft
Invited
Active
Suspended
ReviewRequired
Inactive
Archived
DeletedReferenceOnly
```

## 9.3 organization_link_type

```text
Member
Admin
Owner
ExternalMember
ServiceMember
Viewer
Unknown
```

## 9.4 validation_result

```text
Valid
Invalid
NotFound
Inactive
Suspended
Archived
ReviewRequired
OrganizationRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 User Requires Identity

A User must reference a valid Identity.

User Service must validate Identity reference through Identity Service or approved contract.

## 10.2 User Is Not Identity

User manages account participant context.

Identity recognizes actor reference.

## 10.3 User Is Not Organization

User may be linked to Organization.

Organization owns operating context.

## 10.4 User Does Not Grant Permission

User linkage, role label or assignment does not grant permission by itself.

Permission Service must determine allowed action.

## 10.5 User Does Not Evaluate Policy

User status may be a policy input.

Policy Service evaluates contextual constraints.

## 10.6 User Contact Is Not Customer/Agent Contact Automatically

User may link to contact contexts, but User Service must not create Customer, Agent or Service Provider contact objects automatically.

## 10.7 User Changes Must Be Auditable

User-sensitive operations must preserve actor, source, request context and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Identity Service | User must reference Identity | Identity owns actor recognition. |
| Organization Service | User may link to Organization | Organization owns operating context. |
| Permission Service | Uses User/Identity context | Permission grants action. |
| Policy Service | Uses User/Organization context | Policy constrains action. |
| Task Service | May assign Task to User | Task owns work unit. |
| Communication Service | May reference User as participant | Communication owns message lifecycle. |
| Audit Service | Records User/Identity actor trace | Audit owns accountability trail. |
| Event Service | Records User events | Event records occurrence. |

---

# 12. Event Usage

User Service emits:

```text
UserCreated
UserUpdated
UserStatusChanged
UserIdentityLinked
UserIdentityUnlinked
UserOrganizationLinked
UserOrganizationUnlinked
UserArchived
UserReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Validation events may be sampled or emitted where audit requires.
- Events must reference User ID.
- Identity link events must reference Identity ID.
- Organization link events must reference Organization ID.
- Events must not expose sensitive user metadata unnecessarily.
```

---

# 13. API Usage

Potential Phase 1 APIs:

```text
POST /users
GET /users/{id}
PATCH /users/{id}
POST /users/{id}/status
POST /users/{id}/identity
POST /users/{id}/organizations
DELETE /users/{id}/organizations/{organizationId}
POST /users/reference/validate
POST /users/resolve-by-identity
```

API rules:

```text
- APIs must invoke User Service operations.
- APIs must not implement authentication provider logic.
- APIs must not grant Permission.
- APIs must preserve actor context and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use User Service only under governed Agent Contracts.

Allowed AI use:

```text
validate User reference for task or communication context
summarize non-sensitive user context
identify missing User-Identity link
identify missing User-Organization link
prepare user-link review note
```

AI must not:

```text
create User without authorized service
grant permission through User
bypass policy using User reference
impersonate User
alter User status without authorized service
expose sensitive user metadata
create Customer/Agent/Provider contact automatically
```

AI User use requires:

```text
Agent Identity
Agent Contract
Permission Rule
Policy Rule
User Access Rule
Identity Access Rule
Organization Access Rule where applicable
Audit Rule
Human Review Rule for sensitive user changes
```

---

# 15. Validation Rules

User Service must enforce:

```text
[ ] user_type is controlled.
[ ] status is controlled.
[ ] createUser requires valid identity_reference_id.
[ ] createUser produces stable immutable User ID.
[ ] updateUser does not mutate immutable ID.
[ ] changeUserStatus follows allowed lifecycle.
[ ] linkUserIdentity references valid Identity.
[ ] linkUserOrganization references valid Organization.
[ ] validateUserReference rejects missing, suspended, inactive, archived or deleted-reference users where not allowed.
[ ] User Service does not grant Permission.
[ ] User Service does not replace Identity Service.
[ ] User Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

User Service should return controlled errors:

```text
UserNotFound
InvalidUserType
InvalidUserStatus
InvalidUserTransition
InvalidUserReference
IdentityRequired
InvalidIdentityReference
OrganizationNotFound
InvalidOrganizationReference
DuplicateUserIdentityLink
DuplicateUserOrganizationLink
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownUserError
```

Errors must be safe for product display and API consumption.

Sensitive implementation details must not be exposed.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite user domain spec
cite user object spec
cite identity service spec
preserve User / Identity boundary
preserve User / Organization boundary
preserve User / Permission boundary
preserve User / Policy boundary
implement only Phase 1 MVP operations unless task says otherwise
write tests for createUser requiring Identity
write tests for validateUserReference
write tests for controlled user_type
write tests for controlled status
write tests preventing User Service from granting Permission
write tests preventing authentication implementation inside User Service
write tests preventing Customer/Agent/Provider contact creation from User Service
write tests for event emission on mutation
```

Codex must not:

```text
invent full authentication system
store passwords or OAuth secrets
treat User as Identity
treat User as Organization tenant
grant Permission from User Service
evaluate Policy inside User Service beyond basic reference/status validation
create Customer, Agent or Service Provider contacts automatically
allow AI to impersonate User
allow product UI to redefine User status
```

---

# 18. Acceptance Criteria

This User Service Specification is accepted only if:

```text
[ ] It defines User Service purpose.
[ ] It defines User Service Core meaning.
[ ] It identifies User Service as Foundation Core Service.
[ ] It defines service operations.
[ ] It defines inputs and outputs.
[ ] It defines controlled values.
[ ] It defines service rules.
[ ] It defines relationships.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It includes Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial User Service specification. Establishes User Service as account participant service, separates it from Identity, Organization, Permission, Policy and authentication, and defines Phase 1 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
