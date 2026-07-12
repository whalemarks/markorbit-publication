# B03-CH-26 — Error Handling and Safe Failure

## Chapter Purpose

Execution does not become reliable by avoiding every error.

It becomes reliable by ensuring that errors do not produce false success, hidden partial action, duplicated effects, unauthorized continuation, corrupted state or misleading professional conclusions.

A professional operating system must be able to stop safely.

The governing principle is:

```text
Expose what is known.
Preserve what already happened.
Block what is no longer safe.
Do not invent success, failure or authority.
```

This chapter defines how the MarkOrbit Execution System coordinates errors, blocks, conflicts, partial completion, uncertainty and safe failure while preserving the authority of Book 02 contracts and owning Services.

It does not define exception classes, API status codes, database rollback mechanisms, queue workers, circuit breakers, logging frameworks or Product error screens.

The core governance path is:

```text
execution condition detected
→ determine whether it is an error, block, conflict, uncertainty or expected denial
→ identify the operation phase and affected effect
→ inspect confirmed, partial and uncertain outcomes
→ preserve versions, references and audit context
→ apply Permission, Policy and Human Review boundaries
→ classify continuation, retry, reconciliation, escalation or terminal stop
→ delegate any mutation to the owning Service
→ return a safe and truthful execution result
```

Safe failure is not passive error reporting.

It is an execution decision that limits harm when the intended path cannot continue with sufficient authority, certainty or integrity.

---

## 1. Dependency Baseline

This chapter builds directly on Chapters 10, 14–16 and 25. Its primary Book 02 dependencies are the approved error, idempotency, versioning, audit, Human Review, Permission and Policy contracts, together with the relevant Task, Communication and Workflow API contracts.

Book 02 owns canonical structures, controlled values and Service behavior. This chapter defines only how Execution consumes them.

## 2. Error, Failure, Block and Uncertainty Are Different

A reliable system must preserve distinctions between conditions that may look similar in a Product surface.

| Term | Governance meaning |
|---|---|
| Validation issue | Input or structure does not satisfy a required contract |
| Permission denial | The actor is not authorized for the requested action |
| Policy block | The action is restricted under an applicable Policy |
| Human Review requirement | The operation cannot proceed until accountable review is completed |
| Version conflict | The requested action is based on stale or mismatched state |
| Business conflict | The request conflicts with current domain state or another governed action |
| Technical error | A component could not perform its expected technical responsibility |
| External failure | A provider, connector or official system rejected or could not complete an action |
| Partial failure | Some governed effects completed while others did not |
| Uncertain outcome | The system cannot yet determine whether an effect occurred |
| Degraded condition | A non-essential capability is unavailable but a narrower safe path may remain |
| Terminal failure | The operation cannot continue under the current request and context |
| Safe stop | Execution intentionally halts to prevent unauthorized, duplicate or misleading action |

These conditions must not be collapsed into a generic “failed” label.

A Permission denial is not a technical outage.

A Human Review requirement is not an exception.

A version conflict is not evidence of corrupted data.

A timeout is not proof that an external action failed.

A partial failure is not total failure.

A safe stop is not system weakness. It is a governance control.

---

## 3. What Safe Failure Means

Safe failure means that when execution cannot continue, the system preserves truth, authority and recoverability.

A safe failure should make clear:

```text
what was requested
what was evaluated
what completed
what did not complete
what remains uncertain
which protected effects may already exist
which versions and approvals applied
why execution stopped
what action is allowed next
what action is prohibited
who must review or reconcile
```

This is a conceptual execution result, not a new Core schema.

### 3.1 Safe Failure Properties

A safe failure has the following properties:

1. **Truthful** — it does not claim success or failure beyond available evidence.
2. **Bounded** — it stops before unauthorized or duplicate protected action.
3. **Traceable** — it preserves correlation, references, versions and decision context.
4. **Non-destructive** — it does not erase confirmed effects to make the operation appear atomic.
5. **Recoverable where possible** — it identifies safe continuation, correction or reconciliation.
6. **Fail-closed where required** — it does not continue protected action when authority or certainty is missing.
7. **Exposure-limited** — it does not disclose restricted internal or personal information.
8. **Service-respecting** — it does not take ownership away from the Service that controls mutation.
9. **Human-accountable** — it escalates professional decisions rather than automating them.
10. **Product-neutral** — it defines execution meaning without prescribing UI.

