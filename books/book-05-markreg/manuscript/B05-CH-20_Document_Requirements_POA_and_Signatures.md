# B05-CH-20 — Document Requirements, POA and Signatures

**Status:** Part III Draft  
**Chapter Map:** B05-TOC-V0.1  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

Trademark work often depends on documents whose form, authority, language, signature, certification, and physical status matter.

A generic upload box is not enough.

The central progression is:

```text
Document Requirement
→ Document Request
→ Source Material
→ Validation
→ Transformation Where Required
→ Signature or Certification
→ Review
→ Formal Document or Filing-Package Use
```

```text
Uploaded File
≠ Valid Document
≠ Signed Authority
≠ Physical Original
≠ Official Record
```

---

## 1. Requirements Are Service- and Jurisdiction-Specific

A document may be required because of filing route, jurisdiction, applicant type, priority, assignment, change, office action, opposition, renewal, maintenance, local representation, or evidence.

The Product should identify the requirement source and checked date.

---

## 2. Requirement and Request Are Different

A requirement states what is needed.

A request states:

- who should provide it;
- format;
- language;
- signature;
- certification;
- deadline;
- delivery route;
- reason;
- consequence of omission.

Several requests may satisfy one requirement.

---

## 3. Files Need Provenance

For each source file, preserve:

- uploader;
- represented organization;
- received date;
- source;
- filename;
- media type;
- hash where appropriate;
- stated document type;
- language;
- version;
- related requirement;
- confidentiality.

A filename is not sufficient provenance.

---

## 4. Document Type Must Be Confirmed

Examples include certificate of incorporation, business licence, identity document, priority document, assignment, licence, POA, declaration, affidavit, consent, evidence exhibit, office notice, and registration certificate.

AI may classify a likely type. The Product should allow correction and Review.

---

## 5. Document Forms Must Remain Distinct

```text
Digital Scan
≠ Certified Copy
≠ Notarized Copy
≠ Legalized Copy
≠ Apostilled Copy
≠ Physical Original
≠ Official Electronic Record
```

The Product should record which form is required and which form was received.

---

## 6. Physical Custody May Matter

A physical original may have holder, storage location, courier status, tracking number, dispatch date, received date, return requirement, and destruction policy.

A scan cannot prove current physical custody.

---

## 7. Language and Translation Need Version Control

A translation should preserve:

- source document;
- source and target language;
- translator;
- method;
- date;
- certification;
- reviewed terminology;
- version;
- relationship to the source.

Machine translation may support understanding. It may not satisfy a certified-translation requirement automatically.

---

## 8. Notarization, Legalization and Apostille Are Separate

The Product should distinguish notarization, consular legalization, apostille, chamber certification, corporate seal, witness, and local certification.

A generic “legalized” status may hide incomplete steps.

---

## 9. A POA Is a Formal Authority Document

A POA may define:

- principal;
- representative;
- scope;
- jurisdiction;
- matters covered;
- duration;
- revocation;
- signature;
- seal;
- witness;
- notarization;
- legalization;
- original requirement.

A template should not be reused beyond its approved context.

---

## 10. POA Scope Must Match the Intended Action

A POA may authorize filing, prosecution, renewal, assignment, opposition, appeal, cancellation, receipt of documents, or appointment of associates.

The Product should not assume that one POA authorizes every action.

---

## 11. Signatory Identity and Authority Are Separate

The Product should verify:

```text
Who signed?
For which organization?
In which capacity?
Under what authority?
For which document version?
At what time?
Using which signature method?
```

Identity does not automatically prove authority.

---

## 12. Signature Methods Need Defined Effect

Possible methods include wet ink, qualified electronic signature, platform signature, typed name, scanned signature, corporate seal, and click acceptance.

The acceptable method depends on document, jurisdiction, organization policy, and stage.

---

## 13. Signature Placement and Version Matter

A signature should link to the exact document version.

If content changes after signature, the Product should determine whether the signature remains valid, re-signing is required, only a non-material correction occurred, or professional Review is required.

A detached signature image should not be applied to changed content without authority.

---

## 14. Blank Signatures and Pre-Signed Forms Are High Risk

The Product should flag blank signed pages, undated signatures, broad reusable POAs, signatures detached from content, copied seals, unclear capacity, missing principal, and altered pages.

AI may detect indicators. An eligible human decides the response.

---

## 15. Document Completeness Is Multidimensional

A document may be:

- structurally complete;
- readable;
- signed;
- properly dated;
- properly certified;
- translated;
- within validity;
- matched to applicant;
- matched to scope;
- acceptable for filing.

These are different validations.

---

## 16. Requirement Status Should Be Specific

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

“Uploaded” is not enough.

---

## 17. Document Use Must Be Purpose-Bound

A corporate document supplied for one filing may not be reusable for an unrelated transaction.

The Product should preserve permitted purpose, organization, applicant, Matter, jurisdiction, retention, and sharing scope.

---

## 18. Provider Access Should Be Limited

Before sharing, the Product should confirm provider identity, conflict status, appointment, scope, confidentiality, need to know, and transmission route.

Sensitive documents should not be exposed during preliminary provider discovery.

---

## 19. Formal Document Creation Belongs to the Proper Service

MarkReg may prepare document drafts, signature packages, translation packages, review notes, and delivery packages.

A formal Document record should be created or recorded by the applicable Owning Service or formal document process.

The Artifact and formal Document may reference each other.

---

## 20. Delivery Does Not Equal Filing

A signed POA delivered to a provider is not the same as provider acceptance, office filing, official acknowledgement, or recordal.

The Product should show the current event precisely.

---

## 21. AI May Assist Document Work

AI may classify, extract, compare, detect missing fields, identify signature blocks, prepare translations, redact, summarize, and map files to requirements.

AI should not certify authenticity, notarize, legalize, sign, establish authority, claim physical custody, or declare official acceptance.

---

## 22. Failure Modes to Reject

```text
Upload treated as acceptance
Scan treated as physical original
Signature image reused on changed document
POA assumed universal
Machine translation shown as certified
Notarization and apostille merged
Provider receives documents before appointment
Wrong applicant document reused
Superseded document remains active
AI certifies authenticity
```

---

## 23. Minimum Document Lock

```text
Requirement, request, file,
Artifact, formal Document,
signature, certification,
physical original, delivery,
and official filing remain distinct.

Every material document preserves
source, version, purpose, actor,
authority, validation, and lineage.

AI may classify, extract, compare,
translate, redact, and prepare.

Humans and authorized external actors
sign, certify, review, and accept.
```

---

## 24. Handoff to Readiness Validation

The output is a versioned set of document requirements, requests, received materials, signature or certification states, validation results, and accepted-use decisions.

The next chapter combines commercial, informational, professional, document, authority, payment, provider, deadline, and filing dimensions into a readiness model that does not hide blockers behind one score.
