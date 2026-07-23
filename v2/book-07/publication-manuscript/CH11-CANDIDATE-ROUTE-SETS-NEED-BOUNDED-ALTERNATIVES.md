# CH11 — Candidate Route Sets Need Bounded Alternatives

A Provider directory gives the user names.

A managed network must give the user a decision structure.

That structure is the Candidate Route Set.

```text
Provider List
≠ Candidate Route Set

Candidate Route Set
≠ Recommendation

Candidate Route
≠ Provider Appointment
```

Once MGSN has formed the Need and evaluated current Eligibility, it should produce a small set of routes that are safe enough to consider, materially different enough to compare and clear enough to support an accountable choice.

## 1. More visible choice can reduce control

A long list appears empowering, but it transfers unresolved network work back to the least informed participant.

The user may not know which Provider is qualified, conflicted, available or operating under a current Package. It may not know whether prices cover the same scope, whether the route is managed or self-managed, what Evidence will return or how the Matter can recover after failure.

```text
Visible Choice Volume
≠ meaningful choice
```

MGSN should therefore reduce eligible supply into a bounded set rather than expose the Provider pool.

## 2. A Candidate Route is more than a Provider name

A Candidate Route represents a complete proposed path.

It connects:

- Provider Organization and relevant Capability;
- Service Package and route family;
- current Eligibility and conditions;
- relationship context;
- price and timing assumptions;
- conflict, data and authority prerequisites;
- expected Evidence and Return;
- Provider Acceptance requirement;
- recovery and replacement expectations;
- known risks and Unknowns.

The same Provider can appear through different routes where the Package, management layer or responsibility structure is materially different. Several Providers should not be displayed as distinct alternatives when the practical trade-off is negligible.

## 3. The set should be intentionally small

A useful default is:

```text
one Recommended Route
+ up to two materially differentiated alternatives where useful
```

There may be one route where supply is scarce, the deadline is urgent or the customer requires a particular Provider. There may be no route where the Network cannot support the Need safely.

The number is not a rigid rule. Every displayed alternative must help the user make a real decision.

## 4. Alternatives must differ materially

Meaningful differences may concern:

- relationship continuity;
- scope and Package inclusions;
- price structure;
- timing or urgent capacity;
- professional specialization;
- language and communication model;
- Evidence quality;
- data handling;
- review requirements;
- recovery depth.

For example:

```text
Route A
lower cost, ordinary timing, standard filing scope

Route B
higher cost, confirmed urgent capacity, stronger deadline support

Route C
existing Provider relationship, familiar communication, narrower managed layer
```

Alternatives should not be artificial variations created to make the Recommendation appear neutral.

## 5. Three route families

### R1 — External self-managed route

The Originating Workplace uses an external Provider and remains responsible for selection, negotiation, instruction, payment, monitoring, Evidence and recovery.

MGSN should not imply the same procurement, fulfillment or replacement protection as a managed route.

### R2 — MGSN recommended managed route

MGSN forms the route from admitted supply, applies current Eligibility, recommends a route and manages the governed fulfillment chain after user disposition and Provider Acceptance.

### R3 — MGSN managed preferred-provider route

The Workplace nominates an existing Provider relationship. MGSN preserves the preference only when the Provider passes current admission, qualification, conflict, availability, Package, data and risk requirements.

```text
Preferred Provider
≠ automatic R3 route
```

The route family should be visible because responsibility and recovery differ.

## 6. Comparability requires normalization

Two routes cannot be compared through headline price alone.

The Candidate Route Set should normalize the material differences in:

- included and excluded professional work;
- official fees, taxes and disbursements;
- platform-managed service layer;
- urgency and contingent items;
- timing assumptions;
- deliverables;
- Evidence and Return;
- likely later-stage costs;
- validity period.

```text
Lower Headline Price
≠ lower total route cost
```

Where prices or timing remain estimated, the uncertainty should be explicit rather than presented as direct equivalence.

## 7. Relationship context is relevant but bounded

The user should know whether a route uses its existing Provider, a new MGSN Provider, an affiliate, a specialist or a limited pilot route.

That context can affect continuity and confidence. It must not conceal restrictions, related-party incentives, materially higher cost, weaker Evidence or narrower scope.

```text
Relationship Continuity
= legitimate decision factor

Route Display
≠ ownership of the relationship
```

## 8. Commercial influence follows Eligibility

MGSN may earn fees or negotiate Provider terms. Those economics must not decide whether a route enters the Candidate Route Set.

The correct order is:

```text
Qualification and Eligibility gates
→ Candidate Route Set
→ commercial comparison among eligible routes
```

A Provider should not buy entry through advertising, referral payments, volume commitments or preferred-placement fees. Material conflicts that could distort Recommendation should be governed and disclosed appropriately.

## 9. Token alternatives create false choice

An alternative is not meaningful when its Evidence has expired, its Package misses the Need, its Provider is unavailable, conflict review is incomplete or the Network would not actually allocate it.

```text
Ineligible Route Shown as Alternative
= false choice
```

If only one route is eligible, MGSN should say so and explain the dependency. If no route is eligible, the set should remain empty.

## 10. Route transparency is not Provider-pool export

Before user disposition, MGSN may disclose enough to compare qualification, service fit, Package, timing, price, Evidence, relationship status and restrictions.

Provider identity should be disclosed when required for professional selection, conflict review, customer approval, Provider Acceptance or legal responsibility.

```text
Route Transparency
≠ unrestricted Provider-pool export
```

The Network should support accountable choice without becoming a downloadable directory.

## 11. The route set needs provenance and freshness

Each route should preserve the Need version, Eligibility result, Package version, price validity, availability, conflict state, relationship provenance, routing-policy version and known Unknowns.

This supports explanation, audit, refresh, dispute review and recovery.

A route set becomes stale when the Need, deadline, conflict result, availability, price, Package, responsible professional or restriction changes. The prior set should remain visible rather than being silently rewritten.

## 12. User disposition remains a choice, not an appointment

The user may confirm the Recommended Route, choose an alternative, reject all routes, request explanation or rematch, nominate a Preferred Provider, use R1, postpone or change the Need.

```text
Route Selected by User
≠ Provider Accepted
≠ customer approved final action
```

The next stage is Provider Allocation and Acceptance.

## 13. AI can compare but cannot populate the set dishonestly

AI can normalize Package descriptions, identify material differences, detect missing comparison fields and draft route summaries.

It must not include an ineligible Provider, invent price or availability, hide commercial influence, disclose restricted data, convert popularity into professional fit or turn the Recommended Route into appointment.

## 14. Representative failure patterns

### Directory disguised as choice

The user receives twenty names with little route context.

**Recovery:** reduce them to eligible, materially differentiated routes.

### Hidden single route

The platform presents one route as inevitable without explaining excluded alternatives or dependency.

**Recovery:** disclose why only one route remains and allow challenge or external self-management.

### Lowest price dominates

A cheaper route excludes necessary work and Evidence.

**Recovery:** normalize scope and cost layers before Recommendation.

### Paid placement enters the set

A commercially preferred Provider appears despite weaker fit or unresolved conditions.

**Recovery:** remove the route and review the commercial conflict.

### Stale route remains selectable

The user confirms after price or capacity has expired.

**Recovery:** refresh the affected checks before Allocation.

## 15. Product principle

The Candidate Route Set converts eligible supply into governable choice.

```text
Eligible Routes
→ bounded, materially different alternatives
→ Recommendation
→ meaningful user disposition
```

The next chapter explains why the Recommendation must show its reasoning, uncertainty and trade-offs rather than present one route as an unexplained platform answer.