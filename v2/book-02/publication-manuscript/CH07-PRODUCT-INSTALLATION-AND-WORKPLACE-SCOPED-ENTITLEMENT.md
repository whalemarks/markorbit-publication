# CH07 — Product Installation and Workplace-scoped Entitlement

## A Product is not simply switched on for a user

MarkOrbit Products operate inside Workplaces. They consume shared semantics, project business records, invoke Capabilities and connect to external systems. Treating Product access as a global user flag would ignore the most important operating question:

> In which business context is this Product allowed to act, on which records, under which policy and for whose benefit?

Book 02 therefore distinguishes:

```text
Product
Product Installation
Entitlement
Capability Access
Assignment Authority
```

## Product

A Product is a governed arrangement of capabilities, interfaces, rules, workflows, projections and commercial promises.

Examples include Lite, MarkReg and Sites.

The Product definition may describe:

- intended outcomes;
- supported roles;
- required Core contracts;
- available capabilities;
- default safeguards;
- interoperability requirements;
- commercial edition boundaries.

The Product itself does not own each Workplace’s business records or relationships.

## Product Installation

A Product Installation represents the activation and configuration of a Product inside one Workplace.

It should preserve at least:

- Workplace identity;
- Product and version;
- installation status;
- enabled modules or edition;
- policy profile;
- connector configuration;
- data scopes;
- AI memory policy;
- allowed projections and Handoffs;
- administrative responsibility;
- suspension, migration and removal state.

```text
Product exists on the platform
≠ Product installed in this Workplace
```

One Product may be installed differently across Workplaces. A solo consultant may use Lite without team collaboration. An agency may use Lite and MarkReg with white-label controls. A service provider may use only an MGSN-facing operating surface.

## Installation does not transfer ownership

When MarkReg is installed in an agency Workplace, MarkReg may display Customers, Orders, Matters and Evidence relevant to its service routes. That does not make MarkReg the owner of those relationships or records.

```text
displayed by Product
≠ owned by Product
```

The Product operates through references, Projections, Handoffs and controlled write-backs. The Owning Service and Workplace remain identifiable.

## Entitlement

Entitlement answers whether a Person, Membership, Workplace or represented role may access a Product function or resource.

Entitlement can arise from:

- Product edition;
- Workplace policy;
- Membership role;
- purchased service scope;
- accepted Engagement;
- administrative delegation;
- compliance or jurisdiction restrictions.

Entitlement should be explicit about:

- subject;
- Product Installation;
- resource or function;
- action type;
- scope;
- effective time;
- expiry;
- source of entitlement;
- revocation state.

```text
subscription paid
≠ authority to perform every action
```

A paid edition may unlock collaboration tools, but it cannot create professional qualification, customer consent or filing authority.

## Entitlement is not Assignment

Entitlement grants potential access to a Product function. Assignment authorizes a specific actor to perform bounded work in a specific context.

A reviewer may be entitled to use review tools but still require Assignment to review a particular Work Package. A Workplace administrator may configure MarkReg but lack authority to approve a filing.

```text
Entitlement
≠ Eligibility
≠ Assignment
≠ Approval
```

Book 03 governs the runtime transition from eligible actor to accepted Assignment. Book 02 preserves the distinctions.

## Capability Access

A Product Installation may expose Capabilities. Capability Access defines whether a Capability may be invoked in a Workplace context and under which operating mode.

Capability Access should consider:

- Product policy;
- data scope;
- user role;
- risk tier;
- model or tool availability;
- cost controls;
- privacy restrictions;
- professional authority;
- required Review and Approval.

A Product can expose an AI drafting Capability without granting authority to send the draft or apply it to formal state.

```text
Capability available
≠ protected action authorized
```

## Connector boundaries

Connectors are often the point at which Product configuration becomes consequential.

A connector may access:

- email;
- calendars;
- document stores;
- trademark databases;
- payment services;
- external provider portals;
- public publishing channels.

Connector configuration must remain scoped to the Product Installation and Workplace purpose. Installing a connector for Lite content publishing should not silently permit MarkReg to read private mail or Execution to submit official filings.

```text
connector connected
≠ every Product may use it
≠ every action is authorized
```

## Installation lifecycle

A Product Installation should support:

```text
proposed
→ configured
→ active
→ restricted or suspended
→ migrating
→ removed
```

Removal must address:

- data export;
- active obligations;
- unresolved Work Packages;
- scheduled actions;
- retained evidence;
- connector revocation;
- AI memory disposition;
- customer-facing projections;
- legal retention requirements.

```text
Product removed
≠ history erased
≠ active obligations abandoned
```

## Shadow and pilot modes

A Product may be installed in shadow or pilot mode to observe and recommend without mutating formal state or communicating externally.

Such modes must be explicit. A Product should not be described as operational when it only generates previews.

```text
shadow recommendation
≠ production execution
```

## Constitutional rule

```text
Product defines reusable operating capability.
Product Installation binds it to one Workplace.
Entitlement permits bounded access.
Assignment authorizes specific work.
Approval authorizes a specific consequential transition.
```

This separation allows Products to be reusable across the platform without turning installation, payment or visibility into unlimited authority.