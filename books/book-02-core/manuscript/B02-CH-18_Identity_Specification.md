# Book 02

# 18 — Identity Specification

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-18

**Chapter Title:** Identity Specification

**Part:** Part III — Core Specification System

**Chapter Type:** Specification

**Status:** Draft

**Version:** 0.1.0

**Owner:** MarkOrbit Publications Editorial Board

**Related Planning Documents:**

- B02-PLN-0001 — Core Positioning
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- B02-EDT-0001 — Editorial Protocol and Chapter Writing Template

---

# 1. Chapter Purpose

This chapter defines the Identity Specification of the MarkOrbit Core.

Part II defined the Core Kernel Architecture.

Part III begins the Core Specification System.

The first specification is Identity because every other Core capability depends on knowing who or what is acting, represented, responsible, authorized, contacted, assigned, reviewed or connected.

Identity is not only login.

Identity is not only user account.

Identity is not only contact record.

Identity is the shared representation of actors and actor-linked entities across the MarkOrbit ecosystem.

MarkOrbit needs identity for:

- users;
- organizations;
- customers;
- partners;
- agents;
- service providers;
- contact persons;
- attorney representatives;
- AI agents;
- external systems;
- business responsibility;
- permissions;
- communication;
- audit;
- routing;
- network collaboration.

If identity is fragmented, every product will create its own understanding of customer, agent, user and provider.

Then permissions, responsibility, communication and AI governance will also fragment.

This chapter defines the Core Identity Specification so that all downstream domains and products can share one identity foundation.

---

# 2. Core Question

This chapter answers one question:

> How shall MarkOrbit represent, link, verify, govern and consume identity across people, organizations, users, customers, partners, agents, service providers, AI agents and external systems?

The answer is:

> MarkOrbit shall define identity as a Core foundation that represents actors and actor-linked entities through stable Identity Objects, Identity Relationships, Contact Points, Roles, Verification Status, Permission Context and Audit Context.

Identity enables responsibility.

Identity enables permission.

Identity enables communication.

Identity enables collaboration.

Identity enables audit.

Identity enables AI governance.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- Identity Specification purpose;
- Identity Model application;
- identity ontology;
- identity domain relationship;
- identity object types;
- person identity;
- organization identity;
- user identity;
- customer identity;
- partner identity;
- agent identity;
- service provider identity;
- AI agent identity;
- external system identity;
- contact point;
- identity relationship;
- role;
- identity verification;
- identity lifecycle;
- identity quality;
- identity merge and duplicate handling;
- identity permissions;
- identity events;
- identity services;
- identity contracts;
- AI usage;
- product consumption;
- MVP boundary;
- `core-specs/` requirements;
- Codex implementation rules.

## 3.2 Out of Scope

This chapter does not define:

- product login page;
- complete authentication infrastructure;
- third-party KYC vendor integration;
- CRM page design;
- contact management UI;
- agent marketplace UI;
- MGSN membership pricing;
- product onboarding flow;
- full permission engine details;
- complete database schema;
- production API endpoints;
- implementation code.

Those belong to product documents, `core-specs/`, Book 06 or implementation documents.

---

# 4. Identity Definition

In the MarkOrbit Core, Identity means:

> a stable representation of an actor or actor-linked entity that may participate in professional work, hold responsibility, own relationships, access Core assets, communicate, be assigned work, provide capability, receive value, or appear in audit history.

This definition includes:

- human persons;
- organizations;
- system users;
- customers;
- partners;
- agents;
- service providers;
- AI agents;
- external systems;
- contact points;
- roles and relationships.

Identity is broader than user account.

A user account is one expression of identity.

A customer is one business role of identity.

An agent is one professional collaboration role of identity.

A service provider is one network role of identity.

An AI agent is one governed automated actor identity.

---

# 5. Identity Specification Position

Identity Specification belongs to Part III because it translates Core architecture into specification rules.

It is connected to Part II as follows:

```text
Canonical Models
    Identity Model

Core Domains
    Identity
    Organization
    User
    Permission
    Customer
    Partner
    Agent
    Service Provider
    Communication

Core Objects
    Identity
    Person
    Organization
    User
    Contact Point
    Role
    Identity Link

Core Services
    Identity Resolution
    Identity Linking
    Identity Verification
    User Context
    Organization Lookup

Execution Primitives
    IdentityLinked Event
    IdentityMerged Event
    IdentityVerified Event

Core Contracts
    Identity Data Contract
    Identity Resolution API Contract
    Identity Event Contract
    Identity Consumption Contract
```

Identity is a foundation.

It must be available before higher-level responsibility, permission, routing, communication and AI governance can operate reliably.

---

# 6. Identity Principles

The Identity Specification is governed by the following principles.

## Principle 1 — Identity Before Permission

Permission requires identity.

No permission rule can be reliable if the actor is not identified.

## Principle 2 — Identity Before Responsibility

Business responsibility requires identity.

Matter owner, customer owner, review authority and agent assignee must refer to identity.

## Principle 3 — Identity Before Communication

Communication records require identity or at least contact points that may later resolve to identity.

## Principle 4 — Identity Before Audit

Audit records require actor identity, system identity or at minimum source identity.

## Principle 5 — Identity Is Not Only User

A user is not the only identity type.

Customers, agents, service providers and AI agents also require identity representation.

## Principle 6 — Identity May Be Incomplete

Some identities start as incomplete, imported, inferred or unverified.

The Core must represent identity quality.

## Principle 7 — Identity May Have Multiple Roles

One entity may be a customer, partner, agent and service provider in different contexts.

The Core should model roles and relationships rather than duplicate entities blindly.

## Principle 8 — Identity Must Be Governed

Identity creation, linking, merging, verification and exposure require permission and audit.

---

# 7. Identity Ontology

Identity belongs primarily to System Ontology.

It also touches Reality Ontology and Collaboration Ontology.

## 7.1 System Ontology

Identity is a system foundation because it enables access, permission, audit and responsibility.

## 7.2 Reality Ontology

People, organizations, customers, agents and service providers exist outside MarkOrbit.

The Core represents them.

## 7.3 Collaboration Ontology

Identity supports professional collaboration among customers, partners, agents, service providers and AI agents.

The Identity Specification therefore supports multiple ontology layers.

Its primary architectural position is Foundation Domain.

---

# 8. Identity Domain Relationships

Identity is related to several Core Domains.

| Domain | Identity Relationship |
|--------|----------------------|
| Identity | owns identity representation and resolution |
| Organization | owns organization structure and organization identity |
| User | owns system user participation |
| Permission | depends on identity and role |
| Policy | may apply identity-based rules |
| Customer | uses identity for customer entity and contacts |
| Partner | uses identity for partner agency |
| Agent | uses identity for foreign agent or attorney |
| Service Provider | uses identity for provider representation |
| Communication | links messages to identity and contact points |
| Matter | assigns responsibility to identities |
| Order | links order ownership to identities |
| Task | assigns work to identities |
| Event | records actor identity |
| AI Capability | requires AI agent identity and actor context |

Identity must not be redefined independently by these domains.

They consume the Identity Specification.

---

# 9. Identity Object Types

The Identity Specification recognizes the following primary identity object types.

```text
Identity
Person
Organization
User
Customer Identity
Partner Identity
Agent Identity
Service Provider Identity
AI Agent Identity
External System Identity
Contact Point
Role
Identity Relationship
Identity Verification
Identity Link
```

Not every object must be implemented immediately.

But the model must allow these object types to exist without conflict.

---

# 10. Identity Object

## 10.1 Definition

Identity Object is:

> the stable Core representation of an actor or actor-linked entity that may be referenced by permissions, responsibilities, communications, events, tasks, services, products or AI agents.

## 10.2 Purpose

Identity Object provides:

- stable reference;
- actor recognition;
- relationship anchoring;
- permission context;
- audit subject;
- communication participant;
- routing participant;
- responsibility holder.

## 10.3 Minimum Attributes

A minimal Identity Object should include:

```text
identity_id
identity_type
display_name
status
verification_status
source
created_at
updated_at
```

Additional attributes belong to detailed object specs.

## 10.4 Identity Types

Baseline identity types include:

```text
person
organization
user
customer
partner
agent
service_provider
ai_agent
external_system
unknown_contact
```

The identity type should not replace domain-specific objects.

It provides shared identity anchoring.

