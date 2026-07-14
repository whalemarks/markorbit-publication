# B05-CH-23 — Filing Package as a Governed Artifact

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

Part III ended with accepted commercial scope, sufficient Formal Intake, a Requirement Set, a purpose-specific Readiness Assessment and returned formal references.

CH23 defines `MR-A11 Filing Package Candidate`:

> What exact, versioned content is proposed for filing, from which sources, for which jurisdiction, route, filing unit and applicant?

```text
EL-16 / CH23
approved journey inputs
+ accepted Documents and source materials
+ active Jurisdiction Pack version
+ filing-specific content
+ visible unresolved items
→ MR-A11 Filing Package Candidate
```

A Filing Package Candidate is not Filing Approval, provider instruction, Execution, submission or official acknowledgement.

## 1. Product Question and Primary Action

**Product question:** What exactly is proposed for filing?

**Primary action:** Review the package, resolve differences and confirm only the facts the current actor is authorized to confirm.

The user should see one coherent package version rather than unrelated form fields.

## 2. Required Inputs

A package must reference exact versions of:

- Commercial Instruction;
- Formal Intake;
- Requirement Set;
- Readiness Assessment;
- filing unit and mark representation;
- Applicant and Authority Context;
- classes and goods/services;
- jurisdiction and route;
- priority, use or other filing basis where relevant;
- accepted Documents and source materials;
- responsible professional;
- active Jurisdiction Pack;
- relevant Order, Matter and Execution references.

The Product must not silently consume the latest value merely because an upstream record changed.

## 3. Package Contract

| Area | Minimum controlled content |
| --- | --- |
| identity | package ID, version, jurisdiction, route, Matter and filing unit |
| applicant | legal identity, address, entity details and source |
| mark | exact representation, type, colour, transliteration, translation and description |
| scope | classes, goods/services, local wording, limitations and disclaimers |
| claims | priority, use, convention, seniority, intent or other basis |
| representation | provider, professional or connector route and eligibility conditions |
| Documents | formal references, accepted-use decisions and original/copy state |
| fees | fee-driving units and source version used for execution readiness |
| evidence | source references for material facts and Professional Decisions |
| conditions | blockers, warnings, assumptions, expiry and revalidation triggers |
| responsibility | preparer, factual confirmer, reviewer and approver |

A rendered official form or connector payload is one view of the package, not the entire governed artifact.

## 4. Source Lineage

Every material value must identify whether it came from:

- a verified formal record;
- a user-confirmed fact;
- accepted Formal Intake;
- a formal Document;
- a Professional Decision;
- a Jurisdiction Pack Rule;
- a provider-specific requirement;
- a calculation;
- an unresolved assumption.

Conflicting sources remain visible until an accountable Decision resolves or bounds them.

## 5. Components, Documents and Views

```text
Source file ≠ formal Document ≠ Filing Package Candidate
```

A package may reference application data, mark files, goods/services schedules, priority records, POA, declarations, translations, applicant evidence and payment instructions.

Purpose-limited views may include:

- client factual-confirmation view;
- Professional Review view;
- provider-instruction view;
- connector-payload preview;
- official-form rendering;
- audit and comparison view.

A view may hide internal cost, privileged notes or unrelated portfolio data. It may not alter package meaning.

## 6. Version, Diff and Material Change

Each issued package version retains:

- stable identity and creation time;
- exact upstream versions;
- rendered outputs and payload hashes where appropriate;
- factual confirmation, Review and approval state;
- supersession link;
- linked Execution attempts.

A structured diff should classify:

```text
Added
Removed
Changed
Reformatted only
Source changed
Rule version changed
Review impact
Approval impact
Execution impact
```

Material changes include applicant, mark, route, filing basis, priority, class, goods/services, declaration, signatory, required Document, fee-driving unit or provider-specific filing requirement.

A material change creates a new package version and invalidates only the confirmations, Reviews, approvals and Execution readiness that depended on the changed content.

## 7. Unresolved Items and User Surface

A package may retain visible non-blocking warnings. It must not hide:

- unresolved applicant conflict;
- unreviewed goods/services wording;
- invalid POA;
- stale Rule or Pack version;
- missing required declaration;
- unknown fee-driving unit;
- unverified deadline-sensitive claim.

The client-facing surface should show applicant, exact mark, jurisdiction, route, classes, goods/services, claims, Documents, warnings and the effect of confirmation.

Use a precise action label such as:

```text
Confirm factual filing content
```

Do not label factual confirmation as `Submit application`.

## 8. `EMBERLOOP` — `EL-16`

MarkReg creates separate US, EU and UK Filing Package Candidates because routes, forms, providers, declarations, fees and acknowledgement evidence differ.

The US word-mark package references Quote v3, Commercial Instruction v1, Formal Intake v4, Requirement Set v2, Readiness Assessment v5, the selected applicant, revised goods wording and the active US Pack version.

EU and UK packages may reuse authorized facts, but each remains an independent governed artifact.

## 9. Controlled Scenario

### `MR-SCN-16` — Package changed after confirmation or approval

A revised device logo, applicant detail, goods item, route or fee-driving fact creates a new filing-unit or package version. The Product shows the material diff, invalidates affected Review or Filing Approval and blocks Execution of the superseded version.

**Boundary:** automated comparison does not determine legal equivalence or grant renewed approval.

## 10. AI Assistance

AI may assemble authorized candidate values, compare versions, detect omissions, prepare rendered previews and map fields to provider or connector schemas.

AI may not invent facts, resolve legal positions, establish authority, approve a package, sign a declaration or submit externally.

## 11. Chapter Lock

```text
Filing Package Candidate = exact proposed filing content.
Package preparation ≠ Filing Approval.
Filing Approval ≠ Execution.
Submission ≠ official acknowledgement.
```

## 12. Handoff to CH24

CH23 produces `MR-A11 Filing Package Candidate`.

CH24 records factual confirmation, `MR-D02 Professional Decision` and `MR-D03 Filing Approval` for one exact package version and permitted route.
