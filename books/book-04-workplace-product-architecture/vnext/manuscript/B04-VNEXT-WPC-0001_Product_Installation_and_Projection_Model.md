# B04-VNEXT-WPC-0001 — Product Installation and Projection Model

## Status

```text
Book 04 vNext Amendment Manuscript
WP-C Candidate
RC1 source remains unchanged
```

## Amendment rule

For the chapters listed in `B04-CORR-0002`, this document supplies the controlling vNext interpretation after Owner merge.

```text
RC1 text
+ accepted WP-B amendment
+ accepted WP-C amendment
= current Book 04 vNext interpretation for covered scope
```

---

## 1. Product participation is a governed relationship

A Product is not made part of a Workplace merely because a link, menu item, feature flag or shared login exists.

The authoritative participation relationship is **Product Installation**.

```text
Product Installation
= Workplace-scoped Product identity
+ entitlement
+ configuration
+ permission
+ activation state
+ authorized context scope
+ projection scope
+ Handoff / Return rules
```

Product Installation is architectural identity. It may later be implemented through configuration records, deployment descriptors, service contracts or other mechanisms, but it must not be reduced to any one implementation technique.

A Product Installation does not by itself create:

- a new Organization;
- a new Workplace;
- a new database;
- a new tenant;
- a new Owning Service;
- formal-state mutation authority;
- ownership of Workplace data;
- unrestricted access to all Workplace context.

---

## 2. Product, Installation and Projection are distinct

### Product

The Product defines its focused value proposition, journeys, Product-local concepts and governed responsibilities.

### Product Installation

The Installation defines how that Product participates in one Workplace.

The same Product may have different Installations in different Workplaces. Each Installation may differ in entitlement, configuration, users, permissions, enabled capabilities and projection scope.

### Product Projection

A Projection is a purpose-limited representation or interaction surface derived from authorized context.

Examples include:

- a Product panel inside Workplace;
- a client-facing status view;
- a Today card;
- a portfolio summary;
- an Artifact preview;
- a returned outcome shown in an originating Product.

```text
Product ≠ Product Installation ≠ Product Projection
```

A Projection does not acquire the authority of the source merely because it displays source-derived information.

---

## 3. Entitlement is not authority

Entitlement answers whether a Workplace may use a Product or capability under an applicable commercial, policy or administrative basis.

Entitlement does not answer whether a specific user may view a specific record, approve a decision or mutate formal state.

```text
Entitled Product
≠ authorized user
≠ authorized record scope
≠ formal-state authority
```

A conforming Installation evaluates all of these separately:

1. Product entitlement;
2. Installation activation;
3. user membership and role;
4. Workplace permission;
5. record or context scope;
6. Product policy;
7. Human Review requirements;
8. Owning Service authority.

---

## 4. Configuration is bounded

Installation configuration may determine:

- enabled modules;
- default views;
- permitted workflows;
- notification preferences;
- client-facing projection settings;
- approved templates;
- integration endpoints;
- Handoff destinations;
- Return acceptance policies.

Configuration cannot silently redefine Core meaning, alter Owning Service responsibility or expand access beyond Workplace policy.

```text
Configuration may specialize use.
Configuration may not redefine authority.
```

---

## 5. Projection is purpose-limited

Every Projection must be explainable through:

```text
source authority
→ authorized context
→ projection purpose
→ permitted audience
→ permitted interaction
→ expiry or revocation rule
```

A Projection may be read-only or interactive. Interaction does not imply direct mutation of the projected source.

An interactive projection may prepare a request, candidate, review or Handoff. The appropriate Owning Service still controls formal mutation.

Examples:

```text
Displayed deadline ≠ authority to change deadline
Editable recommendation ≠ approved professional decision
Visible payment status ≠ Finance ledger authority
Client approval button ≠ completed filing
```

---

## 6. Projection, Handoff and Return form different contracts

### Projection

Projection makes authorized context visible or interactable without transferring responsibility.

### Handoff

Handoff transfers typed context toward another Product, Service or Workplace boundary for a stated purpose.

A Handoff must identify:

- originating context;
- destination;
- purpose;
- payload type;
- authority and provenance;
- permitted use;
- required acceptance;
- expiry or revocation;
- audit identity.

