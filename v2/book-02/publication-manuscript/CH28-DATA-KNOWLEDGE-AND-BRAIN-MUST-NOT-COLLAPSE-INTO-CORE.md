# CH28 — Data, Knowledge and Brain Must Not Collapse into Core

## Shared intelligence requires separation, not one giant truth system

MarkOrbit needs a coherent path from source material to useful action.

A simplified description may look like:

```text
Source
→ Data
→ Knowledge
→ Brain
→ Product or Execution
→ Formal Outcome
```

The sequence is useful only when each layer keeps its own responsibility.

If all layers collapse into one central object store, the platform can no longer answer:

- whether a value came from an official source or an inference;
- whether a Claim was reviewed;
- whether a Recommendation was approved;
- whether a customer fact may be reused;
- which service may correct the formal record;
- which version of a model or dataset produced the result;
- whether a downstream Product owns or merely references the information.

Book 02 therefore establishes the following constitutional boundary:

```text
Core
≠ Data Store
≠ Data Refinery
≠ Knowledge Repository
≠ Brain Runtime
≠ Formal-state Owning Service
```

Core defines the shared language that lets these layers interoperate. It does not absorb their content, operations or authority.

## The responsibility map

A durable platform can summarize the layers as follows:

| Layer | Primary responsibility | Does not automatically own |
| --- | --- | --- |
| Core | shared semantics, identifiers, contracts, compatibility and authority distinctions | every record, database, workflow, Claim or model result |
| Data | source capture, structured records, provenance, transformation, quality and versioned Data Products | customer relationship, professional interpretation or formal business state |
| Knowledge | Sources, Documents, Claims, Versions, Citations, Links and review state | official authority, customer decisions or universal truth |
| Brain | typed retrieval, inference, recommendation, candidate and explanation results | canonical facts, Approval, professional authority or formal-state mutation |
| Product | audience experience, commercial promise, entitlement and capability composition | every referenced object or underlying semantic definition |
| Execution | governed work coordination, Review, Approval, Apply, Return and reconciliation | Customer, Order, Matter, Payment or official truth by default |
| Owning Service | validation and mutation of a declared formal business object | unrelated objects and platform-wide semantics |

The table is not a deployment prescription. One technical service may host more than one responsibility during an early implementation. The semantic boundaries must still remain visible.

```text
same codebase
≠ same authority
```

## Core is the grammar, not the library

Core may define:

- a stable reference envelope;
- source and provenance fields;
- epistemic status vocabulary;
- Evidence and Citation links;
- versioning and compatibility rules;
- authority references;
- Projection, Handoff and Return contracts;
- candidate-before-Canonical behavior.

Core should not contain:

- every trademark record;
- every source document;
- every Knowledge Claim;
- every embedding or retrieval index;
- model prompts and tool chains;
- provider-specific practices;
- Product ranking weights;
- customer-specific memory;
- volatile pipeline internals.

```text
shared contract
≠ centralized content ownership
```

The distinction keeps Core stable while Data, Knowledge and Brain evolve quickly.

## Data answers what was recorded and transformed

Data preserves:

- source records;
- structured records;
- identifiers;
- transformation history;
- quality metrics;
- candidate records;
- versioned releases.

Data is strongest when the platform asks:

> What did the source contain, how was it processed and which release exposed it?

Data is not sufficient by itself to answer:

> What does the rule mean for this customer, which route is preferable or may we perform the protected action?

```text
structured data
≠ interpreted knowledge
≠ authorized decision
```

## Knowledge answers what is being asserted and supported

Knowledge preserves:

- who or what the source is;
- which document was captured;
- what Claims are being made;
- what evidence supports or contradicts them;
- which version applies;
- how the Claim was reviewed and cited.

Knowledge is strongest when the platform asks:

> What proposition is supported, under which source, jurisdiction, period and review state?

Knowledge does not answer by itself:

> Which action did the customer authorize, which actor is eligible or did the official state change?

```text
accepted Knowledge Claim
≠ Customer Instruction
≠ Apply Authority
≠ Formal State
```

## Brain answers a context-specific reasoning question

Brain uses Data and Knowledge to answer questions such as:

- which sources are relevant;
- what may be inferred;
- which options should be compared;
- what record or route should be considered;
- how a complex result can be explained.

