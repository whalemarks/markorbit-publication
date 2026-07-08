# core-specs/agents/

**Repository:** `book-02-core`  
**Directory:** `core-specs/agents/`  
**Document:** `core-specs/agents/README.md`  
**Book:** Book 02 — MarkOrbit Core Specification  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Directory Purpose

The `core-specs/agents/` directory contains detailed Agent Specification files for MarkOrbit Core.

An Agent is a governed actor that may perform or assist a defined capability under identity, permission, contract, context, review and audit rules.

This directory exists to define governed AI Agents, System Agents and Codex-related Agents in a way that can later be used by:

```text
contracts
services
events
APIs
workflows
objects
Codex tasks
validation scripts
audit systems
product consumers
```

The purpose of this directory is not to store prompts.

The purpose is to define the identity, authority, allowed capabilities, prohibited capabilities, authorized knowledge, object access, service access, event access, review rules, audit rules, API exposure and execution boundaries of Agents.

---

# 2. Canonical Agent Rule

Book 02 uses the following canonical rule:

```text
AI is a governed capability.
AI is not the Core.
AI is not above the Core.
AI is not a replacement for professional responsibility.
```

Therefore:

```text
No Agent Identity, no agent.
No Agent Contract, no AI Core consumption.
No authorized knowledge, no professional answer.
No review rule, no high-risk output.
No audit, no governed AI execution.
```

---

# 3. Agent Is Not Prompt

An Agent is not automatically:

```text
a prompt
a model call
a chat session
a product helper
a workflow note
a background job
a search query
a code generation request
a document template
```

A prompt may be used by an Agent.

A model call may be performed by an Agent.

A product helper may expose an Agent.

But none of these artifacts define the Agent.

A Core Agent requires:

```text
Agent Identity
Agent Contract
owning domain or system
allowed capabilities
prohibited capabilities
authorized knowledge
allowed object access
allowed service access
allowed event access
risk level
human review rule
audit rule
failure behavior
acceptance criteria
```

---

# 4. Directory Boundary

## 4.1 agents/ Owns

This directory owns:

```text
Agent Specification files
Agent Identity requirements
Agent Contract requirements
agent category
agent type
agent purpose
owning domain or system
allowed capabilities
prohibited capabilities
authorized knowledge rules
object access rules
service access rules
event access rules
API exposure rules
workflow usage rules
risk level
review requirement
audit requirement
failure behavior
MVP depth
deferred scope
acceptance criteria
```

## 4.2 agents/ Does Not Own

This directory does not own:

```text
Core architecture decisions
Domain meaning
Object meaning
Service implementation logic
Event semantics
API routing
workflow state machines
product UI
prompt libraries
model provider selection
training data policy
physical database schema
Codex implementation code
```

Those belong to other specification layers.

---

# 5. Source Chain

Every Agent Specification file must cite its source chain.

Required source chain:

```text
B02-CH-26 — AI Capability and Agent Governance Specification
B02-APP-G — Agent Index
indexes/agent-index.md
core-specs/agents/{agent-name}.md
codex-tasks/{task}.md
```

Related sources may include:

```text
indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/codex-task-index.md
B02-CH-16 — Core Execution Primitives
B02-CH-17 — Core Contract Architecture
B02-CH-24 — Service Specification
B02-CH-25 — Event Specification
B02-CH-27 — Core Consumption Specification
B02-CH-30 — MVP Execution Matrix
core-specs/contracts/
```

---

# 6. Required Agent Spec Groups

Agent Specification files should be grouped by responsibility.

Expected directory structure:

```text
core-specs/agents/README.md
core-specs/agents/_template.md

core-specs/agents/governance/
core-specs/agents/professional-assistance/
core-specs/agents/execution-assistance/
core-specs/agents/communication/
core-specs/agents/opportunity-routing/
core-specs/agents/codex/
core-specs/agents/spec-review/
core-specs/agents/system/
core-specs/agents/reserved/
```

