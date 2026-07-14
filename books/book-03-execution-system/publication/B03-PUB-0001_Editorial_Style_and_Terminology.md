# B03-PUB-0001 — Editorial Style and Terminology

**Status:** Release Candidate 1

## Purpose

Book 03 is an architecture and governance publication. It must remain precise enough for implementation planning without becoming implementation code or a Product manual.

## Style Rules

- Define one execution distinction fully, then cross-reference it.
- Use tables for state, ownership and boundary comparisons.
- Use code blocks for durable paths and constitutional locks.
- Capitalize governed concepts: Workflow, Task, Review, Communication, Event, Service, Permission and Policy.
- Use `preview` and `apply` as operation meanings, not casual synonyms.
- Use **Human Review** for accountable review.
- Use **Human–AI** with an en dash.
- Use **Owning Service** for the authority that changes formal business facts.
- Use **Product surface** only for a user-facing surface. Workplace itself is not reduced to one Product surface.
- Use **organization**, not tenant, as the primary architecture term.

## Required Distinctions

```text
Execution State ≠ Core Lifecycle State
Task Plan ≠ Active Task
Draft ≠ Approved Communication
Approval ≠ Send
Send ≠ Delivery
Preview ≠ Apply
Recommendation ≠ Decision
AI Output ≠ Human Review
Workflow Observation ≠ Domain Event
Product Presentation ≠ Execution Truth
```

## Book 04 Interpretation

Book 04 is **MarkOrbit Workplace and Product Architecture**.

Workplace provides authorized organization context and may expose Product and operating surfaces.

Products consume Execution.

Neither Workplace nor a Product surface may expand Execution depth.
