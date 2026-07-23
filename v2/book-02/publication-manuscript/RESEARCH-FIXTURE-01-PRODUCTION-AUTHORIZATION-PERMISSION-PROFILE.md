# Research Fixture 01 — Production Authorization as a Permission Profile

## 1. Status

```text
Artifact class: Noncanonical research fixture
Core contract: NO
Public export: NO
Implementation authorization: NO
Migration authority: NO
```

This fixture tests whether Production Authorization can be represented through the frozen Permission, Policy, Capability, Identity, Versioning, Audit and Human Review contracts without creating a new Core Object.

## 2. Research hypothesis

```text
Production Authorization
= specialized Permission profile
+ Policy constraints
+ Capability and implementation version references
+ effective period
+ review and audit context
```

Production Authorization permits bounded participation in real production work. It does not create Assignment, professional qualification, Professional Authority or approval for a protected action.

## 3. Base frozen fields reused

The profile reuses frozen Permission semantics:

- subject type and subject reference;
- action;
- resource type and resource reference;
- scope type and scope reference;
- effect;
- status;
- organization context;
- Policy reference;
- Capability reference;
- source reference;
- created/updated and audit metadata.

It does not change frozen Permission controlled values.

## 4. Research-only profile shape

```yaml
research_profile:
  profile_type: ProductionAuthorizationPermissionProfile
  profile_version: research-v0.1
  canonical: false

permission_reference:
  permission_reference_id: permission-ref-001
  subject_type: Identity
  subject_reference_id: identity-ref-human-reviewer-001
  action: participate_in_bounded_production
  resource_type: CapabilityExecution
  resource_reference_id: capability-ref-trademark-classification-001
  scope_type: Product
  scope_reference: product-installation-ref-markreg-001
  effect: Allow
  status: Active
  organization_reference_id: workplace-org-ref-001
  capability_reference_id: capability-ref-trademark-classification-001
  policy_reference_ids:
    - policy-ref-data-scope-001
    - policy-ref-review-required-001
  source_reference: authorization-decision-ref-001

profile_extensions:
  effective_from: 2026-07-01T00:00:00Z
  effective_until: 2026-10-01T00:00:00Z
  allowed_work_profile_types:
    - trademark-classification-preparation
  implementation_binding:
    implementation_type: Human
    implementation_reference_id: identity-ref-human-reviewer-001
    implementation_version: null
  data_ceiling:
    allowed_data_classes:
      - CustomerProvidedNonSensitive
      - PublicTrademarkData
    prohibited_data_classes:
      - PaymentCredentials
      - UnredactedIdentityDocuments
  tool_ceiling:
    allowed_tool_reference_ids:
      - tool-ref-classification-search-readonly
    prohibited_actions:
      - external_submission
      - communication_send
      - payment_execution
  supervision:
    human_review_required: true
    required_reviewer_role: senior-classification-reviewer
  reevaluation:
    triggers:
      - capability_contract_version_changed
      - policy_changed
      - implementation_suspended
      - material_quality_failure
      - effective_until_reached
```

## 5. Human subject example

The subject may prepare a classification recommendation under a declared Product and Capability scope.

The profile does not authorize the subject to:

- sign or submit a trademark application;
- provide reserved legal advice;
- contact the customer outside the assigned communication rule;
- access unrelated Matter data;
- approve its own protected output;
- receive payment or move funds.

```text
Production Authorized
≠ Assigned
≠ Professionally Authorized
≠ Approved for External Action
```

## 6. AI or deterministic implementation example

```yaml
research_profile:
  profile_type: ProductionAuthorizationPermissionProfile
  profile_version: research-v0.1
  canonical: false

permission_reference:
  permission_reference_id: permission-ref-ai-001
  subject_type: AIAgent
  subject_reference_id: agent-ref-classification-drafter-001
  action: generate_internal_draft
  resource_type: CapabilityExecution
  resource_reference_id: capability-ref-classification-draft-001
  scope_type: Workflow
  scope_reference: workflow-ref-classification-preparation-001
  effect: Allow
  status: Active
  capability_reference_id: capability-ref-classification-draft-001
  policy_reference_ids:
    - policy-ref-ai-no-external-action-001
    - policy-ref-human-review-required-001

profile_extensions:
  implementation_binding:
    implementation_type: AIAgent
    model_reference: model-ref-001
    model_version: model-version-locked
    instruction_version: instruction-version-003
    retrieval_policy_version: retrieval-policy-002
    allowed_tool_reference_ids:
      - tool-ref-knowledge-retrieval-readonly
    memory_scope: TaskContextOnly
  output_ceiling:
    allowed_output_types:
      - internal_classification_draft
      - source_list
      - unknowns_and_limitations
    prohibited_output_effects:
      - customer_instruction
      - final_professional_opinion
      - external_submission
      - formal_state_mutation
  review:
    human_review_required: true
    review_scope: complete_professional_review
```

Required equation:

```text
Model benchmark passed
≠ Production Authorization

Production Authorization
≠ Professional Authority
```

## 7. Positive validation cases

A conforming profile must:

1. reference a frozen Permission record or exact equivalent Permission shape;
2. identify the subject;
3. identify the controlled action;
4. bind resource and scope;
5. reference the applicable Capability;
6. reference relevant Policy decisions or rules;
7. define effective time or reevaluation behavior where the authorization is time-sensitive;
8. define data and Tool ceilings where consequential access is possible;
9. preserve source and audit references;
10. require Human Review where protected downstream use is possible.

## 8. Negative validation cases

Reject or classify as unsafe when:

```text
subject missing
scope missing
action is unrestricted wildcard
effect absent
Capability reference absent for capability-bound work
AI implementation version absent
external action appears in allowed actions
professional qualification is inferred from profile
Assignment is created automatically
Human Review is omitted for protected use
expired profile is treated as active
revoked profile leaves Tool access active
Product entitlement is substituted for Permission
```

## 9. Revocation behavior

Research rule:

```text
Permission revoked or expired
→ block new production invocation
→ identify active Assignments
→ pause or re-evaluate affected work
→ revoke unnecessary Tool and data access
→ preserve prior Evidence and accepted work
→ emit trace through owning services
```

```text
Authorization Revoked
≠ Prior Work Erased
```

## 10. Profile sufficiency test

The Permission-profile hypothesis succeeds when it can represent:

- human and AI/system subjects;
- Capability and Product/Workflow scope;
- effective periods;
- Policy and review requirements;
- data and Tool ceilings;
- revocation effects;
- version-bound implementation constraints;

without modifying frozen Permission meaning or controlled values.

It fails when independent consumers require a durable authorization identity and lifecycle that cannot be safely carried through Permission references and profile extensions.

## 11. Fixture verdict

```text
Profile is structurally plausible: YES
Frozen Permission must change now: NO
New Production Authorization Object proven necessary: NO
Book 03 enforcement still required: YES
Professional Authority created: NO
Canonical activation: NOT AUTHORIZED
```
