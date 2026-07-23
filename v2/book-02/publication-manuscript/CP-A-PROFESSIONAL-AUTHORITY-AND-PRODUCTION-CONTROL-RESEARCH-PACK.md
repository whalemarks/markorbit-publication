# CP-A — Professional Authority and Production Control Research Pack

## 1. Research purpose

This pack examines whether the v2 distinctions among Capability Evidence, Certification, Professional Qualification, Production Authorization, task-specific Eligibility, Assignment and Professional Authority can be represented through the frozen `B02-BASELINE-V0.1` contracts or require one or more formal Book 02 Change Proposals.

This is pre-proposal research. It does not add a Core Object, controlled value, lifecycle, public export or implementation task.

## 2. Constitutional problem

Professional systems routinely collapse several different questions:

```text
Who is the actor?
What can the actor do?
What is the actor allowed to do?
What is contextually permitted now?
Has the actor been evaluated?
May the actor enter production?
Is the actor eligible for this exact work?
Has the actor been assigned?
Does the actor hold the required professional authority?
```

The frozen Book 02 baseline already separates several of these:

```text
Identity recognizes.
Capability describes possible action.
Permission authorizes a controlled action.
Policy evaluates contextual constraints.
Human Review records accountable review.
Task carries assignment and responsibility references.
Owning Services execute and mutate state.
```

The v2 manuscript adds a further authority chain:

```text
Capability Evidence
≠ Certification
≠ Professional Qualification
≠ Production Authorization
≠ Task-specific Eligibility
≠ Assignment
≠ Professional Authority
```

The research question is whether that chain is:

- an explanatory composition over existing frozen records;
- a set of profiles over existing Objects and Contracts;
- one or more new shared Core contracts;
- a change to the meaning of Permission, Policy, Task, Identity or Human Review.

## 3. Frozen source inventory

Primary frozen sources:

- `core-specs/objects/identity.md`;
- `core-specs/objects/permission.md`;
- `core-specs/objects/policy.md`;
- `core-specs/objects/task.md`;
- `core-specs/contracts/common/human-review.md`;
- `core-specs/contracts/common/references.md`;
- `core-specs/contracts/common/audit-context.md`;
- `core-specs/contracts/common/versioning.md`;
- `core-specs/contracts/common/errors.md`;
- AI governance and Agent contracts;
- Service Provider and Organization specifications;
- Evidence and Document specifications;
- Assignment Workflow Contract;
- Task and Workflow Contract Services;
- Permission and Policy Services.

Relevant v2 sources:

- CH13 — Capability Definition;
- CH14 — Skill, Tool, Service and Implementation Profiles;
- CH15 — Proficiency, M-mode and R-tier;
- CH16 — Certification, Qualification and Production Authorization;
- CH20 — Contextual Engagement Roles;
- CH22 — Assignment;
- CH23 — Contribution, Review and Outcome.

## 4. Frozen distinctions already available

### 4.1 Identity

Frozen Identity is a stable actor reference. It can represent a person, system, service, AI agent, external actor or organization actor.

It expressly does not mean Permission, Role, Capability, Agent, Service Provider or Customer.

```text
Identity recognizes.
Identity does not authorize.
Identity does not assign responsibility.
Identity does not execute work.
```

This is sufficient to identify the subject of a credential, certification, authorization or professional appointment. It is not sufficient to express the authority itself.

### 4.2 Capability

The frozen architecture places Capability before Permission and Policy. Capability describes available or possible action.

This supports the v2 rule:

```text
Capability
≠ permission
≠ assignment
≠ professional authority
```

Capability alone therefore cannot carry production or professional authority.

### 4.3 Permission

Frozen Permission authorizes a recognized subject to perform a defined action on a defined resource or scope.

Available frozen fields already include:

```text
subject type and subject ID
action
resource type and resource ID
scope type and scope reference
effect
status
organization context
policy reference
capability reference
source reference
audit metadata
```

The frozen scope types include Organization, Domain, Object, Service, Workflow, API, Product and DataAccess.

This can express many bounded production grants. It does not by itself express:

- a certification scheme;
- evidence basis and assessor;
- government or professional qualification;
- appointment to a Matter;
- conflict clearance;
- qualification verification status;
- a distinct authorization lifecycle tied to model or implementation version.

### 4.4 Policy

Frozen Policy evaluates contextual constraints and may return Allow, Deny, ReviewRequired, ApprovalRequired, AuditRequired or Escalate.

Its scope may include Product, Agent and Jurisdiction.

Policy can therefore evaluate:

- credential freshness;
- jurisdiction;
- conflict rules;
- data class;
- review requirements;
- model or implementation restrictions;
- suspension conditions;
- supervision requirements.

