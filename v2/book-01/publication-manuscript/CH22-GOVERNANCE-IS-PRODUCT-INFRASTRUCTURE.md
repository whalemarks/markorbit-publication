# Chapter 22 — Governance Is Product Infrastructure

Governance is often treated as documentation added after a Product is designed. In professional systems, that sequence is backwards.

When a Product handles customer relationships, legal records, professional advice, deadlines, payments, evidence and external providers, governance determines what the Product is allowed to do.

It is therefore part of the Product infrastructure.

## 1. Governance appears in ordinary user actions

A user experiences governance when the system decides:

- whether a record can be edited;
- whether AI may propose or apply a change;
- whether a Provider may see customer identity;
- whether a contributor is eligible for a Work Package;
- whether a recommendation requires human approval;
- whether evidence is sufficient to mark a milestone complete;
- whether a payment may be released;
- whether a deadline is confirmed or still a candidate.

These are Product behaviors, not policy footnotes.

## 2. Five authority questions

Every consequential action should answer five questions:

```text
Who owns the business relationship?
Who defines the meaning?
Who may change formal state?
Who holds the source or evidence?
Who bears professional or legal responsibility?
```

When these answers differ, the system must preserve the difference.

## 3. Preview, approval and Apply

AI-assisted systems frequently collapse suggestion and execution.

MarkOrbit should preserve:

```text
Preview
→ specific approval
→ Apply
→ verified result
```

Approval must identify the actual proposed action, affected records, version and known consequences.

A general statement such as “allow AI assistance” is not sufficient authorization for every future mutation.

## 4. Segregation of duties

High-risk actions may require different people or roles to:

- prepare;
- review;
- approve;
- execute;
- reconcile.

The system should not assume one actor can safely control the entire chain.

Segregation is especially important for:

- funds;
- deadline changes;
- Provider appointment;
- filing instruction;
- official-status acceptance;
- credential issuance;
- production authorization;
- canonical knowledge promotion.

## 5. Governance must remain visible

A Product becomes frustrating when it blocks actions without explanation.

Governance controls should therefore explain:

- what rule applies;
- why the action is restricted;
- what evidence is missing;
- who can approve;
- what alternative route exists.

Good governance is not invisible bureaucracy. It is understandable constraint.

## 6. Exceptions are part of the design

Professional work produces exceptions:

- urgent filing requests;
- missing originals;
- uncertain official status;
- Provider silence;
- conflicting instructions;
- customer requests outside scope;
- expired credentials;
- unexpected official fees.

A mature system does not eliminate exceptions. It gives them typed states, responsible owners and recovery paths.

## 7. Audit without surveillance

Auditability requires enough evidence to reconstruct consequential decisions.

It does not justify recording every human action indefinitely.

The system should collect evidence proportionate to:

- risk;
- authority;
- financial impact;
- legal consequence;
- dispute probability.

Purpose limitation and retention rules remain essential.

## 8. Governance creates commercial trust

Customers, agencies, contributors and Providers will use the platform for serious work only when they understand:

- their relationships will be protected;
- work will not be reassigned silently;
- fees will not be changed without basis;
- evidence will be preserved;
- mistakes can be corrected;
- responsibility will not disappear between systems.

Governance is therefore a growth mechanism. It lowers the trust cost of collaboration.

## Closing

In MarkOrbit, governance is not a committee standing outside the Product.

It is the set of operational contracts that allow distributed actors, AI and systems to work together without erasing responsibility.
