# MarkReg / Lite — Target Repository Confirmation Checklist

## 1. Purpose

This checklist must be completed before `MARKREG-RESEARCH-001` or `LITE-RESEARCH-001` is handed to Codex or another implementation agent.

A publication use case is not enough. The target repository, local conventions, current baseline and research-only path must be verified first.

## 2. Universal confirmation gate

For each target consumer, record:

```text
repository full name
repository default branch
current baseline commit
repository owner
package manager
runtime language
existing test framework
existing fixture conventions
existing validation commands
allowed research path
forbidden paths
branch naming rule
PR title convention
required CI
current production-readiness status
```

Handoff is blocked when any required field is Unknown.

## 3. MarkReg checklist

### Repository identity

- [ ] Exact MarkReg implementation repository confirmed.
- [ ] Default branch confirmed.
- [ ] Current head SHA recorded.
- [ ] Repository status distinguishes implementation from publication material.
- [ ] Existing frozen or accepted MarkReg baseline identified.

### Local structure

- [ ] Package manager and install command confirmed.
- [ ] Typecheck command confirmed.
- [ ] Lint command confirmed.
- [ ] Test command confirmed.
- [ ] Fixture validation convention confirmed.
- [ ] Suitable fixture-only research directory identified.
- [ ] Existing Matter, Task, Document, Evidence and filing-package types inspected.

### Consumer use case

The approved research scenario is:

```text
Reviewable International Trademark Filing Package
```

The local implementation must preserve:

```text
Filing-readiness Outcome
≠ Customer Final Instruction
≠ Professional Filing Approval
≠ Official Filing
```

- [ ] Local Product records remain Product-local.
- [ ] Provider Package remains Product-local.
- [ ] Fee Quote remains Product-local.
- [ ] Customer Instruction remains Product-local or Owning-Service-owned.
- [ ] Official filing and receipt reconciliation remain outside the fixture proof.
- [ ] No production connector is required.

### Authority and data

- [ ] Customer and Matter data used only as synthetic fixtures.
- [ ] No real client or confidential data.
- [ ] Professional Authority represented only by test references.
- [ ] No actual filing, payment, communication or Provider appointment.
- [ ] Unknown and missing-document cases included.

### Handoff decision

```text
MARKREG-RESEARCH-001:
READY_FOR_HANDOFF / BLOCKED
```

Current programme status:

```text
BLOCKED_TARGET_BASELINE
```

## 4. Lite checklist

### Repository identity

- [ ] `whalemarks/markorbit-lite` confirmed as the intended repository.
- [ ] Default branch confirmed.
- [ ] Current head SHA recorded.
- [ ] README or equivalent repository authority resolved.
- [ ] Current implementation sprint and accepted architecture identified.

### Local structure

- [ ] Package manager confirmed.
- [ ] Typecheck, lint and test commands confirmed.
- [ ] Existing `kernel`, `workspace`, `persistence`, `brain`, `intelligence`, `capability`, `workflow` and `guide` boundaries inspected where present.
- [ ] Existing fixture conventions confirmed.
- [ ] Suitable research-only path identified.
- [ ] Public Product code and research fixtures kept separate.

### Consumer use case

The approved research scenario is:

```text
Source-backed Trademark Content Package
```

The local implementation must preserve:

```text
Publication-readiness Outcome
≠ Published
≠ Marketing Consent
≠ Professional Opinion
```

- [ ] Content Brief remains Product-local.
- [ ] Audience Profile remains Product-local.
- [ ] Campaign Asset remains Product-local.
- [ ] Publishing schedule remains Product-local.
- [ ] Performance metrics remain Product-local.
- [ ] Sources and Brain-result types remain visible.
- [ ] AI draft never becomes automatic publication approval.

### Authority and data

- [ ] Only synthetic or openly permitted source fixtures used.
- [ ] Source authority class included.
- [ ] Citation and provenance preserved.
- [ ] Unsupported Claim negative fixture included.
- [ ] Copyright, redistribution and AI-training permissions are not inferred.
- [ ] No external publishing or marketing action.

### Handoff decision

```text
LITE-RESEARCH-001:
READY_FOR_HANDOFF / BLOCKED
```

Current programme status:

```text
BLOCKED_LOCAL_BASELINE
```

## 5. Independence test

The two consumer proofs count as independent only when:

- they live in distinct Product or Execution repositories;
- they use different Product contexts;
- their fixtures are independently implemented;
- they do not share one hidden implementation that merely replays the same schema;
- each shows why the profile is useful locally;
- each preserves the same shared boundary without sharing Product-local fields.

```text
same prose copied twice
≠ two independent consumers
```

## 6. Blockers that prohibit handoff

Do not hand off when:

- repository identity is uncertain;
- no accepted baseline is known;
- no test command exists and none is approved for the task;
- the proposed path would enter production code;
- real customer data is required;
- external action is required;
- Product-local records would be promoted to Core;
- the repository cannot preserve research-only status;
- the owner has not accepted the target scope.

## 7. Confirmation record template

```yaml
consumer_task_id: string
repository: string
default_branch: string
baseline_sha: string
owner: string
package_manager: string
commands:
  install: string
  typecheck: string
  lint: string
  test: string
  fixture_validation: string
research_path: string
forbidden_paths: []
required_ci: []
synthetic_data_only: true
external_actions_disabled: true
status: READY_FOR_HANDOFF | BLOCKED
blockers: []
confirmed_by: string
confirmed_at: datetime
```

## 8. Checklist verdict

```text
MarkReg repository confirmed: NO
Lite repository existence confirmed: YES
Lite repository-local baseline confirmed: NO
MarkReg handoff authorized: NO
Lite handoff authorized: NO
Publication use cases retained: YES
```
