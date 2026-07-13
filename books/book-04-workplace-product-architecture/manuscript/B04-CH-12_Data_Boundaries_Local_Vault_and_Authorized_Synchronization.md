# B04-CH-12 — Data Boundaries, Local Vault and Authorized Synchronization

**Status:** Draft 1  
**Chapter Map:** B04-TOC-V0.1  
**Part:** Part II — Organization Context and Operating Environment

## Chapter Purpose

This chapter defines how an Organization Workplace establishes data boundaries, uses a Local Vault, and authorizes synchronization without turning storage location into ownership, a local copy into formal authority, or synchronization into unrestricted replication.

Chapter 07 established organization identity and active Workplace Context.

Chapter 08 established people, roles, permissions, responsibility, and accountability.

Chapter 09 established clients, relationships, service context, pricing, preferences, and organization-specific business rules.

Chapter 10 established private knowledge, AI Context, preferences, and organizational memory.

Chapter 11 established how work, review, Communication, and attention become visible through governed operating surfaces.

The remaining question in Part II is:

> Where may organizational information exist, who may use it, for which purpose, under which authority, and what may cross the boundary between local, private, shared, Product, and network environments?

Professional organizations work with information that differs greatly in sensitivity, size, authority, lifecycle, and operational value.

Examples include:

- public trademark records;
- official rules and fee schedules;
- customer instructions;
- identity and contact data;
- evidence;
- draft legal positions;
- signed documents;
- provider pricing;
- internal notes;
- private templates;
- local databases;
- AI Context;
- browser credentials;
- exported reports;
- rendered Artifacts;
- audit records;
- organizational memory.

Treating all of this information as one cloud data pool would violate organizational autonomy and expose unnecessary risk.

Treating all of it as local-only would weaken continuity, collaboration, governed Execution, cross-Product operation, and recovery.

The architecture therefore requires deliberate boundaries rather than one universal storage rule.

The central proposition of this chapter is:

```text
Data Boundary
=
identity
+ authority
+ classification
+ purpose
+ permission
+ policy
+ location
+ retention
+ allowed movement
+ audit
```

Local Vault provides a logical local or private technical boundary.

Workplace provides the organization policy and context that govern its use.

Core and Owning Services remain authoritative for formal business facts.

Products consume only authorized data.

AI Agents receive purpose-bound context.

Synchronization occurs only through an explicit policy decision.

The constitutional distinctions are:

```text
Data ownership ≠ storage location

Storage location ≠ formal authority

Local copy ≠ source of truth

Synchronization ≠ unrestricted replication

Sharing ≠ synchronization

Backup ≠ operational access

Encryption ≠ authorization

Derived value ≠ automatically safe value

Local AI ≠ ungoverned AI

Cloud AI ≠ entitlement to full context
```

This chapter defines the architecture.

It does not select a database, encryption algorithm, file format, cloud provider, synchronization engine, deployment topology, or backup product.

---

## 1. Professional Data Does Not Form One Undifferentiated Pool

A professional organization does not hold one kind of data.

It holds many kinds of information with different meanings and obligations.

A public trademark record may be broadly reusable.

A client instruction may be confidential and purpose-limited.

A signed Power of Attorney may be shared only with defined participants.

An internal provider evaluation may be commercially sensitive.

A draft legal strategy may require restricted access and Human Review.

A local trademark database may be too large to synchronize fully.

A browser credential should not become general Product context.

An AI-generated summary may be useful but still require source trace and review.

If all of these are treated as ordinary files in one common pool, the system loses the ability to answer:

```text
Who controls this information?

Who may access it?

For what purpose?

Which Product may use it?

May AI read it?

May it leave the device?

May it be synchronized?

May it be shared with another Workplace?

Which version is authoritative?

How long may it remain?

What must happen when access is revoked?
```

A data architecture for professional services must therefore begin with classification and governance, not storage convenience.

The first rule is:

> Data movement must follow professional meaning and authority, not the easiest available technical path.

---

## 2. Data Boundary Is a Governance Boundary

A data boundary is not merely a database partition, tenant identifier, folder, network segment, or encryption key.

Those mechanisms may help implement a boundary.

They do not define the boundary by themselves.

A data boundary expresses:

- which organization controls the context;
- which client or Matter is affected;
- which people, Products, Agents, and Services may access it;
- which purposes are allowed;
- which uses are prohibited;
- which location classes are permitted;
- which synchronization modes are allowed;
- which retention rules apply;
- which audit and deletion obligations exist.

A useful model is:

```text
Data Boundary
=
Subject
+ Controller
+ Authorized Actors
+ Purpose
+ Classification
+ Permitted Locations
+ Permitted Operations
+ Permitted Transfers
+ Retention
+ Trace
```

The same technical store may contain data with several boundaries.

The same information may also appear in several authorized locations under different rights.

For example:

```text
Official trademark record
→ public source cache in Local Vault
→ normalized reference in shared information service
→ linked Matter context in Workplace
```

The content may be related.

The rights, authority, retention, and operational role of each representation differ.

A technical partition is therefore not enough.

Workplace must preserve the governance meaning of the data wherever it appears.

---

## 3. Classification, Ownership, Custody, Authority, and Location Are Different

Data discussions become confused when several questions are collapsed.

### Classification

Classification asks:

> How sensitive, restricted, authoritative, or shareable is this information?

### Ownership or control

Ownership or control asks:

> Which organization or person has the right and responsibility to decide how this information is used?

### Custody

Custody asks:

> Which system, provider, device, person, or organization currently holds a copy or controls access to it?

### Formal authority

Formal authority asks:

> Which Owning Service or recognized source is authoritative for the current business fact?

### Location

Location asks:

> Where is the information physically or logically stored or processed?

These questions may produce different answers.

Example:

```text
Customer instruction
Classification:
client-restricted

Controller:
serving organization under the engagement

Custody:
Workplace and an authorized local device

Formal authority:
the approved instruction record or relevant Owning Service

Location:
private cloud plus Local Vault reference
```

Another example:

```text
Official filing status
Classification:
organization-visible professional record

Controller:
organization controls its use in Workplace

Custody:
MarkReg, local cache, and official-source connector

Formal authority:
relevant Owning Service based on verified official evidence

Location:
several authorized environments
```

