# MarkOrbit Publication Repository

This is the unified MarkOrbit publication repository.

It is a publication, specification and architecture-governance repository, not a software product repository. Its purpose is to manage the publication structure, governance, shared editorial assets, review workflow, release artifacts and owner-approved MarkOrbit architecture records for multiple MarkOrbit books.

## Repository Layout

- `architecture/` records owner-approved architecture canon, decision registers and open questions.
- `books/` stores MarkOrbit books. Each book lives under `books/` in its own book directory.
- `shared/` stores shared publication assets, including glossary material, style guidance, templates, and diagrams.
- `reviews/` stores review-round materials and editorial review records.
- `release/` stores draft, release-candidate, and published release artifacts.
- `codex/` stores explicit Codex prompts, tasks, and reports for repository maintenance work.

## Current Architecture Status

The current repository-level architecture baseline is [MarkOrbit Orbital Professional Operating Architecture vNext](architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.md), recorded as an Owner Confirmed Canonical Working Baseline effective 2026-07-13.

The Canon establishes `Orbital` as the primary architecture language, records “各行其道，彼此牵引，共同演进”, defines each Organization Workplace as an independent Orbit, and preserves Book 02 as the frozen Core Specification Baseline v0.1. It does not authorize unrestricted implementation, production deployment, or external protected action.

## Publication Responsibility

This repository coordinates publication-level structure, specifications and governance across the MarkOrbit book series. Individual books retain responsibility for their own manuscripts and book-specific specifications.

## Book Content

Existing book content is preserved. Book migration, manuscript cleanup, architecture changes and product implementation are handled only through explicit future tasks.

## Current Book Status

- Book 01 — MarkOrbit — The Operating System for Global Brand Services (`books/book-01-operating-system/`) is an existing draft; publication maturity was not reassessed by the Architecture Canon vNext task.
- Book 02 — MarkOrbit Core Specification (`books/book-02-core-specification/`) is the Frozen Core Specification Baseline v0.1.
- Book 03 — MarkOrbit Execution System (`books/book-03-execution-system/`) is Complete Draft 1 / Owner Accepted, pending final publication preparation, and not execution-ready pending dependency review.
- Book 04 — MarkOrbit Workplace and Product Architecture ([`books/book-04-workplace-product-architecture/`](books/book-04-workplace-product-architecture/README.md)) is Scaffolded Planning Baseline; architecture direction locked; manuscript not started.
- Book 05 — MarkReg (`books/book-05-markreg/`) is planned.
- Book 06 — MarkOrbit Lite (`books/book-06-markorbit-lite/`) is planned.
- Book 07 — Mark Global Service Network (`books/book-07-mark-global-service-network/`) is planned.
