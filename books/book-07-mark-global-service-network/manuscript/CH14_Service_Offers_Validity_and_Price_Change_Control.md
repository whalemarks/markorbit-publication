# B07-CH-14 — Service Offers, Validity and Price Change Control

## The offer is a governed promise

A Service Offer is not a copied provider quotation and not a vague estimate. It is the demand-side commercial presentation of a defined MGSN route, package, assumptions, price and validity window.

It should answer five questions:

1. What service is being offered?
2. What is included and excluded?
3. What assumptions make the price valid?
4. How long is the offer valid?
5. What happens if a material assumption changes?

## Offer composition

A Demand-Side Offer may contain:

- jurisdiction and service type;
- route type;
- admitted Service Package version;
- scope, deliverables and expected evidence;
- required customer actions and documents;
- official-fee assumptions;
- variable disbursements;
- platform service layer;
- demand-side price;
- estimated timing;
- validity period;
- material exclusions;
- change triggers;
- cancellation, refund or credit rules where applicable.

The offer may refer to a Recommended Route without disclosing the full provider pool or internal procurement cost.

## Offer validity

Validity should be explicit because several inputs can expire:

- provider procurement terms;
- official-fee schedules;
- exchange-rate assumptions;
- provider availability;
- urgency windows;
- document assumptions;
- customer-specific eligibility;
- sanctions, tax or remittance conditions.

An expired offer must not be silently treated as current. The system should require refresh, operator confirmation or re-quotation.

## Assumptions and dependencies

A price can remain valid only while its assumptions remain true. Typical assumptions include:

- number of classes or items;
- applicant type;
- no legalization requirement;
- no opposition, refusal or hearing;
- standard processing speed;
- electronic rather than original documents;
- no additional translation;
- no late surcharge;
- no material official-fee change.

Assumptions should be visible enough for the demand participant to understand what can change.

## Price exceptions

A Price Exception is a controlled departure from the admitted package or standard offer. Examples include:

- urgent work;
- unusual evidence volume;
- complex ownership chain;
- mandatory local appearance;
- non-standard filing basis;
- exceptional courier or legalization cost;
- negotiated strategic pricing.

A Price Exception should record:

- reason;
- affected cost layer;
- approving authority;
- scope and duration;
- whether the provider term also changed;
- whether the user must reconfirm.

## Change control

A material change can occur before confirmation, after confirmation but before provider acceptance, or during fulfillment.

The response depends on timing:

```text
before user confirmation
→ revise or replace the offer

after user confirmation, before provider acceptance
→ disclose change and require renewed disposition where material

after provider acceptance
→ use exception, correction, additional approval, refund or dispute controls
```

A route should not continue merely because the original offer existed.

## Materiality

Not every internal variance requires user reapproval. Materiality should consider:

- total price impact;
- scope reduction;
- deadline impact;
- provider substitution;
- legal or professional-risk change;
- new customer obligation;
- loss of an included deliverable;
- change from fixed to estimated amount.

The threshold may differ by Product configuration and jurisdiction, but the rationale must remain reviewable.

## Commercial reconciliation

At the end of the transaction, the Product may compare:

- original offer;
- accepted revisions;
- actual official fees and disbursements;
- credits or refunds;
- approved additional work;
- final settlement projection.

Commercial Reconciliation explains the service economics. Formal posting remains with the appropriate Finance authority.

## No bait-and-switch routing

The platform must not display an artificially attractive offer and then substitute a materially different provider, scope or price without renewed control. Recommendation, offer, allocation and provider acceptance are separate stages, but the commercial promise must remain traceable across them.

## Control statement

A trustworthy offer is specific enough to be relied upon and conditional enough to remain honest. Validity and change control prevent both false certainty and uncontrolled repricing.
