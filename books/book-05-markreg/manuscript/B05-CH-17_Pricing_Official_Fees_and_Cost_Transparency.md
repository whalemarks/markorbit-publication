# B05-CH-17 — Pricing, Official Fees and Cost Transparency

**Status:** Part III Draft  
**Chapter Map:** B05-TOC-V0.1  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

A proposal is not decision-ready unless its costs are understandable.

International trademark pricing is difficult because several cost authorities coexist:

- official offices;
- professional organizations;
- external providers;
- translators, notaries, couriers, banks, and tax authorities;
- exchange rates;
- later procedural stages;
- uncertain office actions and disputes.

The central proposition is:

```text
Transparent Cost Model
=
Scope Reference
+ Fee Components
+ Fee Authority
+ Quantity and Unit Logic
+ Currency
+ Exchange-Rate Basis
+ Tax and Bank Treatment
+ Included and Excluded Stages
+ Validity
+ Assumptions
+ Uncertainty
+ Recalculation Rules
```

```text
Price
≠ Official Fee
≠ Professional Fee
≠ Provider Cost
≠ Invoice
≠ Payment
≠ Lifecycle Total
```

---

## 1. Cost Has Several Authorities

An official fee is determined by an official body.

A professional fee is determined by the responsible organization under its commercial rules.

A provider cost may be quoted by an external professional or vendor.

Tax, bank, card, and remittance costs may come from different authorities.

MarkReg may assemble and calculate. It should not obscure who controls each component.

---

## 2. Official Fees Need Source and Version

An official-fee record should preserve:

- office;
- jurisdiction;
- fee type;
- filing route;
- applicant category where relevant;
- class or item basis;
- effective date;
- source;
- checked date;
- currency;
- amount;
- assumptions;
- version.

A number without source and date is not a reliable official-fee representation.

---

## 3. Official Fee Schedules May Be Conditional

Official fees may vary by:

- paper or electronic filing;
- applicant type;
- class count;
- item count;
- route;
- priority claim;
- color claim;
- expedited processing;
- publication;
- registration;
- certificate;
- amendment;
- extension.

The Product should express the rule, not only the current total.

---

## 4. Professional Fees Need Defined Scope

A professional fee should identify what work it covers.

Examples include strategy consultation, search, classification, drafting, filing preparation, provider coordination, review, filing, reporting, registration-stage handling, renewal preparation, and office-action response.

A line labelled “service fee” is too ambiguous when several organizations participate.

---

## 5. Provider Cost Is Not Automatically the Client Price

An external provider may quote official fees, professional fees, disbursements, tax, translation, courier, and later-stage work.

The organization may add its own coordination, professional, finance, and support value.

```text
Provider Cost
≠ Client Price
```

Private provider pricing and organization margin rules must remain protected.

---

## 6. Unit Logic Must Be Visible

A fee may be calculated per:

- application;
- filing unit;
- class;
- item;
- jurisdiction;
- designation;
- applicant;
- priority claim;
- document;
- signature;
- hour;
- response;
- stage.

The user should understand why the total changes.

---

## 7. Scope Changes Require Recalculation

A change in class count, goods/services count, filing unit, jurisdiction, route, applicant, search mode, or document scope may change several fee components.

The Product should identify which calculations became stale.

---

## 8. Currency Must Remain Explicit

Each amount should preserve:

- source currency;
- presentation currency;
- exchange-rate source;
- rate;
- checked time;
- spread or conversion rule;
- rounding rule.

A converted amount is not the original official fee.

---

## 9. Exchange-Rate Risk Must Be Allocated

Possible policies include:

```text
Fixed until quote expiry
Recalculated at acceptance
Recalculated at invoice
Recalculated at payment
Recalculated at remittance
Customer bears variance
Organization bears variance within tolerance
```

The policy should be visible before acceptance.

---

## 10. Tax and Bank Treatment Must Be Clear

The Product should identify whether amounts are tax inclusive, tax exclusive, subject to withholding, VAT or GST, card charges, bank fees, intermediary deductions, or gross-up.

Tax treatment may depend on payer, recipient, jurisdiction, and service type. It should not be guessed by a generic Product rule.

---

## 11. Filing-Stage and Later-Stage Costs Must Be Separated