---

# 11. Person Identity

A Person Identity represents a human individual.

Examples:

- customer contact;
- agency staff;
- attorney contact;
- foreign agent representative;
- internal operator;
- reviewer;
- signatory;
- sales contact.

A Person Identity may be linked to:

- User;
- Organization;
- Customer;
- Partner;
- Agent;
- Service Provider;
- Contact Point;
- Role;
- Matter;
- Task;
- Communication.

Person Identity must support incomplete data.

For example, an email sender may be known only by name and email.

Later, the system may link that sender to an Agent organization.

---

# 12. Organization Identity

An Organization Identity represents a legal, business or professional organization.

Examples:

- client company;
- Chinese agency partner;
- foreign law firm;
- service provider company;
- trademark office;
- user’s own organization;
- external platform or institution.

An Organization Identity may be linked to:

- Customer;
- Partner;
- Agent;
- Service Provider;
- User;
- Person;
- Contact Point;
- Matter;
- Order;
- Communication;
- Service Network.

Organization Identity should support:

- legal name;
- trade name;
- country or region;
- organization type;
- contact points;
- relationships;
- verification status.

---

# 13. User Identity

A User Identity represents a person or account that can access MarkOrbit system functions.

User Identity is related to, but not identical to, Person Identity.

A User should link to:

- Identity;
- Person where available;
- Organization;
- Role;
- Permission;
- Product access;
- audit records;
- task assignments.

User Identity supports:

- login context;
- product access;
- action authorization;
- task assignment;
- review responsibility;
- audit actor;
- AI interaction attribution.

User Identity does not define product UI or authentication infrastructure.

It defines Core user participation meaning.

---

# 14. Customer Identity

Customer Identity represents a person or organization that receives or may receive professional services.

Customer Identity may be:

- direct end client;
- Chinese agency client;
- brand owner;
- applicant;
- trademark owner;
- prospect;
- opportunity source.

Customer Identity should link to:

- Identity;
- Organization or Person;
- Brand;
- Trademark;
- Order;
- Matter;
- Opportunity;
- Communication;
- Customer Owner.

Customer Identity is not only a CRM record.

It is part of business responsibility and professional service context.

---

# 15. Partner Identity

Partner Identity represents an agency, channel or business partner that collaborates with MarkOrbit.

Examples:

- Chinese trademark agency partner;
- referral partner;
- platform partner;
- regional business partner.

Partner Identity may link to:

- Organization Identity;
- User;
- Customer records;
- Orders;
- Matters;
- Opportunities;
- Communication;
- Business Responsibility.

Partner Identity is different from Customer Identity, although the same organization may play both roles.

The relationship should be modeled through identity roles, not duplication.

---

# 16. Agent Identity

Agent Identity represents a professional foreign agent, attorney, law firm or associate involved in trademark service execution.

Agent Identity may be:

- individual attorney;
- law firm;
- IP agency;
- country associate;
- regional representative.

Agent Identity should link to:

- Organization Identity;
- Person contacts;
- Jurisdiction coverage;
- Service capability;
- Matter assignment;
- Communication;
- Reliability record;
- Routing decision;
- Service Network.

Agent Identity is not merely contact information.

It supports routing, capability matching, service responsibility and network collaboration.

---

# 17. Service Provider Identity

Service Provider Identity represents an external provider that offers professional or operational service capability.

Examples:

- trademark filing provider;
- translation provider;
- notarization provider;
- evidence collection provider;
- document processing provider;
- local counsel;
- platform-based service vendor.

Service Provider Identity may overlap with Agent Identity.

The same organization may be both Agent and Service Provider.

The Core should allow multiple roles linked to one identity.

Service Provider Identity supports Book 06 and network execution.

---

# 18. AI Agent Identity

AI Agent Identity represents an AI or automated agent acting under Core governance.

AI Agent Identity is required because AI actions must be attributable.

An AI Agent Identity should define:

- agent name;
- agent purpose;
- owning domain;
- allowed capabilities;
- Agent Contract;
- knowledge sources;
- allowed tools or services;
- risk level;
- human review requirement;
- audit requirement;
- product consumers.

AI Agent Identity does not mean AI has independent professional responsibility.

AI acts under governance.

