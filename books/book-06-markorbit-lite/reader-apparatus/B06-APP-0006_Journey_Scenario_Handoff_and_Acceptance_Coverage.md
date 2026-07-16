# B06-APP-0006 — Journey, Scenario, Handoff and Acceptance Coverage

## Status and authority

```text
Record: B06-APP-0006
Type: Reader-facing coverage appendix
Status: Candidate — accepted on RC Hardening B owner merge
Primary authority: B06-SPEC-0002–0004
Creates new journeys, scenarios, contracts or criteria: NO
```

## 1. Reference journeys — `ML-J01–J04`

| ID | Journey | Primary chapters | Supporting chapters |
| --- | --- | --- | --- |
| ML-J01 | Existing Customer Portfolio Opportunity | CH12, CH15–CH16 | CH07–CH11, CH17–CH21, CH26, CH30 |
| ML-J02 | Historical Customer Reactivation | CH13, CH15–CH16 | CH07–CH11, CH20, CH28, CH30 |
| ML-J03 | Prospect Candidate Development | CH14–CH16 | CH09–CH11, CH20, CH27–CH28, CH30, CH32 |
| ML-J04 | Case-to-Work-Product | CH22–CH25 | CH17–CH21, CH28–CH31 |

### Journey integrity

Every journey must preserve:

- initiating source and authority;
- active Organization and subject scope;
- Product-local records;
- Human decisions and Review;
- destination Handoff and typed Return;
- safe stop, failure and unknown states;
- externally owned formal records;
- scoped feedback, correction and reuse.

## 2. Conformance scenarios — `ML-SCN-01–SCN-24`

### Customer and Service Growth

| ID | Scenario focus | Primary chapters | Severity |
| --- | --- | --- | --- |
| ML-SCN-01 | Valid portfolio maintenance/service gap | CH09, CH12, CH30 | STANDARD |
| ML-SCN-02 | Stale or conflicting source | CH08–CH10, CH12, CH30–CH31 | MAJOR |
| ML-SCN-03 | Missing Customer or Matter access | CH08, CH12, CH29–CH31 | BLOCKING |
| ML-SCN-04 | Accepted Candidate must remain Product-local | CH10, CH16, CH28, CH30–CH31 | BLOCKING |
| ML-SCN-05 | Customer response confirms real need | CH15–CH16, CH30 | STANDARD |
| ML-SCN-06 | Revenue conflicts with client interest/risk | CH10, CH12, CH30–CH32 | BLOCKING |

### Historical customer and prospect development

| ID | Scenario focus | Primary chapters | Severity |
| --- | --- | --- | --- |
| ML-SCN-07 | Historical contact is stale | CH13–CH15, CH31 | MAJOR |
| ML-SCN-08 | Historical customer opted out | CH13–CH15, CH31 | BLOCKING |
| ML-SCN-09 | Public source creates Prospect Candidate | CH14, CH30 | STANDARD |
| ML-SCN-10 | Contact exists but channel permission is unknown | CH13–CH15, CH20, CH31 | BLOCKING |
| ML-SCN-11 | Duplicate prospect across sources | CH14, CH31–CH32 | MAJOR |
| ML-SCN-12 | Platform prospect is invalid | CH14, CH31–CH32 | STANDARD |

### Professional work products

| ID | Scenario focus | Primary chapters | Severity |
| --- | --- | --- | --- |
| ML-SCN-13 | Raw AI text remains Content/draft | CH17–CH18, CH31 | BLOCKING |
| ML-SCN-14 | Render success remains separate from approval | CH19, CH31 | BLOCKING |
| ML-SCN-15 | Failed/mismatched Render remains incomplete | CH19, CH31–CH32 | MAJOR |
| ML-SCN-16 | Publish Package ready is not published | CH20, CH31 | BLOCKING |
| ML-SCN-17 | Post-Review edit creates new version | CH18–CH21, CH31 | MAJOR |
| ML-SCN-18 | Unknown publication result is preserved | CH20–CH21, CH28–CH31 | BLOCKING |

### Cases, memory and reusable capability

| ID | Scenario focus | Primary chapters | Severity |
| --- | --- | --- | --- |
| ML-SCN-19 | Restricted case facts excluded or blocked | CH22–CH25, CH31 | BLOCKING |
| ML-SCN-20 | Successful case does not become universal rule | CH22–CH25, CH31 | MAJOR |
| ML-SCN-21 | Repeated preference remains candidate until accepted | CH23, CH31 | STANDARD |
| ML-SCN-22 | Organization Memory requires Review and provenance | CH23–CH25, CH31 | BLOCKING |

### Handoff, local data and formal state

| ID | Scenario focus | Primary chapters | Severity |
| --- | --- | --- | --- |
| ML-SCN-23 | Destination revalidates Handoff and returns provenance | CH26–CH29, CH31 | BLOCKING |
| ML-SCN-24 | Local readability does not imply synchronization | CH08, CH23, CH25, CH29, CH31 | BLOCKING |

### Scenario totals

