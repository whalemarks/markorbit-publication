# MarkOrbit Publication Repository

This is the unified MarkOrbit publication repository.

It is a publication, specification, and architecture-governance repository, not a software Product repository. Its purpose is to manage publication structure, governance, shared editorial assets, review workflow, release artifacts, and owner-approved MarkOrbit architecture records across the book series.

## Repository Layout

- `architecture/` records owner-approved architecture canon, decision registers, and open questions.
- `books/` stores MarkOrbit books. Each book lives under `books/` in its own canonical directory.
- `shared/` stores shared publication assets, including glossary material, style guidance, templates, and diagrams.
- `reviews/` stores repository-level review-round materials and editorial review records.
- `release/` stores draft, release-candidate, and published release artifacts.
- `codex/` stores explicit Codex prompts, tasks, and reports for repository maintenance work.

## Current Architecture Status

The current repository-level architecture baseline is [MarkOrbit Orbital Professional Operating Architecture vNext](architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.md), recorded as an Owner Confirmed Canonical Working Baseline effective 2026-07-13.

The Canon establishes `Orbital` as the primary architecture language, records “各行其道，彼此牵引，共同演进”, defines each Organization Workplace as an independent Orbit, and preserves Book 02 as the frozen Core Specification Baseline v0.1. It does not authorize unrestricted implementation, production deployment, or external protected action.

## Publication Responsibility

This repository coordinates publication-level structure, specifications, and governance across the MarkOrbit book series. Individual books retain responsibility for their own manuscripts and book-specific specifications.

## Current Book Status

- Book 01 — MarkOrbit — The Operating System for Global Brand Services (`books/book-01-operating-system/`) is an existing draft; publication maturity has not been reassessed.
- Book 02 — MarkOrbit Core Specification (`books/book-02-core-specification/`) is the Frozen Core Specification Baseline v0.1.
- Book 03 — MarkOrbit Execution System (`books/book-03-execution-system/`) is Complete Draft 1 / Owner Accepted, pending final publication preparation and separate implementation-readiness work.
- Book 04 — MarkOrbit Workplace and Product Architecture ([`books/book-04-workplace-product-architecture/`](books/book-04-workplace-product-architecture/README.md)) is Release Candidate 1. CH00–CH39 publication finishing and B04-REV-0004 RC1 validation are complete; owner final publication review is pending.
- Book 05 — MarkReg (`books/book-05-markreg/`) is planned.
- Book 06 — MarkOrbit Lite (`books/book-06-markorbit-lite/`) is planned.
- Book 07 — Mark Global Service Network (`books/book-07-mark-global-service-network/`) is planned.

## Current Book 04 Gate

```text
architecture and targeted review revisions owner accepted
→ native-English and publication finishing completed
→ Release Candidate 1 validation passed
→ owner final publication review
→ final publication approval and merge
```

Book 04 is ready for owner final publication review. It is not approved for final publication without owner approval, unrestricted implementation, production deployment, or external protected action.
