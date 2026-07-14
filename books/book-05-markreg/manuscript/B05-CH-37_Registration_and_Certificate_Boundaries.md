# B05-CH-37 — Registration and Certificate Boundaries

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part VI — Registration and Portfolio Continuity

## Chapter Purpose

Part V may end with a registration-stage candidate. Part VI begins only when a sourced official event supports a registered right.

```text
EL-30 / CH37
MR-E08 Registration Outcome Record
→ MR-V01 Filing and Scope Diff View
→ MR-B01 Right Baseline
→ maintenance and portfolio continuity
```

The Product question is:

> What was officially registered, according to which source, what differs from the approved and acknowledged scope, and what continuing obligations now exist?

```text
Official registration record
≠ certificate
≠ certificate file
≠ Product projection
≠ permanent validity
```

## 1. Registration Outcome Record

`MR-E08 Registration Outcome Record` should preserve:

- office, jurisdiction and official identifiers;
- registration and effective dates;
- registered owner and mark representation;
- registered classes and goods/services;
- limitations, disclaimers, exclusions or conditions;
- official source, retrieval time and source version;
- certificate relationship and availability;
- unresolved source, owner or scope conflicts.

A Provider Report may trigger verification. It does not create registration.

## 2. Registered-Scope Diff

`MR-V01 Filing and Scope Diff View` compares:

```text
approved Filing Package Candidate
→ acknowledged filing record
→ officially registered scope
```

The diff should expose deleted or narrowed items, fewer classes, limitations, normalized owner data and prosecution-stage changes. The Product must not label the original requested scope as registered when the official result is narrower.

## 3. Official Record and Certificate

| Record | Controlled meaning |
| --- | --- |
| official registration record | office-controlled current record |
| certificate | office-issued representation of registration |
| certificate file | received digital or scanned material |
| `MR-E08` | sourced historical registration outcome |
| `MR-B01` | reviewed operational baseline for later work |
| Product projection | user-facing explanation derived from sources |

A certificate may be delayed, electronic, corrected or reissued. Its absence does not necessarily disprove registration; its presence does not prove the register is still unchanged.

`MR-SCN-30` applies when the certificate differs from the current official record: retain both, use current verified official data for the baseline and expose the difference.

## 4. Owner and Current-State Verification

The registered owner should be compared with:

- the approved applicant;
- the acknowledged filing owner;
- current official data;
- the client’s business-owner claim;
- pending name changes, assignments or mergers;
- instructor and signatory authority.

Conflicting values remain separate until professionally resolved. MarkReg does not replace the official owner with the expected group company.

## 5. Right Baseline

`MR-B01 Right Baseline` is the reviewed starting point for future lifecycle work. It should contain:

- official identity, jurisdiction and identifiers;
- registered mark, owner and scope;
- registration, priority and term information;
- certificate state;
- current representative;
- active proceedings and limitations;
- known maintenance and use obligations;
- next verified deadline;
- linked official sources and Evidence;
- unresolved ownership, scope or source conflicts.

A later official change creates a new baseline version. It does not rewrite the historical registration outcome.

## 6. Registration Does Not Remove Risk

A registered right may remain exposed to:

- cancellation or invalidation;
- non-use vulnerability;
- pending appeal or dispute;
- owner or recordal conflict;
- maintenance and renewal duties;
- representative requirements;
- unpaid later-stage charges;
- certificate or official-record correction.

Registration status and vulnerability must be shown separately.

## 7. `EMBERLOOP` — `EL-30`

A sourced UK registration event is verified. MarkReg:

1. creates `MR-E08 Registration Outcome Record UK v1`;
2. compares the approved, acknowledged and registered scopes in `MR-V01`;
3. preserves a narrowed item introduced during examination;
4. creates `MR-B01 Right Baseline UK v1`;
5. records certificate availability as a separate sourced fact;
6. opens maintenance and evidence-planning work.

The US application remains under examination. The EU application remains in opposition. Neither is counted as registered.

## 8. `RIVERKITE` Verification Contrast

`RK-02` requires each of the six registrations to be verified independently by identifier, owner, scope and source date. An unresolved owner conflict blocks unsupported authority but does not erase the official registration history.

## 9. Controlled Scenarios

- **MR-SCN-10 — Stale official status:** refresh a stale source before deadline-sensitive or protected action relies on it.
- **MR-SCN-26 — Corrected official event:** preserve prior and corrected sources and re-evaluate affected records.
- **MR-SCN-30 — Certificate differs from current official record:** retain the certificate as Evidence and expose the current-source diff.
- **MR-SCN-33 — One challenged right in a portfolio:** preserve the challenged right independently from unaffected rights.

## 10. AI Assistance

AI may extract registration data, compare scopes, classify certificate files and identify possible mismatches. It must not create registration, authenticate a certificate, decide ownership or remove official limitations.

## 11. Minimum Registration Lock

```text
Registration begins with sourced official evidence.

Registration Outcome Record,
official record, certificate,
Product projection and Right Baseline
remain distinct.

Registered scope is compared with
approved and acknowledged scope.

Registration does not erase
maintenance, use, ownership,
dispute or vulnerability conditions.
```

## 12. Handoff to Maintenance

CH38 turns the verified `MR-B01 Right Baseline` into `MR-B02 Maintenance Obligation Set` and `MR-B03 Use-Evidence Coverage Record` without treating a reminder or calculated date as an official deadline.
