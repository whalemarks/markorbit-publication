# CH11 — Candidate Route Sets Need Bounded Alternatives

A provider directory gives the user names.

A managed network must give the user a decision structure.

That difference is the purpose of the Candidate Route Set.

```text
Provider List
≠ Candidate Route Set

Candidate Route Set
≠ Recommendation

Candidate Route
≠ Provider Appointment
```

Once MGSN has formed the Need and evaluated current Eligibility, it should produce a small set of routes that are safe enough to consider, materially different enough to compare and clear enough to support an accountable choice.

## 1. Why more choice can reduce control

An open directory appears empowering because it offers many providers.

In practice, the user may not know:

- which Provider is currently qualified;
- whether the Provider has a conflict;
- which package version applies;
- whether prices include the same work;
- whether the Provider can meet the deadline;
- whether customer identity has been disclosed;
- whether the route is managed or self-managed;
- what Evidence will be returned;
- what happens if the Provider fails.

A long list transfers unresolved network work back to the user.

```text
visible choice volume
≠ meaningful choice
```

MGSN should reduce the eligible supply portfolio into a bounded, explainable set of alternatives.

## 2. The Candidate Route is more than a Provider

A Candidate Route should represent the complete proposed path, not merely the name of a Provider.

It may include:

- Provider Organization;
- Provider Network Profile reference;
- responsible professional requirements;
- Capability;
- Service Package version;
- route type;
- relationship context;
- professional and network qualification state;
- current Eligibility result;
- price structure;
- timing assumptions;
- data and conflict conditions;
- Provider Acceptance requirement;
- required Evidence and Return;
- recovery and replacement conditions;
- known risks and Unknowns.

The same Provider may appear through more than one route if the package, delivery model or responsibility structure is materially different.

```text
same Provider
+ different package or responsibility chain
= different route
```

Conversely, several Providers should not appear as separate alternatives when their service, price, timing and risk are effectively identical and the distinction adds no decision value.

## 3. A bounded set should be small

The default Candidate Route Set should be intentionally limited.

A useful pattern is:

```text
one Recommended Route
+ up to two materially differentiated alternatives where useful
```

There may be fewer routes when:

- only one route is eligible;
- alternatives would not be meaningfully different;
- disclosure is restricted;
- the deadline is urgent;
- the customer requires an existing Provider;
- all other supply is unavailable or unsafe.

There may be no route where the network cannot support the Need safely.

The number is not an inflexible mathematical rule. The principle is that every displayed alternative must help the user make a real choice.

## 4. Material differentiation

An alternative is meaningful when it changes an important trade-off.

Possible dimensions include:

- relationship continuity;
- price structure;
- turnaround;
- professional specialization;
- language;
- urgency capacity;
- evidence quality;
- communication model;
- direct versus managed route;
- risk and review requirements;
- data location;
- replacement depth;
- scope or package inclusion.

Examples:

```text
Route A — lower cost, standard timing, ordinary filing scope
Route B — higher cost, urgent capacity, stronger deadline commitment
Route C — existing Provider relationship, familiar communication, narrower evidence standard
```

The alternatives should not be artificial variations created to make the Recommendation appear balanced.

## 5. The three delivery-route families

MGSN recognizes three broad delivery routes.

### R1 — External Self-managed Route

The Originating Workplace uses an external Provider outside the managed MGSN route.

The Workplace remains responsible for:

- provider choice;
- negotiation;
- instruction;
- payment;
- deadline follow-up;
- evidence collection;
- correction and recovery.

MGSN may retain limited source-qualified visibility where permitted, but it does not imply the same management, replacement or evidence guarantees as R2 or R3.

### R2 — MGSN Recommended Managed Route

MGSN forms the route from admitted supply, applies current Eligibility, provides a Recommendation and manages the governed fulfillment chain after user confirmation and Provider Acceptance.

This is the default managed route.

### R3 — MGSN Managed Preferred-provider Route

The Originating Workplace identifies an existing Provider relationship, and MGSN attempts to preserve that route within managed controls.

The Provider must still pass:

- admission;
- Capability review;
- qualification;
- conflict;
- availability;
- package;
- price;
- data;
- risk and evidence requirements.

```text
preferred Provider
≠ automatic R3 route
```

These route families should be disclosed because they carry different responsibilities and recovery expectations.

## 6. Route comparability requires normalized structure

Two routes cannot be compared merely by placing headline prices side by side.

The Candidate Route Set should normalize at least:

- included professional work;
- excluded work;
- official fees;
- professional fees;
- taxes;
- disbursements;
- platform-managed layer;
- urgency or contingency items;
- validity period;
- timing assumptions;
- deliverables;
- Evidence;
- expected Return;
- likely later-stage costs.

```text
lower headline price
≠ lower total route cost
```

Where prices cannot yet be normalized, the uncertainty should be explicit.

A route with an estimate may remain a valid alternative, but it should not be displayed as directly equivalent to a fixed offer.

## 7. Relationship context should be visible but bounded

The user should understand when a route is:

- its existing Provider;
- introduced by another participant;
- a new MGSN-recommended Provider;
- affiliated with another participant;
- selected as a specialist or urgent-capacity route;
- being tested under a limited pilot status.

Relationship context can affect confidence, communication and continuity.

It must not conceal:

- current restrictions;
- conflicts;
- materially higher cost;
- weaker evidence;
- related-party incentives;
- a paid ranking arrangement;
- a narrower service scope.

```text
relationship continuity
= legitimate decision factor

relationship ownership
= not created by route display
```

## 8. Commercial influence must not decide Eligibility

