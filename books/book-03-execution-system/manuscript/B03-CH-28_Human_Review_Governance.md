# B03-CH-28 — Human Review Governance

**Status:** Release Candidate 1

## Chapter Purpose

Human Review is the accountable control that prevents preparation, automation, AI assistance and workflow coordination from becoming professional authority by themselves.

A system may validate structure, compare versions, extract facts, detect conflicts, prepare drafts and recommend next steps. None of those actions proves that the intended professional decision is correct, authorized or suitable for protected execution.

The governing principle is:

```text
Machines may prepare.
Humans must review what requires accountable judgment.
Approval must remain bound to the exact version, scope and intended action.
```

This chapter defines how the MarkOrbit Execution System coordinates Human Review across preparation, protected action, change, uncertainty, exception and escalation.

It does not define reviewer user interfaces, staffing models, employment roles, professional licensing rules, legal-opinion standards, queue implementation or organizational approval charts.

The core governance path is:

```text
review need identified
→ exact subject, version and intended action bound
→ reviewer eligibility and independence checked
→ sources, assumptions and unresolved issues disclosed
→ reviewer examines the governed material
→ reviewer approves, rejects, requests revision, abstains or escalates
→ decision scope and conditions recorded
→ apply revalidates version, Permission, Policy and review status
→ owning Service performs any allowed mutation
→ Event and audit references preserve accountability
```

Human Review is not a decorative checkpoint.

It is the mechanism by which professional judgment remains attributable, bounded and reviewable.

---

## 1. Dependency Baseline

This chapter builds directly on Chapters 12, 15, 16, 25–27 and 29. Its primary Book 02 dependencies are the approved Human Review, Permission, Policy, versioning, audit, idempotency, error and AI Context contracts, together with the relevant Task, Communication and Workflow API contracts.

Book 02 owns canonical structures, controlled values and Service behavior. This chapter defines only how Execution consumes them.

## 2. Review, Approval, Authorization and Execution Are Different

These terms must remain distinct.

| Term | Governance meaning |
|---|---|
| Review | Accountable examination of a defined subject, version, evidence base and intended action |
| Approval | A governed decision that the reviewed subject may proceed within a defined scope and conditions |
| Rejection | A governed decision that the reviewed subject may not proceed in its current form |
| Revision request | A decision that changes are required before a new review decision |
| Authorization | Permission to perform a protected action under applicable Policy and role constraints |
| Apply | A protected execution request based on current contracts, state and review |
| Execution | Coordination and performance of the approved action by the owning Service |
| Sign-off | A recorded accountable decision; it must not be treated as a generic or transferable credential |
| Acknowledgment | Confirmation that information was received or seen; it is not approval |
| Consultation | Advice or input from another person; it does not automatically satisfy the required review |
| Validation | Structural or contract checking; it is not Human Review |
| AI assistance | Machine-supported preparation or analysis; it is not Human Review |

A reviewer may approve a draft without being authorized to send it.

A person may be authorized to send without being qualified to review professional content.

A Workflow may verify that review exists without becoming the reviewer.

A Product confirmation click is not Human Review unless the governing contract defines the actor, scope, version and decision.

---

## 3. Why Human Review Exists

Human Review is required where execution depends on judgment that cannot be safely reduced to structural validation.

Typical reasons include:

- legal or professional consequence;
- financial consequence;
- external Communication;
- official submission;
- Evidence sufficiency;
- provider selection;
- interpretation of conflicting Knowledge;
- exception to ordinary Policy;
- change affecting approved meaning;
- uncertain or partial execution outcome;
- AI-assisted preparation;
- sensitive data disclosure;
- irreversible action;
- deadline-sensitive decision;
- action affecting another person's rights or obligations.

Human Review protects against several failure modes.

### 3.1 Preparation Mistaken for Authority

A complete-looking package may still be incorrect.

A well-written Communication may still be inappropriate to send.

A provider comparison may still omit a material commercial or professional constraint.

