# B07-PLN-0010 — Contextual Participant Roles, Supply Portfolio and Network Growth

## Status

```text
Owner Direction Incorporated
Charter Input — Not Yet a Final Charter Decision
```

## Purpose

This record clarifies three Product principles that were not sufficiently explicit in the Pre-Writing Audit:

1. an Organization may act as both a service demander and a service provider in different service contexts;
2. MGSN should maintain multiple qualified providers for the same jurisdiction and service rather than depend on one exclusive route;
3. demand-side and provider-side participants should be encouraged to introduce their existing counterparties into MGSN because MGSN can materially improve process efficiency, funds safety, fulfillment visibility and management quality.

These principles refine the platform-owned hub model. They do not create peer-to-peer participant networking.

## 1. Participant Identity Is Stable; Network Role Is Contextual

MGSN should not permanently divide Organizations into mutually exclusive categories of `demand side` and `provider side`.

The stable participant is the Organization.

The role depends on the current Capability Need, jurisdiction, service and collaboration context.

```text
Organization Participant
├── Demand Role
│   └── requests a Capability it does not currently provide
└── Supply Role
    └── offers an admitted and verified Capability through MGSN
```

Examples:

- a Chinese trademark agency may provide China filing capability while requesting United States, European Union or opposition capability;
- a United States law firm may provide United States prosecution capability while requesting China, Madrid or regional filing capability;
- a regional filing provider may provide routine filing services while requesting specialist litigation, translation or local legalization support;
- an Organization may act as demand side in one Matter and supply side in another Matter at the same time.

Therefore:

```text
Organization type
≠ permanent network-side identity

Provider
= contextual role supported by an admitted Capability Profile

Demand participant
= contextual role created by a qualified Capability Need
```

A provider-side role must not be represented only by a fixed `organization.type = service_provider` or a mutually exclusive account class.

## 2. Dual-Role Participation Does Not Create Lateral Networking

Even when an Organization plays both roles, all MGSN-managed activity remains hub-mediated.

```text
Organization A
├── submits Capability Need → MGSN
└── submits Capability Supply → MGSN

Organization B
├── submits Capability Need → MGSN
└── submits Capability Supply → MGSN
```

MGSN may match A and B in a specific collaboration, but A and B do not acquire an independent participant-to-participant network edge from that match.

```text
Dual-role participant
≠ unrestricted bilateral network participant

Prior relationship
≠ default platform bypass right

MGSN collaboration
≠ transfer of the platform provider resource or routing interface
```

Permitted professional communication inside a managed collaboration remains purpose-bound, auditable and governed by MGSN or the relevant Owning Service.

## 3. Multiple Providers per Jurisdiction and Service

MGSN should normally avoid depending on one provider for an entire country or service category.

The platform may negotiate and maintain multiple providers for the same service scope to improve:

- pricing leverage;
- availability;
- specialization;
- service continuity;
- geographic or language coverage;
- urgent capacity;
- replacement capability;
- performance comparison;
- resilience against conflict, suspension or provider failure.

An internal supply portfolio may include roles such as:

```text
Primary Route
Alternative Route
Specialist Route
Urgent-Capacity Route
Relationship-Preserved Route
Backup Route
Pilot / Testing Route
Restricted or Suspended Route
```

These are platform supply-management classifications. They are not necessarily user-visible labels and do not create permanent provider rank.

## 4. Recommended Route Plus Bounded Choice

The default Product experience remains platform recommendation, not open browsing.

However, maintaining multiple providers allows MGSN to give the demand-side user meaningful bounded choice.

Candidate experience direction:

```text
Qualified Capability Need
→ MGSN eligible provider portfolio
→ platform Recommended Route
→ selected bounded alternatives where useful
→ user confirms, selects an alternative,
  requests rematch or chooses external route
→ platform validates final route
→ provider allocation and acceptance
```

Potential user-facing option patterns include:

- one Recommended Route plus one or two alternatives;
- a lower-cost option, a faster option and a specialist option;
- a platform-recommended option plus the user's admitted preferred provider;
- one managed service package where provider identity remains controlled;
- different option depth for routine, specialist, urgent and high-risk services.

The exact number and disclosure depth remain Charter decisions.

The following remain prohibited:

```text
Multiple providers
≠ open bidding hall

User choice
≠ unrestricted access to the full provider pool

Alternative display
≠ disclosure of confidential provider procurement cost

Price comparison
≠ lowest-price-only allocation
```

Eligibility, professional fit, conflict, availability and risk must be applied before price or margin optimization.

## 5. Bidirectional Participant Introduction

MGSN should support two controlled introduction directions.

### 5.1 Demand participant introduces an existing provider

```text
Demand Organization has an external provider
→ invites or suggests the provider to MGSN
→ platform performs identity, capability,
  qualification, commercial and risk review
→ provider independently joins MGSN
→ existing relationship may be represented
  as relationship provenance or preference
→ future work may use MGSN-managed route
```

This allows the demand Organization to retain a familiar provider while gaining:

- standardized instructions;
- document and status continuity;
- platform procurement where available;
- funds protection;
- milestone control;
- settlement and reconciliation;
- exception and replacement governance;
- unified management with other jurisdictions.

Introduction does not compel platform admission and does not convert the provider into an unrestricted user-owned network resource.

### 5.2 Provider introduces an existing demand participant

```text
Provider has an existing demand-side client or agency relationship
→ invites the Organization to MGSN
→ invited Organization independently joins
  through Workplace, Lite or another accepted interface
→ existing relationship provenance is recorded
→ MGSN-managed requests use platform interfaces,
  commercial controls, funds and fulfillment rules
```

