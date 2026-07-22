# CH23 — Contribution, Review and Outcome

## Production needs three different records

A performer can submit work. A reviewer can judge it. A Delivery Owner or other authorized actor can assemble an accepted result.

These are different events.

```text
Contribution
≠ Review
≠ Outcome
```

The distinction matters because professional work is often collaborative, versioned and purpose-specific. One actor may produce a draft, another may verify the sources, a third may provide a local-law opinion, and a fourth may approve the final package for a customer decision.

Without separate semantics, the system cannot explain who produced what, who judged it, what was accepted, or whether any formal state changed.

Contribution and Outcome remain candidate shared semantics. Review is an established governance concept. This chapter explains their proposed relationship without activating new frozen Core objects.

## Contribution is attributable production

Contribution answers:

> What bounded work, artifact, opinion, verification, data transformation or other professional input did this actor or implementation produce under an authorized context?

A Contribution should preserve:

- stable identifier and version;
- originating Work Package and Assignment or equivalent authorized context;
- contributor identity and represented actor;
- Capability and implementation references;
- input references and exact versions;
- produced artifact or structured output;
- source and Evidence references;
- assumptions, limitations and Unknowns;
- tool, model and Skill versions;
- generation or completion time;
- contributor completion claim;
- data-use and reuse conditions;
- supersession and correction history.

```text
Contribution submitted
≠ Contribution accepted
≠ Work Package complete
≠ Outcome assembled
```

## Contribution is not a generic attachment

A file uploaded to a Matter may be useful, but it is not necessarily a Contribution.

A governed Contribution identifies:

- what work it represents;
- which contract it attempts to satisfy;
- who produced it;
- which inputs and Tools were used;
- which authority boundary applied;
- which Evidence supports it;
- what remains unresolved.

```text
attachment present
≠ attributable production record
```

This distinction enables review, compensation, quality learning and safe reuse.

## Contribution types

A shared contract may support typed Contributions such as:

- fact research;
- source verification;
- structured extraction;
- translation or transliteration;
- professional opinion;
- trademark similarity analysis;
- visual continuity assessment;
- filing-package preparation;
- customer communication draft;
- provider instruction package;
- document correction;
- deterministic validation result;
- AI-generated candidate;
- recovery or reconciliation finding.

The type should describe what was produced and how it may be used. It should not imply final authority.

```text
professional-opinion Contribution
≠ final Matter decision by default
```

## Human and machine Contributions

Human, AI and deterministic systems can all produce Contributions, but their provenance differs.

A human Contribution may record:

- qualification and jurisdiction;
- represented organization;
- professional role;
- source reasoning;
- signature or attestation where needed.

An AI Contribution should record:

- model and version;
- policy and prompt reference;
- source set;
- tool calls;
- memory context;
- input and output hashes;
- confidence or uncertainty indicators;
- prohibited-use limits;
- required human review.

A deterministic Contribution should record:

- rule and implementation version;
- exact inputs;
- execution result;
- validation and error state.

```text
AI Contribution
≠ AI authority

Deterministic result
≠ source rule verified
```

## Corrections and revisions

A revised Contribution should not overwrite the earlier version.

It should preserve:

- prior version;
- review findings addressed;
- changed fields or artifacts;
- reason for revision;
- new sources or assumptions;
- whether prior review remains valid.

```text
Contribution v2
≠ Contribution v1 silently edited
```

A material change normally invalidates review bound to the previous version unless the review contract explicitly allows limited carryover.

## Review is typed judgment

Review answers:

> Did an authorized reviewer evaluate this exact object and version against a declared purpose, criteria and authority boundary, and what disposition resulted?

A Review should preserve:

- reviewed object and exact version;
- Review type;
- reviewer identity and represented actor;
- reviewer Qualification or authorization;
- purpose and criteria;
- jurisdiction and scope;
- supporting and conflicting Evidence;
- findings;
- limitations and Unknowns;
- disposition;
- conditions;
- effective time;
- invalidation conditions;
- supersession or appeal history.

```text
reviewed
≠ approved
≠ applied
```

## Review types must remain explicit

Possible Review types include:

- structural or schema review;
- source review;
- factual review;
- professional or legal review;
- jurisdiction review;
- document-form review;
- identity review;
- fee and deadline review;
- privacy and disclosure review;
- visual review;
- communication review;
- execution-readiness review;
- financial review.

```text
reviewed for formatting
≠ reviewed for legal accuracy
```

A single `reviewed=true` flag destroys the meaning needed for safe reuse.

## Review disposition

A useful controlled disposition may include:

```text
Accepted
Accepted with Conditions
Accepted for Limited Purpose
Revision Required
Additional Evidence Required
Customer Decision Required
Professional Authority Required
Escalation Required
Rejected for Defined Reason
Review Inconclusive
```

Acceptance for a limited purpose must remain visible downstream.

For example, a draft may be accepted for customer discussion but not accepted for official filing.

```text
accepted for discussion
≠ accepted for protected action
```

## Reviewer independence and role conflict

The same actor may contribute and review in some low-risk contexts, but role combination must be governed.

Potential conflicts include:

- contributor as sole final reviewer;
- AI output validated only by the same model route;
- Provider reviewing its own disputed fee;
- Payment Receiver approving its own settlement claim;
- Relationship Owner suppressing professional risk to protect conversion.

```text
same actor can hold multiple roles
≠ every role combination is acceptable
```

The Review contract should identify required independence and escalation conditions.

## Review is version-bound

