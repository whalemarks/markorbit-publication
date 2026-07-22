# Chapter 02 — Product, Service and Operating Model

MarkReg is easy to misunderstand because the name can refer to several related things.

A user may mean the software they open each day. A partner may mean the standardized service it purchases. An internal team may mean the operating method used to deliver trademark work. A customer may mean the service brand that accepts responsibility for a complete outcome.

These meanings belong together, but they cannot be collapsed.

The current architecture requires a layered model:

```text
MarkReg Product
→ reusable trademark-service capability

MarkReg Product Installation
→ MarkReg enabled and configured inside a Workplace

MarkReg service catalog
→ defined Outcomes, scopes, exclusions and commercial terms

MarkReg operating model
→ production, review, external fulfillment, evidence and recovery pattern

MarkReg-operated Workplace
→ self-operated business organization that may contract and deliver directly
```

The distinction determines who owns the customer relationship, who contracts, who receives payment, who bears delivery responsibility and who has professional authority.

## 1. MarkReg is first a focused Product

The Product organizes international trademark work across:

- need and decision readiness;
- search and risk;
- filing preparation;
- external filing;
- prosecution and response;
- registration and certificate handling;
- maintenance and renewal;
- recordal and transactions;
- portfolio continuity.

It provides Product-local state such as:

- recommendation sessions;
- question progression;
- option comparison;
- intake progress;
- missing-information views;
- preparation status;
- Jurisdiction Pack selection;
- Product resume state;
- customer-facing lifecycle projections.

This state exists to operate the MarkReg journey. It does not automatically become shared Core state.

```text
Useful Product state
≠ new canonical object automatically
```

## 2. A Product Installation belongs to a Workplace

A Product does not operate in an organizational vacuum.

A MarkReg Product Installation is enabled within a specific Workplace. The installation inherits and configures:

- acting organization;
- Membership and roles;
- customer relationships;
- private Knowledge;
- language and brand presentation;
- service catalog;
- pricing and approval rules;
- internal capabilities;
- Provider preferences;
- AI and data policies;
- external integrations;
- audit and retention.

The same MarkReg Product may be installed in multiple Workplaces without combining their customers, pricing, memory or authority.

A person may participate in several Workplaces. Their MarkReg access and role derive from the active context.

```text
Person can use MarkReg in Workplace A
≠ Person can access MarkReg data in Workplace B
```

## 3. The Product is not the Workplace

Earlier descriptions sometimes treated MarkReg as simultaneously a Product Installation and a self-operated Workplace. The commercial intention was understandable: MarkReg needs a direct service operation that can prove the model and serve customers.

The current architecture draws a sharper boundary.

```text
MarkReg Product
≠ MarkReg-operated Workplace
```

The Product supplies reusable capability. The Workplace is the business-sovereignty and Product-operation boundary.

A MarkReg-operated Workplace may:

- acquire and serve customers directly;
- become Relationship Owner;
- become Contracting Party;
- receive payment;
- employ or engage delivery personnel;
- purchase Provider services;
- bear Delivery responsibility;
- manage complaints and recovery.

Those roles arise from the Workplace's business and contractual position, not from the Product's existence.

## 4. MarkReg is also a standardized service catalog

A Product feature tells the user what the system can do. A service catalog tells the customer or partner what Outcome is offered under which conditions.

A service catalog may define:

- service name;
- jurisdiction and lifecycle stage;
- included and excluded work;
- assumptions;
- required customer inputs;
- professional review level;
- expected external route;
- official and Provider cost treatment;
- delivery evidence;
- later-stage fees;
- validity and change conditions.

Examples include:

- status and deadline verification;
- preliminary search review;
- new application preparation and filing;
- office-action response coordination;
- declaration or renewal;
- ownership recordal;
- transfer due diligence;
- certificate validation;
- portfolio maintenance monitoring.

The catalog should prevent a customer from mistaking one bounded output for complete lifecycle responsibility.

## 5. Service scope needs an Outcome definition

A service should identify what successful delivery means.

“Trademark filing” can mean several different Outcomes:

- a reviewed package ready for submission;
- instruction accepted by a local Provider;
- submission reported by the Provider;
- official filing receipt obtained;
- formalities passed;
- registration completed.

The service description should state which Outcome is included and what evidence supports completion.