The provider receives potential benefits including:

- lower order-management cost;
- standardized intake;
- better instruction quality;
- reliable funds and settlement;
- fewer missing documents;
- structured status reporting;
- reduced reconciliation workload;
- access to additional qualified demand where permitted.

The demand Organization receives global capability beyond the introducing provider's own coverage.

## 6. Introduction Is Not Automatic Admission or Relationship Transfer

Every introduced participant connects independently to MGSN.

```text
Introduction
≠ automatic admission
≠ automatic verification
≠ automatic provider activation
≠ automatic customer conversion
≠ ownership transfer of the pre-existing relationship
```

MGSN owns and governs the network participation, platform profile, routing eligibility, managed commercial terms, funds process and fulfillment state.

The introducing Organization retains its private-space relationship history and customer or provider context, subject to applicable rights and agreements.

A managed MGSN route creates a platform-governed service relationship for that transaction. It does not erase the historical relationship, but it also does not permit participants to bypass platform controls for MGSN-managed work.

## 7. Relationship Provenance and Protection

The Charter should consider a controlled `Relationship Provenance` concept containing, at minimum:

- introducing Organization;
- invited Organization;
- introduction direction;
- pre-existing relationship declaration;
- relationship start or evidence date where available;
- service or jurisdiction scope;
- external-route or MGSN-route history;
- current preference status;
- disclosure restrictions;
- attribution and incentive status;
- dispute or correction status.

Relationship provenance may support:

- preferred-provider routing;
- preservation of a familiar cooperation route;
- invitation incentives;
- attribution and anti-poaching controls;
- explanation of why a provider is shown;
- continuity when migrating an external route into MGSN.

It must not become:

- unrestricted ownership of another participant;
- a permanent routing monopoly;
- a mechanism that blocks a better eligible route where customer interest or risk requires an alternative;
- a substitute for provider admission, conflict, availability or performance review.

## 8. Network Growth Flywheel

Bidirectional introduction creates a managed network growth loop:

```text
More demand participants
→ more aggregated demand
→ stronger procurement and package standardization
→ better provider economics and more quality providers
→ broader coverage, lower cost and stronger fulfillment
→ more attractive demand-side participation
```

and:

```text
More provider participants
→ more jurisdiction and specialist coverage
→ better availability and route resilience
→ stronger user results
→ more demand and repeat use
→ more valuable provider participation
```

Existing bilateral relationships can migrate into MGSN-managed operation because MGSN offers management value, not merely discovery.

The desired adoption reason is:

> Participants join because MGSN materially improves service execution, funds safety, status continuity, document control, reconciliation and global capability management.

## 9. Participant Experience Implications

A dual-role Organization should not need two unrelated identities.

Candidate experience:

```text
Organization Space
├── Request Global Services
│   ├── Capability Need
│   ├── Route and Offer
│   ├── Funds and Milestones
│   └── Returned Results
└── Provide Services
    ├── Capability Profile
    ├── Invitations and Availability
    ├── Accepted Work
    ├── Delivery Evidence
    └── Settlement
```

The Product may present different workspaces or modes, but the underlying Organization identity remains stable.

Role separation still requires:

- separate permissions;
- separate demand and supply responsibilities;
- separate payable and receivable accounting;
- conflict and self-dealing controls;
- no automatic offset between funds owed and funds receivable;
- clear audit context for every role transition.

## 10. Candidate Charter Decisions

This record recommends that the Charter Candidate evaluate and likely lock:

```text
OD-09 — Participant roles are contextual, not mutually exclusive.
OD-10 — MGSN maintains multi-provider supply portfolios.
OD-11 — Default recommendation may include bounded alternatives.
OD-12 — Demand and provider participants may introduce counterparties.
OD-13 — Introductions create provenance, not automatic admission or ownership transfer.
OD-14 — All MGSN-managed collaboration remains hub-controlled.
OD-15 — Dual-role financial, permission and conflict contexts remain separated.
```

These numbers are candidate Charter decisions and are not yet accepted Product Charter decisions.

## 11. Questions Requiring Further Discussion

Before Charter acceptance, determine:

1. how many alternatives a demand user normally sees;
2. whether provider identity is shown before route confirmation;
3. whether the user sees price, speed and specialist trade-offs or only packaged outcomes;
4. what commercial incentive applies when a participant introduces supply or demand;
5. whether an introduction creates a protected attribution period;
6. how non-circumvention applies to pre-existing relationships;
7. when an existing bilateral relationship may remain outside MGSN;
8. whether a provider-introduced demand participant may immediately access the full MGSN network;
9. whether a demand-introduced provider may serve other demand participants after platform admission;
10. how dual-role Organizations separate payables, receivables, credit and settlement;
11. how conflicts are handled when one Organization is both purchaser and supplier in related work;
12. whether MGSN may route work back to the same Organization or an affiliated Organization;
13. how relationship provenance affects matching without becoming an unfair permanent preference;
14. what invitation, referral, discount, credit or service incentives are appropriate;
15. how platform procurement advantage is preserved when participants already know each other.

## 12. Gate

This record is a controlled input to the Book 07 Network and Product Charter Candidate.

It does not accept:

- a final Product Charter;
- a canonical Provider object;
- a database schema;
- a public provider directory;
- an open bidding mechanism;
- automatic participant admission;
- automatic provider appointment;
- participant-to-participant network ownership;
- payment or settlement implementation;
- production routing.
