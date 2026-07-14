# B05-CH-26 — Provider Appointment, Instruction and Acceptance

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

CH25 ended with `MR-D04 Human Selection`.

CH26 defines how that selection becomes a bounded relationship and accepted engagement:

```text
EL-19 / CH26
MR-D04 Human Selection
→ MR-A15 Provider Appointment Candidate
→ authorized appointment
→ MR-A16 Provider Instruction
→ receipt
→ MR-D05 Provider Acceptance or rejection
```

Selection, appointment, instruction, receipt and acceptance remain distinct. Provider Acceptance is not submission or official acknowledgement.

## 1. Product Question and Primary Action

**Product question:** Has the selected provider been properly appointed and accepted the exact work?

**Primary action:** Authorize the appointment or instruction assigned to the current actor, or resolve the provider response.

Any `Send to provider` action must show scope, authority, disclosed information and expected return evidence.

## 2. Appointment Candidate

`MR-A15 Provider Appointment Candidate` may contain:

- provider identity and organization;
- instructing organization and applicant or right holder;
- Matter and package references;
- jurisdiction, role and service scope;
- authority requested;
- POA or appointment Document;
- commercial or engagement reference;
- confidentiality and data-use terms;
- conflict and eligibility evidence;
- effective period;
- revocation and substitution rules.

The appointment candidate is separate from the Filing Package Candidate.

## 3. Appointment and Disclosure Authority

The Product must identify who may appoint counsel, filing agents, translators, document vendors, couriers or filing-capable services.

Before sensitive information is disclosed, verify:

- provider identity;
- active conflict and eligibility state;
- purpose and minimum necessary scope;
- appointment or confidentiality basis;
- approved package version;
- secure route;
- Document and original-handling authority;
- responsible sender.

A commercial user who selected a provider may not have authority to appoint it for the applicant.

## 4. Provider Instruction Contract

`MR-A16 Provider Instruction` identifies:

| Area | Required content |
| --- | --- |
| identity | instruction ID, version, Matter, sender and provider |
| scope | jurisdiction, route, filing unit, classes and service stage |
| package | exact approved Filing Package version and attachments |
| authority | Filing Approval and appointment references |
| deadline | source, time zone, target and latest acceptance time |
| fees | agreed terms, official funds and payment condition |
| communication | response channel, responsible actors and escalation |
| expected evidence | acceptance, rejection, correction, filing receipt or official acknowledgement |
| restrictions | no material change, substitution, extra cost or filing outside stated authority |

The instruction must be reproducible after the event.

## 5. Separate Instruction Approval

A separate gate may be required when:

- the provider differs from the approved route;
- official funds will be committed;
- sensitive Documents will be disclosed;
- the provider may alter filing content;
- urgency fees or commercial exceptions apply;
- the engagement extends beyond the approved stage.

Filing Approval does not automatically grant every commercial, disclosure or provider-instruction authority.

## 6. Receipt and Provider Acceptance

Use explicit provider states:

```text
Not sent
Sent
Delivery confirmed
Receipt acknowledged
Acceptance pending
Accepted
Accepted with conditions
Clarification requested
Rejected
No response
Unknown
```

`MR-D05 Provider Acceptance` records:

- accepted instruction version and scope;
- responsible provider actor;
- acceptance time;
- fee and deadline commitment;
- conditions and missing information;
- provider reference;
- expected filing route and evidence.

Delivery, receipt and an ambiguous `noted` response do not prove acceptance.

## 7. Provider-Proposed Change

A provider may propose changes to applicant format, goods/services, mark description, route, declaration, fees, Documents or timing.

A material proposal creates a new candidate version and returns to the relevant professional, client, commercial and approval gates. The provider may advise; it may not silently mutate the approved package.

## 8. Rejection, Substitution and Termination

A rejection or inability to accept records:

- reason and affected scope;
- deadline consequence;
- data already disclosed;
- fee and cancellation effect;
- Document or original custody;
- conflict recheck needs;
- Filing Approval impact;
- renewed routing requirement.

Substitution restarts the necessary CH25 and CH26 controls.

Internal termination does not itself remove an official representative; official recordal remains a separate protected action.

## 9. Purpose-Limited Provider Access

The provider receives only information required for conflict checking, appointment, accepted service, deadline handling and evidence return.

Access to one Matter must not expose unrelated clients, portfolio strategy, other providers, procurement costs or margin.

## 10. `EMBERLOOP` — `EL-19`

The selected US private partner receives an appointment and Instruction referencing the approved US word-mark package.

The provider acknowledges receipt, confirms eligibility and fee terms, and requests one declaration revision. It does not file until the revised package receives targeted Professional Review and renewed Filing Approval.

The revised Instruction is then accepted as `MR-D05 Provider Acceptance`.

## 11. Controlled Scenarios

### `MR-SCN-20` — Provider proposes a material change

The Product creates a new candidate version and routes it back to the required Decision gates. Provider advice does not replace client or professional authority.

### `MR-SCN-21` — Receipt without acceptance

When delivery is confirmed but acceptance is pending, the surface shows `received — acceptance pending` and blocks provider Execution.

### `MR-SCN-22` — Provider over-access

A request for unrelated portfolio, client or margin data is denied and the accepted purpose remains preserved.

## 12. AI Assistance

AI may draft appointment and instruction records, compare acceptance with instruction, extract conditions and detect scope or fee mismatches.

AI may not appoint, disclose sensitive materials, accept provider terms, approve extra fees, authorize material changes or treat an ambiguous response as acceptance.

## 13. Chapter Lock

```text
Selection identifies the intended provider.
Appointment creates the permitted relationship.
Instruction defines the requested work.
Provider Acceptance confirms the engagement scope.
Provider Acceptance ≠ submission.
Provider receipt ≠ official receipt.
```

## 14. Handoff to CH27

CH26 produces an accepted provider Instruction or approved direct route.

CH27 creates `MR-A17 Execution Request` and preserves the authority boundaries among MarkReg, Book 03 Execution, providers, connectors, Owning Services and official offices.
