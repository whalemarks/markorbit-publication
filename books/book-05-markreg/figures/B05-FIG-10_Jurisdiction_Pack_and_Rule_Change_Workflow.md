# B05-FIG-10 — Jurisdiction Pack and Rule Change Workflow

## Control

- **Status:** Controlled Figure Source v1.0 — PF-07
- **Disposition:** retained
- **Format:** Mermaid flowchart
- **Primary sources:** CH45, B05-SPEC-0004 v0.3 and Appendix F
- **Intended placement:** CH45 and Appendix F

## Caption

**Figure 10. A detected legal, fee, form or practice change does not become an active Product rule automatically.** The change must be sourced, analyzed, professionally reviewed, tested and released as a new Pack version before protected Product behavior may depend on it.

## Controlled Source

```mermaid
flowchart TB
    SIG["change signal\nofficial publication, provider advice, portal behavior or monitoring"] --> E07["MR-E07\nSource Record"]
    E07 --> G04["MR-G04\nRule Change Candidate"]
    G04 --> IMP["affected Rule, form, fee, Quote, package, approval and open-journey analysis"]
    IMP --> D02{"MR-D02\nProfessional Decision"}
    D02 --> G02["MR-G02\nRule Record"]
    G02 --> TEST["scenario and regression evidence"]
    TEST --> G01["MR-G01\nJurisdiction Pack"]
    G01 --> G03["MR-G03\nimmutable Pack Version Record"]
    G03 --> D12{"MR-D12\nPack Release Approval"}
    D12 --> REL["released support state and effective scope"]
    REL --> REV["affected journey revalidation, repricing, re-signature, suspension or no-action disposition"]

    G05["MR-G05\nOrganization Overlay"] --> IMP
    G06["MR-G06\nAI Task Context"] --> G07["MR-G07\nAI Output Record"]
    G07 -. "candidate only; requires source and Human disposition" .-> G04

    E07 -. "source capture is not active Rule" .-> G02
    G04 -. "change detection is not Rule adoption" .-> D12
    G05 -. "organization custom is not law" .-> G02
    REL -. "Pack release is not production or protected-action authority" .-> REV
```

## Accessibility Description

A change signal is captured as a Source Record and classified as a Rule Change Candidate. The Product analyzes affected rules, forms, fees, Quotes, packages, approvals and open journeys. An eligible professional makes a Decision, after which the Rule Record is updated and tested. The Rule enters a Jurisdiction Pack and immutable Pack Version, and an authorized professional owner grants Pack Release Approval. The released version then triggers journey revalidation, repricing, re-signature, suspension or a no-action decision. An Organization Overlay may inform impact analysis but cannot replace law. AI may produce a candidate only when tied to sources and Human disposition.

## Grayscale and Legibility Notes

- The primary workflow is vertical and numbered by controlled record IDs.
- Human Decisions use diamonds; candidate and released records use labelled rectangles.
- Overlay and AI inputs enter from the side with explicit boundary labels.
- The figure should render in portrait orientation and remain readable as a checklist-like process.

## Simplifications and Boundary

The figure does not define jurisdiction law or a universal source hierarchy for every legal question. Pack release may still leave a service Research Only, Suspended or otherwise limited. Neither a released Pack nor a passing scenario grants production deployment, provider appointment, Filing Approval or External Protected Action authority.