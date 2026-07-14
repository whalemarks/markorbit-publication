# B05-SPEC-0004 — Minimum Jurisdiction-Pack and Commercial-Control Contract

## Status

- **Status:** Controlled Draft
- **Applies to:** Book 05 Parts II–IV
- **Purpose:** Define the minimum rule and commercial dependencies required before governed filing execution is drafted

## 1. Minimum Jurisdiction-Pack Contract

A jurisdiction pack is a versioned Product configuration and evidence bundle. It is not law, legal advice, an official office, or an autonomous authority.

Each pack must provide, where applicable:

| Area | Minimum content |
| --- | --- |
| Identity | jurisdiction, office, route, service family, language, pack version, effective date |
| Sources | source identifiers, source type, retrieval date, effective date, confidence, interpretation status |
| Eligibility | applicant, representation, filing basis, priority, signatory and provider conditions |
| Filing units | accepted mark types, image/file rules, color, transliteration, series or variant constraints |
| Classification | edition/version, local deviations, class-count rules, item limits and fee-count behavior |
| Goods/services | accepted vocabularies, local wording rules, limitations, amendment constraints |
| Search | available search modes, data coverage, known limitations and freshness |
| Documents | POA, signature, scan/original, notarization, legalization, translation and certification rules |
| Fees | official-fee components, currency, tax status, unit logic, effective date and source |
| Deadlines | event basis, calculation rule, timezone/calendar, extension rules, source authority |
| Provider need | local-representation requirement, capability, language, conflict and credential conditions |
| Validation | blockers, warnings, conditional rules, override authority and expiry triggers |
| Execution entry | accepted package shape, connector/provider route, acknowledgement expectations |
| Outcome mapping | official identifiers, statuses, evidence and lifecycle continuation |

## 2. Rule Evaluation Requirements

Every material rule evaluation must retain:

- pack version;
- source reference;
- source effective or retrieval date;
- input values consumed;
- result;
- confidence or interpretation status;
- override availability and authority;
- affected Product artifacts;
- revalidation triggers.

A jurisdiction-pack update must not silently mutate an accepted Quote, approved Filing Package, formal instruction, or completed official outcome. It must identify affected journeys and require the appropriate revalidation.

## 3. Freshness and Conflict

Rules may be marked:

- current and source-backed;
- current but interpretation-required;
- stale;
- conflicting;
- incomplete;
- unavailable.

Protected action must be blocked when a required rule is unavailable, stale beyond policy, or materially conflicting unless an authorized professional records a sourced decision.

## 4. Commercial Component Model

A Quote may contain:

| Component | Description | Visibility |
| --- | --- | --- |
| Official fee | fee payable to an office or mandatory authority | client-visible |
| Professional fee | organization charge for professional work | client-visible |
| Provider pass-through | external provider charge passed through | client-visible or summarized under policy |
| Internal provider cost | organization procurement cost | internal only |
| Tax | applicable tax, with inclusive/exclusive treatment | client-visible |
| Currency adjustment | controlled conversion or buffer | client-visible when charged |
| Contingency | explicitly described possible cost | client-visible |
| Later-stage fee | examination, publication, registration, response, renewal or other future stage | client-visible as included, excluded, or estimated |
| Discount | approved reduction and basis | client-visible; approval evidence internal |
| Margin | internal commercial measure | internal only |

## 5. Quote Controls

Every Quote must state:

- scope and service family;
- jurisdictions, filing units, classes, items or other fee-driving units;
- component amounts and currencies;
- tax-inclusive or tax-exclusive treatment;
- exchange-rate source or organization rate policy;
- rate timestamp and validity;
- validity and expiry;
- assumptions;
- inclusions and exclusions;
- later-stage fees;
- provider pass-through policy;
- official-fee-change treatment;
- payment schedule;
- refund and cancellation treatment;
- approval identity for discounts or exceptions;
- superseded Quote reference where applicable.

## 6. Exchange-Rate Policy

The organization must define:

- permitted rate sources;
- base and quote currencies;
- spread or buffer policy;
- rounding rule;
- refresh frequency;
- threshold for repricing;
- treatment of gains and losses;
- client-visible explanation.

The Product may calculate. It may not invent a rate policy or hide an unapproved margin inside an “official fee.”

## 7. Discounts and Margin Authority

Discounts must identify:

- amount or percentage;
- affected components;
- reason;
- approving role;
- minimum-margin or exception rule;
- expiry or one-time condition.

Client-visible discounts must not alter official-fee labels. Internal margin and cost data must remain access-controlled.

## 8. Deposits, Staged Payments, and Payment Readiness

Payment schedules may include:

- full prepayment;
- deposit plus balance;
- filing-stage and registration-stage payments;
- recurring portfolio payments;
- approved credit terms.

Commercial readiness must show the exact payment condition currently required. A received deposit does not equal filing approval, and professional readiness does not imply payment readiness.

## 9. Official-Fee and Provider-Cost Changes

When a fee changes after Quote creation, MarkReg must determine:

1. whether the Quote is still valid;
2. whether the accepted terms allocate the variance;
3. whether the change exceeds an approved threshold;
4. whether revised acceptance is required;
5. whether payment or refund adjustments are required;
6. which artifacts and readiness dimensions are affected.

No amount may be silently changed after acceptance.

## 10. Refund, Cancellation, and Failed Filing

Commercial policy must distinguish:

- unperformed professional work;
- completed professional work;
- unrecoverable official fees;
- refundable official fees;
- provider cancellation charges;
- foreign-exchange differences;
- client-caused delay or invalid instruction;
- organization or provider failure;
- duplicate or rejected payment;
- filing failure before and after official receipt.

The Product records and explains the applicable policy. Owning financial services remain authoritative for actual receipts, refunds, and accounting records.

## 11. Commercial Conformance Tests

A commercial flow conforms only when it can demonstrate:

- expired Quotes cannot be silently accepted;
- changed fees trigger controlled variance handling;
- tax and currency treatment are visible;
- discounts require the correct authority;
- internal cost and margin remain access-controlled;
- payment stages remain separate from professional and execution approval;
- later-stage fees are not misleadingly represented as included;
- refunds and failed filings preserve an auditable component history.
