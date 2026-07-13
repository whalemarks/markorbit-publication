# B04-CH-08 — People, Roles, Permissions and Accountability

**Status:** Draft 1  
**Chapter Map:** B04-TOC-V0.1  
**Part:** Part II — Organization Context and Operating Environment

## Chapter Purpose

This chapter defines how people participate in an Organization Workplace and how that participation becomes governed through organizational relationships, roles, permissions, responsibility, review authority, delegation, and accountability.

Chapter 07 established that the organization is the real professional and commercial actor, Workplace is its governed operating representation, and Workplace Context is the authorized frame within which current work is interpreted.

That context remains incomplete until the system can answer:

```text
Which person is participating?

Why may that person act for this organization?

Which role and scope are active?

What may the person see, prepare, review, approve, or request?

Which responsibility has been assigned?

Who remains professionally and organizationally accountable?
```

The central proposition of this chapter is:

```text
Person
→ real human participant

User
→ system-access representation

Organization Relationship
→ why the person may participate in the Workplace

Role
→ how the person participates in a defined context

Permission
→ which action the recognized actor may perform
on which resource and within which scope

Policy
→ which contextual conditions constrain the action

Responsibility Assignment
→ who owns, performs, reviews, approves, or monitors the work

Accountability
→ who must answer for the professional or organizational outcome
```

These concepts are related.

They are not interchangeable.

This chapter does not create a second Identity, Permission, Policy, Business Responsibility, Human Review, or Execution model.

Book 02 remains authoritative for shared identity, permission, policy, and responsibility meaning.

Book 03 remains authoritative for review, approval, Workflow, Task, and protected-action coordination.

Book 04 explains how an independent organization consumes those foundations through Workplace without allowing organization charts, Product interfaces, informal practice, or AI assistance to redefine authority.

---

## 1. People Make the Organization Operational

An organization may have identity, clients, private knowledge, business rules, and Products.

People make those elements operational.

People interpret client needs, prepare work, make professional judgments, review outputs, approve commitments, select providers, monitor deadlines, and accept risk.

Workplace must therefore represent not only the organization but also the people who act for it.

Those people may include:

- organization owners and managers;
- trademark professionals and attorneys;
- sales, process, finance, and quality users;
- knowledge and content contributors;
- technical administrators;
- temporary team members;
- invited client participants;
- foreign associates and specialist providers;
- external reviewers, consultants, and auditors.

The same person may perform several functions.

Different people may perform the same function in different contexts.

A simple account list is therefore insufficient.

Workplace must preserve the relationship among:

```text
human identity
system access
organizational relationship
contextual role
permission
responsibility
professional authority
accountability
```

Without that relationship, the system may know who logged in but still fail to know whether the person is entitled, qualified, responsible, or authorized to act.

---

## 2. Person, User, and Organizational Relationship Are Distinct

A person exists outside MarkOrbit.

A User represents system participation.

An organizational relationship explains why the person may act within a particular Workplace.

```text
Person
≠
User
≠
Organization Relationship
```

One person may have:

- one User identity;
- several organization relationships;
- several Product access contexts;
- several roles;
- several delegated responsibilities;
- historical responsibility after current access ends.

A login establishes access to an account.

It does not establish:

- which organization the person is acting for;
- which role is active;
- which client may be accessed;
- which professional qualification applies;
- which approval authority exists;
- which protected action may proceed.

The minimum relationship is:

```text
Person Identity
        ↓
User Identity
        ↓
Organization Relationship
        ↓
Active Workplace Context
```

An organization relationship may arise from employment, ownership, partnership, client invitation, professional engagement, provider assignment, delegated review, or temporary collaboration.

It should be explicit where it affects access, confidentiality, responsibility, or audit.

The rule is:

```text
Authentication proves account access.

Organizational context establishes participation.

Neither alone establishes complete authority.
```

---

## 3. Participation Must Be Scoped and Purpose-Bound

A recognized identity should not receive Workplace participation merely because the person is known.

Participation requires a valid relationship, scope, and purpose.

```text
Recognized Identity
+
Active Organization Relationship
+
Defined Scope and Purpose
=
Eligible Workplace Participant
```

