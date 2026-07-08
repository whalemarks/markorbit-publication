# Domain Specification — Organization

**Spec ID:** B02-DOM-ORGANIZATION  
**Spec Type:** Domain  
**Domain Name:** Organization  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/organization.md; core-specs/objects/organization-unit.md; core-specs/objects/organization-membership.md; core-specs/objects/organization-role-binding.md; core-specs/objects/tenant-boundary.md  
**Related Service Specs:** core-specs/services/organization-registration-service.md; core-specs/services/organization-membership-service.md; core-specs/services/organization-context-resolution-service.md; core-specs/services/organization-status-service.md  
**Related Event Specs:** core-specs/events/organization-created.md; core-specs/events/organization-updated.md; core-specs/events/organization-disabled.md; core-specs/events/organization-member-added.md; core-specs/events/organization-member-removed.md; core-specs/events/organization-context-resolved.md  
**Related Contract Specs:** core-specs/contracts/organization/organization-contract.md; core-specs/contracts/organization/organization-membership-contract.md; core-specs/contracts/organization/tenant-boundary-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Organization Domain defines the Core meaning of an operating entity, team, business unit or tenant boundary within MarkOrbit.

It exists so that identities, users, permissions, policies, matters, orders, workflows, AI Agents, product consumers and audit records can operate within a stable organizational context.

Organization is required before:

```text
User membership
Permission assignment
Policy evaluation
Matter ownership
Order ownership
Task assignment
Review ownership
Approval ownership
AI Agent authorization
Product tenancy
Audit trace
Codex task ownership
```

The Organization Domain is a Foundation Domain because accountable execution requires not only a known actor, but also a known organizational context.

---

# 2. Core Meaning

Organization means:

```text
a stable Core-recognized operational or legal container that can own, group, authorize, isolate or contextualize actors, data, responsibilities and execution.
```

Organization is not merely:

```text
a company profile page
a customer record
a partner record
a law firm profile
a service provider profile
a department label
a sales account
a billing account
a tenant database
a workspace UI
```

Organization answers:

```text
Within which Core-recognized entity does this actor operate?
Which organization owns or contextualizes this action?
Which organizational boundary applies to data, permission, policy, workflow and audit?
Can this organization be used consistently by products and services?
```

---

# 3. Domain Category

Organization is a Foundation Domain.

Foundation Domains provide the minimum Core basis for:

```text
actor context
ownership
membership
tenant boundary
permission scope
policy scope
data isolation
workflow responsibility
audit responsibility
product consumption boundary
```

Organization must be implemented before higher-level business execution and collaboration domains can operate safely.

---

# 4. Architectural Position

Organization sits immediately after Identity and before Permission and Policy in the Core execution chain.

```text
Identity recognizes the actor
        ↓
Organization provides operating context
        ↓
User links human account to organization
        ↓
Permission assigns allowed action in context
        ↓
Policy evaluates constraints in context
        ↓
Services execute accountable actions
        ↓
Events and audit preserve organizational trace
```

Organization provides the context in which Core actions are performed.

It does not define the actor.

That belongs to Identity.

It does not define allowed actions.

That belongs to Permission and Policy.

---

# 5. Scope

The Organization Domain includes:

```text
organization definition
organization lifecycle
organization status
organization type
organization hierarchy boundary
organization unit boundary
organization membership boundary
tenant boundary
organization context resolution
organization ownership reference
organization audit reference
organization-to-user association boundary
organization-to-product consumption boundary
```

The Organization Domain supports multiple organization forms.

Organization types may include:

```text
Internal Operating Company
Client Organization
Partner Organization
Service Provider Organization
Agent Organization
System Organization
Sandbox Organization
```

MVP implementation should focus on:

```text
internal operating organization
client organization reference
system organization reference
organization membership
organization context resolution
tenant boundary
```

---

# 6. Boundary

## 6.1 In Boundary

The Organization Domain owns:

```text
Core organization definition
organization creation
organization status
organization type
organization context reference
organization membership boundary
organization unit boundary
tenant boundary reference
organization audit reference
organization event emission
organization reference used by other domains
```

## 6.2 Out of Boundary

The Organization Domain does not own:

```text
identity recognition
user profile details
permission rules
policy rules
customer lifecycle
partner commercial relationship
service provider qualification
agent professional capability
billing account
invoice account
product workspace UI
sales pipeline ownership
Matter lifecycle
Order lifecycle
AI Agent capability authorization
physical multi-tenant database design
company registry verification
```

Those responsibilities belong to:

```text
Identity Domain
User Domain
Permission Domain
Policy system
Customer Domain
Partner Domain
Service Provider Domain
Agent Domain
Order Domain
Matter Domain
AI Governance
Finance implementation
Product implementation
Infrastructure implementation
```

