# MO-PUB-REV-0001 — Books 01–04 Portfolio Baseline Review

## 1. Identity

```text
Review ID: MO-PUB-REV-0001
Scope: Books 01–04
Authority: MarkOrbit Orbital Architecture Canon vNext
Decision classes: PASS / EDITORIAL CORRECTION / CHANGE PROPOSAL REQUIRED
Purpose: Establish the pre-Product Portfolio Baseline for Book 05
Status: Completed — Owner Acceptance Pending
```

## 2. Review Question

> Do Books 01–04 form a coherent, bounded and sufficiently stable publication baseline for the dedicated MarkReg publication without reopening accepted architecture through informal wording?

## 3. Portfolio Responsibility Chain

```text
Book 01
→ Industry vision and Operating System principles

Book 02
→ Shared Core semantics, Objects, Services and contracts

Book 03
→ Governed Execution

Book 04
→ Workplace and Product Architecture
```

The chain is coherent.

Book 05 may now define MarkReg as a focused Product that consumes this baseline.

## 4. Decision Matrix

| Book | Decision | Required action | Result |
| --- | --- | --- | --- |
| Book 01 | EDITORIAL CORRECTION | Repair missing CH01, update publication map, align Organization/Workplace, Knowledge, AI and MGSN language, complete publication apparatus | Completed; RC1 |
| Book 02 | PASS | Keep frozen; record historical publication-label errata outside the manuscript | Frozen baseline preserved |
| Book 03 | EDITORIAL CORRECTION | Reconcile active Book 04 and Workplace wording; complete publication finishing | Completed; RC1 |
| Book 04 | PASS | Record owner acceptance through merged RC1 and lock as downstream architecture baseline | Completed; RC1 locked |

## 5. Book 01 Findings

### Critical Publication Defect

`manuscript/02_Chapter_01.md` contained a publication-structure fragment rather than Chapter 1.

This was a manuscript corruption, not an architecture decision.

It has been replaced by a complete chapter explaining why the industry needs shared operating infrastructure.

### Architecture Drift Corrected

- Organization remains the real actor.
- Workplace is its primary organizational operating environment.
- Ecosystem thinking broadens innovation without replacing organizations.
- Private Knowledge is not automatically shared.
- AI does not automatically learn from all Workplace activity.
- MGSN is private first and preserves Human Selection and relationship ownership.
- The publication map now reflects Books 01–07.

### Decision

```text
Book 01 conceptual continuity: PASS
Editorial correction: COMPLETED
Book 02 semantic amendment required: NO
Status: Release Candidate 1
```

## 6. Book 02 Findings

Book 02 remains the Frozen Core Specification Baseline v0.1.

Its manuscript contains historical publication references such as:

- `Book 03 — Workplace Framework`;
- `Book 04 — MarkReg`;
- earlier Book 05–06 numbering.

These are historical editorial labels.

The accepted interpretation is supplied by the repository Architecture Canon and current publication registry.

No Core Object, Service, Event, contract, status or authority conflict was found that requires a semantic change.

### Decision

```text
Frozen baseline integrity: PASS
Direct manuscript edit: NO
Editorial errata recorded at portfolio level: YES
Change Proposal required: NO
```

## 7. Book 03 Findings

The owner-accepted Execution architecture remains sound.

Active manuscript drift was limited to:

- historical `Book 04 Product System` labels;
- statements reducing Workplace to a Product surface;
- two active tenant references.

These were corrected without changing Execution meaning.

Portfolio-baseline publication finishing was completed with:

- status normalization;
- structural, terminology and targeted editorial review;
- terminology and source notes;
- glossary reconciliation;
- subject index;
- ten figures;
- cross-book review;
- RC1 validation.

### Decision

```text
Execution architecture: PASS
Editorial correction: COMPLETED
Workflow depth changed: NO
Protected-action boundary changed: NO
Book 02 Change Proposal required: NO
Status: Release Candidate 1
Final public-release copyedit: SEPARATE GATE
```

## 8. Book 04 Findings

Book 04 RC1 was owner approved and merged.

Its CH00–CH39 architecture, publication apparatus and cross-book reconciliation remain valid.

Book 04 is the downstream authority for Workplace and Product Architecture and the conformance source for Books 05–07.

### Decision

```text
Architecture: PASS
Publication finishing: PASS
Owner acceptance through merge: RECORDED
Status: Release Candidate 1 — Portfolio Baseline Locked
```

## 9. Cross-Book Locks

```text
Organization is the real actor.
Workplace is the organization-level operating environment of an independent Orbit.
Core defines shared meaning.
Execution governs coordinated work.
Products compose focused user journeys.
MGSN connects independent organizational Orbits.
Owning Services change and record formal business facts.
Humans remain professionally accountable.
AI assists under explicit governance.
```

```text
Information ≠ Knowledge
Candidate ≠ Canonical
Recommendation ≠ Decision
Approval ≠ Execution
Product Presentation ≠ Formal Truth
Routing Recommendation ≠ Appointment
```

## 10. Historical Errata Policy

Historical planning and review records may preserve earlier labels.

Active manuscripts and current status records use the present publication map.

Book 02 remains frozen.

A historical label does not authorize a semantic reinterpretation.

## 11. Book 05 Entry Gate

Book 05 may begin when this Portfolio Baseline is owner accepted.

Book 05 must demonstrate:

- Book 02 Core conformance;
- Book 03 Execution conformance;
- Book 04 Workplace and Product conformance;
- MarkReg independence from Workplace, MGSN and Owning Services;
- Human Review and protected-action boundaries;
- typed Handoffs and formal outcomes;
- no silent upstream redefinition.

## 12. Final Decision

```text
Books 01–04 structural continuity: PASS
Architecture responsibility chain: PASS
Necessary editorial corrections: COMPLETED
Book 02 semantic Change Proposal required: NO
Book 03 Execution change required: NO
Portfolio Baseline ready for owner acceptance: YES
Book 05 planning ready after merge: YES
Unrestricted implementation ready: NO
Production ready: NO
External protected action authorized: NO
```