A passing validator may still rely on wrong facts.

### 3.2 Automation Bias

Users may over-trust:

- high-confidence AI output;
- complete forms;
- green readiness indicators;
- machine-generated recommendations;
- provider rankings;
- automatically calculated deadlines;
- prior successful patterns.

Human Review must create a deliberate point where the reviewer examines the underlying subject, not merely the system's confidence.

### 3.3 Accountability Gap

Without explicit Human Review, responsibility becomes ambiguous.

The system must not leave the professional record implying that:

```text
the Workflow decided
the AI approved
the system selected
the Product authorized
```

Accountable decisions must remain attributable to a human actor acting within authorized scope.

---

## 4. The Review Subject

A review is valid only when its subject is explicit.

The subject may include:

- Core object reference;
- content version;
- Document version;
- Evidence set;
- Communication package;
- application package;
- provider comparison;
- response strategy;
- renewal instruction;
- assignment package;
- Task result;
- Workflow transition proposal;
- change proposal;
- exception request;
- reconciliation conclusion.

The review subject must be narrow enough that the reviewer can understand what the decision covers.

### 4.1 Subject Completeness

A review request should identify:

```text
what is being reviewed
which version is being reviewed
why review is required
which action may follow
which sources and assumptions were used
which issues remain unresolved
which constraints apply
what the reviewer is being asked to decide
```

A review request must not hide material uncertainty behind a concise summary.

### 4.2 Composite Review Packages

A review package may contain multiple components.

For example:

```text
Communication body
recipient set
attachments
send channel
purpose
source Matter
deadline context
```

Approval of one component does not automatically approve all components.

The review package must state whether the reviewer is approving:

- content only;
- legal strategy only;
- factual accuracy only;
- send package;
- provider selection;
- external submission;
- full protected action.

### 4.3 Review Subject Must Not Change Silently

If the subject changes after review begins, Execution must:

1. create or identify the new version;
2. preserve the prior review context;
3. show the change where relevant;
4. determine whether the original review remains applicable;
5. require renewed review for material changes.

A reviewer must not unknowingly decide on a moving target.

---

## 5. Version and Scope Binding

Human Review must be bound to the exact version and scope that the reviewer examined.

A review binding may include:

- subject reference;
- subject version;
- related object versions;
- source versions;
- intended action;
- jurisdiction;
- recipient or provider;
- amount or fee;
- attachment versions;
- review purpose;
- reviewer identity or capability;
- decision;
- decision time;
- conditions;
- expiry;
- revocation status;
- applicable Permission and Policy context.

This is a conceptual governance set. Book 03 does not define a new Core schema.

### 5.1 Exact-Version Rule

The governing rule is:

```text
Reviewed version must equal the version presented for protected apply,
unless an explicit compatibility rule and accountable decision permit otherwise.
```

### 5.2 Scope Rule

Approval scope must not expand silently.

Examples:

- approval to prepare is not approval to file;
- approval to send one Communication is not approval to send a revised Communication;
- approval of one provider is not approval of another;
- approval for one jurisdiction is not approval for another;
- approval of one fee is not approval of a changed fee;
- approval of a classification proposal is not approval of every later goods/services revision.

### 5.3 Time Rule

Review may become stale because:

- deadline context changed;
- external status changed;
- Knowledge changed;
- provider terms changed;
- Policy changed;
- source Documents changed;
- review validity period ended;
- the reviewer revoked the decision;
- a new material fact appeared.

Human Review must not be treated as permanently valid by default.

---

## 6. Reviewer Eligibility

Not every human is an eligible reviewer for every decision.

Eligibility may depend on:

- Permission;
- Policy;
- organizational role;
- professional capability;
- jurisdiction knowledge;
- Matter relationship;
- independence;
- conflict status;
- data-access authority;
- delegation;
- review level;
- value or risk threshold.

Book 02 owns the canonical identity, capability, Permission and Policy contracts.

