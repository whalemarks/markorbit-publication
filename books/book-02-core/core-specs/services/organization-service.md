# Service Specification — Organization Service

**Spec ID:** B02-SVC-ORGANIZATION-SERVICE  
**Spec Type:** Service  
**Service Name:** Organization Service  
**Owning Domain:** Organization  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-18 — Identity Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/organization.md  
**Related Object Specs:** core-specs/objects/organization.md; core-specs/objects/user.md; core-specs/objects/identity.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/organization-created.md; core-specs/events/organization-updated.md; core-specs/events/organization-status-changed.md; core-specs/events/organization-user-linked.md; core-specs/events/organization-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/organization/organization-contract.md; core-specs/contracts/organization/organization-reference-contract.md; core-specs/contracts/organization/organization-user-link-contract.md; core-specs/contracts/organization/organization-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Organization Service defines the Core service boundary for creating, updating, validating, linking and managing Organization objects.

It exists so that User, Identity, Permission, Policy, Customer, Partner, Agent, Service Provider, Audit, AI Agents, APIs and product consumers can consistently reference operating contexts without confusing Organization with Customer, Partner, Service Provider, tenant billing account, permission grant or authentication system.

Organization Service is required before:

```text
workspace or tenant context
organization profile creation
user-to-organization linkage
organization-scoped permission evaluation
organization-scoped policy evaluation
customer/provider/partner reference boundary
audit context attribution
AI organization-context handling
cross-domain organization reference validation
```

---

# 2. Core Meaning

Organization Service means:

```text
the Core service that manages operating context references and organization membership/linkage for MarkOrbit-recognized workspaces, companies, teams or institutional contexts.
```

Organization Service does not mean:

```text
Customer Service
Partner Service
Service Provider Service
billing account service
permission engine
policy engine
authentication provider
full CRM/company profile system
```

Organization Service answers:

```text
Does this Organization exist?
Can this Organization be used as operating context?
Which Users are linked to this Organization?
Which Identity/User/Service contexts may reference it?
Is the Organization active, suspended, archived or reference-only?
Can another domain safely store this Organization reference?
```

---

# 3. Service Category

Organization Service is a Foundation Core Service.

It manages operating context.

It does not grant permission.

It does not evaluate policy.

It does not replace business-party domains.

---

# 4. Architectural Position

Organization Service sits beside User Service and above Identity actor recognition.

```text
Identity Service recognizes actor references
        ↓
User Service manages account participants
        ↓
Organization Service provides operating context
        ↓
Permission Service determines allowed action
        ↓
Policy Service evaluates contextual constraints
        ↓
Audit records actor and context trace
```

Organization provides context.

User participates.

Permission authorizes.

Policy constrains.

---

# 5. Scope

Organization Service includes:

```text
organization creation
organization update
organization status management
organization user linkage
organization reference validation
organization resolution
organization audit trace
organization event emission
```

MVP scope includes:

```text
create organization
get organization
update organization metadata
change organization status
link user to organization
unlink user from organization
validate organization reference
resolve organization context
emit organization events
```

Deferred scope includes:

```text
billing account lifecycle
subscription management
advanced org hierarchy
enterprise SSO
legal entity verification
company registry integration
advanced team/department management
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createOrganization | Create Organization object | Yes | OrganizationCreated |
| getOrganization | Retrieve Organization by ID | Yes | No |
| updateOrganization | Update governed Organization metadata | Yes | OrganizationUpdated |
| changeOrganizationStatus | Change Organization lifecycle status | Yes | OrganizationStatusChanged |
| linkOrganizationUser | Link User to Organization | Yes | OrganizationUserLinked |
| unlinkOrganizationUser | Remove User link | Partial | OrganizationUserUnlinked |
| validateOrganizationReference | Validate whether Organization can be referenced | Yes | OrganizationReferenceValidated |
| resolveOrganizationContext | Resolve Organization context from request/reference | Yes | No |
| archiveOrganization | Archive Organization reference | Partial | OrganizationArchived |

---

# 7. Inputs

Organization Service accepts:

```text
organization_type
name_reference
status
user_reference_id
identity_reference_id
link_type
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
organization_type
name_reference
status
source_reference
actor_context
```

Required for user linkage:

```text
organization_reference_id
user_reference_id
link_type
actor_context
```

Required for validation:

```text
organization_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Organization Service returns:

```text
Organization object
Organization reference
Organization validation result
Organization user link result
Organization status result
Organization context result
Organization event reference
error result
```

Validation output must include:

```text
is_valid
organization_reference_id
status
reason_code
policy_hint where applicable
```

Validation output must not expose unnecessary confidential organization metadata.

---

# 9. Controlled Values

## 9.1 organization_type

```text
InternalOrganization
CustomerOrganization
PartnerOrganization
AgentOrganization
ServiceProviderOrganization
SystemOrganization
Unknown
```

## 9.2 status

```text
Draft
Active
Suspended
ReviewRequired
Inactive
Archived
DeletedReferenceOnly
```

## 9.3 organization_user_link_type

