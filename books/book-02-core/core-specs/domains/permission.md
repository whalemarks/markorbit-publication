# Domain Specification — Permission

**Spec ID:** B02-DOM-PERMISSION  
**Spec Type:** Domain  
**Domain Name:** Permission  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/permission.md; core-specs/objects/role.md; core-specs/objects/permission-assignment.md; core-specs/objects/access-scope.md; core-specs/objects/permission-check-result.md  
**Related Service Specs:** core-specs/services/permission-assignment-service.md; core-specs/services/permission-check-service.md; core-specs/services/role-management-service.md; core-specs/services/access-scope-validation-service.md; core-specs/services/permission-audit-reference-service.md  
**Related Event Specs:** core-specs/events/permission-assigned.md; core-specs/events/permission-revoked.md; core-specs/events/permission-check-passed.md; core-specs/events/permission-check-failed.md; core-specs/events/role-created.md; core-specs/events/role-updated.md; core-specs/events/access-scope-violation-detected.md  
**Related Contract Specs:** core-specs/contracts/permission/permission-contract.md; core-specs/contracts/permission/permission-assignment-contract.md; core-specs/contracts/permission/access-scope-contract.md; core-specs/contracts/permission/permission-check-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Permission Domain defines the Core meaning of allowed action in MarkOrbit.

It exists so that Identity, User, Organization, Policy, Services, APIs, Workflows, AI Agents and Codex tasks can determine whether an actor may perform a governed action within a defined scope.

Permission is required before:

```text
API access
service execution
task assignment
review approval
workflow transition
AI Agent action
document mutation
classification review
matter operation
order operation
organization administration
Codex task acceptance
external exposure
```

The Permission Domain is a Foundation Domain because Core execution must know not only who the actor is and where the actor operates, but also what the actor may do.

---

# 2. Core Meaning

Permission means:

```text
a governed Core authorization rule or assignment that determines whether an actor may perform a specific action on a specific resource within a defined scope.
```

Permission is not merely:

```text
a UI menu visibility setting
a role name
an admin badge
a user type
an organization membership
a product subscription level
a database access grant
a hard-coded if statement
a frontend route guard
```

Permission answers:

```text
Who is requesting the action?
What action is being requested?
Which resource or object is affected?
Within which organization or tenant boundary?
Under which role, assignment or scope?
Is the action allowed before Policy is evaluated?
What audit trace is required?
```

---

# 3. Domain Category

Permission is a Foundation Domain.

Foundation Domains provide the minimum Core basis for:

```text
authorization
access control
service execution control
API access control
role-based execution
scope-based execution
workflow transition safety
AI Agent action limitation
Codex implementation control
audit accountability
```

Permission must be implemented after Identity, Organization and User are defined, and before high-risk services or APIs are production-enabled.

---

# 4. Architectural Position

Permission sits between actor/context recognition and governed execution.

```text
Identity recognizes the actor
        ↓
Organization provides operating context
        ↓
User represents the account
        ↓
Permission determines allowed action
        ↓
Policy evaluates contextual constraints
        ↓
Service executes or rejects action
        ↓
Event and Audit preserve trace
```

Permission decides whether an actor is authorized to attempt an action.

Policy may still block or constrain the action.

Permission does not define business rules.

Permission does not replace Policy.

---

# 5. Scope

The Permission Domain includes:

```text
permission definition
role definition boundary
permission assignment
permission revocation
access scope
resource scope
organization scope
tenant boundary reference
permission check
permission check result
permission audit reference
permission event emission
permission use by Services, APIs, Workflows and Agents
```

MVP implementation should focus on:

```text
basic Permission
basic Role
Permission Assignment
Access Scope
Permission Check Result
Permission Assignment Service
Permission Check Service
Access Scope Validation Service
PermissionAssigned event
PermissionRevoked event
PermissionCheckPassed event
PermissionCheckFailed event
```

---

# 6. Boundary

## 6.1 In Boundary

The Permission Domain owns:

```text
Core authorization meaning
permission definition
role boundary
permission assignment
permission revocation
access scope
permission check
permission check result
permission-related audit reference
permission event emission
permission references used by Services, APIs, Workflows and Agents
```

## 6.2 Out of Boundary

The Permission Domain does not own:

```text
identity recognition
user profile
organization membership by itself
policy evaluation logic
business eligibility rules
pricing rules
subscription plans
customer grade rules
professional judgment
review decision meaning
approval authority meaning
AI Agent capability definition
workflow state design
product UI menu layout
frontend route design
physical database privilege implementation
infrastructure IAM provider configuration
```

Those responsibilities belong to:

```text
Identity Domain
User Domain
Organization Domain
Policy system
Business Responsibility system
Review and Approval system
AI Governance
Workflow Contract system
Product implementation
Infrastructure implementation
```

## 6.3 Boundary Notes

Identity answers who the actor is.

Organization answers where the actor operates.

User answers which Core account is acting.

Permission answers whether the actor may attempt the action.

Policy answers whether contextual constraints allow the action.

Review and Approval answer whether professional or governance acceptance is required.

---

# 7. Domain Rules

## 7.1 Permission Requires Actor Reference

Every permission check must reference an Identity Principal, User, System Actor or explicitly authorized Agent Identity.

Anonymous governed execution is prohibited unless explicitly defined as public-read or system bootstrap behavior.

## 7.2 Permission Requires Organization or Scope Context

Most permission checks must include Organization, Tenant Boundary or Access Scope.

Global permissions must be explicitly declared and reviewed.

## 7.3 Permission Does Not Replace Policy

Permission may allow an action, but Policy may still block it.

Permission must not encode all contextual business constraints.

## 7.4 Permission Does Not Replace Review or Approval

Permission to perform an action does not equal professional approval.

High-risk actions may require additional Review or Approval.

## 7.5 Permission Must Be Auditable

Permission-sensitive actions must preserve audit trace.

Audit-sensitive permission actions include:

```text
permission assignment
permission revocation
role creation
role update
global access grant
cross-organization access grant
policy override attempt
AI Agent permission grant
Codex task permission grant
high-risk service execution
permission check failure for protected resource
```

## 7.6 Permission Must Be Product-Neutral

Products may consume Permission.

Products must not create product-local authorization rules that bypass Core Permission for governed actions.

---

# 8. Primary Objects

The Permission Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Permission | Permission | Must Implement | Core authorization rule representing allowed action. |
| Role | Permission | Must Implement | Controlled grouping of permissions for assignment convenience. |
| Permission Assignment | Permission | Must Implement | Assignment of permission or role to actor within scope. |
| Access Scope | Permission / Organization | Must Implement | Boundary within which a permission applies. |
| Resource Scope | Permission | Partial Implement | Object, resource or domain boundary affected by permission. |
| Permission Check Result | Permission | Must Implement | Result of evaluating whether an action is authorized. |
| Permission Status | Permission | Must Implement | Controlled status of a permission or assignment. |
| Permission Audit Reference | Permission / Audit | Partial Implement | Audit reference for permission-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Identity Principal | Identity | Permission checks require actor identity. |
| User | User | Permission may be assigned to User. |
| Organization | Organization | Permission scope may be organization-bound. |
| Tenant Boundary | Organization | Permission scope must respect tenant boundary. |
| Policy Evaluation Context | Policy | Policy evaluates context after or with permission. |
| Task Assignment | Task | Task assignment may require permission. |
| Review Record | Review and Approval | Review actions require permission and may create review records. |
| Approval Record | Review and Approval | Approval actions require permission and may create approval records. |
| AI Agent | AI Governance | AI Agent actions require Agent Contract and Permission. |
| API Contract | API | API access requires permission rules. |
| Workflow Transition | Workflow Contract | Workflow transitions require permission checks. |
| Audit Record | Audit | Audit records permission-sensitive actions. |

---

# 9. Primary Services

