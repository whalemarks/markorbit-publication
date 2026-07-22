# CH24 — External Protected Actions Need Explicit Authority and Idempotent Boundaries

## 1. External action is where internal intent becomes external consequence

MarkOrbit may prepare, analyze, review and approve work internally. An `External Protected Action` begins when the system causes or may cause an effect outside the internal preparation boundary.

Examples include:

- filing with an official office;
- signing or transmitting a declaration;
- sending a binding professional communication;
- appointing or instructing a provider;
- disclosing protected customer information;
- initiating a payment or refund;
- publishing a professional claim;
- contacting a customer under represented authority;
- withdrawing, surrendering or amending a right;
- delivering credentials or certificates.

```text
Prepared Internally
≠ Externally Effective
```

The correct chain is:

```text
Prepared Package
→ Required Review
→ Decision-ready Preview
→ Specific Approval
→ Final Authority Check
→ Idempotent Apply
→ External Return
→ Reconciliation
→ Formal-state Validation
```

## 2. Protected Action is defined by consequence, not interface

A button click may be low risk or highly consequential. An API call may be internal or may create a legally significant external event.

The classification should consider:

- external recipient;
- official or contractual effect;
- funds;
- protected data;
- professional reservation;
- customer relationship;
- reversibility;
- deadline;
- duplicate risk;
- public reach.

```text
Simple Interface
≠ Simple Consequence
```

## 3. Every Protected Action requires an authority chain

The action record should identify:

- initiating requester;
- represented Workplace;
- Delivery Owner;
- Relationship Owner where relevant;
- customer instruction;
- professional qualification;
- provider appointment;
- approver;
- Apply actor or service identity;
- exact payload;
- legal or policy basis.

```text
Technical Ability to Apply
≠ Authority to Apply
```

A service account with access to an official portal must not become a universal source of authority.

## 4. Provider selection, appointment, acceptance and instruction remain separate

The provider lifecycle should preserve:

```text
Provider Candidate
→ Eligibility
→ Recommendation
→ Selection
→ Appointment
→ Provider Acceptance
→ Matter Instruction
→ Provider Action
→ Provider Return
```

Each transition may require different approvals and evidence.

```text
Provider Selected
≠ Provider Appointed
≠ Provider Accepted
≠ Provider Instructed
```

A quotation request does not authorize filing. A provider's willingness to act does not prove customer approval.

## 5. Official submission requires exact payload identity

Before filing or transmitting an official package, the system should bind:

- applicant or owner;
- mark representation;
- goods and classes;
- filing basis;
- declarations;
- evidence;
- signatory;
- provider;
- office;
- fees;
- attachments;
- package version or hash.

```text
Approved Package Hash
= Submitted Package Hash
```

Any material difference requires a new Preview and Approval.

## 6. Idempotency prevents duplicate consequence

A Protected Action should have an idempotency strategy before the first attempt.

The record should include:

- idempotency key;
- business object;
- target system;
- payload hash;
- attempt number;
- prior external reference;
- response;
- timeout state;
- safe-retry rule;
- reconciliation owner.

```text
Same User Intent
≠ Safe to Repeat the External Action
```

Duplicate filings, payments, provider instructions or customer messages can create cost, contradiction and professional harm.

## 7. Technical idempotency is not always enough

Some external systems do not support idempotency keys. Others may accept a request but fail to return the result.

MarkOrbit therefore needs business-level duplicate controls, such as:

- search for official application number;
- provider acknowledgement check;
- payment transaction lookup;
- sent-message verification;
- payload and time-window comparison;
- manual reconciliation;
- duplicate-warning gate.

```text
No Duplicate Response
≠ No Duplicate External Effect
```

## 8. Unknown must block unsafe retry

Possible Apply results include:

```text
Not Attempted
Attempted
Acknowledged
Accepted
Rejected
Partially Applied
Failed Before Effect
Failed After Possible Effect
Unknown
Reconciliation Required
```

When effect is uncertain:

```text
Unknown
→ Preserve Evidence
→ Reconcile
→ Decide Whether Retry Is Safe
```

```text
Timeout
≠ Failure
≠ Permission to Retry
```

## 9. Evidence Contract is part of the action design

Before Apply, the workflow should state what external evidence is required.

### Official filing

- official number;
- filing date;
- office acknowledgement;
- filed representation;
- filed goods;
- fee receipt.

### Provider instruction

- acceptance;
- scope;
- deadline;
- fee;
- conflict confirmation;
- expected return.

### Payment

- recipient;
- transaction reference;
- amount and currency;
- settlement status;
- official or provider receipt;
- refund rule.

### Customer communication

