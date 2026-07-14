# B05-CH-24 — Professional Review and Filing Approval

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

CH23 produced `MR-A11 Filing Package Candidate`.

CH24 defines who confirms facts, who performs accountable Professional Review and who grants `MR-D03 Filing Approval` for one exact package version.

```text
EL-17 / CH24
Filing Package Candidate
→ factual confirmation
→ MR-D02 Professional Decision
→ internal or policy approval where required
→ MR-D03 Filing Approval
```

Review, confirmation, approval, Execution, submission and official acknowledgement remain distinct.

## 1. Product Question and Primary Action

**Product question:** What still requires confirmation, Professional Review or approval before the package may enter governed Execution?

**Primary action:** Complete the task assigned to the current actor, with the exact effect displayed.

The Product must not give every participant one generic `Approve` button.

## 2. Review and Confirmation Types

| Activity | Main subject | Accountable actor |
| --- | --- | --- |
| factual confirmation | applicant, address, mark, priority, use and declared facts | authorized client or fact owner |
| Professional Review | route, scope, wording, claims, risk and procedural position | eligible professional |
| Document review | POA, declaration, translation, certification and accepted use | qualified reviewer |
| commercial review | changed scope, fees, exceptions and terms | authorized commercial actor |
| technical review | formats, schema, files and payload integrity | qualified technical actor |
| provider review | local feasibility and provider-specific requirements | eligible provider or professional |
| deadline review | source, calculation, urgency and extension assumptions | accountable professional or deadline owner |

One successful Review does not imply that all dimensions passed.

## 3. Client Confirmation

Client confirmation may cover:

- factual identity and address;
- ownership instruction;
- exact mark selected;
- business scope;
- priority and use facts;
- selected goods/services;
- authorized declarations;
- acceptance of disclosed residual risk.

Client confirmation does not turn the client into the professional reviewer.

## 4. Professional Decision

`MR-D02 Professional Decision` records:

- reviewer identity, qualification and represented organization;
- exact package version and Review scope;
- sources and Pack version;
- accepted items and required changes;
- blockers, warnings and assumptions;
- reasoned professional conclusion;
- expiry and revalidation triggers.

AI may prepare the record but cannot become the accountable reviewer.

## 5. Filing Approval Contract

`MR-D03 Filing Approval` authorizes one exact package version to enter a permitted Execution route.

It identifies:

- package ID and version;
- jurisdiction, route and filing unit;
- approving actor, organization and authority basis;
- permitted Execution route or bounded alternatives;
- approval time and expiry;
- conditions and non-blocking warnings;
- fee-payment authority, if included;
- whether provider instruction or connector invocation requires another gate.

A broad instruction such as `file the trademark` is insufficient when several packages, filing units or routes exist.

## 6. Approval Does Not Equal External Effect

```text
Filing Approval ≠ provider appointment
Filing Approval ≠ provider acceptance
Filing Approval ≠ connector transmission
Filing Approval ≠ official-fee acceptance
Filing Approval ≠ submission
Filing Approval ≠ official acknowledgement
```

Approval permits the next controlled step; it does not prove that step occurred.

## 7. Separation of Duties and Delegation

Organization policy may separate preparation, Professional Review, factual confirmation, Filing Approval, payment release, provider instruction and credential use.

A small practice may allow one eligible professional to perform several roles, but the separate Decisions and timestamps must remain visible.

Delegated authority must identify scope, duration, purpose and expiry. Delegation cannot create professional qualification or unlimited authority.

## 8. Conditional and Scoped Approval

Approval may be conditioned on:

- payment reconciliation;
- provider acceptance;
- original Document arrival;
- filing before a sourced deadline;
- no material change;
- final confirmation of a specified fact.

Approval may also be limited by jurisdiction, filing unit, class, wording version, route, provider, connector, fee ceiling, declaration version or time window.

An unmet condition blocks only the protected action it controls.

## 9. Change, Expiry and Reapproval

A package change is classified as:

| Change class | Minimum response |
| --- | --- |
| presentation only | recorded comparison; approval may remain under policy |
| factual correction | renewed factual confirmation and targeted Review |
| professional-scope change | new Professional Review |
| commercial-scope change | Quote or acceptance revalidation |
| filing-material change | new Filing Approval |
| route or provider change | renewed routing and appointment checks |

Approval may also expire because a Pack, fee, deadline, provider, Document, applicant or authority changed.

The Product must identify exactly which Decision became stale.

## 10. Outcomes of Review

A reviewer or approver may:

- approve;
- approve with conditions;
- return for correction;
- reject;
- defer pending evidence;
- escalate;
- request specialist Review.

The reviewed version and reason remain retained.

## 11. `EMBERLOOP` — `EL-17`

The client confirms the US word mark, applicant and goods wording. The responsible professional reviews the declaration, filing basis, wording and current US Pack. Deposit receipt satisfies the commercial condition.

A separate Filing Approval is recorded for each US, EU and UK package. Approval of the US word-mark package does not authorize the device mark or another jurisdiction.

## 12. Controlled Scenarios

### `MR-SCN-16` — Package changed after approval

A material change creates a new package version, shows the diff and invalidates affected confirmation, Professional Review and Filing Approval.

### `MR-SCN-17` — Incomplete Professional Review

Filing Approval is blocked while required issues, evidence or source checks remain unresolved, unless a defined conditional path is valid.

### `MR-SCN-18` — Delegated approval expires

An actor attempting approval outside delegated scope or time is blocked and routed to an eligible approver.

## 13. AI Assistance

AI may prepare checklists, compare versions, identify unresolved items, summarize changes and draft Decision records.

AI may not perform accountable Professional Review, confirm client facts, grant commercial exceptions, issue Filing Approval or authorize external action.

## 14. Chapter Lock

```text
Factual confirmation covers authorized facts.
Professional Review covers accountable judgment.
Filing Approval covers one exact package and route.
Material change invalidates dependent Decisions.
Approval permits Execution; it does not prove submission.
```

## 15. Handoff to CH25

CH24 produces reviewed packages and exact-version Filing Approvals.

CH25 defines `MR-C01 Capability Need`, `MR-A14 Routing Recommendation` and `MR-D04 Human Selection` before any provider is appointed or instructed.
