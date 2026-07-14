# B05-CH-21 — Validation, Readiness and Missing Information

**Status:** Productized Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

Part III now contains Proposal, Quote, Acceptance, Commercial Instruction, Formal Intake and Requirement Set versions. This chapter determines readiness for a named next action without hiding critical blockers behind one completion percentage.

The controlling rule is `MR-CR-02`: Product readiness is not approval.

## 1. User Question

> Why are we not ready, what exactly is blocked, who must act, and what will become possible after the issue is resolved?

Readiness must always be expressed as:

```text
Ready for [specific action]
under [specific scope and versions]
subject to [named blockers, warnings and conditions]
```

## 2. Readiness Assessment Contract

A `Readiness Assessment` must identify:

- target action;
- service, jurisdiction and filing-unit scope;
- exact upstream artifact versions;
- rule and jurisdiction-pack versions;
- checks and results by dimension;
- blockers, warnings, conditions and recommendations;
- owner and resolution action for every unresolved item;
- professional decisions or overrides;
- checked time and expiry triggers;
- next permitted action.

## 3. Readiness Dimensions

| Dimension | Typical evidence |
| --- | --- |
| Commercial | valid Quote, accepted scope, instruction and approvals |
| Intake | sufficient service-specific facts |
| Identity and authority | applicant, instructor, payer and signatory context |
| Professional | reviewed strategy, route, mark, classes, wording and risk |
| Document | accepted files, signatures, certification and originals |
| Payment | required deposit, advance, credit or reconciliation state |
| Provider | capability, conflict, availability, selection and acceptance state |
| Deadline | sourced event, calculation, timezone, extension and verification |
| Approval | version-specific Human approval where required |
| Execution | valid formal references, permissions and entry conditions |

A journey may be ready for professional review and payment request while not ready for filing approval or submission.

## 4. Result Types

The Product must distinguish:

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

Useful gates include:

- ready for client option selection;
- ready for Quote issuance;
- ready for Formal Intake;
- ready for professional review;
- ready for document signature;
- ready for payment request;
- ready for Order or Matter creation;
- ready for filing-package preparation;
- ready for filing approval;
- ready for provider appointment;
- ready for governed execution.

“Complete” without a named purpose is not a valid gate.

## 6. Missing-Item Contract

Every unresolved item must state:

- what is missing or conflicting;
- why it matters;
- owner;
- deadline or required stage;
- acceptable evidence;
- current effect;
- fallback or override route;
- escalation;
- affected artifact and action.

The Product should offer a direct resolution action rather than a generic error message.

## 7. Overrides

An override must retain:

- rule and original result;
- reviewer identity and authority;
- reason and supporting source;
- exact affected scope and version;
- residual risk;
- expiry or revalidation condition.

Some blockers are not overridable within MarkReg. AI cannot waive a blocker or create professional approval.

## 8. Version, Expiry and Revalidation

Readiness expires or becomes stale when material inputs change, including:

- accepted scope or Quote;
- applicant or signatory;
- mark version;
- goods/services;
- documents;
- payment condition;
- provider availability;
- deadline evidence;
- jurisdiction-pack or official-fee version.

The Product identifies exactly which checks must rerun. It does not silently preserve a green status.

## 9. EMBERLOOP Reference Journey

The current Readiness Assessment shows:

| Dimension | Result | Required action |
| --- | --- | --- |
| Commercial | conditional | deposit receipt required |
| Intake | ready | none |
| Documents | conditional | complete US declaration |
| Professional | conditional | approve revised goods wording |
| Payment | blocked | reconcile deposit |
| Filing approval | not granted | approve the future Filing Package version |
| Execution | not ready | formal references and later gates required |

The client sees that EU and UK document preparation can progress while the US declaration remains open. The system does not label the whole journey simply “70% complete.”

## 10. Conformance Scenario — Missing Payment

**Given** Intake, documents and professional review are complete but the required deposit has not been received.  
**When** filing-package preparation readiness is evaluated.  
**Then** MarkReg shows professional and document readiness as ready while commercial/payment readiness remains blocked, and explains the exact payment condition.  
**Authority boundary:** payment state does not replace filing approval.  
**Evidence retained:** payment terms, financial-source state, readiness version and later reconciliation event.

## 11. Conformance Scenario — Professional Override

**Given** a jurisdiction rule warns that one goods item is unacceptable.  
**When** an authorized professional identifies a sourced local exception.  
**Then** MarkReg permits a reasoned override limited to that item, jurisdiction and version, and preserves the original warning.  
**Authority boundary:** only an authorized human may make the professional decision.  
**Evidence retained:** warning, source, reviewer, reason, scope, residual risk and expiry trigger.

## 12. User Surface

The readiness surface should show:

1. named target actions;
2. result by dimension;
3. blockers before warnings;
4. exact owner and next action;
5. due date or urgency;
6. version and checked time;
7. change or expiry reason;
8. accessible evidence and override history.

One primary action should be highlighted: resolve blocker, provide evidence, make payment, request review, accept risk or proceed to the permitted next gate.

## 13. AI Boundary

AI may compare versions, detect missing data, explain blockers, suggest resolution steps, generate summaries and route requests.

AI may not approve professional sufficiency, establish authority, reconcile payment as final, waive rules, appoint a provider, grant Filing Approval or declare official acceptance.

## 14. Failure Modes

The Product must reject:

```text
One percentage used for every action
Uploaded file treated as document-ready
Paid treated as filing-ready
Recommended provider treated as appointed
Calculated deadline treated as verified
Warning and blocker mixed
Override without authority
Material change leaves readiness valid
Unknown result shown as ready
AI grants filing approval
```

## 15. Chapter Output

The output is a versioned Readiness Assessment with purpose-specific gates, owners, resolution actions and expiry conditions.

The next chapter uses the permitted gate results to prepare idempotent, traceable requests for formal Order, Matter, payment, responsibility and Execution contexts.