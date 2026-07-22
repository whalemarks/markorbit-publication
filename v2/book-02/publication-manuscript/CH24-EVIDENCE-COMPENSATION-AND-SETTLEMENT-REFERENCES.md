# CH24 — Evidence, Compensation and Settlement References

## Professional delivery and financial delivery are related but not identical

A professional platform needs to know what work was performed, whether it was accepted, what commercial promise applied, who should be paid, who actually paid, whether funds settled, and whether any amount remains disputed.

These questions cannot be compressed into one `paid` flag.

Book 02 therefore separates:

```text
Evidence
≠ Compensation
≠ Settlement
≠ Payment Custody
```

Core may define neutral references and shared meanings needed for interoperability. Detailed pricing, commission, invoicing, tax, payout and funds-management policy remain with the applicable commercial or financial Owning Service.

## Evidence remains the common lineage

Evidence supports both professional and financial decisions.

Examples include:

- accepted Assignment terms;
- Contribution and Review records;
- provider invoice;
- customer approval;
- official fee schedule;
- bank receipt;
- payment-gateway return;
- refund acknowledgement;
- commission agreement;
- tax document;
- currency-conversion record.

```text
invoice exists
≠ amount approved
≠ payment sent
≠ funds received
≠ purpose satisfied
```

Every material financial state should be traceable to its purpose, authority and evidence.

## Compensation is the commercial value owed for governed contribution

Compensation answers:

> Under an accepted commercial arrangement, what value may become payable to an actor for defined work, availability, outcome, responsibility or approved expense?

Compensation may relate to:

- Work Package completion;
- accepted Contribution;
- time within an approved cap;
- professional review;
- delivery ownership;
- provider service;
- referral or commission entitlement;
- urgent work;
- approved expense;
- cancellation or reserved capacity.

```text
participated
≠ compensation automatically owed

Contribution submitted
≠ compensation automatically released
```

The applicable contract and evidence determine the entitlement.

## Compensation reference

A neutral shared reference may preserve:

- beneficiary or payee reference;
- represented Organization or Workplace;
- commercial agreement reference;
- Assignment, Work Package, Engagement, Order or Matter reference;
- compensation type;
- amount or calculation method;
- currency;
- milestone or trigger;
- acceptance requirement;
- reviewer or approver requirement;
- tax and expense treatment reference;
- due date;
- dispute state;
- cancellation and adjustment rule;
- Settlement reference.

Core should avoid embedding product-specific pricing formulas or commission percentages as universal semantics.

## Compensation and professional acceptance

A Review result can affect compensation where the contract says so, but it should not become a hidden forfeiture mechanism.

A Contribution may require revision because:

- the contributor made a material defect;
- inputs were wrong;
- the Work Package changed;
- the source rule changed;
- the reviewer introduced a new requirement;
- the customer changed direction;
- the platform or Tool failed.

```text
revision required
≠ contributor automatically at fault
```

Compensation policy should distinguish the cause and preserve appeal or dispute evidence.

## Payment is an event, not the whole financial state

Payment may describe an attempt or transfer event.

The platform should distinguish:

```text
Payment Requested
Payment Approved
Payment Initiated
Payment Processor Accepted
Funds Debited
Funds Received
Funds Applied
Payment Failed
Payment Reversed
Payment Refunded
Payment Unknown
```

```text
Payment Initiated
≠ Funds Settled
```

A gateway success response may indicate technical acceptance while bank settlement remains pending.

## Settlement is reconciliation of obligations and transfers

Settlement answers:

> Have the relevant financial obligations, transfers, allocations, adjustments and disputes been reconciled for the declared purpose?

A Settlement record or reference may preserve:

- settlement purpose;
- participating payer and payee references;
- related compensation, invoice, Order, Matter or provider service;
- amount requested;
- amount approved;
- amount paid;
- amount received;
- amount applied;
- amount refunded;
- amount credited;
- amount outstanding;
- currency and exchange-rate evidence;
- tax, bank and remittance charges;
- allocation rules;
- dispute and correction state;
- completion authority;
- completion time.

```text
customer paid
≠ provider paid
≠ official fee paid
≠ contributor compensated
≠ Settlement complete
```

## Financial state is purpose-specific

One amount may contain several fee classes:

```text
Official Fee
Provider Professional Fee
Workplace Service Fee
Contributor Compensation
Translation Fee
Courier Fee
Tax
Bank or Remittance Charge
```

The platform should not present the total as an official fee or assume that all components share the same refundability and evidence requirements.

```text
Provider Invoice Total
≠ Official Fee
```

## Approval is separate from payment

Financial Approval should bind:

- approver and authority source;
- exact recipient;
- purpose;
- amount or maximum;
- currency;
- related object and version;
- conditions;
- effective time;
- expiry.

```text
Customer approved service
≠ customer approved every later cost
```

A customer may approve a filing route while a finance actor separately approves provider prepayment. A professional may verify an official fee without having authority to move funds.

## Payment orchestration is not custody

Execution may coordinate:

- payment request;
- approval checkpoint;
- payee verification;
- provider invoice collection;
- gateway invocation;
- Return validation;
- financial reconciliation.

But:

```text
Payment Orchestration
≠ Payment Custody
```

This manuscript does not authorize:

- escrow;
- pooled customer funds;
- money transmission;
- stored-value accounts;
- discretionary control of third-party funds.

