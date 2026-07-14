# Publication Manifest

## Repository Purpose

The MarkOrbit publication repository is the unified publication home for MarkOrbit books, shared editorial assets, review materials, release artifacts, architecture decisions, governance records, and controlled task records.

The repository records owner-approved canonical architecture and controlled publication drafts, but editorial or implementation convenience must not silently redefine architecture.

## Architecture Authority

Current architecture authority: [MarkOrbit Orbital Architecture Canon vNext](architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.md).

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
| Book 05 | MarkReg: The Full-Lifecycle International Trademark Product | `books/book-05-markreg/` | CH00–CH22 Productization Closed — Part IV Authorized |
| Book 06 | MarkOrbit Lite | `books/book-06-markorbit-lite/` | Planned |
| Book 07 | Mark Global Service Network | `books/book-07-mark-global-service-network/` | Planned |

Book 05 has an owner-accepted chapter map, controlled Product specifications, productized CH08–CH22 and a closure review authorizing Part IV. Planned missing Book 06–07 directories are expected to produce warnings only, not validation errors.

## Planned Book Positioning

### Book 01 — MarkOrbit — The Operating System for Global Brand Services

Canonical path: `books/book-01-operating-system/`

Positioning: Defines industry vision and Operating System principles.

Publication state: Release Candidate 1 after MO-PUB-REV-0001 restored Chapter 1, reconciled the current publication map, aligned Orbital Architecture terminology, and completed publication apparatus.

### Book 02 — MarkOrbit Core Specification

Canonical path: `books/book-02-core-specification/`

Positioning: Defines shared Core semantics, objects, services, and contracts.

Baseline ID: B02-BASELINE-V0.1. Version: 0.1.0. Status: Frozen Core Specification Baseline. Future semantic change requires the existing Book 02 Change Proposal process.

### Book 03 — MarkOrbit Execution System

Chinese title: Book 03 — MarkOrbit 执行系统

Canonical path: `books/book-03-execution-system/`

Positioning: Defines how approved Core contracts become governed operational execution.

Publication state: Release Candidate 1. Owner-accepted Execution architecture is preserved; publication finishing and cross-book reconciliation are complete.

### Book 04 — MarkOrbit Workplace and Product Architecture

Canonical path: `books/book-04-workplace-product-architecture/`

Positioning: Defines how an independent professional organization establishes its own operating orbit and consumes MarkOrbit Core, Execution, Knowledge, Intelligence, Capabilities, Products, and network services through its Workplace.

Publication state: Release Candidate 1 — Owner Accepted / Portfolio Locked. CH00–CH39 remain structurally complete under B04-TOC-V0.1. Publication finishing and owner approval through merge of PR #31 are complete. B04-REV-0005 records the portfolio lock.

### Book 05 — MarkReg: The Full-Lifecycle International Trademark Product

Canonical path: `books/book-05-markreg/`

Positioning: Defines the flagship full-lifecycle international trademark Product, including need understanding, recommendation, intake, filing preparation, governed execution handoff, examination, registration, maintenance, provider collaboration, and portfolio continuity.

Publication state: CH00–CH22 Productization Closed — Part IV Authorized. B05-TOC-V0.1 is owner accepted. B05-SPEC-0001 through B05-SPEC-0004 define the controlled Product contracts. B05-REV-0007 closes B05-REVISION-PACK-001 and authorizes CH23–CH29.

### Book 06 — MarkOrbit Lite

Canonical path: `books/book-06-markorbit-lite/`

Positioning: Future publication subject for the lightweight Workplace for trademark professionals.

### Book 07 — Mark Global Service Network

Canonical path: `books/book-07-mark-global-service-network/`

Positioning: Future publication subject for the service-routing, Capability, and Trust network connecting independent Workplaces.

## Books 01–04 Portfolio Baseline

The current cross-book review is `MO-PUB-REV-0001`.

```text
Book 01 — Release Candidate 1
Book 02 — Frozen Core Specification Baseline v0.1
Book 03 — Release Candidate 1
Book 04 — Release Candidate 1, Owner Accepted and Portfolio Locked
```

The effective baseline is `MO-PUB-BASELINE-0001`.

Current gate:

```text
Portfolio Baseline merged and effective
→ Book 05 B05-TOC-V0.1 owner accepted
→ CH00–CH22 productized and reviewed
→ B05-REVISION-PACK-001 closed
→ Part IV CH23–CH29 authorized
```

Ready for Book 05 controlled publication drafting: **YES**

Ready for unrestricted implementation: **NO**

External protected action authorized: **NO**