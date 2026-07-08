# Agent Specification Template

**Repository:** `book-02-core`  
**Directory:** `core-specs/agents/`  
**Template ID:** B02-TPL-AGENT  
**Template Type:** Agent Specification Template  
**Source Chapter:** B02-CH-26 — AI Capability and Agent Governance Specification  
**Source Appendix:** B02-APP-G — Agent Index  
**Source Index:** indexes/agent-index.md  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# How to Use This Template

Copy this template to the appropriate agent category directory.

Recommended locations:

```text
core-specs/agents/governance/{agent-name}.md
core-specs/agents/professional-assistance/{agent-name}.md
core-specs/agents/execution-assistance/{agent-name}.md
core-specs/agents/communication/{agent-name}.md
core-specs/agents/opportunity-routing/{agent-name}.md
core-specs/agents/codex/{agent-name}.md
core-specs/agents/spec-review/{agent-name}.md
core-specs/agents/system/{agent-name}.md
core-specs/agents/reserved/{agent-name}.md
```

Use lowercase kebab-case filenames.

Examples:

```text
ai-governance-agent.md
classification-assistant-agent.md
trademark-status-summary-agent.md
routing-assistant-agent.md
workflow-assistant-agent.md
codex-implementation-agent.md
spec-consistency-review-agent.md
office-action-assistant.md
```

This template is for governed Core Agents only.

Do not use this template for:

```text
prompts
model calls
chat sessions
product helpers without Agent Contract
uncontrolled automation scripts
unreviewed AI features
UI assistants without Core governance
database jobs without Core service boundary
```

A prompt is not an Agent.

A model call is not an Agent.

A chat session is not an Agent.

A product helper is not automatically an Agent.

---

# Agent Specification — {Agent Name}

**Spec ID:** B02-AGT-{AGENT-ID}  
**Spec Type:** Agent  
**Agent Name:** {Agent Name}  
**Agent Category:** Governance | Professional Assistance | Execution Assistance | Communication | Opportunity and Routing | Codex Implementation | Spec Review | External Professional | System  
**Agent Type:** AI Agent | System Agent | Codex Agent | External Professional Agent | Human Agent  
**Owning Domain/System:** {Domain or Cross-Cutting System}  
**Source Chapter:** B02-CH-26 — AI Capability and Agent Governance Specification  
**Source Appendix:** B02-APP-G — Agent Index  
**Source Index:** indexes/agent-index.md  
**Related Contract Spec:** core-specs/contracts/agent-contract.md  
**Related Object Specs:** core-specs/objects/ai-governance/{object}.md  
**Related Service Specs:** core-specs/services/ai-governance/{service}.md  
**Related Event Specs:** core-specs/events/ai-governance/{event}.md  
**Related API Specs:** core-specs/api/{api}.md  
**Related Workflow Specs:** core-specs/workflows/{workflow}.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase/Wave:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Wave 0–7  
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred  
**Risk Level:** Low | Medium | High | Critical  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Describe why this Agent exists.

The purpose should answer:

```text
What Core capability does this Agent assist or execute?
Why must this Agent be governed by Core?
Which objects, services, events, contracts, APIs or workflows depend on it?
Which products or systems may consume it?
```

Example format:

```text
The {Agent Name} assists with ...
It exists so that ...
It is required by ...
```

---

# 2. Agent Meaning

Define the canonical meaning of this Agent.

```text
{Agent Name} is a governed agent that ...
```

The meaning must be governance-first.

Do not define the Agent as:

```text
a prompt
a model call
a chat session
a UI helper
a script
a background job
an unbounded AI capability
```

Preferred definition pattern:

```text
This Agent performs or assists a defined Core capability under Agent Identity, Agent Contract, authorized knowledge, permission, policy, review and audit rules.
```

---

# 3. Agent Category

Select one canonical category.

```text
Governance Agent
Professional Assistance Agent
Execution Assistance Agent
Communication Agent
Opportunity and Routing Agent
Codex Implementation Agent
Spec Review Agent
External Professional Agent
System Agent
```

