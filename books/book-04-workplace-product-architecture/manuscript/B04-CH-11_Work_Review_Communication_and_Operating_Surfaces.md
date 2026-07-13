# B04-CH-11 — Work, Review, Communication and Operating Surfaces

**Status:** Draft 1  
**Chapter Map:** B04-TOC-V0.1  
**Part:** Part II — Organization Context and Operating Environment

## Chapter Purpose

This chapter defines how an Organization Workplace makes work, review, Communication, attention, exceptions, and organizational coordination visible through governed operating surfaces.

Chapter 07 established organization identity and active Workplace Context.

Chapter 08 established people, roles, permissions, responsibility, review eligibility, and accountability.

Chapter 09 established clients, relationships, service context, pricing, preferences, and organization-specific business rules.

Chapter 10 established private knowledge, AI Context, preferences, and organizational memory.

The next question is:

> How does all of that organizational context become a usable daily operating environment without turning the interface into a second Workflow engine, Task system, Review authority, Communication service, or formal system of record?

Workplace must help people understand:

```text
What requires attention?

What work is active?

What is only proposed?

What is waiting or blocked?

What must be reviewed?

What has been approved but not executed?

Which Communication is still a draft?

Which outcome has actually occurred?

Which Product or Owning Service is authoritative?
```

The central proposition of this chapter is:

```text
Operating Surface
=
an authorized, role-aware, purpose-bound projection
of work, review, Communication, context, and attention
from authoritative sources
```

An operating surface may display, summarize, filter, group, prioritize, explain, and collect user intent.

It does not become authoritative merely because it is where the user interacts.

The chapter must preserve six constitutional boundaries:

```text
Surface ≠ Source of Truth

Work Item ≠ Task

Review Surface ≠ Review Authority

Communication Surface ≠ Communication Send Authority

Presentation State ≠ Business State

User Action in a Surface ≠ Formal Mutation
```

Book 02 remains authoritative for Core Objects, statuses, permissions, policies, responsibility, Communication meaning, Task meaning, Human Review contracts, and formal mutation ownership.

Book 03 remains authoritative for Workflow coordination, Task lifecycle, Review and Approval lifecycle, Communication execution boundaries, permission and policy gates, protected-action controls, Event trace, retry, safe failure, and Human–AI execution handoff.

Book 04 defines how Workplace exposes and composes those responsibilities for an organization without absorbing them.

---

## 1. Professional Work Must Become Visible Somewhere

An organization may have valid records, governed Workflows, assigned Tasks, pending reviews, draft Communications, client instructions, private knowledge, and approaching deadlines.

Those elements create little operational value if people cannot see what matters now.

Professional work becomes difficult when it is distributed across:

- email inboxes;
- chat threads;
- spreadsheets;
- calendars;
- Product-specific dashboards;
- local files;
- Task lists;
- Matter records;
- provider portals;
- personal memory;
- AI conversations.

The problem is not only storage.

It is operational visibility.

A professional needs a coherent answer to:

```text
What requires my attention today?

What belongs to me?

What belongs to my team?

What is waiting on a client or provider?

What needs professional review?

What is at risk?

What changed since I last looked?

Which prepared action can move forward?
```

Workplace provides the organizational frame in which those answers can be assembled.

But the answer must remain grounded in authoritative sources.

The interface must not invent a simpler reality merely to make the screen look organized.

The principle is:

```text
Workplace makes professional work legible.

It does not redefine what the work is.
```

---

## 2. An Operating Surface Is a Governed Projection

An operating surface means:

> a user-facing or Agent-facing projection that presents authorized organizational context, work, review, Communication, exceptions, and possible actions for a defined purpose.

Examples may include:

- a Today surface;
- a personal work queue;
- a team work queue;
- a review queue;
- a Communication center;
- a client activity surface;
- a Matter overview;
- an exception and risk surface;
- a management overview;
- a Product-embedded Workplace panel;
- an external collaborator portal;
- a client status portal;
- an AI-assisted operating view.

The term `surface` is intentional.

A surface presents and composes information from underlying responsibilities.

It may provide interaction.

It does not automatically own:

- the underlying Object;
- the formal status;
- the lifecycle;
- the permission decision;
- the review decision;
- the send action;
- the filing action;
- the payment action;
- the Event;
- the audit record.

The relationship is:

```text
Authoritative Objects, Services, Execution, and Context
        ↓
Authorized projection and composition
        ↓
Operating Surface
        ↓
User understanding and intent
        ↓
Governed request or handoff
```

The surface is an operational window.

It is not a replacement authority.

---

## 3. Workplace Is Not One Universal Dashboard

The phrase `Workplace surface` must not be reduced to one dashboard.

Different users and purposes require different views.

An independent professional may need:

- Today priorities;
- client follow-up;
- review requests;
- draft Communications;
- upcoming deadlines;
- recommended next actions.

A process team may need:

- assigned Tasks;
- waiting work;
- blocked work;
- missing documents;
- provider responses;
- escalation conditions.

A reviewer may need:

- review scope;
- exact version;
- supporting Evidence;
- known limitations;
- intended downstream action;
- decision history.

A manager may need:

- workload distribution;
- unresolved exceptions;
- deadline exposure;
- review bottlenecks;
- service quality signals;
- responsibility gaps.

