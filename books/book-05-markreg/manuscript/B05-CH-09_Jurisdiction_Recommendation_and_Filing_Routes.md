# B05-CH-09 — Jurisdiction Recommendation and Filing Routes

**Status:** Revised Draft — Productized  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part II — Need, Strategy and Recommendation  
**Revision basis:** B05-REVISION-PACK-001

## Chapter Purpose

This chapter defines how MarkReg converts a confirmed Need Brief into explainable jurisdiction and filing-route recommendations.

The Product must help the user answer two separate questions:

1. where protection is needed;
2. which direct, regional, or international route is appropriate.

A country recommendation is not automatically a route recommendation, and neither is a filing instruction.

## 1. Product Question

> Which jurisdictions matter now, which can wait, and which route best fits each priority under the current facts?

The answer must reflect business need rather than a generic list of available countries.

## 2. Required Inputs

The Product consumes:

- confirmed Need Brief version;
- current and planned markets;
- manufacturing, sales, distribution, licensing, and crowdfunding context;
- existing applications and registrations;
- applicant eligibility and possible basic filings;
- timing and priority constraints;
- budget and risk posture;
- jurisdiction-pack versions;
- local-representation and provider requirements.

Jurisdiction rules must satisfy the minimum contract in [B05-SPEC-0004](../specifications/B05-SPEC-0004_Jurisdiction_Pack_and_Commercial_Control_Contract.md).

## 3. Recommendation Categories

Each jurisdiction should be classified as one of:

| Category | Meaning |
| --- | --- |
| Required now | A material commercial, legal, timing, or defensive reason supports immediate action. |
| Strongly recommended | Significant value or risk justifies action, but deferral remains possible. |
| Optional | Useful protection with lower immediate priority. |
| Deferred | Relevant later, with a recorded trigger for reconsideration. |
| Not recommended | Current cost, eligibility, route, evidence, or business facts do not justify action. |
| Professional review required | The Product cannot safely rank the jurisdiction without accountable judgment. |

The Product must explain the reason and evidence for the category.

## 4. Filing-Route Comparison

For each jurisdiction, MarkReg may compare:

- direct national filing;
- regional filing;
- international registration route;
- later designation or expansion;
- local filing through a provider;
- a controlled decision not to file yet.

The comparison must show:

- eligibility dependencies;
- territorial scope;
- dependency on a basic application or registration where applicable;
- language and representation requirements;
- approximate timing and uncertainty;
- fee-driving units;
- document requirements;
- provider or connector dependency;
- later-stage obligations;
- major failure or dependency risks.

## 5. Recommendation Set Contract

Jurisdiction and route outputs form part of `MR-A03 Recommendation Set`.

Each entry includes:

- jurisdiction and office identity;
- route candidate;
- recommendation category;
- business rationale;
- jurisdiction-pack version and source status;
- assumptions;
- confidence or interpretation status;
- cost and timing effects;
- provider need;
- unresolved issues;
- professional review status;
- alternative routes.

A route selected by the user remains a Product decision candidate until required review and formalization occur.

## 6. User Surface

The user should see a comparison rather than a map of unexplained countries.

The primary surface shows:

- required, recommended, optional, and deferred jurisdictions;
- route alternatives for each jurisdiction;
- why each option is suggested;
- what changes if a market is added or removed;
- source freshness or uncertainty warnings;
- one primary action: **Compare and set priorities**.

The Product should not present all jurisdictions as equally urgent.

## 7. Reference Journey A — EMBERLOOP

MarkReg presents:

- **Option A:** United States and European Union first; United Kingdom later;
- **Option B:** United States, European Union, and United Kingdom first;
- **Option C:** evaluate an international route after confirming a suitable basic filing;
- **Deferred:** Japan and Australia until launch traction or distribution plans become clearer.

The Product exposes route dependencies, local-representation requirements, expected later costs, and timing uncertainty. It does not label one route “best” without assumptions.

## 8. Conformance Scenarios

### MR-CH09-SCN-01 — Route dependency changes

**Given** an international route depends on a basic filing that has not been confirmed.  
**When** route options are shown.  
**Then** MarkReg presents the route as conditional, identifies the missing dependency, and preserves a direct-filing alternative.  
**Authority boundary:** the Product does not invent eligibility.  
**Evidence retained:** pack version, eligibility rule, source facts, alternatives, and professional decision.

### MR-CH09-SCN-02 — Stale jurisdiction rule

**Given** a required representation or fee rule is stale or conflicting.  
**When** a deadline-sensitive recommendation is prepared.  
**Then** MarkReg labels the rule status, blocks protected-action readiness where necessary, and requests source refresh or professional verification.  
**Authority boundary:** sourced Product configuration is not official truth by itself.  
**Evidence retained:** old rule, source date, refresh attempt, and resulting decision.

This applies `MR-SCN-10` and `MR-CR-05`.

## 9. Change Propagation

Adding or removing a jurisdiction may change:

- route eligibility;
- provider need;
- filing units;
- classes and goods/services versions;
- search scope;
- documents;
- fees and currency exposure;
- timelines;
- readiness.

The Product must identify affected artifacts rather than silently updating them.

## 10. Handoff to CH10

CH09 produces versioned jurisdiction and route candidates within the Recommendation Set.

CH10 may compose these candidates into understandable country bundles and portfolio scenarios, but a bundle must never hide the independent legal, cost, evidence, and lifecycle consequences of each jurisdiction.