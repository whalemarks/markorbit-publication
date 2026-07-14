# B03-CH-16 — Human–AI Execution Handoff

**Status:** Release Candidate 1

## Chapter Purpose

This chapter defines how AI and agents hand prepared work to authorized humans and governed services without becoming execution authority.

AI can create leverage in execution by:

- summarizing;
- classifying;
- comparing;
- drafting;
- identifying gaps;
- preparing Task plans;
- preparing Communication drafts;
- explaining Workflow previews;
- summarizing audit trace.

The risk begins when prepared output silently becomes:

- approved;
- authoritative;
- complete;
- sent;
- submitted;
- selected;
- paid;
- state-changing.

The Human–AI Execution Handoff exists to preserve the boundary.

```text
AI prepares.
Execution packages context.
Human Reviews or decides where required.
Owning Service performs allowed action.
Trace distinguishes every role.
```

---

## 1. Dependency Baseline

This chapter completes Part II and extends:

- [Chapter 09 — Execution Object and State Model](B03-CH-09_Execution_Object_and_State_Model.md)
- [Chapter 10 — Workflow Coordination Model](B03-CH-10_Workflow_Coordination_Model.md)
- [Chapter 12 — Review and Approval Lifecycle](B03-CH-12_Review_and_Approval_Lifecycle.md)
- [Chapter 15 — Permission and Policy Gates](B03-CH-15_Permission_and_Policy_Gates.md)

It consumes:

- [AI Context Contract](../../book-02-core-specification/core-specs/contracts/common/ai-context.md)
- [AI Agent Governance](../../book-02-core-specification/core-specs/agents/ai-agent-governance.md)
- [Agent Registry](../../book-02-core-specification/core-specs/agents/agent-registry.md)
- [Agent API Contract](../../book-02-core-specification/core-specs/contracts/api/agent-api-contract.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)
- [Developer Start Here](../../book-02-core-specification/core-specs/DEVELOPER_START_HERE.md)
- [Execution System Blueprint](../planning/B03-PLN-0002_Execution_System_Blueprint.md)

Book 03 coordinates handoff using approved Agent identity, capability, Permission, Policy, AI Context and Human Review rules. It does not create new AI authority.

---

## 2. Handoff Boundary

A handoff is the transfer of prepared material and responsibility for the next governed decision.

It is not:

- transfer of Core ownership;
- automatic acceptance;
- automatic Human Review;
- automatic service execution;
- delegation of unrestricted authority;
- an AI approval mechanism.

The handoff must make visible:

```text
What AI did
Which Agent identity/capability was used
Which sources were used
What is missing
What was omitted by Policy
What output mode was produced
What remains uncertain
Which human role is required
Which downstream service is required
Which protected actions remain forbidden
```

---

## 3. Agent Identity and Capability

Every AI-assisted step must resolve:

- Agent reference;
- registry key;
- Agent Contract reference/version;
- Agent role;
- capability used;
- allowed data scope;
- execution mode;
- registry status;
- Permission;
- Policy.

An unregistered or suspended Agent must not participate in protected execution.

Capability is specific.

Examples:

- summarize audit trace;
- prepare Task plan;
- draft Communication;
- compare routing candidates;
- identify evidence gaps;
- explain Workflow preview.

Capability does not imply:

- Permission;
- Policy allowance;
- Human Review;
- service authority;
- approval;
- send;
- submit;
- select;
- pay;
- emit Events.

---

## 4. AI Context

AI Context should preserve:

- AI-assisted flag;
- Agent identity;
- registry key;
- Agent Contract;
- role;
- capability;
- data access scope;
- output mode;
- source scope;
- restricted capability;
- confidence where allowed;
- downstream service required;
- Human Review requirement;
- Policy omissions;
- version.

AI Context is not a prompt dump.

It should not expose:

- hidden reasoning;
- secrets;
- restricted prompts;
- unrestricted source content;
- Policy internals;
- Permission internals.

It provides governed provenance.

---

## 5. Handoff Package

A handoff package is a conceptual bundle for review or downstream coordination.

It may contain:

- subject references;
- Execution Context;
- AI Context;
- prepared output;
- source references;
- source version;
- known facts;
- assumptions;
- missing information;
- uncertainty;
- Policy omissions;
- proposed next action;
- required reviewer role;
- intended downstream service;
- prohibited actions;
- audit correlation.

The package is not a new Core Object or schema.

It describes what must remain visible.

### 5.1 Source Separation

The package should distinguish:

- Core-sourced fact;
- external source;
- user-provided fact;
- AI inference;
- AI suggestion;
- reviewer decision;
- service result;
- Event trace.

AI inference must not be presented as Core fact.

### 5.2 Output Mode

Prepared output should identify its mode, such as:

- summary;
- draft;
- recommendation;
- comparison;
- checklist;
- gap analysis;
- preview explanation.