Eligibility does not automatically grant permission.

For example:

- an employee may be a member but have no finance authority;
- an external reviewer may review one Artifact but see no wider portfolio;
- a client contact may confirm one instruction but see no internal notes;
- a foreign associate may receive one assigned Task but have no access to provider evaluations;
- a former employee may remain in historical audit records but have no current access.

Participation should therefore preserve:

- organization;
- relationship type;
- scope and purpose;
- start and end;
- status;
- authority source;
- confidentiality conditions;
- revocation;
- historical trace.

The same person may participate in several Workplaces.

Authority in one Orbit must not carry automatically into another.

---

## 4. Teams and Organizational Units Provide Structure, Not Authority

Professional organizations operate through teams, offices, departments, practice groups, and temporary project groups.

Workplace may represent those structures because they help organize:

- Product access;
- work visibility;
- reviewer selection;
- client responsibility;
- service coverage;
- escalation;
- reporting;
- local knowledge.

But:

```text
Team membership
≠
permission
```

A filing-team member may not be qualified to approve legal strategy.

A finance-team member may not be permitted to approve refunds.

A management-team member may still be excluded from a restricted Matter.

Teams provide organizational context.

They may help assign roles or define scope.

They must not replace explicit permission, Policy, qualification, or responsibility.

Temporary groups should be purpose-bound, time-bound, auditable, and closed when the purpose ends.

---

## 5. Role Defines Contextual Participation

A Role describes how an identity participates in a defined context.

Illustrative roles may include:

```text
organization_owner
workplace_admin
account_owner
sales_user
matter_owner
matter_operator
filing_preparer
review_authority
finance_verifier
knowledge_reviewer
partner_coordinator
external_collaborator
client_participant
```

Book 04 does not establish one universal role enumeration.

A solo professional may combine several functions.

A large organization may separate them among teams.

The architectural requirement is stable meaning and governed mapping, not uniform titles.

A Role should answer:

```text
How does this actor participate?

For which organization, Product, client, Matter, or work type?

Which responsibility types may be assigned?

Which permission and Policy rules may be relevant?

Which review or escalation paths may include the actor?
```

Roles may be scoped to:

- organization;
- office or team;
- Product;
- client or portfolio;
- Matter;
- Workflow or Task;
- review;
- network collaboration;
- time period.

A role without scope creates authority ambiguity.

---

## 6. Role Is Not Job Title

A job title expresses an organizational or commercial position.

A Role expresses system and professional participation in context.

```text
Job title
≠
Role
```

A managing partner may not be the reviewer for every Matter.

A trademark attorney may not have access to every client.

An operations manager may manage people without holding legal-review authority.

An administrator may manage membership without authority to approve a filing.

Workplace may map titles or organization positions to role templates.

The mapping remains organization-specific and governed.

The system must avoid the shortcut:

```text
organizational seniority
=
unlimited system and professional authority
```

Seniority may influence authority.

It does not replace explicit scope, permission, qualification, or responsibility.

---

## 7. Permission Answers a Specific Authorization Question

Permission answers:

> May this recognized actor perform this action on this resource within this scope?

A minimum permission evaluation includes:

```text
Actor
+ Action
+ Resource
+ Organization
+ Scope
+ Context
```

Examples include:

- may this user read this Matter?
- may this user prepare this quotation?
- may this user assign this Task?
- may this reviewer access this Evidence?
- may this AI Agent use this knowledge source?
- may this external collaborator download this Document?
- may this finance user verify this payment?

Permission is not one broad status such as `staff`, `admin`, or `trusted`.

The same participant may be allowed to read and prepare, denied from approving, or required to request Human Review.

Authority should be no broader than the actor, action, resource, purpose, and scope require.

---

## 8. Role, Permission, Policy, Approval, and Responsibility Must Remain Separate

These concepts influence whether work may proceed, but they answer different questions.

```text
Role:
How does the actor participate?

Permission:
May the actor perform this action?

Policy:
Is the action contextually allowed now,
and under which conditions?

Approval:
Has an authorized human accepted
this defined subject, scope, and version?

Responsibility:
Who owns, performs, reviews, monitors,
or must answer for the work?
```

