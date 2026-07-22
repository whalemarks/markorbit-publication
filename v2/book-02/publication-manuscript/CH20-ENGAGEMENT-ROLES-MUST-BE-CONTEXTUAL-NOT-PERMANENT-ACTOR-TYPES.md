# CH20 — Engagement Roles Must Be Contextual, Not Permanent Actor Types

## A person or organization is not reducible to one platform role

Professional collaboration produces many role names:

- Demand Originator;
- Relationship Owner;
- Contracting Party;
- Payment Receiver;
- Solution Orchestrator;
- Capability Contributor;
- Professional Authority;
- Delivery Owner;
- Reviewer;
- Approver;
- Provider;
- Customer Contact.

The architecture becomes brittle when these roles are stored as permanent types attached to a Person, Organization or Workplace.

The same actor can legitimately hold different roles in different Engagements, Matters and Work Packages.

```text
actor identity
≠ permanent engagement role
```

Book 02 therefore treats engagement roles as contextual assignments or references, not universal actor classes.

## The role record needs context

A contextual role should identify:

- actor;
- represented Person, Organization or Workplace;
- Engagement or other governing context;
- role type;
- purpose;
- scope;
- object references;
- authority source;
- allowed actions;
- disclosure rights;
- effective time;
- expiry;
- delegation and re-delegation rules;
- suspension or revocation;
- Evidence.

```text
same actor
+ different context
= different role and authority
```

A Workplace may be Relationship Owner in one white-label Engagement and Delivery Owner in another. A lawyer may be Professional Authority for one jurisdiction and merely a contributor in a cross-border strategy exercise outside that jurisdiction.

## Demand Originator

Demand Originator identifies who introduced, detected or first articulated a Need or Opportunity.

Possible originators include:

- customer;
- partner Workplace;
- Lite public-data signal;
- MarkReg lifecycle event;
- professional adviser;
- internal account manager;
- automated monitoring service.

Demand origin does not automatically create ownership of the customer, revenue, delivery or decision.

```text
Demand Originator
≠ Relationship Owner
≠ Contracting Party
≠ commission entitlement automatically
```

Commercial attribution or commission should rely on separate governed terms and Evidence.

## Relationship Owner

Relationship Owner coordinates the legitimate commercial and communication relationship with the customer for a defined scope.

Responsibilities may include:

- contact continuity;
- consent and communication rules;
- branding and disclosure expectations;
- commercial protection;
- introduction of delivery participants;
- relationship handover where authorized.

But:

```text
Relationship Owner
≠ owner of the customer
≠ Matter Formal-state Authority
≠ Professional Authority
≠ universal commercial approver
```

The role is bounded by the Engagement, Workplace sovereignty and applicable customer rights.

## Contracting Party

Contracting Party identifies the Person or Organization bound by the relevant commercial or legal agreement.

There may be several contracts:

- customer service agreement;
- provider agreement;
- contributor terms;
- platform subscription;
- data-processing agreement;
- referral or revenue-share agreement.

```text
Contracting Party for one agreement
≠ Contracting Party for every relationship
```

The role must reference the specific contract or commitment.

## Payment Receiver

Payment Receiver identifies which actor is authorized to receive a defined payment under a commercial arrangement.

It does not establish custody authority over all funds or permission to redirect payments.

```text
Payment Receiver
≠ Relationship Owner
≠ Professional Authority
≠ universal Payee
≠ payment approval
```

The role should be tied to amount category, currency, purpose, recipient verification and settlement reference.

## Solution Orchestrator

Solution Orchestrator coordinates the overall route from Need to a viable combination of Products, Capabilities, Workplaces or providers.

The role may:

- compare routes;
- assemble a delivery model;
- identify dependencies;
- coordinate handoffs;
- expose decision-ready options.

It does not automatically own delivery execution, customer relationship or professional approval.

```text
Solution Orchestrator
≠ Delivery Owner automatically
≠ Professional Authority
≠ Customer Decision Maker
```

The distinction is especially useful when Guide or a partner designs the route but another team performs delivery.

## Capability Contributor

Capability Contributor is an actor who supplies bounded work, analysis, artifact, verification or professional input within an authorized context.

The role may be held by:

- Person;
- Workplace;
- contributor network participant;
- provider professional;
- governed AI or deterministic implementation.

