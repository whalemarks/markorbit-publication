# MARKREG-RESEARCH-001 — Filing-readiness Consumer Proof Specification

## Objective

Demonstrate whether MarkReg can consume the five noncanonical profiles for one international trademark filing-readiness package without requiring new frozen Core Objects.

## Consumer scenario

```text
Customer Need
→ Matter and Order context
→ filing-readiness Work Package profile
→ Tasks
→ bilateral Provider Assignment profile where needed
→ Contributions
→ Human Review
→ filing-readiness Outcome
```

The proof ends before customer final instruction, external filing, payment or official-state mutation.

## Required use case

Prepare one fixture-only international trademark filing package containing:

- applicant and mark references;
- jurisdiction and class references;
- required-document checklist;
- goods/services preparation Task;
- applicant-data verification Task;
- local-provider review Task;
- at least one corrected Contribution;
- final purpose-limited filing-readiness Outcome.

## Required profile use

### Production Authorization

Demonstrate that an internal human or AI implementation may prepare a draft under bounded Permission and Policy constraints while lacking professional filing authority.

### Work Package

Group multiple Tasks into one filing-readiness deliverable without replacing frozen Task.

### Bilateral Assignment

Use only when a local Provider or professional must explicitly accept the work. Preserve that acceptance separately from Provider listing and professional appointment.

### Contribution

Represent submitted drafts, translations, classifications, verification notes or Provider returns with version and supersession trace.

### Outcome

Represent acceptance that the package is ready for a customer or professional decision.

Required lock:

```text
Filing-readiness Outcome
≠ Customer Final Instruction
≠ Professional Filing Approval
≠ Official Filing
≠ Official Receipt
```

## Minimum fixture sequence

```text
WP-MR-001 created as research profile
→ Task set linked
→ internal Assignment represented through Task
→ external bilateral Assignment offered and accepted
→ Contribution v1 submitted
→ Human Review requests correction
→ Contribution v2 supersedes v1
→ filing-readiness Outcome accepted for decision-support purpose
→ no Apply occurs
```

## Required negative cases

Reject or flag:

1. Provider listing treated as accepted Assignment.
2. Provider Assignment treated as professional authority.
3. AI draft treated as professional filing opinion.
4. all Tasks Completed treated as filing readiness without Review.
5. filing-readiness Outcome treated as customer instruction.
6. Outcome treated as official filing.
7. Provider Return treated as official receipt without reconciliation.
8. customer relationship transferred through direct Provider contact.

## Evidence required

The consumer proof must produce:

- fixture files;
- validation results;
- field-use matrix;
- fields unused by MarkReg;
- Product-local fields that must remain outside Core;
- exact frozen references consumed;
- state-separation assertions;
- unresolved gaps.

## Product-local records

The following should remain MarkReg-owned unless separately governed:

```text
Candidate Route Set
Provider Package
Filing Package
Case Fixture
Customer Instruction Record
Fee Quote
Commission or Margin Record
Official Filing Attempt
Official Receipt Reconciliation
```

## Success criteria

The proof succeeds when:

- the filing-readiness case can be represented without changing frozen Task, Permission or Human Review;
- all five profiles remain noncanonical;
- Product-local records remain outside Core;
- exact-version Contribution correction is demonstrated;
- Outcome is accepted without formalization;
- no external action is performed;
- the report states whether bilateral Assignment provides stable cross-Product value.

## Failure meaning

A failed proof does not automatically justify a new Core Object. It must identify whether the failure comes from:

- missing shared semantics;
- Product-local requirements;
- Book 03 runtime requirements;
- legal/professional authority requirements;
- an inadequate research fixture.

## Completion report

Report:

```text
Consumer level reached
Profiles consumed
Fields used
Fields rejected
Product-local extensions
Negative cases passed
Semantic gaps
Formal proposal recommendation
```

## Boundary

```text
MarkReg consumer proof
≠ MarkReg production implementation
≠ filing authorization
≠ customer instruction
```