MGSN may have commercial relationships with Providers. The network may earn service fees or benefit from standardized procurement.

Those economics must not pull an ineligible route into the candidate set.

The order is:

```text
Qualification and Eligibility gates
→ Candidate Route Set
→ commercial comparison among eligible routes
```

Not:

```text
commercial preference
→ route inclusion
→ justification afterward
```

A Provider should not buy its way into the route set through:

- advertising;
- higher platform payments;
- referral incentives;
- volume commitments;
- preferred placement fees;
- unrelated partnership status.

Where a material commercial relationship could influence Recommendation, the relevant conflict should be governed and disclosed appropriately.

## 9. Diversity without token alternatives

A bounded route set should not use weak alternatives merely to create the appearance of competition.

For example, an alternative is not meaningful when:

- its evidence has expired;
- its package does not cover the Need;
- it cannot meet the deadline;
- it has not completed conflict review;
- the Provider is not available;
- its price is not current;
- the network would not actually allocate it.

```text
ineligible route shown as alternative
= false choice
```

If only one route is eligible, MGSN should say so and explain the dependency risk.

If no route is eligible, the set should be empty.

## 10. Provider identity disclosure within the route set

The route set does not always need to reveal every Provider identity immediately.

Before user disposition, MGSN may show enough information to compare:

- qualification state;
- service fit;
- relationship status;
- package scope;
- timing;
- price;
- evidence and recovery expectations;
- relevant restrictions.

Provider identity may be disclosed where necessary for:

- professional selection;
- conflict review;
- customer approval;
- legal responsibility;
- Provider Acceptance;
- applicable transparency requirements.

The disclosure model should not turn MGSN into an exportable provider directory.

```text
route transparency
≠ unrestricted provider-pool export
```

## 11. Route evidence and provenance

Each route should preserve how it was formed.

Relevant evidence may include:

- Need version;
- eligibility decision;
- Provider and Capability evidence versions;
- package version;
- availability confirmation;
- conflict status;
- quote and validity;
- relationship provenance;
- routing policy version;
- operator or AI assistance;
- known Unknowns;
- reasons for inclusion.

This evidence supports:

- Recommendation explanation;
- later audit;
- dispute review;
- route refresh;
- recovery after failure;
- learning about supply gaps.

The network should be able to explain why a route was in the set and why another route was excluded.

## 12. Route set freshness

The Candidate Route Set is time-bound.

It may become stale when:

- the Need changes;
- the Provider’s availability changes;
- a conflict result arrives;
- the package or price expires;
- the responsible professional changes;
- a Provider is restricted;
- a deadline becomes urgent;
- customer disclosure changes the risk;
- the user delays its decision;
- an official fee changes.

A stale route set should not remain open indefinitely.

Possible responses include:

```text
refresh route set
remove stale route
reconfirm price
recheck availability
request conflict review
return to operator review
```

The system should preserve the prior set rather than silently rewriting the alternatives that the user originally saw.

## 13. User dispositions

The Candidate Route Set should support meaningful user responses.

Possible dispositions include:

- confirm the Recommended Route;
- choose an alternative;
- reject all routes;
- request rematch;
- request clarification;
- nominate a preferred Provider;
- choose the external self-managed route;
- postpone;
- narrow or change the Need;
- escalate for professional or commercial review.

```text
route selected by user
≠ Provider accepted
≠ customer approved final action
```

The next stage remains Provider Allocation and Acceptance.

## 14. Candidate set and AI

AI may help:

- compare eligible routes;
- detect material differences;
- normalize package descriptions;
- identify missing comparison fields;
- summarize known risks;
- generate explanation drafts;
- detect stale evidence;
- test whether alternatives are genuinely differentiated.

AI should not:

- include an ineligible Provider;
- hide commercial influence;
- invent a price or availability state;
- treat public popularity as professional suitability;
- disclose restricted Provider or customer data;
- convert the Recommended Route into appointment;
- suppress a relationship-preserved route without a governed reason.

The route set should show which conclusions depend on model assistance and which depend on verified evidence or human review.

## 15. Failure modes

### 15.1 Directory disguised as choice

The user receives twenty Provider names with little package or qualification context.

Correct response: form a bounded set of eligible, materially differentiated routes.

### 15.2 Hidden single route

The platform displays one route as inevitable without explaining whether alternatives existed or why they were excluded.

Correct response: show the selection basis, dependency and available dispositions.

### 15.3 Lowest price dominates

A cheaper route excludes necessary work and evidence, but it appears first.

Correct response: normalize package and cost structure before Recommendation.

### 15.4 Paid placement enters the set

A commercially preferred Provider appears despite weaker service fit.

Correct response: keep Eligibility independent and govern commercial conflicts.

### 15.5 False alternatives

Two ineligible or unavailable routes are shown to make the Recommendation seem neutral.

Correct response: display only routes that the network could genuinely pursue.

### 15.6 Provider pool leaks

A Workplace exports all contact details from the Candidate Route Set and bypasses network controls.

Correct response: apply progressive Provider disclosure and preserve route-scoped communication.

### 15.7 Stale route chosen

The user confirms a route after price and availability expired.

Correct response: refresh affected checks before allocation.

## 16. Product principle

The Candidate Route Set converts qualified supply into governable choice.

```text
current eligible routes
+ normalized package and cost structure
+ material differentiation
+ bounded disclosure
+ explicit route responsibilities
= meaningful alternatives
```

The set should be small enough to understand, complete enough to expose real trade-offs and honest enough to return one route or no route when that is the truth.

The next chapter explains how MGSN moves from alternatives to a Recommendation without turning explanation into manipulation or recommendation into appointment.
