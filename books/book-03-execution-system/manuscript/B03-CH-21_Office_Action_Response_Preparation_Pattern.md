# B03-CH-21 — Office Action Response Preparation Pattern

## Chapter Purpose

The Office Action Response Preparation Pattern converts an official notice and related Matter context into a governed professional preparation package without certifying the deadline, deciding final legal strategy or submitting an official response.

Official actions may include:

- examination opinions;
- refusals;
- objections;
- requirements;
- notices;
- classification issues;
- cited-mark issues;
- formal deficiencies;
- requests for evidence;
- other office communications requiring analysis or response.

The pattern answers:

```text
Which official notice and Trademark are in scope?
What can be read directly from the notice?
Which dates are source facts, calculated candidates or professionally confirmed deadlines?
Which issue categories appear to apply?
What Documents, Evidence and Knowledge sources are available?
Which facts are missing, conflicting or Policy-restricted?
What possible response paths require professional evaluation?
What review package can be prepared?
Why must current MVP execution stop at preview?
What must remain forbidden before official submission?
```

The governing path is:

```text
Official notice source
→ source and reference validation
→ notice extraction with provenance
→ deadline context preparation
→ issue and affected-scope preparation
→ Document / Evidence / Knowledge gap analysis
→ possible response-path preview
→ Human Review requirement
→ safe preview result
→ stop before strategy finalization or submission
```

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
- [Chapter 18 — Application Preparation Pattern](B03-CH-18_Application_Preparation_Pattern.md)
- [Chapter 19 — Communication Review Pattern](B03-CH-19_Communication_Review_Pattern.md)
- [Chapter 20 — Provider Routing Preparation Pattern](B03-CH-20_Provider_Routing_Preparation_Pattern.md)

Its primary Book 02 sources are:

- [Office Action Response Workflow](../../book-02-core-specification/core-specs/workflows/office-action-response-workflow.md)
- [Office Action Response Workflow Contract](../../book-02-core-specification/core-specs/contracts/workflows/office-action-response-workflow-contract.md)
- [Workflow Specifications Index](../../book-02-core-specification/core-specs/workflows/index.md)
- [Workflow Contract Index](../../book-02-core-specification/core-specs/contracts/workflows/index.md)
- [Trademark API Contract](../../book-02-core-specification/core-specs/contracts/api/trademark-api-contract.md)
- [Jurisdiction API Contract](../../book-02-core-specification/core-specs/contracts/api/jurisdiction-api-contract.md)
- [Classification API Contract](../../book-02-core-specification/core-specs/contracts/api/classification-api-contract.md)
- [Document API Contract](../../book-02-core-specification/core-specs/contracts/api/document-api-contract.md)
- [Evidence API Contract](../../book-02-core-specification/core-specs/contracts/api/evidence-api-contract.md)
- [Knowledge API Contract](../../book-02-core-specification/core-specs/contracts/api/knowledge-api-contract.md)
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

Book 02 owns the Workflow, contract, Objects, Services, controlled values, validation rules and implementation depth.

### 1.1 Current Depth Rule

The current Office Action Response Workflow is:

```text
Stub Now
Level 1/2
Preview / Validation Stub
Apply not production-enabled
```

The Workflow Contract may describe a future governed preparation model. It does not enable production apply in the current MVP.

This chapter therefore preserves the stricter current rule:

```text
Preview may validate and organize professional preparation.
Apply must return a controlled disabled result with no side effects.
No official response may be submitted.
```

---

## 2. Pattern Position

The pattern is downstream of a Trademark application and an official notice.

It may connect to:

- Matter and Order preparation;
- Document and Evidence handling;
- Classification review;
- Knowledge retrieval;
- Task planning;
- Communication Review;
- Provider Routing Preparation;
- Human Review;
- later official submission under an enabled owning contract.

Current outputs may include:

