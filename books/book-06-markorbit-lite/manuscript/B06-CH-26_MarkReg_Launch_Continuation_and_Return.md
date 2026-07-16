# B06-CH-26 — MarkReg Launch, Continuation and Return

**Status:** Complete Draft 1  
**Chapter Map:** B06-TOC-V0.1 — Owner Accepted  
**Part:** Part VI — MarkOrbit Gateways and Continuity  
**Primary controls:** ML-H02, ML-H03, ML-HC-01

## Chapter Purpose

This chapter explains how Lite hands a qualified trademark-service need to MarkReg without duplicating MarkReg's lifecycle, and how MarkReg results return to Lite without becoming Lite-owned formal truth.

The central proposition is:

> Lite prepares continuity; MarkReg owns the formal trademark Product lifecycle.

The gateway succeeds when the user does not need to reconstruct the entire situation, while MarkReg still performs its own validation and creates its own controlled records.

## 1. Why Lite needs a MarkReg gateway

Lite may discover customer value before a formal trademark Product journey exists.

Examples include:

- a customer portfolio contains a possible filing gap;
- a historical customer confirms a new jurisdiction need;
- a prospect responds with a concrete trademark request;
- a returned status creates a maintenance or dispute question;
- a work product helps the customer select an option;
- the user identifies that a qualified need now requires formal intake.

At that point, Lite has useful context, but it does not have authority to turn the context into:

- Formal Intake;
- a Product Session;
- a Matter;
- a filing instruction;
- an applicant record of authority;
- an approved professional action;
- an official submission.

Those belong to MarkReg and the relevant Owning Services.

Without a gateway, the user must manually repeat:

- who the customer is;
- what trademark is involved;
- what need was identified;
- what the customer said;
- which option was selected;
- which Artifact Version was reviewed;
- which facts remain missing;
- what authority is available;
- what deadline or urgency is suspected.

That repetition creates friction and error.

The goal is therefore not to merge Lite and MarkReg.

The goal is:

```text
qualified Lite context
→ typed MarkReg Handoff
→ MarkReg revalidation
→ formal MarkReg state
→ typed Return
→ Lite continuity
```

## 2. `ML-H03` is a request, not a lifecycle state

`ML-H03 MarkReg Handoff` is a Product-local transfer record.

It says:

> Lite has prepared a bounded package that may justify launching or continuing a MarkReg journey.

It does not say:

- MarkReg has accepted the request;
- Formal Intake is complete;
- a Matter has been created;
- the customer has instructed filing;
- the applicant and authority context is valid;
- a deadline has been confirmed;
- any external action is authorized.

The distinction is fundamental:

```text
MarkReg Handoff prepared
≠ MarkReg Handoff accepted
≠ Product Session created
≠ Formal Intake complete
≠ Matter active
≠ official action authorized
```

Lite may show the Handoff in Today as:

- ready for confirmation;
- sent to MarkReg;
- more information required;
- rejected;
- blocked;
- accepted with a Product Session reference;
- returned with a lifecycle result.

It must not invent the destination state.

## 3. The minimum MarkReg package

`ML-HC-01` defines the minimum package for a MarkReg Handoff.

A practical package should contain only the context necessary for MarkReg to decide what to do next.

### 3.1 Origin and responsibility

- Lite Session and Organization;
- initiating user;
- responsible user or proposed owner;
- source Candidate or Qualification Result;
- purpose of the Handoff;
- requested consequence;
- return address and expected Return class.

### 3.2 Customer and applicant context

- Customer reference, when one exists;
- Contact reference and communication context;
- proposed applicant or rights-holder information;
- whether the applicant identity is confirmed, proposed or missing;
- relationship owner;
- known authorization or instruction source;
- unresolved identity, authority or conflict questions.

A Customer and an applicant may be related but are not necessarily the same legal person.

```text
customer relationship
≠ applicant identity
≠ authority to instruct
```

### 3.3 Trademark context

- mark text or representation;
- trademark reference, if one already exists;
- relevant jurisdictions;
- classes or goods/services information, if known;
- current known status;
- source and freshness of each material status;
- related applications or registrations;
- selected Artifact Version or customer explanation.

Lite must label proposed, inferred and confirmed information separately.

### 3.4 Need and selected direction

- the service need as currently understood;
- why the need is relevant now;
- customer response supporting qualification;
- options discussed;
- option selected, if any;
- business objective;
- timing or urgency;
- professional risks already identified;
- rejected or deferred alternatives.

The Handoff must not compress a nuanced customer choice into a false instruction.

```text
customer asked for information
≠ customer selected an option

customer selected an option
≠ customer authorized filing
```

### 3.5 Sources, versions and missing information