Those activities require separate legal, financial, operational and security authority.

## Payee verification

Financial fraud often enters through changed bank details, impersonation or ambiguous beneficiary names.

Payee verification should preserve:

- legal recipient identity;
- account-holder identity;
- bank and country;
- currency;
- instruction source;
- prior verified instructions;
- change history;
- independent verification method;
- final approver;
- effective time.

```text
email contains bank details
≠ payee verified
```

A changed payment instruction may require out-of-band confirmation and additional Review.

## Official fee evidence

Official fees are time, jurisdiction and action specific.

A fee claim should preserve:

- official source or authoritative evidence;
- effective date;
- jurisdiction and office;
- action and class count;
- surcharges or publication fees;
- currency;
- calculation rule;
- assumptions;
- provider markup separation;
- reviewer where required.

```text
fee calculated correctly
≠ source fee schedule current
```

Knowledge may preserve the source and Claim; the applicable Product may quote the customer; the financial service may approve and pay; the Owning Service may validate whether payment supports the formal action.

## Provider payment and action readiness

Provider prepayment may be necessary but should not imply professional or execution readiness.

```text
Provider Paid
≠ Package Approved
≠ Provider Appointed
≠ Filing Authorized
≠ Filing Completed
```

Conversely, a package may be professionally ready while funds remain unavailable.

The states should remain parallel rather than overwriting one another.

## Contributor compensation

Contributor compensation should be linked to the accepted commercial context and production evidence.

Possible checkpoints include:

```text
Assignment Accepted
Contribution Submitted
Contribution Accepted
Revision Resolved
Work Package Accepted
Payment Approved
Funds Settled
```

The platform should avoid using the final customer payment as the only trigger unless the contributor contract explicitly accepts that dependency.

```text
customer has not paid
≠ contributor automatically bears all collection risk
```

## Referral and commission

A Demand Originator or Relationship Owner may have a contractual commission or referral entitlement, but role identity alone does not create it.

```text
Demand Originator
≠ Commission Entitlement
```

A commission claim should preserve:

- agreement and version;
- qualifying event;
- eligible revenue basis;
- exclusions;
- rate or calculation;
- relationship and attribution evidence;
- payment status;
- dispute and correction history.

Product-specific Commission Claim records should remain local unless stable cross-product interoperability proves a shared contract is required.

## Refund and credit

Refund and credit must remain separate.

```text
Refund
= funds returned

Credit
= value retained for future use
```

A business cannot silently replace an approved refund with a credit. The record should preserve customer agreement, amount, currency, affected fee component and effective conditions.

## Reversal, chargeback and correction

Financial corrections must preserve the earlier events.

Possible events include:

- duplicate payment correction;
- overpayment allocation;
- partial refund;
- bank reversal;
- chargeback;
- exchange-rate correction;
- invoice correction;
- tax correction;
- beneficiary correction.

```text
financial correction
≠ historical transfer erased
```

The system must show whether external funds movement has been reversed or whether only an internal allocation changed.

## Unknown financial state

Timeouts and conflicting returns can create financial Unknowns.

Examples:

- bank debited but gateway timed out;
- provider denies receipt;
- payment processor reports completed but account not credited;
- refund initiated but not received;
- duplicate payment risk unresolved.

```text
Unknown
≠ Failure
≠ Success
≠ Permission to Pay Again
```

Book 03 governs reconciliation and safe retry. Book 02 preserves the shared financial meanings.

## Settlement and formal completion

Professional completion, Order completion and financial completion should remain independent.

```text
Professional Outcome Complete
≠ Order Commercially Complete
≠ Settlement Complete
≠ Matter Closed
```

A Matter can remain active after the provider has been paid. A refund dispute can remain open after the professional work was completed. A certificate may be issued while courier and contributor expenses remain unsettled.

## Data and privacy

Financial Evidence often contains sensitive data.

Access should be limited by purpose and role:

- contributor may see compensation terms relevant to their Assignment;
- Delivery Owner may see funds readiness without full bank data;
- finance actor may see payee details;
- professional reviewer may see official fee evidence without customer card information;
- auditor may receive a controlled evidence projection.

```text
financially relevant
≠ visible to every delivery participant
```

## AI boundary

AI may:

- extract invoice candidates;
- compare fee schedules;
- detect duplicate amounts;
- recommend reconciliation questions;
- classify compensation triggers;
- draft financial explanations.

AI may not silently:

- approve payment;
- change payee details;
- move funds;
- waive a dispute;
- create a commission entitlement;
- infer custody authority.

```text
AI recommends payment
≠ payment approved
≠ payment executed
```

## Candidate status

Evidence and Settlement references are established or reconciled shared concepts, subject to exact frozen mapping. Compensation-specific shared semantics should remain neutral and minimal.

Detailed objects such as:

- Provider Invoice;
- Contributor Payout;
- Commission Claim;
- Customer Credit;
- Official Fee Quote;
- Tax Document;

should remain product-local or financial-service records unless the F0–F4 process demonstrates a stable shared need.

## Constitutional rule

```text
Evidence explains the obligation and transfer.
Compensation defines governed commercial entitlement.
Settlement reconciles obligations, transfers and corrections.

None creates payment authority or custody by implication,
and no single “paid” state may replace the full financial lineage.
```
