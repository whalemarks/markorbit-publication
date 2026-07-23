# Research Fixture 03 — Accepted Bilateral / Cross-Workplace Assignment Lifecycle

## 1. Status

```text
Artifact class: Noncanonical research fixture
Research track: B02-CP-RESEARCH-B1
Canonical Assignment Object: NO
Frozen Task mutation: NO
```

This fixture tests the narrow case in which frozen Task assignee fields may be insufficient: an Assignment that must be offered, accepted, declined, expired, suspended or revoked across organizational or Workplace boundaries.

## 2. Research hypothesis

Simple internal work allocation remains a frozen Task assignment.

A distinct Assignment record may be justified only when the relationship is bilateral or cross-Workplace and its lifecycle must survive independently of Task status.

```text
Simple Internal Allocation
= Task assignee / responsibility fields

Accepted Bilateral Assignment
= candidate independent lifecycle
```

## 3. Research-only shape

```yaml
research_record:
  record_type: BilateralAssignmentResearchProfile
  record_version: research-v0.1
  canonical: false

identity:
  assignment_reference_id: research-assignment-001

work_context:
  target_work_type: WorkPackageProfile
  target_work_reference_id: research-work-package-001
  task_reference_ids:
    - task-ref-professional-review-001
  matter_reference_id: matter-ref-001
  workflow_contract_reference_id: workflow-contract-ref-filing-preparation-001

parties:
  offering_workplace_reference_id: workplace-ref-origin-001
  receiving_workplace_reference_id: workplace-ref-delivery-001
  offered_to_identity_reference_id: identity-ref-reviewer-001
  represented_organization_reference_id: organization-ref-provider-001

scope:
  role: professional_reviewer
  allowed_actions:
    - review_filing_package
    - issue_review_decision
    - request_revision
  prohibited_actions:
    - external_submission
    - customer_instruction
    - payment_approval
    - formal_state_mutation
  visible_data_reference_ids:
    - projection-ref-minimum-filing-package-001
  tool_reference_ids:
    - tool-ref-document-viewer-readonly

eligibility_and_authority:
  permission_decision_reference_id: permission-decision-ref-001
  policy_decision_reference_id: policy-decision-ref-001
  eligibility_decision_reference_id: eligibility-ref-001
  professional_authority_reference_id: professional-authority-ref-001
  conflict_clearance_reference_id: conflict-clearance-ref-001

commercial_and_operational_terms:
  compensation_reference_id: compensation-ref-001
  confidentiality_reference_id: confidentiality-ref-001
  customer_contact_rule: no_direct_contact
  required_return_contract_reference_id: return-contract-ref-review-001

lifecycle:
  status: Offered
  offered_at: 2026-08-01T08:00:00Z
  response_due_at: 2026-08-03T08:00:00Z
  accepted_at: null
  declined_at: null
  effective_from: null
  expires_at: 2026-08-15T08:00:00Z
  suspended_at: null
  revoked_at: null
  completed_at: null

trace:
  created_by_identity_reference_id: identity-ref-delivery-owner-001
  source_reference_ids:
    - engagement-ref-001
  event_reference_ids: []
```

## 4. Candidate lifecycle

Research-only states:

```text
Draft
→ Offered
→ Accepted
→ Active
→ Completed
```

Alternative transitions:

```text
Offered → Declined
Offered → Expired
Accepted / Active → Suspended
Accepted / Active → Revoked
Active → Replaced
Any nonterminal state → Cancelled where safe
```

These values are not approved Core controlled values.

## 5. Offer and acceptance rules

An offer must specify:

- exact target work and version;
- role and allowed actions;
- data and Tool scope;
- deadlines;
- review and Return requirements;
- compensation or commercial reference where applicable;
- customer contact rules;
- Permission, Policy and Eligibility references;
- Professional Authority where reserved work is involved.

Acceptance must be attributable to the receiving actor or organization.

```text
Offer Sent
≠ Assignment Accepted

Email Delivered
≠ Responsibility Accepted
```

## 6. Activation rule

The Assignment becomes active only when:

- the offer is accepted;
- Permission and Policy decisions remain valid;
- Eligibility remains current;
- required professional authority and conflict clearance are valid;
- the effective time begins;
- required data access is activated;
- the target work version has not materially changed.

```text
Accepted
≠ Active by default
```

## 7. Amendment rule

A material change to any of the following requires explicit amendment or replacement:

- target work version;
- role;
- allowed action;
- data disclosure;
- deadline;
- compensation;
- contact permission;
- required professional authority;
- review or Return contract.

```text
New Attachment Sent
≠ Assignment Scope Automatically Changed
```

## 8. Suspension and revocation

Suspension temporarily blocks new production while preserving the Assignment record.

Revocation ends authority under the Assignment.

Required behavior:

```text
suspend or revoke
→ stop new work
→ restrict Tool and data access
→ identify active Contributions
→ preserve evidence and trace
→ decide whether reassignment is required
→ do not erase previously accepted work
```

```text
Assignment Revoked
≠ Professional Qualification Revoked
≠ Prior Work Erased
```

## 9. Relationship and authority locks

```text
Assignment Accepted
≠ Customer Relationship Transferred
```

```text
Assignment Accepted
≠ Professional Authority Created
```

```text
Professional Authority Valid
≠ Assignment Accepted
```

```text
Assignment Completed
≠ Work Package Accepted
≠ Formal State Updated
```

## 10. Task relationship

The accepted Assignment may be referenced by one or more frozen Tasks.

Task Service remains owner of Task assignee and status fields.

A possible application rule is:

```text
accepted Assignment reference
→ Task Service may update assignee/reference after validation
```

The Assignment profile must not directly mutate Task status.

## 11. Positive validation cases

A valid bilateral Assignment must:

1. identify offeror and recipient;
2. bind exact work and version;
3. define role, allowed and prohibited actions;
4. define data and Tool scope;
5. preserve Permission and Policy decisions;
6. preserve Eligibility and professional-authority references where required;
7. require attributable acceptance;
8. define expiry and revocation behavior;
9. preserve commercial and contact rules where applicable;
10. preserve audit and Event trace.

## 12. Negative validation cases

Reject when:

```text
recipient inferred from Provider listing
acceptance absent
work version absent
scope uses unrestricted wildcard
professional authority inferred from qualification only
customer contact allowed without rule
compensation terms silently changed
expired Assignment used for new work
revocation leaves access active
Assignment changes Matter or official state directly
Assignment completion is treated as Outcome acceptance
```

## 13. Consumer-proof threshold

A shared Assignment contract becomes plausible only when at least two independent consumers require:

- attributable acceptance;
- independent lifecycle;
- cross-Workplace continuity;
- access activation and revocation;
- stable reference across Task changes;
- audit and compensation linkage.

Book 03 is the likely execution consumer. A Product such as MarkReg or Lite must independently demonstrate the same contract need.

## 14. Fixture verdict

```text
Simple Task assignment remains sufficient for internal allocation: YES
Bilateral Assignment lifecycle is semantically distinct: YES
Cross-Workplace shared identity may be justified: YES
Independent consumer proof completed: NO
Formal Change Proposal ready: NO
Canonical activation: NOT AUTHORIZED
```