- source references;
- source timestamps;
- exact Artifact Version;
- exact communication or response reference;
- corrections already known;
- missing information;
- uncertainties;
- expired or stale elements;
- data classification and disclosure scope.

### 3.6 Authority and review context

- Human Review status;
- user confirmation status;
- known authority documents or references;
- applicant-signatory questions;
- payment or commercial status, when relevant;
- protected-action requirements;
- limits on what MarkReg may assume from the package.

The package should make absence visible.

A blank field must not look like a confirmed negative.

## 4. Launch and continuation are different

A MarkReg Handoff may request either:

1. launch of a new Product journey; or
2. continuation of an existing Product journey.

### 4.1 Launch request

A launch request applies when no appropriate active MarkReg Product Session exists.

The Handoff may ask MarkReg to:

- create or propose a Product Session;
- begin Formal Intake;
- determine the correct service module;
- request missing applicant or trademark information;
- identify that the need is unsupported or outside scope.

A launch request should include duplicate-detection context.

Lite should not create a second journey simply because the user reached MarkReg through a different Today item.

### 4.2 Continuation request

A continuation request applies when a MarkReg Product Session or relevant formal reference already exists.

Examples:

- the customer supplied missing information;
- the user selected a returned option;
- a new Artifact Version has been reviewed;
- the customer changed an instruction;
- a returned result creates a new action;
- a local/private document is now authorized for transfer.

A continuation package must reference:

- the existing Product Session or formal record;
- the earlier Handoff or Return;
- what changed;
- the new source or version;
- whether previous approval remains valid;
- the exact continuation requested.

```text
new information
≠ silent mutation of prior intake
```

## 5. MarkReg must revalidate the package

Continuity reduces repetition but does not remove destination responsibility.

MarkReg must revalidate at least:

- customer and applicant identity;
- authority to instruct;
- duplicate Product Sessions or Matters;
- trademark identity;
- jurisdiction and procedure;
- classes and goods/services;
- legal and procedural timing;
- source freshness;
- document and Evidence sufficiency;
- professional Review requirements;
- commercial instruction and payment conditions;
- External Protected Action controls.

MarkReg may accept some fields and reject others.

For example:

```text
customer reference: accepted
trademark representation: accepted
applicant identity: more information required
filing urgency: unverified
selected goods/services: review required
```

The destination must not treat Lite confidence as MarkReg verification.

```text
Lite qualification
≠ MarkReg validation
```

## 6. Possible destination responses

The MarkReg gateway must preserve typed responses.

### 6.1 Accepted with formal reference

MarkReg may return:

- Product Session reference;
- Formal Intake reference;
- requested service-module reference;
- existing Matter or related record reference;
- accepted continuation reference.

The Return should identify what was accepted and what remains open.

### 6.2 More information required

MarkReg may request:

- applicant identity;
- ownership information;
- authority or signed documents;
- mark representation;
- goods/services;
- jurisdiction choice;
- client instruction;
- fee acceptance;
- deadline evidence;
- conflict clarification;
- translation or legalization requirements.

Lite should turn the request into an understandable continuation item, not invent the missing answer.

### 6.3 Rejected

A Handoff may be rejected because:

- the need is not qualified;
- the request duplicates an existing journey;
- the service is outside MarkReg scope;
- required authority is absent;
- the user or Organization lacks access;
- the request conflicts with policy;
- the package is stale or internally inconsistent.

Rejection is a meaningful result and should preserve the reason.

### 6.4 Blocked or failed

A request may be blocked by:

- permissions;
- conflict controls;
- policy;
- missing Review;
- protected-action requirements;
- unavailable destination service.

A technical failure must remain distinct from a professional or policy rejection.

### 6.5 Unknown

If Lite cannot confirm whether MarkReg received or processed the request, the state is:

```text
unknown_external_outcome
```

The Product must not assume acceptance or submit the same Handoff again without checking for duplicate consequences.

## 7. Return is a projection, not copied ownership

`ML-H02 Return Envelope Presentation` allows Lite to show the user what MarkReg returned.

A Return may contain:

- destination;
- source Handoff;
- destination reference;
- destination status;
- result class;
- requested next action;
- missing information;
- responsible participant;
- source time and freshness;
- links to the formal Product surface.

Lite may present:

```text
MarkReg accepted the request
Product Session MR-...
Applicant information still required
Next action: review and supply applicant details
```

Lite must not create its own parallel Product Session or Matter state.

```text
Return presentation
≠ duplicated destination record
```

The destination remains the status authority.

If MarkReg later changes the status, Lite must refresh or mark the projection stale.

## 8. Return into Today

A Return becomes useful when it enters the user's daily operating model.

Today may show:

- MarkReg needs more information;
- a Product Session has been created;
- Review is required;
- a customer decision is needed;
- a formal result has returned;
- a new customer opportunity has emerged;
- a previous Lite Candidate should be retired;
- a new Artifact should be prepared.

