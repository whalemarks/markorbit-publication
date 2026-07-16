# B07-PLN-0006 — Owner Decisions and Open Questions

## Status

```text
Owner Direction Incorporated
Open for Remaining Charter Decisions
```

## Purpose

This record separates owner-confirmed pre-writing direction from questions that remain open for the Network and Product Charter Candidate.

Owner confirmation at this stage accepts planning direction only. It does not accept a final Product Charter, controlled baseline, schema, API or implementation.

## A. Owner-Confirmed Pre-Writing Direction

### OD-01 — MGSN ownership

```text
MGSN resources, provider supply,
procurement capability, routing interfaces,
funds controls and network operating data
are platform-owned or platform-governed resources.
```

Users gain access to global capability through MGSN. Access does not transfer ownership of the underlying supply network.

### OD-02 — Central hub topology

```text
Demand-side Workplace / Lite
            ↓
          MGSN
            ↑
Provider Workplace / Provider Interface
```

All MGSN participants connect to the platform hub.

MGSN does not create an independent participant-to-participant network.

### OD-03 — Meaning of private space

`Private` means the independent Workplace, Lite or provider-side space controlled by each participant.

Demand-side private space includes:

- customers;
- contacts;
- internal relationships;
- pricing;
- Documents;
- Knowledge;
- preferences;
- approvals;
- business history.

Provider private space includes internal staff, operations, methods, workload and professional records.

Private space does not mean a user-owned MGSN provider subnetwork.

### OD-04 — External self-managed route remains permitted

A user may continue using an external provider without importing it into Lite, Workplace or MGSN.

```text
External Self-Managed Route
→ user manages provider, price, payment and follow-up
→ platform visibility is limited
→ user uploads documents and status manually
→ Product continuity resumes from source-qualified evidence
```

MGSN procurement, funds protection, replacement and fulfillment guarantees do not apply.

### OD-05 — Platform matching is the default when no external route exists

When the user lacks a suitable external route, the normal experience is:

```text
Service Need
→ MGSN eligibility and supply evaluation
→ platform Recommended Best Route
→ user confirms, rejects or adjusts
→ platform allocation
→ provider acceptance
```

The platform may automatically match and preselect the recommended route.

The user retains the final route decision unless a future accepted managed-service mandate expressly authorizes standing allocation.

### OD-06 — User-preferred provider inside MGSN

A user may state a provider preference.

If that provider is admitted to or evaluated for MGSN, the preferred route remains subject to:

- qualification;
- capability scope;
- conflict;
- availability;
- procurement terms;
- service package;
- funds and fulfillment rules;
- platform suspension and risk controls.

Preference does not compel platform admission or appointment.

### OD-07 — Same provider may appear under different routes

The same provider may be:

- used outside MGSN as an External Self-Managed Route; or
- used through MGSN as a managed preferred-provider route.

The two routes have different procurement, payment, responsibility, evidence, status and guarantee consequences.

### OD-08 — Platform price advantage is strategic

MGSN intends to use aggregated demand and unified procurement to obtain stronger pricing and service terms than fragmented one-off buying.

This is a strategic target and value proposition. It is not yet accepted as a universal price guarantee for every service or jurisdiction.

## B. Remaining Product and Architecture Questions

### OQ-01 — MGSN legal and commercial role

For each service model, determine whether the platform acts as:

- principal;
- reseller;
- disclosed agent;
- managed-service provider;
- marketplace operator;
- payment coordinator;
- another legally reviewed role.

### OQ-02 — Provider as role or record

Determine whether `Provider` is:

- an Organization role in a service context;
- an MGSN-owned profile;
- a Core object;
- a Product projection;
- a combination under explicit ownership rules.

### OQ-03 — Formal collaboration ownership

Determine which service owns:

- allocation;
- instruction;
- Provider Acceptance;
- collaboration status;
- milestone;
- replacement;
- closure.

MGSN must not silently duplicate Order, Matter, Task, Workflow or Execution authority.

### OQ-04 — Standing allocation mandate

Determine whether selected service packages may allow:

```text
user accepts managed-service mandate
→ platform allocates eligible provider
→ no separate provider-choice confirmation per transaction
```

This must remain distinct from ordinary automatic matching.

## C. Matching and User Experience Questions

### OQ-05 — Number of user-visible options

Decide whether the user receives:

- one Recommended Best Route;
- one recommendation plus alternatives;
- several ranked platform options;
- only a service package with provider hidden;
- different models by service category.

### OQ-06 — Provider identity visibility

Define when the user sees:

- provider Organization;
- responsible professional;
- qualification;
- evidence;
- contact information;
- availability;
- cost or procurement information;
- incidents or restrictions.

### OQ-07 — Matching explanation

Determine which matching dimensions must be explained without disclosing confidential procurement logic or enabling platform bypass.

### OQ-08 — User-requested rematch

Define:

- valid rematch reasons;
- alternative limits;
- urgency impact;
- price changes;
- when platform policy may refuse an alternative.

### OQ-09 — No-candidate and fallback

Decide when MGSN may:

- return no eligible route;
- recruit new supply;
- offer operator-assisted sourcing;
- use an official connector;
- suggest the user use an external self-managed route.

## D. External Route Questions

### OQ-10 — External route projection