A client may need:

- safe status summaries;
- required actions;
- approved deliverables;
- authorized Communications;
- next expected milestone.

These surfaces may all belong to one Workplace architecture.

They should not be forced into one universal screen or one universal information density.

The rule is:

```text
One organizational Orbit
may require several operating surfaces.

Several operating surfaces
must still preserve one authority model.
```

---

## 4. Operating Surfaces Have Different Purposes

A useful architectural classification includes the following surface types.

### 4.1 Attention Surface

Shows what may require attention now.

Examples:

- approaching deadline;
- overdue Task;
- review request;
- missing client instruction;
- provider non-response;
- failed execution attempt;
- policy warning;
- recommendation requiring confirmation.

An attention surface may aggregate many object types.

It must preserve which type each item actually is.

### 4.2 Work Surface

Shows active governed work.

Examples:

- Tasks assigned to the user;
- Tasks assigned to the team;
- Workflow-related work;
- work waiting on dependency;
- blocked work;
- work under review.

The Work Surface does not own Task lifecycle.

### 4.3 Review Surface

Shows bounded Human Review requests, reviewed material, source versions, review scope, reviewer authority, and intended downstream action.

It must not collapse review, approval, and execution.

### 4.4 Communication Surface

Shows Communication drafts, reviews, participant context, approved versions, send preparation, delivery result, and related records.

It must distinguish internal collaboration from governed external Communication.

### 4.5 Object or Matter Surface

Shows one professional object and the relevant context around it.

Examples may include:

- Matter overview;
- Order overview;
- Opportunity overview;
- client relationship overview;
- Document or Evidence context;
- provider engagement context.

The surface may aggregate linked information without becoming the owner of every linked object.

### 4.6 Coordination Surface

Shows relationships among work, dependencies, people, providers, reviews, and handoffs.

It supports coordination without replacing Workflow coordination.

### 4.7 Exception Surface

Shows failures, blocks, conflicts, stale context, missing responsibility, missing knowledge, permission denial, and escalation requirements.

### 4.8 Management Surface

Shows organizational patterns and safe aggregates for planning, quality, capacity, and accountability.

Management visibility must remain subordinate to privacy, client restrictions, and purpose limitation.

### 4.9 External Participation Surface

Provides limited, purpose-bound views to clients, providers, partners, or invited collaborators.

It must never expose the full internal Workplace merely because external participation is useful.

These categories are logical.

They do not require separate applications or services.

One Product may compose several surface types.

---

## 5. A Generic Work Item Must Not Erase Semantic Difference

Many interfaces use a generic card or list item called a `work item`.

That can be useful for presentation.

But a generic visual container may represent very different underlying meanings:

- an active Task;
- a Task suggestion;
- a review request;
- a Notification;
- a Communication draft;
- an Event-derived alert;
- a deadline warning;
- a recommendation;
- an Opportunity Candidate;
- a missing-information request;
- a Workflow waiting condition;
- a failed action requiring correction.

These items are not interchangeable.

The surface must preserve the source type.

A user should be able to understand:

```text
This is active work.

This is only a suggestion.

This is a review request.

This is information only.

This is a warning.

This is a draft.

This is an approved item awaiting separate execution.
```

A generic card may provide one interaction pattern.

It must not create one universal lifecycle.

The distinction is:

```text
Common presentation container
≠
common business object
```

---

## 6. Work Signal, Recommendation, Task Plan, and Active Task Are Different

Workplace may detect or display possible work before a formal Task exists.

Examples include:

- a deadline is approaching;
- a client has not replied;
- a provider response appears incomplete;
- a registration may require renewal;
- a draft requires review;
- an information gap may block progress;
- a Recommendation proposes follow-up.

These conditions may become work signals.

A work signal is not automatically an active Task.

The correct progression is:

```text
Observation or Event
→ work signal
→ explanation or recommendation
→ proposed action or Task plan
→ validation and authorization
→ Task Service creation
→ active Task
```

The operating surface may expose all stages.

It must label them accurately.

Unsafe presentation:

```text
Your Task: Renew this trademark
```

when the system has only identified a possible renewal need.

Safer presentation:

```text
Possible renewal need detected.
Review the registration status and confirm whether a renewal Task should be created.
```

The surface should not use active-work language before active-work authority exists.

---

## 7. Task Visibility Does Not Transfer Task Ownership

A Workplace should make Tasks visible in a useful organizational context.

It may show:

- Task title;
- Task type;
- source object;
- assignee;
- responsible owner;
- status;
- priority;
- due context;
- review requirement;
- blocking condition;
- related Workflow;
- related client or Matter;
- latest safe activity;
- available governed actions.

But the source Task remains owned by the Task Service and Book 02 semantics.

The surface may translate controlled status into friendly language.

For example:

```text
Source status: InProgress
Displayed label: In progress
```

or:

```text
Source status: Waiting
Displayed label: Waiting for client documents
```

The displayed language must remain traceable to the source status.

The surface must not invent substitute canonical states such as:

- almost done;
- AI finished;
- handled;
- ready;
- no concern;
- complete enough.

Such phrases may be explanatory annotations.

They must not replace the formal status.

The rule is:

```text
Workplace displays Task state.

Task Service owns Task state.
```

