# CH31 — Operating Metrics Must Measure Completion and Recovery

A network can look successful while failing customers.

It may have thousands of Providers, rapidly growing transaction volume and short average response times. Yet if work remains incomplete, deadlines are missed, Evidence is weak and recovery depends on heroic manual intervention, the apparent success is misleading.

MGSN therefore needs operating metrics that measure what the network is supposed to accomplish: reliable completion, visible evidence and recoverable failure.

```text
Network Activity
≠ Network Capability

Transaction Volume
≠ Successful Fulfillment

Fast Response
≠ Safe Completion
```

## 1. Metrics should follow the operating chain

The relevant chain is:

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
→ Acceptance
→ Settlement
→ Reconciliation
→ Recovery where required
```

A useful metric should identify where performance was gained or lost within this chain.

A single end-to-end average can conceal:

- slow conflict checks;
- weak Provider Acceptance;
- incomplete Instructions;
- missing Evidence;
- unresolved corrections;
- settlement holds;
- formal-state delays outside MGSN;
- recovery work after a nominal completion.

## 2. Completion is the primary unit

The network should measure completion at several levels.

### Route completion

Did the Need reach a usable route or a legitimate no-route conclusion?

### Engagement completion

Did the accepted Provider complete the governed scope?

### Milestone completion

Were required Milestones completed and accepted with Evidence?

### Return completion

Did the Provider supply the required typed Return and supporting Evidence?

### Reconciliation completion

Were funds, documents, open obligations and formal-state handoffs reconciled?

```text
Provider Says Done
≠ Engagement Complete

