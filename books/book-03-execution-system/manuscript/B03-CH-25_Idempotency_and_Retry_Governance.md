# B03-CH-25 — Idempotency and Retry Governance

## Chapter Purpose

Execution is rarely a single uninterrupted path.

A request may be repeated because a user refreshes a page, a network connection closes before confirmation, a provider responds late, a service times out, a worker restarts, or a reviewer asks for a corrected version. Some repeated attempts are harmless. Others can create duplicate Tasks, duplicate Communications, duplicate instructions, duplicate payments, duplicate filings, conflicting state transitions or misleading Events.

Idempotency and retry governance exist to prevent repetition from becoming duplicate professional action.

The governing principle is:

```text
Repeat the request when safe.
Do not repeat the effect merely because the result is uncertain.
```

This chapter explains how the Execution System coordinates retry-safe behavior while preserving the authority of Book 02 contracts and owning Services. It does not define a new idempotency model, a queue, a workflow engine, an Event Bus or a persistence design.

The core governance path is:

```text
Execution attempt
→ identify semantic operation
→ establish idempotency scope
→ inspect prior outcome and current state
→ revalidate version, Permission, Policy and Human Review
→ classify retry safety
→ replay, continue, reconcile, block or escalate
→ delegate any allowed mutation to the owning Service
→ preserve trace without duplicating effects
```

Idempotency is not only a technical safeguard. In a professional operating system, it is a control against duplicated legal, financial, operational and communicative consequences.

---

## 1. Dependency Baseline

This chapter builds directly on Chapters 10, 12 and 14–16. Its primary Book 02 dependencies are the approved idempotency, error, versioning, audit, Human Review, Permission and Policy contracts, together with the relevant Task, Communication and Workflow API contracts.

Book 02 owns canonical structures, controlled values and Service behavior. This chapter defines only how Execution consumes them.

## 2. Idempotency, Retry and Replay Are Different

These terms must not be used as synonyms.

| Term | Governance meaning |
|---|---|
| Attempt | One invocation or effort to perform an operation |
| Retry | A later allowed attempt after failure, interruption or changed condition |
| Idempotent replay | Reuse or return of the same governed result for the same semantic request without duplicating effects |
| Continuation | Resume from a known safe point after partial progress |
| Reconciliation | Determine whether an uncertain external or cross-service effect actually occurred |
| Reapply | A new protected apply request after current gates are re-evaluated |
| Resend | A new protected Communication send request |
| Audit replay | Read-only reconstruction of what happened |
| Duplicate business action | Two actions that may represent the same real-world intent, even when their technical keys differ |

A retry is not automatically safe.

An idempotent replay is not a new mutation.

An audit replay must not execute anything.

A new idempotency key does not prove that a new business action is legitimate.

These distinctions matter because the same user-visible instruction—“try again”—can require very different governance depending on what is already known.

---

## 3. The Semantic Operation

Idempotency protects a **semantic operation**, not merely an HTTP request, button click, process invocation or background job.

The Execution System must be able to answer:

```text
What action was intended?
Which subject and target were involved?
Which exact version was used?
Which protected effect was requested?
Which reviewer and approval applied?
Which Permission and Policy context applied?
Which external or internal Service owned the effect?
Which earlier attempt may represent the same operation?
```

A semantic operation may include:

- operation type;
- subject reference;
- target reference;
- source version;
- intended effect;
- channel or destination;
- reviewer-bound version;
- approval scope;
- jurisdiction or Matter scope;
- idempotency scope;
- correlation and audit context.

This is a conceptual governance view. It does not create a new Core object.

### 3.1 Same Key, Same Semantic Request

The same valid idempotency key may be reused only for the same semantic request within the same defined scope.

The correct behavior may be to:

- return the existing result;
- report that the operation remains in progress;
- continue from a known safe checkpoint;
- report a previous safe failure;
- require reconciliation;
- reject the retry because the earlier result is uncertain.

### 3.2 Same Key, Different Semantic Request

The same key with changed meaning must fail safely.

Changes that may alter semantic identity include:

- different subject or target;
- different document or draft version;
- different recipient;
- different attachment;
- different amount or currency;
- different provider;
- different filing scope;
- different approval;
- different intended action;
- different Workflow Contract version where the change affects behavior.

The system must not silently reinterpret the old key.

### 3.3 Different Key, Same Business Intent

Idempotency keys cannot replace business duplicate detection.

Two requests may use different keys while still appearing to represent the same:

- filing;
- payment;
- provider instruction;
- Communication;
- Task;
- assignment recordal;
- renewal action;
- protected state transition.

The owning domain or Service may need a separate duplicate-candidate check. Execution must not declare two actions independent merely because their keys differ.

---

## 4. Idempotency Scope

An idempotency key is meaningful only inside an explicit scope.

Possible scope dimensions include:

```text
operation
owning Service
subject
target
Matter or Order
channel
external provider
version
time boundary
tenant or organization
```

The scope must be narrow enough to avoid unrelated conflicts and strong enough to prevent harmful duplication.

Examples:

- Task creation idempotency belongs to Task Service and the intended Task identity.
- Communication approval idempotency is separate from Communication send idempotency.
- Communication send idempotency may include exact content version, recipient set, attachments and channel.
- A provider instruction may require a scope tied to provider, Matter, service request and instruction version.
- A payment attempt may require a scope tied to payable obligation, amount, currency and payment authority.
- A filing or submission may require a scope tied to the exact authorized submission package and official destination.

Book 03 does not define the canonical key format. It requires Execution to preserve and consume the scope defined by Book 02 and the owning Service.

### 4.1 Scope Must Not Expand Silently

A key created for draft preparation must not be reused for send.

A key created for review completion must not be reused for filing.

A key created for provider comparison must not be reused for provider engagement.

A key created for internal state preparation must not be reused for an external legal action.

Each protected effect requires the appropriate idempotency boundary.

---

## 5. Outcome Classes

Before retrying, Execution must classify what is known about the earlier attempt.

A useful governance model is:

| Outcome class | Meaning | Default response |
|---|---|---|
| Not started | No governed effect began | Retry may be possible after current gates |
| Rejected before effect | Validation, Permission, Policy or review blocked the action | Do not retry until the blocking condition changes |
| In progress | The owning Service accepted the operation but has not completed it | Observe or reconcile; do not create a parallel effect |
| Completed | The effect completed and the governed result is known | Replay the result; do not repeat the effect |
| Failed before effect | Failure is confirmed before mutation or external action | Retry may be allowed |
| Failed after partial effect | Some effects occurred before failure | Continue or compensate only under explicit Service governance |
| Outcome uncertain | Confirmation is missing or contradictory | Reconcile before any duplicate-sensitive retry |
| Superseded | A later version or decision replaced the earlier operation | Require a new governed request |
| Cancelled | The operation was intentionally stopped | Retry requires current authority and a new decision where applicable |

The most dangerous state is often not failure. It is uncertainty.

A timeout does not prove that nothing happened.

A missing Event does not prove that no mutation occurred.

A missing provider confirmation does not prove that the provider did not act.

A Product surface showing “failed” does not override the owning Service or external reconciliation result.

---

## 6. Retry Classification

Execution should classify retries by consequence, not only by technical error type.

### 6.1 Safe Replay

Safe replay returns or reconstructs an already governed result without repeating the effect.

Examples:

- returning an existing preview;
- returning a prior validation result;
- returning the reference of an already-created Task;
- returning the status of an already-accepted operation.

### 6.2 Safe Recalculation

A side-effect-free calculation may be repeated when its inputs and versions are explicit.

Examples:

- rebuilding a comparison;
- recalculating a readiness view;
- regenerating a gap analysis;
- re-running validation.

The result must disclose whether source versions changed.

### 6.3 Gated Retry

A retry may proceed only after current gates are evaluated again.

Applicable gates may include:

- validation;
- current object state;
- version;
- Permission;
- Policy;
- Human Review;
- idempotency;
- owning-Service availability;
- external destination state.

