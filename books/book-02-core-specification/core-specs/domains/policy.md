# Domain Specification — Policy

**Spec ID:** B02-DOM-POLICY  
**Spec Type:** Domain  
**Domain Name:** Policy  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/policy.md; core-specs/objects/policy-rule.md; core-specs/objects/policy-scope.md; core-specs/objects/policy-evaluation-context.md; core-specs/objects/policy-decision.md; core-specs/objects/policy-exception.md  
**Related Service Specs:** core-specs/services/policy-definition-service.md; core-specs/services/policy-evaluation-service.md; core-specs/services/policy-scope-validation-service.md; core-specs/services/policy-exception-review-service.md; core-specs/services/policy-audit-reference-service.md  
**Related Event Specs:** core-specs/events/policy-created.md; core-specs/events/policy-updated.md; core-specs/events/policy-enabled.md; core-specs/events/policy-disabled.md; core-specs/events/policy-evaluated.md; core-specs/events/policy-allowed.md; core-specs/events/policy-blocked.md; core-specs/events/policy-exception-requested.md; core-specs/events/policy-exception-approved.md; core-specs/events/policy-exception-rejected.md  
**Related Contract Specs:** core-specs/contracts/policy/policy-contract.md; core-specs/contracts/policy/policy-rule-contract.md; core-specs/contracts/policy/policy-evaluation-contract.md; core-specs/contracts/policy/policy-exception-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Policy Domain defines the Core meaning of contextual governance rules in MarkOrbit.

It exists so that permissions, services, APIs, workflows, AI Agents, reviews, approvals and Codex tasks can be constrained by rules that depend on context, risk, scope, status, responsibility or governance requirements.

Policy is required before:

```text
high-risk service execution
cross-organization access
AI output use
Agent capability enforcement
workflow transition gating
review-required decisions
approval-required decisions
external communication release
document exposure
classification recommendation use
Codex task acceptance
reserved-scope protection
prohibited-overreach enforcement
```

The Policy Domain is a Foundation Domain because authorization alone is not enough. Core execution must also evaluate contextual governance rules.

---

# 2. Core Meaning

Policy means:

```text
a governed Core rule or rule set that evaluates context and determines whether an action is allowed, blocked, requires review, requires approval, requires audit or must be escalated.
```

Policy is not merely:

```text
permission
role
user type
organization membership
legal advice
business pricing rule
product configuration
UI setting
hard-coded condition
database constraint
AI prompt instruction
informal operating habit
```

Policy answers:

```text
Under this context, should this action proceed?
Does this action require review?
Does this action require approval?
Does this action require audit?
Does this action violate a reserved boundary?
Does this action trigger prohibited-overreach rules?
Does this action require escalation?
```

---

# 3. Domain Category

Policy is a Foundation Domain.

Foundation Domains provide the minimum Core basis for:

```text
contextual governance
risk-based constraints
review gating
approval gating
AI safety
Agent boundary control
workflow safety
API exposure control
Codex implementation control
reserved-scope protection
audit readiness
```

Policy is a Foundation Domain, but its MVP depth is Partial Implement because the MVP needs a controlled policy boundary and basic evaluation, not a full dynamic policy engine.

---

# 4. Architectural Position

Policy sits after Permission and before governed execution.

```text
Identity recognizes the actor
        ↓
Organization provides operating context
        ↓
User represents the account
        ↓
Permission determines allowed action
        ↓
Policy evaluates contextual constraints
        ↓
Review / Approval may be required
        ↓
Service executes or blocks action
        ↓
Event and Audit preserve trace
```

Permission answers whether the actor may attempt the action.

Policy answers whether the action may proceed under the current context.

Policy does not replace Permission.

Policy does not replace Review or Approval.

Policy may require Review or Approval.

---

# 5. Scope

The Policy Domain includes:

```text
policy definition
policy rule boundary
policy status
policy scope
policy evaluation context
policy evaluation decision
policy exception boundary
policy review requirement
policy approval requirement
policy audit requirement
policy event emission
policy use by Services, APIs, Workflows, Agents and Codex tasks
```

MVP implementation should focus on:

```text
basic Policy
basic Policy Rule
Policy Scope
Policy Evaluation Context
Policy Decision
Policy Evaluation Service
Policy Scope Validation Service
PolicyBlocked event
PolicyAllowed event
PolicyExceptionRequested event
basic prohibited-overreach policy checks
```