```text
STANDARD: 5
MAJOR: 5
BLOCKING: 14
Total: 24 / 24 covered
```

## 3. Handoff contracts — `ML-HC-01–HC-08`

| ID | Destination | Primary chapters | Required boundary |
| --- | --- | --- | --- |
| ML-HC-01 | MarkReg | CH16, CH26 | Launch/continuation request is not Product Session or Matter acceptance |
| ML-HC-02 | MGSN | CH27 | Capability Need is not provider appointment; disclosure is staged and minimized |
| ML-HC-03 | Human Review | CH18, CH28 | Exact-version Review is separate from user confirmation |
| ML-HC-04 | Communication Service | CH15, CH20, CH28 | Prepared/accepted send request is not necessarily sent or delivered |
| ML-HC-05 | Opportunity Service | CH16, CH28 | Qualification Result is not formal Opportunity until destination acceptance |
| ML-HC-06 | Task / Execution | CH11, CH28 | Attention/Prepared Action is not Task, Workflow or protected execution |
| ML-HC-07 | Delivery / Publish | CH20, CH28 | Package readiness is not delivery/publication; rights and evidence required |
| ML-HC-08 | Knowledge Governance | CH24, CH28 | Contribution Candidate is not accepted Knowledge |

### Contract totals

```text
Handoff contracts: 8 / 8 covered
Destination revalidation required: 8 / 8
Typed Return required: 8 / 8
Automatic authority transfer allowed: 0 / 8
```

## 4. MVP 0 acceptance criteria — `ML-AC-01–AC-12`

| ID | Criterion | Primary chapters | Acceptance meaning |
| --- | --- | --- | --- |
| ML-AC-01 | Authorized context | CH08, CH30 | Bounded Organization/customer/trademark scope is explicit |
| ML-AC-02 | Opportunity relevance | CH09–CH12, CH30 | At least one timely and explainable Service-Value Candidate |
| ML-AC-03 | Source quality | CH08–CH09, CH30 | Source, freshness, confidence and missing information visible |
| ML-AC-04 | Work-product value | CH17–CH21, CH30 | User uses or meaningfully edits a trustworthy work product |
| ML-AC-05 | User action | CH11, CH15, CH20, CH30 | Final user confirmation precedes consequential customer action |
| ML-AC-06 | Typed response | CH15, CH21, CH30 | Response, no response, rejection, correction and unknown remain distinct |
| ML-AC-07 | Qualification | CH10, CH15–CH16, CH30 | Real need distinguished from weak activity or generic interest |
| ML-AC-08 | Governed Handoff | CH16, CH26–CH28, CH30 | Destination accepts, rejects or requests information explicitly |
| ML-AC-09 | Return continuity | CH11, CH26–CH30 | Returned result retains origin and does not become shadow formal state |
| ML-AC-10 | Capability accumulation | CH21–CH25, CH30 | Scoped feedback, correction or reusable candidate is preserved |
| ML-AC-11 | Safety and privacy | CH29–CH31 | No BLOCKING violation; unsafe action is stopped |
| ML-AC-12 | Product/commercial evidence | CH30–CH32 | Recurring use, cost and plan evidence collected without redefining Product |

### Pass rule

```text
ML-AC-01–AC-11: mandatory
ML-AC-12: evidence required; threshold remains experiment-specific
content quantity alone: insufficient
prospect quantity alone: insufficient
blocking scenario violation: not allowed
```

## 5. Failure-state coverage

| State | Primary chapters |
| --- | --- |
| stale | CH08–CH10, CH19, CH25, CH29–CH31 |
| incomplete | CH17–CH20, CH26, CH29–CH31 |
| unsupported | CH19, CH26–CH29, CH31 |
| blocked_by_permission | CH08, CH28–CH31 |
| blocked_by_policy | CH11, CH20, CH28–CH31 |
| review_required | CH18–CH20, CH28–CH31 |
| rejected | CH10, CH16, CH26–CH31 |
| failed | CH19–CH21, CH26–CH32 |
| unknown_external_outcome | CH15, CH20–CH21, CH26–CH31 |
| expired | CH13–CH15, CH19–CH20, CH23–CH25, CH29 |
| suppressed | CH10, CH13–CH15, CH29 |
| retired | CH21–CH25, CH29–CH31 |

## 6. Coverage interpretation

Coverage demonstrates that the manuscript contains the accepted meaning and boundary. Conformance still requires observable Product behavior and negative tests.

```text
correct words in documentation
≠ conforming Product behavior
```

## Authority links

- [B06-SPEC-0002 — Reference Journeys and State Transitions](../specifications/B06-SPEC-0002_Reference_Journeys_and_State_Transitions.md)
- [B06-SPEC-0003 — Conformance Scenarios and Failure Paths](../specifications/B06-SPEC-0003_Conformance_Scenarios_and_Failure_Paths.md)
- [B06-SPEC-0004 — Handoff, Work-Product, MVP and Historical Reconciliation](../specifications/B06-SPEC-0004_Handoff_Work_Product_MVP_and_Historical_Reconciliation.md)
