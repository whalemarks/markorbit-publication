# B04-CH-13 — Information Access, Provenance and Context Assembly

**Status:** Draft 1  
**Chapter Map:** B04-TOC-V0.1  
**Part:** Part III — Knowledge, Intelligence and Capability Consumption

## Chapter Purpose

Part II defined the Organization Workplace as an independent operating environment.

It established:

- organization identity and active Workplace Context;
- people, roles, permissions, and accountability;
- clients, relationships, services, and business rules;
- private knowledge, preferences, AI Context, and organizational memory;
- work, review, Communication, and operating surfaces;
- data boundaries, Local Vault, and authorized synchronization.

Part III now asks a different question:

> How does Workplace consume shared information, knowledge, intelligence, capabilities, Skills, and AI assistance without losing source, authority, privacy, purpose, or professional accountability?

This chapter begins with the first layer of that question: information.

Professional work depends on access to many kinds of information:

- official records;
- laws and regulations;
- office guidelines;
- trademark databases;
- application and registration histories;
- client instructions;
- Documents and Evidence;
- Communications;
- provider responses;
- fee schedules;
- internal notes;
- private databases;
- prior Matters;
- public websites;
- acquired datasets;
- Product state;
- Event and audit trace;
- AI-extracted facts;
- local files.

Information can be useful before it becomes governed Knowledge.

It can also be incomplete, stale, duplicated, transformed, restricted, contradictory, or wrong.

Workplace therefore needs more than search.

It needs an architecture for:

```text
discovering information
→ determining whether it may be accessed
→ retrieving an authorized representation
→ preserving provenance and version
→ evaluating freshness and conflict
→ selecting only what serves the purpose
→ assembling explainable context
→ supplying that context to a human, Product, Skill, or AI Agent
→ expiring or releasing the context when the purpose ends
```

The central proposition of this chapter is:

```text
Authorized Professional Context
=
Identity
+ Organization
+ Purpose
+ Subject
+ Permitted Sources
+ Access Decisions
+ Selected Information
+ Provenance
+ Version and Time
+ Restrictions
+ Missing and Conflicting Context
+ Review Boundary
```

The constitutional distinctions are:

```text
Information access ≠ information truth

Discovery ≠ retrieval

Retrieval ≠ selection

Selection ≠ professional judgment

Context assembly ≠ unrestricted aggregation

Context package ≠ database

Context package ≠ prompt

Source citation ≠ source authority

Fresh information ≠ correct information

Structured information ≠ governed Knowledge

AI extraction ≠ verified fact

Information used ≠ conclusion reached

More context ≠ better context
```

Book 02 remains authoritative for Core Objects, Knowledge semantics, references, Permission, Policy, AI Context, and audit contracts.

Book 03 remains authoritative for governed Execution and protected-action handoff.

This chapter defines how Workplace consumes information under those authorities.

It does not redefine them.

---

## 1. Information Is the First Consumable Layer

Information is the first consumable layer between raw reality and professional understanding.

For the purposes of Workplace architecture, Information means:

> a recorded, observed, received, acquired, extracted, or derived representation that may inform professional work but does not become governed Knowledge, Evidence, a formal business fact, or a professional conclusion merely because it is available.

Examples include:

- an official status displayed on a trademark-office website;
- a downloaded XML record;
- an email from a foreign associate;
- a user-entered client instruction;
- a scanned certificate;
- a fee shown on a public page;
- a paragraph extracted from a guideline;
- a local spreadsheet;
- a crawler result;
- a Product projection;
- an AI summary;
- a deadline calculated from available dates;
- a note from a previous Matter.

Information may be:

- authoritative or unofficial;
- primary or secondary;
- public or private;
- raw or structured;
- current or stale;
- complete or partial;
- direct or derived;
- human-authored or machine-generated;
- verified or unverified.

This is why Information must remain distinct from Knowledge.

Knowledge is a governed reference under source, scope, version, status, and validation rules.

Information may be an input to Knowledge.

It may support a current task without becoming reusable Knowledge.

It may later become Evidence, a Document, a Communication, or a formal record through the appropriate Owning Service.

The first rule of Part III is therefore:

```text
Availability creates a possibility of use.

It does not create authority.
```

---

## 2. Information, Data, Content, Knowledge, Evidence, and Formal Facts Are Different

Several related concepts must remain separate.

### Data

Data is a recorded representation in a technical or structured form.

Examples include fields, rows, JSON, XML, images, text, timestamps, and files.

### Content

Content is authored or generated material intended to communicate, explain, present, or support an outcome.

Content may contain information.

### Information

Information is data or content interpreted as potentially relevant to a professional purpose.

### Knowledge

Knowledge is a governed reference that has source, scope, status, version, validation, and usage boundaries.

### Evidence

Evidence is information registered and governed for an evidentiary purpose.

### Formal business fact

A formal business fact is a recognized state owned by the relevant Owning Service.

Examples include:

- a formal Matter state;
- a Task state;
- a recorded Order;
- an approved Communication status;
- a verified filing result.

### Professional conclusion

A professional conclusion is a human-accountable judgment or an approved outcome reached under the relevant professional and review boundary.

The relationship may be illustrated as:

```text
Raw data or content
        ↓
Potentially relevant information
        ↓
Governed Knowledge, Evidence, Document,
or formal object registration where appropriate
        ↓
Professional reasoning and review
        ↓
Approved conclusion or governed action
```