- validated source references;
- plain-language notice summary;
- detected issue-category candidates;
- missing notice fields;
- deadline-present indicator;
- deadline not certified warning;
- affected-scope preview;
- possible response paths;
- required Documents and Evidence;
- professional review requirements;
- Task plan preview;
- Communication outline;
- safe errors.

The pattern does not create a filed response.

---

## 3. Response Preparation Boundary

Several stages must remain distinct.

| Stage | Meaning |
|---|---|
| Notice receipt | A source was received |
| Notice validation | The source reference and access can be evaluated |
| Extraction | Stated facts are captured with provenance |
| Deadline context | Date sources and candidate deadline meaning are organized |
| Issue categorization | Possible categories are identified |
| Legal analysis | An authorized professional evaluates law and facts |
| Strategy selection | An authorized decision chooses a response path |
| Evidence preparation | Sources and use context are prepared |
| Drafting | Proposed response content is prepared |
| Review | The exact package is evaluated |
| Filing authorization | A separate protected decision permits submission |
| Submission | An official external action occurs |
| Office acknowledgment | The office confirms receipt where supported |

The current MVP stops before legal analysis becomes final and before any state-changing preparation apply.

### 3.1 Receipt Is Not Verified Official Status

An uploaded notice may be:

- incomplete;
- duplicated;
- mistranslated;
- associated with the wrong Trademark;
- missing pages;
- superseded;
- an informal copy;
- inaccessible under Policy.

### 3.2 Extraction Is Not Interpretation

AI or a human may extract a date, cited mark or affected class.

Extraction does not certify:

- legal meaning;
- deadline;
- response options;
- consequence;
- accuracy of OCR;
- current official status.

### 3.3 Response Outline Is Not Legal Strategy

An outline can organize issues and candidate paths.

It does not decide which argument, amendment, evidence, appeal or procedural step is professionally appropriate.

### 3.4 Reviewed Draft Is Not Filed

Even an approved draft must pass a separate filing authorization and official submission boundary.

---

## 4. Official Notice Source Package

The pattern begins with a stable source package.

It should identify, where available:

- official notice Document reference;
- source type;
- issuing office;
- Trademark reference;
- application or registration context;
- issue date as stated;
- response date as stated;
- notice type as stated or unknown;
- page and attachment completeness;
- language;
- source version;
- translated version;
- OCR or extraction version;
- prior related notices;
- Policy omissions;
- AI involvement.

### 4.1 Original, OCR and Translation

These must remain distinct:

```text
Original Document
≠ OCR text
≠ translated text
≠ AI summary
≠ professional interpretation
```

The reviewer should be able to identify which layer supports each statement.

### 4.2 Document Reference Boundary

A valid Document reference does not prove:

- authenticity;
- completeness;
- current official status;
- permission to read raw content;
- professional sufficiency;
- correct linkage to the Trademark.

Document Service owns Document behavior and access rules.

### 4.3 Superseded Notices

A later notice may change or replace an earlier requirement.

The pattern may identify possible supersession.

It must not decide the authoritative notice without governed source and professional review.

---

## 5. Trademark, Matter and Order Context

The response package should resolve:

- Trademark reference and current visible state;
- applicant or owner context;
- jurisdiction;
- filing route where relevant;
- affected application or registration;
- Matter;
- Order;
- responsible organization;
- service scope;
- prior professional decisions;
- related Documents, Evidence and Communications.

### 5.1 Trademark State Is Not Rewritten From the Notice

A notice may describe official status.

The Workflow must not mutate Trademark state from extracted text.

Trademark Service owns that behavior and requires its own contract and evidence.

### 5.2 Matter and Order Mismatch

Examples include:

- the Matter covers review only, while filing work is requested;
- the Order excludes an appeal or hearing;
- local counsel is required but not routed;
- Evidence collection is outside approved scope;
- a new class or issue expands the work.

The preview should expose the mismatch rather than silently expand scope.

---

## 6. Deadline Context

Deadline handling is a high-risk preparation area.

