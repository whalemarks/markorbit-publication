# Research Fixture 02 — Work Package as a Task / Workflow Profile

## 1. Status

```text
Artifact class: Noncanonical research fixture
Frozen Task replacement: NO
New Core Object: NO
Public export: NO
```

This fixture tests whether a Work Package can be represented as a profile that groups frozen Tasks under one Workflow and acceptance context.

## 2. Research hypothesis

```text
Work Package Profile
= package-level purpose and acceptance envelope
+ frozen Task references
+ frozen Workflow Contract reference
+ parent Matter / Order references
```

The profile exists only where a bounded production unit cannot be represented adequately by one Task.

## 3. When the profile is unnecessary

Do not create a Work Package profile when:

- one Task fully represents the work;
- one assignee completes one deliverable;
- Task status and Human Review are sufficient;
- no package-level acceptance or transfer exists;
- no independent package history must survive Task replacement.

```text
Every Task
≠ Work Package
```

## 4. Research-only shape

```yaml
research_profile:
  profile_type: WorkPackageTaskWorkflowProfile
  profile_version: research-v0.1
  canonical: false

identity:
  work_package_reference_id: research-work-package-001

business_context:
  matter_reference_id: matter-ref-001
  order_reference_id: order-ref-001
  customer_reference_id: customer-ref-001

workflow_context:
  workflow_contract_reference_id: workflow-contract-ref-filing-preparation-001
  workflow_application_reference_id: workflow-application-ref-001

purpose:
  purpose_code: prepare_reviewable_trademark_filing_package
  purpose_statement: >-
    Produce one internally complete and professionally reviewable filing package
    without performing external filing or changing official state.
  scope_reference_id: scope-ref-001
  exclusions:
    - external_submission
    - payment_execution
    - customer_signature_creation
    - official_state_confirmation

inputs:
  required_reference_ids:
    - applicant-identity-evidence-ref-001
    - trademark-representation-ref-001
    - goods-services-instruction-ref-001
    - jurisdiction-rule-version-ref-001
  assumptions_reference_ids:
    - assumption-ref-001
  unknown_reference_ids:
    - unknown-ref-signatory-authority-001

production:
  task_reference_ids:
    - task-ref-applicant-verification-001
    - task-ref-mark-validation-001
    - task-ref-goods-classification-001
    - task-ref-document-readiness-001
    - task-ref-professional-review-001
  required_capability_reference_ids:
    - capability-ref-identity-verification-001
    - capability-ref-classification-preparation-001
    - capability-ref-filing-readiness-review-001
  production_authorization_reference_ids:
    - permission-ref-production-001

acceptance:
  acceptance_criteria_reference_id: acceptance-criteria-ref-001
  required_human_review_reference_types:
    - identity_review
    - classification_review
    - filing_readiness_review
  prohibited_acceptance_shortcuts:
    - all_tasks_completed
    - file_generated
    - provider_says_ready

schedule:
  due_at: 2026-08-15T09:00:00Z
  dependency_reference_ids:
    - dependency-ref-customer-confirmation-001

trace:
  source_reference_ids:
    - customer-instruction-ref-001
  event_reference_ids: []
```

## 5. Frozen Task relationship

Each Task remains independently owned by Task Service and retains its frozen status.

Example:

```text
Task A: Completed
Task B: Completed
Task C: ReviewRequired
Task D: Open
Work Package Profile: Not Ready for Acceptance
```

The profile must not redefine frozen Task statuses.

```text
Work Package status
≠ Task status
```

Where a package-level display state is needed, it should be derived or research-local until a shared lifecycle is approved.

## 6. Package-level acceptance

The package may be accepted only when:

- all required Tasks reach acceptable terminal or review states;
- required outputs exist at the accepted versions;
- Unknowns are resolved or explicitly accepted;
- required Human Reviews are complete;
- the accepting actor or service has the applicable authority;
- the acceptance purpose and exclusions are recorded.

```text
All Tasks Completed
≠ Work Package Accepted
```

## 7. Task replacement scenario

A Task may be cancelled and recreated without changing package identity.

```yaml
replacement:
  original_task_reference_id: task-ref-goods-classification-001
  replacement_task_reference_id: task-ref-goods-classification-002
  reason: source_goods_list_materially_changed
  effective_at: 2026-08-04T09:00:00Z
  old_task_preserved: true
```

This scenario is one of the strongest arguments for a stable Work Package profile. It does not yet prove the need for a canonical Core Object.

## 8. Multi-contributor scenario

The package may contain Tasks assigned to:

- a customer intake specialist;
- an AI-assisted classifier;
- a professional reviewer;
- a document-preparation contributor;
- a Delivery Owner.

The package profile does not merge their Assignments, Contributions or authority.

```text
One Work Package
≠ One Assignee
≠ One Professional Authority
```

## 9. Positive validation cases

A valid profile must:

1. identify the package purpose;
2. reference a Workflow Contract;
3. reference one or more frozen Tasks;
4. preserve parent Matter or Order where applicable;
5. define inputs, scope and exclusions;
6. define package-level acceptance criteria;
7. preserve required Capability and governance references;
8. avoid direct mutation of Task, Matter or official state;
9. preserve Task replacement history;
10. remain noncanonical.

## 10. Negative validation cases

Reject when:

```text
profile silently replaces Task identity
Task statuses are renamed
package is accepted only because every Task says Completed
external submission is treated as package-owned action
Matter state is changed directly
Workflow Contract is absent for governed multi-step work
acceptance criteria are absent
unknowns are discarded
Task replacement erases the old Task
Product-specific pricing fields are promoted into Core semantics
```

## 11. Consumer questions

A consumer must demonstrate:

- why one Task is insufficient;
- why a Product-local grouping record is insufficient;
- why the package must survive Task replacement;
- why package identity must be shared across Products or Workplaces;
- who owns package mutation;
- how package acceptance differs from formal-state mutation.

## 12. Fixture verdict

```text
Task remains canonical: YES
Work Package profile is plausible: YES
Package-level identity may be useful: YES
Shared root Object proven necessary: NO
Independent consumer proof required: YES
Canonical activation: NOT AUTHORIZED
```
