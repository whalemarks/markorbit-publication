# B05-CH-45 — Jurisdiction Packs, AI Assistance and Rule Versioning

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part VII — Product Experience and Evolution

## Chapter Purpose

Jurisdiction intelligence is a governed dependency, not hidden Product code or model memory.

```text
MR-E07 Source Record
→ MR-G02 Rule Record
→ MR-G01 Jurisdiction Pack
→ MR-G03 Pack Version Record
→ Product behavior and Human Review
→ MR-G04 Rule Change Candidate
→ MR-D12 Pack Release Approval
```

`EL-38` applies this chain to rule-sensitive Product behavior and bounds AI assistance through `MR-G06` and `MR-G07`.

## 1. User Question and Primary Action

**User question:** Which source and Pack version support this behavior, and what must be verified before action?

**Primary action:** Use an active permitted Pack version, or escalate the rule for professional verification.

Every rule-sensitive surface identifies jurisdiction, authority, service module, lifecycle stage, source, checked date, effective date where known, Pack version, support state, professional owner and affected artifact.

## 2. MR-G01 Jurisdiction Pack

A Jurisdiction Pack controls a defined jurisdiction, office, service module, lifecycle stage and time period. It may govern:

- filing route and applicant eligibility;
- classification and goods/services conditions;
- Documents, signatures and representative requirements;
- official fee and quantity rules;
- examination, publication and dispute stages;
- registration, maintenance and renewal obligations;
- recordal and transaction requirements;
- Product questions, warnings and blockers;
- provider and Execution prerequisites.

One country name does not imply support for every service or lifecycle stage.

## 3. Pack Support States

A support claim uses one of the controlled states:

```text
Research Only
Guidance Capable
Preparation Capable
Execution Capable
Lifecycle Capable
Suspended
Retired
```

A Product or Conformance claim cannot exceed the relevant Pack module state.

Research or Guidance support does not authorize preparation, filing, monitoring or ongoing lifecycle operation.

## 4. MR-E07 Source Record and Source Hierarchy

Each material source retains authority or author, jurisdiction, language, publication and effective dates, retrieval time, immutable copy or checksum where permitted, supersession state, access restrictions and reviewer notes.

A URL alone is not provenance.

The source hierarchy generally prioritizes current official legislation, office rules, fee schedules, forms, notices, guidance and authenticated system behavior. Verified professional advice and organization experience may supplement gaps but remain identified and scoped.

Provider advice is valuable practice evidence. It is not official truth merely because the provider is local.

## 5. MR-G02 Rule Record

A Rule Record contains:

- human-readable rule and machine-readable condition;
- jurisdiction, service and lifecycle scope;
- source links and exceptions;
- effective date and review trigger;
- confidence and verification state;
- professional owner;
- affected Product behavior;
- test scenarios and change history.

Rule states may include draft, under verification, active, active with limitation, disputed, suspended, superseded, withdrawn or unknown after change.

Only a permitted state may drive protected Product behavior.

## 6. MR-G03 Pack Version Record

A Pack version is a coherent reviewed set of sources, Rules, forms, fees and migration instructions.

It records prior version, release and effective dates, included Rules, known gaps, approval, affected journeys and revalidation requirements.

A new Pack version does not rewrite historical Decisions. It may affect:

- new work;
- open unapproved work;
- approved but unexecuted work;
- future maintenance obligations;
- client Communication;
- already completed work only through a new sourced event, correction or explicit historical note.

## 7. MR-G04 Rule Change Candidate

Detection is not adoption.

```text
change signal
→ source capture
→ MR-G04 Rule Change Candidate
→ impact assessment
→ professional verification
→ Rule and Pack candidate
→ scenarios and tests
→ MR-D12 Pack Release Approval
→ affected-journey revalidation
```

A change may come from official publication, fee or form comparison, connector validation, professional observation, provider notice, controlled crawling or a user-reported discrepancy.

The Candidate preserves old and new evidence, effective-date uncertainty, affected artifacts, urgent temporary controls and required Communications.

## 8. Fee, Form and Deadline Changes

A fee change requires review of Quote validity, accepted but unexecuted instructions, provider payables, payment sufficiency, variance clauses and later-stage charges.

A form or schema change requires review of fields, declarations, signature, attachments, connector behavior and approved but unexecuted packages.

A deadline-rule change requires the original basis, new basis, earliest credible internal target and professional verification to remain visible.

No change silently mutates an accepted Quote, approved Package or historical record.

## 9. MR-G05 Organization Overlay

An organization may configure review levels, private providers, commercial policy, internal deadline buffers, templates, risk tolerance and Communication controls.

The overlay remains distinguishable from:

- official Rule;
- professional interpretation;
- Product default;
- provider requirement;
- client instruction.

Where an overlay conflicts with an active Pack Rule, the authoritative Rule controls the protected action and the conflict is escalated.

## 10. MR-G06 AI Task Context

Every material AI task is purpose-limited and identifies:

- actor and role;
- jurisdiction, service and lifecycle stage;
- Pack and Rule versions;
- permitted source set and organization overlay;
- relevant artifact versions;
- confidentiality limits;
- expected output class;
- prohibited conclusions.

The model must not rely on unstated memory for current jurisdiction Rules.

Without an active source set, AI may create a research or verification request, not a current legal conclusion.

## 11. MR-G07 AI Output Record

A material output records task purpose, model and system version, input references, Pack and Rule versions, generation time, uncertainty, citations or source mapping, Human disposition and affected artifacts.

The output is classified as an extraction, comparison, explanation draft, recommendation candidate, Rule-change candidate or evaluation candidate.

The Product need not expose hidden model reasoning. It must expose enough source and version basis for accountable Review.

AI may assist extraction, comparison, gap detection, explanation, drafting and prioritization. It may not approve a Pack, decide legal ownership, create professional authority, authorize protected action or claim official effect.

## 12. Controlled Scenarios

- `MR-SCN-07` — an official-fee change triggers controlled commercial impact rather than silent repricing;
- `MR-SCN-09` — only an eligible professional may approve a sourced exception;
- `MR-SCN-36` — an AI request without a valid Pack or source set produces verification work, not current-law advice;
- `MR-SCN-37` — an organization overlay cannot override an active authoritative Rule.

## 13. Reference Journeys

For `EMBERLOOP`, a later UK maintenance Pack changes an internal Evidence reminder but not the official renewal deadline. Historical filing and registration versions remain unchanged.

In the EU opposition, provider advice conflicts with a newer official notice. The Rule becomes disputed; deadline automation is blocked and the earliest credible internal target remains visible until professional verification.

For `RIVERKITE`, a fee-table change affects each open renewal Package according to its jurisdiction, stage, Quote and approval state. Historical completed actions are not repriced.

## 14. Minimum Pack and AI Lock

```text
Model memory ≠ current law.
Provider advice ≠ official truth.
Organization custom ≠ law.
Change detection ≠ Rule adoption.
Pack release ≠ legal enactment.
New Rule ≠ rewritten history.
AI output ≠ Human Review or Decision.
Support claim ≠ Execution authority.
```

## 15. Handoff to Metrics and Delivery

CH46 defines how `MR-G08 Metric Definition`, `MR-G09 Evaluation Record`, `MR-C11 Pilot Context` and `MR-D13 Pilot or Release Decision` test whether these Product controls work safely in a bounded MVP or pilot.