Execution must consume them.

### 6.1 Authentication Is Not Qualification

A logged-in user is not automatically an eligible reviewer.

### 6.2 Seniority Is Not Universal Authority

A senior actor may still lack:

- subject expertise;
- jurisdiction capability;
- independence;
- access to required Evidence;
- approval authority for the specific action.

### 6.3 Participation Is Not Review Authority

A person who prepared the content may provide context but may not satisfy a required independent review.

### 6.4 Eligibility Must Be Evaluated at Decision Time

Eligibility may change between assignment and decision.

Execution should re-evaluate current Permission and Policy before accepting the review decision.

---

## 7. Independence and Separation of Duties

Some decisions require a person other than the preparer or executor.

The purpose is not bureaucracy. It is to reduce self-confirmation and concentration of authority.

Possible separation patterns include:

```text
preparer ≠ reviewer
reviewer ≠ sender
requester ≠ approver
provider recommender ≠ provider approver
payment preparer ≠ payment approver
migration author ≠ migration approver
AI-output editor ≠ independent reviewer
```

The exact requirement belongs to Policy and domain governance.

### 7.1 Self-Review

Self-review may be permitted for low-risk work under explicit Policy.

It must not be assumed.

### 7.2 Independent Review

Independent review may be required when:

- action is irreversible;
- value exceeds threshold;
- confidential data will be disclosed;
- official rights are affected;
- exception is requested;
- AI produced material content;
- the preparer has a conflict;
- prior execution failed or became uncertain.

### 7.3 Two-Person Control

Some actions may require two accountable decisions.

Examples:

- high-value payment;
- material provider engagement;
- filing under changed instructions;
- emergency Policy exception;
- destructive migration;
- release of sensitive Evidence.

Two clicks by the same person do not satisfy two-person control.

### 7.4 Separation Must Persist Through Execution

It is not enough to separate roles during review if the same actor can later bypass the result through an unrestricted administrator path.

Any override must itself be governed.

---

## 8. Conflict of Interest

A reviewer may be unable to act impartially because of:

- personal interest;
- commercial incentive;
- provider relationship;
- client conflict;
- authorship of disputed work;
- performance target;
- prior commitment;
- family or organizational relationship;
- responsibility for the failure being reviewed;
- role in the external transaction.

Execution should allow conflict disclosure and reassignment where required.

### 8.1 Conflict Disclosure Is Not Automatic Disqualification

Policy determines whether a disclosed conflict:

- is acceptable;
- requires another reviewer;
- requires additional review;
- prohibits participation.

### 8.2 Hidden Conflict

The system may not know every conflict.

The review process should require the human actor to make an accountable declaration where the consequence warrants it.

### 8.3 AI Cannot Determine Human Impartiality

AI may identify possible relationships from governed data.

It may not declare a reviewer independent or conflicted as final professional truth.

---

## 9. Review Request Lifecycle

A review request is not merely a Task title.

It is a governed request for an accountable decision.

A conceptual lifecycle may include:

```text
prepared
→ requested
→ assigned
→ accepted
→ in review
→ revision requested
→ resubmitted
→ approved, rejected, abstained or escalated
→ expired, revoked or superseded where applicable
```

The controlled statuses belong to Book 02.

### 9.1 Prepared

The review package is assembled but has not yet entered accountable review.

### 9.2 Requested

The exact subject, version and decision request are fixed for the review.

### 9.3 Assigned

An eligible reviewer is identified.

Assignment does not equal acceptance or decision.

### 9.4 In Review

The reviewer is examining the package.

Execution must avoid changing the subject silently.

### 9.5 Revision Requested

The reviewer identifies required changes.

The revised package becomes a new version and requires renewed review.

### 9.6 Decision

The reviewer records a governed outcome.

### 9.7 Expired, Revoked or Superseded

A prior decision may cease to authorize future action while remaining historically preserved.

---

## 10. Review Inputs and Evidence Sufficiency

