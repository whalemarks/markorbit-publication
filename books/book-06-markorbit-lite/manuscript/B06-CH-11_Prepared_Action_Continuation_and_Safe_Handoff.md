# B06-CH-11 — Prepared Action, Continuation and Safe Handoff

**Status:** Complete Draft 1  
**Chapter Map:** B06-TOC-V0.1 — Owner Accepted  
**Part:** Part II — The Daily Operating Model

## Chapter Purpose

This chapter explains how MarkOrbit Lite turns a qualified Product-local candidate into an exact-purpose Prepared Action, preserves unfinished work through Continuation State, and hands the selected context to the correct destination without claiming that preparation is execution.

The central proposition is:

> Lite should reduce the effort required to act while increasing the clarity of what will happen, who remains responsible, what must be reviewed and which destination will own the formal result.

The controlled anchors are:

```text
ML-W05 — Prepared Action
ML-W10 — Readiness Result
ML-S05 — Continuation State
ML-H01 — Handoff Envelope
ML-H02 — Return Envelope Presentation
```

## 1. A Recommendation Is Not Yet an Action Package

A recommendation may explain:

- why a customer should be contacted;
- why a report may be useful;
- why a candidate should be reviewed;
- why MarkReg may be the correct destination.

The user still needs a concrete package.

A Prepared Action should specify:

- exact subject;
- exact purpose;
- selected candidate;
- selected work-product version;
- intended recipient or destination;
- proposed consequence;
- required checks;
- required Human Review;
- final user confirmation;
- missing information;
- expiry and revalidation conditions.

```text
recommendation
→ explains what may be useful

Prepared Action
→ makes the selected next step inspectable and ready for a governed decision
```

## 2. `ML-W05 Prepared Action`

A Prepared Action is a Product-local record describing a possible consequential step.

Examples include:

- prepare a customer follow-up Communication;
- request Human Review of an Artifact Version;
- request formal Opportunity creation;
- launch or continue a MarkReg Product Session;
- request a Capability Need through MGSN;
- request Task or Workflow creation;
- prepare Delivery or Publish operation;
- request source verification.

A Prepared Action should preserve:

- origin;
- active Organization and user;
- purpose;
- subject references;
- source set;
- selected version;
- intended destination;
- consequence preview;
- authority and permission requirements;
- review and confirmation state;
- blockers;
- return address.

## 3. Prepared Action Is Not Execution

This distinction is non-negotiable.

A Prepared Action may look complete. The message may be written. The recipient may be selected. The Attachment may be rendered. The MarkReg package may be assembled.

None of these facts proves that an external action occurred.

```text
prepared
≠ approved
≠ confirmed
≠ accepted by destination
≠ completed
```

A conforming Product must not use an attractive “one-click” experience to hide these state differences.

## 4. Readiness Must Be Typed

`ML-W10 Readiness Result` distinguishes whether a work product or action package is:

```text
ready
review_required
blocked
incomplete
stale
unsupported
expired
```

Readiness should identify the reason.

### Ready

All Product-local preparation requirements are satisfied for the next permitted step.

### Review required

The package is structurally prepared but requires a defined professional or organizational Review.

### Blocked

Policy, permission, conflict, opt-out or another hard condition prevents progression.

### Incomplete

Required information, source or version is missing.

### Stale

A source, price, status, contact or selected version requires refresh.

### Unsupported

The Product or destination does not support the requested path.

### Expired

The package or authority context is no longer valid.

A generic “Not ready” state is insufficient because the next safe action depends on the reason.

## 5. Missing Information Should Produce a Specific Next Step

A Prepared Action may be incomplete because it lacks:

- verified customer identity;
- current contact details;
- channel permission;
- trademark ownership;
- a current official status;
- a reviewed Artifact Version;
- a required document;
- destination eligibility;
- professional Review;
- final user confirmation.

The Product should not fill these gaps silently.

It may prepare:

- a request for information;
- a source refresh;
- a verification checklist;
- a Review Handoff;
- an alternative action with lower consequence.

```text
missing information
→ visible blocker or request
≠ AI-invented completion
```

