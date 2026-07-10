# B03-CH-14 — Event Trace, Audit and Replay

## Chapter Purpose

This chapter defines how Book 03 uses Events and Audit Context to make execution observable, reviewable and reconstructable without turning Events into commands or logs into professional truth.

Book 02 defines Events as meaningful records of completed facts.

Events are not:

- commands;
- workflows;
- Tasks;
- Notifications;
- Communications;
- arbitrary logs;
- analytics clicks;
- AI conclusions.

Book 03 consumes Event references and audit context.

It does not create Event semantics, emission authority or payload contracts.

The central rules are:

```text
Owning Services emit authoritative Events.
Execution observes and correlates.
Audit Context explains the operation.
Replay reconstructs; it does not re-execute.
```

---

## 1. Dependency Baseline

This chapter extends:

- [Chapter 09 — Execution Object and State Model](B03-CH-09_Execution_Object_and_State_Model.md)
- [Chapter 10 — Workflow Coordination Model](B03-CH-10_Workflow_Coordination_Model.md)
- [Chapter 13 — Communication Execution Boundary](B03-CH-13_Communication_Execution_Boundary.md)

It consumes:

- [Event Object](../../book-02-core-specification/core-specs/objects/event.md)
- [Event Index](../../book-02-core-specification/indexes/event-index.md)
- [Event API Contract](../../book-02-core-specification/core-specs/contracts/api/event-api-contract.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Idempotency Contract](../../book-02-core-specification/core-specs/contracts/common/idempotency.md)
- [Core Traceability Matrix](../../book-02-core-specification/core-specs/TRACEABILITY.md)
- [Event Trace, Audit and Replay Planning](../planning/B03-PLN-0010_Event_Trace_Audit_Replay.md)

All Event types, payload meaning, source and emission authority remain Book 02-owned.

---

## 2. Event Boundary

An Event records a completed fact allowed by an Event specification.

Examples may include:

- Task created;
- Task completed;
- Matter status changed;
- Workflow Contract applied;
- Communication sent;
- Human Review referenced by an owning-service Event;
- Document attached;
- routing selection recorded.

The Event producer is the owning service or Event Service under the approved architecture.

Execution must not emit an Event merely because:

- a workflow step was reached;
- Product displayed success;
- AI predicted completion;
- a review was approved;
- a Task plan included the action;
- an API request was accepted by the orchestration layer.

The completed fact must be owned and supported.

---

## 3. Event vs Audit Context

Event and Audit Context serve different purposes.

| Concern | Event | Audit Context |
|---|---|---|
| Primary meaning | Completed fact | Context of an operation |
| Owner | Event Service or owning service under Event spec | Common Contract used by governed operations |
| Can create business state? | No; records state-changing fact | No |
| Includes actor/context? | As defined by payload | May connect actor, target, subject, decisions and trace |
| Can be command? | No | No |
| Can be log? | Not arbitrary log | Not raw logging implementation |
| Visibility | Event Policy | Audit Policy, possibly different |
| Use in Book 03 | Trace reference | Operation explanation and correlation |

An operation may succeed while Event recording fails or is delayed where architecture allows separate results.

Execution must not hide that distinction.

---

## 4. Execution Trace

Execution Trace is the ordered, source-linked reconstruction of:

- request;
- source references;
- contract versions;
- actor;
- AI participation;
- workflow preview/apply;
- Task plan and active Tasks;
- Permission and Policy decisions;
- Human Review;
- owning-service requests;
- service outcomes;
- errors;
- idempotency;
- Event references;
- timestamps;
- Product-exposed outcome.

Execution Trace is a Book 03 coordination view.

It is not a new Event stream or source of truth.

Each element should retain its authority.

---

## 5. Correlation and Causation

Correlation connects records belonging to the same operational path.

Causation describes which allowed prior operation or fact led to another record.

Execution may use:

- correlation ID;
- causation ID;
- Workflow application reference;
- Task reference;
- Human Review reference;
- Communication reference;
- Event references;
- subject and target references.

Correlation does not mean every correlated item has the same owner or status.

Causation does not create permission to re-execute.

### 5.1 Correlation Scope

A correlation scope should be bounded.

One global correlation ID for an entire customer history may expose too much and obscure meaning.

### 5.2 Cross-Organization Trace

Cross-organization trace must respect Policy, redaction and non-disclosure.

A partner or provider should not receive internal review notes merely because the records share correlation.

---

## 6. Event Observation

Execution may observe Events through allowed Event APIs or references.

Observation may support:

- progress refresh;
- audit reconstruction;
- duplicate detection;
- service-outcome confirmation;
- exception investigation;
- Product status refresh;
- reviewer context.