## 6.3 Boundary Notes

Organization defines the Core container.

Customer defines a commercial relationship.

Partner defines a collaboration relationship.

Service Provider defines a supply-side professional service relationship.

Agent defines professional representation or associate identity.

An organization may later participate in those roles, but Organization itself does not own those business meanings.

---

# 7. Domain Rules

## 7.1 Organization Must Be Stable

An Organization must have a stable Core ID.

Product workspace IDs, billing account IDs or external CRM IDs must not replace Core Organization IDs.

## 7.2 Organization Must Provide Execution Context

Governed Core actions must be performed within an organization context unless explicitly defined as system-level actions.

## 7.3 Organization Does Not Grant Permission

Membership in an organization does not automatically authorize all actions.

Permission and Policy must decide what an actor may do inside the organization context.

## 7.4 Organization Must Support Tenant Boundary

Organization must support a Core-level tenant or operating boundary.

The tenant boundary defines where data, permissions, policies, workflows and audit context are scoped.

Physical database tenancy is implementation-specific and does not define Core meaning.

## 7.5 Organization Must Be Auditable

Organization-sensitive actions must preserve organization reference.

Audit-sensitive organization actions include:

```text
organization creation
organization status change
membership creation
membership removal
organization context switch
permission assignment inside organization
policy override inside organization
matter ownership assignment
AI Agent authorization inside organization
Codex task acceptance inside organization
```

---

# 8. Primary Objects

The Organization Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Organization | Organization | Must Implement | Stable Core-recognized operational or legal container. |
| Organization Unit | Organization | Partial Implement | Sub-structure inside an Organization for operational grouping. |
| Organization Membership | Organization | Must Implement | Association between Identity/User and Organization context. |
| Organization Role Binding | Organization / Permission | Partial Implement | Link between organization membership and role or permission assignment. |
| Organization Status | Organization | Must Implement | Controlled status indicating whether organization may be used in Core execution. |
| Tenant Boundary | Organization | Must Implement | Core boundary used for data, permission, policy and execution isolation. |
| Organization Context | Organization | Must Implement | Resolved context used by Services, Events, Workflows and APIs. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Identity Principal | Identity | Membership references a recognized actor. |
| User | User | User may participate in Organization through membership. |
| Permission Assignment | Permission | Permission may be scoped to Organization. |
| Policy Evaluation Context | Policy | Policy uses Organization as context. |
| Customer | Customer | Customer may reference an Organization. |
| Partner | Partner | Partner may reference an Organization. |
| Service Provider | Service Provider | Service Provider may reference an Organization. |
| Matter | Matter | Matter may be owned or contextualized by Organization. |
| Order | Order | Order may be owned or contextualized by Organization. |
| AI Agent | AI Governance / Agent specs | Agent authorization may be scoped to Organization. |
| Audit Record | Audit | Audit records organization context. |

---

# 9. Primary Services

The Organization Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Organization Registration Service | Organization | Must Implement | Register a new Core Organization. |
| Organization Context Resolution Service | Organization | Must Implement | Resolve active organization context for an actor or action. |
| Organization Membership Service | Organization | Must Implement | Add, remove or update organization membership through governed rules. |
| Organization Status Service | Organization | Must Implement | Enable, suspend or disable organization usage. |
| Tenant Boundary Validation Service | Organization | Must Implement | Validate that an action occurs within an allowed organization or tenant boundary. |
| Organization Unit Service | Organization | Partial Implement | Create or manage organization units. |
| Organization Reference Validation Service | Organization | Must Implement | Validate organization references used by other domains. |

Service rules:

```text
- Mutating Organization services must emit events.
- Organization services must not assign permissions directly.
- Organization services must not define Customer, Partner or Service Provider lifecycle.
- Organization context resolution must support audit trace.
- Organization membership changes must be governed and auditable.
```

---

# 10. Primary Events

The Organization Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| OrganizationCreated | Organization Registration Service | Must Implement | A Core Organization has been created. |
| OrganizationUpdated | Organization Registration Service / Organization Status Service | Partial Implement | Organization metadata or controlled fields have changed. |
| OrganizationDisabled | Organization Status Service | Must Implement | Organization has been disabled for governed execution. |
| OrganizationSuspended | Organization Status Service | Partial Implement | Organization has been suspended from some or all actions. |
| OrganizationReenabled | Organization Status Service | Partial Implement | Organization has been reenabled through governed review. |
| OrganizationMemberAdded | Organization Membership Service | Must Implement | Actor/User has been added to Organization membership. |
| OrganizationMemberRemoved | Organization Membership Service | Must Implement | Actor/User has been removed from Organization membership. |
| OrganizationMembershipUpdated | Organization Membership Service | Partial Implement | Organization membership status or metadata changed. |
| OrganizationContextResolved | Organization Context Resolution Service | Partial Implement | Organization context was resolved for an action. |
| TenantBoundaryViolationDetected | Tenant Boundary Validation Service | Must Implement | An attempted action violated organization or tenant boundary. |