Define the minimum route projection required in MarkReg, Lite or Workplace.

Candidate information includes:

- route type;
- provider identity if disclosed;
- expected milestones;
- user responsibility;
- last known status;
- status source;
- required manual evidence;
- next reminder.

### OQ-11 — Provider identity withholding

Decide whether the user may keep an external provider completely undisclosed while still using Product reminders and manual uploads.

### OQ-12 — Continuity evidence minimum

Determine which evidence is required before the Product may represent:

- submitted;
- officially acknowledged;
- registered;
- refused;
- completed;
- paid;
- closed.

### OQ-13 — Conflict between manual and official evidence

Define reconciliation when:

- user report conflicts with Document;
- provider email conflicts with official source;
- uploaded certificate belongs to another Matter;
- external status becomes stale.

### OQ-14 — External route conversion into MGSN

Determine whether and when an active external route may switch to MGSN-managed fulfillment, including responsibility, price, payment, Document and milestone reset.

## E. Procurement and Commercial Questions

### OQ-15 — Primary commercial model

Choose the initial priority among:

- platform wholesale network;
- managed service package;
- reseller model;
- subscription plus managed transactions;
- hybrid by service category.

### OQ-16 — Customer-facing pricing authority

Determine whether the user may:

- freely set resale price;
- set within a corridor;
- use platform fixed packages;
- use recommended price;
- vary by Product edition or service.

### OQ-17 — Procurement transparency

Define visibility for:

- end customer;
- demand-side user;
- provider;
- operator;
- finance;
- audit.

### OQ-18 — Routing neutrality

Define how price, margin, preferred-provider status, performance, quality, capacity and strategic supply allocation influence matching.

Commercial benefit must not silently override professional eligibility or customer interest.

### OQ-19 — Non-circumvention

Determine:

- contact disclosure stages;
- prohibited bypass behavior;
- consequences;
- loss of platform guarantees;
- enforceability;
- treatment after collaboration completion.

## F. Funds and Financial-Risk Questions

### OQ-20 — Funds holder

Determine which legal entity or regulated partner receives and holds funds.

### OQ-21 — Release model

Choose among:

- milestone release;
- official-fee release plus completion release;
- post-completion release;
- provider credit;
- service-specific rules.

### OQ-22 — Refund and replacement authority

Determine who decides:

- refund;
- partial refund;
- replacement;
- platform compensation;
- provider deduction;
- dispute escalation.

### OQ-23 — Official-fee protection

Define controls for:

- official-fee separation;
- currency movement;
- unused balances;
- evidence;
- refund;
- reconciliation.

## G. Provider Governance Questions

### OQ-24 — Provider admission modes

Consider:

- platform recruitment;
- invitation;
- verified application;
- user suggestion followed by platform review;
- strategic provider program.

### OQ-25 — Verification depth

Define levels and expiry for identity, qualification, capability, office, references and outcomes.

### OQ-26 — Performance and Trust visibility

Determine which information is:

- platform-private;
- provider-visible;
- demand-user-visible;
- aggregate;
- public, if any.

### OQ-27 — Correction, suspension and retirement

Define provider notice, response, appeal, emergency suspension, active-service handling, reinstatement and historical retention.

## H. MVP and Publication Questions

### OQ-28 — Initial service scope

Choose among:

- international trademark filing;
- filing and registration;
- selected high-volume lifecycle services;
- all trademark lifecycle services;
- broader brand services.

### OQ-29 — Initial demand-side user

Candidate priority:

- Chinese trademark agency international department;
- small agency;
- independent professional;
- MarkReg user;
- operator-assisted internal model.

### OQ-30 — Initial provider cohort

Candidate supply:

- existing foreign associates;
- strategic high-volume providers;
- verified law firms;
- filing providers;
- regional master providers.

### OQ-31 — Operator-assisted versus self-service

Determine which matching, procurement, funds and exception activities remain operator-assisted in MVP 0.

### OQ-32 — Reference journeys

At minimum include:

- routine filing with platform recommendation;
- user-preferred MGSN provider;
- external self-managed filing and manual status upload;
- urgent opposition or cancellation;
- provider conflict or unavailability;
- official-fee advance;
- non-performance and replacement;
- provider application and verification;
- dispute and correction;
- suspension or withdrawal.

### OQ-33 — Book title and subtitle

Current title:

```text
Mark Global Service Network
```

Candidate subtitle:

```text
Platform-Governed Global Capability,
Procurement and Trusted Fulfillment
```

## Recommended Minimum Before Charter Acceptance

Before accepting a Charter Candidate, constrain at minimum:

```text
OQ-01 legal/commercial role
OQ-02 Provider ownership model
OQ-03 collaboration ownership
OQ-04 standing allocation mandate
OQ-05 option presentation
OQ-10 external route projection
OQ-15 commercial model
OQ-20 funds holder
OQ-21 release model
OQ-28 initial service scope
OQ-29 initial user
OQ-30 provider cohort
OQ-31 operator assistance
```

## Gate

Owner acceptance of Pre-Writing Audit v0.1 accepts OD-01–OD-08 as planning direction and authorizes preparation of the Network and Product Charter Candidate.

It does not resolve OQ-01–OQ-33 or authorize implementation, payment custody, provider appointment, Product Baseline, Chapter Map or manuscript drafting.