The path is not automatic.

The same information may never become Knowledge.

A public website excerpt may be useful for one inquiry but unsuitable as a reusable rule.

An email may support an internal decision without becoming formal Evidence.

An AI extraction may help locate a clause but still require examination of the source.

The architecture must preserve these transitions rather than collapsing them.

---

## 3. Access Is Not Truth

A user, Product, or Agent may be authorized to access information.

That decision answers:

```text
May this actor obtain this representation
for this purpose
under this organization and policy context?
```

It does not answer:

```text
Is the information true?

Is it current?

Is it complete?

Is it authoritative?

Is it legally sufficient?

May it support external advice?

May it be used without review?
```

Permission and Policy govern access and contextual use.

Source authority, validation, version, provenance, professional review, and object ownership govern other questions.

This distinction prevents a common error:

```text
The system allowed me to read it
therefore
the system certified it as correct.
```

A Product may display an official-source record and an internal note side by side.

Both may be accessible.

They do not have equal authority.

An AI Agent may retrieve a source excerpt and a prior draft.

Both may enter the context package.

The context must preserve which is which.

The constitutional rule is:

```text
Access authorization governs availability.

It does not certify meaning.
```

---

## 4. Discovery, Retrieval, Selection, Assembly, and Use Are Separate Stages

Professional information consumption is not one operation.

### Discovery

Discovery identifies that relevant information or a source may exist.

Examples include:

- search result;
- source catalog entry;
- file metadata;
- Knowledge reference;
- linked Matter record;
- provider profile;
- official database candidate.

### Retrieval

Retrieval obtains an authorized representation from the source or owning system.

### Selection

Selection chooses which retrieved information is relevant to the current purpose.

### Transformation

Transformation may normalize, extract, translate, summarize, redact, classify, or structure information.

### Context assembly

Context assembly combines selected information with identity, purpose, scope, restrictions, provenance, time, and governance metadata.

### Use

Use occurs when a human, Product, Skill, Assistant, Guide, or Agent consumes the assembled context.

The stages form this chain:

```text
Discover
→ authorize
→ retrieve
→ validate reference
→ transform where allowed
→ select
→ assemble
→ use
→ trace
→ expire
```

Each stage may fail independently.

A source may be discovered but inaccessible.

Information may be retrievable but irrelevant.

Relevant information may be too restricted for the intended Product.

A transformation may lose a material qualification.

A context package may be valid for drafting but insufficient for filing.

Keeping the stages distinct makes those failures visible.

---

## 5. Information Sources Must Remain Identifiable

Professional context may combine many source types.

A minimum source model should distinguish:

```text
Official primary source

Official secondary source

Authoritative shared Knowledge reference

Core or Owning Service record

Organization-private record

Client instruction

Matter or service record

Document

Evidence

Communication

Provider or professional advice

Public database

Public website

Imported dataset

Local Vault source

Acquisition worker output

Historical case

Product projection

Human observation

AI extraction

AI-generated candidate

Unknown source
```

The label alone is not enough.

A source representation may also need:

- source identity;
- publisher or owner;
- organization and client scope;
- source type;
- location or reference;
- acquisition method;
- retrieval time;
- effective time;
- language;
- version;
- status;
- access restriction;
- transformation history;
- validation or review status.

A source should not become anonymous merely because it was imported into a common index.

The rule is:

```text
Indexing may improve retrieval.

It must not erase source identity.
```

---

## 6. Primary and Secondary Sources Must Remain Distinct

A primary source originates the relevant fact, rule, instruction, or record.

A secondary source describes, interprets, summarizes, republishes, or derives from another source.

Examples:

```text
Trademark office register
→ primary source for the displayed official record

Commercial trademark database
→ secondary or aggregated source

Statute or regulation
→ primary legal source

Professional commentary
→ secondary interpretation

Client-signed instruction
→ primary source for the instruction

Internal summary of the instruction
→ secondary representation

Foreign associate’s current written advice
→ primary source for that associate’s stated position

AI summary of the advice
→ derived secondary representation
```

Primary does not automatically mean complete or current.

Secondary does not automatically mean unreliable.

But the distinction affects professional use.

A secondary source may be valuable for discovery, comparison, explanation, or cross-checking.

High-consequence use may require retrieval of the primary source.

The architecture should support the pattern:

```text
Secondary source discovers or explains.

Primary source confirms where the consequence requires it.
```

---

## 7. Provenance Is the History of an Information Representation

Provenance answers:

> Where did this information representation come from, how did it reach the current context, and what happened to it along the way?

A useful provenance chain may include:

```text
origin source
→ acquisition event
→ raw capture
→ parsing or extraction
→ normalization
→ translation
→ redaction
→ enrichment
→ synchronization
→ retrieval
→ selection
→ context assembly
→ use
```

Not every use requires every detail.

But the system should preserve enough provenance to explain material professional influence.

Provenance may identify:

- original source;
- source owner or publisher;
- source reference;
- acquisition actor or worker;
- acquisition method;
- retrieval time;
- source effective time;
- raw representation reference;
- transformation steps;
- model or tool used;
- human reviewer;
- output version;
- omissions;
- target context;
- correlation trace.

The constitutional rule is:

```text
Transformation may change representation.

It must not hide origin.
```

---

## 8. Provenance Is Not the Same as Citation

A citation points to a source.

Provenance explains the lineage of the representation being used.