## 6. Preview Must Show Exact Consequence

Before final confirmation, the user should be able to inspect:

- what will be sent, created or requested;
- which exact version is involved;
- who or which service will receive it;
- which account or channel will be used;
- what formal state may be requested;
- which facts remain uncertain;
- whether the action can be reversed;
- what result is expected to return.

Examples:

```text
Send this exact customer email to Contact C
through Communication Service.
```

```text
Request formal Opportunity creation
for Customer A and Service Need N.
```

```text
Launch MarkReg with this customer, trademark,
need and selected source package.
```

Vague labels such as “Proceed” or “Continue” should not hide materially different consequences.

## 7. User Confirmation Is Not Human Review

A user may confirm:

- the recipient;
- selected content;
- channel;
- intended destination;
- commercial intent;
- timing.

Human Review may separately decide:

- professional adequacy;
- legal or factual support;
- client interest;
- disclosure safety;
- version approval;
- suitability for external use.

One person may perform both roles in a solo practice, but the decisions remain semantically distinct.

```text
user confirmation
≠ professional Review
```

The Product should preserve which decision occurred and against which version.

## 8. Final Confirmation Must Be Close to the Consequence

Confirmation gathered too early may no longer be valid after:

- the Artifact changes;
- the recipient changes;
- the source becomes stale;
- the destination changes;
- the consequence becomes broader;
- a new risk appears;
- a price expires.

A conforming flow should re-confirm when a material field or version changes.

```text
confirmation of Version 2
≠ confirmation of Version 3
```

## 9. `ML-S05 Continuation State`

Professional work is often interrupted.

Continuation State preserves the Product journey between sessions.

It may retain:

- originating candidate;
- current purpose;
- selected subject;
- latest Artifact Version;
- current Readiness Result;
- unresolved questions;
- completed user dispositions;
- required Review;
- intended Handoff;
- defer or expiry condition;
- last returned result.

Continuation should help the user resume without reconstructing the journey from memory.

## 10. Continuation Must Not Invent Destination State

Suppose a user prepares a MarkReg Handoff and closes Lite before sending it.

Continuation may say:

> MarkReg package prepared; final confirmation required.

It must not say:

> MarkReg application started.

Similarly:

- a prepared message is not sent;
- a routed Review is not approved;
- an Opportunity request is not a formal Opportunity;
- a Task request is not an assigned Task;
- a Publish Package is not published.

```text
Product continuity
≠ formal lifecycle continuity
```

## 11. Continuation Needs Freshness Checks

A journey resumed later may depend on changed information.

Before progression, Lite may need to revalidate:

- official status;
- contact details;
- customer relationship;
- selected source;
- price;
- policy;
- Artifact Version;
- destination availability;
- user and Organization context.

The Product should not assume that a once-ready package remains ready indefinitely.

## 12. `ML-H01 Handoff Envelope`

A Handoff Envelope is the common versioned package used to transfer selected context to a destination.

Minimum fields include:

- origin Product and session;
- active Organization;
- responsible user;
- subject references;
- purpose;
- selected candidate;
- selected work-product version;
- sources and provenance;
- missing information;
- intended consequence;
- authority and Review context;
- allowed disclosure scope;
- expected return type;
- return address;
- expiry.

A Handoff Envelope is not a raw data dump.

It is a minimized, purpose-bound transfer package.

## 13. Different Destinations Need Different Handoffs

### Human Review

Needs exact version, sources, claims, audience and requested decision.

### Communication Service

Needs draft, exact recipients, channel, attachments, purpose and send consequence.

### Opportunity Service

Needs qualified candidate, customer/prospect reference, evidence, proposed owner and scope.

### MarkReg

Needs customer/applicant/trademark context, service need, selected sources, missing information and authority context.

### MGSN

Needs a minimized Capability Need, jurisdiction, service, constraints and disclosure scope.

### Task / Execution

Needs proposed work, actor, dependencies, Review context and protected-action boundary.

The common Envelope pattern does not imply identical content.

## 14. Destination Revalidation Is Mandatory

A destination must be able to reject or request more information.

