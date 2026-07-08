# Service Specification — Permission Service

**Spec ID:** B02-SVC-PERMISSION-SERVICE  
**Spec Type:** Service  
**Service Name:** Permission Service  
**Owning Domain:** Permission  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-18 — Identity Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/permission.md  
**Related Object Specs:** core-specs/objects/permission.md; core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/permission-created.md; core-specs/events/permission-updated.md; core-specs/events/permission-status-changed.md; core-specs/events/permission-evaluated.md; core-specs/events/permission-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/permission/permission-contract.md; core-specs/contracts/permission/permission-evaluation-contract.md; core-specs/contracts/permission/permission-reference-contract.md; core-specs/contracts/permission/permission-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Permission Service defines the Core service boundary for creating, updating, validating and evaluating Permission objects and permission rules.

It exists so that Identity, User, Organization, Policy, Services, APIs, AI Agents and product consumers can consistently determine whether an actor is allowed to perform an action on a resource without confusing Permission with Identity, User role, Organization membership, Policy, approval, workflow review or professional judgment.

Permission Service is required before:

```text
service action authorization
API authorization
actor-resource-action evaluation
organization-scoped access control
task action permission check
document/evidence access check
AI agent action permission check
admin operation permission check
audit trace for permission-sensitive actions
```

---

# 2. Core Meaning

Permission Service means:

```text
the Core service that determines whether a recognized actor is allowed to perform a specific action on a specific resource within a defined context.
```

Permission Service does not mean:

```text
Identity Service
User Service
Organization Service
Policy Service
authentication provider
approval workflow
professional review
business responsibility assignment
role label only
```

Permission Service answers:

```text
Who is asking?
What action is requested?
Which resource or object is affected?
Which organization or context applies?
Is the action allowed, denied or review-required?
Which permission rule caused the result?
Should Policy Service also evaluate contextual constraints?
What audit trace is required?
```

---

# 3. Service Category

Permission Service is a Foundation Core Service.

It is the authorization service.

It does not authenticate credentials.

It does not evaluate broader contextual policy.

It does not replace workflow approval or professional review.

---

# 4. Architectural Position

Permission Service sits after Identity/User/Organization recognition and before Policy and service execution.

```text
Identity recognizes actor
        ↓
User represents account participant
        ↓
Organization provides operating context
        ↓
Permission Service determines allowed action
        ↓
Policy Service evaluates contextual constraints
        ↓
Domain Service executes allowed action
        ↓
Event and Audit record outcome
```

Permission answers “may this actor do this action?”

Policy answers “is this action contextually allowed now?”

---

# 5. Scope

Permission Service includes:

```text
permission creation
permission update
permission status management
permission evaluation
permission reference validation
permission rule matching
permission audit trace
permission event emission
```

MVP scope includes:

```text
create permission
get permission
update permission metadata
change permission status
evaluate permission
validate permission reference
emit permission events
```

Deferred scope includes:

```text
full RBAC/ABAC engine
complex inheritance
fine-grained policy composition
external IAM integration
privilege escalation workflow
advanced permission analytics
permission simulation UI
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createPermission | Create Permission object/rule | Yes | PermissionCreated |
| getPermission | Retrieve Permission by ID | Yes | No |
| updatePermission | Update governed metadata/rule fields | Yes | PermissionUpdated |
| changePermissionStatus | Change Permission lifecycle status | Yes | PermissionStatusChanged |
| evaluatePermission | Evaluate actor-action-resource permission | Yes | PermissionEvaluated |
| validatePermissionReference | Validate whether Permission can be referenced | Yes | PermissionReferenceValidated |
| listActorPermissions | List permissions for actor/context | Partial | No |
| archivePermission | Archive Permission reference | Partial | PermissionArchived |

---

# 7. Inputs

Permission Service accepts:

```text
permission_type
status
actor_reference_id
actor_type
action
resource_type
resource_reference_id
organization_reference_id
scope_reference
condition_reference
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
permission_type
actor_reference_id or actor_group_reference
action
resource_type
scope_reference
status
source_reference
actor_context
```

Required for evaluation:

```text
requesting_actor_reference_id
action
resource_type
resource_reference_id
organization_reference_id where applicable
request_context
```

Required for validation:

```text
permission_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Permission Service returns:

```text
Permission object
Permission reference
Permission evaluation result
Permission validation result
Permission status result
Permission event reference
error result
```

Evaluation output must include:

```text
decision
actor_reference_id
action
resource_type
resource_reference_id
matched_permission_reference_id
reason_code
policy_required
review_required
audit_required
```

Evaluation output must not expose unrelated permissions or confidential resource details.

---

# 9. Controlled Values

## 9.1 permission_type

```text
ActionPermission
ResourcePermission
DomainPermission
ServicePermission
AdminPermission
AIAgentPermission
SystemPermission
Unknown
```

## 9.2 status

```text
Draft
Active
Suspended
ReviewRequired
Deprecated
Archived
DeletedReferenceOnly
```

## 9.3 decision

```text
Allowed
Denied
ReviewRequired
NotFound
Suspended
PolicyRequired
Unknown
```

## 9.4 action_type

Suggested controlled values:

```text
Create
Read
Update
Delete
Archive
Link
Unlink
Evaluate
Approve
Reject
Assign
Execute
Export
Send
Import
Unknown
```

---

# 10. Service Rules

## 10.1 Permission Requires Recognized Actor

Permission evaluation must reference a valid Identity/User/System/AI actor context.

Permission Service may call Identity/User services for reference validation.

## 10.2 Permission Grants Allowed Action Only

Permission determines whether an actor may perform an action.