MVP should not implement a full dynamic policy engine.

---

# 6. Boundary

## 6.1 In Boundary

The Policy Domain owns:

```text
Core policy meaning
policy definition
policy rule boundary
policy scope
policy evaluation context
policy decision values
policy exception boundary
policy review requirement flag
policy approval requirement flag
policy audit requirement flag
policy event emission
policy references used by Services, APIs, Workflows, Agents and Codex tasks
```

## 6.2 Out of Boundary

The Policy Domain does not own:

```text
identity recognition
organization membership
permission assignment
role management
business pricing strategy
customer grade strategy
legal judgment
professional opinion
review decision content
approval decision content
AI Agent capability definition
workflow state design
API endpoint design
physical database constraints
infrastructure security policy configuration
product UI settings
```

Those responsibilities belong to:

```text
Identity Domain
Organization Domain
Permission Domain
Business Responsibility system
Review and Approval system
AI Governance
Workflow Contract system
API specs
Product implementation
Infrastructure implementation
```

## 6.3 Boundary Notes

Permission determines authorization.

Policy evaluates context.

Review determines professional or governance acceptance.

Approval records a formal acceptance action.

Audit preserves the trace.

Policy may require review, approval or audit, but does not itself perform review, approval or audit.

---

# 7. Domain Rules

## 7.1 Policy Requires Context

Every policy evaluation must use a Policy Evaluation Context.

The context should include relevant references such as:

```text
actor identity
user
organization
permission result
target object
requested service
requested action
risk level
workflow state
AI Agent identity if applicable
MVP depth
reserved boundary status
review status
approval status
```

## 7.2 Policy Does Not Grant Permission

Policy cannot authorize an action when Permission denies it, unless a separately approved override mechanism exists.

MVP should not implement policy override that bypasses Permission.

## 7.3 Policy May Require Review or Approval

Policy decisions may include:

```text
Allowed
Blocked
ReviewRequired
ApprovalRequired
AuditRequired
EscalationRequired
ExceptionRequired
```

## 7.4 Policy Must Protect Reserved Scope

Policy must prevent reserved or deferred scope from being production-enabled as MVP.

This applies to:

```text
reserved domains
reserved workflows
future APIs
future agents
future product consumers
full marketplace scope
official filing automation
full opportunity scoring
external integration platform
```

## 7.5 Policy Must Be Auditable

Policy-sensitive actions must preserve audit trace.

Audit-sensitive policy actions include:

```text
policy creation
policy update
policy disablement
policy evaluation for high-risk action
policy block
policy exception request
policy exception approval
policy exception rejection
reserved-scope block
prohibited-overreach detection
AI governance policy decision
Codex task policy decision
```

## 7.6 Policy Must Be Product-Neutral

Products may consume Policy.

Products must not create product-local governance rules that bypass Core Policy for governed actions.

---

# 8. Primary Objects

The Policy Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Policy | Policy | Partial Implement | Core governance rule set applied to contextual execution. |
| Policy Rule | Policy | Partial Implement | Controlled rule inside a Policy. |
| Policy Scope | Policy / Organization / Permission | Must Implement | Scope within which a Policy applies. |
| Policy Evaluation Context | Policy | Must Implement | Context used to evaluate policy. |
| Policy Decision | Policy | Must Implement | Controlled result of policy evaluation. |
| Policy Exception | Policy / Review and Approval | Partial Implement | Governed exception to policy decision. |
| Policy Status | Policy | Partial Implement | Controlled status of Policy or Policy Rule. |
| Policy Audit Reference | Policy / Audit | Partial Implement | Audit reference for policy-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Identity Principal | Identity | Policy context references actor identity. |
| User | User | Policy context may reference user. |
| Organization | Organization | Policy scope may be organization-bound. |
| Permission Check Result | Permission | Policy may evaluate after permission check. |
| Review Record | Review and Approval | Policy may require review. |
| Approval Record | Review and Approval | Policy may require approval. |
| AI Agent | AI Governance | AI Agent actions are policy-sensitive. |
| AI Output | AI Governance | AI output use may be governed by policy. |
| Workflow Transition | Workflow Contract | Workflow transitions may require policy checks. |
| API Contract | API | API access may require policy checks. |
| Codex Task | Codex Governance | Codex tasks must pass policy/prohibited-overreach rules. |
| Audit Record | Audit | Audit records policy-sensitive actions. |

