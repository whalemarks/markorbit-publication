# Service Specification — Identity Service

**Spec ID:** B02-SVC-IDENTITY-SERVICE  
**Spec Type:** Service  
**Service Name:** Identity Service  
**Owning Domain:** Identity  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-18 — Identity Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/identity.md  
**Related Object Specs:** core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Event Specs:** core-specs/events/identity-created.md; core-specs/events/identity-updated.md; core-specs/events/identity-linked.md; core-specs/events/identity-status-changed.md; core-specs/events/identity-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/identity/identity-contract.md; core-specs/contracts/identity/identity-reference-contract.md; core-specs/contracts/identity/identity-link-contract.md; core-specs/contracts/identity/identity-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Identity Service defines the Core service boundary for creating, validating, linking, updating and resolving Identity objects.

It exists so that User, Organization, Permission, Policy, Audit, AI Agents, APIs and product consumers can consistently reference actors without confusing Identity with User account, Organization tenant, Role, Permission or authentication implementation.

Identity Service is required before:

```text
user registration
organization membership
permission evaluation
policy evaluation
audit actor reference
AI agent actor trace
service mutation attribution
cross-domain actor reference validation
```

---

# 2. Core Meaning

Identity Service means:

```text
the Core service that manages stable actor references and identity validation for MarkOrbit-recognized actors.
```

Identity Service does not mean:

```text
authentication provider
password system
OAuth implementation
role engine
permission engine
policy engine
user profile service
organization service
```

Identity Service answers:

```text
Does this actor reference exist?
Can this actor reference be used?
Which Identity is linked to this User, Organization, System Actor or AI Agent?
Is the Identity active, suspended, archived or reference-only?
Can another domain safely reference this Identity?
```

---

# 3. Service Category

Identity Service is a Foundation Core Service.

It is actor-reference infrastructure.

It does not grant access.

It does not evaluate contextual rules.

It does not authenticate credentials.

---

# 4. Architectural Position

Identity Service sits under User, Organization, Permission, Policy and Audit.

```text
Identity Service recognizes actor references
        ↓
User Service manages account participant
        ↓
Organization Service manages operating context
        ↓
Permission Service determines allowed action
        ↓
Policy Service evaluates contextual constraints
        ↓
Audit records actor trace
```

Identity is recognition.

Permission is authorization.

Policy is contextual constraint.

---

# 5. Scope

Identity Service includes:

```text
identity creation
identity update
identity status management
identity link management
identity reference validation
identity resolution
identity audit trace
identity event emission
```

MVP scope includes:

```text
create identity
get identity
update identity metadata
change identity status
link identity to user/system/agent reference
validate identity reference
emit identity events
```

Deferred scope includes:

```text
external identity provider integration
OAuth/SAML implementation
password lifecycle
biometric identity
advanced identity federation
identity risk scoring
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createIdentity | Create stable Identity object | Yes | IdentityCreated |
| getIdentity | Retrieve Identity by ID | Yes | No |
| updateIdentity | Update governed metadata | Yes | IdentityUpdated |
| changeIdentityStatus | Change Identity lifecycle status | Yes | IdentityStatusChanged |
| linkIdentity | Link Identity to User/System/Agent reference | Yes | IdentityLinked |
| unlinkIdentity | Remove governed link | Partial | IdentityUnlinked |
| validateIdentityReference | Validate whether Identity can be referenced | Yes | IdentityReferenceValidated |
| resolveIdentity | Resolve Identity from allowed reference | Yes | No |
| archiveIdentity | Archive Identity reference | Partial | IdentityArchived |

---

# 7. Inputs

Identity Service accepts:

```text
identity_type
display_reference
status
source_reference
linked_object_type
linked_object_reference_id
metadata
actor_context
request_context
```

Required for creation:

```text
identity_type
display_reference
status
source_reference
actor_context
```

Required for validation:

```text
identity_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Identity Service returns:

```text
Identity object
Identity reference
Identity validation result
Identity link result
Identity status result
Identity event reference
error result
```

Validation output must include:

```text
is_valid
identity_reference_id
status
reason_code
policy_hint where applicable
```

Validation output must not expose unnecessary personal or confidential data.

---

# 9. Controlled Values

## 9.1 identity_type

```text
Human
System
AIAgent
ServiceAccount
ExternalActor
Unknown
```

## 9.2 status

```text
Draft
Active
Suspended
ReviewRequired
Archived
DeletedReferenceOnly
```

## 9.3 link_type

```text
UserAccount
OrganizationMember
SystemActor
AIAgentActor
ExternalContact
ServiceAccount
Unknown
```

## 9.4 validation_result