A previous approval is not automatically reusable.

### 6.4 Reconciliation-First Retry

When an earlier effect may have occurred, Execution must reconcile before retry.

Examples:

- send provider accepted the message but confirmation was lost;
- payment gateway timed out after authorization;
- official filing endpoint returned an ambiguous response;
- provider instruction was transmitted but no acknowledgment arrived;
- Service mutation succeeded but Event reference is delayed.

The correct next action may be:

```text
check status
query owning Service
inspect external reference
request human confirmation
pause
escalate
```

It is not automatically “send again.”

### 6.5 Prohibited Automatic Retry

Automatic retry is not appropriate when the action is:

- legally consequential;
- financially consequential;
- externally irreversible;
- professionally approved for one exact version;
- dependent on a deadline or jurisdiction context that may have changed;
- capable of producing duplicate Communication;
- capable of creating duplicate official records;
- dependent on a human judgment that must be renewed.

The absence of an error does not authorize repetition.

---

## 7. Protected Actions

Idempotency is strongest at protected-action boundaries.

### 7.1 Task Creation

A retry must not create duplicate active Tasks for the same intended work merely because the caller did not receive the first Task reference.

Execution should ask Task Service whether:

- the Task already exists;
- a prior creation remains in progress;
- the earlier Task was cancelled, archived or superseded;
- a new Task is genuinely required;
- the same semantic key conflicts with changed Task content.

A Task plan is not an active Task. Idempotency for planning does not replace idempotency for Task Service creation.

### 7.2 Communication

Communication preparation, approval and send are separate scopes.

A repeated review request must not:

- create a second approval for a changed draft;
- treat an old approval as approval of a new version;
- send the Communication;
- infer delivery.

A send retry must preserve:

- exact approved version;
- recipient set;
- attachments;
- channel;
- purpose;
- approval;
- send authority.

When provider outcome is uncertain, reconcile before resend.

### 7.3 Provider Selection and Instruction

A routing preview may be regenerated safely.

Provider selection, engagement, instruction and payment are different protected actions.

A retry must not:

- engage two providers;
- send duplicate instructions;
- create conflicting terms;
- initiate duplicate payment;
- treat a recommendation as authority to proceed.

### 7.4 Payment

Payment is duplicate-sensitive even when an earlier attempt appears to fail.

Execution must not repeat payment merely because:

- the user saw a timeout;
- the Product did not refresh;
- an Event is delayed;
- the gateway response was incomplete.

Reconciliation with the owning financial Service or provider is required when outcome is uncertain.

### 7.5 Filing and Submission

Official submission may create legal consequences immediately or asynchronously.

A retry must not:

- submit the same application twice;
- create parallel filings unintentionally;
- reuse approval after the package changes;
- assume no filing occurred because a confirmation number is absent;
- convert preparation readiness into filing authority.

Where official status is uncertain, the default is reconciliation and Human Review, not blind resubmission.

### 7.6 Core State Mutation

Workflow coordinates; the owning Service mutates.

A retry must call the owning Service with the applicable idempotency and version context. Workflow must not reproduce state changes locally or emit replacement Events to “repair” an uncertain result.

---

## 8. Preview, Apply and Retry

Preview and apply have different retry properties.

### 8.1 Preview

Preview should be side-effect free.

A preview may often be repeated safely, but the result must remain version-aware. A later preview may differ because:

- source objects changed;
- Knowledge changed;
- Permission or Policy changed;
- Workflow Contract version changed;
- a reviewer supplied new information;
- an external status changed.

Repeated preview is not guaranteed to return identical content unless the same versioned inputs are used.

### 8.2 Apply

Apply is protected.

Before every allowed apply attempt, Execution must revalidate:

- current source state;
- target state;
- exact version;
- applicable Workflow Contract;
- Permission;
- Policy;
- Human Review;
- idempotency;
- prior effects.

An old preview is not execution authority.

An old approval is not automatically current.

A retry must not weaken the apply gate.

### 8.3 Apply Result Replay

