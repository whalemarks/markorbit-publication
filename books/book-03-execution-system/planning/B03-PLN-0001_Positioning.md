# B03-PLN-0001_Positioning

## Purpose

This planning scaffold defines the position of Book 03 — MarkOrbit Execution System for Round 0 Fix Pack 01. It is not full book content and does not define Core architecture, product UI, or implementation code.

Book 03 sits between Book 02 Core Specification and Book 04 Product System. It defines how MarkOrbit turns Core contracts into governed operational execution across workflows, tasks, reviews, communications, events, and human-AI collaboration.

## Positioning Statement

Book 03 defines governed execution. It does not define Core primitives, and it does not define product UI.

Book 03 consumes Book 02 contracts and execution primitives, including domain, object, service, workflow, API, event, task, permission, policy, human review, AI context, agent governance, idempotency, validation, error, and versioning contracts. Book 03 coordinates those contracts in execution patterns without redefining them.

Book 03 prepares execution patterns that Book 04 product surfaces may consume. Book 04 may later decide how those patterns appear in product experiences.

## Book 02 Boundary

Book 03 does not redefine domains, objects, services, API contracts, workflow contracts, events, tasks, validation rules, permission models, policy models, human review requirements, idempotency rules, versioning contracts, error contracts, AI context, or agent governance already owned by Book 02.

Codex must not infer new Core architecture from Book 03 planning material. Any missing Core concept remains an open dependency question for Book 02 rather than a Book 03 invention.

## Book 04 Boundary

Workplace is a future product surface, not the main subject of Book 03.

Book 03 does not define customer portal UI, partner center UI, provider network UI, mini-program UI, app screens, API console screens, product packaging, or product UX specifications.

Book 03 may reference Book 04 only to state that product surfaces may consume execution patterns and must not redefine execution governance.

## AI / Agent Authority Boundary

Book 03 does not grant AI or agents authority to approve, send, submit, mutate protected state, emit Events, or define professional truth.

AI and agents may be described only as assistance mechanisms operating within Book 02 governance, human review, permission, policy, audit, and event boundaries.

## Open Questions

- Which Book 02 contracts must be approved before Book 03 drafting begins?
- Which Book 04 surfaces are allowed to consume MVP execution patterns first?
- What execution glossary terms require Book 02 source confirmation?
- What minimum MVP execution boundary must be approved before Round 1 drafting?

## Review Checklist

- Confirm this file remains a scaffold only.
- Confirm Book 03 is positioned between Book 02 Core Specification and Book 04 Product System.
- Confirm no Book 02 content is rewritten.
- Confirm no new Core domains are defined.
- Confirm no product UI specification is created.
- Confirm Workplace remains a future product surface, not Book 03's subject.
- Confirm AI and agents remain assistance mechanisms that cannot approve, send, submit, mutate protected state, emit Events, or define professional truth.

## Next Action

Submit this strengthened positioning scaffold for Book 03 Round 0 Fix Pack 01 review.