---

# 9. Primary Services

The Policy Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Policy Definition Service | Policy | Partial Implement | Create or update controlled Policy definitions. |
| Policy Evaluation Service | Policy | Must Implement | Evaluate Policy against context and return controlled decision. |
| Policy Scope Validation Service | Policy / Organization / Permission | Must Implement | Validate whether a Policy applies to the requested scope. |
| Policy Exception Request Service | Policy | Partial Implement | Request exception to a blocking or review-required decision. |
| Policy Exception Review Service | Policy / Review and Approval | Partial Implement | Review or approve policy exception. |
| Prohibited Overreach Check Service | Policy / Codex Governance | Must Implement | Detect prohibited Core scope or architecture overreach. |
| Policy Audit Reference Service | Policy / Audit | Partial Implement | Produce policy audit reference for governed actions. |

Service rules:

```text
- Mutating Policy services must emit events.
- Policy Evaluation Service must return controlled decision values.
- Policy services must not assign permissions.
- Policy services must not make professional review decisions.
- Policy exception handling must be review-sensitive.
- Prohibited-overreach checks must fail closed for Critical violations.
```

---

# 10. Primary Events

The Policy Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| PolicyCreated | Policy Definition Service | Partial Implement | A Core Policy has been created. |
| PolicyUpdated | Policy Definition Service | Partial Implement | Policy or Policy Rule has changed. |
| PolicyEnabled | Policy Definition Service | Partial Implement | Policy has been enabled for evaluation. |
| PolicyDisabled | Policy Definition Service | Partial Implement | Policy has been disabled from evaluation. |
| PolicyEvaluated | Policy Evaluation Service | Must Implement | Policy evaluation was performed. |
| PolicyAllowed | Policy Evaluation Service | Must Implement | Policy evaluation allowed the action. |
| PolicyBlocked | Policy Evaluation Service | Must Implement | Policy evaluation blocked the action. |
| PolicyReviewRequired | Policy Evaluation Service | Must Implement | Policy evaluation required review. |
| PolicyApprovalRequired | Policy Evaluation Service | Partial Implement | Policy evaluation required approval. |
| PolicyExceptionRequested | Policy Exception Request Service | Partial Implement | A policy exception was requested. |
| PolicyExceptionApproved | Policy Exception Review Service | Partial Implement | A policy exception was approved. |
| PolicyExceptionRejected | Policy Exception Review Service | Partial Implement | A policy exception was rejected. |
| ProhibitedOverreachDetected | Prohibited Overreach Check Service | Must Implement | Prohibited Core scope or architecture overreach was detected. |

Event rules:

```text
- Policy events must reference Policy Evaluation Context where applicable.
- PolicyBlocked and ProhibitedOverreachDetected must be auditable.
- Policy events must not expose protected resource content unnecessarily.
- Policy exception events must reference review or approval records where applicable.
```

---

# 11. Primary Contracts

Policy requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Policy Contract | Policy Contract | Partial Implement | Defines Policy fields, scope, status and rule references. |
| Policy Rule Contract | Policy Contract | Partial Implement | Defines controlled rule structure and evaluation boundary. |
| Policy Scope Contract | Policy / Permission Contract | Must Implement | Defines organization, resource, action, risk and applicability scope. |
| Policy Evaluation Contract | Policy Contract | Must Implement | Defines evaluation input, context, decision and output values. |
| Policy Exception Contract | Policy / Review Contract | Partial Implement | Defines exception request, review and approval requirements. |
| Prohibited Overreach Contract | Policy / Codex Contract | Must Implement | Defines overreach checks, severity and blocking behavior. |
| Policy Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for policy-sensitive actions. |

Contract rules:

```text
- Policy Evaluation Contract must use controlled decision values.
- Policy Contract must not define Permission assignment.
- Policy Exception Contract must require review for high-risk exceptions.
- Prohibited Overreach Contract must be reusable by Codex tasks and validation.
```

---

# 12. Relationships to Other Domains

## 12.1 Identity

Policy context references actor identity.

Identity does not define policy logic.

## 12.2 User

Policy may evaluate user status, user context or user responsibility.

User does not define policy logic.

## 12.3 Organization

Policy scope may be organization-bound.

Organization provides context and tenant boundary.

## 12.4 Permission

Permission determines whether an actor may attempt an action.

