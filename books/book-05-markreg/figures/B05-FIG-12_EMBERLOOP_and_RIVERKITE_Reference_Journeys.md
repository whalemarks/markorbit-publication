# B05-FIG-12 — EMBERLOOP and RIVERKITE Reference Journeys

## Control

- **Status:** Controlled Figure Source v1.0 — PF-07
- **Disposition:** retained
- **Format:** Mermaid flowchart
- **Primary sources:** B05-SPEC-0002 v0.3 and Appendix D
- **Intended placement:** Appendix D

## Caption

**Figure 12. The two controlled reference journeys enter MarkReg from different lifecycle positions.** EMBERLOOP begins with a new international filing need; RIVERKITE begins with six existing registrations and portfolio obligations. Their jurisdictions and rights remain independent throughout the Product journey.

## Controlled Source

```mermaid
flowchart TB
    subgraph EL["B05-JRN-A-EMBERLOOP — EL-01–EL-40"]
        EL0["new business need"] --> EL1["jurisdiction, route, filing-unit, applicant, scope and risk recommendations"]
        EL1 --> EL2["Proposal, Quote, acceptance, Intake and Handoff"]
        EL2 --> EL3["Package, Review, Approval, provider routing, Execution and acknowledgement"]
        EL3 --> EL4["independent official paths"]
        EL4 --> UK["United Kingdom\nregistered; Right Baseline and maintenance active; renewal not yet open"]
        EL4 --> US["United States\nunder examination after acknowledged Response Package v2"]
        EL4 --> EU["European Union\nverified opposition; no closure assumed"]
        EL4 --> JA["Japan and Australia\nfuture-action candidates only"]
        UK --> EL5["Product Session, Pack governance, metrics and Conformance evidence"]
        US --> EL5
        EU --> EL5
        JA --> EL5
    end

    subgraph RK["B05-JRN-B-RIVERKITE — RK-01–RK-18"]
        RK0["six independent registration histories"] --> RK1["verify Right Baselines, owners, obligations, use Evidence and deadlines"]
        RK1 --> RK2["five renewal-related workflows"]
        RK2 --> R4["four ordinary renewals"]
        RK2 --> RO["one ownership-linked renewal"]
        RK1 --> CD["one cancellation-defense right"]
        RO --> CT["two-step chain-of-title correction"]
        R4 --> RK3["portfolio continuity and action planning"]
        CT --> RK3
        CD --> RK3
        RK1 --> UL["use-Evidence and licence actions remain open"]
        UL --> RK3
        RK3 --> RK4["Product Session, Pack governance, metrics and Conformance evidence"]
    end

    EL5 -. "new-filing path does not define portfolio history" .-> RK4
    RK4 -. "portfolio entry does not require replaying every new-filing step" .-> EL5
```

## Accessibility Description

The figure contains two vertical journey panels. EMBERLOOP starts with a new business need, moves through recommendation, commercial confirmation, Intake, filing preparation, governed action and acknowledgement, then separates into four jurisdiction outcomes: the United Kingdom is registered with maintenance active and renewal not yet open; the United States remains under examination after an acknowledged second response package; the European Union remains in verified opposition; Japan and Australia are future-action candidates only. RIVERKITE starts with six independent registrations, verifies baselines and obligations, then separates into four ordinary renewals, one ownership-linked renewal, one cancellation-defense right, a two-step chain-of-title correction and open use-evidence and licence actions. Both journeys later support Product Session, Pack governance, metrics and Conformance evidence.

## Grayscale and Legibility Notes

- Each journey is enclosed in a separately titled subgraph.
- Jurisdiction and right outcomes are written in full and do not depend on color.
- Render as a two-column landscape figure or as two consecutive portrait panels.
- No arrow should visually merge the independent UK, US, EU, Japan/Australia or six RIVERKITE right states.

## Simplifications and Boundary

The figure summarizes the controlled examples and omits many intermediate EL and RK steps. It does not represent real clients, current jurisdiction law or guaranteed outcomes. It does not invent filing, registration, settlement, renewal, recordal, cancellation or closure results beyond B05-SPEC-0002 v0.3.