The Today item should answer:

1. what changed in MarkReg;
2. which Lite journey it relates to;
3. what the user should inspect;
4. what may be prepared in Lite;
5. what must continue in MarkReg;
6. whether the Return is fresh and complete.

A MarkReg Return does not automatically create an active Lite Task.

It may create an Attention Item or Continuation State.

## 9. MarkReg outcomes can create new Lite value

The relationship is not one-way.

A returned result may create:

- a client explanation;
- a renewal or maintenance opportunity;
- an additional jurisdiction recommendation;
- a portfolio inconsistency signal;
- a case lesson candidate;
- a reusable work-product candidate;
- a customer follow-up package;
- an Organization Memory Candidate.

Example:

```text
MarkReg returns examination result
→ Lite presents sourced Return
→ user inspects professional consequence
→ Lite prepares customer explanation Artifact
→ user confirms Communication
→ customer responds
→ MarkReg continuation may be required
```

This creates continuity without transferring lifecycle ownership.

## 10. Corrections must cross the gateway

Suppose Lite sent an incorrect proposed applicant name.

MarkReg requested clarification, and the customer supplied the correct legal entity.

The correction path should be:

```text
customer correction
→ ML-M02 Correction Record
→ affected Lite Candidate and Artifact identified
→ continuation Handoff with corrected source
→ MarkReg revalidation
→ destination record corrected under its own controls
→ Return confirms destination result
```

Lite must not silently edit a displayed MarkReg record and claim the destination has changed.

Similarly, if MarkReg corrects an official or formal fact, Lite should:

- update the Return projection;
- mark affected Candidates stale or corrected;
- identify affected Artifacts;
- retire invalid recommendations;
- preserve the correction lineage.

## 11. A complete example

A small agency manages a client's domestic mark and notices that the customer has begun selling in another jurisdiction.

### In Lite

```text
public and customer-authorized market signal
→ Service-Value Candidate
→ user inspects relevance
→ customer-facing expansion brief
→ customer requests a quotation and filing options
→ Qualification Result
→ MarkReg Handoff prepared
```

The Handoff includes:

- Customer reference;
- proposed applicant information;
- mark representation;
- target jurisdiction;
- preliminary goods/services context;
- customer response;
- selected work-product version;
- missing signed authority;
- source and data restrictions.

### In MarkReg

MarkReg revalidates and returns:

```text
Product Session created
formal applicant name requires confirmation
goods/services review required
power of attorney required before filing
```

### Back in Lite

Today shows:

- MarkReg Product Session reference;
- two information requests;
- a link to continue in MarkReg;
- an option to prepare a plain-language customer request Artifact.

Lite does not show:

```text
filing started
Matter complete
application ready
```

unless MarkReg returns those formal results.

## 12. Common failure patterns

### Failure 1 — creating a shadow Matter

Lite copies MarkReg status fields into a Product-local record and updates them independently.

Why it fails:

- two sources of truth emerge;
- corrections diverge;
- users cannot know which status is authoritative.

### Failure 2 — treating a Handoff as acceptance

The UI changes from “ready to send” directly to “MarkReg case opened.”

Why it fails:

- destination validation is skipped;
- duplicate and authority checks disappear.

### Failure 3 — sending too much context

The Handoff includes the user's entire customer archive and unrelated Matters.

Why it fails:

- purpose limitation is lost;
- confidentiality exposure grows;
- MarkReg must sort through irrelevant data.

### Failure 4 — sending too little context

Only a chat summary is sent, without sources, versions or missing information.

Why it fails:

- MarkReg cannot distinguish fact from inference;
- the user must repeat the full story.

### Failure 5 — blind retry

A timeout occurs and Lite automatically sends the same launch request again.

Why it fails:

- duplicate Product Sessions or work may be created.

## 13. Conformance questions

A conforming implementation should be able to answer:

- Which Lite record caused the MarkReg Handoff?
- Which user and Organization initiated it?
- Which exact Artifact Version was included?
- Which facts were confirmed, proposed or missing?
- What authority context was supplied?
- Did MarkReg accept, reject, block or request more information?
- What formal reference did MarkReg return?
- Which service owns the displayed status?
- What happens if the Return becomes stale?
- How are corrections propagated?
- How are duplicate launch requests prevented?
- Can the user continue in MarkReg without re-entering authorized context?

## Chapter Conclusion

The MarkReg gateway should feel continuous to the user while remaining explicit in architecture.

```text
Lite understands the opportunity
MarkReg owns the formal lifecycle
Lite preserves daily continuity
```

The Product becomes more valuable because it reduces reconstruction, not because it collapses responsibility.

That is the correct role of `ML-H03` and `ML-HC-01`.