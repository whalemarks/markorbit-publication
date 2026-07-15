# B06-PLN-0002 — Book 06 Authority and Source Map

## 1. Status

```text
Record: B06-PLN-0002
Status: Controlled Source Map v0.1
Purpose: identify the governing source for every major Book 06 responsibility
Authority change created: NO
```

## 2. Authority hierarchy

| Level | Source | Book 06 use |
| --- | --- | --- |
| 1 | MarkOrbit Orbital Architecture Canon and ADR vNext | constitutional language and accepted Lite identity |
| 2 | Books 01–04 Portfolio Baseline | vision, shared meaning, Execution, Workplace and Product conformance |
| 3 | Book 05 RC1 | MarkReg-specific Handoff, Product Session and Return behavior |
| 4 | Book 06 Product Charter and Specifications | Lite purpose, Product-local records, journeys, scenarios and MVP |
| 5 | supplemental Product research | candidate ideas requiring assessment |
| 6 | ADRs, contracts and code | implementation only; cannot create professional meaning |

## 3. Repository-level sources

| Source | Controlling meaning for Book 06 |
| --- | --- |
| `governance/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.md` | Lite is a lightweight Workplace for trademark professionals; Today/NBA is the primary experience; Product and authority boundaries remain separate |
| `governance/ARCHITECTURE-DECISION-REGISTER-vNEXT.md` | ARC-009, ARC-015, ARC-017–021, ARC-024, ARC-026–027 |
| `release/baselines/MO-PUB-BASELINE-0001_Books_01-04.md` | accepted Books 01–04 dependency chain and Change Proposal classes |
| `reviews/portfolio/MO-PUB-REV-0001_Books_01-04_Portfolio_Baseline_Review.md` | cross-book locks and historical-errata interpretation |
| `PUBLICATION-GOVERNANCE.md` | downstream books record findings; they do not silently edit accepted upstream meaning |

## 4. Book 01 sources

| Topic | Source | Book 06 implication |
| --- | --- | --- |
| industry and OS purpose | `books/book-01-operating-system/manuscript/02_Chapter_01.md` and Book 01 overall | Lite is one Product expression, not the Operating System |
| business value | `manuscript/06_Chapter_05.md` | organizations create customer value, growth strategy and differentiation |
| Workplace | `manuscript/07_Chapter_06.md` | Organization remains actor; Workplace is operating environment; Lite does not replace the organization |
| operating models | Book 01 Part III | Lite must support different professional business models without imposing one sales doctrine |
| ecosystem | Book 01 Part IV | external capability and collaboration remain bounded by the network architecture |

## 5. Book 02 sources

| Responsibility | Existing authority | Lite treatment |
| --- | --- | --- |
| identity, organization, user and role | Core objects/services | consume references and authorized context |
| permission and policy | Core contracts/services | evaluate; never replace with UI availability |
| customer/contact | Customer services | display and reference; no duplicate Lite customer model |
| brand/trademark | Brand and Trademark services | consume and enrich through Product-local presentation |
| document/evidence | Document and Evidence boundaries | reference and prepare; do not relabel case files as Evidence or formal Documents |
| order/matter | owning services | receive or display formal references; do not create silently |
| task | Task Service | Today item or recommendation may request Task creation only |
| opportunity | Opportunity Service | lead or Value Candidate may request qualification; no silent formal Opportunity |
| communication | Communication Service | draft/prepare only until governed send |
| AI output and recommendation | AI governance | preserve Agent, source, context, review and disposition |
| knowledge | Knowledge governance | consume governed Knowledge; local experience remains private/candidate until promoted |

## 6. Book 03 sources

| Topic | Source | Book 06 implication |
| --- | --- | --- |
| Task lifecycle | `B03-CH-11_Task_Lifecycle_Model.md` | Today/NBA/lead card is not active Task |
| Review and approval | Book 03 CH12 and CH28 | review is version- and scope-specific |
| Communication | `B03-CH-13_Communication_Execution_Boundary.md` | draft, review, approve, prepare send and send remain separate |
| Permission/Policy gates | Book 03 CH15 | current authorization is re-evaluated before action |
| Human–AI handoff | `B03-CH-16_Human_AI_Execution_Handoff.md` | AI prepares; Human and Owning Service retain authority |
| idempotency/failure | Book 03 CH25–CH26 | follow-up, publish and handoff retries must not duplicate effects |
| MVP boundary | Book 03 CH31–CH33 | external protected action remains separately gated |

## 7. Book 04 sources

| Topic | Primary source | Book 06 responsibility |
| --- | --- | --- |
| organization context | CH07–CH12 | consume identity, clients, private Knowledge, memory and data zones |
| Assistant/Guide/Agent | CH16 | preserve distinct user-facing and runtime roles |
| value candidates and NBA | CH17 | define Lite-specific candidate production, explanation and ranking |
| Prepared Action | CH18 | define Lite preparation packages and handoff behavior |
| Human Review/Owning Service | CH19 | no direct professional or formal authority |
| Product architecture | CH20–CH22 | preserve focused Product identity and purpose-bound context |
| Lite profile | CH23 | dedicated Book 06 starting constitution |
| MarkReg/MGSN profiles | CH24–CH25 | Lite must hand off instead of absorb |
| cross-Product continuity | CH27 | define typed launch, preparation, review, execution, outcome and failure returns |
| Asset Library | CH28 | case examples/templates are governed reusable resources |
| Content/Artifact/Document | CH29 | case-derived outputs are Artifacts; internal files and formal Documents remain distinct |
| Artifact lifecycle | CH30 | version, source, rights, review and approval |
| Render/Edit/Delivery/Publish | CH31 | one-click language must preserve separate consequences |
| outcome and feedback | CH32 | Product result, formal result and business outcome remain distinct |
| conformance | CH38 | Product Charter, specifications and implementation must show traceable authority and evidence |

## 8. Book 05 sources

| Topic | Source | Lite constraint |
| --- | --- | --- |
| entry and embedded experience | CH43 | one MarkReg journey; Lite supplies purpose-limited context |
| participant surfaces | CH44 | visibility and action rights remain role- and purpose-limited |
| Pack/AI governance | CH45 | jurisdiction rules, sources and AI output remain governed |
| metrics and MVP | CH46 | speed, activity and legal outcome are not sufficient quality measures |
| conformance | CH47 | publication, pilot, implementation, production and protected action remain separate |
| Product records | B05-SPEC-0001 | consume MR-A12 Handoff, MR-C10 Product Session, MR-A30 Return Envelope |
| cross-book reconciliation | B05-PUB-0007 | Book 05 only defines its bounded behavior inside Lite; full Lite architecture belongs to Book 06 |

## 9. Required Book 06 traceability

Every future Book 06 Product record, journey or scenario should identify:

```text
Book 06 concept
→ governing Book 01 principle
→ consumed Book 02 object/service or explicit Product-local status
→ Book 03 execution boundary where consequence exists
→ Book 04 Workplace/Product requirement
→ Book 05 contract where MarkReg participates
→ Book 06 owner and lifecycle
→ conformance scenario and evidence
```

## 10. Finding classification rule

A Book 06 issue must be classified as:

- **PASS** — existing authority is sufficient;
- **PRODUCT-LOCAL DECISION** — Book 06 may define behavior without upstream change;
- **EDITORIAL CORRECTION** — wording or reference only;
- **UPSTREAM FINDING** — ambiguity or missing shared contract should be recorded;
- **CHANGE PROPOSAL REQUIRED** — proposed meaning would alter frozen Core, Execution authority or Workplace/Product constitution.

No upstream semantic change has been identified by the current audit.
