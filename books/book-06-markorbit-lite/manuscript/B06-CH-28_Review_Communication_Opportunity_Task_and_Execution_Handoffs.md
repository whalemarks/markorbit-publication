# B06-CH-28 — Review, Communication, Opportunity, Task and Execution Handoffs

**Status:** Complete Draft 1  
**Chapter Map:** B06-TOC-V0.1 — Owner Accepted  
**Part:** Part VI — MarkOrbit Gateways and Continuity  
**Primary controls:** ML-H01, ML-H05–ML-H08, ML-HC-03–ML-HC-07

## Chapter Purpose

This chapter explains why Lite must use distinct Handoff contracts for Review, Communication, Opportunity, Task and Execution rather than hiding all consequences behind one generic action button.

The central proposition is:

> Different destinations create different formal consequences, so each Handoff must identify the exact decision, authority, version and result expected from that destination.

Lite may orchestrate continuity across these services. It may not collapse their responsibilities into a single Product-local state.

## 1. A single “execute” action is unsafe

A user may move from a Lite Candidate to several different next steps:

- ask a professional to review an Artifact;
- send a message to a customer;
- request creation of a formal Opportunity;
- request creation of a Task or Workflow;
- submit a protected operation to governed Execution.

These actions look sequential in the user journey, but they are not semantically equivalent.

```text
review a recommendation
≠ approve customer contact
≠ send Communication
≠ create Opportunity
≠ create Task
≠ execute protected action
```

A generic button such as:

```text
Proceed
```

may conceal:

- which destination is being invoked;
- which exact version is affected;
- which recipients will receive information;
- whether professional Review is required;
- whether a formal business record will be created;
- whether an External Protected Action may follow;
- who is accountable for the result.

Lite therefore needs typed Handoffs.

## 2. The common Handoff envelope

`ML-H01 Handoff Envelope` provides the common structure.

Every material Handoff should preserve:

- origin Product and Lite Session;
- active Organization;
- initiating user;
- responsible participant;
- source Candidate, Artifact or Return;
- exact selected version;
- purpose;
- destination;
- intended consequence;
- sources and provenance;
- data classification;
- disclosure scope;
- required authority;
- Human Review and user-confirmation status;
- missing information;
- expiry;
- return address;
- expected result classes.

The envelope is common.

The destination contract is not.

```text
common transport structure
≠ common formal meaning
```

## 3. Review Handoff — `ML-H05` and `ML-HC-03`

A Review Handoff asks an accountable reviewer to decide something about an exact Artifact or Prepared Action version.

### 3.1 Minimum package

- exact Artifact Version or Prepared Action version;
- purpose;
- audience or recipient;
- sources;
- material claims;
- deterministic fields;
- missing information;
- uncertainty;
- legal, professional or policy questions;
- decision requested;
- scope of possible approval;
- expiry or re-review triggers.

### 3.2 Typed Review results

The reviewer may return:

- approved;
- rejected;
- revisions required;
- limited approval;
- more information required;
- unsupported;
- conflict or permission block.

Limited approval must preserve its scope.

Examples:

```text
approved for internal client discussion only
approved for this named customer only
approved if fee and deadline fields are updated
approved for email, not public publication
```

Lite must not flatten limited approval into a universal `approved` badge.

### 3.3 Review is version-specific

If the reviewed version changes materially, the Review result may no longer apply.

```text
Artifact v3 approved
+ price, legal claim or recipient changed
→ Artifact v4
→ Review required again where applicable
```

### 3.4 Review is not user confirmation

A professional may approve the accuracy of a customer explanation.

The user may still decide not to send it.

Conversely, a user may want to send an unreviewed draft.

The Product must make the missing Review visible and block the action when policy requires it.

```text
Human Review
≠ final user confirmation
```

## 4. Communication Handoff — `ML-H06` and `ML-HC-04`

A Communication Handoff asks the Communication Service or another governed destination to send an exact message to exact recipients through a defined channel.

### 4.1 Minimum package

- exact draft or Artifact Version;
- exact recipient or recipient set;
- recipient identity and relationship;
- channel;
- sender identity or account;
- subject and purpose;
- attachments;
- customer/Matter context;
- consent, opt-out and suppression checks;
- Review status;
- final user confirmation;
- expected send consequence;
- retry and duplicate policy.

### 4.2 Prepared is not sent

The lifecycle should preserve:

```text
not_requested
→ prepared
→ ready_for_confirmation
→ confirmed
→ accepted_by_communication_service
→ sent / failed / blocked / unknown
```

Lite must not skip directly from prepared to sent.

### 4.3 Recipient and channel are part of the decision

A message approved for one recipient is not automatically approved for another.

A draft approved for email is not automatically approved for public social media or instant messaging.