Brain is strongest when the platform asks:

> Given this declared context, what retrieval, inference, recommendation, candidate or explanation can assist the next governed decision?

Brain does not become canonical because it is interactive, fluent or highly capable.

```text
Brain Result
≠ Knowledge Claim by default
≠ Decision
≠ Formal State
```

## The correct flow is governed promotion, not silent copying

A safe route may be expressed as:

```text
Source Record
→ Structured Data Record
→ Knowledge Claim Candidate
→ Reviewed Knowledge Version
→ Typed Brain Result
→ Contribution or Decision Candidate
→ Review and Approval
→ Governed Apply
→ Evidence Return
→ Owning Service Formal-state Validation
```

Every arrow represents a change of purpose or authority. The system should record the actor, version, evidence and acceptance rule applied at that boundary.

The path is not mandatory for every low-risk record. It is a semantic map showing that later states cannot be assumed from earlier ones.

## Collapse failure 1: the central truth database

A central truth database tries to store one current value for everything.

It creates problems when:

- official records and provider reports conflict;
- source data is stale;
- AI produces an alternative interpretation;
- customer facts differ by Matter;
- products require different purpose-limited views;
- historical decisions relied on earlier versions.

The database may overwrite uncertainty with a clean field.

```text
one current value
≠ one uncontested truth
```

Core should support references, candidates, conflicts and versioned acceptance rather than force every layer into one mutable row.

## Collapse failure 2: the Knowledge repository becomes Core

A large Knowledge system may appear to define the platform because it contains laws, procedures, provider practices and internal methods.

But Knowledge content is more volatile than Core semantics.

A fee Claim can change tomorrow. A provider practice can change by office or practitioner. A Markdown structure can be replaced. A retrieval strategy can improve.

Core should define how Sources, Claims, Versions and Citations are referenced where stable interoperability requires it. It should not freeze every Knowledge schema or content item into the constitutional layer.

```text
Knowledge importance
≠ Core ownership
```

## Collapse failure 3: Brain output becomes Knowledge automatically

Brain can produce useful summaries and insights at high speed. Automatically storing every result as shared Knowledge creates:

- duplicated and contradictory Claims;
- stale model-generated content;
- customer-data leakage;
- uncertain source lineage;
- self-reinforcing errors;
- training contamination;
- unclear professional responsibility.

A Brain result may become a reusable Knowledge Candidate only through a controlled promotion route.

```text
Brain Result accepted for one task
≠ reusable shared Knowledge
```

Promotion may require source review, de-identification, rights review, professional validation and explicit approval.

## Collapse failure 4: Core becomes the workflow engine

Once Core defines the shared objects, an implementation may be tempted to place eligibility, assignment, review, approval, tool invocation and retries inside Core.

That would mix stable semantics with volatile execution policy.

Book 03 owns governed execution. Core may define the references Execution exchanges, but it does not run the whole workflow.

```text
Core contract
≠ Execution runtime
```

This permits different Products and Workplaces to use different implementations while preserving the same meaning.

## Collapse failure 5: Product views become duplicate truth stores

Lite, MarkReg and Sites may cache or project data for performance and user experience.

A Product-local copy must preserve:

- source reference;
- version;
- purpose;
- freshness;
- correction path;
- permitted actions.

```text
display copy
≠ new authoritative record
```

When a source changes, the Product should refresh or mark the Projection stale rather than silently diverge.

## Versioning must remain independent across layers

Data, Knowledge, Brain and Core change for different reasons.

```text
Core Contract Version
Data Product Version
Knowledge Version
Brain Policy or Model Version
Product Version
Workflow Version
```

These versions should be linked but not forced to move together.

A model upgrade may not require a Core change. A new Data Product release may not invalidate the Knowledge Version if the relevant records are unchanged. A Core reference change may require migration even when the content itself is stable.

```text
one layer changed
≠ every layer silently upgraded
```

Consumers need compatibility declarations and impact analysis.

## Authority remains separate through the whole stack

At every layer, the platform must preserve:

- business sovereignty;
- semantic authority;
- formal-state authority;
- physical custody;
- legal, evidentiary and professional authority.

Examples:

- Data may physically store an official record without becoming the official authority;
- Knowledge may cite a legal rule without becoming the qualified professional adviser;
- Brain may recommend a filing route without becoming the customer's decision maker;
- Core may define Professional Authority references without issuing a licence;
- Execution may coordinate a filing without owning the official Matter state.

```text
access to information
≠ authority to act on it
```

## Purpose and rights must survive movement between layers

A record may move through Data, Knowledge, Brain and Product contexts. Its rights and purpose do not disappear.

The platform should preserve:

- original acquisition basis;
- customer or source confidentiality;
- permitted Product and Workplace use;
- retention;
- redistribution;
- cross-border restrictions;
- AI use;
- model-training permission;
- withdrawal and deletion obligations.

```text
operational access
≠ shared Knowledge permission
≠ AI-training permission
```

The transition into a different layer is a new use decision, not an automatic extension of the original permission.

## Customer-specific context must not leak into shared intelligence

Matter and customer context may contain:

- identity documents;
- instructions;
- commercial priorities;
- private legal positions;
- communication history;
- provider disputes;
- payment information.

Brain may use this information for the authorized task. It should not automatically enter shared Knowledge or another customer's context.

```text
Pattern Reuse
≠ Customer-content Reuse
```

Reusable learning should be separately governed, validated and de-identified where appropriate.

## Formal-state changes remain at the end of a governed route

No upstream intelligence layer should mutate formal state simply because it has strong evidence.

The route remains:

```text
Data or Knowledge Evidence
→ Brain or Human Analysis
→ Contribution
→ Typed Review
→ Specific Decision or Approval
→ Apply where required
→ Return and Reconciliation
→ Owning Service Validation
→ Formal-state Mutation
```

```text
strong evidence
≠ mutation authority
```

The Owning Service decides whether the evidence satisfies its formal-state contract.

## Corrections need cross-layer impact analysis

When an error is found, the platform should identify where it originated.

```text
Source Error
Extraction Error
Normalization Error
Claim Error
Citation Error
Inference Error
Recommendation Error
Decision Error
Projection Error
Formal-state Error
```

The correction should target the correct layer and then trace affected downstream objects.

A source correction may require Data reprocessing, Knowledge versioning, Brain-result invalidation, Product refresh and formal-state review. It should not be handled by overwriting the final display and leaving the causal chain unchanged.

## Observability must reconstruct the path

For consequential use, the platform should be able to reconstruct:

- source and Data Product version;
- Knowledge Claims and Citations;
- Brain result type and model or policy version;
- Product or Execution context;
- Contribution, Review and Approval;
- applied payload;
- Return and reconciliation;
- formal-state validation.

```text
final value visible
≠ decision path reconstructable
```

Observability supports correction, professional responsibility and safe learning.

## Business value of separation

The separation is not only technical governance. It enables:

- reuse of the same Data Product across Products;
- source-backed public and customer content;
- replacement of models without rewriting formal records;
- independent improvement of retrieval and Knowledge workflows;
- white-label and multi-Workplace sovereignty;
- safer external-provider collaboration;
- correction propagation;
- auditable AI-assisted professional work;
- future commercialization of governed Data and Capability products.

A platform that collapses all intelligence into one store may move faster briefly. It becomes difficult to trust, license, integrate and evolve.

## Candidate status

Book 02 v2 proposes shared contracts for Data Products, Knowledge objects and typed Brain Results. The reconciliation classifies some as existing semantics and others as F2/F3 profiles or candidates.

This chapter locks the ownership and authority boundaries. It does not activate every proposed object, prescribe a single database or require one monolithic Knowledge or Brain implementation.

## Ten-year rule

Models, storage systems, Markdown tools, vector indexes, crawling frameworks and Product interfaces will change.

The following boundary should remain stable:

```text
Core defines shared meaning.
Data preserves sourced structured records.
Knowledge preserves sourced Claims and Versions.
Brain produces typed context-specific intelligence.
Execution governs consequential transitions.
Owning Services establish formal state.
Products compose the experience.
```

## Constitutional rule

```text
Data, Knowledge and Brain may be deeply connected,
but they must not collapse into Core
or into one undifferentiated truth system.

Interoperability requires shared contracts.
Trust requires separate provenance,
authority, lifecycle, purpose and ownership.
```
