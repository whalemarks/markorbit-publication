# Object Specification — Organization

**Spec ID:** B02-OBJ-ORGANIZATION  
**Spec Type:** Object  
**Object Name:** Organization  
**Owning Domain:** Organization  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-18 — Identity Specification; B02-CH-22 — Domain Specification  
**Source Domain Spec:** core-specs/domains/organization.md  
**Related Object Specs:** core-specs/objects/organization-profile.md; core-specs/objects/organization-status.md; core-specs/objects/organization-member-reference.md; core-specs/objects/organization-unit.md; core-specs/objects/organization-context.md  
**Related Service Specs:** core-specs/services/organization-registration-service.md; core-specs/services/organization-profile-service.md; core-specs/services/organization-status-service.md; core-specs/services/organization-member-reference-service.md; core-specs/services/organization-reference-validation-service.md  
**Related Event Specs:** core-specs/events/organization-created.md; core-specs/events/organization-updated.md; core-specs/events/organization-status-changed.md; core-specs/events/organization-member-linked.md; core-specs/events/organization-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/organization/organization-contract.md; core-specs/contracts/organization/organization-profile-contract.md; core-specs/contracts/organization/organization-context-contract.md; core-specs/contracts/organization/organization-member-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Organization object defines the Core-recognized operating context for a group, company, team, tenant or institutional actor in MarkOrbit.

It exists so that Users, Identities, Permissions, Policies, Customers, Orders, Matters, Tasks, AI Agents, Services, APIs and product consumers can consistently reference the organizational context in which work is performed, governed or consumed.

Organization is required before:

```text
tenant context
team context
user membership reference
permission context
policy context
order ownership context
matter execution context
task assignment context
data isolation context
product workspace context
audit context
```

---

# 2. Core Meaning

Organization means:

```text
a Core-recognized operating context that groups actors, users, teams, resources or service activities under a governed organizational boundary.
```

Organization is not:

```text
Identity
User
Customer
Partner
Agent
Service Provider
Permission
Policy
Role
Matter
Order
Billing account
Legal ownership proof
```

Organization answers:

```text
Which organizational context does this action belong to?
Which users or identities may be associated with this organization?
Which permissions and policies are evaluated under this context?
Which workspace, tenant, team or company boundary applies?
Which customers, orders, matters, tasks or communications may reference this organization?
What audit trace is required?
```

---

# 3. Object Category

Organization is a Foundation Object owned by the Organization Domain.

It provides operating context for MarkOrbit execution.

It may be used by business and collaboration domains, but it must not absorb the meanings of Customer, Partner, Agent or Service Provider.

---

# 4. Architectural Position

Organization sits above Identity and beside User as operating context.

```text
Identity recognizes actor
        ↓
User represents account
        ↓
Organization provides operating context
        ↓
Permission and Policy evaluate access and constraints
        ↓
Business objects execute within context
        ↓
Event and Audit preserve trace
```

Organization provides context.

It does not grant permission.

It does not represent customer relationship by itself.

It does not prove legal ownership.

---

# 5. Scope

The Organization object includes:

```text
organization id
organization type
organization name/reference
organization status
organization profile reference
organization context
organization parent reference
organization unit reference
organization member reference
organization owner reference
source reference
metadata
created time
updated time
audit metadata
```

MVP scope includes:

```text
organization id
organization type
organization name/reference
organization status
organization context
parent organization reference
basic member reference
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Organization ID. |
| organization_type | enum | Yes | Yes | Company, Team, Tenant, Department, InternalUnit, ExternalOrganization, Unknown. |
| name_reference | string | Yes | Yes | Display/name reference; not legal proof by itself. |
| status | enum | Yes | Yes | Controlled Organization status. |
| context_type | enum | Yes | Yes | Tenant, Workspace, TeamContext, ExternalContext, SystemContext, Unknown. |
| parent_organization_id | string | No | Yes | Parent organization reference where applicable. |
| profile_reference_id | string | No | Partial | Organization Profile reference. |
| owner_identity_id | string | No | Partial | Optional responsible owner identity. |
| member_references | array | No | Yes | User/Identity references; structure may be separate object. |
| source_reference | string | No | Yes | Import/source/system reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 organization_type

MVP controlled values:

```text
Company
Team
Tenant
Department
InternalUnit
ExternalOrganization
Unknown
```

## 7.2 context_type

MVP controlled values:

```text
Tenant
Workspace
TeamContext
ExternalContext
SystemContext
Unknown
```

## 7.3 status

MVP controlled values:

```text
Draft
Active
Suspended
Archived
Merged
DeletedReferenceOnly
```

---

# 8. Object Rules

## 8.1 Organization ID Must Be Stable

Organization ID must be immutable after creation.

Merged or superseded organizations must preserve reference history.

## 8.2 Organization Must Not Grant Permission

Organization membership or context does not itself grant access.

Permission and Policy must still be evaluated.

## 8.3 Organization Must Not Replace Customer

An Organization may be linked to Customer, but Organization is not Customer.

Customer owns demand-side commercial relationship.

Organization owns operating context.

## 8.4 Organization Must Not Replace Agent, Partner or Service Provider

External parties may have Organization references.

But Agent, Partner and Service Provider preserve their own relationship meanings.

## 8.5 Organization Must Support Context Isolation

Organization should support tenant/workspace/team context for data governance.

Product consumers must not bypass Organization context.

## 8.6 Organization Must Be Auditable

Organization-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
organization creation
organization status change
organization parent change
organization member linking
organization owner change
organization merge
organization archival
organization context change
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Identity | Organization may link to identity actors | Identity remains actor reference. |
| User | Organization may contain user references | User remains account. |
| Permission | Permission may be scoped by Organization | Organization does not grant permission. |
| Policy | Policy may evaluate Organization context | Organization does not define policy. |
| Customer | Customer may reference Organization | Customer remains demand-side relationship. |
| Partner | Partner may reference Organization | Partner remains cooperation relationship. |
| Agent | Agent may reference Organization | Agent remains trademark collaborator. |
| Service Provider | Provider may reference Organization | Provider remains capability profile. |
| Order | Order may reference Organization context | Order remains commercial service request. |
| Matter | Matter may reference Organization context | Matter remains execution container. |
| Task | Task may be assigned within Organization context | Task remains work unit. |
| Audit Record | Audit may reference Organization | Audit remains accountability system. |

---

# 10. Lifecycle

Organization lifecycle states:

```text
Draft
Active
Suspended
Archived
Merged
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → Active
Active → Suspended
Suspended → Active
Active → Archived
Draft → Archived
Active → Merged
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Active → DeletedReferenceOnly without archival or governed deletion
Merged → Active without explicit restoration service
Archived → Active without review where policy requires it
```

---

# 11. Service Usage

Organization object is created and managed through:

```text
Organization Registration Service
Organization Profile Service
Organization Status Service
Organization Member Reference Service
Organization Context Service
Organization Reference Validation Service
Organization Audit Reference Service
```

Service rules:

```text
- Services must validate organization_type.
- Services must validate context_type.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not grant permissions.
- Services must not create Customer, Partner, Agent or Service Provider directly.
```

---

# 12. Event Usage

Organization object emits or participates in:

```text
OrganizationCreated
OrganizationUpdated
OrganizationStatusChanged
OrganizationMemberLinked
OrganizationMemberUnlinked
OrganizationParentUpdated
OrganizationContextUpdated
OrganizationMerged
OrganizationArchived
OrganizationReferenceValidated
```

Event rules:

```text
- Organization events must reference Organization ID.
- Status events must preserve previous and new status.
- Member events must reference User or Identity where allowed.
- Organization events must not expose confidential member details unnecessarily.
```

---

# 13. API Usage

Potential MVP APIs:

```text
POST /organizations
GET /organizations/{id}
PATCH /organizations/{id}
POST /organizations/{id}/status
POST /organizations/{id}/members
DELETE /organizations/{id}/members/{memberId}
POST /organizations/reference/validate
```

API rules:

```text
- APIs must invoke Organization Services.
- APIs must not grant Permission.
- APIs must not create Customer, Partner, Agent or Service Provider directly.
- APIs must preserve tenant/workspace context.
- APIs must preserve audit context.
```

---

# 14. AI Agent Usage

AI Agents may reference Organization only under governed Agent Contracts.

Allowed AI use:

```text
summarize organization context if authorized
identify missing organization reference
suggest organization linkage for review
flag organization/customer boundary mismatch
flag organization/provider boundary mismatch
```

AI must not:

```text
create organizations without authorized service
merge organizations without review
infer legal ownership from organization context
grant permission based on organization membership
treat organization as Customer, Partner, Agent or Service Provider
expose organization member data outside authorized scope
```

AI organization use requires:

```text
Agent Identity
Agent Contract
Permission Rule
Policy Rule
Audit Rule
Human Review Rule for merge or sensitive linkage
```

---

# 15. Validation Rules

Organization object must pass:

```text
[ ] id is present and immutable.
[ ] organization_type is controlled.
[ ] context_type is controlled.
[ ] status is controlled.
[ ] Organization does not grant Permission.
[ ] Organization does not replace Customer.
[ ] Organization does not replace Agent, Partner or Service Provider.
[ ] Organization can be referenced by Permission, Policy, Event and Audit.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite organization domain spec
preserve Organization / Identity boundary
preserve Organization / User boundary
preserve Organization / Permission boundary
preserve Organization / Customer boundary
preserve Organization / Partner / Agent / Service Provider boundaries
implement only MVP fields unless task says otherwise
write tests for stable id
write tests for controlled organization_type
write tests for controlled context_type
write tests for controlled status
write tests preventing Organization from granting Permission
write tests preventing Organization from becoming Customer
write tests for event emission on mutation
```

Codex must not:

```text
invent full tenant billing system inside Organization object
invent HR org chart system
grant permission through Organization
treat Organization as Customer or legal owner
store sensitive member data by default
allow product UI to redefine Organization status
```

---

# 17. Acceptance Criteria

This Organization Object Specification is accepted only if:

```text
[ ] It defines Organization purpose.
[ ] It defines Organization Core meaning.
[ ] It identifies Organization as Foundation Object.
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
| 0.1.0 | Draft | Initial Organization object specification. Establishes Organization as stable Core operating context, separates Organization from Customer, Partner, Agent, Service Provider, User, Permission and Policy, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
