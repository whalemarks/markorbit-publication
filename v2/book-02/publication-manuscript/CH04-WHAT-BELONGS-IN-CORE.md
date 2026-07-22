# CH04 — What Belongs in Core

## Core admission is a discipline, not a naming exercise

A platform that grows quickly creates new nouns every day.

Products introduce routes, requests, listings, campaigns, review types, provider packages, content objects, simulations, credentials and transaction states. Many are useful. Few deserve permanent Core status.

The admission question is not:

> Is this concept important?

The correct question is:

> Must independent Products or platform layers share one stable meaning for this concept in order to interoperate safely over time?

## The five-question test

Every proposed Core concept should be tested against five questions.

1. Does the accepted Core baseline already define the same meaning?
2. Can existing objects, references, evidence and states express it by composition?
3. Is it mainly a profile, role, view or Product-local specialization?
4. Do multiple independent Products need to exchange it using one stable contract?
5. Would adding it change existing lifecycle, authority, ownership or compatibility obligations?

The result belongs to one of five classes.

```text
F0 — already covered
F1 — composition
F2 — explanatory profile
F3 — candidate shared addition
F4 — formal Change Proposal
```

## F0 — already covered

A new label may describe an existing Core meaning more clearly without creating a new object.

For example, a Product may call an Opportunity a `Transaction Opportunity`. If the underlying meaning remains a possible value route and the additional fields are transaction-local, the Product should specialize Opportunity rather than create another universal root.

## F1 — composition

Some concepts are combinations of existing references.

A Contracting Party can often be represented as an Organization playing a declared role in an Order, Contract or Engagement. A Payment Receiver may be an Organization role plus a payment reference. A Capability Evidence record may be Evidence with Capability, Assessment and actor context.

Composition avoids duplicate lifecycles and competing identities.

## F2 — explanatory profile

A profile deserves documentation because several systems may use the pattern, but it does not require a new universal business object.

Examples include:

- business-sovereignty profile;
- demand, capability or asset projection;
- Provider Organization profile;
- Simulation Workplace mode;
- jurisdiction-specific Instruction Package;
- risk or collaboration-mode vocabulary before activation.

Profiles preserve shared understanding while allowing Product-local implementation.

## F3 — candidate shared addition

A candidate addition appears durable, cross-product and semantically distinct.

The current Book 02 reconciliation identifies several strong candidates, including:

```text
Need
Engagement
Work Package
Assignment
Contribution
Outcome
Professional Authority
Relationship Owner
Delivery Owner
Capability Certification
Production Authorization
Resale Authorization
```

Even strong candidates remain provisional. Their appearance in multiple books is evidence for a formal review, not a shortcut around it.

## F4 — formal Core Change Proposal

A concept requires an F4 process when it changes frozen meaning, introduces a new authoritative lifecycle, changes ownership or validation, or imposes downstream migration.

The minimum path is:

```text
frozen-baseline mapping
→ lifecycle and authority analysis
→ cross-book impact analysis
→ Change Proposal
→ conformance fixtures
→ implementation migration plan
→ Owner approval
```

Publication prose cannot substitute for this process.

## Cross-product use is necessary but not sufficient

A concept can appear in many Products and still not belong in Core.

A pricing rule may be reused across Lite and MarkReg. A recommendation score may appear in several interfaces. A provider procurement checklist may support multiple services. Those patterns may deserve shared libraries or Product contracts, but their volatility makes them poor universal semantics.

Core admission requires both reuse and long-term semantic stability.

## Authority and lifecycle must be clear

A candidate object should not enter Core until it can answer:

- who creates it;
- who may mutate it;
- which states are authoritative;
- how it is versioned;
- what evidence supports transitions;
- how it is corrected;
- how it is deprecated;
- which downstream systems must migrate.

A noun without authority and lifecycle is not a Core object. It is an architectural wish.

## Example: Work Package

Work Package is a strong candidate because MarkReg production, Lite paid contribution and Book 03 Execution all need a bounded unit with objective, inputs, output, authority, deadline, review and acceptance criteria.

However, activating it changes how existing Task, Workflow, Assignment and Order contracts interact. The platform must prove that Work Package is not merely a Product-local wrapper and must define compatibility with existing implementations.

Until then:

```text
Work Package in publication architecture
≠ activated public Core contract
```

## Example: Knowledge Claim

Knowledge systems need Source, Document, Claim, Version, Citation and Review State semantics. Core may need stable references so Products can cite and exchange Knowledge Objects.

Core should not become the Knowledge store, ingestion pipeline, Markdown vault or claim-review operation.

```text
shared Knowledge reference
≠ Core ownership of Knowledge content
```

Book 06 and the Knowledge Refinery can evolve their internal structures while honoring the shared reference and provenance contract.

## Example: trademark marketplace records

Trademark Inventory, Listing, Buyer Inquiry and Candidate Route Set are important to Lite. Their lifecycle is shaped by authorization, visibility, pricing and marketplace policy.

They should remain Lite or commerce-local unless another independent Product needs the same stable contracts and the semantics have matured.

They can reference shared Trademark, Organization, Opportunity, Projection, Evidence and authority concepts without entering Core themselves.

## The cost of expanding Core

Every new Core contract creates:

- documentation obligations;
- conformance tests;
- public API commitments;
- downstream implementation work;
- migration responsibility;
- compatibility debt;
- governance cost.

Core expansion is justified only when the cost of semantic divergence is greater.

## Constitutional rule

```text
Product desire alone is not sufficient reason to alter Core.
```

Core should contain the smallest durable set of meanings that allows the wider MarkOrbit system to evolve independently without losing interoperability, authority or trust.
