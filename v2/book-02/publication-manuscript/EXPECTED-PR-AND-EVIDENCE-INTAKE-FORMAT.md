# Book 02 — Expected PR and Evidence Intake Format

## 1. Purpose

This format defines the minimum information required when a downstream research task returns to the Book 02 programme through a pull request or equivalent reviewed change.

It standardizes evidence intake. It does not replace repository-local contribution rules, CI, professional review or the formal Book 02 Change Proposal process.

## 2. Intake principle

```text
PR Opened
≠ Evidence Complete
≠ Research Accepted
≠ Semantic Candidate Approved
```

The intake package must make the returned result reproducible and allow reviewers to distinguish:

- implementation evidence;
- fixture evidence;
- consumer-local design;
- proposed shared semantics;
- unsupported assertion;
- production claim.

## 3. Required PR metadata

Every downstream research PR must state:

```yaml
research_return:
  task_id: string
  task_version: string
  source_task_path: string
  source_task_commit_sha: string
  target_repository: string
  base_branch: string
  head_branch: string
  head_sha: string
  research_only: true
  canonical: false
  production_enabled: false
  external_actions_enabled: false
```

It must also include:

- concise objective;
- exact changed files;
- explicit exclusions;
- fixtures added;
- validators added;
- commands run;
- observed output;
- known gaps;
- deviations from task instructions;
- rollback or deletion path.

## 4. Required evidence directory

A downstream repository should store research evidence in one clearly isolated location, for example:

```text
research/book-02-profiles/<task-id>/
```

or another repository-local path approved in the handoff.

The evidence set should contain:

```text
README or research manifest
schemas or research types
positive fixtures
negative fixtures
validator implementation
validation report
reason-code register
boundary assertions
consumer mapping
known limitations
```

No file in this directory should be imported by production entry points.

## 5. Fixture inventory format

```yaml
fixture_inventory:
  task_id: string
  profile_types:
    - profile_type: string
      schema_version: string
      positive_fixture_ids: [string]
      negative_fixture_ids: [string]
      boundary_assertion_ids: [string]
  total_positive: integer
  total_negative: integer
  total_boundary_assertions: integer
```

Every fixture must identify:

- fixture ID;
- profile type and version;
- source frozen contracts;
- expected result;
- expected reason codes;
- payload;
- whether Unknown is expected;
- whether the fixture tests an authority boundary.

## 6. Validation report format

```yaml
validation_report:
  task_id: string
  validator_version: string
  executed_at: string
  deterministic: true
  network_accessed: false
  input_mutated: false
  external_action_attempted: false
  results:
    - fixture_id: string
      actual_result: VALID | INVALID | UNKNOWN
      expected_result: VALID | INVALID | UNKNOWN
      reason_codes: [string]
      passed: boolean
  totals:
    passed: integer
    failed: integer
    unknown: integer
```

A report with omitted negative fixtures is incomplete even when all included tests pass.

## 7. Boundary evidence

The PR must provide direct evidence for applicable boundaries:

```text
Production Authorization ≠ Assignment
Production Authorization ≠ Professional Authority
Work Package ≠ Task
Assignment ≠ Eligibility
Contribution Submitted ≠ Accepted
Review ≠ Apply
Outcome Accepted ≠ Formal State Updated
Provider Return ≠ Accepted Outcome
```

Evidence can include:

- test names and output;
- validator reason codes;
- code paths that deliberately stop before mutation;
- absence of production imports;
- explicit type separation;
- fixtures proving illegal transitions are rejected.

## 8. Command evidence

The return should list exact commands and outcomes:

```text
install
format check
lint
typecheck
unit tests
fixture validation
research-specific test command
```

For each command, record:

- command string;
- exit status;
- environment or runtime version;
- summary count;
- whether failures were fixed or waived.

Do not claim a check ran when only a related repository workflow ran.

## 9. PR review evidence

Required review metadata:

- review threads and resolution status;
- submitted reviews;
- requested reviewers where applicable;
- workflow runs associated with the exact head SHA;
- combined status checks;
- repository-local manual review conclusion;
- final merge SHA or reason not merged.

```text
Workflow success on unrelated files
≠ research-profile semantic validation
```

## 10. Consumer evidence

Each consumer return must state:

- which fields it used;
- which fields it ignored;
- which fields remained consumer-local;
- which lifecycle states were necessary;
- which owning service or module controlled mutation;
- which profile boundaries were tested;
- why frozen composition was or was not sufficient.

A narrative use case without fixtures is L1 evidence only.

## 11. Deviation format

```yaml
deviations:
  - deviation_id: string
    source_requirement: string
    actual_implementation: string
    reason: string
    semantic_impact: none | possible | material
    approval_required: boolean
```

Material deviations must block acceptance until reviewed.

## 12. Intake rejection conditions

Reject or return the package when:

- task version is missing;
- branch contains unrelated changes;
- public Core exports changed without authorization;
- fixtures are not marked noncanonical;
- network or external actions are enabled;
- negative fixtures are missing;
- reason codes are nondeterministic or absent;
- Task or Human Review is silently replaced;
- production readiness is claimed;
- the PR merges before evidence review when the handoff requires pre-merge review;
- reported checks do not correspond to the exact head SHA.

## 13. Intake decision values

```text
INTAKE_COMPLETE
INTAKE_INCOMPLETE
SEMANTIC_REVIEW_REQUIRED
REVISION_REQUIRED
REJECTED_SCOPE_VIOLATION
REJECTED_AUTHORITY_VIOLATION
ACCEPTED_AS_RESEARCH_EVIDENCE
```

```text
ACCEPTED_AS_RESEARCH_EVIDENCE
≠ accepted as shared contract
```

## 14. Intake template

```markdown
# <TASK-ID> Evidence Return

## Source task
- Path:
- Version:
- Commit:

## PR
- Repository:
- URL:
- Base:
- Head:
- Head SHA:

## Scope completed

## Changed files

## Fixtures
- Positive:
- Negative:
- Boundary assertions:

## Commands and results

## Evidence links

## Deviations

## Known gaps

## Authority locks

## Requested intake decision
```

## 15. Format verdict

```text
Evidence intake format: DEFINED
Downstream PR required for implementation proof: YES
Fixtures and exact-head checks required: YES
Narrative-only evidence sufficient for L2: NO
Automatic semantic admission: NO
```