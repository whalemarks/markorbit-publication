# Publication Roadmap

## Purpose

This roadmap records the accepted publication sequence and current controlled gates for the MarkOrbit publication portfolio. Publication order does not determine software implementation order.

## Completed Foundation

```text
Book 02 Frozen Core Specification Baseline v0.1 — ACTIVE
Orbital Architecture Canon vNext.1 — ACTIVE
Books 01–04 Portfolio Baseline — ACCEPTED
Repository release-state reconciliation — COMPLETE
Books 05–07 Release Candidate 1 — APPROVED AND FROZEN
Book 04 Workplace Sovereignty WP-A–WP-F — OWNER ACCEPTED / CLOSED
Book 04 vNext Integration 01–02C — OWNER ACCEPTED
Book 04 vNext Candidate 01–04 generation milestones — OWNER ACCEPTED
Book 04 Candidate Reviews 01–03 — OWNER ACCEPTED
Book 04 vNext Candidate 04 — OWNER ACCEPTED EDITORIAL BASELINE
```

The Workplace Sovereignty clarification remains compatible with Book 02 and does not require an immediate Book 02 Change Proposal.

## Current Book Registry

| Book | Title | Status |
| --- | --- | --- |
| Book 01 | MarkOrbit — The Operating System for Global Brand Services | RC1 — Portfolio Baseline Accepted |
| Book 02 | MarkOrbit Core Specification | Frozen Core Specification Baseline v0.1 |
| Book 03 | MarkOrbit Execution System | RC1 — Portfolio Baseline Accepted |
| Book 04 | MarkOrbit Workplace and Product Architecture | vNext Candidate 04 — Owner Accepted / Materialization in Review |
| Book 05 | MarkReg | RC1 — Approved and Frozen |
| Book 06 | MarkOrbit Lite | RC1 — Approved and Frozen |
| Book 07 | Mark Global Service Network | RC1 — Approved and Frozen |

## Book 04 Workplace Sovereignty vNext

### Accepted programme

```text
WP-A–WP-F — OWNER MERGED / CLOSED
INTEGRATION-01–02C — OWNER MERGED
CANDIDATE-01 — OWNER MERGED / DIAGNOSTIC BUILD
CANDIDATE-REVIEW-01 — OWNER MERGED / REVISE
CANDIDATE-02 — OWNER MERGED / ROUTE-AWARE BUILD
CANDIDATE-REVIEW-02 — OWNER MERGED / REVISE
CANDIDATE-03 — OWNER MERGED / EDITORIAL CONSOLIDATION BUILD
CANDIDATE-REVIEW-03 — OWNER MERGED / REVISE
CANDIDATE-04 — OWNER MERGED / FINAL CONSISTENCY BUILD
OWNER-ACCEPTANCE-01 — ACCEPT
```

Final editorial result:

```text
Chapters accepted: 40 / 40
Required correction classes: 12 / 12
Accepted amendment packages: 4 / 4
Editorial weave coverage: 40 / 40
Reader-text leakage findings: 0
Architecture authority regressions: 0
Remaining title contradictions: 0
Remaining stale transitions: 0
RC1 manuscript files changed: 0
Immediate Book 02 Change Proposal: NO
Owner Acceptance decision: ACCEPT
```

## Current Controlled Task

```text
PUB-TASK-B04-VNEXT-PUBLICATION-PREP-01
Materialize Accepted Manuscript and Prepare Freeze Candidate
```

Required result:

```text
Accepted chapters materialized: 40 / 40
Candidate 04 byte-equivalence: PASS
Materialization manifest coverage: PASS
RC1 source modifications: 0
Publication freeze readiness: YES
Freeze authorization: NOT YET GRANTED
```

The accepted Candidate 04 is being materialized in `books/book-04-workplace-product-architecture/accepted-vnext/`. The directory remains generated from accepted sources and is verified byte-for-byte against a fresh Candidate 04 build.

## Decision

```text
ACCEPT — Candidate 04 is the accepted Book 04 vNext editorial baseline.
Materialize accepted baseline: AUTHORIZED
Freeze: NOT YET AUTHORIZED
Public/commercial distribution: NOT YET AUTHORIZED
```

The immutable RC1 manuscript remains the historical portfolio baseline.

## Next Controlled Gates

```text
Owner merge of PUBLICATION-PREP-01
→ verify repository materialization and SHA-256 manifest
→ optional copyediting, references, front matter and rendering checks
→ explicit Book 04 vNext freeze decision
→ explicit publication and distribution decision
```

## Book 04 Decision Sequence

```text
WP-A–WP-F — ACCEPTED / CLOSED
→ Integration 01–02C — ACCEPTED
→ Candidate 01 — BUILD MILESTONE
→ Candidate Review 01 — REVISE
→ Candidate 02 — BUILD MILESTONE
→ Candidate Review 02 — REVISE
→ Candidate 03 — EDITORIAL CONSOLIDATION BUILD
→ Candidate Review 03 — REVISE
→ Candidate 04 — FINAL CONSISTENCY CORRECTION
→ Owner Acceptance — ACCEPT
→ Accepted manuscript materialization
→ Freeze decision
→ optional publication and distribution decision
```

## Future Publication and Architecture Workstreams

- Book 01 and Book 03 public-release copyediting and branded rendering;
- Book 04 accepted-vNext materialization, finishing and freeze decision;
- Books 05–07 optional final brand/design production and distribution decisions;
- Structured Information and Derived Value specifications;
- Local Vault architecture;
- Capability and Skill governance;
- Agent and Assistant architecture;
- Artifact and Delivery architecture;
- repository canonical alignment audits;
- implementation specifications in the relevant code repositories.

## Publication and Authority Boundary

No current roadmap phase authorizes unrestricted Product implementation, production deployment, public/commercial distribution, payment custody, automatic Provider appointment, autonomous professional action or External Protected Action.