The pattern should distinguish:

| Deadline element | Meaning |
|---|---|
| Stated date | A date appears in the source |
| Extracted date | A date was captured by human or machine |
| Calculated candidate | A rule or interval was applied provisionally |
| Professional confirmation | An authorized human confirmed the deadline within scope |
| System reminder | A Task or Notification may reference a date |
| Official extension result | An office or authorized provider confirmed a change |

These are not interchangeable.

### 6.1 Deadline Present Does Not Mean Certified

The preview may safely state:

```text
A response date appears in the notice.
Deadline certification remains false.
Professional confirmation is required.
```

### 6.2 Sources May Conflict

Possible conflicts include:

- notice date versus portal date;
- original versus translated date;
- calendar calculation versus stated deadline;
- local holiday treatment;
- service date versus issue date;
- extension availability;
- earlier versus later notice;
- office time zone.

The pattern should preserve the conflict and escalate.

### 6.3 Urgency

Urgency should be derived cautiously.

A near candidate date may justify priority or escalation.

It does not authorize:

- deadline certification;
- bypassing review;
- automatic provider selection;
- unreviewed filing;
- automatic customer communication.

### 6.4 Reminder Is Not Deadline Truth

A Task or reminder may help operations.

Completing or rescheduling it does not alter the official deadline.

---

## 7. Issue Categorization

The preview may identify possible categories such as:

- formal requirement;
- classification issue;
- absolute-ground issue;
- relative-ground or cited-mark issue;
- specimen or use-related issue;
- ownership or applicant issue;
- disclaimer or description issue;
- evidence request;
- procedural question;
- unknown.

These are candidates, not final legal conclusions.

### 7.1 Source Anchoring

Each detected issue should point to:

- notice section or page;
- quoted or summarized source;
- affected class or item where stated;
- cited reference where stated;
- confidence or uncertainty where allowed;
- required professional confirmation.

### 7.2 Multiple Issues

One notice may contain multiple independent issues with different:

- affected scope;
- evidence needs;
- response paths;
- reviewers;
- costs;
- deadlines;
- consequences.

The pattern should not compress them into one generic “refusal.”

### 7.3 Unknown Category Is Valid

If the source is incomplete or ambiguous, the correct result may be unknown plus a review requirement.

Forcing a category can create false professional truth.

---

## 8. Affected Scope Preparation

The preview may organize:

- affected classes;
- affected goods or services;
- cited marks;
- formal requirements;
- requested amendments;
- affected applicant details;
- Evidence demands;
- procedural options stated in the notice.

It must distinguish:

- source-stated scope;
- extracted scope;
- AI-inferred scope;
- professionally confirmed scope.

### 8.1 Partial Scope

An issue may affect only part of an application.

The pattern must not imply the entire Trademark is refused or abandoned unless the governing source supports it.

### 8.2 Classification Boundary

Classification Service owns Classification behavior.

AI may compare affected items and prepare questions.

It must not finalize amendments or certify acceptance.

---

## 9. Document, Evidence and Knowledge Preparation

Response preparation may require three different source classes.

### 9.1 Documents

Documents may include:

- official notice;
- application record;
- cited-mark material;
- prior correspondence;
- draft response;
- applicant instructions;
- authority documents.

Document presence does not prove professional sufficiency.

### 9.2 Evidence

Evidence may support:

- use;
- acquired distinctiveness;
- coexistence context;
- factual assertions;
- ownership;
- market conditions;
- other professionally reviewed propositions.

Evidence Service owns Evidence behavior.

A summary or sufficiency preview is not a legal sufficiency conclusion.

### 9.3 Knowledge

Knowledge sources may include governed:

- jurisdiction rules;
- office guidance;
- classification material;
- procedures;
- reviewed internal guidance;
- other allowed sources.

Knowledge retrieval does not certify that the source is current, complete or controlling for the specific Matter.

### 9.4 Source Hierarchy

