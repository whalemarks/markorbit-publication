# B05-PUB-0005 — Figure Register

## Status

- **Status:** Controlled Figure Register v1.0 — PF-07 source complete
- **Primary workstream:** PF-07 — Figures and Publication Apparatus
- **Source directory:** `books/book-05-markreg/figures/`
- **Planned identities reviewed:** 12
- **Retained controlled sources:** 11
- **Merged dispositions:** 1
- **Rendered validation:** pending PF-08

## Purpose

The controlled figure set reduces repeated explanation and provides reusable architecture, lifecycle and reader-reference diagrams.

A figure may simplify layout. It may not simplify away authority, independent jurisdiction or right state, source, version, Human Decision, formalization or external-effect boundaries.

## Final Disposition

| Planned ID | Final title or disposition | Primary placement | Source status |
| --- | --- | --- | --- |
| [B05-FIG-01](../figures/B05-FIG-01_MarkReg_Position_in_the_MarkOrbit_Architecture.md) | MarkReg Position in the MarkOrbit Architecture | CH04; reuse CH43/CH47 | retained — controlled source v1.0 |
| [B05-FIG-02](../figures/B05-FIG-02_Full-Lifecycle_Product_Journey.md) | Full-Lifecycle Product Journey | CH07; Appendix A | retained — controlled source v1.0 |
| [B05-FIG-03](../figures/B05-FIG-03_Need-to-Handoff_Artifact_and_Decision_Lineage.md) | Need-to-Handoff Artifact and Decision Lineage | CH16 or CH22; Appendix A | retained and expanded — controlled source v1.0 |
| [B05-FIG-04](../figures/B05-FIG-04_State_and_Authority_Layers.md) | State and Authority Layers | CH07; Appendix B | retained — controlled source v1.0 |
| B05-FIG-05 | Recommendation to Commercial Instruction | merged into B05-FIG-03; no separate source | formally merged |
| [B05-FIG-06](../figures/B05-FIG-06_Filing_Package_to_Official_Acknowledgement.md) | Filing Package to Official Acknowledgement | CH28 or CH29 | retained — controlled source v1.0 |
| [B05-FIG-07](../figures/B05-FIG-07_Examination_Dispute_and_Remedy_Paths.md) | Examination, Dispute and Remedy Paths | CH30 or CH36 | retained — controlled source v1.0 |
| [B05-FIG-08](../figures/B05-FIG-08_Registration_and_Portfolio_Continuity.md) | Registration and Portfolio Continuity | CH37 or CH42 | retained — controlled source v1.0 |
| [B05-FIG-09](../figures/B05-FIG-09_Participant_Visibility_and_Action_Rights.md) | Participant Visibility and Action Rights | CH44; Appendix C | retained — controlled source v1.0 |
| [B05-FIG-10](../figures/B05-FIG-10_Jurisdiction_Pack_and_Rule_Change_Workflow.md) | Jurisdiction Pack and Rule Change Workflow | CH45; Appendix F | retained — controlled source v1.0 |
| [B05-FIG-11](../figures/B05-FIG-11_MarkReg_MVP_Delivery_Sequence.md) | MarkReg MVP Delivery Sequence | CH46 | retained — controlled source v1.0 |
| [B05-FIG-12](../figures/B05-FIG-12_EMBERLOOP_and_RIVERKITE_Reference_Journeys.md) | EMBERLOOP and RIVERKITE Reference Journeys | Appendix D | retained — controlled source v1.0 |

## Merge Decision — B05-FIG-05

The planned Recommendation-to-Commercial-Instruction figure duplicated the first half of the Artifact and Decision Lineage.

PF-07 therefore expanded B05-FIG-03 to cover:

```text
Business Context Snapshot
→ Need Brief
→ Recommendation Set
→ Option Set
→ Proposal
→ Quote
→ Client Acceptance
→ Commercial Instruction
→ Formal Intake
→ Requirement Set
→ Readiness Assessment
→ Handoff Envelope
```

Keeping a second diagram would add maintenance and reader-navigation cost without a distinct Product responsibility.

## Figure Contract

Every retained figure records:

- stable figure ID and title;
- controlled source chapters, specifications or appendices;
- intended placement;
- reader-facing caption;
- Mermaid source;
- accessibility description;
- grayscale and legibility notes;
- explicit simplifications and authority boundary.

## Visual Grammar

The source set uses text, grouping, shape and arrow labels instead of color alone.

| Visual form | Controlled reading |
| --- | --- |
| ordinary process node | Product-local artifact, context or activity |
| diamond | accountable Decision, gate, conflict or branch |
| database-shaped node | formal shared record or stable baseline |
| terminal node | official evidence, official event or bounded outcome |
| labelled subgraph | Product, formal, Execution, provider, official, lifecycle or journey lane |
| dotted or labelled return arrow | correction, conflict, reconciliation, Handoff, Return or constitutional distinction |

A renderer may apply color, but removing color must not remove meaning.

## Source-Level Accessibility Review

PF-07 review confirms that every retained figure:

- has a complete text alternative;
- names each material node and arrow consequence;
- avoids color-only distinctions;
- preserves a defined reading direction;
- identifies recommended portrait or landscape orientation;
- records narrow-layout or page-split constraints;
- states simplifications that could otherwise mislead a reader.

This is source-level accessibility and legibility evidence. PF-08 must still inspect actual Mermaid, Markdown and target publication rendering.

## Placement and Reuse Rule

A figure may be referenced from several chapters or appendices. The source file controls one caption and one diagram meaning.

Placement may change during layout without changing the figure ID. A changed figure meaning requires a new controlled version and impact review against its chapters, appendices, Glossary and Subject Index.

## Authority Locks

The retained figures preserve:

```text
Recommendation ≠ Decision
Readiness ≠ Approval
Approval ≠ Execution
Human Selection ≠ provider appointment or acceptance
Provider Report ≠ Official Truth
Submission ≠ official acknowledgement
Acknowledgement ≠ official outcome
Registration ≠ certificate availability
Renewal Approval ≠ renewed right
Signed transaction ≠ official owner update
Visibility ≠ action right
Pilot ≠ production
Publication or Conformance ≠ External Protected Action authority
```

B05-FIG-12 also preserves independent EMBERLOOP jurisdictions and independent RIVERKITE rights.

## PF-07 Completion State

```text
Twelve planned figures reviewed: COMPLETE
Eleven retained sources created: COMPLETE
One duplicate figure formally merged: COMPLETE
Captions and controlled source references: COMPLETE
Text accessibility descriptions: COMPLETE
Source-level grayscale and legibility review: COMPLETE
Rendered Mermaid validation: OPEN — PF-08
Target-format page fit and non-truncation: OPEN — PF-08
```

This register controls the PF-07 figure inventory. It does not make the rendered publication RC1.