It does not decide whether contextual policy, workflow, professional review or business responsibility allows the action.

## 10.3 Permission Is Not Policy

Policy evaluates contextual constraints.

Permission Service may return `policy_required`, but Policy Service owns policy evaluation.

## 10.4 Permission Is Not Approval

Approval may be required even when permission is allowed.

Workflow Contract and Policy may require review or approval.

## 10.5 Assignment Does Not Grant Permission

Task assignment, responsibility assignment or organization membership must not be treated as permission unless an explicit permission rule applies.

## 10.6 AI Agent Must Be Permission-Governed

AI actions must be evaluated through Permission Service or an approved permission contract.

## 10.7 Permission Changes Must Be Auditable

Permission-sensitive operations must preserve actor, source, request context, evaluation result and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Identity Service | Validates actor reference | Identity recognizes actor. |
| User Service | Provides user context | User manages participant. |
| Organization Service | Provides operating context | Organization provides context. |
| Policy Service | Evaluates contextual constraints | Policy does not grant permission. |
| Workflow Contract | May require permission guards | Workflow owns transition structure. |
| Task Service | May check task action permission | Task owns work unit. |
| Document Service | May check document access | Document owns artifact. |
| Evidence Service | May check evidence access | Evidence owns proof layer. |
| AI Agent Governance | Requires permission for AI action | Agent Contract governs AI use. |
| Audit Service | Records permission-sensitive action | Audit owns accountability trail. |
| Event Service | Records permission events | Event records occurrence. |

---

# 12. Event Usage

Permission Service emits:

```text
PermissionCreated
PermissionUpdated
PermissionStatusChanged
PermissionEvaluated
PermissionDenied
PermissionReviewRequired
PermissionArchived
PermissionReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Permission evaluation events may be emitted where audit requires.
- Denied or review-required actions should be traceable where security or governance requires.
- Events must reference actor, action and resource type safely.
- Events must not expose unrelated permission rules or sensitive resource content.
```

---

# 13. API Usage

Potential Phase 1 APIs:

```text
POST /permissions
GET /permissions/{id}
PATCH /permissions/{id}
POST /permissions/{id}/status
POST /permissions/evaluate
POST /permissions/reference/validate
GET /permissions/actors/{actorReferenceId}
```

API rules:

```text
- APIs must invoke Permission Service operations.
- APIs must not authenticate credentials.
- APIs must not evaluate Policy except by calling Policy Service.
- APIs must not approve workflow or professional actions by themselves.
- APIs must preserve actor context and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Permission Service only under governed Agent Contracts.

Allowed AI use:

```text
check whether the AI actor may perform an action
check whether a referenced user may access a resource
summarize non-sensitive permission result
flag missing permission
prepare permission review note
```

AI must not:

```text
grant itself permission
create permission rule without authorized service and review
bypass policy by relying only on permission
impersonate another actor
hide denied permission results
alter permission status without authorized service
```

AI Permission use requires:

```text
Agent Identity
Agent Contract
Permission Rule
Policy Rule
Permission Access Rule
Audit Rule
Human Review Rule for permission creation, escalation or high-risk action
```

---

# 15. Validation Rules

Permission Service must enforce:

```text
[ ] permission_type is controlled.
[ ] status is controlled.
[ ] decision is controlled.
[ ] createPermission produces stable immutable Permission ID.
[ ] updatePermission does not mutate immutable ID.
[ ] changePermissionStatus follows allowed lifecycle.
[ ] evaluatePermission requires actor, action and resource context.
[ ] evaluatePermission distinguishes Allowed from PolicyRequired and ReviewRequired.
[ ] Task assignment does not grant permission.
[ ] Organization membership does not grant permission by itself.
[ ] Permission Service does not evaluate Policy as final outcome.
[ ] Permission Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Permission Service should return controlled errors:

```text
PermissionNotFound
InvalidPermissionType
InvalidPermissionStatus
InvalidPermissionTransition
InvalidPermissionReference
ActorReferenceRequired
InvalidActorReference
ActionRequired
ResourceReferenceRequired
InvalidResourceReference
PermissionDenied
PolicyRequired
ReviewRequired
AuditContextMissing
UnknownPermissionError
```

Errors must be safe for product display and API consumption.

Sensitive permission rules or protected resource details must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite permission domain spec
cite permission object spec
cite identity/user/organization service specs
preserve Permission / Identity boundary
preserve Permission / User boundary
preserve Permission / Organization boundary
preserve Permission / Policy boundary
preserve Permission / Approval boundary
implement only Phase 1 MVP operations unless task says otherwise
write tests for evaluatePermission requiring actor/action/resource context
write tests for controlled permission_type
write tests for controlled status
write tests for controlled decision
write tests preventing task assignment from granting permission
write tests preventing organization membership from granting permission by itself
write tests preventing Permission Service from evaluating Policy as final outcome
write tests for event emission on mutation
```

Codex must not:

```text
invent full IAM system beyond approved MVP
implement password or authentication logic
treat User role label as Permission automatically
treat Organization membership as Permission automatically
evaluate Policy inside Permission Service as final outcome
approve workflow or professional review from Permission Service
allow AI to grant or escalate its own permissions
allow product UI to redefine Permission status
```

---

# 18. Acceptance Criteria

This Permission Service Specification is accepted only if:

```text
[ ] It defines Permission Service purpose.
[ ] It defines Permission Service Core meaning.
[ ] It identifies Permission Service as Foundation Core Service.
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
| 0.1.0 | Draft | Initial Permission Service specification. Establishes Permission Service as authorization service, separates it from Identity, User, Organization, Policy and approval, and defines Phase 1 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