Event rules:

```text
- Organization events must reference Organization.
- Membership events must reference actor identity or user where applicable.
- Tenant boundary violations must be auditable.
- Organization events must not expose unrelated customer, partner or financial details.
```

---

# 11. Primary Contracts

Organization requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Organization Contract | Organization Contract | Must Implement | Defines Organization fields, status, type and reference behavior. |
| Organization Membership Contract | Organization Contract | Must Implement | Defines membership fields, actor references and status. |
| Organization Context Contract | Organization Contract | Must Implement | Defines resolved organization context used by services and events. |
| Tenant Boundary Contract | Organization / Policy Contract | Must Implement | Defines organization-level boundary checks for data and execution. |
| Organization Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for organization-sensitive actions. |

Contract rules:

```text
- Organization Contract must not define Customer, Partner or Service Provider business lifecycle.
- Organization Membership Contract must not assign permissions by itself.
- Tenant Boundary Contract must be reusable by Services, APIs, Workflows and Agents.
```

---

# 12. Relationships to Other Domains

## 12.1 Identity

Identity recognizes actors.

Organization provides the context in which actors operate.

Organization Membership links Identity/User to Organization.

## 12.2 User

User represents the human or operational account.

Organization Membership determines which Organization contexts the user may operate within.

## 12.3 Permission

Permission uses Organization context to scope allowed actions.

Organization does not grant permission.

## 12.4 Policy

Policy uses Organization context for evaluation.

Organization does not define policy logic.

## 12.5 Customer

Customer may reference an Organization, but Customer owns commercial/customer lifecycle.

Organization does not mean Customer.

## 12.6 Partner

Partner may reference an Organization, but Partner owns collaboration relationship.

Organization does not mean Partner.

## 12.7 Service Provider

Service Provider may reference an Organization, but Service Provider owns supply-side service capability.

Organization does not mean Service Provider.

## 12.8 Matter and Order

Matter and Order may be owned or contextualized by Organization.

Organization does not define Matter or Order lifecycle.

## 12.9 AI Governance

AI Agent authorization may be scoped to Organization.

Organization does not define Agent capabilities or AI output review rules.

## 12.10 Audit

Audit records should include organization context for governed actions.

Audit storage and report rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Organization only under governed Agent Contracts.

Allowed AI use:

```text
resolve organization context for a permitted action
identify missing organization context in a task or workflow
summarize organization-scoped execution trace if authorized
flag potential tenant boundary mismatch
explain organization membership status if authorized
```

AI must not:

```text
create Organization without authorized service
add or remove organization members without governed service
assign permissions
override tenant boundary
infer customer/partner/service-provider relationship from Organization alone
bypass organization-scoped policy checks
approve organization status changes
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Organization Object Access Rule
Organization Service Access Rule
Organization Event Access Rule
Tenant Boundary Rule
Audit Rule
Human Review Rule where high-risk
```

---

# 14. Workflow Usage

Organization participates in workflows but does not own most business workflows.

Organization-sensitive workflows may include:

```text
organization-registration-workflow.md
organization-membership-review-workflow.md
organization-disablement-review-workflow.md
organization-context-resolution-workflow.md
tenant-boundary-violation-review-workflow.md
agent-organization-authorization-workflow.md
```

Workflow rules:

```text
- Organization workflows must reference Workflow Contracts.
- Membership changes must be auditable.
- Tenant boundary violations must block unsafe transitions.
- Organization status changes should require review when high-risk.
- Organization workflows must not assign permissions directly.
```

---

# 15. API Usage

Organization APIs expose organization registration, membership and context resolution through governed services.

Potential MVP APIs:

```text
POST /organizations
GET /organizations/{id}
POST /organizations/{id}/disable
POST /organizations/{id}/reenable
POST /organizations/{id}/memberships
DELETE /organizations/{id}/memberships/{membership_id}
POST /organizations/context/resolve
POST /organizations/tenant-boundary/validate
```

API rules:

```text
- APIs must invoke Organization Services.
- APIs must preserve actor identity and organization audit context.
- APIs must not bypass Permission or Policy checks.
- APIs must not expose cross-organization data.
- Mutating APIs must emit or cause service-level events.
- Membership APIs must not grant permissions unless governed by Permission services.
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
Third-party provider portals
Advanced analytics
```

Product rule:

```text
Products consume Organization.
Products do not redefine Organization.
```

