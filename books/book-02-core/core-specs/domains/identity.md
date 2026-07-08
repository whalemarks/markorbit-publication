# Domain Specification — Identity

**Spec ID:** B02-DOM-IDENTITY  
**Spec Type:** Domain  
**Domain Name:** Identity  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/identity-principal.md; core-specs/objects/identity-credential.md; core-specs/objects/identity-provider-link.md; core-specs/objects/authentication-session.md  
**Related Service Specs:** core-specs/services/identity-principal-resolution-service.md; core-specs/services/identity-registration-service.md; core-specs/services/identity-credential-verification-service.md; core-specs/services/authentication-session-service.md  
**Related Event Specs:** core-specs/events/identity-created.md; core-specs/events/identity-linked.md; core-specs/events/identity-verified.md; core-specs/events/identity-disabled.md; core-specs/events/authentication-succeeded.md; core-specs/events/authentication-failed.md  
**Related Contract Specs:** core-specs/contracts/identity/identity-contract.md; core-specs/contracts/identity/authentication-session-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Identity Domain defines the Core meaning of a recognized actor in MarkOrbit.

It exists so that users, organizations, permissions, AI agents, workflows, services, audit records and product consumers can refer to a stable identity without redefining identity in each product.

Identity is required before:

```text
User
Organization
Permission
Policy
Task
Review
Approval
AI Agent
Audit
Codex Task
Workflow
API access
```

The Identity Domain is a Foundation Domain because all accountable execution requires a known actor.

---

# 2. Core Meaning

Identity means:

```text
a stable Core-recognized actor reference that can be authenticated, linked, resolved, disabled, audited and used as the basis for accountable execution.
```

Identity is not merely:

```text
a login form
an email address
a phone number
a user profile
an organization member
a permission role
a contact record
a customer record
a product account page
```

Identity answers:

```text
Who or what is this actor within Core?
Can this actor be resolved consistently?
Can this actor be authenticated or linked?
Can actions by this actor be audited?
Can this actor be used by User, Permission, Workflow, Agent and API layers?
```

---

# 3. Domain Category

Identity is a Foundation Domain.

Foundation Domains provide the minimum Core basis for:

```text
actor recognition
accountability
access control
ownership
review
approval
audit
system execution
AI governance
Codex implementation control
```

Identity must be implemented before higher-level professional and business domains can execute safely.

---

# 4. Architectural Position

Identity sits at the base of the Core architecture.

```text
Principles define
        ↓
Core provides
        ↓
Identity recognizes actors
        ↓
User / Organization / Permission assign roles and access
        ↓
Services execute accountable actions
        ↓
Events and audit preserve trace
```

Identity provides the actor reference used by other domains.

It does not define what the actor is allowed to do.

That belongs to Permission and Policy.

---

# 5. Scope

The Identity Domain includes:

```text
identity principal definition
identity principal lifecycle
identity provider linkage
credential reference and verification boundary
authentication session boundary
identity resolution
identity enablement and disablement
identity audit reference
identity-to-user association boundary
identity-to-agent association boundary
identity-to-external-actor association boundary
```

The Identity Domain supports both human and non-human actors.

Actor types may include:

```text
Human User
System Actor
AI Agent
Codex Agent
External Professional Agent
Service Account
Integration Actor
```

MVP implementation should focus on Human User, System Actor and AI Agent identity references.

---

# 6. Boundary

## 6.1 In Boundary

The Identity Domain owns:

```text
recognition of an actor as a Core identity
identity principal creation
identity principal resolution
identity principal status
identity provider link
credential verification boundary
authentication session boundary
identity disablement
identity audit reference
identity event emission
identity reference used by other domains
```

## 6.2 Out of Boundary

The Identity Domain does not own:

```text
user profile meaning
organization membership
role assignment
permission rules
policy rules
customer contact information
partner contact information
service provider profile
agent professional qualification
AI Agent capability authorization
workflow task ownership
product UI account settings
password storage implementation
OAuth provider implementation
physical authentication infrastructure
```

Those responsibilities belong to:

```text
User Domain
Organization Domain
Permission Domain
Policy system
Partner Domain
Agent Domain
Service Provider Domain
AI Governance
Workflow Contract system
Product implementation
Infrastructure implementation
```