Human or business responsibility remains assigned separately.

---

# 19. External System Identity

External System Identity represents a non-human system or integration that interacts with MarkOrbit.

Examples:

- trademark office data source;
- email system;
- payment system;
- file storage system;
- partner platform;
- data import tool;
- Codex implementation process;
- automation runner.

External System Identity supports:

- source attribution;
- audit;
- import provenance;
- integration permission;
- event source tracking;
- failure tracking.

External systems should not be anonymous when they create or modify Core data.

---

# 20. Contact Point

A Contact Point represents a communication endpoint.

Examples:

```text
email address
phone number
WhatsApp account
WeChat account
Skype account
website
postal address
office address
```

A Contact Point may belong to:

- Person;
- Organization;
- Customer;
- Partner;
- Agent;
- Service Provider;
- unknown contact.

Contact Points may exist before full identity is resolved.

For example, an email sender can be stored as an unknown contact point first.

Later, it may be linked to an Agent or Customer.

Contact Point is not equivalent to Identity.

It is evidence or channel of identity.

---

# 21. Role

A Role defines how an identity participates in a context.

Examples:

```text
customer_owner
matter_owner
matter_operator
review_authority
agent_contact
service_provider_contact
partner_admin
internal_admin
sales_user
process_user
finance_user
ai_assistant
external_system
```

Roles may be:

- global;
- organization-level;
- product-level;
- matter-level;
- workflow-level;
- network-level.

Role does not equal permission by itself.

Permission may be derived from role, policy, context and object relationship.

---

# 22. Identity Relationship

Identity Relationship represents a structured relationship between identities.

Examples:

```text
Person belongs to Organization
User belongs to Organization
Customer represented by Contact Person
Agent belongs to Law Firm
Service Provider participates in Service Network
Partner owns Customer relationship
Matter assigned to Agent
User acts for Organization
AI Agent acts under Product Context
```

Relationship types may include:

- employment;
- representation;
- ownership;
- contact;
- assignment;
- delegation;
- service participation;
- network membership;
- responsibility;
- communication;
- authorization.

Identity relationships should be explicit when they affect permission, responsibility, communication or audit.

---

# 23. Identity Verification

Identity Verification represents the level of trust in an identity.

Baseline verification statuses may include:

```text
unverified
imported
inferred
self_declared
email_verified
human_verified
officially_verified
trusted_partner_verified
deprecated
merged
blocked
```

Verification affects:

- permission;
- routing;
- communication trust;
- AI context quality;
- service provider selection;
- audit confidence;
- data quality.

For example, a routing decision should treat a human-verified Agent differently from an imported unverified contact.

Verification status should be visible to services and AI agents where risk matters.

---

# 24. Identity Lifecycle

Identity Objects should have lifecycle.

Baseline identity lifecycle may include:

```text
Created
Active
Pending Verification
Verified
Suspended
Merged
Deprecated
Archived
Blocked
```

Lifecycle transitions should be governed.

Examples:

- unverified identity becomes verified;
- duplicate identities are merged;
- outdated contact is deprecated;
- risky identity is blocked;
- inactive identity is archived.

Lifecycle changes may publish Events.

---

# 25. Identity Quality

Identity quality describes how reliable an identity is.

Quality dimensions may include:

- completeness;
- source authority;
- verification status;
- duplication risk;
- relationship confidence;
- freshness;
- contact validity;
- conflict status;
- human review status;
- AI extraction confidence.

Identity quality affects downstream execution.

Examples:

- AI should warn when using unverified identity context.
- Routing should avoid low-quality agent records where alternatives exist.
- Permission should not be granted based only on inferred identity.
- Communication should flag uncertain recipient identity where sensitive documents are involved.

---

# 26. Identity Source and Provenance

Identity should preserve source and provenance.

Sources may include:

- manual creation;
- user registration;
- imported CRM data;
- trademark record;
- email;
- document;
- agent spreadsheet;
- service provider directory;
- official registry;
- partner submission;
- AI extraction;
- external integration.

Provenance should indicate:

- source type;
- source reference;
- import time;
- extraction method;
- confidence;
- reviewer;
- verification status.

Identity source matters because not all identities have equal reliability.

---

# 27. Identity Linking