```text
same words
+ different recipient or channel
→ different consequence
```

### 4.4 Unknown send result

A network timeout may occur after the destination accepted the send request.

The state must remain:

```text
unknown_external_outcome
```

until the destination confirms sent, failed or blocked.

Blind retry may create duplicate customer contact.

## 5. Opportunity Formalization Handoff — `ML-H07` and `ML-HC-05`

A Lite Service-Value Candidate or Qualification Result may justify asking the Opportunity Service to create or update formal Opportunity state.

The Handoff should contain:

- qualified customer or prospect reference;
- service need;
- supporting response or Evidence reference;
- source Candidate;
- relationship owner;
- proposed opportunity owner;
- expected service or Product destination;
- timing;
- commercial context when permitted;
- uncertainty and missing information;
- duplicate-check hints;
- privacy and disclosure scope.

### 5.1 Formalization is a destination decision

The Opportunity Service must decide:

- whether the need meets formal Opportunity criteria;
- whether an Opportunity already exists;
- who owns it;
- which stage applies;
- whether the customer/prospect identity is sufficient;
- whether the request should be rejected or returned for more information.

```text
qualified Lite need
≠ formal Opportunity

Opportunity request sent
≠ Opportunity created
```

### 5.2 Returned formal reference

If accepted, the destination may return:

- Opportunity reference;
- owner;
- formal stage;
- next required action;
- related Customer or Contact reference;
- duplicate or merged reference.

Lite may present the result in Today.

It must not maintain a parallel Opportunity stage.

## 6. Task and Execution Handoff — `ML-H08` and `ML-HC-06`

A Prepared Action may require formal work management or protected execution.

Examples include:

- create a Task to collect applicant information;
- start a Workflow for quotation Review;
- assign a document request;
- request a governed filing-preparation step;
- submit an operation that may lead to an External Protected Action.

The Handoff should contain:

- proposed work;
- actor or role;
- authority context;
- subject;
- dependencies;
- exact inputs and versions;
- required Review;
- deadline source;
- protected-action classification;
- expected result;
- rollback, failure or cancellation considerations.

### 6.1 Lite does not create active Task truth

A Today item may suggest:

```text
collect applicant address
```

That suggestion is not an active Task until the Task or Execution service accepts and returns a formal reference.

```text
Attention Item
≠ Task

Prepared Action
≠ Workflow
```

### 6.2 Execution revalidates authority

The destination must revalidate:

- who may perform the action;
- who may approve it;
- whether required information is complete;
- whether the deadline is authoritative;
- whether policy permits the action;
- whether the action is reversible;
- whether an External Protected Action is involved.

Lite cannot transfer authority merely by including a user-confirmation field.

### 6.3 Protected actions need stronger gates

Where a request may result in filing, payment, formal submission, legal representation, rights change or another protected consequence, the destination must preserve:

- exact actor;
- exact subject;
- exact instruction;
- exact document or Evidence references;
- exact approval;
- exact destination;
- execution result;
- acknowledgement and reconciliation.

The Lite Handoff may begin the process but cannot complete the protected action.

## 7. Handoffs may form a chain, but authority does not flow automatically

A common journey may be:

```text
Artifact v2
→ Review Handoff
→ limited approval returned
→ Communication Handoff
→ customer response returned
→ Opportunity Formalization Handoff
→ Opportunity reference returned
→ Task/Execution Handoff
```

Each transition requires its own conditions.

The earlier result does not automatically authorize the later action.

```text
Review approved
≠ send authorized

message sent
≠ Opportunity qualified

Opportunity created
≠ Task approved

Task created
≠ protected action authorized
```

Lite may guide the user through the chain.

It must not create a hidden cascade in which one click triggers every downstream action.

## 8. Exact version continuity across destinations

Version integrity is essential.

Suppose:

1. Artifact v3 was reviewed;
2. the user edits the fee in the message;
3. Communication sends the edited text;
4. Opportunity is created from the response.

The system must know that the sent content was not identical to the reviewed Artifact v3.

A conforming chain should identify:

- reviewed Artifact Version;
- any later derivative or edited version;
- exact sent message version;
- response reference;
- Qualification Result version;
- Opportunity Handoff version.

```text
same subject
≠ same version
```

Without version continuity, approval and accountability become unreliable.

## 9. Data minimization differs by destination

Each destination needs different information.

### Human Review

Needs sources, claims, audience, purpose and exact version.

### Communication Service

Needs recipients, channel, draft, attachments, sender and send consequence.

### Opportunity Service

Needs qualified need, customer/prospect identity, ownership and formalization evidence.

### Task / Execution

Needs work definition, actor, authority, dependencies, approval and execution consequence.

