# B05-CH-16 — Proposal and Option Design

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

Part II produced a versioned `Recommendation Set` and `Option Set`. This chapter turns those strategic candidates into a decision-ready `Proposal` without collapsing recommendation, price, acceptance, instruction, approval or Execution.

The controlled output is `MR-A05 Proposal`. The `EMBERLOOP` reference step is `EL-09`.

## 1. Product Question

> Which service option should the client choose, what does each option include, and what changes if the client chooses differently?

A Proposal should reduce decision burden without hiding legal scope, assumptions or later obligations.

```text
Recommendation
→ comparable options
→ informed client selection
```

The Proposal does not yet create a Quote, binding acceptance, Commercial Instruction, Order, Matter or filing authority.

## 2. Proposal Contract

A conforming Proposal references exact upstream versions and records:

| Field | Required meaning |
| --- | --- |
| objective | confirmed business objective and Need Brief version |
| option identity | stable ID and version for every option |
| scope atoms | jurisdiction, route, filing unit, class, item, search, service stage and provider need |
| recommendation category | required, strongly recommended, optional, deferred or not recommended |
| inclusions | work, Review cycles, stages and deliverables included |
| exclusions | omitted searches, later fees, disputes, legalization, courier or other work |
| assumptions | applicant, route, class count, item count, timing, documents, provider and Pack Version |
| dependencies | decisions, evidence or events required before later progression |
| consequences | coverage, timing, price, risk, maintenance and priority effects |
| price state | estimate-ready, quote-ready or pricing blocked |
| validity | expiry and revalidation conditions |
| next action | select, customize, request Review, defer or reject |

The Proposal references the `Recommendation Set` and `Option Set`; it does not detach copied facts from their source versions.

## 3. Option Design

Useful patterns include:

```text
Minimum Required Protection
Recommended Launch Protection
Expanded Portfolio Coverage
Staged Filing Plan
Search-First Plan
Urgent Filing with Recorded Residual Risk
```

Options must reflect real strategic differences. Bronze, silver and gold labels do not conform when they hide differences in rights, stages, search depth or later costs.

Each option remains decomposable by:

- jurisdiction and route;
- filing unit and mark variant;
- applicant assumption;
- class and goods/services scope;
- search level;
- professional and provider service;
- document and formality requirements;
- included and excluded lifecycle stages;
- deadline or filing wave.

A lower total may mean narrower scope, fewer rights, deferred work or excluded later stages. The comparison must say which.

## 4. User Surface

The primary surface shows:

1. the objective being solved;
2. the recommended option and rationale;
3. meaningful alternatives;
4. a like-for-like difference table;
5. assumptions and unresolved decisions;
6. included and excluded stages;
7. current price and timing state;
8. one primary next action.

The client may select an option, customize permitted scope atoms, request Professional Review, defer an element or request a revised option.

```text
Option selection
≠ Quote acceptance
≠ Commercial Instruction
≠ Filing Approval
```

## 5. Controlled Change

A material change to applicant, mark, jurisdiction, route, class, goods/services, search scope, deadline, provider need or Pack Version creates a new Option Set and Proposal version.

The Product identifies:

- changed scope atoms;
- assumptions made stale;
- price inputs requiring recalculation;
- prior selections preserved;
- Review or approval requiring repetition;
- downstream records that must not silently change.

`MR-SCN-13` applies when the business facts change after recommendation. `MR-SCN-14` applies when the client knowingly selects a non-recommended option.

## 6. Professional and Commercial Intervention

Professional Review is required when option suitability depends on material legal, procedural or risk judgment.

Commercial review is required for:

- non-standard scope;
- discount or margin exception;
- unusual payment or credit terms;
- uncertain provider cost;
- capped or fixed-price commitments;
- urgent or high-exposure work.

AI may compose, compare, summarize and explain options. It may not grant a discount, waive an exclusion, promise an outcome or select for the client.

## 7. Reference Journey — `EL-09`

For `EMBERLOOP`, MarkReg presents:

| Option | Scope | Main trade-off |
| --- | --- | --- |
| A | word mark in US and EU | lowest launch cost; UK and device deferred |
| B | word and device in US, EU and UK | recommended launch coverage; higher filing and maintenance burden |
| C | word and device in five markets | broader coverage; exceeds the stated initial budget |
| D | search-first staged plan | reduces filing uncertainty; may pressure the launch schedule |

The professional recommends Option B. The client selects that exact option version. Japan and Australia remain deferred candidates with visible reconsideration triggers.

This selection becomes the source for pricing. It is not yet Quote acceptance or authorization to begin filing.

## 8. Conformance Check

**Given** the client selected Option B.  
**When** the client removes the device filing and adds Japan.  
**Then** MarkReg creates new Option Set and Proposal versions, recalculates affected inputs and preserves the prior selection.

**Boundary:** the Product may compose the revision but does not bind either party.  
**Evidence:** prior and new versions, changed scope atoms, actor, rationale and affected price state.

## 9. Failure Modes

Reject:

```text
One package presented as one legal right
Required and optional scope mixed together
Later stages hidden
Search included without scope
Selected option treated as accepted Quote
Proposal overwritten after selection
AI-created commercial exception
Assumptions buried in unstructured text
```

## 10. Chapter Output and Handoff

CH16 produces `MR-A05 Proposal`, linked to exact upstream artifacts and containing one or more decision-ready options.

CH17 applies the controlled commercial component model and creates the source-backed price basis for the selected option.