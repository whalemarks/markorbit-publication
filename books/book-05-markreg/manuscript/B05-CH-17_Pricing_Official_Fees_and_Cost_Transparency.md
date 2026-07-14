# B05-CH-17 — Pricing, Official Fees and Cost Transparency

**Status:** Productized Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

CH16 produced a decision-ready Proposal. This chapter defines the price basis for each option and makes every cost driver, authority, currency, tax treatment, validity condition and later-stage exposure understandable.

The normative commercial model is `B05-SPEC-0004`.

## 1. User Question

> What will this option cost now, what may cost more later, and why does the amount change?

The Product must not present one unexplained total or describe a filing-stage amount as a lifecycle total.

## 2. Commercial Component Model

Every price component must carry a type, authority, source, scope, unit, currency, visibility and validity state.

| Component | Authority | Client visibility |
| --- | --- | --- |
| Official fee | official office or mandatory authority | visible |
| Professional fee | responsible organization | visible |
| Provider pass-through | external provider | visible or policy-approved summary |
| Internal provider cost | organization procurement | internal only |
| Tax | applicable tax authority and policy | visible |
| Currency adjustment | approved organization policy | visible when charged |
| Contingency | defined possible trigger | visible |
| Later-stage fee | future official or professional stage | visible as included, excluded or estimated |
| Discount | authorized commercial approval | visible; approval evidence internal |
| Margin | internal commercial measure | internal only |

`Provider Cost ≠ Client Price`. Internal procurement and margin data remain access-controlled.

## 3. Fee-Driving Units

The price model must expose quantities such as:

- application or filing unit;
- jurisdiction or designation;
- class and item count;
- applicant or priority claim;
- search level;
- document, translation, certification or courier step;
- professional review cycle;
- procedural stage;
- provider or connector route.

A scope change identifies which components require recalculation instead of replacing one opaque total.

## 4. Official-Fee Evidence

An official-fee component must identify:

- jurisdiction and office;
- route and fee type;
- applicable applicant, class, item or stage rule;
- original currency and amount;
- effective date;
- source and retrieval date;
- jurisdiction-pack version;
- assumptions and confidence.

A number without source and effective date is not a reliable official-fee representation.

## 5. Currency and Exchange Rate

Every converted amount must retain:

```text
Source Currency
Presentation Currency
Rate Source or Approved Policy
Rate Timestamp
Spread or Buffer
Rounding Rule
Validity
Repricing Threshold
Variance Allocation
```

The Product may calculate an approved policy. It may not hide margin inside an “official fee” or invent an exchange-rate policy.

## 6. Tax, Bank and Remittance Treatment

The price surface must state whether amounts are:

- tax inclusive or exclusive;
- subject to VAT, GST, withholding or gross-up;
- subject to card, bank or intermediary charges;
- payable in a different currency;
- subject to provider or official remittance deductions.

Tax treatment must come from applicable policy or review, not a generic AI assumption.

## 7. Later-Stage Cost Treatment

Every foreseeable later stage must be classified:

```text
Included Now
Expected Later
Possible or Contingent
Unknown Until Event
Excluded
```

Examples include registration fees, publication fees, office-action responses, opposition, evidence, certificates, declarations, renewals, recordals and legalization.

## 8. Estimate, Cap and Fixed Price

These labels have different effects:

| Price form | Meaning |
| --- | --- |
| Estimate | current expected amount subject to stated change conditions |
| Cap | amount will not exceed the stated ceiling under the stated scope |
| Fixed price | stated scope is priced at the stated amount under defined conditions |

The Product must not label an estimate as fixed or imply that an initial package covers unknown disputes.

## 9. Discounts and Margin Authority

A discount requires:

- affected component;
- amount or percentage;
- reason;
- approving role;
- minimum-margin or exception result;
- validity and one-time conditions.

Discounts must not alter official-fee labels. AI may calculate an approved discount but cannot grant one.

## 10. Payment Schedule

The price model may support:

- full prepayment;
- deposit plus balance;
- filing-stage and registration-stage payments;
- official-fee advance;
- recurring portfolio billing;
- approved credit terms.

The schedule explains when funds are required. It does not represent payment receipt or filing approval.

## 11. EMBERLOOP Reference Journey

For selected Proposal Option B, the Product creates a price basis for word and device filings in US, EU and UK.

The client sees:

- official fees by jurisdiction and filing unit;
- organization professional fees;
- US provider pass-through costs;
- applicable tax treatment;
- quote currency and source currencies;
- deposit requirement;
- registration-stage and office-action fees as excluded or estimated;
- expiry tied to fee, provider-rate and exchange-rate validity.

Internal users may also see provider cost, discount authority and margin. The client does not see protected procurement details.

## 12. Conformance Scenario — Fee Change Before Filing

**Given** the client later accepts a valid Quote based on an official-fee version.  
**When** the relevant official fee changes before filing.  
**Then** MarkReg compares old and new sources, applies the accepted variance policy, identifies affected amounts and determines whether revised acceptance is required.  
**Authority boundary:** no silent repricing and no invented waiver.  
**Evidence retained:** both fee versions, Quote terms, variance calculation, approver and client decision.

## 13. User Surface

The pricing screen should provide:

1. total payable now;
2. component breakdown;
3. original and presentation currencies;
4. tax and payment treatment;
5. included and excluded stages;
6. possible later costs;
7. validity and repricing conditions;
8. scope changes that alter price;
9. one action: proceed to Quote, revise scope, or request commercial review.

## 14. Failure Modes

The Product must reject:

```text
Official and professional fees merged without labels
Provider cost exposed as margin data
Exchange rate or tax treatment omitted
Per-class or per-item rule hidden
Later registration fee silently omitted
Discount applied without authority
Estimate presented as fixed
Accepted price overwritten
Unpaid amount displayed as received
```

## 15. Chapter Output

The output is a versioned commercial price basis linked to the selected Proposal option and exact fee, currency, tax and provider sources.

The next chapter turns that basis into a binding-capable Quote, records exact acceptance, and separates Commercial Instruction from payment and filing authority.