Observation does not authorize mutation.

### 6.1 Event Freshness

An Event proves a fact at its recorded time.

It may not prove current state.

Execution may need the owning service's current state before a protected action.

### 6.2 Event Visibility

Event payload visibility follows Policy.

Execution may receive:

- full allowed payload;
- safe summary;
- reference only;
- redacted result;
- NotFound substitution;
- PermissionDenied;
- PolicyRestricted.

AI must not reconstruct omitted payload.

---

## 7. Event Emission Boundary

Only approved producers emit authoritative Events.

Prohibited direct emitters include:

- Product UI;
- API routing layer;
- Workflow coordination layer;
- AI or agent layer;
- Human Review Contract by itself;
- Task plan;
- preview;
- audit summary.

A service may emit only Events defined for its successful or allowed outcome.

An API response must not claim an Event unless:

- the Event specification exists;
- the owning producer emitted it;
- the reference is valid;
- visibility allows exposure.

---

## 8. Audit Context

Audit Context may preserve:

- operation name;
- operation category;
- result;
- actor;
- organization;
- AI/agent participation;
- subject;
- target;
- Permission decision reference;
- Policy decision reference;
- Human Review reference;
- correlation;
- causation;
- idempotency key;
- Event references;
- source;
- requested and completed times.

Audit Context does not:

- evaluate Permission;
- evaluate Policy;
- certify compliance;
- define Event payload;
- change business state;
- prove professional correctness.

It explains the governed operation.

---

## 9. Audit Trail

An Audit Trail is a durable, ordered view of authorized audit evidence.

It should distinguish:

- planned action;
- requested action;
- accepted service action;
- rejected service action;
- completed fact;
- partial completion;
- failed Event recording;
- retry;
- replayed idempotent response;
- human decision;
- AI preparation;
- Product display.

Audit Trail must not merge these into a success narrative.

### 9.1 Restricted Evidence

Review notes, prompts, evidence, recipient details and internal Policy information may have stricter visibility than the fact that an operation occurred.

### 9.2 Safe Audit Summary

A Product or reviewer may receive a safe summary rather than full details.

The summary should disclose restricted-field omission.

---

## 10. Replay Meaning

Replay in Book 03 means controlled reconstruction for:

- diagnosis;
- review;
- audit;
- learning;
- support;
- quality analysis.

Replay does not mean:

- re-emitting Events;
- re-running service actions;
- resending Communications;
- recreating Tasks;
- reapplying Workflows;
- changing historical state;
- changing review decisions;
- generating new professional truth.

The default replay is read-only.

### 10.1 Deterministic Reconstruction Limits

A historical path may not be fully reproducible because:

- source data changed;
- Policy changed;
- Permission changed;
- contract version deprecated;
- external system unavailable;
- restricted fields omitted;
- AI model or source set changed;
- human judgment cannot be recreated.

Replay must disclose missing evidence and uncertainty.

### 10.2 Simulation Is Separate

A future simulation may apply historical context to current rules or a sandbox.

That is not replay.

It needs a separate approved contract and must not mutate production state.

---

## 11. Idempotent Replay vs Audit Replay

These terms must remain separate.

| Term | Meaning |
|---|---|
| Idempotent replay | Same semantic request with same idempotency key returns or preserves the same allowed result without duplicate effects |
| Audit replay | Read-only reconstruction of what happened |
| Retry | New allowed attempt after failure or changed condition |
| Reapply | New protected Workflow apply request |
| Resend | New protected Communication send request |

Confusing these terms can duplicate harmful actions.

---

## 12. Partial and Conflicting Trace

Execution may encounter:

- service success without visible Event reference;
- Event reference with restricted payload;
- partial workflow application;
- conflicting Product cache;
- duplicate request;
- missing correlation;
- delayed external confirmation;
- different versions.

The safe response is not to invent a complete history.

Execution should identify:

- confirmed facts;
- inferred relationships;
- missing evidence;
- restricted evidence;
- conflicts;
- required owning-service check;
- whether the path can proceed.

AI may summarize but must preserve uncertainty.

---

## 13. Trace and State

Event trace supports state interpretation but does not replace current state.

For example:

```text
TaskCompleted Event exists
```

proves an allowed completed Task fact.

It does not prove:

- Task is not later archived;
- Matter completed;
- filing submitted;
- Communication sent;
- all workflow steps complete.

Current protected decisions use current owning-service state plus trace where required.

---

## 14. Trace and Human Review

Review trace should distinguish:

- review requested;
- reviewer assigned or identified;
- review started;
- decision recorded;
- review expired;
- reviewed version;
- downstream service reliance.

