# Research Fixture Schema and Validation Acceptance Criteria

## Purpose

Define one common validation envelope for the five Batch 13 noncanonical profiles.

The envelope is research-only and must not be presented as a Book 02 Core Contract.

## Common fixture envelope

```yaml
fixture:
  fixture_id: string
  profile_type: string
  profile_version: string
  status: research-only
  canonical: false
  source_specification_references: list[string]
  frozen_contract_references: list[string]
  purpose: string
  expected_result: pass | reject
  expected_reason_codes: list[string]
  payload: object
```

Required metadata:

- stable fixture identifier;
- exact profile type and version;
- explicit `research-only` status;
- explicit `canonical: false` marker;
- source publication references;
- nearest frozen contracts;
- declared validation expectation;
- deterministic reason codes.

## Shared validator behavior

A validator must:

1. reject missing research-status markers;
2. reject unknown profile versions unless compatibility is declared;
3. preserve Unknown rather than invent values;
4. validate references syntactically without claiming target existence unless a fixture registry is supplied;
5. return typed errors rather than free-form-only text;
6. avoid mutation of input fixtures;
7. avoid network access;
8. produce deterministic output;
9. expose no production execution function;
10. never convert validation success into semantic activation.

## Result envelope

```yaml
validation_result:
  fixture_id: string
  valid: boolean
  profile_type: string
  profile_version: string
  reason_codes: list[string]
  errors: list[object]
  warnings: list[object]
  boundary_assertions: list[object]
```

## Required reason-code families

```text
RESEARCH_STATUS_REQUIRED
CANONICAL_FLAG_MUST_BE_FALSE
PROFILE_TYPE_UNSUPPORTED
PROFILE_VERSION_UNSUPPORTED
SUBJECT_REFERENCE_REQUIRED
TARGET_WORK_REQUIRED
SCOPE_REQUIRED
PERMISSION_REFERENCE_REQUIRED
POLICY_REFERENCE_REQUIRED
REVIEW_REFERENCE_REQUIRED
EXACT_VERSION_REQUIRED
ACCEPTANCE_PURPOSE_REQUIRED
FORMAL_STATE_COLLAPSE_FORBIDDEN
PROFESSIONAL_AUTHORITY_INFERENCE_FORBIDDEN
CUSTOMER_RELATIONSHIP_TRANSFER_FORBIDDEN
ASSIGNMENT_INFERENCE_FORBIDDEN
OUTCOME_APPLY_COLLAPSE_FORBIDDEN
```

## Test inventory

Minimum:

| Profile | Positive | Negative | Boundary |
|---|---:|---:|---:|
| Production Authorization | 1 | 3 | 3 |
| Work Package | 1 | 3 | 3 |
| Bilateral Assignment | 1 | 4 | 4 |
| Contribution | 1 | 3 | 3 |
| Outcome | 1 | 4 | 4 |
| **Total minimum** | **5** | **17** | **17** |

## State-separation assertions

The test suite must explicitly assert:

```text
ProductionAuthorization.status
≠ Assignment.status

WorkPackage.status
≠ Task.status

Assignment.status
≠ Eligibility.result

Contribution.status
≠ Review.status

Outcome.status
≠ FormalState.status
```

## Reference discipline

Fixtures may reference frozen Objects and Contracts but must not duplicate or redefine them.

Examples:

```text
permission_reference_id
policy_reference_id
human_review_reference_id
task_reference_ids
workflow_contract_reference_id
document_reference_ids
evidence_reference_ids
```

A local research fixture may define a mock reference registry for deterministic tests. It must not be described as a canonical database.

## Compatibility behavior

Research profile versions should use an explicit version string.

Validation must distinguish:

```text
parseable
≠ compatible
≠ semantically accepted
```

Unknown major versions should fail closed. Unknown optional fields may be retained only when the profile policy permits extension.

## No execution surface

The research package must not contain methods such as:

```text
apply
submit
send
pay
file
mutateOfficialState
```

Any demonstration of downstream behavior must use preview-only or simulated result records.

## Acceptance gate

The fixture package passes only when:

- every positive fixture validates;
- every negative fixture fails for the expected reason codes;
- every boundary assertion is independently tested;
- test order does not affect results;
- validation output is deterministic;
- no public Core export changed;
- no external connector or production dependency was added;
- documentation preserves noncanonical status.

## Failure gate

The package fails when:

- a profile is exported as Core;
- Task or Human Review is replaced;
- an accepted Outcome mutates state;
- Assignment creates professional authority;
- AI or system authorization implies external-action authority;
- validation relies on live external services;
- passing fixtures are described as production readiness.

## Evidence report

A generated report should include:

```text
profile type
fixture counts
pass/fail counts
reason-code coverage
boundary assertion coverage
frozen references used
unresolved semantic gaps
consumer implications
```

## Constitutional lock

```text
Fixture validates a research hypothesis.
It does not validate a new Core semantic.
```
