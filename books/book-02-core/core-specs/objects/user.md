# Object Specification — User

**Spec ID:** B02-OBJ-USER  
**Spec Type:** Object  
**Object Name:** User  
**Owning Domain:** User  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-18 — Identity Specification; B02-CH-22 — Domain Specification  
**Source Domain Spec:** core-specs/domains/user.md  
**Related Object Specs:** core-specs/objects/identity.md; core-specs/objects/user-profile.md; core-specs/objects/user-status.md; core-specs/objects/user-organization-membership.md; core-specs/objects/user-preference-reference.md; core-specs/objects/user-session-reference.md  
**Related Service Specs:** core-specs/services/user-registration-service.md; core-specs/services/user-profile-service.md; core-specs/services/user-status-service.md; core-specs/services/user-organization-membership-service.md; core-specs/services/user-reference-validation-service.md  
**Related Event Specs:** core-specs/events/user-created.md; core-specs/events/user-updated.md; core-specs/events/user-status-changed.md; core-specs/events/user-organization-linked.md; core-specs/events/user-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/user/user-contract.md; core-specs/contracts/user/user-profile-contract.md; core-specs/contracts/user/user-organization-membership-contract.md; core-specs/contracts/user/user-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The User object defines the Core account-level participant used by MarkOrbit products, services and workflows.

It exists so that Identity, Organization, Permission, Policy, Task, Workflow, Event, Notification, Communication, AI Governance and product consumers can consistently refer to a person or account interacting with the system.

User is required before:

```text
login/account association
workspace participation
organization membership
permission evaluation
policy evaluation
task assignment
responsibility assignment
event actor attribution
notification recipient resolution
communication participant reference
audit trace
product access
```

---

# 2. Core Meaning

User means:

```text
a Core-recognized account participant that links to Identity and may participate in Organizations, Permissions, Policies, workflows, tasks, communications and product experiences.
```

User is not:

```text
Identity
Organization
Permission
Policy
Role
Customer
Partner
Agent
Service Provider
AI Agent
Contact
Employee record
```

User answers:

```text
Which account participant is using MarkOrbit?
Which Identity does the User reference?
Which Organization context may the User belong to?
What status does the User account hold?
Can the User be referenced by Permission, Policy, Task, Event, Notification and Communication?
What product-facing profile or preference references apply?
What audit trace is required?
```

---

# 3. Object Category

User is a Foundation Object owned by the User Domain.

It is a Core account participant object.

It must reference Identity, but it must not replace Identity.

It may be linked to Organization, but it must not replace Organization.

---

# 4. Architectural Position

User sits between Identity and product/account participation.

```text
Identity recognizes actor
        ↓
User represents account participant
        ↓
Organization provides operating context
        ↓
Permission determines allowed action
        ↓
Policy evaluates contextual constraints
        ↓
Task / Workflow / Communication use User as participant
        ↓
Event and Audit preserve trace
```

User participates.

Identity recognizes.

Organization contextualizes.

Permission authorizes.

Policy constrains.

---

# 5. Scope

The User object includes:

```text
user id
identity reference
user type
user status
display reference
profile reference
organization membership reference
preference reference
session reference boundary
source reference
metadata
created time
updated time
audit metadata
```

MVP scope includes:

```text
user id
identity id
user type
user status
display reference
profile reference
organization membership references
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable User ID. |
| identity_id | string | Yes | Yes | Required reference to Identity. |
| user_type | enum | Yes | Yes | HumanUser, SystemUser, ServiceUser, AIAgentUser, ExternalUser, Unknown. |
| status | enum | Yes | Yes | Controlled User status. |
| display_reference | string | No | Yes | Product-facing display reference; not legal proof. |
| profile_reference_id | string | No | Partial | User Profile reference. |
| organization_memberships | array | No | Yes | Organization membership references. |
| preference_reference_id | string | No | Deferred | User preferences reference. |
| session_reference_id | string | No | Deferred | Session reference boundary; not authentication system. |
| source_reference | string | No | Yes | Import/source/system reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 user_type

MVP controlled values:

```text
HumanUser
SystemUser
ServiceUser
AIAgentUser
ExternalUser
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
Invited
Active
Suspended
Archived
DeletedReferenceOnly
```

## 7.3 membership_status

MVP controlled values for organization membership references:

```text
Pending
Active
Suspended
Removed
Archived
```

---

# 8. Object Rules

## 8.1 User Must Reference Identity

Every User must reference a valid Identity.

A User without Identity is not Core-valid.

## 8.2 User Must Not Replace Identity

Identity is the actor recognition layer.

User is the account participant layer.

One User must not be used as the canonical Identity.

## 8.3 User Must Not Grant Permission

A User account does not automatically grant action rights.

Permission and Policy must still be evaluated.

## 8.4 User Must Not Replace Organization Membership Rules

User may reference Organization memberships.

Organization and membership rules must remain governed by Organization, Permission and Policy.

## 8.5 User Is Not Customer Contact by Default

A User may be linked to a Customer Contact in a governed relationship.

User must not automatically become Customer, Partner, Agent, Service Provider or contact person.

## 8.6 User Must Be Auditable

User-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
user creation
identity linkage
user status change
organization membership change
profile reference update
user archival
external user linkage
AI agent user creation
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Identity | User must reference Identity | User is not Identity. |
| Organization | User may have memberships | User is not Organization. |
| Permission | Permission may evaluate User context | User does not grant Permission. |
| Policy | Policy may evaluate User context | User does not define Policy. |
| Capability | Capability may bind to User context | Capability remains separate. |
| Business Responsibility | Responsibility may assign to User | Responsibility remains separate. |
| Task | Task may assign User | Task remains work unit. |
| Event | Event may reference User/Identity | Event remains signal. |
| Notification | Notification may resolve User as recipient | Notification remains awareness intent. |
| Communication | User may participate in Communication | Communication remains message lifecycle. |
| Customer | User may be linked to Customer Contact | Customer remains demand-side relationship. |
| AI Agent | AI Agent may have User reference | AI Governance controls capability. |
| Audit Record | Audit may reference User | Audit remains accountability system. |

---

# 10. Lifecycle

User lifecycle states:

```text
Draft
Invited
Active
Suspended
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → Invited
Draft → Active
Invited → Active
Active → Suspended
Suspended → Active
Active → Archived
Draft → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Active → DeletedReferenceOnly without archival or governed deletion
Suspended → DeletedReferenceOnly without archival
Archived → Active without review where policy requires it
```

---

# 11. Service Usage

User object is created and managed through:

```text
User Registration Service
User Profile Service
User Status Service
User Organization Membership Service
User Reference Validation Service
User Audit Reference Service
```

Service rules:

```text
- Services must validate identity_id.
- Services must validate user_type.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not grant permissions.
- Services must not create Identity unless Identity service is invoked.
- Services must not create Customer, Partner, Agent or Service Provider directly.
```

---

# 12. Event Usage

User object emits or participates in:

```text
UserCreated
UserUpdated
UserStatusChanged
UserIdentityLinked
UserOrganizationLinked
UserOrganizationUnlinked
UserProfileUpdated
UserArchived
UserReferenceValidated
```

Event rules:

```text
- User events must reference User ID.
- UserIdentityLinked must reference Identity ID.
- Status events must preserve previous and new status.
- Organization membership events must reference Organization where allowed.
- User events must not expose confidential profile or membership details unnecessarily.
```

---

# 13. API Usage

Potential MVP APIs:

```text
POST /users
GET /users/{id}
PATCH /users/{id}
POST /users/{id}/status
POST /users/{id}/organizations
DELETE /users/{id}/organizations/{organizationId}
POST /users/reference/validate
```

API rules:

```text
- APIs must invoke User Services.
- APIs must require valid Identity reference.
- APIs must not grant Permission.
- APIs must not mutate Organization lifecycle directly.
- APIs must preserve audit context.
```

---

# 14. AI Agent Usage

AI Agents may reference User only under governed Agent Contracts.

Allowed AI use:

```text
summarize user context if authorized
identify missing user identity reference
suggest user-organization linkage for review
flag user/identity boundary mismatch
flag user/customer contact boundary mismatch
```

AI must not:

```text
create users without authorized service
link users to identities without review where required
grant permission based on user account
infer personal attributes
treat User as Customer, Partner, Agent or Service Provider
expose user profile or membership data outside authorized scope
```

AI user use requires:

```text
Agent Identity
Agent Contract
Permission Rule
Policy Rule
Audit Rule
Human Review Rule for sensitive linkage
```

---

# 15. Validation Rules

User object must pass:

```text
[ ] id is present and immutable.
[ ] identity_id is present.
[ ] identity_id references valid Identity.
[ ] user_type is controlled.
[ ] status is controlled.
[ ] User does not grant Permission.
[ ] User does not replace Identity.
[ ] User does not replace Organization.
[ ] User does not become Customer/Partner/Agent/Service Provider automatically.
[ ] User can be referenced by Task, Event, Notification, Communication and Audit.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite user domain spec
cite identity object spec
preserve User / Identity boundary
preserve User / Organization boundary
preserve User / Permission boundary
preserve User / Customer / Partner / Agent / Service Provider boundaries
implement only MVP fields unless task says otherwise
write tests for stable id
write tests for required identity_id
write tests for controlled user_type
write tests for controlled status
write tests preventing User from granting Permission
write tests preventing User from becoming Identity
write tests preventing User from becoming Customer Contact automatically
write tests for event emission on mutation
```

Codex must not:

```text
invent full authentication system inside User object
invent HR employee profile system
grant permission through User
create Identity implicitly without Identity service
treat User as Customer or contact automatically
store sensitive profile attributes by default
allow product UI to redefine User status
```

---

# 17. Acceptance Criteria

This User Object Specification is accepted only if:

```text
[ ] It defines User purpose.
[ ] It defines User Core meaning.
[ ] It identifies User as Foundation Object.
[ ] It defines fields.
[ ] It defines controlled values.
[ ] It defines object rules.
[ ] It defines relationships.
[ ] It defines lifecycle.
[ ] It defines service usage.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It includes Codex implementation notes.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial User object specification. Establishes User as Core account participant, requires Identity reference, separates User from Identity, Organization, Permission, Customer and external-party roles, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
