# CH35 — Core Change Governance and the F0–F4 Admission Gate

## Core changes must be earned

Every Product will eventually discover concepts that feel important enough to become shared platform semantics.

That pressure is natural. It is also the primary way Core becomes unstable.

A useful local noun can appear in several workflows, gain internal popularity and then be promoted into Core before its lifecycle, authority, compatibility and ownership have been understood.

Book 02 therefore requires every proposed shared concept to pass a controlled admission process.

```text
Useful Concept
≠ Core Concept
```

The governing model is:

```text
F0 — Already Covered
F1 — Composition
F2 — Explanatory Profile
F3 — Candidate Shared Addition
F4 — Formal Core Change Proposal Required
```

The classification is not a maturity score. It determines the smallest safe semantic treatment.

## F0 — Already covered

F0 applies when the frozen Core already expresses the same meaning, even if the Product uses a different term.

The correct action is to:

- map the Product term to the existing concept;
- document aliases where useful;
- correct local misuse;
- avoid duplicate identifiers and lifecycles.

```text
Different Label
≠ Different Semantic Object
```

Examples may include a Product-local name for an existing Opportunity, Review or Evidence reference.

## F1 — Composition

F1 applies when existing objects, roles, references, states and Evidence can express the concept together.

The correct action is to define a composition profile rather than create a new root object.

Examples may include:

- Contracting Party as an Organization role within an Order or Engagement;
- Capability Evidence as Evidence with Capability and assessment context;
- Revision Request as a Review disposition;
- Payment Receiver as an Organization role plus payment reference.

```text
Common Composition
≠ New Atomic Object Required
```

Composition preserves reuse while keeping Core smaller.

## F2 — Explanatory profile or controlled specialization

F2 applies when the concept deserves a stable documented profile, role vocabulary or specialization but does not need an independent universal lifecycle.

Examples may include:

- Provider as an Organization profile;
- Contributor as an Assignment or Engagement role;
- Transaction Opportunity as an Opportunity profile;
- Listing as an Asset Projection profile;
- Professional Qualification as a Credential specialization;
- Brain Result types as controlled profiles.

A profile may define:

- required references;
- allowed fields;
- validation rules;
- authority restrictions;
- lifecycle constraints inherited from the parent concept.

```text
Shared Profile
≠ Independent Root Authority
```

## F3 — Candidate shared addition

F3 applies when a concept appears durable, cross-product and semantically distinct enough to justify investigation as a new shared contract.

F3 is not activation.

A Candidate should include:

- problem statement;
- cross-product evidence;
- proposed meaning;
- distinction from existing concepts;
- authority and ownership model;
- lifecycle candidate;
- field-level draft;
- versioning and compatibility impact;
- privacy and rights impact;
- migration implications;
- unresolved alternatives.

```text
F3 Candidate
≠ Active Core Object
```

Current strong candidates include Need, Engagement, Work Package, Assignment, Contribution, Outcome, Professional Authority, Relationship Owner, Delivery Owner, Capability Certification, Production Authorization and Resale Authorization.

## F4 — Formal Core Change Proposal

F4 applies when the proposal would:

- change existing meaning;
- modify identifiers;
- create or change authoritative lifecycle;
- alter formal-state ownership;
- change authority or validation requirements;
- impose migration obligations;
- break consumer compatibility;
- redefine a frozen semantic boundary.

F4 requires a formal Core Change Proposal before adoption.

```text
Better Design
≠ Permission to Replace Frozen Meaning
```

The proposal must be reviewed as a constitutional change, not as an ordinary feature request.

## The five-question classification test

Every term should first be tested against five questions:

1. Does the frozen Core already define the same meaning?
2. Can existing objects and references express it by composition?
3. Is it mainly a profile, role, view or Product-local specialization?
4. Must independent Products exchange it using one stable contract?
5. Would introduction change existing meaning, lifecycle, authority or compatibility?

The answers determine the narrowest appropriate class.

## Admission criteria

A concept should enter Core only when all of the following are substantially true:

- at least two independent Products or platform layers require it;
- those contexts need one stable meaning;
- local implementations would create harmful divergence;
- authority and lifecycle boundaries are clear;
- Product-specific policy can be excluded;
- versioning, compatibility and migration can be governed;
- the benefit exceeds the long-term cost of expansion.

```text
Used in Two Places
≠ Admission Criteria Satisfied
```

The two uses must be independent enough to demonstrate a shared semantic need rather than copied implementation preference.

## Exclusion criteria

A concept should usually remain outside Core when it is mainly:

- UI arrangement;
- recommendation algorithm;
- pricing policy;
- ranking rule;
- course curriculum;
- Product-specific workflow;
- provider procurement package;
- operational checklist;
- model prompt;
- tool binding;
- temporary implementation convenience.

These may be important and reusable. They are simply not constitutional semantics.

## Required Change Proposal contents

A formal proposal should include:

### Problem and evidence

- problem statement;
- affected Products and layers;
- examples of semantic divergence;
- why existing composition is insufficient.

### Proposed contract

- stable identifier;
- definition;
- fields and controlled values;
- authority and ownership;
- lifecycle;
- validation and Evidence;
- Unknown and correction behavior.

### Boundary analysis

- distinction from existing objects;
- Product-local policy excluded;
- interaction with Workplace sovereignty;
- interaction with Execution;
- interaction with Data, Knowledge and Brain;
- formal-state implications.

### Compatibility and migration

- contract version;
- affected consumers;
- mapping from existing records;
- conformance fixtures;
- deprecation plan;
- rollback and correction route.

### Decision and status

- reviewers;
- objections and alternatives;
- approved scope;
- rejected scope;
- effective date;
- implementation and migration authority.

## Publication is not activation

A manuscript can describe a Candidate in depth without making it canonical.

```text
Publication Prose
≠ Semantic Activation
```

Activation requires the approved governance artifact, contract version, conformance updates, migration planning and Owner decision.

This distinction allows strategic and editorial work to proceed without silently changing implementation obligations.

## Code is not activation either

An experimental implementation may exist before the semantic contract is approved.

```text
Prototype Exists
≠ Core Object Active
```

Prototype records should remain Product-local or explicitly experimental. They must not be emitted as canonical shared records or used to force downstream migration.

## Repeated use does not bypass review

A local concept can become common through copying.

```text
Widely Copied
≠ Semantically Correct
```

Repeated use may strengthen the evidence for F3 review, but it may also reveal that several Products copied the same weak abstraction.

The admission process must still test composition, authority, lifecycle and compatibility.

## Candidate registry

Book 02 should maintain a Candidate registry containing:

- candidate identifier;
- proposed name and aliases;
- classification;
- source books and Products;
- owner of the proposal;
- status;
- open questions;
- dependencies;
- decision history;
- next gate.

Useful statuses include:

```text
Observed
Under Mapping
F0 Resolved
F1 Composed
F2 Profiled
F3 Candidate
F4 Proposal Drafted
Approved
Rejected
Deferred
Withdrawn
```

The registry prevents candidates from disappearing into prose or being implemented without a decision trail.

## Decision rights

Core change governance should distinguish:

- proposal author;
- semantic reviewer;
- domain reviewer;
- architecture reviewer;
- privacy or legal reviewer where required;
- downstream consumer reviewer;
- final Owner approval.

```text
Subject-matter Expertise
≠ Final Semantic Authority
```

A domain expert may identify a real need. The final decision must also consider platform-wide compatibility and ownership.

## Objections must be preserved

A rejected alternative may become relevant later.

The proposal should preserve:

- competing models;
- reasons for rejection;
- assumptions;
- conditions that could reopen the decision.

```text
Decision Made
≠ Alternative Erased
```

This reduces repeated debate and helps future reviewers understand the original trade-offs.

## Emergency changes

A security, legal or integrity incident may require urgent restriction.

Emergency governance may:

- suspend a route;
- block a value;
- revoke an authorization;
- require additional Review;
- mark a contract invalidated.

It should not silently introduce a permanent new semantic model.

```text
Emergency Restriction
≠ Permanent Core Redesign
```

A retrospective Change Proposal should document and normalize any lasting change.

## Conformance is part of approval

A shared contract is incomplete until consumers can demonstrate correct interpretation.

Approval should require, where applicable:

- normative contract text;
- controlled examples;
- valid and invalid fixtures;
- authority edge cases;
- lifecycle transitions;
- Unknown and correction cases;
- version compatibility tests.

```text
Definition Approved
≠ Ecosystem Conformant
```

## Migration authority remains separate

Even after a contract is approved, migration may require a separate release decision.

```text
Core Contract Approved
≠ Production Migration Authorized
```

The platform may need staged implementation, supervised pilots, compatibility windows and rollback evidence.

## Constitutional rule

```text
Core expands only through evidence,
classification, boundary analysis,
formal decision, conformance and migration governance.

No Product, manuscript, model, prototype
or repeated local use may activate shared semantics by implication.
```
