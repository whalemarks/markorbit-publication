# CP-B — Production Field and Ownership Matrix

## 1. Purpose

This matrix tests each proposed production-chain field against frozen Book 02 ownership.

The governing rule is:

```text
A useful field does not justify a new Core Object.
A new Object requires stable identity, lifecycle, ownership,
interoperability value and migration evidence.
```

## 2. Field comparison

| Proposed field | Frozen coverage | Gap | Preliminary disposition |
|---|---|---|---|
| parent Matter | Task.matter_reference_id | none | retain Task reference |
| parent Order | Task.order_reference_id | none | retain Task reference |
| Workflow Contract | Task.workflow_contract_reference_id | none | retain Task reference |
| workflow state | Task.workflow_state_reference | partial | retain or Book 03 runtime profile |
| concrete work type | Task.task_type | direct | retain frozen controlled values |
| title and description | Task title/description references | direct | retain |
| scope | Task description; Workflow Contract; no typed Task scope field in MVP table | partial | governed profile reference |
| exclusions | no exact frozen field | missing | profile field, not root-object proof |
| expected deliverable | Document/Evidence refs; task type | partial | profile field |
| input references | Document/Evidence/Communication refs | direct/partial | retain references |
| data classification | Permission/Policy/DataAccess context | composable | governance profile |
| required Capability | Permission capability reference; Capability spec | composable | profile reference |
| production mode | no frozen M-mode | missing | Book 03/Product policy |
| risk/review tier | Policy and Human Review; no frozen R-tier | composable | Book 03/Product policy |
| acceptance criteria | Human Review scope and Owning Service rules | partial | profile reference |
| due time | Task.due_at | direct | retain |
| dependencies | Task dependency references | direct | retain |
| assignee | Task assignee fields | direct | retain for simple assignment |
| responsibility | Task responsibility reference | direct/partial | retain |
| Assignment offer | no exact field | missing | candidate accepted-assignment profile |
| Assignment acceptance | no exact field | missing | candidate accepted-assignment profile |
| Assignment expiry | no exact field | missing | candidate profile |
| Assignment revocation | Permission/Task reassignment can partly model | partial | candidate profile if history must survive |
| contributor | created_by or artifact owner not sufficient | partial | Contribution profile |
| submission basis | Task/Assignment refs | composable | Contribution profile |
| submitted artifacts | Document/Evidence refs | direct | Contribution profile |
| submitted version | Common Versioning | composable | Contribution profile |
| supersedes submission | Common References/Versioning | composable | Contribution profile |
| review request | Human Review | direct | retain frozen contract |
| reviewer | Human Review reviewer | direct | retain |
| review scope/status/decision | Human Review | direct | retain |
| accepted Contribution | no exact frozen shared field | missing | Outcome profile |
| acceptance purpose | Human Review scope may partly cover | partial | Outcome profile |
| accepted scope and exclusions | no exact frozen result envelope | partial | Outcome profile |
| accepting service | Owning Service and review target | composable | Outcome profile |
| correction state | Workflow and versioning can model | partial | profile field |
| formal-state application | Owning Service result/event | direct boundary, not Outcome-owned | reference only |
| compensation | Order/Product settlement | outside Task chain | Product or separate commercial reference |

## 3. Identity test

### Work Package

A stable identity may be justified when one package:

- groups several Tasks;
- has package-level acceptance criteria;
- has one Assignment or several Contributions;
- survives Task replacement;
- is transferred across Workplaces;
- has package-level commercial or correction obligations.

Without those properties, a Task profile is sufficient.

### Assignment

A stable identity may be justified when Assignment:

- requires acceptance;
- can expire, be declined or revoked;
- carries commercial or confidentiality terms;
- grants exact data access;
- persists while Tasks change;
- crosses Organization or Workplace boundaries.

Simple internal allocation should remain Task assignment.

### Contribution

A stable identity may be justified when a submission:

- groups multiple artifacts;
- can be corrected or superseded;
- has its own review state;
- must preserve contributor attribution independently of artifact ownership;
- is reusable as Evidence across Products.

Otherwise, Document/Evidence plus Event references may be sufficient.

### Outcome

A stable identity may be justified when an accepted result:

- must be consumed by several downstream services;
- remains valid after Task closure;
- has purpose-limited acceptance;
- may be corrected or superseded;
- must be distinguished from formal-state mutation;
- crosses Product or Workplace boundaries.

