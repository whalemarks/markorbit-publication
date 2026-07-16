# B07-PLN-0009 — Network Topology and Private-Space Boundary

## Status

```text
Owner Direction Incorporated
Ready for Owner Acceptance on Merge
```

## Purpose

This record fixes the MGSN network topology and clarifies the meaning of participant private space.

## Canonical Topology Candidate

```text
Demand-side Workplace / Lite
            ↓
          MGSN
            ↑
Provider Workplace / Provider Interface
```

Every demand-side participant connects to MGSN.

Every service provider connects to MGSN.

MGSN does not create or endorse an independent peer-to-peer network among demand users and service providers.

The platform remains the network hub, service interface, procurement controller, funds controller and fulfillment coordinator.

## Hub-and-Spoke Principle

```text
Demand User A ─┐
Demand User B ─┼→ MGSN ←┬─ Provider X
Demand User C ─┘         ├─ Provider Y
                          └─ Provider Z
```

Not:

```text
Demand User A ↔ Provider X
Demand User B ↔ Provider Y
Provider X ↔ Provider Y
User A ↔ User B
```

Any permitted direct Communication is a controlled interaction inside an MGSN-governed collaboration, not creation of an independent network relationship.

## Demand-Side Private Space

`Private` refers to the participant's own operating space:

```text
Organization Workplace
or
MarkOrbit Lite personal / small-team space
```

It may contain:

- customers;
- customer contacts;
- leads and Opportunities;
- internal relationships;
- internal pricing and sales strategy;
- Documents and working materials;
- private Knowledge and memory;
- preferences;
- internal approvals;
- service history;
- MGSN requests and returned results;
- External Route projections and uploaded Evidence.

Private space does not mean:

- a user-owned MGSN provider pool;
- a user-owned global agent network;
- unrestricted provider contacts;
- direct provider export;
- user-controlled routing infrastructure;
- hidden peer-to-peer marketplace;
- ownership of platform procurement terms, Trust or network data.

## Provider Private Space

A provider may operate through its own Workplace or controlled provider interface.

Provider-private information may include:

- team and workload;
- methods;
- internal cost structure;
- Documents and professional work;
- operating notes;
- internal approvals;
- Evidence not approved for network display.

The provider connects only permitted projections to MGSN.

The provider does not gain direct access to demand-side private spaces.

## MGSN Exchange Model

```text
Demand-side authorized projection
→ MGSN service and commercial context
→ provider-side permitted projection
→ provider response and delivery
→ MGSN validation, funds and fulfillment controls
→ demand-side Return
```

MGSN determines, under accepted policy and service model:

- required information;
- disclosure stage;
- permitted recipient;
- Communication mode;
- funds movement;
- milestone Evidence;
- replacement;
- Return scope.

## Relationship Model

The stable managed-network relationship graph is:

```text
Demand-side participant ↔ MGSN
Provider participant ↔ MGSN
```

Not:

```text
Demand-side participant ↔ Provider participant
```

A provider may perform work for a demand-side user's customer, but the MGSN network relationship remains mediated and governed by the platform.

Named professional interaction may be enabled for service quality, conflict checking or professional responsibility. It does not create unrestricted independent connectivity.

## External Self-Managed Route

A user may separately maintain an external provider relationship outside MGSN.

```text
Demand-side private space
→ external provider outside MGSN
→ user-managed Communication, payment and follow-up
→ manual Evidence upload
→ source-qualified Product continuity
```

This external relationship is not part of the MGSN network graph.

MGSN does not guarantee its price, funds, delivery, replacement or status.

## Why the Hub Must Remain Controlled

The hub protects:

- procurement leverage;
- service consistency;
- provider quality;
- customer confidentiality;
- funds and settlement safety;
- milestone Evidence;
- audit and reconciliation;
- replacement;
- non-circumvention;
- interface stability;
- accumulated platform capability;
- long-term economics.

## User Autonomy Under Hub Control

Candidate user authorities include:

- customer ownership and management;
- customer objective;
- route decision;
- approval of data projection into MGSN;
- customer-facing pricing where permitted;
- acceptance or rejection of platform offer;
- final confirmation of Recommended Best Route;
- preferred-provider request;
- required professional or commercial approval;
- outcome review;
- correction and dispute request.

The user does not control:

- MGSN provider pool;
- provider admission;
- platform procurement terms;
- matching and routing infrastructure;
- funds-release rules;
- provider settlement;
- platform Trust records;
- provider suspension;
- interface contracts.

## Orbit Reconciliation

```text
Each participant operates in its own private space.
Each participant connects to MGSN through controlled projections.
MGSN coordinates the managed network interaction.
Participants do not merge Workplaces or form an uncontrolled lateral network.
```

The phrase `MGSN connects independent Workplaces` means:

> MGSN is the controlled platform hub through which independent Workplaces access global capability.

It does not mean direct Workplace-to-Workplace networking.

## Charter Lock Candidate

```text
All managed demand-side and provider-side participants connect to MGSN.

MGSN does not support an independent peer-to-peer network.

Private space means each participant's own operating boundary.

MGSN resources, provider supply, procurement, matching,
routing, funds, fulfillment and network Evidence remain platform-governed.

External self-managed relationships remain outside MGSN
and return only through bounded manual projections.
```

## Gate

Owner merge may accept this topology and private-space direction as part of Pre-Writing Audit v0.1.

It does not authorize Product Charter acceptance, schema, APIs, network implementation or production deployment.