For example:

```text
Citation:
official guideline URL

Provenance:
official PDF retrieved on a certain date
→ page extracted
→ text normalized
→ translated
→ summarized by an AI Agent
→ reviewed by a named professional
→ used in a specific context package
```

A citation can be correct while the derived text is flawed.

A valid source URL does not prove that:

- the relevant version was retrieved;
- the correct section was extracted;
- no qualification was omitted;
- the translation was accurate;
- the summary preserved scope;
- the source was effective on the relevant date.

Therefore:

```text
Citation supports traceability.

Provenance supports explainability of transformation.
```

Both may be required.

Neither replaces professional review.

---

## 9. Source Authority Must Remain Explicit

Source authority is contextual.

A source may be authoritative for one question and not another.

Examples:

- an official register may be authoritative for recorded status but not for the client’s commercial intention;
- a client instruction may be authoritative for what the client requested but not for legal sufficiency;
- a foreign associate may be authoritative for their own quotation and practical advice but not necessarily for an official legal rule;
- an internal template may be approved for organization use but not authoritative outside its defined scope;
- a historical Matter may show prior practice but not establish a current rule.

A context package should therefore avoid one universal “trusted” label.

It may need to identify:

```text
authority type

authority scope

validation status

professional-use limitation

effective period

review requirement
```

The question is not only:

```text
Is this source trusted?
```

It is:

```text
Trusted for what claim,
for which purpose,
in which time,
under which scope?
```

---

## 10. Freshness and Effective Time Are Different

Freshness asks when information was retrieved, checked, or updated.

Effective time asks when the represented rule, fact, instruction, price, or status applies.

These may differ.

Examples:

- a rule retrieved today may have taken effect last year;
- a current webpage may describe a future fee;
- an old email may remain the latest valid client instruction;
- a recently synchronized cache may contain an older source version;
- a historical Matter must use the rule effective at the relevant filing date, not today’s rule.

A useful time model may include:

```text
source publication time

source effective time

retrieval time

transformation time

validation time

context assembly time

context expiry time

professional-action time
```

The system should not use one generic `updated_at` field to answer all of these questions conceptually.

The principle is:

```text
Recent retrieval
≠
currently effective information

Current information
≠
historically applicable information
```

---

## 11. Historical Context Must Not Be Rewritten by Current Information

Professional records often need the information available at the time of action.

A past quotation may have used:

- an earlier official fee;
- an earlier exchange rate;
- an earlier provider price;
- a prior client instruction;
- a former organization policy;
- a superseded office guideline.

When reviewing the past, the system should not silently replace those inputs with current values.

Historical explainability may require preserving:

- the selected source version;
- the context assembly time;
- the applicable policy version;
- the user and organization context;
- the known uncertainty;
- the output produced;
- the review or decision made.

Current information supports current work.

Historical information explains historical work.

The architecture therefore distinguishes:

```text
Current context assembly

Historical context reconstruction
```

Historical reconstruction should not imply that the exact past internal state can always be recreated.

It should preserve enough trace to explain material influences.

---

## 12. Structured Information Is Not Automatically Governed Knowledge

Information may be normalized into structured fields.

Examples include:

```text
application number

mark text

filing date

status

jurisdiction

class

owner name

deadline candidate

official fee

provider fee

document requirement
```

Structure improves retrieval, comparison, validation, and Product use.

But structure does not create authority.

A field may be:

- incorrectly parsed;
- mapped to the wrong object;
- copied from a stale source;
- missing a qualification;
- derived from an unofficial database;
- valid only for one purpose;
- unreviewed.

The correct relationship is:

```text
Raw source
→ structured information
→ validation or governance where required
→ Knowledge, Evidence, or formal state only through the proper authority
```

This prevents the Data layer from silently becoming the Knowledge or Core layer.

---

## 13. Extraction Must Preserve the Source Boundary

Extraction turns content into selected information.

It may be performed by:

- parser;
- OCR;
- rule-based system;
- human;
- AI model;
- connector;
- acquisition worker.

The extracted output must remain linked to:

- source;
- location within source;
- extraction method;
- extraction time;
- confidence or limitation;
- transformation version;
- reviewer where applicable.

An extracted statement should not be presented as if it were the source itself.

Examples:

```text
Source:
official examination guideline

Extracted information:
opposition period = 30 days

Required trace:
document version
section or page
effective date
jurisdiction
exceptions
extraction method
review state
```

If the source contains exceptions, an isolated extracted value may be misleading.

The rule is:

```text
Extraction increases usability.

It must not erase context required for meaning.
```

---

## 14. Translation Is a Transformation, Not a Neutral Copy

MarkOrbit operates across jurisdictions and languages.

Translation is essential.

It is also a transformation.

A translated representation may alter:

- legal terminology;
- scope;
- tone;
- ambiguity;
- defined terms;
- dates;
- names;
- qualification;
- responsibility.

A context package using translated information may need to preserve:

- source language;
- translated language;
- original reference;
- translator type;
- machine or human assistance;
- review status;
- known ambiguity;
- terminology mapping.

For professional use:

```text
Translated text may support understanding.

The original remains the source unless the translated version
has a separately governed authority.
```

An AI translation should remain marked as AI-assisted where required.

High-consequence content may require bilingual review.

---

## 15. Summaries Must Preserve Material Limitations

Summaries reduce information volume.

They are useful for:

- operating surfaces;
- AI Context;
- Matter orientation;
- provider comparison;
- review preparation;
- client explanation.

But summarization may remove:

- exceptions;
- uncertainty;
- conditions;
- dissenting views;
- date limitations;
- source hierarchy;
- procedural detail;
- negative facts.

A safe summary should preserve or expose:

- source references;
- summary purpose;
- relevant scope;
- omitted detail where material;
- uncertainty;
- contradiction;
- review requirement;
- status as a summary.

The principle is:

```text
Summary improves attention.

It does not replace the source where the consequence
depends on omitted detail.
```

A Product should allow a reviewer to reach the source or a sufficiently complete representation where needed.

---

## 16. Information Conflict Must Be Preserved, Not Smoothed Away

Professional information often conflicts.

Examples include:

- two official pages show different fees;
- a foreign associate’s advice differs from a guideline;
- two databases report different status;
- client instructions changed;
- a local record differs from the Owning Service;
- two internal experts interpret a rule differently;
- an AI extraction conflicts with the source text.

A system may be tempted to choose one value and hide the conflict.

That creates false certainty.

A context package should be able to represent:

```text
consistent information

partially consistent information

conflicting information

superseded information

unresolved information

missing information
```

Conflict handling may include:

- authority comparison;
- effective-date comparison;
- source retrieval;
- version check;
- human review;
- professional escalation;
- safe refusal;
- separate presentation.

The correct rule is:

```text
Conflict is information.

It must not disappear merely to simplify the interface.
```

---

## 17. Missing Context Must Be First-Class

The absence of required information may be more important than the information already retrieved.

Examples include:

- no confirmed client instruction;
- no current official fee;
- no verified owner identity;
- no filing date;
- no source for a deadline;
- no evidence of provider authorization;
- no applicable Knowledge reference;
- no review authority;
- no current policy decision.

Missing context should be represented explicitly.

It may lead to:

- clarification request;
- research task;
- Knowledge gap;
- source acquisition;
- review request;
- blocked preparation;
- recommendation limitation;
- safe refusal;
- escalation.

The system should not fill missing context through plausible inference without marking it.

The principle is:

```text
Unknown
≠
No

Missing
≠
Not required

Inferred
≠
Confirmed
```

---

## 18. Information Access Must Be Purpose-Bound

Information should be accessed for a defined purpose.

Purposes may include:

- internal orientation;
- client intake;
- quotation preparation;
- jurisdiction research;
- classification support;
- provider evaluation;
- filing preparation;
- review;
- Communication drafting;
- Artifact generation;
- audit explanation;
- knowledge validation;
- network collaboration.

The same information may be permitted for one purpose and prohibited for another.

Examples:

- client Evidence may be used for a Matter but prohibited from general Product analytics;
- provider pricing may support internal quotation but not client-facing disclosure;
- private provider criticism may support selection but not MGSN publication;
- organization templates may support drafting but not shared Knowledge promotion;
- personal notes may support the individual user but not team context.

Purpose must influence:

- source selection;
- access decision;
- representation depth;
- redaction;
- retention;
- AI access;
- Human Review;
- output use.

The rule is:

```text
Authorized information
does not mean
authorized for every purpose.
```

---

## 19. Context Assembly Begins with Identity and Subject

A context package should not begin with a broad search query.

It should begin with:

```text
Which organization?

Which user or Agent?

Which role or responsibility?

Which Product or operating surface?

Which client, Matter, object, or subject?

Which purpose?

Which intended output or decision?

Which consequence level?
```

These answers constrain what may be retrieved.

The minimum context frame may include:

```text
organization reference

actor reference

Product reference

purpose

subject references

client or Matter scope

permission decisions

policy decisions

data boundary

professional responsibility

review requirement
```

Only then should source discovery and retrieval proceed.

This order prevents context flooding.

---

## 20. Context Assembly Is an Ephemeral Professional Operation

Context assembly creates a purpose-specific view of information.

It should not be treated as a permanent universal record by default.

A context package may exist for:

- one AI response;
- one review;
- one Product screen;
- one draft;
- one recommendation;
- one workflow step;
- one historical explanation.

The package may be:

- assembled on demand;
- cached temporarily;
- stored as a trace reference;
- invalidated after policy change;
- expired after the purpose ends;
- reconstructed under a later authorized request.

The important distinction is:

```text
Context package
≠
new universal data store
```

Permanent storage should require its own purpose, classification, retention, and authority.

The package should not silently become organizational memory, shared Knowledge, or Product-owned state.

---

## 21. Context Package Is Not a Prompt

AI systems often express context through prompts.

But prompt construction is only one possible implementation detail.

A governed context package may be used by:

- human reviewer;
- Product;
- Skill;
- Assistant;
- Guide;
- AI Agent;
- workflow preparation;
- document generator;
- comparison engine.

The context package should preserve structured governance fields that free-text prompts cannot safely replace.

Conceptually, it may contain:

```text
context identity

purpose

subject references

selected information items

source and provenance references

authority and validation markers

time and version

restrictions

missing context

conflicts

allowed operations

output mode

review requirements

expiry
```

A prompt may consume a projection of this package.

The prompt does not define the authority of the information.

The rule is:

```text
Prompt carries instructions and selected context.

Governance determines what may enter the prompt
and how the output may be used.
```

---

## 22. Context Assembly Must Prefer the Minimum Sufficient Context

