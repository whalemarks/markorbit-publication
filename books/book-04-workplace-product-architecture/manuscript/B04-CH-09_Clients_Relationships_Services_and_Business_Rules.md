# B04-CH-09 — Clients, Relationships, Services and Business Rules

**Status:** Release Candidate 1  
**Chapter Map:** B04-TOC-V0.1  
**Part:** Part II — Organization Context and Operating Environment

## Chapter Purpose

This chapter defines how an Organization Workplace represents clients, relationship context, professional service offerings, engagement conditions, pricing context, preferences, and organization-specific business rules.

CH07 established the organization and active Workplace Context.

CH08 established how people participate through relationships, roles, permissions, responsibility, and accountability.

The next question is:

```text
For whom is the organization working?

What relationship gives the work meaning?

Which professional service is being considered or delivered?

Which commercial and operating rules apply?

How does that context remain coherent across Products
without becoming centrally owned or redefining Core?
```

The central proposition of this chapter is:

```text
Client Identity
→ identifies the person or organization involved

Client Relationship
→ represents this organization’s governed relationship
with that client or represented party

Service Offering
→ describes professional value the organization may provide

Service Context
→ describes the specific need, scope, parties,
commercial conditions, and operating constraints

Business Rules
→ express organization-specific commercial and operating logic

Core Objects and Owning Services
→ formalize Customers, Opportunities, Orders, Matters,
Documents, Communications, and other business facts
```

These concepts are connected.

They are not interchangeable.

This chapter does not create a second Customer, Opportunity, Order, Matter, Policy, Pricing, or Service model.

Book 02 remains authoritative for shared Identity, Customer, Opportunity, Order, Matter, Permission, Policy, Business Responsibility, and Owning Service meaning.

Book 03 remains authoritative for Workflow, Task, review, approval, Communication execution, and protected-action coordination.

Book 04 explains how an independent organization preserves the client and commercial context required to consume those foundations through Workplace.

---

## 1. Professional Work Begins with a Relationship

Professional services are not delivered to abstract records.

They are delivered through relationships among people and organizations.

A trademark service may involve:

- the organization providing the service;
- an instructing agency;
- an end client;
- a brand owner;
- an applicant;
- a trademark owner;
- an authorized contact;
- a payer;
- a beneficiary;
- a foreign associate;
- an external professional representative.

These parties may be the same.

They may also be different.

For example:

```text
Chinese trademark agency
→ instructing client and commercial customer

Brand company
→ represented end client and applicant

Named employee
→ communication contact

Yoomarks
→ service organization

Foreign associate
→ external service provider
```

A system that collapses all of these parties into one generic `customer` field loses professional meaning.

Workplace must preserve both identity and relationship context.

The first question is not only:

```text
Who is this entity?
```

It is also:

```text
What relationship does this organization have with the entity,
for which purpose,
under which engagement,
and with which responsibilities?
```

---

## 2. Client Is a Relationship Role, Not a Universal Identity Type

A person or organization may be a client in one context and something else in another.

The same organization may be:

- a direct client;
- a referral partner;
- an instructing agency;
- an applicant;
- a service provider;
- a co-counsel;
- a network participant;
- a prospect;
- a former client.

Therefore:

```text
Identity
≠
Client Relationship
```

Identity provides a stable reference to a real-world person or organization.

Client Relationship describes how that identity participates in one organization’s professional and commercial context.

A shared MarkOrbit identity may help several Products recognize that two records refer to the same organization.

It must not imply that every Workplace shares the same relationship with that organization.

For example:

```text
Shared Identity:
Company X

Workplace A relationship:
long-term direct client with negotiated pricing

Workplace B relationship:
prospective client with no engagement

Workplace C relationship:
adverse party in a dispute
```

The identity may be shared or resolvable.

The relationship context remains organization-specific and purpose-bound.

---

## 3. The Client Relationship Belongs to the Organization’s Orbit

MarkOrbit may provide shared infrastructure for identity resolution, communication, Products, Execution, and network participation.

Use of that infrastructure does not transfer the professional relationship to the platform.

The organization retains control over its relationship context, including:

- engagement history;
- authorized contacts;
- service history;
- client instructions;
- commercial terms;
- pricing arrangements;
- communication preferences;
- confidentiality expectations;
- responsible professionals;
- partner or referral attribution;
- trust and service experience;
- retention and access policy.

