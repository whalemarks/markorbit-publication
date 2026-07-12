# B03-CH-23 — Assignment Preparation Pattern

## Chapter Purpose

The Assignment Preparation Pattern organizes current ownership, proposed parties, affected Trademarks, transaction scope, Documents, Evidence, jurisdiction requirements and professional review without certifying legal effect, mutating owner state or filing an official recordal.

Assignment work may involve:

- full or partial transfer;
- merger or corporate succession;
- name or address change questions;
- one or many Trademarks;
- current owner and proposed new owner;
- transaction agreement;
- signatures;
- notarization, legalization or translation;
- chain-of-title material;
- authority Documents;
- jurisdiction-specific recordal;
- Matter, Order, provider and fee scope.

The pattern answers:

```text
Which Trademark records and jurisdictions are in scope?
Who is shown as current owner by each source?
Who are the proposed assignor and assignee?
What transaction type and affected scope are stated?
Which Documents and Evidence support party identity, authority and chain of title?
Which signature, notarization, legalization or translation questions remain?
What can be organized in preview?
Which conclusions require Human Review?
Why must current MVP execution stop before apply?
What remains forbidden before official recordal and verified owner update?
```

The governing path is:

```text
Assignment request or ownership-change signal
→ reference and source validation
→ party and Trademark scope preparation
→ transaction and chain-of-title context
→ Document / Evidence gap analysis
→ jurisdiction and formal-requirement review package
→ Matter / Order / provider context
→ Human Review requirement
→ safe preview
→ stop before legal certification, owner mutation or filing
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
- [Chapter 19 — Communication Review Pattern](B03-CH-19_Communication_Review_Pattern.md)
- [Chapter 20 — Provider Routing Preparation Pattern](B03-CH-20_Provider_Routing_Preparation_Pattern.md)
- [Chapter 22 — Renewal Preparation Pattern](B03-CH-22_Renewal_Preparation_Pattern.md)

Its primary Book 02 sources are:

- [Assignment Workflow](../../book-02-core-specification/core-specs/workflows/assignment-workflow.md)
- [Assignment Workflow Contract](../../book-02-core-specification/core-specs/contracts/workflows/assignment-workflow-contract.md)
- [Workflow Specifications Index](../../book-02-core-specification/core-specs/workflows/index.md)
- [Workflow Contract Index](../../book-02-core-specification/core-specs/contracts/workflows/index.md)
- [Trademark API Contract](../../book-02-core-specification/core-specs/contracts/api/trademark-api-contract.md)
- [Customer API Contract](../../book-02-core-specification/core-specs/contracts/api/customer-api-contract.md)
- [Jurisdiction API Contract](../../book-02-core-specification/core-specs/contracts/api/jurisdiction-api-contract.md)
- [Knowledge API Contract](../../book-02-core-specification/core-specs/contracts/api/knowledge-api-contract.md)
- [Matter API Contract](../../book-02-core-specification/core-specs/contracts/api/matter-api-contract.md)
- [Order API Contract](../../book-02-core-specification/core-specs/contracts/api/order-api-contract.md)
- [Document API Contract](../../book-02-core-specification/core-specs/contracts/api/document-api-contract.md)
- [Evidence API Contract](../../book-02-core-specification/core-specs/contracts/api/evidence-api-contract.md)
- [Task API Contract](../../book-02-core-specification/core-specs/contracts/api/task-api-contract.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [AI Context Contract](../../book-02-core-specification/core-specs/contracts/common/ai-context.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)

Book 02 owns the Workflow, contract, Trademark owner state, related Services, controlled values and implementation depth.

### 1.1 Current Depth Rule

The current Assignment Workflow is:

```text
Stub Now
Level 1/2
Preview / Validation Stub
Apply not production-enabled
```

The broader Workflow Contract does not enable production assignment behavior in the current MVP.

This chapter applies the stricter rule:

```text
Preview may organize assignment preparation.
Apply remains disabled with no side effects.
No owner mutation, legal-effect certification, provider instruction or official recordal occurs.
```

---

## 2. Pattern Position

The pattern may begin from:

- a customer request;
- a merger or acquisition;
- an assignment agreement;
- an ownership mismatch;
- a portfolio review;
- Renewal preparation;
- an official record;
- a prior Matter;
- a provider report;
- a proposed internal owner update.

A request or Document may signal a possible ownership change.

It does not certify:

- current ownership;
- assignor authority;
- assignee identity;
- contract validity;
- legal effect;
- effective date;
- signature validity;
- jurisdiction acceptance;
- completed recordal.

Current outputs may include:

- validated references;
- party and Trademark scope;
- transaction-type candidate;
- missing fields;
- Document and Evidence gaps;
- formal-requirement review needs;
- Matter and Order mismatch;
- Task plan preview;
- Communication outlines;
- Human Review requirement;
- safe errors.

---

## 3. Assignment Boundary

The following facts must remain separate.

| Fact | Meaning |
|---|---|
| Assignment requested | A party asks for transfer-related work |
| Agreement drafted | Proposed transaction text exists |
| Agreement signed | Signatures appear on a version |
| Contract effective | The transaction may have legal effect under applicable law |
| Rights transferred | Ownership may have changed substantively |
| Recordal authorized | A specific official filing is approved |
| Recordal submitted | Documents were sent to an office |
| Recordal received | The office acknowledged receipt |
| Recordal accepted | The office approved the change |
| Official register updated | The office record shows the new owner |
| Core owner state updated | Trademark Service records supported internal state |

No earlier fact automatically proves a later one.

### 3.1 Signature Is Not Legal Effect

A signature image or electronic signature may exist while:

- signer authority is unverified;
- required parties are missing;
- the wrong version was signed;
- execution formalities are incomplete;
- conditions precedent remain;
- governing law affects effect;
- notarization or legalization is required;
- the transaction scope is unclear.

### 3.2 Legal Effect Is Not Official Recordal

Some rights may transfer between parties before an office updates its register.

Other jurisdictions or actions may require recordal for specific effects.

The Workflow and AI do not decide that legal conclusion.

### 3.3 Official Recordal Is Not Automatic Core Mutation

Trademark Service should update owner state only from evidence and contracts it accepts.

A Workflow preview, uploaded agreement or Human Review record does not directly mutate the Trademark.

---

## 4. Trademark Scope

The preview should resolve:

- Trademark references;
- jurisdiction for each;
- registration or application numbers where visible;
- current internal owner;
- current official owner source where available;
- classes and goods/services;
- pending status;
- existing encumbrance or related transaction signals where governed;
- source versions;
- mismatches;
- Policy omissions.

### 4.1 One Transaction, Multiple Rights

An agreement may cover:

- several Trademarks;
- multiple jurisdictions;
- applications and registrations;
- related domains or other assets;
- only part of a portfolio;
- selected classes or goods/services.

The pattern must not assume that every referenced Brand or Trademark is included.

### 4.2 Full and Partial Assignment

A partial assignment may raise questions about:

- affected classes;
- affected goods/services;
- jurisdiction allowance;
- division or linked procedures;
- retained rights;
- Brand or goodwill context;
- professional review.

The pattern may identify the issue.

It must not certify that a proposed partial transfer is legally recordable.

### 4.3 Applications and Registrations

An assignment of a pending application may have different requirements from a registration.

The preview should preserve the exact right type and source status.

---

## 5. Party Preparation

The pattern should distinguish:

- current recorded owner;
- proposed assignor;
- proposed assignee;
- Customer;
- requesting contact;
- payer;
- representative;
- signatory;
- beneficial or related party where governed;
- organization acting for each party.

These roles must not collapse.

### 5.1 Name and Identity

Party preparation may include:

- legal name;
- entity type;
- country or region;
- address;
- registration identifier where permitted;
- name translations or transliterations;
- Customer reference;
- identity Documents;
- organization references;
- conflicting names;
- prior names.

AI may normalize formatting.

It must not create a legal identity or choose among conflicting entities.

### 5.2 Signatory Authority

A signatory may be:

- director;
- officer;
- authorized representative;
- attorney;
- another role.

A title in a signature block does not prove authority.

The preview may request supporting authority and Human Review.

### 5.3 Cross-Organization Policy

Assignment files may expose sensitive information about two or more parties.

Policy governs:

- visibility;
- sharing;
- internal notes;
- commercial terms;
- identity data;
- agreement content;
- provider access.

---

## 6. Transaction Context

The preview may organize:

- assignment type;
- stated effective date;
- consideration or commercial terms where allowed;
- full or partial scope;
- included rights;
- excluded rights;
- conditions;
- governing law statement;
- signature status;
- recordal jurisdictions;
- requested service;
- unresolved professional questions.

### 6.1 Type Is Not Self-Proving

Labels such as:

- full assignment;
- merger;
- name change;
- address change;
- reorganization;
- succession

may have different legal and documentary consequences.

The Workflow should not accept a label as final professional classification.

### 6.2 Effective Date

The preview may display a stated date.

It must distinguish:

- date stated in agreement;
- signature date;
- closing date;
- conditional effective date;
- professional conclusion;
- official recordal date;
- internal update date.

### 6.3 Consideration and Confidentiality

Commercial terms may be restricted.

The preview should not expose or summarize them unless Policy permits and the review needs them.

---

## 7. Chain of Title

A current owner and proposed assignor may not match.

Possible reasons include:

- prior unrecorded assignment;
- merger;
- name change;
- transliteration difference;
- office data lag;
- incorrect internal record;
- incomplete chain;
- wrong Trademark;
- unauthorized request.

The pattern should prepare a chain-of-title view containing:

- each asserted owner;
- supporting source;
- transaction date;
- affected rights;
- gaps;
- contradictions;
- review requirement.

This is a conceptual review view, not a new Core Object.

### 7.1 Missing Link

A missing link should not be papered over by AI inference.

The safe result may require:

- earlier agreement;
- merger certificate;
- name-change certificate;
- official extract;
- declaration;
- professional opinion;
- provider confirmation.

### 7.2 Official Record and Private Agreement

The office record and private agreement may support different facts.

The preview should present the mismatch rather than declare one universally controlling.

---

## 8. Document Preparation

Possible Documents include:

- assignment agreement;
- short-form assignment;
- deed;
- merger certificate;
- name-change certificate;
- corporate registry extract;
- identity Document;
- Power of Attorney;
- signatory authority;
- consent;
- recordal form;
- translation;
- notarization;
- legalization or apostille;
- provider instruction;
- official receipt.

For every Document, the preview may identify:

- reference;
- type;
- version;
- party;
- signature status;
- language;
- intended jurisdiction;
- intended use;
- content-access status;
- missing formalities;
- reviewer requirement.

Reference validity does not prove sufficiency.

### 8.1 Signed Version Integrity

The signed version must be distinguishable from:

- draft;
- redline;
- unsigned clean copy;
- translated copy;
- short form;
- notarized copy;
- filed copy.

AI comparison can identify differences.

It cannot certify which version has legal effect.

### 8.2 Notarization, Legalization and Translation

The pattern may flag that review is required.

It must not certify:

- notarial validity;
- apostille validity;
- legalization chain;
- certified translation quality;
- office acceptability.

### 8.3 Document Linkage

Linking a Document to a Trademark or Matter does not mutate ownership.

Document Service owns the link behavior. Trademark Service owns owner state.

---

## 9. Evidence Preparation

Supporting Evidence may include:

- chain-of-title material;
- corporate succession records;
- prior official owner extracts;
- proof of authority;
- transaction completion evidence;
- other jurisdiction-specific support.

Evidence Service owns Evidence behavior and use context.

A sufficiency preview or summary is assistance.

It does not prove:

- ownership;
- transaction validity;
- recordability;
- official acceptance.

---

## 10. Jurisdiction and Knowledge Context

The preview may retrieve governed Knowledge about:

- required forms;
- signature rules;
- notarization;
- legalization;
- translation;
- original or copy requirements;
- recordal timing;
- party information;
- partial assignment;
- pending applications;
- fees;
- local representation.

Knowledge sources should preserve:

- jurisdiction;
- authority;
- effective date;
- version;
- retrieval time;
- applicability;
- limitations;
- review status.

AI must not treat a generic country note as a final Matter-specific conclusion.

---

## 11. Matter, Order and Provider Context

The preview may identify:

- Assignment Matter;
- Order scope;
- number of Trademarks;
- jurisdictions;
- party count;
- Document work;
- translation or legalization work;
- provider need;
- official and service fees;
- commercial restrictions;
- payment state where allowed;
- scope mismatch.

### 11.1 Scope Mismatch

Examples include:

- one Trademark ordered but five covered;
- one jurisdiction ordered but multiple records included;
- simple recordal ordered but chain repair required;
- translation or legalization excluded;
- provider work not approved;
- an ownership change requires a separate Matter.

The preview should expose mismatch.

### 11.2 Provider Routing

The pattern may identify that local provider support is needed.

Provider selection remains governed by Chapter 20.

No provider is selected or instructed by Assignment preview.

### 11.3 Payment

The pattern does not approve or execute payment.

Fee context, payment authorization and payment result remain separate.

---

## 12. Preview Behavior

Current MVP preview may:

- validate request shape;
- validate Trademark, Document and Evidence references;
- check Permission and Policy;
- organize current and proposed parties;
- identify assignment-type candidates;
- identify affected Trademarks and scope;
- identify chain-of-title gaps;
- identify signature and authority questions;
- identify notarization, legalization and translation review needs;
- identify jurisdiction questions;
- identify Matter and Order mismatch;
- prepare readiness checklist;
- prepare Task plan preview;
- prepare client and provider Communication outlines;
- prepare AI-assisted gap summary;
- require Human Review;
- return safe warnings and errors.

Preview must not:

- mutate Trademark owner;
- certify current ownership;
- certify party authority;
- certify legal effect;
- certify effective date;
- certify signature validity;
- certify notarization, legalization or translation;
- certify recordal readiness;
- create Matter or Order;
- create Documents or Evidence;
- create active Tasks;
- create Communication;
- select or engage a provider;
- execute payment;
- file recordal;
- emit Events.

### 12.1 Preview Statement

A safe preview should state:

```text
This is an assignment-preparation preview.
Party, ownership, authority, legal effect, formalities and recordal readiness require Human Review.
No owner state changed and no official recordal was filed.
Apply is not production-enabled.
```

---

## 13. Apply Is Disabled in Current MVP

An apply request must return a controlled disabled result.

It must be:

- side-effect free;
- version-aware;
- Policy-safe;
- explicit;
- non-retryable as a currently supported production action.

It must not:

- mutate Trademark owner;
- create or update Matter or Order;
- create active Tasks;
- create Communications;
- attach Documents or Evidence;
- select or instruct a provider;
- approve or execute payment;
- emit Events;
- file official recordal;
- silently perform preview while reporting apply.

### 13.1 Future Apply

A future preparation apply would still require:

- owning-service behavior;
- supported versions;
- idempotency;
- Permission;
- Policy;
- Human Review;
- Document and Evidence Services;
- Task Service;
- Communication Review;
- Provider Routing;
- payment boundary;
- separate official filing;
- official result verification;
- Trademark Service update from supported facts.

This chapter does not enable that scope.

---

## 14. Task Plan Preview

The pattern may prepare planned Tasks such as:

- confirm affected Trademarks;
- confirm current owner;
- confirm assignor and assignee;
- verify signatory authority;
- resolve chain-of-title gap;
- collect agreement;
- collect corporate Documents;
- obtain Power of Attorney;
- review effective date;
- review partial scope;
- review notarization or legalization;
- obtain translation;
- confirm provider and fee scope;
- prepare client confirmation;
- prepare recordal instruction;
- perform readiness review.

The current stub creates no active Tasks.

Task completion would not prove legal effect, filing or official owner update.

---

## 15. Communication Preparation

The preview may prepare outlines for:

- party confirmation;
- missing Document request;
- authority question;
- chain-of-title question;
- formalities explanation;
- provider inquiry;
- provider instruction;
- internal escalation.

An outline remains non-final.

No Communication is created or sent by the current stub.

Future external messages require Communication Review and Communication Service.

---

## 16. AI-Assisted Assignment Preparation

AI may:

- compare party names;
- summarize agreements;
- compare drafts and signed versions;
- identify missing signatures;
- organize affected Trademarks;
- prepare chain-of-title chronology;
- identify Document gaps;
- retrieve governed jurisdiction Knowledge;
- prepare questions;
- prepare checklists and outlines;
- flag inconsistencies.

AI must not:

- certify ownership;
- certify assignor authority;
- certify assignee identity;
- certify legal effect;
- certify effective date;
- certify signature validity;
- certify notarization or legalization;
- certify recordal readiness;
- approve the assignment;
- select a provider;
- send instructions;
- file recordal;
- mutate Trademark owner;
- emit Events.

### 16.1 Name Similarity

AI may detect similar names.

It must not conclude that two legal entities are the same without governed evidence and review.

### 16.2 Agreement Summary

A summary helps navigation.

It does not replace review of the exact signed Document and governing law.

---

## 17. Human Review Gates

Human Review is required for:

- current ownership;
- assignor and assignee identity;
- signatory authority;
- transaction type;
- affected rights;
- chain of title;
- legal effect;
- effective date;
- Document sufficiency;
- signature validity;
- notarization, legalization and translation;
- recordal readiness;
- provider instruction;
- payment authorization where applicable;
- official filing authorization.

Review must be bound to:

- exact Trademark set;
- parties;
- jurisdiction;
- transaction scope;
- exact Document versions;
- Evidence;
- intended downstream action;
- reviewer role;
- current time.

Human Review does not mutate owner state or file recordal.

---

## 18. Permission and Policy

Permission may govern:

- Trademark access;
- assignment preview;
- owner and party data;
- Document and Evidence access;
- Matter and Order access;
- commercial terms;
- provider context;
- Communication preparation.

Policy may:

- hide owner or party identity;
- redact agreement content;
- hide consideration;
- restrict cross-organization sharing;
- limit provider visibility;
- restrict AI source use;
- require Human Review;
- downgrade output;
- return NotFound.

Permission does not override Policy.

Human Review does not bypass either.

---

## 19. Trace and Audit

Current preview emits no Events.

Where retained under an owning contract, audit context should preserve:

- actor and organization;
- Trademark references;
- current owner sources;
- proposed parties;
- assignment-type candidate;
- affected scope;
- transaction and Document versions;
- chain-of-title gaps;
- formal-requirement questions;
- Evidence and Knowledge sources;
- AI involvement;
- Policy omissions;
- required Human Review;
- Workflow version;
- explicit no-side-effect result.

Future Event references remain trace.

They do not prove legal effect or authorize owner mutation.

---

## 20. Safe Failure

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
- restricted owner or party data;
- agreement content;
- consideration;
- identity Documents;
- private chain-of-title notes;
- provider terms;
- Policy internals;
- Permission internals;
- prompts;
- hidden reasoning;
- stack traces.

A safe recovery result may identify:

- missing party field;
- owner mismatch;
- chain gap;
- wrong Document version;
- missing signature or authority source;
- required professional role;
- safe next question;
- that no owner state changed and no recordal occurred.

---

## 21. Example — Portfolio Assignment With an Unrecorded Prior Transfer

A request covers four Trademarks in two jurisdictions.

The supplied sources show:

- office records naming Company A;
- current customer named Company B;
- proposed assignee Company C;
- an agreement from B to C;
- a prior unsigned document suggesting A transferred to B;
- different signatories across versions;
- one jurisdiction requiring formalities review;
- an Order covering only two Trademarks.

### 21.1 Preview

The pattern:

- validates visible Trademark and Document references;
- separates official owner, asserted current owner and proposed parties;
- identifies the A-to-B chain gap;
- identifies the unsigned prior Document;
- identifies inconsistent signatories;
- flags formalities review;
- exposes Order scope mismatch;
- prepares Document, Evidence and Knowledge gaps;
- prepares Task and Communication outlines;
- requires Human Review.

### 21.2 AI Assistance

AI may:

- build a chronology;
- compare party names;
- identify missing signatures;
- list affected rights;
- prepare questions.

It cannot certify that B owns the Trademarks or that the B-to-C assignment is effective.

### 21.3 MVP Stop

Apply remains disabled.

No owner mutation, Matter, Order update, Task, Communication, provider instruction, payment, Event or official recordal occurs.

The result says:

```text
Assignment preparation preview complete.
Ownership, chain of title, authority, scope and formalities require professional review.
No owner state changed and no recordal was filed.
```

---

## 22. Pattern Acceptance Checklist

The Assignment Preparation Pattern is correct when:

- [ ] current MVP remains preview-only;
- [ ] apply remains disabled and side-effect free;
- [ ] request, signature, legal effect, rights transfer, recordal and owner update remain distinct;
- [ ] Trademark scope is exact;
- [ ] full and partial assignment questions remain review-gated;
- [ ] current owner, assignor, assignee, Customer, contact, payer and signatory remain distinct;
- [ ] name similarity is not identity proof;
- [ ] signatory title is not authority proof;
- [ ] transaction type and effective date are not autonomously certified;
- [ ] chain-of-title gaps remain explicit;
- [ ] signed and draft Document versions remain distinct;
- [ ] notarization, legalization and translation remain professional questions;
- [ ] Document linkage does not mutate ownership;
- [ ] Evidence summary is not sufficiency;
- [ ] Matter, Order, provider and payment boundaries remain visible;
- [ ] Task plan is not active Task;
- [ ] Communication outlines are not sent;
- [ ] AI output remains non-final;
- [ ] Human Review gates every professional conclusion;
- [ ] no provider is selected or engaged;
- [ ] no payment is executed;
- [ ] no official recordal is filed;
- [ ] no owner state is mutated;
- [ ] Workflow emits no Events.

---

## 23. Product Boundary

Book 04 may present affected Trademarks, parties, chain of title, Documents, signature gaps and review needs. It must show that package preparation is not legal transfer or official recordal.

## 24. Implementation Boundary

This pattern adds no ownership-law engine, signature certification, chain-of-title certification, owner mutation, payment, provider selection, filing connector or autonomous assignment agent. Apply remains disabled.

## 25. Chapter Result

The Assignment Preparation Pattern builds a governed ownership-change review package without creating ownership truth.

```text
Resolve the exact rights.
Separate current owner, assignor, assignee and signatory.
Preserve transaction and Document versions.
Expose chain-of-title gaps.
Treat signatures and formalities as review questions.
Organize Evidence and Knowledge without certifying sufficiency.
Require Human Review.
Keep apply disabled.
Do not mutate, pay, send, file or emit.
```

The pattern succeeds when every party, right, source, gap and required professional decision is visible before any official or internal ownership change.

The next chapter defines the **Evidence Review Preparation Pattern**, the final pattern in Part III, where source Documents, Evidence identity, target propositions, time and jurisdiction context, completeness and sufficiency assistance must remain distinct from professional evidentiary conclusions.