More information is not always better.

Excessive context can:

- expose private data;
- confuse the user or model;
- increase contradiction;
- hide the most relevant source;
- weaken auditability;
- increase cost and latency;
- carry one client’s information into another purpose;
- make revocation harder;
- encourage unsupported inference.

The target is:

```text
minimum sufficient authorized context
```

This does not mean the smallest possible context.

It means enough context to support the purpose safely, with no unnecessary information.

A context assembly process may prioritize:

- primary source over duplicate copy;
- current applicable version;
- validated Knowledge where available;
- directly relevant client instruction;
- relevant Matter state;
- required policy and review boundary;
- known conflict;
- material missing information.

It may omit:

- unrelated clients;
- unrelated Matters;
- full organization history;
- private notes with no current purpose;
- redundant source copies;
- restricted fields;
- superseded versions unless historically relevant.

---

## 23. Context Budget Is a Governance Concept Before It Is a Token Limit

AI systems introduce token and context-window limits.

But a professional context budget is broader than a technical token budget.

It includes limits on:

- sensitivity;
- purpose;
- source count;
- time range;
- client scope;
- Matter scope;
- version range;
- private information;
- derived information;
- AI access;
- retention.

A technically available context window should not determine how much information is included.

The correct order is:

```text
governance budget
→ relevance budget
→ technical representation budget
```

When information must be reduced, the system should preserve:

- material facts;
- source trace;
- qualification;
- conflict;
- uncertainty;
- review boundary.

Compression should not prioritize brevity over professional meaning.

---

## 24. Context Views May Differ by Consumer

The same underlying purpose may produce different authorized views.

### Human professional view

May include detailed sources, conflict, full Documents, prior reasoning, and review controls.

### Product view

May include structured fields, summaries, status, and source links required for the journey.

### AI Agent view

May include policy-filtered content, source references, allowed tools, output mode, and explicit missing context.

### Client view

May include approved explanation and selected information, excluding internal notes and provider-sensitive context.

### Network participant view

May include only the minimum collaboration package.

The views may differ.

The source and authority should remain consistent.

The principle is:

```text
Different consumers may receive different representations.

They must not receive different invented truths.
```

---

## 25. Human Context and AI Context Share Sources but Not Necessarily Scope

A human professional and an AI Agent may work on the same purpose.

They do not necessarily receive the same context.

A human reviewer may access:

- full source Documents;
- sensitive Evidence;
- internal notes;
- provider history;
- conflict details.

An AI Agent may be limited to:

- approved extracts;
- safe summaries;
- selected fields;
- restricted source references;
- no raw Evidence;
- no private contact information.

Conversely, an AI Agent may retrieve a broad public corpus for comparison while the human sees only selected results.

The access decision must remain explicit.

The architecture should avoid the hidden assumption:

```text
If the user can see it,
the AI can see it.
```

or:

```text
If the AI retrieved it,
the user is authorized to see the raw source.
```

---

## 26. AI Extraction and Retrieval Results Remain Candidates

AI may assist with:

- source discovery;
- relevance ranking;
- extraction;
- translation;
- summarization;
- comparison;
- contradiction detection;
- missing-context detection;
- classification;
- context compression.

These outputs remain candidates unless governed otherwise.

AI must not silently convert:

- extraction into verified fact;
- summary into Knowledge;
- relevance score into authority;
- inference into client instruction;
- predicted deadline into official deadline;
- similarity into legal conclusion;
- source frequency into professional truth.

A safe AI-assisted information result should preserve:

```text
AI participation

Agent identity

Capability or Skill used

data access scope

sources

output mode

confidence or uncertainty

missing context

restricted omissions

Human Review requirement
```

CH16 develops Agent roles in more detail.

This chapter establishes only the information boundary.

---

## 27. Search Ranking Must Not Become Source Authority

Search, retrieval, and recommendation systems rank information.

Ranking may use:

- semantic similarity;
- keyword match;
- recency;
- source type;
- user history;
- Product context;
- validation status;
- authority;
- popularity.

A high-ranked result is not necessarily the most authoritative result.

A frequently cited secondary article may rank above an official source.

A recent internal note may rank above a validated rule.

A personalized result may reflect convenience rather than professional relevance.

The interface and context package should not present ranking as authority.

The distinction is:

```text
Retrieval score
≠
source authority

Relevance score
≠
professional correctness
```

Authority and validation should remain separately visible.

---

## 28. Public Information Still Requires Provenance and Usage Control

Public information is not unrestricted professional truth.

Public sources may have:

- licensing terms;
- access limits;
- outdated pages;
- unofficial mirrors;
- incomplete records;
- jurisdiction limitations;
- language issues;
- changed URLs;
- automated-access restrictions;
- privacy implications when aggregated.

Workplace may use public information through:

- direct retrieval;
- acquisition workers;
- public datasets;
- shared indexes;
- Local Vault;
- external providers.

The source record should preserve:

- source;
- acquisition method;
- retrieval date;
- terms or restrictions where relevant;
- public or derived status;
- transformation.

Public data may support discovery broadly.

High-consequence use may still require confirmation.

---

## 29. Private Information Requires a Stronger Context Boundary

Private information may include:

- client instructions;
- unpublished applications;
- Evidence;
- internal strategy;
- provider pricing;
- private Communications;
- organization notes;
- financial data;
- credentials;
- personal information.

Context assembly must apply the data boundaries defined in CH12.

