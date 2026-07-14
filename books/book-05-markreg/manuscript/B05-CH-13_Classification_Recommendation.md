# B05-CH-13 — Classification Recommendation

**Status:** Revised Draft — Productized  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part II — Need, Strategy and Recommendation  
**Revision basis:** B05-REVISION-PACK-001

## Chapter Purpose

Classification is not a keyword-to-number lookup. It connects the user’s actual offering, intended use, filing unit, jurisdictions, goods/services wording, search scope, fee structure, and future protection strategy.

This chapter defines how MarkReg creates explainable class candidates while preserving uncertainty and professional review.

## 1. Product Question

> Which classes are necessary, related, optional, uncertain, or unsupported for the confirmed business need?

The Product should reduce the user’s need to understand classification systems without hiding why a class is proposed.

## 2. Required Inputs

Classification may consume:

- confirmed Need Brief;
- filing-unit candidates;
- current and planned products and services;
- software, platform, retail, manufacturing, and support activities;
- jurisdictions and routes;
- existing rights;
- evidence of use or launch plans;
- budget preference;
- jurisdiction-pack classification version and local deviations.

The Product must retain the source business descriptions used for each recommendation.

## 3. Class Recommendation Categories

| Category | Meaning |
| --- | --- |
| Primary | Directly supports the main current or planned offering. |
| Related | Protects a connected commercial activity or material extension. |
| Optional | May add value but is not currently essential. |
| Future | Relevant only after a stated expansion trigger. |
| Uncertain | Material ambiguity requires clarification or professional review. |
| Unsupported | Current facts do not justify the class. |

A class candidate should never be presented only as a number.

## 4. Class Candidate Contract

Each candidate records:

- class number and classification edition/version;
- jurisdiction or route applicability;
- category;
- business rationale;
- source products, services, or activities;
- linked filing units;
- goods/services concepts to be drafted;
- local deviations and item limits;
- fee effect;
- search effect;
- confidence or uncertainty;
- professional review status;
- user selection;
- supersession history.

Class candidates form part of `MR-A03 Recommendation Set` and feed the Option Set.

## 5. Product Behavior

MarkReg should:

1. translate business language into class candidates;
2. separate goods, software, retail, platform, and other activities where needed;
3. show primary and related classes before optional expansion;
4. identify unsupported assumptions;
5. explain local class or item-count consequences;
6. connect each class to proposed goods/services concepts;
7. show added fees and search scope;
8. request professional review for material ambiguity;
9. preserve removed candidates and reasons.

## 6. User Surface

The user sees:

- class number and plain-language label;
- why it is suggested;
- which business activities support it;
- primary, related, optional, or uncertain status;
- estimated fee and search impact;
- linked goods/services concepts;
- local warnings;
- one primary action: **Accept, remove, or request review**.

The Product should not force the user to browse the entire classification system before receiving a recommendation.

## 7. Reference Journey A — EMBERLOOP

EMBERLOOP combines smart outdoor cooking equipment with a companion application and possible online retail activity.

MarkReg identifies:

- a primary equipment class;
- a primary or related downloadable-software class;
- an optional retail-services class;
- possible connected-device or platform concepts requiring clarification.

The user chooses a narrower launch scope. The Product preserves the deferred retail and service candidates as future expansion notes.

## 8. Conformance Scenario

### MR-SCN-04 — Class uncertainty

**Given** a product spans hardware, software, and online retail activity.  
**When** class candidates are generated.  
**Then** MarkReg separates primary, related, optional, and unsupported classes; explains why each is suggested; and requests professional review where ambiguity is material.  
**Authority boundary:** automated classification is not final professional advice.  
**Evidence retained:** source business description, classification version, confidence, user selection, and reviewer changes.

## 9. Local Variation and Versioning

The same business concept may produce different acceptable wording, item counts, fees, or procedural consequences across jurisdictions.

Each evaluation must retain:

- jurisdiction-pack version;
- classification edition;
- local deviation;
- effective date;
- input facts;
- result;
- review status.

A pack update must identify affected class candidates and downstream goods/services versions.

## 10. Change Propagation

Adding or removing a class may change:

- goods/services wording;
- search scope;
- official and professional fees;
- provider cost;
- filing-unit strategy;
- Proposal and Quote;
- documents and declarations;
- readiness.

The Product creates a new Recommendation Set or Option Set version rather than mutating accepted commercial scope.

## 11. Handoff to CH14

Class selection defines broad categories only.

CH14 translates the chosen business scope into jurisdiction-specific goods and services that are explainable, reviewable, versioned, and connected to fee and search consequences.