# CH28 — Funds, Compensation and Settlement Need Governed Evidence, Not Implied Custody

## 1. Money movement is not a single execution state

Professional delivery involves several distinct financial events:

- customer payment;
- Workplace revenue recognition;
- provider prepayment;
- official fee payment;
- Contributor compensation;
- refund;
- credit;
- reimbursement;
- settlement between participating organizations.

These events must not be collapsed into one field called `paid`.

```text
Customer Paid
≠ Provider Paid
≠ Official Fee Paid
≠ Contributor Compensated
≠ Settlement Complete
```

## 2. Execution may coordinate financial checkpoints without owning funds

Book 03 governs when financial evidence is required before or after work. It does not automatically make MarkOrbit a bank, escrow agent or money transmitter.

```text
Payment Orchestration
≠ Payment Custody

Funds Record
≠ Authority to Move Funds
```

Any custody, pooled-funds, escrow or regulated payment function would require separate legal, commercial and technical authorization.

## 3. Financial objects should identify their purpose

A Funds Checkpoint or financial event should record:

- purpose;
- payer;
- payee;
- amount;
- currency;
- fee category;
- related Order, Matter or Work Package;
- approval source;
- due date;
- payment route;
- evidence required;
- refundability;
- settlement status;
- reconciliation owner.

```text
Amount Known
≠ Payment Authorized
```

## 4. Official fee, provider fee and service fee remain separate

The system should preserve:

```text
Official Fee
Provider Professional Fee
MarkReg or Workplace Service Fee
Contributor Compensation
Translation or Document Fee
Courier, Tax and Remittance Cost
```

```text
Provider Invoice Total
≠ Official Fee
```

This distinction is essential for pricing, customer explanation, refunds and later reconciliation.

## 5. Financial approval must be specific

A valid funds approval should identify:

- exact amount or maximum;
- currency;
- recipient;
- purpose;
- Matter;
- package or provider version;
- expiry;
- conditions;
- source of authority.

```text
Customer Approved Service
≠ Customer Approved Every Later Cost
```

If fees change materially, re-approval may be required.

## 6. Professional readiness and funds readiness are independent

Possible states include:

```text
Professionally Ready / Funds Not Ready
Funds Ready / Professionally Not Ready
Provider Paid / Customer Approval Missing
Customer Paid / Provider Not Paid
Official Fee Paid / Submission Unknown
```

```text
Payment Received
≠ Execution Ready
```

## 7. Provider prepayment must be linked to accepted scope

Before paying a provider, verify:

- provider eligibility;
- appointment;
- provider acceptance;
- scope;
- fee version;
- payee details;
- deadline;
- refund rule;
- Evidence Contract;
- customer or Workplace authorization.

```text
Provider Requests Funds
≠ Provider Entitled to Funds
```

## 8. Payee verification is part of execution safety

The system should record:

- legal recipient name;
- bank or payment-account identity;
- country;
- currency;
- source of payment instructions;
- change history;
- verification method;
- fraud warning;
- final approver.

A change in bank details should trigger enhanced verification.

```text
Email Contains Bank Details
≠ Payee Verified
```

## 9. Official fee payment requires evidence

Evidence may include:

- official receipt;
- transaction number;
- official portal record;
- provider disbursement statement;
- filed application linked to payment;
- currency and amount.

```text
Provider Debited
≠ Official Fee Applied to the Matter
```

## 10. Contributor compensation follows accepted production value

Contributor compensation should be linked to:

- Assignment;
- accepted scope;
- Contribution;
- review result;
- revision cause;
- agreed amount;
- completion or milestone condition;
- dispute status.

```text
Contribution Submitted
≠ Compensation Automatically Released

Review Finding
≠ Automatic Forfeiture
```

The compensation decision must distinguish performer error from changed scope, missing inputs and new customer instructions.

## 11. Reviewer and recovery work also have economic value

The system should not assume that senior review, incident recovery or provider reconciliation is free.

Possible compensated activities include:

- professional review;
- complex synthesis;
- emergency escalation;
- rework caused by external change;
- provider replacement;
- formal correction;
- customer recovery communication.

