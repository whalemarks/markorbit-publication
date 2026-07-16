# B06-CH-31 — Evaluation, Conformance and Zero-Tolerance Conditions

## Chapter Role

This chapter defines how MarkOrbit Lite is evaluated as a Product and tested for conformance with its accepted Charter and Product Baseline.

The central proposition is:

> Product success and Product conformance are related but different. A Product may attract usage while violating its authority boundaries, and a safe Product may still fail to create enough user value. Both questions must be answered explicitly.

Evaluation asks:

```text
Does Lite create meaningful, repeatable and sustainable professional value?
```

Conformance asks:

```text
Does Lite preserve the required meanings, responsibilities and safety controls while creating that value?
```

A release or pilot must not hide failure in one dimension behind success in the other.

---

## 1. Four evaluation record types

The Product Baseline defines four records used in this chapter.

### `ML-E01 Evaluation Run`

A bounded test with:

- purpose;
- population;
- Organization and access scope;
- Product version;
- source versions;
- supported journeys;
- time window;
- metrics;
- scenario set;
- known limitations;
- decision owner.

### `ML-E02 Outcome Observation`

A typed observation about:

- use;
- response;
- Handoff;
- returned result;
- correction;
- failure;
- unknown outcome.

It must preserve source and confidence.

### `ML-E03 Reuse Evidence`

Evidence that a work product, lesson, preference, memory or Asset was reused within an allowed scope and produced a known result.

### `ML-E04 Safety / Privacy Finding`

A recorded defect, prevented defect or boundary violation involving:

- access;
- privacy;
- rights;
- authority;
- Review;
- external action;
- formal-state ownership;
- local/synchronization boundaries;
- misleading Product status.

These records help distinguish Product evidence from impressions.

## 2. Evaluation must be longitudinal

A one-time successful demonstration is insufficient.

Lite is intended to organize daily and recurring professional practice.

Therefore an Evaluation Run should examine:

- first-use value;
- recurring use;
- repeated journey completion;
- whether context improves future work;
- whether stale information is detected;
- whether users trust and correct the Product;
- whether Handoff and Return continuity survives over time;
- whether cost remains sustainable as usage grows.

The Product may appear impressive in a controlled demo while failing in continued use because:

- recommendations become repetitive;
- sources become stale;
- users cannot understand why items appear;
- corrections do not propagate;
- generated content creates fatigue;
- prospect quality falls;
- destination results do not return;
- support and Review cost grows faster than revenue.

## 3. Meaningful use is not screen activity

A meaningful use event should correspond to professional progress.

Examples include:

- inspecting and correcting a Service-Value Candidate;
- using or meaningfully editing an Artifact;
- confirming a customer action;
- classifying a real response;
- qualifying or rejecting a service need;
- sending a governed Handoff;
- acting on a returned result;
- accepting or rejecting a memory or Asset candidate;
- retiring stale capability.

The following are weak signals by themselves:

- opening the application;
- scrolling Today;
- viewing a generated item;
- clicking a notification;
- starting a generation request;
- downloading a file without using it.

Evaluation should report both activity and meaningful-use evidence rather than substituting one for the other.

## 4. Evaluation dimensions

A complete Product evaluation should include at least eight dimensions.

### 4.1 Recurring professional use

Measure:

- weekly active professional rate;
- days with meaningful use;
- return after first useful result;
- journey completion frequency;
- use across more than one Product loop;
- time to resume unfinished work.

Recurring use does not need to mean daily use for every edition.

A portfolio-focused edition may produce strong weekly or event-driven value.

### 4.2 Opportunity relevance

Measure:

- Candidate inspection rate;
- acceptance for preparation;
- rejection;
- suppression;
- correction;
- reason for rejection;
- time sensitivity;
- client-value assessment;
- professional-risk assessment.

A high acceptance rate is not automatically desirable.

It may indicate overly broad acceptance, weak user scrutiny or commercial pressure.

### 4.3 Work-product utility

Measure:

- actual use;
- meaningful edits;
- complete rewrite rate;
- deterministic-field defect rate;
- Review revision rate;
- time saved;
- user confidence;
- use by the intended audience;
- correction and retirement.

### 4.4 Customer and service outcomes

Measure:

- confirmed customer actions;
- delivery or send result;
- response type;
- qualified need rate;
- rejected or no-need outcomes;
- MarkReg or formal Opportunity Handoff;
- formal reference returned;
- later service or revenue references where supplied by Owning Services.

### 4.5 Handoff and Return quality

Measure:

- destination acceptance;
- more-information requests;
- rejection;
- duplicate requests;
- missing authority context;
- missing sources or versions;
- time to Return;
- continuity after Return;
- unknown-outcome reconciliation.

### 4.6 Capability accumulation

Measure:

- Feedback and Correction records;
- accepted preferences;
- Personal and Organization Memory candidates;
- Reusable Asset candidates;
- safe reuse;
- Reuse Evidence;
- prevented repeated errors;
- retired or superseded material;
- Knowledge contributions accepted or rejected.