This principle should not be misunderstood as a claim that a client is property.

Clients remain independent persons or organizations, and legal rights in data, files, and records depend on applicable law, professional duties, contracts, and client rights.

The architectural point is narrower:

> A central platform must not treat the relationship context created by one organization as centrally owned commercial inventory.

The relationship may use shared identities and shared services.

Its organization-specific history, commitments, and private context remain within the governing Orbit unless authorized otherwise.

---

## 4. One Client May Participate Through Several Distinct Parties

Professional engagement often separates commercial, legal, and operational roles.

A conforming Workplace should be able to distinguish at least conceptually among:

```text
instructing client
represented party
applicant or owner
payer
beneficiary
primary contact
authorized signatory
portfolio contact
professional representative
referral source
```

These roles should not be inferred from convenience.

The email sender is not automatically the authorized instructing party.

The payer is not automatically the trademark owner.

The applicant is not automatically the commercial customer.

The primary contact is not automatically authorized to approve every decision.

A Product may simplify the user experience, but the underlying relationship must remain explainable.

For example, MarkReg may present one unified intake journey while preserving:

```text
Who requested the filing?

Who owns the mark?

Who will sign the Power of Attorney?

Who receives the invoice?

Who may approve goods and services?

Who receives status Communications?
```

Product simplicity must not erase professional role distinctions.

---

## 5. Relationship Context Must Be Explicit and Scoped

A Client Relationship should be understood through a defined context rather than one unlimited profile.

A minimum conceptual relationship context may include:

```text
relationship identity
participating organization
related person or organization identity
relationship role
authority source
service or engagement scope
responsible users
client contacts
confidentiality level
Product visibility
start and end
status
provenance
```

The context may be scoped to:

- the whole client relationship;
- one brand portfolio;
- one jurisdiction;
- one service line;
- one Order;
- one Matter;
- one project;
- one temporary consultation;
- one network collaboration.

A broad relationship does not automatically authorize access to every Matter, Document, price, or Communication.

Likewise, a limited engagement must not silently become a permanent full-client relationship.

The rule is:

```text
Known client
≠
unlimited context
```

Client context remains subject to identity, permission, purpose, relationship scope, professional duty, and applicable Policy.

---

## 6. Relationship Ownership and Operational Responsibility Are Different

An organization may assign an account owner, relationship manager, sales owner, responsible partner, matter owner, or process operator.

These assignments serve different purposes.

```text
Relationship ownership
→ responsibility for continuity of the client relationship

Commercial ownership
→ responsibility for opportunity, quotation, and conversion

Professional ownership
→ responsibility for professional judgment and service quality

Matter ownership
→ responsibility for a specific formal Matter

Execution responsibility
→ responsibility for performing assigned work

Communication responsibility
→ responsibility for approved client interaction
```

One person may hold several responsibilities.

They must not be treated as automatically equivalent.

A salesperson may own the commercial relationship but lack authority to approve legal advice.

A process user may execute filing preparation but not own the client relationship.

A responsible professional may approve the advice but not set discount levels.

A Product may display one “owner” field for convenience.

Workplace architecture must preserve the underlying distinctions wherever they affect permission, review, escalation, value attribution, or accountability.

---

## 7. Relationship Types Must Remain Contextual

Organizations may maintain several relationship types, such as:

- direct client;
- agency client;
- enterprise client;
- referral partner;
- channel partner;
- co-counsel;
- represented party;
- former client;
- prospective relationship;
- restricted or conflicted relationship.

These types help the organization determine:

- who may communicate;
- which pricing applies;
- which services may be offered;
- which conflict or confidentiality checks are required;
- which Product journey is appropriate;
- which users may access the context;
- which external providers may be involved.

But relationship-type labels must not become universal Core semantics without governance.

Different organizations may use different commercial categories.

The architecture should preserve meaning and mapping without requiring one global taxonomy for every firm.

The minimum shared requirement is that relationship purpose, scope, and authority remain explicit enough for downstream use.

---

## 8. Prospective Relationships Must Not Become Formal Clients Silently

Before a formal client relationship exists, an organization may observe:

- a contact inquiry;
- a referral;
- a market signal;
- a content interaction;
- a potential brand need;
- an AI-detected service opportunity;
- an imported contact;
- an existing customer’s new requirement.

These may justify follow-up.

They do not automatically establish:

- an engagement;
- representation;
- confidentiality scope;
- a formal Opportunity;
- an Order;
- a Matter;
- professional responsibility.

The candidate-before-canonical principle applies:

```text
relationship signal
→ prospective relationship context
→ qualification and human confirmation
→ formal Opportunity where appropriate
→ accepted commercial commitment
→ Order or Matter through the proper Owning Service
```

Workplace may surface and organize signals.

It must not silently create professional obligations from inferred interest.

Detailed candidate and Next Best Action architecture belongs to CH17.

The relationship boundary established here is that observed interest is not the same as accepted client status.

---

## 9. Client Context Is Larger Than a Matter

A Matter is a formal professional execution object.

A client relationship extends beyond one Matter.

It may include:

- several brands;
- several jurisdictions;
- several Matters;
- several Orders;
- historical advice;
- recurring renewals;
- communication preferences;
- pricing arrangements;
- responsible contacts;
- portfolio strategy;
- relationship risk;
- service history;
- future opportunities.

Therefore:

```text
Client Relationship
≠
Matter
```

The relationship may exist before the first Matter and continue after a Matter closes.

At the same time, a Matter may require more restricted context than the broader client profile.

A sensitive dispute, acquisition, or evidence package may be visible only to a specific team.

Workplace preserves relationship continuity.

The relevant Owning Service preserves formal Matter state.

Neither should absorb the other.

---

## 10. Service Offering Describes Professional Value

A professional organization needs to describe what it can offer.

Examples include:

- trademark filing;
- search and clearance;
- office action response;
- opposition;
- cancellation;
- renewal;
- assignment;
- recordal;
- portfolio management;
- evidence preparation;
- local representation;
- strategic advice;
- provider coordination.

A Service Offering is the organization’s commercial and professional expression of value.

It may define:

- service name;
- target client;
- jurisdiction or coverage;
- included work;
- excluded work;
- prerequisites;
- expected deliverables;
- pricing approach;
- review level;
- responsible team;
- external Capability requirements;
- Product entry points.

A Service Offering is not the same as a Core Service.

```text
Professional Service Offering
→ what the organization offers to a client

Core Service
→ authoritative system boundary for formal operations and mutation
```

The distinction is essential.

A Product may present a professional service package.

A Core Service may create an Order or update a Matter.

The similar word does not imply the same architectural responsibility.

---

## 11. Capability, Service Offering, Product, and Workflow Are Different

A professional service often uses Capabilities, Products, and Workflows.

It is not identical to any of them.

```text
Capability
→ what professional ability is available

Skill
→ how the capability may be implemented

Service Offering
→ how the organization packages professional value
for a client or market

Product
→ how the user experiences a focused journey

Workflow
→ how governed multi-step work proceeds
```

For example:

```text
Capability:
Prepare Trademark Classification

Service Offering:
United States Trademark Application Package

Product:
MarkReg filing journey

Workflow:
Intake → preparation → review → approval → submission preparation
```

The organization may change packaging or pricing without redefining the Capability.

A Product may change its user journey without changing the service contract.

A Workflow may evolve without changing the public name of the service.

Keeping these distinctions allows Products and organizations to innovate without semantic drift.

---

## 12. Service Context Connects Need to Governed Work

A Service Offering is general.

Service Context is specific.

Service Context describes the professional and commercial frame for one identified need.

A minimum conceptual model may include:

```text
client relationship
represented party
requested outcome
service type
jurisdiction and scope
relevant brands or trademarks
commercial context
required information and Documents
responsible users
review requirements
external provider needs
Product origin
status and provenance
```

Service Context may exist before a formal Order or Matter.

It may begin when:

- a client asks a question;
- Lite identifies a likely need;
- MarkReg begins guided intake;
- an existing Matter creates a related need;
- MGSN identifies missing jurisdiction capability;
- a professional prepares service options.

The context may later support creation of formal Objects through the proper Owning Services.

```text
Service Context
→ supports preparation and decision

Order
→ records accepted commercial commitment

Matter
→ records formal professional work
```

Service Context must not become a hidden substitute for Order or Matter state.

---