It should not trust Lite merely because:

- the user qualified a candidate;
- the package appears complete;
- AI confidence is high;
- a previous similar Handoff succeeded.

The destination may revalidate:

- formal object existence;
- authority;
- current state;
- eligibility;
- policy;
- version;
- required documents;
- conflict;
- professional sufficiency.

```text
Handoff
≠ destination acceptance
```

## 15. `ML-H02 Return Envelope Presentation`

The destination may return:

```text
accepted
more_information_required
rejected
blocked
failed
unknown_external_outcome
formal_record_reference_returned
completed_by_destination
```

Lite presents the returned result with:

- destination;
- source time;
- formal reference where available;
- status;
- missing information;
- next permitted actions;
- relationship to the originating candidate and package.

The Return remains destination-sourced.

## 16. Unknown Outcomes Must Remain Unknown

External operations may produce ambiguity:

- a connector times out;
- a Communication service cannot confirm delivery;
- a manual user action is not reported;
- a provider does not acknowledge receipt;
- a destination accepted the package but later state is unavailable.

The Product must not guess.

It may:

- request reconciliation;
- show a pending/unknown state;
- ask the user;
- check the destination;
- wait for authoritative evidence.

It must not blindly retry a consequential action because a success response was absent.

```text
no confirmation
≠ failure
≠ safe to repeat
```

## 17. Failure Is Part of the Product Journey

A rejected or blocked Handoff should return enough information to continue safely.

Examples:

- missing applicant information;
- unsupported jurisdiction;
- expired price;
- invalid recipient;
- insufficient authority;
- conflicting status;
- review rejected;
- policy blocks disclosure.

The Product may prepare the next corrective step.

Failure should not force the user to reconstruct the entire context from zero.

## 18. Handoff Does Not Transfer Professional Responsibility Automatically

A destination may accept technical custody of a package without accepting professional responsibility.

The Product should distinguish:

- package receipt;
- service acceptance;
- professional appointment;
- Task ownership;
- filing authority;
- external-action completion.

For example, MGSN returning provider candidates does not appoint a provider.

MarkReg creating a Product Session does not itself prove a filing instruction.

Communication Service accepting a send request does not prove delivery or customer agreement.

## 19. A Safe Handoff Is Minimal but Sufficient

Too little context causes repeated questions and errors.

Too much context creates privacy, disclosure and authority risk.

The Product should send the smallest package that allows the destination to:

- understand the purpose;
- verify the subject;
- inspect sources;
- identify missing information;
- evaluate authority;
- return a typed result.

This is hybrid minimization in action.

## 20. Minimum Conforming Prepared Action and Handoff Flow

A minimum conforming experience should demonstrate:

1. a qualified Product-local candidate;
2. an exact-purpose Prepared Action;
3. typed Readiness Result;
4. visible blockers and missing information;
5. exact-version preview;
6. separate Review and final confirmation;
7. Continuation State without invented formal status;
8. freshness revalidation on resume;
9. minimized Handoff Envelope;
10. destination revalidation;
11. typed Return presentation;
12. preserved failure and unknown states;
13. no automatic retry of an unknown consequential action;
14. no claim that Handoff transfers authority by itself.

## 21. Part II Operating Model

Part II has now established the complete daily sequence:

```text
Lite Session
→ Today Snapshot
→ Authorized Context
→ Source Observation
→ Signal
→ Candidate
→ Recommendation Presentation
→ User Disposition
→ Qualification Result
→ Prepared Action
→ Readiness
→ Review / final confirmation
→ Handoff Envelope
→ destination revalidation
→ Return Envelope Presentation
→ Continuation
```

The sequence gives Lite a simple daily experience without collapsing the distinctions required for professional work.

## Chapter Conclusion

MarkOrbit Lite should make responsible action easier, not make consequential action invisible.

```text
prepare precisely
→ preview consequence
→ review where required
→ confirm exact action
→ hand off minimally
→ preserve typed result
```

Part III will apply this operating model to Customer and Service Growth, beginning with the highest-value source: the user’s existing customer and trademark portfolio.