# Research Fixture 04 — Contribution Submission and Supersession

## 1. Status

```text
Artifact class: Noncanonical research fixture
Canonical Contribution Object: NO
Document or Evidence ownership change: NO
```

This fixture tests whether Contribution can remain a submission profile over frozen Document, Evidence, Event, Task and Human Review contracts.

## 2. Research hypothesis

```text
Contribution
= attributable submission envelope
+ artifact and Evidence references
+ exact work basis
+ version and supersession trace
```

Contribution does not replace the underlying Documents or Evidence records.

## 3. Research-only shape

```yaml
research_profile:
  profile_type: ContributionSubmissionProfile
  profile_version: research-v0.1
  canonical: false

identity:
  contribution_reference_id: research-contribution-001

work_basis:
  target_work_type: WorkPackageProfile
  target_work_reference_id: research-work-package-001
  task_reference_ids:
    - task-ref-goods-classification-001
  assignment_reference_id: research-assignment-001

contributor:
  contributor_identity_reference_id: identity-ref-contributor-001
  represented_organization_reference_id: organization-ref-delivery-001
  contribution_role: classification_preparer

submission:
  submitted_version: 1
  submitted_at: 2026-08-05T08:00:00Z
  artifact_reference_ids:
    - document-ref-classification-draft-v1
    - document-ref-source-table-v1
  evidence_reference_ids:
    - evidence-ref-official-classification-source-001
  source_reference_ids:
    - knowledge-version-ref-classification-2026-07
  declared_scope:
    - class_recommendation
    - selected_goods_draft
  exclusions:
    - legal_clearance_opinion
    - filing_approval
  assumptions_reference_ids:
    - assumption-ref-business-scope-001
  unknown_reference_ids:
    - unknown-ref-future-product-line-001

trace:
  supersedes_contribution_reference_id: null
  event_reference_ids:
    - event-ref-contribution-submitted-001
```

## 4. Artifact ownership

The profile references artifacts but does not own their content lifecycle.

```text
Document Service owns Document records.
Evidence Service owns Evidence records.
Contribution profile preserves submission context.
```

Deleting or replacing the profile must not erase the referenced artifacts where retention policy requires preservation.

## 5. Review relationship

A Human Review record targets the exact Contribution version.

```yaml
review_reference:
  human_review_reference_id: human-review-ref-001
  target_object_type: ContributionResearchProfile
  target_object_reference_id: research-contribution-001
  target_version: 1
  review_scope: classification_accuracy_and_source_support
  review_status: Completed
  review_decision: RevisionRequired
```

```text
Contribution v1 reviewed
≠ Contribution v2 reviewed
```

## 6. Supersession example

```yaml
research_profile:
  profile_type: ContributionSubmissionProfile
  profile_version: research-v0.1
  canonical: false

identity:
  contribution_reference_id: research-contribution-002

work_basis:
  target_work_reference_id: research-work-package-001
  assignment_reference_id: research-assignment-001

submission:
  submitted_version: 2
  submitted_at: 2026-08-06T08:00:00Z
  artifact_reference_ids:
    - document-ref-classification-draft-v2
    - document-ref-source-table-v2
  evidence_reference_ids:
    - evidence-ref-official-classification-source-001
    - evidence-ref-customer-product-confirmation-001

trace:
  supersedes_contribution_reference_id: research-contribution-001
  supersession_reason: addresses_review_revision_request
```

The first Contribution remains in the audit history.

```text
Superseded
≠ erased
```

## 7. Multi-artifact and non-document support

A Contribution may group:

- several Documents;
- structured records;
- Evidence;
- a Communication draft;
- an AI-generated candidate;
- a deterministic validation result.

The profile is justified only when the submission context must be preserved independently of each artifact.

## 8. Positive validation cases

A valid Contribution profile must:

1. identify exact target work;
2. identify contributor and represented context;
3. identify submitted version and time;
4. reference all submitted artifacts and Evidence;
5. preserve scope, exclusions, assumptions and Unknowns;
6. preserve Assignment where applicable;
7. preserve supersession relation;
8. support exact-version Human Review;
9. avoid mutating underlying artifact ownership;
10. remain noncanonical.

## 9. Negative validation cases

Reject when:

```text
contributor absent
work basis absent
submitted version absent
artifact list silently changes after review
AI artifact lacks model or source provenance
superseded version is deleted
Contribution submission is treated as acceptance
Contribution is treated as Task completion
Contribution is treated as official or formal truth
```

## 10. Fixture verdict

```text
Submission profile is semantically useful: YES
Document and Evidence remain canonical owners: YES
Independent Contribution root Object proven necessary: NO
Version and supersession requirements demonstrated: YES
Canonical activation: NOT AUTHORIZED
```
