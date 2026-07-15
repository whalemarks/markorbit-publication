# Appendix A — Full-Lifecycle Artifact and Decision Map

**Status:** Controlled Reader Draft v0.3 — PF-06D Reconciled  
**Primary source:** B05-SPEC-0001 v0.3  
**Supporting chapters:** CH08–CH47  
**Reader purpose:** provide a compact map of MarkReg Product records and accountable Decisions.

## A.1 Reading Rule

```text
Controlled Specification
→ reviewed Appendix projection
→ reader reference
```

B05-SPEC-0001 controls if a conflict exists.

| Prefix | Meaning |
| --- | --- |
| `MR-A` | Product Artifact |
| `MR-C` | scoped Context |
| `MR-D` | accountable Decision |
| `MR-E` | Evidence or source-backed record |
| `MR-B` | Baseline or obligation record |
| `MR-V` | View or Projection |
| `MR-G` | Governance and configuration record |

```text
Artifact ≠ Decision
Decision ≠ Approval unless defined
Approval ≠ Execution
Evidence ≠ interpretation
Projection ≠ Official Truth
```

## A.2 New Filing Lineage

```text
MR-A01 Business Context Snapshot
→ MR-A02 Need Brief
→ MR-A03 Recommendation Set
→ MR-A04 Option Set
→ MR-C12 Applicant and Authority Context where material
→ MR-A05 Proposal
→ MR-A06 Quote
→ MR-D01 Client Acceptance
→ MR-A07 Commercial Instruction
→ MR-A08 Formal Intake
→ MR-A09 Requirement Set
→ MR-A10 Readiness Assessment
→ MR-A12 Handoff Envelope
→ MR-A11 Filing Package Candidate
→ MR-D02 Professional Decision
→ MR-D03 Filing Approval
→ MR-A16 Provider Instruction or MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E04 Official Acknowledgement Evidence
→ MR-E05 Official Event Snapshot
→ MR-B01 Right Baseline or another sourced outcome
```

An acknowledged application may continue into examination, publication, dispute, abandonment, refusal, registration or another sourced outcome.

## A.3 Examination, Publication and Dispute

```text
MR-E05 Official Event Snapshot
→ MR-C03 Examination Context
→ MR-A19 Issue Set
→ MR-A20 Response Option Set
→ MR-D06 Response Strategy Decision
→ MR-A21 Response Strategy
→ MR-A22 Response Package Candidate
→ MR-D03 Filing Approval
→ MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E04 Official Acknowledgement Evidence
→ MR-V02 Outcome Snapshot
```

```text
MR-E05 Official Event Snapshot
→ MR-C04 Publication Window Context
→ MR-C05 Adversarial Context
→ MR-A23 Evidence Plan
→ MR-A24 Adversarial Package Candidate
→ MR-D07 Adversarial or Settlement Decision
→ MR-D03 Filing Approval where needed
→ MR-C06 Remedy Context where activated
→ MR-V02 Outcome Snapshot
```

Informal concern, formal challenge, Decision, filing, settlement instrument and official closure remain separate.

## A.4 Registration and Maintenance

```text
MR-E08 Registration Outcome Record
→ MR-V01 Filing and Scope Diff View
→ MR-B01 Right Baseline
→ MR-B02 Maintenance Obligation Set
→ MR-B03 Use-Evidence Coverage Record
→ service-specific next actions
```

A certificate is Evidence associated with an outcome. It is not automatically the current official register or a complete obligation set.

## A.5 Renewal

```text
MR-B01 Right Baseline
→ MR-B02 Maintenance Obligation Set
→ MR-A10 Readiness Assessment
→ MR-A26 Renewal Package Candidate
→ MR-D08 Renewal Approval
→ MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E04 Official Acknowledgement Evidence
→ MR-E09 Official Update Evidence
→ updated MR-B01 Right Baseline
```

## A.6 Recordal, Transaction and Licence

```text
MR-B01 Right Baseline
→ MR-C07 Recordal Context or MR-C08 Transaction Context
→ MR-A28 Affected-Right Set
→ MR-V03 Chain-of-Title View
→ MR-A27 Recordal Package Candidate
→ MR-D09 Recordal Approval
→ MR-A17 Execution Request
→ MR-E09 Official Update Evidence
→ updated MR-B01 Right Baseline
```

`MR-C09 Licence Context` remains distinct from ownership and assignment.

```text
Signed transaction
≠ recordal filed
≠ official owner updated
```

