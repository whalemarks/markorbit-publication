# CH18 — Funds Checkpoints Do Not Prove Performance

Money moving through a service chain creates strong psychological signals.

A customer has paid. The Workplace has transferred funds. The Provider has issued an invoice. The platform shows a funded balance. It is easy to assume that the service is therefore underway, complete or officially filed.

That assumption is unsafe.

```text
funds received
≠ Provider accepted
≠ work started
≠ milestone completed
≠ official fee paid
≠ protected action performed
```

MGSN must represent funds as typed checkpoints linked to scope, authority, evidence and reconciliation.

## 1. The difference between money and performance

Funds can move before, during or after work.

They may represent:

- customer prepayment;
- Workplace credit;
- Provider advance;
- official-fee reserve;
- platform service fee;
- reimbursable disbursement;
- milestone release;
- refund reserve;
- disputed amount;
- unallocated balance.

None of these states proves performance.

A Provider may require pre-funding before beginning. A customer may pay while documents remain incomplete. Funds may reach the wrong beneficiary. Official fees may remain unpaid even after the Provider receives money. A service may be completed before final settlement.

The commercial and fulfillment timelines must therefore remain separate but connected.

## 2. Typed funds checkpoints

A useful funds model may include:

```text
Offer Approved
Invoice Issued
Customer Payment Requested
Customer Payment Received
Funds Cleared
Funds Allocated to Engagement
Provider Funding Required
Provider Funding Authorized
Provider Funding Sent
Official-fee Reserve Recorded
Official Fee Reported Paid
Official Payment Evidence Received
Milestone Eligible for Settlement
Settlement Authorized
Settlement Executed
Refund Required
Refund Authorized
Refund Executed
Dispute Hold
Reconciliation Complete
```

These are not universal ledger entries. They are operating checkpoints that must reconcile to the authoritative finance system.

```text
MGSN checkpoint
≠ Finance ledger truth
```

## 3. Authority to receive, hold and release funds

The ability to record payment information does not create legal authority to hold customer money, operate escrow, transmit funds or release client money.

The route must identify:

- which entity invoices;
- which entity receives funds;
- in which currency;
- for whose account;
- under which contractual basis;
- whether funds are held, passed through or merely reported;
- who authorizes transfer;
- which regulated or banking constraints apply;
- what evidence is required.

```text
payment workflow designed
≠ payment custody authorized
```

Where the platform lacks authority for a funds function, the route must use an external or participant-controlled payment path and record only the resulting evidence.

## 4. Customer payment

Customer payment may satisfy a commercial prerequisite.

It does not necessarily satisfy:

- document completeness;
- conflict clearance;
- Provider Acceptance;
- professional review;
- customer approval of final content;
- protected-action authority;
- official-fee payment.

The system should avoid labels such as “Ready to file” when the only completed condition is payment.

A safer result is:

```text
funds condition satisfied
other readiness conditions pending
```

## 5. Provider pre-funding

Some Providers require payment before accepting or acting. Others accept work first and invoice later.

The route should state:

- whether pre-funding is required;
- whether it is a condition of Acceptance or performance;
- which amount is Provider fee and which is official fee;
- whether unused funds are refundable;
- what happens if the Matter cannot proceed;
- whether currency variance is reconciled;
- when proof of receipt is expected.

Provider funding should be linked to the accepted engagement and price version.

```text
money sent to Provider
≠ Provider received
≠ Provider allocated funds correctly
```

## 6. Official-fee funding

Official-fee funding requires additional separation.

The network should distinguish:

```text
Official Fee Estimated
Official Fee Approved
Official Fee Reserved
Funds Sent for Official Fee
Provider Reports Official Fee Paid
Official Receipt Received
Official State Reconciled
```

A Provider statement may be relevant evidence. An official receipt or authoritative acknowledgement may provide stronger evidence. Neither automatically updates the Owning Service until validated.

## 7. Beneficiary controls

Changing the beneficiary is a material event.

The network should verify:

- beneficiary name;
- relationship to the Provider Organization;
- bank location;
- currency;
- account change provenance;
- invoice consistency;
- sanctions or restriction checks where required;
- dual approval for material changes;
- confirmation through a trusted channel.

```text
new bank details in an email
≠ verified payment instruction
```

