# B05-FIG-08 — Registration and Portfolio Continuity

## Control

- **Status:** Controlled Figure Source v1.0 — PF-07
- **Disposition:** retained
- **Format:** Mermaid flowchart
- **Primary sources:** CH37–CH42, B05-SPEC-0001 v0.3 and Appendix A
- **Intended placement:** CH37 or CH42

## Caption

**Figure 8. Registration begins a continuing rights-management cycle rather than ending the Product journey.** Each right retains its own official record, obligations, renewal, ownership and dispute state before being projected into a portfolio view.

## Controlled Source

```mermaid
flowchart TB
    E08(["MR-E08\nRegistration Outcome Record"]) --> V01["MR-V01\nFiling and Scope Diff View"]
    V01 --> B01[("MR-B01\nRight Baseline")]
    B01 --> B02["MR-B02\nMaintenance Obligation Set"]
    B01 --> B03["MR-B03\nUse-Evidence Coverage Record"]

    B02 --> RN{"Lifecycle action required"}

    RN -->|"renewal"| A26["MR-A26\nRenewal Package Candidate"]
    A26 --> D08{"MR-D08\nRenewal Approval"}
    D08 --> RE["governed renewal Execution and Evidence"]
    RE --> E09(["MR-E09\nOfficial Update Evidence"])
    E09 --> B01

    RN -->|"official-record change"| C07["MR-C07\nRecordal Context"]
    C07 --> A27["MR-A27\nRecordal Package Candidate"]
    A27 --> D09{"MR-D09\nRecordal Approval"}
    D09 --> E09

    RN -->|"assignment, merger or licence"| C08["MR-C08\nTransaction Context"]
    C08 --> C09["MR-C09\nLicence Context where applicable"]
    C08 --> A28["MR-A28\nAffected-Right Set"]
    A28 --> V03["MR-V03\nChain-of-Title View"]
    V03 --> C07

    B01 --> AGG["independent Right Baselines"]
    B02 --> AGG
    B03 --> AGG
    AGG --> V04["MR-V04\nPortfolio Continuity View"]
    V04 --> A29["MR-A29\nPortfolio Action Plan"]

    C08 -. "signed transaction is not official owner update" .-> E09
    D08 -. "Renewal Approval is not a renewed right" .-> E09
    V04 -. "portfolio aggregation does not create one global legal state" .-> A29
```

## Accessibility Description

A verified Registration Outcome Record is compared with the filing scope and used to establish a Right Baseline. The baseline supports a Maintenance Obligation Set and a Use-Evidence Coverage Record. When action is required, the journey may branch into renewal, official recordal or a transaction such as assignment, merger or licensing. Each action has its own candidate package, Human approval, governed Execution and Official Update Evidence before the baseline changes. Independent baselines and obligations may then be summarized in a Portfolio Continuity View and prioritized through a Portfolio Action Plan.

## Grayscale and Legibility Notes

- The Right Baseline is shown as a stable record node and remains visually central.
- Renewal, recordal and transaction paths use distinct labelled branches.
- Human approvals use diamonds; official update evidence uses a terminal shape.
- For print, render in portrait orientation with the portfolio aggregation at the bottom.

## Simplifications and Boundary

The figure does not imply that every registered right has the same maintenance, use, renewal or recordal duties. It does not merge independent rights or jurisdictions. Contractual effect, official recordal and current official ownership remain separate states.