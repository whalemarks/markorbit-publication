# Publication Manifest

## Repository Purpose

The MarkOrbit publication repository is the unified publication home for MarkOrbit books, shared editorial assets, reviews, release artifacts, architecture decisions, governance records and controlled task records.

Editorial, commercial or implementation convenience must not silently redefine accepted architecture.

## Architecture Authority

Current architecture authority: [MarkOrbit Orbital Architecture Canon vNext](architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.md).

- Version: vNext
- Status: Owner Confirmed Canonical Working Baseline
- Effective date: 2026-07-13
- Authority: Repository-level MarkOrbit architecture governance

## Book Registry

| Book | Title | Canonical Path | Status |
| --- | --- | --- | --- |
| Book 01 | MarkOrbit — The Operating System for Global Brand Services | `books/book-01-operating-system/` | Release Candidate 1 |
| Book 02 | MarkOrbit Core Specification | `books/book-02-core-specification/` | Frozen Core Specification Baseline v0.1 |
| Book 03 | MarkOrbit Execution System | `books/book-03-execution-system/` | Release Candidate 1 |
| Book 04 | MarkOrbit Workplace and Product Architecture | `books/book-04-workplace-product-architecture/` | Release Candidate 1 — Owner Accepted / Portfolio Locked |
| Book 05 | MarkReg: The Full-Lifecycle International Trademark Product | `books/book-05-markreg/` | Release Candidate 1 — Approved and Frozen |
| Book 06 | MarkOrbit Lite | `books/book-06-markorbit-lite/` | Release Candidate 1 — Owner Accepted |
| Book 07 | Mark Global Service Network | `books/book-07-mark-global-service-network/` | Network and Product Charter v0.1 — Ready for Owner Acceptance on Merge |

## Portfolio Baseline

Books 01–04 form the accepted pre-Product Portfolio Baseline.

Book 02 remains frozen. Semantic changes require the existing Change Proposal process.

Books 05–07 consume the baseline and may not silently redefine Core, Execution or Workplace authority.

## Book 05 — MarkReg

Book 05 defines the flagship full-lifecycle international trademark Product.

Publication state:

```text
Release Candidate 1 — Approved and Frozen
```

Book 05 RC1 is protected by its accepted release record, immutable content baseline and `release/book-05-rc1` pointer.

Final public/commercial distribution remains a separate gate.

## Book 06 — MarkOrbit Lite

Book 06 defines the AI business operating system for independent trademark professionals and small agencies, architecturally a lightweight Workplace Product.

Accepted Product Baseline:

```text
B06-SPEC-0001–0004
ML-S01–S05
ML-O01–O08
ML-W01–W10
ML-M01–M08
ML-H01–H08
ML-E01–E06
ML-J01–J04
ML-SCN-01–24
ML-HC-01–HC-08
ML-AC-01–AC-12
```

Frozen RC1 reader-facing inventory:

```text
B06-TOC-V0.1
B06-CH-00–B06-CH-33: 34 chapters
B06-APP-0001–B06-APP-0007: 7 Reader Apparatus records
Total ordered reader-facing inputs: 41
```

Immutable identity:

```text
Reader-facing content baseline:
7ce03755e03bb4876768a34a4ee3d2c3b74bddb1

Owner-decision activation commit:
060e807be90081977bcc322f1557b9fc950f5209

RC1 Decision Record:
B06-REL-0002

RC1 Freeze Record:
B06-REL-0003

Machine release manifest:
release/B06-RC1.yaml

Release pointer after freeze merge:
release/book-06-rc1
```

Validation evidence:

```text
Content/render workflow run: 29477787207
Content artifact ID: 8367264203
Content artifact digest:
sha256:2446561090311a6d6e5912ebdc1e109a2b0e5cf525109db9eb3b0762ee27236b

Final governance workflow run: 29478801425
Governance artifact ID: 8367659673
Governance artifact digest:
sha256:dcfd3f85169f1275d38dd09e34f8338089bd4b6dbd90573a3ebe0dbd5c3819da

Chapters: 34 / 34
Reader Apparatus: 7 / 7
Local links: 283 checked / 0 broken
Anchors: 10 checked / 0 broken
Controlled IDs: 93 / 93
Semantic figures: 12 / 12 rendered
PDF validation render: 410 pages / 0 near-blank pages
External URLs: 0
Material external claims requiring citation: 0
Blocking / major / warning findings: 0 / 0 / 0
Upstream conflicts: 0
Change Proposal required: NO
```

RC Hardening A, B and C are accepted. `RC-H01–RC-H06` are closed.

Book 06 RC1 was accepted through owner merge of PR #76 on 2026-07-16.

Book 06 RC1 acceptance does not approve final branded-publication production, Product implementation, production deployment or final public/commercial distribution.

## Book 07 — Mark Global Service Network

### Accepted Pre-Writing Baseline

Book 07 Pre-Writing Audit v0.1 was accepted through owner merge of PR #78 on 2026-07-16.

```text
B07-PLN-0001–0009 — ACCEPTED
B07-REV-0001 — PASS / ACCEPTED
B07-VAL-0001 — PASS / ACCEPTED
```

Accepted starting direction:

```text
Platform-owned MGSN resources
Central MGSN hub
Independent participant private spaces
R1 External Self-Managed Route
R2 Recommended Managed Route
R3 Managed Preferred-Provider Route
Default best-route matching
User final confirmation
Platform procurement, funds and fulfillment direction
```

### Current Gate

```text
Network and Product Charter v0.1
Ready for Owner Acceptance on Merge
```

### Current Charter Records

