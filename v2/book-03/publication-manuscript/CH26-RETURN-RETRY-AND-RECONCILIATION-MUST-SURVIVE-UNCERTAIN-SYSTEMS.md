# CH26 — Return, Retry and Reconciliation Must Survive Uncertain Systems

## 1. External systems do not always tell the truth immediately

Professional execution crosses systems that may be slow, partial, inconsistent or silent. A connector can time out after creating an application. A payment can be deducted while settlement remains pending. A provider can say “filed” before an official receipt exists. An office portal can show one status while a formal notice shows another.

The execution model must therefore preserve uncertainty.

```text
Apply Attempt
→ Return
→ Interpretation
→ Validation
→ Reconciliation if Necessary
→ Formal-state Decision
```

```text
No Clear Return
≠ No External Effect
```

## 2. Return is evidence, not truth

A Return may come from:

- deterministic internal code;
- AI tool invocation;
- connector response;
- provider email;
- payment gateway;
- official portal;
- official document;
- courier record;
- manual operator report.

Each Return should identify:

- source;
- time;
- related Apply attempt;
- payload or package version;
- external reference;
- response type;
- completeness;
- confidence;
- validation status;
- conflicts.

```text
Return Received
≠ Outcome Verified
```

## 3. Return classes must remain distinct

Useful Return classes include:

```text
Technical Delivery Return
Provider Operational Return
Payment Processing Return
Official Acknowledgement
Official Substantive Result
Manual Observation
Customer Response
Reconciliation Finding
```

An HTTP 200 is a Technical Delivery Return. It is not the same as an Official Acknowledgement.

```text
HTTP Success
≠ Office Acceptance
```

## 4. Unknown is a first-class execution state

Unknown should be used when:

- timeout occurred after transmission;
- provider claims action without evidence;
- payment status conflicts;
- official portal is unavailable;
- duplicate external reference exists;
- return is incomplete;
- manual and system records disagree;
- an external action may have occurred after cancellation.

```text
Unknown
≠ Failure
≠ Success
≠ Permission to Retry
```

## 5. Retry must be justified by duplicate safety

Before retry, the system should ask:

- Is the operation naturally idempotent?
- Was an idempotency key used?
- Can the external target detect duplicates?
- Is there an external reference?
- Can official or provider records be queried?
- What harm could duplication cause?
- Is the deadline more dangerous than the duplicate risk?
- Who approves the retry?

```text
Retry Available
≠ Retry Safe
```

## 6. Technical and business idempotency are different

Technical idempotency may prevent duplicate API calls from creating duplicate records.

Business idempotency asks whether repeating the intended action would create duplicate legal, commercial or customer effects.

```text
Same Idempotency Key Rejected
≠ No Earlier External Effect
```

Examples requiring business-level reconciliation include:

- trademark filing;
- official fee payment;
- provider appointment;
- customer deadline notice;
- publication of a professional claim;
- withdrawal request.

## 7. Reconciliation is a governed investigation

A Reconciliation Case should preserve:

- triggering uncertainty;
- affected Apply attempts;
- package hash;
- external target;
- known returns;
- conflicting evidence;
- deadline exposure;
- funds exposure;
- duplicate risk;
- owner;
- investigation steps;
- finding;
- next approved action.

```text
Reconciliation
≠ Informal Checking
```

## 8. Reconciliation sources should be ordered by authority

Possible evidence hierarchy:

```text
Official Document
Official Record or Portal
Official Transaction Reference
Provider Evidence
Connector Log
Payment Processor Record
Manual Observation
Unverified Statement
```

The hierarchy may vary by jurisdiction and procedure, but source authority must be explicit.

```text
Provider Statement
≠ Official Record
```

## 9. Conflicting evidence must remain visible

Examples:

- provider says filed, portal has no record;
- portal shows filed, receipt is missing;
- payment processor says completed, provider says unpaid;
- official notice uses different applicant details;
- courier says delivered, provider says original not received.

The system should not overwrite one source with another. It should record:

```text
Source A Claim
Source B Claim
Conflict Type
Current Working Interpretation
Required Verification
```

## 10. Deadline pressure changes priority, not truth