---

## 8. Presentation State and Business State Must Remain Separate

Operating surfaces often maintain interface-specific state.

Examples include:

- unread;
- read;
- pinned;
- unpinned;
- expanded;
- collapsed;
- hidden;
- dismissed;
- snoozed;
- bookmarked;
- filtered;
- grouped;
- personally ranked.

These states may improve usability.

They are not business states.

For example:

```text
Dismissed alert
≠
resolved risk
```

```text
Snoozed Task card
≠
Task waiting or due date changed
```

```text
Marked as read
≠
review completed
```

```text
Hidden recommendation
≠
recommendation rejected under governance
```

```text
Removed from personal view
≠
responsibility transferred
```

A conforming architecture must distinguish at least three state layers:

```text
Presentation State
→ how the surface is currently shown

Interaction State
→ what the user has opened, acknowledged, selected, or prepared

Formal State
→ the authoritative status of the underlying Object or Execution record
```

Where recommendation acceptance, review decision, Task transition, or formal acknowledgment has business meaning, the action must be recorded through the proper authority rather than only as interface state.

---

## 9. Work Queues Must Be Role-Aware and Context-Aware

A work queue is not simply a list of everything the user can technically access.

It should be assembled according to:

- active organization;
- active operating identity;
- user role;
- assignment;
- responsibility;
- team scope;
- Product context;
- client or Matter restrictions;
- professional qualification;
- Permission;
- Policy;
- review eligibility;
- risk;
- purpose.

A user may be able to view a Matter but not act on its Tasks.

A manager may be able to view team workload but not review legal advice.

A reviewer may be eligible to review one category of output but not another.

An external collaborator may see only one assigned item and its permitted supporting context.

A work queue should therefore answer:

```text
Why is this item visible to me?

What relationship do I have to it?

What am I allowed to do?

What remains outside my authority?
```

Visibility should be explainable where consequence matters.

Role-aware presentation must not be implemented as role label alone.

It must consume actual identity, permission, policy, responsibility, and object relationship context.

---

## 10. The Today Surface Is an Attention Model, Not a New Source of Truth

Lite and other Workplace editions may use a Today surface as the main entry point.

Today may bring together:

- active Tasks;
- pending reviews;
- client follow-up;
- Communication drafts;
- deadline warnings;
- recommendations;
- knowledge gaps;
- provider delays;
- prepared actions;
- opportunities for professional or commercial follow-up.

This is valuable because professional work is not experienced as separate databases.

It is experienced as competing demands for attention.

But Today must remain an attention model.

It must not become a new universal object lifecycle.

A Today item should preserve:

- source type;
- source reference;
- reason for appearance;
- current source status;
- organization context;
- client or Matter context where allowed;
- risk or urgency basis;
- available actions;
- whether Human Review is required;
- whether the item is generated or recommended;
- freshness.

The Today surface may say:

```text
Review required before client delivery
```

It must not say:

```text
Ready to send
```

unless the relevant review, approval, Permission, Policy, version, and send-preparation conditions actually support that conclusion.

---

## 11. Prioritization Supports Attention but Does Not Create Authority

Operating surfaces may order items by:

- deadline proximity;
- legal or financial risk;
- client importance;
- contractual commitment;
- blocked dependency;
- aging;
- review requirement;
- assignment;
- organizational priority;
- recommendation score;
- user preference.

Prioritization may improve focus.

It does not alter the underlying object unless a governed action does so.

For example:

```text
Displayed first
≠
formal priority changed
```

```text
AI-ranked as urgent
≠
official deadline confirmed
```

```text
User moved card upward
≠
Task priority updated
```

A surface should distinguish:

```text
Formal priority
Personal display priority
AI recommendation priority
Risk or deadline signal
```

When prioritization is generated by Intelligence, the surface should explain the principal reasons and limitations.

High-consequence items should not be hidden solely because personalization predicts low interest.

Organizational policy may constrain how critical work can be filtered, snoozed, or dismissed.

---

## 12. Review Surfaces Must Present a Bounded Review Request

A Review Surface is not a general invitation to inspect a Matter.

It should present a bounded review request.

The reviewer needs to know:

- what is being reviewed;
- which version is being reviewed;
- the review scope;
- the required reviewer role;
- why review is required;
- the relevant sources;
- known missing information;
- AI involvement;
- policy omissions;
- intended downstream action;
- expiry or freshness conditions;
- whether independence or separation of duties applies.

Unsafe review presentation:

```text
Please review this filing.
```

Safer review presentation:

```text
Review version 4 of the proposed Class 9 goods/services list
for consistency with the client-confirmed business scope,
the cited jurisdiction practice, and the intended filing strategy.
This review does not authorize submission.
```

The surface should not require the reviewer to infer scope from surrounding screens.

Review context must be explicit enough to support accountable judgment.

---

## 13. Reviewer Eligibility Does Not Arise from the Review Surface

The existence of a Review button does not make the user an authorized reviewer.

Reviewer eligibility depends on:

- human identity;
- organization;
- role;
- professional qualification where applicable;
- review scope;
- Permission;
- Policy;
- responsibility assignment;
- separation-of-duty requirements;
- conflict restrictions;
- current status.

