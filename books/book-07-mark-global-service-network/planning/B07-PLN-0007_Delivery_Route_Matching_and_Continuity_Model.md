# B07-PLN-0007 — Delivery Route, Matching and Continuity Model

## Status

```text
Draft for Owner Review
```

## Purpose

This record defines the candidate route model through which a demand-side user completes work when an external service provider is required.

It distinguishes:

- platform-managed global capability;
- a user's external self-managed route;
- user preference inside the MGSN supply pool;
- platform visibility and responsibility;
- matching, confirmation and allocation;
- continuity when work occurs outside platform control.

This is a planning model only. It does not create accepted Product records, database states, payment authority, appointment authority or implementation contracts.

## Core Principle

```text
A user may retain an external self-managed route.

MGSN remains the default governed route
when the user needs platform-provided global capability.

Platform matching may preselect the best governed route.

The user retains the final confirmation,
rejection or adjustment decision.
```

## Network Topology

```text
Demand-side Workplace / Lite
            ↓
          MGSN
            ↑
Provider Workplace / Provider Interface
```

Demand-side users and providers do not form an MGSN-owned horizontal connection with each other.

All MGSN-managed discovery, commercial offer, instruction, milestone, funds, delivery and return states pass through platform-controlled interfaces.

A relationship that exists outside MGSN remains outside the MGSN-managed route unless the user deliberately chooses to use the platform route.

## Route R1 — External Self-Managed Route

### Meaning

The user already has an external provider or filing route and chooses to continue using it outside MGSN.

The user is not required to:

- import the provider into Lite;
- register the provider in the Workplace;
- disclose the provider to MGSN;
- use platform procurement;
- use platform funds control;
- use platform Communication or instruction interfaces.

### Platform treatment

The system may record only a bounded route projection such as:

```text
Route type: External Self-Managed
Platform visibility: Limited
Provider identity: Optional / withheld
Commercial terms: External
Funds protection: Not provided by MGSN
Fulfillment guarantee: Not provided by MGSN
Status source: User-supplied evidence
```

### Process black hole

Because the provider works outside MGSN, the platform may not automatically receive:

- instruction acknowledgement;
- provider acceptance;
- payment status;
- filing or service progress;
- official receipt;
- office correspondence;
- registration certificate;
- invoice or official-fee evidence;
- completion or failure state.

This gap is a known process black hole, not a platform error.

### Continuity bridge

The Product should help the user compensate through a manual bridge:

```text
External route selected
→ platform marks visibility as limited
→ user manages provider and payment
→ Product requests expected evidence and dates
→ user uploads documents, receipts and status
→ source and confidence remain visible
→ MarkReg / Workplace resumes from accepted evidence
```

Candidate assistance may include:

- missing-document reminders;
- expected milestone checklist;
- manual status entry;
- upload requests;
- source and confidence labels;
- stale-state warning;
- deadline reminders;
- reconciliation when later evidence conflicts with earlier user input.

The platform must not present user-reported external status as provider-confirmed or official truth.

### Responsibility

The user is responsible for:

- provider selection;
- direct negotiation;
- payment and credit risk;
- instruction accuracy;
- follow-up;
- obtaining and uploading evidence;
- resolving non-performance;
- confirming official results.

MGSN does not provide implied procurement, funds, replacement or fulfillment guarantees for this route.

## Route R2 — MGSN Recommended Managed Route

### Meaning

The user does not have a suitable external route, or chooses to use platform capability.

MGSN evaluates the need and determines the best governed route under the current service model.

### Default matching sequence

```text
Service Need
→ Capability and service typing
→ jurisdiction and eligibility gates
→ platform supply search
→ price, capability, availability,
  risk and performance comparison
→ platform Recommended Best Route
→ default option presented to user
→ user confirms, rejects or requests adjustment
→ platform allocation
→ provider acceptance
→ managed fulfillment
```

### Automatic matching versus automatic appointment

The Product may automatically:

- evaluate eligible platform supply;
- rank suitable routes;
- preselect the recommended route;
- prepare a customer-facing platform offer;
- identify the strongest default option.

The Product must not treat matching as final provider appointment before the required user confirmation or accepted managed-service instruction.

```text
Automatic matching
≠ autonomous appointment

Default recommendation
≠ final user instruction

User confirmation
≠ provider acceptance
```

### Optimization dimensions

The platform recommendation may consider:

- service and jurisdiction fit;
- qualification and evidence;
- conflict status;
- current availability;
- expected response time;
- procurement price;
- total platform service cost;
- official-fee handling;
- delivery quality;
- correction and dispute history;
- funds and settlement risk;
- language and communication;
- data-handling restrictions;
- provider capacity;
- replacement continuity;
- platform strategy and supply balance.

No single dimension, including price, should silently determine the result.

### User authority

The user may:

- accept the recommended platform route;
- reject it;
- state an additional constraint;
- request a different service depth;
- request another platform-qualified option where the service model permits;
- choose an external self-managed route instead;
- cancel before the applicable commitment point.

The user does not receive unrestricted access to the full provider pool, confidential procurement terms or platform routing logic.

### Platform value

The platform expects to create a better offer through:

- aggregated demand;
- repeat procurement;
- negotiated provider terms;
- standardized service scope;
- quality and fulfillment governance;
- payment reliability for providers;
- provider replacement capability;
- lower search and failure cost.