Explain why the category is correct.

```text
This Agent belongs to {Agent Category} because ...
```

---

# 4. Agent Type

Select one canonical type.

```text
AI Agent
System Agent
Codex Agent
External Professional Agent
Human Agent
```

Explain the type boundary.

```text
Agent Type: {Agent Type}
Reason:
    ...
```

If the agent is AI-assisted, all AI governance sections in this template are mandatory.

---

# 5. Owning Domain or System

State the primary owner.

```text
Owning Domain/System: {Domain or Cross-Cutting System}
Owner Type: Baseline Core Domain | Cross-Cutting Core Specification System | AI Governance | Codex Task System | Specification Governance
```

Ownership rules:

```text
- Every Agent must have one primary owner.
- Product ownership is not Core Agent ownership.
- Cross-cutting ownership must be explicit.
- AI Governance applies to all AI Agents.
```

Related domains or systems:

```text
- ...
- ...
```

---

# 6. Scope

Define what is inside this Agent.

```text
This Agent includes:
- ...
- ...
- ...
```

The scope should include allowed assistance, service access, object access, event access, knowledge use, review behavior and audit behavior.

It should not include unapproved professional decision-making, official filing, evidence alteration, external commitments or product UI behavior.

---

# 7. Agent Boundary

Define the Agent boundary.

## 7.1 In Boundary

```text
- ...
- ...
```

## 7.2 Out of Boundary

```text
- ...
- ...
```

## 7.3 Boundary Notes

Explain boundary-sensitive distinctions.

Examples:

```text
This Agent may recommend ...
This Agent may summarize ...
This Agent may draft ...
This Agent must not approve ...
This Agent must not submit ...
This Agent must not mutate Core Objects outside governed services.
```

---

# 8. Agent Identity

Define Agent Identity requirements.

```text
Agent Identity required: Yes
Agent Identity Object: AI Agent Identity | System Identity | Codex Agent Identity | External Professional Identity
Identity Spec: core-specs/objects/ai-governance/ai-agent-identity.md
```

Agent identity must include:

```text
agent_id
agent_name
agent_type
agent_category
agent_version
owning_domain_or_system
status
risk_level
contract_reference
created_at
updated_at
```

No Agent Identity, no agent.

---

# 9. Agent Contract

Define Agent Contract requirements.

```text
Agent Contract required: Yes
Agent Contract Spec: core-specs/contracts/agent/agent-contract.md
```

The Agent Contract must define:

```text
allowed capabilities
prohibited capabilities
authorized knowledge
allowed object access
allowed service access
allowed event access
allowed API access
input rules
output rules
risk level
human review rule
permission rule
policy rule
audit rule
failure behavior
product consumer boundary
workflow usage
```

No Agent Contract, no AI Core consumption.

---

# 10. Allowed Capabilities

List allowed capabilities.

Use this format:

| Capability | Meaning | Conditions | Notes |
|------------|---------|------------|-------|
| {Capability} | {Meaning} | {Conditions} | {Notes} |

Allowed capabilities may include:

```text
summarize
classify
recommend
draft
validate
compare
flag
route
extract metadata
check consistency
prepare review notes
suggest next task
```

Allowed capabilities must be specific.

Avoid broad language such as:

```text
do legal work
handle trademark cases
manage filings
make decisions
process everything
```

---

# 11. Prohibited Capabilities

List prohibited capabilities.

```text
This Agent must not:
- ...
- ...
```

Default prohibited capabilities:

```text
make final professional decisions without review
submit official filings
sign documents
send external communication without approval
alter evidence
invent legal authority
use unauthorized knowledge
bypass permission rules
bypass policy rules
bypass human review
bypass audit
mutate Core Objects outside governed services
change MVP scope
create Core domains, objects, services or events
```

Add agent-specific prohibited capabilities.

---

# 12. Authorized Knowledge

Define authorized knowledge sources.

Use this format:

| Knowledge Source | Source Type | Allowed Use | Required Citation | Notes |
|------------------|-------------|-------------|-------------------|-------|
| {Knowledge Source} | internal / official / reviewed / fixture / index / spec | {Allowed Use} | Yes / No | {Notes} |

