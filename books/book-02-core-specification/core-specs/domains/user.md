# Domain Specification — User

**Spec ID:** B02-DOM-USER  
**Spec Type:** Domain  
**Domain Name:** User  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/user.md; core-specs/objects/user-profile.md; core-specs/objects/user-status.md; core-specs/objects/user-organization-context.md; core-specs/objects/user-preference.md  
**Related Service Specs:** core-specs/services/user-registration-service.md; core-specs/services/user-profile-service.md; core-specs/services/user-status-service.md; core-specs/services/user-organization-context-service.md; core-specs/services/user-reference-validation-service.md  
**Related Event Specs:** core-specs/events/user-created.md; core-specs/events/user-updated.md; core-specs/events/user-disabled.md; core-specs/events/user-reactivated.md; core-specs/events/user-organization-context-changed.md  
**Related Contract Specs:** core-specs/contracts/user/user-contract.md; core-specs/contracts/user/user-profile-contract.md; core-specs/contracts/user/user-organization-context-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The User Domain defines the Core meaning of a human or operational user account in MarkOrbit.

It exists so that Identity, Organization, Permission, Policy, Task, Review, Approval, Workflow, AI Agent governance, API access and audit records can refer to a user consistently.

User is required before:

```text
organization membership
permission assignment
policy evaluation
task ownership
review ownership
approval ownership
workflow participation
professional responsibility
AI-assisted user actions
Codex task acceptance
product account consumption
```

The User Domain is a Foundation Domain because professional execution requires an accountable user actor associated with Identity and Organization context.

---

# 2. Core Meaning

User means:

```text
a Core-recognized human or operational account that is associated with Identity, may participate in Organizations, and may be referenced by Permissions, Tasks, Reviews, Workflows, APIs and Audit Records.
```

User is not merely:

```text
an email address
a login credential
a contact record
a customer contact
an employee record
a partner contact
a service provider profile
a CRM lead
a product avatar
a chat participant
a billing recipient
```

User answers:

```text
Which Core account represents this human or operational participant?
Which Identity Principal is associated with this user?
Which Organization contexts can this user participate in?
Can this user be referenced by permissions, tasks, reviews, workflows and audit?
What is the user's controlled Core account status?
```

---

# 3. Domain Category

User is a Foundation Domain.

Foundation Domains provide the minimum Core basis for:

```text
accountable human participation
user account lifecycle
organization membership participation
permission assignment target
policy evaluation input
task ownership
review and approval responsibility
audit actor reference
product consumption
```

User must be implemented after Identity and alongside Organization and Permission.

---

# 4. Architectural Position

User sits between Identity and operational execution.

```text
Identity recognizes the actor
        ↓
Organization provides operating context
        ↓
User represents the human or operational account
        ↓
Permission assigns allowed action
        ↓
Policy evaluates constraints
        ↓
Tasks, Reviews and Workflows assign responsibility
        ↓
Events and Audit preserve trace
```

User does not replace Identity.

User does not define Organization context by itself.

User does not grant Permission.

User provides the Core account layer used by higher-level execution.

---

# 5. Scope

The User Domain includes:

```text
user account definition
user lifecycle
user status
user profile boundary
user-to-identity association boundary
user-to-organization participation boundary
user organization context
user reference validation
user audit reference
user preference boundary
user product consumption reference
```

The User Domain supports multiple user roles across products and organizations, but role meaning and permission rules belong to Permission.

MVP implementation should focus on:

```text
basic User
User Status
User Profile boundary
User-to-Identity association
User-to-Organization context reference
User Reference Validation
audit reference
```

---

# 6. Boundary

## 6.1 In Boundary

The User Domain owns:

```text
Core User definition
user account lifecycle
user status
user profile boundary
user display reference
user-to-identity association boundary
user organization context reference
user reference validation
user audit reference
user event emission
```

## 6.2 Out of Boundary

The User Domain does not own:

```text
identity authentication
credential verification
organization creation
organization membership governance by itself
permission assignment rules
policy evaluation logic
employee HR records
customer contact lifecycle
partner contact lifecycle
agent professional qualification
service provider profile
billing contact management
task lifecycle
review decision meaning
approval authority
AI Agent capability authorization
product UI account page
profile image storage implementation
```

Those responsibilities belong to:

```text
Identity Domain
Organization Domain
Permission Domain
Policy system
Customer Domain
Partner Domain
Agent Domain
Service Provider Domain
Task Domain
Review and Approval system
AI Governance
Product implementation
Infrastructure implementation
```

## 6.3 Boundary Notes

Identity recognizes the actor.

User represents the Core account.

Organization provides operating context.

Permission decides what the user may do.

Policy constrains whether the action may proceed.

Task, Review and Workflow assign responsibility to users.

---

# 7. Domain Rules

## 7.1 User Must Reference Identity

Every active User must be associated with at least one Identity Principal or a formally declared identity association rule.

A User without resolvable Identity cannot perform governed Core actions.

## 7.2 User Must Operate in Organization Context

Most governed user actions must include Organization context.

System-level user actions must be explicitly declared.

## 7.3 User Does Not Grant Permission

A User account does not automatically authorize actions.

Permission and Policy must decide allowed actions.

## 7.4 User Must Be Auditable

User-sensitive actions must preserve user reference and identity reference.

Audit-sensitive user actions include:

```text
user creation
user status change
user organization context change
permission assignment involving user
task assignment
task completion
review approval
workflow transition
AI output review
Codex task acceptance
external communication approval
```

## 7.5 User Must Be Product-Neutral

Product-specific account views must consume the User Domain.

They must not redefine User meaning.

---

# 8. Primary Objects

The User Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| User | User | Must Implement | Core-recognized human or operational account. |
| User Profile | User | Partial Implement | Minimal descriptive profile fields for display and account reference. |
| User Status | User | Must Implement | Controlled status indicating whether user may participate in Core execution. |
| User Identity Link | User / Identity | Must Implement | Association between User and Identity Principal. |
| User Organization Context | User / Organization | Must Implement | Resolved organization context for user execution. |
| User Preference | User | Deferred | Product-neutral preference boundary for future consumption. |
| User Reference | User | Must Implement | Portable reference to User used by Services, Events, APIs and Workflows. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Identity Principal | Identity | User must reference Identity. |
| Organization | Organization | User may operate within Organization context. |
| Organization Membership | Organization | User participation in Organization is governed through membership. |
| Permission Assignment | Permission | Permission may reference User as target actor. |
| Policy Evaluation Context | Policy | Policy uses User and Organization context. |
| Task Assignment | Task | Task may be assigned to User. |
| Review Record | Review and Approval | Review may be performed by User. |
| Approval Record | Review and Approval | Approval may be performed by User. |
| AI Output | AI Governance | User may request, review or approve AI output. |
| Audit Record | Audit | Audit records User reference. |

---

# 9. Primary Services

The User Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| User Registration Service | User | Must Implement | Create a Core User associated with Identity. |
| User Profile Service | User | Partial Implement | Create or update product-neutral user profile fields. |
| User Status Service | User | Must Implement | Enable, suspend, disable or reactivate a user through governed rules. |
| User Identity Link Service | User / Identity | Must Implement | Associate or validate User-to-Identity relationship. |
| User Organization Context Service | User / Organization | Must Implement | Resolve organization context for user execution. |
| User Reference Validation Service | User | Must Implement | Validate that a User reference is valid, active and usable. |
| User Audit Reference Service | User / Audit | Partial Implement | Produce user audit reference for governed actions. |

Service rules:

```text
- Mutating User services must emit events.
- User services must not assign permissions directly.
- User services must not create Organization without Organization service.
- User services must not perform authentication infrastructure by themselves.
- User status changes must be auditable.
```

---

# 10. Primary Events

The User Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| UserCreated | User Registration Service | Must Implement | A Core User has been created. |
| UserUpdated | User Profile Service / User Status Service | Partial Implement | Controlled user fields have changed. |
| UserDisabled | User Status Service | Must Implement | User has been disabled for governed execution. |
| UserSuspended | User Status Service | Partial Implement | User has been suspended from some or all actions. |
| UserReactivated | User Status Service | Partial Implement | User has been reactivated through governed rules. |
| UserIdentityLinked | User Identity Link Service | Must Implement | User has been associated with an Identity Principal. |
| UserOrganizationContextChanged | User Organization Context Service | Must Implement | User's active organization context changed or was resolved. |
| UserReferenceValidated | User Reference Validation Service | Partial Implement | User reference has been validated for a governed action. |

Event rules:

```text
- User events must reference User.
- UserIdentityLinked must reference Identity Principal.
- Organization-context events must reference Organization or Tenant Boundary.
- User events must not expose credential secrets.
- User status events must be auditable.
```