A lower price than fragmented one-off procurement is a strategic hypothesis and target, not a universal promise for every service or jurisdiction.

## Route R3 — MGSN Managed Preferred-Provider Route

### Meaning

The user has a preference for a particular provider, and that provider is already admitted to or can be evaluated by MGSN.

The preference may arise from:

- prior external cooperation;
- language or communication familiarity;
- client request;
- specialized expertise;
- prior successful delivery;
- relationship continuity.

### Candidate sequence

```text
User states provider preference
→ platform resolves provider identity
→ platform checks MGSN admission and scope
→ eligibility, conflict and availability review
→ procurement and service-model review
→ platform compares preferred route
  with Recommended Best Route
→ user receives permitted explanation
→ user confirms permitted route
→ platform allocates and manages service
```

### Preference does not override platform gates

A preferred provider may still be unsuitable because of:

- conflict;
- unavailable capacity;
- expired qualification;
- service mismatch;
- data-handling restriction;
- unacceptable commercial terms;
- suspension;
- unresolved incident;
- inability to meet the deadline;
- service package incompatibility.

```text
User preference
≠ provider eligibility
≠ platform admission
≠ provider appointment
```

### Same provider, different route consequences

A provider may be used in two distinct ways:

```text
Outside MGSN
→ External Self-Managed Route
→ user manages price, funds, instruction and evidence
→ MGSN guarantees do not apply
```

or:

```text
Inside MGSN
→ MGSN Managed Preferred-Provider Route
→ platform procurement and service terms apply
→ platform funds and fulfillment controls apply
→ managed status and evidence return apply
```

The provider identity may be the same, but the route, responsibilities, price basis, guarantees and audit trail are different.

## Route Comparison Matrix

| Dimension | R1 External Self-Managed | R2 MGSN Recommended Managed | R3 MGSN Managed Preferred Provider |
| --- | --- | --- | --- |
| Provider source | user's external route | platform supply pool | user preference resolved within platform supply |
| Provider disclosure to platform | optional or limited | platform-known | platform-known or evaluated |
| Matching | user-managed | platform default optimization | platform validation of user preference |
| Final user decision | direct external decision | confirm / reject / adjust | confirm permitted preferred route or alternative |
| Procurement | user | platform | platform |
| Provider cost visibility | external | controlled | controlled |
| Customer-facing offer | user-managed | platform/Product offer | platform/Product offer |
| Funds control | user/external | platform-managed model | platform-managed model |
| Fulfillment monitoring | manual | platform-managed | platform-managed |
| Provider acceptance | external | platform-recorded | platform-recorded |
| Evidence return | manual upload | structured platform return | structured platform return |
| Replacement support | user responsibility | platform policy | platform policy |
| Platform guarantee | none implied | according to accepted service model | according to accepted service model |
| Process continuity | manual bridge | native continuity | native continuity |
| Platform bypass issue | not applicable because route is declared external | prohibited within managed route | prohibited within managed route |

## Visibility and Status Rules

The Product must distinguish at least:

```text
platform-managed fact
provider-reported fact
user-reported external fact
official-source fact
unknown external state
```

Suggested display principles:

- external routes carry a persistent `External / User Managed` indicator;
- platform-managed routes carry current platform milestone and funds status;
- manually uploaded documents preserve uploader, source, date and confidence;
- unknown status remains unknown;
- no external route is shown as MGSN guaranteed;
- provider identity masking does not hide platform responsibility for a managed route;
- platform recommendation should explain the main fit and constraint dimensions without exposing confidential procurement data.

## Experience Consequence

The primary route-selection experience may present:

```text
Recommended Platform Route
Your Preferred Platform Provider
Use My Own External Route
```

The visual hierarchy should normally emphasize the Recommended Platform Route because it provides the strongest continuity, funds protection, negotiated procurement and fulfillment control.

The external route remains available but displays its operational consequences before confirmation.

## Conformance Locks

```text
External route remains permitted.

External route does not receive
implied MGSN guarantees.

Platform matching may be automatic.

Final user confirmation remains required
unless a separately accepted managed-service mandate
expressly authorizes platform allocation.

User preference does not bypass
eligibility, conflict, availability,
procurement or provider-governance gates.

The same provider outside and inside MGSN
creates two different service routes.

External status must be manually bridged
and source-qualified.

Platform-managed collaboration remains
MGSN-centered and does not create
an unrestricted horizontal network relationship.
```

## Open Decisions for Charter

The Charter Candidate must still constrain:

- whether any managed-service package permits standing user authorization for platform allocation;
- how many alternatives the user sees in each service category;
- whether provider identity is visible before user confirmation;
- how an external route is represented in MarkReg and Workplace;
- the minimum manual evidence required to resume lifecycle continuity;
- whether external provider identity can remain completely undisclosed;
- how platform price advantage is measured and communicated;
- when a user-preferred provider can be onboarded into MGSN;
- whether the preferred provider receives special commercial treatment;
- how non-circumvention applies after a managed collaboration;
- which failures trigger automatic replacement versus user approval.

## Gate

Owner acceptance of this planning record may authorize its use in the Book 07 Network and Product Charter Candidate.

It does not authorize implementation, provider appointment, payment custody, production routing or manuscript drafting.