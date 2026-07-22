# CH02 — Authority Must Remain Separated

## One platform contains several different kinds of authority

Many architecture errors begin with the word “owner.” A system may say that a user owns a record, a Workplace owns a customer, a service owns a state, a provider owns a document or Core owns an object. These statements are not equivalent.

Book 02 requires every important record and transition to distinguish at least five authority dimensions:

```text
business sovereignty
semantic authority
formal-state authority
physical custody
legal, evidentiary and professional authority
```

Collapsing them creates accidental power.

## Business sovereignty

Business sovereignty answers:

> Which Workplace or accountable organization legitimately controls the commercial relationship, operating policy and customer context?

A Workplace may determine:

- which Products are installed;
- who may act on its behalf;
- how it prices services;
- which customer relationships it accepts;
- which partner routes it permits;
- how its private information is projected.

Workplace sovereignty does not permit the Workplace to redefine shared Core terms or official legal facts.

```text
business sovereignty
≠ semantic sovereignty
≠ official authority
```

## Semantic authority

Semantic authority answers:

> Which specification defines the stable meaning and compatibility contract?

Core holds semantic authority for shared concepts. A Product may create a local profile or view, but it may not silently change the universal meaning of Customer, Order, Matter, Evidence, Projection, Handoff or Return.

A Lite `Transaction Opportunity` may specialize Opportunity. It should not create a second incompatible root meaning for Opportunity merely because the marketplace needs more fields.

## Formal-state authority

Formal-state authority answers:

> Which Owning Service may create, validate and mutate the authoritative business record?

Execution can coordinate a submission. It cannot, by itself, decide that an application is officially filed. A Product can display a completion state. It cannot manufacture the official result. A Provider Return can supply evidence. It cannot directly become accepted truth.

```text
execution outcome
≠ formal-state mutation
```

The Owning Service must validate the evidence against the applicable rule and preserve the prior state, transition reason and correction path.

## Physical custody

Physical custody answers:

> Who currently stores or possesses the file, original document, credential, asset or data copy?

Custody is not ownership and is not authority.

An external provider may physically hold an original power of attorney. A cloud service may store a certificate. A contributor may temporarily view a customer document. None of those facts automatically grants the right to reuse, disclose, destroy, market with or train on the material.

```text
custody
≠ ownership
≠ purpose expansion
```

## Legal, evidentiary and professional authority

This dimension answers:

> Which institution or qualified actor may establish, interpret, certify or act upon a fact for the relevant purpose?

Examples include:

- a trademark office establishing an official register event;
- a court issuing a decision;
- a qualified local professional giving a reserved opinion;
- a customer-authorized signatory approving a filing;
- a verified source supporting a fee or deadline claim.

Platform confidence, AI quality, Certification and Production Authorization cannot create such authority where external law or professional rules reserve it.

```text
Capability
≠ Professional Qualification
≠ Professional Authority
```

## Authority is contextual

A person may hold several roles without holding every authority.

A director may approve the company’s commercial decision but not provide the local legal opinion. A trademark consultant may prepare a filing package but not sign the applicant’s declaration. A Relationship Owner may communicate with the customer but not approve a payment from another Workplace. A Delivery Owner may coordinate the entire route while relying on other actors for final professional approval.

Core should therefore represent authority as contextual references rather than permanent labels attached to a person.

```text
role in one Engagement
≠ universal actor type
```

## Delegation must preserve its source

Delegated authority should record:

- delegating actor;
- receiving actor;
- represented Workplace or Organization;
- purpose;
- allowed actions;
- object scope;
- effective time;
- expiry;
- revocation;
- whether re-delegation is permitted.

A generic `admin` role is rarely sufficient for consequential action.

## Authority and visibility

Seeing a record does not establish any of the authorities above.

```text
visible
≠ editable
≠ approvable
≠ applicable
≠ ownable
```

A shared Product can project information across Workplaces while preserving relationship ownership, purpose limitation and minimum necessary disclosure.

## Cross-book boundary

Book 03 explains how authority is checked before Assignment, Review, Approval and Apply. Book 05 explains how MarkReg uses these boundaries through a trademark lifecycle. Book 06 explains how Lite uses them in content, marketplace and capability experiences.

Book 02 defines the stable distinctions those systems must not erase.

## Constitutional rule

```text
No convenience layer may merge business sovereignty,
semantic authority, formal-state authority,
physical custody and professional authority
into one implicit “owner” field.
```

The platform becomes trustworthy when every consequential decision can answer not only who acted, but what kind of authority they possessed and for which exact purpose.