### 3.2 Safe Failure Is Not Silent Failure

A silent failure hides the fact that the expected result was not achieved.

Examples include:

- dropping a Communication without reporting that send did not complete;
- omitting a failed Task creation while showing the Workflow as complete;
- swallowing a provider rejection and continuing with a recommendation;
- treating missing Knowledge as empty Knowledge;
- replacing a failed official status check with stale cached status without disclosure;
- suppressing a version conflict and applying to the latest object.

Safe failure must be visible to the authorized actor and traceable in the governed execution record.

---

## 4. Failure Classification Dimensions

A single error code is rarely enough to guide execution.

The Execution System should classify a failure across several dimensions.

### 4.1 Origin

The condition may originate from:

- caller input;
- object state;
- owning Service;
- Permission;
- Policy;
- Human Review;
- Knowledge;
- connector;
- external provider;
- official authority;
- network or infrastructure;
- AI-assisted component;
- Product request;
- configuration or version mismatch.

Origin identifies responsibility. It does not automatically determine blame.

### 4.2 Phase

The condition may occur during:

- preview;
- validation;
- review request;
- review decision;
- apply preparation;
- owning-Service mutation;
- external transmission;
- external processing;
- Event reference return;
- reconciliation;
- continuation;
- result rendering.

The same technical error has different consequences depending on phase.

A timeout before external transmission may permit retry.

A timeout after external transmission may require reconciliation.

### 4.3 Effect Certainty

The effect may be:

- confirmed absent;
- confirmed completed;
- partially completed;
- in progress;
- uncertain;
- superseded;
- reversed through a separately governed action.

This dimension is essential for duplicate-sensitive operations.

### 4.4 Correctability

The condition may be:

- caller-correctable;
- reviewer-correctable;
- owning-Service-correctable;
- operator-correctable;
- externally reconcilable;
- dependent on changed Permission or Policy;
- dependent on a new version;
- terminal for the current request;
- unknown.

### 4.5 Retryability

Retryability may be:

- safe now;
- safe after correction;
- safe after delay;
- safe only with the same idempotency scope;
- safe only after reconciliation;
- safe only after renewed Human Review;
- prohibited;
- unknown.

Chapter 25 governs the retry decision.

### 4.6 Consequence

The condition may affect:

- presentation only;
- advisory output;
- internal preparation;
- Task creation;
- review;
- Communication;
- payment;
- provider instruction;
- official filing or submission;
- Core state mutation;
- deadline handling;
- Evidence sufficiency;
- audit integrity.

The higher the consequence, the stricter the failure boundary must be.

---

## 5. Fail Closed, Fail Safely and Degrade Gracefully

These concepts must be separated.

### 5.1 Fail Closed

Fail closed means the protected action is denied when required authority, validation, version, Policy, Permission or Human Review cannot be established.

Protected actions generally fail closed when:

- actor authority is missing or cannot be verified;
- Policy evaluation is unavailable;
- exact approved version cannot be established;
- idempotency state is uncertain;
- external effect may already have occurred;
- required professional review is absent;
- required object state cannot be confirmed;
- the requested action conflicts with current state.

Fail closed does not necessarily mean the entire Product becomes unavailable.

The system may still allow:

- read-only status;
- authorized audit inspection;
- correction of input;
- preparation of a new draft;
- submission of a review request;
- reconciliation;
- escalation.

### 5.2 Fail Safely

Fail safely means the system stops or narrows execution while preserving confirmed facts and exposing the next governed action.

A safe failure may produce:

```text
blocked
waiting
review required
reconciliation required
version conflict
partial completion
terminal failure
```

The exact controlled status must come from Book 02.

### 5.3 Graceful Degradation

Graceful degradation is appropriate only when the missing capability is non-essential to the requested action.

Examples:

- an analytics view is unavailable while authoritative object status remains accessible;
- an AI summary is unavailable while source Documents remain available;
- an optional recommendation service is unavailable while the user can continue manual preparation;
- a secondary provider comparison source is unavailable and the comparison explicitly discloses incomplete coverage.

Degradation is not acceptable when it removes a required governance gate.

The system must not degrade by:

- skipping Human Review;
- bypassing Permission or Policy;
- using stale authority;
- substituting AI confidence for professional judgment;
- sending through an unapproved channel;
- filing without required validation;
- treating missing deadline information as no deadline;
- converting uncertain payment or filing status into failure.

The governing rule is:

```text
Availability may degrade.
Governance must not.
```

---

## 6. The Execution Failure Envelope

When an operation stops, Execution needs a coherent view of the condition.

A conceptual failure envelope may include:

- operation reference;
- semantic request identity;
- subject and target references;
- execution phase;
- error or block category;
- owning component;
- current version;
- requested version;
- confirmed effects;
- absent effects;
- uncertain effects;
- prior attempt references;
- Permission result;
- Policy result;
- Human Review state;
- idempotency scope;
- retry or continuation guidance;
- reconciliation requirement;
- safe user-facing message;
- restricted diagnostic reference;
- audit correlation.

This is not a new Book 02 object or API schema.

Its purpose is to prevent fragmented error handling where each layer tells a different story.

### 6.1 One Condition, Different Views

The same underlying condition may require different views:

- **Execution view** — enough detail to coordinate next action;
- **Service view** — enough detail to diagnose and own the effect;
- **Reviewer view** — enough detail to make an accountable decision;
- **Product view** — safe, clear and permission-filtered explanation;
- **Audit view** — evidence of what occurred and why execution stopped;
- **External view** — limited information suitable for a provider or client.

These views must refer to the same governed truth.

They must not independently redefine the outcome.

---

## 7. Validation Failures

Validation failures occur before an operation can rely on the requested input or structure.

Examples include:

- missing required fields;
- invalid controlled values;
- inconsistent references;
- malformed version context;
- unsupported operation type;
- incomplete review scope;
- invalid recipient or attachment reference;
- missing required Evidence linkage.

Validation should fail before protected effects begin whenever possible.

### 7.1 Validation Must Be Specific

Unsafe:

```text
Invalid request.
```

Safer:

```text
Application preparation cannot continue because the applicant reference is missing and the classification version is not identified.
No filing or external submission was attempted.
```

The message should identify correctable conditions without exposing restricted details.

### 7.2 Validation Is Not Professional Judgment

Structural validity does not prove:

- legal sufficiency;
- professional correctness;
- Evidence admissibility;
- filing eligibility;
- deadline accuracy;
- provider suitability;
- client authorization.

Execution must not convert a passing validator into approval.

### 7.3 Validation Failure and Retry

A corrected request is often a new attempt.

If the semantic request changes, the system must not silently reuse an old approval or incompatible idempotency scope.

---

## 8. Permission, Policy and Review Stops

Permission denial, Policy restriction and Human Review requirements are governed stops, not unexpected technical failures.

### 8.1 Permission Denial

A Permission denial should indicate:

- the requested action was not authorized;
- whether the actor may request review or escalation;
- whether any effect began;
- which safe read-only or corrective actions remain available.

It should not reveal internal role mappings, sensitive Policy logic or restricted object data.

### 8.2 Policy Restriction

A Policy restriction should preserve:

- the applicable Policy reference or safe category;
- the blocked action;
- the scope of the restriction;
- the permitted next step;
- whether an exception path exists under governance.

Execution must not create an ad hoc exception.

### 8.3 Human Review Required

A review stop should identify:

- exact version;
- exact intended action;
- review scope;
- required reviewer capability or role;
- current preparation state;
- what will remain blocked until review completes.

A system error must not be disguised as “review required.”

A review requirement must not be cleared by AI confidence, a previous approval for another version, or Product-level confirmation.

---

## 9. Version Conflicts and Stale State

A version conflict occurs when the requested operation is based on state that is no longer current or no longer compatible.

Examples:

- a draft changed after approval;
- a Task changed after assignment;
- a provider quote changed after comparison;
- an application package changed after readiness review;
- Matter status changed before apply;
- a Policy or Workflow Contract version changed;
- external official status changed after preview.

The safe response is not to apply the request to the latest version automatically.

Execution should:

1. stop the protected action;
2. identify the expected and current versions;
3. preserve the prior decision context;
4. expose material changes;
5. require regeneration, revalidation or renewed Human Review where needed;
6. use a new governed request when semantic identity changes.

Version conflict handling is developed further in Chapter 27.

---

## 10. Partial Failure

