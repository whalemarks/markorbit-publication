# Architecture Decision Register vNext.1

- **Version:** vNext.1
- **Status:** Active Decision Register — ready for Owner activation on merge
- **Authority:** Repository-level MarkOrbit architecture governance
- **Canon:** [MarkOrbit Orbital Professional Operating Architecture vNext.1](MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.1.md)
- **Supersedes:** `DECISION-REGISTER-vNEXT.md` as the active register

The decisions from `ARC-001–ARC-028` remain accepted except where refined by the decisions below. The earlier register remains historical evidence.

## Preserved decisions

The following decision families remain in force:

```text
ARC-001–ARC-002
MarkOrbit as the total architecture and Orbital as the primary metaphor

ARC-004–ARC-007
federated governance as a characteristic,
separate Core / Execution / Workplace / Product responsibilities,
constitutional spine plus horizontal planes,
and cross-cutting governance

ARC-013–ARC-028
Information / Knowledge / Value distinctions,
Capability / Skill distinctions,
AI and Workflow boundaries,
Artifact and Delivery distinctions,
Candidate-before-canonical,
Product Loop First,
publication map,
Book 02 freeze,
and External Protected Action boundary
```

The following earlier decisions are refined by `ARC-029–ARC-036`:

```text
ARC-003 — Organization Workplace as an independent Orbit
ARC-008 — Workplace as primary operating unit
ARC-009 — Lite as lightweight Workplace
ARC-010 — MarkReg flagship lifecycle Product
ARC-011 — MGSN connection model
ARC-012 — MGSN private-first model
ARC-023 — Book 04 Workplace and Product Architecture
ARC-024 — Books 05–07 Product publication map
```

## ARC-029 — Workplace is the Organization-scoped business-sovereignty and accountability boundary.

- **Decision:** Workplace is the Organization-scoped business-sovereignty, accountability, permission, Product-operation and projection boundary.
- **Rationale:** A generic operating environment or platform shell does not adequately preserve customer relationships, private business context, internal pricing, permissions, Knowledge and accountable commercial responsibility.
- **Consequence:** Concrete business records must operate in an explicit Workplace context. Products and shared services may consume authorized context but may not silently convert Workplace business assets into platform-owned business assets.
- **Status:** Accepted for vNext.1 on Owner merge.
- **Affected books/products:** Architecture Canon, Book 04, MarkReg, Lite, Sites, MGSN.

## ARC-030 — Authority is divided into five dimensions.

- **Decision:** Business sovereignty, semantic authority, formal-state authority, physical custody and legal/source authority are separate dimensions.
- **Rationale:** The generic term `owner` previously collapsed commercial control, schema authority, state mutation, infrastructure custody and legal rights.
- **Consequence:** Every material architecture record should identify the relevant authority dimension. Physical hosting does not imply business sovereignty; Workplace sovereignty does not imply unrestricted mutation authority.
- **Status:** Accepted for vNext.1 on Owner merge.
- **Affected books/products:** All books and Products.

## ARC-031 — Product participation occurs through Workplace-scoped Product Installations.

- **Decision:** Products operate for an Organization through a Workplace-scoped Product Installation.
- **Rationale:** Product access, entitlement, configuration, permission, data scope and projection scope require a stable organizational boundary.
- **Consequence:** Product Installation becomes an architecture relationship. It does not require separate source-code deployment or database per Workplace.
- **Status:** Accepted for vNext.1 on Owner merge.
- **Affected books/products:** Book 04, MarkReg, Lite, Sites, future Products.

## ARC-032 — Product Projection, Handoff and Return are distinct.

- **Decision:** A Projection is a purpose-limited view or interaction surface; a Handoff transfers typed context toward another authority boundary; a Return brings typed outcome or Evidence back.
- **Rationale:** Treating all external surfaces as the same interaction obscures permission, source, destination and formal-state responsibilities.
- **Consequence:** Products must define projection scope separately from Handoff and Return contracts. Delivery does not imply destination acceptance or ownership transfer.
- **Status:** Accepted for vNext.1 on Owner merge.
- **Affected books/products:** Book 03, Book 04, Lite, Sites, MarkReg, MGSN.

## ARC-033 — Lite is a lightweight Workplace Product and may expose a client-facing projection.

