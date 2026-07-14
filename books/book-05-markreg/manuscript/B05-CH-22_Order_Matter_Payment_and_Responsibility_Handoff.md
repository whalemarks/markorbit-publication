# B05-CH-22 — Order, Matter, Payment and Responsibility Handoff

**Status:** Part III Draft  
**Chapter Map:** B05-TOC-V0.1  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

Part II produced strategy and scope candidates.

Part III has now produced a Proposal, Price Model, Quote, Acceptance, Commercial Instruction, Formal Intake, document states, and Readiness Assessment.

The Product must now hand the journey into formal business and execution contexts.

The central progression is:

```text
Accepted Commercial Scope
+ Commercial Instruction
+ Sufficient Formal Intake
+ Required Readiness
→ Formal Object Creation Requests
→ Order Reference
→ Matter Reference
→ Payment Context
→ Responsibility Assignment
→ Execution Context
```

```text
Order
≠ Matter
≠ Payment
≠ Responsibility
≠ Workflow
≠ Filing Approval
≠ Submission
```

---

## 1. Formal Objects Are Created by Owning Services

MarkReg may prepare requests and required data.

The appropriate Owning Service creates and records:

- Order;
- Matter;
- payment request or financial record;
- responsibility assignment;
- formal Document;
- Execution Context where applicable.

MarkReg retains references and Product projections.

---

## 2. Product Journey State Must Not Become Formal State by Renaming

A Product-local state such as `Ready to Start` does not become an Order merely because its label changes.

Formalization requires defined authority, validated input, identity, source, creation event, stable identifier, and policy compliance.

---

## 3. Order Represents Commercial Commitment

An Order may define:

- customer;
- service;
- accepted scope;
- price;
- currency;
- tax;
- payment terms;
- commercial owner;
- effective time;
- cancellation;
- amendments;
- related proposal and Quote.

The Order should not be used as the professional Matter record by default.

---

## 4. Matter Represents Professional Work Context

A Matter may define:

- client;
- applicant or right holder;
- service type;
- jurisdiction;
- filing unit or right;
- professional scope;
- responsible team;
- confidentiality;
- deadlines;
- related Documents and Evidence;
- related Order.

One Order may create several Matters. One Matter may have several commercial events.

---

## 5. Order-to-Matter Cardinality Must Remain Flexible

Examples:

```text
One Order
→ several country filing Matters

One Order
→ search Matter + filing Matters

One Order
→ renewal Matters for several registrations

One Matter
→ initial filing + later commercial amendments
```

The Product should not assume one-to-one identity.

---

## 6. Scope Must Be Decomposed for Formalization

The handoff should identify service, jurisdiction, route, filing unit, applicant, classes, goods/services, stage, provider need, price allocation, responsibility, and deadline context.

This supports correct Matter and Execution formation.

---

## 7. Commercial and Professional Scope May Differ in Shape

A client may buy a package.

Professional work may require separate Matters by jurisdiction, filing unit, proceeding, right, office action, renewal, or provider.

The Product should preserve the commercial package while allowing professional decomposition.

---

## 8. Payment Is a Separate Formal Context

Payment may involve invoice, receipt, credit, deposit, official-fee advance, refund, write-off, provider payment, reconciliation, and variance.

```text
Quote Amount
≠ Invoice Amount
≠ Amount Due
≠ Amount Received
≠ Amount Reconciled
≠ Amount Remitted
```

---

## 9. Payment Conditions Affect but Do Not Define Professional State

A Matter may exist before payment.

Work may be paused pending payment.

A filing may require official funds before submission.

A credit client may proceed under approved terms.

The Product should represent the organization’s policy without treating every unpaid Matter as invalid.

---

## 10. Payer and Applicant Remain Distinct

The payer may be client, applicant, affiliate, agency, parent company, procurement entity, or finance intermediary.

Payment should reference the correct Order and Matter without changing applicant identity.

---

## 11. Payment Reconciliation Needs Evidence

A payment state may depend on bank reference, transaction identifier, amount, currency, payer, recipient, date, invoice, allocation, fees deducted, refund, and confirmation.

AI may help match. The financial Owning Service records reconciliation.

---

## 12. Responsibility Assignment Must Be Explicit

Responsibilities may include:

- commercial owner;
- professional owner;
- coordinator;
- reviewer;
- approver;
- deadline owner;
- provider manager;
- document owner;
- client decision owner;
- finance owner.

Assignment should identify role, person or organization, authority, start, and scope.

---

## 13. Responsibility Is Not Mere Notification

Adding a person to an email does not assign responsibility.

