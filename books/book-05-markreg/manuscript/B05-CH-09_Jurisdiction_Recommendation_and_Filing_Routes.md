# B05-CH-09 — Jurisdiction Recommendation and Filing Routes

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part II — Need, Strategy and Recommendation

## Chapter Purpose

This chapter converts a confirmed Need Brief into explainable jurisdiction and filing-route candidates.

It separates two questions:

1. where protection matters;
2. which direct, regional or international route is appropriate.

A jurisdiction recommendation is not automatically a route recommendation. Neither is a client Decision, filing instruction or statement that the jurisdiction/service is Execution Capable.

The controlled example is `EL-02` in B05-SPEC-0002.

## 1. Product Question

> Which jurisdictions matter now, which may be deferred, and which route fits each priority under the current facts?

The answer must reflect business activity, risk, timing, eligibility and cost rather than a generic country list.

## 2. Required Context

The Recommendation Set may consume:

- confirmed Need Brief version;
- current and planned markets;
- manufacturing, sourcing, sales, distribution, licensing and crowdfunding context;
- existing applications and registrations;
- applicant and basic-filing eligibility;
- timing, priority and budget constraints;
- risk posture;
- applicable Jurisdiction Pack versions;
- local-representation, provider and document requirements.

A Pack reference must identify jurisdiction, service, lifecycle stage, version and support state. Research Only or Guidance Capable evidence must not be presented as Execution Capable support.

## 3. Recommendation Categories

| Category | Meaning |
| --- | --- |
| Required now | A material commercial, legal, timing or defensive reason supports immediate action. |
| Strongly recommended | Significant value or risk supports action, although deferral remains possible. |
| Optional | Useful protection with lower current priority. |
| Deferred | Relevant later, with a recorded reconsideration trigger. |
| Not recommended | Current facts do not justify action. |
| Professional Review required | Material uncertainty prevents a reliable recommendation without accountable judgment. |

Each category must show its rationale, assumptions, source status and consequence.

## 4. Route Comparison

For each jurisdiction, MarkReg may compare:

- direct national filing;
- regional filing;
- international registration route;
- later designation or expansion;
- local-provider filing;
- a controlled Decision not to file yet.

The comparison should show:

- eligibility dependencies;
- territorial scope;
- dependency on a basic application or registration where applicable;
- language and representation requirements;
- timing and uncertainty;
- fee-driving units;
- document requirements;
- provider or connector dependency;
- later-stage obligations;
- major failure and dependency risks.

The Product must not label a route “best” without stating the facts and trade-offs that make it preferable.

## 5. Controlled Output

Jurisdiction and route candidates belong to:

```text
MR-A03 — Recommendation Set
→ MR-A04 — Option Set
```

Each entry records:

- jurisdiction and office identity;
- route candidate;
- recommendation category;
- business rationale;
- Pack Version, source status and support state;
- assumptions and confidence;
- cost and timing effects;
- provider or connector need;
- unresolved dependencies;
- Professional Review status;
- alternative routes;
- user selection state and supersession history.

Selection remains a Product Decision candidate until the required professional, client, commercial and formal boundaries are satisfied.

## 6. User Surface

The user should see a comparison rather than an unexplained map:

- required, recommended, optional and deferred jurisdictions;
- route alternatives;
- rationale and assumptions;
- main cost, timing and representation effects;
- source freshness and uncertainty warnings;
- the effect of adding or removing a market;
- one primary action: **Compare and set priorities**.

The interface should make clear that a recommendation is not a guarantee of eligibility, acceptance or registration.

## 7. Reference Journey — `EL-02 EMBERLOOP`

MarkReg compares:

- direct United States filing;
- European Union regional filing;
- direct United Kingdom filing;
- a conditional Madrid-route scenario that depends on a suitable basic filing;
- deferred Japan and Australia candidates.

The Recommendation Set preserves direct alternatives where route eligibility is unresolved. Japan and Australia remain future-action candidates; no filing is assumed.

## 8. Controlled Scenarios

### `MR-SCN-03` — Territory and route comparison

A request for “Europe” must be decomposed into EU, UK and relevant national consequences. A regional bundle is not one global right.

### `MR-SCN-13` — Material business change

A new launch market or changed timing creates a new recommendation version and identifies affected route, scope, search, Quote and Package records.

### `MR-SCN-14` — Client chooses a non-recommended option

The Product preserves the professional recommendation, records the informed client Decision and carries the consequences forward. Client selection does not rewrite the recommendation history.

Minimum evidence includes Pack Version, rule sources, alternatives, assumptions, professional disposition and client Decision.

## 9. Change Propagation

Adding or removing a jurisdiction may change:

- route eligibility;
- provider need;
- filing units;
- classes and goods/services;
- search scope;
- documents;
- official fee and client-price assumptions;
- timing and readiness.

The Product creates new Recommendation Set and Option Set versions. It must not silently alter an accepted Quote or approved Package.

## 10. Handoff to CH10

CH09 produces jurisdiction and route candidates.

CH10 composes them into understandable portfolio scenarios. A bundle may simplify comparison, but it must preserve the independent right, fee, evidence, deadline and lifecycle consequences of every jurisdiction.
