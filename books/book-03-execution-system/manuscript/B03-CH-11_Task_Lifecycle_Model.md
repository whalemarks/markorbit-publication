# B03-CH-11 — Task Lifecycle Model

**Status:** Release Candidate 1

## Chapter Purpose

This chapter defines how Book 03 coordinates the lifecycle of active Tasks without moving Task ownership out of Book 02 Core.

A Task is an owned Core Object.

Workflow, AI, Product and Human Review may identify work, propose work, display work or provide evidence about work. They do not create, assign, transition, complete or cancel an active Task outside Task Service.

The chapter answers:

```text
How does proposed work become an active Task?
Who may assign it?
What does Task status mean?
When is Human Review required?
What does completion prove?
How are blocking, cancellation, archive, failure and retry handled?
How does Task trace relate to Workflow and business outcomes?
```

The central rule is:

```text
Task Service owns active Task lifecycle.
Task completion proves Task completion only.
```

---

## 1. Dependency Baseline

This chapter extends:

- [Chapter 09 — Execution Object and State Model](B03-CH-09_Execution_Object_and_State_Model.md)
- [Chapter 10 — Workflow Coordination Model](B03-CH-10_Workflow_Coordination_Model.md)

It consumes:

- [Task Object](../../book-02-core-specification/core-specs/objects/task.md)
- [Task API Contract](../../book-02-core-specification/core-specs/contracts/api/task-api-contract.md)
- [Workflow Contract API Contract](../../book-02-core-specification/core-specs/contracts/api/workflow-contract-api-contract.md)
- [Workflow Specifications Index](../../book-02-core-specification/core-specs/workflows/index.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [Idempotency Contract](../../book-02-core-specification/core-specs/contracts/common/idempotency.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)
- [Core Traceability Matrix](../../book-02-core-specification/core-specs/TRACEABILITY.md)

Book 02 controls Task status and transition rules. Book 03 coordinates those rules and must not create replacement values.

---

## 2. Task Boundary

A Task represents active work.

It is not:

- a Workflow Contract;
- a workflow step;
- a task-plan suggestion;
- an Event;
- a Notification;
- a Matter;
- an Order;
- a Communication;
- a Product card;
- an AI recommendation.

A Task has its own identity, type, status, assignment, subject references, priority, due context, review links and audit trace.

Task assignment does not grant Permission.

Task completion does not mutate related objects automatically.

AI-suggested work is not an approved active Task.

---

## 3. Proposed Work vs Active Task

Book 03 distinguishes three stages.

| Stage | Meaning | Authority |
|---|---|---|
| Work signal | A need, gap, requirement or next action has been identified | May come from Workflow, human, service, Event observation or AI assistance |
| Task plan | A governed proposal describing possible Tasks | Workflow preview/prepare-task-plan under Contract |
| Active Task | Task Service accepted creation and returned a Task reference | Task Service |

The path is:

```text
Work signal
→ proposed Task
→ validation and gates
→ Task Service create request
→ active Task or safe rejection
```

No earlier stage should be displayed as active work.

---

## 4. Task Creation

Task creation must include enough governed context to establish:

- Task type;
- safe title and description;
- subject or target references;
- source workflow/step where applicable;
- actor and organization;
- required owner role;
- priority;
- due-date basis;
- review requirement;
- Permission and Policy context;
- version;
- idempotency;
- audit correlation.

Creation routes through Task Service.

Task Service validates:

- reference validity;
- Task type and required fields;
- actor authority;
- Policy restrictions;
- duplicate-sensitive behavior;
- allowed relationships;
- safe exposure.

### 4.1 Creation Does Not Mean Assignment

A Task may be created before it has an assignee.

Creation and assignment are distinct operations.

### 4.2 Creation Does Not Mean Work Started

A created or Open Task is not necessarily InProgress.

### 4.3 Idempotent Creation

Duplicate-sensitive creation requires idempotency.

A replay must not create:

- duplicate Tasks;
- duplicate assignments;
- duplicate review links;
- duplicate Events.

---

## 5. Controlled Task Status

Book 02 defines Task status values including:

- Draft;
- Open;
- Assigned;
- InProgress;
- Waiting;
- Blocked;
- UnderReview;
- Completed;
- Cancelled;
- Archived;
- DeletedReferenceOnly;
- Unknown.

Book 03 uses those values as controlled sources.

It does not create alternatives such as:

- To Do;
- Doing;
- Done;
- Almost Done;
- AI Complete;
- Product Complete.

Product may display friendly language, but the source Task status remains identifiable.

---

## 6. Task Lifecycle

A typical Task lifecycle may include:

```text
Draft
→ Open
→ Assigned
→ InProgress
→ UnderReview
→ Completed
→ Archived
```

Other valid paths may include:

```text
Open → Waiting → Assigned
InProgress → Waiting → InProgress
InProgress → Blocked → InProgress
UnderReview → InProgress
Open / Assigned / InProgress → Cancelled
Completed / Cancelled → Archived
```

The exact transition must be allowed by Task Service and its contract.

Book 03 does not assume every Task follows the same path.

### 6.1 Draft

Task content is not ready for active work.

### 6.2 Open

The Task is active and available for assignment or work under policy.

### 6.3 Assigned

An assignee relationship exists.

Assignment does not prove work began.

### 6.4 InProgress

Work is being performed.

### 6.5 Waiting

The Task cannot currently progress because an expected dependency, response or time condition is pending.

### 6.6 Blocked

A known blocking condition prevents progress.

Waiting and Blocked should not be collapsed if the owning contract distinguishes them.

### 6.7 UnderReview

Task output or completion evidence is being reviewed.

### 6.8 Completed

Task Service accepted the Task completion transition.

### 6.9 Cancelled

The Task is no longer intended to continue under the current lifecycle.

Cancellation does not automatically reverse prior effects.

### 6.10 Archived

The Task is retained as historical reference under policy.

---

## 7. Assignment

Assignment is a governed relationship.

It may involve:

- User;
- role;
- organization unit;
- team;
- authorized service role;
- future approved agent-assistance context.

Assignment must check:

- Task state;
- assignee reference;
- organization scope;
- Permission;
- Policy;
- conflict or segregation rules;
- workload or routing constraints where an approved contract defines them;
- Human Review where required.

Assignment does not grant the assignee access beyond Permission and Policy.

### 7.1 AI Is Not an Accountable Assignee by Default

AI may assist a human-owned Task where Agent governance allows.

It must not silently become the accountable assignee.

If Book 02 later defines an Agent assignment model, Book 03 must consume that approved model.

### 7.2 Reassignment

Reassignment should preserve:

- prior assignee;
- reason;
- actor;
- time;
- affected review;
- audit trace.

It must not erase prior responsibility.

---

## 8. Task Context

An active Task should remain linked to its professional context.

Relevant references may include:

- Matter;
- Order;
- Trademark;
- Customer;
- Document;
- Evidence;
- Communication;
- Workflow Contract;
- Human Review;
- Event;
- actor or organization.

Task context is not ownership.

A Task linked to a Matter does not own Matter state.

A Task linked to a Communication does not own send authority.

A Task linked to a filing does not own filing submission.

---

## 9. Due-Date Basis

A Task may use a due-date basis derived from:

- official deadline;
- internal SLA;
- workflow sequence;
- customer commitment;
- review target;
- dependency timing.

Book 03 must distinguish:

```text
official or professional deadline
internal task due date
suggested due date
Product reminder
AI-estimated timing
```

AI may suggest timing.

It must not certify an official deadline.

A Task due date does not replace the owning deadline source.

---

## 10. Work Evidence and Completion Preparation

Before completion, the Task may need:

- work summary;
- output references;
- document or evidence references;
- completion checklist;
- review reference;
- unresolved issue disclosure;
- safe customer-facing summary;
- source and version context.

AI may prepare a completion draft.

Preparation is not completion.

### 10.1 Completion Gate

Completion may require:

- required output exists;
- required references validate;
- required Human Review completed;
- Permission and Policy allow transition;
- current Task state supports completion;
- no blocking conflict;
- version supported;
- idempotency where duplicate-sensitive.

### 10.2 Review Return

If review requests changes:

```text
UnderReview
→ InProgress
```

may be appropriate where Task Service allows it.

The review outcome does not perform the status transition itself.

---

## 11. Governed Status Transition

A Task transition request contains:

- requested status;
- safe reason;
- completion summary where applicable;
- actor and organization;
- Permission and Policy context;
- Human Review reference where required;
- idempotency where required;
- correlation.

Task Service returns:

- previous status;
- current status;
- transition time;
- completion time where applicable;
- restricted-field omission;
- Event references where allowed.

```text
requested_status is intent.
current_status is service-confirmed state.
```

A rejected transition may return StateTransitionNotAllowed, PermissionDenied, PolicyRestricted, HumanReviewRequired, Conflict or another safe error.

---

## 12. Task Completion Is Narrow

Task completion proves that Task Service accepted completion of that Task.

It does not prove:

- Matter completed;
- Order completed;
- Communication sent;
- Document accepted by an authority;
- evidence is legally sufficient;
- provider selected;
- payment approved;
- filing submitted;
- deadline met;
- trademark registered;
- professional conclusion correct.

If Task completion should trigger evaluation of another action, that action still follows its own contract and gates.

This is one of the most important truth boundaries in MarkOrbit.

---

## 13. Waiting and Blocking

Execution should make a safe blocking reason visible.

Possible reasons include:

- missing reference;
- missing Document;
- external response pending;
- Human Review pending;
- Permission denied;
- Policy restricted;
- conflict;
- unsupported version;
- downstream service unavailable;
- official information unavailable.

The reason must be safe and policy-compliant.

AI may summarize the reason but must not remove or override it.

### 13.1 Waiting Is Not Failure

Waiting may be the correct state while an external dependency is expected.

### 13.2 Blocked Is Not Cancelled

A blocked Task may resume if the blocker is resolved.

### 13.3 Product Must Not Hide Blockers

Product may simplify the display but must not present blocked work as active progress or completion.

---

## 14. Cancellation

Cancellation requires authority and context.

It should consider:

- Task state;
- reason;
- existing work product;
- dependent Tasks;
- review status;
- Workflow impact;
- Matter or Order impact;
- audit requirements.

Cancellation does not:

- delete history;
- reverse service effects;
- cancel a Matter or Order automatically;
- revoke a sent Communication;
- erase Event trace.

If compensation or reversal is required, it needs an owning-service contract.

---

## 15. Archive and Historical Reference

Archived Tasks remain historical records subject to Policy.

Archive should preserve:

- identity;
- status;
- assignment history;
- relevant output references;
- review links;
- Event references;
- timestamps;
- version context;
- restricted-field rules.

Archived does not mean unrestricted.

DeletedReferenceOnly should preserve safe reference behavior without exposing deleted content.

---

## 16. Task Trace

Task execution should support answers to:

```text
Who created the Task?
Why was it created?
Which workflow or object produced the need?
Who was assigned?
What state transitions occurred?
Which review was required?
What evidence supported completion?
What did AI prepare?
What did Task Service accept?
Which Events trace the result?
```

Workflow and API layers do not emit Task Events directly.

Task Service may emit allowed Task Events after successful operations.

Event references remain audit trace.

---

## 17. AI-Assisted Task Work

AI may:

- summarize Task context;
- identify missing information;
- propose a Task;
- prepare a task plan;
- draft work output;
- prepare a completion summary;
- explain blockers;
- summarize trace.

AI must not:

- create an active Task outside Task Service;
- assign or reassign accountable owners;
- start or complete a Task;
- approve work;
- remove a blocker;
- certify professional completion;
- send a linked Communication;
- close a Matter or Order;
- emit Events.

AI assistance must preserve source scope and missing context.

---

## 18. Worked Example: Evidence Review Task

A Task is created to review evidence for an application.

### 18.1 Creation

Workflow proposes:

```text
Task type: EvidenceReview
Subject: Evidence Package reference
Required owner role: Professional Reviewer
Human Review required: true
```

Task Service validates and creates the active Task.

### 18.2 Progress

The Task is Assigned, then InProgress.

AI may summarize the Evidence Package and identify missing items.

The AI summary is not an evidence sufficiency decision.

### 18.3 Review

The Human Reviewer examines source evidence and records a review decision.

If more information is needed, the Task may move from UnderReview back to InProgress.

### 18.4 Completion

After accepted review evidence exists, an authorized user requests Completed.

Task Service accepts or rejects.

If accepted:

- Task becomes Completed;
- allowed Event trace is recorded;
- Execution refreshes its progress view.

The Evidence Object, Matter and application workflow retain their own states.

---

## 19. Task Invariants

1. Task Service owns active Task lifecycle.
2. Task plan is not active Task.
3. AI suggestion is not active Task.
4. Creation is not assignment.
5. Assignment is not Permission.
6. Assignment is not work started.
7. UnderReview is not Completed.
8. Review decision does not transition Task automatically.
9. Requested status is not current status.
10. Task completion proves Task completion only.
11. Cancellation does not reverse prior effects.
12. Archive preserves governed history.
13. Due date is not automatically an official deadline.
14. Retry must preserve idempotency.
15. Workflow does not create Tasks directly.
16. API does not emit Task Events directly.
17. Product display does not own Task state.
18. AI does not complete or approve.
19. Partial work and blockers remain visible.
20. Related Core Objects retain separate state.

---

## 20. Task Anti-Patterns

- AI output becomes an active Task.
- A Task card in Product is treated as the Task source of truth.
- Assignment grants access automatically.
- Completion closes the Matter.
- A completed Task marks an official filing complete.
- Cancellation deletes trace.
- Waiting and Blocked are hidden as InProgress.
- Review approval completes the Task without Task Service.
- Retry creates duplicate Tasks.
- A workflow emits TaskCreated directly.
- Suggested due date is displayed as an official deadline.
- Archived Tasks expose restricted history.

---

## 21. MVP Depth

The MVP should support:

- Task reference;
- creation through Task Service;
- controlled status;
- assignment;
- governed transition;
- Task-to-object links;
- Human Review reference;
- blockers and safe errors;
- completion preparation;
- idempotency where required;
- Event references;
- Product-safe projection.

It does not require:

- a general-purpose project management system;
- resource optimization;
- advanced scheduling;
- autonomous AI assignment;
- automatic professional completion;
- cross-product Task UI;
- complex compensation logic;
- Task event streaming.

---

## 22. Non-Goals of This Chapter

This chapter does not define:

- new Task fields;
- new Task statuses;
- database tables;
- Task UI;
- workforce planning;
- official deadline calculation;
- AI task authority;
- Matter or Order completion;
- Communication sending;
- Event types;
- service implementation;
- queue or scheduler design.

It defines execution coordination around the Book 02 Task lifecycle.

---

## 23. Chapter Conclusion

The Task lifecycle converts approved work intent into accountable active work.

The path is:

```text
Signal
→ Task plan
→ gates
→ Task Service creation
→ assignment
→ work
→ review where required
→ governed transition
→ completion, cancellation or archive
→ trace
```

Task remains distinct from Workflow, Matter, Order, Communication and Event.

Task completion is narrow.

Assignment does not grant Permission.

Human Review does not transition status by itself.

AI prepares but does not create, assign, approve or complete.

The next chapter defines the Review and Approval lifecycle that Tasks, Workflows, Communications and protected actions depend on.
