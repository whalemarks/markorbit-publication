# CH21 — Fulfillment Needs Observable Milestones

A Provider can be busy without the engagement being under control.

Emails may be exchanged, documents may be drafted and fees may have been paid, yet the Originating Workplace may still be unable to answer the most basic questions:

- What has actually been completed?
- What remains blocked?
- Which deadline is now at risk?
- What Evidence proves the current state?
- Who must act next?
- Which failure requires correction, escalation or replacement?

MGSN therefore treats fulfillment as an observable milestone chain rather than a stream of activity.

```text
activity
≠ progress

progress claimed
≠ milestone achieved

milestone achieved
≠ milestone accepted
```

## 1. Why activity logs are insufficient

International professional work often produces large communication volumes.

A Provider may report:

- “We are checking.”
- “The application is under process.”
- “We have submitted the documents.”
- “The office has not replied.”
- “The certificate should arrive soon.”

These statements may be sincere. They are too ambiguous for governed fulfillment.

The network needs to know:

```text
which action occurred
for which Matter version
at which authority
on which date
with which Evidence
under which responsibility
and with what next required step
```

A milestone converts narrative status into an inspectable operating claim.

## 2. Milestones must represent meaningful state transitions

A useful milestone is not every small task.

It should represent a transition that matters to at least one of:

- customer expectation;
- deadline safety;
- professional responsibility;
- financial release;
- Evidence completeness;
- formal-state reconciliation;
- correction or replacement readiness.

Possible milestones include:

```text
Provider Acceptance Confirmed
Conflict Review Completed
Instruction Package Acknowledged
Documents Validated for Preparation
Draft Ready for Review
Customer-approved Version Ready
Protected Action Performed
Official Acknowledgement Received
Office Action Reported
Correction Completed
Registration Evidence Returned
Final Return Accepted
Engagement Reconciled
```

The exact milestone set depends on the Service Package and jurisdiction.

## 3. Milestone grammar

Each milestone should define:

- identity;
- engagement and package version;
- responsible Provider;
- objective;
- prerequisite state;
- expected output;
- required Evidence;
- deadline or target time;
- responsible actor;
- reviewer or acceptance authority;
- failure conditions;
- correction route;
- escalation trigger;
- settlement relevance;
- next permitted transition.

```text
milestone name
+ acceptance criteria
+ Evidence requirement
+ responsible actor
+ next transition
= observable fulfillment checkpoint
```

## 4. Planned, started, reported, evidenced and accepted are different

A milestone may pass through states such as:

```text
planned
ready
started
reported complete
Evidence pending
under review
accepted
accepted with follow-up
correction required
rejected
disputed
blocked
cancelled
superseded
unknown
```

These states should not be collapsed.

```text
Provider reports complete
≠ Evidence received
≠ Evidence validated
≠ milestone accepted
```

## 5. Deadlines belong to milestones

A deadline should not live only in an email or calendar note.

The relevant milestone should record:

- deadline source;
- exact date and time where known;
- jurisdiction or authority;
- timezone;
- confidence;
- responsible actor;
- required prior milestones;
- safe internal target;
- escalation threshold;
- consequences of failure;
- last verified date.

Unknown or disputed deadlines must remain explicit.

```text
estimated deadline
≠ verified official deadline
```

## 6. Evidence-first progress reporting

Every material progress claim should identify the Evidence expected to support it.

Examples:

| Milestone | Typical Evidence |
|---|---|
| Provider Acceptance | typed acceptance or signed engagement confirmation |
| Filing performed | filing copy and official or portal acknowledgement |
| Official fee paid | official payment receipt or verifiable authority record |
| Office action received | official communication and retrieval context |
| Correction completed | corrected document, submission evidence and explanation |
| Registration completed | certificate or official registration record |

Provider-generated Evidence may be necessary but should not automatically be treated as official truth.

## 7. Work can proceed while a later action remains blocked

Fulfillment needs staged readiness.

A Provider may be permitted to:

- review documents;
- prepare a draft;
- conduct a conflict check;
- translate a specification;
- identify missing materials;

while still being prohibited from:

- filing;
- paying an official fee;
- withdrawing a right;
- accepting a settlement;
- signing on behalf of a customer.

```text
preparation milestone ready
≠ protected-action milestone authorized
```

## 8. Critical path and dependency visibility

Milestones should expose dependencies.

```text
Customer Approval
→ Funds Clearance
→ Provider Filing
→ Official Acknowledgement
```

If Customer Approval is late, the system should not report “Provider delay.”

If Provider Acceptance is missing, the network should not treat later activity as safely attributable.

Critical-path visibility enables fair accountability.

## 9. Milestone ownership is not universal authority

Different actors may own different milestones:

- Originating Workplace: customer communication and instruction readiness;
- Provider: professional preparation and local action;
- Customer or authorized representative: approvals and signatures;
- MGSN: managed coordination and Return completeness;
- Finance: payment execution and reconciliation;
- Owning Service: formal business-state validation.

```text
Milestone Owner
≠ Owner of Every Decision in the Engagement
```

## 10. Exception triggers

A milestone should trigger review when:

- it misses its target;
- Evidence is absent or contradictory;
- the Provider changes scope or price;
- a deadline changes;
- the responsible professional changes;
- a new third party appears;
- the Provider stops responding;
- funds are requested outside the approved package;
- an official result conflicts with the Provider report.

The trigger should open a typed exception rather than merely add another reminder.

## 11. No-response is a fulfillment state

Silence must be observable.

A no-response state should record:

- last confirmed communication;
- unanswered requests;
- urgency;
- deadline exposure;
- alternate contact attempts;
- escalation status;
- whether replacement is being prepared;
- what Evidence and documents are available for transfer.

```text
no response
≠ no risk
```

## 12. Completion requires closure, not the last deliverable

A Provider may return a certificate while the engagement still lacks:

- funds reconciliation;
- customer report;
- official-state validation;
- missing original documents;
- refund of unused funds;
- closure of correction obligations;
- final archive and retention decisions.

A complete engagement therefore needs a closure milestone.

```text
final deliverable received
≠ engagement reconciled
```

## 13. AI assistance

AI may assist with:

- extracting milestone candidates from communications;
- comparing expected and received Evidence;
- identifying overdue dependencies;
- detecting contradictory status statements;
- drafting escalation summaries;
- highlighting missing acknowledgements.

AI must not:

- declare a milestone accepted without the responsible authority;
- invent Evidence;
- convert an estimated deadline into official fact;
- infer a protected action occurred from payment or preparation;
- blame a party without the dependency record.

## 14. Failure scenarios

### 14.1 “Filed” without filing Evidence

The Provider reports submission, but no filing copy or acknowledgement is returned.

Correct response: mark the milestone as reported complete with Evidence pending, not accepted.

### 14.2 Deadline missed because approval was invisible

The Provider waits for customer approval, while the Workplace assumes filing is underway.

Correct response: expose the blocked dependency and responsible actor.

### 14.3 Final certificate received but unused funds remain

The deliverable is complete, but the financial relationship remains unreconciled.

Correct response: keep the closure milestone open.

### 14.4 Provider silence treated as ordinary delay

Repeated requests go unanswered near a deadline.

Correct response: trigger no-response escalation and replacement readiness.

## 15. Product principle

Fulfillment becomes manageable when each important state transition is observable, attributable and evidenced.

```text
accepted route
→ versioned instruction
→ observable milestones
→ Evidence-backed review
→ correction or acceptance
→ typed Return
→ reconciliation and closure
```

The next chapter explains the Provider Return: the structured Evidence package that allows the Originating Workplace to understand what happened without confusing a Provider report with official or formal truth.