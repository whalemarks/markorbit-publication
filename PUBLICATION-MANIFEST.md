# Publication Manifest

## Repository Purpose

The MarkOrbit publication repository is the unified publication home for MarkOrbit books, shared editorial assets, review materials, release artifacts, architecture decisions, governance records and controlled task records.

Editorial or implementation convenience must not silently redefine architecture.

## Architecture Authority

Current architecture authority: [MarkOrbit Orbital Architecture Canon vNext](governance/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.md).

- Version: vNext
- Status: Owner Confirmed Canonical Working Baseline
- Effective date: 2026-07-13
- Authority: Repository-level MarkOrbit architecture governance

## Book Registry

| Book | Title | Canonical Path | Status |
|---|---|---|---|
| Book 01 | MarkOrbit — The Operating System for Global Brand Services | `books/book-01-operating-system/` | Release Candidate 1 |
| Book 02 | MarkOrbit Core Specification | `books/book-02-core-specification/` | Frozen Core Specification Baseline v0.1 |
| Book 03 | MarkOrbit Execution System | `books/book-03-execution-system/` | Release Candidate 1 |
| Book 04 | MarkOrbit Workplace and Product Architecture | `books/book-04-workplace-product-architecture/` | Release Candidate 1 — Owner Accepted / Portfolio Locked |
| Book 05 | MarkReg: The Full-Lifecycle International Trademark Product | `books/book-05-markreg/` | Release Candidate 1 — Approved and Frozen |
| Book 06 | MarkOrbit Lite | `books/book-06-markorbit-lite/` | Release Candidate 1 — Approved and Frozen on Owner Merge |
| Book 07 | Mark Global Service Network | `books/book-07-mark-global-service-network/` | Planned |

Book 05 is frozen through its accepted RC1 content baseline, permanent release record and `release/book-05-rc1` pointer.

Book 06 RC1 is accepted through `B06-REV-0016` and `B06-REL-0002`, and frozen through `B06-REL-0003`, `release/B06-RC1.yaml` and the post-merge `release/book-06-rc1` pointer.

## Planned Book Positioning

### Book 01 — MarkOrbit — The Operating System for Global Brand Services

Defines industry vision and Operating System principles. Publication state: Release Candidate 1.

### Book 02 — MarkOrbit Core Specification

Defines shared Core semantics, objects, services and contracts. Baseline B02-BASELINE-V0.1 remains frozen; semantic changes require the existing Change Proposal process.

### Book 03 — MarkOrbit Execution System

Defines how approved Core contracts become governed operational execution. Publication state: Release Candidate 1.

### Book 04 — MarkOrbit Workplace and Product Architecture

Defines independent organizational Workplaces and their consumption of MarkOrbit capabilities. Publication state: Release Candidate 1 — Owner Accepted / Portfolio Locked.

### Book 05 — MarkReg

Defines the flagship full-lifecycle international trademark Product. Publication state: Release Candidate 1 — Approved and Frozen. Final public/commercial distribution remains a separate unapproved gate.

### Book 06 — MarkOrbit Lite

Defines the AI business operating system for independent trademark professionals and small agencies, architecturally a lightweight Workplace Product.

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

Complete manuscript argument:

```text
Product Constitution
→ Daily Operating Model
→ Customer and Service Growth
→ Professional Work Products
→ Cases, Memory and Business Assets
→ MarkOrbit Gateways and Continuity
→ MVP and Product Conformance
→ Commercial Plans and Sustainable Economics
→ Product Evolution Without Constitutional Drift
```

All `RC-H01–RC-H06` requirements are closed.

RMB 99, recurring/daily content, Prospect Candidate quantity, Asset limits, Handoff support levels and quotas remain commercial experiments rather than Product constitution.

Lite does not absorb MarkReg Product Sessions, Formal Intake or Matters; MGSN Trust, Routing or provider appointment; Review approval; Communication send state; formal Opportunity; active Task/Workflow; or Execution and protected-action authority.

Book 06 RC1 approval and freeze do not approve final branded-publication production, Product implementation, production deployment or final public/commercial distribution.

### Book 07 — Mark Global Service Network

Future publication subject for service-routing, Capability and Trust between independent Workplaces.

## Books 01–04 Portfolio Baseline

The current cross-book review is `MO-PUB-REV-0001` and the effective baseline is `MO-PUB-BASELINE-0001`.

```text
Book 01 — Release Candidate 1
Book 02 — Frozen Core Specification Baseline v0.1
Book 03 — Release Candidate 1
Book 04 — Release Candidate 1, Owner Accepted and Portfolio Locked
```

Current gate:

```text
Books 01–04 Portfolio Baseline
→ Book 05 MarkReg RC1 approved and frozen
→ Book 06 Product Charter v0.3 accepted
→ Book 06 Product Baseline v0.1 accepted
→ Book 06 Chapter Map v0.1 accepted
→ Book 06 Waves 1–7 accepted
→ Book 06 Whole-Book Complete Draft 1 accepted
→ RC Hardening A/B/C accepted
→ Book 06 Release Candidate 1 approved
→ Book 06 RC1 freeze owner merge
→ create release/book-06-rc1 pointer
→ optional final brand/design production
→ final publication/distribution decision
```

All 34 Book 06 chapter files drafted: **YES**

Whole-book Complete Draft 1 accepted: **YES**

RC Hardening A/B/C accepted: **YES**

Book 06 RC1 accepted: **YES**

Book 06 RC1 freeze ready for owner merge: **YES**

Ready for unrestricted implementation: **NO**

Ready for production deployment: **NO**

Ready for final public/commercial distribution: **NO**

External protected action authorized: **NO**
