# CH25 — Data References, Products and Refinery Ownership

## Data must be reusable without becoming ownerless

MarkOrbit depends on large volumes of trademark, applicant, owner, agent, attorney, goods, jurisdiction, status, fee, deadline and relationship data.

The platform must be able to ingest, normalize, compare, publish and reuse this information across Products. It must also preserve who supplied it, what transformation occurred, which service is responsible for it and whether it is suitable for the present purpose.

A single word such as `data` cannot carry all of those meanings.

Book 02 therefore keeps the following distinctions explicit:

```text
Source Record
≠ Structured Record
≠ Data Reference
≠ Data Product
≠ Projection
≠ Formal Business State
```

The central principle is:

```text
Core defines shared data references and contracts.
Data-owning services preserve data content, provenance and quality.
```

Core does not become the universal database merely because every Product needs shared identifiers.

## Source Record preserves what was encountered

A Source Record represents data as obtained from a declared origin.

It should preserve, where applicable:

- source identity;
- source authority class;
- source record identifier;
- jurisdiction;
- retrieval time;
- source publication or effective time;
- original representation;
- file or payload hash;
- acquisition method;
- access rights and restrictions;
- extraction status;
- known defects;
- supersession or withdrawal status.

Examples include:

- an official trademark-office record;
- a monthly data file;
- an official register page;
- a provider-supplied status report;
- a customer-uploaded company document;
- a public agent directory;
- a courier or payment return.

A Source Record preserves what the source said. It does not guarantee that the source was correct, current or authoritative for every purpose.

```text
Source Record captured
≠ proposition accepted
≠ formal state established
```

## Structured Record is a governed transformation

A Structured Record is produced when source content is parsed, normalized or mapped into a defined schema.

The transformation may include:

- encoding repair;
- field extraction;
- date normalization;
- address parsing;
- name normalization;
- classification mapping;
- language and transliteration handling;
- source-field preservation;
- duplicate-candidate detection;
- integrity checks.

The structured representation must remain linked to the source and transformation version.

```text
normalized
≠ verified
≠ canonical
```

A parser can correctly extract an incorrect source value. A normalization rule can make two distinct names look similar. A schema can omit a legally significant distinction.

The transformation history must therefore remain inspectable.

## Data Reference connects without copying authority

A Data Reference allows another Product, service or record to point to an identified data object or release.

A useful reference may contain:

- namespace;
- object type;
- stable identifier;
- owning service;
- object or release version;
- source jurisdiction;
- retrieval or effective time;
- expected resolution behavior.

The reference does not grant authority to mutate the source object.

```text
Data Reference available
≠ data ownership transferred
≠ source state editable
≠ unrestricted reuse permitted
```

Lite can reference a trademark record. MarkReg can reference the same mark in a Matter. Knowledge can cite the record. Brain can retrieve it. None of these actions changes the Data-owning service.

## Data Product is a versioned reusable contract

A Data Product is not merely a database table or exported file.

It is a governed, versioned release of structured information intended for declared consumers and purposes.

A Data Product contract may include:

- product identity and version;
- owning service or accountable publisher;
- schema and semantic references;
- source coverage;
- jurisdiction and time coverage;
- refresh cadence;
- freshness and completeness statements;
- provenance requirements;
- quality metrics;
- rights and permitted uses;
- correction and withdrawal behavior;
- compatibility policy;
- consumer expectations;
- known limitations.

Examples might include:

- a versioned official trademark-status dataset;
- an applicant-and-owner resolution candidate set;
- an agent and attorney directory product;
- a goods-and-services classification reference product;
- a deadline-candidate feed;
- a jurisdictional fee and requirement release.

```text
Data Product
≠ commercial Product
≠ database instance
≠ universal canonical truth
```

The Data Product is an information contract. Lite or MarkReg remains the customer-facing Product.

## Canonical reference does not mean universal truth

Book 02 v2 identifies shared references for concepts such as:

```text
Trademark
Applicant
Owner
Agent
Attorney
GoodsServiceItem
Jurisdiction
StatusEvent
DeadlineCandidate
EntityResolutionCandidate
```

These references allow systems to speak consistently. They do not imply that every underlying record is final or that Core owns the content.

Some objects are deliberately candidates.

```text
DeadlineCandidate
≠ verified deadline

EntityResolutionCandidate
≠ accepted identity merge
```

The applicable service or authorized reviewer must decide whether the candidate is sufficient for the intended purpose.

## Refinery is transformation governance

A Data Refinery receives source material and produces controlled structured releases.

A typical route may be described as:

```text
Acquire
→ Preserve Raw Source
→ Parse
→ Normalize
→ Validate Structure
→ Generate Candidates
→ Review or Reconcile
→ Publish Versioned Data Product
```

The Refinery should preserve:

- input source and hash;
- transformation code or rule version;
- schema version;
- records accepted, rejected and quarantined;
- quality checks;
- unresolved conflicts;
- candidate-generation method;
- manual interventions;
- publication decision;
- release and rollback history.