Identity Linking connects records that represent the same or related real-world actor.

Examples:

- email sender linked to Person Identity;
- Person linked to Organization;
- Organization linked to Customer;
- Organization linked to Agent;
- Agent linked to Service Provider;
- AI agent linked to Agent Contract;
- external system linked to import source.

Identity Linking may be:

- automatic;
- AI-assisted;
- rule-based;
- manual;
- verified;
- provisional.

Identity Linking should record confidence and source.

High-risk links should require human review.

---

# 28. Identity Merge and Duplicate Handling

Duplicate identities are expected.

For example:

- same agent appears in spreadsheet and email;
- same customer appears under Chinese and English names;
- same attorney uses different email addresses;
- same organization has legal name and trade name;
- same service provider appears as agent and provider.

Identity Merge should define:

- duplicate detection rule;
- merge candidate confidence;
- merge authority;
- fields to preserve;
- relationships to preserve;
- audit record;
- rollback or correction rule;
- events emitted.

Merge should not silently delete history.

A merge should preserve provenance and audit trace.

---

# 29. Identity Permission

Identity is the foundation of permission.

Permission rules may depend on:

- user identity;
- organization identity;
- role;
- customer ownership;
- matter assignment;
- agent relationship;
- service provider relationship;
- product access;
- policy;
- verification status;
- risk level.

Examples:

- a user may view matters owned by their organization;
- an internal process user may assign tasks;
- a partner user may only access their customers;
- an AI agent may access only permitted objects under Agent Contract;
- an unverified external contact may not receive sensitive document links.

Permission should not be defined only at product UI level.

It belongs to Core governance.

---

# 30. Identity and Business Responsibility

Business Responsibility depends on Identity.

Examples:

- Customer Owner is an identity or role assignment.
- Matter Owner is an identity or organization.
- Review Authority is an identity with permission.
- Agent Assignee is an Agent Identity.
- Opportunity Owner is a user or organization identity.
- Service Provider Responsibility links to provider identity.
- AI output responsibility links to human reviewer identity.

Responsibility assignment should never use free text when identity reference is available.

Free text may be used only as temporary or legacy data.

---

# 31. Identity and Communication

Communication depends on Identity and Contact Points.

A message may be linked to:

- sender identity;
- recipient identity;
- unknown contact point;
- organization;
- customer;
- partner;
- agent;
- service provider;
- matter;
- order;
- task;
- event.

Communication records should support later identity resolution.

For example, an email from a new Kenyan agent may first be stored as unknown contact.

After review, it may be linked to an Agent Identity and Matter.

This allows communication to become part of professional memory.

---

# 32. Identity and Routing

Routing depends on identity quality and capability.

Routing may use:

- Agent Identity;
- Service Provider Identity;
- Jurisdiction Coverage;
- Service Capability;
- Trust Record;
- Reliability Record;
- Communication History;
- Matter Context;
- Policy;
- Business Responsibility.

Routing should not treat unverified contact records as reliable agents.

Agent and Service Provider identities should have quality and verification status.

---

# 33. Identity and AI Capability

AI Capability requires Identity.

AI needs to know:

- acting user;
- affected customer;
- related matter;
- responsible reviewer;
- AI agent identity;
- allowed tools;
- authorized knowledge;
- permitted objects;
- audit actor;
- product context.

AI output should record:

- AI agent identity;
- requesting user identity;
- reviewed by identity where applicable;
- approved by identity where applicable;
- related objects;
- related events.

AI without identity creates audit and responsibility risk.

---

# 34. Identity Events

Identity-related Events may include:

```text
IdentityCreated
IdentityLinked
IdentityMerged
IdentityVerified
IdentityDeprecated
IdentityBlocked
ContactPointAdded
ContactPointVerified
RoleAssigned
RoleRemoved
OrganizationLinked
UserActivated
UserSuspended
AgentIdentityVerified
ServiceProviderLinked
AIIdentityRegistered
```

Event specs should identify:

- source domain;
- related identity;
- actor;
- previous state;
- new state;
- source;
- verification status;
- audit rule;
- downstream consumers.

Identity events support audit, permission, communication and network reliability.

---

# 35. Identity Services

Baseline Identity Services include:

```text
Identity Resolution Service
Identity Creation Service
Identity Linking Service
Identity Merge Service
Identity Verification Service
Contact Point Validation Service
Organization Lookup Service
User Context Service
Role Assignment Service
Identity Quality Evaluation Service
```

These services should be specified in:

```text
core-specs/services/
```

## 35.1 Identity Resolution Service

Resolves whether an input refers to an existing identity.

Inputs may include:

- name;
- email;
- organization name;
- external ID;
- jurisdiction;
- role;
- source record.

Output may include:

- matched identity;
- confidence;
- duplicate candidates;
- unresolved status;
- review requirement.

## 35.2 Identity Linking Service

Links identities or contact points.

Output should include:

- link type;
- confidence;
- source;
- reviewer where applicable;
- event.

## 35.3 Identity Verification Service

Updates verification status under permission and policy rules.

It should emit `IdentityVerified` where meaningful.

---

# 36. Identity Contracts

Identity requires multiple contracts.

## 36.1 Identity Data Contract

Defines identity object meaning, fields, source, quality and sensitivity.

## 36.2 Identity Resolution API Contract

Defines how products, services and AI agents resolve identities.

## 36.3 Identity Event Contract

Defines identity-related events such as `IdentityLinked` and `IdentityMerged`.

## 36.4 Identity Agent Contract

Defines how AI may assist identity resolution, linking or duplicate detection.

## 36.5 Identity Consumption Contract

Defines how products consume identity without redefining users, customers, agents or providers.

Detailed contracts belong to:

```text
core-specs/contracts/
core-specs/api/
core-specs/events/
core-specs/agents/
```

---

# 37. Identity Data Contract Baseline

A baseline Identity Data Contract should define:

```text
identity_id
identity_type
display_name
legal_name
alternate_names
status
verification_status
source
source_reference
quality_score
created_at
updated_at
created_by
updated_by
primary_contact_point
related_organization
roles
relationships
audit_reference
```

This list is not a final database schema.

It is a semantic baseline.

Detailed fields belong to `core-specs/objects/identity.md`.

---

# 38. Identity API Surface Baseline

A baseline Identity API surface may include:

```text
resolveIdentity
createIdentity
getIdentity
updateIdentity
linkIdentity
mergeIdentity
verifyIdentity
searchOrganizations
getUserContext
assignRole
validateContactPoint
```

These operation names are conceptual.

Implementation may choose REST, RPC or internal service patterns.

The API Contract must preserve meaning.

---

# 39. Identity AI Usage

AI may assist Identity, but under governance.

Permitted AI-assisted uses may include:

- duplicate identity detection;
- email sender identification;
- organization name normalization;
- contact extraction from documents;
- agent profile summarization;
- service provider capability extraction;
- relationship suggestion;
- identity quality warning.

Prohibited or restricted AI uses include:

- silently merging identities without review;
- granting permission based only on AI inference;
- verifying identity without authority;
- exposing sensitive identity data without permission;
- assigning legal responsibility without human approval;
- creating agent trust scores without defined policy.

AI output must indicate confidence and source.

High-risk identity changes require human review.

---

# 40. Identity Product Consumption

Products consume Identity differently.

## 40.1 MarkReg

Consumes identity for:

- users;
- customers;
- matter owners;
- agent assignment;
- communication participants;
- review authorities.

## 40.2 Lite

Consumes identity for:

- client intake;
- guided filing context;
- customer identity;
- brand owner information;
- AI interaction attribution.

## 40.3 MGSN

Consumes identity for:

- partners;
- agents;
- service providers;
- service network participants;
- trust and reliability context.

## 40.4 Workplace

Consumes identity for:

- task assignment;
- workflow responsibility;
- review authority;
- event actor display;
- human-AI collaboration context.

Products may display identity differently.

They shall not redefine identity meaning.

---

# 41. Identity MVP Boundary

The Identity MVP should implement enough to support early Core execution.

MVP should include:

```text
Identity
Organization
User
Role
Contact Point
Basic Identity Relationship
Basic Verification Status
User Context Service
Identity Resolution Service
Permission Context Integration
IdentityLinked Event
Identity Data Contract
```

MVP may defer:

- advanced identity merge;
- full external verification;
- full trust scoring;
- full MGSN network identity;
- advanced AI-assisted identity matching;
- complex identity graph visualization.

