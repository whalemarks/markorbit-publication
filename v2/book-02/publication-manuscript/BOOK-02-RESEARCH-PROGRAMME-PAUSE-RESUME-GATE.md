# Book 02 — Research Programme Pause / Resume Gate

## 1. Purpose

This gate prevents Book 02 research from expanding indefinitely when downstream evidence, authority review or consumer ownership is missing.

It defines when the programme must pause, what may continue during a pause and what evidence is required to resume.

## 2. Programme states

```text
ACTIVE
LIMITED_RESEARCH
PAUSED
RESUME_REVIEW
RESUMED
CLOSED
SUPERSEDED
```

### ACTIVE

Approved research tasks may be handed off and reviewed.

### LIMITED_RESEARCH

Only mapping, fixtures, source review and noncanonical profiles may continue. No formal proposal may open.

### PAUSED

No new candidate, fixture family or downstream implementation task may be added unless required to resolve a stated blocker.

### RESUME_REVIEW

Returned evidence is evaluated against the resume criteria.

### RESUMED

A bounded next phase is approved with an explicit task list and stop condition.

### CLOSED

The candidate is retained as profile, rejected or completed through a formal governance outcome.

## 3. Mandatory pause triggers

Pause the relevant candidate track when any of the following occurs:

1. fewer than two independent L2 consumers after the planned consumer tasks complete;
2. target repository or accountable owner is not identified;
3. legal or professional review is required but unavailable;
4. the candidate cannot distinguish its lifecycle from a frozen Object;
5. proposed ownership remains ambiguous;
6. public Core export changes are requested before proposal acceptance;
7. research implementation attempts network, production or protected external action;
8. fixtures cannot preserve Unknown or reject illegal transitions;
9. the same candidate produces materially conflicting consumer meanings;
10. the evidence package is not reproducible from exact commits;
11. research begins generating more prose without resolving the current gate;
12. a new Architecture Canon decision supersedes the assumptions.

## 4. Current programme decision

As of Batch 15:

```text
Overall Book 02 publication reconstruction: LIMITED_RESEARCH
Frozen baseline replacement: PAUSED / NOT AUTHORIZED
Formal Change Proposal programme: PAUSED
Downstream fixture handoff: ACTIVE FOR APPROVED TASKS ONLY
External qualification research: LIMITED_RESEARCH
Bilateral Assignment formal gate: PAUSED
```

Approved active task:

```text
EXEC-RESEARCH-001
```

Defined but blocked tasks:

```text
MARKREG-RESEARCH-001
LITE-RESEARCH-001
CROSS-CONSUMER-REVIEW-001
B02-CP-RESEARCH-B1
```

## 5. Work allowed during pause

Allowed:

- exact frozen-source mapping;
- source, privacy and legal question preparation;
- noncanonical fixture correction;
- downstream evidence intake;
- evaluation using the accepted rubric;
- semantic delta logging;
- documentation-only clarification;
- deletion of abandoned research artifacts;
- repository-local task preparation after target confirmation.

Not allowed:

- creating new candidate root Objects;
- changing frozen controlled values;
- adding public Core exports;
- implementing production connectors;
- enabling external actions;
- opening an omnibus Change Proposal;
- calling research fixtures canonical;
- changing Book 03 runtime ownership;
- using downstream implementation as proof of authority.

## 6. Resume criteria by track

### 6.1 Production Authorization

Resume formal semantic analysis only when:

- EXEC-RESEARCH-001 returns accepted L2 evidence;
- a second independent consumer demonstrates the same profile need;
- Permission/Policy insufficiency is proven for at least one shared field;
- revocation behavior is tested;
- Assignment and Professional Authority remain separate.

Otherwise retain as Permission Profile.

### 6.2 Work Package

Resume F3 analysis only when:

- two consumers require package identity independent of Task;
- package-level acceptance is tested;
- Task replacement continuity is demonstrated;
- one owner and correction path are identified;
- compatibility with frozen Task is documented.

Otherwise retain as Task/Workflow Profile.

### 6.3 Bilateral Assignment

Resume the formal gate only when:

- two independent L2 consumer proofs exist;
- both require attributable offer and acceptance;
- both require a lifecycle independent of Task;
- ownership, revocation and replacement are resolved;
- cross-Workplace data and contact rules are tested;
- Professional Authority and Provider Appointment remain references only;
- compatibility score passes the formal gate.

### 6.4 Contribution and Outcome

Resume root-object analysis only when:

- two consumers require stable cross-boundary identity;
- profile composition is shown insufficient;
- exact version and supersession are required;
- relying-service ownership is stable;
- Outcome remains separate from formal-state mutation.

### 6.5 External Qualification and Professional Authority

Resume pre-proposal work only when:

- at least three jurisdiction samples are documented;
- official source hierarchy is tested;
- privacy and disciplinary-data review is complete;
- external state and platform verification state are separated;
- appointment and Matter scope are defined;
- legal and professional reviewers approve the representation boundary.

## 7. Resume packet

A request to resume must include:

```yaml
resume_request:
  track_id: string
  prior_state: PAUSED | LIMITED_RESEARCH
  blocker_resolved: [string]
  evidence_prs: [string]
  evidence_head_shas: [string]
  consumer_scores: [number]
  semantic_delta_log_ids: [string]
  remaining_risks: [string]
  requested_next_tasks: [string]
  stop_condition: string
```

The request must identify a bounded phase. “Continue research” is not an adequate scope.

## 8. Resume decisions

```text
RESUME_APPROVED
RESUME_APPROVED_WITH_LIMITS
REMAIN_PAUSED
CLOSE_AS_PROFILE
CLOSE_AS_PRODUCT_LOCAL
CLOSE_AS_BOOK_03_RUNTIME
REJECT_AND_ARCHIVE
SUPERSEDED_BY_NEW_AUTHORITY
```

## 9. Stop conditions

Every resumed phase must stop when:

- stated outputs are complete;
- a disqualifying authority violation appears;
- evidence contradicts the candidate's shared meaning;
- the target repository changes materially;
- required reviewer becomes unavailable;
- public contract change is requested without governance;
- the phase exceeds its named task set.

## 10. Publication status boundary

Book 02's publication manuscript may remain complete while semantic research is paused.

```text
Publication manuscript complete
≠ candidate programme must continue
```

The current first publication reconstruction does not depend on activating the research candidates.

## 11. Gate verdict

```text
Book 02 manuscript expansion: PAUSED
Approved downstream research handoff: LIMITED ACTIVE
Formal Change Proposal opening: PAUSED
Bilateral Assignment gate: PAUSED
Frozen replacement: NOT AUTHORIZED
Resume requires evidence packet: YES
```