```text
Owner
Admin
Member
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
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Organization Provides Operating Context

Organization Service provides operating context for users, permissions, policies, audit and product workspaces.

It must not be reduced to billing account or customer profile.

## 10.2 Organization Is Not Customer

Organization may be linked to Customer.

Customer Service owns demand-side commercial party context.

## 10.3 Organization Is Not Partner, Agent or Service Provider

Organization may reference or be referenced by collaboration objects.

Partner, Agent and Service Provider own their own business meanings.

## 10.4 Organization Does Not Grant Permission

Organization membership or link type does not grant permission by itself.

Permission Service must determine allowed action.

## 10.5 Organization Does Not Evaluate Policy

Organization status and type may be policy inputs.

Policy Service evaluates contextual constraints.

## 10.6 User Linkage Must Be Explicit

User-to-Organization linkage must be created through Organization Service or approved contract.

Implicit linkage from email domain, contact data or customer data is prohibited unless explicitly validated.

## 10.7 Organization Changes Must Be Auditable

Organization-sensitive operations must preserve actor, source, request context and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Identity Service | May validate actor context | Identity owns actor recognition. |
| User Service | User may link to Organization | User owns account participant. |
| Permission Service | Uses Organization as context | Permission grants action. |
| Policy Service | Uses Organization as context | Policy constrains action. |
| Customer Service | May reference Organization | Customer owns demand-side party. |
| Partner Service | May reference Organization | Partner owns cooperation relationship. |
| Agent Service | May reference Organization | Agent owns collaborator profile. |
| Service Provider Service | May reference Organization | Provider owns provider profile. |
| Audit Service | Records Organization context | Audit owns accountability trail. |
| Event Service | Records Organization events | Event records occurrence. |

---

# 12. Event Usage

Organization Service emits:

```text
OrganizationCreated
OrganizationUpdated
OrganizationStatusChanged
OrganizationUserLinked
OrganizationUserUnlinked
OrganizationArchived
OrganizationReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Validation events may be sampled or emitted where audit requires.
- Events must reference Organization ID.
- User link events must reference User ID.
- Events must not expose sensitive organization metadata unnecessarily.
```

---

# 13. API Usage

Potential Phase 1 APIs:

```text
POST /organizations
GET /organizations/{id}
PATCH /organizations/{id}
POST /organizations/{id}/status
POST /organizations/{id}/users
DELETE /organizations/{id}/users/{userId}
POST /organizations/reference/validate
POST /organizations/resolve-context
```

API rules:

```text
- APIs must invoke Organization Service operations.
- APIs must not implement billing/subscription lifecycle.
- APIs must not grant Permission.
- APIs must preserve actor context and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Organization Service only under governed Agent Contracts.

Allowed AI use:

```text
validate Organization reference
summarize non-sensitive organization context
identify missing User-Organization link
identify organization context mismatch
prepare organization-link review note
```

AI must not:

```text
create Organization without authorized service
grant permission through organization membership
bypass policy using organization reference
treat Customer or Provider as Organization automatically
alter Organization status without authorized service
expose sensitive organization metadata
```

AI Organization use requires:

```text
Agent Identity
Agent Contract
Permission Rule
Policy Rule
Organization Access Rule
User Access Rule where applicable
Audit Rule
Human Review Rule for sensitive organization changes
```

---

# 15. Validation Rules

Organization Service must enforce:

```text
[ ] organization_type is controlled.
[ ] status is controlled.
[ ] createOrganization produces stable immutable Organization ID.
[ ] updateOrganization does not mutate immutable ID.
[ ] changeOrganizationStatus follows allowed lifecycle.
[ ] linkOrganizationUser references valid User.
[ ] validateOrganizationReference rejects missing, suspended, inactive, archived or deleted-reference organizations where not allowed.
[ ] Organization Service does not grant Permission.
[ ] Organization Service does not replace Customer, Partner, Agent or Service Provider services.
[ ] Organization Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Organization Service should return controlled errors:

```text
OrganizationNotFound
InvalidOrganizationType
InvalidOrganizationStatus
InvalidOrganizationTransition
InvalidOrganizationReference
UserNotFound
InvalidUserReference
DuplicateOrganizationUserLink
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownOrganizationError
```

Errors must be safe for product display and API consumption.

Sensitive implementation details must not be exposed.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite organization domain spec
cite organization object spec
cite user service spec
preserve Organization / Customer boundary
preserve Organization / Partner boundary
preserve Organization / Agent boundary
preserve Organization / Service Provider boundary
preserve Organization / Permission boundary
preserve Organization / Policy boundary
implement only Phase 1 MVP operations unless task says otherwise
write tests for createOrganization
write tests for validateOrganizationReference
write tests for controlled organization_type
write tests for controlled status
write tests preventing Organization Service from granting Permission
write tests preventing billing/subscription lifecycle inside Organization Service
write tests preventing automatic Customer/Agent/Provider creation from Organization Service
write tests for event emission on mutation
```

Codex must not:

```text
invent full tenant billing system
treat Organization as Customer
treat Organization as Partner
treat Organization as Agent
treat Organization as Service Provider
grant Permission from Organization Service
evaluate Policy inside Organization Service beyond basic reference/status validation
create business-party objects automatically
allow product UI to redefine Organization status
```

---

# 18. Acceptance Criteria

This Organization Service Specification is accepted only if:

```text
[ ] It defines Organization Service purpose.
[ ] It defines Organization Service Core meaning.
[ ] It identifies Organization Service as Foundation Core Service.
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
| 0.1.0 | Draft | Initial Organization Service specification. Establishes Organization Service as operating context service, separates it from Customer, Partner, Agent, Service Provider, Permission, Policy and billing, and defines Phase 1 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