## 13. Engagement Context Defines the Authorized Relationship for Work

A service need does not by itself establish an engagement.

Engagement Context describes the authorized basis on which the organization may proceed.

It may include:

- instructing party;
- represented party;
- authority to instruct;
- service scope;
- exclusions;
- conflicts or restrictions;
- fee basis;
- payment expectations;
- communication channel;
- confidentiality conditions;
- responsible professional;
- termination or expiry conditions.

Engagement Context may be supported by:

- a signed agreement;
- accepted terms;
- a partner framework;
- a standing instruction;
- a Product confirmation;
- an approved Order;
- a documented professional relationship.

Workplace may preserve and expose the relevant context.

It does not determine legal enforceability merely by storing a record.

The real organization and the applicable legal and professional framework remain authoritative.

---

## 14. Pricing Is Organization Context, Not Universal Truth

Professional pricing depends on the organization, client, service, jurisdiction, provider, currency, timing, risk, and commercial strategy.

MarkOrbit must therefore avoid one universal price model.

Pricing context may include:

- public list price;
- standard internal price;
- client-specific price;
- partner price;
- provider cost;
- official fee;
- professional fee;
- margin target;
- discount authority;
- tax treatment;
- currency;
- exchange-rate basis;
- validity period;
- payment schedule;
- refund or cancellation rule.

These values must remain distinguishable.

```text
Provider cost
≠
client price

Price recommendation
≠
approved quotation

Quotation
≠
accepted Order

Estimated official fee
≠
final official charge

Discount permission
≠
discount approval
```

Workplace may preserve pricing rules and client-specific commercial context.

Products may calculate and present options.

AI may explain or prepare a draft.

An approved Owning Service must formalize the quotation, Order, payment obligation, or financial state where required.

---

## 15. Pricing Authority Must Be Explicit

Not every user who can view a service may price it.

Not every user who can prepare a quotation may approve a discount.

Not every account owner may alter provider cost assumptions.

Pricing authority may depend on:

- role;
- client relationship;
- service type;
- margin threshold;
- discount level;
- currency exposure;
- provider commitment;
- risk;
- approval policy;
- time validity.

A Workplace should preserve distinctions among:

```text
may view price
may calculate price
may prepare quote
may approve discount
may issue quote
may amend commercial terms
may accept payment condition
```

These are different permissions and responsibilities.

A Product button must not collapse them.

Where a price affects an external commitment, protected state, or formal record, Permission, Policy, review, Execution, and the proper Owning Service still apply.

---

## 16. Business Rules Express Organization-Specific Operating Logic

Organizations need rules that reflect how they operate.

Examples include:

- minimum margin thresholds;
- client acceptance conditions;
- service eligibility;
- discount limits;
- preferred provider rules;
- review requirements;
- communication preferences;
- payment conditions;
- document completeness expectations;
- escalation thresholds;
- restricted jurisdictions;
- service exclusions;
- data-handling requirements;
- quality-control rules.

These rules are part of organizational context.

They should not be promoted automatically into universal Core semantics.

A useful distinction is:

```text
Core rule
→ shared semantic or governance rule
that must remain consistent across MarkOrbit

Organization business rule
→ rule specific to one organization’s
commercial or operating practice

Client-specific instruction
→ rule or preference applicable to one relationship

Product behavior
→ interaction or composition choice for one Product
```

Workplace preserves and supplies organization business rules.

It does not become a second Core Policy engine.

---

## 17. Business Rule, Preference, Policy, Contract, and Workflow Are Distinct

Organization-specific logic appears in several forms.

They must not be confused.

### Preference

A preferred but overridable choice.

Example:

```text
Prefer Provider A for routine filings in Jurisdiction X.
```

### Business rule

A documented organization requirement or commercial rule.

Example:

```text
Quotes below the minimum margin require management review.
```

### Policy

A governed contextual constraint evaluated through the appropriate Policy boundary.

Example:

```text
Sensitive client evidence may not be shared with an external provider
without explicit authorization.
```

### Contract or engagement term

An agreed obligation among parties.

Example:

```text
The quotation remains valid for thirty days.
```

### Workflow condition

A governed execution requirement within a specific process.

Example:

```text
The filing package cannot proceed to submission preparation
until the goods and services review is complete.
```

A Workplace may present these together.

