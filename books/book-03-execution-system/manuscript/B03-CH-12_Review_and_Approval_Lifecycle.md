# B03-CH-12 — Review and Approval Lifecycle

## Chapter Purpose

This chapter defines how Book 03 coordinates Human Review and approval without allowing review to become hidden execution authority.

Human Review is required for protected professional or external-facing work.

It records accountable evaluation.

It may support an approval decision.

It does not:

- grant Permission;
- approve Policy;
- mutate Core Object state;
- complete a Task;
- apply a Workflow;
- send a Communication;
- select a provider automatically;
- submit a filing;
- approve payment by implication;
- emit an Event.

The central rule is:

```text
Review decides whether reviewed material satisfies the review scope.
Owning Services decide whether that result satisfies an action gate.
Execution revalidates and coordinates the downstream action separately.
```

---

## 1. Dependency Baseline

This chapter extends:

- [Chapter 09 — Execution Object and State Model](B03-CH-09_Execution_Object_and_State_Model.md)
- [Chapter 10 — Workflow Coordination Model](B03-CH-10_Workflow_Coordination_Model.md)
- [Chapter 11 — Task Lifecycle Model](B03-CH-11_Task_Lifecycle_Model.md)

It consumes:

- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [AI Context Contract](../../book-02-core-specification/core-specs/contracts/common/ai-context.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Task API Contract](../../book-02-core-specification/core-specs/contracts/api/task-api-contract.md)
- [Workflow Contract API Contract](../../book-02-core-specification/core-specs/contracts/api/workflow-contract-api-contract.md)
- [Review Gate Model](../planning/B03-PLN-0008_Review_Gate_Model.md)

Book 03 consumes the Human Review Contract. It does not create new review decisions, reviewer authority or approval semantics.

---

## 2. Review Boundary

Human Review answers a bounded question.

Examples:

- Is the Communication draft acceptable for the stated audience and purpose?
- Is the Classification Recommendation acceptable within the stated evidence and jurisdiction context?
- Is the evidence package sufficient for the defined review scope?
- Is the provider-selection recommendation acceptable?
- Is workflow apply ready for authorized execution?
- Is filing preparation ready for a separate submission action?

Review does not answer every downstream question.

A review of a draft does not approve every later version.

A review of evidence does not decide registrability.

A review of a workflow preview does not approve apply after material context changes.

---

## 3. Review vs Approval

Review and approval are related but distinct.

| Concept | Meaning |
|---|---|
| Review | Accountable examination of defined material, evidence, context and risk |
| Review outcome | Approved, Rejected, Revised, Escalated, NeedsMoreInformation, NotApplicable or another Book 02-controlled decision |
| Approval boundary | The point at which an authorized decision permits a specific downstream request to be considered |
| Downstream action | Service-owned execution that still requires current Permission, Policy, state and contract validation |

Approval is never unlimited.

It should be bounded by:

- subject;
- scope;
- reviewed version;
- reviewer role;
- decision;
- time;
- Policy;
- intended downstream action.

---

## 4. Review Lifecycle

Book 02 defines review statuses including:

- Requested;
- InReview;
- Completed;
- Rejected;
- Escalated;
- Expired;
- Cancelled;
- NotRequired;
- Unknown.

A typical lifecycle is:

```text
Requested
→ InReview
→ Completed
```

Alternative paths include:

```text
Requested → Cancelled
Requested / InReview → Escalated
InReview → Rejected
Requested / InReview → Expired
Review evaluation → NotRequired
```

Review decision is separate from review status.

A Completed review may have a decision such as Approved, Rejected, Revised, Escalated, NeedsMoreInformation or NotApplicable.

Execution must preserve both.

---

## 5. Review Request

A Review Gate should create or resolve a review request under the governing contract.

The request should identify:

- subject references;
- review scope;
- required reviewer role;
- reason review is required;
- source version;
- draft or evidence version;
- relevant Permission and Policy context;
- AI involvement;
- missing context;
- intended downstream action;
- expiry or freshness rules where applicable;
- audit correlation.

A review request is not approval.

### 5.1 Review Scope Must Be Specific

Unsafe scope:

```text
Review this Matter.
```

Safer scope:

```text
Review version 3 of the proposed external response for factual accuracy,
approved fee wording and consistency with the attached evidence.
```

Specific scope protects downstream reliance.

### 5.2 Review Evidence Must Be Stable

The reviewer needs to know:

- what was reviewed;
- which version;
- which sources;
- which fields were omitted;
- which AI output was used;
- which context was unavailable.

Material changes after review may invalidate reliance.

---

## 6. Reviewer Authority

A reviewer must be an authorized human role.

Authority depends on:

- identity;
- organization;
- role;
- review scope;
- Permission;
- Policy;
- professional responsibility;
- separation-of-duty requirements where applicable.

