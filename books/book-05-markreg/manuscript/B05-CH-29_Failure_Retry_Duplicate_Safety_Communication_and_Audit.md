# B05-CH-29 — Failure, Retry, Duplicate Safety, Communication and Audit

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

CH28 preserved submission, acknowledgement and unknown states.

CH29 defines recovery when an attempt is failed, partial, conflicting or uncertain:

```text
EL-22 / CH29
unknown, partial or rejected result
→ MR-C02 Reconciliation Context
→ MR-A18 Recovery and Reconciliation Plan
→ reconcile
→ safe retry, correction, route change or stop
→ sourced Communication and audit continuity
```

Retry is a governed Decision, not an automatic response to an error.

## 1. Product Question and Primary Action

**Product question:** What failed, what may already have happened, and what is the safest next action?

**Primary action:** Follow the approved recovery path: reconcile, correct, retry, change route, escalate or stop.

The Product must explain why retry is permitted or blocked.

## 2. Failure and Partial Effect

Failures may arise from preparation, authority, provider, connector, payment, office, Communication, evidence or reconciliation.

One attempt may create mixed effects, for example:

- package sent but attachment failed;
- official funds debited but receipt absent;
- one filing unit succeeded while another failed;
- identifier created but payment unresolved;
- provider instruction accepted but official action unknown;
- formal record updated while Product projection remained stale.

Each effect must remain separately represented.

## 3. Reconciliation Context

`MR-C02 Reconciliation Context` identifies:

- expected result;
- package, route and attempt identity;
- known technical, provider, financial and official evidence;
- unresolved contradictions;
- possible legal or financial effects;
- duplicate-risk scope;
- deadline and urgency;
- reconciliation owner;
- permitted queries and confidentiality boundary.

Unknown does not mean failed, and it does not mean safe to retry.

## 4. Stable Idempotency

Every protected-action request uses a stable identity derived from Matter, package version, jurisdiction, route, action type and intended effect.

The identity must survive page refresh, worker restart and uncertain response. A retry must not receive a new identity merely to bypass duplicate detection.

Duplicate effects may include:

- two applications;
- two fee payments;
- repeated provider instructions;
- duplicate Orders, Matters or invoices;
- repeated corrections or Communications;
- conflicting representative appointments.

## 5. Retry Safety Decision

Before retry, determine:

1. whether the prior request left the controlled system;
2. whether delivery occurred;
3. whether the provider or office may have acted;
4. whether funds moved;
5. whether an identifier exists;
6. whether the route supports idempotent retry;
7. whether the package changed;
8. whether approval remains active;
9. whether the deadline permits reconciliation;
10. who may authorize the next action.

If the effect is unknown, reconcile before retry.

## 6. Recovery Plan

`MR-A18 Recovery and Reconciliation Plan` may classify the next action as:

```text
Safe technical retry
Correction and retry
Retry with same idempotency identity
New package and renewed approval
Route substitution
Manual reconciliation only
Compensation or remediation
Do not retry
```

The Plan records reason, authority, evidence, deadline effect, communication need and closure condition.

## 7. Reconciliation Sources and Outcomes

Reconciliation may compare connector requests, provider Communications, official accounts or databases, receipts, payment records, Matter and Execution Events, payload hashes and professional observations.

Possible outcomes are:

```text
No external effect occurred
Effect occurred and evidence recovered
Partial effect occurred
Duplicate effect occurred
Effect remains unknown
```

Compensation or remediation does not erase the original Event.

## 8. Route Substitution

Changing from connector to provider, or between providers, requires renewed routing, Selection, appointment, conflict and availability checks, commercial review, package transformation comparison, Filing Approval impact assessment and duplicate-risk reconciliation.

Urgency does not authorize bypassing these controls.

## 9. Communication

A Communication must distinguish:

- confirmed fact;
- provider report;
- technical result;
- Product interpretation;
- unresolved uncertainty;
- requested action;
- deadline and consequence.

A client must not be told `filed successfully` while official acknowledgement remains unknown.

High-impact Communications—such as error admissions, withdrawals, scope changes, refunds or legal-consequence statements—require the applicable Human Review and `MR-D11 Communication Approval`.

AI may draft; it does not approve or send under its own authority.

## 10. Audit Continuity

The audit trace retains:

- artifact and Decision versions;
- actors, organizations and authority;
- Tasks, Workflows and route;
- credential boundary;
- payload or instruction hash;
- timestamps;
- technical, provider, official and payment evidence;
- Communications;
- idempotency identity and retries;
- reconciliation, remediation and final sourced state.

Audit records are attributable, source-linked, append-oriented and corrected through superseding records rather than silent overwrite.

## 11. `EMBERLOOP` — `EL-22`

The EU connector attempt remains acknowledgement-unknown after technical success.

MarkReg blocks a second submission, opens `MR-C02`, checks the official account and payment state, queries the connector using the existing idempotency identity and recovers a verified official receipt and application number.

The Product projection is updated only after verification. No duplicate filing or payment occurs.

## 12. Controlled Scenarios

### `MR-SCN-23` — Technical success without official receipt

The Product preserves sent or provider-reported state, opens reconciliation and does not claim official filing.

### `MR-SCN-24` — Unsafe retry could duplicate an application

A blind retry is blocked while external effect is unknown. Retry is allowed only after evidence classifies the prior attempt and the applicable authority approves the recovery path.

### `MR-SCN-15` — Duplicate payment risk

A timeout after a possible payment acceptance opens reconciliation and blocks a second charge until financial state is known.

## 13. AI Assistance

AI may classify failures, correlate Events, detect duplicate risk, propose reconciliation steps and draft factual Communications.

AI may not authorize retry, commit funds, change routes, admit liability, send high-impact Communications, alter audit records or resolve an unknown state without evidence.

## 14. Part IV Lock

```text
Failure may be partial or unknown.
Unknown effect requires reconciliation.
Protected actions use stable idempotency identity.
Retry follows evidence, authority and duplicate-risk checks.
Communication states uncertainty honestly.
Audit preserves every material version, Decision, action and recovery.
```

## 15. Handoff to Part V

Part IV now produces:

```text
Filing Package Candidate
→ Professional Review and Filing Approval
→ Routing Recommendation and Human Selection
→ Appointment, Instruction and Provider Acceptance
→ Execution Request
→ submission and acknowledgement evidence
→ reconciliation, recovery and audit
```

Part V begins only from sourced official notices, status and deadlines. It must not infer examination context from Product expectation or provider narrative alone.
