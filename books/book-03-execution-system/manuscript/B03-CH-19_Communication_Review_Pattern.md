# B03-CH-19 — Communication Review Pattern

**Status:** Release Candidate 1

## Chapter Purpose

The Communication Review Pattern governs the path from a proposed message to a version-bound review outcome without allowing draft preparation, approval and transmission to collapse into one action.

Communication can create immediate external consequences.

A message may affect:

- customer expectations;
- legal or professional position;
- fees and commercial scope;
- deadlines;
- evidence handling;
- provider instructions;
- confidentiality;
- filing or response strategy;
- responsibility between organizations.

The pattern therefore answers:

```text
What Communication or draft is being reviewed?
Which exact content version is in scope?
Who is the intended audience and recipient set?
Which sources, attachments and subject references support the draft?
What content is missing, uncertain or Policy-restricted?
Which human role must review it?
What review decision was recorded?
May Communication Service update the review status?
What remains required before any separate send action?
```

Its governing sequence is:

```text
Draft context
→ side-effect-free review preview
→ Human Review package
→ version-bound review decision
→ Communication Service status update
→ follow-up Tasks where needed
→ separate send boundary
```

The pattern does not send external Communications.

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
- [Chapter 17 — Intake Execution Pattern](B03-CH-17_Intake_Execution_Pattern.md)
- [Chapter 18 — Application Preparation Pattern](B03-CH-18_Application_Preparation_Pattern.md)

Its primary Book 02 sources are:

- [Communication Review Workflow](../../book-02-core-specification/core-specs/workflows/communication-review-workflow.md)
- [Communication Review Workflow Contract](../../book-02-core-specification/core-specs/contracts/workflows/communication-review-workflow-contract.md)
- [Workflow Specifications Index](../../book-02-core-specification/core-specs/workflows/index.md)
- [Workflow Contract Index](../../book-02-core-specification/core-specs/contracts/workflows/index.md)
- [Communication Object](../../book-02-core-specification/core-specs/objects/communication.md)
- [Document API Contract](../../book-02-core-specification/core-specs/contracts/api/document-api-contract.md)
- [Matter API Contract](../../book-02-core-specification/core-specs/contracts/api/matter-api-contract.md)
- [Order API Contract](../../book-02-core-specification/core-specs/contracts/api/order-api-contract.md)
- [Task API Contract](../../book-02-core-specification/core-specs/contracts/api/task-api-contract.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [AI Context Contract](../../book-02-core-specification/core-specs/contracts/common/ai-context.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Idempotency Contract](../../book-02-core-specification/core-specs/contracts/common/idempotency.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)

Book 02 owns Communication state, the Workflow, contract, review actions, Services, controlled values and validation. This chapter describes their operational use without defining new Communication statuses or a new sending contract.

---

## 2. Pattern Position

The pattern may receive a draft from:

- Intake;
- Application Preparation;
- Provider Routing Preparation;
- Office Action Response Preparation;
- Renewal Preparation;
- Assignment Preparation;
- Evidence Review Preparation;
- an authorized human;
- a governed Communication Agent;
- an existing Communication requiring revision or renewed review.

It may produce:

- review context prepared;
- changes requested;
- reviewed;
- approved for send;
- rejected;
- review required;
- blocked;
- safe failure;
- active follow-up Tasks;
- a versioned handoff to a separate send-preparation boundary.

It does not produce:

- external transmission;
- official submission;
- provider instruction dispatch;
- delivery confirmation;
- recipient acceptance.

---

## 3. Pattern Lock

The pattern is governed by six invariants.

```text
Draft is not review.
Review is not approval.
Approval is not send preparation.
Send preparation is not transmission.
Transmission is not delivery.
Delivery is not recipient acceptance.
```

The MVP adds an especially important lock:

```text
Communication Review Workflow may coordinate review status.
It may not send a Communication directly.
```

### 3.1 Approval for Send Is a Bounded Decision

Approved for send means the reviewed version may be considered for the named downstream purpose.

It does not mean:

- the message was sent;
- the final sender remains authorized;
- the recipient set is still current;
- attachments remain unchanged;
- Permission and Policy still allow transmission;
- the Communication Service accepted a send request;
- delivery occurred.

### 3.2 Workflow Apply Is Not Send

Apply may coordinate Communication Service to create a scoped draft or update review status.

It must not:

- invoke external dispatch as Workflow-owned behavior;
- mark sent;
- infer delivery;
- emit a send Event directly.

### 3.3 Human Review Is Not a Transmission Mechanism

A reviewer records an accountable decision.

The reviewer does not send by completing review.

A Product action that both approves and sends would collapse two protected actions unless an owning contract explicitly governs them as separate decisions and effects.

---

## 4. Communication Review Context

Execution assembles a bounded review context.

| Context area | Review question |
|---|---|
| Communication | Which reference and state are current? |
| Version | Which exact draft is being reviewed? |
| Type | Is this an internal note, client message, provider message or official instruction? |
| Channel | Which intended transmission channel applies? |
| Audience | Internal, customer, partner, provider, official or another controlled audience? |
| Participants | Who is the intended sender and recipient set? |
| Subject | Which Customer, Trademark, Matter, Order, Document, Evidence or provider context is linked? |
| Sources | Which facts, Documents, prior Communications and decisions support the draft? |
| Attachments | Which exact references and versions are included? |
| Risk | Which professional, confidentiality, commercial or deadline risks exist? |
| AI | What did AI draft, revise, translate or flag? |
| Governance | Which Permission, Policy and Human Review requirements apply? |
| Purpose | What downstream action is proposed after review? |
| Trace | Which correlation, prior review and Event references connect the work? |

This context is not a new Core object.

### 4.1 Subject Reference Does Not Authorize Disclosure

A valid Matter or Order reference does not mean every fact may be copied into an external message.

Policy still governs:

- subject visibility;
- recipient visibility;
- commercial term visibility;
- Document metadata;
- Evidence content;
- internal notes;
- review rationale.

### 4.2 Audience and Recipient Are Different

Audience type describes the intended relationship category.

Recipient set identifies the actual people or governed address references.

Approval for a customer audience does not approve an arbitrary customer contact.

---

## 5. Draft Preparation

The pattern may begin with an existing Communication reference or a draft that Communication Service is allowed to create within the Workflow scope.

The draft package should identify:

- draft text or content reference;
- version;
- communication type;
- channel;
- audience;
- intended sender;
- intended recipients;
- subject references;
- attachments;
- source references;
- AI involvement;
- missing information;
- uncertainty;
- Policy omissions;
- required review role.

### 5.1 Draft Sources

Draft content may come from:

- verified Core facts;
- user-provided instructions;
- professional analysis;
- Document or Evidence summaries;
- prior Communication;
- template material;
- AI suggestions;
- human edits.

The pattern must preserve source distinctions.

An AI-generated deadline sentence is not verified because it is fluent.

A copied prior message is not current merely because it was previously approved.

### 5.2 Internal Notes Are Not External Drafts

Internal review notes may contain:

- uncertainty;
- candid risk;
- provider pricing;
- restricted customer facts;
- reviewer comments.

The pattern must not convert internal content into an external message without explicit preparation, Policy evaluation and Human Review.

### 5.3 Draft Version

Review applies to a stable version.

Material changes include:

- recipients;
- sender;
- channel;
- fee;
- deadline;
- service scope;
- legal or professional conclusion;
- instruction;
- attachment;
- disclaimer;
- language that changes meaning.

Material change normally requires a new review decision.

---

## 6. Review Preview

Preview is side-effect free.

It may:

- validate the Communication or draft reference;
- validate subject references;
- assess audience and channel;
- identify restricted content;
- identify missing review inputs;
- identify required reviewer role;
- prepare allowed review actions;
- prepare risk flags;
- prepare a Task plan;
- prepare AI-assisted revision suggestions;
- disclose Policy omissions;
- return warnings and safe errors.

Preview must not:

- create or update Communication state;
- approve;
- reject;
- request changes as an active transition;
- create active Tasks;
- send;
- mutate a subject;
- emit Events.

### 6.1 Preview Questions

A useful preview should answer:

```text
Is the current draft stable enough to review?
Are the sender, recipient, purpose and channel known?
Are sources and attachments available under Policy?
Which professional claims require verification?
Which fields were omitted or redacted?
Which review role is required?
Which review actions are allowed now?
What must remain blocked?
```

### 6.2 Policy Redaction During Preview

If content is restricted, the preview may be:

- blocked;
- redacted;
- downgraded to safe summary;
- routed to a reviewer with different authority;
- returned as NotFound where non-disclosure applies.

A redacted preview must not be described as full-content review.

---

## 7. Human Review Package

The review package should contain the minimum sufficient governed context.

It may include:

- Communication reference;
- exact content version;
- intended sender;
- exact recipient set;
- channel;
- purpose;
- audience;
- subject references;
- attachments and versions;
- sources;
- known facts;
- uncertain statements;
- AI Context;
- Policy omissions;
- risk flags;
- requested review action;
- intended downstream action;
- expiry or freshness conditions.

### 7.1 Review Scope

Unsafe scope:

```text
Approve this email.
```

Safer scope:

```text
Review version 5 of the provider instruction email for the named provider,
service scope, quoted fee wording, deadline statement and two listed attachments.
If approved, the version may proceed to a separate send-preparation check.
```

### 7.2 Reviewer Authority

The reviewer must have authority for the defined scope.

A Task assignee is not automatically a professional reviewer.

An administrator is not automatically authorized to approve legal or commercial wording.

AI is never the accountable reviewer.

### 7.3 Reviewer Visibility

Reviewer authority does not automatically grant unrestricted access.

Policy still controls:

- hidden recipients;
- cross-organization content;
- confidential Documents;
- provider commercial terms;
- private review notes;
- Evidence content.

---

## 8. Review Actions and Meanings

Book 02 identifies review actions including preparation, change request, reviewed status, approval for send and rejection.

The pattern must preserve their different meanings.

### 8.1 Prepare Review

Creates or organizes review context.

It does not record a substantive review decision.

### 8.2 Request Changes

States that the current version cannot proceed without revision.

The result should identify:

- reviewed version;
- requested changes;
- responsible role;
- source or risk basis;
- whether a new review is required.

### 8.3 Mark Reviewed

Records that review occurred under a defined scope.

It must not be presented as approval unless the recorded decision supports approval.

### 8.4 Approve for Send

Allows the exact version to proceed toward a separate send boundary under stated conditions.

It requires current Permission, Policy and Human Review where protected.

It does not transmit.

### 8.5 Reject

Blocks the current reviewed version for the defined purpose.

Rejection does not necessarily forbid every future revised version.

---

## 9. Approval Reliance

After approval, Execution must decide whether the recorded result can still be relied upon for the intended next step.

It checks:

- Communication reference;
- exact version;
- recipient set;
- sender;
- channel;
- purpose;
- attachments;
- reviewer and role;
- decision;
- conditions;
- expiry;
- current subject state;
- current Permission;
- current Policy;
- material changes.

### 9.1 Recipient Change

Adding, removing or replacing a recipient may change:

- confidentiality;
- privilege;
- commercial exposure;
- Policy;
- review scope.

Approval for one recipient set is not approval for another.

### 9.2 Attachment Change

Attachments are part of the reviewed package.

Adding a new Document, changing an Evidence version or removing a required attachment may invalidate reliance.

### 9.3 Thread and Reply Risk

A reply must not inherit recipients or disclosure scope blindly from a prior thread.

Execution revalidates current participants and quoted content.

### 9.4 Freshness

Approval may become stale because:

- deadline or official status changed;
- fee changed;
- Matter facts changed;
- provider changed;
- authority changed;
- Policy changed;
- a newer Communication version exists.

---

## 10. Apply Through Owning Services

Apply requires:

- supported Workflow Contract version;
- current actor and organization;
- Communication reference or explicitly scoped draft creation;
- requested review action;
- idempotency key;
- Permission Context;
- Policy Context;
- Human Review reference where required;
- current Communication state;
- current version;
- safe errors;
- AI Context where applicable.

Apply may coordinate:

| Result | Owner |
|---|---|
| Draft creation where scoped | Communication Service |
| Review status transition | Communication Service |
| Reviewer note recording | Communication Service |
| Active follow-up Task creation | Task Service |
| Event trace | Owning service or Event Service integration |

The Workflow does not own those changes.

### 10.1 Apply Result

The result may include:

- Communication reference;
- current review status;
- active Task references;
- Human Review requirement;
- restricted fields omitted;
- idempotency replay result;
- warnings;
- safe errors;
- Event references as trace.

It must not include a Workflow-created claim that transmission or delivery occurred.

---

## 11. Separate Send Boundary

After approval, a separate send-preparation process must revalidate:

- approved content version;
- sender identity and authority;
- recipient set;
- channel;
- attachments;
- approval conditions;
- Permission;
- Policy;
- idempotency;
- current Communication state;
- current subject facts.

In the current MVP depth, Communication Review Workflow does not send.

A future external send, if implemented, must remain:

- Communication Service-owned;
- Permission and Policy governed;
- Human Review gated where required;
- idempotency protected;
- safe-error controlled;
- Event traced;
- versioned.

### 11.1 Prepared Is Not Sent

A copyable or downloadable message package is not proof of transmission.

A Product opening the user's email client is not proof of send.

A manual operator stating “ready” is not proof of send.

### 11.2 Sent Is Not Delivered

Even Communication Service acceptance may differ from:

- provider acceptance;
- transmission;
- delivery;
- bounce;
- read;
- recipient acceptance.

Execution must record only the result supported by the owning Service and available evidence.

---

## 12. Task Coordination

The preview may prepare Tasks such as:

- revise content;
- confirm recipient;
- confirm sender;
- verify fee;
- verify deadline wording;
- attach a Document;
- obtain professional review;
- resolve Policy restriction;
- prepare send package;
- check uncertain transmission outcome.

A Task plan is not an active Task.

Only Task Service creates active Tasks during apply.

Task completion does not prove:

- Communication approved;
- Communication sent;
- delivery;
- recipient acceptance;
- Matter progress.

Communication Service state remains authoritative.

---

## 13. AI-Assisted Review

AI may:

- draft or revise wording;
- translate;
- summarize;
- compare versions;
- identify missing facts;
- flag inconsistent fees or deadlines;
- identify unsupported claims;
- prepare attachment checklists;
- suggest tone changes;
- prepare review questions;
- summarize Policy omissions where allowed.

AI must not:

- approve;
- reject as the accountable reviewer;
- select final recipients;
- certify legal correctness;
- certify authority;
- certify client instruction;
- certify provider commitment;
- change review status;
- send;
- mutate subject state;
- emit Events.

### 13.1 Tone Improvement Must Preserve Meaning

An AI rewrite may make language more polished while accidentally changing:

- certainty;
- responsibility;
- price;
- deadline;
- scope;
- legal conclusion;
- requested action.

Meaning-changing edits require renewed review.

### 13.2 Translation Is a New Review Surface

A translated message may require review because:

- legal nuance changed;
- terminology became stronger or weaker;
- names or addresses were transformed;
- attachments use another language;
- the reviewer approved only the source language.

Translation assistance does not inherit approval automatically.

---

## 14. Permission and Policy Gates

Permission and Policy remain independent.

The pattern may require Permission to:

- read Communication;
- prepare draft;
- review;
- approve;
- request a future send;
- access subject references;
- create follow-up Tasks.

Policy may govern:

- content visibility;
- recipient visibility;
- review-note visibility;
- customer data;
- provider terms;
- Document and Evidence metadata;
- cross-organization disclosure;
- AI source use;
- Event visibility.

An allowed Permission does not override a Policy restriction.

A Policy allowance does not authorize an actor.

Human Review does not bypass either.

---

## 15. Idempotency and Duplicate Effects

Apply requires idempotency.

The same key and semantic review action should replay without duplicating:

- Communication drafts;
- status transitions;
- reviewer notes where contract treats them as duplicate-sensitive;
- active Tasks;
- Events.

A changed version, action, reviewer note or subject context may require conflict rather than replay.

A future send must use its own Communication-delivery idempotency scope.

Review idempotency must not be mistaken for send idempotency.

### 15.1 Unknown Send Outcome

If a later provider outcome is unknown, blind retry may create duplicate external consequences.

The safe next action may be reconciliation or status checking rather than immediate resend.

---

## 16. Trace and Audit

Trace should preserve, where Policy allows:

- draft source;
- content version;
- AI assistance;
- preview;
- Permission and Policy evaluations;
- Human Review request and decision;
- reviewer role;
- review status transition;
- Task creation;
- approval conditions;
- idempotent replay;
- safe error;
- Event references.

The Workflow does not emit Events directly.

Audit should make it possible to answer:

```text
What version was reviewed?
Who reviewed it and under what authority?
Which recipients, channel and attachments were in scope?
What AI changed?
Which content was omitted by Policy?
What decision was recorded?
Did Communication Service accept the status transition?
What separate step remains before send?
```

---

## 17. Safe Failure and Recovery

Controlled outcomes include:

- validation failure;
- invalid reference;
- Permission denied;
- Policy restricted;
- Human Review required;
- missing reviewer role;
- version mismatch;
- state conflict;
- idempotency key required;
- idempotency conflict;
- unsupported version;
- NotFound under non-disclosure;
- internal safe error.

Errors must not expose:

- hidden recipients;
- restricted message content;
- restricted customer data;
- provider commercial terms;
- private review notes;
- raw Document or Evidence content;
- Policy internals;
- Permission internals;
- prompts;
- hidden reasoning;
- stack traces.

A recoverable result should identify, where allowed:

- current version;
- blocked action;
- safe reason;
- required role;
- required change;
- whether prior review remains usable;
- whether a new preview is required.

---

## 18. Example — Foreign Provider Instruction

A Matter requires an instruction email to a foreign service provider.

The draft contains:

- requested service;
- mark and applicant references;
- target jurisdiction;
- stated deadline;
- quoted fee;
- two attachments;
- request to proceed.

### 18.1 Preview

The pattern identifies:

- recipient reference is available;
- provider commercial terms are Policy-controlled;
- deadline source needs verification;
- fee approval is missing;
- one attachment version differs from the Matter context;
- Human Review is required;
- AI may prepare a safer revision and gap summary.

### 18.2 First Review

The reviewer selects changes requested because:

- fee authority is missing;
- deadline wording is too certain;
- attachment version is inconsistent.

Communication Service records the review status through apply. Task Service creates follow-up Tasks.

No message is sent.

### 18.3 Revision

A new version:

- cites the verified deadline source;
- uses the approved fee;
- includes the correct attachments;
- preserves the named provider and service scope.

AI assists with wording, but the new version requires review.

### 18.4 Approval

An authorized reviewer approves the exact version for the named provider, sender, channel, purpose and attachment set.

The result is approved for send.

It is still unsent.

### 18.5 Handoff

A separate send-preparation step must refresh:

- recipients;
- sender authority;
- current attachments;
- Permission;
- Policy;
- approval conditions;
- idempotency.

Only Communication Service may later record an allowed transmission result.

---

## 19. Pattern Acceptance Checklist

The Communication Review Pattern is correct when:

- [ ] Communication or draft identity is explicit;
- [ ] exact content version is stable;
- [ ] sender, audience, recipient set, channel and purpose remain distinct;
- [ ] subject references do not imply disclosure authority;
- [ ] attachments are included in review scope;
- [ ] internal notes are not exposed as external content;
- [ ] AI output remains draft, suggestion or risk analysis;
- [ ] translation and material revision trigger appropriate review;
- [ ] preview has no side effects;
- [ ] Human Review is role-, scope- and version-bound;
- [ ] review actions retain different meanings;
- [ ] approved for send is not presented as sent;
- [ ] approval reliance revalidates recipients, attachments and freshness;
- [ ] apply requires Idempotency, Permission and Policy;
- [ ] Communication Service owns draft and review status;
- [ ] Task Service alone creates active Tasks;
- [ ] Workflow does not send;
- [ ] Workflow does not emit Events directly;
- [ ] Task completion does not prove Communication state;
- [ ] safe failure protects restricted content;
- [ ] a separate send boundary remains visible.

---

## 20. Product Boundary

Book 04 may provide drafting, comparison, review and later send surfaces. It must preserve draft, reviewed, approved-for-send, sent and delivered as separate states. Book 03 does not define editors, inboxes or send interfaces.

## 21. Implementation Boundary

This pattern adds no new Communication state model, messaging connector, template engine, queue, API schema or Product UI. Communication send remains a separate Service-owned and separately approved capability.

## 22. Chapter Result

The Communication Review Pattern keeps preparation, accountable decision and external consequence separate.

```text
Draft with provenance.
Preview without side effects.
Review a stable version.
Record a bounded decision.
Apply status only through Communication Service.
Create Tasks only through Task Service.
Revalidate approval before any later send.
Never treat approval as transmission.
```

The pattern succeeds when the exact reviewed version, decision, conditions and remaining send boundary are visible.

The next chapter defines the **Provider Routing Preparation Pattern**, where candidate discovery, comparison and recommendation must remain separate from final provider selection, commitment and instruction.
