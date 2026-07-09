# B03-PLN-0005_Book_02_Dependency_Map

## Purpose

This scaffold maps Book 03 dependency on Book 02 Core Specification. It protects the Core boundary before Book 03 drafting begins.

## Dependency Principle

Book 03 consumes Book 02. Book 03 does not redefine Book 02.

Execution coordinates Core contracts. Execution does not own Core primitives. Execution does not expand AI authority. Codex must not infer new Core architecture from Book 03.

## Book 02 Source Areas Consumed by Book 03

### Core Domains

Book 03 may reference approved Core domains only as execution inputs, scopes, or constraints.

### Core Objects

Book 03 may coordinate execution around approved Core objects without redefining object identity, schema, lifecycle ownership, or source of truth.

### Core Services

Book 03 may reference approved services as execution dependencies without defining new service responsibilities.

### Workflow Contracts

Book 03 may consume approved workflow contracts to describe coordination, sequencing, review points, and safe failure boundaries.

### API Contracts

Book 03 may reference approved API contracts as integration constraints, not as new API specifications.

### Events

Book 03 may consume approved event contracts for trace, audit, and replay planning without creating new event types or event-emission authority.

### Tasks

Book 03 may consume approved task contracts to describe task lifecycle coordination.

### Permission / Policy

Book 03 may consume approved permission and policy contracts as execution gates.

### Human Review

Book 03 may consume approved human review contracts and identify where execution must stop for authorized review.

### AI Context / Agent Governance

Book 03 may consume approved AI context and agent governance contracts. It must keep AI and agents within assistance boundaries.

### Idempotency

Book 03 may consume approved idempotency contracts for retry-safe execution planning.

### Error and Versioning Contracts

Book 03 may consume approved error handling and versioning contracts for safe failure and change-control planning.

### Validation System

Book 03 may consume approved validation contracts as prerequisites and execution checkpoints.

## What Book 03 May Consume

- Approved Book 02 domains, objects, services, contracts, events, tasks, permissions, policies, validations, and governance constraints.
- Approved execution primitives and state boundaries defined by Book 02.
- Approved human review and AI/agent governance limits.
- Approved idempotency, error, and versioning rules.

## What Book 03 Must Not Redefine

- Core domains, objects, object schemas, or source-of-truth rules.
- Core services or service boundaries.
- API contracts or workflow contracts.
- Event contracts, event authority, or event emission rules.
- Task contracts, validation contracts, permission models, or policy models.
- Human review authority or professional truth.
- AI context, agent governance, or AI/agent execution authority.
- Idempotency, error, or versioning contracts.

## Open Questions

- Which exact Book 02 contract files are canonical dependencies for each Book 03 chapter?
- Which Book 02 workflow contracts are required for MVP execution patterns?
- Which Book 02 validation, permission, and policy gates are mandatory before execution drafting?
- Which Book 02 AI/agent governance clauses must be cited in Book 03 planning files?

## Review Checklist

- Confirm Book 03 consumes Book 02 and does not redefine it.
- Confirm execution coordinates Core contracts but does not own Core primitives.
- Confirm no new Core domains are introduced.
- Confirm AI/agent authority is not expanded.
- Confirm unresolved Core questions are routed back to Book 02 review.

## Next Action

Review this dependency map before Book 03 Round 1 drafting and link approved Book 02 source areas to the Book 03 execution glossary and MVP boundary.
