# CH12 — Preview Before Apply

## 1. Apply is the boundary where preparation may become consequence

A professional execution system must distinguish between preparing an action and causing the action to occur.

```text
Prepare
≠ Preview
≠ Approve
≠ Apply
≠ External Effect
≠ Formal-state Update
```

`Apply` means invoking the implementation that may produce a consequential effect.

Examples include:

- sending a customer communication;
- appointing a provider;
- transmitting an application;
- paying an official or provider fee;
- disclosing protected information;
- publishing a professional claim;
- changing a formal business object;
- issuing a certificate or credential;
- releasing compensation;
- initiating an official withdrawal or correction.

The stronger the external consequence, the more important it is that the user and responsible authority can inspect a Preview before Apply.

## 2. Preview is a decision object, not a screenshot

A Preview should explain the exact proposed action in a form that an authorized person can understand and decide upon.

It should include:

- action type;
- exact target;
- affected objects;
- package version;
- actor or implementation;
- provider or recipient;
- data to be disclosed;
- cost and currency;
- deadline;
- expected result;
- irreversible or difficult-to-reverse consequences;
- known uncertainty;
- required Review and Approval;
- idempotency boundary;
- expected Return or Evidence Contract;
- recovery route.

```text
Preview
≠ Decorative Confirmation Screen
```

A confirmation modal that says “Are you sure?” without showing the relevant facts does not provide meaningful governance.

## 3. Preview must reflect the exact Apply payload

The Preview and Apply operation must be cryptographically or structurally linked to the same object version.

```text
Previewed Payload
= Applied Payload
```

Where exact identity is required, the system should preserve:

- payload hash;
- object version;
- package identifier;
- selected implementation;
- timestamp;
- Approval relationship.

If the payload changes after Approval, the system must detect the difference.

```text
Preview v1 Approved
+ Payload v2
= Re-preview and Re-approval Required
```

## 4. A Preview should expose material differences

Users should not have to compare entire long documents manually.

The Preview may highlight:

- applicant name changed;
- address reordered or normalized;
- logo image replaced;
- class deleted;
- goods narrowed;
- translation modified;
- legal argument changed;
- provider changed;
- fee increased;
- recipient list expanded;
- attachment changed;
- deadline revised;
- new disclosure added.

The system should show both the current proposed value and the previously reviewed or approved value.

## 5. Preview does not create Approval

A user can inspect a Preview without approving it.

```text
Preview Viewed
≠ Preview Understood
≠ Approval Granted
```

The Approval event must still identify:

- approver;
- authority;
- exact Preview version;
- authorized action;
- conditions;
- time.

## 6. Apply is not always an external action

Some Apply operations mutate an internal formal object rather than an outside system.

Examples include:

- accepting a Contribution;
- updating a formal Matter state after validation;
- granting Production Authorization;
- publishing a Knowledge Object;
- releasing a customer-delivery package;
- recording a verified official status.

These internal mutations still require governance when they create reliance or alter formal truth.

```text
Internal Apply
≠ Low-consequence by Default
```

## 7. External Protected Action requires stronger controls

An `External Protected Action` is an Apply operation that affects an external party, official system, funds, protected data or binding professional position.

Examples include:

- filing with an office;
- sending binding legal communication;
- appointing or instructing a provider;
- moving or holding funds;
- disclosing customer documents;
- signing or submitting a declaration;
- publishing a professional statement;
- contacting a customer under represented authority.

The governing chain is:

```text
Prepared Package
→ Required Review
→ Decision-ready Preview
→ Specific Approval
→ Final Eligibility and Authority Check
→ Idempotent Apply
→ Return
→ Reconciliation
→ Formal-state Validation
```

## 8. Apply authority must be checked at execution time

Authority can change between Approval and Apply.

The system should recheck:

- Approval validity;
- actor authority;
- professional qualification;
- provider appointment;
- Product and Workplace policy;
- data-disclosure permission;
- current deadline;
- cost threshold;
- required funds checkpoint;
- package version;
- conflict status;
- execution mode.

```text
Authorized When Previewed
≠ Authorized When Applied
```

## 9. Idempotency is part of Apply design

Every consequential Apply should have an idempotency or duplicate-safety strategy.

The execution record should preserve:

- idempotency key;
- prior attempts;
- external reference;
- payload hash;
- timestamps;
- response;
- timeout state;
- retry policy;
- reconciliation state.

```text
Retry Request
≠ Permission to Repeat External Effect
```

A second application, payment or customer message can cause real harm even if the first attempt returned no response.

## 10. Unknown is the safe state after ambiguous Apply

An Apply attempt can result in:

```text
Not Attempted
Attempted
Delivered
Accepted
Rejected
Partially Applied
Failed Before Effect
Failed After Possible Effect
Unknown
Reconciliation Required
```

A network timeout does not prove failure.

```text
Timeout
≠ Not Filed
≠ Not Paid
≠ Not Sent
```

When external effect is uncertain, Execution must preserve `Unknown` and begin reconciliation before retry.

## 11. External success is not formal-state truth

A connector may return HTTP success. A provider may confirm completion. A payment gateway may show processing.

These are different evidence layers.