This control protects against fraud, undisclosed rebrokering and administrative error.

## 8. Milestone-linked funds

Funds should be linked to what they are intended to support.

Examples:

- allocation reserve;
- engagement commencement;
- draft delivery;
- customer-approved filing package;
- official filing Evidence;
- registration-stage action;
- certificate Return;
- correction completion.

The milestone definition should state:

- expected output;
- required Evidence;
- acceptance authority;
- amount eligible for release;
- holdback or exception rules;
- correction and dispute path.

A milestone cannot be considered complete merely because a Provider invoice references it.

## 9. Partial performance

Professional work can be partially completed.

A Provider may have:

- conducted a search;
- prepared a draft;
- reviewed documents;
- completed conflict work;
- attempted a filing that failed;
- paid one official fee but not another;
- delivered a corrected submission after an error.

The funds record should support partial allocation and settlement rather than forcing the engagement into paid/unpaid or complete/incomplete binaries.

## 10. Holds

A hold may be needed when:

- Evidence is missing;
- work is disputed;
- the beneficiary changed unexpectedly;
- official payment cannot be confirmed;
- the Provider is suspended;
- a refund may be required;
- the customer changed scope;
- a deadline or authority issue remains unresolved.

A hold should identify:

- amount;
- reason;
- authority;
- affected milestone;
- review date;
- release conditions;
- participant notification.

A hold is not a finding of wrongdoing. It is a protective state pending resolution.

## 11. Refunds

Refund logic must distinguish:

- unearned Provider fee;
- unused official-fee reserve;
- non-refundable external disbursement;
- completed milestone value;
- platform service already delivered;
- currency or banking cost;
- disputed amount;
- customer-caused cancellation;
- Provider-caused failure.

```text
engagement cancelled
≠ every amount automatically refundable
≠ no amount refundable
```

The result should follow accepted terms, evidence and applicable rules.

## 12. Reconciliation

Funds reconciliation answers:

- what was requested;
- what was received;
- what cleared;
- what was allocated;
- what was sent;
- what was paid to an authority;
- what work was accepted;
- what remains unused;
- what is disputed;
- what should be refunded or settled.

Reconciliation should occur at meaningful stages and at engagement closure.

The final financial state should not rely on one participant’s narrative when independent evidence is expected.

## 13. Payment status and user interface

Interfaces can create false certainty through labels.

“Paid” may mean:

- customer paid Workplace;
- Workplace paid platform;
- platform sent Provider funds;
- Provider received funds;
- official fee paid.

The interface should name the checkpoint precisely.

```text
Paid
→ paid by whom
→ to whom
→ for what
→ cleared when
→ evidenced how
```

## 14. AI boundaries

AI may help:

- extract invoice amounts;
- classify cost layers;
- compare beneficiary details;
- detect duplicate invoices;
- identify missing official receipts;
- reconcile expected and returned amounts;
- flag unusual changes.

AI must not:

- authorize payment;
- change a beneficiary;
- release funds;
- declare performance complete;
- infer an official fee was paid without evidence;
- decide a disputed refund.

## 15. Failure modes

### 15.1 Customer paid, so the system marks filed

Documents are incomplete, but payment creates a “completed” status.

Correct response: keep funds and filing readiness separate.

### 15.2 Provider reports official payment without receipt

The network treats the report as official truth.

Correct response: record the report as evidence and seek the expected authoritative acknowledgement.

### 15.3 Bank details change in the same email thread

Funds are sent without independent verification.

Correct response: hold payment and verify the beneficiary through a trusted channel.

### 15.4 Full settlement after partial performance

The Provider completed preparation but did not perform the protected action.

Correct response: evaluate milestone evidence and settle only under accepted terms.

### 15.5 Refund is calculated from the total only

Official disbursements, earned work and unused reserves are not separated.

Correct response: reconcile each cost and funds layer.

## 16. Product principle

Funds should make fulfillment possible without becoming a substitute for fulfillment evidence.

```text
typed funds checkpoints
+ explicit authority
+ beneficiary controls
+ milestone linkage
+ Finance reconciliation
= governable commercial flow
```

The next chapter explains how settlement should follow accepted milestones and Evidence rather than invoices, optimism or elapsed time.