Final Invoice Paid
≠ Reconciliation Complete
```

## 3. Route formation metrics

Useful route metrics may include:

- percentage of Needs with at least one eligible route;
- percentage producing one recommended route and meaningful alternatives;
- time to first eligible route;
- percentage requiring operator or professional review;
- percentage ending in no eligible route;
- percentage where Unknowns were disclosed before user confirmation;
- rematch rate;
- preferred-provider qualification rate;
- route expiry before confirmation;
- reasons for route rejection.

These metrics should be segmented by service, jurisdiction, urgency and risk.

A low eligible-route rate may reveal a genuine supply gap. It should not automatically incentivize the system to weaken Eligibility.

```text
Higher Route Coverage
≠ Permission to Admit Unsafe Routes
```

## 4. Allocation and Acceptance metrics

The network should know:

- Allocation acknowledgement rate;
- Provider Acceptance rate;
- time to Provider response;
- conditional Acceptance rate;
- clarification rate;
- decline reasons;
- no-response and expiry rate;
- conflict-related decline rate;
- capacity-related decline rate;
- percentage of replacements required before work starts.

A high decline rate is not automatically bad. Providers may be correctly rejecting conflicts or unrealistic deadlines.

The more useful question is whether the route was formed using current, accurate supply evidence.

```text
Provider Decline
may indicate
safe professional behavior
or stale network data
```

## 5. Instruction quality metrics

Instruction failures create downstream cost.

Relevant measures include:

- percentage of Instruction Packages acknowledged without clarification;
- missing-authority rate;
- version-conflict rate;
- customer-approval completeness;
- document-readiness rate;
- incorrect applicant, address, goods or deadline incidents;
- number of superseded instructions before action;
- protected-action blocks triggered correctly;
- percentage of urgent instructions reconstructed after off-platform communication.

The objective is not to eliminate clarification. It is to reduce avoidable ambiguity while preserving the Provider’s duty to stop when something is unclear.

## 6. Fulfillment metrics

Fulfillment should be measured through observable Milestones.

Relevant measures include:

- on-time Milestone rate;
- Evidence-first completion rate;
- reported-complete but Evidence-pending rate;
- Milestones requiring correction;
- blocked Milestones by reason;
- deadline escalation rate;
- Provider no-response during open work;
- average time from reported completion to accepted completion;
- percentage of Milestones accepted conditionally or partially;
- open-engagement aging.

A low average duration can be misleading if difficult Matters are excluded or abandoned.

Metrics should preserve denominator integrity.

```text
Completed Quickly
because difficult cases disappeared
≠ good performance
```

## 7. Return quality metrics

Return quality determines whether the Originating Workplace can safely continue the Matter.

Useful measures include:

- typed Return completeness;
- required Evidence present;
- official Evidence present where expected;
- Return linked to correct Matter, Milestone and Instruction version;
- discrepancy rate between Provider assertion and official Evidence;
- supersession quality;
- time to corrected Return;
- percentage of Returns accepted on first review;
- percentage creating a new Need;
- percentage leaving material Unknowns.

The network should not reward Providers for optimistic status language unsupported by Evidence.

## 8. Correction metrics

Correction is a normal part of accountable fulfillment.

Metrics may include:

- discrepancy frequency by type;
- time to containment;
- time to Correction Plan;
- time to corrective action;
- corrective Evidence completeness;
- repeat discrepancy rate;
- customer harm avoided or reduced;
- cost allocation outcome;
- percentage corrected without replacement;
- percentage requiring professional or external review.

The goal is not simply fewer recorded corrections. A network that discourages disclosure may appear cleaner while becoming more dangerous.

```text
Fewer Reported Incidents
≠ Fewer Actual Problems
```

## 9. Replacement and recovery metrics

Recovery is a defining MGSN capability.

The network should measure:

- time from failure detection to Safe Stop;
- time to current-state reconstruction;
- time to eligible replacement route;
- time to replacement Acceptance;
- deadline preservation rate;
- percentage of Evidence successfully transferred;
- duplicated cost;
- funds recovered or reconciled;
- original-document recovery;
- official representative-change completion where required;
- percentage of Matters returned to a stable path;
- residual Unknowns after recovery.

A recovery metric should not count replacement selection as recovery completion.

```text
New Provider Chosen
≠ Continuity Restored
```

## 10. Commercial and funds metrics

Commercial metrics should distinguish value from volume.

Relevant measures include:

- quote validity at confirmation;
- fixed, estimated, conditional and Unknown cost distribution;
- Provider price-change rate;
- official-fee variance;
- new-beneficiary exception rate;
- funds hold duration;
- official-payment Evidence rate;
- settlement after accepted Evidence;
- refund and credit cycle time;
- unresolved reconciliation amount;
- cost of replacement and correction;
- margin by service where legitimately available.

Higher margin should not be treated as a Recommendation-quality metric.

## 11. Trust, incident and dispute metrics

Governance metrics may include:

- evidence freshness;
- incident frequency by service and severity;
- containment time;
- finding distribution;
- percentage caused by control design rather than one participant;
- dispute duration;
- partial settlement rate;
- external referral rate;
- appeal and correction outcomes;
- repeat incident rate;
- time from finding to Product improvement.

Public comparison should not be inferred from internal governance metrics.

## 12. Anti-gaming principles

Every metric creates incentives.

Common distortions include:

- Providers declining complex work to preserve completion rates;
- operators delaying incident creation;
- difficult Matters being excluded from denominators;
- Evidence requirements being weakened to shorten cycle time;
- corrections being handled off-record;
- no-route outcomes being suppressed;
- old Matters being marked complete to reduce aging;
- Provider Returns accepted without validation.

MGSN should therefore preserve:

- clear denominators;
- service and risk segmentation;
- Unknown and no-route outcomes;
- auditability;
- metric definitions and versions;
- exception review;
- quality metrics alongside speed metrics;
- recovery metrics alongside completion metrics.

```text
Metric Improvement
without control integrity
may be operational degradation
```

## 13. Cohort and service-specific analysis

Metrics should be interpreted by relevant context:

- jurisdiction;
- service family;
- procedural stage;
- urgency;
- Provider experience level;
- first engagement versus repeat engagement;
- preferred-provider versus recommended route;
- ordinary versus recovery work;
- risk tier;
- evidence requirement;
- package version.

A routine filing route and an emergency contentious route should not be judged by the same raw turnaround expectation.

## 14. Customer and Workplace outcomes

MGSN should also examine outcomes visible to participating Workplaces:

- fewer uncontrolled deadlines;
- clearer price and scope;
- lower time spent chasing Providers;
- higher Evidence completeness;
- faster recovery;
- preserved customer relationship;
- reduced one-person dependency;
- improved visibility across jurisdictions;
- ability to continue work after Provider or platform exit.

Satisfaction feedback can be useful but should not replace operating evidence.

```text
Customer Satisfaction
≠ Completion Proof
```

## 15. Metrics do not create causation

A Provider may correlate with delays because it receives the most difficult Matters. A jurisdiction may appear expensive because official fees are higher. A new Provider may have little data rather than poor performance.

Metrics should support inquiry, not automatic judgment.

AI and analytics may identify patterns, but they must disclose:

- sample size;
- missing data;
- selection effects;
- service complexity;
- confidence;
- competing explanations;
- relevant incidents or policy changes.

## 16. The core MGSN scorecard

A balanced operating scorecard can be organized around five questions:

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

## 17. Product principle

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

The final chapter brings these parts together and explains what kind of infrastructure MGSN is intended to become.