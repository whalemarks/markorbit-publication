# Appendix B — Lifecycle State and Authority Matrix

**Status:** Controlled Scaffold — content completion pending PF-02 and PF-04  
**Primary sources:** CH07, CH21–CH42, B05-SPEC-0001 and B05-SPEC-0003  
**Reader purpose:** show which state is being described, who may change it, and what external effect it carries.

## B.1 Core Rule

MarkReg must never collapse every lifecycle dimension into one status.

```text
Product state
≠ formal business state
≠ Execution state
≠ provider-reported state
≠ official status
≠ professional interpretation
≠ client-facing projection
```

## B.2 State Domains

| State domain | Examples | Typical authority | External effect |
| --- | --- | --- | --- |
| Product journey | draft, incomplete, ready for review, blocked, superseded | MarkReg plus accountable users | none by itself |
| commercial | Quote draft, valid, accepted, expired; payment pending or received | commercial and finance services | commercial effect only within applicable terms |
| formal work | Order open, Matter active, Task assigned, Review pending | Owning Services and Workplace | organizational effect, not official-office effect |
| approval | client confirmed, Professional Review complete, Filing Approval active | authorized Human role and approval service | authorizes only the stated next step |
| Execution | prepared, queued, started, failed, unknown, reconciled | Book 03 Execution and execution-capable service | coordinated operational effect |
| provider | instructed, received, accepted, declined, change requested, reported filed | appointed provider | provider relationship effect; not automatically official truth |
| official submission | sent, delivery confirmed, accepted by office, rejected, correction required | external office evidence | procedural effect depends on official evidence |
| official lifecycle | filed, under examination, published, opposed, registered, cancelled, expired | official authority | authoritative official status |
| professional interpretation | low risk, response recommended, evidence insufficient, appeal viable | eligible professional | advice or decision support, not official outcome |
| client projection | action required, waiting for office, registered scope summary | MarkReg from sourced evidence | explanatory only |
| continuing obligation | renewal due, use declaration required, recordal pending | official rule plus verified calculation | future duty; reminder is not the deadline itself |

## B.3 Key State Distinctions

| Distinction | Required reading |
| --- | --- |
| recommendation vs decision | the Product may propose; an accountable actor decides |
| readiness vs approval | readiness describes conditions; approval grants bounded authority |
| approval vs Execution | approval permits an action; Execution coordinates it |
| sent vs delivered | a request may leave the sender without reaching the destination |
| delivered vs provider received | technical delivery does not prove Human or provider receipt |
| provider received vs provider accepted | receipt does not establish accepted engagement |
| provider reported filed vs officially acknowledged | provider report requires evidence and may remain unverified |
| officially acknowledged vs registered | acknowledgement begins or confirms a procedure; registration is a later outcome |
| registered vs certificate available | the right may exist before or independently of a certificate file |
| certificate vs current official record | a certificate may become historically accurate but operationally stale |
| renewal filed vs renewed right | filing requires later acknowledgement or official update |
| assignment signed vs official owner updated | contractual effect and recordal effect remain separate |
| monitoring signal vs legal conclusion | a signal opens Review; it does not establish infringement or required action |

## B.4 Illustrative Authority Matrix

| State transition | May propose | Must review or confirm | May authorize | Evidence required |
| --- | --- | --- | --- | --- |
| Need Brief draft → confirmed | MarkReg or user | user or professional where material | user confirmation | source facts and change history |
| Quote draft → accepted | commercial surface | client verifies exact version | authorized client actor | Quote version and acceptance record |
| Intake incomplete → ready for Review | MarkReg | coordinator and professional | no external authority | requirement and validation results |
| package candidate → reviewed | professional preparer | eligible reviewer | reviewer decision | package diff and source lineage |
| reviewed package → Filing Approval | Product may request | client and professional conditions as applicable | authorized approver | exact package version and approval scope |
| approved → Execution started | MarkReg may prepare request | Execution entry validation | existing approval only | Handoff and idempotency identity |
| sent → official acknowledgement | provider or connector may report | reconciliation or official-source check | no additional Product authority | official receipt, office account or verified evidence |
| official notice → response strategy | MarkReg and professional may propose | eligible professional and client where needed | defined response authority | notice, Issue Set, deadline and strategy version |
| registration event → Right Baseline | MarkReg may project | professional or responsible team verifies | no creation of official right | official record and registered-scope comparison |
| renewal candidate → renewal filing | MarkReg may prepare | professional, client, finance and approver as applicable | exact renewal approval | right verification, fees, package and route |
| transaction document → official recordal | client and professional may prepare | authority and chain of title reviewed | recordal approval | signed documents, official filing and result |

## B.5 Unknown and Conflict States

The Product must support explicit states such as:

- source unavailable;
- source conflict;
- provider report awaiting evidence;
- technical outcome unknown;
- deadline disputed;
- rule changed and unverified;
- approval invalidated by later change;
- official event corrected or superseded;
- owner identity conflict;
- chain-of-title gap.

Unknown does not mean failed, successful or safe to retry.

## B.6 Completion Work

PF-02 and PF-04 must:

1. map each state to controlled artifacts and decisions;
2. identify source, owner and transition evidence;
3. index the Given/When/Then scenarios that test each high-risk distinction;
4. align state terms across all chapters and figures;
5. validate that client-facing labels do not overstate provider or official state.

This appendix becomes publication-ready only after the controlled state and scenario indexes are reconciled.