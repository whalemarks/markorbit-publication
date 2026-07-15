# B06-CH-08 — Authorized Context, Sources and Data Boundaries

**Status:** Complete Draft 1  
**Chapter Map:** B06-TOC-V0.1 — Owner Accepted  
**Part:** Part II — The Daily Operating Model

## Chapter Purpose

This chapter defines the authorized context that MarkOrbit Lite may assemble before it observes, recommends, prepares or hands off work.

The central proposition is:

> Useful intelligence begins with the right context under the right identity, purpose, permission and data boundary.

Lite must not treat all available data as one undifferentiated pool.

It must know:

- who is acting;
- for which Organization;
- for which customer, trademark, Matter or business purpose;
- which sources support the context;
- which data may be viewed, transformed, synchronized, disclosed or handed off;
- which facts remain uncertain or restricted.

## 1. Context Is More Than Retrieved Information

A generic search system can return documents, records and text.

A professional Product must also know:

- whether the user is authorized to see them;
- whether the Organization controls them;
- whether they are current;
- whether they apply to the same customer, mark or Matter;
- whether they may be used for internal analysis only;
- whether they may support a client-facing Artifact;
- whether they may leave the local environment;
- whether a formal destination may receive them.

```text
available information
≠ authorized context
```

Authorized context is a purpose-bound assembly of identities, references, sources, restrictions and intended consequences.

## 2. Every Lite Session Begins With Acting Context

`ML-S01 Lite Session` should identify at least:

- active user;
- active Organization;
- Product mode;
- role and responsibility context;
- permitted customer, trademark and Matter scope;
- session start and expiry;
- relevant data and AI policy;
- available destinations.

The same person may participate in multiple Organizations.

They may act:

- as an independent professional;
- as a member of a small agency;
- as an external collaborator;
- under a client-specific engagement;
- in a personal learning or preparation mode.

Lite must not carry assumptions from one context into another silently.

```text
same user
≠ same Organization
≠ same permissions
≠ same client purpose
```

## 3. The Organization Remains the Professional and Commercial Center

Lite is individual-first, but it is not identity-free.

The active Organization provides context for:

- customer relationship ownership;
- service scope;
- business rules;
- pricing and commercial preferences;
- professional responsibility;
- internal review requirements;
- local and cloud policy;
- reusable assets and memory;
- approved external destinations.

A solo professional may operate an Organization of one.

The architectural principle remains the same:

> The work belongs to an accountable professional context, not to an unbounded AI persona.

## 4. Subject Context Must Be Explicit

A Lite journey may involve several subject types:

- Customer;
- Contact;
- Trademark;
- Brand or business unit;
- Matter;
- Order;
- Opportunity;
- document or Evidence reference;
- provider or jurisdiction context;
- prospective organization or person.

These subjects are not interchangeable.

A public company name may support a Prospect Candidate. It does not establish a Customer relationship.

A trademark record may support a service signal. It does not establish that a particular Contact is authorized to instruct.

A Matter reference may provide restricted context. It does not authorize the same facts for public content.

Lite should preserve the exact subject and the relationship among subjects.

## 5. Purpose Limits What Context Is Necessary

The same data may be appropriate for one purpose and excessive for another.

### Internal portfolio analysis

May require:

- customer and trademark references;
- status history;
- service history;
- internal notes;
- selected case context.

### Customer follow-up preparation

May require:

- recipient identity;
- relevant trademark facts;
- current service-value explanation;
- approved customer-facing claims;
- communication preference.

### Public content production

Should generally require less:

- approved public or reusable sources;
- no Client Restricted or Matter Restricted facts;
- audience and rights scope;
- approved brand elements.

### MarkReg Handoff

May require:

- applicant, customer and trademark context;
- identified need;
- sources;
- missing information;
- authority and destination details.

```text
more context
≠ better context
```

The Product should assemble the minimum useful context for the specific purpose.

## 6. Source Types Have Different Authority

Lite may consume several source classes.

### Official sources

Examples include official office records, notices and registers.

They may carry high authority for particular facts, but the Product must still preserve:

- retrieval time;
- jurisdiction;
- document or record version;
- interpretation limitations;
- superseded or corrected status.

### Organization-controlled sources

Examples include:

- customer records;
- internal service history;
- approved price lists;
- templates;
- notes;
- private case materials;
- organization policies.

These may be authoritative for organization practice, but not for law or official status.

### Client-provided sources

Examples include:

- business plans;
- product descriptions;
- ownership information;
- instructions;
- signed documents.

They may be critical to a Matter, but may contain unverified claims or restricted data.

### Provider and professional sources

Examples include:

- local counsel advice;
- service reports;
- provider quotations;
- professional assessments.

These require identity, date, scope and version.

### Public and market sources

Examples include:

- company websites;
- product launches;
- public directories;
- news;
- public contact channels.

They may support observations and prospects, but do not prove purchase intent, legal rights or channel permission.

### AI-generated or transformed content

AI output may summarize, extract, classify or propose.

It is never self-authorizing source truth.

## 7. Provenance Must Travel With the Context

A material Lite record should preserve:

- original source;
- source type;
- source owner or controller;
- retrieval or effective date;
- version;
- transformations;
- inferred versus explicit elements;
- confidence;
- known contradiction;
- intended purpose;
- allowed destination.

Provenance is not merely a citation field.

It allows the user and destination to decide:

- whether the information can be trusted;
- whether it is fresh enough;
- whether it can support a claim;
- whether it needs professional verification;
- whether it may be disclosed.

## 8. Freshness Is Contextual

Not every source becomes stale at the same rate.

A brand name approved by the Organization may remain stable for years.

A contact email may become stale quickly.

