# B07-CH-31 — Reference Journeys and Conformance Scenarios

## 1. Why journeys and scenarios matter

A Product Constitution can sound coherent while leaving edge cases unresolved.

Reference Journeys show how the main Product loops connect. Conformance Scenarios test whether a future specification or implementation preserves the controlled distinctions under normal, adverse and ambiguous conditions.

```text
Reference Journey
= end-to-end explanatory path

Conformance Scenario
= boundary test that must remain true
```

Neither is an implementation script or database design.

## 2. MG-J01 — Routine filing through R2

```text
Originating Workplace identifies filing need
→ Capability Need Projection
→ R2 Recommended Managed Route
→ eligibility, conflict and Availability gates
→ Candidate Route Set
→ Recommended Route
→ user confirmation
→ allocation and Provider Acceptance
→ Managed Network Engagement
→ funds and milestones
→ filing Evidence
→ typed Return
→ Workplace and Owning Service validation
```

This journey tests the ordinary managed route while preserving the distinction between recommendation, confirmation, acceptance, completion and formal truth.

## 3. MG-J02 — Existing provider migrates into MGSN

```text
User identifies existing provider
→ independent invitation
→ Relationship Provenance
→ provider admission
→ Capability Evidence and verification
→ procurement and Service Package admission
→ R3 request
→ platform gates
→ user confirmation
→ managed Engagement
```

A prior relationship may influence preference, but it does not replace MGSN admission or create permanent exclusivity.

## 4. MG-J03 — External route with manual continuity

```text
User selects R1
→ platform records visibility limits
→ user manages provider and funds externally
→ Product requests expected Evidence
→ user uploads receipt, document or status
→ source qualification
→ downstream continuity resumes from qualified Evidence
```

This journey proves that MGSN can respect external routes without pretending to observe or guarantee them.

## 5. MG-J04 — Conflict requires an alternative

```text
Recommended provider identified
→ conflict check fails
→ provider excluded
→ qualified alternative selected
→ explanation returned
→ user confirms
→ allocation and acceptance
```

Relationship strength, price or platform margin cannot override a failed conflict gate.

## 6. MG-J05 — Delay and replacement

```text
Milestone overdue
→ Network Incident
→ Correction Request
→ insufficient response
→ Replacement Decision
→ scope and funds reconciliation
→ alternative provider accepts
→ governed continuity package
→ completion and Return
```

Replacement must preserve the original Evidence, decisions, funds history and provider responsibility. It is not a silent substitution.

## 7. MG-J06 — Demand participant introduces a provider

```text
Existing provider suggested
→ independent invitation
→ admission and Evidence review
→ Relationship Provenance
→ Service Package negotiation
→ first managed work completed
→ incentive eligibility evaluated
→ provider may serve other eligible participants
```

Introduction expands MGSN supply but does not transfer ownership of the provider to the introducing participant.

## 8. MG-J07 — Provider introduces a demand participant

```text
Provider invites existing client or agency
→ invited Organization independently joins
→ Workplace or Lite connection created
→ Relationship Provenance
→ first paid managed route completed
→ bounded incentive evaluated
→ Organization may use wider MGSN capability
```

The provider does not own all future demand created by the invited Organization.

## 9. MG-J08 — Dual-role Organization

```text
Organization requests foreign capability as Demand Role
while providing domestic capability as Supply Role
→ permissions remain separated
→ payables and receivables remain separated
→ no automatic offset
→ no self-routing without disclosure and approval
```

The Organization is one participant identity, but each role has a distinct authority, data and financial context.

## 10. Scenario groups

The thirty-two controlled scenarios form seven groups.

### Participation and privacy — MG-SCN-01–04

They require that:

- customer details are not projected without purpose and permission;
- provider admission does not expose private cost or workload;
- withdrawal stops future routing while preserving lawful history;
- platform operator identity does not grant unrestricted Workplace access.

### Capability and supply — MG-SCN-05–08

They require that:

- unverified claims remain unverified;
- expired qualification blocks eligibility;
- restrictions can be service- or jurisdiction-specific;
- one country and service may have several active portfolio routes.

### Procurement and offers — MG-SCN-09–12

They require that:

- procurement cost is not the user-facing offer by default;
- official-fee changes trigger change control;
- exceptions do not silently overwrite standard terms;
- platform margin cannot override eligibility, conflict or fit.

### Routing and choice — MG-SCN-13–18

They require that:

- no eligible candidate is a safe result;
- automatic matching remains a recommendation;
- user confirmation remains distinct from Provider Acceptance;
- a preferred provider cannot bypass gates;
- only bounded meaningful alternatives are shown;
- R1 remains available with disclosed limitations.

### Funds and fulfillment — MG-SCN-19–24

They require that:

- receipt of funds does not itself authorize release;
- MGSN does not replace the Finance ledger;
- milestone Evidence does not automatically mutate Matter truth;
- unknown external outcomes remain unknown;
- replacement preserves provenance and history;
- Return requires Owning Service validation.

### Trust and relationships — MG-SCN-25–28

They require that:

- one poor result does not create a universal permanent score;
- Relationship Provenance does not create permanent exclusivity;
- invitation registration alone does not trigger rewards;
- private preference is not automatically shared.

### Dual roles and governance — MG-SCN-29–32

They require that:

- payables and receivables are not automatically offset;
- self-routing and affiliate routing require disclosure and approval;
- provider contact does not grant unrestricted bypass rights;
- genuine pre-existing external business may remain external without platform guarantees.

## 11. Positive, negative and ambiguous tests

A future implementation should not test only successful completion.

### Positive test

The authorized path completes with expected Evidence and Return.

### Negative test

A prohibited path is blocked, such as allocating an expired provider or releasing funds without authority.

### Ambiguous test

The system preserves uncertainty, such as conflicting provider evidence or an unknown official outcome.

```text
Ambiguity represented honestly
> false operational certainty
```

## 12. Traceability

Every future fixture, UI flow, API contract or implementation task should identify the controlled scenarios it covers.

A useful traceability record includes:

- scenario ID;
- preconditions;
- participant roles;
- expected controlled records;
- prohibited mutation;
- expected result;
- Evidence required;
- audit reference.

If a design cannot explain how it preserves an applicable scenario, it is not yet conformant.

## 13. Change control

Reference Journeys and scenarios are controlled Product semantics.

An implementation may add detail, but it must not silently weaken them. A proposed change that alters participant authority, route meaning, funds boundaries, formal-state ownership or protected-action rules requires a controlled upstream amendment.

## 14. Product rule

MGSN is conformant only when its normal journeys work and its difficult scenarios fail safely. Product quality is demonstrated by preserved boundaries under pressure, not merely by successful happy-path transactions.