A Review Surface may show eligible reviewers or route a request toward an eligible role.

It must not create authority through interface placement.

The following remain distinct:

```text
Can see the review request

Can comment on the material

Can prepare review notes

Can perform the formal review

Can approve the downstream purpose

Can execute the downstream action
```

AI may prepare review support.

AI is not the reviewer.

An administrator may manage access.

Administration is not professional review authority.

---

## 14. Review Status, Review Decision, Approval, and Execution Must Not Collapse

A Review Surface must distinguish:

```text
Review status
→ where the review process currently is

Review decision
→ what the authorized reviewer concluded within scope

Approval boundary
→ whether a specific downstream request may be considered

Execution result
→ whether the proper service performed the action
```

A review may be `Completed` with a decision of:

- Approved;
- Rejected;
- Revised;
- Escalated;
- NeedsMoreInformation;
- NotApplicable.

`Approved` means the reviewed material satisfied the defined review scope.

It does not mean:

- the Task completed;
- the Communication sent;
- the provider was appointed;
- the filing was submitted;
- the payment occurred;
- the Matter advanced;
- the official result was recorded.

The Review Surface should display the next authority clearly.

For example:

```text
Review approved.
Separate send preparation and current authorization are still required.
```

This prevents the interface from implying that approval and action are the same event.

---

## 15. Review Must Remain Version-Specific and Purpose-Specific

A Review Surface must identify the reviewed version.

If material changes after review, the surface must not continue to show the new version as approved by inheritance.

Material changes may include:

- recipient;
- legal position;
- fee;
- deadline;
- jurisdiction;
- goods/services;
- evidence;
- attachment;
- provider;
- instruction;
- conclusion;
- intended downstream use.

The review should also remain purpose-specific.

Approval for:

```text
internal discussion
```

is not approval for:

```text
client Delivery
```

Approval for:

```text
provider recommendation
```

is not approval for:

```text
provider appointment
```

Approval for:

```text
filing preparation
```

is not approval for:

```text
official submission
```

The surface should expose version mismatch, stale review, or changed purpose rather than silently carrying forward the approval label.

---

## 16. Communication Surfaces Must Respect the Communication Lifecycle

Communication is where internal preparation may create external consequence.

A Communication Surface may display:

- incoming Communication;
- draft outgoing Communication;
- intended participants;
- channel;
- linked client, Matter, Order, Task, or provider;
- content version;
- attachments;
- sources;
- AI involvement;
- review requirement;
- approval status;
- send preparation;
- transmission result;
- delivery result;
- audit reference.

The lifecycle must remain visible:

```text
Draft
→ Review
→ Approval
→ Prepare Send
→ Send by Communication Service
→ Record
→ Audit
```

The surface may help move between these stages.

It must not collapse them into one Send button without governance.

A draft has no send authority.

A review does not transmit.

An approval is bounded to version, recipients, channel, purpose, and context.

Send preparation does not transmit.

Communication Service remains authoritative for transmission behavior and result.

---

## 17. Internal Collaboration and External Communication Are Different

Professionals often discuss work internally before communicating externally.

Internal collaboration may include:

- comments;
- annotations;
- mentions;
- internal chat;
- review notes;
- draft alternatives;
- private questions;
- AI-assisted analysis;
- escalation discussion.

These interactions are not automatically external Communications.

The architecture must preserve:

```text
Internal collaboration
≠
external Communication
```

An internal note may contain:

- uncertainty;
- candid provider evaluation;
- margin information;
- legal risk analysis;
- incomplete facts;
- AI-generated alternatives;
- client-confidential material not intended for another participant.

A Communication Surface must prevent internal content from flowing into external output by convenience.

Conversion from internal discussion to external Communication should be deliberate, versioned, and reviewable.

AI must not convert internal notes into externally attributed statements without authorized preparation and review.

---

## 18. Participant and Recipient Context Must Be Revalidated

A visible contact or previous participant does not automatically remain an authorized recipient.

Before external Communication, the operating surface should make relevant context visible, including:

- sender identity;
- sender organization;
- sender authority;
- recipient identity or safe contact reference;
- recipient role;
- relationship to client, Matter, Order, provider, or collaboration;
- channel;
- confidentiality restriction;
- attachment access;
- cross-organization policy;
- current purpose.

Reply interfaces create particular risk.

A previous email thread may contain:

- outdated recipients;
- former employees;
- copied third parties;
- a provider no longer assigned;
- a client contact whose role changed;
- a disclosure scope that no longer applies.

The surface should not treat thread continuity as current authorization.

The rule is:

```text
Previous participation
≠
current recipient authorization
```

---

## 19. Task, Review, Communication, Notification, and Event Must Remain Distinct

Operating surfaces often aggregate several kinds of activity.

The architecture must preserve the differences.

### Task

A governed unit of active work with lifecycle and responsibility.

### Review

A bounded accountable examination of defined material and scope.

### Communication

A governed message or exchange with participant, channel, content, status, and transmission meaning.

### Notification

An awareness signal delivered to a user or role.

### Event

A record that something occurred in the system or professional process.

These concepts may relate.

For example:

```text
Event: Provider response received
→ Notification: Matter owner informed
→ Task: Review provider response
→ Review: Evaluate proposed response strategy
→ Communication: Send approved instruction to client or provider
```