A filing may later require examination response, publication, registration, certificate, maintenance declaration, proof of use, opposition response, or renewal.

Each later-stage cost should be classified as:

```text
Included
Expected but not yet due
Possible
Contingent
Unknown
Excluded
```

---

## 12. Estimate, Cap and Fixed Price Are Different

```text
Estimate
→ current expected amount, subject to change

Cap
→ amount will not exceed stated ceiling under stated scope

Fixed Price
→ stated scope is priced at a fixed amount under stated conditions
```

The Product should not label an estimate as fixed.

---

## 13. Contingency Needs a Defined Trigger

A contingency may relate to office action, objection, extra class, excess item, document legalization, urgency, provider change, route change, currency variance, tax, or extension.

A generic “additional charges may apply” is not sufficient where the likely trigger can be identified.

---

## 14. Discounts Need Authority and Scope

A discount record should identify:

- authorized organization;
- approver;
- basis;
- amount or percentage;
- affected fee components;
- validity;
- conditions;
- reason;
- exclusions.

AI may calculate an authorized discount. It may not grant one.

---

## 15. Packages Must Not Hide Legal Units

A multi-country or multi-class package may improve usability.

The underlying components should remain inspectable.

The package should not imply that all jurisdictions have one fee, all classes have the same consequence, all provider work is identical, or all later stages are included.

---

## 16. Cost Comparison Requires Like-for-Like Scope

Two options should not be compared only by total.

The Product should normalize jurisdictions, filing units, classes, items, search level, included stages, provider service, document work, later fees, tax, and exchange-rate basis.

A cheaper option may simply contain less.

---

## 17. Price Validity Needs Independent Reasons

A price may expire because official fees, provider rates, currency, discounts, scope, deadline urgency, tax treatment, or source verification changed.

Price validity may differ from strategic validity.

---

## 18. Price Revision Must Preserve History

A revised price should retain old component, new component, reason, effective time, source, affected scope, acceptance effect, invoice effect, and payment effect.

Past accepted terms should not be overwritten.

---

## 19. Quote Currency and Payment Currency May Differ

The Product should distinguish:

```text
Quote Currency
Invoice Currency
Payment Currency
Provider Currency
Official Fee Currency
Accounting Currency
```

This supports reconciliation and variance analysis.

---

## 20. Payment Timing Is Separate from Price

Payment may be prepaid, deposit plus balance, postpaid, credit account, milestone based, official-fee advance, provider advance, or reimbursable disbursement.

The pricing model should describe timing but should not present unpaid price as paid.

---

## 21. Cost Uncertainty Should Be Dimensional

Uncertainty may be:

- fee-schedule uncertainty;
- exchange-rate uncertainty;
- scope uncertainty;
- provider uncertainty;
- tax uncertainty;
- procedural uncertainty;
- timing uncertainty.

A single vague risk label is not enough.

---

## 22. AI May Explain Cost Drivers

AI may break down totals, compare options, detect omitted stages, recalculate quantities, explain currency impact, flag stale sources, prepare scenarios, and identify inconsistent tax treatment.

AI should not invent official fees, assume tax status, waive charges, promise fixed totals, hide later-stage cost, or change accepted price.

---

## 23. Failure Modes to Reject

```text
Official and professional fees merged without labels
Provider cost exposed as organization margin data
Initial filing fee shown as lifecycle total
Exchange rate omitted
Tax treatment guessed
Per-class rule hidden
Later registration fee omitted
Discount granted without authority
Estimate labelled fixed
Accepted price overwritten
Unpaid price displayed as paid
```

---

## 24. Minimum Pricing Lock

```text
Cost is decomposed by authority,
scope, unit, stage, currency,
tax, validity, assumption, and uncertainty.

Official fee, professional fee,
provider cost, invoice, payment,
and lifecycle total remain distinct.

A lower total is not automatically
a better or equivalent option.

AI may calculate and explain.

Only authorized organizations
set or approve commercial terms.
```

---

## 25. Handoff to Quote Formation

The output is a versioned Price Model attached to each proposal option.

The next chapter defines how one option becomes a Quote, how acceptance is recorded, and why commercial instruction still does not equal filing approval or submission.
