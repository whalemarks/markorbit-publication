# B05-CH-40 — Changes, Recordals and Ownership Updates

**Status:** Part VI Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part VI — Registration and Portfolio Continuity

## Chapter Purpose

Official records may need correction or updating after filing or registration. A business fact, signed document, internal master-data change and official recordal are not the same event.

The central progression is:

```text
Detected Change
→ Recordal Context
→ Requirement Set
→ Recordal Package Candidate
→ Review and Approval
→ Governed Filing
→ Official Acknowledgement
→ Updated Right Baseline
```

```text
Internal Data Update
≠ Signed Change Document
≠ Recordal Filed
≠ Official Record Updated
```

---

## 1. User Question and Primary Action

**User question:** Which official records are wrong or outdated, what legal event caused the change, and what filing is required in each jurisdiction?

**Primary action:** Confirm the change event and affected rights, resolve evidence and authority requirements, and approve the jurisdiction-specific Recordal Package Candidate.

---

## 2. Change Types Must Remain Distinct

Possible contexts include:

- owner name change without change of legal identity;
- owner address change;
- representative or address-for-service change;
- correction of clerical error;
- limitation of goods or services;
- change of legal form;
- merger;
- assignment or transfer;
- licence recordal;
- security interest;
- cancellation of a prior recordal;
- change following court or administrative decision.

The Product should not treat all of these as a generic `owner update`.

---

## 3. Recordal Context

Each Recordal Context should preserve:

- change type;
- affected party or right;
- previous value;
- proposed value;
- effective date;
- factual source;
- legal basis;
- supporting Documents;
- affected jurisdictions and rights;
- urgency and deadline;
- pending proceedings;
- authority and signatory;
- provider need;
- source jurisdiction-pack version;
- unresolved conflicts.

---

## 4. One Business Event May Require Many Official Actions

A corporate name change may affect:

- several jurisdictions;
- applications and registrations;
- different owner identifiers;
- pending oppositions;
- local representatives;
- renewal filings;
- licences and security interests.

The Product may present one portfolio initiative while preserving each official filing as an independent governed action.

---

## 5. Requirement Set

Recordal requirements may include:

- change certificate;
- registry extract;
- merger document;
- assignment instrument;
- POA;
- declaration;
- notarization;
- legalization or apostille;
- certified translation;
- original document;
- consent from another party;
- official fee;
- local representative;
- chain-of-title evidence.

Each requirement should preserve source, format, language, validity, signature, certification and accepted-use status.

---

## 6. Previous and Proposed Values

The Product should show a precise diff:

```text
Official Current Value
→ Requested New Value
```

It should preserve:

- spelling and punctuation;
- original-language and translated value;
- address components;
- legal form;
- entity identifiers;
- affected owner or representative role;
- rights included and excluded.

A normalization for display should not silently become the filed value.

---

## 7. Recordal Package Candidate

The package should contain:

- Recordal Context reference;
- official right identifiers;
- current official data;
- proposed official data;
- change type and effective date;
- supporting Documents;
- statement or form content;
- signatory and authority;
- jurisdiction rules and source versions;
- fees and provider route;
- deadline and dependency;
- unresolved issue;
- package version;
- review and approval records.

---

## 8. Sequencing with Other Actions

Recordal may interact with:

- renewal;
- office-action response;
- opposition or cancellation;
- assignment completion;
- licence execution;
- enforcement;
- provider appointment;
- certificate correction.

The Product should allow:

```text
Recordal before other action
Recordal together with other action
Other action under current record
Parallel actions
Professional escalation required
```

The sequence is jurisdiction-specific and should be explicitly decided.

---

## 9. Approval and Authority

Recordal Approval should identify:

- package version;
- affected rights;
- current and proposed data;
- authority basis;
- Document set;
- fees;
- execution route;
- professional decision on sequencing;
- decision-maker;
- approval time;
- invalidation conditions.

An internal administrator changing a CRM record does not authorize an official recordal.

---

## 10. Official Acknowledgement and Partial Results

Possible results include:

- recordal accepted for all rights;
- accepted for some rights only;
- deficiency issued;
- additional evidence requested;
- owner data normalized by office;
- effective date changed;
- application updated but registration not updated;
- certificate reissue pending;
- recordal rejected;
- status unknown.

The Product should update each right independently and retain the requested-versus-recorded diff.

---

## 11. Reference Journey — RIVERKITE

One registration shows the predecessor company as owner, while the business asserts ownership transferred through an acquisition.

MarkReg creates:

```text
Recordal Context — Assignment
→ Requirement Set
→ Chain-of-Title Review
→ Recordal Package Candidate v3
```

The renewal and assignment recordal proceed in parallel under the jurisdiction-specific professional decision recorded in CH39.

The Product keeps three facts separate:

- current official owner;
- claimed beneficial or contractual owner;
- proposed owner after recordal.

It does not mark the assignee as official owner until the office acknowledges the recordal.

---

## 12. Reference Journey — EMBERLOOP

The UK Right Baseline contains a corrected address already reflected in the official record. No recordal is opened.

A later group-company reorganization is recorded only as a potential change signal until transaction documents and affected-right scope are confirmed.

---

## 13. Conformance Scenarios

### Scenario A — CRM name changed

**Given** the client updates its display name in Workplace  
**When** no legal change evidence exists  
**Then** the Product does not create or mark an official recordal as completed.

### Scenario B — One event affects many rights

**Given** a corporate name change across twelve jurisdictions  
**When** the initiative is created  
**Then** the Product may group the project but creates independent jurisdiction-specific packages, approvals and results.

### Scenario C — Office records unexpected normalization

**Given** the office accepts the change but formats the legal name differently  
**When** acknowledgement is received  
**Then** the Product preserves the requested value, official recorded value and professional assessment.

### Scenario D — Partial acceptance

**Given** one portfolio package covers five rights  
**When** three are accepted and two receive deficiencies  
**Then** each Right Baseline is updated independently and the overall initiative remains partially complete.

---

## 14. AI Assistance Boundary

AI may:

- classify change signals;
- compare official and proposed values;
- identify affected rights;
- extract supporting Documents;
- prepare candidate forms and diffs;
- summarize sequencing options.

AI may not:

- decide legal identity continuity;
- establish ownership;
- sign change documents;
- approve sequencing;
- mark official data changed without acknowledgement;
- apply one jurisdiction rule universally.

---

## 15. Minimum Recordal Lock

```text
Business fact, internal data,
signed document, recordal package,
filed action and official update
remain distinct.

One portfolio event may require
many independent official actions.

Current, claimed and proposed ownership
must never be silently collapsed.
```

---

## 16. Handoff to Assignment and Chain of Title

The output is a versioned Recordal Context and, where approved, an acknowledged official update.

CH41 focuses on assignments, licences, mergers and the chain-of-title evidence needed to connect successive owners and authorized users.