A Role may help identify relevant permissions.

It does not guarantee permission.

Permission may allow preparation while Policy requires review or blocks external sharing.

Approval may be required even when permission is allowed.

Responsibility assignment does not grant permission automatically.

Workplace consumes all five.

It must not collapse them into one role label or Product setting.

---

## 9. Product Access Is Not Resource or Professional Authority

An organization may enable Lite, MarkReg, MGSN interfaces, or organization-specific applications.

A user may be entitled to open a Product.

That does not mean the user may access every record or perform every action within it.

```text
Product entitlement
≠
resource permission
≠
professional authority
```

A MarkReg user may see only assigned Matters.

A Lite user may receive a recommendation but lack authority to create a formal Opportunity.

An MGSN user may compare provider candidates but lack authority to appoint or instruct one.

A Workplace administrator may manage Product seats but remain excluded from confidential Evidence.

Products should request and consume permission decisions rather than infer authority from navigation, subscription tier, team membership, possession of a URL, or presence of a button.

```text
Visible in the interface
≠
authorized in the system
```

---

## 10. Access, Preparation, Review, Approval, and Execution Are Different Authorities

Professional systems often collapse several actions into a generic `can manage` permission.

MarkOrbit must distinguish:

```text
Access
Preparation
Review
Approval
Execution
Formal Mutation
Accountability
```

Access determines whether information may be viewed.

Preparation determines whether a draft, recommendation, request, or Artifact may be created.

Review determines whether a human may conduct accountable examination within a defined scope.

Approval permits a defined downstream request to be considered.

Execution coordinates the operational step.

Formal mutation belongs to the relevant Owning Service.

Accountability identifies who must answer for the professional or business outcome.

These authorities may belong to different actors.

```text
Process user
→ prepares

Qualified reviewer
→ reviews

Authorized human
→ approves where required

Execution
→ coordinates

Owning Service
→ records the formal fact

Responsible professional and organization
→ remain accountable
```

A Product may present all stages.

It must not make them semantically identical.

---

## 11. Professional Qualification Does Not Arise from Configuration

Some authority exists outside MarkOrbit.

It may depend on legal qualification, professional license, jurisdictional admission, employment authority, client engagement, power of attorney, internal delegation, or contractual appointment.

Workplace may record and verify representations of those facts.

It does not create them by assigning a role.

```text
Role assignment
≠
professional qualification
```

and:

```text
Permission
≠
external legal authority
```

Assigning `review_authority` does not make an unqualified person a licensed professional.

Assigning `filing_user` does not create authority to represent a client before an office.

Assigning `organization_owner` does not prove legal ownership.

Workplace should preserve the difference among:

```text
claim
evidence
verification
role
permission
professional authority
```

Where risk matters, reviewer or action eligibility may depend on verified qualification, jurisdiction, restriction, and expiry.

---

## 12. Responsibility Makes Organizational Work Explicit

Permission answers whether an action may be performed.

Responsibility answers who owns or must perform the work.

Professional service operations may require:

- customer ownership;
- Opportunity ownership;
- Order or Matter ownership;
- execution responsibility;
- Task assignment;
- review and approval responsibility;
- Communication and deadline responsibility;
- escalation responsibility;
- external-provider responsibility;
- AI-output review responsibility;
- audit responsibility.

These responsibilities should not remain hidden in memory or informal messages.

A responsibility assignment should identify, where relevant:

- responsible identity or organization;
- responsibility type;
- related object or work;
- scope;
- source of assignment;
- status and time;
- delegation or escalation path;
- acceptance where required;
- audit reference.

A sales user may own the client while a process user executes the Matter.

A reviewer may examine an output without owning its preparation.

An external associate may perform a filing step while the instructing organization retains responsibility for client advice and provider selection.

Workplace should make those distinctions visible without redefining Core responsibility semantics.

---

## 13. Accountability Is Not the Same as Assignment

Assignment identifies who is expected to perform or own a defined responsibility.

Accountability identifies who must answer for the outcome.

```text
Work may be delegated.

Final accountability may remain.
```

