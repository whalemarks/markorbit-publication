# B05-CH-19 — Formal Intake and Information Sufficiency

**Status:** Productized Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

Need Understanding collected enough context to recommend. Formal Intake now collects and verifies enough information to prepare the accepted service scope.

The controlling lineage is:

```text
Accepted Quote
+ Commercial Instruction
+ Confirmed Recommendation Artifacts
→ Formal Intake
→ Requirement Set
→ Readiness Assessment
```

`Need Brief ≠ Formal Intake`, and complete Intake does not equal filing approval.

## 1. User Question

> Which formal facts are still needed, why are they needed, and which existing facts can be reused safely?

The Product should not restart with a universal form. It should ask only the questions required by the selected service, jurisdiction, route, filing unit and unresolved conditions.

## 2. Intake Contract

A `Formal Intake` must identify:

- service family and accepted scope;
- linked Quote and Commercial Instruction versions;
- questions and conditional triggers;
- answers and source state;
- contributor identity and authority;
- reused facts and their source versions;
- unresolved conflicts and unknowns;
- linked documents;
- validation and professional-review results;
- sufficiency purpose;
- stable version and supersession history.

## 3. Information States

Every material value must be distinguished as:

```text
Verified Fact
User-Declared Fact
Imported Fact
Inferred Candidate
Professional Conclusion
Unknown
Disputed
```

The interface must not present inference as confirmation or overwrite a conflict with the latest entry.

## 4. Authorized Reuse

MarkReg may reuse authorized information from:

- organization and client context;
- brand and portfolio records;
- prior Matters and rights;
- Need Brief and Recommendation Set;
- accepted Proposal and Quote;
- verified applicant and signatory records;
- stored Documents.

Reuse is allowed only when the fact is sufficiently current, correctly scoped and traceable. A stale or conflicting fact triggers confirmation rather than silent copying.

## 5. Progressive Disclosure

A question should appear when its answer:

- changes scope, route or fees;
- determines a jurisdiction requirement;
- resolves identity or authority;
- creates or removes a document requirement;
- affects professional review;
- affects a deadline or protected action.

Conditional questions should explain their trigger where useful.

Examples:

```text
Priority claimed
→ collect office, date, number, applicant and document state

Non-Latin mark content
→ collect language, translation, transliteration and meaning

Legal-entity applicant
→ confirm entity type, place of organization and signatory capacity
```

## 6. Service-Specific Intake

The shared framework must support different requirement sets for:

- new filing;
- search;
- office action;
- opposition or appeal;
- renewal or maintenance;
- assignment, change or recordal;
- evidence or declaration.

A page or form alone does not establish service-family support. The service must satisfy the conformance criteria in `B05-SPEC-0001`.

## 7. Sufficiency Dimensions

Intake sufficiency must be evaluated by purpose and dimension:

| Dimension | Example questions |
| --- | --- |
| Identity | Is the applicant or right holder correctly identified? |
| Scope | Are filing units, jurisdictions, classes and items fixed enough? |
| Authority | Is the instructor and signatory authority known? |
| Deadline | Are priority or filing dates sourced and usable? |
| Professional | Have material judgments been reviewed? |
| Commercial | Does Intake match accepted scope? |
| Document | Can the Requirement Set be finalized? |

One completion percentage must not hide a blocking gap.

## 8. Missing, Unknown and Conflicting Information

Each unresolved item must be classified as:

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

It must also identify owner, reason, due point, acceptable evidence, fallback and affected action.

“Unknown” is a valid state. The Product must not force an invented answer.

## 9. Material Change and Versioning

Changes to applicant, mark, route, priority, class, goods/services, jurisdiction, signatory, document or deadline create a new Intake version and identify:

- affected questions;
- affected Requirement Set rules;
- affected Quote assumptions;
- prior reviews that became stale;
- downstream artifacts requiring revalidation.

Already formalized objects are not silently mutated.

## 10. Participants and Access

Different participants may contribute different facts:

- client business contact;
- applicant representative;
- signatory;
- finance or procurement contact;
- professional reviewer;
- external provider after proper engagement.

Every material answer preserves who supplied it. Access remains purpose-limited, particularly for unpublished marks, identity documents, transactions, signatures and payment information.

## 11. EMBERLOOP Reference Journey

MarkReg reuses the accepted US/EU/UK scope, selected applicant, filing units, class candidates and goods/services package.

It asks only for unresolved service-specific facts:

- final applicant registration details;
- priority status;
- authorized signatory;
- final mark files;
- US declaration inputs;
- confirmation of the revised goods wording.

The operating subsidiary initially conflicts with the parent-company portfolio record. The conflict remains visible until the professional records the selected applicant and reason. Formal Intake v4 references the corrected applicant and invalidates the earlier document preview.

## 12. Conformance Scenario — Stale Reused Fact

**Given** a prior Matter contains an applicant address last verified three years ago.  
**When** the address is reused for the current filing Intake.  
**Then** MarkReg labels the source and age, requests confirmation, and prevents unconfirmed reuse where the jurisdiction requires current details.  
**Authority boundary:** reuse is assistance, not verification.  
**Evidence retained:** old source, confirmation request, response, reviewer decision and new version.

## 13. User Surface

The Intake surface should show:

1. progress by section and purpose;
2. prefilled facts with source labels;
3. inferred values clearly distinguished;
4. conflicts and unknowns;
5. why each new question appears;
6. contributors and delegated sections;
7. blockers and next action;
8. changes that will affect price, documents or review.

The primary action is to complete, delegate, confirm or request review—not to declare the filing ready.

## 14. Failure Modes

The Product must reject:

```text
One universal form for every service
Imported fact treated as current truth
Inference shown as user confirmation
Unknown answer forced into a value
Conflict overwritten
Completion percentage hides a blocker
Provider sees unrelated information
Material Intake change leaves review valid
Complete Intake treated as filing approval
```

## 15. Chapter Output

The output is a versioned Formal Intake with a purpose-specific sufficiency result.

The next chapter converts jurisdiction and service rules into a Requirement Set for documents, signatures, translations, certification and physical originals.