A reviewer needs enough information to make the requested decision.

A review package may include:

- source Documents;
- Evidence;
- object state;
- version comparison;
- deadline context;
- jurisdiction context;
- provider terms;
- fee information;
- prior decisions;
- unresolved issues;
- AI assistance disclosure;
- assumptions;
- limitations;
- related Events;
- audit references.

### 10.1 Completeness Disclosure

The package should state what is missing.

Unsafe:

```text
Ready for approval.
```

when important sources are unavailable.

Safer:

```text
Prepared for review.
Official fee confirmation is unavailable.
The deadline source is secondary and requires professional confirmation.
```

### 10.2 Source Quality

A reviewer should be able to distinguish:

- official source;
- provider source;
- client statement;
- internal Knowledge;
- prior Matter;
- AI extraction;
- inferred value;
- unverified external content.

Presentation must not make all sources appear equally authoritative.

### 10.3 Evidence Presence vs Evidence Sufficiency

The existence of Evidence does not prove that it supports the intended proposition.

Human Review may need to assess:

- relevance;
- authenticity;
- date;
- jurisdiction;
- ownership;
- continuity;
- consistency;
- admissibility;
- completeness;
- contradiction.

### 10.4 Hidden Assumptions

Assumptions that affect the decision should be explicit.

Examples:

- applicant identity inferred from prior Matter;
- deadline calculated from an unverified event date;
- provider fee assumed to include disbursements;
- Communication recipient assumed authorized;
- use Evidence assumed to relate to the correct mark.

---

## 11. Review Decision Classes

A review decision should be specific enough to govern next action.

Possible decision classes include:

### 11.1 Approve

The reviewed subject may proceed within the defined scope and conditions.

Approval does not execute the action.

### 11.2 Approve With Conditions

The subject may proceed only if defined conditions are satisfied.

Conditions must be objectively verifiable where possible.

Examples:

- remove a disputed attachment;
- confirm applicant address;
- use only the approved provider;
- do not send before a stated date;
- require final fee confirmation;
- limit filing to approved goods/services.

### 11.3 Reject

The subject must not proceed in its current form.

Rejection should identify enough reason to support correction or closure without exposing restricted information.

### 11.4 Revision Requested

The reviewer requests changes and expects a new version.

The prior review does not approve the revised version.

### 11.5 Abstain

The reviewer declines to decide because of:

- conflict;
- insufficient expertise;
- insufficient information;
- lack of authority;
- procedural concern.

Abstention is not rejection.

### 11.6 Escalate

The reviewer determines that another level or capability is required.

Escalation does not authorize the action.

### 11.7 No Decision

A timed-out or abandoned review is not approval.

Silence must not be interpreted as consent unless an explicit, lawful and governed contract says otherwise.

For protected professional actions, approval should be explicit.

---

## 12. Conditions, Reservations and Dissent

Human Review should preserve nuance without becoming ambiguous.

### 12.1 Conditions

A condition should identify:

- required action;
- responsible actor;
- verification method;
- time or scope;
- effect if unsatisfied.

Vague conditions such as “please double-check” are not sufficient for a protected apply gate.

### 12.2 Reservations

A reviewer may approve while recording a reservation.

Execution must determine whether the reservation:

- is informational;
- limits scope;
- requires another review;
- blocks apply;
- creates an exception.

Product presentation must not hide a material reservation.

### 12.3 Dissent

Where multiple reviewers participate, dissent must be preserved.

The system must not replace:

```text
one approval, one rejection
```

with:

```text
review complete
```

Policy must determine whether the decision requires:

- unanimity;
- majority;
- designated final authority;
- escalation;
- no unresolved objection.

### 12.4 Reviewer Comments Are Not Automatically Instructions

A comment may be:

- observation;
- question;
- recommendation;
- required change;
- condition;
- professional opinion.

The review decision should identify which comments are binding for execution.

---

## 13. Review Depth and Proportionality

