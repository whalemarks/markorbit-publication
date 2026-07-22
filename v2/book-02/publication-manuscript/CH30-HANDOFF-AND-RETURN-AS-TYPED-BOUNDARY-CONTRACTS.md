# CH30 — Handoff and Return as Typed Boundary Contracts

## Boundary crossing must be explicit

When work, context or evidence moves from one Product, Workplace, service or provider to another, the platform must preserve more than a message and attachment.

It must preserve:

- what is being transferred;
- why;
- under whose authority;
- for which object and version;
- what the recipient may do;
- what the recipient must return;
- when the transfer expires or changes.

Book 02 therefore treats Handoff and Return as typed boundary contracts.

```text
Handoff
≠ Message Forward
≠ Assignment
≠ Provider Appointment
≠ External Action

Return
≠ Reply Message
≠ Accepted Outcome
≠ Official Truth
```

## Handoff carries governed context outward

Handoff answers:

> What bounded context and responsibility are being passed from an origin to a destination for a declared next purpose?

A Handoff contract may include:

- origin and destination;
- represented Workplaces and Organizations;
- purpose;
- related Need, Opportunity, Engagement, Order, Matter or Work Package;
- exact object and package versions;
- accepted facts, candidates, assumptions and Unknowns;
- scope and exclusions;
- data and document disclosure;
- customer-contact rules;
- Relationship Owner and Delivery Owner;
- authority and appointment references;
- expected next action;
- deadline and time zone;
- fee or cost ceiling;
- required acknowledgement and acceptance;
- Evidence Return contract;
- amendment, cancellation and recovery route.

```text
Handoff prepared
≠ Handoff authorized

Handoff sent
≠ Handoff accepted
```

## Destination acceptance is a separate state

The recipient should acknowledge:

- correct package and version received;
- scope understood;
- capacity available;
- conflict status;
- authority and qualification status;
- deadline accepted;
- fee terms accepted where relevant;
- missing documents or conditions;
- Return requirements understood.

```text
Delivery confirmed
≠ Responsibility accepted
```

A courier receipt, email delivery or portal upload proves only a delivery event. It does not establish that the professional provider accepted the work or that the external authority accepted the submission.

## Handoff does not create Assignment automatically

A Product-to-Product Handoff may transfer context before any performer is selected. A provider Handoff may accompany an appointment but is not itself the appointment. An Assignment may authorize internal production without transferring the broader customer or Matter context.

```text
Handoff
≠ Assignment
≠ Engagement
≠ Appointment
```

The records may reference one another while preserving separate lifecycles and authorities.

## Minimum necessary disclosure

The destination should receive only the information required for the accepted purpose.

Possible controls include:

- field selection;
- document selection;
- redaction;
- temporary links;
- watermarking;
- download restrictions;
- retention limits;
- onward-sharing limits;
- training-use prohibition.

```text
Recipient needs the work
≠ Recipient needs the entire customer history
```

Customer data access does not create permission for direct contact or relationship ownership.

```text
Customer Data Access
≠ Customer Contact Permission
≠ Relationship Ownership
```

## Handoff packages must remain versioned

A Handoff may include applicant data, goods, documents, fees, instructions and deadlines. Material changes require a new version or explicit amendment.

```text
New Attachment Sent
≠ Prior Instruction Automatically Superseded
```

The recipient must know:

- what changed;
- what remains valid;
- whether work should stop;
- whether prior output can still be used;
- whether Review or Approval must be repeated.

## Return carries result and evidence inward

Return answers:

> What did the destination produce, observe, attempt or receive, and what evidence now comes back to the origin?

Return types may include:

```text
Contribution Return
Provider Acknowledgement
Operational Status Return
Official Acknowledgement
Document Return
Payment Return
Error Return
Unknown Return
Correction Request
```

A Return contract should preserve:

- originating Handoff or Assignment;
- destination actor and represented role;
- input and package version;
- action attempted;
- result claimed;
- output artifact;
- evidence and external reference;
- time;
- cost or fee evidence;
- limitations;
- Unknowns;
- validation status.

## Return is not accepted truth

```text
Return Received
≠ Return Validated
≠ Outcome Accepted
≠ Formal State Updated
```

The origin or applicable Owning Service validates whether the Return satisfies the declared contract.

A provider may return “filed,” while the package differs from the approved version or lacks an official receipt. A contributor may return a translation that is complete but unsuitable for the declared legal purpose.

```text
Producer reports completion
≠ Origin accepts required outcome
```

## Evidence Return contract

The expected evidence should be defined before the destination acts.

For a trademark filing, the contract might require:

- official application number;
- filing date and time;
- filed mark;
- applicant;
- filed classes and goods;
- official acknowledgement;
- fee receipt;
- provider identity;
- deviations from the approved package.

For a document review, it might require:

- reviewed version hash;
- identified defects;
- reviewer identity and authority;
- decision and limitations;
- revision instructions.

```text
“Done”
≠ Evidence Return contract satisfied
```

## Unknown Return must be supported

External systems and people can produce uncertain outcomes:

- timeout;
- silence;
- partial receipt;
- contradictory status;
- payment debited but not confirmed;
- portal unavailable;
- provider says completed but evidence missing.

```text
Unknown
≠ Success
≠ Failure
≠ Permission to Retry
```

Book 03 governs reconciliation and retry. Book 02 ensures the shared Return contract can represent uncertainty without coercing it into a clean status.

## Corrections and late Returns

A Return may arrive after reassignment, cancellation or a later Return. It should not overwrite newer records automatically.

The platform should preserve:

- arrival time;
- action time;
- related package version;
- supersession relationship;
- conflict with other Returns;
- whether reconciliation is required.

```text
Latest Return received
≠ most authoritative Return
```

A late official receipt may be more authoritative than an earlier provider report, while an old provider update may be stale despite arriving last.

## Handoff cancellation is not external reversal

Cancellation may stop future internal work, but the destination may already have acted.

```text
Handoff Cancelled
≠ External Effect Reversed
```

The origin must determine:

- whether the destination accepted;
- whether an external action occurred;
- whether documents or funds are held;
- whether a withdrawal or correction is possible;
- whether customer communication is required.

## Provider replacement

Before replacing a provider, the platform must assess:

- acceptance state;
- work already performed;
- official or financial effect;
- original-document custody;
- duplicate-action risk;
- outstanding fees;
- authority revocation;
- customer and deadline impact.

```text
New Provider Selected
≠ Old Provider Effect Ended
```

The replacement Handoff should reference the prior route and preserve reconciliation obligations.

## Product-to-Product Handoff

Lite may hand a validated service signal to MarkReg. MarkReg may hand an external instruction package to a provider network. A Knowledge workflow may return accepted Claims to a Product.

The Handoff should transfer only the context needed for the next responsibility.

```text
Product Handoff
≠ Customer Transfer
≠ Formal-state Transfer
```

The source Product may remain Relationship Owner while the destination becomes Delivery Owner for a bounded scope.

## AI and automation

AI may prepare a Handoff package, classify a Return or identify missing evidence. It cannot create disclosure authority, provider appointment or acceptance.

```text
AI Generated Handoff
≠ Handoff Approved

AI Classified Return as Success
≠ Formal Success Established
```

Automated processing should preserve model, rule, source, package version and human disposition where material.

## Candidate status

Handoff and Return are existing shared mechanisms. Instruction Package, Evidence Return and Provider Appointment may remain profiles or candidate specializations rather than new universal root objects.

## Constitutional rule

```text
Handoff transfers bounded context and responsibility outward.
Return carries typed result and evidence inward.

Neither creates acceptance, ownership,
professional authority, external effect
or formal state by implication.
```
