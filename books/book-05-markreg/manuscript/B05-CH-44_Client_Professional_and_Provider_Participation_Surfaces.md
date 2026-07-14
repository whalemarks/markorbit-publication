# B05-CH-44 — Client, Professional and Provider Participation Surfaces

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part VII — Product Experience and Evolution

## Chapter Purpose

One lifecycle may involve clients, professionals, reviewers, approvers, coordinators, finance users, providers and administrators. MarkReg must give each participant a purpose-limited surface without allowing visibility to become authority.

```text
one controlled record set
→ MR-V05 Participant Surface Projection
→ role- and purpose-limited fields
→ explicit action rights
→ accountable Handoff or Decision
```

## 1. User Question and Primary Action

**User question:** What may I see, contribute, decide, approve or communicate at this step?

**Primary action:** Complete the action permitted by the active role, or hand the step to the accountable participant.

Every material surface identifies:

- participant and active role;
- represented client, organization or provider;
- purpose;
- visible and editable fields;
- requested action and consequence;
- artifact version and source freshness;
- required evidence or authority;
- deadline, expiry and next participant.

## 2. MR-V05 Participant Surface Projection

`EL-37` uses `MR-V05 Participant Surface Projection` to present one controlled record set differently by role and purpose.

A projection does not own the underlying fact. It must retain links to the controlled Artifact, Context, Decision, Evidence, Baseline or formal object from which it is derived.

## 3. Participant Contract

| Participant | Primary contribution | Prohibited assumption |
| --- | --- | --- |
| client contact | business facts, selections and client Decisions | Professional Review or Filing Approval |
| applicant or owner representative | identity, ownership and authority evidence | authority beyond the represented entity |
| professional | judgment, strategy and governed preparation | client commercial authority automatically |
| reviewer | source, quality, evidence, scope and risk Review | Execution or provider appointment |
| approver | exact-version bounded approval | permission to edit the approved record silently |
| coordinator | collect, route, remind, reconcile and escalate | professional strategy authority by default |
| account owner | relationship and commercial continuity | legal or filing authority automatically |
| finance participant | price, payment, payable, tax and refund facts | access to unrelated evidence or strategy |
| provider | accepted engagement work and return evidence | portfolio-wide or organization-wide access |
| administrator | role and policy configuration | impersonation of accountable actors |
| AI assistant | extraction, comparison, drafting and explanation | identity, Review, approval or external authority |

One person may hold several roles, but each material action records the role used.

## 4. Visibility Classes

Information is classified by field and purpose, not only by page:

- **client visible:** reviewed scope, options, client-facing price, status and Decisions;
- **professional restricted:** analysis, amendments, evidence assessment and strategy;
- **organization private:** margin, provider comparison, private Knowledge and policy;
- **provider purpose-limited:** accepted instructions, required facts, Documents and return Evidence;
- **finance restricted:** payment, tax, payable, credit and refund information;
- **personal local:** Lite notes and personal learning;
- **official-source public:** sourced office information with retrieval context;
- **confidential Evidence:** purpose- and participant-restricted Evidence.

Visibility never grants editing, Review, approval, delegation or Execution rights by itself.

## 5. Material Action Rights

| Action | Client | Professional / reviewer | Approver | Coordinator | Finance | Provider | Administrator | AI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| provide or correct facts | within authority | yes with source | no | collect or propose | payment facts | request or return engagement facts | no | extract or flag |
| choose commercial option | authorized client | advise | policy approval only | coordinate | confirm conditions | no | no | explain |
| create professional strategy | no | eligible professional | no | no | no | proposal within engagement | no | draft candidate |
| perform Professional Review | no | eligible reviewer | no | no | no | only if separately eligible and appointed | no | no |
| grant Filing Approval | no | only if separately authorized | yes | no | no | no | no | no |
| select provider | where organization policy permits | recommend or Review | approve if required | coordinate | cost input | no | no | compare evidence |
| accept provider engagement | no | no unless acting as provider | no | no | no | appointed provider | no | no |
| execute protected action | no | through governed route | no | coordinate only | payment gate only | accepted and instructed provider | no | no |
| verify official event | acknowledge | verify | no | reconcile | no | report with Evidence | no | summarize source |
| send protected Communication | confirm or approve where required | prepare or approve if authorized | approve where required | send if authorized | financial only | engagement only | no | draft only |

