# Chapter 19 — Evidence and Audit Must Reconstruct Every Consequential Decision

A trustworthy professional system should be able to answer a basic question months or years later:

> Why did this action happen, based on which facts, versions, approvals and authority?

Most case systems can show that a file exists or that a status changed. Fewer can reconstruct the decision that produced the change.

MarkReg should preserve enough evidence to explain:

- what was known;
- what remained Unknown;
- which source controlled;
- what the customer decided;
- what the professional concluded;
- what Package was approved;
- who acted;
- what external evidence returned;
- how the Product updated its projection;
- what later correction or supersession occurred.

```text
Source
→ extracted or supplied fact
→ reviewed context
→ recommendation or Package
→ Decision and approval
→ authorized action
→ external evidence
→ validated Outcome
→ continuing record
```

## 1. Evidence is not the same as a file

A file may be:

- a customer upload;
- an official notice;
- a Provider attachment;
- an unsigned draft;
- an email export;
- a screenshot;
- an internally generated report;
- an AI-produced document;
- a certificate copy;
- a payment receipt.

Its presence does not establish what it proves.

```text
File Exists
≠ Evidence Accepted
≠ Fact Verified
≠ Decision Authorized
```

An Evidence record should preserve:

- evidence type;
- source and custodian;
- acquisition channel;
- creation and receipt dates;
- jurisdiction and related right;
- file or record version;
- integrity and legibility state;
- language and translation state;
- confidentiality and permitted use;
- what claim or decision it may support;
- reviewer and acceptance state;
- conflict or supersession;
- retention and deletion conditions.

## 2. Evidence, source fact, interpretation and decision are separate

Consider a Provider email stating:

> The application has been filed successfully.

The system should distinguish:

```text
Provider Email
= received evidence

Provider Statement
= externally reported fact candidate

Professional or Owning Service Validation
= interpretation of evidential sufficiency

Official Receipt or Register Entry
= stronger external evidence where available

Formal Filing State
= state controlled by the applicable Owning Service
```

The Provider email may justify follow-up. It may not justify a final official-status claim.

## 3. Evidence should be purpose-scoped

The same material may be sufficient for one purpose and insufficient for another.

A screenshot may support:

- a preliminary website-use review;
- a customer clarification request;
- a historical content record.

It may not be sufficient for:

- a formal use declaration;
- ownership verification;
- a transaction warranty;
- official filing evidence.

```text
Evidence accepted for triage
≠ evidence accepted for filing
≠ evidence accepted for legal conclusion
```

The acceptance purpose should be explicit.

## 4. Evidence quality has several dimensions

Evidence should not be compressed into one confidence score.

Relevant dimensions include:

- source authority;
- authenticity indicators;
- completeness;
- legibility;
- temporal relevance;
- jurisdictional relevance;
- identity match;
- mark-version match;
- goods or service match;
- chain of custody;
- translation quality;
- contradiction with other sources;
- professional sufficiency for the intended purpose.

A high-quality scan of the wrong document remains the wrong evidence.

## 5. Consequential decisions need a Decision Record

A consequential Decision may include:

- applicant selection;
- filing route;
- goods deletion;
- priority claim;
- acceptance of search risk;
- evidence inclusion;
- OA response strategy;
- non-renewal;
- restoration or re-filing;
- transaction scope;
- Provider replacement;
- public content publication;
- fee or route amendment.

The Decision Record should identify:

- decision type;
- related Customer, Order, Matter, Work Package or public content object;
- exact source and Package versions;
- presented options;
- stated assumptions and Unknowns;
- material risks and consequences;
- deciding actor and represented authority;
- professional recommendation where applicable;
- timestamp and validity period;
- conditions that invalidate or reopen the Decision.

```text
Customer clicked Approve
≠ decision reconstructable
```

The system should retain what the customer actually saw.

## 6. Approval evidence must bind the exact version

Approval should preserve:

- approver identity;
- represented Organization;
- authority basis;
- approved object and version;
- material diff from prior version;
- costs and currency where relevant;
- expiry or invalidation conditions;
- channel and original response;
- any stated limitation.

If a Package changes materially, the prior approval should not remain silently active.

```text
Approval of Package v2
≠ Approval of Package v3
```

## 7. External actions require an evidence contract

Before a Provider, connector or professional performs an external action, MarkReg should define what evidence must return.

Examples include:

- Provider acknowledgement;
- Provider acceptance;
- submitted Package reference;
- technical delivery log;
- filing receipt;
- official application number;
- fee receipt;
- courier tracking;
- office notice;
- updated official record;
- certificate;
- signed transaction document;
- recordal acknowledgement.

The Evidence Contract should state:

- required artifact or event;
- expected source;
- required fields;
- time expectation;
- validation owner;
- follow-up and escalation;
- what state may change after validation.

```text
Provider Says “Done”
≠ Evidence Contract Satisfied
```

## 8. Audit must reconstruct the full chain

A useful audit should be able to trace:

```text
Customer objective
→ recommendation basis
→ accepted scope
→ formal Intake
→ source and Requirement Set
→ Work Packages and Assignments
→ Contributions and Reviews
→ customer and professional Decisions
→ approved Package
→ Provider or connector action
→ returned evidence
→ official validation
→ customer delivery
→ future obligation
```

The audit should not require reading hundreds of unrelated email messages in chronological order.

## 9. Audit views should follow the question

Different users need different audit views.

### Customer-facing evidence view

Shows:

- what was completed;
- official references;
- material approvals;
- paid or outstanding fees;
- delivered documents;
- unresolved risks;
- next obligations.

### Delivery audit view

Shows:

- Work Package chain;
- Assignment and review;
- source versions;
- Provider Returns;
- exception and recovery history;
- responsibility.

### Professional audit view

Shows:

- legal or procedural issues;
- source hierarchy;
- professional recommendation;
- evidence choices;
- exact approvals;
- protected-action authority.

### Commercial audit view

Shows:

- Quote and Order scope;
- amendments;
- payment states;
- Provider and contributor costs;
- refund or remediation decisions.

### Content and conversion audit view

Shows:

- public claim source;
- factual reviewer;
- page and CTA version;
- recommendation logic;
- user consent and conversion events;
- correction propagation.

One audit model can support several projections without exposing unnecessary private data.

## 10. Official evidence and official truth remain distinct

An official-looking PDF may still be:

- incomplete;
- superseded;
- incorrectly associated;
- a copy without current status;
- inconsistent with the register;
- missing a page;
- issued before a later correction.

```text
Official Document
≠ Current Official State in Every Context
```

The Owning Service should validate the official event and preserve the source and retrieval time.

## 11. Corrected evidence must not erase history

Suppose an office issues a corrected receipt or certificate.

The system should preserve:

```text
Original Evidence
→ conflict or correction event
→ Corrected Evidence
→ impact analysis
→ affected Decisions and projections
→ customer or Provider correction
```

Historical evidence may remain relevant to explain earlier decisions. It should be marked superseded rather than silently overwritten.

## 12. Unknown is auditable

An audit should show not only what was known but also what remained unresolved at the decision time.

Examples:

- no official receipt available;
- Provider advice conflicted with an official page;
- applicant authority not yet confirmed;
- certificate original location unknown;
- payment deducted but not reconciled;
- recordal filed but office update pending;
- public content source stale.

```text
Unknown at time of decision
≠ evidence missing from audit
```

The Unknown itself should be recorded with owner, impact and next verification action.

## 13. AI provenance must be visible

AI may:

- extract fields;
- classify documents;
- compare versions;
- summarize communications;
- identify contradictions;
- generate a candidate claim;
- draft a Decision explanation;
- assemble an audit package.

The record should preserve:

- model or service where material;
- prompt or task context where appropriate;
- source objects supplied;
- output version;
- human verification;
- correction history;
- prohibited data boundary.

```text
AI-generated Summary
≠ Source Evidence
```

