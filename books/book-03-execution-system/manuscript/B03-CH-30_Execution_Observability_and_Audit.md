# B03-CH-30 — Execution Observability and Audit

**Status:** Release Candidate 1

## Chapter Purpose

Execution cannot be governed when important behavior is invisible.

A professional operating system must be able to determine what was requested, what was prepared, what was reviewed, what was approved, what was attempted, what changed, what completed, what failed, what remains uncertain and which actor or Service owns the next action.

Observability makes execution understandable while it is happening.

Audit makes governed execution reconstructable after it happened.

The governing principle is:

```text
Observe execution without redefining truth.
Record accountable facts without exposing protected information.
Preserve enough context to explain action, failure and authority.
Keep diagnostics, metrics, Events and audit distinct.
```

This chapter defines how the MarkOrbit Execution System coordinates execution signals, correlation, Event references, audit context, operational health, review evidence and authorized investigation.

It does not define logging vendors, monitoring platforms, database schemas, dashboard layouts, telemetry protocols, alerting products, Event Bus implementation or Product UI.

The core governance path is:

```text
execution begins
→ operation, actor, version and authority context identified
→ Services and Workflow produce governed signals
→ signals are correlated without changing domain truth
→ protected data is filtered by Permission and Policy
→ anomalies, delays, failures and uncertainty become visible
→ owning actors receive actionable escalation
→ Events and audit preserve accountable facts
→ historical reconstruction remains version-correct and read-only
```

Observability is not a substitute for governance.

Audit is not a substitute for execution truth.

Both exist to make governed execution inspectable without transferring authority to telemetry systems.

---

## 1. Dependency Baseline

This chapter builds directly on Chapters 14 and 25–29. Its primary Book 02 dependencies are the approved Event, Audit Context, versioning, Human Review, Permission, Policy, idempotency, error and AI Context contracts, together with the relevant Task, Communication and Workflow API contracts.

Book 02 owns canonical structures, controlled values and Service behavior. This chapter defines only how Execution consumes them.

## 2. Observability, Monitoring, Event Trace and Audit Are Different

These terms must remain distinct.

| Term | Governance meaning |
|---|---|
| Observability | The ability to understand execution state and behavior from governed signals |
| Monitoring | Ongoing inspection of selected signals against expected conditions |
| Metric | An aggregated measurement of behavior, volume, latency, quality or risk |
| Log | A diagnostic record produced by software or infrastructure |
| Trace | A correlated view of activity across components or execution steps |
| Domain Event | A governed fact about a meaningful change owned by the applicable Service or Event boundary |
| Audit record | Evidence that supports reconstruction of accountable execution and decision context |
| Alert | A signal that a defined condition may require attention |
| Incident | A condition in which execution integrity, availability, confidentiality or correctness may be materially affected |
| Report | A curated presentation of operational or governance information |
| Replay | Read-only reconstruction of prior behavior from preserved references and records |
| Analytics | Aggregated interpretation used to understand patterns, performance or risk |

A log line is not automatically a Domain Event.

A trace span is not Human Review.

A metric is not proof that an individual action occurred.

An alert is not a professional conclusion.

An audit record is not authority to repeat execution.

A dashboard is not Core truth.

---

## 3. The Three Observation Planes

Execution observability should distinguish three planes.

### 3.1 Operational Telemetry Plane

This plane answers:

```text
Is the execution machinery functioning?
```

It may include:

- availability;
- latency;
- queue or backlog;
- error rate;
- connector response;
- resource use;
- timeout;
- tool failure;
- retry count;
- degraded capability.

Operational telemetry supports diagnosis and intervention.

It does not define professional or domain truth.

### 3.2 Execution Coordination Plane

This plane answers:

```text
Where is the governed operation, and what blocks or permits its next step?
```

It may include:

- Workflow position;
- Task state;
- pending review;
- current version;
- Permission or Policy gate;
- idempotency state;
- partial completion;
- reconciliation requirement;
- next allowed action;
- owning Service.

This plane must preserve Book 02 semantics.

### 3.3 Accountability and Audit Plane

This plane answers:

```text
Who did what, under which authority, to which exact version, with what result?
```

It may include:

- actor;
- sponsor;
- review decision;
- approval scope;
- protected action;
- Service result;
- Event reference;
- external reference;
- change activation;
- exception or override;
- uncertainty and resolution.

These planes may be correlated.

They must not be collapsed.

For example, a successful connector call in the telemetry plane does not by itself prove that a filing is legally complete in the accountability plane.

---

## 4. The Execution Observation Unit

Observability becomes useful only when signals can be related to a governed unit of work.

A conceptual observation unit may include:

- operation reference;
- semantic request;
- Workflow reference;
- Task reference;
- subject and target references;
- actor and sponsor;
- organization or Matter scope;
- version set;
- Permission and Policy context;
- Human Review reference;
- idempotency scope;
- owning Service;
- tool or connector reference;
- attempt reference;
- Event reference;
- external reference;
- time boundary.

This is a governance view, not a new Core object.

### 4.1 Semantic Correlation

Correlation should follow the semantic operation, not only the technical request.

One business action may cross:

- Product;
- Workflow;
- Task Service;
- Communication Service;
- provider connector;
- external authority;
- Event trace.

The system should be able to relate these signals without pretending that all components share ownership.

### 4.2 Correlation Does Not Merge Authority

Correlation allows investigation.

It does not allow Workflow to rewrite Service state or telemetry to redefine Event meaning.

### 4.3 Correlation Must Survive Retries

A retry may create a new attempt while remaining part of the same semantic operation.

Observability should distinguish:

```text
semantic operation
attempt 1
attempt 2
reconciliation
final disposition
```

It must not count every retry as a separate professional action.

---

## 5. Required Execution Questions

A well-observed execution should allow an authorized actor to answer:

1. What was requested?
2. Who or what initiated it?
3. Which actor sponsored any AI or agent activity?
4. Which exact versions were used?
5. Which Workflow Contract governed coordination?
6. Which Tasks were planned and which active Tasks were created?
7. Which Human Review was required?
8. Which review decision existed?
9. Which Permission and Policy gates applied?
10. Which Services were called?
11. Which protected actions were attempted?
12. Which effects are confirmed?
13. Which effects did not occur?
14. Which effects remain uncertain?
15. Which Events were emitted by the owning boundary?
16. Which external references exist?
17. Which errors, retries or reconciliation actions occurred?
18. What is the current safe next action?
19. Who owns that next action?
20. What information may the current viewer lawfully see?

If the system cannot answer these questions, it may still be technically observable but not operationally governable.

---

## 6. Signal Classes

Execution signals should be classified by meaning.

### 6.1 Lifecycle Signals

Examples:

- operation prepared;
- review requested;
- review completed;
- Task created;
- apply requested;
- Service accepted;
- Service completed;
- operation blocked;
- operation waiting;
- reconciliation required;
- operation closed.

These signals may or may not be Domain Events.

Their authority depends on the owning contract.

### 6.2 Gate Signals

Examples:

- validation passed or failed;
- Permission allowed or denied;
- Policy allowed, restricted or unavailable;
- Human Review required;
- version conflict;
- idempotency conflict;
- protected action blocked.

Gate signals explain why execution may or may not continue.

### 6.3 Effect Signals

Examples:

- Core mutation confirmed;
- Communication send accepted;
- delivery confirmed;
- provider instruction accepted;
- payment authorized;
- filing receipt obtained;
- Evidence package stored.

Effect signals require strong ownership and reference integrity.

### 6.4 Diagnostic Signals

Examples:

- timeout;
- malformed response;
- tool exception;
- connector latency;
- queue delay;
- unavailable dependency;
- invalid payload;
- model failure.

Diagnostic signals assist operations.

They must not be promoted to domain truth without Service interpretation.

### 6.5 Risk Signals

Examples:

- stale review;
- repeated override;
- duplicate candidate;
- unsupported AI claim;
- unusual provider change;
- deadline uncertainty;
- data-access anomaly;
- repeated retry;
- Event reference gap.

A risk signal is not proof of wrongdoing or professional error.

### 6.6 Security Signals

Examples:

- unauthorized access attempt;
- prompt injection;
- cross-Matter data request;
- tool escalation attempt;
- secret exposure;
- unusual export volume;
- compromised provider indication.