Actual permission must also satisfy jurisdiction, qualification, organization policy, delegation, relationship and accepted engagement.

## 6. Client Surface

The client surface presents understandable options, consequences, client-facing fees, required facts, reviewed status and pending Decisions.

It does not expose internal margin, provider ranking, unrelated conflict checks, private Knowledge, internal reviewer notes, credentials or unreviewed AI output.

Client confirmation, Quote acceptance and Commercial Instruction remain separate from Professional Review, Filing Approval and Execution.

## 7. Professional, Reviewer and Approver Surfaces

The professional surface retains sources, Pack versions, artifact lineage, issue matrices, redlines, Evidence provenance, deadlines, provider reports, AI candidates and prior Decisions.

The reviewer surface emphasizes material diff, unresolved warnings, changed sources, affected rights and proposed external effect.

The approver surface states exactly:

- what version is being approved;
- jurisdiction, route, right and scope;
- provider or connector route;
- fee and payment condition;
- deadline, risk and conditions;
- approval expiry and invalidation triggers.

A generic `Approve` button without scope is non-conforming.

## 8. Coordinator, Finance and Provider Surfaces

A coordinator may collect, remind, route, reconcile and escalate. Coordination does not create professional or client authority.

Finance sees the accepted Quote, price components, payable, currency, tax, payment and refund state. Payment confirmation is not Filing Approval.

A provider sees only the accepted engagement, approved version, required facts and Documents, deadlines, fee terms and expected Evidence. A provider proposal cannot silently alter approved scope.

## 9. Role Switching and Delegation

Each role switch records:

- active role and represented party;
- authority basis;
- exact action, scope and version;
- start, expiry and conflict state.

Delegation records delegator, delegate, purpose, scope, expiry, subdelegation rule and acceptance.

Delegation cannot create professional qualification, client authority, provider appointment or organization relationship that does not otherwise exist.

## 10. Multi-Party Decisions

MarkReg shows a decision chain rather than one aggregated `approved` state:

```text
client scope confirmed
+ Professional Review complete
+ payment condition satisfied
+ exact-version Filing Approval active
+ Provider Acceptance active
≠ official filing completed
```

Each Decision keeps its own actor, authority, scope, version and expiry.

## 11. Communication Surface

A Communication surface distinguishes:

```text
draft
→ reviewed draft
→ approved Communication
→ sent
→ delivered or failed
→ acknowledged
→ corrected or superseded
```

Recipients, purpose, language, confidentiality, source basis, attachments and approving role are visible before send. Corrections link to the original rather than overwriting history.

## 12. Controlled Scenarios

- `MR-SCN-11` — expired authority blocks the affected action;
- `MR-SCN-18` — delegated approval outside scope or time is blocked;
- `MR-SCN-22` — provider access is limited to the accepted engagement;
- `MR-SCN-34` — private Lite notes do not transfer silently;
- `MR-SCN-35` — the wrong organization context cannot open protected content.

## 13. Reference Journeys

For `EMBERLOOP`, the client, US professional, EU dispute professional, UK maintenance coordinator, finance team and providers receive different projections of the same controlled records. No surface shows one false global status.

For `RIVERKITE`, the executive, ownership specialist, renewal coordinator, defense professional, licence reviewer and providers receive only the rights and Evidence required for their tasks. One portfolio does not create unrestricted access.

## 14. Minimum Participation Lock

```text
Visibility ≠ authority.
Client Decision ≠ Professional Review.
Review ≠ approval.
Approval ≠ Execution.
Coordination ≠ professional judgment.
Payment ≠ filing authority.
Provider access ≠ portfolio access.
Administrator access ≠ impersonation.
```

## 15. Handoff to Jurisdiction and AI Governance

CH45 defines the Pack, Rule, source and AI contracts that support these surfaces without converting model memory, organization custom or provider advice into official law.
