# Chapter 17 — Product Projection and External Experience

A Workplace does not interact with the outside world only through internal screens. Customers, providers, contributors, buyers, sellers and reviewers each need a view of the relevant work. The danger is that external experience is often implemented as a separate portal with duplicated records, improvised permissions and ambiguous authority.

MarkOrbit instead treats an external experience as a Product Projection: a purpose-limited Product-generated view of governed source objects.

## 1. A portal is not a new sovereignty domain

A client portal, provider instruction page, trademark listing page, quotation link or review screen may look like a standalone product. Architecturally, however, it should usually remain a view generated from an existing Workplace and Product Installation.

```text
External page
≠ new Workplace
≠ new owner of the underlying data
≠ new formal-state authority
```

Creating a new sovereignty domain for every portal would fragment responsibility. The same customer, Matter, trademark asset or Engagement would acquire several competing copies and unclear owners.

A Product Projection preserves a single accountable source while adapting the experience for a specific audience.

## 2. Product Projection differs from general Projection

General Projection represents a bounded need, capability, asset or audience. Product Projection is the way a Product turns governed source objects into an external operating experience.

It should record:

- source Workplace;
- source Product Installation;
- source objects and Owning Services;
- intended audience;
- purpose and allowed actions;
- visible fields and documents;
- branding and language configuration;
- authentication method;
- expiry and revocation;
- write-back rules;
- evidence and audit policy.

This makes the external interface accountable to the same authority model as the internal Product.

## 3. External views must be role-specific

Different audiences need different experiences.

### Customer view

A customer may need to:

- review a recommendation;
- approve a filing route;
- upload a document;
- sign or confirm an instruction;
- see status, deadlines and fees;
- receive an Outcome and next-step explanation.

The customer does not need internal margin, competing provider quotations, staff notes or unrelated Workplaces.

### Provider view

A provider may need:

- the formal instruction package;
- appointed role and scope;
- material customer and Matter facts;
- required documents;
- deadlines;
- reporting and evidence obligations;
- escalation channel.

The provider does not automatically need the originating Workplace's entire customer history or private commercial model.

### Contributor view

A bounded contributor may need only a Work Package, evidence subset, acceptance criteria and submission channel.

### Buyer or seller view

A transaction participant may need a listing, request, match rationale, due-diligence package and communication path, with identity disclosed progressively.

## 4. Read access and write-back are separate decisions

An external participant may be allowed to view information without being allowed to change formal state.

```text
View status
≠ update status

Upload document
≠ validate document

Submit response
≠ accept Outcome
```

Write-back should create a typed event such as Customer Approval, Provider Return, Contribution, Document Submission or Change Request. The Owning Service then validates whether and how that event changes formal business state.

This prevents an external page from becoming an uncontrolled second database.

## 5. Branding does not change authority

White-label and co-branded experiences are commercially important. An originating Workplace may want the customer-facing portal to use its own name, domain, language and visual identity.

Branding can change presentation, but it cannot change facts that must be disclosed. A legally required professional representative cannot be hidden merely because the portal is white-labeled. The platform must distinguish:

- commercial brand presented to the customer;
- Relationship Owner;
- Contracting Party;
- Professional Authority;
- Delivery Owner;
- platform or Product operator.

These identities may overlap, but the interface must not create a false representation.

## 6. Product Projection must survive source change

An external view becomes dangerous when it continues showing stale information after the source changes.

The system should detect and handle:

- changed deadlines;
- superseded quotations;
- revoked provider appointment;
- updated applicant or owner;
- replaced documents;
- withdrawn customer approval;
- closed Opportunity or Engagement;
- changed resale authorization.

A Product Projection should refresh, pause or require re-approval when material source fields change.

## 7. Public and private experiences are different

Some Product Projections may be public, such as a concept brand page or trademark listing. Others may be accessible only through invitation, authenticated membership or appointment.

Public visibility requires stronger minimization because the audience is unknown and copying is difficult to control. Private access allows more information, but still only for the declared purpose.

```text
Public Product Projection
≠ unrestricted reuse license
```

Copyright, trademark, customer, asset and data rights remain governed even when a page is publicly visible.

## 8. AI-generated external content

Products may use AI to generate summaries, recommendations, brand concepts, translated instructions or customer explanations. The external experience must disclose the status of that content.

Useful labels include:

- official fact;
- customer-provided statement;
- professional opinion;
- AI-assisted draft;
- concept visualization;
- unverified translation;
- pending review.

For example, a brand incubation page may show packaging and store images, but those images must be clearly presented as concept demonstrations rather than existing commercial facts.

## 9. Failure modes

Product Projection fails when:

- a portal becomes a disconnected copy of source data;
- external users can silently overwrite formal state;
- branding conceals legally relevant identities;
- stale information remains active;
- a public page reveals private customer or pricing information;
- AI-generated text appears as verified professional advice;
- write-back is not tied to an authenticated actor and represented Workplace;
- revocation removes the page but leaves downloadable access uncontrolled.

## 10. Product implications

A Product Projection engine should support:

- audience templates;
- disclosure previews;
- object and field policies;
- branding and localization;
- authentication and invitation;
- typed external actions;
- source-change monitoring;
- expiry, suspension and revocation;
- evidence and audit trails;
- clear authority labels.

The goal is not merely a better portal. It is an external experience that remains part of a governed operating system.

> Product Projection lets a Workplace present the right experience to the right participant without creating a second, unaccountable version of the business.