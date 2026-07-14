# B05-CH-23 — Filing Package as a Governed Artifact

**Status:** Part IV Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

Part III ends with a validated Handoff Envelope and formal Order, Matter, payment, responsibility, and Execution references.

CH23 defines the next Product artifact:

> What exact, versioned content is proposed for filing, from which sources, under which unresolved conditions, and for which jurisdiction, filing unit, applicant, and route?

The answer is the **Filing Package Candidate** defined as `MR-A11` in [B05-SPEC-0001](../specifications/B05-SPEC-0001_Product_Artifact_and_Decision_Map.md).

```text
Approved journey inputs
+ jurisdiction-pack version
+ formal Documents and accepted source materials
+ filing-specific content
+ unresolved warnings
→ Filing Package Candidate
```

A Filing Package Candidate is not Filing Approval, provider instruction, submission, official acknowledgement, or official truth. This preserves `MR-CR-02` through `MR-CR-05`.

---

## 1. User Question and Primary Action

**User question:** What exactly will be filed?

**Primary action:** Review the package summary, resolve identified differences, and confirm the factual content that the user is authorized to confirm.

The user should see one package version, not a collection of unrelated form fields.

---

## 2. Required Inputs

A Filing Package Candidate must reference exact versions of:

- Commercial Instruction;
- Formal Intake;
- Requirement Set;
- Readiness Assessment;
- filing unit;
- applicant and authority context;
- classes and goods/services;
- jurisdiction and filing route;
- priority claim where applicable;
- accepted Documents and source materials;
- responsible professional;
- applicable jurisdiction pack;
- relevant Order, Matter, and Execution references.

It must not silently consume the latest value merely because a source record changed.

---

## 3. Minimum Package Contents

Where applicable, the package contains:

| Area | Minimum controlled content |
| --- | --- |
| Identity | package ID, version, jurisdiction, route, Matter, filing unit |
| Applicant | legal name, address, entity details, nationality/incorporation, applicant source |
| Mark | exact representation, type, color position, transliteration, translation, description |
| Scope | classes, goods/services, local wording, limitations, disclaimers |
| Claims | priority, use, convention, seniority, intent or other route-specific basis |
| Representation | local representative or connector route and eligibility conditions |
| Documents | formal Document references, accepted-use decisions, original/copy status |
| Fees | fee-driving units and official-fee version used for execution readiness |
| Evidence | source references for material factual and professional conclusions |
| Conditions | blockers, warnings, assumptions, expiry and revalidation triggers |
| Responsibility | preparer, reviewer, approver and confirmation owner |

A rendered filing form may be one representation of the package. It is not the entire governed artifact.

---

## 4. Source Lineage

Every material package value must identify whether it came from:

- verified formal record;
- user-confirmed fact;
- accepted Formal Intake value;
- formal Document;
- professional decision;
- jurisdiction-pack rule;
- provider-specific requirement;
- calculated value;
- unresolved assumption.

The Product must make conflicting sources visible instead of choosing silently.

---

## 5. Package Components and Formal Documents

A Filing Package Candidate may include or reference:

- application data sheet;
- mark image or representation file;
- goods/services schedule;
- priority data;
- POA;
- declaration;
- translation or transliteration statement;
- applicant evidence;
- supporting evidence;
- payment or fee instruction data;
- provider instruction attachment.

A component file remains distinct from a formal Document and from the package as a whole.

```text
Source file ≠ formal Document ≠ Filing Package Candidate
```

---

## 6. Package Views

The same package may have purpose-limited views:

- client confirmation view;
- professional review view;
- provider instruction view;
- connector payload preview;
- official-form rendering;
- audit and comparison view.

Views may hide internal cost, private provider evidence, unrelated portfolio data, or privileged notes. They must not alter package meaning.

---

## 7. User Confirmation Surface

The client-facing view should emphasize:

1. applicant;
2. exact mark;
3. jurisdictions and routes;
4. classes and goods/services;
5. priority or use claims;
6. material declarations;
7. documents requiring signature or factual confirmation;
8. unresolved warnings;
9. what confirmation does and does not authorize.

The primary action should be labelled precisely, for example:

```text
Confirm factual filing content
```

It must not be labelled `Submit application` unless the user is actually performing an authorized governed submission action.

---

## 8. Version and Immutability

Every issued package version preserves:

- package identifier and version;
- created time and actor;
- exact upstream versions;
- rendered outputs and payload hashes where appropriate;
- review and confirmation state;
- approval state;
- superseded-by reference;
- execution attempts already linked to it.

A material change creates a new package version.

---

## 9. Material Change Rules

Material changes include:

- applicant identity or address;
- mark representation;
- jurisdiction or route;
- filing basis or priority;
- class or goods/services scope;
- declaration content;
- signatory or authority;
- required Document;
- fee-driving unit;
- provider-specific filing requirement.

A material change invalidates affected confirmation, Review, Filing Approval, and execution readiness.

Non-material presentation changes may preserve approval only under explicit policy and recorded comparison.

---

## 10. Package Diff

The Product should provide a structured comparison between versions:

```text
Added
Removed
Changed
Reformatted only
Source changed
Rule version changed
Approval impact
Execution impact
```

A reviewer must be able to distinguish a punctuation correction from a changed applicant, item, claim, or representation.

---

## 11. Unresolved Items

A package may contain visible non-blocking warnings, but it must not hide:

- unresolved applicant conflict;
- unapproved goods/services wording;
- invalid POA;
- stale jurisdiction rule;
- missing required declaration;
- unknown fee-driving unit;
- unverified deadline-sensitive claim.

Each unresolved item identifies effect, owner, due point, override authority, and retained evidence.

---

## 12. `EMBERLOOP` Reference Journey

For `EMBERLOOP`, MarkReg creates separate package candidates for the United States, European Union, and United Kingdom because route, forms, representatives, declarations, fees, and acknowledgement evidence differ.

The US word-mark package references:

- accepted Quote v3;
- Commercial Instruction v1;
- Formal Intake v4;
- Requirement Set v2;
- Readiness Assessment v5;
- the approved word-mark filing unit;
- revised goods wording following the search review;
- the current US jurisdiction-pack version;
- the provider-specific declaration still requiring final professional review.

The EU and UK packages reuse authorized facts but remain independent governed artifacts.

---

## 13. Conformance Scenario — Mark File Changes

**Given** the client uploads a revised device logo after factual confirmation.  
**When** MarkReg compares it with the confirmed package.  
**Then** it creates a new filing-unit candidate and package version, identifies affected search, pricing, documents and approval, and prevents execution of the superseded package.  
**Authority boundary:** automated comparison does not decide legal equivalence or approve filing.  
**Evidence retained:** both files, comparison result, affected versions, user explanation and reviewer decision.

---

## 14. AI Assistance

AI may:

- assemble candidate values from authorized sources;
- compare package versions;
- detect conflicts and omissions;
- generate rendered previews;
- explain fields in plain language;
- map values to provider or connector schemas.

AI may not invent facts, select unresolved legal positions, confirm authority, approve a package, sign a declaration, or submit externally.

---

## 15. Minimum Chapter Lock

```text
A Filing Package Candidate is a versioned,
source-linked and purpose-bound Product artifact.

It states exactly what is proposed for filing,
not merely which form fields are populated.

Material changes invalidate affected
confirmation, Review, approval and execution.

Package preparation is not Filing Approval.
Filing Approval is not execution.
Submission is not official acknowledgement.
```

---

## 16. Handoff to CH24

CH23 produces a reviewable Filing Package Candidate.

CH24 defines professional Review, client confirmation, internal approval, Filing Approval, separation of duties, and the exact authority required before the package may enter governed execution.