```text
Contribution v1 reviewed
≠ Contribution v2 reviewed
```

Even a small change can matter where it affects:

- applicant identity;
- mark representation;
- goods and services;
- professional conclusion;
- fee or deadline;
- disclosed data;
- provider instruction;
- public statement.

The system should use object version or hash binding rather than a loose status on the containing Matter.

## Outcome is accepted result for a declared purpose

Outcome answers:

> What result has been accepted from one or more Contributions and Reviews for a specific purpose, by an actor authorized to assemble or accept that result?

A proposed Outcome should preserve:

- purpose;
- related Work Package or other request;
- included Contribution versions;
- Review records and dispositions;
- excluded or rejected Contributions;
- unresolved disagreements and Unknowns;
- acceptance authority;
- limitations;
- Evidence lineage;
- effective time;
- validity and expiry;
- permitted downstream uses;
- correction and supersession history.

```text
Outcome accepted
≠ customer approved
≠ external action performed
≠ formal state changed
```

## Outcome assembly

Complex work may involve several Contributions that cannot simply be merged into one text.

Outcome assembly should preserve:

- agreement;
- scope differences;
- source conflicts;
- professional conflicts;
- commercial tradeoffs;
- unresolved points;
- authority differences.

```text
multiple Contributions
≠ collective approval
≠ majority truth
```

A legal reviewer’s conclusion, a visual designer’s assessment and a commercial adviser’s recommendation may all be valid within different scopes. Outcome assembly must not average away their distinctions.

## Delivery Owner and Outcome

A Delivery Owner may coordinate Outcome assembly and ensure package completeness without owning every underlying authority.

```text
Delivery Owner assembles
≠ Delivery Owner supplies every professional judgment
```

The assembled Outcome should identify which parts rely on:

- customer-confirmed facts;
- official sources;
- AI inference;
- professional advice;
- provider practice;
- commercial recommendation.

## Outcome acceptance

Outcome acceptance is purpose-specific.

Possible examples include:

- accepted as an internal research result;
- accepted as a customer decision package;
- accepted as filing-ready pending customer approval;
- accepted as provider-ready instruction;
- accepted as public-content-ready pending publication approval;
- accepted as evidence sufficient for formal-state validation.

```text
Outcome accepted for one purpose
≠ accepted for every downstream purpose
```

## Outcome and Approval

Review and Outcome acceptance do not replace Approval.

A professionally reviewed filing package may still require:

- customer instruction;
- commercial approval;
- payment approval;
- data-disclosure approval;
- final professional approval;
- provider appointment.

```text
Outcome decision-ready
≠ next action authorized
```

Book 03 owns the runtime Approval and Apply sequence.

## Outcome and formal state

An accepted Outcome may support a formal-state transition but cannot perform it by implication.

```text
accepted filing Outcome
→ specific Approval
→ governed Apply
→ external Return
→ Owning Service validation
→ formal Matter state
```

A Provider Return may be one Contribution to the validation Outcome. It does not independently establish official truth.

## Rejected Contributions remain evidence

A rejected Contribution should not disappear.

It may remain relevant for:

- audit;
- dispute;
- compensation;
- training or remediation where authorized;
- quality analysis;
- explaining why another route was selected.

```text
rejected
≠ erased
≠ automatically worthless
```

Access should remain purpose-limited and privacy-aware.

## Compensation connection

Compensation may depend on:

- Assignment acceptance;
- Contribution submission;
- acceptance or rejection reason;
- revision responsibility;
- milestone completion;
- quality and deadline terms.

But Review should not be manipulated into a payment switch without contractual rules.

```text
Review finding
≠ automatic forfeiture
```

A Contribution can be rejected because the Work Package changed, the source was defective or the reviewer required a different route. Responsibility must be examined.

## Learning and quality evidence

Contribution and Review history can support capability learning, but only with context.

A useful signal should preserve:

- package difficulty;
- input quality;
- M-mode;
- R-tier;
- reviewer Qualification;
- defect type and severity;
- revision behavior;
- final Outcome;
- customer or official effect;
- recovery cost.

```text
Contribution accepted
≠ universal Capability proven
```

Operational data also does not automatically become AI-training data.

## Example: multi-jurisdiction filing route

Contributions may include:

- Data service: official owner and status records;
- AI: classification candidates and issue spotting;
- local professional: jurisdiction-specific requirements;
- commercial team: cost and route comparison;
- customer: priority and budget decision.

Reviews may include factual, professional, commercial and privacy review.

The Outcome may present several governed options rather than one false consensus.

## Example: certificate recovery

Contributions may include:

- courier tracking;
- provider correspondence;
- official register search;
- payment evidence;
- customer records.

The Outcome may be:

```text
Certificate issuance likely but original custody Unknown;
provider escalation and official verification required;
no formal receipt status update authorized yet.
```

That is a valid Outcome even though the desired certificate has not yet been recovered.

## Candidate status and admission

Contribution and Outcome are strong F3 candidates because multiple Books require stable provenance, acceptance and reuse boundaries.

Before activation, the platform must resolve overlap with:

- existing Evidence and Review records;
- document and artifact records;
- Workflow outputs;
- provider Returns;
- Matter decisions;
- formal-state transition evidence;
- assessment and credential evidence.

Field-level proposals, fixtures and migration analysis remain required.

## Constitutional rule

```text
Contribution records attributable production.
Review records typed judgment over an exact version.
Outcome records an accepted result for a declared purpose.

None automatically creates Approval,
external effect or formal state.
```
