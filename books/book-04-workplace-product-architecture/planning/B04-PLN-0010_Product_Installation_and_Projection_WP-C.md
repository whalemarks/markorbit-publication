# B04-PLN-0010 — Product Installation and Projection WP-C

## Status

```text
Work Package C Candidate
Ready for Owner acceptance on merge
Book 04 RC1 remains immutable
```

## Purpose

Translate the active Canon's Product participation model into a controlled Book 04 vNext amendment without rewriting RC1 in place.

## Controlling distinctions

```text
Product
≠ Product Installation
≠ Product Projection

Projection
≠ Handoff
≠ Return
```

## Definitions

### Product

An independently governed capability and user-journey system with its own product identity and bounded responsibilities.

### Product Installation

A Workplace-scoped relationship recording Product identity, entitlement, configuration, permission, activation state and projection scope.

An Installation does not imply a separate codebase, database, tenant, formal-state authority or ownership of Workplace data.

### Product Projection

A purpose-limited view or interaction surface derived from authorized context. Projection does not transfer ownership or formal-state authority.

### Handoff

A typed transfer of authorized context toward another authority boundary. Handoff sent does not mean destination acceptance.

### Return

A typed outcome, Evidence, Artifact or status projection returned to an originating context. Return received does not mean automatic formal-state mutation.

## Installation control model

A conforming Product Installation must identify:

1. Workplace;
2. Product;
3. entitlement basis;
4. activation state;
5. configuration set;
6. user and role permissions;
7. authorized context scope;
8. projection surfaces;
9. Handoff and Return contracts;
10. audit and revocation rules.

## Chapter allocation

| Chapter | Required correction |
| --- | --- |
| CH20 | Product principles must distinguish Product identity from Workplace participation. |
| CH21 | Shared foundations do not create shared data ownership or automatic authority. |
| CH22 | Replace generic embedding with Installation and Projection semantics. |
| CH26 | Editions become configuration and entitlement patterns, not new authority models. |
| CH27 | Cross-Product continuity must use typed Projection, Handoff and Return. |
| CH30 | Artifact provenance must retain originating Workplace and Product context. |
| CH31 | Render, Edit, Delivery and Publish surfaces are projections unless formalized elsewhere. |
| CH32 | Outcomes and feedback return through typed Return and explicit acceptance. |
| CH38 | Conformance must test Installation identity, projection scope and contract boundaries. |

## Non-goals

WP-C does not:

- define Product-specific schemas or APIs;
- alter Books 05–07 frozen Product semantics;
- authorize implementation;
- create an integrated Book 04 vNext baseline;
- authorize protected action.

## Gate

Owner merge accepts the amendment and correction ledger for WP-C scope and authorizes WP-D Product and network interface correction.