MVP must not skip identity entirely.

Without identity, permission, responsibility, audit and AI governance cannot be reliable.

---

# 42. Identity Specification Structure for core-specs/

The detailed Identity Specification should be split across `core-specs/`.

Recommended files:

```text
core-specs/domains/identity.md
core-specs/objects/identity.md
core-specs/objects/person.md
core-specs/objects/organization.md
core-specs/objects/user.md
core-specs/objects/contact-point.md
core-specs/objects/identity-relationship.md
core-specs/services/identity-resolution.md
core-specs/services/identity-linking.md
core-specs/services/user-context.md
core-specs/events/identity-linked.md
core-specs/events/identity-merged.md
core-specs/contracts/identity-data-contract.md
core-specs/api/identity-api.md
core-specs/agents/identity-resolution-assistant.md
```

These files should reference this chapter as the manuscript source.

---

# 43. Identity Specification Template

A detailed Identity Domain specification should include:

```text
# Identity Domain Specification

1. Domain Purpose
2. Domain Responsibility
3. Ontology Layer
4. Domain Category
5. Canonical Model Dependencies
6. In Scope
7. Out of Scope
8. Primary Objects
9. Referenced Objects
10. Identity Types
11. Identity Lifecycle
12. Identity Quality Rules
13. Identity Verification Rules
14. Identity Linking Rules
15. Identity Merge Rules
16. Core Services
17. Events Published
18. Contracts
19. Permission and Policy Requirements
20. AI Usage
21. Product Consumers
22. MVP Boundary
23. Acceptance Criteria
24. Revision Notes
```

Object, service, event, API and agent specs should follow the structures defined in Chapters 14 through 17.

---

# 44. Identity Review Questions

When reviewing Identity specifications, reviewers shall ask:

1. What identity type is represented?
2. Is this a person, organization, user, customer, partner, agent, provider, AI agent or external system?
3. Which Core Domain owns this identity meaning?
4. Is the identity verified, inferred, imported or unknown?
5. What source and provenance are recorded?
6. What contact points are linked?
7. What relationships are linked?
8. What roles are assigned?
9. What permissions depend on this identity?
10. What business responsibility depends on this identity?
11. What communication records depend on this identity?
12. What AI capability may use this identity?
13. What events should be emitted for changes?
14. What product consumes this identity?
15. Would fragmentation occur if the product defined identity locally?
16. Can Codex implement this from approved specs?

---

# 45. Identity Anti-Patterns

## 45.1 User Equals Identity

Only login users are treated as identities.

Correction:

```text
User is one identity expression.
Customers, agents, providers, partners and AI agents also require identity.
```

## 45.2 Contact Equals Identity

Email or phone number is treated as full identity.

Correction:

```text
Contact Point may link to Identity.
It is not the full identity.
```

## 45.3 CRM Record Equals Customer Identity

Customer data is trapped inside product CRM.

Correction:

```text
Customer Identity must connect to Core Identity, Organization, Matter, Order and Communication.
```

## 45.4 Agent as Free Text

Foreign agent is stored only as free-text name in a matter.

Correction:

```text
Agent should be a Core Identity-linked object where repeated collaboration exists.
```

## 45.5 AI Without Identity

AI output is not attributed to AI agent identity, requesting user or reviewer.

Correction:

```text
AI activity must record AI agent identity and human responsibility.
```

## 45.6 Silent Merge

Duplicate identities are merged without audit.

Correction:

```text
Merge requires audit, provenance and rollback or correction strategy.
```

## 45.7 Product-Local Identity

MarkReg, Lite and MGSN define separate identities for the same actor.

Correction:

```text
Shared identity belongs to Core.
Products may define product-specific views.
```

---

# 46. Identity Rules

The following rules are established by this chapter.

## Rule 1 — Identity SHALL be a Core Foundation

Identity is required by permission, responsibility, communication, audit and AI governance.

## Rule 2 — Identity SHALL NOT mean only user account

User is one identity expression, not the whole identity model.

## Rule 3 — Identity Objects SHALL have source and quality where relevant

Imported, inferred or AI-extracted identity must record provenance and confidence.

## Rule 4 — Contact Points SHALL NOT replace Identity