---

# 11. Primary Contracts

User requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| User Contract | User Contract | Must Implement | Defines User fields, status, identity link and reference behavior. |
| User Profile Contract | User Contract | Partial Implement | Defines product-neutral profile fields and display reference. |
| User Identity Link Contract | Identity / User Contract | Must Implement | Defines User-to-Identity association. |
| User Organization Context Contract | User / Organization Contract | Must Implement | Defines organization context used by User actions. |
| User Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for user-sensitive actions. |

Contract rules:

```text
- User Contract must reference Identity rather than replace Identity.
- User Contract must not define Permission rules.
- User Organization Context Contract must not redefine Organization.
- User Profile Contract must not become CRM contact management.
```

---

# 12. Relationships to Other Domains

## 12.1 Identity

Identity recognizes the actor.

User represents the Core account associated with the actor.

Every active User must link to Identity.

## 12.2 Organization

Organization provides operating context.

User participates in Organization through membership and context resolution.

## 12.3 Permission

Permission may reference User as a target actor.

User does not grant permission.

## 12.4 Policy

Policy evaluates User and Organization context.

User does not define policy logic.

## 12.5 Task

Task may be assigned to User.

Task lifecycle and task status belong to Task Domain.

## 12.6 Review and Approval

Review and Approval may reference User as reviewer or approver.

Review decision meaning belongs to Review and Approval system.

## 12.7 Customer

Customer contacts may be related to users in product implementation, but User is not Customer Contact.

Customer lifecycle belongs to Customer Domain.

## 12.8 Partner / Agent / Service Provider

A User may work for or represent a Partner, Agent or Service Provider organization.

Professional role, qualification and service capability belong to those domains.

## 12.9 AI Governance

User may request, review, approve or reject AI output.

AI Agent capability and AI Output governance belong to AI Governance.

## 12.10 Audit

Audit records should include User reference for governed actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use User only under governed Agent Contracts.

Allowed AI use:

```text
resolve whether a User reference exists
summarize user-scoped task or review context if authorized
flag missing user reference in tasks, workflows or Codex tasks
identify whether a user is required for review or approval
explain user status if authorized
```

AI must not:

```text
create User without authorized service
disable or reactivate User without governed service
assign permissions
approve its own user-related output
infer private personal attributes
turn user profile into CRM contact intelligence
bypass organization or permission checks
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
User Object Access Rule
User Service Access Rule
User Event Access Rule
Organization Context Rule
Permission Rule
Audit Rule
Human Review Rule where high-risk
```

---

# 14. Workflow Usage

User participates in workflows but does not own most workflows.

User-sensitive workflows may include:

```text
user-registration-workflow.md
user-disablement-review-workflow.md
user-organization-context-workflow.md
task-assignment-workflow.md
review-assignment-workflow.md
approval-workflow.md
ai-output-review-workflow.md
codex-task-acceptance-workflow.md
```

Workflow rules:

```text
- User workflows must reference Workflow Contracts.
- User status changes must be auditable.
- User participation in task/review workflows must preserve responsibility assignment.
- User workflows must not assign permissions directly.
- AI-assisted user workflows must preserve Agent Contract and audit rules.
```

---

# 15. API Usage

User APIs expose user registration, status, profile and context resolution through governed services.

Potential MVP APIs:

```text
POST /users
GET /users/{id}
POST /users/{id}/disable
POST /users/{id}/reactivate
POST /users/{id}/identity-links
POST /users/{id}/organization-context/resolve
POST /users/reference/validate
```

Potential partial APIs:

```text
PATCH /users/{id}/profile
GET /users/{id}/audit-reference
POST /users/{id}/suspend
```

API rules:

```text
- APIs must invoke User Services.
- APIs must preserve Identity and Organization context.
- APIs must not bypass Permission or Policy checks.
- APIs must not expose credential secrets.
- Mutating APIs must emit or cause service-level events.
- User APIs must not create Customer, Partner, Agent or Service Provider profiles.
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
User preference consumers
```

Product rule:

```text
Products consume User.
Products do not redefine User.
```

---

# 17. MVP Scope

User is a Phase 1 / Wave 1 Must Implement domain.

MVP includes:

```text
User
User Status
User Reference
User Identity Link
User Organization Context
User Registration Service
User Status Service
User Identity Link Service
User Organization Context Service
User Reference Validation Service
UserCreated event
UserDisabled event
UserIdentityLinked event
UserOrganizationContextChanged event
basic user metadata validation
source traceability to Identity, Organization, Permission, Policy and Audit systems
```

MVP should support:

```text
internal user account
basic user status
identity association
organization context resolution
user audit reference
task/review/approval user reference
Codex actor user reference
```

MVP does not require advanced user preferences, HR records or customer-facing profile management.

---

# 18. Deferred Scope

Deferred scope includes:

```text
advanced user preference system
public profile pages
avatar/image management
HR employee record management
self-service account recovery UI
user behavior analytics
user risk scoring
complex delegation model
external directory synchronization
cross-tenant user federation
customer portal identity self-management
marketplace public user profile
social login provider implementation
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
User should use stable immutable ID.
User should reference Identity Principal through approved contract.
User Status should use controlled values.
User Organization Context should be reusable by Services, Events, Workflows, APIs and Audit Records.
Disabled users should not perform new governed actions unless explicit exception is approved.
User events should not expose credential secrets or unnecessary private data.
User profile fields should remain minimal and product-neutral in MVP.
```

Suggested controlled User Status values:

```text
Draft
Active
Invited
Suspended
Disabled
Archived
Merged
Superseded
DeletedReferenceOnly
```

MVP controlled status values:

```text
Active
Suspended
Disabled
```

Suggested User Type values:

```text
InternalUser
ClientUser
PartnerUser
ServiceProviderUser
AgentUser
SystemUser
CodexUser
```

MVP controlled User Type values:

```text
InternalUser
SystemUser
CodexUser
```

Do not treat a product login page as Core User meaning.

---

# 20. Codex Implementation Notes

Codex may implement User only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve User / Identity / Organization boundaries
preserve User / Permission / Policy boundaries
preserve User / Customer / Partner / Agent / Service Provider boundaries
implement only MVP scope unless task says otherwise
write tests for user creation
write tests for user-to-identity association
write tests for user organization context resolution
write tests for user disablement
write tests preventing permission assignment inside User
write tests preventing Customer Contact from replacing User
```

Codex must not:

```text
invent authentication infrastructure inside User
invent Permission rules inside User
invent Organization membership governance inside User
invent Customer contact lifecycle inside User
create HR employee system as User MVP
implement public profile features in MVP
treat email address as User identity
create AI Agent behavior without Agent Contract
```

---

# 21. Validation Rules

User Domain must pass the following checks.

```text
[ ] User is classified as Foundation Domain.
[ ] User is counted within the 26 baseline Core Domains.
[ ] User does not change the baseline Core Domain Map.
[ ] User has MVP Phase 1 / Wave 1 classification.
[ ] User has MVP Depth = Must Implement.
[ ] User defines Core meaning.
[ ] User boundary excludes Identity authentication implementation.
[ ] User boundary excludes Permission and Policy rules.
[ ] User boundary excludes Customer, Partner, Agent and Service Provider lifecycle.
[ ] User owns User object.
[ ] User defines User Status.
[ ] User defines User Identity Link.
[ ] User defines User Organization Context.
[ ] User lists primary services.
[ ] Mutating User services emit events.
[ ] User lists primary events.
[ ] User defines contract requirements.
[ ] User defines AI Agent usage constraints.
[ ] User defines workflow usage constraints.
[ ] User defines API usage constraints.
[ ] User defines product consumers.
[ ] User defines MVP and deferred scope.
[ ] User defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn User into Identity
turn User into Permission
turn User into Organization membership governance
turn User into Customer Contact
turn User into Partner Contact
turn User into Agent professional profile
turn User into Service Provider profile
turn User into HR employee system
turn User into product profile UI
treat email or phone as the only user identity
assign permissions directly through User
bypass Policy through user status
allow AI to create, disable or reactivate users without contract and review
allow product account IDs to replace Core User ID
allow Codex to define new user architecture
```

---

# 23. Acceptance Criteria

This User Domain Specification is accepted only if:

```text
[ ] It defines User purpose.
[ ] It defines User Core meaning.
[ ] It identifies User as Foundation Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Identity, Organization, Permission, Policy, Task, Review, Customer, Partner, Agent, Service Provider, AI Governance and Audit.
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
| 0.1.0 | Draft | Initial User Domain specification. Establishes User as Phase 1 Foundation Domain, defines User, User Status, User Identity Link, User Organization Context, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
