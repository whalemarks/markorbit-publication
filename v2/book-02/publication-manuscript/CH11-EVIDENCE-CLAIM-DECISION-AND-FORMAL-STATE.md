# CH11 — Evidence, Claim, Decision and Formal State

## Trust depends on preserving the path from source to state

Professional systems become unreliable when they store only the latest value.

A deadline appears. A fee changes. A provider reports a filing. A reviewer accepts a package. A user approves an action. An official register later shows a result.

These events do not have the same meaning.

Book 02 requires the platform to distinguish:

```text
Evidence
≠ Claim
≠ Decision
≠ Formal State
```

The distinction allows the platform to explain not only what it currently believes, but why, under whose authority and for which purpose.

## Evidence is governed support

Evidence is not merely a file attachment.

Evidence records the support for a proposition, review, decision or state transition. It should preserve:

- source;
- actor or institution;
- capture time;
- method;
- original artifact or stable reference;
- version;
- purpose;
- authority;
- integrity information;
- review and disposition;
- correction or supersession history.

Possible Evidence includes:

- official records;
- signed documents;
- provider returns;
- customer statements;
- payment receipts;
- system logs;
- review records;
- source-backed calculations;
- verified observations.

```text
file present
≠ Evidence accepted
```

A file can be unreadable, outdated, unrelated, unauthorized or insufficient for the intended purpose.

## Claim is a proposition supported by Evidence

Claim answers:

> What is being asserted, by whom, on what basis and with what status?

Examples include:

- the applicant's legal name is X;
- the official fee is Y;
- the deadline falls on a given date;
- the provider filed the application;
- the trademark owner has changed;
- the document satisfies the local requirement.

Claims should preserve:

- statement;
- subject and scope;
- claimant or derivation method;
- supporting and conflicting Evidence;
- jurisdiction and effective period;
- epistemic status;
- review state;
- correction history.

A Claim can be sourced, inferred, disputed, accepted for a limited purpose or unresolved.

```text
well-supported Claim
≠ universal truth for every purpose
```

## Decision is an attributable judgment

Decision answers:

> Which authorized actor selected, accepted, rejected or approved a route based on the available Claims and Evidence?

A Decision should record:

- decision type;
- actor and represented role;
- authority source;
- object and version;
- considered Claims and Evidence;
- alternatives;
- Unknowns;
- conditions;
- effective time;
- expiry or revocation;
- downstream action permitted or blocked.

Examples include:

- accept an identity resolution for filing preparation;
- require additional Evidence;
- approve a package for submission;
- reject a Contribution;
- select a provider;
- determine that no safe route is available.

```text
Decision recorded
≠ external action performed
≠ formal state changed
```

Book 03 governs the operational sequence around Review, Approval and Apply. Book 02 preserves the shared semantic difference.

## Formal State belongs to the Owning Service

Formal State answers:

> What authoritative business condition has been accepted by the service responsible for that object?

Examples include:

- an Order is accepted;
- a Matter is formally open;
- a payment is settled;
- an application is verified as filed;
- a registration record is validated;
- a Product Installation is suspended.

Formal State should not be mutated directly by an AI output, a generic Workflow completion or a provider email.

```text
Claim accepted
≠ Formal State mutated

Provider Return received
≠ Official State established
```

The Owning Service must validate the applicable Evidence and authority before changing the formal record.

## Epistemic status must remain explicit

The platform should distinguish at least:

```text
User-confirmed Fact
Authorized Reused Fact
Source-derived Candidate
AI Inference
Default Assumption
Professional Recommendation
Unknown
Requires Professional Advice
```

These labels describe how information is known, not merely confidence.

A highly confident AI inference remains an inference. A customer-confirmed address may still be insufficient for official identity. A professional recommendation may be authoritative advice without being an official fact.

## Conflicting Claims

The system must permit several Claims to coexist.

For example:

```text
Provider Claim: filed on 10 July
Official Portal Claim: no record found
Payment Evidence: fee debited
Receipt Evidence: missing
```

The architecture should preserve the conflict and create a reconciliation path rather than overwrite one source with another.

```text
latest source
≠ automatically strongest authority
```

## Derived Evidence and calculations

A deadline calculation or fee estimate is often derived from several inputs.

The derived record should preserve:

- source rule;
- rule version;
- triggering event;
- jurisdiction;
- assumptions;
- calculation method;
- generated result;
- reviewer where required.

```text
calculation executed correctly
≠ inputs and rule were correct
```

When a source rule changes, historical calculations remain tied to the earlier version. New policy must not silently rewrite the past.

## Evidence Contracts

For consequential work, the expected Evidence should be defined before execution.

A filing Return Contract might require:

- official application number;
- filing date;
- filed mark;
- filed goods and classes;
- official acknowledgement;
- fee receipt;
- provider identity.

```text
provider says “done”
≠ Evidence Contract satisfied
```

Evidence Contracts connect Book 02 semantics to Book 03 execution without making Core the runtime engine.

## Correction and supersession

A correction should create a governed transition:

```text
new Evidence
→ correction Claim
→ Review or Decision
→ formal correction by Owning Service
→ affected-reference propagation
```

The prior Claim, Decision and State history should remain visible to authorized auditors.

```text
corrected
≠ never happened
```

## Knowledge boundary

Knowledge systems may organize Sources, Claims, Citations, Versions and Review States. Core may define the references required for interoperability.

Core does not become the universal Knowledge repository, and a Knowledge Claim does not automatically mutate a Customer, Matter or official record.

```text
Knowledge accepted
≠ business state changed
```

## AI boundary

AI can:

- extract candidate Evidence;
- identify conflicting Claims;
- summarize sources;
- propose decisions;
- detect missing provenance.

AI cannot silently:

- convert an inference into a fact;
- create professional authority;
- approve a protected action;
- establish official truth;
- erase conflicting Evidence.

## Constitutional rule

```text
Evidence supports Claims.
Authorized actors make Decisions.
Owning Services establish Formal State.

The path among them must remain versioned,
attributable, reviewable and correctable.
```