Policy evaluates contextual constraints after or alongside Permission.

Permission and Policy must remain separate.

## 12.5 Review and Approval

Policy may require Review or Approval.

Review and Approval systems perform and record the actual review or approval.

## 12.6 AI Governance

AI Agent actions and AI Output usage are policy-sensitive.

Policy does not define Agent capability, but may block or require review for Agent action.

## 12.7 API

API access may require policy evaluation.

API specs must reference Policy Evaluation where required.

## 12.8 Workflow Contract

Workflow transitions may require Policy Evaluation before state change.

Policy does not define workflow states.

## 12.9 Codex Governance

Codex tasks must pass Policy and prohibited-overreach checks.

Policy blocks Codex from implementing deferred or reserved scope as MVP.

## 12.10 Audit

Audit records should include policy-sensitive decision references.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Policy only under governed Agent Contracts.

Allowed AI use:

```text
explain policy requirements for a task or workflow if authorized
flag missing policy checks in specs or Codex tasks
identify possible reserved-scope violations
suggest that review or approval is required
summarize policy evaluation result if authorized
prepare policy exception notes for human review
```

AI must not:

```text
create Policy without authorized service
disable Policy without governed service
approve policy exception by itself
bypass Policy Evaluation Service
override Permission denial
turn prompt instructions into Core Policy
invent policy rules from general assumptions
silently downgrade policy severity
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Policy Object Access Rule
Policy Service Access Rule
Policy Event Access Rule
Permission Rule
Review Rule
Audit Rule
Human Review Rule for policy exceptions
```

---

# 14. Workflow Usage

Policy participates in workflows and gates execution.

Policy-sensitive workflows may include:

```text
policy-definition-review-workflow.md
policy-exception-review-workflow.md
prohibited-overreach-review-workflow.md
ai-output-policy-review-workflow.md
codex-task-policy-gate-workflow.md
reserved-scope-block-workflow.md
api-policy-authorization-workflow.md
```

Workflow rules:

```text
- Policy workflows must reference Workflow Contracts.
- Policy exceptions must be auditable.
- High-risk policy changes must require review.
- Prohibited-overreach findings must block Codex acceptance when Critical.
- Policy workflows must not assign permissions directly.
- Policy workflows must not perform professional review decisions themselves.
```

---

# 15. API Usage

Policy APIs expose policy evaluation and exception handling through governed services.

Potential MVP APIs:

```text
POST /policies/evaluate
POST /policies/scopes/validate
POST /policies/prohibited-overreach/check
```

Potential partial APIs:

```text
POST /policies
PATCH /policies/{id}
POST /policies/{id}/disable
POST /policies/exceptions
POST /policies/exceptions/{id}/review
```

API rules:

```text
- APIs must invoke Policy Services.
- APIs must preserve Identity, User, Organization and Permission context.
- APIs must not assign permissions.
- APIs must not approve policy exceptions without Review and Approval workflow.
- Mutating APIs must emit or cause service-level events.
- Policy APIs must not expose protected resource content unnecessarily.
```

API details belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

## 16.1 MVP Consumers

```text
Workplace
MarkReg
MarkOrbit Lite
AI Agents
Codex Implementation
Validation tools
```

## 16.2 Partial Consumers

```text
Partner Center
Client Portal
Service Platform
Reporting consumers
Admin consumers
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Advanced analytics
Risk engines
```

Product rule:

```text
Products consume Policy.
Products do not redefine Policy.
```

---

# 17. MVP Scope

Policy is a Phase 1 / Wave 1 Partial Implement domain.

MVP includes:

```text
Policy Scope
Policy Evaluation Context
Policy Decision
basic Policy Rule boundary
Policy Evaluation Service
Policy Scope Validation Service
Prohibited Overreach Check Service
PolicyEvaluated event
PolicyAllowed event
PolicyBlocked event
PolicyReviewRequired event
ProhibitedOverreachDetected event
basic policy metadata validation
source traceability to Permission, API, Agent, Workflow, Codex and Validation systems
```

MVP should support:

```text
basic service-level policy checks
basic API policy checks
basic workflow policy checks
basic AI Agent policy checks
basic Codex prohibited-overreach checks
reserved-scope blocking
review-required decisions
audit references for policy-sensitive actions
```