Human Review should be proportionate to risk, complexity and consequence.

A useful conceptual model is:

| Review depth | Typical purpose |
|---|---|
| Confirmation | Verify a narrow fact or unchanged version |
| Standard review | Examine correctness and readiness of ordinary work |
| Enhanced review | Address material risk, AI assistance, uncertainty or external consequence |
| Specialist review | Apply domain or jurisdiction expertise |
| Independent review | Separate preparer and reviewer |
| Multi-party review | Require more than one accountable decision |
| Emergency review | Decide under time pressure with constrained scope |
| Retrospective review | Examine action already taken or uncertain outcome |

This does not define controlled values unless Book 02 formalizes them.

### 13.1 Low Risk Does Not Mean No Accountability

A lighter review may still need:

- exact subject;
- reviewer identity;
- decision;
- time;
- scope;
- trace.

### 13.2 High Risk Requires More Than More Fields

Enhanced review is not achieved by adding a longer checklist alone.

It may require:

- specialist capability;
- independent reviewer;
- source verification;
- second approval;
- conflict declaration;
- explicit uncertainty analysis;
- deadline review;
- direct inspection of original Documents.

### 13.3 Repeated Success Does Not Remove Review Automatically

A familiar pattern may reduce effort.

It does not remove Human Review where Policy still requires it.

---

## 14. Multiple Reviewers and Quorum

Some review decisions require more than one reviewer.

The review model should identify:

- required number of reviewers;
- required capabilities;
- independence requirements;
- order, if any;
- quorum;
- conflict rules;
- how abstention affects quorum;
- how dissent is resolved;
- final decision authority;
- whether one review may invalidate another.

### 14.1 Sequential Review

One reviewer acts after another.

Examples:

```text
professional review
→ commercial approval
→ send authorization
```

Later approval must not silently cure defects in earlier review.

### 14.2 Parallel Review

Multiple reviewers examine the same version independently.

If the subject changes during parallel review, all affected reviews may become stale.

### 14.3 Quorum

Quorum must be evaluated on eligible, completed decisions.

An assigned reviewer who did not decide does not count.

### 14.4 Final Authority

A designated final authority may resolve disagreement only within Policy.

It must not erase dissent from audit.

---

## 15. Delegation and Substitution

A reviewer may delegate or be replaced only where the governing model permits it.

### 15.1 Delegation

Delegation should identify:

- delegator;
- delegate;
- scope;
- time period;
- capability;
- limits;
- reason;
- revocation.

Delegation of review responsibility does not necessarily delegate send, payment or filing authority.

### 15.2 Substitution

Substitution may be required because of:

- absence;
- conflict;
- workload;
- deadline;
- changed capability;
- revoked Permission.

The substitute reviewer must receive the full governed package.

### 15.3 No Informal Proxy

A colleague's verbal confirmation, chat message or email may provide evidence, but it should not be transformed into a formal review decision unless the contract permits and the required context is captured.

### 15.4 AI Is Not a Delegate

An AI assistant cannot receive delegated Human Review authority.

---

## 16. Review Freshness, Expiry and Revocation

A review decision may cease to authorize future execution.

### 16.1 Freshness

Freshness depends on:

- elapsed time;
- change in source;
- change in object state;
- change in Policy;
- change in deadline context;
- change in provider terms;
- change in external status;
- new material fact;
- changed intended action.

### 16.2 Expiry

Some approvals may have an explicit validity window.

Expiry does not delete the decision.

It ends its authority for future apply.

### 16.3 Revocation

An authorized reviewer or governance authority may revoke a decision where permitted.

Revocation should identify:

- decision being revoked;
- reason;
- time;
- scope;
- affected operations;
- whether any action already occurred;
- required remediation or escalation.

### 16.4 Supersession

A later review decision may supersede an earlier one for the same governed subject and scope.

Historical decisions remain traceable.

### 16.5 Pending Apply

