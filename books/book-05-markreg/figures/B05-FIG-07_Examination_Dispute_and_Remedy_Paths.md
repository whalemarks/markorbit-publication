# B05-FIG-07 — Examination, Dispute and Remedy Paths

## Control

- **Status:** Controlled Figure Source v1.0 — PF-07
- **Disposition:** retained
- **Format:** Mermaid flowchart
- **Primary sources:** CH30–CH36, B05-SPEC-0001 v0.3 and Appendix A
- **Intended placement:** CH30 or CH36

## Caption

**Figure 7. Official events can lead to examination, publication, adversarial or remedy paths that remain separately sourced and approved.** The figure shows Product records and Decisions around those paths; it does not predict or guarantee an official outcome.

## Controlled Source

```mermaid
flowchart TB
    E05(["MR-E05\nOfficial Event Snapshot"]) --> T{"Event type and verified scope"}

    T -->|"examination issue"| C03["MR-C03\nExamination Context"]
    C03 --> A19["MR-A19\nIssue Set"]
    A19 --> A20["MR-A20\nResponse Option Set"]
    A20 --> A21["MR-A21\nResponse Strategy"]
    A21 --> D06{"MR-D06\nResponse Strategy Decision"}
    D06 --> A22["MR-A22\nResponse Package Candidate"]
    A22 --> D03{"MR-D03\nFiling Approval where filing follows"}
    D03 --> RESP["governed response Execution and Evidence"]

    T -->|"publication or challenge window"| C04["MR-C04\nPublication Window Context"]
    C04 --> CH{"Verified challenge or no-challenge state"}
    CH -->|"challenge"| C05["MR-C05\nAdversarial Context"]
    C05 --> A23["MR-A23\nEvidence Plan"]
    A23 --> A24["MR-A24\nAdversarial Package Candidate"]
    A24 --> D07{"MR-D07\nAdversarial or Settlement Decision"}
    D07 --> ADV["governed filing, settlement or Communication path"]

    RESP --> V02["MR-V02\nOutcome Snapshot"]
    ADV --> V02
    CH -->|"verified no-challenge closure where supported"| V02

    V02 --> REM{"Remedy or continuation required?"}
    REM -->|"yes"| C06["MR-C06\nRemedy Context"]
    C06 --> NEXT["new strategy, package, approval and evidence cycle"]
    REM -->|"no or not yet"| CONT["continue sourced lifecycle monitoring"]

    E05 -. "official event is not professional interpretation" .-> T
    D07 -. "settlement Decision is not signed agreement or official closure" .-> ADV
```

## Accessibility Description

An Official Event Snapshot enters a decision point that identifies the verified event type and affected scope. An examination issue creates an Examination Context, Issue Set, Response Options, Response Strategy, Human Decision, Response Package and, where needed, Filing Approval and governed response filing. A publication event creates a Publication Window Context. A verified challenge creates an Adversarial Context, Evidence Plan, adversarial package and authorized dispute or settlement Decision. Each path produces a sourced Outcome Snapshot. A further branch determines whether a Remedy Context or continued lifecycle monitoring is required.

## Grayscale and Legibility Notes

- Examination and publication/dispute paths occupy separate branches with labelled event types.
- Decisions and branch points use diamonds; sourced official events use terminal shapes.
- The figure should render as a full-page portrait diagram.
- Path labels must remain visible when printed without color.

## Simplifications and Boundary

The figure does not enumerate every examination ground, opposition stage, appeal, review, cancellation, invalidation, restoration or settlement form. No path is automatic. A Product Outcome Snapshot remains sourced interpretation and does not create official closure, registration or remedy success.