Security signals require restricted handling and appropriate escalation.

---

## 7. Structured Observability

Free-form text alone is insufficient for governed observability.

Signals should preserve structured references where available, such as:

- operation type;
- actor type;
- object reference;
- version;
- gate;
- result class;
- Service;
- attempt;
- time;
- severity;
- correlation;
- retryability;
- uncertainty;
- data classification;
- jurisdiction;
- organization;
- Matter.

The canonical structures belong to Book 02 or implementation contracts.

### 7.1 Stable Meaning

A signal field must not change meaning silently between versions.

### 7.2 Controlled Values

Where a controlled value exists, Execution should use it rather than inventing local labels.

### 7.3 Human-Readable Context

Structured signals should still permit a concise explanation for authorized users.

### 7.4 No Unbounded Payload Dumping

Observability must not copy entire:

- Documents;
- Communications;
- Evidence;
- prompts;
- provider responses;
- personal profiles;
- application packages;

into logs or metrics merely for convenience.

References and controlled summaries are preferred.

---

## 8. Event Trace Governance

Domain Events represent governed facts.

The Execution System may correlate and consume Events.

It must not treat Events as generic logs.

### 8.1 Event Ownership

The owning Service or approved Event boundary determines:

- whether a governed fact occurred;
- which Event type applies;
- which subject changed;
- which version resulted;
- which actor and context are recorded.

Workflow must not emit substitute Events merely because it observed a technical result.

### 8.2 Event Completeness

An Event should preserve enough context to interpret the governed fact.

That may include:

- event type;
- subject;
- action;
- actor;
- source;
- time;
- version;
- audit context;
- related operation;
- Service reference.

The exact contract belongs to Book 02.

### 8.3 Missing Event

A missing Event does not prove that no effect occurred.

The system must distinguish:

```text
effect not confirmed
Event not observed
Event delayed
Event emission failed
effect confirmed by another governed reference
```

Missing trace may require reconciliation.

### 8.4 Duplicate Event

A retry should not produce duplicate Domain Events for one completed effect.

A repeated observation of the same Event is not a new Event.

### 8.5 Event Ordering

Distributed execution may produce delayed or apparently out-of-order signals.

Execution must not rewrite Event time or meaning to create a convenient sequence.

It may preserve:

- occurrence time;
- observation time;
- correlation;
- causal reference;
- uncertainty.

### 8.6 Event Replay

Event or audit replay is read-only.

It must not:

- repeat mutation;
- recreate Tasks;
- resend Communications;
- resubmit filings;
- repeat payment;
- re-engage providers;
- rerun agents with live tools.

---

## 9. Audit Context

Audit context connects action to accountability.

A conceptual audit context may include:

- actor;
- actor type;
- sponsor;
- organization;
- Matter;
- operation;
- purpose;
- Permission result;
- Policy result;
- Human Review;
- version set;
- idempotency scope;
- Service;
- source;
- AI assistance;
- agent identity;
- external reference;
- Event references;
- exception or override;
- time.

Book 03 does not define a new Audit Context Contract.

### 9.1 Purpose Limitation

Audit collection should be tied to a legitimate governance purpose.

“Collect everything” is not a sufficient purpose.

### 9.2 Accountability Without Private Thought

Audit should preserve material facts and decisions.

It should not require:

- private human thought;
- hidden model reasoning;
- unrestricted drafts;
- unrelated personal information.

### 9.3 Historical Stability

Audit context should remain interpretable after:

- version change;
- Policy change;
- Product redesign;
- provider change;
- model change;
- Workflow Contract change.

Historical rendering must not silently use current meaning.

---

## 10. Metrics Governance

Metrics help understand system behavior at scale.

They can also mislead.

### 10.1 Useful Metric Categories

Possible categories include:

- operation volume;
- completion rate;
- blocked rate;
- partial completion;
- uncertainty rate;
- review turnaround;
- revision rate;
- stale-approval rate;
- retry rate;
- duplicate-prevention rate;
- connector failure rate;
- reconciliation duration;
- deadline escalation;
- override frequency;
- AI correction rate;
- agent refusal rate;
- Event trace gap;
- Task backlog.

### 10.2 Metrics Are Aggregates

A metric cannot prove an individual case result.