They must not become one generic activity stream with no semantic identity.

A Notification does not assign work.

An Event does not prove the user saw it.

A Task does not prove the related external action happened.

A Review does not send a Communication.

A Communication does not replace the Event trace.

---

## 20. Activity Streams Need Semantic and Privacy Discipline

An activity stream may help users understand recent change.

But a naive stream can become noisy, misleading, or unsafe.

The stream should distinguish:

- formal Events;
- user comments;
- Task transitions;
- review decisions;
- Communication activity;
- document versions;
- AI-assisted preparation;
- system warnings;
- presentation interactions.

Not every activity should be shown to every user.

For example:

- internal provider criticism may be restricted;
- pricing and margin events may be limited;
- AI prompt detail may not be exposed;
- client-private evidence may not appear in a team-wide stream;
- security-related access decisions may require safe summaries;
- deleted or restricted content may need reference-only history.

An activity stream is a projection of permitted trace.

It is not the raw audit log.

The rule is:

```text
Audit preserves accountable occurrence.

Activity Surface presents authorized operational meaning.
```

---

## 21. Cross-Product Aggregation Must Preserve Source References

A Workplace may aggregate activity from Lite, MarkReg, MGSN interfaces, and organization-specific applications.

For example:

```text
Lite
→ identifies a client follow-up need

MarkReg
→ holds a filing preparation journey

MGSN interface
→ presents provider candidates

Execution
→ coordinates Tasks and Review

Communication Service
→ records approved external send
```

A cross-Product surface may present these together.

It must preserve:

- source Product;
- source Object type;
- source reference;
- source status;
- current version;
- ownership;
- organization context;
- handoff state;
- available actions.

Cross-Product aggregation must not rely on uncontrolled copies that drift from the authoritative source.

The surface may cache or summarize under policy.

The authoritative reference must remain identifiable.

The principle is:

```text
Cross-Product continuity
is created through governed references and handoffs,
not by creating another competing record.
```

---

## 22. Object-Centric, Work-Centric, and Relationship-Centric Views Are Complementary

Professional work can be viewed from different centers.

### Object-centric view

Centers on a Matter, Order, Trademark, Opportunity, Document, or other object.

It answers:

```text
What is the current state of this professional object?
```

### Work-centric view

Centers on Tasks, reviews, waiting conditions, blocks, and next actions.

It answers:

```text
What work must be done?
```

### Relationship-centric view

Centers on a client, provider, partner, or organizational relationship.

It answers:

```text
What is happening in this relationship?
```

### Attention-centric view

Centers on urgency, risk, change, and user responsibility.

It answers:

```text
What requires attention now?
```

No one view replaces the others.

A Matter page is not a personal work queue.

A work queue is not a complete client history.

A client surface is not the formal Matter lifecycle.

A Today surface is not the whole Workplace.

Workplace may connect these views through stable references and authorized navigation.

---

## 23. Context Assembly for Surfaces Must Be Minimized

A surface should receive only the context required for its purpose.

A personal work queue may need:

- Task title;
- assignment;
- due context;
- safe client reference;
- risk signal;
- next allowed action.

It may not need:

- all client evidence;
- all pricing history;
- all provider notes;
- all internal knowledge;
- all Communications.

A review surface may need more detailed evidence and version context.

A management surface may need aggregated patterns rather than sensitive item-level content.

A client portal may need a safe status and required client action without internal debate or provider evaluation.

The architectural rule is:

```text
Surface context
=
minimum authorized context for the surface purpose
```

A richer interface does not justify broader access.

Surface design must remain subordinate to Workplace Context, Permission, Policy, client restriction, and professional responsibility.

---

## 24. AI May Summarize and Assist Operating Surfaces Under Governance

AI can make operating surfaces more useful.

It may:

- summarize active work;
- explain why an item appears;
- group related Tasks;
- identify possible duplicates;
- summarize a Communication thread;
- compare versions;
- identify missing context;
- prepare review questions;
- explain a blocked condition;
- suggest a next action;
- generate a safe status summary;
- help the user navigate related context.

But AI assistance creates specific risks.

AI must not:

- turn a work signal into an active Task silently;
- represent a Recommendation as an assignment;
- mark a Task complete;
- complete a Review;
- infer approval from inactivity;
- select final external recipients;
- send a Communication;
- hide stale or conflicting source status;
- summarize away a critical exception;
- expose restricted context;
- present confidence as professional truth.

AI-generated surface summaries should preserve:

- source scope;
- freshness;
- missing context;
- uncertainty;
- restricted omissions;
- source references where consequence matters;
- Human Review requirements;
- downstream authority.

An AI summary is a convenience layer.

It does not replace the source record.

---

## 25. Recommendations and Next Best Actions Must Remain Candidate Guidance

A surface may present recommendations or Next Best Actions.

Examples include:

- request missing client documents;
- review an approaching deadline;
- follow up with a provider;
- prepare a renewal recommendation;
- create a Task;
- begin a MarkReg intake;
- compare MGSN provider candidates;
- prepare a client Communication.

These suggestions may be highly valuable.

They remain candidates until the user or governed service accepts them.

The surface should show:

- why the action is suggested;
- the evidence or rule behind it;
- whether the source is current;
- what is missing;
- the expected consequence;
- whether confirmation is required;
- whether Task creation, Review, or Execution will follow;
- whether the action may be dismissed or deferred;
- whether policy requires escalation.

The surface must not create a hidden path:

```text
Recommendation
→ automatic protected action
```

The safe path is:

```text
Recommendation
→ explanation
→ user evaluation
→ authorized confirmation
→ governed request
→ Execution or Owning Service
```

Detailed recommendation and Next Best Action architecture belongs to CH17.

This chapter establishes only how those candidates appear safely in operating surfaces.

---

## 26. Surface Actions Capture Intent and Initiate Governed Handoff

An operating surface may contain buttons or commands such as:

- create Task;
- assign;
- start work;
- request review;
- approve;
- prepare Communication;
- send for approval;
- prepare filing;
- select provider candidate;
- escalate;
- archive;
- dismiss recommendation.

The button itself is not the authority.

A user action in the interface should be understood as:

```text
captured intent
or
a request to an authoritative service
```

The downstream authority must still validate:

- identity;
- organization;
- role;
- Permission;
- Policy;
- responsibility;
- object state;
- version;
- review requirement;
- idempotency;
- current context.

The surface should return the actual result:

```text
Task created
```

or:

```text
Task creation rejected because a duplicate active Task already exists
```

or:

```text
Review required before this request can proceed
```

The surface must not display optimistic success before the authoritative service accepts the request.

---

## 27. Waiting, Blocked, Failed, and Escalated Conditions Need Clear Presentation

Professional work often does not progress linearly.

A surface should distinguish:

### Waiting

Progress depends on an expected response, date, information, or external condition.

### Blocked

A known condition prevents progress.

### Failed

An attempted operation did not complete successfully.

### Escalated

Responsibility or attention has been elevated because of risk, delay, conflict, or policy.

These conditions must not be reduced to one red warning icon.

The user should understand:

- what happened;
- which source recorded it;
- who is responsible;
- what is needed;
- whether retry is permitted;
- whether review is required;
- whether a deadline is affected;
- whether an external party is involved;
- what safe next actions exist.

A failed external action should not appear as completed because the user clicked once.

A retry should not create duplicate Tasks, Communications, filings, provider instructions, or payments.

The surface may simplify technical error detail.

It must preserve operational truth and safe recovery paths.

---

## 28. Critical Exceptions Must Not Be Hidden by Personalization

Personalization may help users manage attention.

But critical professional items must remain protected from accidental invisibility.

Examples include:

- official deadline risk;
- permission denial;
- review rejection;
- failed filing attempt;
- failed payment;
- provider instruction failure;
- confidentiality warning;
- missing responsible owner;
- stale approval;
- version mismatch;
- blocked evidence requirement;
- unresolved client instruction conflict.

Policy may require that such items:

- remain visible;
- require acknowledgment;
- cannot be dismissed permanently;
- escalate after a period;
- appear to a responsible owner;
- generate a Notification;
- create or propose a Task;
- remain in audit trace.

The interface should distinguish:

```text
user preference
from
organizational obligation
```

A clean dashboard is not more important than visible professional risk.

---

## 29. External Collaborator and Client Surfaces Must Be Purpose-Limited

A Workplace may provide surfaces to:

- clients;
- foreign associates;
- service providers;
- partner agencies;
- external reviewers;
- invited consultants.

These participants may need to:

- supply information;
- upload Documents;
- review a defined item;
- confirm an instruction;
- view safe progress;
- respond to a request;
- receive an approved outcome.

They do not need the full internal Workplace.

External surfaces should be limited by:

- relationship;
- role;
- invitation;
- object scope;
- time;
- purpose;
- data class;
- confidentiality;
- Product context;
- revocation conditions.

An external collaborator should not gain access to other clients, internal provider comparisons, pricing margins, unrelated Communications, private knowledge, or management views.

A client status surface should not expose internal uncertainty as confirmed fact.

An external provider surface should not imply that assignment equals authority beyond the defined service scope.

The rule is:

```text
External participation receives the minimum governed surface,
not a reduced copy of the whole Workplace.
```

---

## 30. Management Surfaces Need Aggregation Without Surveillance

Managers need visibility into organizational operation.

Useful management views may include:

- workload distribution;
- unassigned work;
- deadline exposure;
- review backlog;
- blocked Tasks;
- provider-response delay;
- recurring quality issues;
- Communication bottlenecks;
- service conversion;
- unresolved responsibility;
- capacity and skill gaps.

But management visibility must remain governed.

It should not become unlimited access to:

- all private client content;
- all legal analysis;
- all personal notes;
- all AI conversations;
- all employee activity;
- all confidential Evidence;
- all provider criticism.

A management surface should prefer the least sensitive information that supports the management purpose.

It should distinguish operational metrics from professional judgment.

For example:

```text
Review queue aging
```

may be visible without exposing every review comment.

```text
Provider response delay
```

may be visible without exposing unrelated confidential Communications.

Management authority is not universal knowledge access.

---

## 31. Operating Surfaces Must Preserve Historical Explainability

Current views support current work.

Historical views explain past work.

A surface should avoid rewriting history through current labels, current assignments, or current policy.

For example, a past action may have used:

- an earlier organization identity;
- a former reviewer;
- an older Task status model;
- a previous Communication version;
- a different provider;
- an earlier policy;
- a former client instruction;
- an older Product journey.

Historical surfaces should preserve enough context to answer:

```text
What did the user see at the time?

Which status was authoritative?

Which version was reviewed?

Who was responsible?

Which policy applied?

What action actually occurred?
```

This does not mean every presentation preference must be preserved forever.

It means that professional records and consequential decisions must remain explainable under the context active when they occurred.

---

## 32. Local and Offline Surfaces Remain Governed

A Workplace may expose operating surfaces through local applications, cached views, offline tools, or Local Vault-supported experiences.

Local presentation does not remove governance.

A local surface must still consider:

- identity;
- device context;
- organization scope;
- data classification;
- synchronization freshness;
- stale status risk;
- permission revocation;
- local encryption and access;
- pending outbound actions;
- conflict resolution;
- audit requirements.

An offline Task view may be stale.

An offline review package may no longer match the current version.

A locally prepared Communication may require fresh recipient and Policy validation before send.

A local success indicator must not imply cloud or external execution occurred.

Detailed Local Vault and synchronization architecture belongs to CH12.

The boundary established here is:

```text
Local availability
≠
current authority or confirmed external result
```

---

## 33. The Minimum Operating Surface Model

A minimum conceptual model can be expressed as:

```text
Authoritative Sources
  │
  ├── Core Objects and Owning Services
  ├── Execution Workflows and Tasks
  ├── Human Review and Approval records
  ├── Communication lifecycle and results
  ├── Events, Notifications, and audit trace
  ├── Workplace identity, roles, responsibility, and policy
  ├── clients, relationships, and service context
  └── private knowledge and AI Context
        │
        ▼
Authorized Surface Assembly
  │
  ├── source selection
  ├── permission and policy filtering
  ├── role and purpose filtering
  ├── safe summarization
  ├── grouping and prioritization
  ├── freshness and version checks
  └── explanation and source reference
        │
        ▼
Operating Surfaces
  │
  ├── Attention / Today
  ├── Work Queue
  ├── Review Queue
  ├── Communication Center
  ├── Object / Matter View
  ├── Relationship View
  ├── Exception View
  ├── Management View
  └── External Participation View
        │
        ▼
User Understanding and Intent
        │
        ▼
Governed Request
        │
        ▼
Execution or Owning Service
        │
        ▼
Formal Result and Event Trace
```

The model is architectural.

It does not require one dashboard framework, one front-end repository, one state-management library, one notification service, or one Product shell.

---

## 34. Required Distinctions

This chapter establishes the following distinctions:

```text
Operating Surface ≠ Source of Truth
```

A surface projects authoritative state; it does not own that state by visibility.

```text
Work Item ≠ Task
```

A generic card may represent a signal, suggestion, review, Notification, Communication, or Task.

```text
Work Signal ≠ Active Task
```

Possible work becomes active only when Task Service accepts creation.

```text
Presentation State ≠ Business State
```

Read, pinned, hidden, dismissed, and snoozed do not change formal object state.

```text
Displayed Priority ≠ Formal Priority
```

Personal or AI ranking does not silently update Task priority or deadline.

```text
Review Surface ≠ Reviewer Authority
```

Authority depends on identity, role, Permission, Policy, scope, and professional responsibility.

```text
Review Decision ≠ Execution Result
```

Approved material may still require current gates and service execution.

```text
Internal Collaboration ≠ External Communication
```

Internal comments and AI analysis do not become external statements automatically.

```text
Communication Draft ≠ Approved Communication
```

Drafting, review, approval, send preparation, transmission, and recordal remain separate.

```text
Notification ≠ Task
```

Awareness does not automatically create responsibility.

```text
Event ≠ User Acknowledgment
```

An occurrence record does not prove that a user saw or accepted it.

```text
Surface Action ≠ Formal Mutation
```

The interface captures intent; authoritative services validate and act.

```text
Cross-Product Aggregation ≠ New System of Record
```

Continuity depends on governed references rather than duplicate authority.

---

## 35. Failure Modes This Chapter Prevents

### Dashboard authority drift

The dashboard becomes the practical source of truth even when its state differs from authoritative services.

### Generic work-item collapse

Tasks, recommendations, reviews, Notifications, and Communication drafts are presented as one object with one misleading lifecycle.

### Presentation-state mutation

Dismiss, snooze, read, or drag-and-drop actions silently alter formal business state.

### Hidden active work creation

AI recommendations or deadline signals appear as assigned Tasks without Task Service creation.

### Friendly-status divergence

Product labels become incompatible replacements for canonical status values.

### Review-action collapse

A review button implies reviewer authority, and approval implies execution.

### Communication shortcut

Draft, review, approval, send preparation, and transmission collapse into one interface action.

### Internal-content leakage

Internal comments, private notes, provider criticism, or AI analysis enter external Communication accidentally.

### Recipient inheritance

Previous thread participants are treated as automatically authorized recipients.

### Critical-risk suppression

Personalization hides deadlines, failures, rejected reviews, or permission problems.

### Cross-Product duplication

Each Product copies Tasks, review state, Communication, and relationship context into its own competing store.

