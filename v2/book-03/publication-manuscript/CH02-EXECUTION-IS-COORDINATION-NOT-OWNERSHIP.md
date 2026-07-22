# Chapter 02 — Execution Is Coordination, Not Ownership

Execution sits in the middle of many important events. It receives requests, evaluates eligibility, assigns work, collects contributions, routes reviews, records approvals, invokes systems and returns evidence. Because it touches so much, it can easily be mistaken for the owner of everything it coordinates.

That would be a serious architectural error.

## 1. The temptation of central ownership

A central execution layer can see that:

- a customer requested work;
- a Workplace accepted responsibility;
- a Product started an intake;
- a Matter needs an outcome;
- a Contributor submitted a result;
- a Provider reports completion;
- a payment checkpoint was reached;
- an official record may have changed.

From an implementation perspective, it may seem efficient to store the definitive status of all these objects inside one workflow engine. The result would initially look simpler: one queue, one state machine, one audit log and one administrative screen.

Over time, however, the simplification would destroy important distinctions.

The workflow engine would begin deciding who owns the customer, whether an Order exists, whether a Matter is complete, whether payment is settled, whether a Provider has authority and whether an official act occurred. Product convenience would silently become business and professional authority.

Book 03 rejects that model.

```text
Orchestration
≠ Business Ownership
≠ Relationship Ownership
≠ Professional Authority
≠ Formal-state Authority
```

## 2. What Execution actually owns

Execution may be authoritative for its own coordination records, including:

- the Capability Request received;
- the version and context validated;
- eligibility findings;
- the implementation binding selected;
- Assignment offers and acceptance;
- scoped access granted;
- Contributions returned;
- Review findings;
- Approval records;
- apply attempts;
- idempotency and retry data;
- Provider or connector returns;
- reconciliation status;
- execution evidence and audit events.

These records answer the question:

> What governed work was requested, prepared, assigned, reviewed, attempted and returned?

They do not necessarily answer:

> What is the definitive current business or official state of the customer, order, matter, payment, document or trademark right?

That second question belongs to the relevant Owning Service and authoritative external sources.

## 3. Workplace remains the business-sovereignty context

A Workplace is not merely a tenant identifier passed into a task. It is the context within which customer relationships, commercial policies, private knowledge, Product Installations, members, data permissions and collaboration choices are governed.

Execution must therefore receive and respect Workplace context, but it does not absorb it.

```text
Execution inside a Workplace
≠ Execution owns the Workplace

Access to Workplace data
≠ Right to reuse the data elsewhere

Assignment from a Workplace
≠ Transfer of the customer relationship
```

This is particularly important in white-label and co-delivery arrangements. MarkReg may prepare work. A Contributor may review a classification. An MGSN Provider may file locally. Execution coordinates these actions. The originating Workplace may still remain the Relationship Owner and Contracting Party.

Execution cannot infer customer ownership from who completed the most work, who saw the customer details or who received a payment.

## 4. Product remains the experience and capability surface

Products such as Lite, MarkReg and Sites provide user experiences and domain-specific capabilities. They may create or initiate execution requests, show progress and project selected results back to users.

But Product state and Execution state are different.

A Product may display:

- preparing;
- waiting for review;
- customer approval required;
- submitted;
- evidence available.

Underneath, Execution may preserve more detailed states and evidence. Neither layer should silently become the formal owner of a Matter or official record merely because it presents the status.

```text
Product Projection
≠ Formal State

Simplified User Status
≠ Loss of Underlying Distinctions
```

The Product can simplify presentation. It cannot simplify away responsibility.

## 5. Owning Services retain formal-state authority

A formal object needs one clearly identified authority for mutation. Depending on the object, that may be the Owning Service for:

- Customer;
- Opportunity;
- Engagement;
- Order;
- Matter;
- Payment;
- Document;
- Assignment;
- official-right baseline;
- other governed records.

Execution can propose or report a transition. The Owning Service determines whether the returned evidence satisfies the formal contract.

For example:

```text
Provider Return Received
→ Execution records Return
→ Owning Service validates receipt and identifiers
→ Matter formal state may change
```

The middle step cannot be skipped. A Provider's email, an AI interpretation or a successful HTTP response may be evidence candidates, but they are not automatically formal truth.

## 6. Core remains semantic authority

Execution uses shared concepts but does not redefine them ad hoc.

If Book 03 needs Capability Request, Work Package, Assignment, Contribution, Review, Outcome or Evidence contracts, one of two things must be true:

1. the concept already exists under accepted Core semantics; or
2. it remains explicitly Execution-local until a Core governance decision promotes or reconciles it.

The manuscript may describe the required behavior. It may not silently declare every useful execution record a universal Core object.

```text
Execution Needs a Concept
≠ Core Automatically Owns a New Object
```

This distinction prevents publication text, implementation convenience and canonical semantics from drifting apart.

## 7. Relationship ownership is not inferred from participation

Many participants may touch the same work:

- Demand Originator;
- Relationship Owner;
- Product operator;
- Delivery Owner;
- Contributor;
- Reviewer;
- Approver;
- Provider;
- Payment Receiver;
- Recovery Owner.

These roles can be held by different people and organizations. Execution must preserve the role record for the specific Engagement or Work Package.

It must not derive permanent organization types from temporary participation.

```text
Can Communicate
≠ Owns Relationship

Receives Funds
≠ Owns Customer

Performs Work
≠ Holds Professional Authority

Reviews Work
≠ Becomes Delivery Owner
```

This is one reason Assignment must be scoped and time-bound. Participation should end when the relevant authority and access end.

## 8. Professional authority cannot be manufactured operationally

Execution can identify a highly capable person, a certified contributor or a reliable AI implementation. It can recommend them for a task. It cannot manufacture statutory or jurisdictional authority.

A person may be capable of preparing an Office Action response but not legally permitted to represent the applicant. An AI system may identify strong arguments but cannot sign or assume professional responsibility. A Contributor may produce excellent evidence analysis but cannot automatically instruct an external office.

```text
Operational Capability
≠ Professional Qualification
≠ Customer Representation
```

Where professional authority is required, Execution must verify the authority, bind it to the action and preserve the accountable actor.

## 9. Financial records do not create custody authority

Execution may coordinate commercial checkpoints:

- quotation accepted;
- invoice issued;
- customer paid;
- Provider prepayment required;
- Contributor compensation earned;
- official fee evidence returned;
- refund or credit pending.

These records are necessary for work coordination. They do not imply that MarkOrbit or Execution is legally authorized to hold, pool, transmit or escrow funds.

```text
Payment Coordination
≠ Payment Custody

Settlement Trigger
≠ Permission to Move Funds
```

Book 03 therefore treats settlement as governed evidence and trigger logic unless a separate, explicit legal and Product architecture authorizes more.

## 10. Coordination without ownership is a strength

Separating coordination from ownership may look more complex than one central database. In fact, it is what allows MarkOrbit to support:

- multiple Products;
- independent Workplaces;
- white-label delivery;
- co-delivery;
- internal and external providers;
- professional networks;
- different jurisdictions;
- portable customer relationships;
- auditable responsibility.

The system can coordinate deeply without becoming a hidden commercial principal, universal employer, universal professional firm or central owner of every record.

That is not a limitation of Execution. It is the foundation of trustworthy collaboration.

## 11. The ownership boundary

The governing rule is:

> Execution owns the evidence of governed coordination. It does not automatically own the business, professional or official objects affected by that coordination.

This boundary keeps the trust engine powerful without turning it into an unaccountable center of platform sovereignty.
