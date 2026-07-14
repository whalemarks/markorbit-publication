# B05-SPEC-0001 — MarkReg Product Artifact and Decision Map

## Status

- **Status:** Controlled Draft
- **Applies to:** Book 05 Parts I–IV
- **Authority:** Book 05 Product specification
- **Supersedes:** dispersed, non-canonical artifact descriptions in CH07–CH22

## 1. Purpose

This specification defines the canonical Product-local artifacts, decisions, lineage, review gates, formalization targets, and downstream consumers used by MarkReg.

It does not redefine Core Objects, formal Order or Matter records, Execution state, official records, or Owning Service authority.

## 2. Constitutional Rules

| Rule ID | Rule |
| --- | --- |
| MR-CR-01 | Recommendation is not Decision. |
| MR-CR-02 | Product readiness is not approval. |
| MR-CR-03 | Approval is not execution. |
| MR-CR-04 | Submission is not official acknowledgement. |
| MR-CR-05 | Product projection is not official truth without source evidence. |
| MR-CR-06 | AI assistance never replaces accountable Human Review. |
| MR-CR-07 | Product-local artifacts do not silently become formal shared objects. |
| MR-CR-08 | Every material artifact has source lineage, version identity, responsibility, and supersession rules. |

Later chapters should reference these named rules instead of restating the full constitutional argument.

## 3. Canonical Lineage

```text
Business Context
→ Need Brief
→ Recommendation Set
→ Option Set
→ Proposal
→ Quote
→ Commercial Instruction
→ Formal Intake
→ Requirement Set
→ Readiness Assessment
→ Approved Filing Package Candidate
→ Order / Matter / Execution Handoff
```

Not every journey uses every artifact. Renewal, office-action, assignment, recordal, and portfolio journeys may enter at different points, but must preserve equivalent lineage, authority, and evidence.

## 4. Artifact and Decision Register