```text
Work performed
≠ promised Outcome achieved

Provider instructed
≠ official filing acknowledged
```

Where the service includes only preparation or coordination, that limit should be visible before the customer accepts the quotation.

## 6. The operating model connects many production sources

MarkReg may assemble an Outcome from:

- internal staff;
- deterministic systems;
- governed AI assistance;
- certified Contributors;
- expert Reviewers;
- external professional Providers;
- connectors;
- official sources.

The customer should not need to coordinate this supply chain.

The Product must preserve:

- who performed each Work Package;
- who reviewed it;
- who approved the consequence;
- which Provider accepted external work;
- what evidence returned;
- which Owning Service validated formal state;
- who remains responsible for customer delivery.

Unified service should reduce customer complexity, not erase internal accountability.

## 7. Product, production and professional authority remain distinct

MarkReg can prepare a filing package through software and distributed production. The final external action may still require a qualified professional.

```text
Product capability
≠ production eligibility
≠ Professional Authority
≠ external execution permission
```

The operating model should distinguish:

- AI generation;
- deterministic validation;
- Contributor preparation;
- professional Review;
- customer confirmation;
- commercial approval;
- filing approval;
- Provider appointment;
- external submission;
- official acknowledgement.

Combining several steps into one interface does not combine their authority.

## 8. MarkReg depends on surrounding architecture

MarkReg is a flagship Product, not an isolated system.

### Workplace

Supplies the authorized business context, relationship ownership, roles, private Knowledge, pricing and Product configuration.

### Core

Defines shared semantic authority for Organization, Customer, Trademark, Order, Matter, Task, Document, Evidence, Communication, Permission, Policy and related objects.

### Governed execution

Coordinates Workflows, Work Packages, Assignments, Reviews, approvals, retries, idempotency, Events and protected actions.

### Owning Services

Create and change formal business state such as Customer, Order, Matter, payment, appointment or validated trademark-service state.

### MGSN Connection / Gateway

Allows a Workplace to request managed external fulfillment under its configured policies.

### MGSN Network

Maintains Provider eligibility, routing, fulfillment evidence and recovery across the managed network.

### Official sources

Create official procedural records and outcomes.

MarkReg composes the user experience across these boundaries while respecting their authority.

## 9. Live reference, snapshot, Projection and candidate

The Product may display several representations of one underlying subject.

| Representation | Use | Authority |
|---|---|---|
| live reference | current formal object from an Owning Service | remains with the Owning Service |
| snapshot | historical context used for a Decision or Review | fixed to source and time |
| Product Projection | MarkReg-facing interpretation of another state | informative and revocable |
| candidate | proposed information awaiting acceptance | provisional |
| cache | technical copy for performance | no independent business authority |

A formal applicant record may be referenced live. A quotation preserves a snapshot of that applicant context. An AI extraction may create a candidate correction. A customer-facing page may show a Product Projection.

These representations should not silently overwrite each other.

## 10. Product access does not create a service relationship

A Workplace may install MarkReg for internal preparation without purchasing a direct MarkReg service.

A partner may use:

- software only;
- bounded capability fulfillment;
- white-label production;
- co-delivery;
- complete direct service;
- MGSN-supported fulfillment.

```text
Product access
≠ service Engagement

Service Engagement
≠ customer relationship transfer
```

The system should know whether a current action is ordinary Product use, accepted internal work, a paid professional service or an external Engagement.

## 11. The self-operated Workplace is necessary but bounded

A direct MarkReg operation provides several strategic benefits:

- real customer demand;
- proof of lifecycle design;
- operational evidence;
- failure and recovery cases;
- Provider performance data;
- Capability evidence;
- commercial learning;
- reference implementations.

It also creates risks:

- partner fear that the platform will take customers;
- hidden preference for self-operated service;
- cross-Workplace data leakage;
- centralization of all commercial relationships;
- confusing Product administration with service authority.

The MarkReg-operated Workplace should therefore remain an explicit independent Workplace with its own:

- customer relationships;
- contracts;
- pricing;
- people;
- permissions;
- Matter and delivery responsibilities;
- financial records;
- complaint and recovery process.

Platform administration does not grant that Workplace unrestricted access to partner Workplaces.

## 12. Standardization should improve reliability, not erase jurisdiction

