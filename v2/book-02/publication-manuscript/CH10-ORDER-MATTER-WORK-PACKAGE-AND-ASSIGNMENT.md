# CH10 — Order, Matter, Work Package and Assignment

## One customer request creates several different records

A customer may say, “Please file this trademark in the United States.”

That single sentence can lead to:

- a commercial commitment;
- a long-lived professional subject;
- several bounded units of work;
- multiple actor-specific authorizations;
- review and approval events;
- external submissions and returns.

A weak architecture stores all of this in one `case`, `task` or `order` record. That makes reporting easy at first and governance impossible later.

Book 02 preserves four different meanings:

```text
Order
≠ Matter
≠ Work Package
≠ Assignment
```

## Order is the commercial commitment

Order answers:

> What has the customer or contracting party agreed to obtain and pay for?

An Order may preserve:

- customer and contracting references;
- accepted scope;
- pricing and fee components;
- service promise;
- delivery terms;
- cancellation and refund rules;
- relevant Matter references;
- current commercial status.

Order status should describe the commercial relationship, not every professional or official state.

```text
Order accepted
≠ Matter ready
≠ work assigned
≠ filing submitted
```

An Order can be paid while work is blocked by missing documents. A Matter can remain active after the original Order is financially complete. One Order can cover several Matters, and one Matter can require later Orders for additional services.

## Matter is the long-lived professional subject

Matter answers:

> What professional subject, right, dispute, application or lifecycle context is being managed over time?

For trademark work, a Matter may follow:

- search;
- filing preparation;
- application;
- prosecution;
- registration;
- maintenance;
- recordal;
- transaction;
- recovery.

Matter should preserve formal and professional continuity even when commercial arrangements change.

```text
Matter
≠ invoice container
≠ workflow instance
≠ universal task list
```

The Owning Service retains formal-state authority for the Matter or the specific formal record represented by it.

## Work Package is the bounded production contract

Work Package answers:

> What exact outcome must be produced as a governable unit of work?

The Book 02 reconciliation treats Work Package as a candidate shared semantic because Books 03, 04, 05 and 06 all need a stable bounded unit between broad goals and individual execution.

A proposed Work Package contract includes:

- objective;
- purpose;
- input references and versions;
- required output;
- exclusions;
- eligibility conditions;
- authority ceiling;
- visible data;
- deadline;
- review policy;
- acceptance criteria;
- evidence return;
- compensation reference where applicable.

```text
Work Package
≠ Workflow
≠ Step
≠ Product Task
```

The Work Package should remain meaningful whether completed by an employee, a contributor, an AI-assisted route, a deterministic system or an external provider.

## Assignment is the scoped authorization to perform work

Assignment answers:

> Which eligible actor or implementation is authorized to perform this exact Work Package, under what terms?

Assignment should bind:

- Work Package version;
- assignee;
- represented Workplace;
- accepted role;
- data scope;
- allowed actions;
- deadline;
- review requirements;
- authority ceiling;
- compensation terms;
- expiry, suspension and revocation.

```text
Assignment accepted
≠ work completed
≠ Contribution accepted
≠ professional action approved
```

Assignment is neither a permanent role nor a general platform credential.

## Why Matter must not contain every task directly

Matter is long-lived. Work Packages are bounded and versioned. Assignments are temporary and actor-specific.

If all work is stored as mutable fields on the Matter:

- historical scope disappears;
- review cannot bind an exact output version;
- reassignment overwrites prior responsibility;
- compensation cannot be linked to accepted production;
- AI and human contributions become indistinguishable;
- external provider action cannot be separated from internal preparation.

A Matter should reference the governed execution records rather than absorb them.

## Why Order must not become the execution state

Order systems often expose statuses such as `processing`, `completed` and `failed`. These are too coarse for professional work.

The platform may simultaneously have:

```text
Order: paid
Matter: active
Work Package: revision required
Assignment: reassigned
Official State: pending examination
Provider Return: incomplete
```

No single status should overwrite the others.

## Decomposition example: trademark filing

A single filing Matter may require Work Packages such as:

1. applicant identity verification;
2. mark representation validation;
3. classification and goods preparation;
4. search analysis;
5. document readiness;
6. fee verification;
7. professional filing review;
8. customer approval package;
9. provider instruction package;
10. return and official acknowledgement validation.

Each Work Package can have a different implementation, reviewer, deadline and authority boundary.

The external filing itself remains a protected action governed by Book 03. It should not be hidden inside a generic “filing task completed” flag.

## One Work Package may support several records

A verified owner-resolution Work Package may support multiple Matters. A translation review may support a filing package and a public content correction. Reuse is possible only when:

- purpose is compatible;
- source and version remain valid;
- authority permits reuse;
- affected records preserve provenance.

```text
reusable outcome
≠ universal permission to copy
```

## Amendments

If the customer changes the applicant, mark, goods, jurisdiction or budget, the architecture must determine which records change.

The Order may require a commercial amendment. The Matter may preserve the same professional continuity or may need a new related Matter. Existing Work Packages may become invalid. Assignments may require suspension. Reviews and approvals may expire.

```text
scope changed
≠ update one description field
```

A material amendment must preserve old versions and propagate the impact explicitly.

## Completion remains multidimensional

The platform should support separate completion statements:

```text
Order commercially complete
Matter lifecycle stage complete
Work Package accepted
Assignment closed
External action confirmed
Formal state validated
Financial reconciliation complete
```

These may occur at different times.

## Candidate status

Matter and Order are active shared concepts. Work Package and Assignment remain high-priority candidate shared semantics pending the formal Core Change Proposal process.

Publication prose does not activate them.

## Constitutional rule

```text
Order owns the commercial promise.
Matter preserves the professional subject.
Work Package defines bounded production.
Assignment grants scoped performance authority.

None may substitute for the others.
```
