# B05-CH-08 — Need Understanding Before Forms

**Status:** Revised Draft — Productized  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part II — Need, Strategy and Recommendation  
**Revision basis:** B05-REVISION-PACK-001

## Chapter Purpose

MarkReg begins with the business problem, not with a filing form.

This chapter defines how the Product converts an ordinary-language request into a versioned **Need Brief** that can support jurisdiction, route, filing-unit, classification, goods/services, search, pricing, and intake decisions.

The canonical artifact and version rules are defined in [B05-SPEC-0001](../specifications/B05-SPEC-0001_Product_Artifact_and_Decision_Map.md). The reference case used here is Journey A in [B05-SPEC-0002](../specifications/B05-SPEC-0002_Reference_Journeys.md).

## 1. Product Question

> What problem is the user actually trying to solve, and which missing facts would materially change the next recommendation?

The Product must not assume that “register this logo” already determines:

- the applicant;
- the filing unit;
- the jurisdictions;
- the route;
- the classes;
- the goods and services;
- the search scope;
- the budget allocation;
- the timing strategy.

It must also avoid replacing a paper form with a longer questionnaire.

## 2. Inputs and Source Hierarchy

The Need Brief may consume:

1. authorized organization and client context;
2. existing brand and portfolio records;
3. user-provided business facts;
4. uploaded brand assets;
5. timing, budget, and risk preferences;
6. professional corrections or clarifications.

Known facts should be reused rather than re-asked. A fact is re-requested only when it is stale, ambiguous, conflicting, or insufficient for the present purpose.

Every consumed fact must be distinguishable as:

- source-backed;
- user-confirmed;
- inferred;
- professionally corrected;
- unresolved.

## 3. Minimum Question Set

The first interaction should normally resolve only:

| Area | Minimum question |
| --- | --- |
| Objective | What business outcome should the trademark protection support? |
| Markets | Where is the business active or planning to launch? |
| Offering | What products, software, services, or commercial activities are involved? |
| Timing | Is there a launch, exhibition, crowdfunding, filing, or priority deadline? |
| Use | Which marks are already used, and in what form? |
| Ownership | Is there a known applicant or group ownership policy? |
| Risk | Is pre-filing search or speed more important? |
| Budget | Which markets or filing units must be prioritized if scope must be reduced? |

The Product should ask a follow-up question only when the answer changes a material recommendation or exposes a professional-risk issue.

## 4. Need Brief Contract

The Need Brief is `MR-A02` under B05-SPEC-0001.

A conforming Need Brief includes:

- stable artifact and version identifiers;
- business objective;
- brand and offering summary;
- current and planned markets;
- relevant timing;
- initial applicant and authority context;
- known mark forms;
- budget and risk posture;
- assumptions;
- unresolved questions;
- source references;
- user confirmation or correction status.

The Need Brief is not Formal Intake. It is intentionally smaller and may contain unresolved assumptions.

## 5. Product Interaction

The user surface should show:

- the interpreted need in plain language;
- facts reused from authorized context;
- assumptions the Product made;
- conflicts or uncertainty;
- one primary action: **Confirm or edit the Need Brief**;
- an explanation that confirmation allows recommendations to begin but does not authorize filing.

A material edit must show the likely consequence before application. For example, changing the launch market may affect route, fees, provider requirements, documents, and timing.

## 6. Reference Journey A — EMBERLOOP

For Northstar Kitchenware, MarkReg asks only for product categories, planned launch markets, launch date, current use, applicant structure, mark forms, and budget priority.

It reuses known company registration data and produces:

> **Need Brief v1:** Protect the `EMBERLOOP` word mark and core flame-loop device before launch; prioritize the United States and European Union; avoid unnecessary filings; preserve a later expansion route for the United Kingdom, Japan, and Australia.

The user can correct the market priority or mark forms before any jurisdiction recommendation is produced.

## 7. Conformance Scenario

### MR-CH08-SCN-01 — Progressive clarification

**Given** the user requests “register our brand overseas” and the organization profile already contains company and brand records.  
**When** MarkReg prepares the Need Brief.  
**Then** it reuses known facts, asks only for markets, offering, timing, mark forms, risk, and budget, exposes its assumptions, and requests confirmation.  
**Authority boundary:** the Product interprets the need but does not make the final legal or commercial decision.  
**Evidence retained:** source records, questions asked, answers, assumptions, revisions, and confirmed Need Brief version.

Applicant conflict is governed by `MR-SCN-01` in [B05-SPEC-0003](../specifications/B05-SPEC-0003_Conformance_Scenarios_and_User_Surfaces.md).

## 8. Change and Supersession

A material change creates a new Need Brief version. Prior versions remain available.

Changes to markets, offering, applicant, mark form, timing, or budget must identify affected downstream artifacts. They must not silently rewrite an accepted Proposal, Quote, Formal Intake, or formal business object.

This applies `MR-CR-07` and `MR-CR-08`.

## 9. Product Measures

Useful measures include:

- questions asked before first Need Brief;
- percentage of authorized facts reused;
- user correction rate;
- time to confirmation;
- downstream recommendation revisions caused by missed need facts;
- rate of premature form abandonment.

The objective is not the fewest possible questions. It is the fewest questions that preserve a safe and explainable next decision.

## 10. Handoff to CH09

A confirmed Need Brief authorizes preparation of a **Recommendation Set**. It does not authorize filing, payment, provider appointment, or creation of official truth.

CH09 uses the Need Brief to determine which jurisdictions and filing routes should be required, recommended, optional, deferred, or rejected.