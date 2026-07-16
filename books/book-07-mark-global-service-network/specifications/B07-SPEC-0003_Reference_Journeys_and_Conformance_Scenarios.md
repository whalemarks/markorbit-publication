# B07-SPEC-0003 — MGSN Reference Journeys and Conformance Scenarios

## Reference Journeys

### MG-J01 — Routine Filing Through Recommended Managed Route

```text
Originating Workplace identifies filing need
→ MG-R01 Capability Need Projection
→ R2 selected
→ MG-R03 / R04 eligibility, conflict and availability
→ MG-R05 Candidate Route Set
→ MG-R06 Recommended Route
→ user confirms through MG-R07
→ MG-R08 allocation and Provider Acceptance
→ MG-F01 Engagement
→ funds and milestones
→ filing Evidence
→ MG-F09 Return Envelope
→ Originating Workplace resumes Matter continuity
```

### MG-J02 — Preferred Existing Provider Migrates Into MGSN

```text
user identifies existing provider
→ provider introduction and MG-T01 provenance
→ provider admission and Capability verification
→ procurement / service-package admission
→ R3 route request
→ platform gates
→ user confirmation
→ managed Engagement
```

### MG-J03 — External Self-Managed Route With Manual Continuity

```text
user selects R1
→ MGSN records route and visibility limits
→ user manages provider and funds externally
→ reminders request expected Evidence
→ user uploads receipt / office Document / status
→ source qualification
→ downstream Product resumes from qualified Evidence
```

### MG-J04 — Provider Conflict Requires Alternative

```text
Recommended provider identified
→ conflict check fails
→ candidate excluded
→ alternate portfolio route selected
→ explanation shown
→ user confirms
→ allocation and acceptance
```

### MG-J05 — Provider Delay and Replacement

```text
milestone overdue
→ MG-E01 Incident
→ correction request
→ no satisfactory response
→ MG-E03 Replacement Decision
→ funds and scope reconciliation
→ alternative provider accepts
→ continuity package transferred through governed Handoff
→ completion and Return
```

### MG-J06 — Demand Participant Introduces Provider

```text
existing provider suggested
→ independent provider invitation
→ admission and Evidence review
→ Relationship Provenance
→ service-package negotiation
→ first managed work completed
→ incentive eligibility evaluated
→ provider may serve other eligible demand participants
```

### MG-J07 — Provider Introduces Demand Participant

```text
provider invites existing client/agency
→ invited Organization independently joins
→ Workplace / Lite connection created
→ Relationship Provenance
→ first paid managed route completed
→ bounded incentive evaluated
→ invited Organization may use broader MGSN subject to entitlement
```

### MG-J08 — Dual-Role Organization

```text
Organization requests foreign capability as Demand Role
while providing domestic capability as Supply Role
→ permissions remain separated
→ payables and receivables remain separated
→ no automatic offset
→ no self-routing without governance approval
```

## Conformance Scenarios

### Participation and Privacy

- **MG-SCN-01:** A Workplace cannot project customer details before a valid purpose and permission scope exists.
- **MG-SCN-02:** Provider admission does not expose its private cost or internal workload to demand participants.
- **MG-SCN-03:** Withdrawal prevents future routing but preserves lawful historical Evidence and obligations.
- **MG-SCN-04:** A platform operator cannot use operator identity to view unrelated Workplace private records.

### Capability and Supply

- **MG-SCN-05:** An unverified Capability Claim cannot be treated as verified supply.
- **MG-SCN-06:** Expired qualification blocks route eligibility until reviewed.
- **MG-SCN-07:** A provider may be active for one jurisdiction/service and restricted for another.
- **MG-SCN-08:** One country/service may contain multiple active providers with different portfolio roles.

### Procurement and Offers

- **MG-SCN-09:** Provider procurement cost is not exposed as the user-facing offer by default.
- **MG-SCN-10:** An official-fee change invalidates or updates affected offers under change control.
- **MG-SCN-11:** A commercial exception requires review and does not silently overwrite standard terms.
- **MG-SCN-12:** Platform margin cannot override eligibility, conflict or professional fit.

### Routing and Choice

- **MG-SCN-13:** No eligible candidate is a safe result and must not be filled with an unverified contact.
- **MG-SCN-14:** Automatic matching produces a recommendation, not an appointment.
- **MG-SCN-15:** User confirmation does not equal Provider Acceptance.
- **MG-SCN-16:** A preferred provider failing conflict or qualification gates cannot be allocated.
- **MG-SCN-17:** The Product may show one recommendation and up to two materially distinct alternatives without exposing the full pool.
- **MG-SCN-18:** A user may select R1 after rejecting managed routes, with visibility limitations disclosed.

### Funds and Fulfillment

- **MG-SCN-19:** Funds received do not authorize release without the required condition and authority.
- **MG-SCN-20:** A network funds projection cannot replace the Finance ledger.
- **MG-SCN-21:** Provider milestone Evidence may support but does not automatically mutate Matter status.
- **MG-SCN-22:** Unknown provider outcome remains unknown and is not automatically retried.
- **MG-SCN-23:** Replacement preserves provenance, scope, funds and Evidence history.
- **MG-SCN-24:** A Return Envelope is validated by the receiving Owning Service before formal state mutation.

### Trust and Relationships

- **MG-SCN-25:** One poor result does not create a universal permanent Trust score.
- **MG-SCN-26:** Relationship Provenance does not create permanent provider exclusivity.
- **MG-SCN-27:** Invitation registration alone does not trigger an incentive.
- **MG-SCN-28:** Private Workplace preference is not automatically visible to other participants.

### Dual Roles and Governance

- **MG-SCN-29:** Demand-side payables and supply-side receivables are not automatically offset.
- **MG-SCN-30:** An Organization cannot route related work to itself or an affiliate without disclosure and governance approval.
- **MG-SCN-31:** Provider contact obtained through MGSN does not grant an unrestricted bypass right for MGSN-originated work.
- **MG-SCN-32:** Genuine pre-existing external business may remain outside MGSN, but receives no implied platform guarantees.

## Scenario Gate

Every future Product specification, fixture or implementation must demonstrate how it preserves these scenarios or explicitly propose a controlled amendment.
