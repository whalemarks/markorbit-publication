# Appendix C — Participant Visibility and Action Rights Matrix

**Status:** Controlled Scaffold — content completion pending PF-04  
**Primary sources:** CH05, CH24–CH26, CH43–CH44 and B05-SPEC-0003  
**Reader purpose:** provide one compact view of who may see, contribute, review, approve, execute and communicate at each stage.

## C.1 Role Rule

One person may hold several roles, but every material action must record the role used.

```text
Identity
≠ represented organization
≠ participant role
≠ professional qualification
≠ delegated authority
```

## C.2 Participant Summary

| Participant | Primary responsibility | Must not be assumed to have |
| --- | --- | --- |
| client contact | provide business facts and make client decisions | Professional Review or Filing Approval |
| applicant or owner representative | confirm identity, ownership and authority facts | authority beyond the represented entity |
| professional | provide professional judgment and prepare governed work | client commercial authority unless separately granted |
| reviewer | assess quality, law, evidence, scope or risk | Execution or provider-appointment authority |
| approver | grant a bounded approval for an exact version and purpose | power to change the artifact silently |
| coordinator | collect, route, remind, reconcile and escalate | professional strategy authority by default |
| account owner | manage client relationship and continuity | legal or filing authority automatically |
| finance participant | confirm payment, cost and invoice conditions | access to unrelated confidential evidence |
| external provider | accept a bounded engagement and perform instructed work | organization-wide client or portfolio access |
| organization administrator | configure accounts, roles and policy | silent impersonation of accountable participants |
| AI assistant | assist with analysis, drafting and explanation | identity, permission, Review, approval or external authority |

## C.3 Visibility Classes

| Visibility class | Typical content | Default audience |
| --- | --- | --- |
| client visible | decisions, scope, client-facing price, reviewed status and next action | authorized client participants |
| professional restricted | legal analysis, evidence assessment, amendments and internal strategy | eligible professionals and reviewers |
| organization private | margin, provider comparisons, internal policy and private Knowledge | permitted organization roles |
| provider purpose-limited | accepted engagement inputs, deadlines and return evidence | appointed provider participants |
| finance restricted | payment, tax, payable, refund and reconciliation details | finance and authorized commercial roles |
| personal local | Lite-only notes and personal learning | the authorized Lite user |
| official-source public | office records with source and freshness context | role-appropriate surfaces |
| confidential evidence | restricted evidence with purpose and access controls | expressly permitted participants |

Visibility is field- and purpose-specific. A page label alone is insufficient access control.

## C.4 Action Rights Matrix

| Action | Client | Professional | Reviewer | Approver | Coordinator | Finance | Provider | AI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| provide facts | yes | yes | comment | no | collect | payment facts only | request or return task facts | suggest extraction |
| correct facts | yes within authority | yes with source | review | no | propose correction | payment facts only | propose correction | flag conflict |
| choose commercial option | yes | advise | review if required | policy only | coordinate | confirm payment condition | no | explain options |
| create legal or filing strategy | no | yes | review | no | suggest only | no | propose within engagement | draft candidate only |
| confirm package facts | yes | yes | review | no | coordinate | no | request change | compare versions |
| perform Professional Review | no | eligible only | yes | no | no | no | only if appointed and eligible | no |
| grant Filing Approval | no | only if separately authorized | no | yes | no | no | no | no |
| select provider | client or organization actor if authorized | recommend | review conflict or eligibility | approve under policy where required | coordinate | review cost only | no | rank candidate evidence only |
| accept provider engagement | no | no unless provider role | no | no | no | no | yes | no |
| execute filing | no | only through governed route | no | no | coordinate | confirm payment gate | yes if accepted and instructed | no |
| verify official event | acknowledge | yes | review | no | reconcile | no | report with evidence | summarize sourced evidence |
| send protected Communication | approve where required | prepare or approve if authorized | review | approve where required | send if authorized | financial messages only | engagement messages only | draft only |

Actual rights depend on jurisdiction, organization policy, professional qualification, delegation and engagement scope.

## C.5 Multi-Party Gate Example

```text
Client confirmed facts and scope
+ Professional Review complete
+ payment condition satisfied
+ Filing Approval active
+ provider accepted instruction
≠ official filing completed
```

Each gate has its own actor, evidence and expiry.

## C.6 Delegation Requirements

Delegation should record:

- delegating and receiving actors;
- role and action delegated;
- scope and purpose;
- organization context;
- start and expiry;
- prohibited subdelegation;
- accepted or declined state;
- audit reference.

Delegation cannot create a qualification or client authority the recipient does not possess.

## C.7 Surface-Specific Exclusions

### Client surface should not expose by default

- internal margin;
- provider ranking notes;
- unrelated clients or rights;
- internal reviewer comments;
- unreviewed AI reasoning;
- credential and connector details.

### Provider surface should not expose by default

- competing provider quotes;
- organization-wide portfolio data;
- unrelated Matter history;
- internal margin;
- personal Lite notes;
- unrestricted private Knowledge.

### Finance surface should not require

- unrelated legal evidence;
- full dispute strategy;
- provider conflicts beyond commercial necessity;
- confidential client material unrelated to payment.

## C.8 Completion Work

PF-04 must:

1. reconcile all role names and action verbs across CH05, CH24–CH26 and CH43–CH44;
2. assign conformance scenarios to each high-risk permission boundary;
3. verify that client, provider and finance views are purpose-limited;
4. map delegation, expiry and role-switch behavior;
5. test that one actor holding several roles still produces separate decision records.

This appendix becomes publication-ready only after the user-surface and scenario contract is extended through CH47.