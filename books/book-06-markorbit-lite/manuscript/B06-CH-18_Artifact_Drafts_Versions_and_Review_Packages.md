# B06-CH-18 — Artifact Drafts, Versions and Review Packages

**Status:** Complete Draft 1  
**Chapter Map:** B06-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Professional Work Products  
**Primary controls:** ML-W02, ML-W03, ML-W04, ML-H05, ML-HC-03

## Chapter Purpose

This chapter defines the Artifact as a versioned business result and explains how immutable versions and exact-purpose Review Packages preserve professional responsibility.

The central proposition is:

> Versioning makes Review meaningful, and Review makes professional responsibility visible.

## 18.1 The Artifact is the business result

Structured Content becomes valuable when it is organized into a result that someone can inspect, review, use, deliver or publish.

That result is an Artifact.

Examples include:

- a customer portfolio recommendation;
- a quotation or service proposal;
- a trademark layout report;
- an examination-response explanation;
- a case summary;
- a customer-development package;
- a social image post;
- a short video project;
- an internal decision brief;
- a MarkReg launch-support package.

An Artifact is not defined by file format. It is defined by purpose, audience, source, version and intended use.

```text
PDF file alone ≠ Artifact
MP4 file alone ≠ Artifact
email body alone ≠ Artifact
Artifact may have one or more files or representations
```

## 18.2 `ML-W02` — Artifact Draft

An Artifact Draft is a business result under preparation.

It should identify:

- Artifact type;
- purpose;
- intended audience;
- active Organization;
- responsible user;
- subject references;
- Structured Content source;
- selected source versions;
- claim set;
- deterministic fields;
- missing information;
- data classification;
- allowed destinations;
- required Review;
- current draft state.

Draft states may include:

```text
assembling
incomplete
awaiting_source
awaiting_user_input
awaiting_review
revision_required
ready_for_version
blocked
retired
```

A draft can change. It is therefore unsuitable as the direct target of a consequential Review or external action unless the exact content is frozen into a version.

## 18.3 `ML-W03` — Artifact Version

An Artifact Version is an immutable snapshot of the business result.

It should preserve:

- version identifier;
- parent Artifact;
- exact content;
- exact deterministic fields;
- source references and versions;
- generated components;
- transformation history;
- renderer or representation intent;
- author and responsible user;
- timestamp;
- classification;
- intended audience;
- review state;
- permitted use;
- supersession and retirement state.

The version rule is simple:

```text
reviewed version
+ later edit
→ new version
```

The Product must never silently change a reviewed or selected Artifact Version.

## 18.4 Why immutability matters

Without immutable versions, Lite cannot reliably answer:

- What did the reviewer approve?
- What did the user confirm?
- What was sent to the customer?
- What was rendered?
- What was published?
- Which version produced the customer response?
- Which version contains the factual error?
- Which derivatives must be retired?

An editable “current document” is not enough for governed professional work.

## 18.5 Version identity across formats

One Artifact Version may have several representations:

```text
Artifact Version V3
├── HTML preview
├── PDF render
├── PNG carousel
├── MP4 render
└── plain-text Communication excerpt
```

The representations must remain linked to V3.

A representation that changes substantive content is not merely another format. It creates a new version or derivative Artifact.

Examples:

- converting a report to PDF without changing content: representation;
- shortening the report for a customer message: derivative or new version;
- adding a new legal claim in the video: new version;
- changing only image resolution: representation;
- changing the quoted price: new version.

## 18.6 Artifact is not Document or Evidence

A Document may be a formal record, received correspondence, filing material or controlled business document.

Evidence supports a claim, action or decision.

An Artifact is a Product result prepared for a purpose.

```text
customer certificate PDF
→ may be Document or Evidence

customer-facing certificate explanation
→ Artifact

case evidence bundle
→ Evidence

case-based training summary
→ Artifact
```

An Artifact may reference Documents or Evidence, but it does not absorb their ownership, authenticity or retention meaning.

## 18.7 Review is a defined professional act

Human Review is not the same as reading, editing or confirming.

Review should identify:

- exact Artifact Version;
- reviewer identity and role;
- review purpose;
- claims and issues under review;
- source set;
- audience and destination;
- decision requested;
- limitations;
- review result;
- conditions and expiry.

Possible results include:

```text
approved
approved_for_limited_purpose
approved_with_conditions
revision_required
rejected
blocked
insufficient_information
```

A general “looks good” reaction is insufficient for a high-risk professional Artifact when a formal Review is required.

## 18.8 `ML-W04` — Review Package

