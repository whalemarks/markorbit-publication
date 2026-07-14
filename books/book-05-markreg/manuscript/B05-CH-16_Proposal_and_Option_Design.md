# B05-CH-16 — Proposal and Option Design

**Status:** Productized Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

Part II produced a versioned `Recommendation Set` and `Option Set`. This chapter turns those strategic candidates into a decision-ready `Proposal` without collapsing recommendation, price, acceptance, instruction, approval, or execution.

The canonical artifacts and rules are defined by:

- `B05-SPEC-0001` — Product Artifact and Decision Map;
- `B05-SPEC-0002` — Reference Journeys;
- `B05-SPEC-0003` — Conformance Scenarios and User-Surface Contract;
- `B05-SPEC-0004` — Jurisdiction-Pack and Commercial-Control Contract.

The controlling rule is `MR-CR-01`: Recommendation is not Decision.

## 1. User Question

> Which service option should I choose, what does each option include, and what changes if I choose differently?

The Product should not present one opaque package with a “recommended” badge. It must provide meaningful alternatives with comparable scope, assumptions, consequences, and next actions.

## 2. Proposal Contract

A `Proposal` must reference exact upstream versions and contain:

| Field | Required meaning |
| --- | --- |
| Objective | the confirmed business problem and Need Brief version |
| Option identity | stable ID and version for every option |
| Scope atoms | jurisdiction, route, filing unit, class, items, search, stage, provider need |
| Decision category | required, strongly recommended, optional, deferred, not recommended |
| Inclusion | work, review cycles, filing stages and deliverables included |
| Exclusion | omitted searches, later fees, disputes, legalization, courier or other work |
| Assumptions | applicant, route, class count, item count, timing, documents, provider and rules |
| Dependencies | decisions or events that must occur before later progression |
| Consequences | coverage, timing, cost, risk, maintenance and priority effects |
| Price state | estimate-ready, quote-ready, or pricing blocked |
| Validity | expiry conditions and sources that may require revalidation |
| Next action | select, customize, request review, defer, or reject |

A Proposal references the `Recommendation Set`; it does not silently copy or detach from it.

## 3. Option Design

Useful option patterns include:

```text
Minimum Required Protection
Recommended Launch Protection
Expanded Portfolio Coverage
Staged Filing Plan
Search-First Plan
Urgent Filing with Recorded Residual Risk
```

Options must represent real strategic differences. Artificial bronze/silver/gold packaging that hides legal scope does not conform.

## 4. Atomic Scope and Comparison

Every option must remain decomposable by:

- jurisdiction and filing route;
- filing unit and mark variant;
- applicant assumption;
- class and goods/services package;
- search level;
- professional and provider service;
- documents and formalities;
- included and later stages;
- deadline or phase.

The comparison surface must show like-for-like differences. A lower total may reflect fewer rights, narrower scope, excluded stages, lower search depth, or deferred work.

## 5. User Surface

The primary screen should show:

1. the objective being solved;
2. the recommended option and reason;
3. alternative options;
4. a difference table;
5. assumptions and unresolved decisions;
6. exclusions and expected later work;
7. cost state and timing state;
8. one primary next action.

The user may:

- select an option;
- customize allowed scope atoms;
- request professional review;
- defer an element;
- ask for a revised option;
- preserve the current option without instructing work.

Option selection does not equal Quote acceptance or Commercial Instruction.

## 6. EMBERLOOP Reference Journey

For `EMBERLOOP`, MarkReg presents:

| Option | Scope | Main trade-off |
| --- | --- | --- |
| A | word mark in US and EU | lowest launch cost; UK and device deferred |
| B | word and device in US, EU and UK | recommended launch coverage; higher filing and maintenance cost |
| C | word and device in five markets | broader coverage; exceeds the stated initial budget |
| D | search-first staged plan | reduces filing risk; may pressure the launch schedule |

The Product explains that the word mark is the core filing unit, the device is strongly recommended, and Japan and Australia may be deferred with visible consequences.

The client selects Option B. The selection is recorded against the exact option version and becomes the source for pricing. It is not yet a binding Quote acceptance.

## 7. Conformance Scenario — Material Option Change

**Given** the client selects Option B.  
**When** the client removes the device filing and adds Japan.  
**Then** MarkReg creates a new Option Set and Proposal version, recalculates affected scope and price inputs, and preserves the prior selection.  
**Authority boundary:** the Product may compose the revised option but does not bind either party.  
**Evidence retained:** prior and new options, changed scope atoms, actor, reason, affected estimates and acceptance state.

## 8. Change Propagation

A material change to applicant, mark variant, jurisdiction, route, class, goods/services, search scope, deadline, provider requirement or rule version must identify:

- affected option elements;
- affected assumptions;
- pricing components that became stale;
- prior user selections;
- review or approval that must be repeated;
- downstream artifacts that must not silently change.

## 9. Professional and Commercial Intervention

Professional review is required when option suitability depends on material legal, procedural or risk judgment.

Commercial review is required when an option contains:

- non-standard scope;
- discount or margin exception;
- unusual payment terms;
- provider-cost uncertainty;
- capped or fixed-price commitments;
- urgency or high commercial exposure.

AI may compose, compare and explain. It may not grant discounts, waive exclusions, promise outcomes, or select for the client.

## 10. Failure Modes

The Product must reject:

```text
One package presented as one legal right
Required and optional scope mixed together
Later-stage fees hidden
Search embedded without scope
Selected option treated as accepted Quote
Proposal overwritten after selection
AI-created commercial exception
Assumptions buried in unstructured text
```

## 11. Chapter Output

The chapter output is a versioned `Proposal` containing one or more decision-ready options linked to exact upstream artifacts.

The next chapter applies the commercial component model and produces a transparent, controllable price basis for the selected option.