Partial failure occurs when some effects complete and others do not.

Professional systems frequently cross ownership boundaries:

```text
Workflow coordination
→ Task Service
→ Communication Service
→ provider or authority
→ Event trace
```

A single operation may not be atomic across those boundaries.

### 10.1 Preserve Partial Truth

Unsafe result:

```text
Operation failed.
```

when a Task was created and a Communication was sent.

Safer result:

```text
Task creation completed.
Communication send outcome is confirmed.
Provider acknowledgment was not received.
The operation is partially complete and requires reconciliation.
```

The system must not erase completed effects to simplify the status.

### 10.2 No Assumed Rollback

Execution must not assume that an external or cross-service effect can be rolled back.

Examples that may be irreversible or separately governed include:

- sent Communication;
- accepted payment;
- provider instruction;
- official filing;
- signed Document;
- emitted domain Event;
- changed ownership record;
- disclosed confidential material.

Any compensation or reversal is a new governed action, not automatic cleanup.

### 10.3 Continuation Plan

A safe continuation plan should identify:

- confirmed completed effects;
- remaining steps;
- blocked steps;
- uncertain effects;
- required reconciliation;
- required renewed authority;
- current versions;
- prohibited repetitions.

The continuation plan does not authorize the remaining actions by itself.

---

## 11. Uncertain Outcomes

Uncertainty must be represented directly.

A system may be uncertain because:

- a response was lost;
- an external provider is eventually consistent;
- a Service completed mutation but confirmation is delayed;
- Event trace has not arrived;
- a connector returned an ambiguous status;
- different sources disagree;
- an official system is unavailable;
- a human acted outside the system.

Unsafe behavior includes:

- converting uncertainty to failure so the user can retry;
- converting uncertainty to success to avoid escalation;
- selecting the “most likely” outcome through AI;
- hiding the uncertainty behind a generic progress indicator.

The safe outcome is:

```text
Outcome uncertain.
Protected repetition is blocked.
Reconciliation is required.
```

Chapter 25 defines the reconciliation-first retry rule.

### 11.1 Deadline-Sensitive Uncertainty

Uncertainty near a legal or operational deadline requires explicit escalation.

Execution may:

- surface the known deadline source and confidence;
- identify the missing confirmation;
- prioritize Human Review;
- prepare a reconciliation checklist;
- preserve evidence of attempted action.

Execution must not:

- certify the deadline;
- assume an extension;
- assume submission occurred;
- submit again without authority;
- allow AI to choose the legal strategy.

---

## 12. External and Connector Failures

External systems introduce failure modes outside MarkOrbit control.

Examples include:

- authentication rejection;
- provider outage;
- rate limit;
- malformed provider response;
- official system maintenance;
- delayed acknowledgment;
- conflicting status;
- unsupported jurisdiction behavior;
- attachment rejection;
- payment authorization ambiguity.

### 12.1 Connector Failure Is Not Domain Truth

A connector reports what it observed.

It does not redefine:

- trademark status;
- filing status;
- payment status;
- Communication delivery;
- provider engagement;
- legal effect.

The owning Service must interpret the connector result under its contract.

### 12.2 Fallback Provider

A fallback provider may be used only when:

- Policy allows it;
- Permission allows it;
- routing rules permit it;
- the action has not already occurred elsewhere;
- Human Review remains valid for the changed provider or channel;
- confidentiality and data-transfer constraints are satisfied;
- the fallback does not change commercial or legal meaning without renewed decision.

Automatic fallback is dangerous for:

- Communication send;
- filing;
- payment;
- provider instruction;
- Evidence transfer;
- confidential Documents.

A different provider is often a different semantic operation.

### 12.3 External Error Messages

External error text must be treated as untrusted input.

It may contain:

- inconsistent terminology;
- internal provider details;
- personal data;
- HTML or code;
- unsupported conclusions;
- misleading retry guidance.

Execution may preserve a restricted diagnostic reference while presenting a normalized, permission-safe explanation.

---

## 13. Communication Failure Governance

Communication failure requires special handling because intent, send, delivery and receipt are separate facts.

Possible conditions include:

- draft generation failed;
- review request failed;
- approval was rejected;
- send was not attempted;
- provider rejected the send;
- send was accepted but delivery is unknown;
- delivery failed;
- delivery succeeded but receipt is unknown;
- recipient replied outside the system.