Sending the same broad package to all destinations violates purpose limitation.

```text
one case file
→ four different minimized Handoffs
```

## 10. Destination responses must remain typed

A destination may return:

- accepted;
- more information required;
- rejected;
- blocked;
- failed;
- unknown external outcome;
- formal reference returned;
- completed by destination.

The meaning depends on the destination.

For example:

```text
Review accepted
= exact version approved within scope

Communication accepted
= send request accepted, not necessarily sent

Opportunity accepted
= formal Opportunity created or updated

Execution accepted
= request entered governed execution, not necessarily completed
```

A generic green checkmark cannot explain these differences.

## 11. Return and continuation in Today

Lite may present destination results as Attention Items:

- Review revisions required;
- Communication failed;
- Opportunity duplicate found;
- Task created and assigned;
- Execution blocked by missing approval;
- protected action completed by destination;
- external outcome unknown.

Each item should show:

- destination;
- source Handoff;
- result type;
- formal reference, if any;
- source time;
- responsible participant;
- next action;
- whether the result is complete or provisional.

Lite should link the user to the destination surface for formal work.

It may prepare the next Product-local Artifact or Handoff, but it must not mutate the destination record.

## 12. Cancellation, revision and supersession

A user may change direction after preparing a Handoff.

Before destination acceptance, the Product may allow the request to be withdrawn or superseded.

After acceptance, cancellation depends on destination rules.

Examples:

- an unsent Communication request may be cancelled;
- a sent message cannot be unsent through Product state;
- an unreviewed package may be replaced;
- an approved Review remains historical even when superseded;
- a formal Opportunity may require a formal close reason;
- an active Task may require cancellation or reassignment;
- an executed protected action may be irreversible.

```text
Lite marks request cancelled
≠ destination consequence reversed
```

The Return must confirm any destination cancellation.

## 13. A complete example

A customer confirms interest in filing a new mark.

### Step 1 — Review

Lite prepares a filing-options Artifact and sends `ML-H05`.

The reviewer returns:

```text
limited approval
approved for customer discussion
class scope still requires formal MarkReg review
```

### Step 2 — Communication

The user confirms the exact message and sends `ML-H06`.

Communication returns:

```text
sent
message reference COMM-...
```

### Step 3 — Customer response

The customer requests a formal quotation and selects one jurisdiction.

Lite creates a Qualification Result.

### Step 4 — Opportunity

Lite sends `ML-H07`.

Opportunity Service returns:

```text
formal Opportunity created
owner assigned
```

### Step 5 — MarkReg and Task

A MarkReg Handoff creates a Product Session, and the destination requests applicant details.

Lite prepares `ML-H08` to create a Task for information collection.

The Task Service returns a formal Task reference.

At no point does Lite claim that filing has been approved or completed.

## 14. Common failure patterns

### Failure 1 — one-click cascade

“Approve” triggers message send, Opportunity creation and Task creation.

Why it fails:

- separate decisions and authorities disappear;
- the user cannot inspect consequences.

### Failure 2 — stale Review reused

An old Review result is applied to a changed Artifact.

Why it fails:

- exact-version integrity is broken.

### Failure 3 — Communication accepted shown as sent

The destination accepted the request but has not confirmed delivery.

Why it fails:

- the customer may receive duplicate follow-up after retry.

### Failure 4 — Lite owns Opportunity stage

Lite changes an Opportunity from qualified to won without the Opportunity Service.

Why it fails:

- formal commercial truth is duplicated.

### Failure 5 — Task suggestion becomes deadline authority

A Today item is treated as a formal deadline-bound Task.

Why it fails:

- the source and accountable workflow are unclear.

### Failure 6 — user confirmation treated as protected-action approval

The user clicks confirm and the Product files or pays automatically.

Why it fails:

- Execution and External Protected Action controls are bypassed.

## 15. Conformance questions

A conforming implementation should answer:

- Which Handoff contract is being used?
- What exact consequence is requested?
- Which version is being reviewed, sent, formalized or executed?
- Which destination owns the result?
- Is Human Review required?
- Has the user confirmed the exact recipient, channel and action?
- What data is necessary for this destination?
- What data has been withheld?
- Did the destination accept the request or complete the action?
- What formal reference was returned?
- What happens after a material edit?
- Can a request be cancelled or superseded?
- What happens when the result is unknown?
- Is any protected action being implied or triggered?

## Chapter Conclusion

Lite should feel like one coherent Product while preserving multiple formal responsibility boundaries.

```text
one user journey
≠ one formal service
```

The correct architecture is:

```text
Lite prepares and explains
Human decides
Destination revalidates and owns formal state
Return restores continuity
```

Typed Handoffs are what make that continuity trustworthy.