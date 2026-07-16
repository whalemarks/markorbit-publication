# Publication Manifest

## Repository Purpose

The MarkOrbit publication repository is the unified publication home for MarkOrbit books, shared editorial assets, reviews, release artifacts, architecture decisions, governance records and controlled task records.

Editorial, commercial or implementation convenience must not silently redefine accepted architecture.

## Active Architecture Authority

Current active authority:

- [MarkOrbit Orbital Professional Operating Architecture vNext.1](architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.1.md)
- [Architecture Decision Register vNext.1](architecture/DECISION-REGISTER-vNEXT.1.md)

```text
Version: vNext.1
Status: Active Canon — effective on Owner merge
Authority: Repository-level MarkOrbit architecture governance
Amendment basis: MO-ADR-WSP-001 + MO-ARCH-AMEND-001
```

The previous vNext Canon and Decision Register remain historical working-baseline records.

Book 02 remains:

```text
Baseline ID: B02-BASELINE-V0.1
Version: 0.1.0
Status: Frozen Core Specification Baseline
```

`MO-B02-CPA-001` concludes that the Workplace sovereignty clarification does not require an immediate Book 02 semantic Change Proposal. Future semantic changes still require the established process.

## Workplace Sovereignty Constitution

```text
Workplace
= Organization-scoped business-sovereignty,
  accountability, permission, Product-operation
  and projection boundary

Core
= shared semantic authority and capabilities

Owning Service
= formal business-state authority

MGSN Connection / Gateway
= Workplace-scoped projection and network interface

MGSN Network
= platform-owned and platform-governed managed network
```

Authority dimensions remain distinct:

```text
Business sovereignty
Semantic authority
Formal-state authority
Physical custody
Legal / source authority
```

## Book Registry

| Book | Title | Canonical Path | Status |
| --- | --- | --- | --- |
| Book 01 | MarkOrbit — The Operating System for Global Brand Services | `books/book-01-operating-system/` | Release Candidate 1 |
| Book 02 | MarkOrbit Core Specification | `books/book-02-core-specification/` | Frozen Core Specification Baseline v0.1 |
| Book 03 | MarkOrbit Execution System | `books/book-03-execution-system/` | Release Candidate 1 |
| Book 04 | MarkOrbit Workplace and Product Architecture | `books/book-04-workplace-product-architecture/` | Release Candidate 1 — Historical / Next-Version Correction Planned |
| Book 05 | MarkReg: The Full-Lifecycle International Trademark Product | `books/book-05-markreg/` | Release Candidate 1 — Approved and Frozen |
| Book 06 | MarkOrbit Lite | `books/book-06-markorbit-lite/` | Release Candidate 1 — Owner Accepted and Frozen |
| Book 07 | Mark Global Service Network | `books/book-07-mark-global-service-network/` | Reconciled Charter v0.1 — Ready for Owner Acceptance on Merge |

## Portfolio Governance

Books 01–04 remain the accepted historical pre-Product publication baseline.

Active architecture clarification may require versioned correction without silently rewriting accepted publication history.

- Book 04 has a controlled next-version correction plan: `MO-ARCH-PLN-001`.
- Book 05 RC1 remains frozen.
- Book 06 RC1 remains accepted and frozen.
- Book 07 consumes Active Canon vNext.1 and may not redefine Core, Execution or Workplace authority.

## Book 05 — MarkReg

```text
Release Candidate 1 — Approved and Frozen
Release pointer: release/book-05-rc1
```

MarkReg operates through a Workplace-scoped Product Installation. Future clarification must preserve the frozen RC1 lifecycle and use versioned governance rather than silent in-place semantic change.

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

Release identity:

```text
Reader-facing content baseline:
7ce03755e03bb4876768a34a4ee3d2c3b74bddb1

Owner-decision activation commit:
060e807be90081977bcc322f1557b9fc950f5209

RC1 Decision Record: B06-REL-0002
RC1 Freeze Record: B06-REL-0003
Machine release manifest: release/B06-RC1.yaml
Release pointer: release/book-06-rc1
```

Validated result:

```text
34 / 34 chapters
7 / 7 Reader Apparatus files
283 local links / 0 broken
10 anchors / 0 broken
93 / 93 controlled IDs
12 / 12 semantic figures
410-page validation PDF / 0 near-blank pages
0 Blocking / Major / Warning findings
```

Lite remains a lightweight Workplace Product and may additionally expose client-facing projections. It is not reduced to a client portal.

## Book 07 — Mark Global Service Network

### Accepted Pre-Writing Baseline

Book 07 Pre-Writing Audit v0.1 was accepted through owner merge of PR #78.

```text
B07-PLN-0001–0009 — ACCEPTED
B07-REV-0001 — PASS / ACCEPTED
B07-VAL-0001 — PASS / ACCEPTED
```

### Reconciled Charter Baseline

```text
B07-PLN-0010 — Network and Product Charter Candidate v0.1
B07-PLN-0011 — Owner Decision Matrix / OD-01–OD-33
B07-PLN-0013 — Workplace Sovereignty Charter Reconciliation
B07-REV-0003 — Reconciled Charter Review / PASS
B07-VAL-0003 — Scope and Authority Check / PASS
```

`B07-PLN-0013` is the controlling interpretation where earlier Charter language is incomplete or ambiguous.

### Product Identity

```text
platform-owned managed global service network
+ central MGSN hub
+ provider supply portfolios
+ aggregated demand and procurement
+ recommended route and bounded user choice
+ controlled funds and fulfillment
+ participant Workplace business sovereignty
+ governed Handoff and Return
+ platform Trust and network evolution
```

### Canonical Topology

```text
Originating Workplace
→ authorized demand projection
→ MGSN Connection / Gateway
→ platform-owned MGSN Network
→ controlled provider allocation / instruction
→ Execution Provider Workplace
→ governed Return
→ Originating Workplace
```

MGSN does not create an unrestricted participant-to-participant network graph.

### Route Constitution

```text
R1 — External Self-Managed Route
R2 — MGSN Recommended Managed Route
R3 — MGSN Managed Preferred-Provider Route
```

### Current Review Result

```text
B07-REV-0003: PASS
B07-VAL-0003: PASS
Blocking findings: 0
Major findings: 0
Book 02 Change Proposal required now: NO
Reconciled Charter ready for Owner acceptance: YES
```

### Owner Merge Effect

Owner merge accepts:

```text
Active Canon vNext.1
Active Decision Register vNext.1
B07-PLN-0010
B07-PLN-0011 / OD-01–OD-33
B07-PLN-0013
B07-REV-0003
B07-VAL-0003
Reconciled Book 07 Network and Product Charter v0.1
```

Owner merge authorizes preparation of:

```text
Book 07 Controlled Product Baseline Candidate
Product-local records and controlled IDs
Reference journeys and conformance scenarios
Handoff and Return contracts
MVP 0 acceptance and evaluation baseline
```

Owner merge does not accept or authorize:

```text
Controlled Product Baseline itself
Chapter Map
Manuscript drafting
Database schema
API contracts
Payment custody or funds release
Provider appointment implementation
Production deployment
External Protected Action
```

## Current Portfolio Gate

```text
Active Canon vNext.1
→ Book 05 RC1 approved and frozen
→ Book 06 RC1 owner accepted and frozen
→ Book 07 Reconciled Charter ready for Owner acceptance
→ Controlled Product Baseline Candidate next
```

## Global Authority Boundary

Ready for unrestricted implementation: **NO**

Ready for production deployment: **NO**

Ready for final public/commercial distribution: **NO**

External Protected Action authorized: **NO**