The architecture must not assume:

```text
stored locally
=
owned locally
```

or:

```text
stored centrally
=
owned by the platform
```

or:

```text
copied into Workplace
=
authoritative business fact
```

These distinctions are essential to organizational autonomy and reliable professional operation.

---

## 4. A Minimum Data-Zone Model

Book 04 uses a logical data-zone model to make boundaries understandable.

These zones are architectural categories.

They are not mandatory databases, repositories, cloud accounts, or network segments.

### 4.1 Public Source Zone

The Public Source Zone contains information available from public or officially accessible sources.

Examples include:

- public trademark records;
- public office notices;
- laws and regulations;
- public examination guidelines;
- public fee schedules;
- public classification data;
- public websites;
- public professional publications.

Public availability does not eliminate provenance, licensing, freshness, or usage requirements.

Public data may still be outdated, incomplete, copyrighted, rate-limited, or subject to source terms.

### 4.2 Shared MarkOrbit Knowledge and Capability Zone

This zone contains governed shared assets intended for authorized reuse across Products or Workplaces.

Examples may include:

- validated jurisdiction knowledge;
- governed Knowledge Assets;
- approved Capability definitions;
- Skill metadata;
- Workflow definitions;
- shared templates authorized for broad use;
- public or shared service information.

Shared does not mean unrestricted.

Permission, Product entitlement, authority level, version, and risk may still limit use.

### 4.3 Organization Workplace Zone

This zone contains organization-controlled operational context.

Examples include:

- organization profile;
- users and roles;
- Product configuration;
- client relationship context;
- pricing preferences;
- private templates;
- partner history;
- operating rules;
- organizational memory;
- review assignments;
- private Artifact context.

This zone belongs to the independent Orbit.

The platform does not acquire ownership merely because shared infrastructure hosts part of it.

### 4.4 Client-Restricted Zone

This zone contains information restricted to a particular customer relationship or approved group of relationships.

Examples include:

- client instructions;
- private portfolio information;
- commercial terms;
- confidential correspondence;
- client-specific preferences;
- client-specific risk positions;
- internal relationship notes.

Client-restricted information must not be reused across clients merely because the same user or Product can technically access it.

### 4.5 Matter- or Service-Restricted Zone

This zone contains information restricted to a particular professional service, Matter, Order, review, dispute, or filing journey.

Examples include:

- filing documents;
- evidence;
- draft legal arguments;
- official notices;
- provider instructions;
- review comments;
- matter-specific AI Context;
- protected Communication drafts.

A user who has access to the client relationship may not automatically have access to every restricted Matter.

### 4.6 Personal Private Zone

This zone contains personal operating context that belongs to an individual user under organization policy.

Examples may include:

- personal drafts;
- personal notes;
- personal preference settings;
- local reading history;
- private planning;
- personal Assistant context;
- unsynchronized working files.

Personal does not mean outside organizational governance.

Where the information relates to professional work, retention, confidentiality, conflict, and handoff rules may still apply.

### 4.7 Local Device and Local Vault Zone

This zone contains information retained or processed within an authorized local or private environment.

Examples may include:

- large local databases;
- raw source files;
- local search indexes;
- local case libraries;
- device-bound credentials;
- browser sessions;
- private caches;
- locally rendered outputs;
- locally processed AI context;
- offline work packages.

Local location does not define ownership or authority.

It defines an additional technical and privacy boundary.

### 4.8 Trusted Network Exchange Zone

This zone contains the minimum information intentionally exchanged among independent Workplaces through MGSN or another governed collaboration channel.

Examples may include:

- service request brief;
- selected organization identity;
- capability requirement;
- authorized provider profile;
- limited Matter context;
- approved documents;
- collaboration status;
- outcome evidence;
- trust feedback.

This zone must not become a mirror of either Workplace.

Its purpose is controlled exchange.

The zones may overlap logically.

A single item may move from one zone to another only through authorized transformation, sharing, synchronization, Delivery, or promotion.

---

## 5. Data Classification Must Drive Treatment

Location alone cannot determine treatment.

A file stored in Local Vault may be public.

A record stored in a shared cloud service may be highly restricted.

A safe architecture therefore classifies information by professional sensitivity and permitted use.

A minimum conceptual classification may include:

```text
Public

Shared Governed

Organization Private

Client Restricted

Matter Restricted

Personal Private

Credential or Secret

Regulated or Legally Restricted

Derived Candidate

Audit Restricted
```

### Public

Public information may be broadly accessible, but provenance, source terms, freshness, and integrity still matter.

### Shared Governed

Shared governed information is intentionally available to authorized consumers under version and usage rules.

### Organization Private

Organization-private information belongs to the operating context of one Workplace.

### Client Restricted

Client-restricted information may be used only for the relevant relationship and authorized purpose.

### Matter Restricted

Matter-restricted information may require narrower role, reviewer, or service scope.

### Personal Private

Personal-private information remains within individual scope unless professional or policy obligations require controlled handoff.

### Credential or Secret

Credentials, access tokens, signing keys, browser sessions, and similar secrets require special treatment and should not become ordinary AI or Product context.

### Regulated or Legally Restricted

Some information may be subject to legal, professional, regulatory, contractual, residency, privilege, or evidence obligations.

### Derived Candidate

Derived candidates include summaries, classifications, inferred preferences, risk signals, Task Suggestions, and other outputs that remain non-canonical.

### Audit Restricted

Audit information may be essential for accountability while still restricted because it contains actor, access, failure, security, or sensitive context.

Classification should influence:

- storage;
- access;
- AI usage;
- synchronization;
- sharing;
- retention;
- export;
- backup;
- deletion;
- review;
- audit.

The classification model may later become more detailed.

The architectural rule is stable:

> Data treatment must be justified by classification and purpose, not by Product convenience.

---

## 6. Formal Source of Truth Must Remain Explicit

Workplace may expose information from many locations.

The system must still know which source is authoritative for each formal fact.

Potential representations include:

- authoritative Core Object;
- Owning Service record;
- official external evidence;
- Product projection;
- local cache;
- imported spreadsheet;
- AI extraction;
- user note;
- derived summary;
- synchronized replica.