The mode sets expectation.

A recommendation is not decision.

A draft is not approved content.

---

## 6. Handoff Destinations

AI output may hand off to:

### 6.1 Human Preparation

A human continues editing or gathering information.

### 6.2 Human Review

An authorized reviewer evaluates the output and sources.

### 6.3 Workflow Preview

Prepared context is used for a no-side-effect preview.

### 6.4 Task Plan

AI-prepared work is considered for governed Task creation.

### 6.5 Owning Service Preparation

A service request may be prepared, but the service still applies its contract.

### 6.6 Product Explanation

Product may display a safe explanation of a governed outcome.

None of these destinations authorizes AI to cross the next gate.

---

## 7. Human Reception

The receiving human should be able to:

- inspect sources;
- inspect missing context;
- see AI involvement;
- edit;
- reject;
- request more information;
- escalate;
- approve within authority;
- preserve rationale;
- identify a different downstream action.

The interface belongs to Book 04.

The execution requirement is that the information exists and authority remains explicit.

### 7.1 Human Acceptance Is Bounded

A human may accept an AI draft as a starting point.

That is not necessarily Human Review.

A Human Review decision must follow the Human Review Contract where required.

### 7.2 Human Editing

If the human materially edits the output:

- the reviewed version must be updated;
- source and authorship distinction should remain;
- previous approval may no longer apply;
- AI involvement should not be erased.

---

## 8. Review Handoff

For protected work, handoff to Human Review includes:

- exact output version;
- review scope;
- evidence;
- Agent identity;
- capability;
- source scope;
- missing context;
- Policy omissions;
- risk;
- intended downstream action.

The reviewer may:

- approve;
- reject;
- revise;
- request information;
- escalate.

The reviewer does not execute the downstream action.

After review, Execution refreshes Permission, Policy, state and version.

---

## 9. Service Handoff

If review and gates allow, Execution may prepare a request for an owning Service.

The service handoff includes:

- target reference;
- intended operation;
- actor;
- organization;
- Permission decision;
- Policy decision;
- Human Review reference;
- AI Context where relevant;
- idempotency;
- version;
- audit context.

The owning Service may accept or reject.

AI does not call the service as an independent authority.

An Agent-assisted technical invocation, if later allowed, remains governed by the same service contract and explicit execution mode.

---

## 10. Handoff Outcomes

A handoff may result in:

- accepted for preparation;
- accepted for review;
- rejected;
- revision requested;
- more information required;
- escalated;
- downstream service required;
- Permission denied;
- Policy restricted;
- expired;
- conflict;
- safe error.

These outcomes do not all mean AI output was wrong.

They describe the governed path.

### 10.1 Rejection Is Valuable Trace

Rejected AI output should preserve:

- reason category;
- reviewed version;
- reviewer;
- source issue;
- missing context;
- Policy issue;
- safe learning signal where allowed.

It must not silently disappear.

### 10.2 Revision Loop

A revision loop may be:

```text
AI draft
→ Human Review
→ changes requested
→ human or AI-assisted revision
→ new version
→ new review where required
```

Approval for the prior version does not carry automatically.

---

## 11. Confidence and Uncertainty

Confidence may help prioritize review.

It does not grant authority.

High confidence does not:

- satisfy Human Review;
- grant Permission;
- approve Policy;
- verify source freshness;
- certify legal truth;
- permit send or submission.

Low confidence should not be hidden.

The handoff should state:

- uncertain areas;
- missing sources;
- conflicting sources;
- unsupported inference;
- review questions.

---

## 12. Data Scope and Policy Omission

AI may only use evaluated data scope.

If Policy omits fields:

- the Agent must not access them;
- the output must not reconstruct them;
- the handoff must disclose omission where safe;
- the human must not assume full context;
- downstream action may require different authority or context.

A Human Reviewer with broader access may conduct a separate governed review.

That does not retroactively make the AI output full-context.

---

## 13. Handoff and Task

AI may propose a Task or prepare Task content.

The handoff path is:

```text
AI proposes Task
→ human/Workflow considers Task plan
→ gates
→ Task Service creates active Task
```

AI may work inside an active Task as assistance.

AI must not:

- assign itself;
- mark InProgress;
- mark Completed;
- approve output;
- close related objects.

Task trace should identify AI assistance.

---

## 14. Handoff and Communication

AI may draft Communication.

The handoff path is:

```text
AI draft
→ human preparation/review
→ bounded approval
→ prepare send
→ Communication Service
```

AI must not:

- choose final recipients;
- approve;
- send;
- confirm delivery;
- mark sent;
- retry unknown delivery.

Chapter 13 controls the Communication boundary.

---

## 15. Handoff and Workflow

AI may:

- explain applicability;
- summarize context;
- identify missing fields;
- prepare Task plan;
- explain preview;
- suggest review questions.

