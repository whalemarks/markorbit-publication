# MO-ARCH-SRC-001 — Workplace Sovereignty Draft Input Assessment

## Status

```text
Controlled Architecture Input Assessment
Ready for Owner Review
```

## Purpose

This record evaluates three owner-supplied Workplace sovereignty drafts as architecture inputs. The drafts contain substantial corrections to the current architecture baseline, but they also preserve older Lite and MGSN assumptions that must not be accepted without qualification.

The drafts are treated as source material, not as automatically accepted Canon.

## Source Set

The reviewed source set contains:

1. a comprehensive Workplace sovereignty, Product projection, distribution and direct-service-routing ADR draft;
2. a shorter Workplace sovereignty and Product projection ADR draft;
3. a product-positioning note describing Workplace as the Partner's independent business sovereignty space.

## Classification Method

Each significant proposition is classified as:

```text
KEEP
REFRAME
MOVE TO PRODUCT BOOK
MOVE TO DISTRIBUTION GOVERNANCE
MOVE TO MGSN CHARTER
DEFER
REJECT
```

## A. Propositions to KEEP

### A1 — Workplace is a business-sovereignty boundary

```text
Workplace
= Organization-owned operating boundary
for business records, people, permissions,
Product Installations, projections and accountability
```

This is the central correction required by the current Canon.

### A2 — Physical hosting is not business ownership

```text
storage provider ≠ business owner
platform operator ≠ customer owner
shared capability provider ≠ owner of concrete business facts
```

### A3 — Core owns shared semantics and capabilities, not every concrete business record

Core may define schemas, states, rules, Packs, algorithms, permissions, audit and connector protocols without becoming the business owner of each Customer, Order, Matter, Document or Communication instance.

### A4 — MarkReg self-operated business is a Workplace

MarkReg self-operated business must run inside its own Organization and Workplace boundary and must not receive default access to Partner Workplace data merely because the platform operates MarkReg.

### A5 — Product Installation is a first-class architecture relationship

MarkReg, Lite, Sites and future Products must have explicit Workplace-scoped installation, configuration, entitlement, access and audit context.

### A6 — Projection does not silently change ownership

Public, customer-facing and network projections expose bounded views or actions without silently changing the ownership of source records.

### A7 — Default isolation and purpose-limited cross-Workplace access

Cross-Workplace access requires explicit purpose, scope, recipient, duration, permission, revocation and audit.

### A8 — Portable sovereignty

Organizations must be able to export the business records, content and configurations they own, subject to legal retention and shared-platform restrictions.

### A9 — Sites is a Workplace public projection Product

Sites content and configuration belong to the Workplace. Sites does not become the authoritative Customer, Order or Matter system.

### A10 — Cross-Workplace collaboration uses governed Handoff and Return

Collaboration must not rely on unrestricted bilateral database access.

## B. Propositions to REFRAME

### B1 — Workplace as a container

The drafts sometimes describe Workplace as if it directly owns every Product-specific record by itself.

Reframe as:

```text
Workplace
= default business ownership and accountability boundary

Owning Service / Product
= formal state authority within that Workplace boundary
```

Workplace sovereignty must not collapse Owning Service authority.

### B2 — Concrete record ownership

Avoid saying every record is simply “owned by Workplace” without distinguishing:

- business ownership and accountability;
- semantic authority;
- formal state mutation authority;
- physical custody;
- source rights;
- legal or official authority.

### B3 — Product Installation

Installation does not mean each Workplace receives separate code, database or deployment.

It means a governed Workplace-scoped Product relationship, which may be delivered through shared multi-tenant infrastructure.

### B4 — Provider Relationship

A Workplace may own private history, preference and external-route context concerning providers. It does not own the platform MGSN provider pool, procurement terms, platform Trust or routing infrastructure.

### B5 — MGSN Node

Replace broad `Workplace-owned MGSN Node` language with:

```text
Workplace-owned or controlled:
- MGSN connection configuration;
- authorized demand projection;
- authorized supply projection;
- private preferences and history;
- received Return projections.

Platform-owned or governed:
- MGSN network;
- admitted provider supply;
- Capability Profiles;
- procurement;
- matching and routing;
- funds and fulfillment controls;
- platform Trust;
- network operating data.
```

### B6 — Direct-to-executor routing

Keep the no-hidden-rebrokering objective, but do not assume every service can always use one legally final entity.

The accepted principle should be:

```text
No undisclosed or ungoverned rebrokering.
Every material execution participant must be disclosed,
authorized and responsibility-mapped.
```

### B7 — Customer ownership

Use `business relationship and record authority` rather than absolute legal ownership where privacy, professional privilege, applicant rights or statutory duties create separate rights.

## C. MOVE TO PRODUCT BOOK

### C1 — Detailed Lite screens and client functions

The draft's client-facing Lite features belong in Book 06 or a future Lite edition, not in the architecture ADR.

### C2 — Sites component library and publishing implementation

Static-first publishing, Design System as Data, components, CDN and Widget SDK belong in the future Sites Product Book and implementation specifications.

### C3 — MarkReg detailed lifecycle

The ADR should state MarkReg's installation and ownership boundaries, while Book 05 retains lifecycle detail.

## D. MOVE TO DISTRIBUTION GOVERNANCE

The following belong in a separate Distribution Product or commercial-governance record:

- Relationship Distributor;
- Traffic Affiliate;
- referral links and codes;
- attribution;
- commission rules and ledgers;
- campaign conversion;
- payout and reversal;
- channel protection.

They are important, but they should not dominate the Workplace sovereignty ADR.

## E. MOVE TO MGSN CHARTER

The following should be controlled by Book 07 after the upstream ADR is accepted:

- participant demand and supply roles;
- multi-provider supply portfolios;
- procurement strategy;
- route recommendation and bounded choice;
- funds control;
- fulfillment and replacement;
- provider admission and suspension;
- Relationship Provenance;
- direct execution and disclosed sub-execution;
- non-circumvention;
- MGSN platform ownership.

## F. DEFER

Defer pending legal, accounting or implementation review:

- legal meaning of business-data ownership;
- funds custody and regulated payment roles;
- data deletion versus retention;
- export of platform-derived Trust and procurement data;
- private deployment obligations;
- exact ProductInstallation schema;
- exact cross-Workplace API model;
- self-operated MarkReg legal role by service category.

## G. Propositions to REJECT

### G1 — Lite is only a client-facing projection

Rejected because the accepted Book 06 direction defines Lite as a lightweight Workplace Product for independent professionals and small teams, with an optional client-facing projection.

### G2 — Each Workplace owns its own MGSN network

Rejected. A Workplace owns its connection and authorized projections, not the platform provider supply, procurement system, routing logic, funds controls or platform Trust.

### G3 — MGSN is a peer-to-peer network of Workplace-owned nodes

Rejected for the current Book 07 direction. MGSN is a platform-owned and platform-governed hub through which participating Workplaces connect.

### G4 — Projection alone authorizes formal state transfer

Rejected. Projection provides visibility or bounded interaction; Handoff, acceptance and Owning Service rules govern formal collaboration state.

### G5 — Core semantic ownership implies concrete-record business ownership

Rejected.

## Source Assessment Decision

```text
Workplace sovereignty correction: REQUIRED
Core capability / business ownership separation: REQUIRED
Product Installation relationship: REQUIRED
MarkReg self-operated Workplace: REQUIRED
Sites public projection: SUPPORTED
Lite-only-client interpretation: REJECTED
Workplace-owned MGSN network: REJECTED
Platform-owned MGSN with Workplace connections: REQUIRED
Distribution detail inside this ADR: MOVE OUT
```

## Gate

This source assessment supports preparation and Owner review of `MO-ADR-WSP-001`.

It does not amend the Architecture Canon, Books 02–07, Product specifications or implementation by itself.