```text
Coordination Work
≠ No Production Value
```

## 12. Compensation does not create unrestricted rights

Payment for a Contribution does not automatically grant:

- public publication rights;
- AI-training rights;
- removal of attribution;
- reuse outside the Matter;
- unlimited derivative use.

```text
Compensation Paid
≠ Unrestricted Reuse Authorized
```

Rights and confidentiality remain separately governed.

## 13. Refundability must be phase-specific

A single service may contain:

- unstarted service fee;
- completed search fee;
- provider fee already incurred;
- non-refundable official fee;
- unused funds;
- refundable deposit;
- contingent future-stage fee.

```text
Matter Cancelled
≠ Entire Amount Refundable
≠ Nothing Refundable
```

The financial record should show what value was delivered and what external cost was already incurred.

## 14. Credits and refunds remain distinct

```text
Refund
= funds returned

Credit
= amount retained for future use
```

A customer should not be given a credit when a refund was promised without explicit agreement.

## 15. Settlement between Workplaces requires role clarity

In white-label or co-delivery work, settlement may involve:

- Relationship Owner;
- Delivery Workplace;
- Provider Workplace;
- Contributor;
- platform service.

The settlement record should preserve:

- commercial role;
- revenue basis;
- cost allocation;
- referral or production fee;
- taxes;
- dispute and reversal rules;
- customer ownership boundary.

```text
Settlement Recipient
≠ Customer Relationship Owner
```

## 16. Commercial attribution and professional responsibility remain separate

A party may receive:

- referral revenue;
- production fee;
- coordination fee;
- provider fee;
- review fee.

That revenue does not automatically create Professional Authority or Delivery Ownership.

```text
Revenue Share
≠ Authority Share
```

## 17. Financial reconciliation needs a complete ledger of evidence

Reconciliation should compare:

```text
Amount Requested
Amount Approved
Amount Paid
Amount Received
Amount Applied
Amount Refunded
Amount Credited
Amount Outstanding
```

It should also preserve:

- exchange-rate difference;
- bank charge;
- tax;
- duplicate payment;
- overpayment;
- underpayment;
- disputed amount;
- evidence source.

## 18. Professional completion and financial completion are different

```text
Professional Outcome Complete
≠ Financial Reconciliation Complete
```

A Matter may be professionally finished while a provider refund, customer credit or Contributor payment remains open.

Likewise, accounts may be settled while the official outcome remains Unknown.

## 19. Payment failure requires typed recovery

Possible payment failures include:

- authorization declined;
- transfer returned;
- wrong payee;
- wrong currency;
- duplicate payment;
- provider denies receipt;
- official fee not applied;
- customer chargeback;
- refund delayed.

Each requires its own evidence and recovery path.

```text
Payment Failed
≠ Same Recovery for Every Failure
```

## 20. AI may assist financial coordination but not silently authorize movement

AI can:

- classify fees;
- compare invoice versions;
- detect mismatch;
- summarize approvals;
- prepare reconciliation;
- flag suspicious payee changes.

It cannot create payment authority or custody rights.

```text
AI Recommends Payment
≠ Payment Approved
≠ Payment Executed
```

## 21. High-risk funds actions are External Protected Actions

Before a consequential funds action, require:

```text
Verified Payee
→ Exact Amount and Purpose
→ Specific Approval
→ Preview
→ Authorized Apply
→ Payment Return
→ Settlement Verification
→ Reconciliation
```

Idempotency and duplicate safety are mandatory.

## 22. Audit must reconstruct the financial decision

The system should be able to answer:

- Why was this amount requested?
- Who approved it?
- Which scope did it cover?
- Who received it?
- Was the official fee actually paid?
- What remained unused?
- Was the customer informed?
- Was any refund or credit due?
- Who closed the reconciliation?

## 23. Governing principle

Financial governance supports accountable delivery only when purpose, authority, evidence and reconciliation remain visible.

```text
Commercial State
≠ Professional State
≠ External State
```

MarkOrbit can coordinate those states without pretending that coordination itself creates custody, settlement finality or authority.