A Matter owner may delegate document preparation while remaining accountable for the Matter.

An organization may instruct a foreign associate while remaining accountable to its own client for the engagement it controls.

An AI Agent may prepare a draft while an authorized human remains accountable for professional use.

Accountability may exist at individual, managerial, organization, external-provider, service, and audit levels.

The architecture should identify, for consequential work:

```text
performing actor
+
reviewing or authorizing actor where required
+
authoritative Owning Service
+
accountable professional or organization
```

Assignment must not imply that final accountability has transferred.

Accountability must not erase who actually performed the work.

---

## 14. Delegation and Responsibility Transfer Are Distinct

Delegation assigns work or a bounded responsibility to another actor while original accountability may remain.

Responsibility transfer moves a defined responsibility from one owner, stage, or context to another.

```text
Delegation
→ another actor performs within assigned scope

Transfer
→ the responsible owner or stage changes
```

Examples of delegation include document preparation, initial checks, deadline monitoring, or translation review.

Examples of transfer include sales owner to Matter owner, internal team to external provider, or departing employee to replacement owner.

Both should preserve:

- source and target actors;
- scope;
- authority source;
- effective time;
- acceptance where relevant;
- conditions;
- audit;
- revocation or correction;
- effect on final accountability.

Delegation must not silently expand permission.

Transfer must not silently erase history.

---

## 15. Review Authority Is Organizational Eligibility, Not the Review Lifecycle

Workplace must help determine who may serve as a reviewer.

It does not own the review lifecycle.

CH08 answers:

```text
Who is eligible and authorized
to review this class of work
for this organization and scope?
```

CH19 and Book 03 answer:

```text
How does a specific review request,
decision, approval, and Owning Service handoff proceed?
```

Reviewer eligibility may depend on:

- verified identity;
- active organization relationship;
- role and permission;
- professional qualification;
- jurisdiction and work type;
- client restrictions;
- Policy and risk;
- independence and conflict status;
- delegation and time.

Being assigned a Task does not make a person an authorized reviewer.

Being an administrator does not create professional review authority.

AI is not a Human Reviewer.

Workplace may maintain reviewer eligibility, preferred reviewers, availability, and escalation paths.

Execution coordinates the particular review and preserves subject, scope, version, decision, and downstream reliance.

---

## 16. Separation of Duties and Contextual Restrictions

Some actions should not be performed and approved by the same actor.

Examples may include:

```text
preparer ≠ reviewer

payment requester ≠ payment verifier

high-value quote preparer ≠ discount approver

provider recommender ≠ final selector where Policy requires independence

AI output requester ≠ sole high-risk professional reviewer
```

The required separation may depend on risk, client policy, organization policy, professional rules, financial threshold, or conflict concerns.

A solo professional may necessarily combine functions.

In that case, the architecture should make the combined responsibility visible rather than pretending separation exists.

A person may also be generally permitted but restricted in a particular context because of conflict of interest, prior representation, confidentiality, client instruction, commercial interest, jurisdiction limitation, or information barrier.

```text
General permission
≠
contextual eligibility
```

Policy may deny, require disclosure, change reviewer, block sharing, or escalate.

Overrides should preserve reason, authority, scope, risk, time, and audit.

---

## 17. External Collaborators and Client Participants Need Limited Context

Workplace may include foreign associates, specialist counsel, translators, evidence providers, consultants, auditors, and client participants.

They should not receive the organization’s full Workplace merely because collaboration exists.

A useful external-participation model is:

```text
External Identity
+
Verified Relationship
+
Defined Purpose
+
Scoped Role and Permission
+
Time Limit
+
Confidentiality and Policy
=
Authorized External Participation
```

External access should identify:

- sponsoring organization or user;
- related client, Matter, Task, or Artifact;
- visible information;
- permitted and prohibited actions;
- expiry;
- download or export restrictions;
- review or acceptance obligations;
- offboarding and audit.

MGSN discovery or provider selection does not automatically grant Workplace access.

Provider appointment, responsibility assignment, access grant, and protected instruction remain separate steps.

Client participation should also remain distinct from internal membership.

