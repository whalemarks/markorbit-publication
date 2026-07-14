# B05-CH-29 — Failure, Retry, Duplicate Safety, Communication and Audit

**Status:** Part IV Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

CH28 defines submission, acknowledgement and unknown states.

CH29 answers:

> When filing execution fails or becomes uncertain, how does MarkReg prevent duplicate legal and financial effects, recover safely, communicate honestly, and preserve a complete audit trail?

```text
Execution attempt
→ success, failure, partial failure or unknown
→ reconciliation
→ safe retry, correction, route change or stop
→ sourced Communication and audit continuity
```

Retry is a governed decision, not a button pressed after every error.

---

## 1. User Question and Primary Action

**User question:** What failed, what may already have happened, and what is the safest next action?

**Primary action:** Follow the approved recovery path: reconcile, correct, retry, change route, escalate, or stop.

The Product must explain why an immediate retry is allowed or blocked.

---

## 2. Failure Categories

Failures may be:

| Category | Examples |
| --- | --- |
| preparation | invalid package, missing Document, expired approval |
| authorization | absent authority, credential scope failure, approval mismatch |
| provider | rejection, non-response, conflict, deadline inability |
| connector | timeout, authentication, schema, file or service error |
| payment | decline, duplicate debit, unknown acceptance, insufficient funds |
| office | validation rejection, duplicate warning, maintenance outage |
| communication | delivery failure, ambiguous response, wrong recipient |
| evidence | receipt missing, identifier unverified, package mismatch |
| reconciliation | systems disagree on whether an effect occurred |

A failure category should identify the authority and evidence needed for recovery.

---

## 3. Partial Failure

One attempt may produce mixed effects:

- package transmitted but file attachment failed;
- official fee debited but application receipt absent;
- provider filed one class but rejected another;
- one jurisdiction succeeded while another failed;
- office created an identifier but payment remains unresolved;
- Communication sent but wrong attachment included;
- formal Matter updated while Product projection did not.

The Product must represent each effect separately.

---

## 4. Idempotency

Every protected-action request should carry a stable idempotency identity based on:

- Matter;
- package version;
- jurisdiction and route;
- action type;
- intended official or provider effect;
- approved attempt sequence.

Execution should use this identity to detect repeated requests and prior results.

The key must not be regenerated merely because a user refreshes the page or a worker restarts.

---

## 5. Duplicate Risk

Duplicate effects may include:

- two official applications;
- two fee payments;
- two provider instructions;
- duplicate Matter or invoice records;
- repeated client Communications;
- two correction filings;
- conflicting representative appointments.

A duplicate can create cost, priority, ownership, procedural and reconciliation problems.

---

## 6. Retry Safety Decision

Before retry, the Product and Execution context should determine:

1. whether the prior request left the controlled system;
2. whether delivery is confirmed;
3. whether the provider or office may have acted;
4. whether funds moved;
5. whether an identifier exists;
6. whether the route supports idempotent retry;
7. whether the package changed;
8. whether approval remains valid;
9. whether the deadline permits reconciliation;
10. who may authorize the retry.

If the effect is unknown, the default is reconcile before retry.

---

## 7. Retry Classes

```text
Safe technical retry
Correction and retry
Retry with same idempotency identity
Retry requiring new package version
Retry requiring new approval
Route substitution
Manual reconciliation only
Do not retry
```

The chosen class and reason must be retained.

---

## 8. Reconciliation

Reconciliation may compare:

- connector request and response;
- provider Communications;
- official database;
- official receipt search;
- payment and bank records;
- office account history;
- Matter and Execution Events;
- package hashes and identifiers;
- user or professional observations.

The outcome may be:

```text
No effect occurred
Effect occurred and evidence recovered
Partial effect occurred
Duplicate effect occurred
Effect remains unknown
```

---

## 9. Compensation and Remediation

Recovery may require:

- cancel queued action;
- reverse or refund payment;
- withdraw duplicate instruction;
- notify provider;
- correct official filing;
- request duplicate application withdrawal;
- create incident or professional escalation;
- preserve deadline rights;
- inform the client;
- update package, approval or route.

Compensation does not erase the original Event.

---

## 10. Route Substitution

Changing from connector to provider, or between providers, requires:

- renewed routing and selection;
- appointment and conflict checks;
- fee and payment review;
- package transformation comparison;
- Filing Approval impact assessment;
- duplicate and official-effect reconciliation;
- new instruction and acceptance.

Urgency does not justify bypassing these controls.

---

## 11. Communication Principles

