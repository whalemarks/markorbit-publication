# Book 03 Engineering Source Map

## 1. Authority lock

The engineering source is the frozen `B03-RC1-FROZEN-01` baseline under `books/book-03-execution-system/`.

Precedence:

```text
Book 02 frozen authority and completed markorbit-core exports
→ Book 03 frozen manuscript
→ approved engineering decisions and task specifications
→ fixtures and validators
→ executable tests
→ implementation code
```

Execution coordinates approved Core contracts. It does not redefine Core Objects, owning Services, controlled states, Events, Permission, Policy or Human Review.

## 2. Repository boundary

Book 03 CH34 requires a dedicated Execution implementation repository. The intended boundary is `markorbit-execution` or an equivalently dedicated repository approved by the Owner.

The following are not valid runtime locations:

- `markorbit-core`;
- `markorbit-publication`;
- a Product repository;
- an Integration or connector repository.

The publication repository may retain source maps, governance notes, planning records and architecture reviews only.

## 3. Engineering transformation by chapter group

| Chapters | Engineering output |
|---|---|
| CH00–CH07 | authority hierarchy, system boundary, execution invariants and Core-consumption rules |
| CH08–CH10 | execution component map, reference-based progress projection and workflow coordination lifecycle |
| CH11–CH16 | Task, Human Review, Communication, Event trace, Permission/Policy and Human–AI handoff contracts |
| CH17–CH24 | eight workflow specifications |
| CH25–CH30 | idempotency, retry, safe failure, versioning, review governance, agent boundary and observability |
| CH31–CH34 | MVP depth lock, workflow registry, readiness gates and formal implementation roadmap |

## 4. Non-object rule

Book 03 does not create a second Core object model. In particular:

- no universal `ExecutionObject`;
- no universal status enum replacing object-specific states;
- no Execution-owned copy of Trademark, Matter, Order, Task, Communication, Workflow Contract, Event or Human Review;
- no Workflow-owned mutation authority.

Execution may define reference-based, versioned and time-bounded coordination projections such as an Execution Progress View. Such projections are not authoritative Core state.

## 5. Coordination lifecycle

The common coordination lifecycle is:

```text
resolve
→ preview
→ review
→ apply
→ delegate
→ observe
→ expose outcome
```

Apply is not implied by preview. Owning Services perform mutations. Task Service owns active Task creation. Human Review gates protected work. Events are trace, not commands.

## 6. MVP workflow lock

### Depth A — internal apply allowed

| Workflow | Allowed result | Explicit stop |
|---|---|---|
| Intake Execution | governed internal preparation through owning Services | no external action |
| Application Preparation | governed internal application-preparation effects | no filing, payment or provider engagement |
| Communication Review | governed internal review transition | no external send |

### Depth B — preview only

| Workflow | Allowed result | Apply |
|---|---|---|
| Provider Routing Preparation | candidate comparison and review questions | disabled |
| Office Action Response Preparation | issue, source, option and evidence-gap preview | disabled |
| Renewal Preparation | readiness, source and gap preview | disabled |
| Assignment Preparation | party, document and recordal-readiness preview | disabled |
| Evidence Review Preparation | inventory, contradiction and review-question preview | disabled |

### Depth C — deferred

External send, official filing/submission, payment, provider engagement/instruction, recordal, filing of renewal or office-action response, Evidence certification, unrestricted Core mutation and autonomous professional execution remain outside the MVP.

## 7. Required engineering asset families

The dedicated Execution repository must eventually contain:

1. canonical-source manifest;
2. repository-boundary and change-control rules;
3. workflow-depth registry;
4. Execution operation, context, preview, apply and safe-error contracts;
5. Core-consumption boundary pinned to approved `markorbit-core` exports;
6. version, Permission, Policy, Human Review, idempotency and audit coordinators;
7. all eight side-effect-free previews;
8. a common Depth B apply lock;
9. three Depth A internal apply coordinators;
10. constrained AI/Agent assistance adapters;
11. deterministic fixtures, validators and negative boundary tests;
12. pilot-readiness and final MVP audit evidence.

## 8. Task sequencing decision

The formal CH34 task sequence remains authoritative. This source-map task does not renumber it.

Immediate next formal task:

```text
EXEC-TASK-001 — Initialize Execution Repository
```

Then:

```text
EXEC-TASK-002 — Canonical Source Manifest
EXEC-TASK-003 — Repository Boundary Architecture Note
EXEC-TASK-004 — Execution Change-Control Rules
EXEC-TASK-005 — Initial Fixture and Validation Harness
```

No runtime behavior begins before the Phase 0 gate passes.

## 9. Traceability rule

Every future Execution artifact must trace:

```text
Book 03 chapter
→ engineering requirement id
→ Execution contract or coordinator
→ Core dependency/export
→ fixture
→ positive and negative tests
→ implementation PR
```

A missing or conflicting Core export produces `blocked by Core dependency`; it does not authorize local reimplementation.
