# CH31 — Operating Metrics Must Measure Completion and Recovery

A network can look successful while failing customers.

It may have many Providers, rising transaction volume and short response times. Yet if work remains incomplete, Evidence is weak and recovery depends on heroic manual intervention, the apparent success is misleading.

```text
Network Activity
≠ Network Capability

Transaction Volume
≠ Successful Fulfillment

Fast Response
≠ Safe Completion
```

MGSN therefore needs metrics that follow the operating chain and measure reliable completion, visible Evidence and recoverable failure.

## 1. Metrics should follow the chain

```text
Need Projection
→ Eligibility
→ Candidate Route Set
→ Recommendation
→ User Disposition
→ Allocation
→ Provider Acceptance
→ Instruction
→ Fulfillment
→ Return
→ Settlement
→ Reconciliation
→ Recovery where required
```

A single end-to-end average can hide slow Conflict checks, weak Acceptance, missing Evidence, unresolved Corrections or formal-state delays outside MGSN.

## 2. Completion has several layers

The network should distinguish:

- Route completion: a usable route or legitimate no-route conclusion;
- Engagement completion: the accepted scope was fulfilled;
- Milestone completion: required checkpoints were accepted with Evidence;
- Return completion: the typed Return and supporting Evidence arrived;
- Reconciliation completion: funds, documents, open obligations and formal-state handoffs were closed.

```text
Provider Says Done
≠ Engagement Complete

Final Invoice Paid
≠ Reconciliation Complete
```

## 3. Route and Acceptance metrics

Useful measures include:

- Needs with an Eligible Route;
- time to first Eligible Route;
- no-route and Unknown rates;
- rematch and route-expiry rates;
- Provider response, Acceptance and decline reasons;
- Conflict or capacity-related declines;
- replacements required before work starts.

A low route-coverage rate may reveal a real supply gap. It should not pressure the system to weaken Eligibility.

```text
Higher Route Coverage
≠ Permission to Admit Unsafe Routes
```

A Provider decline may also indicate safe professional behavior rather than poor performance.

## 4. Instruction and Fulfillment quality

Instruction measures may include missing authority, version conflict, document readiness, customer approval completeness and correctly triggered Protected-action blocks.

Fulfillment measures should focus on observable Milestones:

- on-time accepted Milestones;
- Evidence-first completion;
- reported-complete but Evidence-pending states;
- blocked or corrected Milestones;
- deadline escalations;
- no-response during open work;
- open-engagement aging.

```text
Completed Quickly
because difficult cases disappeared
≠ Good Performance
```

Denominators must preserve difficult, failed and abandoned Matters.

## 5. Return, Correction and Recovery metrics

Return quality measures whether the Originating Workplace can safely continue the Matter. Relevant indicators include attribution, official Evidence, first-review acceptance, discrepancy rate, material Unknowns and corrected Return time.

Correction metrics should measure containment, Correction Plan speed, corrective Evidence and recurrence—not merely the number of recorded Corrections.

```text
Fewer Reported Incidents
≠ Fewer Actual Problems
```

Recovery metrics should include:

- time to Safe Stop;
- time to current-state reconstruction;
- time to Eligible replacement and Provider Acceptance;
- deadline preservation;
- Evidence, funds and original-document recovery;
- formal representative change where required;
- residual Unknowns.

```text
New Provider Chosen
≠ Continuity Restored
```

## 6. Commercial and governance metrics

Commercial metrics may cover quote validity, official-fee variance, new-beneficiary exceptions, Funds Hold duration, settlement after accepted Evidence, refund cycle time and unresolved reconciliation amounts.

Higher margin is not a Recommendation-quality metric.

Governance metrics may include Evidence freshness, Incident severity and containment time, Dispute duration, external referral, recurrence and time from finding to Product improvement.

Internal governance metrics should not become public Provider rankings.

## 7. Every metric can be gamed

Common distortions include:

- declining complex work to preserve completion rates;
- delaying Incident creation;
- excluding difficult Matters;
- weakening Evidence requirements to shorten cycle time;
- handling Corrections off record;
- suppressing no-route outcomes;
- marking old Matters complete without reconciliation.

MGSN should preserve clear denominators, service and risk segmentation, metric definitions, Unknown outcomes, auditability and quality measures alongside speed measures.

```text
Metric Improvement
without control integrity
may be Operational Degradation
```

## 8. Context and causation

Metrics should be interpreted by jurisdiction, service family, procedural stage, urgency, route type, Provider experience, risk tier and Package version.

A Provider may correlate with delays because it receives the hardest work. A jurisdiction may appear expensive because official fees are higher. Sparse data is not the same as poor performance.

Metrics support inquiry. They do not create causation or automatic blame.

## 9. The core MGSN scorecard

A balanced scorecard can be organized around five questions:

```text
1. Can the network form a safe route?
2. Can the Provider accept and understand the work?
3. Can the work be completed with Evidence?
4. Can failure be corrected or replaced?
5. Can the Matter, funds and authority be reconciled?
```

The corresponding metric families are:

```text
Coverage and Eligibility
Acceptance and Instruction Quality
Completion and Return Quality
Correction and Recovery
Reconciliation and Governance
```

## 10. Product principle

MGSN should not optimize for the appearance of activity.

It should measure whether global professional capability was actually made usable, completed and recoverable.

```text
Operational Success
= Safe Route
+ Clear Acceptance
+ Versioned Instruction
+ Observable Fulfillment
+ Accepted Evidence
+ Reconciled Outcome
+ Recoverable Failure
```

The final chapter brings these elements together and explains what kind of infrastructure MGSN is intended to become.