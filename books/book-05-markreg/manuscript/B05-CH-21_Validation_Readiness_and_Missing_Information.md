# B05-CH-21 — Validation, Readiness and Missing Information

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

Part III now contains Proposal, Quote, Client Acceptance, Commercial Instruction, Formal Intake and Requirement Set versions. This chapter determines readiness for a named next action without hiding blockers behind one completion percentage.

The controlled output is `MR-A10 Readiness Assessment`. The `EMBERLOOP` reference step is `EL-14`.

```text
Readiness
≠ Professional Review
≠ Filing Approval
≠ Execution
```

## 1. Product Question

> What is ready, what remains blocked, who must act, and what becomes possible after resolution?

Readiness is always stated as:

```text
Ready for [specific action]
under [specific scope and versions]
subject to [named blockers, warnings and conditions]
```

## 2. Readiness Assessment Contract

A conforming assessment records:

- target action;
- service, jurisdiction and filing-unit scope;
- exact upstream versions;
- active Rule Records and Pack Versions;
- checks and results by dimension;
- blockers, warnings, conditions, recommendations and information;
- owner and resolution action for every unresolved item;
- Professional Review and override Decisions;
- checked time, expiry and revalidation triggers;
- next permitted action.

## 3. Readiness Dimensions

| Dimension | Typical evidence |
| --- | --- |
| commercial | valid Quote, accepted scope, instruction and commercial approvals |
| Intake | sufficient service-specific facts |
| identity and authority | applicant, instructor, payer and signatory context |
| professional | reviewed strategy, route, mark, classes, wording and risk |
| Document | accepted files, signatures, certification and originals |
| payment | deposit, advance, credit or reconciliation state |
| provider | capability, conflict, selection, appointment and acceptance state |
| deadline | sourced event, calculation, timezone and verification |
| approval | version-specific Human approval where required |
| Execution | valid formal references, Permissions and entry conditions |

A journey may be ready for Professional Review or payment request while not ready for Filing Approval or submission.

## 4. Result Types

```text
Blocker
→ the target action is prohibited

Warning
→ action may proceed with visible risk or acknowledgement

Condition
→ action depends on a later or external event

Recommendation
→ improvement is advised but not mandatory

Information
→ context without gate effect
```

Color alone must not convey the effect.

## 5. Purpose-Specific Gates

Examples include:

- ready for option selection;
- ready for Quote issuance;
- ready for Formal Intake;
- ready for Professional Review;
- ready for Document signature;
- ready for payment request;
- ready for Order or Matter creation;
- ready for Filing Package preparation;
- ready for Filing Approval;
- ready for provider appointment;
- ready for governed Execution.

`Complete` without a named purpose is not a valid state.

## 6. Missing-Item Contract

Every unresolved item states:

- what is missing, stale or conflicting;
- why it matters;
- accountable owner;
- due point;
- acceptable evidence;
- current gate effect;
- fallback or override route;
- escalation;
- affected records and action.

The Product should offer a direct resolution action instead of a generic error.

## 7. Override and Professional Review

An override records the original Rule, result, reviewer, authority, rationale, source, exact scope, residual risk and expiry.

`MR-SCN-09` permits only a reasoned, scoped and versioned Professional Override.

`MR-SCN-17` blocks Filing Approval when required Professional Review remains incomplete.

Some blockers are not overridable within MarkReg. AI cannot waive a Rule or create professional approval.

## 8. Payment and Commercial Separation

`MR-SCN-08` requires payment readiness to remain separate from professional and approval readiness.

```text
payment confirmed
≠ Filing Approval

Filing Approval active
≠ payment confirmed
```

A missing payment may block a named commercial or Execution gate while other dimensions remain ready.

## 9. Version, Expiry and Revalidation

Readiness becomes stale when a material input changes, including:

- accepted scope or Quote;
- applicant or signatory;
- mark version;
- goods/services;
- Documents;
- payment condition;
- provider status;
- deadline evidence;
- Pack Version or official fee.

The Product identifies the checks to rerun. It does not preserve an old green state.

## 10. Reference Journey — `EL-14`

`EMBERLOOP` Readiness Assessment v5 shows:

| Dimension | Result | Required action |
| --- | --- | --- |
| commercial | conditional | reconcile deposit |
| Intake | ready | none |
| Document | conditional | complete US declaration |
| professional | conditional | approve revised goods wording |
| payment | blocked | confirm and reconcile deposit |
| Filing Approval | not granted | review future Filing Package version |
| Execution | not ready | formal references and later gates required |

EU and UK preparation may continue while the US declaration remains open. The Product does not summarize this as `70% complete`.

## 11. User Surface

Show:

1. named target action;
2. result by dimension;
3. blockers before warnings;
4. owner and resolution action;
5. due date or urgency;
6. version and checked time;
7. expiry or change reason;
8. supporting Evidence and override history.

The primary action is resolve a blocker, provide Evidence, make or reconcile payment, request Review, accept a permitted risk or proceed to the next allowed gate.

## 12. AI Boundary

AI may compare versions, detect missing data, explain blockers, suggest resolution steps, summarize and route requests.

AI may not approve professional sufficiency, establish authority, reconcile payment as final, waive Rules, appoint a provider, grant Filing Approval or declare official acceptance.

## 13. Failure Modes

Reject:

```text
One percentage used for every action
Uploaded file treated as Document-ready
Paid treated as filing-ready
Recommended provider treated as appointed
Calculated deadline treated as verified
Warning and blocker mixed
Override without authority
Material change leaves readiness valid
Unknown result shown as ready
AI grants Filing Approval
```

## 14. Chapter Output and Handoff

CH21 produces `MR-A10 Readiness Assessment v5` with purpose-specific gates, owners, resolution actions and expiry conditions.

CH22 uses only permitted gate results to prepare `MR-A12 Handoff Envelope` for formal Order, Matter, payment, responsibility and Execution contexts.