It may use:

- references instead of content;
- metadata instead of raw files;
- redacted extracts;
- safe summaries;
- local processing;
- temporary access;
- restricted AI scope;
- Human Review.

Private context should not be copied into shared indexes merely to improve search.

The rule remains:

```text
Private information may participate in context.

It does not become shared by participation.
```

---

## 30. Local Vault May Supply Context Without Full Synchronization

Local Vault may hold information that is too large, sensitive, or restricted for broad synchronization.

Workplace may still use it through:

- local search;
- metadata lookup;
- local extraction;
- local AI retrieval;
- selected context projection;
- source reference;
- derived value;
- approved summary.

A context package may therefore include:

```text
local source reference

local availability marker

approved metadata

policy-filtered extract

derived candidate

synchronization restriction
```

The receiving Product or Agent need not receive the entire local source.

This supports the principle:

```text
Bring the authorized question to the data
where possible,
rather than moving all data to the consumer.
```

Local Vault remains governed.

A local result does not become authoritative solely because it was processed locally.

---

## 31. Acquisition Workers Produce Information, Not Knowledge

Distributed acquisition workers may collect:

- official updates;
- public database records;
- provider websites;
- fee pages;
- public contacts;
- public decisions;
- source changes.

Their outputs may include:

- raw capture;
- structured information;
- source metadata;
- change signal;
- extraction candidate;
- failure report.

The worker does not decide that the output is governed Knowledge.

It should preserve:

- job identity;
- source;
- acquisition time;
- acquisition method;
- scope;
- worker identity;
- transformation;
- completeness;
- failure;
- restrictions.

The path is:

```text
Acquisition
→ Information
→ Validation or comparison
→ Knowledge candidate where appropriate
→ governed Knowledge only through the proper process
```

This boundary is especially important for Mo Crawl and other distributed data acquisition systems.

---

## 32. Product Projections Must Preserve Their Owning Source

Products may display information from:

- Core Objects;
- Owning Services;
- shared Knowledge;
- organization-private context;
- Local Vault;
- external sources;
- AI output.

A Product may cache or project this information.

It must not imply that the Product owns all represented facts.

A Product view should preserve enough information to answer:

```text
What is the source?

Is this current?

Is this authoritative?

Is this a summary?

Is this AI-assisted?

Can it be edited here?

Which service controls the formal state?

Is review required?
```

Part IV develops Product embedding.

The information rule is:

```text
Product presentation may simplify.

It must not erase source and authority.
```

---

## 33. Cross-Product Context Handoff Must Preserve Provenance

One Product may hand a purpose-bound context to another.

Example:

```text
Lite
→ identifies possible trademark need

MarkReg
→ receives approved client and recommendation context

MGSN interface
→ receives a limited capability request

Execution
→ receives prepared action and source trace
```

The handoff should preserve:

- organization;
- user or Agent;
- client or subject;
- purpose;
- selected information;
- source references;
- private-data restrictions;
- missing context;
- review requirement;
- version;
- originating Product;
- correlation trace.

The receiving Product should not treat the package as its own original truth.

It should be able to retrieve current authoritative state where required.

Cross-Product continuity does not justify broad context replication.

---

## 34. Cross-Workplace Context Must Be Reassembled at the Boundary

When information crosses from one Workplace to another, the receiving Workplace should not inherit the sender’s full internal context.

The sender prepares an authorized exchange representation.

The receiver assembles its own context under its own:

- organization identity;
- user and role;
- purpose;
- Permission;
- Policy;
- client or collaboration scope;
- retention;
- review boundary.

The model is:

```text
Sender internal context
→ approved exchange package
→ receiving boundary
→ receiving access and policy evaluation
→ receiver-specific context assembly
```

This preserves independent Orbits.

An MGSN collaboration package may carry references and source trace.

It does not transfer the sender’s internal Permission, responsibility, or professional judgment.

---

## 35. Context Must Be Versioned Enough to Support Review

A reviewer must know what information was reviewed.

If context changes materially after review, the prior decision may no longer apply.

Material changes may include:

- new client instruction;
- changed recipient;
- changed fee;
- new Evidence;
- updated official status;
- changed source version;
- changed deadline;
- changed provider;
- changed policy;
- changed draft;
- resolved or newly discovered conflict.

A context package may therefore need:

- assembly identifier;
- assembly time;
- selected source versions;
- transformation versions;
- package version;
- material-change marker;
- review reference;
- expiry.

This does not mean every retrieval result becomes a permanent object.

It means review must be linked to a sufficiently identifiable context.

The principle is:

```text
Review applies to the context reviewed.

It does not approve unknown future context.
```

---

## 36. Context Expiry Must Be Explicit

Context may become invalid because:

- time passes;
- the source changes;
- Permission changes;
- Policy changes;
- user role changes;
- client instruction changes;
- a Product context ends;
- a Matter closes;
- a provider is replaced;
- data access is revoked;
- the intended purpose completes.

An expired context package should not remain silently usable.

Possible expiry behavior includes:

- reassemble;
- reauthorize;
- refresh selected sources;
- mark stale;
- remove restricted fields;
- invalidate prepared action;
- require new review;
- preserve historical trace only.

The architecture should distinguish:

```text
context valid for current use

context stale but viewable

context historical only

context revoked

context deleted or unavailable
```

---

## 37. Context Assembly Should Produce Explainable Output