It must preserve their different authority and enforcement paths.

A preference must not masquerade as Policy.

A business rule must not bypass Permission.

A contract term must not be changed by Product convenience.

A Workflow condition must not be implemented as an informal reminder.

---

## 18. Organization Rules Need Scope, Source, Version, and Authority

A rule without context becomes dangerous.

A conforming Workplace should preserve, where relevant:

- rule owner;
- authority source;
- organization or unit scope;
- client scope;
- service scope;
- Product scope;
- jurisdiction scope;
- effective date;
- expiry;
- version;
- override authority;
- reason;
- audit and provenance.

For example:

```text
“Require two reviewers”
```

is incomplete.

A usable rule needs to explain:

```text
For which service?

For which risk level?

For which jurisdictions?

Which reviewer qualifications?

Who may override it?

Which version applied to historical work?
```

Current business rules support current decisions.

Historical rules explain historical pricing, review, and service behavior.

Rules must not be rewritten retrospectively without preserving trace.

---

## 19. Client Instructions and Preferences Need Governance

Clients may have important preferences or standing instructions, such as:

- approved communication contacts;
- required purchase-order references;
- preferred jurisdictions;
- goods and services drafting style;
- budget limits;
- escalation contacts;
- prohibited providers;
- reporting frequency;
- document format;
- invoicing requirements;
- language preference;
- confidentiality restrictions.

These instructions can improve service quality and continuity.

They can also become stale, ambiguous, or over-applied.

Workplace should preserve:

- source;
- date;
- scope;
- confirming person;
- authority;
- version;
- exceptions;
- expiry or review date;
- conflicts with current instruction.

A preference for one Matter must not automatically become a permanent organization-wide rule.

An old instruction must not override a newer confirmed direction.

AI personalization must not convert repeated behavior into binding client instruction without validation.

Detailed private knowledge and preference architecture is developed in CH10.

---

## 20. Business Rules Must Not Create Hidden Protected Action

An organization may define automation rules for efficiency.

For example:

- prepare a renewal reminder ninety days before expiry;
- suggest a preferred provider;
- calculate a standard quote;
- create a draft follow-up;
- identify a missing document;
- recommend escalation.

These rules may support preparation.

They do not authorize protected action automatically.

```text
automatic preparation
≠
automatic external commitment
```

A rule must not silently:

- accept a client;
- create representation;
- issue final advice;
- send a Communication;
- approve a quotation;
- appoint a provider;
- place an Order;
- submit a filing;
- approve payment;
- change formal Matter state.

Where consequential action is involved, the chain remains:

```text
Business Rule or Recommendation
→ Prepared Action
→ Permission and Policy
→ required Human Review or Approval
→ governed Execution
→ Owning Service mutation
```

---

## 21. Products Consume Relationship and Service Context Without Owning It

Different Products may use the same organizational relationship for different journeys.

### Lite

Lite may surface:

- follow-up needs;
- client reminders;
- relationship summaries;
- content opportunities;
- service suggestions;
- prepared Communications;
- Next Best Actions.

### MarkReg

MarkReg may use:

- instructing client;
- applicant and owner identity;
- client preferences;
- service package;
- price context;
- required Documents;
- responsible professional;
- Matter continuity.

### MGSN interfaces

MGSN may receive only the authorized need context required to identify or collaborate with providers.

It should not receive the full client profile, pricing history, or private relationship notes by default.

The rule is:

```text
Product consumes authorized relationship context.

Product does not become the owner of the relationship.
```

Cross-Product continuity requires explicit handoff and common references, not unrestricted copying.

---

## 22. Cross-Organization Relationships Need Purpose-Limited Sharing

A service relationship may require collaboration across Workplaces.

For example:

```text
Client Workplace
→ instructing agency Workplace
→ Yoomarks Workplace
→ foreign associate Workplace
```

Each participating organization has its own relationship, responsibility, and data boundary.

The same end client may appear in several contexts.

Cross-organization collaboration must define:

- which party is represented;
- who owns communication with the client;
- which information may be shared;
- which service is delegated;
- which provider receives which Documents;
- who reviews the outcome;
- who remains professionally accountable;
- which organization may record which formal fact.

Participation in MGSN does not make all relationship context common network data.

The network connects authorized service need and Capability.

It does not flatten the organizations into one shared CRM.