```text
Valid
Invalid
NotFound
Suspended
Archived
ReviewRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Identity Recognition Only

Identity Service recognizes actors.

It must not grant permission.

## 10.2 Identity Is Not User

Identity may link to User.

User Service owns account participant details.

## 10.3 Identity Is Not Organization

Identity may act inside Organization context.

Organization Service owns operating context.

## 10.4 Identity Status Must Be Enforced

Inactive, suspended, archived or deleted-reference identities must not be treated as active actor references.

## 10.5 Identity Reference Validation Must Be Explicit

Any domain storing actor reference should validate through Identity Service or an approved reference-validation contract.

## 10.6 Identity Changes Must Be Auditable

Identity-sensitive operations must preserve actor, source, request context and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| User Service | May create/link Identity | User owns account details. |
| Organization Service | May validate member actor references | Organization owns operating context. |
| Permission Service | Uses Identity as actor reference | Permission grants allowed action. |
| Policy Service | Uses Identity in contextual evaluation | Policy constrains action. |
| Audit Service | Records Identity as actor | Audit owns accountability trail. |
| AI Agent Governance | Uses AIAgent Identity | Agent Contract governs AI use. |
| Event Service | Records Identity events | Event records occurrence. |

---

# 12. Event Usage

Identity Service emits:

```text
IdentityCreated
IdentityUpdated
IdentityStatusChanged
IdentityLinked
IdentityUnlinked
IdentityArchived
IdentityReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Validation events may be sampled or emitted where audit requires.
- Events must reference Identity ID.
- Events must not expose sensitive identity metadata unnecessarily.
- AI Agent identity events must identify AI actor type.
```

---

# 13. API Usage

Potential Phase 1 APIs:

```text
POST /identities
GET /identities/{id}
PATCH /identities/{id}
POST /identities/{id}/status
POST /identities/{id}/links
DELETE /identities/{id}/links/{linkId}
POST /identities/reference/validate
POST /identities/resolve
```

API rules:

```text
- APIs must invoke Identity Service operations.
- APIs must not implement authentication provider logic.
- APIs must not grant Permission.
- APIs must preserve actor context and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Identity Service only under governed Agent Contracts.

Allowed AI use:

```text
validate own Identity reference
validate referenced actor for trace
summarize non-sensitive identity context
flag missing identity link
prepare identity-link review note
```

AI must not:

```text
create human identity without authorized service
grant permission through identity
bypass policy using identity reference
impersonate human actor
alter identity status without authorized service
expose sensitive identity metadata
```

AI Identity use requires:

```text
Agent Identity
Agent Contract
Permission Rule
Policy Rule
Identity Access Rule
Audit Rule
Human Review Rule for sensitive identity changes
```

---

# 15. Validation Rules

Identity Service must enforce:

```text
[ ] identity_type is controlled.
[ ] status is controlled.
[ ] createIdentity produces stable immutable Identity ID.
[ ] updateIdentity does not mutate immutable ID.
[ ] changeIdentityStatus follows allowed lifecycle.
[ ] linkIdentity references valid target object type.
[ ] validateIdentityReference rejects missing, suspended, archived or deleted-reference identities.
[ ] Identity Service does not grant Permission.
[ ] Identity Service does not replace User Service.
[ ] Identity Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Identity Service should return controlled errors:

```text
IdentityNotFound
InvalidIdentityType
InvalidIdentityStatus
InvalidIdentityTransition
InvalidIdentityReference
InvalidLinkTarget
DuplicateIdentityLink
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownIdentityError
```

Errors must be safe for product display and API consumption.

Sensitive implementation details must not be exposed.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite identity domain spec
cite identity object spec
preserve Identity / User boundary
preserve Identity / Organization boundary
preserve Identity / Permission boundary
preserve Identity / Policy boundary
implement only Phase 1 MVP operations unless task says otherwise
write tests for createIdentity
write tests for validateIdentityReference
write tests for controlled identity_type
write tests for controlled status
write tests preventing Identity Service from granting Permission
write tests preventing authentication implementation inside Identity Service
write tests for event emission on mutation
```

Codex must not:

```text
invent full authentication system
store passwords or OAuth secrets
treat Identity as User profile
grant Permission from Identity Service
evaluate Policy inside Identity Service beyond basic reference status
allow AI to impersonate Identity
allow product UI to redefine Identity status
```

---

# 18. Acceptance Criteria

This Identity Service Specification is accepted only if:

```text
[ ] It defines Identity Service purpose.
[ ] It defines Identity Service Core meaning.
[ ] It identifies Identity Service as Foundation Core Service.
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
| 0.1.0 | Draft | Initial Identity Service specification. Establishes Identity Service as actor-reference service, separates it from authentication, User, Organization, Permission and Policy, and defines Phase 1 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