The Refinery is not permitted to erase ambiguity merely to produce a clean table.

```text
clean output
≠ truthful output by default
```

## Raw, normalized, candidate and accepted layers must remain distinct

A robust data pipeline should be able to distinguish:

```text
Raw Source Layer
Normalized Source Layer
Candidate Resolution Layer
Accepted Data Layer
Purpose-limited Projection Layer
```

The layers answer different questions.

The Raw Source Layer answers what was received. The Normalized Source Layer answers how it was represented consistently. The Candidate Layer answers what possible joins, deadlines, classifications or corrections were inferred. The Accepted Data Layer records what the responsible authority accepted for a specified purpose. The Projection Layer exposes only what the recipient is allowed to see and use.

```text
Candidate promoted for analytics
≠ accepted for filing
```

A name match may be adequate for statistical grouping but not for an ownership transfer. A calculated deadline may be adequate for internal monitoring but not for customer advice without professional review.

## Data Product ownership is accountability, not monopoly

The Data Product owner is accountable for:

- release integrity;
- schema and semantic alignment;
- provenance;
- quality statements;
- correction handling;
- compatibility;
- consumer communication.

Ownership does not mean that the publisher owns the legal facts represented by official records, the customer relationship associated with a record or all downstream uses.

```text
Data Product Owner
≠ owner of the represented trademark
≠ Relationship Owner
≠ official authority
```

The publisher may be responsible for the quality of its transformation while the trademark office remains authoritative for the official register fact.

## Official data and provider reports must not be blended

A professional platform often receives several kinds of data:

```text
Official Source Data
Authoritative Professional Source
Provider-reported Practice
Customer-provided Fact
Public Web Observation
Internal Operational Record
AI-derived Candidate
```

These categories must remain visible.

A provider may report a local filing practice that is operationally useful but not an official legal requirement. A customer may confirm an address that is suitable for intake but not verified against the corporate register. An AI candidate may identify a probable deadline but not carry professional authority.

```text
same field shape
≠ same authority
```

## Freshness is part of the contract

Trademark status, fees, forms, filing requirements, contact details and provider practices change.

A reusable data record should preserve:

- source date;
- retrieval date;
- effective period;
- last verified time;
- freshness policy;
- recheck trigger;
- stale or conflicted status.

```text
previously correct
≠ currently correct
```

Consumers must be able to determine whether a Data Product release remains suitable for a current decision.

## Corrections must propagate without rewriting history

A correction may arise because:

- the source issued a correction;
- the extraction was wrong;
- a normalization rule was defective;
- two entities were incorrectly merged;
- a source became stale;
- a downstream Product interpreted the field incorrectly.

The correction process should identify:

- affected source and release versions;
- corrected value or candidate;
- evidence and authority;
- affected Data Products;
- affected Projections, Handoffs and Decisions;
- consumers requiring notification;
- whether a formal business record needs separate correction;
- rollback or reprocessing requirements.

```text
Data Product corrected
≠ every downstream formal state silently rewritten
```

An Owning Service must determine whether its formal record should change and preserve its own correction evidence.

## Rights and permitted use travel with the data

Acquisition does not eliminate source rights, confidentiality or purpose restrictions.

A Data Product should carry or reference:

- licensing basis;
- public or restricted status;
- permitted purposes;
- redistribution rules;
- retention;
- cross-border restrictions;
- customer confidentiality;
- model-training permission;
- deletion or withdrawal obligations.

```text
Data accessible for delivery
≠ Data authorized for redistribution
≠ Data authorized for AI training
```

De-identification may reduce risk but does not automatically create a new right to train, publish or resell.

## Cross-book use

### Book 03 — Execution

Execution may request, validate and use Data References, but it does not own the Data Product or silently promote candidates into formal state.

```text
Data available to Workflow
≠ formal fact accepted
```

### Book 05 — MarkReg

MarkReg consumes trademark, owner, deadline, provider and requirement data to support lifecycle services. MarkReg-specific filing packages, customer decisions and Matter state remain Product or Owning Service records.

### Book 06 — Lite

Lite may project trademark supply, status signals, content inputs and commercial opportunities. Public source data does not automatically create a Customer, consent or relationship.

### Knowledge and Brain

Knowledge may cite Data Products and turn records into sourced Claims. Brain may retrieve and reason over them. Neither process changes the source record or Data Product release.

## Candidate status

The reconciliation classifies Data Product as an F2/F3 versioned product-reference concept. Canonical data content remains Data-owned.

This chapter explains the contract and ownership boundary. It does not activate a new universal Data Product object or prescribe one storage engine, file format or pipeline implementation.

## Constitutional rule

```text
Data services preserve source, transformation,
quality, rights and release responsibility.
Core preserves shared references and contracts.
Products consume governed data.
Owning Services decide formal state.

Refinement never grants the Refinery
universal ownership or authority over the facts represented.
```
