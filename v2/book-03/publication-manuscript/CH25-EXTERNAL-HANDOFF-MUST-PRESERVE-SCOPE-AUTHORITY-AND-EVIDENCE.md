# CH25 — External Handoff Must Preserve Scope, Authority and Evidence

## 1. External handoff is not a message send

When work leaves the originating Workplace and enters a provider, partner, official office, payment service or other external actor, the system crosses a boundary of responsibility.

The correct chain is:

```text
Internal Outcome Candidate
→ Handoff Package
→ Recipient Eligibility
→ Appointment or Acceptance
→ Instruction
→ External Work
→ Return Contract
→ Validation
```

A handoff is therefore not complete merely because an email, API call or file transfer occurred.

```text
Instruction Sent
≠ Instruction Accepted
≠ Work Started
≠ External Action Completed
```

## 2. Handoff must identify the parties

Every external handoff should state:

- originating Workplace;
- Relationship Owner;
- Delivery Owner;
- represented customer or applicant;
- recipient organization;
- recipient professional or operator;
- jurisdiction;
- authority source;
- contact channel;
- escalation contact;
- replacement route.

The recipient must know who is instructing, on whose behalf, under which engagement and with what authority.

```text
Platform Originated
≠ Platform Is Contracting Party
```

## 3. Scope must travel with the handoff

The Handoff Package should include:

- exact service requested;
- included and excluded stages;
- target outcome;
- jurisdiction;
- deadline;
- approved package version;
- cost limit;
- communication rules;
- data scope;
- required evidence;
- exception and recovery rules.

A provider receiving “please proceed” cannot safely infer whether the instruction includes filing, publication, registration, certificate collection or later office-action work.

```text
Broad Intent
≠ Complete External Scope
```

## 4. Recommendation, selection, appointment and acceptance remain separate

The provider lifecycle is:

```text
Candidate
→ Eligibility
→ Recommendation
→ Selection
→ Appointment
→ Acceptance
→ Instruction
→ Action
```

Each transition has a different authority source.

```text
Provider Recommended
≠ Provider Selected
≠ Provider Appointed
≠ Provider Accepted
```

The system must not create a live matter merely because a directory entry was clicked.

## 5. Appointment must be explicit

An appointment record should contain:

- provider identity;
- legal or professional entity;
- professional qualification;
- jurisdiction;
- scope;
- fee basis;
- appointment date;
- customer or Workplace authority;
- conflict status;
- confidentiality terms;
- data-processing terms;
- termination conditions.

Where a local agent must be formally appointed, the appointment may also require a POA or other official evidence.

```text
Provider Engagement
≠ Platform Membership
```

## 6. Acceptance is a provider-side event

A provider should affirm:

- it received the correct instruction;
- it accepts the scope;
- it has no conflict;
- it has capacity;
- it accepts the deadline;
- it accepts the fee arrangement;
- it can satisfy the Return Contract;
- it will disclose material changes.

```text
Instruction Delivered
≠ Provider Acceptance
```

Silence must not be interpreted as acceptance.

## 7. Handoff must preserve exact version identity

The provider must receive the exact approved package.

The handoff record should preserve:

- package identifier;
- version;
- checksum;
- attachment list;
- applicant identity;
- mark representation;
- goods or services;
- filing basis;
- supporting evidence;
- fee instruction;
- deadline.

```text
Approved Package Hash
= Handoff Package Hash
```

A material change after handoff requires a controlled amendment.

## 8. Handoff amendment must be traceable

An amendment should identify:

- original instruction;
- changed field;
- reason;
- requester;
- new review;
- new approval;
- effective time;
- whether the provider acknowledged the amendment;
- whether work had already begun.

```text
New Attachment Sent
≠ Original Instruction Automatically Replaced
```

## 9. Data minimization applies to external handoff

The recipient should receive only what is required for the accepted scope.

Possible controls include:

- field-level selection;
- document-level selection;
- redaction;
- restricted download;
- expiry;
- recipient-specific watermark;
- onward-sharing prohibition;
- training-use prohibition.

```text
Provider Needs the Matter
≠ Provider Needs the Entire Customer History
```

## 10. Customer relationship does not transfer by default

A provider may need direct contact for professional or procedural reasons. That does not automatically create commercial ownership of the customer.

The handoff should specify:

```text
No Customer Contact
Platform-mediated Contact
Supervised Direct Contact
Authorized Direct Professional Contact
Emergency Contact under Defined Rule
```

```text
Direct Contact Permission
≠ Customer Relationship Transfer
```

## 11. White-label and co-delivery must remain visible internally

The customer experience may be unified while internal accountability remains explicit.

The record should preserve:

- visible brand;
- Relationship Owner;
- Contracting Party;
- Provider identity where disclosure is required;
- Delivery Owner;
- professional authority;
- invoice path;
- complaint and recovery path.

```text
One Customer Experience
≠ One Hidden Actor
```

## 12. Return Contract is part of the handoff

Before work starts, the provider should know what evidence must be returned.

For filing, this may include:

- official number;
- filing date;
- filed mark;
- filed goods and classes;
- official receipt;
- fee proof;
- official acknowledgement.

For registration, it may include:

- official status source;
- registration number;
- certificate;
- owner details;
- validity period;
- unresolved limitations.

```text
Provider Reports Done
≠ Return Contract Satisfied
```

## 13. Handoff may include funds checkpoints, but not implied custody

The package can state:

- provider fee;
- official fee;
- prepayment requirement;
- maximum approved amount;
- currency;
- refund rule;
- payee;
- proof required.

But:

```text
Funds Checkpoint
≠ Permission to Hold or Move Funds
```

Payment authority remains separately governed.

## 14. Deadlines require explicit acknowledgment

The provider should acknowledge:

- deadline source;
- deadline type;
- timezone;
- grace or restoration status;
- latest safe action time;
- internal target date;
- dependency on documents or funds.

```text
Deadline Included in Email
≠ Deadline Accepted
```

## 15. Handoff failure modes must be anticipated

Common failures include:

- wrong recipient;
- wrong package version;
- provider silence;
- conflict discovered late;
- fee increase;
- missing original document;
- expired appointment;
- duplicate instruction;
- data over-disclosure;
- provider no longer eligible;
- evidence return incomplete.

Each Handoff Package should define escalation and replacement routes.

## 16. Provider substitution is not a simple reassignment

Before replacing a provider, the system must determine:

- whether the first provider accepted;
- whether it acted;
- whether fees were paid;
- whether official effect may exist;
- whether documents or originals are held;
- whether the appointment must be terminated;
- whether customer approval is required;
- whether duplicate action is possible.

```text
New Provider Selected
≠ Old Provider Effect Ended
```

## 17. External handoff through API requires the same governance

An API or connector call should preserve:

- recipient service identity;
- authentication context;
- payload hash;
- authority;
- idempotency key;
- timeout state;
- response;
- external reference;
- retry policy;
- Evidence Contract.

```text
Automated Handoff
≠ Governance-free Handoff
```

## 18. Human email handoff also requires audit

Manual work must record:

- sender;
- represented role;
- recipients;
- subject;
- attachments;
- version;
- instruction;
- deadline;
- provider response;
- later amendments.

```text
Manual
≠ Untracked
```

## 19. Handoff completion is a typed state

Useful states include:

```text
Prepared
Sent
Delivered
Acknowledged
Accepted
Conditionally Accepted
Rejected
Clarification Required
Conflict Declared
Funds Required
Documents Required
Expired
Cancelled
Unknown
```

A single `sent` state is insufficient.

## 20. Governing principle

External handoff is the controlled transfer of a bounded responsibility, not the transfer of all customer, professional or formal-state authority.

```text
Handoff
= scope + authority + recipient + version + evidence + recovery
```

When these elements survive the boundary, external work remains part of one accountable lifecycle.