When a deadline approaches, Reconciliation may need parallel actions:

- official inquiry;
- provider escalation;
- backup provider readiness;
- customer notice;
- protective route analysis;
- funds hold;
- duplicate-risk assessment.

But urgency does not allow the system to declare failure without evidence.

```text
Urgency
≠ Permission to Invent Certainty
```

## 11. Retry policy should be action-specific

A Retry Policy can define:

- maximum attempts;
- delay;
- backoff;
- reconciliation trigger;
- duplicate-risk threshold;
- authority required;
- deadline override;
- stop condition;
- manual takeover.

For high-risk external actions, automatic retry may be prohibited.

```text
Automatic Retry
≠ Default Reliability Strategy
```

## 12. Provider return requires evidence validation

A provider return should be checked against the agreed Return Contract.

Possible findings:

```text
Complete and Validated
Complete but Unverified
Incomplete
Inconsistent
Wrong Matter
Wrong Version
Evidence Missing
Official Verification Pending
Rejected
```

```text
Provider Returned a File
≠ Correct Matter Evidence Received
```

## 13. Payments require their own reconciliation chain

Payment states may include:

```text
Authorized
Initiated
Processing
Debited
Received by Intermediary
Received by Provider
Applied to Official Fee
Refund Pending
Refunded
Chargeback
Unknown
```

```text
Customer Paid
≠ Provider Received
≠ Official Fee Paid
```

## 14. Communication delivery also needs reconciliation

A message can be:

- drafted;
- approved;
- sent;
- accepted by mail server;
- delivered;
- bounced;
- opened;
- acknowledged;
- answered.

```text
Message Sent
≠ Recipient Received
≠ Recipient Understood
```

For consequential deadlines, the workflow may require acknowledgement or alternative contact.

## 15. Cancellation can create uncertain state

If cancellation occurs during an in-flight Apply attempt, the system must determine:

- whether the provider received the instruction;
- whether payment was initiated;
- whether the office accepted the filing;
- whether the message was delivered;
- whether a compensating action is possible.

```text
Cancellation Requested
≠ External Action Cancelled
```

## 16. Compensating action is not rollback

External systems often cannot be rolled back technically. Recovery may require a new action:

- withdrawal;
- correction;
- refund request;
- replacement filing;
- clarification message;
- provider termination;
- data deletion request.

```text
Compensating Action
≠ Historical Erasure
```

## 17. AI may assist reconciliation, but cannot resolve authority conflicts alone

AI can:

- correlate attempt logs;
- compare versions;
- extract external references;
- identify evidence gaps;
- rank likely explanations;
- prepare inquiry drafts.

It cannot silently decide that an official action occurred when the evidence remains conflicting.

```text
AI Likelihood Estimate
≠ Reconciled Formal Truth
```

## 18. Reconciliation ownership must be explicit

The owner should coordinate:

- evidence collection;
- provider contact;
- official verification;
- deadline management;
- customer communication;
- retry decision;
- compensation or refund route;
- formal-state handoff.

The Reconciliation Owner does not automatically gain authority to submit, pay or disclose.

```text
Reconciliation Owner
≠ Unlimited Recovery Authority
```

## 19. Resolution requires evidence-backed closure

Possible resolution states include:

```text
External Effect Verified
No External Effect Verified
Duplicate Effect Verified
Partial Effect Verified
Formal Result Pending
Safe Retry Approved
Compensating Action Required
Unresolved — Continuing Monitoring
```

A workaround is not enough.

```text
Workaround Applied
≠ Reconciliation Closed
```

## 20. Learning follows closure, not speculation

After closure, the system may update:

- Retry Policy;
- connector behavior;
- Provider quality evidence;
- Evidence Contract;
- deadline buffer;
- customer communication;
- Simulation scenario;
- Capability guidance.

But unresolved responsibility should remain unresolved.

## 21. Governing principle

Reliable execution does not assume that every system produces immediate certainty. It preserves ambiguous states, blocks unsafe repetition and turns uncertainty into an auditable investigation.

```text
Return
→ Validate
→ Reconcile
→ Then Decide
```

That discipline is essential wherever external consequences cannot be safely repeated.