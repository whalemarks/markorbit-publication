# Chapter 03 — Context, Scope and Authority

Execution becomes dangerous when it treats an action as self-explanatory.

“Review this.” “Send this.” “File this.” “Pay this.” “Ask the provider.” Each instruction appears simple only because its missing context is being carried informally in someone's memory. Once work moves across people, AI systems, Products, Workplaces and external providers, that informal context breaks down.

Governed Execution therefore makes context, scope and authority explicit before consequential work begins.

## 1. The same action can mean different things

Consider the instruction:

> Please review the goods list.

Depending on context, this may mean:

- check formatting against an internal template;
- normalize goods for a draft recommendation;
- assess whether items fall within a selected class;
- advise a customer on protection strategy;
- approve the final list for filing;
- confirm acceptability under a specific office's practice.

These are not the same Capability, risk or authority level.

The system must know at least:

- which Workplace is represented;
- which Product initiated the work;
- which customer, Order or Matter is relevant;
- which jurisdiction and procedure apply;
- whether the work is simulation, preparation or production;
- whether the expected result is advice, draft, review, approval or action;
- which data may be disclosed;
- which deadlines and commercial constraints apply.

Without this, assignment and AI assistance become guesswork.

## 2. Execution Context is more than metadata

An Execution Context should be understood as the governed frame within which the requested work has meaning.

It may include:

```text
Workplace
Product Installation
Person and represented role
Customer or relationship context
Engagement
Order and Matter references
Jurisdiction and procedure
Capability and version
Data and document scope
Commercial conditions
Deadline and urgency
Risk and review policy
Simulation or production mode
```

Not every request needs every field. The important requirement is that the system knows which facts are known, which are inherited under authority, which are inferred and which remain Unknown.

Context is not merely attached for reporting. It determines what may happen.

For example, the same person may be eligible to perform an internal analysis in one Workplace but prohibited from seeing the data in another. The same AI implementation may be allowed to draft a customer message but not use the content for memory or training. The same Provider may be qualified for one jurisdiction and conflicted in another.

## 3. Scope defines the promised boundary

Scope answers:

> What outcome is included, what is excluded and where does the actor's responsibility stop?

A good scope identifies:

- the target outcome;
- the affected objects;
- included activities;
- excluded activities;
- permitted tools and implementations;
- visible data;
- communication rights;
- review and approval requirements;
- completion evidence;
- expiry and revocation conditions.

For example:

```text
Prepare a draft response package
for the identified Office Action issues,
using the supplied evidence,
for senior professional review.

Excluded:
customer communication,
final legal approval,
provider instruction,
official submission,
additional fee authorization.
```

This is a Work Package scope. It allows meaningful production while preventing the actor from assuming the whole Matter.

## 4. Authority is typed, not general

Systems often reduce authority to a single role such as `admin`, `manager` or `agent`. Professional execution requires more precise authority.

Relevant authority types may include:

- authority to request a Capability;
- authority to access specified data;
- authority to accept an Assignment;
- authority to contribute work;
- authority to review;
- authority to approve a version;
- authority to communicate externally;
- authority to represent the customer;
- authority to appoint a Provider;
- authority to approve cost;
- authority to initiate payment;
- authority to perform a protected action;
- authority to mutate formal state.

These authorities may belong to different actors.

```text
Can Request
≠ Can Perform
≠ Can Review
≠ Can Approve
≠ Can Apply
≠ Can Mutate Formal State
```

A Product user may request a search. A Contributor may perform the search. A trademark professional may review the findings. The customer may accept the commercial risk. An authorized professional may approve a filing route. A Provider may submit. The Owning Service may validate the receipt and update the Matter.

The system should not compress this chain into a single permission.

## 5. Membership, Capability and authority remain separate

Membership establishes that a Person participates in a Workplace under a role and policy. It does not prove that the Person possesses a Capability or may act on every object.

Capability indicates that an actor or implementation can produce a class of outcome under defined conditions. It does not prove current eligibility or authority.

Certification provides evidence about assessed Capability. It does not create professional qualification.

Production Authorization allows specified production work under current policy. It does not create an Assignment.

