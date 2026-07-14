# B05-CH-17 — Pricing, Official Fees and Cost Transparency

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

CH16 produced `MR-A05 Proposal`. This chapter applies the commercial contract in B05-SPEC-0004 and prepares the transparent price basis consumed by `MR-A06 Quote`.

The `EMBERLOOP` reference step is `EL-10`.

## 1. Product Question

> What will this option cost now, what may cost more later, and why may the amount change?

One unexplained total is not sufficient. A filing-stage amount must not be presented as a lifecycle total.

## 2. Commercial Components

Every component records its type, authority, source, scope, unit, currency, visibility and validity.

| Component | Authority | Client visibility |
| --- | --- | --- |
| official fee | official office or mandatory authority | visible |
| mandatory third-party cost | required external service | visible |
| professional fee | responsible organization | visible |
| provider pass-through | external provider | visible or policy-approved summary |
| internal provider cost | organization procurement | internal only |
| tax | applicable authority and organization policy | visible |
| currency adjustment | approved organization policy | visible when charged |
| contingency | stated future trigger | visible |
| later-stage fee | future official or professional stage | included, excluded, estimated or unknown |
| discount | authorized commercial decision | visible; approval evidence internal |
| margin | internal commercial measure | internal only |

```text
official fee
≠ professional fee
≠ provider pass-through
≠ internal provider cost
≠ tax
≠ currency adjustment
≠ margin
```

Internal cost and margin must never be disguised as an official fee.

## 3. Fee-Driving Units

Price must expose the units that drive it, including:

- application or filing unit;
- jurisdiction or designation;
- class and item count;
- applicant or priority claim;
- search mode;
- translation, certification, legalization or courier step;
- Professional Review cycle;
- procedural stage;
- provider or connector route.

A scope change identifies the affected components instead of replacing one opaque total.

## 4. Official-Fee Evidence

An official-fee component identifies:

- jurisdiction and office;
- route and fee type;
- applicable applicant, class, item or stage rule;
- original currency and amount;
- effective date;
- Source Record and retrieval time;
- Pack Version;
- assumptions and unresolved uncertainty.

A number without source, scope and effective date is not a reliable official-fee representation.

## 5. Currency, Tax and Remittance

Every converted amount retains:

```text
source currency
presentation currency
rate source or approved policy
rate timestamp
spread or buffer
rounding rule
validity
repricing threshold
variance allocation
```

The price basis also states whether amounts are tax-inclusive or exclusive and whether bank, card, withholding, gross-up or remittance charges apply.

AI may calculate under an approved policy. It may not invent exchange-rate or tax treatment.

## 6. Later-Stage Cost Treatment

Each foreseeable stage is classified as:

```text
Included Now
Expected Later
Possible or Contingent
Unknown Until Event
Excluded
```

Relevant stages may include registration, publication, office-action response, opposition, evidence, certificates, declarations, renewal, recordal, transaction and legalization.

Unknown future work is not silently absorbed into the current price.

## 7. Estimate, Cap and Fixed Price

| Price form | Meaning |
| --- | --- |
| estimate | current expected amount subject to stated change conditions |
| cap | amount will not exceed a stated ceiling under stated scope |
| fixed price | stated scope is priced at the stated amount under defined conditions |

The Product must not label an estimate as fixed or imply that a filing package covers unknown disputes.

## 8. Discounts, Credit and Payment Schedule

A discount records the affected component, amount, reason, approving role, exception result, validity and one-time conditions.

Payment schedules may include:

- full prepayment;
- deposit plus balance;
- filing-stage and registration-stage payments;
- official-fee advance;
- recurring portfolio billing;
- approved credit terms.

A payment schedule states when funds are required. It does not establish that payment was received, reconciled or sufficient for filing.

## 9. Controlled Change and Reconciliation

`MR-SCN-07` applies when an official fee changes after acceptance. The Product compares old and new sources, applies the accepted variance policy and determines whether revised acceptance is required.

`MR-SCN-15` applies when a payment request may have succeeded but the technical result is unknown. A second charge is blocked until reconciliation completes.

No accepted Quote or payment state may be silently overwritten.

## 10. Reference Journey — `EL-10`

For `EMBERLOOP` Option B, the price basis covers word and device filings in US, EU and UK.

The client-visible view shows:

- official fees by jurisdiction and filing unit;
- professional fees;
- US provider pass-through;
- tax and currency treatment;
- deposit requirement;
- included and excluded stages;
- registration-stage and office-action fees as excluded or estimated;
- validity tied to fee, provider-rate and exchange-rate sources.

Internal users may separately see provider cost, discount authority and margin.

The result is consumed by Quote v3. The price basis itself is not acceptance or filing authority.

## 11. User Surface

Show:

1. amount payable now;
2. component breakdown;
3. original and presentation currencies;
4. tax and remittance treatment;
5. included and excluded stages;
6. foreseeable later costs;
7. validity and repricing conditions;
8. scope changes that alter price;
9. one action: proceed to Quote, revise scope or request commercial review.

## 12. Failure Modes

Reject:

```text
Official and professional fees merged without labels
Internal provider cost exposed as client price
Margin hidden in an official-fee label
Exchange rate or tax treatment omitted
Per-class or per-item rule hidden
Later-stage fee silently omitted
Discount applied without authority
Estimate presented as fixed
Accepted price overwritten
Unknown payment shown as failed or received
```

## 13. Chapter Output and Handoff

CH17 produces a versioned, source-backed commercial price basis for the selected Proposal option.

CH18 uses that basis to issue `MR-A06 Quote`, record exact `MR-D01 Client Acceptance` and create `MR-A07 Commercial Instruction`.