---

## 23. AI May Assist but Must Not Own the Commercial Relationship

AI may support client and service work by:

- summarizing relationship history;
- identifying missing context;
- comparing service options;
- preparing quotation alternatives;
- explaining pricing components;
- detecting inconsistent instructions;
- recommending follow-up;
- drafting client Communications;
- identifying likely service needs;
- preparing a service-context brief.

AI must operate under active Workplace Context, permission, approved knowledge, relationship scope, and audit.

AI must not:

- infer representation without confirmation;
- expose one client’s information to another;
- commit the organization to a price;
- approve a discount;
- accept a client autonomously;
- create a formal Opportunity, Order, or Matter without governed confirmation;
- send client Communication autonomously;
- alter engagement terms;
- appoint a provider;
- claim professional authority.

AI may help the organization understand and prepare.

The organization and accountable humans retain the relationship and decision responsibility.

---

## 24. Relationship, Service, and Rule Context Must Have Lifecycle

Organizations and client relationships change.

A client may become inactive.

Contacts may leave.

A service may be withdrawn.

Pricing may change.

A provider may no longer be preferred.

An engagement may end.

A rule may be superseded.

A minimum lifecycle approach should preserve:

- current status;
- effective period;
- superseded state;
- historical relationship;
- responsible actor;
- reason for change;
- linked active work;
- retention requirement;
- audit.

Deactivation must not erase history.

A former client may remain visible in prior Matters and Communications while losing current access or active pricing.

A superseded price rule must remain available to explain an earlier quotation.

A terminated engagement must block new action without silently invalidating historical records.

The principle is:

```text
Current context governs current work.

Historical context explains historical commitments and outcomes.
```

---

## 25. The Minimum Client and Commercial Context Model

A minimum conceptual model can be expressed as:

```text
Identity
  │
  ├── Person
  └── Organization
        │
        ▼
Client / Relationship Context
  │
  ├── relationship role
  ├── instructing and represented parties
  ├── authorized contacts
  ├── responsible users
  ├── engagement context
  ├── preferences and instructions
  ├── confidentiality and access scope
  ├── service history
  └── lifecycle and provenance
        │
        ▼
Service Context
  │
  ├── requested outcome
  ├── Service Offering
  ├── jurisdiction and scope
  ├── price and commercial context
  ├── business rules
  ├── required review
  ├── external Capability need
  └── Product origin
        │
        ▼
Formalization through Owning Services
  │
  ├── Opportunity
  ├── Order
  ├── Matter
  ├── Document
  ├── Communication
  └── Event
```

This model is architectural.

It does not define one database schema, universal CRM, price engine, contract engine, or service catalog implementation.

Different Products and Workplace editions may implement different views.

The responsibility distinctions must remain.

---

## 26. Required Distinctions

This chapter establishes the following required distinctions:

```text
Identity ≠ Client Relationship

Client Relationship ≠ Matter

Instructing client ≠ represented party

Contact ≠ authority to instruct

Payer ≠ applicant or owner

Relationship owner ≠ professional reviewer

Service Offering ≠ Core Service

Service Offering ≠ Capability

Service Context ≠ Order

Price recommendation ≠ approved quotation

Quotation ≠ accepted Order

Provider cost ≠ client price

Preference ≠ Policy

Business rule ≠ Workflow

Client instruction ≠ universal organization rule

Relationship signal ≠ formal Opportunity

Product visibility ≠ relationship ownership

AI preparation ≠ commercial commitment
```

These distinctions prevent customer convenience, commercial pressure, or Product design from weakening professional and architectural boundaries.

---

## 27. Failure Modes This Chapter Prevents

### Generic-customer collapse

The instructing agency, applicant, owner, payer, and contact are merged into one record.

### Platform relationship capture

Shared infrastructure is treated as the owner of client relationships and commercial history.

### Product CRM fragmentation

Lite, MarkReg, and other Products create incompatible client, pricing, and service profiles.

### Matter-only thinking

The organization loses relationship continuity before and after formal Matters.

### Service ambiguity

Professional Service Offering, Core Service, Capability, Product, and Workflow are treated as the same thing.

### Pricing collapse

Official fees, provider costs, professional fees, discounts, and client prices are mixed.

### Hidden commercial authority