These representations are not equal.

For example:

```text
Local spreadsheet says:
Filed

Official evidence says:
Application received

Owning Service says:
Submission pending verification
```

The local spreadsheet does not become authoritative merely because it is convenient.

A Product projection does not become authoritative because it is visually prominent.

An AI summary does not become authoritative because it is accurate most of the time.

The system should preserve:

```text
authoritative source

source version

retrieval or synchronization time

verification state

derived representations

known conflicts

last confirmed state
```

The core distinction is:

```text
Where the data is visible
≠
which source owns the fact
```

This principle becomes especially important when Local Vault, offline operation, import, synchronization, and cross-Product projections coexist.

---

## 7. Local Vault Is a Logical Local or Private Boundary

Local Vault is the logical local or private technical boundary through which a Workplace may retain, index, process, cache, or protect authorized data outside a broadly shared environment.

A Local Vault may support:

- local files;
- local databases;
- local search indexes;
- local case libraries;
- local knowledge references;
- private caches;
- large source datasets;
- browser-based workflows;
- device-bound credentials;
- local AI inference or retrieval;
- offline work;
- local rendering;
- staged synchronization.

The central definition is:

> Local Vault is an organization-governed local or private data and execution boundary, not a second Core and not an automatically authoritative system of record.

The logical relationship is:

```text
Workplace Policy
        ↓
Local Vault Boundary
        ↓
Authorized local storage, retrieval, processing, and synchronization
```

Local Vault may exist:

- on one professional’s computer;
- on an organization-managed workstation;
- on a local server;
- in a private network;
- in an organization-controlled cloud environment;
- in a hybrid arrangement.

The exact form is an implementation decision.

Book 04 defines why the boundary exists and how it must be governed.

It does not define the technical product.

---

## 8. Local Vault Must Not Become a Second Core

Local Vault may store or process information related to Core Objects.

That does not make it authoritative for Core meaning or formal lifecycle.

It may contain:

- cached Matter records;
- local copies of Documents;
- offline Task projections;
- local Communication drafts;
- local evidence indexes;
- locally generated recommendations;
- synchronized organization profiles.

But it must not silently redefine:

- Matter status;
- Task status;
- Communication status;
- Review outcome;
- Event meaning;
- Permission;
- Policy;
- Business Responsibility;
- formal filing state;
- payment state;
- provider appointment;
- official outcome.

The correct model is:

```text
Core and Owning Services
→ define and mutate formal facts

Local Vault
→ stores, processes, caches, indexes, or prepares
authorized local representations
```

In a future self-hosted deployment, an Owning Service might itself run locally.

That is possible.

But authority would arise from the Owning Service role and contract, not merely from local location.

The distinction is:

```text
Local deployment of authority
≠
authority created by locality
```

This prevents Local Vault from becoming an uncontrolled duplicate system.

---

## 9. Local Does Not Mean Ungoverned

Keeping data local may reduce some exposure.

It does not remove governance obligations.

Local information may still require:

- user identity;
- device identity;
- organization context;
- permission;
- policy;
- access logging;
- classification;
- encryption;
- versioning;
- retention;
- deletion;
- backup;
- conflict handling;
- professional review;
- audit.

A local database can still be copied.

A local browser credential can still be misused.

A local AI model can still receive excessive client context.

A local working file can still be delivered to the wrong recipient.

A local cache can still remain after access is revoked.

The correct rule is:

```text
Local
=
a location and control characteristic

Local
≠
outside MarkOrbit governance
```

Workplace policy should determine who may unlock or use Local Vault, which Products may consume it, which AI Agents may access it, and what may leave it.

Local-first should strengthen autonomy and privacy.

It must not become a justification for invisible or untraceable professional action.

---

## 10. What May Appropriately Remain Local

Some information may remain local because of sensitivity, scale, performance, source restrictions, or operational need.

Examples include:

### Large raw datasets

Trademark office bulk files, historical archives, crawled source material, and large databases may be expensive or unnecessary to synchronize fully.

### Raw evidence and source files

High-volume or highly sensitive evidence may remain local while authorized references, hashes, metadata, or approved extracts are synchronized.

### Local case libraries

An organization may maintain a private case library or historical archive for retrieval and learning.

### Browser sessions and device-bound credentials

Credentials for portals, email, publishing tools, or official systems may be safer when device-bound and not broadly synchronized.

### Personal working materials

Early drafts, notes, scratch analysis, temporary exports, and local preparation may remain local until the user intentionally promotes or submits them.

### Local indexes and embeddings

Search indexes or embeddings may be derived locally to improve retrieval without uploading all source content.

### Private AI Context

Sensitive context may be assembled and processed locally where policy and capability allow.

### Rendered or temporary outputs

Large media files, temporary renders, previews, and exports may remain local unless Delivery or shared review requires them.

The principle is not:

```text
Keep everything local.
```

It is:

```text
Keep raw or sensitive information local
when broader synchronization is unnecessary
and authorized purpose can be achieved through a safer representation.
```

---

## 11. Synchronization Is a Governed Transfer

Synchronization is often treated as a purely technical process.

In MarkOrbit, synchronization is a governed transfer between authorized representations or environments.

It may involve:

- new data;
- changed data;
- metadata;
- references;
- approved summaries;
- derived values;
- versions;
- deletion instructions;
- revocation;
- conflict records;
- audit receipts.

The central definition is:

> Authorized synchronization is the policy-controlled movement or reconciliation of approved data representations across defined boundaries while preserving authority, scope, provenance, version, and downstream restrictions.

Synchronization must answer:

```text
What is moving?

From where?

To where?

Under whose authority?

For which purpose?

At what classification?

In which representation?

Which version?

Which fields are omitted?

Which downstream uses are allowed?

What must be logged?

What happens when access is revoked?
```

A synchronization engine may automate transport.

It must not decide professional legitimacy by itself.

---

## 12. Synchronization Modes Must Be Explicit

Not every data type requires the same synchronization depth.

Book 04 recognizes several logical synchronization modes.

These are architecture patterns, not mandatory protocol names.

### 12.1 No Synchronization

The information remains in its current boundary.

Only the existence of the boundary may be known elsewhere.

Examples may include:

- device-bound secrets;
- highly sensitive raw evidence;
- private personal notes;
- restricted local source archives.

### 12.2 Reference Only

Only a stable reference or locator is shared.

The receiving environment knows that the item exists but does not receive its metadata or content beyond the allowed reference.

### 12.3 Metadata Only

Approved metadata is synchronized without substantive content.

Examples may include:

- file name;
- type;
- size;
- date;
- owner;
- classification;
- source;
- version;
- local availability.

Metadata may still be sensitive and must be classified.

### 12.4 Safe Summary

A policy-filtered summary is synchronized instead of raw content.

The summary must preserve source and limitations.

### 12.5 Derived Value Only

A derived value is synchronized without raw source content.

Examples may include:

- count;
- risk indicator;
- deadline candidate;
- capability evidence summary;
- document completeness result;
- recommendation candidate.

Derived value is not automatically safe.

It may reveal sensitive facts or encode errors from the source.

### 12.6 Selective Content

Only approved fields, sections, pages, records, or extracts are synchronized.

This supports data minimization.

### 12.7 Authorized Full Content

Full content is synchronized because the receiving environment requires it and has appropriate permission, policy, purpose, retention, and security.

### 12.8 Explicit Export or Delivery

The information is packaged for a defined recipient or destination rather than maintained as a continuing synchronized replica.

This is closer to controlled export or Delivery than ongoing synchronization.

The modes can be summarized as:

```text
No Sync

Reference Only

Metadata Only

Safe Summary

Derived Value Only

Selective Content

Authorized Full Content

Explicit Export or Delivery
```

A future implementation may use terms such as Raw Sync, Metadata Sync, or Value Only.

The architecture must still preserve the distinctions above.

---

## 13. Metadata Can Be Sensitive

Metadata is often treated as harmless.

In professional services, metadata may reveal:

- client identity;
- Matter existence;
- filing strategy;
- provider relationship;
- dispute status;
- document type;
- evidence volume;
- deadline;
- fee level;
- communication pattern;
- professional activity;
- geographic scope.

For example:

```text
File:
Draft_Opposition_Response_ClientX.pdf

Metadata only:
title, client, dispute type, creation date, reviewer
```

Even without the document content, the metadata may expose confidential facts.

Therefore:

```text
Metadata Only
≠
No Risk
```

Metadata synchronization must still consider:

- classification;
- purpose;
- recipient;
- field minimization;
- retention;
- network visibility;
- AI access;
- audit.

This is particularly important for Local Vault indexes and cross-Product search.

---

## 14. Derived Value Can Preserve or Amplify Sensitivity

Derived values may appear safer because they do not include raw content.

But a derived value may still reveal or amplify sensitive information.

Examples include:

- high litigation risk;
- likely client churn;
- provider reliability concern;
- insufficient evidence;
- expected filing failure;
- unpaid balance;
- approaching critical deadline;
- suspected conflict;
- confidential commercial priority.

A derived value may also hide uncertainty.

The receiving user may see a simple score without understanding:

- source quality;
- missing context;
- model limitation;
- version;
- transformation logic;
- review status.

Therefore:

```text
Derived Value Only
≠
Automatically Shareable
```

Derived values should preserve, where relevant:

- source references;
- generating method;
- version;
- confidence;
- limitations;
- candidate status;
- review requirement;
- classification;
- allowed use.

Value Factory and Intelligence may create candidates.

Workplace policy still determines whether they may cross a data boundary.

---

## 15. Synchronization Policy Must Be Contextual

Synchronization should not be controlled by one global on/off switch.

A decision may depend on:

- organization;
- user;
- role;
- Product;
- client;
- Matter;
- data classification;
- source;
- authority;
- size;
- residency requirement;
- contractual restriction;
- legal obligation;
- AI use;
- recipient;
- retention;
- network context;
- current risk.

A conceptual decision can be expressed as:

```text
Sync Decision
=
Source Boundary
+ Target Boundary
+ Data Classification
+ Purpose
+ Permission
+ Policy
+ Representation
+ Retention
+ Audit Requirement
```

Examples:

```text
Public trademark bulk file
→ remain local
→ synchronize normalized metadata and provenance

Client evidence archive
→ remain local
→ synchronize approved references and completeness status

Provider quotation email
→ organization private
→ synchronize selected fee fields for authorized quotation preparation

Personal working note
→ no synchronization
→ may later be promoted into reviewed organizational memory

Approved filing package
→ selective or full synchronization
→ only into authorized Matter and Execution context
```

The policy should be specific enough to explain why movement occurred.

---

## 16. Purpose Limitation and Data Minimization Apply to Synchronization

The fact that two environments belong to the same organization does not justify unrestricted synchronization.

A Product should receive only what it needs.

An AI Agent should receive only what its governed role requires.

A reviewer should receive the material needed for the review scope.

An MGSN participant should receive the minimum information needed to evaluate or perform the requested service.

A personal device should not receive all organization data merely because the user is a member.

The principle is:

```text
Same organization
≠
same purpose

Same Workplace
≠
unlimited synchronization

Authorized access
≠
maximum available data
```

Data minimization may be achieved through:

- references;
- field selection;
- redaction;
- safe summaries;
- derived values;
- time-limited access;
- on-demand retrieval;
- local processing;
- purpose-specific packages.

This protects privacy and improves clarity.

It also reduces the amount of context that AI or Products may misuse.

---

## 17. Synchronization Must Preserve Provenance and Version

Synchronized data must not lose its origin.

At minimum, a governed synchronized representation may need to preserve:

- source identity;
- source reference;
- source boundary;
- source version;
- synchronization time;
- synchronization mode;
- transforming actor or service;
- omitted fields;
- validation status;
- target boundary;
- authority status;
- conflict state;
- expiry or retention;
- audit correlation.

A synchronized summary should not appear to be the original source.

A local extract should not appear to be a validated shared Knowledge Asset.

A cached Product projection should not appear to be the current Owning Service record when it is stale.

The principle is:

```text
Movement must not erase origin.

Transformation must not erase transformation.

Caching must not erase freshness.
```

Historical professional work may depend on the version available at the time.

That version must remain explainable even after later synchronization or update.

---

## 18. Cache, Replica, and Authoritative Record Must Be Distinguishable

