# B05-CH-07 — Full-Lifecycle Model and State Distinctions

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part I — Product Constitution and Lifecycle Position

## Chapter Purpose

`Full lifecycle` becomes misleading when every stage is reduced to one Product-owned progress bar.

International trademark work contains overlapping lifecycles for need, recommendation, commercial commitment, formal business objects, preparation, Review, approval, Execution, provider work, official proceedings, continuing rights, Documents and Evidence.

MarkReg must make these lifecycles coherent without claiming to own all of them.

```text
Full-Lifecycle Continuity
=
Stable References
+ Distinct State Planes
+ Versioned Decisions
+ Governed Handoffs
+ Sourced External Events
+ Continuing Obligations
```

## 1. Lifecycle Is a Network, Not a Single Workflow

A common path is:

```text
Need
→ Recommendation
→ Commercial Decision
→ Formal Intake
→ Preparation
→ Review
→ Approval
→ Execution
→ Official Acknowledgement
→ Examination or Other Proceeding
→ Outcome
→ Maintenance and Portfolio Action
```

Real journeys branch.

- a user may arrive with a precise instruction and skip early discovery;
- search may occur before or after jurisdiction selection;
- several filing units may emerge from one brand;
- several jurisdictions may use different routes and providers;
- a Package may be approved in one jurisdiction and blocked in another;
- an application may enter examination, opposition or restoration;
- a registration may require maintenance before renewal;
- ownership recordal may become a dependency for renewal;
- one Portfolio may contain independent rights at every stage.

The Product therefore needs stable relationships between states rather than a universal sequence imposed on every case.

## 2. Canonical Lifecycle Stages

The following stages provide a reader map. They are not one shared status field.

| Stage | Primary Product question | Principal controlled output |
| --- | --- | --- |
| need | what business problem exists? | Business Context Snapshot; Need Brief |
| recommendation | what options should be considered? | Recommendation Set; Option Set |
| Decision | what does an accountable participant choose? | Decision Record |
| commercial | what service scope and price are accepted? | Proposal; Quote; Client Acceptance; Commercial Instruction |
| intake | are the required facts and Documents sufficient? | Formal Intake; Requirement Set |
| readiness | what is ready, blocked or conditional for a purpose? | Readiness Assessment |
| preparation | what exact Package is proposed? | Filing, Response, Renewal or Recordal Package Candidate |
| Review and approval | has the exact version been assessed and authorized? | Review; Filing Approval or other bounded approval |
| Execution | has governed work been requested and progressed? | Execution request, Task and Event references |
| external action | what was sent, delivered or accepted by a provider? | Submission Evidence; Provider Acceptance; Provider Report |
| official proceeding | what has the office recorded or issued? | Official Event Snapshot; Official Acknowledgement Evidence |
| outcome | what current result is sourced? | Outcome Snapshot; Registration Outcome Snapshot |
| continuing right | what obligations and vulnerabilities remain? | Right Baseline; Maintenance Obligation Set |
| Portfolio | what actions are proposed across independent rights? | Portfolio Continuity View; Portfolio Action Plan |

Each output has its own source, version, owner and supersession behavior.

## 3. State Planes

MarkReg should separate at least nine state planes.

### Product Journey State

Describes where the user is in the MarkReg experience, for example:

- exploring need;
- comparing options;
- resolving assumptions;
- completing intake;
- preparing a Package;
- reviewing outcome and next action.

This state is Product-local.

### Recommendation and Decision State

Describes whether a recommendation is draft, presented, superseded, accepted, modified or rejected, and whether an accountable Decision exists.

A recommendation may remain useful after rejection as historical rationale.

### Commercial State

Describes Proposal, Quote, acceptance, expiry, Commercial Instruction, invoice, payment, credit, refund and variance.

Commercial commitment does not create professional readiness or filing authority.

### Formal Business State

Describes shared objects such as Order, Matter, Customer, payment record or formal Document as returned by their Owning Services.

MarkReg references this state; it does not redefine it.

### Preparation, Review and Approval State

Describes candidate versions, validation, Professional Review, requested changes and bounded approval.

Approval always applies to an exact version and consequence.

### Execution State