Authorized knowledge may include:

```text
approved Knowledge Sources
approved Knowledge Assets
jurisdiction rules
classification references
document templates
matter context
trademark context
approved prior examples
Book 02 manuscript
Appendices A–H
indexes/
core-specs/
Codex task files
```

Unauthorized knowledge includes:

```text
unverified web content
unreviewed model memory
unapproved prompt-invented rules
unsupported legal authority
private data outside permission scope
```

No authorized knowledge, no professional answer.

---

# 13. Object Access

Define allowed object access.

Source:

```text
indexes/object-index.md
```

Use this format:

| Object | Access Type | Conditions | Notes |
|--------|-------------|------------|-------|
| {Object Name} | read / create / update / link / validate / recommend / audit-reference | {Conditions} | {Notes} |

Allowed access types:

```text
read
create-draft
recommend
validate
summarize
link-reference
audit-reference
review-reference
```

High-risk mutation must occur through governed services, not direct object mutation.

---

# 14. Service Access

Define allowed service access.

Source:

```text
indexes/service-index.md
```

Use this format:

| Service | Access Type | Conditions | Events Emitted |
|---------|-------------|------------|----------------|
| {Service Name} | invoke / recommend / validate / read-only | {Conditions} | {Events} |

Rules:

```text
- Agents must invoke services only when authorized by Agent Contract.
- Agents must not bypass permission or policy checks.
- Agents must not mutate Core state outside governed services.
- High-risk service output requires review.
```

---

# 15. Event Access

Define event access.

Source:

```text
indexes/event-index.md
```

Use this format:

| Event | Access Type | Source Service | Notes |
|-------|-------------|----------------|-------|
| {Event Name} | consume / cause-through-service / audit-reference | {Service Name} | {Notes} |

Rules:

```text
- AI Agents must not emit Core Events directly.
- Events must be emitted by governed services.
- AI-related events must preserve audit and review rules.
```

---

# 16. API Access

Define API access.

Source:

```text
indexes/api-index.md
```

Use this format:

| API | Access Level | Conditions | Notes |
|-----|--------------|------------|-------|
| {API Name} | No API / Internal API / Product API / Agent API / Admin API | {Conditions} | {Notes} |

Rules:

```text
- Agent API access requires Agent Contract authorization.
- Agent API access requires permission and policy checks.
- High-risk Agent APIs require review and audit.
- Reserved agents should use No API in MVP.
```

---

# 17. Inputs

Define Agent inputs.

Use this format:

| Input | Meaning | Required | Source | Notes |
|-------|---------|----------|--------|-------|
| actor_identity | Actor requesting agent use | Yes | Identity | Required for permission check |
| agent_identity | Agent executing the task | Yes | Agent Identity | Required |
| agent_contract | Contract governing execution | Yes | Agent Contract | Required |
| context_reference | Matter, Trademark, Order, Task or Spec context | Conditional | Core Object | Required when applicable |
| authorized_knowledge_reference | Approved knowledge source | Conditional | Knowledge | Required for professional output |
| correlation_id | Execution trace reference | Yes | Consumer | Required |

Add agent-specific inputs.

---

# 18. Outputs

Define Agent outputs.

Use this format:

| Output | Output Type | Status | Review Required | Notes |
|--------|-------------|--------|-----------------|-------|
| {Output Name} | draft / recommendation / summary / validation result / audit record | {Status} | Yes / No | {Notes} |

AI output statuses must use:

```text
Draft
Recommendation
ReviewRequired
ReviewApproved
ReviewRejected
Expired
Superseded
```

AI output is not professional truth unless review requirements are satisfied.

---

# 19. Risk Level

Define the Agent risk level.

```text
Risk Level: Low | Medium | High | Critical
```

Risk level meaning:

```text
Low
    summary or low-impact assistance

Medium
    workflow, communication, routing or internal recommendation support

High
    professional recommendation, classification, document, evidence, routing or client-facing content support

Critical
    official response, legal strategy, filing, binding commitment or high-liability decision support
```

