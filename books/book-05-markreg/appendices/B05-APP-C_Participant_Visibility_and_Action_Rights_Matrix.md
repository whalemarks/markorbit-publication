# Appendix C — Participant Visibility and Action Rights Matrix

**Status:** Controlled Reader Draft v0.3 — PF-06D Reconciled  
**Primary sources:** CH05, CH24–CH26, CH43–CH44 and B05-SPEC-0003 v0.3  
**Reader purpose:** show who may see, contribute, review, approve, execute and communicate at each material stage.

## C.1 Role Rule

```text
identity
≠ represented organization
≠ participant role
≠ professional qualification
≠ delegated authority
≠ accepted provider engagement
```

One person may hold several roles, but each material action records the role and authority basis used.

## C.2 Participant Summary

| Participant | Primary responsibility | Must not be assumed to have |
| --- | --- | --- |
| client contact | business facts and client Decisions | Professional Review or Filing Approval |
| applicant/owner representative | identity, ownership and authority Evidence | authority beyond represented entity |
| professional | judgment, strategy and governed work | client commercial authority automatically |
| reviewer | quality, Source, Evidence, scope and risk Review | Execution or provider appointment |
| approver | bounded exact-version Approval | power to edit the approved Artifact silently |
| coordinator | collect, route, remind, reconcile and escalate | professional strategy by default |
| account owner | client relationship and commercial continuity | legal or filing authority automatically |
| finance participant | payment, payable, Tax and refund facts | unrelated confidential Evidence |
| provider | accepted engagement and Return Evidence | organization- or portfolio-wide access |
| administrator | users, roles and organization policy | silent impersonation |
| AI assistant | extraction, comparison, draft and explanation | identity, permission, Review, Approval or external authority |

## C.3 Visibility Classes

| Class | Typical content | Default audience |
| --- | --- | --- |
| client visible | reviewed scope, client price, status and Decisions | authorized client participants |
| professional restricted | analysis, Evidence, amendments and strategy | eligible professional roles |
| organization private | Margin, provider comparisons, policy and private Knowledge | permitted organization roles |
| provider purpose-limited | accepted instruction, required Documents and Return Evidence | appointed provider |
| finance restricted | payment, Tax, payable, refund and reconciliation | finance/commercial roles |
| personal local | Lite notes and personal learning | authorized Lite user |
| official-source public | office data with Source/freshness | role-appropriate surfaces |
| confidential Evidence | purpose-restricted Evidence | expressly permitted participants |

Visibility is field-, purpose-, organization- and relationship-specific. `MR-V05 Participant Surface Projection` does not grant an action right.

## C.4 Action Rights

| Action | Client | Professional / reviewer | Approver | Coordinator | Finance | Provider | Admin | AI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| provide/correct facts | within authority | yes with Source | no | collect/propose | payment facts | request/return task facts | no | extract/flag |
| confirm applicant/authority | authorized representative | review `MR-C12` | bounded policy Approval | coordinate | no | request Evidence only | no | compare Sources |
| choose commercial option | authorized client | advise | policy only | coordinate | confirm condition | no | no | explain |
| create professional strategy | no | eligible professional | no | suggestion only | no | propose within engagement | no | draft candidate |
| perform Professional Review | no | eligible reviewer | no | no | no | only if separately eligible | no | no |
| grant Filing Approval | no | only if separately authorized | yes | no | no | no | no | no |
| select provider | policy-dependent | recommend/review | approve if required | coordinate | cost input | no | no | compare Evidence |
| accept engagement | no | no unless provider role | no | no | no | appointed provider | no | no |
| execute protected action | no | through governed route | no | coordinate only | payment gate | accepted provider | no | no |
| verify official event | acknowledge | yes | no | reconcile | no | report with Evidence | no | summarize Source |
| release Pack | no | professional owner/reviewer | Pack approver | coordinate | no | advice only | no | propose candidate |
| send protected Communication | confirm/approve where needed | prepare/approve if authorized | approve if required | send if authorized | financial only | engagement only | no | draft only |

Actual permission also depends on jurisdiction, qualification, organization policy, delegation, relationship and engagement.

## C.5 Multi-Party Gates

```text
client confirmed facts and scope
+ Professional Review complete
+ payment condition satisfied
+ Filing Approval active
+ Provider Acceptance active where required
≠ official filing completed
```

```text
Right Baseline verified
+ owner and scope confirmed through MR-C12 where required
+ Renewal Package reviewed
+ payment condition satisfied
+ Renewal Approval active
≠ renewed register entry verified
```

## C.6 Role Switching and Delegation

Role switching records actor, represented organization, active role, authority source, exact action, scope, version, time, expiry and conflict state.

Delegation records delegator, delegate, role, purpose, scope, start, expiry, subdelegation restriction and acceptance. It cannot create qualification, client authority, provider appointment or relationship that does not otherwise exist.

## C.7 Purpose-Limited Surfaces

- **Client:** reviewed options, scope, client price, Requirements, sourced state and Decisions; no private Margin, provider ranking, internal Review notes, credentials or unrelated data.
- **Professional/reviewer:** Sources, Pack/Rule versions, lineage, diffs, Evidence, conflicts, AI candidates, Review and Approval state.
- **Approver:** exact action, Artifact version, jurisdiction, route, scope, fee, Deadline, unresolved risk, expiry and consequence.
- **Coordinator:** collection, routing, reminders, reconciliation and escalation without professional authority.
- **Finance:** Quote, payable, currency, Tax, discount, payment, refund and reconciliation without unrelated legal strategy.
- **Provider:** accepted scope, required facts, Documents, Deadlines, instruction, fee terms and Return Evidence only.
- **Administrator:** account, role and policy configuration without impersonation.
- **AI:** candidate extraction, comparison, explanation, draft, recommendation or Rule-change output without accountable authority.

## C.8 Embedded and Communication Controls

| Risk | Required behavior |
| --- | --- |
| Lite private data in Handoff | exclude unless purpose-approved |
| deep link in wrong organization | block and require context switch |
| provider over-access | deny outside accepted engagement |
| duplicate Return consumption | return existing result |
| actor changes role | record role and authority per action |
| AI lacks Source context | classify as research/verification task |

Communication states remain draft, reviewed, approved, sent, delivered, failed, acknowledged and corrected/superseded. Correction does not overwrite the original.

## C.9 PF-06D Reconciliation State

```text
Role names and visibility classes: RECONCILED
Action-right matrix: RECONCILED
MR-C12 applicant/authority participation: ADDED
MR-V05 Participant Surface Projection: RECONCILED
Delegation and embedded controls: RECONCILED
PF-08 structural/rendered validation: OPEN
```

Appendix C does not grant permissions. Actual permission remains governed by organization, relationship, qualification, jurisdiction and formal service.