A client may provide facts, upload Documents, confirm instructions, approve fees, or receive selected status views.

The client should not automatically see private margins, internal risk notes, provider criticism, unrelated clients, or unrestricted organizational memory.

```text
Client instruction
≠
internal review
≠
professional approval
≠
formal execution
```

---

## 18. AI Agents, System Actors, and Administrators Have Bounded Authority

AI Agents and external systems must not be treated as human team members merely because they appear in the same interface.

They require recognized identity, purpose, contract, allowed Capabilities, data scope, permission, Policy, risk, review requirement, and audit.

AI may summarize, extract, compare, draft, recommend, and prepare.

It must not grant itself permission, impersonate a human, infer approval from silence, appoint providers, send protected Communications, submit filings, approve payments, or record official outcomes.

```text
AI Agent assignment
≠
human responsibility transfer
```

A requesting user, responsible domain, reviewer, and accountable organization remain identifiable.

Administrator authority must also remain bounded.

```text
Workplace administrator
≠
professional reviewer
≠
finance approver
≠
client owner
≠
Matter owner
```

Emergency access, where required, should be exceptional, purpose-limited, time-limited, strongly authenticated, and fully audited.

Technical administration must not substitute for professional approval or rewrite who made a decision.

---

## 19. Participation and Authority Must Have Lifecycle

People join, change roles, move teams, lose qualification, become unavailable, or leave.

External relationships begin and end.

Delegations expire.

Permissions change.

A conceptual participation lifecycle may include:

```text
Invited
→ Pending
→ Active
→ Limited
→ Suspended
→ Ended
→ Archived
```

Offboarding is not merely account deletion.

The organization must address:

- open Tasks and Matters;
- pending reviews and approvals;
- client and deadline ownership;
- delegated authority;
- Product and local-device access;
- shared links and external collaboration;
- reassignment and audit continuity.

Historical identity references must remain available for explainability.

Ending access must not erase prior responsibility.

Current authority governs current action.

Historical authority explains historical action.

A later role change must not rewrite the context under which an earlier decision occurred, and an expired permission must not continue to authorize future action.

---

## 20. The Minimum People and Authority Model

A minimum conceptual model can be expressed as:

```text
Person / Human Identity
        │
        ├── User Identity
        ├── Professional Claims and Evidence
        └── Contact Points
                │
                ▼
Organization Relationship
        │
        ├── membership or external relationship
        ├── team or organizational unit
        ├── scope and purpose
        └── lifecycle
                │
                ▼
Role Assignment
        │
        ├── organization scope
        ├── Product scope
        ├── client or Matter scope
        ├── review scope
        └── time scope
                │
                ▼
Permission and Policy Context
        │
        ├── actor
        ├── action
        ├── resource
        ├── organization
        ├── purpose
        └── conditions
                │
                ▼
Responsibility Context
        │
        ├── ownership
        ├── execution
        ├── review and approval
        ├── delegation and escalation
        └── accountability
                │
                ▼
Authorized Workplace Participation
```

For consequential work:

```text
Authorized Participant
→ Product or Workplace surface
→ preparation or request
→ governed Execution
→ Human Review and approval where required
→ Owning Service
→ Event, audit, and outcome
```

This is an authority model, not a database, IAM, or service-topology design.

---

## 21. Required Distinctions

This chapter establishes the following required distinctions:

```text
Person ≠ User

Identity ≠ organization relationship

Membership ≠ permission

Team ≠ authority

Job title ≠ Role

Role ≠ Permission

Permission ≠ Policy

Permission ≠ Approval

Assignment ≠ Permission

Product access ≠ resource access

Administrative authority ≠ professional authority

Professional claim ≠ verified qualification

Delegation ≠ responsibility transfer

Review authority ≠ review decision

Client confirmation ≠ professional approval

AI assignment ≠ human accountability

Current authority ≠ historical authority
```

These distinctions prevent Product convenience or organizational habit from becoming hidden system authority.

---

## 22. Failure Modes This Chapter Prevents

### Role inflation

A broad role such as `admin` silently grants professional, financial, and client authority.

### Permission by interface

A visible button or page is treated as proof of authorization.