The system must not collapse these into “message failed.”

### 13.1 Draft Failure

A draft failure does not create send authority.

A fallback draft may be prepared, but must enter normal review.

### 13.2 Send Failure

When send is confirmed absent, a governed retry may be possible.

When send outcome is uncertain, resend is blocked pending reconciliation.

### 13.3 Delivery Failure

Delivery failure does not necessarily permit changing recipient, channel or content without review.

The approved Communication scope may no longer apply.

### 13.4 Product Language

Product language should distinguish:

```text
not sent
send rejected
send accepted
delivery pending
delivery failed
delivery confirmed
receipt unknown
```

Book 04 owns the presentation. Book 03 owns the semantic distinctions.

---

## 14. Task and Workflow Failure Governance

Workflow coordinates; Task Service owns Tasks.

### 14.1 Task Creation Failure

Execution must determine whether Task creation:

- did not begin;
- was rejected;
- completed but the response was lost;
- created a Task with invalid downstream linkage;
- created a duplicate candidate;
- remains in progress.

A new Task must not be created solely because the Product lacks a reference.

### 14.2 Task Execution Failure

A Task may be blocked, waiting, failed, cancelled or otherwise governed under Book 02 statuses.

Execution must not invent status transitions.

A failed Task does not necessarily fail the entire Workflow.

The Workflow Contract should determine whether the operation:

- waits;
- escalates;
- creates a separately authorized remediation Task;
- continues through an allowed alternate path;
- stops.

### 14.3 Workflow Failure

A Workflow does not become the owner of every downstream failure.

It should preserve:

- current coordination position;
- completed Service effects;
- blocked conditions;
- pending reviews;
- allowed next transitions;
- references to owning-Service outcomes.

Workflow must not directly mutate Core state or emit replacement Events to simulate recovery.

---

## 15. Data Integrity and Invariant Violations

An invariant violation means the system observes a state that should not be possible under the governing contracts.

Examples:

- an approved version reference does not exist;
- two mutually exclusive active states appear simultaneously;
- a Task references an unknown Matter;
- an Event claims a mutation without an owning-Service reference;
- a Communication is marked delivered without a send reference;
- an archived object is treated as actively mutable;
- an approval predates the version it claims to approve.

Invariant violations require a stronger response than ordinary validation failure.

Execution should:

1. stop protected continuation;
2. preserve evidence;
3. avoid automatic repair;
4. restrict exposure;
5. escalate to the owning Service or operator;
6. mark affected conclusions as unreliable;
7. require governed reconciliation before resuming.

### 15.1 No Silent Auto-Repair

Automatic repair can destroy evidence and create false history.

Examples of unsafe repair:

- rewriting an Event timestamp;
- assigning a missing reviewer after the fact;
- linking a Task to the most likely Matter;
- changing a version reference to the current version;
- marking a Communication sent because delivery evidence exists;
- generating a replacement domain record without approval.

Repair, migration or correction must be explicitly governed and auditable.

---

## 16. Knowledge and Professional Uncertainty

Some execution failures arise because required professional information is missing, outdated, contradictory or insufficiently authoritative.

Examples:

- no reliable deadline source;
- conflicting jurisdiction requirements;
- outdated fee information;
- incomplete goods/services classification basis;
- unclear provider authority;
- Evidence source cannot support the intended proposition;
- legal effect of a Document is unresolved.

The system must not convert missing Knowledge into a default answer.

Safe behavior may include:

- mark information as unavailable or disputed;
- identify sources and versions;
- request professional review;
- block protected action;
- prepare questions;
- preserve alternative interpretations without selecting one;
- route the gap back to Knowledge or domain ownership.

AI may summarize the conflict. It may not resolve professional truth independently.

---

## 17. AI and Agent Failure Boundary

AI-assisted components may fail through:

- unavailable model;
- incomplete output;
- malformed structured response;
- unsupported claim;
- source mismatch;
- missing citation;
- confidence inconsistency;
- prompt injection;
- tool error;
- hallucinated reference;
- stale context;
- unauthorized data exposure risk.

These failures must not be treated as ordinary content variation when they affect protected execution.

### 17.1 AI Failure Must Degrade to Human-Controlled Work

When AI assistance fails, the system may:

- expose source material;
- allow manual preparation;
- request a human-authored draft;
- show which extraction fields are incomplete;
- preserve the last reviewed version;
- disable the AI-assisted step.

It must not:

- invent missing data;
- silently use an earlier output;
- approve its own fallback;
- continue with lower confidence without disclosure;
- bypass Human Review;
- mutate protected state;
- send, submit or emit governed Events.

### 17.2 Agent Tool Failure

An agent tool failure must not trigger uncontrolled tool repetition.

The agent may prepare a recovery recommendation, but retry remains governed by:

- idempotency;
- current Permission;
- current Policy;
- Human Review;
- effect certainty;
- tool and Service ownership.

### 17.3 AI Error Messages

AI-generated explanations are not authoritative error classification.

The system should rely on governed Service and contract results, not model interpretation, for the final execution disposition.

---

## 18. Error Exposure, Privacy and Security

Error handling can leak more information than normal success paths.

A safe error response must not expose:

- credentials or tokens;
- connection strings;
- internal hostnames where restricted;
- stack traces;
- raw database errors;
- secret configuration;
- hidden Policy logic;
- private review notes;
- AI prompts;
- hidden reasoning;
- unrelated object data;
- personal data beyond the actor's Permission;
- confidential provider terms;
- internal risk scores;
- unrestricted external payloads.

### 18.1 Diagnostic Separation

The system may preserve a restricted diagnostic reference while returning a safe explanation.

For example:

```text
User-facing:
The provider could not confirm the submission outcome.
Reconciliation is required before another submission attempt.

Restricted diagnostic:
Connector correlation reference and provider response retained for authorized operations review.
```

### 18.2 Do Not Reveal Existence Indirectly

An error must not confirm the existence of a restricted Matter, Document, client, provider, filing or Communication to an unauthorized actor.

A safe response may need to say:

```text
The requested operation is unavailable.
```

rather than reveal the protected reason.

---

## 19. Event Trace and Audit

Failures are professionally significant facts.

The trace should support reconstruction of:

- requested operation;
- actor and authority context;
- versions;
- validation result;
- Permission and Policy outcomes;
- Human Review status;
- owning Service;
- execution phase;
- confirmed effects;
- uncertain effects;
- external references;
- error category;
- retry guidance;
- reconciliation actions;
- escalation;
- final disposition.

### 19.1 Workflow Does Not Manufacture Failure Events

Workflow may coordinate failure handling and correlate Event references.

It must not emit domain Events directly merely to make the trace appear complete.

The owning Service or approved Event boundary remains responsible for Events associated with mutation or authoritative status change.

### 19.2 Missing Trace Is a Governance Problem

A missing Event or audit reference does not prove that the effect did not occur.

Execution must preserve uncertainty and reconcile.

### 19.3 Error Logs Are Not the Audit Record

Technical logs may assist diagnosis.

They do not replace governed Event and audit context because logs may be:

- incomplete;
- mutable;
- inaccessible to reviewers;
- overexposed;
- tied to infrastructure rather than semantic operations;
- missing Human Review, Permission or Policy context.

---

## 20. Escalation and Operational Ownership

A safe failure should identify who owns the next governed action.

Possible owners include:

- caller;
- reviewer;
- Matter owner;
- Task owner;
- owning Service;
- provider manager;
- finance operator;
- system operator;
- security operator;
- Knowledge curator;
- legal professional;
- external provider.

Escalation should be based on responsibility, not merely severity.

Examples:

- malformed input → caller;
- stale version → caller or reviewer;
- Permission conflict → administrator or Policy owner;
- uncertain payment → finance Service or operator;
- official submission uncertainty → filing operator or provider;
- invariant violation → owning Service and system operator;
- professional Knowledge conflict → qualified reviewer;
- suspected data exposure → security operator.

### 20.1 Escalation Is Not Approval

Routing a failure to a senior actor does not automatically authorize the blocked action.

The actor must still satisfy applicable Permission, Policy and Human Review requirements.

### 20.2 Escalation Must Preserve Context

An escalation should carry:

- concise failure summary;
- semantic operation;
- affected objects and versions;
- confirmed and uncertain effects;
- deadline context;
- prior attempts;
- blocked action;
- requested decision;
- relevant references;
- exposure-safe diagnostics.

It must not require the next actor to reconstruct the operation from raw logs.