A Review Package contains the exact context required for the reviewer to make a bounded decision.

It should include:

- Artifact Version;
- purpose;
- audience;
- intended action;
- source references;
- factual claims;
- deterministic fields;
- generated content identification;
- missing information;
- uncertainty and contradiction;
- data restrictions;
- previous Review results;
- specific questions for the reviewer;
- deadline or expiry where relevant.

The Review Package should not force the reviewer to reconstruct the source trail manually.

## 18.9 Review scope must be explicit

Approval may be limited by:

- audience;
- jurisdiction;
- customer;
- channel;
- date;
- language;
- purpose;
- version;
- claim set;
- disclosure level.

For example:

```text
Approved for:
internal customer meeting preparation

Not approved for:
public publication or formal legal submission
```

Reusing the same Artifact outside the approved scope requires a new Review decision.

## 18.10 User confirmation is not Human Review

The user may confirm:

- recipient;
- channel;
- account;
- timing;
- selected option;
- external consequence.

A professional reviewer may approve:

- factual accuracy;
- legal or procedural reasoning;
- claim strength;
- confidentiality treatment;
- professional suitability.

These may be performed by the same human in a small practice, but the decisions remain conceptually distinct.

```text
user selects “send”
≠ professional claims reviewed
```

## 18.11 Review Handoff

When Review is provided by another service or role, Lite prepares `ML-H05 Review Handoff` under `ML-HC-03`.

Minimum package:

- exact Artifact/Action version;
- source set;
- claims;
- audience;
- intended purpose;
- decision requested;
- known issues;
- required return address.

The reviewer may return:

- approved;
- rejected;
- revisions required;
- limited approval;
- more information required.

Lite presents the result but does not invent approval when no typed result has returned.

## 18.12 Corrections and review invalidation

A correction may invalidate an earlier Review when it affects:

- a material fact;
- legal basis;
- customer identity;
- trademark status;
- date or deadline;
- quoted price;
- claim strength;
- audience or disclosure;
- required action.

The Product should then:

1. create a Correction Record;
2. identify affected Artifact Versions;
3. mark affected Reviews as superseded or invalid for the changed purpose;
4. create a new draft/version;
5. request new Review where required;
6. trace any external use of the affected version.

## 18.13 Template use does not remove version responsibility

Templates improve speed and consistency, but each produced result still needs:

- correct customer and trademark facts;
- current jurisdiction content;
- correct price and scope;
- appropriate disclosure;
- correct audience;
- version identity;
- review treatment.

```text
approved template
≠ every instance approved
```

The template may be a Reusable Asset. The customer-specific output is a separate Artifact Version.

## 18.14 Artifact lineage

Lite should preserve a lineage such as:

```text
Source Observation
→ Structured Content SC-4
→ Artifact Draft A-12
→ Artifact Version A-12/V1
→ Review Package RP-8
→ revision
→ Artifact Version A-12/V2
→ approved_for_customer_email
→ PDF Render R-21
→ Communication Package CP-6
```

This lineage enables:

- audit;
- correction;
- reuse;
- outcome attribution;
- rights management;
- retirement;
- later learning.

## 18.15 Readiness before rendering

An Artifact Version should not automatically proceed to rendering.

It may still be:

- incomplete;
- stale;
- unsupported;
- review required;
- blocked by rights;
- blocked by missing customer confirmation;
- blocked by deterministic-field mismatch.

Rendering a deficient version may make the deficiency look more credible, not less dangerous.

## 18.16 A practical Artifact and Review checklist

```text
Purpose and audience fixed?                 YES / NO
Exact version created?                      YES / NO
Source set and versions retained?           YES / NO
Deterministic fields verified?              YES / NO
Missing information visible?                YES / NO
Data classification preserved?              YES / NO
Generated content identified?               YES / NO
Review requirement known?                   YES / NO
Review scope and decision requested clear?  YES / NO
Approval result typed and linked?            YES / NO / N/A
Later edits create new version?              YES / NO
Allowed destinations known?                 YES / NO
```

## Chapter Conclusion

The Artifact is the versioned business result at the center of Lite’s professional production loop.

```text
Structured Content
→ Artifact Draft
→ immutable Artifact Version
→ Review Package
→ typed Review result
→ readiness for representation and use
```

Versioning makes Review meaningful. Review makes professional responsibility visible. Lineage makes later delivery, correction, reuse and learning trustworthy.

Without these controls, Lite would merely generate convincing files. With them, it can prepare professional work products whose purpose, facts, responsibility and history remain inspectable.