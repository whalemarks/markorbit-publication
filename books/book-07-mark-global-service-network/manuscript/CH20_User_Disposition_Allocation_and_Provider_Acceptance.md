# B07-CH-20 — User Disposition, Allocation and Provider Acceptance

## The user decides the route

MGSN may recommend, explain and constrain. It does not silently appoint a provider on behalf of the Originating Workplace.

The user must be able to disposition the presented route.

Typical dispositions include:

- confirm the Recommended Route;
- select an offered alternative;
- request rematching;
- request a preferred provider;
- choose the External Self-Managed Route;
- pause the decision;
- reject all routes;
- request clarification.

```text
Recommendation
≠ user instruction
```

## Meaningful confirmation

A valid confirmation should identify:

- the selected route;
- service scope;
- key assumptions;
- customer-facing offer or commercial reference;
- timing expectation;
- material exclusions;
- required documents or funds;
- provider identity where disclosure is required at that stage;
- acceptance of relevant terms.

Confirmation should not rely on hidden material conditions.

## User disposition is version-specific

The user confirms a particular version of:

- Capability Need;
- Candidate Route Set;
- Service Offer;
- route explanation;
- material provider or package conditions.

If those items change materially, the prior confirmation may no longer be sufficient.

```text
Materially changed route
→ renewed user disposition
```

## Allocation

After user confirmation, MGSN may create or prepare a Provider Allocation.

Allocation identifies the provider route the platform intends to instruct, subject to final controls.

It may include:

- selected Service Package;
- provider-side scope;
- deadline and priority;
- funds prerequisites;
- required conflict confirmation;
- instruction materials;
- acceptance deadline;
- contingency route;
- permitted disclosure scope.

```text
User confirmation
≠ Provider Allocation completed
```

An operator or controlled service may still need to verify funds, documentation, restrictions and instruction readiness.

## Provider Acceptance

The provider must accept the proposed engagement.

Provider Acceptance should confirm, as applicable:

- ability to perform the service;
- absence of disqualifying conflict;
- current capacity;
- acceptance of scope;
- acceptance of procurement and settlement terms;
- deadline feasibility;
- required professional responsibility;
- any disclosed subcontracting or local-agent structure;
- expected Evidence and Return obligations.

```text
Provider Allocation
≠ Provider Acceptance
```

## Provider responses

A provider may:

- accept;
- decline;
- request clarification;
- propose a permitted scope correction;
- identify a conflict;
- state that the deadline cannot be met;
- request a price or disbursement exception;
- disclose a required additional professional participant.

The response may trigger renewed user confirmation if it changes material terms.

## No silent substitution

If the allocated provider declines or becomes unavailable, MGSN must not silently substitute another provider while preserving the appearance of the original route.

The Product should:

1. record the failed or withdrawn allocation;
2. reassess the Candidate Route Set;
3. explain any material difference;
4. obtain renewed user disposition where required;
5. create a new Provider Allocation;
6. obtain new Provider Acceptance.

## Timing and expiry

User confirmation and Provider Acceptance may expire.

Expiry may be driven by:

- Service Offer validity;
- deadline movement;
- availability window;
- exchange-rate or official-fee change;
- qualification expiry;
- conflict-check freshness;
- provider acceptance deadline.

The Product should not treat stale consent as current authorization.

## Preferred-provider requests

A preferred-provider request is a user disposition, not a command that overrides governance.

MGSN should evaluate the requested provider through the same required gates. Outcomes may include:

- preferred provider accepted through R3;
- preferred provider conditionally available;
- preferred provider ineligible with explanation;
- alternative managed route offered;
- external R1 route selected by the Workplace.

## External-route disposition

When the user chooses R1, the Product should make the boundary visible.

The user should understand that MGSN is not assuming managed procurement, funds, fulfillment or replacement responsibility.

The Product may still define:

- expected Evidence;
- reminders;
- manual return fields;
- unknown-outcome handling;
- later resumption of Workplace continuity.

## Audit and non-repudiation

The Product should preserve:

- who made the disposition;
- authority to make it;
- timestamp;
- route and offer version;
- explanation shown;
- selected action;
- any override or exception;
- provider response;
- renewed confirmations.

This supports later resolution of disputes about what was recommended, selected or accepted.

## The final separation

The routing sequence contains three distinct decisions:

```text
MGSN recommends
→ user confirms
→ provider accepts
```

None can be silently collapsed into another.

The next stage begins only after a managed route has sufficient commitment to create a Managed Network Engagement and prepare funds, instruction and fulfillment controls.