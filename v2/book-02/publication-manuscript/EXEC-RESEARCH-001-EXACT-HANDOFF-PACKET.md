# EXEC-RESEARCH-001 — Exact Handoff Packet

## 1. Handoff identity

```text
Task ID: EXEC-RESEARCH-001
Task class: fixture-only research
Target repository: whalemarks/markorbit-execution
Source repository: whalemarks/markorbit-publication
Source programme: Book 02 v2 research
Source authority: Batch 14 task specification and Batch 15 intake controls
Canonical effect: none
Production effect: none
```

## 2. Objective

Implement deterministic, repository-local parsing and validation for five explicitly noncanonical research profiles:

1. Production Authorization Permission Profile;
2. Work Package Task/Workflow Profile;
3. Bilateral Assignment Lifecycle Profile;
4. Contribution Submission and Supersession Profile;
5. Outcome Acceptance without Formalization Profile.

The implementation must test whether these profiles can remain compositions over frozen Book 02 contracts and Book 03 runtime concepts.

## 3. Required source documents

The downstream PR must cite and preserve the versions of:

- `EXEC-RESEARCH-001-CODEX-TASK.md`;
- `RESEARCH-FIXTURE-SCHEMA-AND-VALIDATION-ACCEPTANCE-CRITERIA.md`;
- the five `RESEARCH-FIXTURE-*` documents from Batch 13;
- `EXPECTED-PR-AND-EVIDENCE-INTAKE-FORMAT.md`;
- `CONSUMER-PROOF-RESULT-EVALUATION-RUBRIC.md`;
- `SEMANTIC-DELTA-DECISION-LOG-TEMPLATE.md`.

The PR must record the exact publication source commit it used.

## 4. Allowed scope

Allowed:

- a repository-local `research/` or equivalent fixture-only path;
- TypeScript schemas or parsers marked research-only;
- deterministic validators;
- positive, negative and boundary fixtures;
- unit and fixture tests;
- a validation command;
- README or research notes explaining boundaries;
- generated reports committed as deterministic text or JSON when useful.

## 5. Prohibited scope

Not allowed:

- modifying `whalemarks/markorbit-core`;
- adding exports to `@markorbit/core`;
- describing a research profile as canonical;
- replacing Task, Permission, Policy or Human Review;
- implementing a production Workflow Runtime;
- network access;
- database, email, portal, payment or filing connectors;
- external action;
- AI approval or professional authority;
- production readiness claims;
- migration of existing records;
- Product-specific business policy.

## 6. Required fixture inventory

Minimum required:

```text
Positive fixtures: 5
Negative fixtures: 17
Boundary assertions: 17
```

At least one positive fixture per profile is required.

Negative coverage must include:

- Production Authorization without subject, action or scope;
- Production Authorization treated as Assignment;
- AI/system authorization without implementation version;
- Work Package replacing Task;
- all Tasks completed treated as package acceptance;
- Assignment without attributable acceptance;
- Assignment treated as Professional Authority;
- Contribution without contributor or exact work basis;
- Contribution submitted treated as accepted;
- supersession that erases earlier versions;
- Outcome without accepted input version and Human Review;
- Outcome treated as Apply or formal-state mutation;
- Unknown coerced to success or failure;
- Provider Return treated as official truth;
- Review treated as downstream execution;
- unauthorized controlled-value invention;
- public Core export leakage.

## 7. Required validation properties

The validator must report:

```text
deterministic: true
network_accessed: false
input_mutated: false
external_action_attempted: false
```

It must return typed reason codes and preserve Unknown.

Each result must include:

- fixture ID;
- profile type and version;
- pass/fail;
- expected and actual reason codes;
- frozen contract references;
- boundary assertions evaluated;
- unexpected warnings;
- validator version.

## 8. Required state boundaries

Tests must prove:

```text
Production Authorization State ≠ Assignment State
Work Package State ≠ Task State
Assignment State ≠ Eligibility Result
Contribution State ≠ Review State
Outcome State ≠ Formal State
```

Additional mandatory assertions:

```text
Production Authorized ≠ Assigned
Assignment Accepted ≠ Professional Authority
Contribution Submitted ≠ Outcome Accepted
Outcome Accepted ≠ Apply
Provider Return Received ≠ Official State Updated
```

## 9. Required repository-local commands

The downstream PR must expose documented commands for:

- install;
- typecheck;
- lint;
- fixture validation;
- tests;
- clean-checkout verification.

The exact commands must match the repository's package manager and existing conventions.

## 10. Expected PR title

```text
EXEC-RESEARCH-001 — fixture-only validation of Book 02 research profiles
```

## 11. Required PR body sections

```text
Task and source version
Repository baseline
Changed files
Research-only boundary
Fixture inventory
Validation design
Commands and results
Negative coverage
Known gaps
Semantic-delta statement
Evidence return
Non-goals
```

## 12. Evidence return

The downstream task is not complete until it returns:

- PR URL and number;
- base and head SHAs;
- exact changed files;
- fixture list;
- validation output;
- test output;
- workflow runs and combined status;
- review threads and submitted reviews;
- deviations from this packet;
- known gaps;
- merge status and merge SHA, or reason not merged;
- a proposed D0–D4 semantic-delta classification for each profile.

## 13. Acceptance authority

Publication-side acceptance evaluates only whether the research evidence is complete and trustworthy.

It does not:

- approve Core semantics;
- approve production adoption;
- authorize a formal Change Proposal;
- authorize external action.

## 14. Handoff state

```text
Packet status: READY_FOR_HANDOFF
Target acknowledgement: NOT RECORDED
Downstream branch: NOT RECORDED
Downstream PR: NOT RECORDED
Evidence return: NOT RECEIVED
Research acceptance: NOT DECIDED
```

## 15. Success condition

```text
A deterministic fixture-only consumer proof exists in markorbit-execution,
with complete negative coverage and no semantic activation.
```
