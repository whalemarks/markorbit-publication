# MO-ARCH-IMP-001 — Workplace Sovereignty Impact on Books 02–07

## Status

```text
Architecture Impact Assessment
Ready for Owner Review
```

## Purpose

This assessment determines how `MO-ADR-WSP-001` would affect the accepted architecture and Books 02–07.

It does not silently reopen frozen books or authorize manuscript changes.

## Classification

```text
NO CHANGE
CLARIFICATION
NEXT-VERSION CORRECTION
UPSTREAM CONFLICT
REQUIRES CONTROLLED RECORD
```

## Executive Result

| Authority | Classification | Summary |
| --- | --- | --- |
| Architecture Canon vNext | UPSTREAM CONFLICT / REQUIRES CONTROLLED RECORD | Workplace and MGSN definitions require amendment candidate |
| Book 02 | CLARIFICATION / POSSIBLE CHANGE PROPOSAL | Core semantic authority must be separated from concrete-record business ownership |
| Book 03 | CLARIFICATION | Execution remains valid but must carry Workplace and Product context |
| Book 04 | NEXT-VERSION CORRECTION | Workplace definition and Product architecture are materially incomplete |
| Book 05 | NEXT-VERSION CLARIFICATION | MarkReg remains valid; self-operated and Partner operations need Workplace framing |
| Book 06 | CLARIFICATION | Lite remains a lightweight Workplace Product; client projection is secondary |
| Book 07 | UPSTREAM DEPENDENCY / REQUIRES RECONCILIATION | Charter must inherit corrected Workplace/MGSN boundary |

## 1. Architecture Canon vNext

### Current strength

The Canon already states:

- each Organization Workplace is an independent Orbit;
- organizations retain clients, data, knowledge, rules, pricing, relationships and autonomy;
- Workplace is the ecosystem's primary operating unit;
- products and networks consume authorized Workplace context.

### Current deficiency

The Canon describes Workplace as a unified professional operating environment and platform shell, but does not explicitly establish:

- business sovereignty and concrete-record accountability;
- Product Installation;
- projection as a separate concept;
- five authority dimensions;
- MarkReg self-operated Workplace;
- Lite's operating/Product identity versus client projection;
- MGSN connection versus platform network ownership.

The Canon also says MGSN connects Workplaces and begins with private partners, which can conflict with the accepted Book 07 direction that MGSN resources, procurement, routing, funds and network Trust are platform-owned or governed.

### Classification

```text
UPSTREAM CONFLICT
REQUIRES CONTROLLED RECORD
```

### Required action after ADR acceptance

Create a Canon Amendment Candidate. Do not edit the Canon in the ADR task itself.

## 2. Book 02 — Core

### What remains valid

- Core defines shared semantics, controlled records, services and contracts.
- Core definitions remain authoritative.
- formal semantic changes require the existing Change Proposal process.

### Required clarification

Book 02 must distinguish:

```text
canonical type authority
≠ concrete-record business ownership
```

For example:

- Core may define `Customer`, while a concrete Customer relationship belongs to a Workplace context;
- Core may define `Matter`, while formal state is owned by an Owning Service and business responsibility is scoped to a Workplace;
- Core may define `Document`, while source rights and business custody remain contextual.

### Risk

A poorly worded correction could incorrectly make Workplace the semantic owner or bypass Owning Services.

### Classification

```text
CLARIFICATION
POSSIBLE BOOK 02 CHANGE PROPOSAL
```

### Required record

A later Book 02 Change Proposal should be created only if the accepted ADR changes semantic ownership or adds shared types such as `ProductInstallation` to Core.

## 3. Book 03 — Execution

### What remains valid

Execution still governs:

- Workflow;
- authority;
- Human Review and Approval;
- protected actions;
- audit;
- failure and retry;
- formal state mutation.

### Required clarification

Execution context must include:

- authenticated Workplace;
- Product Installation or calling Product;
- source and destination Workplace for cross-boundary collaboration;
- purpose and projection scope;
- Handoff and Return authority.

### Classification

```text
CLARIFICATION
```

No immediate Book 03 manuscript correction is required if existing Execution contracts can carry this context.

## 4. Book 04 — Workplace and Product Architecture

### Material issue

Book 04 is the main affected publication.

The current Workplace definition is too weak if it treats Workplace primarily as:

- an operating environment;
- a collaboration shell;
- organizational context;
- a Product access surface.

It must be upgraded to:

```text
Organization-scoped business sovereignty,
accountability, permission, Product operation
and projection boundary
```

### Required next-version additions

- business sovereignty and accountability;
- concrete-record boundary;
- five authority dimensions;
- Product Installation;
- Product Entitlement and configuration;
- Projection;
- MarkReg self-operated Workplace;
- Sites public projection;
- Lite operating Product plus client projection;
- MGSN connection versus MGSN network;
- portable sovereignty;
- cross-Workplace purpose grants;
- relationship between Workplace and Owning Service.

### Classification

