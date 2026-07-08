# Object Specification — Permission

**Spec ID:** B02-OBJ-PERMISSION  
**Spec Type:** Object  
**Object Name:** Permission  
**Owning Domain:** Permission  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-18 — Identity Specification; B02-CH-22 — Domain Specification  
**Source Domain Spec:** core-specs/domains/permission.md  
**Related Object Specs:** core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/permission-grant.md; core-specs/objects/permission-scope.md; core-specs/objects/permission-action.md; core-specs/objects/permission-status.md; core-specs/objects/permission-evaluation-result.md  
**Related Service Specs:** core-specs/services/permission-grant-service.md; core-specs/services/permission-revocation-service.md; core-specs/services/permission-evaluation-service.md; core-specs/services/permission-scope-validation-service.md; core-specs/services/permission-reference-validation-service.md  
**Related Event Specs:** core-specs/events/permission-created.md; core-specs/events/permission-granted.md; core-specs/events/permission-revoked.md; core-specs/events/permission-evaluated.md; core-specs/events/permission-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/permission/permission-contract.md; core-specs/contracts/permission/permission-grant-contract.md; core-specs/contracts/permission/permission-scope-contract.md; core-specs/contracts/permission/permission-evaluation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Permission object defines the Core authorization rule that determines whether a recognized actor may perform a controlled action within a defined scope.

It exists so that Identity, User, Organization, Policy, Capability, Workflow, Task, API, AI Agent and product consumers can consistently evaluate allowed actions without confusing permission with identity recognition, role label, policy constraint, responsibility assignment or product UI visibility.

Permission is required before:

```text
action authorization
API access control
workflow transition guard
task operation guard
document access guard
evidence access guard
communication access guard
AI agent tool/action access
organization-scoped access
audit trace for allowed or denied action
```

---

# 2. Core Meaning

Permission means:

```text
a Core-recognized authorization rule or grant that allows, denies or constrains a subject’s ability to perform a defined action on a defined resource or scope.
```

Permission is not:

```text
Identity
User
Organization
Policy
Capability
Role
Business Responsibility
Task assignment
Workflow transition
Product UI feature
AI capability
Audit record
```

Permission answers:

```text
Who or what subject is being authorized?
Which action is being evaluated?
Which resource or scope applies?
Is the action allowed, denied or requires review?
Which grant, rule, condition or status applies?
Which organization or context applies?
What audit trace is required?
```

---

# 3. Object Category

Permission is a Foundation Object owned by the Permission Domain.

It is a Core governance object.

It may be consumed by every business, professional and collaboration domain.

It must not absorb Policy, Capability or Business Responsibility meanings.

---

# 4. Architectural Position

Permission sits after Identity/User recognition and before controlled action.

```text
Identity recognizes actor
        ↓
User represents account participant
        ↓
Organization provides operating context
        ↓
Capability describes possible action
        ↓
Permission determines allowed action
        ↓
Policy evaluates contextual constraints
        ↓
Service executes if allowed
        ↓
Event and Audit preserve trace
```

Permission authorizes.

Policy contextualizes.

Capability describes ability.

Responsibility assigns accountability.

---

# 5. Scope

The Permission object includes:

```text
permission id
permission type
permission subject reference
permission action
permission resource reference
permission scope
permission effect
permission status
permission condition reference
organization context
policy reference
capability reference
source reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
permission id
permission type
subject reference
action
resource type
resource id/reference
scope
effect
status
organization context
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Permission ID. |
| permission_type | enum | Yes | Yes | Grant, Deny, Guard, EvaluationRule, SystemRule, Unknown. |
| subject_type | enum | Yes | Yes | Identity, User, Organization, Team, RoleReference, AIAgent, SystemActor. |
| subject_id | string | Yes | Yes | Subject reference. |
| action | string | Yes | Yes | Controlled action name. |
| resource_type | string | Yes | Yes | Target object/domain/resource type. |
| resource_id | string | No | Yes | Optional specific target resource ID. |
| scope_type | enum | Yes | Yes | Global, Organization, Domain, Object, Service, Workflow, API, Product, DataAccess. |
| scope_reference | string | No | Yes | Scope reference where applicable. |
| effect | enum | Yes | Yes | Allow, Deny, ReviewRequired. |
| status | enum | Yes | Yes | Controlled Permission status. |
| condition_reference | string | No | Partial | Optional condition reference; Policy usually owns contextual rules. |
| organization_id | string | No | Yes | Organization context where applicable. |
| policy_reference_id | string | No | Partial | Policy reference where applicable. |
| capability_reference_id | string | No | Partial | Capability reference where applicable. |
| source_reference | string | No | Yes | Source/system/import reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 permission_type

MVP controlled values:

```text
Grant
Deny
Guard
EvaluationRule
SystemRule
Unknown
```

## 7.2 subject_type

MVP controlled values:

```text
Identity
User
Organization
Team
RoleReference
AIAgent
SystemActor
```

## 7.3 scope_type

MVP controlled values:

```text
Global
Organization
Domain
Object
Service
Workflow
API
Product
DataAccess
```

## 7.4 effect

MVP controlled values:

```text
Allow
Deny
ReviewRequired
```

## 7.5 status

MVP controlled values:

```text
Draft
Active
Suspended
Revoked
Expired
Archived
```

---

# 8. Object Rules

## 8.1 Permission Requires Subject, Action and Scope

Every Permission must define:

```text
subject
action
resource or scope
effect
status
```

A Permission without these fields is not Core-valid.

## 8.2 Permission Requires Recognized Subject

Permission subject must reference a valid Identity, User, Organization, Team, AI Agent or System Actor reference.

Unknown free-text subject is prohibited.

## 8.3 Permission Does Not Replace Policy

Permission determines whether an action may be allowed in principle.

Policy evaluates contextual constraints such as jurisdiction, risk, data sensitivity, timing, review requirement or business rule.

## 8.4 Permission Does Not Replace Capability

Capability describes what can be done.

Permission determines whether the subject may do it.

## 8.5 Permission Does Not Assign Responsibility

Permission allows or denies action.

Business Responsibility assigns accountability.

## 8.6 Permission Must Be Auditable

Permission-sensitive changes and evaluations must preserve audit trace.

Audit-sensitive actions include:

```text
permission creation
permission grant
permission revocation
permission status change
permission evaluation
permission denial
permission override
AI permission evaluation
permission scope change
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Identity | Permission may authorize Identity | Identity does not grant Permission. |
| User | Permission may authorize User | User does not grant Permission. |
| Organization | Permission may be scoped by Organization | Organization does not grant Permission. |
| Policy | Policy may constrain Permission evaluation | Policy remains separate. |
| Capability | Permission may authorize capability use | Capability remains descriptive. |
| Business Responsibility | Responsibility may require Permission | Responsibility remains accountability. |
| Task | Task actions may require Permission | Task remains work unit. |
| Workflow Contract | Workflow transitions may require Permission | Workflow remains process structure. |
| Document | Document access/actions may require Permission | Document remains artifact. |
| Evidence | Evidence access/actions may require Permission | Evidence remains proof layer. |
| Communication | Communication access/send may require Permission | Communication remains message lifecycle. |
| AI Agent | AI actions must be Permission-governed | AI Governance remains separate. |
| Event | Permission evaluation may emit Event | Event remains signal. |
| Audit Record | Audit may reference Permission | Audit remains accountability system. |

---

# 10. Lifecycle

Permission lifecycle states:

```text
Draft
Active
Suspended
Revoked
Expired
Archived
```

Lifecycle rules:

```text
Draft → Active
Active → Suspended
Suspended → Active
Active → Revoked
Suspended → Revoked
Active → Expired
Revoked → Archived
Expired → Archived
Draft → Archived
```

Prohibited lifecycle behavior:

```text
Revoked → Active without new grant or restoration service
Expired → Active without renewal/reissue service
Archived → Active without explicit restoration service and review
```

---

# 11. Service Usage

Permission object is created, evaluated and managed through:

```text
Permission Grant Service
Permission Revocation Service
Permission Status Service
Permission Evaluation Service
Permission Scope Validation Service
Permission Reference Validation Service
Permission Audit Reference Service
```

Service rules:

```text
- Services must validate subject reference.
- Services must validate action and scope.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Evaluation service must return controlled result.
- Evaluation service must not execute the requested business action.
- Policy evaluation must be invoked where contextual constraints apply.
```

---

# 12. Event Usage

Permission object emits or participates in:

```text
PermissionCreated
PermissionGranted
PermissionRevoked
PermissionStatusChanged
PermissionScopeUpdated
PermissionEvaluated
PermissionDenied
PermissionReviewRequired
PermissionReferenceValidated
```

Event rules:

```text
- Permission events must reference Permission ID where applicable.
- Evaluation events must preserve subject, action, resource and result references.
- PermissionDenied events must not expose protected resource details unnecessarily.
- AI permission events must identify AI agent source where applicable.
```

---

# 13. API Usage

Potential MVP APIs:

```text
POST /permissions
GET /permissions/{id}
PATCH /permissions/{id}
POST /permissions/{id}/status
POST /permissions/evaluate
POST /permissions/reference/validate
```

API rules:

```text
- APIs must invoke Permission Services.
- APIs must not execute business actions directly.
- APIs must not replace Policy evaluation where Policy applies.
- APIs must preserve audit context.
- AI-facing APIs must respect Agent Contract.
```

---

# 14. AI Agent Usage

AI Agents may use Permission only under governed Agent Contracts.

Allowed AI use:

```text
request permission evaluation
summarize permission denial reason if authorized
identify missing permission reference
flag overbroad permission scope
suggest permission review
```

AI must not:

```text
grant itself permission
override Deny effect
bypass Policy after Permission Allow
execute action after permission check without governed service
create broad permissions without review
hide permission denial
```

AI permission use requires:

```text
Agent Identity
Agent Contract
Capability Binding where applicable
Permission Rule
Policy Rule
Audit Rule
Human Review Rule for high-risk grant or override
```

---

# 15. Validation Rules

Permission object must pass:

```text
[ ] id is present and immutable.
[ ] subject_type is controlled.
[ ] subject_id is present.
[ ] action is present.
[ ] resource_type or scope is present.
[ ] scope_type is controlled.
[ ] effect is controlled.
[ ] status is controlled.
[ ] Permission does not replace Policy.
[ ] Permission does not replace Capability.
[ ] Permission does not assign Responsibility.
[ ] Permission evaluation does not execute action.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite permission domain spec
preserve Permission / Identity boundary
preserve Permission / User boundary
preserve Permission / Organization boundary
preserve Permission / Policy boundary
preserve Permission / Capability / Responsibility boundaries
implement only MVP fields unless task says otherwise
write tests for required subject
write tests for required action
write tests for controlled scope_type
write tests for controlled effect
write tests for controlled status
write tests preventing Permission from executing action
write tests preventing Permission from replacing Policy
write tests preventing AI from granting itself Permission
write tests for event emission on mutation
```

Codex must not:

```text
invent full RBAC/ABAC engine beyond approved scope
grant permission through Identity, User or Organization alone
treat Permission as product UI visibility only
bypass Policy constraints
allow AI self-authorization
execute business action from Permission Evaluation Service
allow product UI to redefine Permission status
```

---

# 17. Acceptance Criteria

This Permission Object Specification is accepted only if:

```text
[ ] It defines Permission purpose.
[ ] It defines Permission Core meaning.
[ ] It identifies Permission as Foundation Object.
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
| 0.1.0 | Draft | Initial Permission object specification. Establishes Permission as Core authorization object, separates Permission from Identity, User, Organization, Policy, Capability and Responsibility, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