If revocation or expiry occurs before apply, Execution must block apply.

If apply already occurred, revocation does not erase the action. It may trigger a separate remediation process.

---

## 17. Review Before Retry, Recovery and Change

Human Review is especially important after execution disturbance.

### 17.1 Retry

A retry may require renewed review when:

- version changed;
- recipient changed;
- provider changed;
- amount changed;
- previous effect is uncertain;
- deadline context changed;
- prior approval expired;
- Policy changed.

### 17.2 Safe Failure Recovery

Recovery from partial or uncertain failure may require a reviewer to decide:

- whether to continue;
- whether to reconcile further;
- whether to compensate;
- whether to communicate externally;
- whether to create a new Task;
- whether to stop.

The reviewer must see confirmed, absent and uncertain effects.

### 17.3 Change Control

A material change may require review of:

- the change itself;
- activation;
- affected work;
- migration;
- rollback;
- emergency restriction.

Approval of the change does not automatically approve every affected execution.

---

## 18. Deadline-Sensitive Review

Deadlines create pressure to weaken review.

The governance rule is the opposite:

```text
Time pressure may shorten the review window.
It must not silently erase the review requirement.
```

### 18.1 Deadline Context

The review package should disclose:

- deadline source;
- date and timezone;
- confidence;
- jurisdiction;
- extension possibility where verified;
- latest safe action time;
- unresolved uncertainty;
- consequence of delay.

### 18.2 Escalation

When ordinary review cannot complete in time, Execution may:

- escalate;
- prioritize;
- narrow the requested decision;
- prepare an emergency review package;
- preserve attempted action and evidence.

Execution must not:

- self-approve;
- allow AI to decide;
- submit based on an unreviewed draft;
- certify an uncertain deadline;
- treat silence as consent.

### 18.3 Narrow Emergency Decision

An emergency reviewer may approve only a constrained action.

Examples:

- send a deadline-preserving inquiry;
- file a minimal protective submission where professionally allowed;
- pause provider instruction;
- block an unsafe channel.

The emergency decision must state its limited scope.

---

## 19. Review Quality and Accountability

Human Review can fail even when the formal steps are complete.

Common quality failures include:

- rubber-stamping;
- reviewing only the summary;
- relying on AI confidence;
- ignoring unresolved issues;
- approving without source access;
- using stale Knowledge;
- approving outside expertise;
- approving a different version;
- treating checklist completion as judgment;
- failing to disclose conflict.

### 19.1 Evidence of Review

The system should preserve enough evidence to establish that the reviewer had:

- the correct subject;
- the relevant version;
- access to required sources;
- the requested decision;
- disclosed issues;
- applicable scope.

This does not require recording private thought processes.

### 19.2 Reason Requirement

Some decisions may require a reason.

A reason should be proportionate.

Approval of routine low-risk work may need concise confirmation.

Rejection, exception, emergency approval or disagreement may require more explanation.

### 19.3 No Hidden Chain of Thought Requirement

Human Review governance should not require storage of private internal reasoning.

It should preserve the accountable decision, material basis, conditions and references.

### 19.4 Review Metrics

Organizations may evaluate:

- review turnaround;
- revision rate;
- stale-review rate;
- conflict disclosure;
- post-review error;
- override frequency;
- emergency-review frequency.

Metrics must not pressure reviewers to approve faster or reduce professional independence.

---

## 20. Overrides and Exceptions

An override allows a blocked condition to be handled through a separately governed authority.

It must never be an undocumented administrator bypass.

### 20.1 Override Requirements

An override should identify:

- blocked rule or condition;
- authority permitting override;
- actor;
- scope;
- reason;
- time;
- affected version;
- risks;
- conditions;
- expiry;
- audit reference.

### 20.2 Override Is Not Universal

An override for one condition does not bypass:

- other Policies;
- Permission;
- version binding;
- idempotency;
- external constraints;
- professional review;
- data-access restrictions.

### 20.3 No AI Override

