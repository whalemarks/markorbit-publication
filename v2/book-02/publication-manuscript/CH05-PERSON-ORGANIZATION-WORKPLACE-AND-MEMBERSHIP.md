# CH05 — Person, Organization, Workplace and Membership

## Identity must not be flattened into one account

Professional platforms often begin with a simple user table. The simplification is attractive because authentication, billing and permissions appear easier when one login equals one actor.

That assumption fails as soon as a real person represents several businesses, a company operates several service units, or an external professional participates in a bounded engagement without joining the customer’s organization.

Book 02 therefore separates four concepts:

```text
Person
Organization
Workplace
Membership
```

They are related, but none is a substitute for another.

## Person

A Person represents a natural human identity or a controlled reference to one.

A Person may:

- authenticate through one or more accounts;
- use several names or scripts;
- hold roles in multiple Organizations;
- join multiple Workplaces;
- receive an Assignment;
- provide a Contribution;
- hold external professional qualifications;
- act through delegated authority.

A Person record does not by itself prove identity, employment, professional qualification, authority to sign or right to represent a customer.

```text
Person identified
≠ identity verified for every purpose
≠ authorized representative
```

Verification must remain purpose-specific. A verified email may be enough to receive a draft. It may be insufficient to approve a filing, transfer a trademark or access highly sensitive documents.

## Organization

An Organization represents a legal, institutional, commercial or professional body.

Examples include:

- a trademark owner;
- an applicant company;
- an agency;
- a law firm;
- a provider organization;
- a platform operator;
- a government office;
- a university or certification body.

An Organization may exist without operating a Workplace in MarkOrbit. It may be referenced only as an applicant, owner, payer, provider, source or counterparty.

The Organization record should preserve identity evidence, names, jurisdictions, identifiers and relationships without pretending that every reference is verified to the same degree.

```text
Organization reference
≠ active platform participant
≠ customer relationship
≠ provider eligibility
```

## Workplace

A Workplace is the business-sovereignty and Product-operation boundary.

It is the context in which an individual or organization conducts work, installs Products, applies operating policy, manages relationships and controls private business records.

A Workplace may be:

- personal;
- organizational;
- a dedicated operating unit;
- a supervised environment;
- a temporary but governed project context where the Canon permits one.

A Workplace is not automatically a legal person. It may represent an Organization, a department, a service line or an independent professional context.

```text
Workplace
≠ Organization
≠ account
≠ database tenant alone
```

The Workplace answers questions such as:

- whose commercial policy applies;
- which Products are installed;
- who may act in this operating context;
- which customer relationships are governed here;
- what information may be projected to other Workplaces;
- how AI memory and shared learning are controlled;
- which connectors, providers and payment arrangements are allowed.

## Membership

Membership connects a Person to a Workplace under a bounded organizational role.

A Membership may record:

- role or role profile;
- effective time;
- status;
- invitation and acceptance;
- supervisory relationship;
- ordinary access boundaries;
- policy acknowledgements;
- expiry, suspension or departure.

Membership should not be overloaded with task authority.

```text
Membership
≠ Assignment
≠ Production Authorization
≠ Professional Qualification
≠ Provider Appointment
```

A member may be allowed to see the Workplace’s dashboard without being allowed to approve an application. A manager may allocate ordinary internal work without being qualified to sign a jurisdiction-specific declaration. A departing member may lose future access while their historical Contributions remain attributable.

## One Person, several represented contexts

A Person may simultaneously be:

- owner of a personal Workplace;
- member of an agency Workplace;
- appointed professional in a Provider Organization;
- reviewer for a bounded Work Package;
- customer representative in another Engagement.

The system must not infer authority in one context from role in another.

```text
same Person
≠ same represented capacity
≠ same allowed purpose
```

Every consequential action should bind to:

- the acting Person;
- the represented Workplace or Organization;
- the role or Assignment;
- the purpose;
- the authority source;
- the object and version affected.

## Organization membership and Workplace membership

Real organizations may maintain employment, partnership or professional relationships outside MarkOrbit. Core should not assume that Workplace Membership reproduces every legal organizational relation.

For example, a consultant may be invited into a Workplace for a limited project without becoming an employee. Conversely, an employee may exist in the Organization’s HR system but have no active Workplace Membership.

```text
organizational relationship
≠ Workplace Membership
```

Where important, the platform should reference the external relationship and its evidence rather than manufacture it from platform access.

## Departure and continuity

Removing a Membership must stop future access and authority but must not erase history.

The platform should preserve:

- actions already taken;
- Contributions and Reviews;
- approvals and delegations;
- evidence of access and disclosure;
- unresolved responsibilities;
- reassignment and handover.

```text
Membership ended
≠ historical attribution deleted
≠ active obligations resolved
```

## Constitutional rule

```text
A Person is the human actor.
An Organization is the institutional body.
A Workplace is the business-sovereignty context.
Membership is the bounded relationship that permits participation.
```

Keeping these concepts separate allows MarkOrbit to support complex professional representation without turning login access into organizational, commercial or professional authority.