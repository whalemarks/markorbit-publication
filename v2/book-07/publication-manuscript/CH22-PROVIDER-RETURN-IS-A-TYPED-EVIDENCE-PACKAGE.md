# CH22 — Provider Return Is a Typed Evidence Package

A Provider Return is not simply “the email the agent sent back.”

International service work can generate many kinds of outputs:

- a filing copy;
- an official acknowledgement;
- a draft argument;
- a translated specification;
- a fee receipt;
- a certificate;
- a procedural report;
- a missing-document notice;
- a refusal;
- a correction request;
- a statement that the Provider could not act.

These outputs do not carry the same authority, completeness or operational consequence.

MGSN therefore treats the Return as a typed Evidence package.

```text
message received
≠ Return complete

Return complete
≠ Return accepted

Return accepted
≠ official or formal state updated
```

## 1. Why an attachment is not enough

A certificate, receipt or screenshot may look conclusive while still leaving unanswered questions:

- Which engagement does it belong to?
- Which version of the instruction was used?
- Is it Provider-generated or official?
- Does it cover all classes, countries or applicants?
- Was the fee actually paid?
- Is the document final or provisional?
- What action is required next?
- Does the customer need to approve anything?
- Is the Matter now complete or merely at a new stage?

The Return must place the document inside an attributable operating context.

## 2. Return types

MGSN may distinguish types such as:

```text
Acknowledgement Return
Progress Return
Milestone Completion Return
Official Communication Return
Correction Return
Exception Return
Funds Evidence Return
Final Deliverable Return
No-action Return
Replacement Handoff Return
Closure Return
```

The type determines what fields, Evidence and review are required.

## 3. Common Return envelope

Every material Return should identify:

- Return identity;
- engagement and Matter reference;
- Provider Organization;
- responsible professional or contact where relevant;
- related milestone;
- related Instruction Package version;
- Return type;
- event or effective date;
- source;
- summary;
- Evidence inventory;
- Provider assertions;
- known Unknowns;
- required next action;
- deadline impact;
- financial impact;
- correction or escalation status;
- confidentiality classification;
- submission time and version.

This envelope does not make all Returns identical. It ensures that a recipient can understand what the package claims.

## 4. Evidence inventory

A Return may contain multiple Evidence items.

Each item should record:

- file or reference identity;
- document type;
- issuer or source;
- date;
- jurisdiction or authority;
- language;
- whether translation is included;
- relationship to the milestone;
- authenticity or confidence status;
- completeness;
- restrictions;
- supersession status.

```text
Evidence attached
≠ Evidence attributable
≠ Evidence sufficient
```

## 5. Provider assertion and official Evidence must be separated

A Provider may report that an application was accepted. The attached official notice may say only that it passed a formal examination.

The Return should preserve both:

```text
Provider Assertion
Official Evidence
MGSN Interpretation or Review
Owning Service Formal-state Decision
```

These are distinct layers.

```text
Provider says registered
≠ official certificate proves registration
≠ Owning Service has updated the formal Matter state
```

## 6. Return completeness

A Return may be incomplete even when the central document is present.

Missing elements may include:

- class or goods coverage;
- official number;
- filing date;
- applicant identity;
- deadline;
- translation;
- fee receipt;
- next procedural step;
- explanation of a discrepancy;
- corrected version;
- evidence for one country in a multi-country package.

Possible completeness states include:

```text
complete
complete with minor follow-up
partially complete
Evidence missing
scope mismatch
source unclear
translation required
superseded
unknown
```

## 7. Return review

Different questions require different reviewers.

### Operational review

Checks:

- engagement and milestone match;
- required files present;
- readable documents;
- versions and dates;
- deadline fields;
- next-step routing.

### Professional review

Checks:

- legal or professional meaning;
- adequacy of analysis;
- whether a correction or response is needed;
- whether the Provider’s conclusion matches the Evidence.

### Customer or Workplace review

Checks:

- business decision;
- acceptance of changes;
- instruction for next action;
- communication to the customer.

### Owning Service validation

Determines whether and how formal business state changes.

```text
MGSN operational acceptance
≠ professional acceptance
≠ customer acceptance
≠ formal-state validation
```

## 8. Returns can create new Needs

A Return may close one milestone and create another Capability Need.

Examples:

- an office action creates a response Need;
- a certificate discrepancy creates a correction Need;
- a refusal creates an appeal or refiling Need;
- a Provider conflict creates a replacement Need;
- an official-fee shortfall creates a funds and deadline Need.

The new Need should not be hidden inside a status note.

```text
Return received
→ new Need identified
→ authorized Projection
→ new route decision where required
```

## 9. Supersession and correction

Returns need version history.

A Provider may first send:

- an incorrect filing copy;
- an incomplete certificate;
- a wrong translation;
- an inaccurate status explanation.

A corrected Return should reference the earlier version and explain:

- what changed;
- why;
- which Evidence is superseded;
- whether a deadline or formal state is affected;
- whether the customer was previously told something incorrect.

```text
latest Return
≠ permission to erase earlier Return
```

## 10. Unknowns and discrepancies

A Return should explicitly preserve discrepancies such as:

- applicant address order differs;
- mark image appears altered;
- certificate is black and white while the filing was in color;
- official number differs from Provider report;
- official fee receipt is missing;
- portal status conflicts with email;
- filing date cannot be verified.

The correct state may be Unknown Pending Reconciliation.

## 11. Return security and privacy

Returns can contain sensitive information:

- customer identity;
- signatures;
- identity documents;
- bank data;
- privileged analysis;
- unpublished marks;
- confidential settlement terms.

Access should follow engagement role, purpose and retention rules.

A Return should not automatically become visible to:

- unrelated Providers;
- introducers;
- public users;
- every member of the Provider Organization;
- participants outside the relevant Workplace.

## 12. Return portability

A structured Return supports continuity when:

- the Provider exits;
- the Workplace changes staff;
- the engagement transfers;
- a replacement Provider takes over;
- an audit or dispute occurs.

Portable does not mean unrestricted export.

The package should preserve enough context to continue safely while respecting rights, privilege and data restrictions.

## 13. AI assistance

AI may:

- classify Return type;
- extract dates and identifiers;
- compare Provider assertions with attached documents;
- detect missing Evidence;
- identify possible discrepancies;
- draft a structured summary;
- propose next-step questions.

AI must not:

- declare an official document authentic without appropriate verification;
- convert a Provider assertion into official truth;
- decide professional meaning without required review;
- update formal Matter state;
- hide contradictions to produce a clean status.

## 14. Failure scenarios

### 14.1 Provider email treated as official confirmation

The Provider writes that registration is complete but sends no certificate or official record.

Correct response: record the assertion and request the required Evidence.

### 14.2 Correct document linked to the wrong Matter

A certificate is uploaded to a similarly named mark.

Correct response: fail attribution review and prevent formal-state update.

### 14.3 New deadline hidden in a long email

An official notice includes a response deadline that is not captured.

Correct response: extract and verify the deadline, open the next Need and escalate.

### 14.4 Corrected Return overwrites the old one

A Provider replaces an incorrect filing copy without explaining the correction.

Correct response: preserve supersession and review the impact of the earlier error.

## 15. Product principle

The Provider Return is the bridge between external work and the Originating Workplace’s governed understanding.

```text
Provider activity
→ typed Return
→ attributable Evidence
→ scoped review
→ acceptance, correction or new Need
→ formal-state validation where appropriate
```

The next chapter explains why correction is not an afterthought or a favor. It is a normal part of accountable fulfillment whenever the delivered work does not satisfy the accepted milestone or instruction.