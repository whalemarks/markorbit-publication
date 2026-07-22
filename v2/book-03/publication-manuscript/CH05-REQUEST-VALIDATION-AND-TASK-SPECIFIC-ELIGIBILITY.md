# CH05 — Request Validation and Task-specific Eligibility

## 1. A request is not ready merely because it is understandable

A Capability Request may be clearly written and still be unsafe, unauthorized or impossible to fulfil.

Execution therefore separates:

```text
Request understood
≠ Request valid
≠ Performer eligible
≠ Work assigned
≠ Action authorized
```

Validation asks whether the requested work may enter the execution system at all. Eligibility asks who or what may perform it under the current context.

These are different decisions.

## 2. Validation protects the system before work begins

A valid request should identify, at minimum:

- the requested Capability and version;
- the represented Workplace;
- the Product Installation or source channel;
- the purpose and expected Outcome;
- the objects and data involved;
- the jurisdiction and procedural context where relevant;
- the requested deadline;
- the allowed implementation classes;
- the required Review policy;
- the applicable authority and entitlement;
- the expected Evidence Return;
- the cancellation and expiry conditions.

Validation is not a clerical form check. It is the first substantive governance gate.

```text
Syntactically complete
≠ Operationally valid
≠ Professionally safe
```

## 3. Validation has several independent dimensions

### 3.1 Identity and representation

Execution must know:

- who made the request;
- whether that Person acts for themselves or represents a Workplace;
- whether the represented role is current;
- whether the Person may request this Capability;
- whether the request concerns a Customer, Matter or internal object they may access.

A person may be a valid member of one Workplace but unauthorized to request work for another.

### 3.2 Object and version validity

The request must reference the correct objects and versions.

Examples include:

- the current Applicant record;
- the exact Mark version;
- the correct Goods set;
- the latest Office Action;
- the approved Listing version;
- the current Provider quotation;
- the exact document package to be reviewed.

```text
Correct object type
+ Wrong object version
= Invalid execution basis
```

### 3.3 Purpose validity

The same data may be used for one purpose and prohibited for another.

A customer email may be available for matter communication but not for marketing. A trademark image may be available for internal review but not public promotion. A confidential case may support delivery but not training.

Validation must therefore bind data access to purpose.

```text
Data visible
≠ Data reusable for every purpose
```

### 3.4 Capability availability

The requested Capability must exist in the relevant Product Installation and be enabled for the Workplace.

A Product may expose a user interface for a future Capability without the current Workplace having:

- an implementation binding;
- an eligible professional route;
- a current source pack;
- a reviewer;
- a safe external connector;
- the legal basis for production use.

The correct result may be:

```text
Capability described
but not currently executable
```

### 3.5 Authority and entitlement

The requester must have authority to initiate the requested class of work.

Execution must distinguish:

- entitlement to request a draft;
- entitlement to request professional review;
- entitlement to incur cost;
- entitlement to appoint a Provider;
- entitlement to communicate externally;
- entitlement to approve an Apply action;
- entitlement to mutate formal state.

```text
Subscription access
≠ Authority to bind a Workplace
```

### 3.6 Input sufficiency

Validation asks whether the minimum inputs exist to begin the requested stage.

This does not mean all final inputs must already be complete. A request may be valid for clarification, triage or preliminary review while not being valid for filing or final approval.

The system should distinguish:

```text
Valid for triage
Valid for preparation
Valid for professional review
Valid for approval
Valid for Apply
```

### 3.7 Risk and review policy

The request must be assigned an initial risk class and corresponding Review requirement.

If risk cannot yet be determined, the request should not silently default to low risk.

Possible states include:

```text
Risk known
Risk candidate
Risk disputed
Risk unknown — classification required
```

### 3.8 Deadline feasibility

A request may be valid in substance but impossible within the requested time.

Execution should compare:

- the verified external deadline;
- the internal safety deadline;
- input readiness;
- reviewer capacity;
- Provider response time;
- document courier time;
- required customer decisions;
- known outage or dependency risk.

```text
Requested deadline
≠ Feasible execution deadline
```

## 4. Validation outcomes must be typed

A binary valid/invalid result loses important operational meaning.

Recommended outcomes include:

```text
Validated
Validated with Conditions
Clarification Required
Additional Evidence Required
Professional Classification Required
Commercial Approval Required
Blocked by Authority
Blocked by Data Scope
Blocked by Product Policy
Blocked by Missing Implementation
Expired
Rejected as Prohibited
Duplicate or Potential Duplicate
Reconciliation Required
```

Each result should identify:

- the deciding rule;
- the missing or conflicting item;
- the responsible party;
- the next safe action;
- whether the request may be revised;
- whether any deadline remains active.

## 5. Duplicate detection occurs before execution

A new request may overlap with:

- an existing active request;
- an assigned Work Package;
- a Provider Instruction;
- an external submission attempt;
- a payment attempt;
- an unresolved Unknown state.