A Local Vault or Product may hold a copy for speed, offline access, search, or convenience.

That copy may be:

- cache;
- replica;
- projection;
- snapshot;
- export;
- working copy;
- authoritative record.

These forms must not be confused.

### Cache

A cache improves access and may be discarded or refreshed.

### Replica

A replica maintains an authorized copy of another source under synchronization rules.

### Projection

A projection contains selected fields or a purpose-specific view.

### Snapshot

A snapshot preserves state at a point in time.

### Export

An export is a packaged copy for a defined use.

### Working copy

A working copy supports preparation and may contain uncommitted changes.

### Authoritative record

An authoritative record is owned by the recognized source or Owning Service.

The system should be able to explain:

```text
Is this current?

Is this authoritative?

Can it be edited here?

Will changes synchronize?

What happens if it conflicts?

May it be used offline?

What is the source?
```

Without these distinctions, local-first operation can create silent divergence.

---

## 19. Offline Work Must Remain Bounded

Local Vault may support offline or degraded operation.

Offline capability can be valuable when:

- travel disrupts connectivity;
- external systems are unavailable;
- large local datasets are used;
- private analysis should remain local;
- work must continue during temporary service failure.

But offline work creates risks:

- stale data;
- outdated Permission;
- changed Policy;
- duplicate action;
- conflicting edits;
- expired review;
- missed revocation;
- duplicate Communication;
- repeated filing or payment;
- uncertain official status.

Offline operation should therefore distinguish:

```text
Read cached context

Prepare local draft

Record local observation

Queue synchronization request

Perform protected action
```

The first four may be allowed under policy.

The last must remain governed and may require reconnection, revalidation, current Permission, current Policy, current state, Human Review, and the proper Owning Service.

The principle is:

```text
Offline preparation may continue.

Protected authority must not be inferred from stale context.
```

---

## 20. Conflict Detection Must Precede Silent Overwrite

Synchronization may produce conflicting changes.

Examples include:

- local draft changed while shared draft changed;
- client instruction updated in another Product;
- provider fee changed after local quotation preparation;
- a user edited a local Matter note after losing access;
- one record was deleted while another copy was updated;
- a local identity merge conflicts with the shared identity model;
- an offline Task projection appears open after the Task was cancelled.

The system must not silently choose the newest timestamp in every case.

Conflict handling may consider:

- authority;
- object ownership;
- version;
- actor;
- scope;
- classification;
- review status;
- effective time;
- transformation type;
- materiality;
- Policy.

Possible outcomes include:

```text
accept authoritative source

retain local working copy separately

create conflict record

request human resolution

merge non-conflicting fields

reject synchronization

quarantine the change

invalidate prepared action
```

A local copy should not overwrite an Owning Service record merely because its timestamp is later.

Conflict resolution must preserve history and trace.

---

## 21. Revocation Must Affect Local and Synchronized Access

Access changes over time.

A user may:

- leave the organization;
- change roles;
- lose client access;
- be removed from a Matter;
- lose Product entitlement;
- lose reviewer eligibility;
- have an Agent Contract suspended;
- have a device revoked.

A data architecture must account for copies that already exist.

Revocation may require:

- preventing future synchronization;
- invalidating credentials;
- removing local decryption access;
- disabling local indexes;
- marking cached data unavailable;
- deleting or quarantining local copies where required;
- preventing AI access;
- invalidating pending prepared actions;
- recording unresolved device risk;
- preserving required audit evidence.

Revocation is not complete merely because the central account was disabled.

The system must distinguish:

```text
permission revoked

access blocked centrally

local copy removed

local key invalidated

device confirmed

retention exception applied

audit preserved
```

These may occur at different times.

The architecture should not claim complete deletion or revocation without evidence.

---

## 22. Retention, Deletion, and Legal Hold Must Travel with the Data

Synchronization creates multiple representations.

Retention obligations must remain understandable across them.

A data item may be subject to:

- organization retention policy;
- client instruction;
- professional record obligation;
- legal hold;
- dispute preservation;
- contractual deletion;
- security incident hold;
- backup retention;
- audit retention;
- personal deletion request.

Deletion is not one operation.

It may involve:

```text
remove active access

delete working copy

delete synchronized replica

expire cached projection

remove search index

remove derived embedding

invalidate reference

retain required audit trace

retain legal-hold copy

record deletion outcome
```

A derived summary or embedding may still contain information from a deleted source.

Deletion policy must therefore consider derived representations.

The principle is:

```text
Data lifecycle follows the information,
not only the original file.
```

Book 04 does not define exact retention periods.

It requires that retention, deletion, and legal-hold rules remain explicit and enforceable across authorized locations.

---

## 23. Backup Is Not Ordinary Access

Backups support recovery.

They should not become shadow operational systems.

A backup may contain:

- historical client data;
- deleted records;
- old credentials;
- superseded drafts;
- restricted evidence;
- prior organizational context.

Backup access should therefore be limited.

The architecture must distinguish:

```text
operational copy

synchronized replica

archive

backup

legal-hold copy
```

Restoration should not silently reintroduce:

- revoked access;
- deleted user accounts;
- outdated Permission;
- superseded policies;
- expired credentials;
- stale Tasks;
- invalid reviews;
- cancelled Communications.

Recovery must reconcile restored data with current authority and governance.

Backup is a resilience mechanism.

It is not a reason to bypass current policy.

---

## 24. Credentials and Secrets Require a Separate Boundary

Some data should not enter ordinary Workplace context at all.

Examples include:

- passwords;
- API keys;
- session cookies;
- signing keys;
- authentication tokens;
- portal recovery codes;
- email credentials;
- payment credentials;
- local encryption keys.

Credentials may be needed for local browser automation, connectors, publishing tools, official portals, or integrations.

But they must not be treated as:

- ordinary Knowledge;
- AI Context;
- Product configuration visible to broad roles;
- synchronized client data;
- network exchange data;
- Artifact content.

A credential boundary should consider:

- device or organization scope;
- approved user;
- approved tool;
- approved action;
- expiry;
- revocation;
- rotation;
- audit;
- non-exportability where possible.

The architectural rule is:

```text
Tool may be authorized to use a credential.

User, Product, or AI does not necessarily receive the credential value.
```

An AI Agent may request an allowed tool action.

It should not receive raw secrets merely because the tool is available.

---

## 25. Local and Cloud AI Must Use the Same Governance Model

AI processing may occur:

- in a shared cloud service;
- in an organization-controlled cloud environment;
- on a local server;
- on a user device;
- through a hybrid route.

Deployment location may affect privacy, performance, cost, and risk.

It does not remove the need for governance.

Both local and cloud AI require:

- Agent identity;
- Capability;
- Skill;
- authorized data scope;
- Permission;
- Policy;
- purpose;
- source trace;
- output mode;
- candidate status;
- Human Review where required;
- audit.

A local model must not receive unrestricted access merely because data does not leave the device.

A cloud model must not receive full Workplace context merely because the provider is approved.

A routing decision may consider:

- classification;
- model capability;
- data residency;
- latency;
- source size;
- cost;
- professional risk;
- local availability;
- organization policy;
- required tools.

The principle is:

```text
Deployment determines where AI runs.

Governance determines what AI may know and do.
```

---

## 26. Personal AI Clone Context Must Remain Private by Default

Lite may present a personalized AI clone, Personal Assistant, Today experience, and goal-specific Guides.

Personalization may use:

- user preferences;
- writing style;
- work habits;
- personal notes;
- prior accepted suggestions;
- interaction history;
- role context;
- organization context.

This context must remain bounded.

A personal AI clone must not become:

- an unrestricted copy of organization memory;
- a portable container of client confidential data;
- a mechanism for carrying one organization’s context into another;
- an owner of formal professional history;
- a hidden synchronization channel.

When the user changes organization, role, client, or Product context, the available memory and data scope may change.

Personal context should be private by default and shared with the organization only through explicit policy or promotion.

The distinction is:

```text
Personalization
≠
ownership of organizational context

Personal continuity
≠
cross-organization data portability
```

---

## 27. Product Access Does Not Authorize Data Synchronization

An organization may enable Lite, MarkReg, MGSN interfaces, and other Products.

Product entitlement means the Product may be used.

It does not mean the Product may synchronize all Workplace data.

Each Product should receive only authorized context.

Examples:

### Lite

Lite may receive Today items, selected client context, private knowledge references, approved preferences, and prepared-action context.

It does not require every raw Matter file or provider record.

### MarkReg

MarkReg may receive client, trademark, service, filing, Document, Matter, and provider context required for the trademark lifecycle.

It does not automatically receive personal content history or unrelated private notes.

### MGSN interfaces

MGSN may receive authorized network identity, capability need, selected evidence, and collaboration context.

It does not receive the organization’s full client list, private pricing, or complete provider evaluations.

Cross-Product continuity should use stable references and authorized context handoffs.

It should not rely on indiscriminate replication.

The rule is:

```text
Product enabled
≠
all organization data synchronized
```

---

## 28. Cross-Product Continuity Requires Explicit Handoff

Work may begin in one Product and continue in another.

For example:

```text
Lite identifies a possible client need.

The user confirms the direction.

MarkReg prepares a formal trademark service journey.

MGSN helps identify an external capability.

Execution coordinates review and authorized action.
```

The handoff may require:

- organization reference;
- user and role context;
- client reference;
- purpose;
- selected recommendation;
- source references;
- permission and policy context;
- private knowledge references;
- data classification;
- required review;
- intended Product;
- allowed retention.

The receiving Product should not reconstruct context from broad database access.

The handoff should be explicit and minimal.

A cross-Product handoff is not necessarily synchronization.

It may be a purpose-bound context package or stable reference.

Detailed Product embedding and lifecycle continuity are developed in Part IV.

The data rule established here is:

```text
Continuity requires sufficient authorized context.

Continuity does not require universal replication.
```

---

## 29. Cross-Workplace Exchange Must Be Minimal and Purpose-Specific

MGSN connects independent Workplaces.

Cross-Workplace exchange creates a stronger boundary than cross-Product use inside one organization.

A service request may require sharing:

- requesting organization identity;
- service need;
- jurisdiction;
- deadline;
- selected Matter facts;
- required Capability;
- approved documents;
- communication route;
- confidentiality restrictions.

It should not automatically share:

- full client history;
- unrelated Matters;
- private pricing strategy;
- internal provider criticism;
- organization memory;
- personal notes;
- unrestricted AI Context;
- entire evidence archive.

The exchange should distinguish:

```text
discovery context

evaluation context

selected-provider context

execution context

outcome context

trust-feedback context
```

Each stage may authorize different information.

A provider candidate does not need the same data as an appointed provider.

An appointed provider does not need all internal review context.

Outcome feedback does not require disclosure of the full client file.

The principle is:

```text
Cross-Orbit exchange expands only as authorized collaboration advances.
```

---

## 30. Network-Safe Capability Evidence Must Be Deliberately Produced

Capability evidence may arise from private organizational work.

Examples may include:

- completed Matter;
- response time;
- jurisdiction experience;
- review quality;
- outcome;
- professional qualification;
- collaboration history.

Private operational data must not be exposed directly as network evidence.

A network-safe representation may require:

- aggregation;
- redaction;
- validation;
- minimum sample size;
- client anonymization;
- purpose limitation;
- confidence;
- organization approval;
- reviewer approval;
- expiry.

The transformation can be expressed as:

```text
Private operational evidence
→ governed evidence candidate
→ validation
→ network-safe capability evidence
→ authorized network profile
```

This protects organizational and client confidentiality while supporting useful routing and trust.

The existence of a derived score does not justify sharing the underlying data.

---

## 31. Distributed Acquisition Workers Must Remain Governed

MarkOrbit may use distributed acquisition workers for public or authorized sources.

Workers may operate on:

- organization computers;
- local servers;
- cloud workers;
- dedicated acquisition nodes;
- browser-based collectors.

Their purpose may include:

- downloading public trademark data;
- collecting official updates;
- capturing authorized provider information;
- monitoring source changes;
- preparing local raw datasets;
- generating structured acquisition results.

A distributed worker is not an autonomous data owner.

It must operate under:

- source authorization;
- job definition;
- organization or system identity;
- allowed scope;
- rate and safety constraints;
- provenance;
- output boundary;
- failure handling;
- audit;
- retention.

Workers may return:

```text
raw content

metadata

structured information

change signal

safe summary

failure report
```

depending on policy.

The coordination architecture should use governed job contracts rather than uncontrolled scraping behavior.

This chapter does not define Mo Crawl implementation.

It establishes that distributed acquisition must respect Workplace data boundaries and Local Vault policy.

---

## 32. Export, Sharing, Delivery, Publish, and Synchronization Are Different

Several forms of data movement must remain distinct.

### Export

Export creates a copy for a defined destination or user-controlled purpose.

### Sharing

Sharing grants another actor access under a defined scope.

### Delivery

Delivery transmits an approved Artifact or outcome to a defined recipient.

### Publish

Publish makes approved content available to a broader audience.

### Synchronization

Synchronization maintains governed correspondence or movement between authorized representations.

### Backup

Backup creates a recovery copy.

These actions differ in:

- recipient;
- purpose;
- lifecycle;
- authority;
- revocation;
- retention;
- audit;
- downstream use.

The distinctions are:

```text
Synchronization ≠ Sharing

Sharing ≠ Delivery

Delivery ≠ Publish

Export ≠ Publish

Backup ≠ Operational Replica
```

Part V defines Artifact Delivery and Publish in more detail.

This chapter defines only the data-boundary implications.

---

## 33. Portability Must Preserve Organizational Autonomy

An independent Orbit should not become trapped in shared infrastructure.

The organization should be able to obtain authorized representations of its own data, subject to:

- client rights;
- legal obligations;
- provider rights;
- shared Knowledge licensing;
- audit integrity;
- credential restrictions;
- deletion and retention rules;
- third-party source terms.

Portability may include:

- organization profile;
- client relationship data;
- private knowledge;
- organization memory;
- Product configuration;
- Artifact history;
- approved Documents;
- partner relationships;
- local references;
- audit exports where appropriate.

Portability does not mean every shared asset becomes organization-owned.

It means the organization can preserve operational continuity and control of its professional environment.

The principle is:

```text
Shared infrastructure may host the Orbit.

It must not imprison the Orbit.
```

Migration should preserve:

- references;
- versions;
- provenance;
- classifications;
- authority status;
- review history;
- retention obligations.

---

## 34. Audit Must Explain Data Movement Without Exposing the Data

Professional and security governance require traceability.

A data-movement audit may need to answer:

```text
Who requested the movement?

Which organization and user context applied?

What data classification was involved?

Which source and target boundaries were used?

Which synchronization mode was applied?

Which fields were omitted?

Which Permission and Policy decisions applied?

Which version moved?

Was the operation successful?

Was a conflict detected?

Was access later revoked?

Was deletion confirmed?
```

Audit should not reproduce all sensitive content merely to prove movement.

It should preserve sufficient evidence while respecting restricted data.

For AI-related movement, audit may also identify:

- Agent identity;
- Skill or tool;
- data access scope;
- local or cloud processing route;
- output mode;
- source references;
- restricted fields omitted;
- Human Review requirement.

Audit supports accountability.

It must not become another uncontrolled copy of the protected information.

---

## 35. Data Boundary Failures Must Be Visible

A synchronization or access failure may affect professional work.

Examples include:

- stale client instruction;
- missing local file;
- failed upload;
- partial synchronization;
- outdated fee data;
- deleted source still referenced;
- revoked user retaining local access;
- conflict not resolved;
- local index using superseded knowledge;
- AI output based on incomplete context;
- external provider missing an approved document.

Failures should be visible in the appropriate operating surface.

A safe result may include:

- warning;
- missing-context marker;
- stale-data marker;
- blocked action;
- review request;
- synchronization retry;
- conflict record;
- local-only indicator;
- authority uncertainty;
- escalation.

The system must not hide a failure by showing the last available value as current.

The principle is:

```text
Known stale data must appear stale.

Known missing data must appear missing.

Known conflict must not appear resolved.
```

Book 03 governs operational retry and safe failure where Execution is involved.

Workplace makes the relevant state visible without inventing replacement lifecycle semantics.

---

## 36. The Minimum Data Boundary and Synchronization Model

A minimum conceptual model can be expressed as:

```text
Data Item or Representation
  │
  ├── subject and source
  ├── organization and client scope
  ├── classification
  ├── authority status
  ├── current location
  ├── permitted actors
  ├── permitted purposes
  ├── permitted Products and Agents
  ├── retention and deletion
  ├── synchronization mode
  └── provenance and audit
        │
        ▼
Workplace Data Policy
        │
        ├── allow local use
        ├── allow Product access
        ├── allow AI access
        ├── allow synchronization
        ├── allow sharing
        ├── require redaction
        ├── require review
        ├── restrict retention
        └── deny or quarantine
        │
        ▼
Authorized Representation or Safe Rejection
```

Local Vault participates as one possible boundary:

```text
Authoritative Source or Approved Input
        │
        ▼
Local Vault
        │
        ├── local store
        ├── local index
        ├── local processing
        ├── local working copy
        ├── local credential boundary
        └── staged synchronization
        │
        ▼
Reference / Metadata / Summary / Derived Value /
Selective Content / Authorized Full Content
        │
        ▼
Authorized Product, Service, Workplace, or Network Context
```

This model is architectural.

It does not define classes, tables, APIs, queues, or services.

---

## 37. Required Distinctions

This chapter establishes the following required distinctions.

```text
Data classification ≠ storage location
```

Sensitivity and allowed use do not follow automatically from where data is stored.

```text
Data ownership or control ≠ custody
```

A platform or device may hold data without owning the professional relationship or use rights.

```text
Custody ≠ formal authority
```

Holding a copy does not make the holder authoritative for the fact.

```text
Local Vault ≠ second Core
```

Local Vault stores and processes authorized local representations. Core and Owning Services retain semantic and mutation authority.

```text
Local copy ≠ source of truth
```

A local copy may be a cache, projection, snapshot, export, or working copy.

```text
Local ≠ ungoverned
```

Identity, Permission, Policy, retention, AI governance, and audit still apply.

```text
Synchronization ≠ unrestricted replication
```