```text
Handoff sent ≠ destination accepted
Destination accepted ≠ action completed
```

### Return

Return brings a typed outcome, Evidence, Artifact, status or exception back to an originating context.

A Return must identify:

- originating Handoff or request;
- returning authority;
- returned payload type;
- provenance;
- completeness and confidence;
- acceptance requirements;
- whether further review or formalization is required.

```text
Return received ≠ accepted as truth
Return accepted ≠ formal-state mutation
```

---

## 7. Cross-Product continuity preserves authority

Cross-Product continuity is not achieved by copying all data into every Product.

It is achieved by preserving:

- stable identity references;
- source authority;
- originating Workplace;
- Installation identity;
- purpose-limited context;
- provenance;
- permission scope;
- Handoff and Return history;
- Artifact lineage.

A Product may maintain Product-local records for its own journey. Those records must not silently become duplicate authority for Customer, Matter, Task, Communication, Finance, official lifecycle or other formally owned facts.

---

## 8. Artifact continuity

Artifacts may move across Products through Projection, Handoff and Return while retaining a single provenance chain.

A conforming Artifact reference records:

```text
originating Workplace
originating Product Installation
author or generating capability
source context
version
review state
approval state
Handoff history
Return history
formalization status
```

Rendering or editing an Artifact in another Product does not erase its origin or automatically transfer ownership.

---

## 9. Outcome and feedback return

An outcome may be displayed in several Products, but its formal authority remains with the source that produced or recorded it.

Returned outcomes may require:

- validation;
- Human Review;
- conflict checking;
- reconciliation;
- acceptance;
- formalization by an Owning Service.

Feedback may improve Product experience or capability evidence, but it must not silently change a formal business record or universal Trust state.

---

## 10. Chapter correction modules

### CH20 — Product Architecture Principles

Add the rule that Product independence is preserved through explicit Installation rather than assumed embedding. Product design must declare the authority it consumes, the projections it exposes and the Handoff/Return contracts it supports.

### CH21 — Product Independence and Shared Foundations

Clarify that shared foundations create interoperability, not shared ownership. A Product consumes Core semantics and governed services without acquiring their authority.

### CH22 — Product Embedding and Cross-Product Context

Replace generic embedding language with Product Installation and Product Projection. An embedded surface is a projection of an installed Product, not evidence that Product and Workplace are one system.

### CH26 — Workplace Editions and Organization-Specific Applications

Treat editions as controlled combinations of entitlement, configuration and projection defaults. Editions do not create different constitutional authority models.

### CH27 — Cross-Product Handoffs and Lifecycle Continuity

Require typed Projection, Handoff and Return. Context continuity must retain provenance, purpose and authority rather than relying on unrestricted shared access.

### CH30 — Artifact Lifecycle, Versioning and Provenance

Add originating Workplace and Product Installation identity to Artifact provenance. Cross-Product editing creates a new governed version, not an untracked copy.

### CH31 — Render, Edit, Delivery and Publish

Clarify that render and edit surfaces are projections unless the appropriate service records a governed transformation or formalization. Delivery and Publish remain separate authority-bearing acts.

### CH32 — Formalization, Outcome and Feedback

Require typed Return and explicit acceptance. Returned outcomes do not mutate formal state until the appropriate authority validates and records them.

### CH38 — Conformance and Future Architecture Specifications

Conformance evidence must show Installation identity, entitlement, activation, permission, projection scope, Handoff contracts, Return contracts, provenance and revocation behavior.

---

## 11. Conformance lock

A future implementation cannot claim Book 04 vNext conformance merely because Products share authentication or data storage.

It must demonstrate:

```text
Product identity: explicit
Installation identity: explicit
Workplace scope: explicit
Entitlement: explicit
Configuration: bounded
Permissions: explicit
Projection scope: purpose-limited
Handoff acceptance: explicit
Return acceptance: explicit
Formal mutation authority: preserved
Provenance: retained
Revocation: supported
```

---

## 12. Non-authorization

This amendment does not authorize schemas, APIs, deployment, production access, automatic action, public distribution or External Protected Action.
