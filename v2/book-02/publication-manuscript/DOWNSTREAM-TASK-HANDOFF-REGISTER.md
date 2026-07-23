# Book 02 — Downstream Task Handoff Register

## 1. Purpose

This register controls how Book 02 research tasks move from publication design into downstream repositories and how evidence returns without silently changing frozen Core semantics.

It is a coordination record only. It does not create a cross-repository workflow runtime, authorize production implementation or change any downstream branch.

## 2. Handoff principles

```text
Publication Task Definition
≠ Downstream Task Accepted
≠ Downstream Task Implemented
≠ Consumer Proof Accepted
≠ Core Change Proposal Opened
```

Every handoff must preserve:

- source specification and version;
- target repository;
- task owner;
- allowed scope;
- prohibited scope;
- expected branch and PR;
- fixture and evidence requirements;
- acceptance authority;
- return state;
- correction and cancellation route.

## 3. Controlled handoff states

```text
DEFINED
READY_FOR_HANDOFF
HANDED_OFF
ACKNOWLEDGED
IN_PROGRESS
PR_OPEN
EVIDENCE_RETURNED
UNDER_REVIEW
ACCEPTED
REJECTED
NEEDS_REVISION
PAUSED
CANCELLED
SUPERSEDED
```

State meanings:

- `DEFINED` — task exists in publication but is not ready for downstream use;
- `READY_FOR_HANDOFF` — scope, exclusions and acceptance criteria are complete;
- `HANDED_OFF` — instructions were delivered to the target repository or executor;
- `ACKNOWLEDGED` — target confirms receipt and intended interpretation;
- `IN_PROGRESS` — research implementation has started;
- `PR_OPEN` — a downstream PR exists;
- `EVIDENCE_RETURNED` — required fixtures, validation output and review evidence were submitted;
- `UNDER_REVIEW` — Book 02 research reviewers are assessing the return;
- `ACCEPTED` — evidence satisfies the research gate only;
- `REJECTED` — evidence does not satisfy the gate;
- `NEEDS_REVISION` — bounded corrections are required;
- `PAUSED` — programme pause gate applies;
- `CANCELLED` — task is no longer pursued;
- `SUPERSEDED` — replaced by a later task version.

```text
ACCEPTED
≠ canonicalized
≠ production-ready
≠ merged into Core
```

## 4. Handoff records

### 4.1 EXEC-RESEARCH-001

```text
Task: fixture-only parsing and validation of five noncanonical profiles
Target repository: whalemarks/markorbit-execution
Source: EXEC-RESEARCH-001-CODEX-TASK.md
Current handoff state: READY_FOR_HANDOFF
Canonical status: NONCANONICAL
Production status: DISABLED
```

Required return:

- downstream branch name;
- PR URL and head SHA;
- exact changed filenames;
- fixture inventory;
- positive and negative validation results;
- deterministic reason-code output;
- proof of no network access and no protected action;
- review threads, reviews and workflow status;
- merge decision;
- deviations from the source task.

Acceptance authority:

```text
Book 02 research review
+ Book 03 repository-local review
```

### 4.2 MARKREG-RESEARCH-001

```text
Task: filing-readiness consumer proof
Target repository: future confirmed MarkReg implementation repository
Source: MARKREG-RESEARCH-001-FILING-READINESS-CONSUMER-PROOF-SPEC.md
Current handoff state: DEFINED
Blocker: target repository and local baseline not confirmed
Canonical status: NONCANONICAL
Production status: DISABLED
```

Required return:

- repository and baseline confirmation;
- filing-readiness fixture chain;
- proof that customer instruction and official filing remain separate;
- Product-local record inventory;
- schema mapping to frozen Task, Evidence and Human Review;
- no external submission path.

### 4.3 LITE-RESEARCH-001

```text
Task: source-backed content-package consumer proof
Target repository: whalemarks/markorbit-lite
Source: LITE-RESEARCH-001-SOURCE-BACKED-CONTENT-CONSUMER-PROOF-SPEC.md
Current handoff state: DEFINED
Blocker: repository-local baseline and executable research location not confirmed
Canonical status: NONCANONICAL
Production status: DISABLED
```

Required return:

- source-backed content fixture;
- exact source and model provenance;
- unsupported-claim rejection case;
- Contribution supersession case;
- publication-readiness without publication;
- preservation of Product-local Content records.

### 4.4 CROSS-CONSUMER-REVIEW-001

```text
Task: compare Execution, MarkReg and Lite evidence
Target: publication research programme
Source: CROSS-CONSUMER-REVIEW-001-CHECKLIST.md
Current handoff state: DEFINED
Blocker: fewer than two independent L2 consumer returns
```

The task may start only after at least two consumer proofs reach `EVIDENCE_RETURNED`.

### 4.5 B02-CP-RESEARCH-B1

```text
Task: accepted bilateral / cross-Workplace Assignment formal gate
Target: Book 02 Change Proposal research
Source: BILATERAL-ASSIGNMENT-FORMAL-GATE.md
Current state: PAUSED
Blocker: independent consumer proof and ownership decision incomplete
```

## 5. Handoff packet minimum fields

```yaml
handoff:
  handoff_id: string
  task_id: string
  task_version: string
  source_repository: string
  source_path: string
  source_commit_sha: string
  target_repository: string
  target_base_ref: string
  expected_branch: string
  allowed_paths: [string]
  prohibited_paths: [string]
  required_outputs: [string]
  required_checks: [string]
  acceptance_authority: [string]
  canonical: false
  production_enabled: false
  external_actions_enabled: false
  state: string
```

## 6. Acknowledgement rules

A downstream acknowledgement must explicitly confirm:

- the task is research-only;
- no public Core export will be changed;
- no frozen Book 02 file will be edited;
- no protected external action is permitted;
- local implementation may be rejected without migration obligation;
- the executor understands expected evidence and stop conditions.

Silence, branch creation or a partial commit is not acknowledgement.

## 7. Amendment and cancellation

If the handoff scope changes, the source task version must change and the target must acknowledge the new version.

```text
Source task amended
≠ active downstream work automatically re-scoped
```

Cancellation must identify:

- whether a downstream branch or PR exists;
- whether temporary research types remain;
- whether fixtures or artifacts must be removed;
- whether any result was reused elsewhere;
- whether a superseding task exists.

## 8. Register verdict

```text
EXEC-RESEARCH-001: READY_FOR_HANDOFF
MARKREG-RESEARCH-001: DEFINED / TARGET BLOCKED
LITE-RESEARCH-001: DEFINED / LOCAL BASELINE BLOCKED
CROSS-CONSUMER-REVIEW-001: BLOCKED BY EVIDENCE COUNT
B02-CP-RESEARCH-B1: PAUSED

Downstream implementation authorized: NO
Production execution authorized: NO
Formal Change Proposal opened: NO
```