# B05-CH-19 — Formal Intake and Information Sufficiency

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

Need Understanding gathered enough context to recommend. This chapter gathers and verifies enough information to prepare the exact accepted service scope.

The controlled output is `MR-A08 Formal Intake`. The `EMBERLOOP` reference step is `EL-12`.

```text
Accepted Quote
+ Commercial Instruction
+ confirmed recommendation records
→ Formal Intake
```

`Need Brief ≠ Formal Intake`, and complete Intake does not equal filing readiness or Filing Approval.

## 1. Product Question

> Which formal facts are still required, why are they required, and which existing facts can be reused safely?

The Product should not restart with a universal form. Questions follow the selected service, jurisdiction, route, filing unit and unresolved conditions.

## 2. Formal Intake Contract

A conforming Formal Intake records:

- service family and accepted scope;
- linked Quote and Commercial Instruction versions;
- questions and conditional triggers;
- answers and source state;
- contributor identity and authority;
- reused facts and source versions;
- unresolved conflicts and unknowns;
- linked files and Documents;
- validation and Professional Review results;
- the purpose for which sufficiency is assessed;
- stable version and supersession history.

## 3. Information States

Every material value is identified as one of:

```text
Verified Fact
User-Declared Fact
Imported Fact
Inferred Candidate
Professional Conclusion
Unknown
Disputed
```

Inference must not be displayed as confirmation. A conflict is preserved until an accountable Decision resolves it.

## 4. Authorized Reuse

MarkReg may reuse authorized information from organization, client, brand, portfolio, prior Matter, Need Brief, Recommendation Set, Proposal, Quote, applicant, signatory and Document records.

Reuse is allowed only when the fact is:

- correctly scoped;
- sufficiently current for the present purpose;
- traceable to a source;
- visible for confirmation or correction;
- not contradicted by a higher-authority source.

Stale or conflicting information triggers a targeted confirmation. Reuse is assistance, not verification.

## 5. Progressive Disclosure

A question appears when its answer may:

- change scope, route or price;
- determine a jurisdiction requirement;
- resolve identity or authority;
- create or remove a document requirement;
- affect Professional Review;
- affect a deadline or External Protected Action.

Examples:

```text
priority claimed
→ collect office, date, number, applicant and document state

non-Latin mark content
→ collect language, translation, transliteration and meaning

legal-entity applicant
→ confirm entity type, place of organization and signatory capacity
```

## 6. Service-Specific Intake

The shared framework may support new filing, search, examination response, dispute, renewal, maintenance, recordal, transaction or evidence work.

A generic form does not establish support. The active Jurisdiction Pack must support the exact jurisdiction, service and lifecycle stage at an appropriate state.

## 7. Sufficiency Dimensions

Sufficiency is purpose-specific:

| Dimension | Question |
| --- | --- |
| identity | is the applicant or right holder correctly identified? |
| scope | are jurisdictions, filing units, classes and items sufficiently fixed? |
| authority | are the instructor and signatory authorized for this purpose? |
| deadline | are priority or filing dates sourced and usable? |
| professional | have material judgments received required Review? |
| commercial | does Intake match accepted scope? |
| document | can the Requirement Set be finalized? |

One completion percentage must not hide a blocking gap.

## 8. Missing and Conflicting Information

Each unresolved item is classified as:

```text
Blocking
Required Before Review
Required Before Approval
Required Before Filing
Required Later
Recommended
Optional
Unable to Obtain
Disputed
```

It also records owner, reason, due point, acceptable evidence, fallback and affected action.

`Unknown` is a valid state. The Product must not force an invented answer.

## 9. Participants and Access

Different sections may be completed by a client business contact, applicant representative, signatory, finance contact, professional reviewer or properly engaged provider.

Every material answer preserves its contributor and represented organization. Access remains purpose-limited for unpublished marks, identity records, transactions, signatures and payment information.

## 10. Change and Supersession

A material change to applicant, mark, route, priority, class, goods/services, jurisdiction, signatory, document or deadline creates a new Formal Intake version.

The Product identifies:

- affected questions;
- affected Requirement Set rules;
- stale Quote assumptions;
- Review requiring repetition;
- downstream records requiring revalidation.

Already formalized objects are not silently changed.

## 11. Reference Journey — `EL-12`

For `EMBERLOOP`, MarkReg reuses the accepted US/EU/UK scope, selected applicant, filing units, class candidates and goods/services version.

It asks only for:

- final applicant registration details;
- priority status;
- authorized signatory;
- final mark files;
- US declaration inputs;
- confirmation of revised goods wording.

The operating subsidiary initially conflicts with the parent-company portfolio record. Formal Intake v4 preserves both sources until the professional Decision confirms the subsidiary and records the rationale.

That change invalidates the earlier document preview. It does not silently rewrite Quote v3.

## 12. User Surface

Show:

1. progress by section and purpose;
2. prefilled facts with source labels;
3. inferred values clearly distinguished;
4. conflicts and unknowns;
5. why each new question appears;
6. contributors and delegated sections;
7. blockers and next actions;
8. changes that affect price, Documents or Review.

The primary action is complete, delegate, confirm or request Review—not declare the filing ready.

## 13. AI Boundary

AI may extract, classify, compare, prefill, detect missing information and draft targeted questions.

AI may not verify an applicant, establish authority, resolve a disputed fact, declare professional sufficiency or invent a value to complete Intake.

## 14. Failure Modes

Reject:

```text
One universal form for every service
Imported fact treated as current truth
Inference shown as user confirmation
Unknown answer forced into a value
Conflict overwritten
Completion percentage hides a blocker
Provider sees unrelated information
Material Intake change leaves Review valid
Complete Intake treated as Filing Approval
```

## 15. Chapter Output and Handoff

CH19 produces `MR-A08 Formal Intake v4` with a purpose-specific sufficiency result.

CH20 converts that Intake and the active Pack rules into `MR-A09 Requirement Set` for Documents, signatures, translations, certification and physical originals.