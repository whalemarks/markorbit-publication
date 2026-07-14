# B05-CH-24 — Professional Review and Filing Approval

**Status:** Part IV Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

CH23 creates a versioned Filing Package Candidate.

CH24 answers:

> Who must review which parts, what may the client confirm, who may approve filing, and what exact package version does that authority cover?

```text
Filing Package Candidate
→ Professional Review
→ Client Confirmation where required
→ Internal or policy approval
→ Filing Approval for one exact package version
```

Review, confirmation, approval, execution, submission, and official acknowledgement remain distinct under `MR-CR-02` through `MR-CR-04`.

---

## 1. User Question and Primary Action

**User question:** What still needs to be checked or approved before filing can proceed?

**Primary action:** Complete the review or confirmation assigned to the current actor, with the exact effect of that action displayed.

The Product must not present every participant with one generic `Approve` button.

---

## 2. Review Types

A package may require separate review of:

| Review type | Main subject |
| --- | --- |
| factual review | applicant, address, mark, priority and declared facts |
| professional review | route, scope, wording, claims, legal or procedural position |
| document review | POA, declaration, translation, certification and accepted use |
| commercial review | scope, fee-driving changes and approved terms |
| technical review | file formats, connector schema and payload integrity |
| provider review | local requirements and filing feasibility |
| deadline review | source, date, urgency and extension assumptions |
| conflict review | provider or professional eligibility |

One successful review does not imply that all dimensions have passed.

---

## 3. Client Confirmation

Client confirmation may cover:

- factual identity and address;
- ownership instruction;
- exact mark selected;
- commercial or business scope;
- priority facts;
- use facts;
- selected goods/services;
- authorized declarations;
- acceptance of disclosed residual risk.

The client does not become the professional reviewer merely by confirming facts.

---

## 4. Professional Review

Professional Review should record:

- reviewer identity and eligibility;
- package version reviewed;
- review scope;
- sources and jurisdiction-pack version;
- accepted items;
- changes required;
- blockers, warnings and assumptions;
- professional decision and reasons;
- expiry or re-review triggers.

AI may prepare the review record. It may not become the accountable reviewer.

---

## 5. Filing Approval

Filing Approval is the explicit decision `MR-D03` authorizing one Filing Package version to enter the permitted execution route.

It must identify:

- package ID and version;
- jurisdiction, route and filing unit;
- approving person and represented organization;
- authority basis;
- approved execution route or permitted alternatives;
- approval time;
- expiry or conditions;
- unresolved non-blocking warnings;
- whether official-fee payment is included in the authority;
- whether provider instruction or connector execution requires another gate.

A broad statement such as `file the trademark` is insufficient when several package versions or routes exist.

---

## 6. Approval Does Not Equal Submission

Filing Approval allows the next controlled execution step.

It does not prove that:

- a provider was appointed;
- a provider accepted instruction;
- a connector transmitted data;
- official fees were paid;
- the office received the application;
- an official filing number exists.

```text
Filing Approval ≠ submission ≠ acknowledgement
```

---

## 7. Separation of Duties

Organization policy may require different actors for:

- preparation;
- professional Review;
- client confirmation;
- commercial exception approval;
- Filing Approval;
- payment release;
- provider instruction;
- connector credential use.

The Product must enforce the configured separation instead of treating all users with workspace access as interchangeable.

---

## 8. Self-Review and Small Organizations

A small practice may allow one eligible professional to prepare, review, and approve.

Where this is permitted, the record should still show the separate decisions and timestamps.

The absence of multiple staff does not justify collapsing preparation, Review, and approval into one invisible state.

---

## 9. Conditional Approval

Conditional approval may state:

```text
Approved subject to deposit receipt
Approved subject to provider acceptance
Approved subject to original POA arrival
Approved subject to filing before stated deadline
Approved subject to no material change
```

A condition must identify:

- owner;
- evidence required;
- due point;
- blocking effect;
- verification method;
- expiry.

An unmet condition prevents the protected action it controls.

---

## 10. Approval Scope

Approval may be limited by:

- jurisdiction;
- filing unit;
- class or goods/services version;
- route;
- provider;
- connector;
- filing date or window;
- fee ceiling;
- declaration version;
- correction tolerance.

Authority must not spread automatically to related packages.

---

## 11. Change After Review or Approval

When a package changes, MarkReg classifies the change:

| Change class | Minimum response |
| --- | --- |
| presentation only | recorded comparison; approval may remain under policy |
| factual correction | renewed factual confirmation and targeted Review |
| professional-scope change | new Professional Review |
| commercial-scope change | Quote or acceptance revalidation |
| filing-material change | new Filing Approval |
| route or provider change | new execution and appointment checks |

The Product must identify exactly which decisions were invalidated.

---

## 12. Rejection, Return and Deferral

A reviewer or approver may:

- approve;
- approve with conditions;
- return for correction;
- reject;
- defer pending evidence;
- escalate;
- request specialist review.

The result should explain the next action and preserve the reviewed package version.

---

## 13. Professional Override

An authorized professional may override a Product warning only when:

- the warning is designated overridable;
- the reviewer is eligible;
- the reason is recorded;
- supporting source or professional basis is linked;
- affected scope is narrow;
- expiry and downstream effect are defined.

A Product blocker marked non-overridable cannot be bypassed through free text.

---

## 14. Approval Expiry

Approval may expire because:

- package version changed;
- jurisdiction pack changed materially;
- official fees changed beyond tolerance;
- deadline passed;
- provider availability or eligibility changed;
- Document expired;
- applicant or authority changed;
- confirmation condition remained unmet.

The Product should show why reapproval is required.

---

## 15. `EMBERLOOP` Reference Journey

For `EMBERLOOP`:

1. the client confirms the US word mark, applicant and goods wording;
2. the responsible professional reviews the declaration, filing basis, wording and current jurisdiction-pack rules;
3. the deposit receipt satisfies the commercial condition;
4. Filing Approval authorizes the exact US word-mark package version for the selected provider route;
5. the EU and UK packages receive separate approval decisions.

Approval of the US package does not authorize the device mark or the EU and UK filings.

---

## 16. Conformance Scenario — Package Changed After Approval

**Given** Filing Package v4 was approved.  
**When** the applicant address and one goods item are changed.  
**Then** MarkReg creates v5, shows the structured diff, invalidates affected confirmation and Filing Approval, and blocks execution until the required reviews are repeated.  
**Authority boundary:** the Product determines policy impact but does not itself grant renewed approval.  
**Evidence retained:** v4, v5, diff, invalidated decisions, new confirmations and approvals.

---

## 17. AI Assistance

AI may:

- prepare review checklists;
- compare package and source versions;
- identify unresolved items;
- summarize client-facing changes;
- detect missing authority evidence;
- draft approval records.

AI may not perform accountable Professional Review, confirm client facts, grant commercial exceptions, issue Filing Approval, or authorize external action.

---

## 18. Minimum Chapter Lock

```text
Review is scoped and attributable.
Client confirmation covers authorized facts.
Professional Review covers accountable judgment.

Filing Approval identifies one exact
package version, authority and route.

A material change invalidates the
specific decisions that depended on it.

Approval permits governed execution.
It does not prove submission or acknowledgement.
```

---

## 19. Handoff to CH25

An approved package may require a qualified external provider.

CH25 defines the Capability Need, private-first discovery, evidence, eligibility, conflict, availability, comparison and Human Selection recommendation used before any provider is appointed or instructed.