Contact Points are channels or evidence of identity.

## Rule 5 — Identity Relationships SHALL be explicit when they affect responsibility

Employment, representation, assignment, ownership and service relationships must be structured where important.

## Rule 6 — Identity Verification SHALL affect trust and permission

Verification status must be visible to services where risk matters.

## Rule 7 — Identity Merge SHALL preserve audit

Merge must not erase history or provenance.

## Rule 8 — AI SHALL NOT verify or merge high-risk identity silently

AI may assist but not govern identity independently.

## Rule 9 — Products SHALL consume Identity through contracts

Products shall not redefine user, customer, agent or provider identity locally.

## Rule 10 — MVP SHALL include Identity foundation

A Core MVP without identity is not acceptable.

---

# 47. Specification Output

This chapter produces the following specification output:

- Identity definition;
- Identity principles;
- Identity ontology;
- Identity domain relationships;
- identity object types;
- Identity Object definition;
- Person Identity;
- Organization Identity;
- User Identity;
- Customer Identity;
- Partner Identity;
- Agent Identity;
- Service Provider Identity;
- AI Agent Identity;
- External System Identity;
- Contact Point;
- Role;
- Identity Relationship;
- Identity Verification;
- Identity Lifecycle;
- Identity Quality;
- Identity Source and Provenance;
- Identity Linking;
- Identity Merge and Duplicate Handling;
- Identity Permission;
- Identity Business Responsibility;
- Identity Communication;
- Identity Routing;
- Identity AI usage;
- Identity Events;
- Identity Services;
- Identity Contracts;
- Identity Data Contract baseline;
- Identity API baseline;
- Product Consumption;
- MVP Boundary;
- `core-specs/` file structure;
- review questions;
- anti-patterns;
- Identity rules.

These outputs guide the detailed specifications in `core-specs/`.

---

# 48. Execution Mapping

This chapter controls identity-related implementation assets.

| Identity Specification Element | Execution Mapping |
|--------------------------------|------------------|
| Identity Object | identity model and persistence |
| Person / Organization | object specs and identity relationship models |
| User | user context, role and permission integration |
| Contact Point | email, phone, messaging and address records |
| Identity Relationship | relationship table or graph structure |
| Verification Status | status fields, review workflow and events |
| Identity Quality | quality scoring, warnings and service conditions |
| Identity Linking | identity resolution and linking service |
| Identity Merge | merge service, audit and correction |
| Identity Events | event specs and event publishing |
| Identity Contracts | data, API, event and consumption contracts |
| AI Usage | agent contract and review rules |
| Product Consumption | MarkReg, Lite, MGSN and Workplace identity views |
| MVP | Codex task sequencing |

Implementation shall preserve identity meaning, provenance, verification and auditability.

---

# 49. Relationship to core-specs/

This chapter is the manuscript source for Identity-related `core-specs/`.

Detailed specs shall be maintained in:

```text
core-specs/domains/identity.md
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
```

No product document shall override the Core Identity Specification.

No implementation task shall create identity meaning without reference to approved Identity specs or explicit architecture review.

---

# 50. Exclusions

This chapter shall not include:

- complete database schema;
- authentication provider implementation;
- login UI;
- user onboarding screen;
- CRM page design;
- agent directory product UI;
- service provider marketplace UI;
- full permission engine;
- all production API endpoints;
- production AI prompts;
- deployment architecture;
- implementation code.

These belong elsewhere.

---

# 51. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines Identity clearly as broader than user account.
- It establishes Identity as a Core Foundation.
- It defines identity object types and relationships.
- It distinguishes Identity, User, Customer, Partner, Agent, Service Provider, AI Agent and Contact Point.
- It defines verification, quality, source, linking, merge and lifecycle rules.
- It connects Identity to permission, business responsibility, communication, routing, AI and audit.
- It defines baseline services, events, contracts and API surface.
- It provides MVP boundary.
- It provides `core-specs/` structure.
- It includes review questions, anti-patterns and rules.
- It supports Book 02 TOC v1.2.
- It supports implementation without becoming product UI or auth infrastructure design.

---

# 52. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 18, defining Identity Specification for the MarkOrbit Core. |

---

**End of Chapter**