AI may identify that an override path exists.

It may not invoke, approve or recommend an override as final professional judgment without human governance.

### 20.4 Repeated Overrides

Repeated override use may indicate:

- defective Policy;
- poor Workflow design;
- outdated Knowledge;
- inadequate staffing;
- Product friction;
- hidden risk acceptance.

Execution should make the pattern observable without automatically changing Policy.

---

## 21. Event Trace and Audit

Human Review must be reconstructable.

The audit view should support determination of:

- review request;
- exact subject and version;
- requested decision;
- reviewer eligibility context;
- assignment and acceptance;
- sources and disclosed limitations;
- AI assistance disclosure;
- decision;
- conditions;
- comments where material;
- time;
- expiry, revocation or supersession;
- applied action;
- owning-Service references;
- Event references;
- dissent or escalation;
- override or exception.

### 21.1 Review Event vs Domain Event

A review decision may be a governed Event according to Book 02.

The owning review, Task or domain Service remains responsible for authoritative mutation and Event emission.

Workflow must not manufacture review Events directly.

### 21.2 Audit Must Preserve Dissent

Audit should not flatten disagreement into a single final status.

### 21.3 Historical Review Rendering

Historical review must show the version and context that existed at decision time.

It must not silently render current content.

### 21.4 Missing Review Evidence

If a protected action appears to have occurred without required review evidence, Execution should:

- preserve the action evidence;
- mark the governance gap;
- avoid creating a retrospective fake approval;
- escalate;
- support remediation.

A later reviewer may conduct retrospective review.

That does not rewrite history as if approval existed before action.

---

## 22. AI and Agent Boundary

AI may assist Human Review by:

- summarizing source material;
- extracting structured facts;
- comparing versions;
- identifying missing fields;
- detecting contradictions;
- preparing questions;
- highlighting deadline or Policy issues;
- drafting review notes;
- classifying possible risk for human consideration;
- checking that stated conditions were addressed.

AI output remains advisory.

AI and agents may not independently:

- act as reviewer;
- approve or reject;
- satisfy quorum;
- declare a change non-material;
- certify Evidence sufficiency;
- certify deadline accuracy;
- resolve conflicting professional sources;
- declare reviewer independence;
- invoke an override;
- send, submit, pay or instruct a provider;
- mutate protected state;
- emit governed Events;
- bypass Permission or Policy;
- reuse an old approval;
- define professional truth.

### 22.1 AI Disclosure

Where AI materially assisted preparation, the review package should disclose:

- that AI assistance was used;
- which parts were AI-assisted;
- source set where relevant;
- unresolved limitations;
- whether a human edited the output.

The disclosure should be useful, not ceremonial.

### 22.2 Reviewer Must Inspect the Basis

A reviewer should not be asked only:

```text
Do you approve the AI answer?
```

The reviewer should be able to inspect:

- source;
- version;
- extracted facts;
- material assumptions;
- changed content;
- unresolved issues.

### 22.3 Agent-Prepared Review

An agent may assemble a review package.

It may not decide that the package is sufficient for approval without the applicable human or Service checks.

---

## 23. Governance Examples

### 23.1 Communication Review

An AI assistant drafts a client Communication explaining an office action.

The governed review package includes:

- exact draft version;
- recipient;
- source office action;
- deadline context;
- extracted refusal grounds;
- unresolved legal issue;
- AI assistance disclosure;
- intended send action.

The reviewer may approve the content but require another authorized person to approve send.

Editing the draft after approval requires renewed review where material.

### 23.2 Provider Selection

A routing system compares three providers.

The reviewer must see:

- current quote versions;
- service scope;
- jurisdiction capability;
- confidentiality constraints;
- commercial assumptions;
- ranking basis;
- conflicts or unavailable data.

Approval of the recommendation does not itself instruct the provider or authorize payment.

### 23.3 Evidence Review

AI groups use Evidence by date and channel.

The reviewer assesses:

- whether the Evidence relates to the correct mark;
- whether it supports the intended jurisdiction and period;
- whether ownership is clear;
- whether gaps remain;
- whether the bundle is suitable for the intended professional action.

The AI grouping does not certify Evidence sufficiency.

### 23.4 Stale Approval

An application package is approved. The goods/services list later changes.

Governed response:

```text
Approved version and current package differ.
The prior approval is stale for filing.
A new review is required.
```

### 23.5 Conflicted Reviewer

The proposed reviewer negotiated the provider terms being disputed.

The reviewer discloses the relationship.

Policy requires reassignment to an independent reviewer.

The original reviewer may provide factual context but may not issue the final decision.

### 23.6 Deadline Emergency

A deadline may expire before ordinary review completes.

Execution prepares an emergency package identifying:

- source and confidence of deadline;
- current draft;
- unresolved issues;
- narrow protective action;
- consequences;
- exact authority requested.

The emergency reviewer approves only the narrow protective action.

The decision does not approve the full strategy.

### 23.7 Partial Failure Review

A provider instruction was sent, but payment status is uncertain.

The reviewer sees:

- confirmed send;
- uncertain payment;
- provider acknowledgment;
- idempotency references;
- blocked retry;
- reconciliation options.

The reviewer may approve reconciliation or escalation.

The reviewer must not authorize duplicate payment without resolving uncertainty.

---

## 24. Governance Rules

Human Review Governance is correct when:

1. review, approval, authorization and execution remain distinct;
2. the exact review subject, version, scope and intended action are explicit;
3. reviewer eligibility is evaluated through current Permission, Policy and capability;
4. independence and separation-of-duties requirements are preserved;
5. conflict disclosure can affect assignment and decision authority;
6. review packages disclose sources, assumptions, limitations and unresolved issues;
7. approval does not expand beyond its stated scope;
8. silence is not treated as approval for protected professional action;
9. material changes create a new review requirement;
10. conditions and reservations remain visible to apply;
11. dissent, abstention and escalation are preserved;
12. multiple-reviewer quorum counts only eligible completed decisions;
13. delegation is explicit and does not transfer unrelated authority;
14. expiry, revocation and supersession end future authority without erasing history;
15. retry, recovery and change re-evaluate review applicability;
16. deadlines may accelerate escalation but do not erase accountability;
17. overrides are separately governed and auditable;
18. Workflow coordinates review but does not become the reviewer;
19. owning Services retain mutation and Event authority;
20. AI assists but does not review, approve, satisfy quorum or define professional truth;
21. Product presentation does not convert acknowledgment or checklist completion into approval;
22. retrospective review does not rewrite history.

---

## 25. Product Boundary

Book 04 may present review queues, sources, version comparisons, decisions, conditions, dissent, expiry and escalation. It must not turn acknowledgment or a confirmation click into Human Review.

## 26. Implementation Boundary

This chapter defines no reviewer database, staffing model, licensing verification, queue algorithm, electronic-signature system, UI, employment rule or autonomous reviewer.

## 27. Chapter Result

Human Review keeps professional authority attributable to an accountable person.

It binds judgment to the exact material, version, scope and intended action that the reviewer actually examined.

The operating rule is:

```text
Define what must be reviewed.
Bind the exact version and action.
Select an eligible and sufficiently independent reviewer.
Disclose sources, assumptions and uncertainty.
Record an explicit, scoped decision.
Preserve conditions, dissent and expiry.
Revalidate before protected apply.
Do not let Workflow, Product or AI become the reviewer.
Keep mutation and Event authority with owning Services.
Preserve the decision for audit without recording private thought.
```

A reliable Execution System does not add a human click at the end of automation.

It structures accountable judgment so that preparation, approval and action remain distinguishable and traceable.

The next chapter defines how AI and agents may participate inside these boundaries without acquiring independent execution authority: **Chapter 29 — Agent-Assisted Execution Governance**.
