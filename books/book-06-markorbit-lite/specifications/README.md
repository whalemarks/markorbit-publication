# Book 06 Controlled Specifications

The Product Charter defines what MarkOrbit Lite is. These Specifications define the controlled Product records, journeys, scenarios, Handoffs and evaluation baseline that may be used by the later chapter map and manuscript.

Specifications are publication-level authority. They are not database schemas, API contracts or implementation authorization.

## Current Candidate Baseline

| Specification | Scope |
| --- | --- |
| B06-SPEC-0001 | Product-local records, controlled IDs, ownership and formalization boundaries |
| B06-SPEC-0002 | Reference journeys, state transitions, variants and failure paths |
| B06-SPEC-0003 | Conformance scenarios and zero-tolerance tests |
| B06-SPEC-0004 | Work-product production, Handoff/Return, MVP evaluation, commercial experiments and historical V1 reconciliation |

## Controlled Ranges

```text
ML-S01–S05      Session, Today and interaction
ML-O01–O08      observations, signals and value candidates
ML-W01–W10      work products, Prepared Actions and rendering
ML-M01–M08      memory, case lessons and reusable Assets
ML-H01–H08      Handoff, Return and destination continuity
ML-E01–E06      evaluation and commercial experiments

ML-J01–J04      reference journeys
ML-SCN-01–24    conformance scenarios
ML-HC-01–HC-08  Handoff contracts
ML-AC-01–AC-12  MVP acceptance criteria
```

## Authority Rule

```text
Books 01–05 and Product Charter v0.3
→ B06-SPEC-0001–0004
→ future chapter map
→ manuscript
→ implementation specification / ADR
```

A controlled Lite record does not create parallel Core, Execution, MarkReg or MGSN truth.

Merge of the Product Baseline PR accepts these Specifications as the Book 06 Product Baseline v0.1. It authorizes a chapter-map candidate, not manuscript drafting or implementation.
