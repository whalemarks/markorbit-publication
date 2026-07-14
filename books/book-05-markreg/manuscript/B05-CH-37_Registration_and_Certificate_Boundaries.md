# B05-CH-37 — Registration and Certificate Boundaries

**Status:** Part VI Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part VI — Registration and Portfolio Continuity

## Chapter Purpose

Registration begins a new operating phase. It does not collapse the official record, certificate, Product projection, maintenance obligations, ownership state, evidence, and portfolio strategy into one object.

The central progression is:

```text
Sourced Registration Event
→ Registration Outcome Snapshot
→ Official Record Verification
→ Certificate Acquisition or Reference
→ Right Baseline
→ Maintenance and Portfolio Continuity
```

```text
Official Registration
≠ Certificate File
≠ Product Status Label
≠ Unqualified Ownership Conclusion
≠ Permanent Validity
```

---

## 1. User Question and Primary Action

**User question:** What exactly has been registered, according to which official source, and what must happen next?

**Primary action:** Verify the registration outcome, inspect the registered scope, confirm certificate and owner details, and accept the resulting Right Baseline for future work.

The Product must explain any mismatch between the expected filing scope and the official registration record.

---

## 2. Registration Must Begin from an Official Event

A Registration Outcome Snapshot should preserve:

- office and jurisdiction;
- application and registration identifiers;
- official event type;
- registration date;
- status effective date;
- registered owner;
- mark representation;
- classes and registered goods/services;
- limitations, disclaimers, conditions or exclusions;
- official source;
- retrieval time;
- evidence file or official URL reference;
- source confidence;
- unresolved conflict.

A provider report may trigger verification, but it does not replace the official registration event.

---

## 3. Registered Scope May Differ from Filed Scope

The Product should compare:

```text
Approved Filing Package
vs
Acknowledged Filing Record
vs
Registered Scope
```

Differences may include:

- deleted goods or services;
- narrowed wording;
- fewer classes;
- disclaimers;
- color or representation conditions;
- owner-name normalization;
- amended applicant details;
- priority changes;
- limitation resulting from examination or settlement.

The Product should produce a scope diff rather than silently marking the full original package as registered.

---

## 4. Registration Record, Certificate and Evidence Are Distinct

| Object | Meaning |
| --- | --- |
| official registration record | office-controlled record of the registered right |
| certificate | official or office-issued representation of registration |
| certificate file | received digital or scanned material |
| Evidence reference | governed evidence of the official event or document |
| Product projection | user-facing representation of the current known state |
| Right Baseline | controlled snapshot used for later lifecycle work |

A certificate may be delayed, replaced, corrected, reissued or electronic only.

The absence of a certificate file does not necessarily mean registration has not occurred. A certificate file alone does not prove that the current official record is unchanged.

---

## 5. Certificate Validation

Certificate handling should preserve:

- issuing office;
- certificate identifier where available;
- issue date;
- registered owner;
- registration number;
- mark and classes;
- language;
- electronic or paper form;
- source channel;
- file hash where appropriate;
- receipt date;
- corrected or replacement status;
- relationship to the official record.

The Product may identify likely inconsistencies. It should not certify authenticity by itself.

---

## 6. Owner Verification at Registration

The registered owner should be compared with:

- approved applicant;
- acknowledged filing owner;
- current client statement;
- corporate changes known during prosecution;
- pending assignment or recordal;
- group-company expectations.

If the official owner differs, the Product should not overwrite either value. It should create an ownership conflict and route it to professional review.

---

## 7. Registration Does Not Mean the Right Is Risk-Free

A registered right may still face:

- cancellation or invalidation;
- non-use vulnerability;
- opposition appeal or pending proceeding;
- ownership dispute;
- recordal deficiency;
- use declaration requirement;
- maintenance deadline;
- renewal deadline;
- limitation or disclaimer;
- local representative requirement;
- unpaid later-stage charge.

The Product should show active vulnerabilities separately from registration status.

---

## 8. Right Baseline

The canonical Product output is a versioned Right Baseline containing:

- official identity and jurisdiction;
- application and registration numbers;
- registered mark version;
- registered owner;
- registered scope;
- registration and priority dates;
- certificate state;
- current representative;
- active proceedings;
- known maintenance obligations;
- known use obligations;
- next verified deadline;
- source versions;
- unresolved conflicts;
- linked Matters, Documents and Evidence.

The Right Baseline is not a new official record. It is the controlled starting point for lifecycle continuity.

---

## 9. User Surface

The registration surface should show:

- **Registered according to:** source and retrieval time;
- **What was registered:** mark, owner, classes and scope;
- **What changed:** diff from the approved filing package;
- **Certificate:** available, pending, corrected, unavailable or not required;
- **Current vulnerabilities:** disputes, use, ownership or maintenance issues;
- **Next action:** confirm, request correction, obtain certificate, open recordal, create maintenance plan or escalate.

Primary actions may include:

```text
Accept Right Baseline
Request Professional Review
Report Owner Mismatch
Request Certificate Follow-Up
Open Correction or Recordal
Create Maintenance Plan
```

---

## 10. Reference Journey — EMBERLOOP

The UK application reaches a sourced registration event.

MarkReg compares the official record with the approved filing package and identifies that one item was narrowed during examination. It creates:

```text
Registration Outcome Snapshot v1
→ Scope Diff v1
→ Right Baseline UK v1
```

The electronic certificate is available and linked as an official Document reference. The Product shows the right as registered, but separately displays the future renewal date and use-related vulnerability timeline.

The EU application remains in opposition and is not included in the registered-right count. The US application remains under examination until a sourced registration event is received.

---

## 11. Conformance Scenarios

### Scenario A — Provider says registered, office record not checked

**Given** a provider reports registration  
**When** no official event or official record has been verified  
**Then** the Product records a provider-reported event and requires official verification before creating the final Right Baseline.

### Scenario B — Certificate scope differs from Product expectation

**Given** the certificate omits one filed item  
**When** the official record confirms the omission  
**Then** the Product creates a registered-scope diff and does not display the omitted item as registered.

### Scenario C — Owner mismatch

**Given** the official registration owner differs from the expected group company  
**When** the record is retrieved  
**Then** the Product creates an ownership conflict and does not silently replace the official or declared owner.

### Scenario D — Certificate unavailable

**Given** registration is confirmed by the official record  
**When** the certificate has not yet been issued  
**Then** the Product may create the Right Baseline while showing certificate state as pending.

---

## 12. AI Assistance Boundary

AI may:

- extract registration details;
- compare filing and registration scope;
- identify likely owner mismatches;
- classify certificate files;
- summarize limitations;
- propose follow-up tasks.

AI may not:

- create official registration;
- certify authenticity;
- decide ownership disputes;
- declare a challenged right secure;
- remove official limitations;
- invent missing certificate data.

---

## 13. Minimum Registration Lock

```text
Registration begins with sourced official evidence.

Official record, certificate,
certificate file, Evidence,
Product projection and Right Baseline
remain distinct.

Registered scope is compared
with the approved and filed scope.

Registration status does not erase
maintenance, use, ownership,
dispute or vulnerability conditions.
```

---

## 14. Handoff to Maintenance

The output is a versioned Right Baseline and Registration Outcome Snapshot.

CH38 turns that baseline into a source-backed Maintenance Obligation Set and calendar without treating a calculated reminder as an official deadline.