Assignment creates a task-specific relationship. It does not extend beyond scope.

Professional Authority permits reserved or regulated action where applicable. It must be independently established.

```text
Membership
≠ Capability
≠ Certification
≠ Production Authorization
≠ Eligibility
≠ Assignment
≠ Professional Authority
```

Execution uses all these concepts, but none can substitute for the others.

## 6. Authority must be current

Authority can expire or become invalid because:

- Membership ended;
- the Assignment was completed or revoked;
- the customer withdrew instruction;
- the approved version changed;
- a professional licence expired;
- a conflict was discovered;
- the Provider declined or stopped accepting work;
- the deadline passed;
- the Product Installation changed policy;
- the data-access purpose ended.

Therefore, authority checks should occur near the consequential boundary, not only when the user first logs in.

```text
Previously Authorized
≠ Authorized Now
```

This is especially important for queued work. A filing prepared on Monday may not be safe to submit on Friday if the applicant changed, the goods were revised or the Provider appointment was withdrawn.

## 7. Delegation must preserve the authority chain

An authorized person may delegate preparation without delegating final authority.

For example:

```text
Professional Authority Holder
→ delegates evidence organization
→ Contributor prepares bounded package
→ Reviewer evaluates package
→ Authority Holder approves exact version
→ Provider performs approved submission
```

The delegate should know:

- who delegated;
- what scope is permitted;
- whether subdelegation is allowed;
- which data may be accessed;
- what review is mandatory;
- when authority expires;
- what actions remain prohibited.

Delegation should not produce orphaned work in which nobody remains accountable for the final outcome.

## 8. Customer decisions and professional decisions differ

A customer may decide:

- which countries matter commercially;
- which mark version to pursue;
- whether to accept cost;
- whether to narrow goods;
- whether to continue after a refusal;
- whether to sell an asset.

A professional may decide or advise on:

- legal interpretation;
- evidence sufficiency;
- procedural acceptability;
- response strategy;
- professional risk;
- reserved actions.

Execution must coordinate the two without pretending that one substitutes for the other.

```text
Customer Business Decision
≠ Professional Opinion

Professional Recommendation
≠ Customer Commercial Approval
```

A customer can accept a disclosed risk, but that does not necessarily authorize an unqualified actor to perform a reserved action.

## 9. AI requires context and authority boundaries too

AI does not operate outside the authority model.

An AI invocation should specify:

- purpose;
- data scope;
- permitted sources;
- collaboration mode;
- prohibited actions;
- expected output type;
- disclosure requirements;
- review policy;
- memory and learning policy;
- expiry of the working context.

A model may be capable of drafting a legal response, but the requested output may be limited to issue extraction. It may be allowed to retrieve private Workplace Knowledge for the current task but prohibited from retaining it. It may recommend a Provider but not appoint one.

```text
Model Capability
≠ Invocation Scope
≠ Action Authority
```

## 10. Scope changes require renewed disposition

Professional work often changes after it begins:

- new documents arrive;
- official fees increase;
- additional classes appear;
- the applicant identity changes;
- an Office Action raises new issues;
- the Provider requires an original document;
- the customer changes the commercial objective.

A material scope change should create an Amendment, revised Work Package or new Approval requirement.

```text
Original Assignment Accepted
≠ Expanded Scope Accepted

Version 1 Approved
≠ Version 2 Approved
```

The system must not treat changing reality as an informal note attached to the original task.

## 11. The context–scope–authority gate

Before high-impact work proceeds, Execution should be able to state:

```text
Context is sufficient
+ Scope is bounded
+ Authority is current
+ Required roles are identified
+ Unknowns are acceptable or escalated
= Work may proceed to the next governed stage
```

Failure at this gate is not bureaucracy. It is early detection of the conditions that later become missed deadlines, unauthorized communications, privacy breaches, unpaid work, duplicate filings and responsibility disputes.

## 12. The governing principle

> An action is not governed merely because the system knows who clicked it. It is governed when the system knows the represented context, promised scope and specific authority for the exact consequence.

Context makes the work intelligible. Scope makes it bounded. Authority makes it legitimate.