The Permission Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Permission Assignment Service | Permission | Must Implement | Assign Permission or Role to actor within scope. |
| Permission Revocation Service | Permission | Must Implement | Revoke permission assignment through governed rules. |
| Permission Check Service | Permission | Must Implement | Determine whether actor may perform an action. |
| Role Management Service | Permission | Must Implement | Create, update or disable controlled Roles. |
| Access Scope Validation Service | Permission / Organization | Must Implement | Validate that requested action is within authorized scope. |
| Permission Reference Validation Service | Permission | Must Implement | Validate Permission, Role or Assignment references. |
| Permission Audit Reference Service | Permission / Audit | Partial Implement | Produce permission audit reference for governed actions. |

Service rules:

```text
- Mutating Permission services must emit events.
- Permission Check Service must return controlled results.
- Permission services must not define Policy logic.
- Permission services must not define professional approval logic.
- Permission assignment and revocation must be auditable.
- Global or cross-organization permissions must be review-sensitive.
```

---

# 10. Primary Events

The Permission Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| PermissionAssigned | Permission Assignment Service | Must Implement | Permission or Role has been assigned to actor within scope. |
| PermissionRevoked | Permission Revocation Service | Must Implement | Permission or Role assignment has been revoked. |
| PermissionCheckPassed | Permission Check Service | Must Implement | Actor was authorized for requested action. |
| PermissionCheckFailed | Permission Check Service | Must Implement | Actor was not authorized for requested action. |
| RoleCreated | Role Management Service | Must Implement | Controlled Role has been created. |
| RoleUpdated | Role Management Service | Partial Implement | Role definition or status has changed. |
| RoleDisabled | Role Management Service | Partial Implement | Role has been disabled for assignment or use. |
| AccessScopeViolationDetected | Access Scope Validation Service | Must Implement | Requested action exceeded assigned scope. |
| PermissionAssignmentReviewRequired | Permission Assignment Service | Partial Implement | Permission assignment requires review before activation. |

Event rules:

```text
- Permission events must reference actor identity or user.
- Permission assignment events must reference scope.
- Permission check events must not leak protected resource content.
- Permission failures for sensitive resources must be auditable.
- Role update events must preserve previous and new controlled references where appropriate.
```

---

# 11. Primary Contracts

Permission requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Permission Contract | Permission Contract | Must Implement | Defines Permission fields, action, resource and status behavior. |
| Role Contract | Permission Contract | Must Implement | Defines Role fields and permission grouping rules. |
| Permission Assignment Contract | Permission Contract | Must Implement | Defines actor, permission, role, scope and assignment status. |
| Access Scope Contract | Permission / Organization Contract | Must Implement | Defines organization, tenant, resource and action scope. |
| Permission Check Contract | Permission Contract | Must Implement | Defines permission check input, output and result values. |
| Permission Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for permission-sensitive actions. |

Contract rules:

```text
- Permission Contract must not define Policy rules.
- Role Contract must not become product UI role labels only.
- Permission Assignment Contract must include actor and scope.
- Permission Check Contract must be reusable by Services, APIs, Workflows and Agents.
```

---

# 12. Relationships to Other Domains

## 12.1 Identity

Identity provides actor reference.

Permission checks must resolve actor identity.

## 12.2 User

User may receive permission assignment.

User status may affect whether a permission can be used.

## 12.3 Organization

Organization provides scope and tenant boundary.

Permission assignment is commonly organization-scoped.

## 12.4 Policy

Policy evaluates contextual constraints.

Permission does not replace Policy.

A permission check may pass while policy evaluation fails.

## 12.5 Task

Task creation, assignment, completion and review may require permission.

Task responsibility belongs to Task Domain.

## 12.6 Review and Approval

Permission-sensitive changes may require review or approval.

Permission to approve does not mean approval has occurred.

## 12.7 AI Governance

AI Agent actions require Agent Identity, Agent Contract and Permission.

Permission does not define AI capabilities.

## 12.8 API

APIs must reference Permission rules.

API exposure must not bypass Permission Check Service.

## 12.9 Workflow Contract