Describes governed Task, Workflow, permission, queue, retry, idempotency, failure and Event progression under Book 03.

### Provider State

Describes provider candidate, selection, appointment, instruction, receipt, Provider Acceptance, work in progress, proposed change, report and delivery.

### Official State

Describes office-issued or office-recorded events and statuses supported by official Evidence.

### Continuing-Right and Portfolio State

Describes registered scope, maintenance obligations, vulnerabilities, renewal, recordal, transactions, monitoring and Portfolio action candidates.

These planes may change at different times and may conflict temporarily. The Product must not force them into one synthetic truth.

## 4. Critical State Distinctions

The following distinctions apply throughout the book.

```text
Need understood
≠ recommendation complete

Recommendation complete
≠ Decision made

Decision made
≠ Quote accepted

Quote accepted
≠ Commercial Instruction

Commercial Instruction
≠ formal Order or Matter

Formal Intake complete
≠ professionally sufficient

Professionally sufficient
≠ reviewed

Reviewed
≠ approved

Approved
≠ executed

Execution requested
≠ sent

Sent
≠ delivered

Delivered
≠ Provider Acceptance

Provider reports submitted
≠ officially acknowledged

Officially acknowledged
≠ registered

Registered
≠ maintenance compliant

Renewal prepared
≠ renewal filed

Renewal filed
≠ renewed status verified

Assignment signed
≠ ownership recordal completed
```

These are not edge cases. They are the core state discipline of the Product.

## 5. State Records Need Domain and Source

A state statement should identify:

- state domain;
- subject and exact version;
- jurisdiction and service;
- source and Evidence;
- actor or system that changed the state;
- time;
- confidence or dispute status;
- expiry or revalidation condition;
- downstream consequence.

`Filed` is insufficient on its own.

Prefer:

- `provider reports the Package submitted; official receipt pending`;
- `connector delivery succeeded; office acceptance not yet established`;
- `official acknowledgement retrieved at [time]`;
- `renewal request sent; renewed register entry not yet verified`.

## 6. Versioned State and Supersession

Many state changes depend on an exact Artifact version.

A material change may affect:

- Recommendation Set;
- Option Set;
- Quote;
- Formal Intake;
- Requirement Set;
- Readiness Assessment;
- Package Candidate;
- Review;
- approval;
- provider instruction;
- Communication;
- Jurisdiction Pack or Rule version.

The Product should preserve:

```text
old version
→ why it was valid
→ Decision or action taken from it
→ new source or change
→ impact assessment
→ superseding version
→ invalidated Review or approval, if any
```

Historical versions remain part of the audit and Decision lineage. Supersession does not mean deletion.

## 7. Material Change

A change is material when it may alter scope, risk, cost, authority, required Documents, provider route, deadline, Review outcome, approval or official consequence.

Examples include:

- applicant or owner change;
- mark representation change;
- jurisdiction, route, class or goods or services change;
- priority change;
- new conflict or search Evidence;
- fee, form or Rule change;
- provider substitution;
- deadline correction;
- Document expiry;
- settlement or response-position change.

Material change triggers an impact assessment and may require repricing, new intake, revalidation, Professional Review, reapproval or suspension.

## 8. Handoffs Connect State Planes

A Handoff should carry stable references rather than flatten all state into a copied payload.

A Handoff Envelope may include:

- origin Product Session;
- acting organization and participant;
- purpose and requested consequence;
- accepted commercial scope;
- formal references;
- exact Artifact versions;
- Review and approval references;
- deadlines and warnings;
- required Permissions;
- idempotency key;
- expected Return and Evidence;
- expiry and failure behavior.

The receiving system or service evaluates the Handoff under its own authority.

```text
Handoff accepted for processing
≠ requested external effect completed
```

## 9. Return and Reconciliation

A Return should identify:

- originating request and idempotency key;
- work or action performed;
- result state and source;
- created or changed formal references;
- Evidence;
- warnings, failure or unknown state;
- required correction or next action;
- whether earlier Product assumptions remain valid.

MarkReg reconciles the Return with the Product journey.

Reconciliation may:

- confirm the expected result;
- identify a partial result;
- detect a changed Package or provider instruction;
- reveal duplicate risk;
- create a correction journey;
- establish an unknown state requiring investigation;
- produce an Official Event Snapshot or Outcome Snapshot.

## 10. Unknown State Is a First-Class State

An external action may be neither safely repeatable nor clearly complete.

Examples include:

- network timeout after submission;
- provider says filed but no Evidence is available;
- payment debited without confirmed order state;
- office record unavailable or inconsistent;
- Return not received from an embedded Product;
- conflicting deadline sources.

The Product should record:

```text
what was attempted
what Evidence exists
what remains unknown
what duplicate or deadline risk exists
who is responsible for reconciliation
when escalation occurs
```

Blind retry is prohibited where duplicate or adverse external effect is possible.

## 11. Independent Jurisdiction State

One brand initiative may produce several independent applications and rights.

A Portfolio view may summarize them, but it must preserve separate:

- filing units and Packages;
- applicants and owners;
- providers;
- official identifiers;
- procedures and deadlines;
- Review and approvals;
- costs and payments;
- outcomes and obligations.

For example, the controlled `EMBERLOOP` journey ends with:

- United Kingdom — registered with continuing obligations;
- United States — under examination after an acknowledged response;
- European Union — in opposition without assumed closure;
- Japan and Australia — candidates only.

No global `registered` status can truthfully represent that Portfolio.

## 12. Continuing-Right State

Registration creates a Right Baseline rather than an endpoint.

The baseline may include:

- official identifier and registration date;
- owner and representative;
- registered mark and scope;
- official status and source;
- certificate or record availability;
- limitations and disclaimers;
- use and Evidence context;
- maintenance and renewal obligations;
- vulnerability and monitoring signals.

Continuing obligations become versioned records with source, responsibility, deadline and consequence.

A reminder generated from an unverified Rule is not a verified obligation.

## 13. Portfolio State Is a View, Not a Right

A Portfolio Continuity View may show:

- independent applications and registrations;
- coverage and ownership inconsistencies;
- upcoming obligations;
- use-Evidence weakness;
- disputes and vulnerabilities;
- duplicate or obsolete rights;
- licensing and transaction context;
- recommended action candidates.

The view does not create one global right or one combined official status.

A Portfolio Action Plan remains a set of proposed actions until each action receives the required Decisions, commercial scope, preparation, Review and approval.

## 14. Client-Facing State Language

Client-facing state should be accurate without exposing unnecessary internal complexity.

Prefer:

- `We are preparing the application details for professional review.`
- `The filing Package is approved and waiting for submission.`
- `The provider reports submission; the official receipt is still pending.`
- `The office has acknowledged the response. Examination remains open.`
- `Registration is verified. Maintenance obligations are being confirmed.`
- `The renewal was filed; the renewed register entry is not yet verified.`

Avoid labels such as `done`, `completed` or `successful` when the relevant consequence is still pending.

## 15. AI and State

AI Assistance may:

- classify a state candidate;
- compare source records;
- identify inconsistencies;
- draft an explanation;
- propose an impact assessment;
- flag stale or missing Evidence.

AI may not:

- create an official state;
- convert Provider Report into Official Truth;
- declare Review or approval complete;
- resolve an authority conflict;
- infer consent from silence;
- retry an External Protected Action autonomously.

Every AI-produced state remains a candidate or Product Projection until accepted under the appropriate rule.

## 16. State Conformance Questions

A conforming implementation should answer:

1. Which state plane does this label belong to?
2. What subject and version does it describe?
3. Who or what changed the state?
4. Which source or Evidence supports it?
5. What remains pending or unknown?
6. Does the state expire or require revalidation?
7. Which Decision or action may occur next?
8. Could the display be mistaken for official or formal truth?
9. Are independent jurisdictions or rights being flattened?
10. Is a retry safe?

## Chapter Lock

```text
Full lifecycle is continuity across distinct state planes.
It is not one Product-owned progress bar.

Every consequential state has a domain, subject, version, source, actor and consequence.

Handoffs connect authority boundaries.
Returns and reconciliation preserve external truth.
Unknown remains explicit until Evidence resolves it.
```

Part II begins with CH08, where this state model is applied to understanding the user’s need before any filing form is presented.