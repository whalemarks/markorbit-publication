# Book 02 — Research Programme Status Board

## 1. Purpose

This board is the current operational snapshot for the Book 02 v2 research programme after completion of the publication reconstruction, frozen-baseline trace, candidate mapping, pre-proposal research, noncanonical fixtures and downstream handoff design.

It is a status and control document. It does not modify `B02-BASELINE-V0.1`, open a Change Proposal, alter `@markorbit/core`, or authorize downstream implementation.

## 2. Programme state

```text
Publication reconstruction: COMPLETE
Frozen baseline identification: COMPLETE
Chapter-level disposition: COMPLETE
Candidate-to-frozen mapping: COMPLETE
Current Core implementation mapping: COMPLETE
Authority drift audit: COMPLETE FOR CURRENT GATE
Pre-proposal research: COMPLETE FOR CP-A / CP-B
Noncanonical fixture design: COMPLETE
Downstream task specification: COMPLETE
Evidence intake and scoring controls: COMPLETE
Manuscript expansion: PAUSED
Formal Change Proposal programme: PAUSED
Production implementation: NOT AUTHORIZED
Frozen replacement: NOT AUTHORIZED
```

Overall state:

```text
LIMITED_RESEARCH
```

Only evidence-generating downstream work and source/legal review may continue.

## 3. Workstream board

| Workstream | Current state | Blocking evidence | Next permitted action |
|---|---|---|---|
| EXEC-RESEARCH-001 | READY_FOR_HANDOFF | repository-local acknowledgement | hand off exact packet to `markorbit-execution` |
| MARKREG-RESEARCH-001 | BLOCKED_TARGET_BASELINE | target implementation repository and local baseline | confirm repository and research path |
| LITE-RESEARCH-001 | BLOCKED_LOCAL_BASELINE | repository-local research path, test command and owner | confirm baseline before handoff |
| CROSS-CONSUMER-REVIEW-001 | BLOCKED_EVIDENCE | two independent L2 evidence returns | wait and intake evidence |
| B02-CP-RESEARCH-A1 | LIMITED_RESEARCH | source, privacy, legal and professional review | conduct jurisdiction sample review |
| B02-CP-RESEARCH-A2 | PAUSED_DEPENDENCY | A1 plus appointment/Matter-scope analysis | do not open formal proposal |
| B02-CP-RESEARCH-B1 | PAUSED_EVIDENCE | two independent L2 consumers and ownership/compatibility proof | wait for consumer evidence |
| Production Authorization profile | PROFILE_RESEARCH | execution fixture proof | validate Permission-profile sufficiency |
| Work Package profile | PROFILE_RESEARCH | two-consumer package-level continuity proof | validate without replacing Task |
| Contribution profile | PROFILE_RESEARCH | cross-consumer submission identity proof | retain Document/Evidence ownership |
| Outcome profile | PROFILE_RESEARCH | cross-consumer purpose-limited acceptance proof | retain formal-state separation |

## 4. Candidate board

| Candidate | Current disposition | Canonical status |
|---|---|---|
| Need | F3 candidate; no active proposal | noncanonical |
| Engagement | F3 candidate; no active proposal | noncanonical |
| Work Package | F2 Task/Workflow profile preferred | noncanonical |
| Assignment | simple assignment remains Task fields; bilateral form is F3 research | noncanonical |
| Contribution | F2 submission profile preferred | noncanonical |
| Outcome | F2 acceptance profile preferred | noncanonical |
| Professional Authority | narrow external-reference research only | noncanonical |
| Relationship Owner | contextual role candidate | noncanonical |
| Delivery Owner | contextual role candidate | noncanonical |
| Capability Certification | profile study | noncanonical |
| Production Authorization | Permission profile preferred | noncanonical |
| Resale Authorization | Product-local or profile pending demand | noncanonical |

## 5. Evidence levels

```text
L0 — assertion only
L1 — documented use case
L2 — deterministic fixture proof in one consumer
L3 — repeated proof in two independent consumers
L4 — accepted shared contract
L5 — production adoption with monitored conformance
```

Current verified level:

| Consumer | Level |
|---|---:|
| Book 03 / `markorbit-execution` | L1 |
| MarkReg publication architecture | L1 |
| Lite repository/publication architecture | L1 |
| two independent consumers | not achieved |

No candidate may advance to formal shared-contract consideration through two narratives alone.

## 6. Active locks

```text
Task remains canonical.
Human Review remains canonical.
Permission controlled values remain unchanged.
Book 03 owns runtime Eligibility and execution.
Owning Services own formal-state mutation.
Brain results remain noncanonical.
Provider Return does not establish official truth.
Assignment does not create Professional Authority.
Production Authorization does not create Assignment.
Outcome acceptance does not perform Apply.
```

## 7. Repository authority

```text
Frozen publication authority:
books/book-02-core-specification/
B02-BASELINE-V0.1

Publication research workspace:
v2/book-02/publication-manuscript/

Engineering implementation:
whalemarks/markorbit-core
@markorbit/core@0.1.0

Execution consumer target:
whalemarks/markorbit-execution
```

The research workspace may explain, compare and prepare evidence. It may not replace the frozen authority.

## 8. Pause conditions

The programme remains paused when any of the following is true:

- no downstream L2 evidence exists;
- target repository baseline is unknown;
- ownership or mutation authority is unresolved;
- a proposal relies only on publication prose;
- a candidate can still be represented as F1 composition or F2 profile;
- legal/professional review is missing for authority-related semantics;
- compatibility and migration evidence is absent;
- a proposed implementation would alter public Core exports.

## 9. Resume conditions

A workstream may resume only when its specific gate is satisfied and recorded in the handoff register.

Formal Change Proposal research additionally requires:

- exact frozen-source mapping;
- at least two independent L2 consumers where applicable;
- semantic-delta classification;
- ownership and lifecycle decision;
- positive and negative fixtures;
- compatibility and migration analysis;
- required legal/professional review;
- explicit owner approval to open a proposal.

## 10. Board verdict

```text
Book 02 manuscript needs more chapters now: NO
Book 02 research should continue without evidence: NO
EXEC-RESEARCH-001 may be handed off: YES
MarkReg task may be handed off now: NO
Lite task may be handed off now: NO
Formal Change Proposal may be opened now: NO
Frozen Core may be replaced: NO
```
