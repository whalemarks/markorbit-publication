# CH21 — Work Package as a Bounded Work Contract

## Why professional work needs a contract smaller than the Matter

A Matter can last for years. A Workflow can coordinate many branches. A Product Task can be little more than a user-interface prompt. A Step may be too small to carry accountability.

Professional delivery therefore needs a bounded unit that can be understood, assigned, reviewed, accepted, compensated and audited without pretending that it represents the entire Matter.

Book 02 uses **Work Package** for that purpose.

```text
Work Package
≠ Matter
≠ Order
≠ Workflow
≠ Step
≠ Product Task
```

Work Package remains a candidate shared semantic. This chapter explains the proposed contract without activating it in frozen Core.

## The central definition

A Work Package is a versioned agreement about one bounded production outcome.

It answers:

> What exact result must be produced, from which inputs, for which purpose, within what authority and data limits, by what deadline, under what review and acceptance rules?

The package is smaller than the professional subject and larger than an isolated operation.

```text
Matter
→ one or more Work Packages
→ one or more Contributions
→ Review
→ accepted Outcome where authorized
```

A Work Package is not proof that the work was performed. It is the contract against which performance can be evaluated.

## Minimum semantic envelope

A proposed Work Package should preserve at least:

- stable identifier and version;
- originating Workplace and Product context;
- related Need, Opportunity, Engagement, Order or Matter references;
- objective and declared purpose;
- required output contract;
- input references and exact versions;
- known facts, Candidates, assumptions and Unknowns;
- scope and explicit exclusions;
- jurisdiction, language and professional context;
- eligibility requirements;
- authority ceiling;
- data visibility and reuse limits;
- allowed Tools or implementation classes;
- M-mode and maximum R-tier where applicable;
- deadline and dependency conditions;
- review policy;
- acceptance criteria;
- Evidence Return contract;
- compensation or settlement reference where applicable;
- amendment, suspension, cancellation and expiry rules.

A package missing these elements may still be a useful local task, but it should not be treated as a governed professional work contract.

## Objective is not enough

The statement “prepare the filing” is too broad.

It does not say:

- which mark version;
- which applicant;
- which jurisdiction;
- which classes and goods;
- whether search advice is included;
- whether official filing is included;
- who may approve changes;
- what evidence must be returned;
- what counts as acceptance.

A bounded Work Package might instead be:

> Prepare a decision-ready United States filing package for the specified applicant and mark version, using the approved goods list, preserving unresolved translation issues, and returning a package suitable for R2 professional review. Official submission is excluded.

```text
clear objective
+ bounded inputs
+ explicit exclusions
+ acceptance contract
= governable work
```

## Output contract

The output contract should describe the result semantically, not merely name a file.

A package may require:

- structured data;
- a reviewed document;
- a source-backed analysis;
- a corrected asset;
- a verified identity record;
- a provider instruction package;
- a decision-ready option set;
- a validated Evidence bundle.

```text
PDF created
≠ output contract satisfied
```

The file format is a representation. The contract should identify required contents, provenance, limitations, review state and machine-readable references where needed.

## Scope and exclusions

Professional disputes often begin with unstated exclusions.

A Work Package should explicitly say whether it includes:

- professional advice;
- customer communication;
- translation;
- source verification;
- legal search;
- fee quotation;
- Provider selection;
- official submission;
- payment initiation;
- post-filing monitoring;
- revision rounds.

```text
not excluded
≠ automatically included
```

At the same time, exclusions must not contradict the promised outcome. A package cannot promise a professionally reliable filing route while excluding every form of source and professional review.

## Inputs must remain versioned

A Work Package should bind exact versions of:

- customer instruction;
- applicant identity;
- mark image;
- goods and services;
- supporting documents;
- fee schedule;
- applicable rule source;
- prior Contribution or Decision.

If an input changes materially, the system should determine whether the existing package remains valid.

```text
new input uploaded
≠ existing Work Package automatically updated
```

Material change may require:

- package amendment;
- new review;
- revised deadline;
- reassignment;
- new commercial approval;
- invalidation of prior Contributions.

## Known facts, Candidates and Unknowns

The package must not present every input as equally established.

It should distinguish:

```text
accepted Fact
source-derived Candidate
AI Inference
default Assumption
professional Recommendation
Unknown
```

A performer should know whether the applicant address is verified, customer-confirmed, extracted from a document or merely inferred from prior records.

```text
input available
≠ input authoritative
```

Unresolved Unknowns may be allowed for preparation but prohibited for final review or Apply.

## Eligibility requirements

A Work Package can state the class of performer or implementation needed without selecting a specific assignee.

Requirements may include:

- Capability and version;
- minimum Capability Evidence or proficiency;
- jurisdiction;
- language;
- professional Qualification;
- Production Authorization;
- conflict status;
- security clearance;
- data-access class;
- reviewer availability;
- capacity before deadline.

```text
eligibility requirements declared
≠ assignee selected
```

Book 03 remains responsible for the task-specific Eligibility decision and Assignment lifecycle.

## Authority ceiling

A package must state what the performer may and may not decide or do.

Possible boundaries include:

- may extract, not verify identity;
- may draft, not send communication;
- may recommend, not approve;
- may prepare payment instruction, not move funds;
- may assemble filing package, not submit;
- may review for document quality, not issue legal opinion.

```text
perform the package
≠ inherit every authority related to the Matter
```

Authority ceiling protects both the customer and the contributor. It prevents delivery expectations from expanding through informal messages.

## Data boundary

The Work Package should specify the minimum necessary data and permitted operations.

```text
view
≠ download
≠ edit
≠ disclose
≠ retain
≠ reuse
≠ train
```

A contributor may need the applicant name and mark image without needing the customer’s complete commercial history. An AI implementation may receive redacted inputs and be prohibited from retaining them as memory or training data.

The package should also identify data-return or deletion duties after completion.

## Deadline and dependency model

A deadline without dependencies creates false accountability.

A Work Package should distinguish:

- target completion time;
- latest safe completion time;
- hard external deadline;
- waiting-on-customer state;
- waiting-on-review state;
- waiting-on-source or Provider state;
- suspension period;
- amendment effect on deadline.

```text
calendar time elapsed
≠ performer delay by default
```

The package should preserve which party controls each dependency.

## Review policy

Review must be specified before production where possible.

The package may state:

- review type;
- reviewer qualification;
- R-tier;
- sample or full review;
- materiality thresholds;
- required source checks;
- version-binding requirement;
- revision process;
- escalation route.

```text
work produced
≠ work review-ready
≠ work accepted
```

The package should not allow the performer to redefine the required review after seeing the result.

## Acceptance criteria

Acceptance criteria should be observable and purpose-specific.

Examples include:

- required fields complete;
- all Claims linked to Sources;
- no unresolved high-risk identity conflict;
- exact mark and goods versions preserved;
- required professional review completed;
- Evidence Contract satisfied;
- prohibited actions not performed;
- output conforms to schema and presentation requirements.

A Work Package may be accepted for a limited purpose, such as customer discussion, while remaining unaccepted for filing.

```text
accepted for discussion
≠ accepted for Apply
```

## Evidence Return contract

The package should declare what evidence the performer must return with the Contribution.

This may include:

- source list;
- tool and model versions;
- transformation log;
- assumptions and Unknowns;
- decision rationale;
- changed fields;
- review notes;
- external references;
- integrity hash;
- time and actor identity.

Without this contract, the result may be useful but impossible to audit or safely reuse.

## Compensation reference

Where the package carries paid work, compensation should be linked to the governed production unit rather than to vague participation.

Possible arrangements include:

- fixed package fee;
- milestone payment;
- hourly work within a cap;
- accepted Contribution fee;
- quality or urgency adjustment;
- revision responsibility;
- cancellation payment.

```text
Work Package exists
≠ compensation automatically owed

Contribution accepted
≠ every commercial dispute resolved
```

Detailed financial policy remains with the applicable commercial and Settlement service.

## Amendments and supersession

A package amendment should preserve:

- prior version;
- changed fields;
- reason;
- approving actor;
- effect on Assignment;
- effect on Contributions and Reviews;
- deadline and compensation impact;
- whether prior work remains reusable.

```text
Work Package v2
≠ Work Package v1 silently rewritten
```

A materially different objective may require a new package rather than an amendment.

## Cancellation and suspension

Cancellation ends future production under the package. Suspension pauses performance while preserving the package and its evidence.

Neither action erases work already performed.

```text
cancelled
≠ no work occurred

suspended
≠ authority remains active for every action
```

The system must address active access, unfinished Contributions, compensation, customer deadlines and reassignment.

## Reuse across Matters

Some accepted outcomes can support more than one Matter, but the Work Package itself should not be copied without context review.

Reuse requires checking:

- purpose compatibility;
- source freshness;
- customer and data authority;
- jurisdiction;
- version continuity;
- professional review scope;
- commercial rights.

```text
reusable artifact
≠ reusable authority
```

## Example: identity verification package

A bounded package may require:

- compare customer-provided company data with official registration evidence;
- identify conflicts and aliases;
- produce an identity Candidate and Evidence table;
- exclude final applicant correction and official submission;
- require R2 review where identity conflicts affect filing.

The result can support a later filing package without itself changing the formal applicant record.

## Example: public content correction package

A package may require:

- identify the outdated public fee claim;
- locate the authoritative current source;
- draft corrected content;
- preserve prior publication version and affected pages;
- require professional and publication approval;
- exclude automatic public deployment.

The package remains distinct from the public Correction action and from Sites’ formal publication state.

## Candidate status and Core admission

Work Package is a strong F3 candidate because several independent Products and layers need a stable bounded work contract.

Before activation, the platform must still complete:

```text
frozen-baseline mapping
→ overlap analysis with Task, Workflow, Matter and Order
→ field and lifecycle proposal
→ authority analysis
→ conformance fixtures
→ migration impact
→ Owner approval
```

## Constitutional rule

```text
A Work Package defines one bounded production outcome,
its inputs, scope, authority, data, review,
acceptance and Evidence Return contract.

It does not create an Assignment,
prove completion, grant professional authority
or mutate formal state.
```
