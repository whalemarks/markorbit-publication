# Object Specification — Identity

**Spec ID:** B02-OBJ-IDENTITY  
**Spec Type:** Object  
**Object Name:** Identity  
**Owning Domain:** Identity  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-18 — Identity Specification  
**Source Domain Spec:** core-specs/domains/identity.md  
**Related Object Specs:** core-specs/objects/identity-principal.md; core-specs/objects/identity-reference.md; core-specs/objects/identity-status.md; core-specs/objects/identity-provider-reference.md  
**Related Service Specs:** core-specs/services/identity-registration-service.md; core-specs/services/identity-resolution-service.md; core-specs/services/identity-status-service.md; core-specs/services/identity-reference-validation-service.md  
**Related Event Specs:** core-specs/events/identity-created.md; core-specs/events/identity-resolved.md; core-specs/events/identity-status-changed.md; core-specs/events/identity-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/identity/identity-contract.md; core-specs/contracts/identity/identity-reference-contract.md; core-specs/contracts/identity/identity-resolution-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Identity object defines the Core-recognized actor reference used across MarkOrbit.

It exists so that Users, Organizations, Permissions, Policies, Capabilities, Tasks, Events, AI Agents, Services, APIs and Audit references can consistently refer to an actor without confusing identity recognition with permission, role, organization membership or account lifecycle.

Identity is required before:

```text
user account association
permission evaluation
policy evaluation
actor attribution
event source attribution
task assignment
responsibility assignment
AI agent governance
audit trace
service invocation context
```

---

# 2. Core Meaning

Identity means:

```text
a stable Core-recognized actor reference that identifies a person, system, service, organization actor, AI agent or external actor for attribution, linking and governance.
```

Identity is not:

```text
Permission
Policy
User
Organization
Role
Capability
Customer
Agent
Service Provider
Communication Contact
```

Identity answers:

```text
Who or what is the actor reference?
Is the identity recognized by Core?
Which status does the identity hold?
Which provider or source created it?
Which user, system, service, AI agent or external reference may link to it?
Can it be used for permission, policy, event and audit context?
```

---

# 3. Object Category

Identity is a Foundation Object owned by the Identity Domain.

It is a Core primitive.

It may be referenced by almost every execution object, but it must not absorb the meanings of those objects.

---

# 4. Architectural Position

Identity sits at the bottom of actor governance.

```text
Identity recognizes actor
        ↓
User may represent account
        ↓
Permission determines allowed action
        ↓
Policy evaluates contextual constraints
        ↓
Capability describes available action
        ↓
Responsibility assigns accountability
        ↓
Services execute
        ↓
Events and Audit record trace
```

Identity recognizes.

It does not authorize.

It does not assign responsibility.

It does not execute work.

---

# 5. Scope

The Identity object includes:

```text
identity id
identity type
identity display reference
identity status
identity provider reference
identity source reference
linked user reference
linked organization reference
linked agent reference
linked system actor reference
identity verification boundary
identity audit metadata
created time
updated time
```

MVP scope includes:

```text
identity id
identity type
identity status
display name/reference
provider reference
source reference
created time
updated time
basic linked user reference
basic linked system actor reference
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Identity ID. |
| identity_type | enum | Yes | Yes | Person, System, Service, AIAgent, ExternalActor, OrganizationActor, Unknown. |
| display_reference | string | No | Yes | Human-readable reference; not legal name proof. |
| status | enum | Yes | Yes | Controlled Identity status. |
| provider_reference | string | No | Yes | Source provider or identity authority reference. |
| source_reference | string | No | Yes | Import/source record reference. |
| linked_user_id | string | No | Yes | Optional User reference. |
| linked_organization_id | string | No | Partial | Optional Organization reference. |
| linked_agent_id | string | No | Partial | Optional AI Agent or external agent reference. |
| verification_level | enum | No | Deferred | Recognition/verification level. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 identity_type

MVP controlled values:

```text
Person
System
Service
AIAgent
ExternalActor
OrganizationActor
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
Active
Suspended
Archived
Merged
DeletedReferenceOnly
```

## 7.3 verification_level

Deferred controlled values:

```text
Unverified
SourceRecognized
AccountVerified
OrganizationVerified
ExternalVerified
SystemVerified
```

Verification level is deferred unless required by later approved tasks.

---

# 8. Object Rules

## 8.1 Identity ID Must Be Stable

Identity ID must be immutable after creation.

Merged or superseded identities should preserve references rather than overwrite history.

## 8.2 Identity Must Not Grant Permission

Identity recognition does not mean the actor may act.

Permission and Policy must still be evaluated.

## 8.3 Identity Must Not Replace User

User represents account and product interaction.

Identity represents actor recognition.

One Identity may link to User, but Identity is not User.

## 8.4 Identity Must Support Actor Attribution

Events, Tasks, Services, API calls and AI actions should be able to reference Identity for attribution.

## 8.5 Identity Must Be Auditable

Identity-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
identity creation
identity status change
identity linking
identity merge
identity archival
provider reference update
AI agent identity creation
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| User | Identity may link to User | Identity is not User. |
| Organization | Identity may link to Organization actor | Identity is not Organization. |
| Permission | Permission may reference Identity | Identity does not grant Permission. |
| Policy | Policy may evaluate Identity context | Identity does not define Policy. |
| Capability | Capability may bind to Identity | Capability remains separate. |
| Business Responsibility | Responsibility may assign to Identity | Responsibility remains separate. |
| Task | Task may assign actor via Identity | Task remains work unit. |
| Event | Event may reference actor Identity | Event remains signal. |
| AI Agent | AI Agent must have Identity | AI capability remains governed separately. |
| Audit Record | Audit may reference Identity | Audit remains accountability system. |

---

# 10. Lifecycle

Identity lifecycle states:

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

Identity object is created and managed through:

```text
Identity Registration Service
Identity Resolution Service
Identity Status Service
Identity Link Service
Identity Reference Validation Service
Identity Audit Reference Service
```

Service rules:

```text
- Services must validate identity_type.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not grant permissions.
- Services must not create User unless User service is invoked.
```

---

# 12. Event Usage

Identity object emits or participates in:

```text
IdentityCreated
IdentityUpdated
IdentityResolved
IdentityStatusChanged
IdentityLinked
IdentityMerged
IdentityArchived
IdentityReferenceValidated
```

Event rules:

```text
- Identity events must reference Identity ID.
- Identity status events must preserve previous and new status.
- Identity merge events must preserve source and target references.
- Identity events must not expose unnecessary sensitive data.
```

---

# 13. API Usage

Potential MVP APIs:

```text
POST /identities
GET /identities/{id}
PATCH /identities/{id}
POST /identities/{id}/status
POST /identities/{id}/resolve
POST /identities/reference/validate
```

API rules:

```text
- APIs must invoke Identity Services.
- APIs must not grant Permission.
- APIs must not create User unless User service is invoked.
- APIs must preserve audit context.
```

---

# 14. AI Agent Usage

AI Agents may reference Identity only under governed Agent Contracts.

Allowed AI use:

```text
identify actor reference in allowed context
summarize identity linkage
flag missing actor attribution
suggest identity-reference validation
```

AI must not:

```text
create identities without authorized service
merge identities without review
infer personal attributes
grant permission based on identity
treat display reference as verified legal name
```

AI identity use requires:

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

Identity object must pass:

```text
[ ] id is present and immutable.
[ ] identity_type is controlled.
[ ] status is controlled.
[ ] Identity does not grant Permission.
[ ] Identity does not replace User.
[ ] Identity can be referenced by Event and Audit.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite identity domain spec
preserve Identity / User boundary
preserve Identity / Permission boundary
preserve Identity / Policy boundary
implement only MVP fields unless task says otherwise
write tests for stable id
write tests for controlled identity_type
write tests for controlled status
write tests preventing Identity from granting Permission
write tests preventing Identity from becoming User
write tests for event emission on mutation
```

Codex must not:

```text
invent authentication system inside Identity object
invent HR/person profile system
grant permission through Identity
store sensitive personal attributes by default
treat display_reference as verified legal name
allow product UI to redefine Identity status
```

---

# 17. Acceptance Criteria

This Identity Object Specification is accepted only if:

```text
[ ] It defines Identity purpose.
[ ] It defines Identity Core meaning.
[ ] It identifies Identity as Foundation Object.
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
| 0.1.0 | Draft | Initial Identity object specification. Establishes Identity as stable Core actor reference, separates Identity from User, Permission, Policy and Organization, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