A human should be able to understand, at an appropriate level:

- why information was included;
- where it came from;
- which version was used;
- what was omitted;
- which sources conflicted;
- which information is missing;
- which restrictions apply;
- whether AI participated;
- whether review is required.

Explainability does not require exposing:

- hidden prompts;
- internal model reasoning;
- secrets;
- restricted source content;
- unrelated private data;
- implementation internals.

The target is professional trace, not model introspection.

A safe explanation may say:

```text
This draft used:
- the client instruction dated X;
- the validated jurisdiction rule version Y;
- the current Matter record;
- the organization template version Z.

The provider fee remains unconfirmed.
One source conflict requires review.
AI assisted with summarization.
```

That is more useful than a generic confidence score.

---

## 38. Context Use Must Be Traceable Without Becoming Surveillance

High-consequence professional use may require a record of:

- actor;
- organization;
- purpose;
- subject;
- source references;
- information versions;
- Agent;
- Permission and Policy decisions;
- output;
- Human Review;
- correlation.

But traceability must not become unlimited observation of every reading action or private thought.

Audit depth should follow:

- consequence;
- data sensitivity;
- professional risk;
- legal obligation;
- organization policy;
- protected action.

A low-risk internal search may need minimal trace.

A filing preparation or external Communication may need stronger trace.

The distinction is:

```text
Professional traceability
≠
unlimited behavioral surveillance
```

Audit Context preserves trace.

It does not certify truth or compliance by itself.

---

## 39. Information Use Does Not Explain the Final Judgment by Itself

A professional decision may be informed by several sources.

But listing sources does not fully explain the reasoning or establish the correctness of the result.

The system should preserve a distinction among:

```text
information available

information selected

information used

analysis performed

recommendation produced

human judgment made

formal action executed

outcome observed
```

Different chapters govern those stages.

CH13 governs information access, provenance, and context assembly.

CH14 governs Knowledge consumption.

CH17 governs candidates, recommendations, and Next Best Action.

CH18 governs the prepared-action handoff.

CH19 governs Human Review, approval, and Owning Service handoff.

The sequence must not collapse.

---

## 40. The Minimum Context Assembly Model

A minimum conceptual model is:

```text
Context Request
  │
  ├── organization
  ├── actor or Agent
  ├── Product
  ├── purpose
  ├── subject
  ├── consequence level
  └── intended consumer
        │
        ▼
Access and Policy Evaluation
        │
        ├── permitted sources
        ├── prohibited sources
        ├── data boundaries
        ├── representation limits
        └── review requirements
        │
        ▼
Information Discovery and Retrieval
        │
        ├── source references
        ├── versions and time
        ├── authority markers
        ├── provenance
        ├── transformation
        └── freshness
        │
        ▼
Selection and Minimization
        │
        ├── relevance
        ├── primary-source preference
        ├── conflict preservation
        ├── missing context
        ├── redaction
        └── context budget
        │
        ▼
Authorized Context Package
        │
        ├── selected information
        ├── source and provenance
        ├── restrictions
        ├── uncertainty
        ├── allowed output mode
        ├── Human Review requirement
        └── expiry
        │
        ▼
Human, Product, Skill, Assistant, Guide, or Agent Use
        │
        ▼
Trace, release, expiry, or historical preservation
```

This is an architectural model.

It is not a schema, API, vector-store design, prompt format, or orchestration graph.

---

## 41. Required Distinctions

This chapter establishes the following required distinctions.

```text
Information access ≠ information truth
```

Permission to retrieve does not certify correctness.

```text
Discovery ≠ retrieval
```

Knowing that a source exists does not mean its content has been obtained.

```text
Retrieval ≠ selection
```

Retrieved information may be irrelevant, excessive, or prohibited for the purpose.

```text
Selection ≠ professional judgment
```

Choosing sources does not decide the professional question.

```text
Information ≠ Knowledge
```

Information may be unverified, temporary, private, conflicting, or purpose-specific.

```text
Information ≠ Evidence
```

Information becomes Evidence only through the appropriate evidentiary registration and governance.

```text
Information ≠ formal business fact
```

Only the relevant Owning Service controls formal state.

```text
Citation ≠ provenance
```

Citation points to a source; provenance records the representation’s lineage.

```text
Source authority ≠ universal trust
```

Authority applies to a defined claim and scope.

```text
Freshness ≠ effective time
```

Recent retrieval does not prove current applicability.

```text
Structured information ≠ governed Knowledge
```

Normalization does not create validation or authority.

```text
AI extraction ≠ verified fact
```

AI-derived information remains marked and reviewable.

```text
Context assembly ≠ unrestricted aggregation
```

Context must remain minimal, purpose-bound, and authorized.

```text
Context package ≠ prompt
```

A prompt may consume context; it does not define governance.

```text
Context package ≠ new source of truth
```

It is a purpose-specific representation.

```text
More context ≠ better context
```

Professional usefulness depends on relevance, authority, sufficiency, and clarity.

```text
Information used ≠ judgment made
```

Source trace does not replace professional reasoning and accountability.

---

## 42. Failure Modes This Chapter Prevents

### Search-equals-truth

The highest-ranked result is treated as the correct professional answer.

### Access-equals-authority

Anything a user or Agent can retrieve is treated as approved for use.

### Source laundering

An unofficial or private source becomes apparently authoritative after being imported into a shared index.

### Provenance loss