Communications must distinguish:

- confirmed fact;
- provider report;
- technical result;
- Product interpretation;
- unresolved uncertainty;
- action requested;
- deadline and consequence.

The Product should not tell a client `filed successfully` while acknowledgement remains unknown.

---

## 12. Client Communication

A material incident communication should state:

- affected jurisdiction, filing unit and Matter;
- what is confirmed;
- what remains unknown;
- whether deadline or rights are at risk;
- what action is underway;
- whether new client decision, document, approval or payment is required;
- next update trigger;
- responsible contact.

Internal technical detail may be summarized, but uncertainty must not be hidden.

---

## 13. Provider Communication

Provider communication should preserve:

- exact instruction and package reference;
- requested evidence or clarification;
- duplicate warning;
- authority for correction or retry;
- fee and deadline consequences;
- required response time;
- secure channel and recipients.

A provider must not receive a contradictory second instruction while the first remains unresolved.

---

## 14. Communication Approval

High-impact Communications may require Review when they:

- admit professional or filing error;
- direct withdrawal or correction;
- change scope or fees;
- disclose confidential information;
- state legal consequences;
- waive rights;
- commit to refunds or remediation.

AI may draft. Authorized Humans approve and send under the applicable Communication process.

---

## 15. Event Trace

The audit trace should include:

- artifact and decision versions;
- actor and organization;
- approvals and authority;
- Task and Workflow references;
- route and credentials boundary;
- outgoing payload or instruction hash;
- timestamps;
- technical, provider and official responses;
- payment Events;
- Communications;
- retries and idempotency keys;
- reconciliation and remediation;
- final sourced state.

The trace should be understandable without reconstructing the journey from email alone.

---

## 16. Audit Integrity

Audit records should be:

- append-oriented;
- attributable;
- timestamped;
- source-linked;
- protected from silent alteration;
- purpose-limited;
- retained under policy;
- exportable for authorized review;
- linked to superseding corrections rather than overwritten.

Audit does not require exposing all private data to every participant.

---

## 17. Incident Learning

After resolution, the organization may record:

- root cause;
- affected rule, connector, provider or process;
- control that failed or was absent;
- remediation;
- jurisdiction-pack or Product update candidate;
- provider relationship impact;
- training need;
- measurable recurrence signal.

Private incident data does not automatically become shared ecosystem Knowledge.

---

## 18. `EMBERLOOP` Reference Journey

The EU connector attempt remains acknowledgement-unknown after technical success.

MarkReg:

1. blocks a second submission;
2. checks the office account and payment state;
3. queries the connector with the existing idempotency key;
4. finds that an official application number was created;
5. retrieves and verifies the receipt;
6. updates the Product projection to officially acknowledged;
7. informs the client with the verified number and filing date.

No duplicate filing or payment occurs.

---

## 19. Conformance Scenario — Timeout After Payment

**Given** an approved connector filing times out after the payment step.  
**When** no acknowledgement is returned.  
**Then** MarkReg records payment as unresolved, blocks automatic retry, initiates reconciliation against the office and financial records, and permits retry only after the prior effect is classified.  
**Authority boundary:** the Product cannot assume failure or success from the timeout alone.  
**Evidence retained:** request, package hash, payment attempt, timeout, queries, reconciliation decision and any later retry.

---

## 20. AI Assistance

AI may:

- classify failures;
- correlate Events and evidence;
- detect duplicate risk;
- propose reconciliation steps;
- draft factual Communications;
- summarize incidents and improvement candidates.

AI may not authorize retry, commit new funds, change routes, admit liability, send high-impact Communications, alter audit records, or mark an unknown effect resolved without evidence.

---

## 21. Minimum Chapter Lock

```text
Failure may be partial or unknown.
Unknown effect requires reconciliation.

Protected actions use stable idempotency identity.
Retry occurs only after duplicate risk,
authority, package, payment and deadline checks.

Communication states confirmed facts
and uncertainty honestly.

Audit preserves every material version,
decision, action, response and recovery.
```

---

## 22. Part IV Completion

Part IV now defines:

```text
Filing Package Candidate
→ Professional Review
→ client confirmation
→ Filing Approval
→ provider or direct-route selection
→ appointment and accepted instruction
→ governed execution
→ submission and acknowledgement states
→ failure, reconciliation, safe retry and audit
```

This progression is sufficient to support Part V — Examination, Publication and Disputes.

Part V begins only from sourced official notices, status and deadlines. It must not infer examination context from Product expectation alone.