MVP does not require a full dynamic policy rule engine.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full dynamic policy engine
advanced rule authoring UI
complex policy inheritance
external policy provider integration
organization-custom policy marketplace
risk scoring policy automation
machine-learned policy recommendations
full policy simulation environment
fine-grained field-level policy
multi-jurisdiction legal policy automation
automatic policy exception approval
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Policy Decision should use controlled values.
Policy Evaluation Context should be reusable by Services, APIs, Workflows, Agents and Codex tasks.
Policy Scope should reference Organization, Permission and target object where applicable.
Prohibited-overreach checks should fail closed for Critical findings.
PolicyBlocked should not expose protected resource data.
Policy exception approval should require Review and Approval integration.
MVP Policy should be simple, explicit and deterministic.
```

Suggested Policy Status values:

```text
Draft
Active
Disabled
Superseded
Archived
```

MVP controlled Policy Status values:

```text
Active
Disabled
```

Suggested Policy Decision values:

```text
Allowed
Blocked
ReviewRequired
ApprovalRequired
AuditRequired
EscalationRequired
ExceptionRequired
NotApplicable
InvalidContext
```

MVP controlled Policy Decision values:

```text
Allowed
Blocked
ReviewRequired
InvalidContext
```

Suggested Policy Severity values:

```text
Info
Warning
Error
Critical
```

Do not treat informal prompts or UI settings as Core Policy.

---

# 20. Codex Implementation Notes

Codex may implement Policy only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Policy / Permission boundary
preserve Policy / Review and Approval boundary
preserve Policy / AI Governance boundary
implement only MVP scope unless task says otherwise
write tests for policy evaluation
write tests for policy blocked result
write tests for policy review-required result
write tests for prohibited-overreach detection
write tests preventing Policy from assigning Permission
write tests preventing deferred scope from becoming MVP
write tests preventing AI from approving policy exceptions
```

Codex must not:

```text
invent full policy engine in MVP
invent business pricing rules inside Policy
invent professional legal judgment inside Policy
create UI configuration as Core Policy
bypass Permission using Policy
auto-approve policy exceptions
downgrade Critical findings without review
allow product UI to mutate policy state directly
allow AI to create or disable policies without contract and review
```

---

# 21. Validation Rules

Policy Domain must pass the following checks.

```text
[ ] Policy is classified as Foundation Domain.
[ ] Policy is counted within the 26 baseline Core Domains.
[ ] Policy does not change the baseline Core Domain Map.
[ ] Policy has MVP Phase 1 / Wave 1 classification.
[ ] Policy has MVP Depth = Partial Implement.
[ ] Policy defines Core meaning.
[ ] Policy boundary excludes Permission assignment.
[ ] Policy boundary excludes Review and Approval decision content.
[ ] Policy boundary excludes business pricing and product UI settings.
[ ] Policy owns Policy Evaluation Context.
[ ] Policy defines Policy Decision.
[ ] Policy defines Policy Scope.
[ ] Policy lists primary services.
[ ] Mutating Policy services emit events.
[ ] Policy Evaluation Service returns controlled decision values.
[ ] Policy lists primary events.
[ ] Policy defines contract requirements.
[ ] Policy defines AI Agent usage constraints.
[ ] Policy defines workflow usage constraints.
[ ] Policy defines API usage constraints.
[ ] Policy defines product consumers.
[ ] Policy defines MVP and deferred scope.
[ ] Policy defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Policy into Permission
turn Policy into Role management
turn Policy into Review or Approval
turn Policy into legal judgment
turn Policy into business pricing strategy
turn Policy into product UI settings
turn Policy into hard-coded implementation convenience
allow Policy to override Permission denial in MVP
allow AI to approve policy exceptions
allow Codex to implement full dynamic policy engine in MVP
allow deferred scope to become MVP
allow product UI to mutate Policy state directly
allow Codex to define new policy architecture
```

---

# 23. Acceptance Criteria

This Policy Domain Specification is accepted only if:

```text
[ ] It defines Policy purpose.
[ ] It defines Policy Core meaning.
[ ] It identifies Policy as Foundation Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Identity, User, Organization, Permission, Review, AI Governance, API, Workflow, Codex Governance and Audit.
[ ] It defines AI Agent usage.
[ ] It defines workflow usage.
[ ] It defines API usage.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Policy Domain specification. Establishes Policy as Phase 1 Foundation Domain with Partial Implement depth, defines Policy Scope, Policy Evaluation Context, Policy Decision, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
