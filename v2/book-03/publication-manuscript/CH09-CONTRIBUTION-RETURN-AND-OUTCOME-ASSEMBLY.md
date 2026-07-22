# CH09 — Contribution, Return and Outcome Assembly

## 1. Work does not become an outcome merely because somebody submitted something

A governed execution system must distinguish between what a performer produced, what an external provider returned, what the review process accepted, what the Delivery Owner assembled and what the Owning Service finally recognized.

The minimum chain is:

```text
Assignment or Invocation
→ Contribution or Provider Return
→ Validation
→ Review
→ Revision or Acceptance
→ Outcome Assembly
→ Delivery Decision
→ Formal-state Update by the Owning Service
```

These transitions cannot be collapsed into one status called `done`.

```text
Contribution Submitted
≠ Contribution Accepted
≠ Work Package Complete
≠ Outcome Assembled
≠ Customer Delivered
≠ Formal State Updated
```

The distinction matters because professional work is frequently partial, conditional, multi-source and version-sensitive. A researcher may return accurate source material but no professional conclusion. An AI may produce a useful draft but omit an exception. A provider may report that an application was filed but fail to return an official receipt. A reviewer may accept the reasoning while requiring the evidence appendix to be replaced.

Execution must preserve those differences instead of hiding them behind a single completion flag.

## 2. Contribution is the internal production return

A `Contribution` records a bounded piece of work returned under an Assignment or governed invocation.

It should identify at least:

- the Assignment or Capability Request;
- the performer;
- represented Workplace and role;
- Capability and version;
- Implementation Binding;
- human–AI collaboration mode;
- input references and exact versions;
- sources consulted;
- tools, scripts or models used;
- output artifact or structured result;
- assumptions;
- uncertainty;
- exclusions;
- evidence supplied;
- submission time;
- revision relationship to earlier Contributions.

A Contribution is not necessarily a document. It may be:

- a normalized data object;
- a deadline calculation;
- a source comparison;
- an image-quality assessment;
- a translated passage;
- a proposed filing package;
- a professional issue classification;
- a communication draft;
- a provider candidate set;
- a structured exception report.

The governing principle is:

```text
Contribution
= attributable production under defined scope
```

It is not:

```text
Contribution
= authority to decide the Matter
```

## 3. Provider Return is a different object

A `Provider Return` is the return from an appointed external professional provider or provider organization.

It may contain:

- acceptance of appointment;
- confirmation of instructions;
- fee request;
- filing receipt;
- official application number;
- office notice;
- professional interpretation;
- status report;
- registration certificate;
- courier record;
- invoice or refund statement.

Provider Return is different from Contribution because the provider may operate under a separate contract, local professional authority and external accountability structure.

```text
Contributor Assignment
≠ Provider Appointment

Contribution
≠ Provider Return
```

But Provider Return is still not automatically official truth.

```text
Provider Reports Filed
≠ Official Filing Verified

Provider Reports Registered
≠ Official Registration Verified
```

The originating Product or Owning Service must validate the returned evidence according to its Evidence Contract.

## 4. Return contracts must be specified before work begins

Every Work Package and Provider Appointment should define what must be returned.

An Evidence or Return Contract may require:

- exact output format;
- mandatory fields;
- source references;
- official receipt;
- proof of payment;
- version identifier;
- document checksum;
- provider statement;
- uncertainty disclosure;
- rejected-item explanation;
- customer-delivery artifact;
- correction obligation.

Without a defined Return Contract, the system cannot distinguish between a complete result and a polite but insufficient reply.

For example:

> Filed successfully.

may not satisfy a filing Return Contract if it lacks:

- official application number;
- filing date;
- filed mark representation;
- filed goods and classes;
- official fee receipt;
- official acknowledgement.

```text
Provider Says “Done”
≠ Return Contract Satisfied
```

## 5. Submission state must preserve version and lineage

Every Contribution and Return must remain attached to the input and package versions on which it was based.

```text
Contribution for Package v1
≠ Contribution for Package v2
```

A later change to:

- applicant identity;
- mark image;
- goods;
- filing basis;
- evidence;
- provider;
- jurisdiction;
- deadline;
- legal argument;

may make an earlier Contribution unusable or only partially reusable.

Execution should record relationships such as:

```text
Supersedes
Corrects
Expands
Narrows
Responds To Review
Derived From
Conflicts With
```

History must remain visible. Replacing a file must not erase the earlier production record.

## 6. Validation precedes professional Review

Validation asks whether the returned material satisfies formal and technical requirements.

Typical validation checks include:

- required artifact exists;
- expected schema is satisfied;
- all mandatory fields are present;
- file is readable;
- source links resolve;
- checksum matches;
- output corresponds to the assigned object;
- submission occurred before deadline;
- prohibited data is absent;
- exact version is identifiable.

Validation does not decide whether the professional reasoning is correct.

```text
Technically Valid
≠ Professionally Correct
≠ Approved
```

A perfectly structured OA response can still contain weak legal reasoning. A valid filing receipt may still reveal that the wrong goods were filed.

## 7. Contributions can be accepted in different ways

Acceptance should not be represented only as yes or no.

Useful states include:

```text
Accepted
Accepted with Limitation
Partially Accepted
Revision Required
Rejected for Defined Failure
Superseded
Cancelled because Inputs Failed
Unknown — Review Incomplete
```

An accepted limitation must be explicit. For example:

- source research accepted, legal conclusion not accepted;
- translation accepted, transliteration pending;
- visual comparison accepted for triage only;
- draft accepted for customer discussion, not for filing;
- provider report accepted as a lead, official verification pending.

```text
Accepted for Triage
≠ Accepted for Filing
≠ Accepted as Formal Truth
```

## 8. Revision must preserve responsibility

A revision request should state:

- which finding triggered revision;
- whether scope changed;
- whether the problem was performer error, missing input or new customer instruction;
- the exact version to revise;
- required changes;
- new deadline;
- whether additional compensation applies;
- whether earlier review remains valid.

```text
Revision Requested
≠ Performer Fault Proven
```

If the customer adds new facts or the official rule changes, the revision is not necessarily a quality failure by the original performer.

## 9. Outcome Assembly integrates typed Contributions

Many professional outcomes require multiple Contributions.

An application package may need:

```text
Identity Verification
+ Mark Representation Check
+ Goods Normalization
+ Translation Review
+ Document Readiness
+ Fee Calculation
+ Professional Review
= Filing Package Candidate
```

A trademark transaction may need:

```text
Official-right Verification
+ Chain-of-title Review
+ Commercial Terms
+ Contract Documents
+ Payment Evidence
+ Recordal Package
= Closing Outcome Candidate
```

Outcome Assembly must not average contradictory professional views. It must retain typed findings and resolve them through accountable synthesis.

```text
Multiple Contributions
≠ Collective Approval
```

## 10. Delivery Owner is accountable for assembly

The Delivery Owner ensures that:

- required Work Packages exist;
- Contributions correspond to the correct versions;
- mandatory Reviews are complete;
- conflicts are resolved or exposed;
- Unknowns are not hidden;
- customer decisions are obtained;
- Evidence Contract requirements are satisfied;
- the assembled Outcome is coherent;
- no Protected Action occurs without authority.

The Delivery Owner may coordinate the result without possessing every specialist qualification.

```text
Delivery Ownership
≠ Universal Professional Authority
```

Where a final legal or jurisdiction-specific judgment is required, the qualified reviewer or Professional Authority must remain identifiable.

## 11. Outcome is a governed result object

An `Outcome` should contain:

- originating Capability Request or Workflow;
- applicable Work Packages;
- accepted Contributions;
- relevant Provider Returns;
- Review and Approval records;
- unresolved limitations;
- evidence;
- customer-facing result;
- Owning Service handoff;
- expiry or revalidation conditions.

Possible Outcome types include:

- recommendation;
- validated data object;
- decision-ready option set;
- approved package;
- execution result;
- official-result candidate;
- customer-delivery package;
- recovery plan;
- no-safe-route result.

```text
Outcome
≠ Always Success
```

A valid Outcome may be:

> No safe filing route can be recommended until applicant identity and priority evidence are resolved.

This is more trustworthy than manufacturing a positive answer.

## 12. Outcome Assembly does not mutate formal state

Execution may assemble an official-result candidate, but the Owning Service decides whether the evidence is sufficient to update its formal object.

```text
Outcome Assembled
→ Owning Service Validation
→ Formal-state Mutation
```

Execution must not silently rewrite:

- Customer;
- Order;
- Matter;
- Payment;
- Trademark Right;
- Provider Appointment;
- Official Status.

```text
Execution Outcome
≠ Formal Business Truth
```

## 13. Customer delivery is a separate transition

A professionally accepted Outcome is not automatically delivered to the customer.

Customer delivery may require:

- Relationship Owner review;
- branded formatting;
- explanation of limitations;
- translation;
- fee reconciliation;
- communication approval;
- attachment validation;
- acknowledgement tracking.

```text
Outcome Accepted
≠ Customer Delivered

Message Sent
≠ Customer Understood
```

The customer-facing result should state what was done, what was not done, what remains Unknown and what next action is required.

## 14. Outcome may expire

Some Outcomes remain valid only while their inputs and sources remain current.

Examples include:

- provider eligibility;
- official fee calculation;
- deadline calculation;
- search result;
- filing readiness;
- recommendation based on current customer priorities;
- content publication approval.

Execution should record:

```text
Valid Until
Recheck Trigger
Source-change Trigger
Matter-change Trigger
Superseded By
```

```text
Accepted Once
≠ Valid Forever
```

## 15. Failure and Unknown must survive assembly

Outcome Assembly must not convert missing information into positive certainty.

An assembled result can preserve:

- unresolved source conflict;
- missing original document;
- provider non-response;
- unverified official status;
- disputed applicant identity;
- incomplete payment reconciliation.

```text
Outcome Complete as a Record
≠ Underlying World Fully Resolved
```

## 16. AI may assemble but cannot silently decide

AI can assist by:

- grouping Contributions;
- detecting conflicts;
- comparing versions;
- generating summaries;
- identifying missing evidence;
- preparing a draft Outcome;
- explaining alternatives.

AI must retain:

- model provenance;
- source references;
- uncertainty;
- which findings came from humans, providers or deterministic tools;
- required human disposition.

```text
AI-generated Outcome Draft
≠ Reviewed Outcome
≠ Approved Outcome
≠ Formal-state Mutation
```

## 17. The governing chain

The trusted production chain is:

```text
Bounded Assignment
→ Attributable Contribution or Provider Return
→ Validation
→ Typed Review
→ Specific Acceptance
→ Outcome Assembly
→ Delivery Decision
→ Formal-state Validation
```

This chain is the point at which MarkOrbit stops being a collection of tasks and becomes a professional execution system.