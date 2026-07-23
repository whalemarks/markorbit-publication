# Book 02 — Consumer Proof Matrix for Candidate Profiles

## 1. Purpose

A shared Core contract requires evidence from independent consumers. Publication usefulness alone is not enough.

This matrix evaluates the current evidence for:

```text
Production Authorization Permission Profile
Work Package Task / Workflow Profile
Accepted Bilateral Assignment
Contribution Submission Profile
Outcome Acceptance Profile
```

## 2. Consumer classes

The expected consumers are:

- Book 03 Execution;
- MarkReg;
- Lite;
- Workplace and partner delivery contexts;
- Data, Knowledge or Brain where relevant.

The proof levels are:

```text
L0 — conceptual reference only
L1 — publication-level use case
L2 — repository contract or fixture
L3 — independent implementation integration
L4 — production-observed interoperability
```

A formal Core proposal normally requires at least two independent consumers at L2 or stronger, plus one implementation consumer before production migration.

## 3. Repository evidence observed

### 3.1 MarkOrbit Execution

Repository:

```text
whalemarks/markorbit-execution
```

Observed README state:

```text
implements Book 03 execution coordination
must not redefine Book 02
is not Product UI
is not external filing, payment or Communication-send system
does not grant autonomous AI authority
current programme: EXEC-TASK-001
```

Consumer-proof classification:

```text
Repository exists: YES
Architecture consumer intent: YES
Candidate-profile implementation: NO EVIDENCE IDENTIFIED
Independent integration proof: NO
Current proof level: L1
```

### 3.2 MarkOrbit Lite

Repository:

```text
whalemarks/markorbit-lite
```

The repository exists, but a `README.md` was not resolved on `main` during this audit. No candidate-profile implementation evidence was identified.

Consumer-proof classification:

```text
Repository exists: YES
Publication use cases: YES
Candidate-profile implementation: NO EVIDENCE IDENTIFIED
Current proof level: L1
```

### 3.3 MarkReg

Book 05 provides extensive Product-level use cases for professional lifecycle delivery, Provider coordination, filing preparation and maintenance.

No independent `markorbit-markreg` implementation repository or candidate-profile integration was established in this batch.

Consumer-proof classification:

```text
Publication use cases: YES
Independent implementation proof: NO
Current proof level: L1
```

## 4. Candidate-by-consumer matrix

| Candidate profile | Book 03 Execution | MarkReg | Lite | Shared-contract decision |
|---|---:|---:|---:|---|
| Production Authorization Permission Profile | strong conceptual need; runtime enforcement owner | professional delivery and Provider route use case | AI/content production use case | retain profile; implementation proof missing |
| Work Package Profile | central execution decomposition use case | filing/package assembly use case | content/transaction package use case | promising shared profile; Task insufficiency not yet proven in code |
| Bilateral Assignment | cross-Workplace execution need | Provider and reviewer assignment use case | contributor/network assignment use case | strongest F3 candidate; acceptance lifecycle proof missing |
| Contribution Profile | execution submission/review use case | documents, provider returns and review artifacts | content and marketplace artifacts | retain F2 profile until shared identity need appears in implementation |
| Outcome Profile | accepted-result handoff use case | reviewed filing/readiness result | accepted content or transaction result | retain F2 profile; cross-consumer identity not proven |

## 5. Required Book 03 proof

Book 03 must demonstrate through contracts or fixtures:

1. Permission and Policy validation before production invocation;
2. a Work Package profile containing more than one frozen Task;
3. Task replacement without loss of package continuity;
4. an offered Assignment requiring attributable acceptance;
5. suspension and revocation affecting Tool and data access;
6. Contribution submission at an exact version;
7. Review of an exact Contribution version;
8. Outcome acceptance without parent formal-state mutation;
9. reconciliation of a Provider Return before acceptance;
10. complete Event and audit trace.

## 6. Required Product proof

At least one Product should independently demonstrate:

- why one frozen Task is insufficient;
- why Product-local records are insufficient;
- why the profile reference must be exchanged with Book 03;
- which fields remain identical across Product and Execution;
- which Product fields remain local;
- which service owns corrections;
- how customer relationship and professional authority remain separate.

### MarkReg candidate proof case

A suitable proof case is:

```text
reviewable international trademark filing package
```

Possible chain:

```text
Matter and Order
→ Work Package Profile
→ several Tasks
→ internal and Provider Assignments
→ Contributions
→ professional Human Review
→ accepted filing-readiness Outcome
→ customer or professional Approval
→ later external filing route
```

The proof must show that accepted filing readiness does not equal official filing.

### Lite candidate proof case

A suitable proof case is:

```text
source-backed trademark content package
```

Possible chain:

```text
Content Brief
→ Work Package Profile
→ retrieval, drafting, visual and review Tasks
→ human/AI Contributions
→ public-content Review
→ accepted publication Outcome
→ separate publication Approval
```

Product-local objects such as Content Brief and Campaign Asset must remain outside Core.

## 7. Shared versus local field test

Likely shared fields:

```text
stable profile reference
work purpose
Task references
Assignment recipient and acceptance
Contribution identity and version
Human Review reference
Outcome purpose and accepted version
Permission and Policy references
Event and audit references
```

Likely Product-local fields:

```text
pricing
campaign metadata
filing-package layout
provider ranking
customer-facing labels
UI state
commission calculation
content channel settings
Product-specific delivery stages
```

## 8. Failure conditions

Consumer proof fails when:

- the second consumer merely copies the first schema without independent need;
- the use case can be solved through a local ID and frozen Task references;
- the candidate imports Product policy into Core;
- Book 03 becomes the formal-state owner;
- a Provider listing becomes Assignment acceptance;
- publication prose is treated as implementation proof;
- test fixtures are written after the public contract is already exported;
- negative cases are absent.

## 9. Current evidence verdict

```text
Independent repositories inspected: 2
Candidate-profile implementation found: 0
Book 03 proof level: L1
MarkReg proof level: L1
Lite proof level: L1
Two independent L2 consumers achieved: NO
Formal F3 proposal consumer gate passed: NO
Profile research may continue: YES
Public Core export authorized: NO
```

## 10. Recommended consumer-proof task sequence

```text
EXEC-RESEARCH-001
Implement fixture-only parsing and validation of the five research profiles
without importing them into public Core exports.

MARKREG-RESEARCH-001
Model one filing-readiness package using frozen Core references
and the noncanonical profiles.

LITE-RESEARCH-001
Model one source-backed content package using frozen Core references
and the noncanonical profiles.

CROSS-CONSUMER-REVIEW-001
Compare fields, lifecycle and ownership;
reject Product-local fields from shared admission.
```

These task identifiers are recommendations only and were not created in downstream repositories by this batch.