For example:

```text
99.9% send success
```

does not prove a specific Communication was delivered.

### 10.3 Metric Definition

Every important metric should identify:

- numerator;
- denominator;
- time window;
- included statuses;
- excluded statuses;
- source;
- version;
- uncertainty treatment;
- scope;
- owner.

### 10.4 Do Not Optimize the Wrong Outcome

Unsafe targets include:

- approval rate;
- minimum review time;
- minimum escalation;
- maximum AI acceptance;
- zero blocked actions.

These may pressure the system to weaken governance.

Safer metrics emphasize:

- correct gate use;
- timely review;
- reduced uncertainty;
- duplicate prevention;
- trace completeness;
- safe recovery;
- source fidelity;
- appropriate escalation.

### 10.5 Segmentation and Privacy

Metrics segmented by client, reviewer, provider or employee may create privacy, fairness or commercial risks.

Permission and Policy govern access and use.

---

## 11. Service Levels and Execution Objectives

Operational objectives may be defined for execution without creating professional guarantees.

Possible objectives include:

- validation response time;
- review-request delivery;
- Task creation acknowledgment;
- connector availability;
- status reconciliation;
- Event trace availability;
- escalation acknowledgment;
- audit-query completion.

### 11.1 Operational Objective vs Professional Outcome

An execution Service may meet its latency objective while the professional work remains unresolved.

A fast response is not a correct legal result.

### 11.2 Deadline-Aware Objectives

Deadline-sensitive work may require stronger escalation and observation.

The system must distinguish:

- operational target;
- legal deadline;
- internal service target;
- client expectation;
- provider commitment.

### 11.3 Error Budget

An error budget may govern operational availability.

It must not authorize:

- skipped review;
- duplicate filing;
- reduced Evidence standards;
- unapproved fallback provider;
- weaker security;
- hidden uncertainty.

### 11.4 Objective Breach

An objective breach may create:

- alert;
- escalation;
- incident review;
- capacity change;
- provider review.

It does not automatically change Core object state.

---

## 12. Alert Governance

Alerts convert signals into requests for attention.

Poor alerts create noise, fatigue and unsafe automation.

### 12.1 Alert Requirements

An actionable alert should identify:

- condition;
- affected scope;
- consequence;
- current certainty;
- owner;
- urgency;
- safe next action;
- prohibited action;
- relevant references.

### 12.2 Alert Severity

Severity should reflect consequence, not only technical intensity.

A low-volume filing duplication risk may be more severe than a high-volume analytics outage.

### 12.3 Deduplication

Repeated signals about one condition should not create uncontrolled duplicate alerts or Tasks.

Alert deduplication does not erase separate affected operations.

### 12.4 Suppression

Alert suppression must not hide:

- security incidents;
- protected-action uncertainty;
- deadline risk;
- repeated unauthorized attempts;
- invariant violations.

Suppression rules require governance.

### 12.5 Auto-Remediation

An alert may trigger safe preparation or read-only diagnosis.

It must not automatically:

- approve;
- resend;
- resubmit;
- pay;
- change provider;
- bypass Policy;
- mutate protected state;
- emit a substitute Event.

---

## 13. Incident Governance

An incident is more than an error.

It is a condition that may materially affect:

- execution integrity;
- confidentiality;
- availability;
- professional correctness;
- audit completeness;
- external effect;
- deadline;
- multiple operations or users.

### 13.1 Incident Identification

Potential incidents include:

- duplicated filing;
- duplicate payment;
- unauthorized Communication;
- data exposure;
- lost approval binding;
- widespread stale Knowledge use;
- provider compromise;
- agent tool escalation;
- missing Event trace across many operations;
- corrupted version references;
- repeated silent fallback.

### 13.2 Incident Containment

Containment may include:

- pause affected Workflow paths;
- disable a provider or tool;
- block protected apply;
- revoke agent access;
- preserve Evidence;
- restrict data exposure;
- route affected work to Human Review.

Containment must be scoped and auditable.

### 13.3 Incident Truth

The system should distinguish:

- suspected;
- confirmed;
- contained;
- ongoing;
- resolved;
- under retrospective review.

### 13.4 Incident Recovery

Recovery must preserve:

- prior effects;
- versions;
- uncertainty;
- affected operations;
- corrective actions;
- Human Review;
- Event references;
- external notification decisions.

### 13.5 Post-Incident Review

A retrospective review may examine:

- root causes;
- contract gaps;
- observability gaps;
- Policy gaps;
- agent behavior;
- Human Review quality;
- Service ownership;
- migration or remediation.

Retrospective review must not fabricate historical approval.

---

## 14. Partial Completion and Uncertainty Observability

Partial and uncertain outcomes must be visible as first-class execution conditions.

### 14.1 Partial Completion View

An authorized actor should be able to determine:

- completed effects;
- pending effects;
- failed effects;
- uncertain effects;
- blocked next action;
- reconciliation owner;
- prior versions;
- retry constraints.

### 14.2 Uncertainty Duration

The system may monitor how long outcomes remain uncertain.

Long uncertainty may require escalation.

### 14.3 No Binary Compression

Unsafe:

```text
failed
```

when a Communication was sent but provider acknowledgment is missing.

Unsafe:

```text
completed
```

when payment or filing confirmation is uncertain.

### 14.4 Resolution

When uncertainty resolves, the audit should preserve:

- prior uncertain state;
- reconciliation action;
- evidence;
- final conclusion;
- actor or Service;
- time.

The system must not rewrite history to pretend certainty existed earlier.

---

## 15. Retry and Idempotency Observability

Retry governance requires visibility across attempts.

Observability should identify:

- semantic operation;
- attempt number;
- idempotency scope;
- prior result;
- retry reason;
- gate revalidation;
- reconciliation;
- final result;
- duplicate prevention;
- blocked retry.

### 15.1 Attempt Count Is Not Effect Count

Three attempts may produce one effect.

One attempt may produce multiple cross-Service effects.

### 15.2 Retry Storm

Repeated automatic attempts may indicate:

- failing dependency;
- wrong retry classification;
- missing idempotency;
- agent loop;
- stale version;
- persistent Policy denial;
- connector outage.

The safe response may be to stop and escalate.

### 15.3 Idempotency Conflict

An idempotency conflict should be observable without exposing protected request details to unauthorized users.

### 15.4 Reconciliation Metrics

Reconciliation duration and unresolved count may reveal operational risk.

They do not determine legal or professional outcome.

---

## 16. Human Review Observability

Human Review must be visible without turning reviewers into surveillance subjects.

Useful signals may include:

- review requested;
- assignment;
- acceptance;
- in-review state;
- revision requested;
- decision;
- conditions;
- expiry;
- revocation;
- dissent;
- escalation;
- stale review;
- apply after approval.

### 16.1 Review Quality Signals

Possible indicators include:

- changed version after review;
- repeated revision;
- missing source;
- frequent override;
- action before review;
- decision outside eligibility;
- unusually fast decision where risk is high.

These are investigation signals, not proof of poor professional conduct.

### 16.2 Reviewer Privacy and Independence

Observability must not create incentives that undermine review quality.

Examples of unsafe use:

- ranking reviewers solely by speed;
- penalizing rejection;
- rewarding high approval rate;
- exposing private comments beyond need;
- using AI to infer reviewer motives.

### 16.3 Review-to-Apply Link

Audit should establish whether the protected apply used the exact approved version and scope.

---

## 17. Version and Change Observability

Change control should be observable across:

- proposal;
- review;
- approval;
- activation;
- effective scope;
- migration;
- deprecation;
- supersession;
- rollback;
- emergency restriction.

### 17.1 Change Impact

The system should identify potentially affected:

- Workflows;
- Tasks;
- approvals;
- Communications;
- filings;
- providers;
- Knowledge-dependent outputs;
- agents;
- Products.

### 17.2 In-Flight Adoption

Observability should distinguish operations that:

- remain pinned;
- revalidate;
- migrate;
- stop;
- restart.

### 17.3 Historical Version

Audit must retain the version that governed the action at the time.

### 17.4 Drift

Configuration, Policy, model, tool or Workflow behavior may drift from the approved version.

Drift signals require investigation.

They do not authorize automatic rewriting of execution history.

---

## 18. Communication Observability

Communication requires separate observation of:

- draft;
- review;
- approval;
- send request;
- provider acceptance;
- delivery;
- failure;
- bounce;
- receipt;
- reply;
- external thread.

### 18.1 Send vs Delivery

A send Event does not prove delivery.

Delivery does not prove receipt by the intended person.

Receipt does not prove understanding or agreement.

### 18.2 Recipient and Attachment Trace

Audit should preserve the exact governed package:

- recipient set;
- sender identity;
- content version;
- attachments;
- channel;
- purpose;
- approval.

### 18.3 Privacy

Communication bodies and attachments should not be copied broadly into telemetry.

### 18.4 Uncertain Send

An uncertain send must block blind resend and remain visible until reconciled.

---

## 19. Provider, Payment and Filing Observability

These execution areas require strong separation between technical and professional status.

### 19.1 Provider

Observability may show:

- quote requested;
- quote received;
- terms version;
- comparison prepared;
- provider approved;
- instruction prepared;
- instruction sent;
- acknowledgment;
- service status.

A provider ranking is not provider approval.

### 19.2 Payment

Observability may show:

- payable obligation;
- amount and currency version;
- approval;
- payment attempt;
- authorization;
- settlement;
- failure;
- uncertainty;
- reconciliation.

Technical gateway success must be interpreted by the owning financial Service.

### 19.3 Filing

Observability may show:

- package prepared;
- review complete;
- filing authority confirmed;
- submission attempt;
- external receipt;
- official number;
- official status;
- uncertainty;
- reconciliation.

A connector response is not automatically the legal status.

### 19.4 External Reference Integrity

External references should be preserved with:

- source;
- time;
- scope;
- version;
- verification state.

---

## 20. AI and Agent Observability

AI and agent participation must be visible enough to support accountability without requiring hidden reasoning.

The system should support determination of:

- AI or agent identity;
- version;
- sponsor;
- authority envelope;
- data scope;
- source references;
- tool calls;
- output versions;
- blocked actions;
- retries;
- failures;
- Human Review;
- apply result.

### 20.1 Assistance Disclosure

Material AI assistance should be disclosed to the reviewer according to Policy.

### 20.2 Tool Trace

A tool call trace should identify:

- tool;
- purpose;
- input reference;
- output reference;
- result;
- attempt;
- effect certainty;
- owning Service.

It should not expose unrestricted secrets or payloads.

### 20.3 Prohibited-Action Signals

Attempts by an agent to:

- approve;
- send;
- submit;
- pay;
- mutate protected state;
- bypass review;
- bypass Policy;
- emit Events;

should be observable and may require security or governance escalation.

### 20.4 Agent Quality Metrics

Possible metrics include:

- human correction rate;
- unsupported-claim rate;
- source-mismatch rate;
- review rejection rate;
- refusal correctness;
- escalation quality;
- stale-context rate;
- prohibited-action attempt rate.

Metrics do not grant authority.

### 20.5 No Hidden-Reasoning Collection

The audit boundary should preserve material inputs, outputs, sources, tools and decisions.

It should not require disclosure of private model chain of thought.

---

## 21. Data Protection and Access Control

Observability data can become a secondary sensitive dataset.

It may reveal:

- client identity;
- Matter existence;
- legal strategy;
- reviewer behavior;
- provider terms;
- deadlines;
- internal failures;
- security incidents;
- AI prompts;
- operational architecture.

Permission and Policy must govern access.

### 21.1 Least Exposure

Authorized users should see only the observability detail needed for their role.

### 21.2 Field-Level Restriction

Some fields may require stronger controls, including:

- personal data;
- confidential Document references;
- security diagnostics;
- provider credentials;
- legal advice;
- private review comments;
- agent security signals.

### 21.3 Redaction

Redaction must preserve useful execution meaning while limiting disclosure.

### 21.4 Separation of Duties

Operational engineers may need technical diagnostics without access to full professional content.

Professional reviewers may need case content without infrastructure secrets.

Security operators may need anomaly details without unrestricted Matter access.

### 21.5 Export

Observability export is a protected action when it contains sensitive or cross-Matter information.

---

## 22. Retention, Integrity and Evidence

Observability and audit records require governed retention.

### 22.1 Retention Purpose

Retention may support:

- operational diagnosis;
- professional accountability;
- dispute;
- regulatory obligation;
- security investigation;
- service improvement;
- incident review.

### 22.2 Retention Is Not Uniform

Different records may require different retention based on:

- jurisdiction;
- organization;
- data class;
- object type;
- Event type;
- professional obligation;
- legal hold;
- security purpose.

### 22.3 Integrity

Audit evidence should be protected against unauthorized:

- alteration;
- deletion;
- backdating;
- reassignment;
- version substitution;
- fabricated approval;
- fabricated Event.

This chapter does not define cryptographic or storage implementation.

### 22.4 Correction

An incorrect audit record should not be silently overwritten.

A correction should preserve:

- original record;
- correction;
- reason;
- authority;
- time;
- relationship.

### 22.5 Legal Hold

Where applicable, a legal hold may suspend ordinary deletion.

Execution must consume the governing Policy rather than invent hold rules.

---

## 23. Audit Query and Investigation

Authorized actors may need to investigate a specific execution.

A governed audit query should define:

- purpose;
- scope;
- actor;
- time range;
- object or operation;
- data access;
- output restrictions;
- export permission.

### 23.1 Investigation Views

An investigation may need:

- chronological view;
- causal view;
- actor view;
- version view;
- Service view;
- review view;
- external-effect view;
- agent-tool view.

These are different presentations of governed references.

### 23.2 Search Is Not Authority

Finding an Event or log does not authorize mutation or disclosure.

### 23.3 Reconstruction Limits

The system should disclose when reconstruction is incomplete because of:

- missing Event;
- expired telemetry;
- external-system limitation;
- historical integration gap;
- unsupported old version;
- unrecorded manual action.

It must not invent missing history.

### 23.4 Audit Export

Audit export must be versioned, access-controlled and purpose-limited.

---

## 24. Operational Dashboards and Product Views

Dashboards can help authorized users understand execution.

They can also create false certainty.

### 24.1 Status Presentation

A dashboard should distinguish:

- current governed status;
- operational health;
- uncertainty;
- partial completion;
- stale data;
- last observation time;
- source.

### 24.2 Aggregation

Aggregated counts should not hide:

- blocked protected actions;
- deadline-sensitive outliers;
- unresolved uncertainty;
- security incidents;
- missing audit trace.

### 24.3 Manual Refresh

Refreshing a dashboard must not retry the underlying operation.

### 24.4 Product Cache

A cached Product view must disclose staleness where material.

It must not override the owning Service.

### 24.5 Administrative Controls

A dashboard control that pauses, retries, overrides or exports is a protected action and must follow applicable governance.

Book 04 owns the interface.

---

## 25. Observability Failure

The observation system itself can fail.

Examples include:

- missing telemetry;
- duplicate signals;
- delayed Event;
- incorrect metric;
- broken correlation;
- clock mismatch;
- inaccessible audit;
- over-redaction;
- data leakage;
- alert failure;
- dashboard staleness.

### 25.1 Observability Failure Is Not Execution Failure

A missing signal does not prove the operation failed.

### 25.2 Fail-Safe Response

When observability is insufficient for a protected action, Execution may need to:

- block repetition;
- mark outcome uncertain;
- reconcile through the owning Service;
- escalate;
- preserve available references.

### 25.3 Monitoring the Monitors

Critical observation paths should themselves have health signals.

This chapter does not define implementation architecture.

### 25.4 No Synthetic Trace

The system must not fabricate Events or audit records to repair a monitoring gap.

### 25.5 Retrospective Enrichment

Later evidence may enrich the audit record.

It must be clearly marked as later-observed or retrospectively added.

---

## 26. Governance Examples

### 26.1 Communication Send Timeout

Communication Service submits an approved message to a provider. The provider response times out.

Observability should show:

```text
approved package version
send attempt
provider request reference
response timeout
delivery unknown
resend blocked
reconciliation owner
```

It must not show “not sent” unless absence is confirmed.

### 26.2 Task Creation Response Lost

Task Service creates a Task, but Workflow loses the response.

The trace correlates:

- semantic operation;
- idempotency scope;
- Task Service attempt;
- existing Task reference;
- Workflow reconciliation.

The final result returns the existing Task.

No duplicate Task is created.

