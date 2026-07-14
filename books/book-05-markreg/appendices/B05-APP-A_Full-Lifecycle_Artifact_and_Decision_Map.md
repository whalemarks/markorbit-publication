# Appendix A — Full-Lifecycle Artifact and Decision Map

**Status:** Controlled Appendix Draft — PF-02 Reconciled; publication editing pending PF-06 and PF-07  
**Primary source:** B05-SPEC-0001 v0.2  
**Supporting chapters:** CH08–CH47  
**Reader purpose:** provide a compact, traceable map of the records and accountable decisions used across MarkReg.

## A.1 Authority and Reading Rule

This appendix is a reader projection of B05-SPEC-0001.

```text
Controlled specification
→ reviewed appendix projection
→ reader reference
```

If this appendix conflicts with B05-SPEC-0001, the specification controls until a reviewed update resolves the conflict.

The record classes are:

| Prefix | Meaning |
| --- | --- |
| `MR-A` | versioned Product artifact or work product |
| `MR-C` | scoped journey or proceeding context |
| `MR-D` | accountable Human or accepted external decision |
| `MR-E` | source-backed evidence or official-event record |
| `MR-B` | continuing baseline or obligation record |
| `MR-V` | derived view or projection |
| `MR-G` | governance, Pack, AI, metric, evaluation or conformance record |

```text
Artifact ≠ Decision
Decision ≠ Approval unless defined
Approval ≠ Execution
Evidence ≠ interpretation
Projection ≠ official truth
```

## A.2 New Filing Lineage