Otherwise, Human Review decision plus Evidence and Event may be sufficient.

## 4. Lifecycle matrix

| Record | Candidate lifecycle | Frozen equivalent | Finding |
|---|---|---|---|
| Task | Draft, Open, Assigned, InProgress, Waiting, Blocked, ReviewRequired, Completed, Cancelled, Archived, DeletedReferenceOnly | exact frozen status | do not change |
| Work Package | Draft, Ready, Active, Review, Completed, Cancelled, Superseded | no exact lifecycle | first test as derived/profile state |
| Assignment | Offered, Accepted, Declined, Expired, Suspended, Revoked, Completed | Task Assigned plus Permission/Policy only partly cover | candidate lifecycle for bilateral cases |
| Contribution | Draft, Submitted, Superseded, Withdrawn | Document/Evidence versions and Events partly cover | profile first |
| Review | Requested, InProgress, Completed, Cancelled, Expired | frozen Human Review controlled status | retain frozen contract |
| Outcome | Candidate, Accepted, Rejected, Superseded, Corrected, Withdrawn | review decision, Event and owning-state results partly cover | profile first; shared identity unresolved |

These candidate labels are not approved controlled values.

## 5. Mutation ownership

### Task

```text
Task Service owns Task status and assignment fields.
```

### Work Package profile

Until a new contract is approved:

```text
profile owner must not mutate Task, Matter or Workflow state directly.
```

### Assignment

Simple model:

```text
Task Service updates assignee and responsibility
only after Permission / Policy / Review requirements pass.
```

Distinct Assignment model:

```text
candidate Assignment Service owns offer/accept/revoke lifecycle;
Task Service consumes the accepted Assignment reference;
Book 03 enforces runtime handoff;
Permission Service owns grants;
Policy Service owns contextual decisions.
```

### Contribution

```text
Document Service owns Documents.
Evidence Service owns Evidence.
Contribution profile links them and preserves attribution.
It does not rewrite the artifact owner.
```

### Review

```text
Human Review Contract records review.
Relying Owning Service decides whether review satisfies its action requirements.
```

### Outcome

```text
Outcome acceptance must be performed by an authorized actor or relying service.
Outcome does not mutate Task, Matter, Order, Trademark or official state automatically.
```

## 6. State-separation controls

Required equations:

```text
Assignment State
≠ Task State
≠ Work Package State
```

```text
Contribution State
≠ Review State
≠ Outcome State
```

```text
Outcome Accepted
≠ Task Completed
≠ Matter Resolved
≠ Formal State Updated
```

```text
Provider Return Received
≠ Contribution Accepted
≠ Outcome Established
```

## 7. Compatibility risks

A proposal may break frozen consumers when it:

- replaces `Task.id` with a Work Package ID;
- removes or changes frozen Task statuses;
- changes `assignee_type` controlled values;
- makes Assignment acceptance mandatory for every Task;
- changes Human Review required fields;
- converts Document or Evidence IDs into Contribution IDs;
- changes Workflow Contract mutation authority;
- automatically maps Task `Completed` to accepted Outcome;
- adds public export types without versioning and migration rules.

## 8. Consumer proof requirements

Before opening a formal F3 proposal, at least two independent consumers should demonstrate the need.

Suggested proof set:

```text
Book 03 Execution
+ MarkReg or Lite
```

The proof should show:

- where Task alone is insufficient;
- why Product-local records cannot solve the problem;
- which fields are identical across consumers;
- which lifecycle must remain shared;
- which service owns mutation;
- how frozen consumers continue to work.

## 9. Proposed decision split

```text
Task remains unchanged and canonical.
Human Review remains unchanged and canonical.
Work Package begins as an F2 profile.
Simple Assignment remains a Task assignment profile.
Accepted bilateral Assignment advances to F3 research.
Contribution begins as an F2 submission profile.
Outcome begins as an F2 acceptance profile.
```

A future proposal should not bundle all five terms into one new contract family.

## 10. Matrix verdict

```text
Frozen Task fields mapped: YES
Frozen Human Review sufficient for review envelope: YES
Work Package root identity proven: NO
Bilateral Assignment identity potentially justified: YES
Contribution root identity proven: NO
Outcome root identity proven: NO
State-separation controls required: YES
Formal proposal ready today: NO
Additional consumer proof required: YES
```