## 6.3 Boundary Notes

Identity recognizes the actor.

User describes the human user's Core account.

Organization defines the group or legal/operational container.

Permission defines what the identity may do.

Policy defines contextual constraints.

AI Governance defines what an AI Agent identity may perform.

---

# 7. Domain Rules

## 7.1 Identity Must Be Stable

An Identity Principal must remain stable across products and services.

Product-specific account IDs must not replace Core Identity IDs.

## 7.2 Identity Must Be Resolvable

Every actor performing a governed Core action must be resolvable to an Identity Principal or explicitly declared System Actor.

## 7.3 Identity Must Be Auditable

High-risk actions must record actor identity.

Audit-sensitive actions include:

```text
permission assignment
policy override
AI output approval
task completion
review approval
workflow transition
document approval
classification decision
Codex task acceptance
external communication action
```

## 7.4 Identity Does Not Grant Permission

Identity recognition alone does not allow action.

Permission and Policy must decide whether the identity may perform an action.

## 7.5 Identity Must Support Non-Human Actors

AI Agents, System Actors, Codex Agents and Integration Actors must have explicit identity references.

A prompt is not an identity.

A model call is not an identity.

A background job is not automatically an identity unless registered as a System Actor or Service Account.

---

# 8. Primary Objects

The Identity Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Identity Principal | Identity | Must Implement | Stable Core-recognized actor reference. |
| Identity Credential | Identity | Partial Implement | Credential reference or verification boundary associated with an identity. |
| Identity Provider Link | Identity | Partial Implement | Link between Core Identity and an external identity provider. |
| Authentication Session | Identity | Partial Implement | Bounded authenticated session associated with an Identity Principal. |
| Identity Status | Identity | Must Implement | Controlled status indicating whether an identity may be resolved or used. |
| Actor Reference | Identity | Must Implement | Portable reference to a human, system, agent or integration actor. |

Related objects owned by other domains:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| User | User | A User is associated with one or more Identity Principals. |
| Organization | Organization | Identity may act within an Organization through membership. |
| Permission Assignment | Permission | Permission references Identity or User as actor. |
| Policy Evaluation Context | Policy | Policy uses identity as one input. |
| AI Agent | AI Governance / Agent specs | AI Agent requires explicit identity reference. |
| Codex Task | Codex Governance | Codex task acceptance records actor identity. |
| Review Record | Review and Approval | Review records reviewer identity. |
| Audit Record | Audit | Audit records actor identity. |

---

# 9. Primary Services

The Identity Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Identity Principal Resolution Service | Identity | Must Implement | Resolve actor reference to Identity Principal. |
| Identity Registration Service | Identity | Must Implement | Register a new Identity Principal. |
| Identity Status Service | Identity | Must Implement | Enable, disable or update identity status through governed rules. |
| Identity Provider Link Service | Identity | Partial Implement | Link or unlink external identity provider reference. |
| Identity Credential Verification Service | Identity | Partial Implement | Verify credential boundary or external credential result. |
| Authentication Session Service | Identity | Partial Implement | Create, validate or revoke authentication session boundary. |
| Actor Reference Validation Service | Identity | Must Implement | Validate that a service/event/action actor is resolvable. |

Service rules:

```text
- Mutating Identity services must emit events.
- Identity services must not assign permissions.
- Identity services must not define organization membership.
- Identity services must preserve audit references.
- Identity disablement must be governed and auditable.
```

---

# 10. Primary Events

The Identity Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| IdentityCreated | Identity Registration Service | Must Implement | A Core Identity Principal has been created. |
| IdentityResolved | Identity Principal Resolution Service | Partial Implement | An actor reference has been resolved to a Core Identity Principal. |
| IdentityLinked | Identity Provider Link Service | Partial Implement | Identity has been linked to an external provider reference. |
| IdentityUnlinked | Identity Provider Link Service | Deferred | Identity has been unlinked from an external provider reference. |
| IdentityVerified | Identity Credential Verification Service | Partial Implement | Identity credential or provider link has been verified. |
| IdentityDisabled | Identity Status Service | Must Implement | Identity has been disabled for governed execution. |
| IdentityReenabled | Identity Status Service | Partial Implement | Disabled identity has been reenabled through governed review. |
| AuthenticationSucceeded | Authentication Session Service | Partial Implement | Authentication session was successfully established. |
| AuthenticationFailed | Authentication Session Service | Partial Implement | Authentication attempt failed. |
| AuthenticationSessionRevoked | Authentication Session Service | Partial Implement | Authentication session was revoked. |