Workflow transitions must validate Permission before state mutation.

Permission does not define workflow states.

## 12.10 Audit

Audit records should include permission-sensitive action references.

Audit storage and report rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Permission only under governed Agent Contracts.

Allowed AI use:

```text
check whether a permission reference exists
summarize permission requirements for a workflow or API if authorized
flag missing permission checks in specs or Codex tasks
identify potential scope mismatch
explain why a permission check failed if authorized
recommend review when permission assignment is high-risk
```

AI must not:

```text
assign permissions without authorized service
grant itself permission
override Permission Check Service
bypass Policy after permission check
approve permission assignment by itself
create new Role architecture
infer hidden permissions from user behavior
escalate privileges
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Object Access Rule
Permission Service Access Rule
Permission Event Access Rule
Access Scope Rule
Policy Rule
Audit Rule
Human Review Rule for high-risk changes
```

---

# 14. Workflow Usage

Permission participates in workflows and gates transitions.

Permission-sensitive workflows may include:

```text
permission-assignment-workflow.md
permission-revocation-workflow.md
role-management-review-workflow.md
access-scope-violation-review-workflow.md
api-access-authorization-workflow.md
ai-agent-permission-review-workflow.md
codex-task-permission-review-workflow.md
```

Workflow rules:

```text
- Permission workflows must reference Workflow Contracts.
- Permission assignments must be auditable.
- High-risk permission changes should require review.
- Cross-organization permissions must require explicit review.
- AI Agent permission changes must require Agent Contract and review.
- Permission workflows must not define Policy logic.
```

---

# 15. API Usage

Permission APIs expose assignment, revocation, role management and permission checks through governed services.

Potential MVP APIs:

```text
POST /permissions/assignments
DELETE /permissions/assignments/{id}
POST /permissions/check
POST /permissions/scopes/validate
POST /roles
GET /roles/{id}
PATCH /roles/{id}
```

Potential partial APIs:

```text
POST /permissions/assignments/{id}/review
GET /permissions/audit-references/{id}
POST /permissions/check/batch
```

API rules:

```text
- APIs must invoke Permission Services.
- APIs must preserve Identity, User and Organization context.
- APIs must not bypass Policy where policy applies.
- Mutating APIs must emit or cause service-level events.
- Permission APIs must not expose protected resource content in failed checks.
- Role APIs must not create product-local roles outside Core rules.
```

API details belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

## 16.1 MVP Consumers

```text
Workplace
MarkReg
MarkOrbit Lite
AI Agents
Codex Implementation
Validation tools
```

## 16.2 Partial Consumers

```text
Partner Center
Client Portal
Service Platform
Reporting consumers
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Advanced analytics
Admin consoles
```

Product rule:

```text
Products consume Permission.
Products do not redefine Permission.
```

---

# 17. MVP Scope

Permission is a Phase 1 / Wave 1 Must Implement domain.

MVP includes:

```text
Permission
Role
Permission Assignment
Access Scope
Permission Check Result
Permission Status
Permission Assignment Service
Permission Revocation Service
Permission Check Service
Role Management Service
Access Scope Validation Service
PermissionAssigned event
PermissionRevoked event
PermissionCheckPassed event
PermissionCheckFailed event
RoleCreated event
AccessScopeViolationDetected event
basic permission metadata validation
source traceability to Identity, User, Organization, Policy, API, Agent and Workflow systems
```

MVP should support:

```text
organization-scoped permissions
role-based assignments
basic service-level permission checks
basic API permission checks
basic workflow transition permission checks
AI Agent permission boundary references
Codex task permission boundary references
audit references for assignment and revocation
```