Each subdirectory should contain agent specs for the corresponding category.

---

# 7. Agent Categories

This directory uses the following agent categories.

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

A spec must use one canonical category.

---

# 8. Agent Types

Agent types may include:

```text
AI Agent
System Agent
Codex Agent
External Professional Agent
Human Agent Reference
Validation Agent
```

This directory primarily specifies:

```text
AI Agent
System Agent
Codex Agent
Validation Agent
```

External Professional Agent meaning is primarily handled through:

```text
Agent domain
Service Provider domain
Routing domain
Communication domain
Service Network domain
```

---

# 9. Agent Spec Metadata

Each Agent Specification file must begin with metadata.

```text
# Agent Specification — {Agent Name}

**Spec ID:** B02-AGT-{AGENT-ID}
**Spec Type:** Agent
**Agent Name:** {Agent Name}
**Agent Category:** Governance | Professional Assistance | Execution Assistance | Communication | Opportunity and Routing | Codex Implementation | Spec Review | External Professional | System
**Agent Type:** AI Agent | System Agent | Codex Agent | Validation Agent | External Professional Agent | Human Agent Reference
**Owning Domain/System:** {Domain or System}
**Source Chapter:** B02-CH-26 — AI Capability and Agent Governance Specification
**Source Appendix:** B02-APP-G — Agent Index
**Source Index:** indexes/agent-index.md
**Related Object Specs:** core-specs/objects/{object}.md
**Related Service Specs:** core-specs/services/{service}.md
**Related Event Specs:** core-specs/events/{event}.md
**Related Contract Specs:** core-specs/contracts/{contract}.md
**Related API Specs:** core-specs/api/{api}.md
**Status:** Draft
**Version:** 0.1.0
**MVP Phase/Wave:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Wave 0–7
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred
**Risk Level:** Low | Medium | High | Critical
**Owner:** MarkOrbit Publications Editorial Board
```

---

# 10. Agent Spec Required Sections

Every Agent Specification must include the following sections.

```text
1. Purpose
2. Agent Meaning
3. Agent Category
4. Agent Type
5. Owning Domain or System
6. Scope
7. Boundary
8. Agent Identity
9. Agent Contract
10. Allowed Capabilities
11. Prohibited Capabilities
12. Authorized Knowledge
13. Object Access
14. Service Access
15. Event Access
16. API Access
17. Inputs
18. Outputs
19. Risk Level
20. Human Review Rule
21. Audit Rule
22. AI Output Status Rules
23. Workflow Usage
24. Product Consumers
25. Failure Behavior
26. MVP Scope
27. Deferred Scope
28. Data and Implementation Notes
29. Codex Implementation Notes
30. Validation Rules
31. Prohibited Overreach
32. Acceptance Criteria
33. Revision Notes
```

---

# 11. Agent Identity Rules

Every implementation-ready Agent must have Agent Identity.

Agent Identity should define:

```text
agent ID
agent name
agent type
agent version
owning domain or system
execution environment
allowed consumers
permission scope
risk classification
status
```

Agent Identity is required for:

```text
permission checks
policy checks
audit records
Agent Contract validation
API access
object access
service invocation
event traceability
review routing
failure handling
```

An Agent without identity is not implementation-ready.

---

# 12. Agent Contract Rules

Every AI Agent, System Agent, Codex Agent or Validation Agent must have an Agent Contract.

Agent Contract must define:

```text
Agent Identity
Agent Purpose
Owning Domain or System
Agent Category
Agent Type
MVP Status
Allowed Capabilities
Prohibited Capabilities
Authorized Knowledge Sources
Authorized Knowledge Assets
Allowed Core Objects
Allowed Core Services
Allowed Core Events
Allowed APIs
Input Context Rules
Output Type
Output Status
Risk Level
Human Review Requirement
Permission Requirements
Policy Requirements
Events Emitted
Audit Requirements
Data Retention Rules
Failure Behavior
Product Consumers
API Exposure
Workflow Usage
Deferred Scope
Acceptance Criteria
Revision Notes
```