Explain why this risk level applies.

```text
Risk rationale:
    ...
```

---

# 20. Human Review Rule

Define human review requirements.

```text
Human Review Required: Yes / No
Review Type: Professional Review | AI Governance Review | Workflow Review | Codex Review | None
Review Owner: ...
Review Object: Review Record | Approval Record | Responsibility Assignment
```

Review trigger:

```text
- ...
- ...
```

Blocking behavior:

```text
none
blocks external use
blocks state transition
blocks final output
blocks implementation acceptance
advisory only
```

No review rule, no high-risk output.

---

# 21. Audit Rule

Define audit requirements.

```text
Audit Required: Yes / No
Audit Object: AI Audit Record | Validation Report | Review Record | Event Audit Reference
```

Audit trigger:

```text
- Agent invoked
- Authorized knowledge used
- Recommendation generated
- Draft generated
- Review required
- Policy violation detected
- High-risk output produced
- Codex implementation produced
```

Audit content:

```text
agent ID
agent version
actor identity
input context reference
knowledge sources used
objects accessed
services invoked
API invoked
output reference
risk level
review requirement
review result
events emitted through services
timestamp
correlation ID
```

No audit, no governed AI execution.

---

# 22. Workflow Usage

Define workflow usage.

```text
Workflow role:
    none / task assistant / review assistant / routing assistant / state summary / next task suggestion / acceptance review / validation assistant
```

Relevant Workflow Contracts:

```text
- ...
```

Relevant Tasks:

```text
- ...
```

Workflow Events:

```text
- ...
```

Workflow rules:

```text
- Agent must not skip required review.
- Agent must not create unapproved workflow states.
- Agent must not complete professional tasks without governed service and responsibility record.
```

---

# 23. Failure Behavior

Define failure behavior.

Use this format:

| Failure Type | Result | Event Emitted | Audit Required | Review/Escalation | Retry Rule |
|--------------|--------|---------------|----------------|-------------------|------------|
| missing Agent Contract | block execution | AgentContractValidationFailed | Yes | Governance review | no retry until fixed |
| unauthorized knowledge | block output | AIUsagePolicyViolationDetected | Yes | Governance review | no retry until source approved |
| permission failure | deny access | PermissionCheckFailed | Yes | optional escalation | retry after permission change |
| policy violation | block or require review | AIUsagePolicyViolationDetected | Yes | required | depends on policy |
| review required | output held | AIReviewRequired | Yes | professional review | retry not applicable |
| invalid context | validation failure | EventValidationFailed | Optional | task owner review | retry after correction |

Add agent-specific failure types.

---

# 24. Product Consumers

Classify product consumers.

## 24.1 MVP Consumers

```text
- MarkReg
- MarkOrbit Lite
- Workplace
- AI Agents
- Codex Implementation
```

## 24.2 Partial Consumers

```text
- MGSN
- Opportunity Engine baseline
- Brand Asset Vault baseline
```

## 24.3 Future Consumers

```text
- Partner Center
- Client Portal
- Service Platform
- External Integrations
- Reporting Consumers
```

Only list consumers that actually consume this Agent.

Products may consume Agents.

Products must not redefine Agent authority.

---

# 25. MVP Scope

Define MVP scope for this Agent.

```text
MVP includes:
- ...
- ...
```

## 25.1 MVP Phase or Wave

```text
Phase/Wave: {Phase or Wave}
```

## 25.2 MVP Depth

```text
Depth: Must Implement | Partial Implement | Reserved Boundary | Deferred
```

## 25.3 MVP Acceptance Summary

```text
MVP acceptance requires:
- Agent Identity defined
- Agent Contract defined
- authorized knowledge rules defined
- object/service/event/API access rules defined
- review rule defined
- audit rule defined
- tests defined
```

---

# 26. Deferred Scope

Define what is explicitly deferred.

```text
Deferred:
- ...
- ...
```

Deferred scope must not be implemented by Codex unless a later approved task changes scope.