### 4.7 Safety, privacy and professional control

Measure:

- blocked unauthorized access;
- blocked opt-out contact;
- prevented restricted-case reuse;
- prevented unreviewed external action;
- prevented Local Only synchronization;
- false formal-state claims;
- unknown outcomes incorrectly retried;
- user understanding of blocks;
- time to remediate findings.

### 4.8 Sustainable operation

Measure:

- AI cost;
- Render and TTS cost;
- storage;
- support;
- professional Review;
- prospect acquisition and validation;
- integration cost;
- correction and incident cost;
- gross margin by plan and usage cohort.

## 5. Conformance is observable behavior

A conformance statement is not satisfied by naming the correct object in a design document.

For example, the statement:

```text
Service-Value Candidate ≠ formal Opportunity
```

must be demonstrated through behavior:

1. Lite creates or displays a Product-local Candidate.
2. User accepts it for preparation.
3. No formal Opportunity appears automatically.
4. An Opportunity Handoff is prepared.
5. Opportunity Service revalidates.
6. A formal reference is returned or the request is rejected.
7. Lite presents the result without claiming ownership.

Likewise:

```text
Render complete ≠ approved
```

requires the Product to display Render success while preserving a separate Review and approval state.

## 6. Scenario families

`ML-SCN-01–ML-SCN-24` form five scenario families.

### 6.1 Customer and Service Growth — `ML-SCN-01–06`

These scenarios test:

- valid portfolio opportunities;
- stale or conflicting sources;
- missing customer or Matter access;
- Candidate/formal Opportunity separation;
- qualified customer need;
- client interest and professional risk over revenue.

### 6.2 Historical customer and prospect development — `ML-SCN-07–12`

These scenarios test:

- stale historical contacts;
- opt-out and suppression;
- source and limitation preservation;
- channel permission;
- duplicate prospects;
- invalid platform-supplied prospects and replacement evidence.

### 6.3 Professional work products — `ML-SCN-13–18`

These scenarios test:

- raw AI output versus Artifact;
- Render versus approval;
- deterministic-field validation;
- Publish Package readiness versus publication;
- post-Review edits and new versions;
- unknown external publication outcomes.

### 6.4 Cases, memory and reusable capability — `ML-SCN-19–22`

These scenarios test:

- Client/Matter Restricted information;
- case reuse without universal inference;
- repeated behavior versus accepted preference;
- Organization Review and provenance.

### 6.5 Handoff, local data and formal state — `ML-SCN-23–24`

These scenarios test:

- destination revalidation and Return provenance;
- local readability versus upload, sharing and authority.

## 7. Severity model

### BLOCKING

A BLOCKING violation invalidates the affected capability or pilot.

Examples include:

- unauthorized Customer or Matter access;
- Candidate automatically becoming formal Opportunity;
- revenue overriding client interest or professional risk;
- outreach after opt-out;
- claiming channel permission without evidence;
- raw AI text represented as approved Artifact;
- Render represented as professional approval;
- Publish Package represented as published;
- unknown external outcome blindly retried;
- restricted case facts exposed;
- Organization Memory promoted without Review;
- destination accepting Lite state without revalidation;
- Local Only data synchronized without authority.

A pilot with a confirmed BLOCKING violation cannot be described as conforming.

### MAJOR

A MAJOR finding must be corrected before a baseline or release.

Examples include:

- stale or conflicting source handled without adequate warning;
- duplicate prospect identity not resolved;
- failed Render counted as entitlement fulfillment;
- substantive post-Review edit without new version;
- case success reused as a broad rule without adequate limitation.

### STANDARD

A STANDARD scenario expresses expected behavior whose failure may be contained but still requires correction and evidence.

## 8. Zero-tolerance conditions

A zero-tolerance condition is a rule whose breach cannot be offset by usage, revenue or user enthusiasm.

The Book 06 zero-tolerance conditions are:

```text
ZT-01  no unauthorized Customer/Matter disclosure
ZT-02  no silent conversion of Candidate into formal state
ZT-03  no autonomous consequential customer contact
ZT-04  no bypass of required Human Review
ZT-05  no claim that prepared, rendered or accepted means externally completed
ZT-06  no blind retry after unknown consequential outcome
ZT-07  no automatic promotion of personal behavior into Organization truth
ZT-08  no reuse of restricted case content without authority
ZT-09  no automatic provider appointment by Lite
ZT-10  no Local Only upload, sharing or remote processing without authority
ZT-11  no revenue optimization that overrides client interest or professional risk
ZT-12  no marketing claim that content or lead volume alone proves Product success
```

These labels are editorial projections of the accepted scenarios and do not create new controlled IDs.

## 9. Blocked action as success

Traditional product analytics often treat a blocked action as friction.

In professional systems, a correct block may be a successful result.

Examples:

- preventing contact with an opted-out historical customer;
- stopping publication because rights are missing;
- refusing to send a changed Artifact under an old approval;
- preventing Local Only material from leaving the device;
- stopping duplicate MarkReg launch after an unknown result;
- requiring applicant authority before formal intake;
- refusing to promote an unsupported case conclusion.

The Product should record:

- what was blocked;
- which rule applied;
- what risk was prevented;
- how the user can resolve the block;
- whether the block was later confirmed correct.

This evidence helps distinguish useful governance from arbitrary obstruction.

## 10. Required negative tests

A strong conformance program deliberately attempts unsafe transitions.

Negative tests should include:

- changing Organization context mid-session;
- opening a Customer/Matter item without access;
- accepting a Candidate and checking that no formal Opportunity appears;
- editing an approved Artifact and attempting to use the old approval;
- rendering a file with mismatched price or applicant data;
- preparing publication without rights;
- retrying a Communication with unknown outcome;
- reusing a Client Restricted case;
- promoting a Personal Memory Candidate into Organization Memory without Review;
- requesting a Provider with excessive customer disclosure;
- reading a local file and attempting unauthorized synchronization;
- selecting a high-revenue option that conflicts with client interest.

Negative-test evidence should be retained alongside positive journey evidence.

## 11. Data quality findings are Product findings

Incorrect or stale source data should not be treated only as an external problem.

Lite's Product responsibility includes:

- exposing source and freshness;
- representing uncertainty;
- requesting verification;
- limiting downstream confidence;
- blocking unsafe actions;
- recording corrections;
- propagating correction impact.

A source defect may not be caused by Lite, but misleading use of that source is a Lite defect.

## 12. Unknown outcomes require reconciliation

Unknown outcomes are especially important because they tempt systems to guess.

A conforming Product must distinguish:

```text
unknown
≠ completed
≠ failed
≠ safe to retry
```

The reconciliation process should use:

- request identifier;
- destination;
- timestamp;
- exact version;
- recipient or account;
- external reference;
- audit events;
- user confirmation;
- destination query where available.

Only after reconciliation should the state change.

## 13. Release and pilot conformance matrix

Before a broader pilot or release, the review should answer:

| Area | Required evidence |
| --- | --- |
| Authorized context | access, Organization and purpose tests |
| Candidate separation | no automatic formal state |
| Work-product integrity | source, version, Review and deterministic validation |
| External action | exact confirmation and typed outcomes |
| Handoff/Return | destination revalidation and provenance |
| Memory/Asset | scoped acceptance, rights and retirement |
| Local/private | synchronization and disclosure controls |
| Safety | all BLOCKING scenarios pass |
| Evaluation | meaningful Product outcome evidence |
| Economics | cost evidence captured without lowering controls |

## 14. Findings and remediation

Every finding should identify:

- finding ID;
- Evaluation Run and Product version;
- scenario or Charter rule;
- severity;
- affected users and records;
- observed behavior;
- expected behavior;
- immediate containment;
- root cause;
- required correction;
- verification evidence;
- downstream impact;
- closure decision.

A finding is not closed because a sentence in documentation changed.

Closure requires evidence that the affected behavior conforms.

## 15. Evaluation integrity

Evaluation can itself become misleading.

Common distortions include:

- excluding rejected Candidates from quality analysis;
- counting prepared drafts as used work products;
- counting opened messages as qualified need;
- counting user-reported publication as confirmed publication;
- ignoring support and Review cost;
- removing high-cost users from unit-economics calculations;
- excluding blocked unsafe actions from Product value;
- combining formal Opportunity creation with Product-local Candidate creation;
- using vanity metrics to justify a predetermined launch.

The Evaluation Run must preserve the original population, exclusions and decision rules.

## 16. Conformance does not guarantee product-market fit

A perfectly conforming Product can still fail because:

- opportunities are not relevant enough;
- work products are not useful;
- users do not trust or understand the workflow;
- the Product is not frequent enough to form a habit;
- integration burden is too high;
- the price is wrong;
- cost is unsustainable;
- the target user is incorrect.

Conformance protects meaning and responsibility.

It does not create demand by itself.

## 17. Product-market fit does not excuse non-conformance

A popular Product may still be unsafe.

High usage or revenue cannot justify:

- unauthorized data use;
- misleading formal status;
- unreviewed legal/professional claims;
- automatic outreach after opt-out;
- unsafe external action;
- hidden memory promotion;
- provider appointment without governance;
- local data exfiltration.

Growth achieved by violating the Product Charter is constitutional drift, not success.

## 18. Chapter conclusion

Lite should be judged through evidence, not feature count or narrative confidence.

A credible evaluation combines:

```text
meaningful recurring use
+ relevant professional value
+ trustworthy work products
+ real customer/service outcomes
+ governed Handoff and Return
+ scoped capability accumulation
+ sustainable operation
+ zero blocking boundary violations
```

This dual requirement—value and conformance—protects Lite from becoming either a safe but irrelevant system or a popular but unsafe automation layer.