Policy does not issue a professional qualification and does not execute an action.

### 4.5 Human Review

Frozen Human Review records requirement, request, reviewer identity, scope, decision, target, source, governance references, timestamps and trace.

It does not:

- create legal or professional judgment by itself;
- grant Permission;
- execute downstream action;
- approve filings by itself;
- mutate domain state outside the Owning Service.

This can record an assessment or credential verification review. It cannot itself become the professional qualification or production authorization.

### 4.6 Task assignment fields

Frozen Task already contains:

```text
assignee type
assignee reference
responsibility reference
workflow reference
matter and order references
status
dependencies
due date
document, evidence and communication references
```

Frozen assignee types include User, Team, Agent, ServiceProvider, SystemActor and AIAgent.

Task assignment identifies who or what is assigned to actionable work. It does not prove qualification, general production authorization or professional authority.

### 4.7 Assignment Workflow

The frozen Assignment Workflow concerns trademark ownership-change preparation. It is not a generic worker Assignment contract.

It expressly states that it does not:

- certify authority;
- approve signatures;
- approve ownership transfer;
- execute payment;
- send communications;
- create active Tasks outside Task Service;
- mutate official ownership state by itself.

This workflow cannot be reused as evidence that a generic cross-domain Assignment Object already exists.

## 5. Candidate concept analysis

### 5.1 Capability Evidence

Nearest frozen contracts:

- Evidence;
- Document;
- Event;
- Human Review;
- Capability reference;
- Audit and Versioning.

Likely disposition:

```text
F1 composition or F2 Evidence profile
```

A Capability Evidence profile could include:

```text
subject reference
Capability reference
scenario or Work reference
observed result
review reference
evaluator reference
version context
scope and limitations
observed date
expiry or recency rule
```

A new root Object is not yet justified.

### 5.2 Capability Certification

Nearest frozen contracts:

- Identity;
- Evidence;
- Human Review;
- Permission;
- Policy;
- Capability;
- Versioning;
- Events.

Missing frozen semantics:

- certification scheme identity and version;
- issuer or assessor authority;
- issue and expiry dates;
- suspension, revocation and supersession lifecycle;
- explicit distinction between certification and legal qualification;
- evidence bundle accepted for certification.

Preliminary disposition:

```text
F3 candidate shared contract
```

Before proposing a root Object, test an Evidence-backed credential profile.

### 5.3 Professional Qualification

Nearest frozen contracts:

- Identity;
- Document;
- Evidence;
- Organization or external authority reference;
- Human Review;
- Versioning;
- Policy.

Professional Qualification is externally granted. Core may represent it but must not issue it.

Required boundaries:

```text
credential record
≠ credential verification
≠ credential current
≠ appointment
≠ authority for a Matter
```

Preliminary disposition:

```text
F2 credential profile or F3 external-qualification reference contract
```

Legal and professional review is mandatory before defining controlled meanings.

### 5.4 Production Authorization

Nearest frozen contracts:

- Permission;
- Policy;
- Capability;
- Identity;
- Human Review;
- Versioning;
- Agent governance;
- Evidence.

Most proposed Production Authorization fields can be represented as a scoped Permission plus Policy references:

```text
subject
allowed action or Capability
Product / Workflow / Service / Data scope
organization context
allow, deny or review effect
status
source
version and audit context
```

Fields that do not map cleanly include:

- allowed Work Package classes;
- M-mode and R-tier;
- Tool access ceiling as a first-class authorization dimension;
- supervision model;
- model/rule/service version binding;
- independent suspension and revocation consequences for active Assignments.

Preliminary disposition:

```text
F2 specialized Permission profile first
F4 only if frozen Permission semantics must change
```

A separate root Object should not be proposed until the profile option fails.

### 5.5 Task-specific Eligibility

Nearest frozen contracts:

- Permission decision;
- Policy decision;
- Identity;
- Capability reference;
- Task;
- Human Review;
- Evidence;
- Book 03 runtime context.

Eligibility is a time-bound decision, not necessarily a durable Object.

Possible shape:

```text
subject reference
target Task or future Work Package reference
Permission decision reference
Policy decision reference
credential and evidence references
conflict and capacity result
review requirement
valid-until time
reason codes
```

Preliminary disposition:

```text
F1 decision composition or F2 Book 03 execution profile
```

The v2 chapter correctly places runtime Eligibility in Book 03.

### 5.6 Assignment

Assignment to exact work is already partially expressible through Task assignee and responsibility fields, Permission, Policy and Human Review.

A separate Assignment record becomes necessary only if the system must preserve a lifecycle such as:

```text
offered
accepted
declined
expired
suspended
revoked
completed
```

and if that lifecycle must survive Task reassignment, multi-contributor work, compensation or cross-Workplace handoff.