### AI summary substitution

A generated summary becomes more trusted than the authoritative source and hides uncertainty or stale context.

### Management surveillance

Operational visibility becomes unrestricted access to private content and individual activity.

### Offline false confidence

A local screen shows success or current status when synchronization or external execution has not occurred.

These failures often improve superficial usability while weakening professional truth, accountability, and trust.

---

## 36. Minimum Conformance Rule

A conforming Workplace should preserve the following rule:

```text
Operating surfaces present authorized projections
of work, review, Communication, context, and attention.

Every surface item preserves its underlying semantic type,
source reference, current authoritative status, and ownership.

Work signals, recommendations, Task plans, and active Tasks
remain distinct.

Presentation state remains separate from business state.

Task lifecycle remains owned by Task Service.

Review eligibility remains based on identity, role,
Permission, Policy, scope, and professional responsibility.

Review status, review decision, approval,
and downstream execution remain distinct.

Communication draft, review, approval, send preparation,
transmission, recordal, and audit remain distinct.

Internal collaboration does not become external Communication
without deliberate governed preparation.

Notifications, Events, Tasks, Reviews,
and Communications remain distinguishable.

Cross-Product aggregation preserves source references
and does not create a new system of record.

AI may summarize, explain, group, and recommend,
but must preserve sources, limitations, freshness,
restricted omissions, and Human Review requirements.

Surface actions capture intent and invoke governed services.
They do not create authority by interface placement.

Critical professional exceptions cannot be hidden
solely by user preference or personalization.

External and management surfaces remain purpose-limited.

Humans remain accountable.

Execution coordinates consequential work.

Owning Services change formal business facts.

Events and audit preserve trace.
```

Different Workplace editions and Products may use different navigation, information density, visual language, ranking, grouping, and interaction patterns.

They may not create different authority models.

---

## 37. Chapter Boundary

This chapter defines how Workplace makes organizational work, review, Communication, attention, and exceptions visible through governed operating surfaces.

It does not define:

- final Product screen designs;
- user-interface component libraries;
- dashboard layouts;
- visual design systems;
- front-end frameworks;
- client-side state-management technology;
- notification delivery infrastructure;
- search implementation;
- final ranking formulas;
- final Next Best Action algorithms;
- Workflow implementation;
- Task status values;
- Review decision values;
- Communication transport;
- email provider integration;
- chat integration;
- Event storage;
- audit storage;
- Local Vault implementation;
- synchronization protocols;
- offline conflict resolution;
- final management metrics;
- autonomous protected action.

Data boundaries, Local Vault, and authorized synchronization belong to CH12.

Information access, provenance, and context assembly are developed further in CH13.

Capability discovery and Skill selection belong to CH15.

Assistant, Guide, and AI Agent interaction belongs to CH16.

Recommendations and Next Best Action belong to CH17.

Prepared-action handoff belongs to CH18.

Human Review, approval, and Owning Service handoff belong to CH19.

Product-specific surfaces and embedding belong to Part IV.

Artifact review, Delivery, and Publish surfaces belong to Part V.

Cross-Workplace collaboration surfaces belong to Part VI.

This chapter does not modify Book 02 Task, Review, Communication, Notification, Event, Permission, Policy, or Business Responsibility semantics.

It does not modify Book 03 Workflow, Task, Human Review, Communication execution, or protected-action authority.

---

## 38. Chapter Conclusion

A professional organization needs more than correct records and governed Workflows.

It needs a coherent operating environment in which people can see what requires attention, understand what is active, recognize what is only proposed, perform bounded review, prepare Communication, identify exceptions, and initiate governed action.

Workplace provides that operating environment through surfaces.

But the surface must remain a projection rather than a substitute authority.

The architecture can be summarized as:

```text
Authoritative professional state
→ Core Objects, Execution, Review, Communication, and Events

Authorized Workplace Context
→ organization, user, role, client, policy, knowledge, and purpose

Operating Surface
→ role-aware projection, grouping, explanation, and interaction

User Intent
→ confirm, prepare, request, review, escalate, or navigate

Governed Handoff
→ Execution or the proper Owning Service

Formal Result
→ authoritative state change and trace
```

A conforming Workplace must preserve:

- clear semantic identity for every surfaced item;
- separation between signals, recommendations, and active Tasks;
- separation between presentation state and business state;
- source-linked Task and Workflow visibility;
- bounded and version-specific Review surfaces;
- distinction among review, approval, and execution;
- governed Communication stages;
- separation of internal collaboration from external Communication;
- recipient and disclosure revalidation;
- distinction among Tasks, Reviews, Communications, Notifications, and Events;
- cross-Product continuity through references rather than competing records;
- purpose-limited context assembly;
- AI assistance with source, freshness, limitation, and review disclosure;
- visible waiting, blocked, failed, and escalated conditions;
- protection of critical professional exceptions;
- limited external and management views;
- historical explainability;
- governed local and offline presentation;
- human professional accountability.

This allows MarkOrbit to provide a unified daily operating experience without centralizing every Product, duplicating every object, or allowing interface convenience to redefine professional truth.

With work, review, Communication, and operating surfaces established, Part II can move to the data boundary that supports them: which information remains local or private, which information may synchronize, and under which authorization that movement may occur.