---

# 17. MVP Scope

Organization is a Phase 1 / Wave 1 Must Implement domain.

MVP includes:

```text
Organization
Organization Membership
Organization Status
Organization Context
Tenant Boundary
Organization Registration Service
Organization Context Resolution Service
Organization Membership Service
Organization Status Service
Tenant Boundary Validation Service
OrganizationCreated event
OrganizationDisabled event
OrganizationMemberAdded event
OrganizationMemberRemoved event
TenantBoundaryViolationDetected event
basic organization metadata validation
source traceability to Identity, User, Permission, Policy and Audit systems
```

MVP should support:

```text
internal organization context
client organization reference
system organization reference
basic membership
basic organization status
tenant boundary validation
audit organization reference
```

MVP does not require full external company verification or multi-level enterprise hierarchy.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full enterprise hierarchy
complex department tree
cross-tenant federation
external company registry verification
advanced organization risk scoring
billing account management
invoice account management
organization-level subscription plans
self-service public workspace creation
marketplace organization onboarding
partner/service-provider accreditation workflow
multi-brand holding company modeling
automated organization deduplication
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Organization should use stable immutable ID.
Organization Status should use controlled values.
Organization Context should be reusable by Services, Events, Workflows, APIs and Audit Records.
Tenant Boundary should be enforced before data mutation and external exposure.
Organization Membership should reference Identity or User through approved contracts.
Disabled organizations should not be used for new governed actions unless an explicit exception is approved.
Organization events should avoid exposing unrelated commercial or financial details.
```

Suggested controlled Organization Status values:

```text
Draft
Active
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

Suggested Organization Type values:

```text
Internal
Client
Partner
ServiceProvider
Agent
System
Sandbox
```

MVP controlled Organization Type values:

```text
Internal
Client
System
```

Do not treat physical tenancy design as Core meaning.

---

# 20. Codex Implementation Notes

Codex may implement Organization only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Organization / Customer / Partner / Service Provider boundaries
preserve Organization / Permission / Policy boundaries
implement only MVP scope unless task says otherwise
write tests for organization creation
write tests for organization context resolution
write tests for organization membership
write tests for tenant boundary validation
write tests preventing permission assignment inside Organization
write tests preventing product workspace ID from replacing Core Organization ID
```

Codex must not:

```text
invent Customer lifecycle inside Organization
invent Partner lifecycle inside Organization
invent Service Provider qualification inside Organization
assign permissions inside Organization services
implement billing/subscription logic as Organization MVP
implement full enterprise hierarchy in MVP
treat database tenant ID as the only organization concept
create cross-tenant access without Permission and Policy
```

---

# 21. Validation Rules

Organization Domain must pass the following checks.

```text
[ ] Organization is classified as Foundation Domain.
[ ] Organization is counted within the 26 baseline Core Domains.
[ ] Organization does not change the baseline Core Domain Map.
[ ] Organization has MVP Phase 1 / Wave 1 classification.
[ ] Organization has MVP Depth = Must Implement.
[ ] Organization defines Core meaning.
[ ] Organization boundary excludes Customer, Partner, Service Provider and billing lifecycle.
[ ] Organization boundary excludes Permission and Policy rules.
[ ] Organization owns Organization object.
[ ] Organization defines Organization Membership.
[ ] Organization defines Tenant Boundary.
[ ] Organization lists primary services.
[ ] Mutating Organization services emit events.
[ ] Organization lists primary events.
[ ] Organization defines contract requirements.
[ ] Organization defines AI Agent usage constraints.
[ ] Organization defines workflow usage constraints.
[ ] Organization defines API usage constraints.
[ ] Organization defines product consumers.
[ ] Organization defines MVP and deferred scope.
[ ] Organization defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Organization into Customer
turn Organization into Partner
turn Organization into Service Provider
turn Organization into Agent professional profile
turn Organization into billing account
turn Organization into subscription management
turn Organization into product workspace UI
turn Organization into physical database tenancy
assign permissions directly through Organization
bypass Policy by organization membership
allow cross-organization data exposure
implement full enterprise hierarchy in MVP
implement marketplace onboarding in MVP
allow AI to change organization status without contract and review
allow Codex to define new organization architecture
```

---

# 23. Acceptance Criteria

This Organization Domain Specification is accepted only if:

```text
[ ] It defines Organization purpose.
[ ] It defines Organization Core meaning.
[ ] It identifies Organization as Foundation Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Identity, User, Permission, Policy, Customer, Partner, Service Provider, Matter, Order, AI Governance and Audit.
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
| 0.1.0 | Draft | Initial Organization Domain specification. Establishes Organization as Phase 1 Foundation Domain, defines Organization, Membership, Tenant Boundary, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
