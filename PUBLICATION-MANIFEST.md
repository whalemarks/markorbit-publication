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
| Book 06 | MarkOrbit Lite | `books/book-06-markorbit-lite/` | RC Hardening A — Editorial and Structural Normalization — Owner Accepted on Merge |
| Book 07 | Mark Global Service Network | `books/book-07-mark-global-service-network/` | Planned |

Book 05 is frozen through its accepted RC1 content baseline, permanent release record and `release/book-05-rc1` pointer.

Book 06 Product Charter v0.3, Product Baseline v0.1, Chapter Map B06-TOC-V0.1, Waves 1–7 and the Whole-Book Complete Draft 1 are accepted. `B06-REV-0014` records RC Hardening A with no blocking, major or upstream findings. Release Candidate status remains unaccepted.

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

Whole-book review result:

```text
Mechanical completeness: PASS
Cross-Part continuity: PASS
Product Charter coverage: PASS
Product Baseline coverage: PASS
Controlled-term meaning integrity: PASS
Cross-Book boundary integrity: PASS
Commercial/Product separation: PASS
Implementation boundary: PASS
Blocking findings: 0
Major findings: 0
Upstream findings: 0
Change Proposal required: NO
```

RC Hardening A result:

```text
Review: B06-REV-0014
Chapter files audited: 34
Chapter files modified: 23
Normalized chapter headers: 34 / 34
Internal wave-merge metadata remaining: 0
CH01 internal drafting-wave content: removed
CH33 reader-facing evolution sequence: applied
Chapter ID/title/order changes: 0
Controlled meaning changes: 0
Blocking findings: 0
Major findings: 0
Upstream findings: 0
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
RC-H01 — chapter metadata normalization: CLOSED ON HARDENING A MERGE
RC-H02 — reader-facing governance cleanup: CLOSED ON HARDENING A MERGE
RC-H03 — controlled terms and distinction apparatus: OPEN — HARDENING B
RC-H04 — repetition and cross-reference hardening: CLOSED ON HARDENING A MERGE
RC-H05 — figures, appendices and index: OPEN — HARDENING B
RC-H06 — source, citation and rendered validation: OPEN — HARDENING C
```

Hardening order:

```text
Work Package A — Editorial and Structural Normalization — OWNER ACCEPTED ON MERGE
→ Work Package B — Reader Apparatus — AUTHORIZED NEXT
→ Work Package C — Source, Render and RC Review
→ owner Release Candidate decision
```

RMB 99, recurring/daily content, Prospect Candidate quantity, Asset limits, Handoff support levels and quotas remain commercial experiments rather than Product constitution.

Lite does not absorb MarkReg Product Sessions, Formal Intake or Matters; MGSN Trust, Routing or provider appointment; Review approval; Communication send state; formal Opportunity; active Task/Workflow; or Execution and protected-action authority.

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
→ RC Hardening A owner merge
→ RC Hardening B
→ RC Hardening C and RC Review
→ owner Release Candidate decision
```

All 34 Book 06 chapter files drafted: **YES**

Whole-book Complete Draft 1 accepted: **YES**

RC Hardening A ready for owner acceptance on merge: **YES**

Ready for Book 06 Release Candidate: **NO**

Ready for unrestricted implementation: **NO**

Ready for production or public/commercial distribution: **NO**

External protected action authorized: **NO**