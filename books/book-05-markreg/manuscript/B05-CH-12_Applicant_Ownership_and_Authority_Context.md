# B05-CH-12 — Applicant, Ownership and Authority Context

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part II — Need, Strategy and Recommendation

## Chapter Purpose

Applicant identity is not a text field. It affects ownership, use, priority, Documents, signatures, provider instructions, later recordals, enforcement and portfolio continuity.

This chapter defines how MarkReg exposes applicant, ownership and authority questions early enough to prevent avoidable rework without choosing the owner autonomously.

The controlled example is `EL-05` in B05-SPEC-0002 v0.3. The canonical Product Context is `MR-C12 Applicant and Authority Context` under B05-SPEC-0001 v0.3.

## 1. Product Question

> Which legal person may own the proposed right, and who has authority to confirm or act for that person?

The Product must distinguish:

- client;
- operating company;
- parent or holding company;
- existing portfolio owner;
- distributor, licensee, founder or predecessor;
- proposed applicant;
- instructing contact;
- signatory;
- payer;
- professional reviewer;
- approver;
- formal representative.

One person or entity may hold several roles, but the roles remain separate.

## 2. Source Context

MarkReg may use:

- organization and client records;
- legal-name and registration Evidence;
- existing portfolio ownership;
- group structure;
- prior applications, assignments and recordals;
- licensing or distribution context;
- business-use Evidence;
- priority claims;
- signatory and delegation records;
- user statements;
- Professional Decisions.

Conflicting sources must remain visible until resolved. A current business-owner claim is not automatically the official owner, applicant or authorized signatory.

## 3. Controlled Context

The chapter produces or updates `MR-C12 Applicant and Authority Context`, recording:

- proposed applicant identity and stable reference;
- legal name, entity type, address and jurisdiction;
- source and verification state;
- relationship to the brand and business;
- ownership rationale;
- comparison with current portfolio owners;
- predecessor, assignment or priority context;
- instructing authority;
- signatory identity, role and authority source;
- payer identity where relevant;
- unresolved conflicts;
- Professional Review and client confirmation state;
- downstream records affected by change.

The Product-local Context remains distinct from formal Organization, Client, Trademark, Order, Matter, representative appointment and official-owner records.

`MR-C01` is reserved for `Capability Need` in provider routing and must not be reused for applicant or authority meaning.

## 4. Product Behavior

MarkReg should:

1. propose candidates from authorized context;
2. compare them with portfolio and priority Evidence;
3. preserve conflicting sources;
4. ask the smallest question that changes risk or Requirements;
5. explain Document, signature, tax, provider and later-ownership effects;
6. request Professional Review for material ownership, predecessor, priority or authority issues;
7. block only affected readiness dimensions;
8. preserve the final accountable Decision and rejected alternatives.

AI may extract entity details or identify inconsistencies. It may not determine the legal owner, validate authority or replace Professional Review.

## 5. Authority Is Purpose-Specific

Authority to perform one action does not establish authority for another.

Separate Evidence may be required to:

- provide factual information;
- accept a Proposal or Quote;
- issue Commercial Instruction;
- sign a POA or declaration;
- approve a Filing Package;
- authorize payment;
- instruct a provider;
- approve an assignment, licence or recordal.

Every consequential action should record actor, organization, role, authority source, scope, version and validity period.

## 6. User Surface

The user should see:

- proposed applicant and source state;
- other owner candidates found;
- the conflict or uncertainty;
- expected effects on eligibility, Documents, priority and signatures;
- instructing and signatory roles;
- unresolved professional questions;
- one primary action: **Confirm applicant and authority context**.

The interface must not imply that confirming a candidate changes an official owner record.

## 7. Reference Journey — `EL-05 EMBERLOOP`

Northstar initially selects its operating subsidiary. Existing portfolio context shows that the parent owns other marks.

MarkReg preserves both sources and asks whether the group follows a centralized ownership policy. The professional reviews business, priority and portfolio context. Northstar confirms the operating subsidiary for the launch filings.

The resulting Decision:

- creates a new `MR-C12` version;
- invalidates the first Requirement preview;
- updates signatory questions;
- preserves the parent-company alternative and rationale;
- does not change any existing official owner record.

## 8. Controlled Scenarios

### `MR-SCN-01` — Applicant ambiguity

When the selected applicant conflicts with portfolio Evidence, MarkReg shows both sources, explains affected work and blocks the affected protected action until resolved or professionally reviewed. The Product does not choose the owner.

### `MR-SCN-11` — Expired or insufficient authority

An expired or out-of-scope signatory, delegation or representative record blocks only the affected action. Role membership alone is not current authority.

Minimum Evidence includes competing sources, user facts, Professional Review, accountable Decision, authority record and affected versions.

## 9. Change Propagation

Changing the applicant, signatory or instructor may affect:

- route eligibility and filing basis;
- priority;
- ownership strategy;
- tax and provider assumptions;
- POA, declaration, translation, notarization, legalization and original requirements;
- Formal Intake;
- Professional Review;
- Filing Package Candidate;
- readiness and Approval;
- future assignment or recordal risk.

The Product must identify and revalidate the affected chain. Prior Decisions remain traceable.

## 10. Handoff to CH13

With the filing units and applicant context visible, CH13 converts the business offering into explainable class candidates. Classification remains connected to jurisdiction, mark form, use, goods/services scope and fee consequences.
