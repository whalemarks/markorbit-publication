# B03-CH-13 — Communication Execution Boundary

## Chapter Purpose

This chapter defines the execution boundary for Communication.

Communication is where preparation becomes external consequence.

A draft may affect:

- customer expectation;
- legal position;
- commercial commitment;
- fee quotation;
- deadline understanding;
- provider instruction;
- evidence handling;
- filing or response strategy;
- confidentiality.

The lifecycle must therefore preserve:

```text
Draft
→ Review
→ Approve
→ Prepare Send
→ Send by Communication Service
→ Record
→ Audit
```

Each stage has a different meaning.

AI may draft.

Human Review may evaluate.

An authorized human may approve within scope.

Communication Service owns Communication behavior and transmission under contract.

Book 03 coordinates the boundaries. It does not send.

---

## 1. Dependency Baseline

This chapter extends:

- [Chapter 09 — Execution Object and State Model](B03-CH-09_Execution_Object_and_State_Model.md)
- [Chapter 12 — Review and Approval Lifecycle](B03-CH-12_Review_and_Approval_Lifecycle.md)

It consumes:

- [Communication Object](../../book-02-core-specification/core-specs/objects/communication.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [AI Context Contract](../../book-02-core-specification/core-specs/contracts/common/ai-context.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Idempotency Contract](../../book-02-core-specification/core-specs/contracts/common/idempotency.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)
- [Communication Review Workflow Contract](../../book-02-core-specification/core-specs/contracts/workflows/communication-review-workflow-contract.md)

Book 03 uses existing Communication states and contract outcomes. It does not create a second messaging model.

---

## 2. Communication Boundary

Communication is not:

- Notification;
- Event;
- Document;
- Evidence;
- Task;
- internal AI output;
- Product toast;
- unrecorded chat text.

Communication has:

- identity;
- type;
- channel;
- direction;
- participants;
- subject and linked references;
- content or content reference;
- status;
- review;
- approval;
- send preparation;
- delivery result;
- audit trace.

Communication Service owns Communication behavior.

---

## 3. Six Execution Stages

### 3.1 Draft

Proposed content is prepared.

Draft may be human-written, AI-assisted or template-derived.

Draft has no send authority.

### 3.2 Review

An authorized reviewer examines the defined version, sources, recipients, risks and scope.

Review does not transmit.

### 3.3 Approve

An authorized decision permits a specific Communication version to proceed toward the defined send purpose.

Approval is bounded.

### 3.4 Prepare Send

Execution assembles and revalidates the final send package.

Preparation does not transmit.

### 3.5 Send

Communication Service transmits through an allowed channel or records an authorized external handoff under its contract.

### 3.6 Record and Audit

The system preserves the sent version, actor, recipients, timing, outcome and trace allowed by Policy.

The stages must not collapse.

---

## 4. Draft Model

A Communication draft should identify:

- Communication reference where created;
- type;
- intended channel;
- direction;
- intended participants;
- linked Matter, Order, Task or other references;
- content version;
- source materials;
- attachments;
- AI assistance;
- missing context;
- Policy omissions;
- review requirement.

### 4.1 AI Draft

AI may:

- propose wording;
- translate;
- summarize;
- structure;
- compare versions;
- identify missing facts;
- prepare a subject line;
- prepare an attachment checklist.

AI must not:

- choose final recipients;
- approve;
- send;
- hide uncertainty;
- invent fees, deadlines, evidence or authority;
- convert internal notes into external statements without review.

### 4.2 Draft Is Versioned

Review and approval rely on a specific version.

A changed draft may require new review.

Material changes include:

- recipient;
- legal position;
- fee;
- scope;
- deadline;
- attachment;
- instruction;
- disclaimer;
- professional conclusion.

---

## 5. Participant and Recipient Boundary

Before send, Execution resolves:

- sender identity;
- sender organization;
- sender authority;
- recipient identity or safe address reference;
- recipient role;
- relationship to Matter/Order/Customer/Provider;
- channel;
- confidentiality restrictions;
- cross-organization Policy;
- attachment visibility.

A valid recipient reference does not imply Permission to communicate.

AI may suggest a candidate recipient from authorized context.

AI must not select the final external recipient.

### 5.1 Group and Multiple Recipient Risk

Multiple recipients may change:

- confidentiality;
- privilege;
- commercial exposure;
- Policy;
- review scope.

Approval for one recipient set is not approval for another.

### 5.2 Reply and Thread Context

A reply must not rely blindly on prior thread participants.

Execution revalidates current recipient and disclosure scope.

---

## 6. Communication Review

Review should examine:

- factual accuracy;
- professional accuracy within scope;
- recipient;
- channel;
- confidentiality;
- fees;
- deadline statements;
- evidence references;
- attachments;
- legal or commercial commitments;
- source and version;
- AI involvement;
- Policy omissions.

A reviewer decision remains linked to the reviewed version and intended purpose.

Review may return:

- Approved;
- Rejected;
- Revised;
- NeedsMoreInformation;
- Escalated;
- NotApplicable.

Review outcome does not send.

---

## 7. Approval Boundary

Approval should answer:

```text
May this specific version be prepared for transmission
to this recipient set
through this channel
for this stated purpose
under current Policy?
```

Approval does not answer:

```text
Has it been sent?
Was it delivered?
Was it read?
Did the recipient accept?
Did the Matter advance?
Is the professional outcome correct?
```

Approval may include conditions such as:

- attachment required;
- named sender required;
- send before or after a stated event;
- additional disclaimer;
- supervisor confirmation;
- recipient restriction;
- channel restriction.

Conditions must remain visible during send preparation.

---

## 8. Prepare Send

Prepare Send assembles the exact transmission package.

It checks:

- approved content version;
- current sender;
- current recipients;
- current channel;
- attachments and versions;
- Permission;
- Policy;
- Human Review;
- approval conditions;
- Communication state;
- idempotency;
- safe audit context.

Possible outcomes include:

- Ready;
- RequiresHumanReview;
- PermissionDenied;
- PolicyRestricted;
- MissingRecipient;
- MissingAttachment;
- VersionMismatch;
- Conflict;
- Error.

These are contract outcomes where defined, not invented Product states.

### 8.1 Prepare Send Is Not Send

A package may be ready but remain unsent.

Product must preserve that distinction.

### 8.2 Freshness

A prepared package may become stale if:

- content changes;
- recipient changes;
- attachment changes;
- Policy changes;
- approval expires;
- sender authority changes;
- related Matter facts change.

Send requires final validation.

---

## 9. Send

Send is protected execution.

It may occur only through Communication Service or an approved provider boundary governed by the owning contract.

Send should preserve:

- idempotency for duplicate-sensitive transmission;
- exact content version;
- exact recipient set;
- sender;
- channel;
- time;
- attachments;
- approval and Human Review references;
- Permission and Policy decisions;
- provider response;
- safe error;
- Event or audit references.

Workflow, API orchestration and AI do not emit send Events or claim send success directly.

### 9.1 Service Acceptance vs Delivery

Communication Service acceptance is not necessarily delivery.

Execution distinguishes:

- send request accepted;
- transmitted;
- provider accepted;
- delivered where known;
- failed;
- bounced or rejected where supported;
- unknown.

Book 03 does not invent delivery certainty.

### 9.2 External Manual Handoff

Where sending remains manual, Execution may prepare a package and require the authorized human to complete or confirm the external action.

The system records only what the contract and evidence support.

It must not mark sent merely because the package was downloaded or copied.

---

## 10. Record and Audit

A Communication record should preserve the allowed evidence of:

- approved content;
- sent content;
- version;
- sender;
- recipient set;
- channel;
- time;
- provider or manual outcome;
- attachments;
- linked objects;
- review;
- approval;
- AI assistance;
- Permission and Policy;
- errors and retries;
- Event references.

Restricted content and review notes remain subject to Policy.

Record does not mean every recipient received or accepted the message.

---

## 11. Idempotency and Duplicate Send

Duplicate Communication can create serious harm.

Duplicate-sensitive send requires idempotency.

The system should distinguish:

- safe replay of the same semantic send request;
- changed content;
- changed recipient;
- changed attachment;
- changed channel;
- changed approval;
- changed purpose.

Same key with different semantic request must conflict.

Retry after an uncertain provider outcome requires caution. Execution must not send again merely because confirmation is missing.

A reconciliation or provider-status check may be required.

---

## 12. Failure and Retry

Possible failures include:

- invalid recipient;
- missing attachment;
- version mismatch;
- Permission denied;
- Policy restricted;
- Human Review required;
- approval expired;
- provider unavailable;
- provider rejected;
- unknown send outcome;
- duplicate conflict.

A safe error should state:

- failed operation;
- affected Communication reference;
- safe reason;
- retryability;
- required next step;
- whether any transmission may have occurred;
- correlation and trace.

Retry must revalidate the entire package.

---

## 13. Communication and Task

A Task may request drafting, review, send preparation or follow-up.

Task completion does not prove send.

Examples:

```text
Drafting Task completed
≠ Communication approved

Review Task completed
≠ Communication sent

Send-preparation Task completed
≠ Communication transmitted
```

Communication Service state remains authoritative.

---

## 14. Communication and Event

Communication is not Event.

An Event may trace:

- Communication created;
- reviewed;
- approved where specified;
- sent;
- failed.

The Event records an allowed completed fact.

It does not contain new send authority.

Event payload visibility may be more restricted than the Communication reference.

---

## 15. Product Outcome

Product may show:

- Draft;
- Needs Review;
- Changes Requested;
- Approved for Send;
- Send Preparation Blocked;
- Sent;
- Delivery Unknown;
- Failed;
- Retry Requires Check.

The exact Product language belongs to Book 04.

The underlying distinctions must remain:

- draft version;
- review result;
- approval scope;
- send preparation;
- send service result;
- delivery evidence;
- trace.

Product must not display “Sent” from approval alone.

---

## 16. Worked Example: Provider Instruction Email

A Matter requires instruction to a foreign provider.

### 16.1 Draft

AI prepares a draft using:

- Matter context;
- approved service scope;
- provider reference;
- deadline context;
- attachment checklist.

AI discloses missing cost confirmation.

### 16.2 Review

A Human Reviewer confirms:

- provider;
- service scope;
- deadline wording;
- attachment;
- no unsupported legal conclusion.

The reviewer selects NeedsMoreInformation because the final fee approval is missing.

### 16.3 Approval

After fee approval is recorded, version 3 is reviewed and approved for the named provider.

### 16.4 Prepare Send

Execution revalidates:

- provider contact;
- content version 3;
- fee;
- attachments;
- sender authority;
- Permission;
- Policy;
- approval.

### 16.5 Send

Communication Service transmits with idempotency.

If provider response is unknown, Execution records send acceptance and unknown delivery rather than sending again automatically.

No Task, Matter or provider-selection state is inferred beyond supported service outcomes.

---

## 17. Communication Invariants

1. AI may draft but not approve or send.
2. Draft is not reviewed.
3. Reviewed is not approved unless decision says so.
4. Approved is not prepared.
5. Prepared is not sent.
6. Sent is not delivered unless evidence supports it.
7. Delivered is not accepted by recipient.
8. Approval is version-, recipient-, channel- and purpose-bounded.
9. Recipient changes require revalidation.
10. Attachments are part of the reviewed package.
11. Permission and Policy remain independent.
12. Communication Service owns send.
13. Workflow does not send directly.
14. Task completion does not prove send.
15. Event reference does not authorize send.
16. Duplicate send is idempotency-sensitive.
17. Unknown provider outcome must not trigger blind retry.
18. Manual handoff is not automatically sent.
19. Product status does not own Communication truth.
20. Audit preserves the exact sent version where allowed.

---

## 18. Communication Anti-Patterns

- AI sends its own draft.
- Approval checkbox has no reviewed version.
- Recipient is changed after approval.
- Attachment is added after review.
- Product marks approved as sent.
- Workflow emits CommunicationSent.
- Send retry duplicates an uncertain transmission.
- Manual download is recorded as sent.
- Internal notes are exposed externally.
- Review notes are exposed without Policy.
- Fee or deadline is generated without verified source.
- Task completion closes Communication.

---

## 19. MVP Depth

The MVP should support:

- Communication reference;
- draft preparation;
- version;
- recipient and channel context;
- Human Review;
- approval;
- prepare-send outcome;
- Permission and Policy;
- idempotency;
- Communication Service handoff;
- safe send result;
- audit and Event references;
- Product-safe distinction between approved, sent and delivery-known.

It does not require:

- a full email client;
- omnichannel messaging;
- delivery analytics platform;
- autonomous sending;
- marketing automation;
- bulk campaign tooling;
- Product UI;
- provider-specific infrastructure in Book 03.

---

## 20. Non-Goals of This Chapter

This chapter does not define:

- new Communication fields or statuses;
- SMTP or provider infrastructure;
- inbox synchronization;
- email templates;
- Product screens;
- autonomous sending;
- legal wording;
- recipient discovery;
- delivery guarantees;
- Event types;
- service implementation.

It defines governed execution around existing Communication contracts.

---

## 21. Chapter Conclusion

Communication execution is a chain of distinct authority boundaries.

```text
Draft
→ Review
→ Approve
→ Prepare Send
→ Send by Communication Service
→ Record
→ Audit
```

Each arrow matters.

AI drafts but does not approve.

Human Review evaluates but does not transmit.

Approval is bounded.

Prepare Send revalidates.

Communication Service sends.

Idempotency prevents duplicate harm.

Audit preserves what the evidence supports.

The next chapter defines how Events, audit context and controlled replay make these and other execution paths traceable without turning Events into commands or logs into professional truth.
