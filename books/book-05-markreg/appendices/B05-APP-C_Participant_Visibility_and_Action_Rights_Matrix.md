# Appendix C — Participant Visibility and Action Rights Matrix

**Status:** Controlled Reader Draft — PF-04 Reconciled  
**Primary sources:** CH05, CH24–CH26, CH43–CH44 and B05-SPEC-0003 v0.2  
**Reader purpose:** show who may see, contribute, review, approve, execute and communicate at each material stage.

## C.1 Role Rule

One person may hold several roles, but every material action must record the role used.

```text
identity
≠ represented organization
≠ participant role
≠ professional qualification
≠ delegated authority
≠ accepted provider engagement
```

## C.2 Participant Summary

| Participant | Primary responsibility | Must not be assumed to have | Priority scenarios |
| --- | --- | --- | --- |
| client contact | business facts and client Decisions | Professional Review or Filing Approval | 14, 28 |
| applicant or owner representative | identity, ownership and authority facts | authority beyond represented entity | 01, 11, 12 |
| professional | professional judgment and governed work | client commercial authority automatically | 04, 09, 17 |
| reviewer | quality, law, source, evidence and risk Review | Execution or provider appointment | 16, 17 |
| approver | bounded approval for an exact version and purpose | power to edit the approved artifact | 16, 18 |
| coordinator | collect, route, remind, reconcile and escalate | professional strategy authority by default | 17, 28 |
| account owner | client relationship and commercial continuity | legal or filing authority automatically | 06, 07 |
| finance participant | payment, payable, tax and refund facts | unrelated confidential evidence | 08, 15 |
| external provider | accepted engagement and return evidence | organization-wide or portfolio-wide access | 19–23 |
| organization administrator | configure users, roles and policy | silent impersonation | 18, 35 |
| AI assistant | extraction, comparison, drafting and explanation | identity, permission, Review, approval or external authority | 09, 36, 37 |

## C.3 Visibility Classes

| Visibility class | Typical content | Default audience | Prohibited disclosure example |
| --- | --- | --- | --- |
| client visible | reviewed scope, client-facing price, status and Decisions | authorized client participants | internal provider ranking |
| professional restricted | analysis, evidence assessment, amendments and strategy | eligible professionals and reviewers | unrelated provider staff |
| organization private | margin, provider comparisons, internal policy and Knowledge | permitted organization roles | client or provider by default |
| provider purpose-limited | accepted instructions, required Documents and return evidence | appointed provider | unrelated portfolio data |
| finance restricted | payment, tax, payable, refund and reconciliation | finance and authorized commercial roles | full dispute evidence |
| personal local | Lite notes and personal learning | authorized Lite user | organization Workplace without transfer instruction |
| official-source public | office data with source and freshness | role-appropriate surfaces | unsourced current-status claim |
| confidential evidence | purpose-restricted evidence | expressly permitted participants | reuse for another proceeding without review |

Visibility is field-, purpose-, organization- and relationship-specific. A page title is not an access-control rule.

## C.4 Action Rights Matrix

| Action | Client | Professional / reviewer | Approver | Coordinator | Finance | Provider | Administrator | AI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| provide facts | within authority | yes with source | no | collect | payment facts only | request or return task facts | no | extract candidate |
| correct facts | within authority | yes with source | no | propose correction | payment facts only | propose correction | no | flag conflict |
| choose commercial option | authorized client | advise | policy approval only | coordinate | confirm condition | no | no | explain options |
| create professional strategy | no | eligible professional | no | suggestion only | no | proposal within engagement | no | draft candidate |
| confirm package facts | yes | yes | no | coordinate | no | request change | no | compare versions |
| perform Professional Review | no | eligible reviewer | no | no | no | only if separately eligible and appointed | no | no |
| grant Filing Approval | no | only if separately authorized | yes | no | no | no | no | no |
| select provider | if organization policy permits | recommend or review | approve if required | coordinate | cost input | no | no | compare evidence |
| accept provider engagement | no | no unless provider role | no | no | no | appointed provider | no | no |
| execute protected action | no | only through governed route | no | coordinate only | payment gate | accepted provider | no | no |
| verify official event | acknowledge | yes | no | reconcile | no | report with evidence | no | summarize sourced evidence |
| release Jurisdiction Pack | no | professional owner or reviewer | Pack approver | coordinate | no | advice only | no | propose change candidate |
| send protected Communication | confirm or approve where required | prepare or approve if authorized | approve where required | send if authorized | financial messages | engagement messages | no | draft only |

Actual rights also depend on jurisdiction, qualification, organization policy, delegation and accepted engagement.

## C.5 Multi-Party Gate Examples

### Filing

```text
client confirmed facts and scope
+ Professional Review complete
+ payment condition satisfied
+ Filing Approval active
+ provider accepted instruction
≠ official filing completed
```

### Response

```text
official notice verified
+ Issue Set reviewed
+ client selected material strategy
+ Response Package reviewed
+ Filing Approval active
≠ response officially acknowledged
```

### Renewal

```text
Right Baseline verified
+ owner and scope confirmed
+ Renewal Package reviewed
+ payment condition satisfied
+ Renewal Approval active
≠ renewed register entry verified
```

