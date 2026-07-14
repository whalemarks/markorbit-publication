# B05-CH-20 — Document Requirements, POA and Signatures

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

CH19 produced `MR-A08 Formal Intake`. This chapter converts the accepted scope, Intake facts and active Jurisdiction Pack rules into `MR-A09 Requirement Set`.

The `EMBERLOOP` reference step is `EL-13`.

```text
Uploaded File
≠ Valid Document
≠ Signed Authority
≠ Physical Original
≠ Official Record
```

## 1. Product Question

> Which Documents are required, what form is acceptable, who must sign, and what is wrong with the materials already supplied?

A generic upload box does not conform. Each request must explain the requirement, acceptable evidence, due point and consequence of a defect.

## 2. Requirement Set Contract

Every requirement records:

- service, jurisdiction and intended action;
- Source Record, Rule Record and Pack Version;
- required Document type;
- principal, applicant or right holder;
- provider or office recipient where known;
- language and translation condition;
- signature, capacity, witness or seal condition;
- scan, certification, notarization, apostille, legalization or original condition;
- validity period;
- deadline and delivery route;
- blocker level and override authority;
- accepted-use purpose.

A requirement is different from a request. One requirement may produce several requests, preparation steps or external certification actions.

## 3. File Provenance

Every received file preserves:

- uploader and represented organization;
- receipt time and source channel;
- file identity, hash or stable reference;
- stated and detected type;
- language;
- linked requirement;
- confidentiality and purpose;
- version and supersession state.

AI may classify a likely type or extract fields. A user or reviewer must be able to correct the result.

## 4. Document Forms

The Product distinguishes:

```text
Digital Scan
Certified Copy
Notarized Copy
Apostilled Copy
Legalized Copy
Physical Original
Official Electronic Record
```

It records both the required and received form. `Uploaded` is not a readiness state.

## 5. POA and Signature Authority

A POA may define:

- principal and representative;
- jurisdiction and service scope;
- actions covered;
- duration and revocation;
- signatory and capacity;
- seal, witness or signature method;
- certification or legalization;
- original or copy requirement.

One POA must not be assumed to cover every filing, examination, renewal, recordal, assignment, opposition or appeal.

A signature record answers:

```text
Who signed?
For which organization?
In which capacity?
Under what authority?
Which exact Document version?
When and by which method?
```

Identity, job title or account access does not establish purpose-specific authority.

`MR-SCN-11` applies when signatory or representative authority has expired or lacks scope.

## 6. Translation and Certification

A translation links to the exact source version and records language pair, translator or method, date, terminology Review, certification state and relationship to the source.

Machine translation may assist understanding. It does not automatically satisfy a certified-translation requirement.

Notarization, apostille, consular legalization, witness, chamber certification and corporate seal remain distinct.

## 7. Validation Dimensions

A Document may be evaluated for:

| Dimension | Example result |
| --- | --- |
| identity | correct or wrong applicant |
| type | expected or wrong Document type |
| version | current, superseded or altered |
| completeness | fields and pages present |
| readability | readable or unusable |
| signature | valid, missing or wrong method |
| authority | verified, uncertain or rejected |
| certification | complete or further step required |
| language | accepted or translation required |
| physical form | scan accepted or original required |
| purpose | accepted for the stated use only |

Use specific states such as Requested, Received, Wrong Type, Wrong Version, Incomplete, Signature Missing, Authority Unverified, Certification Required, Translation Required, Original Required, Under Review, Accepted for Defined Use, Rejected, Expired and Superseded.

## 8. Physical Custody and Sharing

Where a physical original matters, track holder, storage, dispatch, courier, receipt, return and destruction policy.

Before sharing with a provider, confirm appointment, purpose, confidentiality and need to know. Provider discovery alone does not justify access to sensitive client Documents.

## 9. Controlled Scenarios

`MR-SCN-05` requires an invalid POA to be rejected for the stated purpose, with defects explained and only the affected readiness dimension blocked.

`MR-SCN-11` blocks action where signatory or representative authority is expired or insufficient.

**Boundary:** file upload, AI extraction and a familiar signature do not establish legal validity or authority.  
**Evidence:** original file, Pack Version, defect, reviewer Decision, replacement request and accepted version.

## 10. Reference Journey — `EL-13`

`EMBERLOOP` Requirement Set v2 records:

- EU and UK filing materials structurally complete;
- final mark files and applicant details accepted;
- one US declaration pending;
- a defined US provider signature package;
- no physical original required for the accepted route;
- applicant change as an invalidation trigger for POA and declaration requirements.

The client sees which requirement blocks which jurisdiction. The Product does not show one generic `documents incomplete` status.

## 11. User Surface

Show:

1. requirement and reason;
2. responsible provider, signatory or contributor;
3. accepted form and language;
4. deadline and consequence;
5. current file and validation state;
6. defect-specific correction action;
7. physical-original or certification step;
8. affected readiness dimension and jurisdiction.

Primary actions include upload, replace, sign, arrange certification, dispatch an original or request Review.

## 12. AI Boundary

AI may classify, extract, compare, detect missing fields, draft translations, identify signature blocks, redact and map files to requirements.

AI may not authenticate, notarize, legalize, sign, establish authority, claim physical custody or declare official acceptance.

## 13. Failure Modes

Reject:

```text
Upload treated as acceptance
Scan treated as physical original
Signature reused on changed content
POA assumed universal
Machine translation shown as certified
Notarization and apostille merged
Wrong-applicant Document reused
Provider receives files before engagement
Superseded Document remains active
```

## 14. Chapter Output and Handoff

CH20 produces `MR-A09 Requirement Set v2`, linked source files, validation results, signature and certification states, custody information and accepted-use Decisions.

CH21 combines these results with commercial, professional, payment, deadline and approval conditions in `MR-A10 Readiness Assessment`.