The pattern should preserve:

- source authority;
- jurisdiction;
- effective date;
- version;
- applicability;
- review status;
- citation;
- missing or conflicting sources.

AI must not blend conflicting sources into a confident answer without disclosure.

---

## 10. Possible Response Paths

The preview may prepare candidate paths such as:

- request clarification;
- provide missing formal information;
- amend an identified field;
- amend Classification;
- submit Evidence;
- present argument;
- narrow scope;
- seek consent or coexistence-related review;
- request extension where legally available;
- pursue review, appeal or another procedure;
- accept a limited outcome;
- take no action after explicit professional/client decision.

These are illustrative preparation categories, not recommendations for a specific Matter.

### 10.1 Strategy Factors

Professional evaluation may consider:

- notice basis;
- affected scope;
- client objectives;
- Evidence;
- cost;
- timing;
- procedural availability;
- jurisdiction rules;
- cited rights;
- commercial value;
- provider requirements;
- Order scope;
- risk.

The Workflow and AI do not choose the final balance.

### 10.2 Success Probability

The pattern must not certify a probability of overcoming the notice.

If a prediction is later permitted, it remains:

- source-bound;
- uncertainty-disclosed;
- Policy-governed;
- non-final;
- subject to Human Review;
- not a guarantee.

Current Book 02 explicitly forbids success-probability certification.

---

## 11. Preview Behavior

Current MVP preview may:

- validate the request;
- validate Trademark, Matter and Document references;
- check Permission and Policy;
- identify missing notice fields;
- prepare notice summary;
- identify possible issue categories;
- show whether a deadline is present;
- keep deadline certification false;
- prepare affected-scope view;
- prepare possible response paths;
- identify Document and Evidence gaps;
- prepare Task plan preview;
- prepare Communication outline;
- prepare AI-assisted summary;
- require Human Review;
- return safe warnings and errors.

Preview must not:

- mutate Trademark or Matter;
- create Documents or Evidence;
- create active Tasks;
- create Communication;
- select a provider;
- certify the deadline;
- certify legal basis;
- finalize response strategy;
- certify Evidence sufficiency;
- approve filing readiness;
- submit an official response;
- emit Events.

### 11.1 Preview Result Statement

The result should state clearly:

```text
This is a response-preparation preview.
Detected issues and response paths require professional confirmation.
The deadline is not certified.
No official response was created or submitted.
Apply is not production-enabled.
```

---

## 12. Apply Is Disabled in Current MVP

An apply request must return a controlled disabled or invalid-state result.

It must be:

- side-effect free;
- non-retryable as a currently supported production operation;
- version-aware;
- safe under Policy;
- explicit about the unavailable capability.

It must not:

- create a Matter;
- attach Documents or Evidence;
- create active Tasks;
- create Communication;
- update Trademark status;
- select a provider;
- emit Events;
- submit a response;
- silently perform preview while claiming apply.

### 12.1 Future Enablement

A future Book 02 decision might enable governed preparation apply.

It would still require:

- owning-service mutation;
- current Workflow and contract versions;
- idempotency;
- Permission;
- Policy;
- Human Review;
- Task Service;
- Communication Service;
- Document and Evidence Services;
- safe Event trace;
- official submission as a separate protected boundary.

This chapter does not authorize that future scope.

---

## 13. Task Plan Preview

The preview may prepare planned Tasks such as:

- verify notice completeness;
- confirm Trademark linkage;
- confirm deadline professionally;
- review issue categories;
- analyze cited marks;
- review affected Classification;
- obtain client instructions;
- collect Documents;
- collect Evidence;
- retrieve current jurisdiction sources;
- prepare response outline;
- draft response;
- review response;
- prepare client Communication;
- route local provider review;
- prepare filing authorization.

The Task plan is not active.

Current MVP must not create active Tasks.

Future active Tasks may be created only through Task Service after an enabled apply path exists.

Task completion would not prove response submission.