Being assigned a Task does not automatically make the assignee an authorized reviewer.

Being an administrator does not automatically satisfy professional review.

AI is not a reviewer.

### 6.1 Reviewer Independence

Where Policy requires independence, the preparer and reviewer roles must remain distinct.

Book 03 coordinates this rule only when Book 02 Policy defines it.

### 6.2 Delegated Review

Delegation must preserve:

- delegator;
- delegate;
- authority source;
- scope;
- time;
- reason;
- audit trace.

Delegation must not silently expand scope.

---

## 7. Review Context

Review context may include:

- subject references;
- current object states;
- Workflow or Task context;
- draft or output version;
- supporting Documents;
- Evidence;
- prior decisions;
- Permission and Policy outcomes;
- AI Context;
- safe audit summary;
- known limitations;
- intended next action.

The review context is bounded.

It should not expose restricted fields merely because a reviewer exists.

Policy still controls visibility.

---

## 8. AI-Assisted Review Preparation

AI may:

- summarize sources;
- compare versions;
- identify missing evidence;
- identify inconsistent facts;
- prepare review questions;
- organize a checklist;
- explain a contract requirement;
- draft a proposed response;
- summarize prior trace.

AI must disclose source and limitation.

AI must not:

- mark review Completed;
- choose Approved;
- impersonate a reviewer;
- infer approval from no response;
- erase missing evidence;
- certify professional truth;
- execute the downstream action.

AI confidence is not review authority.

---

## 9. Review Decision

The reviewer records a decision within the defined scope.

Possible decisions include:

- Approved;
- Rejected;
- Revised;
- Escalated;
- NeedsMoreInformation;
- NotApplicable.

The decision should preserve:

- review reference;
- reviewed version;
- reviewer;
- role;
- decision;
- safe rationale;
- conditions;
- required revisions;
- time;
- source scope;
- audit context.

### 9.1 Approved

Approved means the reviewed material satisfies the defined review scope.

It does not mean downstream execution already occurred.

### 9.2 Rejected

Rejected means the reviewed material does not satisfy the defined scope.

The downstream action remains blocked.

### 9.3 Revised

Revised means a reviewer-approved revision or revision requirement exists.

Execution must identify which version may be relied upon.

### 9.4 Needs More Information

Execution returns to preparation or context collection.

It must not convert this into approval.

### 9.5 Escalated

A different reviewer role or authority is required.

Escalation is not rejection and not approval.

---

## 10. Approval Reliance

After review, the downstream owning service decides whether the review satisfies its gate.

The service may check:

- correct review scope;
- correct reviewer authority;
- current decision;
- reviewed version matches requested action;
- review not expired;
- Policy conditions satisfied;
- no material context change;
- Permission still valid;
- target state still eligible.

A valid review may still be insufficient for a specific action.

### 10.1 Version Match

If version 3 was approved, version 4 is not automatically approved.

Non-material change treatment requires an owning contract.

### 10.2 Scope Match

Approval for internal draft use is not approval for external send.

Approval for provider recommendation is not final provider selection unless the scope says so and the owning contract allows it.

### 10.3 Time and Context Match

A review may become stale because:

- law or official status changed;
- evidence changed;
- recipient changed;
- price changed;
- Permission changed;
- Policy changed;
- deadline context changed;
- workflow version changed.

Execution revalidates before action.

---

## 11. Review Return Path

The operational return path is:

```text
Review outcome recorded
→ Execution validates reviewer, scope, version and freshness
→ Execution refreshes target state
→ Permission re-evaluated
→ Policy re-evaluated
→ owning service checks review reliance
→ downstream request accepted or rejected
→ trace recorded
```

Review return is not a shortcut.

---

## 12. Review and Task Lifecycle

A Task may enter UnderReview while its work product is reviewed.

The Human Review reference and Task status remain distinct.

Possible paths:

```text
InProgress
→ UnderReview
→ Completed
```

or:

```text
InProgress
→ UnderReview
→ InProgress
```

Task Service owns the transition.

The review decision does not complete the Task automatically.

A completed Task does not mean the reviewed professional action occurred.

---

## 13. Review and Workflow Lifecycle

Workflow preview may identify that Human Review is required before apply.

Workflow apply may return RequiresHumanReview.

After review:

- current Workflow Contract version is checked;
- target state is refreshed;
- Permission and Policy are refreshed;
- review scope and version are validated;
- apply is requested separately.

A previous review must not be reused across materially different apply requests.

---

## 14. Review and Communication

Communication review is especially sensitive.

The lifecycle distinguishes:

```text
Draft
→ Review
→ Approval
→ Prepare Send
→ Send by owning service
→ Record
→ Audit
```

Review may examine:

- content;
- facts;
- evidence;
- recipient;
- confidentiality;
- fee wording;
- legal position;
- attachments;
- version.

Approval does not transmit.

