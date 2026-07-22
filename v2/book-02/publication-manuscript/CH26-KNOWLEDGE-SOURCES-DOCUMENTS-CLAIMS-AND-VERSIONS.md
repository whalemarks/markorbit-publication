# CH26 — Knowledge Sources, Documents, Claims and Versions

## Knowledge is not a pile of files

A professional platform cannot treat every PDF, webpage, email, note and AI summary as equivalent knowledge.

The same subject may be represented by:

- an official rule;
- an office notice;
- a provider email;
- a customer document;
- an internal procedure;
- a publication chapter;
- an AI-generated explanation;
- a stale copied page.

The platform needs a structure that preserves what the source is, what document was captured, what proposition is being asserted, what version applies and how the proposition is cited and reviewed.

Book 02 therefore distinguishes:

```text
Knowledge Source
≠ Knowledge Document
≠ Knowledge Claim
≠ Knowledge Version
≠ Citation
≠ Knowledge Link
≠ Formal Business State
```

The central rule is:

```text
Knowledge organizes sourced meaning.
It does not manufacture authority by storage alone.
```

## Knowledge Source identifies the origin

A Knowledge Source answers:

> From what institution, actor, system or publication did this information originate?

A source record may preserve:

- source identity;
- source class;
- publisher or responsible actor;
- jurisdiction;
- official or unofficial status;
- access location;
- publication and effective dates;
- retrieval date;
- rights and permitted use;
- reliability limitations;
- supersession or withdrawal status.

Useful source classes include:

```text
Official Source
Authoritative Professional Source
Provider-reported Practice
Customer-provided Fact
Internal Verified Knowledge
Public Observation
Inference
Unknown
```

These classes must not be blended into one authoritative voice.

```text
provider says it is required
≠ official rule says it is required
```

A provider report may be operationally important while remaining a statement of practice rather than a statement of law.

## Knowledge Document preserves a captured representation

A Knowledge Document is a governed representation obtained from a Source.

It may be:

- a PDF;
- a webpage snapshot;
- an email;
- a circular;
- a legal text;
- a form or instruction;
- a signed document;
- a Markdown note;
- a structured extract;
- a transcript.

The Document should preserve:

- source reference;
- title and document type;
- original artifact or stable location;
- content hash;
- language;
- jurisdiction;
- publication, effective and retrieval dates;
- extraction or conversion method;
- rights and confidentiality;
- review state;
- supersession history.

```text
Document stored
≠ Document understood
≠ Claim accepted
```

A file may be authentic but obsolete. A current document may be inapplicable to the present jurisdiction. A valid email may report only one provider's internal policy.

## Markdown is a representation, not semantic authority

Markdown is useful because it is readable, diffable, linkable and portable. It can represent structured front matter, claims, citations and relationships.

It is not the source of truth merely because the Knowledge system stores it.

```text
Markdown note
≠ official source
≠ accepted Claim
≠ formal business record
```

A Knowledge staging system may transform crawled or uploaded material into Markdown. The transformation must preserve the source artifact, extraction path, version and review state.

The note can become a durable working representation without replacing the authority of the underlying source.

## Knowledge Claim is an atomic proposition

A Knowledge Claim answers:

> What specific proposition is being asserted, for which jurisdiction, period and purpose?

Examples include:

- an original power of attorney is required;
- a filing fee is a stated amount;
- a deadline is calculated from a particular event;
- multiple-class applications are permitted;
- a provider currently accepts a scanned document before the original arrives;
- a Product workflow requires a defined review step.

A Claim should preserve:

- statement;
- subject;
- jurisdiction and scope;
- effective period;
- source and document references;
- claimant or derivation method;
- supporting and conflicting evidence;
- epistemic status;
- review state;
- limitations;
- supersession and correction.

```text
sentence appears in a Document
≠ Knowledge Claim accepted
```

The Claim is the unit that can be compared, reviewed, contradicted, cited and reused.

## Claims may have different authority for different purposes

A customer statement may be accepted for initial intake but not for official identity validation. A provider practice may be suitable for route planning but not for public legal publication. An old official notice may explain historical action while being unsuitable for a current filing.

```text
accepted for one purpose
≠ accepted for every purpose
```

A Claim should therefore record not only whether it is reviewed, but what purpose and authority the review covers.

## Knowledge Version preserves temporal meaning

Knowledge changes because sources change, interpretations improve and errors are corrected.

A Knowledge Version should preserve:

- version identifier;
- effective time;
- source set;
- included Claims;
- changed Claims;
- review and approval state;
- reason for change;
- compatibility notes;
- superseded version;
- withdrawal or correction state.

```text
Version 2 published
≠ Version 1 never applied
```

Historical Decisions must remain linked to the version they used. A later correction may require impact review, but it should not silently rewrite the evidence available at the earlier time.

## Citation connects use to support

Citation answers:

> Which part of which Source or Document supports this Claim or statement?

A useful Citation may include:

- source and document version;
- page, section, paragraph or anchor;
- quoted or summarized passage reference;
- retrieval time;
- jurisdiction and effective date;
- citation purpose;
- reviewer or validation state.

```text
Source listed in bibliography
≠ specific Claim supported
```

The platform should be able to reconstruct why a fee, deadline, requirement or recommendation appeared in a customer-facing output.

## Knowledge Link represents relationships without asserting identity

Knowledge objects may be related through links such as:

```text
supports
contradicts
supersedes
clarifies
implements
interprets
applies to
exception to
derived from
translated from
```

A link should preserve actor, time, purpose and confidence where relevant.

```text
linked
≠ identical
≠ universally applicable
```

A local provider note can be linked as an interpretation or practice related to an official rule without being merged into the official source.

## Conflict is a first-class knowledge condition

Knowledge systems must allow conflicting Claims to coexist.

For example:

```text
Official Guidance:
scanned POA accepted at filing

Provider Practice:
original POA required before filing

Prior Matter Evidence:
application filed before original arrived
```

The correct response is not to select one sentence and erase the rest. The system should preserve:

- source authority;
- dates;
- jurisdiction;
- provider identity;
- matter context;
- possible interpretations;
- unresolved questions;
- required professional review.

```text
conflict detected
≠ one source automatically false
```

The conflict may reveal a change in practice, a provider policy, an exception or an error.

## Freshness must remain explicit

Knowledge about fees, procedures, forms, digital portals, provider requirements and official practice becomes stale.

Claims should support states such as:

```text
Current
Recheck Due
Stale
Conflicted
Superseded
Withdrawn
Unknown
```

A freshness policy may consider:

- source type;
- publication date;
- jurisdiction;
- known change frequency;
- last verification;
- materiality;
- next use.

```text
not marked stale
≠ current
```

High-impact customer advice may require a fresh source check even when the stored Claim has not reached a routine expiry date.

## Derived knowledge requires transparent transformation

A Knowledge Claim may be derived through:

- translation;
- summarization;
- classification;
- calculation;
- comparison;
- synthesis;
- professional interpretation;
- AI inference.

The derivation should preserve:

- input Claims and versions;
- method;
- tool, model or professional actor;
- assumptions;
- uncertainty;
- output Claim;
- review state.

```text
derived correctly
≠ source inputs correct
≠ professional conclusion authorized
```

An AI summary can improve usability without replacing the original language or professional interpretation.

## Knowledge Candidate precedes reusable Knowledge

Raw extracted statements and AI-proposed Claims should enter a Candidate state.

A possible route is:

```text
Source Acquired
→ Document Preserved
→ Claim Candidate Extracted
→ Source and Scope Validation
→ Review
→ Accepted Knowledge Version
```

Candidates may be rejected, merged, split, qualified or left Unknown.

```text
AI extracted Claim
≠ reusable verified Knowledge
```

The applicable review depth depends on intended use. Internal research notes and public professional guidance should not share the same acceptance threshold.

## Knowledge rights are not implied by access

Knowledge objects may contain:

- copyrighted publications;
- confidential customer material;
- provider know-how;
- licensed databases;
- internal procedures;
- personal data;
- professional work product.

The Knowledge contract should preserve:

- permitted users;
- permitted Products and Workplaces;
- purpose;
- retention;
- reproduction and quotation rights;
- external disclosure;
- cross-border handling;
- AI training permission;
- withdrawal and deletion requirements.

```text
available for retrieval
≠ authorized for publication
≠ authorized for training
```

Operational access for one Matter does not automatically authorize inclusion in a shared Knowledge base.

## Customer and Matter knowledge need separate governance

A customer-specific fact, preference or prior decision may improve continuity. It should not silently become universal knowledge.

```text
Matter Context
≠ Workplace Knowledge
≠ Shared Knowledge
≠ Model-training Data
```

Promotion from Matter context to reusable Knowledge may require:

- purpose review;
- confidentiality review;
- de-identification;
- rights review;
- professional validation;
- removal of customer-specific facts;
- approval.

Pattern reuse is possible without copying customer content.

## Knowledge ownership and semantic authority

The Knowledge service owns the lifecycle of Knowledge Sources, Documents, Claims, Versions, Citations and Links within its declared scope.

Core defines the stable references needed for interoperability. Core does not store every document or decide every professional Claim.

```text
Core reference
≠ Knowledge repository ownership
```

The source institution remains authoritative for its own official publication. The qualified professional remains responsible for reserved interpretation. The Owning Service remains responsible for formal business state.

## Cross-book use

### Book 03 — Execution

Execution may request Knowledge, attach Claims to Work Packages, require source review and include Citations in Contributions. It cannot treat retrieval as approval or mutate formal state because a Claim was found.

### Book 05 — MarkReg

MarkReg may use jurisdictional requirements, fee Claims, deadline rules and provider practices to prepare routes and customer decisions. Matter-specific formal state remains with its Owning Service.

### Book 06 — Lite

Lite may use Knowledge to generate source-backed content, service pages and opportunity explanations. Public publication requires its own review, approval, freshness and correction policy.

### Brain

Brain retrieves and reasons over Knowledge objects. Brain results remain typed and non-canonical unless separately reviewed and accepted.

## Candidate status

The reconciliation classifies Knowledge Source, Document, Claim and Version as existing or candidate shared knowledge contracts depending on the frozen baseline.

This chapter explains the semantic structure. It does not activate missing Core objects, make Markdown canonical or centralize every document in Core.

## Constitutional rule

```text
Source identifies origin.
Document preserves representation.
Claim states a proposition.
Version preserves change over time.
Citation connects use to support.
Review determines purpose-specific acceptance.

Knowledge makes meaning traceable.
It does not convert storage, confidence or repetition
into legal, professional or formal-state authority.
```