| ID | Artifact / Decision | Purpose | Product owner | Source inputs | Review / approval | Supersession | Formalization target | Main consumers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-A01 | Business Context Snapshot | Capture the business, brand, market, timing, budget, risk, and organization context used for the journey. | Product journey | authorized Workplace and user facts | user correction; professional review when material | new snapshot on material context change | none | Need Brief, Recommendation Set |
| MR-A02 | Need Brief | State the problem to solve before asking for formal filing data. | Product journey | Business Context Snapshot, user answers | user confirmation or professional correction | replaced by newer confirmed version | none | Recommendation Set, Proposal |
| MR-A03 | Recommendation Set | Record jurisdiction, route, filing-unit, class, goods/services, search, timing, and risk recommendations with assumptions and confidence. | Product journey | Need Brief, jurisdiction intelligence, portfolio context | accountable professional review for material advice | versioned; prior versions retained | selected decisions may later formalize | Option Set, Proposal, Intake |
| MR-A04 | Option Set | Present comparable alternatives, trade-offs, exclusions, estimated consequences, and next actions. | Product journey | Recommendation Set, pricing inputs | professional or commercial review as required | replaced when scope, fees, or assumptions change | none | Proposal, user selection |
| MR-A05 | Proposal | Explain the recommended service configuration and alternatives. | Product journey | Option Set | internal commercial/professional review | superseded by revised proposal | may lead to Quote | client, professional |
| MR-A06 | Quote | State priced scope, validity, currency, tax treatment, inclusions, exclusions, later-stage fees, assumptions, and payment terms. | commercial Product surface | approved pricing components | commercial approval under organization policy | expires or is replaced; prior quote retained | Order pricing terms | client, finance, sales |
| MR-D01 | Client Acceptance | Record which quote/version and scope the client accepts. | Product journey | valid Quote | client authority validation where required | cannot silently move to a new quote | commercial evidence | Order creation |
| MR-A07 | Commercial Instruction | Record the authorized request to proceed within accepted commercial scope. | Product journey | Client Acceptance, payment terms, authority context | client or organization-authorized actor | amended only by explicit change | Order / Matter trigger candidate | operations, finance |
| MR-A08 | Formal Intake | Collect service-specific facts required for professional preparation. | Product journey | confirmed recommendations, client facts, reused context | user completion; professional validation | versioned on material fact change | formal records through Owning Services | filing team, reviewer |
| MR-A09 | Requirement Set | Define documents, signatures, translations, certification, originals, evidence, deadlines, and jurisdiction-specific conditions. | Product journey | Formal Intake, jurisdiction pack | professional review where required | re-evaluated when rules or facts change | Document and task requirements | user, coordinator, reviewer |
| MR-A10 | Readiness Assessment | Evaluate structural, commercial, professional, documentary, payment, approval, and execution readiness. | Product journey | Intake, Requirement Set, pricing/payment, reviews | named accountable reviewer for overrides | expires on source, fee, rule, or fact change | gate evidence | user, professional, Execution |
| MR-D02 | Professional Decision | Accept, reject, revise, defer, or override a recommendation or readiness result with reasons. | accountable professional | reviewable artifact and evidence | authorized professional only | new decision supersedes but does not erase history | Review / approval record | Product, Execution, audit |
| MR-A11 | Filing Package Candidate | Assemble the version-specific content proposed for filing. | Product journey | approved intake, documents, requirements | professional review and client confirmation as applicable | superseded by new package version | formal Filing Package through Owning Service | approver, Execution |
| MR-D03 | Filing Approval | Authorize a specific Filing Package version for governed execution. | authorized human role | reviewed package and readiness evidence | explicit approval authority | invalidated by material package change | formal approval | Execution |
| MR-A12 | Handoff Envelope | Carry stable references, approved versions, unresolved warnings, responsibilities, deadlines, and expected return evidence into Order, Matter, and Execution contexts. | Product journey | accepted commercial and professional artifacts | handoff validation | new envelope for changed scope/version | formal objects through owning boundaries | Order, Matter, Execution |
| MR-A13 | Official Outcome Projection | Display official acknowledgement, status, notice, deadline, or outcome with source and retrieval metadata. | Product experience | official source or verified provider evidence | interpretation review when necessary | superseded but retained | official evidence remains externally authoritative | client, professional, portfolio |

## 5. Version and Supersession Rules

Every material artifact must carry:

- stable artifact identifier;
- version identifier;
- created and last-updated timestamps;
- source references and source versions;
- responsible actor;
- review status;
- approval status where applicable;
- validity or expiry conditions;
- superseded-by reference;
- downstream references already created from it.

A downstream artifact must identify the exact upstream versions it consumed. Updating an upstream artifact does not silently mutate an already accepted Quote, approved Filing Package, formal Order, Matter, or Execution instruction.

## 6. Change Propagation

| Change | Minimum Product response |
| --- | --- |
| Applicant identity changes | invalidate affected ownership, document, signature, quote, readiness, and filing-package assumptions |
| Jurisdiction changes | regenerate route, provider, fees, documents, timing, and readiness dependencies |
| Mark variant changes | re-evaluate filing units, search, classes, goods/services, image requirements, and cost |
| Official fee changes | expire or reprice affected Quote components according to quote terms |
| Jurisdiction rule version changes | identify affected artifacts and require revalidation before protected action |
| Client accepts a different option | preserve prior selection history and create new downstream scope |
| Professional override occurs | retain original recommendation, override reason, actor, evidence, and affected downstream artifacts |

## 7. Service-Family Conformance

A service family is supported only when MarkReg defines:

1. entry conditions;
2. minimum source facts;
3. canonical Product artifacts;
4. jurisdiction intelligence dependencies;
5. professional review and approval gates;
6. execution route;
7. expected official or external evidence;
8. outcome and status mapping;
9. future obligations and lifecycle continuation;
10. observable acceptance scenarios.

A page, form, provider listing, or fee table alone does not constitute service-family support.
