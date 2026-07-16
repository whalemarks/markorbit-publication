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
| Book 06 | MarkOrbit Lite | `books/book-06-markorbit-lite/` | Release Candidate 1 — Ready for Owner Acceptance on Merge |
| Book 07 | Mark Global Service Network | `books/book-07-mark-global-service-network/` | Planned |

Book 05 is frozen through its accepted RC1 content baseline, permanent release record and `release/book-05-rc1` pointer.

Book 06 Product Charter v0.3, Product Baseline v0.1, Chapter Map `B06-TOC-V0.1`, Waves 1–7, Whole-Book Complete Draft 1 and RC Hardening A/B are accepted. `B06-REV-0016` records PASS for RC Hardening C and Whole-Book RC review. Owner merge accepts Book 06 Release Candidate 1.

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

Accepted Chapter Map and manuscript:

```text
B06-TOC-V0.1
B06-CH-00–B06-CH-33
34 / 34 chapter files
Whole-Book Complete Draft 1 — ACCEPTED
```

Accepted Reader Apparatus:

```text
B06-APP-0001 — Controlled Term Glossary
B06-APP-0002 — Core Distinction Matrix
B06-APP-0003 — Abbreviations and Controlled ID Guide
B06-APP-0004 — Figure Register and Semantic Diagrams
B06-APP-0005 — Controlled Record Coverage
B06-APP-0006 — Journey, Scenario, Handoff and Acceptance Coverage
B06-APP-0007 — Subject Index
```

Release Candidate validation:

```text
Review: B06-REV-0016
Release record: B06-REL-0002
Reader-facing inputs: 41
Reader-facing baseline:
7ce03755e03bb4876768a34a4ee3d2c3b74bddb1

Successful workflow run: 29477787207
Artifact ID: 8367264203
Artifact digest:
sha256:2446561090311a6d6e5912ebdc1e109a2b0e5cf525109db9eb3b0762ee27236b

Chapters: 34 / 34
Reader Apparatus: 7 / 7
Local links: 283 checked / 0 broken
Anchors: 10 checked / 0 broken
Controlled IDs: 93 / 93
Semantic figures: 12 / 12 rendered
PDF: 410 pages / 842,295 bytes / 0 near-blank pages
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

Release Candidate requirement status:

```text
RC-H01 — CLOSED ON HARDENING A MERGE
RC-H02 — CLOSED ON HARDENING A MERGE
RC-H03 — CLOSED ON HARDENING B MERGE
RC-H04 — CLOSED ON HARDENING A MERGE
RC-H05 — CLOSED ON HARDENING B MERGE
RC-H06 — READY TO CLOSE ON CURRENT OWNER MERGE
```

RMB 99, recurring/daily content, Prospect Candidate quantity, Asset limits, Handoff support levels and quotas remain commercial experiments rather than Product constitution.

Lite does not absorb MarkReg Product Sessions, Formal Intake or Matters; MGSN Trust, Routing or provider appointment; Review approval; Communication send state; formal Opportunity; active Task/Workflow; or Execution and protected-action authority.

Book 06 RC1 acceptance does not approve final branded-publication production, Product implementation, production deployment or final public/commercial distribution.

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
→ RC Hardening A accepted
→ RC Hardening B accepted
→ RC Hardening C PASS
→ Book 06 Release Candidate 1 owner merge
→ optional final brand/design production
→ final publication/distribution decision
```

All 34 Book 06 chapter files drafted: **YES**

Whole-book Complete Draft 1 accepted: **YES**

RC Hardening A accepted: **YES**

RC Hardening B accepted: **YES**

RC Hardening C validated: **YES**

Book 06 RC1 ready for owner acceptance on merge: **YES**

Ready for unrestricted implementation: **NO**

Ready for production deployment: **NO**

Ready for final public/commercial distribution: **NO**

External protected action authorized: **NO**
