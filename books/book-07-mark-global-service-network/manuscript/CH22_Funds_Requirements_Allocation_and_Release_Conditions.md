# B07-CH-22 — Funds Requirements, Allocation and Release Conditions

## 1. Product control over funds is not a universal escrow license

MGSN must coordinate money because managed international work creates official fees, provider charges, taxes, disbursements, refunds and settlement obligations. But a Product model cannot create legal authority merely by naming a balance “escrow”.

```text
Funds Requirement
≠ payment custody license
Funds Allocation
≠ accounting ledger
Release Condition
≠ automatic legal authority to release money
```

The legal entity, payment provider, client-money regime, jurisdiction, currency, tax and accounting treatment must be determined before implementation.

## 2. Funds Requirement

A Funds Requirement states what money must be available before a defined action or commitment may proceed.

It should identify:

- engagement and service scope;
- amount and currency;
- official-fee component;
- provider-service component;
- platform-service or risk component;
- variable or estimated amounts;
- payment deadline;
- permitted funding method;
- consequence of non-funding;
- refund and reconciliation assumptions.

A Funds Requirement is a controlled precondition. It is not proof that money has been received, safeguarded or released.

## 3. Purpose allocation

Money should be associated with an explicit purpose.

```text
Received or authorized funds
→ purpose allocation
→ eligible use
→ evidence of use or release
→ reconciliation
```

Typical purpose layers include:

- official fees;
- required disbursements;
- provider professional fees;
- platform-managed service fees;
- taxes or withholding;
- refundable contingency;
- approved additional work.

Purpose allocation prevents one engagement’s funds from being silently used for another purpose.

## 4. Separation from Finance authority

MGSN may project and coordinate funds checkpoints, but it does not own the authoritative Finance Ledger.

The Finance domain or designated payment/accounting service must remain authoritative for:

- actual receipts;
- balances;
- invoices;
- tax documents;
- payable and receivable recognition;
- settlement entries;
- refunds;
- currency conversion entries;
- accounting corrections.

MGSN should reference those authoritative facts rather than duplicate them as independent truth.

## 5. Release conditions

A Release Condition defines what must be true before a specified payment or settlement step may be considered eligible.

Possible conditions include:

- provider acceptance;
- verified filing instruction;
- milestone evidence received;
- official fee payable;
- completion accepted;
- correction period expired;
- dispute resolved;
- refund approved.

A release condition must be:

- linked to a defined amount or allocation;
- evidence-based;
- reviewable;
- time-scoped;
- reversible or correctable where legally possible;
- separated from the actor who benefits from the release when conflict risk exists.

## 6. Release eligibility versus release execution

MGSN may determine that a condition appears satisfied. A legally authorized payment component must execute the movement of funds.

```text
Condition evaluated
→ evidence reviewed
→ release eligible
→ authorized financial actor executes
→ authoritative ledger records
→ MGSN receives settlement projection
```

This prevents Product logic from bypassing legal, banking or accounting controls.

## 7. Variable fees and shortfalls

International services often involve uncertain amounts: official-fee changes, translation costs, courier costs, exchange-rate movements or authority-requested additions.

A shortfall should trigger one of the following:

- use an approved tolerance;
- request additional funds;
- revise the Service Offer;
- reduce or defer scope;
- cancel the pending action;
- open a commercial reconciliation.

The platform must not silently reduce protected work, advance unapproved credit or treat an estimate as a guaranteed final amount.

## 8. Refunds and unused balances

Unused or refundable amounts require traceable treatment.

The record should distinguish:

- official fee not incurred;
- provider work not performed;
- contingency not used;
- overpayment;
- exchange-rate remainder;
- disputed amount;
- non-refundable committed cost.

Refund eligibility and refund execution must be separately governed and recorded.

## 9. Disputes and holds

When completion, evidence, scope or responsibility is disputed, related releases may require a hold.

A hold should identify:

- disputed amount;
- affected allocation;
- reason;
- evidence requested;
- responsible reviewer;
- review deadline;
- permitted interim actions;
- final disposition.

A hold must not be used as arbitrary leverage, and a provider must have an appeal or review path.

## 10. Product rule

MGSN may govern funds requirements, purpose allocations, release eligibility and settlement projections only through explicit legal, accounting and payment authority boundaries. Product semantics never substitute for regulated financial authority.
