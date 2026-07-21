# Part V — Risk, Review and Protected Action

## Chapter 61 — Risk determines execution depth

Execution should not apply the same controls to every task.

A practical model uses:

```text
R0 automated and reversible
R1 automated or assisted with sampling
R2 single professional review
R3 cross-professional or senior review
R4 qualified or expert final authority
```

Risk depends on consequence, uncertainty, reversibility, value, data sensitivity, jurisdiction and the performer's evidence.

## Chapter 62 — R0

R0 applies to deterministic, low-impact and reversible actions such as format normalization or duplicate detection.

Controls still include validation, logging and rollback.

## Chapter 63 — R1

R1 applies where automation is reliable but periodic human sampling remains necessary.

Sampling should be risk-weighted and capable of increasing when error patterns emerge.

## Chapter 64 — R2

R2 requires a competent professional to review the Contribution before acceptance.

Examples may include standard search screening, classification recommendation or evidence triage.

## Chapter 65 — R3

R3 requires senior or cross-disciplinary review.

Examples include trademark beautification that may alter legal identity, complex transaction due diligence or conflicting jurisdiction evidence.

## Chapter 66 — R4

R4 requires a legally qualified professional or designated expert to control the final conclusion or action.

Examples include reserved legal advice, official submission, binding dispute strategy or high-value rights disposition.

## Chapter 67 — Professional Authority

Professional Authority is the role permitted to make or authorize a reserved professional act.

Execution verifies qualification, jurisdiction, status, scope and represented Organization.

Platform certification cannot substitute for legal qualification.

## Chapter 68 — Protected Action

Protected Actions include, according to context:

- official filing;
- binding legal communication;
- provider appointment;
- movement or custody of funds;
- execution of transfer documents;
- disclosure of highly sensitive data;
- deletion or irreversible mutation;
- customer commitment beyond approved scope.

## Chapter 69 — External Protected Action

An action performed in an external system requires:

- explicit authority;
- exact instruction version;
- idempotency key or duplicate control;
- external reference;
- expected response;
- timeout policy;
- reconciliation route;
- returned evidence.

## Chapter 70 — Segregation of duties

High-risk work may require different people to prepare, approve and execute.

The system should prevent one actor from silently creating the instruction, approving it and confirming its own completion where policy requires separation.

## Chapter 71 — Conflict checking

Conflict is evaluated before access and may continue during work.

New information can create a conflict after assignment. Execution must support pause, disclosure, replacement and evidence preservation.

## Chapter 72 — Review independence

A reviewer should not be economically or operationally pressured to accept defective work.

The system may separate production metrics from review quality and monitor abnormal acceptance patterns.

## Chapter 73 — Exception authority

Exceptions should be explicit.

An authorized exception records:

- rule being bypassed;
- reason;
- approving authority;
- compensating control;
- expiry;
- affected objects;
- review outcome.

An exception is not a silent precedent.

## Chapter 74 — Customer approval boundary

Customer approval is required for material business choices such as filing scope, deletion of goods, acceptance of risk, price, provider route or settlement terms.

Customer approval does not authorize an unlawful act or replace professional judgment where qualification is required.

## Chapter 75 — Provider selection and appointment

A provider recommendation is not an appointment.

Execution separates:

```text
candidate route
→ recommendation
→ user or authorized disposition
→ provider acceptance
→ appointment or instruction
```

## Chapter 76 — Funds control

Payment intent, authorization, capture, release, refund and reconciliation are distinct states.

Execution must not treat an invoice, transfer screenshot or provider acknowledgment as final settlement without the applicable funds authority.

## Chapter 77 — Data disclosure review

Before an external assignment or Handoff, Execution evaluates whether the data package is necessary, permitted and appropriately redacted.

A provider's need to perform work does not create unrestricted reuse rights.

## Chapter 78 — High-risk AI output

AI may assist high-risk work, but the output remains a candidate until reviewed by the required authority.

Execution should prevent AI-generated legal conclusions from being presented as finalized professional advice without disclosure and approval.

## Chapter 79 — Risk reclassification

Risk may increase when new facts appear.

Examples include:

- conflicting ownership;
- imminent deadline;
- threatened opposition;
- weak use evidence;
- large transaction value;
- uncertain official status.

Execution must pause or strengthen controls rather than continue under the original lower tier.
