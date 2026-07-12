# B03-CH-17 — Intake Execution Pattern

## Chapter Purpose

This chapter begins Part III — Execution Patterns.

Part II defined the shared architecture for state, Workflow coordination, Tasks, Human Review, Communication, Event trace, Permission, Policy and Human–AI handoff. Part III now applies those boundaries to recurring operational patterns.

The Intake Execution Pattern turns an initial request, uploaded material or observed customer need into a governed preparation result.

It answers:

```text
What has been received?
What can be treated as a source fact?
Which Core references already exist?
What is missing, conflicting or restricted?
Which workflow preview is applicable?
Which Tasks may be planned?
Which review or governance gates must stop progress?
What may be applied through owning Services?
What must remain prepared but unexecuted?
```

Intake is not a promise to accept an engagement, open every downstream object, recommend a final legal strategy or begin filing.

Its purpose is to convert incomplete and potentially ambiguous input into a traceable readiness decision.

```text
Input arrives.
Execution preserves source and uncertainty.
Preview structures the possible work.
Missing information becomes an explicit outcome.
Gates determine whether apply is allowed.
Owning services perform any allowed creation.
The result identifies what exists and what must happen next.
```

---

## 1. Dependency Baseline

This chapter applies the architecture established in:

- [Chapter 08 — Execution Layer Overview](B03-CH-08_Execution_Layer_Overview.md)
- [Chapter 09 — Execution Object and State Model](B03-CH-09_Execution_Object_and_State_Model.md)
- [Chapter 10 — Workflow Coordination Model](B03-CH-10_Workflow_Coordination_Model.md)
- [Chapter 11 — Task Lifecycle Model](B03-CH-11_Task_Lifecycle_Model.md)
- [Chapter 12 — Review and Approval Lifecycle](B03-CH-12_Review_and_Approval_Lifecycle.md)
- [Chapter 15 — Permission and Policy Gates](B03-CH-15_Permission_and_Policy_Gates.md)
- [Chapter 16 — Human–AI Execution Handoff](B03-CH-16_Human_AI_Execution_Handoff.md)

Its primary Book 02 sources are:

- [Customer Intake Workflow](../../book-02-core-specification/core-specs/workflows/customer-intake-workflow.md)
- [Customer Intake Workflow Contract](../../book-02-core-specification/core-specs/contracts/workflows/customer-intake-workflow-contract.md)
- [Workflow Specifications Index](../../book-02-core-specification/core-specs/workflows/index.md)
- [Workflow Contract Index](../../book-02-core-specification/core-specs/contracts/workflows/index.md)
- [Customer API Contract](../../book-02-core-specification/core-specs/contracts/api/customer-api-contract.md)
- [Brand API Contract](../../book-02-core-specification/core-specs/contracts/api/brand-api-contract.md)
- [Matter API Contract](../../book-02-core-specification/core-specs/contracts/api/matter-api-contract.md)
- [Order API Contract](../../book-02-core-specification/core-specs/contracts/api/order-api-contract.md)
- [Document API Contract](../../book-02-core-specification/core-specs/contracts/api/document-api-contract.md)
- [Task API Contract](../../book-02-core-specification/core-specs/contracts/api/task-api-contract.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [AI Context Contract](../../book-02-core-specification/core-specs/contracts/common/ai-context.md)
- [Idempotency Contract](../../book-02-core-specification/core-specs/contracts/common/idempotency.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)

The Book 03 planning boundary remains defined by:

- [MVP Execution Boundary](../planning/B03-PLN-0007_MVP_Execution_Boundary.md)
- [Review Gate Model](../planning/B03-PLN-0008_Review_Gate_Model.md)

Book 02 owns the Customer Intake Workflow, its contract, related Objects, Services, controlled values and validation rules. This chapter explains how those sources operate as an execution pattern. It does not define a second intake contract.

---

## 2. Pattern Position

Intake sits upstream of more specialized preparation patterns.

```text
Unstructured or partially structured input
→ Intake Execution Pattern
→ governed Customer / Brand / Matter / Order context
→ Document references and active Tasks where apply is allowed
→ Application, Communication, Provider Routing or another preparation pattern
```

The pattern can receive input from:

- an authorized Product request;
- an API request accepted under contract;
- an internal operator;
- a customer or partner Communication;
- uploaded Documents;
- an approved manual handoff;
- a resumed Workflow;
- an AI-assisted extraction result;
- an observed condition that is permitted to start evaluation.

An Event reference may contribute context, but an Event is not command authority by itself.

The intake result may be:

- preview ready;
- missing required information;
- duplicate-sensitive;
- review required;
- Permission denied;
- Policy restricted;
- not applicable;
- ready for apply;
- applied through owning Services;
- safely failed;
- paused for a later continuation.

A correct intake does not have to reach apply.

---

## 3. The Intake Lock

The entire pattern is governed by one lock:

```text
Intake may structure a request.
Intake may not manufacture professional truth.
Intake may prepare a Workflow preview.
Preview may not create state.
Apply may coordinate owning Services only after current gates pass.
Apply does not authorize external filing, payment, provider commitment or send.
```

This lock prevents five common forms of authority drift.

### 3.1 Receipt Is Not Acceptance

Receiving a request does not mean:

- the customer has been accepted;
- an engagement exists;
- a quoted scope is approved;
- a Matter is valid for every intended use;
- an Order is commercially approved;
- filing work has begun.

### 3.2 Data Presence Is Not Data Reliability

A name, jurisdiction, logo or goods description may be present while remaining:

- unverified;
- ambiguous;
- inconsistent;
- stale;
- policy restricted;
- supplied by an unknown source;
- inferred rather than stated.

### 3.3 Completeness Is Scope-Relative

An intake may be complete enough to request more information but not complete enough to open an Order.

It may be complete enough to create an internal Task but not complete enough to prepare an application.

There is no universal “intake complete” truth outside the governing contract and intended next action.

### 3.4 Preview Is Not Apply

Preview can validate, compare, identify gaps and prepare a Task plan without side effects.

No Product label, AI confidence score or operator expectation may silently convert preview into apply.

### 3.5 Apply Is Not Downstream Execution

Even a successfully applied Customer Intake Workflow does not:

- submit a trademark application;
- finalize classification;
- select a provider;
- send an external Communication;
- execute payment;
- certify registrability;
- certify evidence sufficiency.

It creates or links only those Core records that owning Services are allowed to create under the contract.

---

## 4. Intake Execution Context

Before coordination, Execution assembles a bounded context.

The context should distinguish:

| Context area | Question |
|---|---|
| Actor | Who requested or resumed intake? |
| Organization | Under which organization and data boundary? |
| Source | Where did each supplied fact or file originate? |
| Subject | Which existing Customer, Brand, Matter, Order or Document references may apply? |
| Intent | What service or outcome is being requested? |
| Version | Which workflow and contract versions govern evaluation? |
| Governance | Which Permission, Policy and Human Review requirements apply? |
| AI involvement | Which Agent capability prepared or transformed material? |
| Trace | Which correlation, prior Workflow or Event references connect the request? |
| Continuation | Is this a new intake, retry, replay or resumed missing-information loop? |

This context is not a new Core Object.

It is the minimum operational view needed to use existing contracts safely.

### 4.1 Source Categories

Execution should preserve the difference among:

- user-provided facts;
- uploaded Document content;
- existing Core facts;
- external source facts;
- operator notes;
- AI extraction;
- AI inference;
- prior review decisions;
- owning-service results.

A field populated by AI extraction remains derived from a source. An AI inference is not converted into a customer declaration.

### 4.2 Unknown Must Remain Unknown

When a required fact is unavailable, Execution should preserve an explicit missing or unknown condition.

Unsafe behavior includes:

- guessing a legal entity name from an email domain;
- treating a contact as the rights owner;
- inferring final jurisdiction from language;
- treating a logo uploader as the Brand owner;
- inventing goods or services from a website description;
- assuming urgency creates authority.

Unknown information should produce a gap, question, Task plan or safe pause.

---

## 5. Pattern Stages

The pattern contains eight conceptual stages.

```text
1. Receive and preserve source
2. Resolve context and references
3. Normalize without inventing
4. Assess duplication and conflict
5. Prepare Workflow preview
6. Evaluate readiness and gates
7. Coordinate apply through owning Services
8. Return traceable outcome and next action
```

These are responsibility stages, not a required technical pipeline.

---

## 6. Stage 1 — Receive and Preserve Source

Execution first records what was actually received.

It should preserve, where allowed:

- source reference;
- received time;
- actor and organization;
- original Document references;
- safe source type;
- language;
- declared intent;
- correlation context;
- AI-assisted flag;
- known omissions.

Receipt must not rewrite the source into a cleaner but unsupported account.

For example, a message saying “we want to protect this logo in Europe” contains useful intent but does not yet establish:

- the applicant;
- ownership;
- exact jurisdictions;
- classes;
- goods and services;
- filing basis;
- budget approval;
- authority to proceed.

The original request and the structured interpretation should remain distinguishable.

---

## 7. Stage 2 — Resolve Context and References

Execution attempts to resolve existing public-safe references.

Possible subjects include:

- Customer;
- Brand;
- Matter;
- Order;
- Document;
- prior Workflow;
- active Task;
- Communication;
- actor and organization.

Reference validation answers whether a reference has an allowed shape and can be used in the current operation.

It does not automatically grant:

- read access;
- update access;
- cross-organization access;
- raw Document content access;
- authority to link or mutate the subject.

Permission and Policy still apply.

### 7.1 Existing Candidate Is Not Confirmed Match

Duplicate-sensitive intake may identify possible existing Customers or Brands.

A candidate match is not identity confirmation.

Execution should preserve:

- match basis;
- uncertainty;
- conflicting fields;
- restricted fields omitted;
- required human confirmation;
- safe next action.

It must not merge records or reuse an existing Customer solely because names look similar.

---

## 8. Stage 3 — Normalize Without Inventing

Normalization converts allowed inputs into forms usable by the Workflow Contract.

It may:

- trim or standardize safe formatting;
- separate declared customer and contact names;
- identify language;
- classify a supplied file by a provisional type;
- map an explicitly requested service to a controlled candidate;
- extract stated jurisdictions;
- preserve original and normalized values;
- mark ambiguity.

Normalization must not:

- resolve a professional conclusion;
- replace missing facts with defaults that change meaning;
- silently translate an uncertain applicant name into a legal identity;
- select final goods or services;
- certify a Document;
- convert a recommendation into a request.

Material transformations should preserve provenance.

---

## 9. Stage 4 — Assess Duplication and Conflict

Intake may encounter two distinct problems.

### 9.1 Duplicate Risk

The same semantic intake may have been submitted before.

Execution uses the Idempotency Contract for apply-sensitive duplication. The same valid key and semantic request should replay safely without duplicating:

- Customer;
- Brand;
- Matter;
- Order;
- active Tasks;
- Communication drafts;
- Events.

A reused key with materially different semantics should produce conflict rather than overwrite.

### 9.2 Business Candidate Duplication

Separate requests may refer to the same real-world customer, Brand or matter.

This is not solved by idempotency alone.

Execution may identify candidate duplication, but owning Services and applicable review rules decide whether records should be reused, linked or kept separate.

### 9.3 Conflicting Sources

When sources disagree, the result should show a conflict such as:

- different owner names;
- inconsistent jurisdictions;
- different service scopes;
- stale versus current address;
- conflicting deadline statements;
- incompatible Document versions.

AI may summarize the conflict. It may not choose which professional fact is authoritative.

---

## 10. Stage 5 — Prepare Workflow Preview

Preview is the default safe evaluation mode.

It may:

- validate request shape and references;
- identify missing Customer or Brand fields;
- assess Matter and Order preparation needs;
- check Document references;
- prepare a Task plan;
- prepare an intake summary;
- prepare a draft missing-information request;
- disclose Policy omissions;
- identify Human Review requirements;
- return safe warnings and errors.

Preview must not:

- create or update Customer, Brand, Matter or Order state;
- attach Documents;
- create active Tasks;
- create or send Communications;
- emit Events;
- execute payment;
- start official filing;
- select a provider.

The preview result should state both readiness and limitation.

A useful preview is not merely “valid” or “invalid.” It explains what the current input permits next.

---

## 11. Readiness Model

Intake readiness is better represented as a bounded outcome than a single percentage.

A conceptual readiness view may contain:

| Dimension | Meaning |
|---|---|
| Source readiness | Required sources exist and their provenance is visible |
| Reference readiness | Required existing references are valid for evaluation |
| Information readiness | Required contract inputs are present or explicitly missing |
| Document readiness | References are valid and allowed for the intended stage |
| Governance readiness | Permission, Policy and Human Review requirements are known |
| Workflow readiness | Preview can determine an allowed next step |
| Apply readiness | Apply-specific version, idempotency and gates are satisfied |
| Downstream readiness | A named next pattern can begin preparation |

This view is conceptual and non-Core.

It must not replace Book 02 controlled outcomes.

### 11.1 Missing Information Is an Operational Result

A missing-information result should identify:

- missing item;
- why it is needed;
- which intended action depends on it;
- whether a safe alternative path exists;
- who may supply or verify it;
- whether a Task plan is appropriate;
- whether a draft Communication may be prepared;
- what must not proceed.

The result should avoid asking for every conceivable field. It should request the minimum information needed for the next governed decision.

### 11.2 Restricted Is Different from Missing

A field may exist but be unavailable because of Policy.

Execution must not describe it as absent if that would mislead the receiver.

Where disclosure is allowed, the result may state that context was omitted or restricted. Where non-disclosure is required, it may return a safe result such as NotFound without revealing existence.

---

## 12. Stage 6 — Evaluate Readiness and Gates

Before apply, Execution refreshes:

- actor and organization;
- target references;
- workflow contract version;
- requested operation;
- Permission;
- Policy;
- Human Review requirement;
- idempotency;
- state eligibility;
- material source changes.

Permission and Policy are independent.

Human Review does not replace either.

### 12.1 Review Gate Examples

Review may be required for:

- cross-organization intake;
- restricted customer data access;
- professional intake confirmation;
- an external-facing missing-information draft;
- transition toward filing readiness;
- responsibility-sensitive acceptance.

The review scope must be specific.

“Approve intake” is too broad if the intended decision is only to approve a draft request for missing applicant information.

### 12.2 Gate Outcomes

The gate may:

- allow preview only;
- allow apply;
- require Human Review;
- require more information;
- redact output;
- block the operation;
- return safe non-disclosure;
- require escalation;
- require a newer contract version.

No outcome should silently downgrade a protected apply into an ungoverned mutation.

---

## 13. Stage 7 — Coordinate Apply Through Owning Services

Apply is allowed only when the governing contract permits it.

Execution coordinates. Owning services perform their own behavior.

| Result area | Owner |
|---|---|
| Customer creation or update | Customer Service |
| Brand creation or update | Brand Service |
| Matter creation | Matter Service |
| Order creation | Order Service |
| Document validation or linking | Document Service |
| Active Task creation | Task Service |
| Communication draft creation | Communication Service |
| Event trace | Owning service or Event Service integration |

The Workflow layer must not perform these mutations directly.

### 13.1 Partial Apply Must Be Explicit

If an apply attempt can produce some allowed service results before a later safe stop, the outcome must clearly distinguish:

- created references;
- unchanged subjects;
- failed or blocked steps;
- compensating action if defined by contract;
- Tasks created;
- review still required;
- safe continuation path.

Book 03 does not invent transaction or rollback semantics. Those require owning contracts.

### 13.2 No Hidden Downstream Commitment

Creating a Matter or draft Order must not be presented as:

- engagement acceptance;
- payment approval;
- provider appointment;
- filing authorization;
- legal conclusion.

The resulting state and Product explanation must remain exact.

---

## 14. Task Planning and Activation

Preview may prepare a Task plan.

Examples include:

- confirm customer identity;
- confirm Brand owner;
- collect a logo file;
- collect applicant documents;
- confirm target jurisdiction;
- obtain goods and services description;
- review a restricted intake;
- prepare the next Workflow preview.

A Task plan is not an active Task.

During apply, Task Service may create active Tasks under the Task API Contract.

AI may suggest Task content, priority or dependencies. It may not create, assign, transition or complete an active Task by its own authority.

Task completion also does not imply that the intake, Matter, Order or downstream application is complete.

---

## 15. Document Handling

Intake frequently includes Documents before their meaning is settled.

Execution should distinguish:

- Document reference validity;
- permission to access metadata;
- permission to access content;
- provisional Document type;
- linkage to a subject;
- professional sufficiency;
- official acceptability.

A valid Document reference does not prove legal sufficiency.

AI may extract or summarize Document content only within allowed scope. It must disclose source scope, uncertainty and Policy omissions.

A logo file may support Brand preparation while remaining insufficient for an official filing package.

An identity document may exist while access to its content remains restricted.

---

## 16. Communication Handoff

Intake may prepare a missing-information request, intake confirmation draft or internal note.

That output remains a draft.

The handoff should identify:

- intended recipient or audience;
- purpose;
- source facts used;
- missing information requested;
- restricted facts omitted;
- AI involvement;
- review requirement;
- version;
- prohibited action: send.

External sending belongs to the governed Communication path described in Chapter 13 and the Communication Review Pattern in Chapter 19.

Intake success must never be inferred from a draft being prepared.

---

## 17. AI-Assisted Intake

AI can reduce intake friction by:

- extracting stated facts;
- summarizing a request;
- comparing versions;
- identifying missing information;
- detecting apparent conflicts;
- proposing the next minimum questions;
- preparing a Task plan suggestion;
- drafting a Communication;
- explaining the preview result.

AI must not:

- approve the customer;
- certify identity or ownership;
- determine registrability;
- make a final jurisdiction or classification decision;
- certify Documents or evidence;
- accept commercial scope;
- apply the Workflow;
- create active Tasks;
- send Communications;
- execute filing or payment;
- emit Events.

### 17.1 Minimize Questions Without Hiding Assumptions

Good AI-assisted intake asks fewer, more consequential questions.

It should not achieve a short interaction by guessing.

A useful sequence is:

```text
Use known governed facts.
Extract only supported statements.
Identify the next decision.
Ask only for gaps blocking that decision.
Offer bounded options when the source supports them.
Expose assumptions and uncertainty.
```

This preserves the product goal of low-friction intake without moving professional truth into AI.

---

## 18. Trace and Audit

The outcome should preserve trace references allowed by Policy.

Trace may cover:

- request receipt;
- workflow preview;
- Permission evaluation;
- Policy evaluation;
- Human Review;
- service-owned creation or update;
- active Task creation;
- Communication draft creation;
- safe error or blocked outcome;
- idempotent replay.

The Workflow does not emit domain Events directly.

Event references record completed facts. They do not authorize the next action.

Audit context should make it possible to reconstruct:

- what input was received;
- which version was evaluated;
- what AI contributed;
- which fields were missing or restricted;
- which gate stopped or allowed progress;
- which owning Service produced each state change;
- what next action was exposed.

---

## 19. Safe Failure and Continuation

Intake must fail safely.

Expected outcomes include:

- validation failure;
- invalid reference;
- Permission denied;
- Policy restricted;
- Human Review required;
- idempotency key required;
- idempotency conflict;
- unsupported version;
- state conflict;
- not found under non-disclosure;
- internal safe error.

Errors must not expose:

- database identifiers;
- restricted customer data;
- restricted Document content;
- Permission internals;
- Policy internals;
- prompts;
- hidden reasoning;
- stack traces.

### 19.1 Continuation Is Not Replay

A continuation supplies new information or a new decision to resume preparation.

A replay repeats the same semantic apply request under idempotency.

A retry attempts an operation again after a retryable failure.

These must remain distinguishable.

### 19.2 Pause Must Be Recoverable

A safe pause should state, where allowed:

- current pattern outcome;
- unresolved requirements;
- next responsible role;
- allowed next action;
- version and reference context;
- whether a new preview is required;
- whether prior review remains valid.

---

## 20. Example — Trademark Service Intake

A customer supplies:

- a company name;
- a logo;
- a short product description;
- the statement “we need protection in the United States and Europe.”

Execution should not jump directly to an application.

### 20.1 Receive

Preserve the message, logo Document reference, actor, organization, time and source.

### 20.2 Resolve

Check whether Customer or Brand candidates already exist, without confirming a match from name similarity alone.

### 20.3 Normalize

Separate:

- declared company name;
- logo reference;
- product description;
- requested regions;
- unknown applicant authority;
- unknown exact European filing route;
- unknown goods and services scope.

### 20.4 Preview

The Customer Intake Workflow preview may show:

- Customer candidate requires confirmation;
- Brand can be prepared from stated name/logo context;
- Matter type may be trademark application preparation;
- target jurisdiction details require clarification;
- applicant identity documents are missing;
- a Task plan can be prepared;
- a missing-information draft can be prepared;
- filing readiness is not established.

### 20.5 Gate

Permission and Policy are evaluated. Human Review is required if a professional or external-facing confirmation is proposed.

### 20.6 Apply

If allowed, owning Services may create or link Customer, Brand, Matter and draft Order context; Document Service may validate or link allowed references; Task Service may create active information-collection Tasks.

### 20.7 Handoff

The next outcome may be:

```text
Intake applied for preparation.
Application filing is not authorized.
Application Preparation Pattern may begin after the named gaps are resolved.
```

This is a successful intake even though no filing occurred.

---

## 21. Pattern Acceptance Checklist

An Intake Execution Pattern is correctly applied when:

- [ ] source facts, derived values and AI inferences remain distinguishable;
- [ ] unknown information remains explicit;
- [ ] existing candidates are not silently treated as confirmed matches;
- [ ] reference validity is not treated as access or mutation authority;
- [ ] preview remains side-effect free;
- [ ] readiness is tied to a named next action;
- [ ] missing and Policy-restricted information remain distinct;
- [ ] Permission and Policy are independently evaluated;
- [ ] required Human Review is specific and version-bound;
- [ ] apply requires current version and idempotency context;
- [ ] owning Services perform state changes;
- [ ] Task plans do not become active Tasks outside Task Service;
- [ ] draft Communications are not sent;
- [ ] AI assistance remains preparation-only;
- [ ] Events are returned as trace, not emitted by the Workflow;
- [ ] safe failure exposes a recoverable next step where allowed;
- [ ] intake success is not confused with engagement, filing, payment or professional approval.

---

## 22. Product Boundary

Book 04 may define intake questions, upload flows, progress, missing-information views and the transition to later preparation. Book 03 requires those Products to preserve candidate, verified, reviewed and applied states. It does not define screens or interaction design.

## 23. Implementation Boundary

This pattern adds no new Intake object, Workflow Contract, Service, API, persistence model, matching engine or legal-validation rule. Implementation must consume the cited Book 02 contracts and owning Services.

## 24. Chapter Result

The Intake Execution Pattern establishes a governed entry into operational work.

```text
Receive without assuming.
Structure without inventing.
Preview without side effects.
Expose gaps without hiding restriction.
Gate before apply.
Mutate only through owning Services.
Hand off an exact next action.
```

The pattern succeeds when it creates trustworthy preparation context, including when the correct result is to pause.

The next chapter applies this prepared context to the **Application Preparation Pattern**, where application readiness must be coordinated without turning preparation into filing authority.