A prompt is not a substitute for Agent Contract.

---

# 13. Authorized Knowledge Rules

Agents may only use authorized knowledge.

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
third-party data without intake validation
```

High-risk professional output must cite authorized knowledge references.

---

# 14. Agent Capability Rules

Agent capabilities must be explicitly allowed.

Allowed capability examples:

```text
summarize status
suggest classification
prepare non-final draft
extract document metadata
summarize communication
suggest routing option
check specification consistency
check prohibited overreach
execute approved Codex task
```

Prohibited capability examples:

```text
submit official filing
make final legal decision
send external communication without approval
alter evidence content
invent legal authority
bypass review
bypass audit
change Core state directly
create Core architecture
expand MVP scope
```

If a capability is not explicitly allowed, it is not allowed.

---

# 15. Object Access Rules

Agent specs must define allowed Core Object access.

Access types:

```text
read
create draft
create recommendation
create audit record
link
validate
request review
no access
```

Agents must not mutate Core Objects directly.

State changes must occur through governed Core Services.

Object access must match:

```text
Agent Contract
Permission Rules
Policy Rules
Review Rules
Audit Rules
```

---

# 16. Service Access Rules

Agent specs must define allowed Core Service access.

Service access types:

```text
read-only invocation
recommendation generation
draft generation
validation request
review request
audit record creation
prohibited
```

Agents may invoke only services authorized by Agent Contract.

High-risk services require human review before output can be treated as final.

---

# 17. Event Access Rules

Agent specs must define event access.

Allowed event roles:

```text
consume event
reference event
request event through service
emit event through governed service
no event access
```

Agents must not emit Core Events directly unless the event is produced through an approved Core Service.

AI governance events include:

```text
AgentContractValidated
AgentContractValidationFailed
AIOutputGenerated
AIRecommendationGenerated
AIReviewRequired
AIUsagePolicyViolationDetected
AIAuditRecordCreated
```

---

# 18. API Access Rules

Agent specs must define API access.

API access requires:

```text
Agent Identity
Agent Contract
Permission Rule
Policy Rule
Allowed API List
Risk Level
Review Rule
Audit Rule
Failure Behavior
```

Agent APIs must not allow AI to:

```text
submit official filings
make final professional decisions
send external communication without approval
alter evidence
invent legal authority
bypass review
bypass audit
mutate Core Objects outside governed services
```

---

# 19. Risk Level Rules

Agent specs must assign a risk level.

Allowed risk levels:

```text
Low
Medium
High
Critical
```

## 19.1 Low

Low-risk agents may summarize, classify low-impact data or assist with non-final suggestions.

## 19.2 Medium

Medium-risk agents may influence service direction, document preparation, workflow routing or internal decision support.

## 19.3 High

High-risk agents may affect legal strategy, filing preparation, classification, evidence, routing, client-facing professional content or business responsibility.

## 19.4 Critical

Critical-risk agents may affect final professional judgment, official submissions, binding commitments, payment, external filing or high-liability decisions.

Critical-risk output always requires human approval.

---

# 20. AI Output Status Rules

AI outputs must use controlled statuses.

```text
Draft
Recommendation
ReviewRequired
ReviewApproved
ReviewRejected
Expired
Superseded
```

AI output is not professional truth unless required review and approval are complete.

Agent specs must state:

```text
output type
output status
review requirement
approval requirement
audit requirement
expiration or supersession behavior
```

---

# 21. Human Review Rules

Human review is required when an Agent:

```text
produces high-risk professional recommendation
creates client-facing draft
suggests filing scope
suggests legal argument
reviews evidence
suggests routing to external provider
triggers workflow state transition
returns AI output for external use
executes Codex implementation acceptance
```

Review rules must define:

```text
review trigger
review owner
review object
approval object
blocking behavior
review events
audit requirement
```

---

# 22. Audit Rules

Every AI Agent must produce audit records when it:

```text
uses professional knowledge
generates recommendation
generates document draft
affects workflow
triggers review
suggests routing
suggests opportunity
uses client data
uses official document data
produces high-risk output
```

Audit records should capture:

```text
agent ID
agent version
input context reference
knowledge sources used
objects accessed
services invoked
output reference
risk level
review requirement
review result
events emitted
timestamp
actor or system initiator
```

---

# 23. High-Priority Agent Specs

Initial agent specs should prioritize:

```text
ai-governance-agent.md
classification-assistant-agent.md
trademark-status-summary-agent.md
codex-implementation-agent.md
spec-consistency-review-agent.md
```

Partial baseline:

```text
document-draft-assistant-agent.md
evidence-review-assistant-agent.md
communication-summary-agent.md
routing-assistant-agent.md
workflow-assistant-agent.md
```

Reserved boundary:

```text
office-action-assistant.md
opportunity-discovery-agent.md
deadline-check-system-agent.md
```

Reserved boundary specs must not be production-enabled in MVP.

---

# 24. Baseline Agent Map

| Agent ID | Agent Name | Category | MVP Status | Risk |
|---------|------------|----------|------------|------|
| AGT-AI-GOV-001 | AI Governance Agent | Governance Agent | Must Implement | High |
| AGT-CLS-001 | Classification Assistant Agent | Professional Assistance Agent | Must Implement / Partial Implement | High |
| AGT-DOC-001 | Document Draft Assistant Agent | Professional Assistance Agent | Partial Implement | High |
| AGT-EVD-001 | Evidence Review Assistant Agent | Professional Assistance Agent | Partial Implement | High |
| AGT-TM-001 | Trademark Status Summary Agent | Professional Assistance Agent | Must Implement / Partial Implement | Medium |
| AGT-OA-001 | Office Action Assistant | Professional Assistance Agent | Reserved Boundary | Critical |
| AGT-COMM-001 | Communication Summary Agent | Communication Agent | Partial Implement | Medium |
| AGT-OPP-001 | Opportunity Discovery Agent | Opportunity and Routing Agent | Reserved Boundary | Medium |
| AGT-ROUTE-001 | Routing Assistant Agent | Opportunity and Routing Agent | Partial Implement | High |
| AGT-WF-001 | Workflow Assistant Agent | Execution Assistance Agent | Partial Implement | Medium |
| AGT-CODEX-001 | Codex Implementation Agent | Codex Implementation Agent | Must Implement | High |
| AGT-SPEC-001 | Spec Consistency Review Agent | Spec Review Agent | Partial Implement | Medium |
| AGT-SYS-001 | Event Processing System Agent | System Agent | Partial Implement | Medium |
| AGT-SYS-002 | Notification Dispatch System Agent | System Agent | Partial Implement | Medium |
| AGT-SYS-003 | Deadline Check System Agent | System Agent | Reserved Boundary | High |

---

# 25. Agent-to-Contract Rule

Every implementation-ready Agent must have related contracts.

Required contracts may include:

```text
Agent Contract
Authorized Knowledge Contract
AI Output Contract
AI Audit Contract
Review Contract
Permission Contract
Policy Contract
API Contract
Service Invocation Contract
Event Contract
```

Agent specs must reference these contracts but should not define full contract detail.

Detailed contract specs belong to:

```text
core-specs/contracts/
```

---

# 26. Agent-to-Service Rule

Agents may invoke only approved Core Services.

Examples:

```text
Classification Assistant Agent
    Classification Recommendation Service
    Classification Validation Service
    GoodsServices Term Lookup Service
    Knowledge Retrieval Service
    AI Audit Recording Service