The system should not automatically create a second execution path merely because the user clicked twice or a connector retried.

```text
New request received
≠ New work must be created
```

Duplicate analysis should preserve:

- request identity;
- idempotency key;
- prior attempt references;
- object and version;
- external references;
- current reconciliation state.

## 6. Eligibility is task-specific

After validation, Execution determines who or what may perform the work.

Eligibility may consider:

```text
Capability Evidence
Certification
Production Authorization
Professional Qualification
Jurisdiction
Language
Conflict
Capacity
Recent Quality Evidence
Data-access Scope
Security Clearance
Review Availability
Commercial Terms
```

No single factor is sufficient by itself.

```text
Capability
≠ Eligibility

Certification
≠ Eligibility

Professional Qualification
≠ Assignment
```

## 7. Eligibility belongs to the exact Work Package

A person may be eligible to:

- verify a status record;
- normalize goods;
- prepare a draft response;
- review translation;
- assess visual quality.

The same person may not be eligible to:

- give a final legal opinion;
- approve a filing;
- appoint a local lawyer;
- communicate binding instructions;
- execute an External Protected Action.

Eligibility must therefore bind:

- Work Package type;
- jurisdiction;
- complexity;
- risk class;
- expected Outcome;
- supervision level;
- allowed tools;
- allowed data;
- expiry.

## 8. Human eligibility and system eligibility differ

A deterministic tool may be eligible because:

- its input contract is satisfied;
- its version is approved;
- the action is reversible;
- validation tests pass;
- the relevant policy permits automation.

An AI implementation may additionally require:

- an approved model class;
- source grounding;
- memory restrictions;
- disclosure rules;
- output constraints;
- human review.

A Person may require:

- Capability Evidence;
- current authorization;
- conflict clearance;
- capacity;
- confidentiality terms;
- professional qualification.

A Provider Organization may require:

- institutional eligibility;
- jurisdiction authorization;
- conflict acceptance;
- commercial terms;
- evidence-return commitments;
- current availability.

These should not be compressed into one generic `eligible = true` field.

## 9. Current eligibility is perishable

Eligibility can change because:

- a professional licence expires;
- a certification becomes stale;
- a conflict arises;
- capacity is exhausted;
- a reviewer becomes unavailable;
- a security incident occurs;
- a jurisdiction rule changes;
- the Work Package scope expands;
- a deadline becomes infeasible.

```text
Eligible yesterday
≠ Eligible now
```

The system should record the time and evidence of each eligibility decision.

## 10. Eligibility does not assign the work

A valid request may produce several eligible routes.

```text
Validated Request
→ Eligible Candidate Set
→ Route Recommendation
→ Selection
→ Offer or Invocation
→ Acceptance
→ Assignment
```

The highest-ranked candidate is not automatically selected. A selected candidate is not assigned until the relevant acceptance or invocation contract exists.

```text
Eligible
≠ Recommended
≠ Selected
≠ Assigned
≠ Accepted
```

## 11. AI may assist eligibility but cannot invent authority

AI can help:

- compare capability evidence;
- identify missing qualification;
- detect jurisdiction mismatch;
- summarize recent quality history;
- flag possible conflict;
- estimate workload.

AI cannot create:

- professional qualification;
- production authorization;
- customer consent;
- conflict clearance;
- Provider acceptance;
- data-access authority.

```text
AI predicts eligibility
≠ Eligibility granted
```

## 12. Eligibility decisions must be explainable

A useful eligibility explanation should show:

- which mandatory gates passed;
- which evidence was used;
- which scope was evaluated;
- which conditions apply;
- what remains unknown;
- when the decision expires;
- who may override or review it.

A single opaque score cannot support accountable professional work.

```text
92% suitable
≠ Eligible for this task
```

## 13. Rejection is not always a negative capability judgment

A candidate may be ineligible because:

- they lack capacity;
- the deadline is too short;
- the data scope is restricted;
- the conflict status is unresolved;
- the required reviewer is unavailable;
- the Workplace chose another route;
- the commercial terms were not accepted.

The system should avoid turning every non-assignment into a negative performance record.

## 14. Validation and eligibility create the safe start line

The execution system should begin work only when it can answer:

```text
What is being requested?
For whom?
For what purpose?
Using which inputs and versions?
Under which authority?
At what risk?
Who or what may perform it?
What Review is required?
What evidence must return?
```

Without these answers, speed is not automation. It is unmanaged exposure.

## 15. Chapter locks

```text
Request Understood
≠ Request Validated

Request Validated
≠ Performer Eligible

Performer Eligible
≠ Work Assigned

Certification
≠ Production Authorization

Professional Qualification
≠ Customer Authority

Data Access
≠ Purpose Permission

Requested Deadline
≠ Feasible Deadline

AI Eligibility Prediction
≠ Eligibility Granted

Duplicate Request
≠ New Execution Path
```