MVP does not require complex attribute-based access control, dynamic policy engines or external IAM integration.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full ABAC policy engine
external IAM synchronization
fine-grained field-level permission system
advanced delegation model
temporary access approval marketplace
public customer self-permission management
cross-tenant federation
permission risk scoring
automatic privilege recommendation
permission anomaly detection
complex approval chains for all roles
external provider RBAC import
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Permission should use stable controlled action identifiers.
Role should be a controlled grouping, not a UI label.
Permission Assignment should reference actor, role or permission, organization context and scope.
Access Scope should be reusable by Services, APIs, Workflows and Agents.
Permission Check Result should use controlled values.
Permission checks should be deterministic and auditable for high-risk actions.
Permission check failure should not leak protected resource data.
```

Suggested Permission Assignment Status values:

```text
Draft
Active
ReviewRequired
Suspended
Revoked
Expired
Superseded
```

MVP controlled assignment status values:

```text
Active
Suspended
Revoked
```

Suggested Permission Check Result values:

```text
Allowed
Denied
PolicyRequired
ReviewRequired
InvalidActor
InvalidScope
InvalidResource
SuspendedActor
SuspendedOrganization
```

MVP controlled permission check result values:

```text
Allowed
Denied
InvalidActor
InvalidScope
```

Do not treat frontend route access as Core Permission meaning.

---

# 20. Codex Implementation Notes

Codex may implement Permission only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Permission / Policy boundary
preserve Permission / Review and Approval boundary
preserve Permission / Identity / User / Organization boundaries
implement only MVP scope unless task says otherwise
write tests for permission assignment
write tests for permission revocation
write tests for permission check
write tests for access scope validation
write tests preventing permission logic inside Identity/User/Organization services
write tests preventing Policy logic from being embedded as Permission
write tests preventing AI self-permission escalation
```

Codex must not:

```text
invent new domain meanings through permissions
implement full ABAC engine in MVP
create UI-only role labels as Core Roles
bypass Policy evaluation where required
allow product UI to mutate permission state directly
allow AI Agents to grant themselves permissions
create global permissions without explicit review rule
treat database grants as Core Permission
```

---

# 21. Validation Rules

Permission Domain must pass the following checks.

```text
[ ] Permission is classified as Foundation Domain.
[ ] Permission is counted within the 26 baseline Core Domains.
[ ] Permission does not change the baseline Core Domain Map.
[ ] Permission has MVP Phase 1 / Wave 1 classification.
[ ] Permission has MVP Depth = Must Implement.
[ ] Permission defines Core meaning.
[ ] Permission boundary excludes Identity, User and Organization meaning.
[ ] Permission boundary excludes Policy evaluation logic.
[ ] Permission boundary excludes professional Review and Approval decision meaning.
[ ] Permission owns Permission object.
[ ] Permission defines Role.
[ ] Permission defines Permission Assignment.
[ ] Permission defines Access Scope.
[ ] Permission defines Permission Check Result.
[ ] Permission lists primary services.
[ ] Mutating Permission services emit events.
[ ] Permission lists primary events.
[ ] Permission defines contract requirements.
[ ] Permission defines AI Agent usage constraints.
[ ] Permission defines workflow usage constraints.
[ ] Permission defines API usage constraints.
[ ] Permission defines product consumers.
[ ] Permission defines MVP and deferred scope.
[ ] Permission defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Permission into Identity
turn Permission into User
turn Permission into Organization membership
turn Permission into Policy
turn Permission into Review or Approval
turn Permission into product menu visibility only
turn Permission into database privilege implementation
turn Role into product UI label only
grant global access without explicit review rules
allow AI to assign permissions to itself
allow product UI to mutate permission state directly
implement full ABAC engine in MVP
bypass tenant boundary validation
allow Codex to define new permission architecture
```

---

# 23. Acceptance Criteria

This Permission Domain Specification is accepted only if:

```text
[ ] It defines Permission purpose.
[ ] It defines Permission Core meaning.
[ ] It identifies Permission as Foundation Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Identity, User, Organization, Policy, Task, Review, AI Governance, API, Workflow and Audit.
[ ] It defines AI Agent usage.
[ ] It defines workflow usage.
[ ] It defines API usage.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Permission Domain specification. Establishes Permission as Phase 1 Foundation Domain, defines Permission, Role, Permission Assignment, Access Scope, Permission Check Result, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
