# B05-CH-13 — Classification Recommendation

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part II — Need, Strategy and Recommendation

## Chapter Purpose

Classification is not a keyword-to-number lookup. It connects the user’s offering, intended use, filing units, jurisdictions, goods/services wording, search scope, fees and future protection strategy.

This chapter defines how MarkReg prepares explainable class candidates while preserving uncertainty, local variation and Professional Review.

The controlled example is `EL-06` in B05-SPEC-0002.

## 1. Product Question

> Which classes are primary, related, optional, future, uncertain or unsupported for the confirmed business need?

The Product should reduce the user’s need to understand the classification system without hiding why a class is proposed or what would change the recommendation.

## 2. Required Context

Classification may use:

- confirmed Need Brief;
- selected filing-unit candidates;
- current and planned products, software, services and commercial activities;
- jurisdictions and routes;
- existing rights;
- use evidence or launch plans;
- budget preference;
- applicable classification edition;
- Jurisdiction Pack version, local deviations, item rules and support state.

Every class recommendation must retain the business description and source context from which it was derived.

## 3. Recommendation Categories

| Category | Meaning |
| --- | --- |
| Primary | Directly supports the main current or planned offering. |
| Related | Protects a connected commercial activity or material extension. |
| Optional | May add value but is not currently essential. |
| Future | Relevant after a stated expansion trigger. |
| Uncertain | Material ambiguity requires clarification or Professional Review. |
| Unsupported | Current facts do not justify the class. |

A class candidate should not appear only as a number. It should show the supported activity, consequence and uncertainty.

## 4. Controlled Output

Class candidates belong to `MR-A03 Recommendation Set` and record:

- class number and classification edition;
- jurisdiction or route applicability;
- recommendation category;
- business rationale and source activities;
- linked filing units;
- goods/services concepts to be drafted;
- local deviations and item limits;
- official-fee, client-price and search effects;
- confidence and uncertainty;
- Professional Review state;
- user selection;
- version and supersession history.

A class candidate is not filing scope. Selected classes still require goods/services definition, commercial confirmation and later Package Review.

## 5. Product Behavior

MarkReg should:

1. translate business language into candidate classes;
2. separate goods, software, platform, retail, manufacturing and support activities where needed;
3. show primary and related classes before optional expansion;
4. identify unsupported assumptions;
5. explain local item-count and fee consequences;
6. connect each class to goods/services concepts;
7. show added search and provider effects;
8. request Professional Review for material ambiguity;
9. preserve removed and deferred candidates with reasons.

AI may classify candidates and compare source descriptions. It must show confidence, source basis and uncertainty. A Human remains responsible for professional disposition.

## 6. User Surface

The user should see:

- class number and plain-language label;
- supporting business activities;
- category and rationale;
- linked goods/services concepts;
- estimated fee and search effects;
- local warnings and uncertainty;
- one primary action: **Accept, remove or request Review**.

The Product should not require the user to browse the complete classification system before receiving useful guidance.

## 7. Reference Journey — `EL-06 EMBERLOOP`

EMBERLOOP combines smart outdoor cooking equipment with a companion application and possible online retail activity.

MarkReg identifies:

- a primary equipment class;
- a primary or related downloadable-software class;
- an optional retail-services class;
- connected-device or platform concepts requiring clarification.

Northstar chooses a narrower launch scope. Deferred retail and service candidates remain future-action notes rather than current filing scope.

## 8. Controlled Scenarios

### `MR-SCN-04` — Class uncertainty

Where hardware, software and retail activities overlap, MarkReg separates primary, related, optional and unsupported candidates and requires Professional Review where ambiguity is material. Automated classification is not final advice.

### `MR-SCN-09` — Professional override

A sourced local exception may support a scoped, versioned professional override. The override records reviewer, reason, source, affected jurisdiction and revalidation condition.

Minimum evidence includes business description, classification version, Pack Version, confidence, user selection and reviewer changes.

## 9. Local Variation and Change

The same business concept may produce different wording, item counts, fees or procedural consequences across jurisdictions.

A Pack or classification update must identify affected:

- class candidates;
- goods/services versions;
- search scope;
- official fees and client price;
- provider cost;
- Proposal and Quote;
- declarations and documents;
- readiness.

The Product creates a new Recommendation Set or Option Set version rather than mutating accepted commercial scope.

## 10. Handoff to CH14

Class selection defines broad categories only.

CH14 translates the selected business scope into jurisdiction-specific goods and services that remain explainable, reviewable, versioned and connected to fee and search consequences.