Reserved agents must not be production-enabled in MVP.

---

# 27. Data and Implementation Notes

Provide implementation-facing notes without defining prompt text or infrastructure code.

Allowed notes:

```text
Agent must have stable ID
Agent version must be recorded
Agent Contract must be validated before execution
Agent must include correlation ID
Agent must cite authorized knowledge when used
Agent output must have controlled status
High-risk output must be review-blocked
Audit must record object/service/API access
```

Prohibited notes:

```text
full prompt text as authority
model vendor-specific behavior
UI component design
controller implementation
database schema
unreviewed automation shortcut
```

---

# 28. Codex Implementation Notes

Define how Codex may implement this Agent.

Codex must:

```text
- cite this agent spec
- cite indexes/agent-index.md
- cite related contract, object, service, event and API specs
- preserve Agent Identity rules
- preserve Agent Contract rules
- preserve authorized knowledge rules
- preserve risk level
- preserve review and audit rules
- preserve MVP depth
- preserve deferred scope
- write tests
- follow prohibited-overreach rules
```

Codex must not:

```text
- implement prompt-only agents
- implement agents without Agent Contract
- implement agents without authorized knowledge rules
- allow agents to mutate Core state directly
- allow agents to bypass permission, policy, review or audit
- implement reserved agents as MVP production features
- allow Codex to define Core architecture
```

Related Codex Tasks:

```text
- B02-CX-W{wave}-{sequence} — {Task Title}
```

---

# 29. Validation Rules

This Agent Specification must pass the following checks.

```text
[ ] Agent name matches indexes/agent-index.md.
[ ] Agent category is defined.
[ ] Agent type is defined.
[ ] Owning domain or system is defined.
[ ] Agent Identity is required.
[ ] Agent Contract is required.
[ ] Allowed capabilities are defined.
[ ] Prohibited capabilities are defined.
[ ] Authorized knowledge is defined.
[ ] Object access is defined.
[ ] Service access is defined.
[ ] Event access is defined.
[ ] API access is defined.
[ ] Inputs are defined.
[ ] Outputs are defined.
[ ] Risk level is defined.
[ ] Human review rule is defined.
[ ] Audit rule is defined.
[ ] Workflow usage is defined or explicitly not required.
[ ] Failure behavior is defined.
[ ] Product consumers are classified.
[ ] MVP scope is defined.
[ ] Deferred scope is defined.
[ ] Codex implementation notes are included.
[ ] Prohibited overreach is defined.
```

---

# 30. Prohibited Overreach

This Agent spec must not be used to:

```text
treat prompts as agents
create AI agents without Agent Contract
create AI agents without audit
create AI agents without review rules
create AI agents without authorized knowledge
allow AI to finalize professional decisions
allow AI to submit official filings
allow AI to mutate Core Objects directly
allow AI to bypass permission or policy
allow Codex to define architecture
expose reserved agents as MVP external APIs
remove risk classifications
remove human review rules from high-risk agents
```

Add agent-specific prohibited overreach:

```text
- ...
- ...
```

---

# 31. Acceptance Criteria

This Agent Specification is accepted only if:

```text
[ ] It defines the Agent purpose.
[ ] It defines Agent meaning.
[ ] It identifies Agent category.
[ ] It identifies Agent type.
[ ] It identifies owning domain or system.
[ ] It defines scope.
[ ] It defines Agent boundary.
[ ] It defines Agent Identity requirements.
[ ] It defines Agent Contract requirements.
[ ] It defines allowed capabilities.
[ ] It defines prohibited capabilities.
[ ] It defines authorized knowledge.
[ ] It defines object access.
[ ] It defines service access.
[ ] It defines event access.
[ ] It defines API access.
[ ] It defines inputs.
[ ] It defines outputs.
[ ] It defines risk level.
[ ] It defines human review rule.
[ ] It defines audit rule.
[ ] It defines workflow usage.
[ ] It defines failure behavior.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes data and implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 32. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial agent specification created from B02-TPL-AGENT. |

---

**End of Agent Specification**