---

## 14. Communication Preparation

Preview may prepare an outline for:

- client explanation;
- missing-information request;
- Evidence request;
- internal review note;
- local associate inquiry;
- filing-instruction draft.

It must preserve:

- draft status;
- source;
- uncertainty;
- deadline-not-certified warning where applicable;
- intended recipient;
- review requirement;
- Policy omissions.

The current stub does not create or send Communication.

Any future external message requires the Communication Review Pattern and Communication Service.

---

## 15. AI-Assisted Response Preparation

AI may:

- summarize the notice;
- extract stated dates and issues;
- identify missing pages or fields;
- suggest issue categories;
- compare cited references;
- identify Evidence gaps;
- retrieve governed Knowledge;
- prepare client questions;
- prepare a response outline;
- compare draft versions;
- flag unsupported claims;
- prepare a review checklist.

AI must not:

- certify the official deadline;
- certify the legal basis;
- choose final strategy;
- certify registrability;
- certify Evidence sufficiency;
- certify success probability;
- approve the response;
- select a final provider;
- send instructions;
- submit the response;
- mutate state;
- emit Events.

### 15.1 Citation and Provenance

AI-prepared analysis should identify:

- source Documents;
- Knowledge sources;
- source version;
- affected notice section;
- extracted versus inferred content;
- missing context;
- conflicting sources;
- Policy omissions.

### 15.2 Hallucination Risk

A plausible legal argument without a governed source is unsafe.

The pattern should treat unsupported citations, deadlines, case references or procedural options as errors or review gaps, not as draft quality.

---

## 16. Human Review Gates

Human Review is required for:

- deadline confirmation;
- notice completeness;
- legal basis;
- issue characterization;
- response strategy;
- amendment scope;
- Evidence sufficiency;
- response draft;
- client-facing legal explanation;
- provider instruction;
- filing readiness;
- submission authorization.

Each review should be bounded by:

- Trademark and Matter;
- official notice version;
- issue scope;
- jurisdiction;
- Evidence version;
- response draft version;
- intended downstream action;
- reviewer role;
- current time and deadline context.

Human Review does not submit the response.

After review, current state, version, Permission and Policy must be refreshed.

---

## 17. Permission and Policy

Permission may govern:

- Trademark access;
- office-action preview;
- Document access;
- Evidence access;
- Matter and Order access;
- Classification access;
- Knowledge retrieval;
- Communication preparation;
- provider data access.

Policy may:

- hide notice existence;
- redact notice content;
- hide Evidence;
- limit Knowledge sources;
- restrict cross-organization use;
- restrict AI source access;
- hide legal strategy notes;
- require Human Review;
- return NotFound under non-disclosure.

Permission does not override Policy.

Human Review does not bypass either.

---

## 18. Trace and Audit

Current preview does not emit Events.

Where a preview is retained under an owning contract, audit context should preserve:

- request actor and organization;
- Trademark and Matter references;
- official notice reference and version;
- extraction and translation versions;
- source dates;
- issue-category candidates;
- deadline-present and not-certified distinction;
- Document, Evidence and Knowledge sources;
- AI involvement;
- Policy omissions;
- required Human Review;
- current Workflow version;
- explicit no-side-effect result.

Future service-owned results may return Event references as trace.

Those references do not authorize filing.

---

## 19. Safe Failure

Controlled outcomes may include:

- validation failure;
- invalid reference;
- Permission denied;
- Policy restricted;
- Human Review required;
- unsupported version;
- invalid state;
- NotFound;
- conflict;
- apply not implemented;
- internal safe error.

Errors must not expose:

- database identifiers;
- restricted Trademark data;
- raw official notice content;
- Evidence content;
- legal strategy notes;
- restricted Knowledge;
- provider data;
- Policy internals;
- Permission internals;
- prompts;
- hidden reasoning;
- stack traces.

A safe recovery result may identify:

- missing source;
- incomplete notice;
- conflicting date;
- required professional role;
- required next question;
- whether a new preview is allowed;
- that no response was submitted.

---

## 20. Example — Cited-Mark Refusal and Formal Requirement

An official notice appears to include:

- a cited-mark refusal;
- a requirement to clarify goods;
- a stated response date;
- several cited registrations;
- one missing attachment page.

### 20.1 Source Preparation

The pattern validates the available notice reference and Trademark reference.

It records:

- original Document version;
- OCR version;
- translation status;
- missing page;
- stated date;
- issuing office;
- affected class candidates.

### 20.2 Preview

The preview:

- identifies a possible relative-ground issue;
- identifies a possible Classification requirement;
- states that the notice is incomplete;
- marks deadline present but not certified;
- lists cited-mark references as extracted;
- prepares Evidence and source gaps;
- prepares possible response-path categories;
- requires professional review;
- prepares a Task plan preview and client-question outline.

### 20.3 AI Assistance

AI may:

- summarize each issue;
- compare the mark strings;
- organize goods and services;
- list missing facts;
- prepare an argument outline;
- flag that the missing page may change analysis.

AI cannot decide that confusion is unlikely or that the refusal will be overcome.

### 20.4 MVP Stop

Apply remains disabled.

No Task, Communication, Matter update, Evidence link, Event or response filing occurs.

The result says:

```text
Preparation preview complete.
Notice completeness, deadline, legal basis, strategy and response draft require Human Review.
No official response was submitted.
```

---

## 21. Pattern Acceptance Checklist

The Office Action Response Preparation Pattern is correct when:

- [ ] current MVP depth is preview-only;
- [ ] apply remains disabled and side-effect free;
- [ ] original notice, OCR, translation, summary and interpretation remain distinct;
- [ ] Document reference validity is not treated as authenticity or completeness;
- [ ] Trademark state is not mutated from extracted notice text;
- [ ] Matter and Order scope mismatches remain visible;
- [ ] stated, extracted, calculated and professionally confirmed dates remain distinct;
- [ ] deadline presence is not deadline certification;
- [ ] issue categories remain candidates until professional review;
- [ ] affected scope preserves source and uncertainty;
- [ ] Documents, Evidence and Knowledge retain separate ownership and meaning;
- [ ] response paths remain non-final;
- [ ] success probability is not certified;
- [ ] AI output cites sources and exposes limitations;
- [ ] Human Review gates deadline, legal strategy, Evidence and response approval;
- [ ] Task plan is not active Task;
- [ ] Communication outline is not created or sent;
- [ ] no provider is selected;
- [ ] no official response is submitted;
- [ ] Workflow emits no Events;
- [ ] safe errors protect legal strategy and restricted sources.

---

## 22. Product Boundary

Book 04 may display the notice, extracted issues, source comparisons, deadline warnings, Evidence gaps and review questions. It must show that no strategy was approved and no response was submitted.

## 23. Implementation Boundary

This pattern adds no deadline-certification logic, substantive legal rules, success prediction, Evidence sufficiency rules, filing connector, provider selection, payment or autonomous legal-response agent. Apply remains disabled.

## 24. Chapter Result

The Office Action Response Preparation Pattern creates a governed professional review package without converting preparation into legal authority.

```text
Preserve the official source.
Separate extraction from interpretation.
Keep deadline presence distinct from certification.
Categorize issues without declaring final legal truth.
Prepare Documents, Evidence and Knowledge with provenance.
Offer possible response paths, not autonomous strategy.
Require Human Review.
Keep apply disabled.
Do not submit, send, select, mutate or emit.
```

The pattern succeeds when the notice, uncertainty, possible work and required professional decisions are visible before any external consequence.

The next chapter defines the **Renewal Preparation Pattern**, where eligibility, official status, deadline context, owner information, Documents, commercial scope and protected payment/submission handoffs must be prepared without certifying renewal rights or executing the renewal.