### 26.3 Filing Receipt Without Event

An external filing receipt exists, but the expected Domain Event is delayed.

The system should present:

```text
external filing effect confirmed by receipt
Event trace pending
resubmission prohibited
owning Service reconciliation required
```

Workflow must not emit a replacement Event.

### 26.4 Stale Human Review

A Communication package is approved, then an attachment changes.

Observability should connect:

- approved version;
- changed version;
- attachment difference;
- stale approval;
- blocked send;
- renewed review request.

### 26.5 Agent Prohibited-Action Attempt

An agent attempts to call a send tool without Human Review.

The tool denies the call.

The governed trace should preserve:

- agent identity;
- sponsor;
- requested action;
- missing gate;
- denial;
- no send effect;
- escalation if Policy requires.

The agent's text claiming success must not override the Service result.

### 26.6 Provider Incident

A provider is suspected of exposing confidential attachments.

Observability supports:

- affected instructions;
- affected Matters;
- send references;
- provider acknowledgments;
- in-flight uncertainty;
- emergency disablement;
- review and notification decisions.

Access to this view is highly restricted.

### 26.7 Misleading Aggregate Metric

A dashboard shows a 98% Workflow completion rate.

Ten incomplete operations are near filing deadlines.

The aggregate metric must not hide the deadline-sensitive exceptions.

Operational reporting should surface both aggregate health and material outliers.

---

## 27. Governance Rules

Execution Observability and Audit are correct when:

1. telemetry, monitoring, logs, traces, Domain Events and audit remain distinct;
2. signals correlate to semantic operations without merging ownership;
3. every protected action can be linked to actor, version, authority and owning Service;
4. operational health does not redefine professional or domain truth;
5. partial completion and uncertainty remain visible;
6. retries distinguish attempts from effects;
7. Human Review is linked to the exact applied version and scope;
8. version and change history remain reconstructable;
9. Communication send, delivery and receipt remain distinct;
10. provider, payment and filing status are interpreted by owning Services;
11. AI and agent identity, sponsor, sources, tools and outputs remain attributable;
12. hidden reasoning is not required for audit;
13. prohibited agent actions are observable and blocked;
14. metrics are defined, scoped and not treated as individual proof;
15. alerts are actionable and do not trigger unauthorized remediation;
16. incidents preserve truth, scope, versions and remediation;
17. observability data follows Permission, Policy, privacy and retention controls;
18. audit correction does not erase original history;
19. audit replay remains read-only;
20. missing trace does not prove missing effect;
21. Product views disclose staleness and uncertainty where material;
22. Workflow coordinates correlation but does not manufacture Domain Events;
23. owning Services retain mutation and Event authority;
24. observability failure causes safe reconciliation, not synthetic certainty.

---

## 28. Product Boundary

Book 04 may present status, timelines, alerts, metrics, audit search and agent activity. It must disclose staleness, partial completion and uncertainty rather than presenting dashboard appearance as truth.

## 29. Implementation Boundary

This chapter defines no logging stack, telemetry protocol, metrics store, dashboard, Event Bus, Event Sourcing, retention implementation, incident platform or autonomous remediation.

## 30. Chapter Result

Execution observability makes operational behavior understandable.

Audit makes accountable behavior reconstructable.

Neither should become an alternate source of truth.

The operating rule is:

```text
Correlate signals to the semantic operation.
Keep telemetry, Events and audit distinct.
Preserve actor, version, authority and Service ownership.
Represent partial completion and uncertainty directly.
Use metrics for patterns, not individual proof.
Make alerts actionable without granting remediation authority.
Protect observability data through Permission, Policy and retention.
Trace AI and agents without storing hidden reasoning.
Keep replay read-only.
Never manufacture certainty to repair missing visibility.
```

A reliable Execution System is not merely observable because it produces large volumes of logs.

It is observable because authorized people can understand what happened, what remains uncertain, which rules governed the action and who owns the next decision.

This chapter completes **Part IV — Execution Governance**.

The next chapter begins **Part V — MVP Execution System** by defining the smallest governed execution boundary that MarkOrbit may implement without collapsing Core, Execution, Integration and Product responsibilities: **Chapter 31 — Execution MVP Boundary**.