Only an authorized representation may cross a defined boundary.

```text
Metadata Only ≠ no risk
```

Metadata may reveal confidential professional facts.

```text
Derived Value Only ≠ automatically safe
```

Derived values may preserve sensitivity, uncertainty, or error.

```text
Product access ≠ data synchronization authority
```

An enabled Product receives only purpose-bound context.

```text
AI location ≠ AI authority
```

Local or cloud deployment does not change professional governance.

```text
Backup ≠ operational access
```

Recovery copies must not bypass current policy.

```text
Export ≠ Publish
```

A controlled copy is not public release.

```text
Revocation requested ≠ local deletion confirmed
```

Access, key invalidation, copy removal, retention exceptions, and audit may differ.

---

## 38. Failure Modes This Chapter Prevents

### Cloud-by-default centralization

All organization and client data is synchronized to one central platform because it is technically convenient.

### Local-authority drift

A local file or database becomes treated as authoritative merely because users rely on it.

### Shadow Core

Local Vault creates alternative Matter, Task, Communication, Review, or Event meanings.

### Product overreach

A Product receives all Workplace data when only limited context is required.

### AI context flooding

An AI model receives broad organizational history without purpose, minimization, or permission.

### Credential leakage

Browser sessions or API keys become ordinary Product or AI context.

### Silent stale state

A cached or offline record appears current after the authoritative source changes.

### Timestamp overwrite

A newer local timestamp overwrites a more authoritative formal record.

### Metadata leakage

Confidential relationships or Matter existence are exposed through supposedly harmless metadata.

### Derived-value leakage

A score or summary exposes restricted information or hides uncertainty.

### Revocation gap

A user loses central access but retains usable local copies or credentials.

### Deletion illusion

The original file is deleted while synchronized summaries, indexes, backups, or embeddings remain.

### Network over-sharing

Provider discovery or collaboration exposes more client and organization context than necessary.

### Uncontrolled distributed acquisition

Local or distributed workers collect data without source authority, scope, provenance, or output policy.

### Vendor lock-in

The organization cannot preserve its own operational history or migrate its Workplace context.

These failures may be technically possible even in a secure system.

The purpose of the architecture is to make them non-conforming.

---

## 39. Minimum Conformance Rule

A conforming Workplace must preserve the following lock:

```text
Data is classified before movement.

Organization and client boundaries remain explicit.

Storage location does not define ownership or authority.

Core and Owning Services remain authoritative for formal facts.

Local Vault is a governed local or private boundary,
not a second Core.

Local information remains subject to identity,
Permission, Policy, retention, and audit.

Synchronization uses an explicit purpose and mode.

Only the minimum authorized representation moves.

Metadata and derived values remain classified.

Provenance, version, authority, and freshness remain visible.

Conflicts do not silently overwrite authoritative state.

Revocation, retention, deletion, and legal hold
apply across authorized representations.

Credentials remain outside ordinary Product and AI context.

Local and cloud AI follow the same governance model.

Cross-Product continuity does not require universal replication.

Cross-Workplace exchange remains minimal and purpose-specific.

The organization retains reasonable portability
of its own professional operating context.
```

A technically functional system that fails this lock does not conform to the Workplace architecture.

---

## 40. Chapter Boundary

This chapter defines:

- logical data boundaries;
- a minimum data-zone model;
- classification principles;
- ownership, custody, authority, and location distinctions;
- Local Vault architectural responsibility;
- authorized synchronization;
- synchronization modes;
- provenance and version requirements;
- cache, replica, projection, and authority distinctions;
- offline boundaries;
- conflict principles;
- revocation;
- retention and deletion;
- credential boundaries;
- local and cloud AI data governance;
- cross-Product and cross-Workplace data movement;
- portability;
- audit and failure visibility.

It does not define:

- database schema;
- file layout;
- local database engine;
- encryption algorithm;
- key-management implementation;
- synchronization protocol;
- conflict-resolution algorithm;
- cloud provider;
- deployment topology;
- backup product;
- device-management platform;
- exact retention periods;
- data-residency legal advice;
- connector implementation;
- Mo Crawl implementation;
- Local Vault Product requirements;
- AI model routing implementation;
- MGSN exchange schemas;
- production security certification.

Those decisions belong to future technical specifications, Product charters, security architecture, legal review, implementation ADRs, and repositories.

This chapter does not modify Book 02 Core semantics.

It does not modify Book 03 Execution authority.

It does not authorize external send, filing, payment, provider appointment, provider instruction, official recordal, autonomous AI action, or unrestricted cross-Workplace data exchange.

---

## 41. Chapter Conclusion

Part II began by asking how an independent professional organization becomes a coherent operating environment inside MarkOrbit.

The answer now includes:

```text
Organization identity and Workplace Context

People, roles, permissions, and accountability

Clients, relationships, services, and business rules

Private knowledge, AI Context, preferences, and memory

Work, review, Communication, and operating surfaces

Data boundaries, Local Vault, and authorized synchronization
```

The organization’s operating environment is therefore not one database and not one Product.

It is a governed context in which identity, responsibility, relationships, knowledge, work, and data movement remain coherent.

Local Vault gives the organization a logical local or private boundary.

It may retain large, sensitive, device-bound, or locally useful information.

It may support local retrieval, private processing, offline preparation, and staged synchronization.

But Local Vault does not become a second Core.

A copy does not become authoritative because it is local.

A cloud record does not become platform-owned because it is hosted centrally.

Synchronization does not justify full replication.

Metadata and derived values do not become safe automatically.

AI deployment does not determine AI authority.

The architecture can be summarized as:

```text
Classify
→ authorize
→ minimize
→ locate
→ process
→ synchronize deliberately
→ preserve provenance
→ resolve conflict
→ retain or delete under policy
→ audit
```

The constitutional outcome is:

> Each Workplace controls how its information remains local, private, shared, synchronized, or exchanged while Core authority, governed Execution, Product independence, professional responsibility, and organizational autonomy remain intact.

This completes Part II.

The next part turns from organization context to consumption:

```text
How does Workplace discover, assemble, evaluate, and use
information, knowledge, intelligence, capabilities, Skills,
Assistants, Guides, AI Agents, recommendations, and governed Execution?
```