## A.7 Portfolio and Cross-Product

```text
independent MR-B01 Right Baselines
+ MR-B02 Maintenance Obligation Sets
+ MR-B03 Use-Evidence Coverage Records
+ sourced lifecycle records
→ MR-V04 Portfolio Continuity View
→ MR-A29 Portfolio Action Plan
→ service-specific Decisions and Handoffs
```

```text
MR-A12 Handoff Envelope
→ MR-C10 Product Session
→ governed MarkReg work
→ MR-A30 Return Envelope
```

Return is idempotent and purpose-limited. It does not create duplicate formal objects or external effects.

## A.8 Compact Record Index

### Product Artifacts

| Range | Records |
| --- | --- |
| MR-A01–A04 | Business Context, Need, Recommendation and Options |
| MR-A05–A07 | Proposal, Quote and Commercial Instruction |
| MR-A08–A12 | Intake, Requirements, Readiness, Filing Package and Handoff |
| MR-A13–A18 | Lifecycle Projection, routing, appointment, provider instruction, Execution request and recovery |
| MR-A19–A25 | Issues, response options/strategy, response/adversarial Packages, Evidence Plan and Communication |
| MR-A26–A30 | renewal, recordal, affected rights, Portfolio Action and Return |

### Scoped Contexts

| Range | Records |
| --- | --- |
| MR-C01–C02 | Capability Need and Reconciliation Context |
| MR-C03–C06 | Examination, Publication Window, Adversarial and Remedy Contexts |
| MR-C07–C09 | Recordal, Transaction and Licence Contexts |
| MR-C10–C11 | Product Session and Pilot Context |
| MR-C12 | Applicant and Authority Context |

`MR-C01` is Capability Need. Applicant and authority meaning belongs only to `MR-C12`.

### Evidence, Baselines and Views

| Range | Records |
| --- | --- |
| MR-E01–E04 | submission, delivery, Provider Report and official acknowledgement |
| MR-E05–E07 | Official Event, Deadline and Source Records |
| MR-E08–E09 | Registration Outcome and Official Update Evidence |
| MR-B01–B04 | Right, maintenance, use-Evidence and provider-capability Baselines |
| MR-V01–V05 | scope diff, outcome, chain of title, portfolio and participant projections |

### Governance Records

| Range | Records |
| --- | --- |
| MR-G01–G05 | Jurisdiction Pack, Rule, Pack Version, change candidate and Organization Overlay |
| MR-G06–G07 | AI Task Context and AI Output Record |
| MR-G08–G10 | Metric Definition, Evaluation Record and Conformance Statement |

## A.9 Decision Index

| ID | Decision | Does not equal |
| --- | --- | --- |
| MR-D01 | Client Acceptance | payment, changed scope or filing |
| MR-D02 | Professional Decision | client authority or Execution |
| MR-D03 | Filing Approval | Execution or official effect |
| MR-D04 | Human Selection | appointment or acceptance |
| MR-D05 | Provider Acceptance | official submission |
| MR-D06 | Response Strategy Decision | Response Filing Approval |
| MR-D07 | Adversarial or Settlement Decision | signed instrument, filing or official closure |
| MR-D08 | Renewal Approval | filed renewal or renewed right |
| MR-D09 | Recordal Approval | official update |
| MR-D10 | Non-Renewal Decision | official lapse before it occurs |
| MR-D11 | Communication Approval | delivery or acknowledgement |
| MR-D12 | Pack Release Approval | legal enactment or official publication |
| MR-D13 | Pilot or Release Decision | production or External Protected Action authority |

## A.10 Formalization Boundary

MarkReg does not own Core Objects; formal Order, Matter, Task, Workflow, Document, Evidence, Review, Approval, Communication or financial records; Book 03 Execution records; provider-system records; or official office records.

```text
Product-local candidate
≠ formal shared object
≠ Execution state
≠ provider report
≠ official record
```

## A.11 PF-06D Reconciliation State

```text
B05-SPEC-0001 v0.3 projection: COMPLETE
MR-C12 registration: COMPLETE
Record ranges and lineages: COMPLETE
Decision index: COMPLETE
Formalization boundary: COMPLETE
Native-English and terminology edit: COMPLETE
Figures and layout: OPEN — PF-07/PF-08
```

Appendix A remains a controlled reader draft until figures and rendered validation pass. It does not authorize implementation, production deployment or External Protected Action.