AI must not:

- choose unauthorized Workflow Contract;
- alter steps;
- apply;
- skip gates;
- create active Tasks;
- emit Events.

Workflow Agent capability is not apply authority.

---

## 16. Handoff and Routing

AI may compare provider candidates under allowed data scope.

It may explain:

- jurisdiction coverage;
- capability;
- price information where verified;
- availability;
- Policy restrictions;
- missing facts.

AI must not select the provider finally.

The handoff should identify:

- candidate set;
- source date;
- scoring method where allowed;
- missing data;
- commercial impact;
- required reviewer/decision-maker.

Final routing remains a protected human and owning-service action.

---

## 17. Handoff Trace

Audit should distinguish:

```text
AI prepared.
Human edited.
Human Reviewed.
Human approved.
Execution revalidated.
Owning Service acted.
Event recorded.
Product displayed.
```

These statements must not collapse into:

```text
AI completed the work.
```

Trace may preserve:

- Agent reference;
- capability;
- output version;
- source scope;
- reviewer;
- decision;
- service result;
- Event references;
- rejection/revision;
- timestamps.

---

## 18. Worked Example: Classification Recommendation

A user provides a list of goods/services.

### 18.1 AI Preparation

AI compares terms against authorized Classification sources.

It prepares:

- suggested classes;
- recommended terms;
- source references;
- ambiguity notes;
- missing business context;
- confidence;
- Human Review requirement.

### 18.2 Human Preparation

The user clarifies the actual products.

AI revises the recommendation as version 2.

### 18.3 Human Review

An authorized reviewer examines:

- source version;
- jurisdiction;
- goods/services;
- ambiguity;
- exclusions;
- version 2.

The reviewer approves selected terms and rejects others.

### 18.4 Service Handoff

Execution refreshes Permission, Policy and source context.

The approved selection is handed to Classification Service under its contract.

Classification Service records the allowed state.

AI did not finalize classification.

The reviewer did not mutate the Classification Object directly.

---

## 19. Handoff Invariants

1. Agent identity is known.
2. Capability is explicit.
3. Capability is not Permission.
4. Permission is not Policy.
5. Policy controls data scope.
6. AI Context preserves provenance.
7. Output mode is explicit.
8. Sources and missing context are disclosed.
9. AI inference is not Core fact.
10. Confidence is not authority.
11. Human acceptance is not always Human Review.
12. Human Review is version- and scope-bounded.
13. Review does not execute.
14. Owning service acts.
15. AI does not create active Tasks.
16. AI does not apply Workflows.
17. AI does not approve or send Communications.
18. AI does not select providers finally.
19. AI does not emit Events.
20. Trace distinguishes AI, human, service and Event roles.

---

## 20. Handoff Anti-Patterns

- Anonymous AI output.
- No source scope.
- High confidence bypasses review.
- Human clicks accept and system treats it as professional approval.
- AI edits approved version after review.
- AI creates active Task.
- AI sends draft.
- Agent capability becomes Permission.
- Product hides Policy omissions.
- Human approval triggers service without revalidation.
- Rejected output disappears.
- Audit says AI completed protected action.
- AI reconstructs restricted data.
- Routing Agent selects provider automatically.

---

## 21. MVP Depth

The MVP should support:

- Agent identity;
- registry key;
- capability validation;
- Agent Contract version;
- AI Context;
- output mode;
- source scope;
- missing context;
- Policy omissions;
- Human Review requirement;
- versioned output;
- accepted/rejected/revised handoff;
- downstream service requirement;
- audit trace.

It does not require:

- autonomous agent runtime;
- multi-agent delegation;
- persistent agent memory platform;
- unrestricted tool use;
- AI approval;
- AI send or submission;
- digital human execution;
- Product review UI;
- automatic learning from all review notes.

---

## 22. Non-Goals of This Chapter

This chapter does not define:

- new Agent roles or capabilities;
- model selection;
- prompt design;
- memory architecture;
- tool framework;
- autonomous execution;
- Human Review UI;
- service implementation;
- Product screens;
- professional truth;
- agent-to-agent authority transfer;
- new Events.

It defines governed handoff using Book 02 Agent and AI contracts.

---

## 23. Chapter Conclusion

Human–AI collaboration is safe when responsibility changes are visible.

```text
AI prepares
→ handoff package preserves source, limits and version
→ human receives and reviews where required
→ Execution refreshes gates
→ owning Service acts
→ trace distinguishes every role
```

AI is valuable because it prepares faster and exposes gaps.

Humans remain accountable for bounded review and decisions.

Services remain authoritative for state-changing behavior.

Events remain authoritative trace.

Product remains presentation.

This closes Part II — Execution Architecture.

The next part moves from shared models to recurring professional execution patterns, beginning with Intake Execution.
