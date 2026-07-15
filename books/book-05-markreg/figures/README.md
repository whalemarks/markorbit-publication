# Book 05 Controlled Figures

## Status

- **Workstream:** PF-07 — Figures and Publication Apparatus
- **Source format:** Mermaid embedded in controlled Markdown files
- **Retained figures:** 11
- **Merged figures:** 1
- **Rendered validation:** pending PF-08

## Disposition

| Planned ID | Disposition | Current source |
| --- | --- | --- |
| B05-FIG-01 | retained | `B05-FIG-01_MarkReg_Position_in_the_MarkOrbit_Architecture.md` |
| B05-FIG-02 | retained | `B05-FIG-02_Full-Lifecycle_Product_Journey.md` |
| B05-FIG-03 | retained and expanded | `B05-FIG-03_Need-to-Handoff_Artifact_and_Decision_Lineage.md` |
| B05-FIG-04 | retained | `B05-FIG-04_State_and_Authority_Layers.md` |
| B05-FIG-05 | merged into B05-FIG-03 | no separate source |
| B05-FIG-06 | retained | `B05-FIG-06_Filing_Package_to_Official_Acknowledgement.md` |
| B05-FIG-07 | retained | `B05-FIG-07_Examination_Dispute_and_Remedy_Paths.md` |
| B05-FIG-08 | retained | `B05-FIG-08_Registration_and_Portfolio_Continuity.md` |
| B05-FIG-09 | retained | `B05-FIG-09_Participant_Visibility_and_Action_Rights.md` |
| B05-FIG-10 | retained | `B05-FIG-10_Jurisdiction_Pack_and_Rule_Change_Workflow.md` |
| B05-FIG-11 | retained | `B05-FIG-11_MarkReg_MVP_Delivery_Sequence.md` |
| B05-FIG-12 | retained | `B05-FIG-12_EMBERLOOP_and_RIVERKITE_Reference_Journeys.md` |

B05-FIG-05 was merged because its Recommendation-to-Commercial-Instruction sequence duplicated the opening half of the artifact and Decision lineage. B05-FIG-03 now covers the full Need-to-Handoff path without creating two near-identical diagrams.

## Figure Contract

Every retained figure includes:

- a stable figure ID and title;
- controlled source chapters, specifications or appendices;
- intended placement;
- a reader caption;
- Mermaid source;
- a text accessibility description;
- grayscale and legibility notes;
- explicit simplifications and authority boundaries.

## Visual Grammar

The figures use text, grouping, shape and arrow labels rather than color alone.

| Visual form | Meaning |
| --- | --- |
| rounded or ordinary process node | Product-local artifact, context or activity |
| diamond | accountable Decision, gate, conflict or branch |
| cylinder or database node | formal shared record or stable source reference |
| stadium or terminal node | official evidence, official event or final bounded output |
| subgraph lane | Product, formal, Execution, provider, official or projection context |
| dashed or labelled return path | correction, reconciliation, Handoff or Return |

The actual renderer may apply color, but the meaning must remain legible when color is removed.

## Authority Rule

A figure is a reader projection. It may simplify layout but may not:

- redefine a controlled record;
- collapse Product, formal, Execution, provider and official states;
- turn a recommendation into a Decision;
- turn approval into Execution;
- turn submission or provider reporting into official acknowledgement;
- merge independent jurisdictions or rights;
- grant implementation, production or External Protected Action authority.

## Validation Boundary

PF-07 controls source content, caption, placement intent and accessibility text. PF-08 must still validate Mermaid parsing, target-format rendering, page fit, grayscale legibility, link behavior, selectable text and non-truncation.