- sender identity;
- recipients;
- attachments;
- delivery evidence;
- response deadline.

```text
External Action Attempted
≠ Evidence Contract Satisfied
```

## 10. External acknowledgement and formal truth are different

```text
Connector Delivered
≠ Office Accepted

Provider Acknowledged
≠ Provider Completed

Payment Gateway Accepted
≠ Funds Settled

Message Delivered
≠ Customer Agreed
```

The Owning Service remains responsible for deciding when returned evidence is sufficient to update the formal business or right state.

## 11. Data disclosure is itself a Protected Action

Before disclosure, the action should identify:

- data fields and files;
- recipient;
- purpose;
- jurisdiction;
- retention;
- onward sharing;
- redaction;
- confidentiality basis;
- model or tool involvement;
- training exclusion;
- deletion or return obligations.

```text
Recipient Needs Some Information
≠ Recipient May Receive the Entire Matter
```

## 12. External communication requires represented-authority clarity

The action record should preserve:

- visible sender;
- represented Workplace;
- professional identity where required;
- Relationship Owner;
- recipients;
- binding claims;
- requested commitment;
- deadline language;
- attachments;
- approval version.

```text
Message Draft Approved
≠ Any Actor May Send It
```

## 13. Funds action needs a separate authority path

A payment-related Protected Action should verify:

- customer-approved scope;
- authorized amount;
- recipient identity;
- official versus Provider fee;
- currency;
- exchange-rate rule;
- refundability;
- payment method;
- settlement evidence;
- custody boundary.

```text
Provider Requests Payment
≠ Customer Approved Payment

Payment Orchestration
≠ Payment Custody
```

This manuscript does not authorize MarkOrbit to act as escrow, money transmitter or pooled custodian.

## 14. AI execution remains bounded by the same controls

In M4 or M5, AI may invoke a tool only where the policy explicitly permits the action.

The policy should define:

- Capability;
- tool;
- target;
- payload class;
- R-tier;
- Approval requirement;
- cost ceiling;
- data limit;
- idempotency;
- stop condition;
- human escalation;
- evidence.

```text
AI Has Tool Access
≠ AI Has Protected-action Authority
```

At R4, the qualified actor remains identifiable even where AI prepares or technically transmits the package.

## 15. Emergency action remains explicit

A deadline emergency may justify a pre-authorized protective route, but the route must be defined in advance or approved by a valid emergency authority.

It should state:

- trigger;
- allowed action;
- maximum cost;
- scope limit;
- required professional authority;
- customer notification;
- post-action Review;
- recovery route;
- expiry.

```text
Deadline Pressure
≠ Unbounded Emergency Authority
```

## 16. Cancellation before and after external effect are different

Before Apply, cancellation may revoke future authority.

After Apply, the system must determine whether the action took effect.

Possible recovery actions include:

- recall provider instruction;
- stop or reverse payment;
- withdraw submission;
- correct official record;
- send clarification;
- replace provider;
- notify customer;
- request refund;
- reconcile status.

```text
Cancellation Requested
≠ External Effect Cancelled
```

## 17. Protected Action permissions must expire

Authority may expire because:

- Approval expired;
- package changed;
- provider changed;
- professional qualification changed;
- deadline passed;
- fee increased;
- customer withdrew instruction;
- conflict appeared;
- risk tier changed.

The Apply service should recheck authority immediately before action.

## 18. Manual actions need the same evidence as connectors

A human logging into a portal or sending an email manually does not remove governance requirements.

The system should capture:

- actor;
- time;
- exact package;
- target;
- result;
- screenshot or receipt where appropriate;
- external reference;
- Unknown and reconciliation state.

```text
Manual
≠ Untracked
```

## 19. Public publication can be a Protected Action

Publishing legal requirements, deadlines, fees or professional claims may influence many users before a Matter exists.

Publication may therefore require:

- source verification;
- professional Review;
- versioned Preview;
- publication Approval;
- rollback capability;
- derivative-content tracking;
- correction workflow.

```text
Content Published
≠ Claim Permanently Valid
```

## 20. Audit must reconstruct the full external-action chain

For each Protected Action, the system should be able to answer:

- What was intended?
- Which object and version were used?
- Who reviewed it?
- Who approved it?
- What authority did they hold?
- What payload was applied?
- Which system or recipient received it?
- What evidence returned?
- Was the result Unknown?
- Was retry safe?
- Which formal state was later updated?

## 21. The governing principle

External Protected Actions are the final boundary between intelligence and consequence.

```text
Explicit Authority
+ Exact Payload
+ Idempotent Boundary
+ Evidence Contract
+ Reconciliation
= Governed External Execution
```

MarkOrbit should make this boundary efficient, but never invisible.