MarkReg needs a stable Product model across countries. International trademark law and practice remain diverse.

The operating pattern is:

```text
Stable Product constitution
+ service-specific lifecycle
+ versioned Jurisdiction Pack
+ sourced Knowledge
+ professional ownership
+ controlled change
```

A Jurisdiction Pack may define:

- supported services;
- required questions;
- filing basis;
- goods rules;
- documents;
- forms;
- official fees;
- local Provider requirements;
- deadlines;
- post-registration obligations.

It does not create official law and should not imply support for lifecycle stages not actually covered.

```text
New-filing support
≠ opposition support
≠ renewal support
≠ transaction support
```

## 13. The operating model must support honest non-automation

Some work can be standardized, automated or sampled. Other work depends on qualified judgment.

Automation may be appropriate for:

- data normalization;
- field validation;
- version comparison;
- deadline candidate generation;
- document completeness checks;
- duplicate detection;
- status retrieval;
- template rendering.

Human or professional judgment may be required for:

- applicant and ownership ambiguity;
- substantive search risk;
- complex goods strategy;
- use-evidence sufficiency;
- response strategy;
- dispute or settlement;
- abandonment;
- Provider selection under conflict;
- legal effect of a mark variation.

A mature operating model knows where not to automate.

## 14. Product metrics must follow the operating promise

Useful metrics include:

- time to first useful option;
- unresolved assumption visibility;
- intake deficiency rate;
- package rework;
- professional Review revisions;
- duplicate-action prevention;
- Provider acceptance and evidence-return reliability;
- unknown-state duration;
- missed deadline or document incidence;
- maintenance continuity;
- customer surprise and complaint rate.

Metrics should not reward:

- reduced questions through missing facts;
- faster filing through weaker Review;
- higher conversion through biased recommendations;
- completion labels without evidence;
- automatic use of an affiliated service;
- Provider routing without acceptance.

## 15. Product boundaries protect commercial trust

MarkReg is not:

- a second Workplace;
- a second Core;
- a duplicate generic execution system;
- an open Provider marketplace;
- an autonomous law firm;
- an official registry;
- a universal all-IP Product;
- a final implementation specification.

These boundaries do not make MarkReg smaller. They let the Product become deep in the lifecycle it actually owns.

## 16. A practical example

A Chinese trademark agency installs MarkReg in its own Workplace.

It uses the Product for:

- customer intake;
- country and class recommendations;
- package preparation;
- internal professional Review;
- external Provider instructions;
- status and evidence return.

The agency remains Relationship Owner and Contracting Party. Its customer sees the agency's brand. MarkReg supplies software and defined production capabilities. A US attorney acts as Professional Authority for the US filing. The Matter state remains in the relevant Owning Service.

Separately, a customer may approach the MarkReg-operated Workplace directly. That Workplace becomes Relationship Owner and Contracting Party for the direct service. It may use the same Product and Provider network, but the customer and commercial records remain separate from the agency's Workplace.

The shared Product does not create shared customers.

## 17. Product and technical implications

The architecture requires:

- Workplace-scoped Product Installations;
- separate entitlement and authority checks;
- Product-local journey state;
- references to shared formal objects;
- typed service catalog and Outcome definitions;
- role and relationship records;
- provider and Contributor separation;
- versioned Jurisdiction Packs;
- configurable branding and communication;
- white-label and co-delivery policies;
- typed Handoff and Return;
- evidence-backed completion;
- isolation of self-operated and partner Workplaces.

## 18. Commercial implications

MarkReg can support multiple revenue models:

- Product subscription;
- direct professional-service margin;
- white-label production fees;
- co-delivery fees;
- bounded capability fees;
- managed external fulfillment;
- lifecycle monitoring;
- transaction services;
- premium Review.

Each charge should identify the responsible role and scope.

The commercial portfolio should reinforce Product adoption without making self-operated service a hidden mandatory route.

## 19. The chapter lock

```text
MarkReg Product
≠ MarkReg-operated Workplace

Product access
≠ service Engagement

Service Engagement
≠ customer relationship transfer

Unified delivery
≠ centralized authority
```

> MarkReg becomes scalable when the Product, service catalog, production system and self-operated business reinforce one another while remaining distinct enough that every customer, partner and professional can see who is responsible for what.