Document Draft Assistant Agent
    Document Draft Service
    Document Validation Service
    Knowledge Retrieval Service
    AI Audit Recording Service

Codex Implementation Agent
    Codex Task Execution Service
    Codex Task Validation Service
    Spec Consistency Check Service
    Prohibited Overreach Check Service
```

Agent specs must define allowed service access and prohibited service access.

---

# 27. Agent-to-Event Rule

Agent-related execution must produce governed events through services.

Examples:

```text
AIOutputGenerated
AIRecommendationGenerated
AIReviewRequired
AIAuditRecordCreated
AgentContractValidated
AgentContractValidationFailed
AIUsagePolicyViolationDetected
CodexTaskStarted
CodexTaskImplemented
CodexTaskTested
CodexTaskAccepted
ProhibitedOverreachDetected
```

Agent specs must state which events may be produced by related services.

Agents must not publish Core Events directly outside governed service flow.

---

# 28. Agent-to-API Rule

Agent APIs must be explicitly authorized.

Examples:

```text
Classification Assistant Agent
    Knowledge Retrieval API
    Jurisdiction Requirement Lookup API
    GoodsServices Term Lookup API
    Classification Recommendation API
    Classification Validation API

Trademark Status Summary Agent
    Trademark Lookup API
    Trademark Lifecycle Summary API
    Jurisdiction Requirement Lookup API

