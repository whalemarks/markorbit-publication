# B05-CH-15 — Search, Availability and Risk Assessment

**Status:** Revised Draft — Productized  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part II — Need, Strategy and Recommendation  
**Revision basis:** B05-REVISION-PACK-001

## Chapter Purpose

Search is a decision-support activity, not a guarantee of registration, use, or freedom from dispute.

This chapter defines when MarkReg recommends search, how it scopes search modes, how findings are interpreted, and how risk changes the Recommendation Set, Option Set, and later commercial journey.

## 1. Product Question

> What search is proportionate to the filing decision, and how should the user understand the remaining risk?

The Product must distinguish:

- whether search is recommended;
- what data and jurisdictions are covered;
- which marks, classes, and goods/services are searched;
- which search method is used;
- what the findings mean;
- what they do not mean;
- what action follows.

## 2. Search Modes

MarkReg may support:

| Mode | Purpose |
| --- | --- |
| Exact or knockout search | Identify obvious identical or near-identical conflicts quickly. |
| Similarity search | Explore broader visual, phonetic, conceptual, or transliteration risk. |
| Class-limited search | Focus on selected classes or related goods/services. |
| Owner or portfolio search | Understand an identified party’s relevant rights. |
| Common-law or market search | Explore use signals outside a registration database where supported. |
| Device or image search | Review relevant figurative elements where data and tools permit. |
| Professional opinion | Convert search evidence into accountable strategy. |

The applicable jurisdiction pack must describe data coverage, freshness, known limitations, and source authority.

## 3. Search Scope Contract

A search request or result records:

- mark representation and version;
- jurisdiction and database scope;
- classes and goods/services version;
- search mode and method;
- search date and data freshness;
- source identifiers;
- query assumptions;
- result set or evidence references;
- automated confidence where used;
- professional interpretation status;
- material findings;
- recommended action;
- residual risk;
- supersession and re-search triggers.

Search outputs contribute to `MR-A03 Recommendation Set`. They do not become official status or final professional advice automatically.

## 4. Product Behavior

MarkReg should:

1. recommend search according to market importance, timing, mark distinctiveness, known conflicts, and risk posture;
2. show the difference between search modes;
3. calculate affected scope from filing units, classes, goods/services, and jurisdictions;
4. expose data limitations and freshness;
5. group findings by relevance without hiding the underlying evidence;
6. request professional interpretation for material risk;
7. connect findings to concrete options: proceed, narrow, change, defer, search further, or seek advice;
8. preserve original findings and later decisions;
9. identify when changed inputs require re-search.

## 5. Risk Expression

Risk should not be reduced to a single unexplained score.

A useful risk assessment identifies:

- issue type;
- affected mark, jurisdiction, class, and item;
- source evidence;
- similarity or conflict basis;
- confidence and uncertainty;
- likely consequence;
- available response options;
- professional interpretation;
- user decision;
- revalidation trigger.

Labels such as low, moderate, or high may summarize the assessment but cannot replace the explanation.

## 6. User Surface

The user sees:

- whether search is recommended and why;
- available search modes and costs;
- scope covered;
- data limitations;
- material findings in plain language;
- affected filing options;
- recommended next steps;
- one primary action: **Order search, revise scope, or proceed with recorded risk**.

The Product must state that no search eliminates all risk.

## 7. Reference Journey A — EMBERLOOP

MarkReg recommends knockout searches in all core markets and expanded review in the United States and European Union.

A similar mark appears for grill-related goods. The professional records moderate risk and recommends narrowing one goods description while retaining the broader word-mark strategy.

The Recommendation Set is revised. The prior wording and original search findings remain traceable.

## 8. Conformance Scenarios

### MR-CH15-SCN-01 — Material input change

**Given** the user replaces the selected device or materially changes goods/services after search.  
**When** the Recommendation Set is recalculated.  
**Then** MarkReg identifies the affected search assumptions, marks the result partially or fully stale, and recommends the appropriate re-search or professional validation.  
**Authority boundary:** the Product does not treat the old search as covering a new filing unit or scope.  
**Evidence retained:** old and new inputs, prior search, stale reason, and resulting decision.

### MR-CH15-SCN-02 — Proceeding with known risk

**Given** a professional interpretation identifies moderate conflict risk.  
**When** the user chooses to proceed.  
**Then** MarkReg records the selected option, the explained risk, the actor and authority, and the exact downstream versions affected.  
**Authority boundary:** user acceptance of risk does not replace filing approval.  
**Evidence retained:** finding, advice, options, user decision, and professional review.

## 9. Freshness and Official-Source Boundary

Search and status data must show retrieval time and source coverage.

A stale database result or Product projection must not be presented as current official truth. `MR-SCN-10`, `MR-CR-04`, and `MR-CR-05` apply.

## 10. Product Measures

Useful measures include:

- search recommendation acceptance rate;
- re-search frequency caused by changed scope;
- percentage of material findings receiving professional review;
- recommendation changes caused by search;
- rate of users proceeding with documented risk;
- later conflicts traceable to known versus unknown search limitations.

Metrics must not reward unnecessary searches or overstate predictive certainty.

## 11. Handoff to Part III

Part II now provides a versioned Recommendation Set covering:

- jurisdictions and routes;
- country bundles;
- filing units;
- applicant and authority context;
- classes;
- goods/services scope;
- search and risk.

Part III converts those recommendations into comparable options, Proposal, Quote, acceptance, Formal Intake, requirements, readiness, and governed handoff.