# Part VI — Reliability, External Execution and Recovery

## Chapter 80 — Reliability is part of professional quality

A correct recommendation is not enough if the system loses the instruction, duplicates a payment or cannot explain whether an external filing occurred.

Execution quality includes technical reliability, operational continuity and evidence preservation.

## Chapter 81 — Idempotency

Protected actions require a stable idempotency boundary.

Repeated attempts with the same approved intent should not create duplicate filings, payments, provider instructions or communications.

## Chapter 82 — Attempt record

Every execution attempt records:

- request and approved version;
- timestamp;
- actor or service;
- destination;
- idempotency key;
- payload reference;
- response;
- external identifier;
- error classification;
- reconciliation state.

## Chapter 83 — Retry policy

Retry depends on failure type.

A network timeout may permit controlled retry after reconciliation checks. A validation rejection requires correction. An authorization failure requires new authority. A provider silence event requires escalation rather than repeated appointment.

## Chapter 84 — Duplicate detection

Execution compares external references, content hashes, official receipts, payment identifiers and prior attempts before retrying.

Duplicate detection should prefer a temporary Unknown state over an irreversible duplicate act.

## Chapter 85 — External reference

An external action should return or later acquire a durable reference such as:

- application number;
- filing receipt;
- provider matter reference;
- payment transaction identifier;
- courier tracking number;
- official document identifier.

The reference links the external event to the originating execution record.

## Chapter 86 — Handoff

A Handoff transfers typed context toward another Product, Workplace or network.

It preserves:

- source and destination;
- purpose;
- permission;
- minimum context;
- version;
- requested outcome;
- response deadline;
- evidence expectations;
- unknown and rejection states.

## Chapter 87 — Return

A Return brings status, Evidence or outcome back to the origin.

```text
Return received
≠ Return accepted

provider statement
≠ official fact

file delivered
≠ document validated
```

The originating context validates the Return under its own rules.

## Chapter 88 — MGSN execution

MGSN execution includes route recommendation, provider acceptance, governed instruction, funds checkpoints, fulfillment monitoring and typed Return.

Execution preserves the distinction between the Workplace-scoped MGSN Connection and the platform-managed network.

## Chapter 89 — External self-managed route

A Workplace may use a provider outside MGSN.

The Workplace then bears negotiation, instruction, payment and non-performance responsibility. MarkOrbit may still record evidence and continuity, but does not imply MGSN guarantees.

## Chapter 90 — Provider silence

Provider silence is not an informal inconvenience. It is an execution condition.

The workflow may trigger:

- reminder sequence;
- alternate communication channel;
- deadline risk escalation;
- replacement eligibility;
- customer disclosure;
- evidence capture;
- route suspension review.

## Chapter 91 — Official-system ambiguity

Official portals may show inconsistent or delayed status.

Execution should retain source snapshots, query time, prior values and confidence. The system may require direct confirmation before customer delivery or subsequent action.

## Chapter 92 — Document rejection

When a POA, specimen, certificate or identity document is rejected, Execution records:

- rejecting authority;
- stated reason;
- affected requirement;
- whether correction is possible;
- deadline;
- customer action needed;
- provider responsibility;
- replacement evidence.

## Chapter 93 — Deadline failure

A missed or endangered deadline creates a governed recovery workflow:

```text
confirm source and time zone
→ determine actual status
→ identify grace, restoration or refiling route
→ allocate responsibility
→ obtain customer decision
→ execute recovery
→ preserve incident evidence
```

## Chapter 94 — Payment failure

Payment failure may occur before or after an external commitment.

Execution separates:

- customer payment failure;
- platform capture failure;
- provider payment failure;
- bank delay;
- currency mismatch;
- duplicate debit;
- refund dispute.

Each has different authority and recovery requirements.

## Chapter 95 — Compensation failure

A contributor's accepted work should not disappear into an unresolved operational queue.

Execution links accepted Contribution, compensation basis, settlement trigger, payment status and dispute route.

## Chapter 96 — Data failure

Incorrect or stale data can produce incorrect work even when the workflow is followed.

Execution records the source version and may open a Data Correction Candidate. Correction of the shared dataset remains governed by the Data Refinery and applicable authority.

## Chapter 97 — Model or tool failure

AI and tools can become unavailable, change behavior or return malformed results.

Capabilities should support fallback bindings where economically justified. The platform should not make a critical professional path dependent on one model without detection and recovery.

## Chapter 98 — Partial completion

A workflow may produce useful partial outcomes even when the complete objective fails.

Execution distinguishes accepted partial work from completed Order delivery and determines compensation, reuse and next steps.

## Chapter 99 — Incident review

Material incidents produce a structured review:

- timeline;
- authority and decisions;
- technical and human causes;
- customer impact;
- financial impact;
- recovery;
- control changes;
- knowledge and capability candidates.

## Chapter 100 — Business continuity

Critical workflows require continuity for:

- deadlines;
- evidence access;
- communication;
- provider replacement;
- payment records;
- audit export;
- manual fallback.

Continuity is especially important when a Product or model is unavailable but a legal deadline continues to run.
