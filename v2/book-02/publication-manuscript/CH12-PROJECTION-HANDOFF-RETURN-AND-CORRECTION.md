# CH12 — Projection, Handoff, Return and Correction

## Shared systems need controlled movement without silent ownership transfer

MarkOrbit is not one application with one database and one operating organization. Products, Workplaces, Execution, Knowledge, Owning Services and external providers must exchange context while preserving sovereignty and authority.

Four shared mechanisms are especially important:

```text
Projection
Handoff
Return
Correction
```

They solve different problems and must remain distinct.

```text
Projection
≠ Handoff
≠ Return
≠ Transfer
≠ Formal-state Mutation
```

## Projection is a governed view

Projection answers:

> What purpose-limited view may another Product, Workplace or actor see from an authorized source context?

A Projection should preserve:

- source object and version;
- projecting Workplace or service;
- recipient context;
- purpose;
- visible fields;
- redactions;
- permitted actions;
- onward-sharing policy;
- effective period;
- revocation and correction behavior.

Projection can support discovery, collaboration, service delivery or public communication without duplicating the source object's authority.

```text
projected record visible
≠ source object transferred
≠ recipient may mutate source state
```

Examples include:

- Lite displaying a trademark status supplied by a Data or Matter service;
- MarkReg displaying customer context from the originating Workplace;
- Sites publishing an approved service or trademark projection;
- MGSN exposing a minimum-necessary Capability Need Projection to candidate providers.

## Projection classes are profiles, not separate roots

Demand, Capability, Asset, Audience and Capacity Projections can use one shared semantic mechanism with different profiles.

A Demand Projection may show the outcome required without revealing the customer identity. A Capability Projection may show a provider's eligible scope without exposing private assessment records. An Asset Projection may show a trademark Listing without transferring title or resale authority.

```text
Asset Projection
≠ ownership proof
≠ Resale Authorization
```

The profile determines fields and policy; the underlying Projection contract preserves purpose and source continuity.

## Handoff transfers bounded work context

Handoff answers:

> What exact context, scope and permission are being passed to another governed actor or Product for a specific next responsibility?

A Handoff should include:

- origin and destination;
- purpose;
- source and object versions;
- scope and exclusions;
- accepted facts and unresolved Candidates;
- Relationship Owner and communication rules;
- data scope;
- expected next action;
- required Review or Approval;
- acceptance state;
- Evidence Return contract;
- expiry, amendment and cancellation.

```text
Handoff sent
≠ Handoff accepted
≠ Assignment created
≠ Provider appointed
≠ external action authorized
```

A Handoff is not a generic forwarding event. It is a versioned responsibility boundary.

## Product Handoff does not transfer the customer

Lite may identify a maintenance need and hand it to MarkReg. A partner Workplace may hand a filing package to a white-label delivery team. MarkReg may hand an instruction package to MGSN.

In every case:

```text
work context transferred
≠ customer relationship transferred
```

The Handoff must preserve the originating Relationship Owner, contact permissions and represented identity unless an explicit and authorized relationship transition is recorded.

## Return carries evidence or result back to the origin

Return answers:

> What did the destination produce, observe or receive, and what evidence now returns to the originating context?

A Return may contain:

- Contribution;
- provider acknowledgement;
- official receipt;
- status report;
- document;
- error;
- Unknown outcome;
- cost or settlement evidence;
- correction request.

Return should preserve:

- originating Handoff or Assignment;
- actor and authority;
- implementation or provider;
- input version;
- output and evidence;
- completion claim;
- limitations;
- external reference;
- uncertainty;
- validation status.

```text
Return received
≠ Return accepted
≠ Outcome validated
≠ Formal State changed
```

The origin or applicable Owning Service validates the Return before relying on it.

## Why Return validation belongs at the origin

The destination may know what it attempted. The origin knows what outcome was requested and which formal object may change.

An external provider can report that it filed an application. The Matter Owning Service must compare the returned mark, applicant, goods, date and official number with the authorized package before updating formal state.

A contributor can submit a translation. The Work Package reviewer must decide whether it meets the defined purpose.

```text
producer confidence
≠ originating acceptance
```

## Correction repairs shared projections without erasing history

Correction answers:

> How is an accepted or projected record amended when new evidence shows that it was incomplete, stale or wrong?

A Correction should preserve:

- affected object and version;
- prior value;
- corrected value or Candidate;
- supporting Evidence;
- correction reason;
- actor and authority;
- effective time;
- affected Projections, Handoffs, Decisions and Outcomes;
- propagation state;
- whether external remediation is required.

```text
Correction
≠ overwrite
≠ historical erasure
```

## Source correction and projection correction are different

Sometimes the source record is wrong. Sometimes the source is correct but a Projection is stale. Sometimes a Product interpreted the source incorrectly.

The architecture should distinguish:

```text
source-record correction
projection refresh
interpretation correction
formal-state correction
external remedial action
```

A corrected source does not automatically prove that every downstream decision should be rewritten. The platform must identify which decisions relied on the prior version and whether they require review.

## Revocation and correction are not the same

Revocation ends future visibility or permission. Correction changes the accepted representation of a fact or object.

```text
Projection revoked
≠ underlying fact corrected

Fact corrected
≠ all prior access revoked
```

Both may be necessary after a privacy, identity or authority incident.

## Handoff amendments

When scope or data changes after a Handoff is accepted, the origin should issue a versioned amendment rather than an informal message.

The destination must know:

- which earlier instruction is superseded;
- what remains valid;
- whether work must stop;
- whether a new Assignment or Approval is required;
- whether already-produced work can still be used.

```text
new attachment sent
≠ prior Handoff automatically superseded
```

## Unknown Returns

External systems can time out, providers can remain silent and communications can fail.

The Return contract must support:

```text
Unknown
≠ Success
≠ Failure
≠ Safe Retry
```

Book 03 governs reconciliation and retry. Book 02 defines the shared status and reference boundaries so every Product interprets the condition consistently.

## Public Projection and correction duties

A public service page, fee table or trademark Listing is still a Projection. It requires:

- source references;
- effective version;
- approval;
- expiry or freshness policy;
- correction propagation;
- removal or replacement history.

A public page should not become an uncontrolled parallel source of professional truth.

## AI and Projection

AI may generate a projected summary or draft Handoff, but it does not create disclosure authority.

```text
AI can summarize the record
≠ AI may disclose the record
```

AI-generated Returns must preserve model, source, tool and review provenance. AI cannot validate its own output into formal state without the applicable governed route.

## Candidate status

Projection, Handoff and Return are established or reconciled shared mechanisms. Product-specific forms remain local profiles. Correction should reuse existing evidence, versioning and Owning Service governance rather than becoming an unrestricted universal mutation object.

## Constitutional rule

```text
Projection controls visibility.
Handoff transfers bounded responsibility.
Return carries evidence back.
Correction repairs accepted meaning.

None transfers ownership, authority or formal state by implication.
```
