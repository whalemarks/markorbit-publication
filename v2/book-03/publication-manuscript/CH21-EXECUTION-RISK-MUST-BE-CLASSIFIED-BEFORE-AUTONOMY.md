# CH21 — Execution Risk Must Be Classified Before Autonomy

## 1. Autonomy is a consequence of risk governance, not a product preference

A professional execution system should not begin with the question:

> How much can AI or automation do?

It should begin with:

> What can go wrong, who may be harmed, how reversible is the action, and which authority is required?

Only after those questions are answered should the system decide whether work may be handled by deterministic software, AI, a human performer, a professional provider or a hybrid route.

```text
Risk Classification
→ Review Tier
→ Human–AI Mode
→ Approval Requirement
→ Apply Boundary
→ Recovery Design
```

The governing principle is:

```text
Autonomy
= bounded permission under a known risk profile
```

It is not:

```text
Autonomy
= model confidence
= technical capability
= user convenience
= commercial pressure
```

## 2. Execution risk is broader than legal risk

A trademark workflow may fail even when the legal conclusion is correct.

Relevant risk dimensions include:

- professional or legal risk;
- customer-decision risk;
- identity and authority risk;
- deadline risk;
- financial risk;
- data and confidentiality risk;
- external-communication risk;
- provider risk;
- duplicate-action risk;
- official-state risk;
- relationship risk;
- operational recovery risk;
- public-content risk;
- AI reliability risk.

```text
Professionally Correct
≠ Operationally Safe
```

A correct filing strategy can still be unsafe if the wrong applicant is used, the wrong provider is instructed, customer authority is missing or a duplicate filing is triggered after a timeout.

## 3. Risk classification attaches to the proposed transition

Risk should not be assigned only to a Product, user or broad service category.

The same Capability can have different risk depending on the requested transition.

Examples:

```text
Extract an address from a document
≠ Replace the formal applicant address

Draft a customer email
≠ Send the email under represented authority

Calculate an estimated fee
≠ Approve and pay the fee

Recommend a provider
≠ Appoint and instruct the provider
```

Risk classification therefore belongs to the exact Capability Request, Work Package, Review or Apply transition.

## 4. Consequence severity must be explicit

A risk record should estimate the consequence of an incorrect or unauthorized action.

Possible consequence classes include:

```text
Informational inconvenience
Internal rework
Customer confusion
Additional cost
Missed opportunity
Loss of filing or priority right
Disclosure of protected information
Binding professional position
Official record corruption
Irreversible external action
Regulatory or professional breach
```

A short action can have a severe consequence.

```text
Small Payload
≠ Small Consequence
```

## 5. Reversibility changes the control design

The system should distinguish:

```text
Fully Reversible
Reversible with Internal Correction
Reversible through External Request
Reversible with Cost or Delay
Partially Reversible
Practically Irreversible
Legally Irreversible
Unknown Reversibility
```

Examples:

- an internal draft can normally be replaced;
- a customer message may require correction but cannot be unsent;
- a provider instruction may be recalled only before action;
- a filing may require withdrawal, amendment or a new application;
- a missed statutory deadline may not be recoverable.

```text
Can Be Corrected
≠ No Harm Occurred
```

## 6. Uncertainty is a risk multiplier

Unknown should increase, not decrease, governance.

Risk multipliers include:

- missing official source;
- conflicting Provider practice;
- unverified customer fact;
- low-confidence extraction;
- unfamiliar jurisdiction;
- ambiguous customer instruction;
- external timeout;
- changed fee schedule;
- uncertain professional qualification;
- incomplete evidence.

Possible responses include:

```text
Request Clarification
Require Additional Source
Increase Review Tier
Reduce AI Autonomy
Block Apply
Require Professional Authority
Enter Reconciliation
```

```text
Unknown
≠ Permission to Use the Most Convenient Assumption
```

## 7. Source quality affects execution risk

A deterministic system can apply an incorrect source perfectly.

The source dimension should identify:

- official rule;
- official fee table;
- official status;
- authoritative professional source;
- Provider-reported practice;
- customer-provided fact;
- internal historical observation;
- AI inference;
- unknown.

```text
Deterministic Execution
≠ Authoritative Basis
```

Stale or weak sources can increase the Review and Approval requirements even when the operation itself is simple.

## 8. Identity and authority errors receive special treatment

Professional work frequently depends on who the customer, applicant, right owner, signatory, provider and approver actually are.

Risk classification should examine:

- identity confidence;
- represented role;
- customer relationship;
- engagement authority;
- signature authority;
- professional appointment;
- approval authority;
- formal-record consistency.

```text
Known Name
≠ Verified Identity
≠ Authorized Role
```

An identity or authority defect should block high-impact Apply even when all other fields are complete.

## 9. Deadline risk is not just time remaining

Deadline risk should consider:

- source and trigger event;
- jurisdiction;
- ordinary deadline;
- extension or grace period;
- time zone;
- document preparation time;
- customer response time;
- provider acceptance time;
- payment time;
- official system availability;
- recovery alternatives.

```text
Deadline Date Known
≠ Deadline Operationally Safe
```

A matter with ten days remaining may be higher risk than one with three days remaining if original documents or local appointment are still unresolved.

## 10. Financial risk includes more than price

Relevant factors include:

- official fees;
- Provider fees;
- taxes and remittance;
- exchange-rate exposure;
- refundable and non-refundable amounts;
- duplicate payment risk;
- customer approval threshold;
- prepayment requirement;
- payment recipient verification;
- reconciliation and refund route.

```text
Amount Within Budget
≠ Funds Action Authorized
```

## 11. Data risk follows purpose and disclosure

Risk classification must account for:

- data sensitivity;
- customer confidentiality;
- privileged or professional information;
- recipient;
- jurisdiction;
- retention;
- onward sharing;
- model or tool provider;
- redaction;
- training exclusion;
- customer-contact impact.

```text
Data Accessible
≠ Data Safe to Disclose
```

## 12. External communication risk is role-sensitive

The same text can have different risk depending on who sends it and under whose authority.

The system should assess:

- represented Workplace;
- Relationship Owner;
- professional identity;
- recipient;
- binding language;
- deadline statement;
- legal position;
- requested commitment;
- attachments;
- possibility of customer confusion.

```text
Correct Draft
≠ Safe Sender
```

## 13. Provider risk is independent of recommendation quality

Provider-related risk includes:

- current eligibility;
- professional qualification;
- conflict;
- capacity;
- deadline reliability;
- evidence-return reliability;
- fee certainty;
- data handling;
- customer-contact behavior;
- replacement route;
- silence history.

```text
Provider Recommended
≠ Provider Safe for This Matter
```

## 14. AI risk is Capability-specific

AI risk should not be expressed only as a general model score.

It depends on:

- Capability;
- model and version;
- source grounding;
- tool access;
- M0–M5 mode;
- input sensitivity;
- output type;
- Review availability;
- consequence;
- reversibility;
- stop conditions;
- recent evaluation evidence.

```text
High Model Benchmark
≠ Low Execution Risk
```

## 15. Risk classification must be explainable

A Risk Record should identify:

- proposed transition;
- consequence severity;
- reversibility;
- uncertainty;
- source quality;
- identity and authority status;
- deadline exposure;
- financial exposure;
- data exposure;
- external effect;
- required professional qualification;
- selected R-tier;
- selected M-mode;
- required Approval;
- required Evidence Contract;
- recovery route.

Users and reviewers should understand why a particular control is required.

## 16. Risk classification can change during work

New facts can raise or lower risk.

Examples:

- official status is verified;
- original POA is found;
- fee increases;
- provider loses availability;
- customer changes applicant;
- AI source conflict appears;
- external system times out;
- deadline becomes urgent.

```text
Risk Classified at Intake
≠ Risk Fixed for the Entire Workflow
```

The system should reclassify before Review, Approval and Apply when material facts change.

## 17. Commercial pressure cannot lower the risk tier silently

A lower-cost or faster route may be legitimate, but it must not erase required controls.

```text
Customer Wants Fastest Route
≠ Review Waived

High Conversion Opportunity
≠ Lower Professional Risk
```

Any exception should be explicit, authorized and limited by non-waivable professional requirements.

## 18. Risk classification should support safe simplification

The purpose of classification is not to maximize bureaucracy.

When risk is low, inputs are structured, sources are current and actions are reversible, the system may safely use:

- deterministic validation;
- sampling;
- M2 assistance;
- bounded M4 execution;
- simplified Approval;
- automated evidence capture.

```text
Governed Low Risk
→ Faster Execution
```

## 19. The governing chain

```text
Proposed Transition
→ Risk Classification
→ R-tier
→ M-mode
→ Review and Approval Requirements
→ Apply Boundary
→ Evidence and Recovery
```

Autonomy should expand only where MarkOrbit can explain the risk, prove the authority, detect failure and recover from ambiguity.