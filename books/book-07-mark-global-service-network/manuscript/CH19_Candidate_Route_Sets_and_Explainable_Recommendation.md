# B07-CH-19 — Candidate Route Sets and Explainable Recommendation

## From eligible supply to a bounded decision surface

After hard gates are applied, MGSN may still have several viable routes. The Product must turn that eligible set into a decision surface a professional can understand and use.

It does not expose the whole provider pool. It creates a Candidate Route Set for the current Capability Need.

```text
Eligible supply
→ Candidate Route Set
→ Recommended Route
→ up to two meaningful alternatives
```

## Candidate Route Set

A Candidate Route Set contains only routes that:

- satisfy mandatory eligibility;
- have current Qualification;
- pass conflict and availability checks to the required stage;
- fit an admitted Service Package;
- comply with restrictions and payment constraints;
- can plausibly meet the deadline;
- remain within the selected route constitution.

A Candidate Route Set is temporary and need-specific. It is not a permanent provider ranking.

## Recommendation dimensions

The Recommended Route should be based on a controlled sequence of considerations:

1. legal and operational eligibility;
2. relevant Capability and professional fit;
3. conflict and current availability;
4. deadline feasibility;
5. risk and continuity;
6. relationship provenance where relevant;
7. service-specific performance and Trust;
8. time and communication fit;
9. price and procurement terms;
10. platform margin and supply utilization only within the preceding constraints.

Commercial factors may distinguish otherwise suitable routes. They may not rescue an unsuitable one.

## One recommendation, not a wall of options

The default user experience should present one Recommended Route.

Where useful, MGSN may add up to two alternatives that are materially different, such as:

- lower price with a longer expected turnaround;
- faster route with an urgency surcharge;
- a relationship-preserved provider;
- a specialist route for unusual complexity;
- a backup route with stronger continuity;
- an external self-managed option.

Alternatives should not be cosmetic duplicates.

```text
More options
≠ better decision support
```

## Explainability

A recommendation should explain the relevant reasons without exposing confidential procurement data, internal weights or the complete provider pool.

A user-facing explanation may include:

- why the route fits the service;
- expected timing;
- important assumptions;
- scope and deliverables;
- material risk notes;
- whether the provider is relationship-preserved;
- why an alternative differs;
- which facts remain uncertain.

It should not falsely imply certainty where the result still depends on provider acceptance, official action or unknown facts.

## Recommendation confidence

The Product may distinguish:

- strong recommendation;
- conditional recommendation;
- preliminary recommendation;
- operator review required;
- no safe recommendation.

Confidence should reflect the quality and freshness of the inputs, not merely algorithmic consistency.

## Provider identity disclosure

Provider identity may be disclosed in stages according to service type, route, conflict needs and commercial controls.

Possible stages include:

- route characteristics before confirmation;
- provider identity where meaningful for informed choice;
- controlled identity disclosure after user disposition;
- direct operational contact only when permitted by the engagement model.

Staged disclosure protects the platform's network resources without turning routing into a blind assignment.

## Internal recommendation evidence

The Product should preserve:

- Candidate Route Set version;
- excluded routes and gate reasons;
- recommendation dimensions used;
- material data sources;
- recommendation outcome;
- uncertainty and assumptions;
- operator overrides;
- commercial exceptions;
- related-party indicators.

This allows later review when an outcome is challenged.

## Operator overrides

An operator may override the machine-generated order where justified by:

- newly discovered risk;
- provider communication not yet reflected in structured data;
- urgent deadline realities;
- a relationship constraint;
- sanctions or payment developments;
- quality concerns;
- a valid user instruction.

An override must be reasoned and auditable.

```text
Operator authority
≠ invisible discretionary favoritism
```

## Recommendation refresh

The recommendation should be refreshed when:

- availability expires;
- the Service Offer expires;
- a provider declines;
- the Capability Need changes;
- a new conflict appears;
- a restriction is imposed;
- timing becomes materially different;
- the user requests rematching.

The Product should not display a stale recommendation as current.

## Avoiding pseudo-neutrality

A recommendation system is not neutral merely because it uses a formula. Bias can enter through:

- incomplete provider coverage;
- stale Evidence;
- hidden paid placement;
- margin optimization;
- historical concentration;
- relationship favoritism;
- operator habits;
- uneven data quality.

MGSN therefore requires governance over both inputs and decision rules.

## Product consequence

The Candidate Route Set and Recommended Route convert complex network supply into bounded professional choice.

The objective is not to show everything. It is to present the best supported route, reveal meaningful alternatives and preserve enough explanation for the user to make the final decision.