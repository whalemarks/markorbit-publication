# B03-CH-20 — Provider Routing Preparation Pattern

**Status:** Release Candidate 1

## Chapter Purpose

The Provider Routing Preparation Pattern organizes the facts, constraints, candidates and review questions needed for a future provider decision without selecting, engaging or instructing a provider.

Provider routing affects:

- professional responsibility;
- customer outcome;
- jurisdiction coverage;
- language capability;
- availability;
- commercial terms;
- confidentiality;
- service quality;
- deadlines;
- cross-organization data exposure.

The pattern therefore answers:

```text
What service and jurisdiction require provider support?
Which Matter and Order context governs the request?
Which provider, Partner and Service Network references may be considered?
What candidate information is visible under Policy?
Which factors support or weaken each candidate?
What information is missing, stale or conflicting?
What may AI compare or recommend?
Which human role must make the final selection?
Why is current MVP execution limited to preview?
What must remain forbidden after preview?
```

The governing path is:

```text
Routing need
→ context and constraint resolution
→ candidate discovery
→ candidate validation
→ comparison and recommendation preparation
→ Human Review requirement
→ safe preview result
→ stop before selection, engagement or instruction
```

In the current MVP depth, the pattern is preview-only.

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
- [Chapter 19 — Communication Review Pattern](B03-CH-19_Communication_Review_Pattern.md)

Its primary Book 02 sources are:

- [Provider Routing Workflow](../../book-02-core-specification/core-specs/workflows/provider-routing-workflow.md)
- [Provider Routing Workflow Contract](../../book-02-core-specification/core-specs/contracts/workflows/provider-routing-workflow-contract.md)
- [Workflow Specifications Index](../../book-02-core-specification/core-specs/workflows/index.md)
- [Workflow Contract Index](../../book-02-core-specification/core-specs/contracts/workflows/index.md)
- [Routing API Contract](../../book-02-core-specification/core-specs/contracts/api/routing-api-contract.md)
- [Service Provider API Contract](../../book-02-core-specification/core-specs/contracts/api/service-provider-api-contract.md)
- [Service Network API Contract](../../book-02-core-specification/core-specs/contracts/api/service-network-api-contract.md)
- [Partner API Contract](../../book-02-core-specification/core-specs/contracts/api/partner-api-contract.md)
- [Jurisdiction API Contract](../../book-02-core-specification/core-specs/contracts/api/jurisdiction-api-contract.md)
- [Matter API Contract](../../book-02-core-specification/core-specs/contracts/api/matter-api-contract.md)
- [Order API Contract](../../book-02-core-specification/core-specs/contracts/api/order-api-contract.md)
- [Task API Contract](../../book-02-core-specification/core-specs/contracts/api/task-api-contract.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [AI Context Contract](../../book-02-core-specification/core-specs/contracts/common/ai-context.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)

Book 02 owns Routing, Service Provider, Service Network and Partner behavior, the Workflow, contract, controlled values and validation.

### 1.1 Current Depth Rule

The Provider Routing Workflow Specification marks the current MVP category as:

```text
Stub Now
Level 1/2
Preview / Validation Stub
Apply not production-enabled
```

The Workflow Contract describes a broader governed routing model and future selection boundary. That broader model does not override the current Workflow implementation depth.

This chapter therefore adopts the more restrictive current rule:

```text
Preview may prepare candidates and review context.
Apply must remain disabled and side-effect free.
No provider selection, engagement, instruction or commercial commitment may occur.
```

---

## 2. Pattern Position

Provider routing preparation may follow:

- Customer Intake;
- Application Preparation;
- Office Action Response Preparation;
- Renewal Preparation;
- Assignment Preparation;
- Evidence Review Preparation;
- another governed Matter or Order preparation flow.

It may support future needs such as:

- local associate identification;
- jurisdiction-specific provider matching;
- quote comparison;
- language or capability matching;
- provider availability review;
- Service Network routing;
- commercial-terms review;
- provider inquiry preparation.

The pattern currently produces only:

- validated routing context;
- candidate preview;
- missing-information list;
- comparison factors;
- exclusions where safely disclosable;
- risk and commercial-review warnings;
- Human Review requirement;
- Task plan preview;
- Communication outline;
- safe errors.

It does not produce a selected provider.

---

## 3. Routing Boundary

Provider routing contains several decisions that must remain distinct.

| Stage | Meaning |
|---|---|
| Need identification | Provider support may be required |
| Candidate discovery | Potential references are found |
| Candidate validation | References and visible attributes are checked |
| Comparison | Candidate factors are organized |
| Recommendation | A non-final preference or options are prepared |
| Human selection | An authorized human makes a bounded choice |
| Commercial approval | Terms and authority are approved |
| Engagement | A governed commitment is created |
| Instruction | Communication is reviewed and sent |
| Provider acceptance | The provider confirms or rejects |
| Service execution | Professional work begins under its own contracts |

The current MVP stops before Human selection.

### 3.1 Candidate Is Not Eligible

A candidate may appear relevant while lacking:

- current capability;
- valid relationship;
- availability;
- required language;
- jurisdiction coverage;
- acceptable commercial terms;
- permitted data access;
- conflict clearance;
- current status;
- authority to accept work.

### 3.2 Eligible Is Not Selected

Eligibility means the provider may remain under consideration.

It does not mean the provider is the best choice or has been selected.

### 3.3 Selected Is Not Engaged

A future reviewed selection still would not prove:

- terms accepted;
- provider instructed;
- provider accepted;
- payment approved;
- work commenced.

---

## 4. Routing Context

Execution assembles a bounded routing context.

| Area | Question |
|---|---|
| Service scope | What professional service is required? |
| Jurisdiction | Which governed target reference applies? |
| Matter | Which professional context creates the need? |
| Order | Which commercial scope and limits apply? |
| Timing | What urgency is stated, and which dates are verified? |
| Capability | Which skills, language or service requirements are explicit? |
| Preferences | Which providers are preferred, excluded or already involved? |
| Network | Which Partner or Service Network context is permitted? |
| Commercial terms | Which fees, currencies or limits may be viewed? |
| Data scope | What customer, Matter or Document context may be disclosed? |
| Governance | Which Permission, Policy and Human Review requirements apply? |
| AI | Which capability, sources and limitations apply to assistance? |
| Version | Which Workflow and contract versions govern preview? |
| Trace | Which prior previews, reviews or provider facts are relevant? |

This is not a new Routing Object.

### 4.1 Matter and Order Must Both Be Respected

Matter context may define professional need.

Order context may define requested or authorized commercial scope.

A provider suitable for the Matter may still fall outside the Order's approved scope.

The preview should expose mismatch instead of silently changing either record.

### 4.2 Urgency Does Not Grant Authority

Urgency may influence comparison or escalation.

It does not permit:

- Policy bypass;
- unreviewed provider choice;
- undisclosed commercial terms;
- automatic instruction;
- payment approval;
- use of stale provider data.

---

## 5. Candidate Discovery

Candidate discovery may consider only governed and Policy-visible sources.

Possible sources include:

- Service Provider references;
- Partner relationships;
- Service Network membership;
- jurisdiction capability;
- service capability;
- language;
- prior governed relationship;
- allowed capacity or availability indicators;
- preferred or excluded references;
- current organization context.

Discovery should preserve:

- source;
- version or freshness;
- visibility limitations;
- missing fields;
- reason the candidate appeared;
- reason for exclusion where safe;
- AI involvement.

### 5.1 Search Result Is Not Recommendation

A returned provider reference may match only a broad field.

The system must not label search order as quality ranking.

### 5.2 Existing Relationship Is Not Current Suitability

A past provider relationship does not prove:

- present capacity;
- current terms;
- current conflict status;
- current legal authorization;
- current quality;
- suitability for a different service.

### 5.3 Excluded Candidate Visibility

Policy may hide:

- candidate existence;
- commercial terms;
- relationship details;
- internal risk notes;
- exclusion reasons.

Where disclosure is allowed, the preview may provide a safe reason category.

It must not leak restricted internals to explain an exclusion.

---

## 6. Candidate Validation

Validation checks what the owning contracts permit.

It may evaluate:

- public-safe reference validity;
- Service Provider status where visible;
- Service Network relationship;
- Partner context;
- jurisdiction reference;
- declared capability;
- required language;
- preferred or excluded status;
- visible commercial data;
- missing or stale attributes;
- required review.

A valid provider reference does not imply:

- permission to view full provider data;
- current eligibility;
- absence of conflicts;
- availability;
- commercial approval;
- final selection.

### 6.1 Freshness

Time-sensitive fields may include:

- availability;
- capacity;
- quote;
- currency;
- service scope;
- contact;
- relationship status;
- authorization;
- conflict result.

The preview should identify freshness where known and mark uncertainty where it is not.

### 6.2 Conflict and Independence

A provider may require conflict or independence review.

The pattern may flag that such review is required.

It does not invent the substantive test or certify that no conflict exists.

---

## 7. Comparison Factors

Comparison organizes facts; it does not make the final decision.

Factors may include:

- jurisdiction capability;
- service type;
- language;
- availability;
- urgency fit;
- required capability;
- network relationship;
- prior governed experience;
- visible commercial terms;
- missing data;
- client constraints;
- Policy limitations;
- risk flags.

### 7.1 Factor Source

Each factor should preserve whether it is:

- Core-sourced fact;
- provider-declared data;
- Partner or Service Network data;
- customer preference;
- operator assessment;
- AI inference;
- stale or unverified input;
- Policy-redacted.

### 7.2 Missing Data Must Not Become a Poor Score Automatically

A candidate with hidden or missing data is not necessarily worse.

The correct outcome may be:

- insufficient information;
- require provider inquiry;
- require different Permission;
- exclude from current preview;
- require human judgment.

### 7.3 Weighting Is a Policy and Decision Surface

A future score may depend on how factors are weighted.

Book 03 does not define universal weights.

Price, speed, relationship, capability and risk may have different importance for different services.

AI must not present an opaque score as professional truth.

---

## 8. Recommendation Preparation

The pattern may prepare:

- candidate shortlist;
- side-by-side comparison;
- advantages and limitations;
- missing-information questions;
- conditional recommendation;
- no-recommendation result;
- escalation request.

A recommendation must state:

- intended service;
- jurisdiction;
- candidate references;
- considered factors;
- source scope;
- missing context;
- Policy omissions;
- time sensitivity;
- AI involvement;
- required Human Review;
- non-final status.

### 8.1 Conditional Recommendation

A useful recommendation may say:

```text
Provider A appears suitable for language and jurisdiction capability,
subject to current availability, conflict clearance and fee confirmation.
Provider B remains an alternative with incomplete commercial data.
Final selection requires authorized Human Review.
```

It must not say “Provider A has been appointed.”

### 8.2 No Candidate Is a Valid Result

The pattern should not force a weak recommendation.

A safe result may be:

- no visible candidate meets current constraints;
- required data is unavailable;
- all candidates need review;
- scope requires a different network;
- provider inquiry is needed;
- Policy prevents comparison.

---

## 9. Preview Behavior

Current MVP preview may:

- validate request shape;
- validate Matter and Order references;
- validate provider-related references;
- check Permission and Policy;
- identify missing routing inputs;
- prepare candidate preview;
- prepare comparison factors;
- show excluded candidates where allowed;
- flag limited provider visibility;
- identify commercial review needs;
- prepare a Task plan preview;
- prepare a provider inquiry outline;
- prepare AI-assisted summary;
- require Human Review;
- return safe warnings and errors.

Preview must not:

- select a provider;
- create a Routing selection;
- engage a provider;
- create commercial commitment;
- update Matter or Order;
- create active Tasks;
- create Communication;
- send a provider message;
- execute payment;
- dispatch filing instructions;
- emit Events.

### 9.1 Preview Must State Its Depth

The result should make clear:

```text
This is a candidate preview.
No final selection was made.
No provider was contacted.
No commercial commitment exists.
Apply is not production-enabled.
```

---

## 10. Apply Is Disabled in Current MVP

If apply is requested, the Workflow must return a controlled safe response such as the Book 02-defined not-implemented or invalid-state outcome.

The response must be:

- side-effect free;
- non-retryable as an enabled production action;
- version-aware;
- safe under Policy;
- explicit that apply is unavailable.

It must not:

- perform a partial provider selection;
- create an active Task as compensation;
- create a draft Communication;
- update Order scope;
- emit an Event;
- store a commercial commitment;
- silently fall back to preview while claiming apply.

### 10.1 Future Apply Boundary

A later Book 02 decision may enable apply.

That future capability would require, at minimum:

- Routing Service ownership;
- supported Workflow and contract versions;
- idempotency;
- Permission;
- Policy;
- Human Review;
- state eligibility;
- Service Provider and Service Network validation;
- commercial-term review;
- Communication Service handoff;
- Task Service ownership;
- owning-service Event trace;
- safe failure and rollback/continuation rules where defined.

This chapter does not authorize that expansion.

---

## 11. Human Review

Human Review is required for future:

- final provider selection;
- provider engagement;
- commercial-term approval;
- client-facing provider recommendation;
- provider instruction;
- cross-organization restricted data use.

The review package should identify:

- service scope;
- jurisdiction;
- Matter and Order references;
- candidate set;
- factors and sources;
- missing information;
- stale data;
- preferred and excluded candidates;
- commercial terms visible to the reviewer;
- Policy omissions;
- AI involvement;
- intended downstream action;
- version and time.

### 11.1 Review Does Not Engage

A Human Review decision may select or approve a provider within a future contract.

It does not itself:

- contact the provider;
- accept terms;
- create payment obligation;
- send instructions;
- start professional work.

The relevant owning Services must separately accept the downstream request.

---

## 12. Communication Preparation

Preview may prepare an outline for:

- availability inquiry;
- quote request;
- conflict-check request;
- internal routing note;
- customer approval question;
- provider instruction draft.

The outline or draft remains uncreated in the MVP routing stub unless separately allowed through Communication Service and the Communication Review Workflow.

No provider contact occurs from routing preview.

### 12.1 Minimum Disclosure

A provider inquiry should disclose only the minimum allowed information for its purpose.

The routing preview must not assume full Matter or customer data may be shared.

### 12.2 Instruction Requires a Separate Boundary

A provider instruction is external-facing and potentially commitment-forming.

It requires:

- selected provider under an enabled contract;
- reviewed service scope;
- approved commercial context;
- exact attachments;
- sender authority;
- Communication review;
- Permission and Policy;
- separate send execution through Communication Service.

---

## 13. Task Plan Preview

The pattern may prepare planned Tasks such as:

- review provider candidates;
- confirm provider status;
- confirm availability;
- obtain conflict clearance;
- request quote;
- verify commercial terms;
- confirm client constraint;
- prepare provider recommendation review;
- prepare Communication review;
- obtain authorized selection.

The Task plan is not active.

The current MVP stub must not create active Tasks.

Future active Tasks may be created only through Task Service after Book 02 enables the applicable apply path.

AI suggestions do not activate Tasks.

---

## 14. AI-Assisted Routing

AI may:

- summarize routing context;
- identify candidate data gaps;
- compare visible factors;
- explain why candidates appeared;
- detect inconsistent provider data;
- prepare questions;
- prepare a conditional recommendation;
- flag risk;
- prepare a provider inquiry outline.

AI must not:

- select the final provider;
- approve commercial terms;
- certify availability;
- certify conflict clearance;
- engage a provider;
- commit an Order;
- send an inquiry or instruction;
- create active Tasks;
- mutate Routing state;
- emit Events.

### 14.1 Ranking Boundary

AI may sort or group candidates for review only when:

- factors are governed;
- source scope is visible;
- missing data is disclosed;
- weighting is explainable;
- Policy permits comparison;
- output is marked non-final.

A ranked list must not be treated as a final selection queue.

### 14.2 Learning From Prior Outcomes

Historical outcomes may help identify questions.

They must not become hidden discrimination, unreviewed exclusion or unrestricted provider scoring.

Policy, data quality, representativeness and current context remain relevant.

---

## 15. Permission and Policy

Permission may govern:

- routing preview;
- provider reference access;
- Partner access;
- Service Network access;
- Matter and Order access;
- commercial-term access;
- future selection or engagement.

Policy may:

- hide provider existence;
- redact commercial terms;
- restrict Partner relationships;
- restrict Service Network visibility;
- limit cross-organization disclosure;
- restrict AI source use;
- require Human Review;
- downgrade to safe summary;
- block preview.

Permission allowance does not override Policy.

Policy visibility does not grant selection authority.

Human Review does not bypass either.

---

## 16. Commercial Terms Boundary

Commercial data may include:

- fees;
- currency;
- included services;
- exclusions;
- taxes;
- disbursements;
- payment timing;
- validity period;
- volume arrangements;
- confidential negotiated terms.

The preview must preserve:

- source;
- date;
- scope;
- visibility;
- currency;
- missing conditions;
- expiry;
- whether terms were merely quoted or approved.

It must not:

- compare hidden terms as if complete;
- convert a quote into approved cost;
- approve payment;
- bind a provider;
- expand an Order.

---

## 17. Trace and Audit

Current preview has no side effects and does not emit Events.

Where a preview result is retained under an owning contract, audit context should make it possible to understand:

- who requested preview;
- which organization and Matter/Order context applied;
- which sources were used;
- which candidates were visible;
- which fields were omitted;
- what AI contributed;
- what comparison factors were used;
- why Human Review was required;
- that no final selection occurred;
- that no provider was contacted;
- which Workflow version was evaluated.

Event references, where later returned by owning Services, remain trace rather than selection commands.

---

## 18. Safe Failure

Controlled outcomes may include:

- validation failure;
- invalid reference;
- Permission denied;
- Policy restricted;
- Human Review required;
- unsupported version;
- invalid state;
- NotFound under non-disclosure;
- conflict;
- apply not implemented;
- internal safe error.

Errors must not expose:

- database identifiers;
- restricted provider data;
- commercial terms;
- Partner relationship internals;
- Service Network internals;
- private risk notes;
- Policy internals;
- Permission internals;
- prompts;
- hidden reasoning;
- stack traces.

A safe preview failure should state, where allowed:

- missing routing input;
- restricted factor;
- required role;
- safe next question;
- whether a new preview may be attempted;
- that no selection or contact occurred.

---

## 19. Example — Local Associate for an Office Action

A Matter requires local support in a target jurisdiction.

The available context includes:

- service type: Office Action response support;
- verified jurisdiction reference;
- response preparation Matter;
- stated deadline;
- language requirement;
- Order budget note;
- two preferred providers;
- one excluded provider;
- incomplete current availability data.

### 19.1 Preview

The pattern:

- validates visible references;
- confirms that provider commercial terms require additional Policy access;
- shows two candidate providers;
- identifies missing availability and conflict information;
- preserves the excluded provider without exposing a restricted reason;
- compares jurisdiction and language capabilities;
- flags that the deadline source requires professional verification;
- prepares an availability/quote inquiry outline;
- requires Human Review;
- states that final selection was not made.

### 19.2 AI Assistance

AI prepares:

- candidate comparison;
- missing-data list;
- conditional recommendation;
- questions for availability, conflict and fee review.

It cannot select either provider.

### 19.3 MVP Stop

Apply is requested accidentally.

The Workflow returns a safe not-enabled result.

No Task, Communication, selection, Order change or Event is created.

### 19.4 Future Handoff

If a later phase enables apply, the prepared review package may support:

- authorized selection;
- commercial approval;
- Communication review;
- provider instruction.

Those remain separate governed actions.

---

## 20. Pattern Acceptance Checklist

The Provider Routing Preparation Pattern is correct when:

- [ ] current MVP depth is explicitly preview-only;
- [ ] Workflow Contract breadth does not silently enable current apply;
- [ ] routing need, candidate, eligibility, recommendation, selection, engagement and instruction remain distinct;
- [ ] Matter and Order contexts are both respected;
- [ ] urgency does not bypass governance;
- [ ] candidate sources and freshness are visible;
- [ ] search order is not presented as quality ranking;
- [ ] missing data is not silently converted into a poor score;
- [ ] commercial terms remain Policy-controlled and time-bound;
- [ ] comparison factors preserve source and limitations;
- [ ] AI output remains non-final;
- [ ] final provider selection requires Human Review;
- [ ] Human Review does not create engagement;
- [ ] preview has no side effects;
- [ ] apply returns a controlled disabled result;
- [ ] no active Tasks are created;
- [ ] no Communication is created or sent;
- [ ] no Matter or Order state is changed;
- [ ] no provider commitment or payment occurs;
- [ ] no Events are emitted by the Workflow;
- [ ] safe errors do not expose provider or network internals.

---

## 21. Product Boundary

Book 04 may present provider candidates, comparisons, missing data and review requirements. It must show that the result is advisory and that apply is unavailable. Book 03 does not define ranking widgets, selection controls or marketplace behavior.

## 22. Implementation Boundary

This pattern adds no scoring engine, automatic selection, conflict engine, engagement contract, payment, provider connector or send capability. Moving beyond preview requires a separate Core and Execution scope decision.

## 23. Chapter Result

The Provider Routing Preparation Pattern creates a governed decision package without creating a provider decision.

```text
Resolve the routing need.
Discover candidates without assuming eligibility.
Validate visible facts without claiming complete knowledge.
Compare without hiding sources or missing data.
Recommend conditionally.
Require Human Review.
Keep apply disabled in the current MVP.
Do not select, engage, instruct, pay or emit.
```

The pattern succeeds when an authorized human can understand the available choices and their limits without the system having created an external commitment.

The next chapter defines the **Office Action Response Preparation Pattern**, where notice intake, deadline context, issue analysis, Evidence and response drafting must be coordinated without allowing AI or Workflow to decide final legal strategy or submit an official response.