Any user who can prepare or view a quote can also issue or approve it.

### Rule drift

Informal preferences become hidden Policies or automated protected actions.

### Stale instruction reuse

Old client preferences or prices are applied without checking scope, version, or current authority.

### Cross-Orbit leakage

A provider or network interface receives the full client and commercial context for a limited collaboration.

### AI relationship overreach

AI infers engagement, commits pricing, or communicates externally without authorized confirmation.

These failures are not merely CRM defects.

They affect confidentiality, professional responsibility, commercial autonomy, Product consistency, and formal execution authority.

---

## 28. Minimum Conformance Rule

A conforming Workplace should preserve the following rule:

```text
Identity remains distinct from organization-specific relationship context.

The organization preserves control of its client relationships,
engagement history, pricing, instructions, and service context.

Commercial, represented, paying, instructing,
and communication parties remain distinguishable.

Client context is scoped, purpose-bound, permission-aware,
versioned, and historically explainable.

Professional Service Offerings remain distinct from
Capabilities, Products, Workflows, and Core Services.

Pricing values and authorities remain explicit.

Organization business rules do not redefine Core,
bypass Permission or Policy,
or authorize protected action by themselves.

Products consume authorized relationship context
without owning the relationship.

Cross-Workplace sharing is purpose-limited.

AI prepares and recommends under governance.

Humans decide.

Execution governs coordinated work.

Owning Services change and record formal business facts.
```

Different organizations may use different client models, service packages, pricing structures, and business rules.

They may not change the shared authority model by local convention.

---

## 29. Chapter Boundary

This chapter defines how client relationships, service context, pricing, preferences, engagement conditions, and organization business rules become coherent within Workplace.

It does not define:

- a universal CRM schema;
- final Customer or Opportunity lifecycle values;
- lead-scoring formulas;
- final service catalog schemas;
- legal engagement templates;
- conflict-checking implementation;
- pricing algorithms;
- tax calculation;
- accounting treatment;
- foreign-exchange services;
- discount approval workflows;
- quote or invoice APIs;
- Order or Matter state transitions;
- Product screens;
- provider contracting;
- payment execution;
- external Communication send;
- protected-action execution.

Private knowledge, AI context, preferences, and organizational memory are developed further in CH10.

Work, review, Communication, and operating surfaces belong to CH11.

Data boundaries, Local Vault, and synchronization belong to CH12.

Opportunity candidates and Next Best Action belong to CH17.

Product-specific client and service journeys belong to Part IV.

Artifact, Document, Delivery, and Publish boundaries belong to Part V.

Network relationship and routing architecture belong to Part VI.

This chapter does not modify Book 02 Customer, Opportunity, Order, Matter, Policy, Permission, Business Responsibility, or Service semantics.

It explains how Workplace supplies organization-controlled relationship and commercial context to those shared foundations.

---

## 30. Chapter Conclusion

A professional organization does not operate through customer records alone.

It operates through relationships, engagements, service commitments, commercial judgment, client instructions, and organization-specific rules.

Workplace preserves that reality around the organization without absorbing the formal authorities around it.

The architecture can be summarized as:

```text
Identity
→ who the person or organization is

Client Relationship
→ how this Organization Workplace relates to them

Service Offering
→ what professional value may be provided

Service Context
→ what need, scope, parties, and conditions apply now

Business Rules
→ how the organization chooses to operate

Permission, Policy, and Responsibility
→ who may act and under which constraints

Execution
→ how consequential work proceeds

Owning Services
→ how formal business facts are created and changed
```

A conforming Workplace must preserve:

- organization-controlled relationship context;
- distinction among instructing, represented, paying, and responsible parties;
- continuity beyond individual Matters;
- explicit service and engagement scope;
- clear pricing components and authority;
- governed business rules;
- Product independence without client fragmentation;
- purpose-limited cross-Workplace sharing;
- human commercial and professional accountability;
- formalization through the proper Owning Services.

This allows MarkOrbit to support service conversion without turning the ecosystem into a centralized CRM, support organizational autonomy without isolating client context, and support AI assistance without allowing generated recommendations to become professional or commercial commitments.

With clients, relationships, services, and business rules established, Part II can move to the private knowledge, AI context, preferences, and organizational memory that allow each Workplace to learn and operate in its own distinctive way.
