# B03-CH-22 — Renewal Preparation Pattern

**Status:** Release Candidate 1

## Chapter Purpose

The Renewal Preparation Pattern organizes Trademark lifecycle facts, jurisdiction context, owner information, Documents, Evidence, commercial scope and review questions without certifying renewal eligibility, executing payment or filing an official renewal.

Renewal work appears repetitive, but the consequences of an incorrect assumption are significant.

A renewal may depend on:

- current Trademark status;
- jurisdiction;
- registration and expiry records;
- ordinary renewal window;
- grace period;
- current owner;
- covered goods and services;
- use or other Evidence;
- authority Documents;
- changes that must be recorded;
- fees and provider scope;
- professional confirmation;
- official submission and acknowledgment.

The pattern answers:

```text
Which Trademark and jurisdiction are in scope?
What date and status sources are available?
Is a renewal window merely present or professionally confirmed?
Does a grace-period signal exist?
Which owner, goods/services, Documents and Evidence require review?
What Matter and Order scope applies?
Which reminders, Tasks or provider instructions may be outlined?
Why must current MVP execution stop at preview?
What remains forbidden before payment or official filing?
```

The governing path is:

```text
Trademark lifecycle signal
→ source and reference validation
→ renewal-window context
→ owner and scope verification package
→ Document / Evidence gap analysis
→ Matter / Order / provider context
→ Human Review requirement
→ safe preview result
→ stop before apply, payment or filing
```

---

## 1. Dependency Baseline

This chapter applies:

- [Chapter 09 — Execution Object and State Model](B03-CH-09_Execution_Object_and_State_Model.md)
- [Chapter 10 — Workflow Coordination Model](B03-CH-10_Workflow_Coordination_Model.md)
- [Chapter 11 — Task Lifecycle Model](B03-CH-11_Task_Lifecycle_Model.md)
- [Chapter 12 — Review and Approval Lifecycle](B03-CH-12_Review_and_Approval_Lifecycle.md)
- [Chapter 13 — Communication Execution Boundary](B03-CH-13_Communication_Execution_Boundary.md)
- [Chapter 14 — Event Trace, Audit and Replay](B03-CH-14_Event_Trace_Audit_and_Replay.md)
- [Chapter 15 — Permission and Policy Gates](B03-CH-15_Permission_and_Policy_Gates.md)
- [Chapter 16 — Human–AI Execution Handoff](B03-CH-16_Human_AI_Execution_Handoff.md)
- [Chapter 19 — Communication Review Pattern](B03-CH-19_Communication_Review_Pattern.md)
- [Chapter 20 — Provider Routing Preparation Pattern](B03-CH-20_Provider_Routing_Preparation_Pattern.md)
- [Chapter 21 — Office Action Response Preparation Pattern](B03-CH-21_Office_Action_Response_Preparation_Pattern.md)

Its primary Book 02 sources are:

- [Renewal Workflow](../../book-02-core-specification/core-specs/workflows/renewal-workflow.md)
- [Renewal Workflow Contract](../../book-02-core-specification/core-specs/contracts/workflows/renewal-workflow-contract.md)
- [Workflow Specifications Index](../../book-02-core-specification/core-specs/workflows/index.md)
- [Workflow Contract Index](../../book-02-core-specification/core-specs/contracts/workflows/index.md)
- [Trademark API Contract](../../book-02-core-specification/core-specs/contracts/api/trademark-api-contract.md)
- [Jurisdiction API Contract](../../book-02-core-specification/core-specs/contracts/api/jurisdiction-api-contract.md)
- [Knowledge API Contract](../../book-02-core-specification/core-specs/contracts/api/knowledge-api-contract.md)
- [Customer API Contract](../../book-02-core-specification/core-specs/contracts/api/customer-api-contract.md)
- [Matter API Contract](../../book-02-core-specification/core-specs/contracts/api/matter-api-contract.md)
- [Order API Contract](../../book-02-core-specification/core-specs/contracts/api/order-api-contract.md)
- [Document API Contract](../../book-02-core-specification/core-specs/contracts/api/document-api-contract.md)
- [Evidence API Contract](../../book-02-core-specification/core-specs/contracts/api/evidence-api-contract.md)
- [Task API Contract](../../book-02-core-specification/core-specs/contracts/api/task-api-contract.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [AI Context Contract](../../book-02-core-specification/core-specs/contracts/common/ai-context.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)

Book 02 owns the Workflow, contract, Trademark lifecycle state, related Services, controlled values and implementation depth.

### 1.1 Current Depth Rule

The current Renewal Workflow is:

```text
Stub Now
Level 1/2
Preview / Validation Stub
Apply not production-enabled
```

The broader Renewal Workflow Contract describes future governed capabilities. It does not enable them in the current MVP.

This chapter uses the stricter current rule:

```text
Preview may organize renewal preparation.
Apply remains disabled and side-effect free.
No renewal, payment, provider engagement, Communication or Event is created.
```

---

## 2. Pattern Position

Renewal preparation begins after a governed Trademark record or lifecycle signal exists.

The signal may come from:

- visible registration and expiry data;
- an authorized user request;
- an imported portfolio record;
- a professional status review;
- an official notice;
- an existing Matter or Order;
- a scheduled internal review;
- a customer Communication;
- a prior service-provider report.

A signal may start evaluation.

It does not certify:

- current registration status;
- renewal eligibility;
- ordinary deadline;
- grace period;
- owner;
- goods and services;
- Evidence requirement;
- official fee;
- provider authority.

Current outputs may include:

- reference validation;
- renewal-window indicators;
- deadline-present but not-certified status;
- missing renewal fields;
- owner and scope gaps;
- Document and Evidence gaps;
- Matter and Order mismatch;
- Task plan preview;
- reminder or instruction outline;
- Human Review requirement;
- safe errors.

---

## 3. Renewal Boundary

The following stages must remain distinct.

| Stage | Meaning |
|---|---|
| Lifecycle signal | A record suggests renewal attention may be needed |
| Candidate identification | A Trademark may be within a renewal-related period |
| Source verification | Relevant official and Core sources are checked |
| Deadline context | Date inputs and possible windows are organized |
| Eligibility review | A professional evaluates whether and how renewal may proceed |
| Owner/scope review | Current holder and covered rights are confirmed |
| Document/Evidence preparation | Required sources are assembled |
| Commercial approval | Scope, fees and authority are approved |
| Filing authorization | A protected decision permits a specific submission |
| Payment execution | A separate financial action occurs |
| Official filing | Renewal is submitted externally |
| Official acknowledgment | Receipt or result is verified |
| Trademark update | Trademark Service records supported lifecycle facts |

The current MVP stops before eligibility review becomes a final conclusion and before any apply effect.

### 3.1 Candidate Is Not Eligible

A Trademark may appear due based on imported or internal data while:

- status changed;
- renewal already occurred;
- the record is duplicated;
- the jurisdiction differs;
- the registration number is wrong;
- the right expired;
- an extension or grace period applies;
- ownership changed;
- a required maintenance action is not a simple renewal.

### 3.2 Eligible Is Not Authorized

Even a professionally eligible renewal still needs:

- customer instruction;
- scope confirmation;
- provider or filing route;
- fee approval;
- Documents;
- Evidence where applicable;
- filing authorization.

### 3.3 Submitted Is Not Renewed

An official submission does not prove:

- office acceptance;
- fee acceptance;
- defect-free filing;
- renewal registration;
- updated expiry date.

The system must record only supported external results.

---

## 4. Trademark and Jurisdiction Source Package

The preview should identify, where available:

- Trademark reference;
- registration number;
- jurisdiction reference;
- current visible status;
- registration date;
- expiry date;
- renewal-window source;
- grace-period source;
- owner or holder source;
- covered classes and goods/services;
- prior maintenance records;
- official status source;
- source retrieval time;
- Knowledge source and version;
- conflicts or missing fields;
- Policy omissions;
- AI involvement.

### 4.1 Core State and External Status

A Core Trademark record is an internal governed fact.

An external office record is a source requiring governed retrieval and interpretation.

Neither should silently overwrite the other.

A mismatch should produce review, not automatic correction.

### 4.2 Knowledge Source Freshness

Jurisdiction renewal rules may change.

Knowledge preparation should preserve:

- jurisdiction;
- effective date;
- source authority;
- version;
- retrieval date;
- applicability;
- known limitations;
- reviewer status.

AI must not treat an undated rule summary as current authority.

---

## 5. Renewal Window and Deadline Context

Deadline preparation must distinguish:

| Element | Meaning |
|---|---|
| Registration date present | A source contains a registration date |
| Expiry date present | A source contains an expiry date |
| Renewal-window signal | A candidate window can be displayed |
| Grace-period signal | A candidate late window may exist |
| Calculated candidate | A provisional calculation was made |
| Professional confirmation | An authorized human confirmed the relevant dates and rules |
| Official acknowledgment | An office confirmed a filing or renewal result |

### 5.1 Deadline Present Is Not Certified

The preview should keep:

```text
deadline_present = true or false
deadline_certified = false
renewal_readiness_certified = false
```

until the owning contract and Human Review support a professional conclusion.

### 5.2 Grace Period Is Not Ordinary Renewal

A grace period may involve:

- additional fees;
- narrower timing;
- different documents;
- risk;
- provider confirmation;
- office-specific calculation.

The pattern must not present a grace-period signal as equivalent to an ordinary renewal window.

### 5.3 Conflicting Dates

Possible conflicts include:

- internal expiry date versus official record;
- registration date versus renewal certificate;
- direct national versus international registration data;
- office time zone;
- prior renewal not reflected internally;
- status change after retrieval.

The result should state the conflict and require professional confirmation.

### 5.4 Reminder Does Not Create Deadline Truth

A reminder, Task or Notification can support attention.

It does not establish or change the legal deadline.

---

## 6. Owner and Authority Review

Renewal preparation must identify:

- current recorded holder;
- customer relationship;
- requesting contact;
- possible ownership change;
- name or address differences;
- representative authority;
- required Power of Attorney or authorization;
- pending assignment or recordal;
- source and version.

### 6.1 Customer Is Not Necessarily Owner

The Customer may be:

- the owner;
- an agency;
- a parent company;
- a representative;
- a payer;
- another authorized party.

The preview must not infer ownership from customer or payment context.

### 6.2 Ownership Mismatch

A mismatch may require:

- clarification;
- ownership-change review;
- Assignment Preparation Pattern;
- additional Documents;
- provider advice;
- separate official recordal.

The Renewal pattern must not silently update the owner or assume the renewal can proceed unchanged.

### 6.3 Authority Is Action-Specific

An authorization may not cover:

- the current jurisdiction;
- renewal;
- payment;
- provider instruction;
- Evidence declaration;
- ownership change.

Existence of a Document does not prove adequate authority.

---

## 7. Goods and Services Scope

Renewal may involve all or part of the registered scope depending on jurisdiction and instructions.

The preview may organize:

- registered classes;
- registered goods/services;
- deleted or limited items;
- use-related context;
- customer instructions;
- Evidence links;
- unclear or conflicting scope;
- professional review requirement.

It must not decide autonomously:

- what should be retained;
- what must be deleted;
- whether use is sufficient;
- whether a declaration is accurate;
- whether broader or narrower renewal is optimal.

### 7.1 Current Business Is Not Registered Scope

A customer's present catalog may differ from the registration.

Preparation should compare sources without replacing the official scope.

### 7.2 Use Evidence Boundary

Where use Evidence matters, the pattern may identify:

- referenced Evidence;
- source Documents;
- time period;
- linked goods/services;
- missing categories;
- jurisdiction context;
- review requirement.

AI may organize and summarize.

It must not certify legal sufficiency.

---

## 8. Document and Evidence Preparation

Possible Documents include:

- registration certificate;
- renewal certificate;
- official status extract;
- owner identity or company Document;
- Power of Attorney;
- change-of-name or address Document;
- assignment Document;
- filing instruction;
- provider form;
- proof of payment;
- official receipt.

Possible Evidence includes:

- use specimens;
- invoices;
- website captures;
- packaging;
- advertising;
- sales records;
- declarations;
- other jurisdiction-specific sources.

Reference validation does not establish:

- authenticity;
- completeness;
- current validity;
- official acceptability;
- Evidence sufficiency;
- relationship to each retained item.

### 8.1 Document Versus Evidence

A Document can be a source for Evidence, but the Objects remain distinct.

Document Service owns Document behavior.

Evidence Service owns Evidence behavior and use context.

### 8.2 Missing Source Is a Valid Outcome

The preview may identify a missing certificate, authority Document or Evidence category.

It should state:

- why the item may be needed;
- which future decision depends on it;
- who may provide or review it;
- whether an alternative source may exist;
- that no filing occurred.

---

## 9. Matter, Order and Commercial Scope

The preview may resolve:

- renewal Matter;
- requested service;
- jurisdiction;
- class count;
- ordinary versus grace-period scope;
- Evidence work;
- ownership-change work;
- provider work;
- official and service fee context;
- payment status where allowed;
- Order mismatch.

### 9.1 Scope Expansion

A simple renewal request may expand if:

- ownership differs;
- Evidence is required;
- a grace period applies;
- provider involvement is needed;
- multiple registrations are involved;
- change recordal is required;
- commercial terms changed.

The pattern should expose expansion rather than silently amend the Order.

### 9.2 Fee Context

A fee may be:

- estimated;
- quoted;
- current official fee;
- provider fee;
- tax or disbursement;
- grace surcharge;
- approved;
- paid;
- unknown.

These meanings must remain distinct.

### 9.3 Payment Boundary

The Renewal pattern does not:

- approve payment;
- charge a customer;
- pay an office;
- pay a provider;
- infer payment from Order approval.

Payment is a separate protected action.

---

## 10. Preview Behavior

Current MVP preview may:

- validate request shape;
- validate Trademark and jurisdiction references;
- check Permission and Policy;
- identify date and status sources;
- show renewal-window and grace-period signals;
- keep deadlines and readiness uncertified;
- identify owner and scope gaps;
- identify Document and Evidence gaps;
- identify Matter and Order mismatch;
- prepare a renewal-readiness checklist;
- prepare Task plan preview;
- prepare reminder and provider-instruction outlines;
- prepare AI-assisted gap summary;
- require Human Review;
- return safe warnings and errors.

Preview must not:

- mutate Trademark;
- create Matter or Order;
- create Documents or Evidence;
- create active Tasks;
- create Communication;
- create Notification;
- select or engage a provider;
- certify deadlines;
- certify renewal eligibility;
- certify Evidence sufficiency;
- approve payment;
- execute payment;
- file renewal;
- emit Events.

### 10.1 Preview Result Statement

A safe result should state:

```text
This is a renewal-preparation preview.
Date, eligibility, ownership, scope and Evidence conclusions require Human Review.
No payment, provider engagement or renewal filing occurred.
Apply is not production-enabled.
```

---

## 11. Apply Is Disabled in Current MVP

If apply is requested, the Workflow must return a controlled disabled result.

It must be:

- side-effect free;
- version-aware;
- safe under Policy;
- explicit that the operation is unavailable;
- non-retryable as an enabled production action.

It must not:

- open a Matter;
- create or update an Order;
- create Tasks, Communications or Notifications;
- attach Documents or Evidence;
- change Trademark state;
- engage a provider;
- approve or execute payment;
- emit Events;
- file renewal;
- silently return preview while claiming apply.

### 11.1 Future Apply

A later enabled preparation path would still require:

- owning-service behavior;
- supported versions;
- idempotency;
- Permission;
- Policy;
- Human Review;
- Task and Communication Service boundaries;
- provider-routing boundary;
- payment boundary;
- separate official submission;
- Event trace through owning Services.

This chapter does not authorize future enablement.

---

## 12. Task Plan Preview

The preview may prepare planned Tasks such as:

- verify official status;
- confirm renewal and grace-period deadlines;
- confirm owner;
- resolve ownership mismatch;
- review registered scope;
- collect authority Documents;
- collect use Evidence;
- confirm customer instruction;
- confirm commercial scope;
- obtain provider quote;
- prepare reminder;
- prepare filing-instruction package;
- review payment authorization;
- perform final renewal-readiness review.

The Task plan is not active.

The current MVP stub does not create active Tasks.

Task completion would not prove payment, filing or renewal.

---

## 13. Communication and Notification Preparation

The preview may prepare outlines for:

- customer reminder;
- missing-information request;
- Evidence request;
- fee confirmation;
- provider inquiry;
- provider instruction;
- internal escalation.

The outline must identify:

- Trademark;
- jurisdiction;
- date source;
- deadline-not-certified warning where applicable;
- requested action;
- source version;
- review requirement;
- Policy omissions.

No Communication or Notification is created or sent by the current stub.

A future external message requires Communication Review and the owning Service.

### 13.1 Reminder Wording

A reminder must not present a candidate deadline as professionally certified.

The wording should reflect the available source and required confirmation.

---

## 14. AI-Assisted Renewal Preparation

AI may:

- summarize portfolio data;
- identify apparent renewal candidates;
- compare internal and external dates;
- identify owner mismatches;
- organize registered scope;
- summarize Document and Evidence gaps;
- prepare checklists;
- prepare reminder or provider-instruction outlines;
- flag urgency;
- prepare review questions.

AI must not:

- certify status;
- certify deadline or grace period;
- decide renewal eligibility;
- decide retained scope;
- certify use Evidence;
- approve fees;
- approve or execute payment;
- select a provider;
- send reminders or instructions;
- file renewal;
- mutate Trademark state;
- emit Events.

### 14.1 Bulk Candidate Risk

AI may help screen a portfolio.

Bulk screening must preserve:

- source date;
- jurisdiction;
- data quality;
- duplicate risk;
- missing official status;
- uncertainty;
- Policy visibility;
- Human Review.

A bulk candidate list is not a docket of certified deadlines.

### 14.2 Recommendation Boundary

AI may recommend that a record receive priority review.

It may not recommend automatic filing or abandonment as a final decision.

---

## 15. Human Review Gates

Human Review is required for:

- official status;
- renewal deadline;
- grace-period deadline;
- eligibility;
- owner and authority;
- retained scope;
- Evidence sufficiency;
- fee and commercial scope;
- provider instruction;
- payment authorization where applicable;
- filing readiness;
- official submission authorization.

Review should be bound to:

- Trademark;
- jurisdiction;
- source versions;
- relevant dates;
- owner;
- classes and goods/services;
- Documents and Evidence;
- Matter and Order;
- intended downstream action;
- reviewer role;
- current time.

Human Review does not execute payment or file the renewal.

---

## 16. Permission and Policy

Permission may govern:

- Trademark and Customer access;
- renewal preview;
- Document and Evidence access;
- Matter and Order access;
- provider context;
- commercial terms;
- Communication preparation.

Policy may:

- hide Trademark existence;
- redact owner data;
- hide Evidence;
- limit commercial terms;
- restrict cross-organization use;
- restrict AI source use;
- require Human Review;
- downgrade output;
- return NotFound.

Permission does not override Policy.

Human Review does not bypass either.

---

## 17. Trace and Audit

Current preview emits no Events.

Where retained under an owning contract, audit context should preserve:

- actor and organization;
- Trademark and jurisdiction references;
- date and status sources;
- retrieval time;
- renewal-window and grace-period signals;
- deadline-not-certified and readiness-not-certified results;
- owner and scope gaps;
- Document and Evidence references;
- AI involvement;
- Policy omissions;
- required Human Review;
- Workflow version;
- explicit no-side-effect result.

Future owning Services may return Event references as trace.

They do not command filing or prove renewal.

---

## 18. Safe Failure

Controlled outcomes may include:

- validation failure;
- invalid reference;
- Permission denied;
- Policy restricted;
- Human Review required;
- unsupported version;
- invalid state;
- NotFound;
- conflict;
- apply not implemented;
- internal safe error.

Errors must not expose:

- database identifiers;
- restricted Trademark or owner data;
- unconfirmed deadline assumptions;
- Evidence content;
- commercial terms;
- provider relationships;
- Policy internals;
- Permission internals;
- prompts;
- hidden reasoning;
- stack traces.

A safe recovery result may identify:

- missing source;
- conflicting date;
- owner mismatch;
- missing Document or Evidence;
- required professional role;
- safe next question;
- that no payment or filing occurred.

---

## 19. Example — Renewal With Ownership and Evidence Questions

A Trademark record contains:

- registration number;
- jurisdiction;
- expiry-date signal;
- three registered classes;
- Customer reference;
- an owner name differing from the current Customer name;
- no current Power of Attorney;
- Evidence for only part of the goods;
- an Order for ordinary renewal.

### 19.1 Preview

The pattern:

- validates visible references;
- identifies the expiry-date source;
- marks deadline present but not certified;
- identifies a possible owner mismatch;
- identifies missing authority Document;
- separates registered scope from available Evidence;
- flags that Evidence sufficiency requires professional review;
- flags possible Assignment Preparation;
- identifies potential Order expansion;
- prepares Task and reminder outlines;
- requires Human Review.

### 19.2 AI Assistance

AI may:

- compare owner names;
- summarize Evidence coverage;
- list missing Documents;
- prepare questions for the customer;
- organize the review package.

It cannot decide that the owner is the same entity or that Evidence covers all goods.

### 19.3 MVP Stop

Apply remains disabled.

No Matter, Order change, Task, Communication, Notification, provider instruction, payment, Event or renewal filing occurs.

The result says:

```text
Renewal preparation preview complete.
Deadline, ownership, scope, Evidence and commercial readiness require review.
No payment or renewal filing occurred.
```

---

## 20. Pattern Acceptance Checklist

The Renewal Preparation Pattern is correct when:

- [ ] current MVP remains preview-only;
- [ ] apply remains disabled and side-effect free;
- [ ] lifecycle signal, candidate, eligibility, authorization, filing and official renewal remain distinct;
- [ ] Core and external status sources remain separate;
- [ ] source freshness is visible;
- [ ] renewal-window, grace-period and deadline certification remain distinct;
- [ ] reminder dates are not treated as legal truth;
- [ ] Customer and owner remain distinct;
- [ ] owner mismatch triggers review rather than silent correction;
- [ ] registered scope is not replaced by current business data;
- [ ] Evidence organization is not legal sufficiency;
- [ ] Document and Evidence ownership remains separate;
- [ ] Matter and Order expansion remains visible;
- [ ] fee quote, approval and payment remain distinct;
- [ ] Task plan is not active Task;
- [ ] Communication and Notification outlines are not sent;
- [ ] AI output remains non-final;
- [ ] Human Review gates professional conclusions;
- [ ] no provider is selected or engaged;
- [ ] no payment is executed;
- [ ] no renewal is filed;
- [ ] Workflow emits no Events;
- [ ] safe errors protect restricted lifecycle and commercial data.

---

## 21. Product Boundary

Book 04 may present renewal candidates, source dates, window warnings, owner checks, Evidence gaps, fees and review needs. It must show that no deadline was certified, no payment occurred and no renewal was filed.

## 22. Implementation Boundary

This pattern adds no deadline engine, eligibility rule, docketing engine, payment, provider selection, filing connector or autonomous renewal agent. Apply remains disabled under the current Workflow depth.

## 23. Chapter Result

The Renewal Preparation Pattern creates a governed renewal review package without creating renewal authority.

```text
Treat lifecycle data as sourced context.
Keep window signals separate from certified deadlines.
Verify owner and scope without silent correction.
Organize Documents and Evidence without certifying sufficiency.
Expose Matter, Order, fee and provider gaps.
Require Human Review.
Keep apply disabled.
Do not pay, file, send, mutate or emit.
```

The pattern succeeds when renewal risk becomes visible early while official and professional truth remains with the proper sources and reviewers.

The next chapter defines the **Assignment Preparation Pattern**, where current ownership, proposed parties, transaction authority, chain of title, Documents, signatures, jurisdiction requirements and official recordal must remain distinct.