Human Review Contract does not emit Events directly.

Owning services may include Human Review references in their Events where specifications allow.

Review notes may remain restricted.

---

## 15. Trace and AI

AI participation should be visible in Audit Context.

Trace should answer:

- which agent or capability assisted;
- which sources were used;
- what output mode was used;
- which version or contract governed;
- what was omitted;
- whether Human Review occurred;
- whether the output was accepted, rejected or revised.

AI must not:

- write authoritative Events;
- rewrite historical trace;
- fill missing events with generated facts;
- hide its own participation;
- certify that replay is complete.

---

## 16. Worked Example: Communication Send Investigation

A customer reports that an instruction email was not received.

Available records show:

- approved Communication version;
- send request;
- idempotency key;
- Communication Service accepted request;
- provider delivery outcome unknown;
- CommunicationSent Event reference exists;
- Event payload is restricted;
- no delivery-confirmed evidence.

A safe audit conclusion is:

```text
The approved Communication was submitted to Communication Service.
The service recorded a sent event.
Delivery confirmation is not available in the authorized trace.
Do not resend automatically until duplicate-send risk is evaluated.
```

An unsafe conclusion is:

```text
The customer received the email, so resend is unnecessary.
```

Another unsafe action is blind resend.

Execution may request provider-status verification or authorized retry review.

---

## 17. Replay Safeguards

Every replay should define:

- purpose;
- requester;
- Permission;
- Policy;
- subject scope;
- time range;
- versions;
- allowed sources;
- redaction;
- AI use;
- output classification;
- whether Human Review is required;
- explicit no-mutation boundary.

Replay output should distinguish:

- fact;
- contract outcome;
- derived sequence;
- missing evidence;
- uncertainty;
- restricted evidence.

---

## 18. Event and Audit Invariants

1. Event records a completed fact.
2. Event is not command.
3. Event is not arbitrary log.
4. Owning service or Event Service emits.
5. Workflow does not emit directly.
6. API routing does not emit directly.
7. AI does not emit.
8. Human Review Contract does not emit directly.
9. Event reference is trace.
10. Event visibility follows Policy.
11. Event may not prove current state.
12. Audit Context does not create Events.
13. Audit Context does not certify compliance.
14. Business success and Event-recording result may differ.
15. Correlation does not transfer ownership.
16. Replay is read-only by default.
17. Replay does not resend, reapply or recreate.
18. Idempotent replay is not audit replay.
19. Missing evidence remains missing.
20. AI does not repair history.

---

## 19. Event and Audit Anti-Patterns

- Product emits business Events.
- Workflow emits Event because a step ended.
- AI generates missing Event records.
- Event triggers protected mutation without command contract.
- Logs are treated as professional trace.
- Correlation ID exposes unrestricted history.
- Replay re-executes service actions.
- Audit summary claims delivery without evidence.
- Restricted payload is reconstructed by AI.
- Event presence is treated as current state.
- Duplicate send is called replay.
- Failed Event recording is hidden.

---

## 20. MVP Depth

The MVP should support:

- Event references;
- Event read and validation;
- subject and producer;
- correlation;
- safe payload visibility;
- Audit Context;
- operation result;
- actor/AI/review trace;
- idempotency linkage;
- safe audit summary;
- read-only reconstruction;
- explicit missing evidence;
- Product-safe trace.

It does not require:

- Kafka or event bus;
- Event sourcing;
- production replay engine;
- full audit dashboard;
- observability platform;
- automatic compensation;
- cross-organization trace sharing;
- AI-generated history.

---

## 21. Non-Goals of This Chapter

This chapter does not define:

- Event types;
- Event payloads;
- Event producer rules beyond existing Book 02 ownership;
- logging infrastructure;
- message broker;
- event sourcing;
- replay engine;
- compliance certification;
- Product audit UI;
- automated remediation;
- resending or reapplying actions.

It defines how Book 03 consumes trace and reconstructs execution safely.

---

## 22. Chapter Conclusion

Execution becomes trustworthy when its claims can be traced to governed sources.

```text
Owning service acts
→ authoritative Event records allowed fact
→ Audit Context connects actor, target, gates and versions
→ Execution correlates the path
→ replay reconstructs without mutation
→ Product exposes a safe view
```

Events are facts, not commands.

Audit Context explains, not certifies.

Replay reconstructs, not re-executes.

AI summarizes, not repairs history.

The next chapter defines the gates that decide whether protected execution may proceed: independent Permission and Policy evaluation, fail-closed behavior, restriction, redaction and Human Review requirements.
