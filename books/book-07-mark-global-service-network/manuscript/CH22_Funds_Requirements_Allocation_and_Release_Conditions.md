# B07-CH-22 — Funds Requirements, Allocation and Release Conditions

## 1. Why funds need a separate control model

International professional services combine several money types that must not be collapsed into one number:

- official fees;
- taxes and mandatory charges;
- third-party disbursements;
- provider service fees;
- platform service and risk costs;
- Originating Workplace margin;
- contingency or variable amounts;
- refunds and reconciliation adjustments.

A managed route therefore needs typed funds controls, not an undifferentiated payment status.

## 2. Funds Requirement

A Funds Requirement states what financial precondition must be satisfied before a defined next step may occur.

It should identify:

- amount or calculation method;
- currency;
- purpose;
- payer and intended beneficiary context;
- due time;
- applicable offer version;
- fixed, estimated, capped or actual-cost nature;
- exchange-rate assumptions;
- refundability or non-refundability assumptions;
- legal or regulatory restrictions;
- the action or milestone it enables.

```text
Funds Requirement
≠ invoice
≠ receipt
≠ ledger posting
≠ proof that money was received
```

Those facts belong to the relevant Finance Owning Service.

## 3. Purpose allocation

When funds are received or authorized, MGSN may maintain a purpose-level allocation projection:

```text
available funds signal
→ purpose allocation
→ readiness evaluation
```

Typical purposes include:

- official filing fee;
- provider professional fee;
- translation or legalization;
- courier or certification;
- platform-managed service cost;
- approved contingency.

Purpose allocation prevents one payment from being treated as universally available for any later expense.

```text
Funds Allocation
≠ ownership of money
≠ Finance Ledger
≠ permission to move money
```

## 4. Release Condition

A Release Condition defines the evidence and approvals required before a contemplated payment or settlement step may proceed.

Possible conditions include:

- provider acceptance;
- instruction readiness;
- official filing evidence;
- milestone completion;
- satisfactory correction;
- absence or resolution of dispute;
- operator approval;
- customer or Workplace approval where required;
- legal, sanctions, tax or foreign-exchange clearance.

A condition can be met, unmet, waived by authorized policy, disputed or expired.

```text
Release Condition met
≠ automatic transfer
```

Actual custody, movement and release require a lawful payment architecture and an authorized Finance service.

## 5. Staged funding

Some engagements need staged funding rather than full advance payment.

A controlled structure may separate:

1. initial commitment amount;
2. official-fee amount;
3. provider milestone amount;
4. variable disbursement reserve;
5. registration or completion-stage amount;
6. refund or reconciliation amount.

Staging must follow the accepted commercial model and must not disguise later unavoidable charges.

## 6. Changes and shortfalls

A funds shortfall can arise from:

- official-fee change;
- exchange-rate movement;
- scope expansion;
- unexpected disbursement;
- tax or withholding;
- corrected provider quotation;
- customer-requested urgency.

The platform must distinguish:

```text
forecast variance
commercial exception
scope change
provider error
platform error
official-fee change
```

The response may require an updated offer, additional approval, use of an approved contingency, cancellation or dispute handling.

No silent reallocation is permitted when the purpose or amount materially changes.

## 7. Refunds and reconciliation

Cancellation or failure does not always mean a full refund. The governed result depends on:

- whether official fees were already paid;
- whether professional work was completed;
- whether the provider breached the accepted scope;
- whether the Originating Workplace changed instructions;
- whether a third-party cost is recoverable;
- whether replacement is available;
- applicable client-money and consumer rules.

MGSN can coordinate a Settlement and Reconciliation Projection, while the Finance Owning Service records the authoritative financial result.

## 8. Legal and implementation gates

Before production funds control exists, the implementation must resolve:

- contracting entities;
- payment-service providers;
- client-money or escrow regulation;
- segregation and safeguarding;
- tax and invoicing;
- foreign exchange;
- sanctions and AML obligations;
- chargebacks and refunds;
- insolvency treatment;
- accounting ownership and audit.

This chapter defines product controls only. It does not claim a universal escrow, custody or funds-release license.