Routing Assistant Agent
    Agent Lookup API
    Service Provider Lookup API
    Capability Matching Baseline API
    Routing Recommendation API

Codex Implementation Agent
    Codex Task Registration API
    Codex Task Validation API
    Spec Consistency Check API
    Prohibited Overreach Check API
```

API access must match:

```text
Agent Contract
API Contract
Permission Rule
Policy Rule
Review Rule
Audit Rule
```

---

# 29. Workflow Usage Rules

Agents may assist workflow but must not own workflow truth.

Allowed workflow assistance:

```text
summarize workflow progress
suggest next task
flag overdue tasks
flag missing review
recommend routing
request review
explain workflow state
```

Prohibited workflow behavior:

```text
create unapproved workflow states
skip required review
complete professional tasks without authority
change Matter status directly
change Order status directly
mutate workflow state outside governed services
```

---

# 30. Product Consumer Rules

Agent specs must classify product consumers.

Consumer categories:

```text
MVP Consumer
Partial Consumer
Future Consumer
```

MVP consumers:

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

Future consumers may include:

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

Products may expose Agents.

Products must not redefine Agent authority.

---

# 31. MVP Depth Rules

Agent specs must preserve MVP depth from:

```text
indexes/agent-index.md
```

Allowed values:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

A `Reserved Boundary` agent may be specified at boundary level but should not be production-enabled in MVP.

A `Deferred` agent should not be implemented without a later approved scope change.

---

# 32. Failure Behavior Rules

Every Agent Specification must define failure behavior.

Failure categories may include:

```text
missing Agent Identity
missing Agent Contract
unauthorized knowledge
permission failure
policy failure
object access denied
service access denied
API access denied
review required
review rejected
AI output invalid
agent hallucination risk
unsupported task
prohibited capability attempted
prohibited overreach detected
external dependency failure
```

For each failure type, define:

```text
result
event emitted if any
audit required
review or escalation required
safe retry rule
```

---

# 33. Data and Implementation Notes

Agent specs may include implementation-facing notes.

Allowed notes:

```text
Agent must have stable ID
Agent must have versioned contract
Agent must log authorized knowledge references
Agent must preserve correlation ID
Agent must create audit record for high-risk output
Agent must require review before external use
Agent must not mutate Core Objects directly
Agent must fail closed on missing permission
```

Prohibited notes:

```text
model provider selection as architecture
prompt text as Agent Contract
unreviewed prompt library
hidden system instructions as governance
physical database schema
controller implementation
UI assistant behavior
vendor-specific inference configuration
```

---

# 34. Codex Implementation Rules

Codex tasks generated from agent specs must:

```text
cite the agent spec
cite indexes/agent-index.md
cite related object, service, event, API and contract specs
preserve Agent Contract requirements
preserve authorized knowledge rules
preserve risk level
preserve human review rules
preserve audit rules
preserve MVP depth
preserve deferred scope
write tests
follow prohibited-overreach rules
```

Codex must not:

```text
create prompt-only agents
create agents without Agent Contract
create agents without authorized knowledge rules
create agents without audit rules
create agents that bypass review
create agents that mutate Core state directly
create agents that define Core architecture
implement reserved agents as production MVP
```

---

# 35. Validation Rules

The `core-specs/agents/` directory must pass the following checks.

```text
[ ] It contains README.md.
[ ] It contains _template.md before detailed specs.
[ ] Every agent spec has metadata.
[ ] Every agent spec references indexes/agent-index.md.
[ ] Every agent has Agent Identity requirement.
[ ] Every AI Agent has Agent Contract requirement.
[ ] Every agent has an owning domain or system.
[ ] Every agent has category and type.
[ ] Every agent has allowed capabilities.
[ ] Every agent has prohibited capabilities.
[ ] Every agent has authorized knowledge rules.
[ ] Every agent has object access rules.
[ ] Every agent has service access rules.
[ ] Every agent has event access rules.
[ ] Every agent has API access rules.
[ ] Every agent has risk level.
[ ] Every high-risk agent has human review rule.
[ ] Every AI Agent has audit rule.
[ ] Every agent has failure behavior.
[ ] No prompt is treated as an Agent.
[ ] No Agent replaces professional responsibility.
[ ] No reserved Agent is production-enabled in MVP.
```

---

# 36. Prohibited Behavior

This directory must not:

```text
treat prompts as Agents
create AI Agents without Agent Contract
create AI Agents without authorized knowledge
create AI Agents without audit
create high-risk Agents without review
allow AI to finalize professional decisions
allow AI to submit official filings
allow AI to send external communication without approval
allow AI to alter evidence content
allow AI to invent legal authority
allow Agents to mutate Core Objects directly
allow Agents to emit Core Events directly outside governed services
allow Codex Agent to define Core architecture
implement reserved Agents as MVP production agents
hide Agent authority inside product UI
```

---

# 37. Acceptance Criteria

The `core-specs/agents/README.md` file is accepted when:

```text
[ ] It defines the purpose of core-specs/agents/.
[ ] It defines Agent as governed actor.
[ ] It states AI is governed capability, not Core.
[ ] It distinguishes Agent from prompt, model call and chat session.
[ ] It defines directory boundary.
[ ] It defines source chain requirements.
[ ] It defines required agent spec groups.
[ ] It defines agent categories and types.
[ ] It defines required metadata.
[ ] It defines required sections.
[ ] It defines Agent Identity rules.
[ ] It defines Agent Contract rules.
[ ] It defines authorized knowledge rules.
[ ] It defines capability rules.
[ ] It defines object, service, event and API access rules.
[ ] It defines risk level rules.
[ ] It defines AI output status rules.
[ ] It defines human review rules.
[ ] It defines audit rules.
[ ] It lists high-priority agent specs.
[ ] It defines baseline agent map.
[ ] It defines agent-to-contract/service/event/API rules.
[ ] It defines workflow usage rules.
[ ] It defines product consumer rules.
[ ] It defines MVP depth rules.
[ ] It defines failure behavior rules.
[ ] It defines data and implementation notes.
[ ] It defines Codex implementation rules.
[ ] It defines validation rules.
[ ] It defines prohibited behavior.
```

---

# 38. Next Action

After this README is accepted, generate:

```text
core-specs/agents/_template.md
```

Do not generate detailed agent specs before the template exists.

---

# 39. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial README for core-specs/agents/. Defines directory purpose, agent identity, Agent Contract, authorized knowledge, access rules, risk/review/audit governance, baseline agent map, validation rules and template handoff. |

---

**End of README**