```text
NEXT-VERSION CORRECTION
```

### Required record

Create a Book 04 Next-Version Correction Plan after the ADR is accepted.

Do not rewrite the accepted Book 04 publication in this task.

## 5. Book 05 — MarkReg

### What remains valid

- MarkReg is the trademark lifecycle Product;
- MarkReg uses Core and Execution;
- Order, Matter, provider instruction and official outcomes retain formal ownership boundaries;
- Book 05 RC1 remains frozen.

### Required next-version clarification

```text
MarkReg Product
operates through a Workplace-scoped installation
```

The next version should distinguish:

- MarkReg self-operated Workplace;
- Partner-operated Workplace;
- Customer and commercial business responsibility;
- formal lifecycle state authority;
- MGSN procurement and provider collaboration;
- Distribution versus MGSN routing.

### Classification

```text
NEXT-VERSION CLARIFICATION
```

No current Book 05 manuscript change is authorized.

## 6. Book 06 — MarkOrbit Lite

### What remains valid

Book 06's accepted direction that Lite is a lightweight Workplace Product remains consistent with the ADR.

Lite's four loops, Today experience, work products, memory/assets and MarkOrbit handoffs remain valid.

### Required clarification

Lite may expose a client-facing projection, but this must not replace its primary identity as a lightweight operating Product for professionals and small teams.

Lite business records must be scoped to an identified Workplace.

### Classification

```text
CLARIFICATION
```

### Explicit rejection

Do not revise Book 06 to say:

```text
Lite = only the Workplace client portal
```

## 7. Book 07 — MGSN

### Current strengths

The Pre-Writing Audit correctly states:

- MGSN resources are platform-owned or governed;
- MGSN is a central hub;
- participants retain private spaces;
- external self-managed routes remain possible;
- platform matching, procurement, funds and fulfillment are central Product value;
- participant roles may be contextual;
- multiple providers may exist per jurisdiction and service.

### Upstream correction required

The Charter must use:

```text
Originating Workplace
→ authorized MGSN projection
→ platform-owned MGSN network
→ controlled provider projection
→ Execution Provider Workplace
→ Return
```

It must distinguish:

- Workplace-owned business and private route context;
- Workplace MGSN connection and projection;
- platform-owned provider pool and routing;
- provider-side Workplace responsibility;
- formal state ownership by Owning Services;
- Distribution referral versus MGSN managed execution.

### Current branch effect

The current Book 07 Charter preparation branch should be treated as paused pending ADR decision.

Planning records created before this ADR remain inputs, but their references to generic demand-side/provider-side participants must be reconciled with Originating and Execution Provider Workplaces.

### Classification

```text
UPSTREAM DEPENDENCY
REQUIRES RECONCILIATION
```

### Required record

After ADR acceptance, create a Book 07 Charter Reconciliation record before continuing the Charter Candidate.

## 8. Product and Architecture Impact Matrix

| Concept | Current ambiguity | Corrected direction | Follow-up owner |
| --- | --- | --- | --- |
| Workplace | environment/shell | business sovereignty and accountability boundary | Architecture / Book 04 |
| Core | shared authority may be confused with business ownership | shared semantics/capability, not automatic concrete-record ownership | Architecture / Book 02 |
| Owning Service | may be hidden by Workplace ownership language | retains formal state authority inside Workplace context | Book 03 / Product specs |
| Product access | generic access | Workplace-scoped Product Installation or equivalent | Book 04 |
| MarkReg self-operation | platform/global business may be implied | isolated MarkReg self-operated Workplace | Book 05 |
| Lite | lightweight Workplace versus client portal ambiguity | operating Product with optional client projection | Book 06 |
| Sites | public product surface | Workplace public projection | future Sites Book |
| MGSN node | Workplace network ownership may be implied | Workplace connection/projection only | Book 07 |
| MGSN network | network between private nodes | platform-owned managed network hub | Book 07 |
| Provider relationship | private history versus network resource | private history remains; platform owns managed supply relationship | Book 07 |
| Projection | visibility may imply state transfer | bounded representation; Handoff/Return govern collaboration | Book 04 / Book 03 |
| Portability | export everything may be implied | export Workplace assets, not platform-confidential network assets | Architecture |

## 9. Required Sequence

```text
1. Owner reviews MO-ADR-WSP-001
2. If accepted, prepare Canon Amendment Candidate
3. Prepare Book 04 Next-Version Correction Plan
4. Determine whether Book 02 Change Proposal is necessary
5. Prepare Book 07 Charter Reconciliation
6. Resume Book 07 Charter Candidate
7. Create downstream Product implementation specifications later
```

## 10. Gate Decision

```text
Architecture correction required: YES
Current Canon direct edit authorized: NO
Book 02 direct edit authorized: NO
Book 04 current edition rewrite authorized: NO
Book 05 RC1 rewrite authorized: NO
Book 06 RC1 rewrite authorized: NO
Book 07 Charter continuation before ADR decision: NO
Implementation authorized: NO
```