Extraction, translation, or summarization removes the path back to the source.

### Citation theater

A source link is displayed even though the used text came through untraceable transformations.

### Freshness confusion

Recent retrieval is mistaken for current legal or commercial applicability.

### Historical rewriting

Current rules or prices silently replace the information used in prior work.

### Context flooding

An Agent or Product receives broad organization and client data because more context appears helpful.

### Cross-client contamination

One client’s instruction, Evidence, or private history enters another client’s context.

### Product-owned truth

A Product cache or projection becomes treated as the formal record.

### AI fact promotion

AI extraction or summary becomes a verified fact without review.

### Conflict smoothing

Contradictory sources are merged into a false single answer.

### Missing-context invention

Unknown information is filled through plausible inference and shown as confirmed.

### Local-source opacity

Local Vault results enter context without source, version, or restriction markers.

### Cross-Orbit leakage

A collaboration package exposes the sender’s internal context rather than a minimal exchange representation.

### Permanent context accumulation

Temporary context packages become an uncontrolled shadow database.

### Review drift

A review remains attached after material context changes.

### Audit overreach

Traceability becomes unnecessary surveillance or copies restricted content into audit logs.

These failures may produce useful-looking outputs.

They do not conform to the Workplace architecture.

---

## 43. Minimum Conformance Rule

A conforming Workplace must preserve the following lock:

```text
Information remains distinct from Knowledge,
Evidence, formal business facts, and professional conclusions.

Context assembly begins with organization,
actor, purpose, subject, permission, policy,
data boundary, and responsibility.

Discovery, retrieval, transformation,
selection, assembly, and use remain distinguishable.

Sources remain identifiable.

Primary and secondary sources remain distinguishable.

Provenance survives acquisition and transformation.

Citation does not substitute for provenance.

Source authority remains scoped.

Version, effective time, and retrieval time remain visible.

Conflicts and missing context remain explicit.

Structured and AI-extracted information
do not become governed truth automatically.

Context is minimal, purpose-bound,
consumer-specific, and time-bound.

Private and local information remains private
unless authorized representation is required.

Products, Skills, Assistants, Guides, and Agents
receive only the context required for their purpose.

Context packages do not become new sources of truth.

Material context changes may invalidate review
or require reassembly.

Information use remains traceable
without exposing unnecessary restricted content.

Human professionals remain accountable
for professional judgment.
```

A technically successful retrieval or RAG system that violates this lock does not conform architecturally.

---

## 44. Chapter Boundary

This chapter defines:

- the Workplace meaning of Information;
- distinctions among data, content, Information, Knowledge, Evidence, formal facts, and professional conclusions;
- information source categories;
- access boundaries;
- discovery, retrieval, selection, transformation, assembly, and use stages;
- primary and secondary source distinctions;
- provenance;
- citation;
- source authority;
- freshness and effective time;
- historical context;
- extraction;
- translation;
- summarization;
- conflict and missing-context treatment;
- purpose limitation;
- minimum sufficient context;
- context packages;
- context budgets;
- consumer-specific views;
- AI-assisted retrieval boundaries;
- Local Vault participation;
- acquisition-worker outputs;
- cross-Product and cross-Workplace context handoff;
- version, expiry, explainability, and trace.

It does not define:

- final Knowledge governance or Brain architecture;
- Knowledge promotion rules;
- Capability or Skill selection;
- Assistant, Guide, or AI Agent runtime design;
- recommendation scoring;
- Next Best Action;
- prepared-action contracts;
- Human Review lifecycle;
- Owning Service mutation;
- search-engine implementation;
- vector database;
- embedding model;
- ranking algorithm;
- RAG framework;
- prompt templates;
- context-window strategy;
- crawler implementation;
- connector implementation;
- database schemas;
- APIs;
- deployment topology;
- production security certification.

Those subjects belong to CH14–CH19, future technical specifications, Product publications, implementation ADRs, and project repositories.

This chapter does not modify Book 02 Core semantics.

It does not modify Book 03 Execution authority.

It does not authorize external Communication, filing, submission, payment, provider appointment, provider instruction, official recordal, autonomous AI professional action, or unrestricted information access.

---

## 45. Chapter Conclusion

Part III begins with a simple but critical proposition:

> Professional intelligence cannot be trusted if the information entering the context has lost its identity, source, time, scope, or restrictions.

Workplace must help professionals and Products find relevant information.

But search alone is not enough.

The system must know:

```text
who is asking

for which organization

for which client, Matter, or subject

for what purpose

from which sources

under which permission and policy

using which representation

with which provenance and version

with which conflicts or gaps

for which consumer

until when
```

The full information-consumption chain is:

```text
Discover
→ authorize
→ retrieve
→ preserve provenance
→ assess source, version, and time
→ transform without hiding origin
→ select the minimum sufficient information
→ preserve conflict and missing context
→ assemble an authorized context package
→ use under consumer-specific limits
→ review where required
→ trace and expire
```

The constitutional outcome is:

```text
Information informs.

Knowledge governs reusable understanding.

Intelligence produces candidates and explanations.

Capabilities perform reusable functions.

AI assists.

Humans judge.

Execution governs action.

Owning Services change formal facts.
```

CH13 establishes the entry boundary.

CH14 now asks the next question:

> When information has become governed Knowledge, how may Workplace consume it without turning the Brain into the owner of private organizational memory, professional judgment, or every source of truth?