- **Decision:** Lite remains a lightweight Workplace Product for independent professionals and small teams and may additionally expose client-facing projections.
- **Rationale:** Reducing Lite to a client portal would discard its Today, growth, work-product, Case, Memory and Asset operating loops.
- **Consequence:** Client Intake, upload, confirmation and status surfaces are projections from an operating Lite context, not the complete identity of Lite.
- **Status:** Accepted for vNext.1 on Owner merge.
- **Affected books/products:** Lite, Book 06.

## ARC-034 — Sites is a Workplace public-brand and content projection Product.

- **Decision:** Sites publishes Workplace-authorized public brand and content projections.
- **Rationale:** Public content, design systems and publication versions need Product governance without becoming the Owning Service for Customer, Order, Matter or Payment.
- **Consequence:** Dynamic Lead, Intake and commercial flows must enter an explicit Workplace and Product route.
- **Status:** Accepted for vNext.1 on Owner merge.
- **Affected books/products:** Sites, Book 04, future Sites publication.

## ARC-035 — MGSN Connection is distinct from the platform-owned MGSN Network.

- **Decision:** An MGSN Connection or Gateway is a Workplace-scoped interface; MGSN itself is the platform-owned and platform-governed managed global professional service network.
- **Rationale:** Workplace relationship history and private preferences must not be confused with ownership of provider supply, procurement terms, routing logic, funds controls or platform Trust.
- **Consequence:** MGSN governs provider admission, supply portfolios, procurement, matching, funds, fulfillment, correction, replacement, suspension and network operating data. Participants do not acquire an unrestricted peer-to-peer network graph.
- **Status:** Accepted for vNext.1 on Owner merge.
- **Affected books/products:** MGSN, Book 07, Workplace, MarkReg, Lite.

## ARC-036 — Cross-Workplace managed service uses Originating and Execution Provider Workplaces.

- **Decision:** Managed service flows use an Originating Workplace, an MGSN Connection, the platform-owned MGSN Network, an Execution Provider Workplace and a governed Return.
- **Rationale:** The demand-side commercial relationship and provider-side professional execution have different business sovereignty, permissions, formal-state and legal responsibilities.
- **Consequence:** The canonical route is:

```text
Originating Workplace
→ authorized projection
→ MGSN Network
→ controlled provider allocation / instruction
→ Execution Provider Workplace
→ governed Return
→ Originating Workplace
```

No undisclosed or ungoverned rebrokering is permitted.
- **Status:** Accepted for vNext.1 on Owner merge.
- **Affected books/products:** Book 03, Book 04, Book 05, Book 06, Book 07.

## ARC-037 — Self-operated platform business uses an isolated Organization and Workplace.

- **Decision:** MarkReg or other platform self-operated business must operate through an explicit self-operated Organization and Workplace.
- **Rationale:** Platform administration must not imply default access to Partner Workplace customers, pricing, Matters or private Knowledge.
- **Consequence:** Self-operated and Partner-operated business use the same Workplace isolation, permission and audit principles.
- **Status:** Accepted for vNext.1 on Owner merge.
- **Affected books/products:** MarkReg, Workplace, platform operations.

## ARC-038 — Workplace portability excludes platform-owned network and shared assets.

- **Decision:** Workplace business records, private Documents, Evidence, Knowledge and portable configuration require governed export and exit paths, but platform-owned network and shared assets are not automatically portable.
- **Rationale:** Business sovereignty requires continuity and exit without transferring other participants' data, confidential procurement terms, platform Trust or shared source code.
- **Consequence:** Portability rules must distinguish Workplace assets from MGSN provider pools, platform routing models, confidential procurement and other platform-owned resources.
- **Status:** Accepted for vNext.1 on Owner merge.
- **Affected books/products:** Workplace, Products, MGSN.

## Book 02 freeze

`MO-B02-CPA-001` concludes that the vNext.1 activation is an architecture clarification and does not itself require an immediate Book 02 semantic Change Proposal.

A formal Book 02 Change Proposal remains mandatory if future work changes:

- Core object identity or cardinality;
- controlled fields;
- formal states or transitions;
- Owning Service authority;
- Event, Handoff or Return contracts;
- Product-local concepts promoted into Core.

## Authority boundary

This register does not authorize implementation, production deployment, payment custody, provider appointment, autonomous professional judgment, filing or External Protected Action.
