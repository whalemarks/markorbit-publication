# B05-CH-40 — Changes, Recordals and Ownership Updates

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part VI — Registration and Portfolio Continuity

## Chapter Purpose

A business change, signed document, internal master-data update and official recordal are different events.

```text
EL-33 / CH40
MR-B01 Right Baseline
→ MR-C07 Recordal Context
→ MR-A27 Recordal Package Candidate
→ MR-D09 Recordal Approval
→ MR-A17 Execution Request
→ MR-E09 Official Update Evidence
→ updated MR-B01 Right Baseline
```

The Product question is:

> What official data must change, what caused the change, which rights and jurisdictions are affected, and what official Evidence will prove the result?

```text
Internal data update
≠ signed change document
≠ recordal filed
≠ official record updated
```

## 1. Recordal Context

`MR-C07 Recordal Context` should preserve:

- change type and legal or factual cause;
- current official value, claimed value and proposed value;
- effective date and source;
- affected rights, jurisdictions and proceedings;
- required Documents and chain-of-title Evidence;
- signatory and instruction authority;
- Provider, fee and deadline requirements;
- dependencies on renewal, dispute or transaction work;
- unresolved conflicts.

Name, address, representative, clerical correction, limitation, merger and assignment are not one generic `owner update`.

## 2. One Event, Many Official Actions

A corporate event may affect several applications, registrations, proceedings and local representatives. MarkReg may group the business initiative, but every official filing retains independent:

- right and jurisdiction;
- current official value;
- Requirement Set;
- package and approval;
- Execution identity;
- acknowledgement and official result.

A portfolio initiative may therefore be partially complete.

## 3. Current, Claimed and Proposed Values

The Product should display a precise diff:

```text
current official value
→ client or business claim
→ proposed filed value
→ value recorded by the office
```

Display normalization must not silently become the filed value. Original-language values, legal form, entity identifier, address components and affected rights remain traceable.

## 4. Recordal Package and Approval

`MR-A27 Recordal Package Candidate` should include:

- `MR-C07` reference;
- current and proposed official data;
- affected-right list;
- supporting Documents and authority;
- form or statement content;
- Pack and source versions;
- fees, Provider and route;
- deadline, sequence and dependencies;
- unresolved issues and package version.

`MR-D09 Recordal Approval` binds exact changes, rights, Documents, jurisdictions, fees and route. An administrator editing Workplace or CRM data cannot grant this approval.

## 5. Sequencing with Other Work

The professional Decision may require:

```text
recordal before renewal or dispute action
recordal filed together with another action
other action under current official data
parallel independent actions
protected action blocked pending resolution
```

The sequence is jurisdiction- and purpose-specific. A transaction’s contractual effective date does not determine every office’s filing sequence.

## 6. Official Result and Partial Completion

`MR-E09 Official Update Evidence` may show:

- full acceptance;
- acceptance for selected rights only;
- office normalization of the requested value;
- deficiency or additional-evidence request;
- application updated while registration remains unchanged;
- certificate reissue pending;
- rejection or unknown status.

Each `MR-B01 Right Baseline` updates only after its own sourced result. Requested and recorded values remain visible.

## 7. `RIVERKITE` — `RK-11`

One registration still names a predecessor company while the group claims ownership through a merger and later assignment. MarkReg creates:

```text
MR-C07 Recordal Context
→ chain-of-title Review
→ MR-A27 Recordal Package Candidate
→ MR-D09 Recordal Approval when ready
```

The ownership-linked renewal and recordal proceed in parallel under the sourced professional Decision. Current official owner, contractual or business-owner claim and proposed recorded owner remain separate until `MR-E09` verifies each official update.

## 8. `EMBERLOOP` — `EL-33`

The reviewed baseline contains no activated EMBERLOOP recordal. A possible future reorganization remains a change signal only; no `MR-C07`, package, approval or official update is invented.

## 9. Controlled Scenarios

- **MR-SCN-16 — Package changed after approval:** a material right, owner, Document or value change invalidates affected approval.
- **MR-SCN-26 — Corrected official event:** preserve old and corrected official results.
- **MR-SCN-31 — Owner mismatch:** expose dependency before renewal or recordal action.
- **MR-SCN-32 — Assignment signed but not recorded:** show contractual and official states separately.
- **MR-SCN-33 — One challenged right:** do not propagate one recordal or dispute state across unrelated rights.

## 10. AI Assistance

AI may classify signals, compare values, identify affected rights, extract Documents and prepare candidate diffs. It must not decide identity continuity, establish ownership, approve sequencing or mark official data changed without sourced Evidence.

## 11. Minimum Recordal Lock

```text
Business fact, internal data,
signed Document, recordal package,
filed action and official update
remain distinct.

One business event may require
many independent official actions.

Current, claimed, proposed
and recorded ownership
must not be collapsed.
```

## 12. Handoff to Transactions

CH41 governs `MR-C08 Transaction Context`, `MR-C09 Licence Context`, `MR-A28 Affected-Right Set` and `MR-V03 Chain-of-Title View` before or alongside recordal work.