Chapter 13 defines this boundary fully.

---

## 15. Review Failure and Expiry

A review may fail operationally because:

- reviewer lacks authority;
- evidence missing;
- version mismatch;
- scope mismatch;
- Policy restriction;
- review expired;
- reviewer conflict;
- source inaccessible;
- restricted data omitted;
- unsupported contract version.

Execution returns a safe error and next step.

Possible next steps include:

- fix request;
- request Human Review;
- request Policy review;
- validate reference;
- escalate;
- prepare a new version;
- no action available.

Expired review must not be silently treated as Approved.

---

## 16. Audit and Event Trace

Review trace should distinguish:

- requested;
- started;
- completed;
- rejected;
- revised;
- escalated;
- expired;
- cancelled.

Human Review Contract does not emit Events directly.

Owning services decide which Events reference Human Review.

Review notes may be more restricted than the fact that review occurred.

Audit should preserve:

- subject;
- version;
- reviewer;
- decision;
- intended action;
- AI involvement;
- Permission and Policy references;
- time;
- resulting service action or rejection.

---

## 17. Worked Example: External Fee Communication

A draft email contains:

- service scope;
- official fee;
- service fee;
- payment timing;
- legal caveat.

### 17.1 Preparation

AI may draft from approved source materials.

The draft records AI Context and source scope.

### 17.2 Review Request

Review scope states:

```text
Review version 2 for factual accuracy, fee accuracy,
recipient suitability and approved legal wording.
```

The reviewer receives sources and Policy-compliant context.

### 17.3 Decision

The reviewer selects NeedsMoreInformation because the exchange rate source is missing.

Execution routes the draft back to preparation.

No approval exists.

### 17.4 Second Review

Version 3 includes the verified exchange-rate source.

The reviewer approves version 3 for the named recipient and stated purpose.

### 17.5 Send Handoff

Execution revalidates:

- version 3;
- recipient;
- current Permission;
- current Policy;
- review freshness;
- attachments;
- Communication state.

Then it may request Communication Service to prepare/send under its contract.

Approval did not send the email.

---

## 18. Review Invariants

1. Human Review is performed by an authorized human.
2. AI output is not Human Review.
3. Review has a specific subject and scope.
4. Review records the reviewed version.
5. Review status and decision remain separate.
6. Completed does not necessarily mean Approved.
7. Approved does not mean executed.
8. Permission and Policy remain independent.
9. Reviewer role does not grant unlimited access.
10. Material change may require new review.
11. Expired review cannot be reused silently.
12. Review does not mutate Core state.
13. Review does not complete Tasks automatically.
14. Review does not apply Workflows automatically.
15. Review does not send Communications.
16. Owning service validates review reliance.
17. Product does not infer approval.
18. AI does not approve.
19. Review trace preserves restricted-data rules.
20. Downstream action is separately audited.

---

## 19. Review Anti-Patterns

- AI marks output reviewed.
- A checkbox with no reviewer identity counts as Human Review.
- Approval has no scope.
- Approval has no version.
- Old approval is applied to changed content.
- Administrator role replaces professional reviewer authority.
- Review completion triggers send automatically.
- Review decision bypasses Permission or Policy.
- Task UnderReview is displayed as professionally approved.
- Missing information is converted into conditional approval without contract.
- Review notes are exposed without Policy.
- Product infers approval from inactivity.

---

## 20. MVP Depth

The MVP should support:

- review requirement;
- review request/reference;
- reviewer role;
- status;
- decision;
- subject and scope;
- reviewed version;
- evidence references;
- AI disclosure;
- Permission and Policy references;
- audit context;
- owning-service reliance check;
- safe expiry/failure;
- Product-safe review condition.

It does not require:

- a universal review platform;
- automated legal approval;
- advanced delegation;
- biometric signature;
- cross-jurisdiction reviewer licensing system;
- Product UI;
- AI reviewer;
- automatic downstream execution.

---

## 21. Non-Goals of This Chapter

This chapter does not define:

- new review statuses or decisions;
- reviewer licensing rules;
- approval UI;
- electronic signature implementation;
- workflow engine behavior;
- Communication infrastructure;
- service APIs;
- Product screens;
- autonomous approval;
- legal or professional truth;
- new Events.

It defines coordination around Book 02 Human Review.

---

## 22. Chapter Conclusion

Human Review is a governed decision point.

The lifecycle is:

```text
Request
→ assemble evidence
→ authorized review
→ record status and decision
→ validate scope, version and freshness
→ refresh Permission, Policy and source state
→ ask owning service to perform the next allowed action
→ preserve trace
```

Review is accountable.

Approval is bounded.

Approved is not executed.

AI prepares but does not review.

Product displays but does not infer.

The next chapter applies these rules to the highest-frequency external boundary in MarkOrbit: Communication preparation, review, approval, send handoff, recording and audit.
