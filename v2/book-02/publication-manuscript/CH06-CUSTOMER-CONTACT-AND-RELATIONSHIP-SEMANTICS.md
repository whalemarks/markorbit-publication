# CH06 — Customer, Contact and Relationship Semantics

## A customer is not merely a person in an address book

Professional platforms routinely collapse several different realities into one “customer” record:

- the person who sent the email;
- the company that will own the trademark;
- the party that signed the engagement;
- the party that pays;
- the party that receives updates;
- the party whose relationship an agency protects.

That shortcut makes simple interfaces possible, but it creates dangerous ambiguity in service delivery, privacy, conflicts, billing and cross-Workplace collaboration.

Book 02 therefore separates:

```text
Customer
Contact Person
Contact Point
Contact Role
Relationship
Relationship Owner
```

## Customer

A Customer is a commercial or service relationship object in a defined Workplace context.

A Customer may reference a Person, an Organization or another permitted party profile. The Customer object records that the Workplace has an accepted relationship for a declared purpose.

It does not automatically establish:

- applicant identity;
- trademark ownership;
- payment responsibility;
- authority to instruct;
- marketing consent;
- authority to sign;
- permanent platform-wide customer status.

```text
Customer
≠ Applicant
≠ Owner
≠ Payer
≠ Instructor
≠ Signatory
```

Those roles may coincide, but the system should record coincidence rather than assume it.

## Contact Person and Contact Point

A Contact Person is a Person referenced for communication in a particular context.

A Contact Point is the actual channel or address used, such as:

- email address;
- phone number;
- messaging account;
- postal address;
- secure portal identity.

One Person may have several Contact Points. One generic mailbox may serve several people. A company address may be valid for service but not for personal outreach.

Each Contact Point should therefore preserve:

- source;
- verification status;
- purpose;
- represented party;
- effective time;
- consent or lawful-use basis where required;
- restrictions and suppression state.

```text
contact data available
≠ permission to use it for every purpose
```

## Contact Role

A Contact Role explains why a Person or Contact Point may be used in a particular relationship.

Examples include:

- operational contact;
- billing contact;
- legal representative;
- applicant signatory;
- owner representative;
- receiving contact;
- emergency deadline contact;
- marketing contact.

A Contact Role must be scoped. A billing contact should not automatically receive confidential prosecution strategy. An operational contact should not automatically approve abandonment. A public company email should not automatically become a marketing lead.

## Relationship

A Relationship records a meaningful, purpose-bound connection between parties or Workplaces.

Examples include:

- customer relationship;
- referral relationship;
- provider relationship;
- co-delivery relationship;
- represented-party relationship;
- professional appointment;
- supplier relationship;
- historical former-customer relationship.

Relationship semantics should preserve:

- participants;
- relationship type;
- origin and provenance;
- purpose;
- effective and expiry dates;
- commercial mode;
- communication permissions;
- confidentiality and non-circumvention terms;
- transfer or termination state.

A Relationship is not just a graph edge. It has commercial, evidentiary and authority consequences.

## Relationship Owner

Relationship Owner identifies the Workplace or accountable party responsible for stewarding a customer or commercial relationship in a given Engagement or operating context.

Relationship ownership means responsibility for:

- customer continuity;
- communication policy;
- disclosure control;
- commercial provenance;
- conflict and non-circumvention rules;
- explicit handover where required.

It does not mean absolute ownership of the person, the legal matter or all associated data.

```text
Relationship Owner
≠ owner of the customer as a person
≠ formal-state authority
≠ professional authority
≠ universal right to withhold portability
```

## Shared visibility does not transfer the relationship

A MarkReg delivery team may need customer facts. A Provider may need the applicant name and contact evidence. Lite may receive an Outcome for future customer service. MGSN may route a Work Package.

None of these disclosures automatically transfers the customer relationship.

```text
customer context projected
≠ customer relationship transferred
```

A Handoff should state:

- originating Relationship Owner;
- receiving role;
- purpose and scope;
- communication mode;
- whether direct contact is allowed;
- whether independent marketing is prohibited;
- whether any relationship transition is intended;
- what evidence must return.

## Customer creation and formalization

A public Inquiry, service lead or content conversion event is not necessarily a Customer.

A controlled path is:

```text
Signal or Inquiry
→ qualification
→ represented-party clarification
→ relationship acceptance
→ Customer creation in an owning Workplace
```

This prevents public records, scraped contacts and anonymous visitors from becoming platform-wide customers by implication.

Likewise, a Customer in Lite does not automatically become a Customer in a MarkReg-operated Workplace. A typed Handoff and receiving acceptance are required.

## Former customers and continuing duties

A Relationship may end while duties remain.

Examples include:

- confidentiality;
- document retention;
- deadline handover;
- unpaid invoices;
- certificate custody;
- conflict restrictions;
- suppression from future outreach.

The relationship lifecycle must therefore distinguish active service, dormant, former, terminated, transferred and disputed states.

```text
no active Matter
≠ no continuing duty
```

## Constitutional rule

```text
Customer identifies an accepted relationship in context.
Contact identifies how and why communication may occur.
Relationship records the purpose-bound connection.
Relationship Owner preserves stewardship without claiming universal ownership.
```

This separation allows MarkOrbit to coordinate across Products and Workplaces while protecting customer choice, commercial provenance and lawful communication.