```text
HTTP Success
≠ Legal Success

Connector Delivered
≠ Office Accepted

Provider Reports Filed
≠ Official Filing Verified

Payment Initiated
≠ Funds Settled
```

The applicable Owning Service determines when evidence is sufficient to update the formal record.

## 12. Apply requires an Evidence Contract

Before Apply, the workflow should specify what result must return.

Examples:

### Filing

- official application number;
- filing date;
- filed mark;
- filed goods and classes;
- official receipt;
- fee evidence.

### Customer communication

- sent-message evidence;
- recipient list;
- attachments;
- delivery status;
- response deadline.

### Provider appointment

- acceptance;
- scope;
- fee;
- deadline;
- conflict confirmation;
- document requirement;
- Evidence Return commitment.

### Payment

- recipient;
- amount;
- currency;
- transaction reference;
- settlement status;
- refund rule.

```text
Apply Attempted
≠ Evidence Contract Satisfied
```

## 13. Funds checkpoints remain separate from professional readiness

A filing may be professionally ready but commercially blocked. It may be paid but professionally incomplete.

```text
Professional Readiness
≠ Funds Readiness
≠ Apply Authority
```

The Preview should disclose:

- customer payment status;
- provider prepayment requirement;
- official fee estimate;
- authorized maximum;
- exchange-rate exposure;
- refundability;
- who receives funds.

Payment orchestration does not grant payment custody.

```text
Payment Orchestration
≠ Permission to Hold or Move Funds
```

## 14. Data disclosure must be previewed

Before sending data to an AI provider, external professional, partner Workplace or public surface, Preview should identify:

- data fields;
- documents;
- recipient;
- purpose;
- retention;
- jurisdiction;
- onward-sharing rule;
- redactions;
- legal or contractual basis.

```text
Data Needed for Work
≠ Unlimited Disclosure Authorized
```

## 15. Communication Apply needs represented-role clarity

A message may be technically sent by MarkOrbit infrastructure while representing a Workplace, professional provider or customer service team.

The Preview should show:

- visible sender;
- represented organization;
- professional identity where required;
- Relationship Owner;
- recipients;
- subject;
- attachments;
- claims and requests;
- deadline language;
- whether the message is binding.

```text
Draft Approved
≠ Permission for Any Actor to Send It
```

## 16. Provider appointment is a protected transition

Provider recommendation, selection, appointment, acceptance and instruction are separate.

```text
Provider Recommended
≠ Provider Selected
≠ Provider Appointed
≠ Provider Accepted
≠ Provider Instructed
```

The appointment Preview should include:

- provider identity;
- qualification and jurisdiction;
- scope;
- professional authority;
- conflict status;
- fee;
- documents to disclose;
- deadline;
- expected evidence;
- replacement and cancellation rules.

## 17. AI execution must remain mode-bound

In M0–M5 collaboration, Apply rights vary.

A simplified pattern is:

```text
M0 — human-only
M1 — AI reference
M2 — AI assist
M3 — AI draft, human approve
M4 — AI execute under explicit governance
M5 — hybrid professional network
```

M4 does not mean unrestricted autonomy. It requires:

- bounded Capability;
- exact policy;
- allowed action set;
- risk tier;
- Approval rule;
- idempotency;
- logging;
- stop conditions;
- human escalation;
- evidence.

```text
AI Can Use Tool
≠ AI May Perform Every Tool Action
```

## 18. Preview must support refusal and alternative routes

A good Preview does not manipulate the approver toward one action. It should allow:

- approve;
- reject;
- request revision;
- choose alternative route;
- reduce scope;
- change provider;
- delay;
- escalate;
- cancel.

Where no safe route exists, the Preview should say so.

## 19. Cancellation after Apply becomes recovery

Before Apply, cancellation may simply terminate future authority.

After Apply, the system must determine whether external effect occurred.

Possible recovery routes include:

- recall instruction;
- stop payment;
- withdraw filing;
- correct record;
- send clarification;
- replace provider;
- request refund;
- notify customer;
- reconcile official state.

```text
Cancel Clicked
≠ External Effect Cancelled
```

## 20. Simulation must prevent accidental Apply

Simulation Workplace and assessment environments must enforce:

- synthetic or isolated objects;
- no live provider instruction;
- no official submission;
- no real payment;
- no real customer communication;
- clear simulation indicators;
- blocked production credentials;
- separate event streams.

```text
Simulation Approval
≠ Production Approval
```

## 21. Observability is required around Apply

For each Apply attempt, the audit trail should reconstruct:

- request;
- package;
- Review;
- Preview;
- Approval;
- actor;
- implementation;
- payload;
- target;
- attempt;
- response;
- external reference;
- retry or reconciliation;
- final validated result.

Without this chain, the system cannot explain what happened when a customer, provider, regulator or auditor asks.

## 22. The governing principle

Preview before Apply creates a deliberate boundary between intelligence and consequence.

```text
Understand
→ Prepare
→ Review
→ Preview
→ Approve
→ Apply
→ Validate
```

MarkOrbit should make preparation fast, assistance intelligent and execution efficient. But it must make consequential action specific, visible, attributable and recoverable.