Event rules:

```text
- Identity events must reference Identity Principal.
- Security-sensitive events must preserve audit reference.
- Authentication events must not expose credential secrets.
- Event naming must represent meaningful Core change or governed access event.
```

---

# 11. Primary Contracts

Identity requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Identity Contract | Identity Contract | Must Implement | Defines Identity Principal fields, status and reference behavior. |
| Actor Reference Contract | Identity Contract | Must Implement | Defines how other domains reference an actor. |
| Authentication Session Contract | Identity Contract | Partial Implement | Defines authenticated session boundary and lifecycle. |
| Identity Provider Link Contract | Identity Contract | Partial Implement | Defines external provider linkage fields and validation. |
| Identity Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for identity-sensitive actions. |

Contract rules:

```text
- Identity Contract must not include permission rules.
- Actor Reference Contract must be reusable by Services, Events, Workflows, Agents and APIs.
- Authentication Session Contract must not define vendor-specific authentication infrastructure.
```

---

# 12. Relationships to Other Domains

## 12.1 User

Identity recognizes the actor.

User describes the human or operational account profile.

A User may have one or more associated Identity Principals depending on implementation policy.

## 12.2 Organization

Organization provides group context.

Identity does not define membership.

Membership is governed by Organization and Permission.

## 12.3 Permission

Permission uses identity or user references to decide allowed actions.

Identity does not grant permission.

## 12.4 Policy

Policy evaluates identity as one input.

Identity does not define policy logic.

## 12.5 AI Governance

AI Agents require explicit identity references.

Agent capability authorization is owned by Agent specs and AI Governance, not Identity.

## 12.6 Workflow Contract

Workflow transitions must record actor identity when actions are accountable.

Identity does not define workflow states.

## 12.7 Audit

Audit records must reference actor identity for governed actions.

Audit storage and reporting rules belong to the Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Identity only under governed Agent Contracts.

Allowed AI use:

```text
resolve whether an actor reference exists
summarize identity-linked audit trace if authorized
flag missing actor reference in a workflow or Codex task
check whether an AI Agent identity is explicitly declared
```

AI must not:

```text
create Identity Principal without authorized service
assign permission
approve identity verification
bypass human review for high-risk identity changes
infer real-world identity beyond approved data
treat a prompt as an identity
treat a model provider as an identity principal
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Object Access Rule
Service Access Rule
Event Access Rule
Audit Rule
```

---

# 14. Workflow Usage

Identity participates in workflows but does not own most workflows.

Identity-sensitive workflows may include:

```text
identity-registration-workflow.md
identity-provider-link-review-workflow.md
identity-disablement-review-workflow.md
authentication-session-review-workflow.md
agent-identity-registration-workflow.md
```

Workflow rules:

```text
- Identity workflows must reference Workflow Contracts.
- Identity disablement must be auditable.
- AI Agent identity creation must require Agent Contract review.
- Identity workflows must not assign business permissions directly.
```

---

# 15. API Usage

Identity APIs expose identity resolution and registration through governed services.

Potential MVP APIs:

```text
POST /identity/principals
GET /identity/principals/{id}
POST /identity/resolve
POST /identity/{id}/disable
POST /identity/{id}/reenable
```

Potential partial APIs:

```text
POST /identity/provider-links
DELETE /identity/provider-links/{id}
POST /auth/sessions
DELETE /auth/sessions/{id}
POST /auth/sessions/validate
```

API rules:

```text
- APIs must invoke Identity Services.
- APIs must not bypass Permission or Policy checks where required.
- APIs must not expose credential secrets.
- APIs must emit or cause service-level events for mutating actions.
- APIs must preserve actor audit context.
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
```

## 16.2 Partial Consumers