Preliminary disposition:

```text
F2 Task-assignment profile or F3 new contract
```

This question is resolved in CP-B rather than CP-A.

### 5.7 Professional Authority

Nearest frozen contracts:

- Identity;
- Organization;
- Permission;
- Policy;
- Human Review;
- Evidence;
- external authority reference;
- Matter and Task references;
- Service Provider and Customer context.

Professional Authority may require:

```text
qualification current
jurisdiction
conflict clearance
customer or organization appointment
Provider acceptance
exact Matter scope
authority to advise, sign, submit or represent
```

No single frozen contract currently expresses the complete externally grounded authority chain.

Preliminary disposition:

```text
F3 / F4 candidate
```

It may need a shared reference contract, but Core must not create the underlying legal authority.

## 6. Rejected alternatives

### Alternative A — Treat Certification as Permission

Rejected because Permission answers whether a subject may perform an action, while Certification records achievement against a standard. Their issuer, evidence, lifecycle and legal effect differ.

### Alternative B — Treat Qualification as Identity verification level

Rejected because frozen `verification_level` concerns identity recognition, not professional licensing, appointment, jurisdiction or reserved rights.

### Alternative C — Treat Human Review completion as professional authority

Rejected because the frozen Human Review Contract expressly does not create professional judgment or downstream action authority by itself.

### Alternative D — Treat Task assignment as general production authorization

Rejected because Task assignment is specific work allocation. It does not establish general production scope, qualification or authority beyond the Task.

### Alternative E — Create one universal Authority Object

Rejected at this stage because it would collapse Permission, Policy, Certification, Qualification, Assignment and Professional Authority into one ambiguous lifecycle.

## 7. Proposed boundary model

The research-supported model is:

```text
Identity
→ identifies the subject

Capability + Evidence
→ describe and support observed ability

Certification profile
→ records achievement against a scheme

Qualification reference
→ represents externally granted credential

Permission profile
→ represents bounded Production Authorization

Policy decision
→ evaluates current constraints

Eligibility result
→ decides suitability for exact work at runtime

Assignment
→ binds the subject to exact work

Professional Authority reference
→ records externally grounded authority for reserved action
```

## 8. Authority ceiling rules

1. Core may represent an external credential but cannot issue it.
2. A platform Certification cannot imply government licence or professional registration.
3. Production Authorization cannot imply Assignment.
4. Assignment cannot imply professional authority.
5. Human Review cannot execute or authorize downstream action by itself.
6. AI and deterministic implementations may receive bounded production permission but cannot hold legal professional qualification.
7. Permission and Policy decisions must be re-evaluated when qualification, scope, version or context changes.
8. Suspension must not erase historical Evidence or accepted work.
9. Owning Services remain responsible for state mutation.
10. Book 03 remains responsible for runtime Eligibility and execution enforcement.

## 9. Required legal and professional review questions

- Which jurisdictions distinguish lawyer, trademark attorney, trademark agent, representative and filing intermediary?
- Which credentials may be verified from public registries?
- What data may be stored about disciplinary status, suspension or restrictions?
- Does representing appointment or authority create evidentiary reliance?
- Which records require source timestamp, expiry and re-verification?
- Which actions are reserved professional acts?
- Can an organization appoint a professional independently of the customer?
- How should conflict clearance be represented without exposing privileged information?
- Which authority records may be shared across Workplaces?
- What disclaimers are required for platform-issued Certification?

## 10. Recommendation

```text
Capability Evidence: F1/F2, no Change Proposal yet
Capability Certification: prepare F3 proposal research
Professional Qualification: prepare controlled external-reference profile
Production Authorization: test F2 Permission profile before F4
Eligibility: Book 03 decision profile, not durable Core Object by default
Assignment: defer final object decision to CP-B
Professional Authority: prepare narrow F3/F4 proposal research with legal review
```

No omnibus Authority Object should be opened.

The next formal proposal work should be split into:

```text
CP-A1 — External Professional Qualification and Authority Reference
CP-A2 — Capability Certification Profile
CP-A3 — Production Authorization as Permission Profile
```

Only CP-A1 is currently likely to require a new shared semantic contract. CP-A2 and CP-A3 must first prove that frozen Evidence, Human Review, Permission and Policy composition is insufficient.

## 11. Research verdict

```text
Frozen authority boundaries mapped: YES
Identity sufficient as authority subject: YES
Permission sufficient for all proposed semantics: NO
Policy sufficient for context evaluation: YES
Human Review sufficient as authority grant: NO
Professional Qualification may be platform-issued: NO
Production Authorization should first be a Permission profile: YES
Professional Authority requires further F3/F4 analysis: YES
Immediate Core change authorized: NO
```