```text
MR-A01 Business Context Snapshot
→ MR-A02 Need Brief
→ MR-A03 Recommendation Set
→ MR-A04 Option Set
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

Not every filing journey reaches registration. An acknowledged application may continue into examination, publication, dispute, abandonment, refusal or another official outcome.

## A.3 Examination and Response Lineage

```text
MR-E05 Official Event Snapshot
→ MR-C03 Examination Context
→ MR-A19 Issue Set
→ MR-A20 Response Option Set
→ MR-A21 Response Strategy
→ MR-D06 Response Strategy Decision
→ MR-A22 Response Package Candidate
→ MR-D03 Filing Approval
→ MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E04 Official Acknowledgement Evidence
→ MR-V02 Outcome Snapshot
```

The same notice may contain several issues. Each issue retains its affected scope, source, response option and consequence.

## A.4 Publication, Opposition and Remedy Lineage

```text
MR-E05 Official Event Snapshot
→ MR-C04 Publication Window Context
→ MR-C05 Adversarial Context
→ MR-A23 Evidence Plan
→ MR-A24 Adversarial Package Candidate
→ MR-D07 Adversarial or Settlement Decision
→ MR-D03 Filing Approval where a protected filing follows
→ later MR-E05 Official Event Snapshots
→ MR-C06 Remedy Context where needed
→ MR-V02 Outcome Snapshot
```

Informal concern, threatened opposition, filed opposition, accepted proceeding, settlement and official closure remain separate.

## A.5 Registration and Maintenance Lineage

```text
MR-E08 Registration Outcome Record
→ MR-B01 Right Baseline
→ MR-B02 Maintenance Obligation Set
→ MR-B03 Use-Evidence Coverage Record
→ service-specific next actions
```

A certificate is evidence associated with a result. It is not automatically the current official record or a complete Maintenance Obligation Set.

## A.6 Renewal Lineage

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

Renewal preparation, approval, filing, acknowledgement and official renewal remain distinct.

## A.7 Recordal and Transaction Lineage

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

```text
Signed assignment or merger document
≠ recordal filed
≠ official owner updated
```

Licence context uses MR-C09 and does not become ownership merely because licensed use supports evidence.

## A.8 Portfolio and Cross-Product Lineage

```text
independent MR-B01 Right Baselines
+ MR-B02 Maintenance Obligation Sets
+ MR-B03 Use-Evidence Coverage Records
+ sourced lifecycle records
→ MR-V04 Portfolio Continuity View
→ MR-A29 Portfolio Action Plan
→ service-specific Decisions and Handoffs
```

For embedded and cross-Product use:

```text
MR-A12 Handoff Envelope
→ MR-C10 Product Session
→ governed MarkReg work
→ MR-A30 Return Envelope
```

The Return Envelope is idempotent and purpose-limited. It does not create a duplicate Order, Matter or official right.

## A.9 Compact Controlled Record Index

### Product artifacts

| Range | Records |
| --- | --- |
| MR-A01–A04 | Business Context, Need Brief, Recommendation Set and Option Set |
| MR-A05–A07 | Proposal, Quote and Commercial Instruction |
| MR-A08–A12 | Formal Intake, Requirement Set, Readiness, Filing Package and Handoff Envelope |
| MR-A13–A18 | Lifecycle Projection, routing, appointment, provider instruction, Execution request and recovery plan |
| MR-A19–A25 | Issue Set, response options and strategy, response/adversarial packages, Evidence Plan and Communication Packet |
| MR-A26–A30 | renewal, recordal, affected-right, portfolio action and Return records |

### Scoped contexts

| Range | Records |
| --- | --- |
| MR-C01–C02 | Capability Need and Reconciliation Context |
| MR-C03–C06 | Examination, Publication Window, Adversarial and Remedy Contexts |
| MR-C07–C09 | Recordal, Transaction and Licence Contexts |
| MR-C10–C11 | Product Session and Pilot Context |

### Evidence and source records

| Range | Records |
| --- | --- |
| MR-E01–E04 | submission, delivery, provider report and official acknowledgement evidence |
| MR-E05–E07 | Official Event Snapshot, Deadline Record and Source Record |
| MR-E08–E09 | Registration Outcome Record and Official Update Evidence |

### Baselines and views

| Range | Records |
| --- | --- |
| MR-B01–B04 | Right Baseline, Maintenance Obligations, Use-Evidence Coverage and Provider Capability Evidence |
| MR-V01–V05 | scope diff, outcome, chain-of-title, portfolio and participant projections |

### Governance records

| Range | Records |
| --- | --- |
| MR-G01–G05 | Jurisdiction Pack, rules, Pack version, change candidate and organization overlay |
| MR-G06–G07 | AI Task Context and AI Output Record |
| MR-G08–G10 | Metric Definition, Evaluation Record and Conformance Statement |

## A.10 Accountable Decision Index

| ID | Decision | Accountable actor | Exact scope | Does not equal |
| --- | --- | --- | --- | --- |
| MR-D01 | Client Acceptance | authorized client actor | exact Quote version and commercial scope | payment, changed scope or filing |
| MR-D02 | Professional Decision | eligible professional | recommendation, readiness, evidence, strategy or override | client authority or Execution |
| MR-D03 | Filing Approval | authorized Human role | exact package, purpose, route, jurisdiction and expiry | Execution or official effect |
| MR-D04 | Human Selection | authorized organization actor | provider or route choice | appointment or provider acceptance |
| MR-D05 | Provider Acceptance | appointed provider | accepted engagement and conditions | official submission |
| MR-D06 | Response Strategy Decision | professional plus client where needed | selected response, amendment and evidence | response filing approval |
| MR-D07 | Adversarial or Settlement Decision | authorized client and professional roles | proceeding, terms, authority and consequence | signed agreement, filing or official closure |
| MR-D08 | Renewal Approval | authorized owner/client and organization role | exact right, scope, package, fee and route | renewed right |
| MR-D09 | Recordal Approval | authorized owner/client and organization role | exact change, rights, documents and jurisdictions | official update |
| MR-D10 | Non-Renewal Decision | authorized owner/client | one right and understood consequence | official lapse before it occurs |
| MR-D11 | Communication Approval | authorized reviewer or sender | exact recipients, purpose, content and attachments | delivery or acknowledgment |
| MR-D12 | Pack Release Approval | accountable professional owner | exact Pack version and effective scope | official law or office rule |
| MR-D13 | Pilot or Release Decision | authorized Product/publication reviewer | profile, evidence, limits and stop conditions | production authority unless separately granted |

## A.11 Formalization Boundary

The following remain outside Product-local ownership:

- Core Organization, Client, Brand and Trademark objects;
- formal Order, Matter, Task, Workflow and responsibility records;
- formal Document, Evidence, Review, Approval, Communication and payment records;
- Book 03 Execution attempts, idempotency and Events;
- provider-system records;
- official office applications, registrations, proceedings and register entries.

```text
Product-local candidate
≠ formal shared object
≠ Execution state
≠ provider report
≠ official record
```

## A.12 Version and Change Rule

Every material controlled record retains stable ID, version, purpose, sources, responsible actor, Review, validity, supersession and downstream references.

A changed upstream fact does not silently mutate:

- an accepted Quote;
- an approved package;
- a formal Order or Matter;
- a provider instruction;
- an Execution attempt;
- an official record;
- a sent Communication.

## A.13 Publication Status

```text
PF-02 controlled-ID reconciliation: COMPLETE
Full-lifecycle lineage reconciliation: COMPLETE
Decision register reconciliation: COMPLETE
Formalization boundary reconciliation: COMPLETE
PF-03 reference-journey editing: STILL REQUIRED FOR APPENDIX D
PF-04 scenario and participant editing: STILL REQUIRED FOR APPENDICES C, E AND G
PF-05 Jurisdiction Pack editing: STILL REQUIRED FOR APPENDIX F
PF-06 native-English and compression edit: REQUIRED
PF-07 final figure and rendered layout integration: REQUIRED
```

Appendix A is now a controlled reader draft. It is not yet Release Candidate copy.