```text
Contributor
≠ employee
≠ Provider automatically
≠ reviewer
≠ final authority
```

Actual work should be represented by Contribution and linked to Assignment or another valid authorization context.

## Professional Authority

Professional Authority identifies the actor whose external qualification, appointment and scope allow a reserved professional judgment or action.

The role cannot be granted merely by Product configuration or Engagement preference.

It requires the applicable combination of:

- verified qualification;
- jurisdiction;
- current status;
- conflict clearance;
- appointment or instruction;
- accepted scope;
- matter-specific authority.

```text
Professional Authority reference
≠ qualification created by platform
```

## Delivery Owner

Delivery Owner coordinates the integrity of the delivery path.

Responsibilities may include:

- Work Package completeness;
- dependency sequencing;
- assignment and reviewer availability;
- customer-decision checkpoints;
- Evidence Return completeness;
- escalation and recovery;
- outcome assembly and delivery communication.

Continue to preserve:

```text
Delivery Owner
≠ Relationship Owner
≠ universal Approver
≠ Professional Authority
≠ formal-state owner
```

Delivery ownership means ensuring the required authority exists, not impersonating that authority.

## Reviewer and Approver

Reviewer performs a typed judgment over an exact object version and declared criteria. Approver grants permission for a specified next transition.

```text
Reviewer
≠ Approver

Approver for communication
≠ Approver for payment
≠ Approver for professional action
```

Both roles must be contextual and version-bound. A standing job title should not substitute for the specific authority record.

## Provider

Provider is normally an Organization profile bearing external professional or operational responsibility. A Provider may participate in an Engagement and may designate individual professionals.

```text
Provider Organization
≠ every employee is Professional Authority

Provider selected
≠ Provider appointed
≠ Provider accepted
```

Provider status, eligibility, appointment, instruction and Return remain separate.

## Roles can coexist without collapsing

One actor may hold several roles simultaneously. The platform should preserve each role independently.

Example:

```text
Partner Workplace
= Demand Originator
+ Relationship Owner
+ Contracting Party
+ Payment Receiver

MarkReg Workplace
= Solution Orchestrator
+ Delivery Owner

Local Provider
= Provider
+ Professional Authority

Customer Director
= Customer Decision Maker
+ Signatory
```

This does not imply that any participant gains the authorities of the others.

## Conflict and incompatibility rules

Some role combinations may create conflict or require additional Review.

Examples include:

- reviewer also being the original contributor;
- provider recommending itself without disclosure;
- payment receiver approving its own disputed charge;
- Relationship Owner withholding material professional risk;
- AI implementation acting as both generator and sole validator.

Core may support role references and incompatibility vocabulary, while Products and governance policies define context-specific conflict rules.

```text
multiple roles allowed
≠ every role combination acceptable
```

## Delegation

A role may be delegated only where the authority source permits it.

Delegation should preserve:

- delegator;
- delegate;
- represented actor;
- exact role and scope;
- effective period;
- prohibited actions;
- re-delegation permission;
- revocation;
- Evidence.

```text
role delegated
≠ source authority transferred permanently
```

## Substitution and continuity

When an actor becomes unavailable, a replacement does not inherit role history automatically.

The platform should:

- end or suspend the prior role;
- identify active responsibilities;
- verify replacement eligibility and authority;
- transfer only permitted context;
- reissue Assignments or approvals where required;
- preserve prior responsibility and Evidence.

```text
new Delivery Owner added
≠ old Delivery Owner ended automatically
```

## Role visibility

Not every role must be public to every participant, but consequential actors should not be hidden where disclosure is required.

A customer-facing experience may need to identify:

- Contracting Party;
- Relationship Owner;
- delivery organization;
- external professional provider;
- Professional Authority;
- payment recipient.

The presentation can remain simple while the underlying authority remains explicit.

## Candidate status

The proposed engagement roles are candidate controlled roles, not activated Person, Organization or Workplace types.

Formal admission requires:

- overlap analysis with Membership, Provider, Reviewer and existing authority records;
- exact authority and lifecycle definition;
- conflict and delegation rules;
- cross-book mapping;
- Change Proposal and fixtures.

## Constitutional rule

```text
Roles describe what an actor is responsible or authorized
to do inside a specific governed context.

They must never become permanent labels that silently
grant authority across every customer, Product, Matter or Workplace.
```
