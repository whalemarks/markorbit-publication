# B05-CH-12 — Applicant, Ownership and Authority Context

**Status:** Revised Draft — Productized  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part II — Need, Strategy and Recommendation  
**Revision basis:** B05-REVISION-PACK-001

## Chapter Purpose

The applicant is not merely a text field. Applicant identity affects ownership, use, priority, documents, signatures, provider instructions, later assignments, enforcement, and portfolio continuity.

This chapter defines how MarkReg identifies applicant, ownership, and authority questions early enough to prevent avoidable rework without allowing the Product to choose the owner autonomously.

## 1. Product Question

> Which legal person should own the proposed right, and who has authority to confirm and act for that person?

The Product must distinguish:

- current operating company;
- parent or holding company;
- existing portfolio owner;
- distributor, licensee, founder, or predecessor;
- intended applicant;
- signatory;
- instructing contact;
- payer;
- professional reviewer;
- formal representative.

These roles may be different.

## 2. Inputs

MarkReg may consume:

- organization and client records;
- legal-name and registration data;
- existing portfolio ownership;
- group structure;
- prior applications and assignments;
- licensing or distribution context;
- business-use evidence;
- priority claims;
- signatory and delegation records;
- user statements;
- professional decisions.

Conflicting sources must remain visible until resolved.

## 3. Applicant and Authority Context Contract

The context should record:

- proposed applicant identity and stable reference;
- legal name, entity type, address, and jurisdiction;
- source and verification status;
- relationship to the business and brand;
- ownership rationale;
- current portfolio owner comparison;
- predecessor or assignment context;
- priority applicant consistency;
- instructing authority;
- signatory identity, role, and authority source;
- payer identity where relevant;
- unresolved conflicts;
- professional review status;
- downstream artifacts affected by change.

The Product must distinguish candidate information from formal records owned elsewhere.

## 4. Product Behavior

MarkReg should:

1. propose known entity candidates from authorized context;
2. identify conflicts with existing portfolio records;
3. ask one targeted question when the conflict changes risk or requirements;
4. explain likely consequences of each candidate;
5. regenerate document and signature requirements after a material change;
6. require professional review for unresolved ownership, priority, predecessor, or authority issues;
7. block only the affected readiness dimensions;
8. preserve the original source and later decision.

## 5. User Surface

The user sees:

- proposed applicant;
- source and verification status;
- existing owners found in the portfolio;
- conflict explanation;
- expected effects on documents, priority, signatures, and later ownership work;
- signatory and instructor roles;
- one primary action: **Confirm applicant and authority context**.

The interface must not imply that the Product has already changed any official owner record.

## 6. Reference Journey A — EMBERLOOP

The user initially selects Northstar’s operating subsidiary. Existing portfolio context shows that the parent owns other marks.

MarkReg displays the conflict and asks whether the group follows a centralized ownership policy. The professional reviews the business and priority context, and the user confirms the operating subsidiary as applicant for the launch filings.

The decision:

- creates a new applicant-context version;
- invalidates the first document-requirement preview;
- updates signatory questions;
- preserves the parent-company alternative and the reason it was not selected.

## 7. Conformance Scenario

### MR-SCN-01 — Applicant ambiguity

**Given** the user selects an operating subsidiary while portfolio records show the parent as owner.  
**When** applicant confirmation is required.  
**Then** MarkReg displays the conflict, explains affected documents and jurisdictions, asks one targeted question, and blocks filing readiness until resolved or professionally overridden.  
**Authority boundary:** the Product does not choose the owner.  
**Evidence retained:** both source records, user response, professional decision, rationale, and affected artifact versions.

## 8. Authority Is Purpose-Specific

Authority must be evaluated for the action in question.

Examples include authority to:

- provide factual information;
- accept a Proposal or Quote;
- issue Commercial Instruction;
- sign a POA or declaration;
- approve a Filing Package;
- authorize payment;
- instruct a provider;
- approve an assignment or recordal.

One authority record must not be reused for a different purpose without validation.

## 9. Change Propagation

Changing the applicant or signatory may affect:

- eligibility and filing basis;
- priority;
- ownership strategy;
- Quote tax or provider assumptions;
- POA and declaration requirements;
- translations, notarization, legalization, and originals;
- Formal Intake;
- professional review;
- Filing Package Candidate;
- readiness and approval;
- future assignment risk.

The Product must identify and revalidate affected artifacts under `MR-CR-08`.

## 10. Handoff to CH13

With the mark units and applicant context visible, CH13 converts the business offering into explainable class candidates. Classification remains connected to jurisdiction, filing unit, use, goods/services scope, and fee consequences.