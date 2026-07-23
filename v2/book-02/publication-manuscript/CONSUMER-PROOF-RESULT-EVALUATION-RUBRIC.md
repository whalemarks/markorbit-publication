# Book 02 — Consumer-proof Result Evaluation Rubric

## 1. Purpose

This rubric evaluates whether a downstream consumer proof provides enough evidence to influence Book 02 semantic decisions.

It does not score code quality in general and does not replace repository-local CI or professional review.

## 2. Evidence levels

```text
L0 — assertion only
L1 — documented use case or architecture intent
L2 — deterministic fixture proof in one independent consumer
L3 — repeated fixture proof in at least two independent consumers
L4 — accepted shared contract with compatibility and migration evidence
L5 — production adoption with monitored conformance
```

Book 02 research currently requires at least L2 evidence from two independent consumers before a shared-contract proposal may advance.

```text
Two L1 narratives
≠ two L2 consumer proofs
```

## 3. Scoring dimensions

Each dimension is scored from 0 to 3.

### A. Task fidelity

- `0` — source task not referenced or materially ignored;
- `1` — partial implementation with unclear deviations;
- `2` — most requirements satisfied and deviations declared;
- `3` — exact task version followed with complete traceability.

### B. Fixture completeness

- `0` — no fixtures;
- `1` — positive examples only;
- `2` — positive and negative fixtures, incomplete boundary coverage;
- `3` — required positive, negative and boundary fixtures complete.

### C. Determinism and reproducibility

- `0` — result cannot be reproduced;
- `1` — manual or environment-sensitive output;
- `2` — repeatable locally with some undocumented assumptions;
- `3` — deterministic commands, versions and exact expected output documented.

### D. Frozen-contract traceability

- `0` — no mapping to frozen contracts;
- `1` — names frozen concepts but does not map fields;
- `2` — maps most fields and ownership boundaries;
- `3` — exact field, lifecycle, owner and mutation mapping.

### E. State separation

- `0` — candidate state collapses into Task, Review or formal state;
- `1` — separation claimed but not tested;
- `2` — key illegal transitions rejected;
- `3` — full state-separation matrix tested with reason codes.

### F. Authority separation

- `0` — permission, assignment, professional authority or external action collapse;
- `1` — boundary stated but not enforced;
- `2` — main authority violations rejected;
- `3` — subject, scope, policy, review, assignment and external authority remain independently enforced.

### G. Ownership clarity

- `0` — no owning module or service identified;
- `1` — technical owner only;
- `2` — lifecycle owner and mutation owner identified;
- `3` — owner, consumer, formal-state owner and correction path are distinct and tested.

### H. Consumer-local boundary

- `0` — Product-local concepts promoted implicitly;
- `1` — local concepts listed without enforcement;
- `2` — local records remain outside shared profiles;
- `3` — validators or architecture tests prevent local leakage into shared semantics.

### I. Compatibility evidence

- `0` — no compatibility analysis;
- `1` — assumes additive change is safe;
- `2` — identifies current consumers and breaking risks;
- `3` — includes backward/forward compatibility and migration or deletion path.

### J. Review and CI evidence

- `0` — no review or exact-head checks;
- `1` — unrelated workflow or informal check only;
- `2` — repository-local checks and PR review present;
- `3` — exact-head CI, review threads, resolved findings and final merge evidence complete.

Maximum score:

```text
30
```

## 4. Minimum gates

A result cannot reach L2 unless all of the following are true:

- Task fidelity score at least 2;
- Fixture completeness score at least 2;
- Determinism score at least 2;
- State separation score at least 2;
- Authority separation score at least 2;
- no forbidden scope change;
- no production or external action;
- exact changed files and head SHA supplied.

A result cannot support formal Change Proposal opening unless:

- at least two independent consumers reach L2;
- combined average score is at least 24/30;
- no dimension scores 0;
- State Separation, Authority Separation and Ownership each score 3 in the cross-consumer review;
- consumer-local disagreements are documented;
- frozen composition and profile alternatives are explicitly rejected with evidence.

## 5. Disqualifying findings

Regardless of score, reject the proof when it:

- modifies frozen Book 02 without a proposal;
- changes public Core exports;
- replaces frozen Task or Human Review;
- creates professional authority through platform data;
- enables external action;
- uses production credentials or networks;
- treats successful validation as formal state;
- claims canonical or production status;
- hides consumer-local fields inside a purported shared contract;
- cannot preserve Unknown.

## 6. Candidate-specific evaluation

### Production Authorization

Required proof:

```text
Permission profile sufficient
+ revocation blocks new production
+ Assignment remains separate
+ professional authority remains separate
```

Advance condition:

Only if at least two consumers prove the same missing field cannot be represented by Permission and Policy.

### Work Package

Required proof:

```text
one package spans several Tasks
+ package identity survives Task replacement
+ package-level acceptance is necessary
```

Advance condition:

Two consumers must require the same identity and lifecycle independently.

### Bilateral Assignment

Required proof:

```text
offer and acceptance attributable
+ cross-Workplace parties
+ independent lifecycle
+ Task fields insufficient
+ revocation and replacement preserved
```

This candidate receives the strictest ownership and compatibility review.

### Contribution

Required proof:

```text
multiple artifacts or non-document output
+ contributor attribution
+ exact submission version
+ supersession
```

Advance only if Document/Evidence/Event profiles cannot provide stable interoperability.

### Outcome

Required proof:

```text
purpose-limited acceptance
+ independent continuity
+ correction or supersession
+ formal-state separation
```

Advance only if relying services need one shared Outcome identity.

## 7. Decision bands

```text
0–11  REJECTED_OR_INSUFFICIENT
12–17 L1_ONLY
18–23 L2_CONDITIONAL
24–27 L2_STRONG
28–30 L2_COMPLETE
```

Cross-consumer decisions:

```text
RETAIN_AS_PROFILE
RETAIN_PRODUCT_LOCAL
RETAIN_BOOK_03_RUNTIME
MORE_EVIDENCE_REQUIRED
ADVANCE_TO_PRE_PROPOSAL
ADVANCE_TO_FORMAL_CHANGE_PROPOSAL
REJECT
```

## 8. Evaluation record

```yaml
evaluation:
  task_id: string
  consumer_repository: string
  pr_url: string
  head_sha: string
  evaluator: string
  scores:
    task_fidelity: 0
    fixture_completeness: 0
    determinism: 0
    frozen_traceability: 0
    state_separation: 0
    authority_separation: 0
    ownership_clarity: 0
    consumer_local_boundary: 0
    compatibility: 0
    review_and_ci: 0
  disqualifying_findings: [string]
  evidence_level: L0 | L1 | L2 | L3 | L4 | L5
  decision: string
  required_follow_up: [string]
```

## 9. Rubric verdict

```text
Consumer-proof scoring model: DEFINED
Two-consumer gate: RETAINED
Narrative use case sufficient for proposal: NO
High score can override authority violation: NO
Automatic Core admission: NO
```