## C.6 Role Switching

When one actor holds several roles, the Product must require an explicit role for each material action.

Example:

```text
same person as account owner
→ may explain Quote

same person acting as eligible professional
→ may record Professional Review

same person acting as authorized approver
→ may grant exact-version Filing Approval
```

The three actions remain separate records with separate authority bases.

## C.7 Delegation Requirements

Delegation must record:

- delegating and receiving actors;
- role and action delegated;
- represented organization;
- purpose and scope;
- start and expiry;
- prohibited subdelegation;
- accepted or declined state;
- audit reference.

Delegation cannot create professional qualification, client authority or provider appointment that the delegate does not otherwise possess.

**Required tests:** MR-SCN-11 and MR-SCN-18.

## C.8 Purpose-Limited Surface Rules

### Client surface

May show:

- business objective and options;
- reviewed scope and assumptions;
- client-facing fees;
- required facts and Documents;
- sourced status and consequence;
- pending Decisions and deadlines.

Must not expose by default:

- internal margin;
- competing provider quotes or ranking notes;
- unrelated client or portfolio data;
- internal reviewer comments;
- unreviewed AI reasoning;
- credentials or connector details.

### Professional and reviewer surface

May show:

- official sources and retrieval evidence;
- Pack and Rule versions;
- artifact lineage and material diffs;
- evidence provenance;
- provider reports and conflicts;
- AI candidates and Human disposition;
- approval and deadline status.

Must identify qualification, represented organization and conflict state.

### Approver surface

Must show:

- requested action;
- exact artifact version;
- jurisdiction, route and affected scope;
- provider or connector path;
- fees and payment condition;
- deadline;
- unresolved risk;
- expiry and consequence.

A generic `Approve` action without scope is non-conforming.

### Coordinator surface

May collect, route, remind, reconcile and escalate.

It must convert strategy or approval suggestions into requests to eligible actors rather than recording them as professional Decisions.

### Finance surface

May show Quote, payable, currency, tax, discount approval, payment, refund and reconciliation facts.

It should not require access to unrelated legal evidence or dispute strategy.

### Provider surface

May show accepted engagement scope, required facts, Documents, deadlines, instructions, fee terms and return-evidence requirements.

It must not expose unrelated Matters, other provider quotes, internal margin, personal Lite notes or unrestricted private Knowledge.

### Administrator surface

May configure accounts, roles and organization policy.

It may not silently impersonate client, professional, approver or provider actions.

### AI surface

May display extraction, comparison, explanation, draft, recommendation or change candidates.

It must not display AI as the accountable actor for Review, approval, permission or external action.

## C.9 Cross-Surface and Embedded Controls

| Risk | Required behavior | Scenario |
| --- | --- | --- |
| Lite private data included in Handoff | exclude unless purpose-approved | MR-SCN-34 |
| deep link opened in wrong organization | block and require context switch | MR-SCN-35 |
| provider requests broader access | deny outside engagement | MR-SCN-22 |
| duplicate Return consumption | return existing result | MR-SCN-25 |
| one actor changes role | record role and authority for each action | MR-SCN-11, 18 |
| AI task lacks source context | classify as research or verification task | MR-SCN-36 |

## C.10 Communication Rights

| Communication type | Preparer | Required reviewer or approver | Sender |
| --- | --- | --- | --- |
| client option explanation | professional, coordinator or AI draft | professional where material | authorized client-service actor |
| filing confirmation request | coordinator or professional | professional / approver as policy requires | authorized coordinator |
| provider instruction | professional or coordinator from approved package | existing approval and appointment checks | authorized organization actor |
| official-event update | coordinator or AI draft from source | responsible professional where interpretation is material | authorized client-service actor |
| dispute or settlement Communication | professional | client and professional authority | authorized professional or coordinator |
| payment notice | finance | finance policy | authorized finance actor |
| correction Communication | responsible preparer | authority matching the corrected subject | authorized sender |

Sent, delivered, acknowledged and corrected remain separate states.

## C.11 Scenario Coverage by Participant

| Participant | Minimum high-risk scenarios |
| --- | --- |
| client | 01, 06, 14, 28, 29 |
| professional | 04, 09, 12, 17, 27, 36 |
| reviewer | 16, 17, 20, 26 |
| approver | 11, 16, 18, 31 |
| coordinator | 17, 23, 28, 29 |
| finance | 07, 08, 15 |
| provider | 19–23, 27 |
| administrator | 18, 35 |
| AI | 09, 36–38 |

## C.12 Reconciliation Status

```text
Role names normalized: COMPLETE
Visibility classes reconciled: COMPLETE
Action-right matrix reconciled: COMPLETE
Role switching and delegation mapped: COMPLETE
Purpose-limited surfaces mapped: COMPLETE
Communication rights mapped: COMPLETE
High-risk scenarios assigned: COMPLETE
PF-04 Appendix C work: COMPLETE
PF-05 jurisdiction evidence linkage: PENDING
PF-06 editorial compression: PENDING
PF-08 validation: PENDING
```

Appendix C is a controlled reader draft reconciled for PF-04. It does not grant permissions; actual permission remains governed by the relevant organization, relationship, qualification, jurisdiction and formal service.