```text
B07-PLN-0010 — MGSN Network and Product Charter Candidate v0.1
B07-PLN-0011 — Charter Owner Decision Matrix / OD-01–OD-33
B07-REV-0002 — Network and Product Charter Review
B07-VAL-0002 — Charter Scope and Consistency Check
```

### Charter Identity

```text
MGSN is the platform-owned and platform-governed
managed global professional service network
that enables trademark professionals and agencies
to deliver services worldwide through one governed
commercial and fulfillment interface.
```

### Network Topology

```text
Demand-side Workplace / Lite
            ↓
          MGSN
            ↑
Provider Workplace / Provider Interface
```

MGSN does not create an independent participant-to-participant network graph.

### Product Promise

```text
platform provider coverage
+ standardized service scope
+ aggregated demand
+ negotiated procurement
+ Recommended Best Route
+ user confirmation
+ controlled funds
+ milestone Evidence
+ correction and replacement
+ typed Return
+ provider and network learning
```

### Delivery Route Constitution

```text
R1 — External Self-Managed Route
R2 — MGSN Recommended Managed Route
R3 — MGSN Managed Preferred-Provider Route
```

R1 remains permitted without provider import. The user manages negotiation, payment, follow-up and manual Evidence return. No MGSN procurement, funds, replacement or fulfillment guarantee is implied.

R2 is the default managed experience. MGSN may automatically compare and preselect one Recommended Best Route. The user confirms, rejects or adjusts before ordinary provider allocation.

R3 permits a preferred provider subject to platform admission, Capability, qualification, conflict, availability, procurement, service-package and risk controls.

```text
Automatic matching ≠ automatic appointment
Recommended Best Route ≠ final instruction
User confirmation ≠ Provider Acceptance
Same provider identity ≠ same route or guarantee
External user report ≠ official truth
```

### Matching and User Choice

The preferred Product presentation is:

```text
one Recommended Best Route
+ main reasons and constraints
+ rematch or preferred-provider request where permitted
+ External Self-Managed Route option
```

The complete provider pool is not a constitutional user-facing requirement.

Standing platform allocation is deferred to a later explicit, revocable and service-specific mandate.

### Commercial and Procurement Constitution

```text
platform wholesale network
+ managed-service packages
```

Pricing layers remain distinct:

```text
provider procurement cost
+ official fees and third-party disbursements
+ platform service, support and risk cost
+ demand-side margin where permitted
= customer-facing offer
```

MGSN aims to obtain lower or more stable pricing and stronger service terms through aggregated demand, repeat volume and negotiated procurement.

This is a strategic target, not a universal lowest-price guarantee.

### Funds and Fulfillment Constitution

```text
offer accepted
→ funds requested
→ funds received or authorized
→ purpose allocation
→ provider commitment
→ governed release
→ Evidence and reconciliation
→ settlement / refund / dispute
→ closure
```

The Charter does not claim a universal escrow, trust-account or regulated payment status.

Contracting entity, funds holder, accounting, tax, foreign-exchange, sanctions and client-money rules remain implementation prerequisites.

### Provider and Trust Constitution

```text
Core Organization
≠ MGSN Provider Profile
≠ Capability Claim
≠ Evidence
≠ verification
≠ service-specific Provider role
≠ Network Service Engagement
```

MGSN Trust is multidimensional, source-aware, time-scoped and service-specific. It is not one permanent public score.

### Initial MVP 0

Primary demand-side users:

- Chinese trademark agencies handling international work;
- independent international trademark professionals;
- authorized Lite, Workplace and MarkReg users.

Initial provider cohort:

- existing platform foreign associates;
- proven high-volume filing providers;
- selected verified law firms.

Initial scope:

- international trademark filing;
- filing through registration where packaged;
- selected high-volume post-filing and registration services;
- operator-assisted specialist matters.

MVP 0 is operator-assisted. Automation supports need typing, eligibility, comparison, recommendation and monitoring. Human operators retain admission, complex procurement, funds review, replacement, dispute and suspension responsibilities.

### Charter Review Result

```text
Review: B07-REV-0002
Decision: PASS
Authority chain: PASS
Product and network identity: PASS
Cross-book ownership boundaries: PASS
Route and matching model: PASS
Procurement and pricing model: PASS
Funds-control constitution: PASS WITH LEGAL MODEL DEFERRED
Provider and Trust model: PASS
MVP 0: PASS
Blocking findings: 0
Major findings: 0
Upstream Change Proposal required: NO
```

### Owner Merge Effect

Owner merge accepts:

```text
B07-PLN-0010 v0.1
B07-PLN-0011
OD-01–OD-33
B07-REV-0002
B07-VAL-0002
```

Owner merge authorizes preparation of:

```text
Book 07 Controlled Product Baseline Candidate
```

Owner merge does not accept or authorize:

```text
Controlled Product Baseline
Chapter Map
Manuscript drafting
Database schema
API contracts
Payment implementation
Provider appointment implementation
Production deployment
Peer-to-peer participant network
External Protected Action
```

## Current Portfolio Gate

```text
Books 01–04 Portfolio Baseline
→ Book 05 RC1 approved and frozen
→ Book 06 RC1 owner accepted
→ Book 07 Pre-Writing Audit v0.1 accepted
→ Book 07 Network and Product Charter v0.1
→ Owner acceptance
→ Book 07 Controlled Product Baseline Candidate
```

## Global Authority Boundary

Ready for unrestricted implementation: **NO**

Ready for production deployment: **NO**

Ready for final public/commercial distribution: **NO**

External Protected Action authorized: **NO**