A provider quotation may expire.

An official status may change overnight.

A legal rule may be superseded.

A customer instruction may remain valid only for a defined Matter or period.

Lite therefore should not use one universal freshness threshold.

It should preserve:

- source date;
- expected review interval where known;
- expiry;
- later conflicting evidence;
- last verified time;
- action sensitivity.

A stale source may still be useful for history. It may not be sufficient for a consequential recommendation.

## 9. Data Classification Must Affect Product Behavior

A practical classification model may include:

```text
Public
Organization Internal
Personal Private
Client Restricted
Matter Restricted
Network Shared
Local Only
```

The labels alone are insufficient. Each classification should affect:

- who may view;
- which AI capability may use it;
- whether it may be synchronized;
- whether it may appear in a work product;
- whether it may be disclosed to a destination;
- whether it may support public publication;
- retention and deletion;
- review requirements.

### Public

May be broadly usable, subject to source quality, rights and purpose.

### Organization Internal

May support organization work but not necessarily external disclosure.

### Personal Private

May support the user’s continuity but must not silently become organization memory.

### Client Restricted

May be used only within the authorized client purpose.

### Matter Restricted

May have even narrower procedural or professional limits.

### Network Shared

May be disclosed only under the relevant MGSN or collaboration rules.

### Local Only

May be readable locally while remaining unavailable for cloud synchronization or external Handoff.

## 10. Local Access Does Not Imply Synchronization

A local file may be technically readable by an authorized component.

That does not mean it may be:

- uploaded;
- indexed centrally;
- used by a remote model;
- shared with the Organization;
- disclosed to a customer;
- included in a MarkReg or MGSN Handoff;
- retained after the session.

```text
local readability
≠ synchronization permission
≠ AI permission
≠ disclosure authority
```

A conforming Lite experience should preserve:

- local origin;
- allowed processing location;
- allowed transformations;
- synchronization state;
- destination limits;
- derived-content restrictions.

Hybrid minimization allows Lite to produce value without centralizing every raw source.

## 11. Private Data Must Not Become Platform Supply

Private customer, asset and relationship data has special risk.

The Product must not silently use:

- a user’s customer list as prospects for another user;
- private inquiries as platform opportunities;
- internal case facts as public content;
- private provider pricing as a general marketplace price;
- organization memory as shared Knowledge;
- local files as training or discovery data.

```text
visible to the platform
≠ available for platform development
```

Purpose limitation and controller identity must remain explicit.

## 12. Context Assembly Should Preserve Missing Information

A Product may infer that a customer and trademark record are related.

It should not hide that the relationship is uncertain.

Useful context should preserve:

- missing owner information;
- uncertain customer identity;
- unverified mark-to-product relationship;
- conflicting status;
- unknown contact permission;
- missing service history;
- unsupported legal conclusion.

A gap may produce:

- a request for information;
- a blocked candidate;
- a lower-confidence recommendation;
- an alternative path;
- a professional review requirement.

Filling every empty field with AI inference creates false certainty.

## 13. Context Is Assembled for a Journey, Not Stored as One Mega-Record

The early temptation is to create a universal Lite profile containing:

- every customer;
- every trademark;
- every case;
- every note;
- every preference;
- every opportunity;
- every generated content item.

This would collapse ownership, purpose and permission.

The better model is:

```text
stable external references
+ Product-local session and candidate state
+ purpose-bound context package
+ typed Handoff Envelope
```

The Product can preserve continuity without inventing a universal data owner.

## 14. Context Must Be Minimized Before Handoff

When Lite hands work to another destination, it should not send the entire user workspace.

A Handoff should include only what the destination needs:

- subject references;
- purpose;
- selected sources;
- selected Artifact Version;
- relevant authority context;
- unresolved questions;
- intended consequence;
- return address.

For MGSN, this may be a minimized Capability Need.

For MarkReg, it may be a service need and applicant/trademark context.

For Human Review, it may be an exact version and claims requiring decision.

For Communication, it may be the recipient, channel, draft and send consequence.

## 15. The Destination Must Revalidate

Even a well-formed context package does not compel the destination to accept it.

The destination may find:

- insufficient information;
- stale sources;
- permission problems;
- unsupported claims;
- missing formal objects;
- conflicting state;
- wrong destination;
- expired authority.

It may return:

```text
accepted
more_information_required
rejected
blocked
failed
formal_record_reference_returned
```

Lite should display the result without rewriting it.

## 16. Context Errors Need Correction, Not Hidden Replacement

When a user corrects:

- customer identity;
- mark ownership;
- contact status;
- source interpretation;
- relationship history;
- data classification;
- allowed destination;

Lite should record a scoped correction.

The correction may affect:

- the current Attention Item;
- related candidates;
- a work-product version;
- a future Preference or Memory Candidate;
- a pending Handoff.

It should not automatically rewrite formal source records that Lite does not own.

## 17. Minimum Conforming Authorized Context

A minimum conforming implementation should demonstrate:

1. active user and Organization context;
2. explicit subject references;
3. purpose-bound context assembly;
4. source type, version and freshness;
5. data classification and controller;
6. confidence and missing information;
7. local/synchronization distinction;
8. allowed destinations;
9. minimized Handoff context;
10. destination revalidation;
11. no private-to-platform leakage;
12. no claim that AI inference is source truth.

## Chapter Conclusion

MarkOrbit Lite can organize a professional’s day only when it knows which context is authorized, current, relevant and transferable.

```text
identity
+ purpose
+ source
+ permission
+ classification
+ freshness
+ destination
→ authorized context
```

The next chapter explains how a source observation becomes a signal and then a Service-Value Candidate without skipping these controls.