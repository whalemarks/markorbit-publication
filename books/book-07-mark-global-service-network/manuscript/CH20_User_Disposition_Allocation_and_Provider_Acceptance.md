# B07-CH-20 — User Disposition, Allocation and Provider Acceptance

## The route decision has three authorities

MGSN may recommend, explain and constrain. It does not silently appoint a provider for the Originating Workplace.

The routing sequence contains three distinct decisions:

```text
MGSN recommends
→ the authorized user disposes the route
→ the provider accepts or refuses
```

Each decision answers a different question:

- **Recommendation** — which eligible route appears best supported?
- **User Disposition** — which route does the Originating Workplace authorize?
- **Provider Acceptance** — will the selected provider accept the defined work under the stated conditions?

```text
Recommendation ≠ user instruction
User Disposition ≠ Provider Allocation
Provider Allocation ≠ Provider Acceptance
```

None may be silently collapsed into another.

## User Disposition

The user must be able to:

- confirm the Recommended Route;
- select an offered alternative;
- request rematching;
- request an eligible preferred provider;
- choose the External Self-Managed Route;
- pause the decision;
- reject all routes;
- request clarification.

A valid disposition identifies the selected route, service scope, material assumptions, Service Offer reference, timing, exclusions, required Documents or funds, and the terms presented at that stage.

## Confirmation is version-specific

The user confirms a particular version of:

- the Capability Need;
- the Candidate Route Set;
- the Service Offer;
- the route explanation;
- material provider or package conditions.

A material change may invalidate the earlier confirmation.

```text
Materially changed route
→ reassessment
→ renewed User Disposition where required
```

The Product must not treat stale consent as current authority.

## Provider Allocation

After User Disposition, MGSN may prepare a Provider Allocation. The allocation identifies the provider route the platform intends to instruct, subject to final readiness controls.

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

An operator or controlled service may still need to verify funds, Documents, restrictions and instruction readiness. Allocation is therefore a controlled preparation decision, not proof that an engagement exists.

## Provider Acceptance

The provider must explicitly accept the proposed engagement. Provider Acceptance should confirm, as applicable:

- ability and authority to perform the service;
- absence of a disqualifying conflict;
- current capacity;
- accepted scope and exclusions;
- procurement and settlement terms;
- deadline feasibility;
- professional responsibility;
- any disclosed subcontracting or required local-agent structure;
- Evidence and Return obligations.

A provider may accept, decline, request clarification, identify a conflict, propose a permitted scope correction, state that the deadline cannot be met, request a commercial exception, or disclose a required additional professional participant.

A response that materially changes scope, timing, price or responsible party may require renewed User Disposition.

## No silent substitution

If the allocated provider declines or becomes unavailable, MGSN must:

1. record the failed or withdrawn allocation;
2. reassess the Candidate Route Set;
3. explain any material difference;
4. obtain renewed User Disposition where required;
5. create a new Provider Allocation;
6. obtain new Provider Acceptance.

A substitute provider must not be presented as though the original confirmed route remained unchanged.

## Timing and expiry

User Disposition and Provider Acceptance may expire because of:

- Service Offer validity;
- deadline movement;
- Availability window;
- exchange-rate or official-fee change;
- Qualification expiry;
- conflict-check freshness;
- provider acceptance deadline.

Expiry requires refresh, reassessment or renewed authority rather than silent continuation.

## Preferred-provider and external-route outcomes

A preferred-provider request is a User Disposition, not an instruction that overrides MGSN gates. The outcome may be:

- R3 with the preferred provider accepted;
- conditional availability requiring clarification;
- ineligibility with an explanation;
- an alternative managed route;
- R1 selected by the Workplace.

When the user chooses R1, the Product must make clear that MGSN does not assume managed procurement, funds, fulfillment or replacement responsibility. It may still support expected Evidence, reminders, manual Return fields and later resumption of Workplace continuity.

## Audit and non-repudiation

The decision chain should preserve:

- the authorized actor;
- timestamp;
- route, need and offer versions;
- explanation shown;
- selected disposition;
- overrides or exceptions;
- allocation decision;
- provider response;
- renewed confirmations.

This record resolves later questions about what was recommended, authorized, allocated and accepted.

## Part IV conclusion

CH16–CH20 have converted a customer need into a controlled route without transferring customer ownership or creating automatic appointment:

```text
Capability Need Projection
→ route classification
→ eligibility and conflict gates
→ Candidate Route Set
→ explainable Recommendation
→ User Disposition
→ Provider Allocation
→ Provider Acceptance
```

Part V begins only after sufficient commitment exists to create a Managed Network Engagement and govern funds, fulfillment, incidents and typed Return.