When apply already completed, the correct behavior is generally to return the governed result or reference, not perform apply again.

The result may state:

```text
Operation already completed under the same semantic request.
Existing result returned.
No duplicate effect was created.
```

---

## 9. Human Review and Version Binding

Human Review must be bound to:

- exact subject;
- exact target;
- exact content or package version;
- intended action;
- scope;
- reviewer role;
- decision;
- applicable constraints;
- time where material.

Retry cannot broaden that decision.

A new review may be required when:

- content changes;
- recipient changes;
- attachments change;
- amount changes;
- provider changes;
- jurisdiction changes;
- filing scope changes;
- deadline context changes;
- Policy changes;
- the previous approval expires or is revoked;
- the operation changes from preparation to external action.

Idempotency preserves duplicate safety. It does not preserve professional authority across changed versions.

### 9.1 Approval Is Not a Reusable Token

Approval is not a generic credential for similar actions.

The system must not interpret:

```text
approved once
```

as:

```text
approved for every retry, version, recipient, provider, payment or submission.
```

---

## 10. Permission and Policy Revalidation

A retry occurs in the present, not in the past.

Permission and Policy must be evaluated against the current context before protected continuation.

Conditions may have changed because:

- user role changed;
- organization relationship changed;
- data access became restricted;
- Matter status changed;
- provider became unavailable;
- jurisdictional constraints changed;
- retention or confidentiality rules changed;
- the object was archived, cancelled or superseded.

Idempotency cannot bypass a current denial.

If the prior operation completed, the system may return a restricted safe result without repeating the action. It must not expose protected content merely because the caller possesses an old key.

Permission and Policy fail closed.

---

## 11. Service Ownership and Cross-Service Effects

Execution coordinates the attempt. It does not become the authority for every effect.

Each owning Service remains responsible for:

- validating its object state;
- applying its own idempotency rules;
- deciding whether mutation is allowed;
- preserving version constraints;
- returning a governed result;
- emitting or causing the appropriate Event through the approved boundary.

Cross-service operations create additional risk.

For example:

```text
Workflow apply
→ Task Service creates Task
→ Communication Service prepares draft
→ external provider receives instruction
```

If the third step becomes uncertain, Execution must not restart the whole chain blindly.

It must determine:

- which effects completed;
- which references exist;
- which step is safe to replay;
- which step requires reconciliation;
- whether current authority still applies;
- whether a new continuation plan is needed.

### 11.1 No Synthetic Success

Execution must not manufacture success because a later step appears to have completed.

### 11.2 No Synthetic Failure

Execution must not mark the whole operation failed merely because one confirmation or Event reference is delayed.

The result should preserve partial truth.

---

## 12. Partial Completion and Safe Continuation

A partially completed operation should resume from a governed checkpoint, not from memory or Product state.

A checkpoint may record or reference:

- semantic operation identity;
- completed effects;
- owning-Service results;
- current versions;
- pending steps;
- blocked conditions;
- external references;
- uncertainty;
- review status;
- Permission and Policy outcomes;
- idempotency linkage;
- audit correlation.

This does not require Book 03 to define a persistence schema.

The governance rule is:

```text
Continue from verified effects.
Do not reconstruct protected state by assumption.
```

### 12.1 Restart vs Continue

Restarting repeats the operation from the beginning.

Continuing resumes after confirmed completed effects.

For duplicate-sensitive operations, continuation is usually safer than restart, but only when the checkpoint and owning-Service state are trustworthy.

### 12.2 Compensation Is Separate

Some systems may support compensation or reversal.

Compensation is not retry.

It is a new governed action with its own:

- authority;
- idempotency;
- Permission;
- Policy;
- Human Review;
- Event trace;
- failure modes.

This chapter does not define compensation workflows.

---

## 13. Uncertain External Outcomes

External systems are not always immediately consistent.

An external action may be:

- accepted but not confirmed;
- completed but not visible;
- queued;
- rejected after delay;
- partially processed;
- represented by a temporary reference;
- visible only through later reconciliation.

Execution should represent uncertainty directly.

Unsafe language:

```text
The filing failed.
```

when the only fact is:

```text
No confirmation was received before timeout.
```

Safer language:

```text
Submission outcome is uncertain.
Do not resubmit automatically.
Reconciliation is required.
```

### 13.1 Evidence for Reconciliation

Reconciliation may use:

- owning-Service status;
- external reference;
- provider acknowledgment;
- official receipt;
- payment authorization reference;
- Communication provider status;
- Event references;
- timestamp and correlation data;
- human confirmation.

The absence of one source must not be treated as proof that no effect occurred.

---

## 14. Retry Budget, Delay and Escalation

Repeated attempts can become harmful even when each attempt is technically allowed.

Execution governance should support limits such as:

- maximum attempt count;
- minimum delay;
- backoff;
- escalation threshold;
- deadline-aware review;
- manual intervention after uncertainty;
- stop conditions after repeated conflict.

This chapter defines the governance need, not a scheduler or queue algorithm.

A retry budget should become stricter when:

- the action is protected;
- external state is uncertain;
- deadlines are near;
- versions are changing;
- different Services disagree;
- repeated attempts reveal a persistent Policy or Permission block;
- the effect could be duplicated.

Retry exhaustion should lead to a safe failure or escalation, not silent repetition.

---

## 15. Errors and Retryability

An Error should communicate whether retry is:

- allowed now;
- allowed after correction;
- allowed after waiting;
- allowed only after reconciliation;
- allowed only with renewed Human Review;
- prohibited;
- unknown and requiring escalation.

Examples:

| Condition | Retry guidance |
|---|---|
| Missing required field | Correct input, then create a new governed attempt |
| Version conflict | Refresh state and revalidate |
| Permission denied | Do not retry until authority changes |
| Policy restricted | Do not retry unless Policy permits |
| Human Review required | Obtain review for the exact version and action |
| Service temporarily unavailable before effect | Retry may be allowed |
| External timeout after submission | Reconcile first |
| Same key with different request | Fail with idempotency conflict |
| Operation already completed | Return existing result |
| Partial completion | Continue from verified checkpoint |
| Unknown outcome | Pause and escalate |

Error handling must not expose:

- secret keys;
- restricted object content;
- private review notes;
- provider credentials;
- internal Policy rules;
- prompts;
- hidden reasoning;
- stack traces;
- sensitive external references beyond the caller's Permission.

Chapter 26 develops safe failure in greater depth.

---

## 16. Event Trace and Audit

Retry governance requires traceability without turning Workflow into an Event producer.

The trace should make it possible to determine:

- original semantic request;
- idempotency scope;
- attempt count;
- prior results;
- completed effects;
- uncertain effects;
- reconciliation actions;
- version changes;
- reviewer and approval context;
- Permission and Policy outcomes;
- owning-Service references;
- final disposition.

The owning Service remains responsible for mutation and its governed Event boundary.

Execution may correlate Event references and attempt history. It must not emit substitute Events to compensate for missing evidence.

### 16.1 Event Duplication

A repeated request must not create duplicate domain Events for one completed effect.

A replayed result may reference the existing Event.

A new Event is appropriate only when a genuinely new governed fact occurs, such as:

- reconciliation completed;
- retry was blocked;
- a new approved attempt began;
- a distinct compensation occurred;

and only through the owning Service or approved Event boundary.

### 16.2 Audit Replay Is Read-Only

Audit replay reconstructs history.

It must never:

- re-run mutation;
- resend Communication;
- recreate Tasks;
- resubmit filings;
- re-engage providers;
- repeat payment.

---

## 17. AI and Agent Boundary

AI may assist retry governance by:

- summarizing attempt history;
- comparing semantic requests;
- identifying changed fields;
- classifying likely retry risk;
- preparing reconciliation questions;
- identifying missing confirmation;
- proposing safe next steps;
- drafting an escalation note.

AI output remains advisory.

AI and agents may not independently:

- decide that an uncertain effect did not occur;
- approve a retry;
- reuse Human Review for a changed version;
- send or resend Communication;
- submit or resubmit a filing;
- repeat payment;
- engage or instruct a provider;
- mutate protected state;
- emit governed Events;
- bypass Permission or Policy;
- create professional truth from incomplete trace.

A high-confidence prediction is not reconciliation.

An AI-generated recommendation is not Human Review.

An agent retry loop must not convert repeated tool use into autonomous authority.

---

## 18. Governance Examples

### 18.1 Duplicate Communication Risk

An approved Communication is sent through a provider. The provider request times out before a delivery reference is returned.

Unsafe response:

```text
Retry send immediately.
```

Governed response:

1. preserve the exact approved version and send scope;
2. mark the outcome uncertain;
3. query Communication Service or provider status;
4. inspect any external reference or acknowledgment;
5. block resend until reconciliation;
6. require renewed review if content, recipient, attachment or purpose changes;
7. return the existing send result if completion is confirmed.

### 18.2 Task Creation Retry

A Workflow apply requests creation of a review Task. Task Service creates it, but the response is lost.

Governed response:

1. repeat the same semantic request with the same valid scope;
2. allow Task Service to locate the existing Task;
3. return the existing Task reference;
4. do not create a second active Task;
5. create a new Task only when the intended work is genuinely distinct or the owning Service permits replacement.

### 18.3 Filing Outcome Uncertain

A filing connector sends a submission package. The connection closes before an official number is returned.

Governed response:

1. do not treat the timeout as confirmed failure;
2. preserve the exact authorized package version;
3. mark submission outcome uncertain;
4. reconcile through the connector, provider or official source;
5. escalate to Human Review where confirmation remains unavailable;
6. do not resubmit automatically;
7. require a new governed decision if the package, jurisdiction, goods/services or authority changes.

### 18.4 Changed Draft Under Old Key

A user edits a Communication after approval and attempts to reuse the original send key.

Governed response:

```text
Idempotency conflict.
Approved version and requested version differ.
New Human Review and a new governed send request are required.
```

The system must not silently send either version.

---

## 19. Governance Rules

The Idempotency and Retry Governance model is correct when:

1. semantic operation identity is explicit;
2. idempotency scope is owned by the relevant contract or Service;
3. same key with changed meaning fails safely;
4. different keys do not bypass business duplicate checks;
5. completed effects are replayed, not repeated;
6. uncertain outcomes trigger reconciliation;
7. partial completion resumes from verified checkpoints;
8. every protected retry revalidates current state, version, Permission, Policy and Human Review;
9. approval remains bound to exact version, scope and action;
10. owning Services retain mutation and Event authority;
11. Communication send, provider instruction, payment and submission are never blindly retried;
12. audit replay remains read-only;
13. retry limits lead to safe failure or escalation;
14. AI assists with analysis but does not authorize or execute retry;
15. Product presentation does not redefine execution truth.

---

## 20. Product Boundary

Book 04 may present attempt history, retry controls, uncertainty and reconciliation. It must not convert an ambiguous outcome into success or failure, and a UI refresh must not repeat the underlying effect.

## 21. Implementation Boundary

This chapter defines no key syntax, storage, locks, queues, schedulers, Event Bus, connector, payment, filing, send implementation or autonomous retry. Implementation follows Book 02 and owning-Service contracts.

## 22. Chapter Result

Idempotency protects the Execution System from duplicate effects. Retry governance determines whether another attempt is safe, gated, uncertain, prohibited or dependent on reconciliation.

The operating rule is:

```text
Identify the same semantic operation.
Preserve the correct idempotency scope.
Inspect what already happened.
Revalidate current authority and versions.
Replay completed results.
Continue from verified checkpoints.
Reconcile uncertain external effects.
Do not repeat protected actions blindly.
Keep mutation and Event authority with owning Services.
Keep AI advisory and Human Review accountable.
```

A reliable Execution System does not equate “no response” with “nothing happened,” and it does not equate “try again” with “perform the action again.”

The next chapter addresses what happens when execution cannot continue safely: **Chapter 26 — Error Handling and Safe Failure**.