```text
Partner Center
Client Portal
Service Platform
Validation tools
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Third-party provider portals
Reporting consumers
```

Product rule:

```text
Products consume Identity.
Products do not redefine Identity.
```

---

# 17. MVP Scope

Identity is a Phase 1 / Wave 1 Must Implement domain.

MVP includes:

```text
Identity Principal
Actor Reference
Identity Status
Identity Principal Resolution Service
Identity Registration Service
Identity Status Service
Actor Reference Validation Service
IdentityCreated event
IdentityDisabled event
basic identity metadata validation
source traceability to User, Permission, Audit and Agent systems
```

MVP should support:

```text
human user identity reference
system actor identity reference
AI Agent identity reference
Codex actor reference
audit actor reference
```

MVP does not require full external provider integration.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full OAuth provider implementation
multi-factor authentication infrastructure
biometric authentication
single sign-on federation
external directory synchronization
customer-facing account recovery flow
advanced identity risk scoring
identity fraud detection
cross-tenant identity federation
public marketplace identity verification
official legal identity verification
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Identity Principal should use stable immutable ID.
Actor Reference should be reusable across Services, Events, Workflows and Audit Records.
Identity Status should use controlled values.
Disabled identities should not be used for new governed actions unless an explicit exception is approved.
Identity events should avoid sensitive credential details.
Authentication implementation may be delegated to infrastructure, but Core must preserve actor identity reference and audit trace.
```

Suggested controlled Identity Status values:

```text
Draft
Active
VerificationRequired
Suspended
Disabled
Merged
Superseded
DeletedReferenceOnly
```

MVP controlled status values:

```text
Active
Disabled
Suspended
```

Do not treat physical authentication infrastructure as Core meaning.

---

# 20. Codex Implementation Notes

Codex may implement Identity only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Identity / User / Permission / Policy boundaries
implement only MVP scope unless task says otherwise
write tests for actor resolution
write tests for identity creation
write tests for identity disablement
write tests preventing permission assignment inside Identity
write tests preventing unowned actor references
```

Codex must not:

```text
invent permission logic inside Identity
invent organization membership logic inside Identity
implement full OAuth infrastructure as Core MVP
store credential secrets as Core domain meaning
treat email address as the only identity
treat product account ID as Core identity
create AI Agent behavior without Agent Contract
```

---

# 21. Validation Rules

Identity Domain must pass the following checks.

```text
[ ] Identity is classified as Foundation Domain.
[ ] Identity is counted within the 26 baseline Core Domains.
[ ] Identity does not change the baseline Core Domain Map.
[ ] Identity has MVP Phase 1 / Wave 1 classification.
[ ] Identity has MVP Depth = Must Implement.
[ ] Identity defines Core meaning.
[ ] Identity boundary excludes Permission, Policy and Organization membership.
[ ] Identity owns Identity Principal.
[ ] Identity defines Actor Reference.
[ ] Identity lists primary services.
[ ] Mutating Identity services emit events.
[ ] Identity lists primary events.
[ ] Identity defines contract requirements.
[ ] Identity defines AI Agent usage constraints.
[ ] Identity defines workflow usage constraints.
[ ] Identity defines API usage constraints.
[ ] Identity defines product consumers.
[ ] Identity defines MVP and deferred scope.
[ ] Identity defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Identity into Permission
turn Identity into User profile
turn Identity into Organization membership
turn Identity into Customer contact management
turn Identity into Partner/Agent profile
turn product login UI into Core architecture
treat email or phone as the only identity
implement full SSO federation in MVP
store credential secrets as Core meaning
allow AI to create or verify identity without contract and review
allow Codex to define new identity architecture
allow product-specific account IDs to replace Core Identity Principal
```

---

# 23. Acceptance Criteria

This Identity Domain Specification is accepted only if:

```text
[ ] It defines Identity purpose.
[ ] It defines Identity Core meaning.
[ ] It identifies Identity as Foundation Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to User, Organization, Permission, Policy, AI Governance, Workflow and Audit.
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
| 0.1.0 | Draft | Initial Identity Domain specification. Establishes Identity as Phase 1 Foundation Domain, defines Identity Principal, Actor Reference, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