The audit should point back to the original evidence.

## 14. Content and SEO claims require evidence lineage

The Growth & Conversion Layer adds public claims such as:

- official fees;
- processing times;
- document requirements;
- POA formalities;
- maintenance deadlines;
- recovery options;
- service availability;
- professional or Provider coverage.

Each material claim should retain:

- jurisdiction;
- source;
- effective or retrieval date;
- claim type;
- reviewer;
- page and component versions;
- expiry or refresh rule;
- known exception;
- correction history.

```text
Published Page
≠ Permanent Truth
```

When a fee or rule changes, MarkReg should identify affected pages, snippets, answer blocks, conversion calculators and Quotes.

## 15. Conversion events also need provenance

A conversion journey may contain:

```text
Page viewed
→ question answered
→ intent inferred
→ route recommended
→ fee range displayed
→ user selected option
→ Intake started
→ quotation requested
→ Customer Instruction candidate
```

The Product should preserve:

- page and content version;
- questions and answers;
- inferred versus confirmed fields;
- recommendation version;
- displayed assumptions;
- consent and contact route;
- transition into formal commercial state.

```text
Conversion Event
≠ Customer Instruction
```

## 16. Evidence retention must be governed

Not all evidence should be kept forever or exposed to every participant.

Retention should consider:

- customer contract;
- professional duty;
- official and limitation periods;
- tax and financial requirements;
- dispute and audit needs;
- privacy and deletion rights;
- confidentiality;
- litigation hold;
- cross-border transfer limits;
- training and learning permissions.

A deletion request may require:

- deletion;
- restricted archival retention;
- de-identification;
- retention of a minimal audit reference;
- legal or professional review.

## 17. Evidence access should be purpose-limited

A contributor may need one document but not the full customer file.

A Provider may need the final instruction Package but not internal pricing.

A customer may need official receipts but not another contributor's private quality record.

An auditor may need integrity evidence without access to unrelated customer content.

```text
Auditability
≠ universal access
```

## 18. Integrity does not require speculative technology

Evidence integrity may be supported by:

- stable identifiers;
- hashes;
- timestamps;
- version history;
- access logs;
- signed or authenticated sources;
- append-only event records;
- source snapshots;
- reconciliation rules.

The Product should not imply that a blockchain, cryptographic hash or timestamp proves the legal truth of the content. These mechanisms may show that bytes did not change; they do not prove ownership, authority or legal sufficiency.

## 19. Evidence gaps should trigger recovery, not cosmetic completion

Examples:

- filing marked complete without receipt;
- customer approval missing;
- Provider invoice lacks fee breakdown;
- certificate file cannot be tied to the right;
- goods deletion has no Decision record;
- public fee claim has no current source;
- AI summary cannot be traced to original communication.

The correct response may be:

```text
Block completion
Request missing evidence
Reconcile external source
Create limitation
Escalate for professional review
Correct customer or public projection
```

## 20. Product implications

MarkReg requires:

- typed Evidence records;
- source and custody metadata;
- purpose-scoped acceptance;
- Decision and approval records;
- exact-version linkage;
- Evidence Contracts for external work;
- audit projections;
- corrected and superseded evidence handling;
- Unknown records;
- AI provenance;
- public-claim lineage;
- conversion-event provenance;
- retention and purpose-limited access;
- evidence-gap recovery.

## 21. Commercial implications

Evidence discipline supports:

- premium professional delivery;
- white-label trust;
- lower dispute and refund cost;
- transaction due diligence;
- audit and compliance services;
- customer retention;
- defensible Provider management;
- reliable content and conversion operations.

Evidence collection and retention costs should be reflected in the service model rather than treated as free administrative residue.

## 22. Operating principle

```text
Source before claim
Purpose before acceptance
Version before approval
Evidence before formal state
Correction without erasure
Audit without universal access
Provenance before learning
```

> MarkReg should not merely remember that something happened. It should preserve enough evidence to explain why it happened, who was authorized, and whether the claimed result was actually achieved.