### Membership overreach

Every team member receives access to all clients and private knowledge.

### Product-defined authority

Different Products invent incompatible role, review, and approval meanings.

### Qualification by configuration

A system role is treated as proof of professional qualification.

### Informal review

A chat message is treated as a complete, scoped, version-bound review.

### Delegation without trace

Work is passed to another actor without preserving scope, authority, or accountability.

### External-collaborator leakage

A provider or client receives broad Workplace access for a limited purpose.

### AI impersonation

An AI Agent appears as reviewer, approver, or responsible professional.

### Offboarding failure

Access ends while Matters, deadlines, reviews, and client responsibilities remain unassigned.

These failures may occur even when authentication is technically secure.

The issue is not only security.

It is organizational and professional authority.

---

## 23. Minimum Conformance Rule

A conforming Workplace should preserve the following rule:

```text
Every participant has a recognized identity
and a valid relationship to the active organization.

Roles are contextual and scoped.

Permissions evaluate actor, action, resource,
organization, and context.

Policy may further constrain an allowed action.

Responsibility, review authority, approval,
and accountability remain distinct.

Professional qualification is not created
by Product or administrator configuration.

External and client participation is
purpose-limited, time-aware, and auditable.

AI and system actors operate under separate
identity, permission, Policy, and review boundaries.

Execution coordinates consequential work.

Owning Services mutate formal business state.

Human professionals and organizations remain accountable.
```

Different Workplace editions may expose different levels of complexity.

A solo professional may occupy several roles.

A large organization may distribute them widely.

The authority distinctions must remain.

---

## 24. Chapter Boundary

This chapter defines how people, roles, permissions, responsibility, review eligibility, and accountability become organization context within Workplace.

It does not define:

- authentication or identity-provider architecture;
- passwords, SSO, MFA, or credential management;
- a universal role catalog;
- a complete RBAC or ABAC engine;
- database schemas;
- HR, payroll, or employment records;
- final organization-chart design;
- professional-license verification APIs;
- conflict-checking implementation;
- exact separation-of-duty matrices;
- Product screen permissions;
- Human Review lifecycle;
- approval-state transitions;
- Task or Workflow lifecycle;
- protected-action execution;
- formal business-state mutation.

Clients, relationships, services, and business rules belong to CH09.

Private knowledge, AI context, preferences, and organizational memory belong to CH10.

Work, review, Communication, and operating surfaces belong to CH11.

Data boundaries and synchronization belong to CH12.

The specific Human Review, approval, and Owning Service handoff model belongs to CH19 and Book 03.

This chapter does not modify Book 02 Identity, Permission, Policy, User, Organization, or Business Responsibility semantics.

It explains how Workplace consumes them in an independent organizational Orbit.

---

## 25. Chapter Conclusion

An organization cannot operate through identity alone.

It needs people whose participation, authority, responsibility, and accountability are explicit.

Workplace connects:

```text
Person
→ User
→ Organization Relationship
→ Role
→ Permission and Policy
→ Responsibility
→ Review and Approval Authority
→ Accountability
```

The organization remains the real professional and commercial actor.

People act for it under defined relationships and scopes.

Roles describe participation.

Permissions determine allowed actions.

Policies apply contextual constraints.

Responsibilities identify ownership and expected performance.

Delegation and transfer preserve continuity.

Review authority remains human, qualified, scoped, and distinct from a review decision.

Execution coordinates consequential work.

Owning Services change formal business facts.

AI and system actors assist under separate governance.

The architecture can therefore be summarized as:

```text
recognized identity
+
valid organization relationship
+
scoped role
+
explicit permission
+
applicable Policy
+
responsibility assignment
+
required human authority
=
authorized and accountable Workplace participation
```

A conforming Workplace must make participation understandable, limited, traceable, and revocable.

It must support organizations of different sizes without turning every difference into new Core semantics.

It must support Product simplicity without hiding authority.

It must support AI assistance without transferring professional responsibility.

It must support collaboration without exposing the whole Orbit.

Only with those distinctions can the organization safely move from identity and context into clients, relationships, private knowledge, operating work, and governed Execution.
