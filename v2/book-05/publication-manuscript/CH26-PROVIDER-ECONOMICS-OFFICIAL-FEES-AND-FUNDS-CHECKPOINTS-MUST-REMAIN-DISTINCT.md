# Chapter 26 — Provider Economics, Official Fees and Funds Checkpoints Must Remain Distinct

International trademark delivery combines several financial systems that look similar from the customer side but carry different authority, risk and evidence.

```text
Official Fee
≠ Provider Professional Fee
≠ MarkReg Service Fee
≠ Contributor Compensation
≠ Tax, Courier or Remittance Cost
```

When these categories are collapsed, customers cannot understand price changes, Workplaces cannot calculate real margin and failures become difficult to assign.

## 1. Provider procurement is a formal service relationship

A Provider arrangement may include:

- service scope;
- jurisdiction and procedure;
- professional qualification;
- official fees;
- Provider professional fees;
- currency and tax;
- prepayment requirements;
- quote validity;
- expected turnaround;
- document and original requirements;
- evidence-return obligations;
- correction and replacement duties;
- cancellation and refund rules.

```text
Provider Listed
≠ Provider Eligible
≠ Provider Appointed
≠ Provider Accepted
```

## 2. Official fees must retain source and effective date

An Official Fee record should preserve:

- issuing authority;
- jurisdiction;
- action and phase;
- class or item basis;
- currency;
- effective date;
- source;
- exemptions or surcharges;
- late or restoration fees;
- verification state.

A Provider invoice may report an official fee, but it does not automatically become the authoritative fee source.

```text
Provider-reported Official Fee
≠ Independently Verified Official Fee
```

## 3. Fee change propagation

When an official fee changes, MarkReg should identify affected:

- public pages;
- GEO answers;
- calculators;
- Quote Candidates;
- accepted but unpaid quotations;
- Orders;
- Provider instructions;
- pending funds checkpoints;
- customer communications.

The system should not silently absorb or pass on a material change without applying the relevant contract and approval rules.

## 4. Funds checkpoints are readiness states

A funds checkpoint may answer:

- has the customer paid the Workplace?;
- has the Workplace approved remittance?;
- has the Provider requested prepayment?;
- are official funds available?;
- has currency conversion completed?;
- has the Provider confirmed receipt?;
- has the official authority received payment?;
- is a refund or credit pending?

```text
Customer Paid
≠ Provider Paid
≠ Official Fee Paid
≠ Filing Completed
```

## 5. Payment status and professional readiness remain separate

A Matter may be:

- professionally ready but awaiting funds;
- paid but missing documents;
- Provider-funded but not customer-approved;
- officially paid but submission status unknown;
- overpaid with credit pending;
- commercially disputed while deadline risk continues.

No single `paid=true` field can represent this safely.

## 6. No unrestricted custody is implied

MarkReg may record external payment and escrow status. It does not thereby gain authority to hold customer or transaction funds.

```text
Payment Orchestration
≠ Payment Custody

Funds Record
≠ Permission to Move Funds
```

Custody, escrow, netting and money transmission require separate legal, commercial and operational authorization.

## 7. Provider quote uncertainty must remain visible

Provider prices may depend on:

- number of classes;
- goods length;
- local publication surcharges;
- translation;
- document legalization;
- exchange rates;
- VAT or withholding;
- urgency;
- unexpected objection;
- original-document courier.

MarkReg should label amounts as fixed, estimated, variable, contingent or pending confirmation.

```text
Provider Estimate
≠ Final Procurement Cost
```

## 8. Provider economics differ from Contributor economics

A Contributor is usually paid for a bounded Work Package. A Provider Organization may accept an accountable external professional service route.

Provider economics may include:

- professional fee;
- official-fee handling;
- organizational overhead;
- regulated responsibility;
- local representation;
- evidence and return obligations;
- replacement or correction duty.

```text
Provider
≠ Contributor with More Permissions
```

## 9. Procurement comparisons require same-scope normalization

Provider comparison should consider:

- included phases;
- official fees;
- service fees;
- document handling;
- evidence returned;
- response time;
- reliability;
- correction obligations;
- customer communication route;
- total expected cost.

The cheapest quote may exclude registration, publication, certificate, courier or later mandatory fees.

## 10. Total expected cost matters

```text
Quoted Provider Cost
+ Review Burden
+ Rework Probability
+ Delay Exposure
+ Replacement Risk
+ Customer-support Cost
+ Refund Exposure
= Expected Delivery Cost
```

A reliable Provider can improve margin despite a higher direct fee.

## 11. Provider prepayment and customer approval

A Provider may require prepayment before filing. MarkReg must still verify:

- customer-approved scope;
- current fee version;
- Provider acceptance;
- deadline;
- refund rule;
- payment receiver;
- currency and remittance details.

```text
Provider Requests Funds
≠ Customer Approved Additional Cost
```

## 12. Credits, refunds and reconciliation

Financial reconciliation should record:

- amount requested;
- amount paid;
- amount applied;
- unused balance;
- refund due;
- credit carried forward;
- currency difference;
- bank or platform charge;
- responsible party;
- evidence.

A case should not be financially closed merely because the professional action is complete.

## 13. Failure scenarios

Governed exceptions include:

- official fee increased after quotation;
- Provider failed after prepayment;
- payment sent to wrong or outdated account;
- duplicate payment;
- currency shortfall;
- Provider invoice conflicts with prior quote;
- official fee paid but filing rejected;
- refund promised but not received;
- Provider holds original documents pending account settlement.

Each requires containment, evidence, customer communication, recovery responsibility and financial state updates.

## 14. Product implications

MarkReg requires:

- separate official, Provider, MarkReg, Contributor and ancillary charge records;
- sourced Official Fee records;
- Provider procurement packages;
- funds checkpoints;
- payment and professional-readiness separation;
- quote uncertainty labels;
- fee-change propagation;
- remittance and reconciliation evidence;
- credits and refunds;
- provider reliability and expected-cost analytics.

## 15. Operating principle

```text
Separate every financial role
Verify official fees
Expose uncertainty
Gate remittance by approval
Track funds through each checkpoint
Reconcile after delivery
Never infer custody authority from orchestration
```

> Reliable global delivery depends not on showing one simple price, but on preserving the real path from customer approval through Provider procurement and official payment to evidenced completion.