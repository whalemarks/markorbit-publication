# Book 02 — Follow-up Dependency Register

## 1. Purpose

This register records every dependency that must be satisfied before paused Book 02 research may resume or a formal Change Proposal may open.

## 2. Dependency table

| Dependency ID | Dependency | Blocks | Current state | Completion evidence |
|---|---|---|---|---|
| DEP-EXEC-01 | `markorbit-execution` acknowledges EXEC-RESEARCH-001 | execution L2 proof | open | target branch and accepted task packet |
| DEP-EXEC-02 | five-profile deterministic fixture PR | Production Authorization, Work Package, Assignment, Contribution and Outcome evaluation | open | PR, fixtures, tests, validation report |
| DEP-MR-01 | MarkReg implementation repository confirmed | MARKREG-RESEARCH-001 | blocked | repository, baseline SHA and local research path |
| DEP-MR-02 | MarkReg filing-readiness L2 proof | cross-consumer gate | blocked | accepted fixture PR and evidence return |
| DEP-LITE-01 | Lite repository-local baseline confirmed | LITE-RESEARCH-001 | blocked | baseline SHA, commands and research path |
| DEP-LITE-02 | Lite content-package L2 proof | cross-consumer gate | blocked | accepted fixture PR and evidence return |
| DEP-CROSS-01 | two independent L2 consumers | shared-profile evaluation | blocked | two accepted evidence returns |
| DEP-CROSS-02 | cross-consumer field/lifecycle/ownership review | bilateral Assignment and other F3 candidates | blocked | completed checklist and decision log |
| DEP-A1-01 | three-jurisdiction qualification source sample | external Qualification reference | open | source matrix and legal review notes |
| DEP-A1-02 | privacy and disciplinary-data analysis | external Qualification reference | open | reviewed privacy memorandum |
| DEP-A2-01 | appointment and Matter-scope model | Professional Authority reference | blocked by A1 | research record and professional review |
| DEP-B1-01 | bilateral Assignment ownership decision | formal Assignment proposal | blocked | owning-service and mutation matrix |
| DEP-B1-02 | bilateral Assignment compatibility/migration analysis | formal Assignment proposal | blocked | compatibility and migration evidence |
| DEP-EDIT-01 | final copyedit, glossary and index | designed publication release | open | editorial review record |
| DEP-EDIT-02 | diagrams, typesetting and rendered proof | designed publication release | open | reviewed render artifact |
| DEP-LEGAL-01 | legal/professional review of authority language | final publication and proposals | open | signed or attributable review record |

## 3. Critical path

```text
EXEC acknowledgement
→ execution fixture PR
→ first L2 evidence

MarkReg or Lite baseline confirmation
→ second consumer fixture PR
→ second L2 evidence

Two L2 returns
→ cross-consumer review
→ semantic-delta decision
→ possible pre-proposal
```

For authority work:

```text
source hierarchy
→ jurisdiction samples
→ privacy/legal review
→ external Qualification reference decision
→ appointment/Matter-scope analysis
→ Professional Authority decision
```

## 4. Dependency rules

1. A blocked dependency may not be bypassed with publication prose.
2. One consumer cannot count twice through two scenarios in the same implementation.
3. A fixture PR without negative coverage does not satisfy L2.
4. A legal review dependency cannot be replaced by model confidence or Provider practice.
5. Completion evidence must be versioned and attributable.
6. Any contradiction with frozen Book 02 creates a new D4 dependency and stops the affected workstream.
7. Production adoption is outside this register and requires separate authorization.

## 5. Current blockers by candidate

| Candidate | Blocking dependencies |
|---|---|
| Production Authorization | DEP-EXEC-02 plus second consumer evidence if shared semantics are proposed |
| Work Package | DEP-EXEC-02, DEP-MR-02 or DEP-LITE-02, DEP-CROSS-02 |
| Bilateral Assignment | DEP-CROSS-01, DEP-CROSS-02, DEP-B1-01, DEP-B1-02 |
| Contribution | DEP-CROSS-01 and stable identity proof |
| Outcome | DEP-CROSS-01 and purpose-limited identity proof |
| External Qualification | DEP-A1-01, DEP-A1-02, DEP-LEGAL-01 |
| Professional Authority | A1 completion, DEP-A2-01, DEP-LEGAL-01 |
| final designed edition | DEP-EDIT-01, DEP-EDIT-02, DEP-LEGAL-01 |

## 6. Dependency closure template

```yaml
dependency_id: string
status: COMPLETE | REJECTED | SUPERSEDED
completed_by: string
completed_at: datetime
evidence_references: []
source_versions: []
review_result: string
remaining_limitations: []
unblocked_workstreams: []
```

## 7. Register verdict

```text
Dependencies currently complete enough to open formal proposal: NO
EXEC task ready to address first dependency: YES
Second independent consumer ready for handoff: NO
Authority legal dependencies complete: NO
Final designed publication dependencies complete: NO
```