---

## 21. Governance Examples

### 21.1 Policy Service Unavailable Before Send

A Communication is approved, but the Policy check required before send is unavailable.

Unsafe response:

```text
Policy service unavailable. Send anyway because the draft was approved.
```

Governed response:

1. preserve the approved version;
2. record that send was not attempted;
3. fail closed at the Policy gate;
4. allow read-only inspection and escalation;
5. re-evaluate Policy when the Service becomes available;
6. require renewed review if content, recipient, channel or Policy scope changes.

### 21.2 Task Created, Workflow Response Failed

Task Service creates a Task, but Workflow does not receive the reference because of a network interruption.

Unsafe response:

```text
Workflow failed. Create the Task again.
```

Governed response:

1. classify the Task creation outcome as uncertain;
2. use the same idempotency scope to query Task Service;
3. return the existing Task reference when found;
4. avoid duplicate active Tasks;
5. preserve the Workflow as partially complete until the reference is reconciled.

### 21.3 Filing Accepted, Event Reference Delayed

An official filing is confirmed by receipt, but the corresponding Event reference is delayed.

Unsafe response:

```text
No Event exists, so filing failed.
```

Governed response:

1. preserve the official receipt as evidence of the external effect;
2. do not resubmit;
3. mark Event trace completion as pending;
4. route the trace gap to the owning Service;
5. avoid manufacturing an Event from Workflow;
6. present filing and trace status separately.

### 21.4 AI Extraction Incomplete

AI extracts an office action but omits a refusal ground.

Unsafe response:

```text
Use the extracted summary because confidence is high.
```

Governed response:

1. mark extraction incomplete;
2. preserve the source Document;
3. block professional strategy generation from being treated as complete;
4. request Human Review;
5. allow AI to compare the source against the extracted fields;
6. prohibit submission or deadline certification.

### 21.5 Stale Approval

A provider instruction changes after approval because the quoted fee and service scope changed.

Governed response:

```text
Approved version no longer matches the requested instruction.
Execution is blocked.
A new review and approval are required.
```

The system must not apply the old approval to the revised instruction.

---

## 22. Governance Rules

Error Handling and Safe Failure are correct when:

1. errors, denials, conflicts, uncertainty and partial completion remain distinguishable;
2. protected actions fail closed when authority or certainty is missing;
3. graceful degradation never removes governance gates;
4. results state what completed, what did not and what remains uncertain;
5. technical failure does not overwrite domain truth;
6. partial effects are preserved rather than hidden;
7. uncertain external outcomes require reconciliation;
8. version conflicts stop automatic apply;
9. Permission, Policy and Human Review remain current and explicit;
10. owning Services retain mutation and Event authority;
11. fallback paths are governed as potentially different semantic operations;
12. invariant violations stop protected continuation and are not silently repaired;
13. AI failure degrades to human-controlled work;
14. error exposure is permission-filtered and security-safe;
15. escalation carries governed context but does not grant authority;
16. Product presentation does not redefine the execution outcome;
17. missing trace does not prove missing effect;
18. safe failure preserves recoverability without inventing implementation behavior.

---

## 23. Product Boundary

Book 04 may present blocked, failed, partial and uncertain outcomes, correction paths and escalation. It must preserve the execution meaning rather than compressing every condition into a generic error.

## 24. Implementation Boundary

This chapter defines no exception framework, status-code mapping, transaction, rollback, queue, circuit breaker, connector, Event Bus, Product UI or autonomous recovery.

## 25. Chapter Result

Error handling is not complete when a system catches an exception.

It is complete when the Execution System can stop without losing truth, duplicating effects, bypassing authority or leaving the next actor to guess what happened.

The operating rule is:

```text
Classify the condition correctly.
Preserve confirmed effects.
Represent uncertainty directly.
Fail closed at protected gates.
Degrade only when governance remains intact.
Do not assume rollback.
Do not silently repair impossible state.
Keep mutation and Event authority with owning Services.
Keep AI advisory.
Escalate with context.
Return a truthful and safe next step.
```

A reliable Execution System does not promise uninterrupted success.

It guarantees that interruption, conflict and failure remain governed.

The next chapter addresses how execution meaning remains stable as contracts, objects, workflows, policies and approved content change over time: **Chapter 27 — Versioning and Change Control**.
