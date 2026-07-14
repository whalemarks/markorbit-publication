# B05-CH-20 — Document Requirements, POA and Signatures

**Status:** Productized Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

CH19 established a versioned Formal Intake. This chapter converts service and jurisdiction rules into a `Requirement Set` and governs document requests, source files, signatures, translations, certification, physical originals and accepted use.

The controlling rule is:

```text
Uploaded File
≠ Valid Document
≠ Signed Authority
≠ Physical Original
≠ Official Record
```

## 1. User Question

> Which documents are required, what form is acceptable, who must sign them, and what is wrong with the documents already supplied?

A generic upload box does not conform. The Product must explain the requirement, acceptable evidence, deadline and consequence of a defect.

## 2. Requirement Set Contract

Every document requirement must identify:

- service, jurisdiction and intended action;
- rule source and jurisdiction-pack version;
- required document type;
- principal, applicant or right holder;
- provider or office recipient where known;
- language and translation condition;
- signature, capacity, witness or seal condition;
- scan, certified copy, notarization, apostille, legalization or original condition;
- validity period;
- deadline and delivery route;
- blocker level and override authority;
- accepted-use purpose.

A requirement is different from the request sent to a participant. One requirement may generate several requests or preparation steps.

## 3. Source File and Provenance

Every received file must preserve:

- uploader and represented organization;
- receipt time and source channel;
- file identity and version;
- stated and detected document type;
- language;
- related requirement;
- confidentiality and purpose;
- hash or integrity reference where appropriate.

AI may classify a likely document type. A user or reviewer must be able to correct it.

## 4. Document Forms

The Product must distinguish:

```text
Digital Scan
Certified Copy
Notarized Copy
Apostilled Copy
Legalized Copy
Physical Original
Official Electronic Record
```

It records both the required form and the received form. “Uploaded” is never a sufficient readiness status.

## 5. POA Contract

A power of attorney may identify:

- principal and representative;
- jurisdiction and scope;
- actions covered;
- duration and revocation;
- signatory and capacity;
- seal, witness or signature method;
- notarization, apostille or legalization;
- original or copy requirement.

The Product must not assume that one POA authorizes every filing, prosecution, renewal, assignment, opposition or appeal.

## 6. Signature Contract

A signature record must answer:

```text
Who signed?
For which organization?
In which capacity?
Under what authority?
Which exact document version?
When and by which method?
```

Identity does not automatically establish authority. If content changes after signature, the Product determines whether re-signing or professional review is required.

Detached signature images, blank signed pages, unclear capacity, copied seals and undated broad POAs require warning or blocking treatment under policy.

## 7. Translation and Certification

A translation must link to the exact source version and retain:

- source and target language;
- translator or method;
- date;
- terminology review;
- certification state;
- relationship to the source document.

Machine translation may assist understanding but does not automatically satisfy certified-translation requirements.

Notarization, apostille, consular legalization, witness, chamber certification and corporate seal remain distinct steps.

## 8. Validation Dimensions

A document may be evaluated for:

| Dimension | Example result |
| --- | --- |
| Identity | correct or wrong applicant |
| Type | expected or wrong document type |
| Version | current, superseded or altered |
| Completeness | fields and pages present |
| Readability | readable or unusable |
| Signature | signed, missing or invalid method |
| Authority | verified, uncertain or rejected |
| Certification | complete or additional step required |
| Language | accepted or translation required |
| Physical form | scan accepted or original required |
| Purpose | accepted for the stated use only |

## 9. Requirement Status

Use specific states:

```text
Not Requested
Requested
Received
Unreadable
Wrong Type
Wrong Version
Incomplete
Signature Missing
Authority Unverified
Certification Required
Translation Required
Original Required
Under Review
Accepted for Defined Use
Rejected
Expired
Superseded
```

## 10. Physical Custody and Sharing

Where a physical original matters, the Product should track holder, storage location, dispatch, courier, receipt, return and destruction policy.

Before sharing with a provider, confirm appointment, purpose, conflict status, confidentiality and need to know. Preliminary provider discovery does not justify access to sensitive client documents.

## 11. EMBERLOOP Reference Journey

The Requirement Set for EMBERLOOP shows different jurisdiction results:

- EU and UK filing materials are structurally complete;
- the final mark files and applicant details are accepted;
- one US declaration remains pending;
- the selected US provider requires a defined signature package;
- no physical original is currently required for the accepted route;
- any applicant change will invalidate the POA and declaration requirements.

The client sees exactly which document blocks which jurisdiction rather than one generic “documents incomplete” label.

## 12. Conformance Scenario — Invalid POA

**Given** a POA is uploaded with a signatory whose authority is not supported and a signature form not accepted by the relevant rule.  
**When** validation occurs.  
**Then** MarkReg marks the POA invalid for the stated jurisdiction and purpose, explains both defects, requests the correct replacement and blocks only the affected readiness dimension.  
**Authority boundary:** file upload and AI extraction do not establish legal validity.  
**Evidence retained:** original file, rule version, detected defects, reviewer decision, replacement request and accepted version.

## 13. User Surface

The document surface should show:

1. requirement and reason;
2. who must provide or sign;
3. accepted format and language;
4. deadline and consequence;
5. current file and validation state;
6. defect-specific correction action;
7. whether an original or external certification step is required;
8. affected readiness and jurisdiction.

Primary actions include upload, replace, sign, arrange certification, send original or request review.

## 14. AI and Human Boundary

AI may classify, extract, compare, detect missing fields, prepare translations, identify signature blocks, redact and map files to requirements.

AI may not authenticate, notarize, legalize, sign, establish authority, claim physical custody or declare official acceptance.

## 15. Failure Modes

The Product must reject:

```text
Upload treated as acceptance
Scan treated as physical original
Signature reused on changed content
POA assumed universal
Machine translation shown as certified
Notarization and apostille merged
Wrong applicant document reused
Provider receives files before proper engagement
Superseded document remains active
```

## 16. Chapter Output

The output is a versioned Requirement Set with document requests, source files, validation results, signature and certification states, custody state and accepted-use decisions.

The next chapter combines these results with commercial, professional, payment, provider and deadline conditions into purpose-specific readiness gates.