Responsibility should have accepted role, expected action, due date or trigger, visibility, escalation, transfer rule, and completion evidence.

---

## 14. Professional Accountability Remains with Eligible Humans

MarkReg may route and remind.

It does not become responsible attorney, filing agent, deadline owner, approver, signatory, or provider.

AI may assist but cannot hold professional responsibility.

---

## 15. Execution Context Begins with Governed Inputs

An Execution Context may reference:

- Order;
- Matter;
- Commercial Instruction;
- Formal Intake;
- filing unit;
- approved scope;
- readiness;
- documents;
- deadlines;
- responsibilities;
- provider;
- policy;
- permissions.

Book 03 governs the Execution pattern. MarkReg does not create a parallel Workflow engine.

---

## 16. Formalization Does Not Automatically Start External Action

Order creation may permit work to begin.

Matter creation may permit professional preparation.

Execution Context creation may permit Task formation.

None automatically means provider instructed, official fee paid, filing submitted, Communication sent, or right recorded.

Protected actions require their own gates.

---

## 17. Handoff Needs Idempotency

Repeated Product requests should not create duplicate Orders, Matters, invoices, payment requests, Tasks, provider instructions, or filing submissions.

The request should carry stable references and idempotency controls.

---

## 18. Partial Formalization Must Be Visible

Possible outcomes include:

```text
Order created; Matter pending
Matter created; payment pending
Payment received; reconciliation pending
Responsibility assigned; provider pending
Execution Context created; filing approval pending
Formalization failed; no object created
Unknown result; reconciliation required
```

The Product should not present partial success as complete.

---

## 19. Failure and Retry Must Preserve Trace

A failed handoff should retain request, target service, timestamp, actor, validation, error, retry status, object reference if created, compensation, and reconciliation owner.

Retry should not duplicate formal effects.

---

## 20. Handoff Events Support Product Continuity

MarkReg may consume events such as Order Created, Matter Created, Invoice Issued, Payment Received, Payment Reconciled, Responsibility Assigned, Task Created, Review Requested, Approval Granted, and Provider Selected.

Events update the Product projection without transferring authority to the Product.

---

## 21. Cross-Organization Handoff Preserves Orbit Boundaries

When agency, client, or provider participates:

- each organization retains identity;
- each retains permissions;
- each retains records;
- each accepts responsibility;
- private data remains purpose-limited;
- authority is not transitive.

A sender’s approval does not automatically grant the receiver authority beyond the accepted scope.

---

## 22. Participant Visibility Should Be Purpose-Limited

A client may need accepted scope, commercial status, missing decisions, document requests, payment status, professional stage, official outcome, and next action.

A provider may need appointed scope, filing unit, applicant, specification, documents, deadline, communication route, and relevant payment condition.

Neither should receive unrelated private data.

---

## 23. AI May Support Formalization Preparation

AI may decompose scope, map proposal items to Matters, detect missing references, propose responsibility assignments, reconcile payment references, summarize handoff state, and detect duplicate requests.

AI should not create authority, assign responsibility without governance, reconcile funds as final, approve filing, instruct provider, or submit externally.

---

## 24. Failure Modes to Reject

```text
Product status renamed as Order
Order used as Matter
Payment treated as filing approval
One Order forced into one Matter
Payer treated as applicant
Email copy treated as responsibility assignment
Retry creates duplicate objects
Partial formalization shown as complete
Matter creation sends provider instruction
Execution Context creation submits filing
AI assigned as accountable professional
```

---

## 25. Minimum Formal Handoff Lock

```text
MarkReg prepares formalization requests.

Owning Services create and record
Order, Matter, payment,
responsibility, Document,
and Execution facts.

Commercial scope and professional work
may have different shapes.

Order, Matter, payment,
responsibility, Workflow,
filing approval, provider instruction,
submission, and official outcome remain distinct.

Handoffs are idempotent,
traceable, purpose-limited,
and safe under partial failure.

Humans and organizations remain accountable.
```

---

## 26. Part III Completion

Part III began with strategy candidates.

It now produces a governed commercial and formalization sequence:

```text
Proposal Candidate
→ Price Model
→ Quote
→ Acceptance
→ Commercial Instruction
→ Formal Intake
→ Document and Signature State
→ Readiness Assessment
→ Order and Matter Formation Requests
→ Payment and Responsibility Context
→ Execution Entry Request
```

This sequence is sufficient to support Part IV.

Part IV begins with the filing package as a governed Artifact, professional Review, provider Routing, direct connector and Owning Service boundaries, submission states, failure, retry, Communication, and audit.
