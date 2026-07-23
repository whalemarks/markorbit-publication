# CH18 — Funds Checkpoints Do Not Prove Performance

Money creates a strong psychological signal.

The customer has paid. The Workplace has transferred funds. The Provider has issued an invoice. A balance appears as funded. It is easy to assume that work has therefore begun, completed or reached the authority.

That assumption is unsafe.

```text
funds received
≠ Provider accepted
≠ work started
≠ milestone completed
≠ official fee paid
≠ protected action performed
```

MGSN must represent money as typed checkpoints linked to scope, authority, Evidence and Finance reconciliation.

## 1. Keep the commercial and fulfillment timelines separate

Funds can move before, during or after performance. They may represent customer prepayment, Provider advance, an official-fee reserve, a milestone release, a disputed amount or an unused balance.

None of those states proves what happened operationally.

A customer may pay while documents remain incomplete. A Provider may require funding before accepting. Money may reach the wrong beneficiary. An official fee may remain unpaid after funds reach the Provider. Work may be completed before final settlement.

The commercial and fulfillment timelines must therefore remain separate but connected.

## 2. Name the checkpoint precisely

Useful operating checkpoints may include:

```text
Offer Approved
Customer Payment Received
Funds Cleared
Funds Allocated to Engagement
Provider Funding Authorized
Provider Funding Sent
Official-fee Reserve Recorded
Official Fee Reported Paid
Official Payment Evidence Received
Milestone Eligible for Settlement
Settlement Authorized
Settlement Executed
Refund or Dispute Hold
Reconciliation Complete
```

These are not universal ledger entries.

```text
MGSN funds checkpoint
≠ Finance ledger truth
```

The authoritative Finance system remains responsible for formal accounting, balances and payment execution.

## 3. Recording money does not create custody authority

The ability to display a payment workflow does not authorize MGSN to hold customer money, operate escrow, transmit funds or release client money.

The route must identify:

- who invoices;
- who receives;
- for whose account;
- whether funds are held, passed through or merely reported;
- who may authorize transfer;
- which banking or regulatory constraints apply;
- what Evidence confirms each step.

```text
payment workflow designed
≠ payment custody authorized
```

Where MGSN lacks the relevant authority, the payment path must remain external or participant-controlled, with MGSN recording only the resulting business Evidence.

## 4. Customer payment satisfies only the funds condition

Payment may be a prerequisite for work. It does not establish document completeness, conflict clearance, Provider Acceptance, professional review, customer approval or filing authority.

A safe status is:

```text
funds condition satisfied
other readiness conditions pending
```

“Paid” should never be used as shorthand for “ready to file.”

## 5. Provider funding must follow the accepted engagement

A Provider may require pre-funding before Acceptance or before performance. The route should make clear:

- which amount is professional fee;
- which amount is official-fee funding;
- whether unused funds are refundable;
- what happens if the Matter cannot proceed;
- how currency variance is reconciled;
- when receipt confirmation is expected.

```text
money sent to Provider
≠ Provider received
≠ Provider allocated it correctly
```

Funding should be tied to the accepted scope, package and price version.

## 6. Official-fee funding needs its own evidence chain

```text
Official Fee Estimated
→ Approved
→ Reserved
→ Sent
→ Provider Reports Paid
→ Official Receipt Received
→ Official State Reconciled
```

Each step proves something different.

A Provider statement may be relevant Evidence. An official receipt or authoritative acknowledgement may be stronger. Neither automatically updates the formal Matter state until the Owning Service validates it.

## 7. Beneficiary changes are material

A new bank account, affiliate or payment location is not a harmless administrative detail.

The network should verify the beneficiary name, relation to the Provider Organization, invoice consistency, bank location, currency, provenance of the change and any applicable restriction checks.

```text
new bank details in an email
≠ verified payment instruction
```

Material beneficiary changes should use trusted-channel confirmation and appropriate approval.

## 8. Link funds to milestones

Funds should be connected to the work they support, such as commencement, draft delivery, a customer-approved package, official filing Evidence, a registration-stage action or certificate Return.

The milestone should identify:

- expected output;
- required Evidence;
- acceptance authority;
- amount eligible for release;
- holdback or exception rule;
- correction and dispute path.

A Provider invoice that names a milestone does not prove the milestone was completed.

## 9. Support partial performance and holds

Professional work is not always all-or-nothing. A Provider may complete intake, drafting or review without completing the protected action. Funds and settlement should be capable of following accepted partial performance.

A hold may be appropriate where Evidence is missing, the beneficiary changed, official payment cannot be confirmed, a refund may be required or a dispute remains open.

A hold should state the amount, reason, authority, release condition and review date.

```text
funds hold
≠ finding of wrongdoing
```

It is a protective state pending resolution.

## 10. Refunds require layer-by-layer reconciliation

Cancellation does not produce one automatic refund answer.

The calculation may need to separate:

- earned Provider work;
- unused official-fee reserve;
- non-refundable disbursements;
- delivered platform service;
- currency and banking costs;
- disputed amounts;
- correction or failure responsibility.

```text
engagement cancelled
≠ every amount refundable
≠ no amount refundable
```

The result should follow the accepted terms, Evidence and applicable rules.

## 11. Payment labels must identify who paid whom

“Paid” can mean customer to Workplace, Workplace to platform, platform to Provider, Provider receipt or official-fee payment.

The interface should instead answer:

```text
paid by whom
→ to whom
→ for what
→ cleared when
→ evidenced how
```

This precision prevents one successful transfer from being mistaken for completion of the whole chain.

## 12. Representative failure patterns

### Customer paid, so the Matter is marked filed

The documents remain incomplete. The correction is to keep funds readiness separate from professional and action readiness.

### Provider reports official payment without receipt

The correction is to record the Provider assertion, seek the expected authoritative Evidence and leave formal state unresolved.

### Bank details change inside the same email thread

The correction is to hold payment and verify the new beneficiary through a trusted channel.

### Full settlement follows partial performance

The Provider prepared the work but did not complete the protected action. The correction is to settle only the accepted milestone value under the agreed terms.

## 13. Product principle

Funds should make fulfillment possible without becoming a substitute for fulfillment Evidence.

```text
typed funds checkpoints
+ explicit authority
+ beneficiary controls
+ milestone linkage
+ Finance reconciliation
= governable commercial flow
```

The next chapter explains how settlement follows accepted milestones and Evidence rather than invoices, optimism or elapsed time.
