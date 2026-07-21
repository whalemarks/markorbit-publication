# Part V — Product Installation and Dynamic Experience

## Chapter 58 — Product is not Workplace

A Product is a reusable operating system component designed for a defined audience and outcome.

A Workplace is the business context in which a Product operates.

```text
Product
≠ Workplace

Product Installation
= Product configured and authorized for one Workplace
```

The distinction allows a shared product to support many Workplaces without claiming ownership of their business records.

## Chapter 59 — Product Installation

A Product Installation should record:

- Product identity and edition;
- lifecycle status;
- enabled capabilities;
- entitlement;
- role mappings;
- data-access scope;
- configuration version;
- projection policy;
- connector policy;
- audit reference;
- activation and retirement context.

A shared multi-tenant implementation may host many Product Installations while maintaining distinct Workplace authority.

## Chapter 60 — Installation lifecycle

A Product Installation may move through:

```text
proposed
→ configured
→ trial
→ active
→ restricted
→ suspended
→ retired
→ archived
```

Activation should verify required permissions, data routes, configuration and policy.

Retirement should address export, pending work, projection withdrawal and connector shutdown.

## Chapter 61 — Capability entitlement

A Product Installation does not automatically enable every platform capability.

Entitlement may depend on:

- subscription edition;
- Workplace type and jurisdiction;
- professional qualification;
- security posture;
- completed onboarding;
- contractual scope;
- production authorization;
- technical readiness.

Entitlement controls availability. It does not replace per-action permission and review.

## Chapter 62 — Dynamic home experience

Different Workplaces should not be forced into one static dashboard.

A marketing-oriented Workplace may prioritize:

- content production;
- campaigns;
- leads;
- trademark promotion;
- transaction opportunities.

A capability-oriented Workplace may prioritize:

- available tasks;
- reviews;
- training;
- certification;
- capacity and earnings.

A service-delivery Workplace may prioritize:

- deadlines;
- Matters;
- customer communication;
- provider returns;
- quality exceptions.

Dynamic experience should remain explainable and user-configurable.

## Chapter 63 — Product composition

A Workplace may use several Products together.

```text
Lite
→ customer growth and trademark commerce

MarkReg
→ full lifecycle service delivery

Sites
→ public brand and content projection

MGSN Connection
→ formal external professional fulfillment
```

Products should exchange typed Handoffs and Returns rather than share unrestricted internal state.

## Chapter 64 — Lite Installation

A Lite Installation may enable:

- Today;
- Content Studio;
- customer and opportunity context;
- trademark inventory;
- resale authorization;
- trademark requests;
- matching;
- inquiry and transaction pipeline;
- capability center;
- contribution tasks;
- handoff into MarkReg.

The Installation may adapt to an individual professional or a small team.

## Chapter 65 — MarkReg Installation

A MarkReg Installation may operate in several modes:

- self-operated direct service;
- partner Workplace white-label production;
- co-delivery;
- enterprise internal service;
- supervised training or shadow production.

The operating mode must be explicit because customer relationship, branding, payment and delivery responsibility differ.

## Chapter 66 — Sites Installation

Sites is a public-brand and content projection Product.

It may govern:

- domain and brand;
- page structure;
- service pages;
- cases and FAQs;
- public trademark listings;
- lead forms;
- widgets;
- publication version.

Sites is not the Owning Service for Customer, Order, Matter, Payment or professional decision records.

## Chapter 67 — Client-facing projection

A client portal or public interaction surface may be projected from Lite or MarkReg.

It can support:

- intake;
- upload;
- decision confirmation;
- status viewing;
- document requests;
- quotation approval;
- result delivery.

A client projection does not become an independent Workplace merely because it has a separate interface.

## Chapter 68 — Product-local state

Some state belongs to the Product Installation rather than Core.

Examples include:

- UI preferences;
- content templates;
- campaign settings;
- dashboard layout;
- local drafts;
- product-specific recommendation state;
- onboarding progress.

Product-local state must not redefine shared business semantics.

## Chapter 69 — Handoff between Products

A Product Handoff should preserve:

- source Product Installation;
- destination;
- Workplace context;
- purpose;
- permission;
- minimum required data;
- version;
- pending and accepted states;
- provenance.

For example, a Lite transaction inquiry may hand off to a MarkReg transfer service without giving MarkReg unrestricted access to all Lite contacts.

## Chapter 70 — Return validation

A Return from another Product or network is a candidate outcome.

```text
Return received
≠ accepted formal truth
```

The destination must validate the Return under its own permissions, Core semantics and Owning Service rules.

## Chapter 71 — Configuration inheritance

Configuration may exist at several levels:

```text
platform default
→ Product default
→ Organization policy
→ Workplace policy
→ Product Installation configuration
→ role preference
→ user preference
```

A lower level may narrow authority but should not silently broaden a higher-level prohibition.

## Chapter 72 — Product freedom and constitutional locks

Products should evolve quickly, but some rules remain constitutional:

- customer relationship does not transfer silently;
- AI does not create formal truth by itself;
- Product state does not bypass Owning Services;
- cross-Workplace access requires purpose and permission;
- external professional actions require qualification and governance;
- evidence retains provenance.

These locks let products innovate without fragmenting the operating system.
