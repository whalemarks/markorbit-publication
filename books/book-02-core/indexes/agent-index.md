# Agent Index

**Repository:** `book-02-core`  
**Directory:** `indexes/`  
**Index ID:** B02-IDX-AGENT  
**Source Appendix:** B02-APP-G — Agent Index  
**Related Appendices:** B02-APP-A — Glossary; B02-APP-C — Core Object Index; B02-APP-D — Core Service Index; B02-APP-E — Event Index; B02-APP-F — API Index  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Index Purpose

This index operationalizes **B02-APP-G — Agent Index**.

The appendix is the canonical manuscript reference.

This file is the implementation-ready agent index used by:

```text
core-specs/agents/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
codex-tasks/
validation scripts
AI governance checks
```

This index does not define prompts.

It defines governed Agents that operate under identity, permission, contract, authorized knowledge, review and audit rules.

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

# 3. Agent Definition

An Agent is a governed actor that may perform or assist a defined capability under identity, permission, contract, context, review and audit rules.

An Agent may be:

```text
Human Agent
External Professional Agent
AI Agent
System Agent
Codex Implementation Agent
```

This index focuses on operational AI Agents, System Agents and Codex-related agents.

External Professional Agents belong primarily to the Agent, Service Provider, Routing, Communication and Service Network domains.

---

# 4. Agent vs Prompt

An AI prompt is not an Agent.

A model call is not an Agent.

A chat session is not an Agent.

A product helper is not automatically an Agent.

An implementation-ready Agent requires:

```text
Agent Identity
Agent Contract
owning domain or cross-cutting system
allowed capabilities
prohibited capabilities
authorized knowledge
allowed object access
allowed service access
allowed event access
input context rules
output type
risk level
human review rule
event emission rule
audit rule
failure behavior
product consumer boundary
versioning
acceptance criteria
```

---

# 5. Agent Index Fields

Each agent entry should include the following fields.

```text
Agent ID
Agent Name
Agent Category
Agent Type
Owning Domain or System
Purpose
MVP Phase or Wave
MVP Status
Consumer Classification
Allowed Capabilities
Prohibited Capabilities
Authorized Knowledge
Allowed Object Access
Allowed Service Access
Allowed Event Access
Inputs
Outputs
Risk Level
Human Review Rule
Events Emitted
Audit Requirements
Failure Behavior
API Exposure
Workflow Usage
Product Consumers
Related Objects
Related Services
Related Contracts
Related Appendices
Future Scope
Acceptance Criteria
```

---

# 6. Agent Categories

This index uses the following agent categories.

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

---

# 7. MVP Status Vocabulary

Agents use the following MVP status values.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

A `Must Implement` agent or governance component is required for the first executable Core kernel.

A `Partial Implement` agent requires baseline specification and limited execution.

A `Reserved Boundary` agent is recognized but should not be deeply implemented in MVP.

A `Deferred` agent belongs to future releases.

---

# 8. Agent Risk Levels

Agents use the following risk levels.

```text
Low
Medium
High
Critical
```

## 8.1 Low

Low-risk agents may summarize, classify low-impact data, or assist with non-final suggestions.

## 8.2 Medium

Medium-risk agents may influence service direction, document preparation, workflow routing or internal decision support.

## 8.3 High

High-risk agents may affect legal strategy, filing preparation, classification, evidence, routing, client-facing professional content or business responsibility.

## 8.4 Critical

Critical-risk agents may affect final professional judgment, official submissions, binding commitments, payment, external filing or high-liability decisions.

Critical-risk output always requires human approval.

---

# 9. AI Output Status Vocabulary

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

AI output is not professional truth unless it has the required review and approval status.

---

# 10. Agent Index Summary

| Agent ID | Agent Name | Category | Owning Domain/System | MVP Phase/Wave | MVP Status | Risk |
|---------|------------|----------|----------------------|----------------|------------|------|
| AGT-AI-GOV-001 | AI Governance Agent | Governance Agent | AI Governance | Phase 4 | Must Implement | High |
| AGT-CLS-001 | Classification Assistant Agent | Professional Assistance Agent | Classification / AI Governance | Phase 2 / 4 | Must Implement / Partial Implement | High |
| AGT-DOC-001 | Document Draft Assistant Agent | Professional Assistance Agent | Document / AI Governance | Phase 2 / 4 | Partial Implement | High |
| AGT-EVD-001 | Evidence Review Assistant Agent | Professional Assistance Agent | Evidence / AI Governance | Phase 2 / 4 | Partial Implement | High |
| AGT-TM-001 | Trademark Status Summary Agent | Professional Assistance Agent | Trademark / AI Governance | Phase 2 / 4 | Must Implement / Partial Implement | Medium |
| AGT-OA-001 | Office Action Assistant | Professional Assistance Agent | Trademark / Document / Knowledge / AI Governance | Future | Reserved Boundary | Critical |
| AGT-COMM-001 | Communication Summary Agent | Communication Agent | Communication / AI Governance | Phase 4 | Partial Implement | Medium |
| AGT-OPP-001 | Opportunity Discovery Agent | Opportunity and Routing Agent | Opportunity / AI Governance | Phase 4 | Reserved Boundary | Medium |
| AGT-ROUTE-001 | Routing Assistant Agent | Opportunity and Routing Agent | Routing / AI Governance | Phase 4 | Partial Implement | High |
| AGT-WF-001 | Workflow Assistant Agent | Execution Assistance Agent | Workflow Contract / Task / AI Governance | Phase 3 / 4 | Partial Implement | Medium |
| AGT-CODEX-001 | Codex Implementation Agent | Codex Implementation Agent | Codex Task System | Wave 0–7 | Must Implement | High |
| AGT-SPEC-001 | Spec Consistency Review Agent | Spec Review Agent | Specification Governance | Wave 0 / 7 | Partial Implement | Medium |
| AGT-SYS-001 | Event Processing System Agent | System Agent | Event | Phase 3 | Partial Implement | Medium |
| AGT-SYS-002 | Notification Dispatch System Agent | System Agent | Notification | Phase 3 | Partial Implement | Medium |
| AGT-SYS-003 | Deadline Check System Agent | System Agent | Task / Matter | Phase 3 | Reserved Boundary | High |

---

# 11. High-Priority MVP Agent Baseline

The high-priority MVP baseline includes:

```text
AI Governance Agent
Classification Assistant Agent
Trademark Status Summary Agent
Codex Implementation Agent
Spec Consistency Review Agent
Event Processing System Agent
```

The following are partial or controlled baseline agents:

```text
Document Draft Assistant Agent
Evidence Review Assistant Agent
Communication Summary Agent
Routing Assistant Agent
Workflow Assistant Agent
Notification Dispatch System Agent
```

The following remain reserved boundaries:

```text
Office Action Assistant
Opportunity Discovery Agent
Deadline Check System Agent
```

---

# 12. AGT-AI-GOV-001 — AI Governance Agent

| Field | Value |
|------|-------|
| Agent Category | Governance Agent |
| Agent Type | AI Agent |
| Owning System | AI Governance |
| MVP Status | Must Implement |
| Risk Level | High |
| API Exposure | Internal API |
| Human Review | Required for governance changes |

## Purpose

Supports enforcement of AI governance rules.

## Allowed Capabilities

```text
check Agent Contract completeness
check authorized knowledge declaration
check missing review rules
check missing audit rules
check risk level declaration
check prohibited capability declaration
support governance review
```

## Prohibited Capabilities

```text
approve its own governance
bypass human review
grant itself object access
change production Agent Contracts without approval
make final professional decisions
```

## Authorized Knowledge

```text
Book 02 AI governance chapters
Appendix A Glossary
Appendix G Agent Index
agent-index.md
Agent Contract templates
approved AI governance rules
```

## Related Objects

```text
AI Agent
Agent Contract
AI Output
AI Audit Record
Review Record
Policy Rule
Permission Rule
```

## Related Services

```text
Agent Contract Validation Service
AI Risk Policy Check Service
AI Audit Recording Service
AI Review Routing Service
```

## Events Emitted

```text
AgentContractValidated
AgentContractValidationFailed
AIUsagePolicyViolationDetected
AIReviewRequired
AIAuditRecordCreated
```

---

# 13. AGT-CLS-001 — Classification Assistant Agent

| Field | Value |
|------|-------|
| Agent Category | Professional Assistance Agent |
| Agent Type | AI Agent |
| Owning Domain/System | Classification / AI Governance |
| MVP Status | Must Implement / Partial Implement |
| Risk Level | High |
| API Exposure | Agent API / Product API |
| Human Review | Required before filing use or final client-facing recommendation |

## Purpose

Assists with goods/services classification, Nice class mapping, local classification constraints and recommendation preparation.

## Allowed Capabilities

```text
suggest Nice classes
suggest goods/services terms
compare proposed terms with approved references
identify possible overbroad or mismatched terms
explain classification reasoning
flag uncertain items for review
```

## Prohibited Capabilities

```text
finalize filing scope without review
submit official filing
invent unsupported goods/services terms as official truth
ignore jurisdiction-specific constraints
bypass professional review
```

## Authorized Knowledge

```text
Nice Classification references
jurisdiction classification rules
approved goods/services term libraries
internal classification knowledge
prior reviewed classification examples
```

## Related Objects

```text
Classification Recommendation
Trademark
Jurisdiction
GoodsServices Term
Knowledge Asset
AI Recommendation
Review Record
AI Audit Record
```

## Related Services

```text
Classification Recommendation Service
Classification Validation Service
GoodsServices Term Lookup Service
Knowledge Retrieval Service
Review Assignment Service
AI Audit Recording Service
```

## Events Emitted

```text
ClassificationRecommendationGenerated
ClassificationReviewRequired
AIRecommendationGenerated
AIAuditRecordCreated
```

---

# 14. AGT-DOC-001 — Document Draft Assistant Agent

| Field | Value |
|------|-------|
| Agent Category | Professional Assistance Agent |
| Agent Type | AI Agent |
| Owning Domain/System | Document / AI Governance |
| MVP Status | Partial Implement |
| Risk Level | High |
| API Exposure | Agent API / Product API |
| Human Review | Required before external use |

## Purpose

Assists with drafting, summarizing, translating or preparing professional documents.

## Allowed Capabilities

```text
draft internal document text
summarize official documents
prepare document checklists
suggest required materials
generate non-final draft letters
extract document metadata
```

## Prohibited Capabilities

```text
submit official documents
sign documents
create binding legal statements without review
modify official evidence without review
send client-facing final documents without approval
```

## Related Objects

```text
Document
Document Requirement
Document Draft
AI Draft
AI Output
Review Record
AI Audit Record
```

## Related Services

```text
Document Requirement Service
Document Draft Service
Document Validation Service
Review Assignment Service
AI Output Registration Service
AI Audit Recording Service
```

## Events Emitted

```text
DocumentGenerated
DocumentReviewRequired
AIOutputGenerated
AIAuditRecordCreated
```

---

# 15. AGT-EVD-001 — Evidence Review Assistant Agent

| Field | Value |
|------|-------|
| Agent Category | Professional Assistance Agent |
| Agent Type | AI Agent |
| Owning Domain/System | Evidence / AI Governance |
| MVP Status | Partial Implement |
| Risk Level | High |
| API Exposure | Internal API / Agent API |
| Human Review | Required |

## Purpose

Assists with preliminary evidence review, evidence grouping and evidence sufficiency notes.

## Allowed Capabilities

```text
summarize evidence files
group evidence by type
identify missing evidence metadata
flag weak evidence
prepare evidence review notes
```

## Prohibited Capabilities

```text
declare evidence legally sufficient as final truth
submit evidence without review
alter evidence content
fabricate evidence
ignore jurisdiction-specific evidence rules
```

## Related Objects

```text
Evidence
Evidence Package
Evidence Review Note
AI Output
Review Record
AI Audit Record
```

## Related Services

```text
Evidence Review Service
Evidence Package Service
AI Output Registration Service
AI Audit Recording Service
Review Assignment Service
```

## Events Emitted

```text
EvidenceReviewRequired
EvidencePackageFlagged
AIOutputGenerated
AIAuditRecordCreated
```

---

# 16. AGT-TM-001 — Trademark Status Summary Agent

| Field | Value |
|------|-------|
| Agent Category | Professional Assistance Agent |
| Agent Type | AI Agent |
| Owning Domain/System | Trademark / AI Governance |
| MVP Status | Must Implement / Partial Implement |
| Risk Level | Medium |
| API Exposure | Agent API / Product API |
| Human Review | Required for client-facing legal interpretation |

## Purpose

Assists with summarizing trademark status and lifecycle information.

## Allowed Capabilities

```text
summarize trademark status
normalize status descriptions
explain lifecycle stage
identify upcoming maintenance or action points
link status to Matter context
```

## Prohibited Capabilities

```text
change official trademark status
override official source data
provide final legal advice without review
invent official deadlines
```

## Related Objects

```text
Trademark
Trademark Status
Trademark Lifecycle Record
Trademark Status Summary
AI Summary
AI Audit Record
```

## Related Services

```text
Trademark Status Normalization Service
Trademark Lifecycle Summary Service
AI Output Registration Service
AI Audit Recording Service
```

## Events Emitted

```text
TrademarkStatusSummaryGenerated
AIOutputGenerated
AIAuditRecordCreated
```

---

# 17. AGT-OA-001 — Office Action Assistant

| Field | Value |
|------|-------|
| Agent Category | Professional Assistance Agent |
| Agent Type | AI Agent |
| Owning Domain/System | Trademark / Document / Knowledge / AI Governance |
| MVP Status | Reserved Boundary |
| Risk Level | Critical |
| API Exposure | No MVP API |
| Human Review | Mandatory |

## Purpose

Supports analysis and draft response preparation for official refusals or office actions.

## Allowed Capabilities

```text
summarize office action text
identify refusal grounds
retrieve relevant knowledge
prepare issue outline
draft non-final response structure
flag missing evidence
```

## Prohibited Capabilities

```text
file official response
make final legal argument without attorney review
guarantee outcome
invent legal authority
ignore jurisdiction-specific rules
send final response to client without approval
```

## Related Objects

```text
Office Action
Document
Evidence
AI Draft
Review Record
AI Audit Record
Knowledge Asset
```

## Related Services

```text
Office Action Analysis Service
Knowledge Retrieval Service
Document Draft Service
Review Assignment Service
AI Audit Recording Service
```

## Events Emitted

```text
OfficeActionSummaryGenerated
OfficeActionReviewRequired
OfficeActionDraftGenerated
AIAuditRecordCreated
```

---

# 18. AGT-COMM-001 — Communication Summary Agent

| Field | Value |
|------|-------|
| Agent Category | Communication Agent |
| Agent Type | AI Agent |
| Owning Domain/System | Communication / AI Governance |
| MVP Status | Partial Implement |
| Risk Level | Medium |
| API Exposure | Agent API / Product API |
| Human Review | Required before external reply or binding action |

## Purpose

Assists with summarizing and linking communications to Core Objects such as Matter, Task, Customer, Agent or Document.

## Allowed Capabilities

```text
summarize email or message content
extract action items
link communication to Matter or Task
identify deadlines mentioned in communication
draft internal notes
```

## Prohibited Capabilities

```text
send external communication without approval
create binding commitments
change Matter state without service
extract private information outside permission scope
```

## Related Objects

```text
Communication
Communication Thread
Communication Summary
Communication Action Item
Matter
Task
AI Output
AI Audit Record
```

## Related Services

```text
Communication Summary Service
Communication Link Service
Communication Action Item Service
AI Output Registration Service
AI Audit Recording Service
```

## Events Emitted

```text
CommunicationSummaryGenerated
CommunicationActionItemDetected
CommunicationLinkedToMatter
AIOutputGenerated
AIAuditRecordCreated
```

---

# 19. AGT-OPP-001 — Opportunity Discovery Agent

| Field | Value |
|------|-------|
| Agent Category | Opportunity and Routing Agent |
| Agent Type | AI Agent |
| Owning Domain/System | Opportunity / AI Governance |
| MVP Status | Reserved Boundary |
| Risk Level | Medium |
| API Exposure | No MVP API |
| Human Review | Required before sales action |

## Purpose

Identifies possible business opportunities from trademark, customer, jurisdiction, status or portfolio signals.

## Allowed Capabilities

```text
identify possible renewal opportunities
identify jurisdiction expansion signals
identify missing protection gaps
suggest follow-up opportunities
rank simple opportunity signals
```

## Prohibited Capabilities

```text
create binding sales commitment
automatically contact client
create full scoring engine in MVP
override sales responsibility
```

## Related Objects

```text
Opportunity
Opportunity Signal
Opportunity Recommendation
Customer
Trademark
AI Recommendation
Responsibility Assignment
```

## Related Services

```text
Opportunity Detection Baseline Service
Opportunity Creation Service
Opportunity Review Service
AI Recommendation Registration Service
Review Assignment Service
```

## Events Emitted

```text
OpportunitySignalDetected
OpportunityCreated
OpportunityReviewRequired
AIRecommendationGenerated
AIAuditRecordCreated
```

---

# 20. AGT-ROUTE-001 — Routing Assistant Agent

| Field | Value |
|------|-------|
| Agent Category | Opportunity and Routing Agent |
| Agent Type | AI Agent |
| Owning Domain/System | Routing / AI Governance |
| MVP Status | Partial Implement |
| Risk Level | High |
| API Exposure | Agent API / Product API |
| Human Review | Required for external assignment or provider selection |

## Purpose

Assists with recommending internal assignees, foreign agents or service providers.

## Allowed Capabilities

```text
suggest routing options
compare provider capability
match jurisdiction and service type
flag missing provider capability
prepare routing recommendation
```

## Prohibited Capabilities

```text
finalize provider selection without approval
assign external work without responsibility record
override policy
create full provider ranking marketplace in MVP
```

## Related Objects

```text
Routing Decision
Routing Candidate
Agent
Service Provider
Capability
Matter
Responsibility Assignment
AI Recommendation
AI Audit Record
```

## Related Services

```text
Routing Recommendation Service
Routing Review Service
Routing Decision Service
Capability Matching Service
AI Recommendation Registration Service
AI Audit Recording Service
```

## Events Emitted

```text
RoutingRecommendationGenerated
RoutingReviewRequired
AIRecommendationGenerated
AIAuditRecordCreated
```

---

# 21. AGT-WF-001 — Workflow Assistant Agent

| Field | Value |
|------|-------|
| Agent Category | Execution Assistance Agent |
| Agent Type | AI Agent |
| Owning Domain/System | Workflow Contract / Task / AI Governance |
| MVP Status | Partial Implement |
| Risk Level | Medium |
| API Exposure | Agent API / Internal API |
| Human Review | Required when state transition affects legal or business responsibility |

## Purpose

Assists with task sequencing, review reminders, workflow progress and execution coordination.

## Allowed Capabilities

```text
summarize workflow progress
suggest next task
identify overdue tasks
flag missing review
explain workflow state
```

## Prohibited Capabilities

```text
create unapproved workflow states
skip required review
complete tasks without service rules
change Matter status without governed service
```

## Related Objects

```text
Workflow Contract
Workflow State
Task
Matter
Review Record
AI Recommendation
AI Audit Record
```

## Related Services

```text
Workflow Transition Validation Service
Task Creation Service
Task Assignment Service
Task Review Service
AI Recommendation Registration Service
AI Audit Recording Service
```

## Events Emitted

```text
NextTaskSuggested
WorkflowReviewRequired
TaskReviewRequired
AIRecommendationGenerated
AIAuditRecordCreated
```

---

# 22. AGT-CODEX-001 — Codex Implementation Agent

| Field | Value |
|------|-------|
| Agent Category | Codex Implementation Agent |
| Agent Type | Codex Agent |
| Owning Domain/System | Codex Task System |
| MVP Status | Must Implement |
| Risk Level | High |
| API Exposure | Internal API |
| Human Review | Required for acceptance |

## Purpose

Assists with implementing approved Core specifications.

## Allowed Capabilities

```text
create repository scaffold
generate spec templates
implement approved models
implement approved services
implement approved events
write tests
update documentation
follow task acceptance criteria
```

## Prohibited Capabilities

```text
invent Core domains
invent object meanings
invent event semantics
invent AI authority
expand deferred features
change MVP scope
ignore source specs
skip tests
```

## Authorized Knowledge

```text
Book 02 manuscript
Appendices A–H
indexes/
core-specs/
codex-tasks/
approved Codex Task files
```

## Related Objects

```text
Codex Task
Spec File
Test Fixture
Implementation Artifact
Acceptance Criteria
Validation Report
```

## Related Services

```text
Codex Task Registration Service
Codex Task Validation Service
Codex Task Execution Service
Spec Consistency Check Service
Prohibited Overreach Check Service
```

## Events Emitted

```text
CodexTaskStarted
CodexTaskImplemented
CodexTaskTested
CodexTaskBlocked
CodexTaskAccepted
ProhibitedOverreachDetected
```

---

# 23. AGT-SPEC-001 — Spec Consistency Review Agent

| Field | Value |
|------|-------|
| Agent Category | Spec Review Agent |
| Agent Type | AI Agent / Validation Agent |
| Owning Domain/System | Specification Governance |
| MVP Status | Partial Implement |
| Risk Level | Medium |
| API Exposure | Internal API |
| Human Review | Required for architecture changes |

## Purpose

Assists with reviewing manuscript, appendices, indexes and `core-specs/` for consistency.

## Allowed Capabilities

```text
check terminology consistency
check domain count consistency
check object ownership
check service-event mapping
check API-contract mapping
check agent contract completeness
check Codex task source references
```

## Prohibited Capabilities

```text
approve architecture alone
silently rewrite canonical specs
change domain baseline
override editorial review
```

## Related Objects

```text
Spec File
Appendix
Index
Review Record
Validation Report
```

## Related Services

```text
Spec Consistency Check Service
Prohibited Overreach Check Service
Codex Task Validation Service
```

## Events Emitted

```text
SpecConsistencyIssueDetected
SpecReviewRequired
ProhibitedOverreachDetected
```

---

# 24. System Agent Baseline

System Agents may perform scheduled or automated tasks.

Examples:

```text
Event Processing System Agent
Notification Dispatch System Agent
Deadline Check System Agent
Status Sync System Agent
Audit Recording System Agent
```

System Agents must operate under:

```text
Identity
Permission
Service Contract
Event Contract
Audit Rule
Failure Behavior
```

System Agents must not bypass Core Services.

---

# 25. Agent-to-Object Mapping

| Agent | Primary Objects |
|------|-----------------|
| AI Governance Agent | AI Agent, Agent Contract, AI Audit Record, Review Record |
| Classification Assistant Agent | Classification Recommendation, Trademark, Jurisdiction, AI Recommendation |
| Document Draft Assistant Agent | Document, Document Draft, AI Draft, Review Record |
| Evidence Review Assistant Agent | Evidence, Evidence Package, Evidence Review Note, AI Audit Record |
| Trademark Status Summary Agent | Trademark, Trademark Status, Trademark Lifecycle Record, AI Summary |
| Office Action Assistant | Office Action, Document, Evidence, Knowledge Asset, AI Draft |
| Communication Summary Agent | Communication, Communication Summary, Communication Action Item, Matter, Task |
| Opportunity Discovery Agent | Opportunity, Opportunity Signal, Opportunity Recommendation, Customer, Trademark |
| Routing Assistant Agent | Routing Decision, Routing Candidate, Agent, Service Provider, Capability |
| Workflow Assistant Agent | Workflow Contract, Task, Matter, Review Record, AI Recommendation |
| Codex Implementation Agent | Codex Task, Spec File, Test Fixture, Implementation Artifact |
| Spec Consistency Review Agent | Spec File, Appendix, Index, Validation Report |

---

# 26. Agent-to-Service Mapping

| Agent | Primary Services |
|------|------------------|
| AI Governance Agent | Agent Contract Validation Service, AI Risk Policy Check Service |
| Classification Assistant Agent | Classification Recommendation Service, Classification Validation Service |
| Document Draft Assistant Agent | Document Draft Service, Document Validation Service |
| Evidence Review Assistant Agent | Evidence Review Service, Evidence Package Service |
| Trademark Status Summary Agent | Trademark Lifecycle Summary Service, Trademark Status Normalization Service |
| Office Action Assistant | Office Action Analysis Service, Knowledge Retrieval Service |
| Communication Summary Agent | Communication Summary Service, Communication Action Item Service |
| Opportunity Discovery Agent | Opportunity Detection Baseline Service, Opportunity Review Service |
| Routing Assistant Agent | Routing Recommendation Service, Routing Review Service |
| Workflow Assistant Agent | Workflow Transition Validation Service, Task Review Service |
| Codex Implementation Agent | Codex Task Execution Service, Codex Task Validation Service |
| Spec Consistency Review Agent | Spec Consistency Check Service, Prohibited Overreach Check Service |

---

# 27. Agent-to-Event Mapping

| Agent | Events |
|------|--------|
| AI Governance Agent | AgentContractValidated, AgentContractValidationFailed, AIUsagePolicyViolationDetected |
| Classification Assistant Agent | ClassificationRecommendationGenerated, ClassificationReviewRequired, AIRecommendationGenerated |
| Document Draft Assistant Agent | DocumentGenerated, DocumentReviewRequired, AIOutputGenerated |
| Evidence Review Assistant Agent | EvidenceReviewRequired, EvidencePackageFlagged, AIOutputGenerated |
| Trademark Status Summary Agent | TrademarkStatusSummaryGenerated, AIOutputGenerated |
| Office Action Assistant | OfficeActionSummaryGenerated, OfficeActionReviewRequired, OfficeActionDraftGenerated |
| Communication Summary Agent | CommunicationSummaryGenerated, CommunicationActionItemDetected |
| Opportunity Discovery Agent | OpportunitySignalDetected, OpportunityReviewRequired, AIRecommendationGenerated |
| Routing Assistant Agent | RoutingRecommendationGenerated, RoutingReviewRequired, AIRecommendationGenerated |
| Workflow Assistant Agent | NextTaskSuggested, WorkflowReviewRequired, TaskReviewRequired |
| Codex Implementation Agent | CodexTaskStarted, CodexTaskImplemented, CodexTaskTested, CodexTaskBlocked, CodexTaskAccepted |
| Spec Consistency Review Agent | SpecConsistencyIssueDetected, SpecReviewRequired, ProhibitedOverreachDetected |

---

# 28. Agent Contract Requirements

Each implementation-ready agent must have an Agent Contract.

Agent Contract fields:

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

---

# 29. Authorized Knowledge Rules

AI Agents may only use authorized knowledge.

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

---

# 30. Agent API Exposure Rules

Agent APIs must be contract-bound.

Agent API exposure levels:

```text
No API
Internal API
Agent API
Product API
Admin API
```

High-risk and critical agents should not be exposed directly to external consumers.

Reserved agents should use `No API` for MVP.

Agent APIs must define:

```text
input contract
output contract
permission rule
policy rule
review rule
audit rule
event side effects
failure behavior
consumer classification
```

---

# 31. Audit Requirements

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

# 32. Prohibited Agent Behavior

Agents must not:

```text
operate without Agent Identity
operate without Agent Contract
use unauthorized knowledge
access objects outside permission scope
invoke services outside allowed service list
emit Core Events directly without governed service
bypass review for high-risk output
treat AI output as final professional truth
submit official filings
make binding commitments
send external communication without approval
invent legal authority
alter evidence content
change MVP scope
create Core domains, objects, services or events
```

---

# 33. Validation Rules

The agent index must pass the following validation checks.

```text
[ ] Every agent has an Agent ID.
[ ] Every agent has a name.
[ ] Every agent has a category.
[ ] Every agent has an owning domain or system.
[ ] Every AI Agent has Agent Identity requirement.
[ ] Every AI Agent has Agent Contract requirement.
[ ] Every AI Agent has authorized knowledge rules.
[ ] Every AI Agent has allowed object access.
[ ] Every AI Agent has allowed service access.
[ ] Every AI Agent has risk level.
[ ] Every AI Agent has human review rule.
[ ] Every AI Agent has audit requirement.
[ ] Every agent has MVP status.
[ ] Every agent has prohibited capabilities.
[ ] Every event-emitting agent maps to governed services.
[ ] No prompt is treated as an agent.
[ ] No AI Agent replaces professional responsibility.
[ ] No reserved agent is exposed as MVP production API.
```

---

# 34. Prohibited Agent Changes

This index must not be changed to:

```text
treat prompts as agents
create AI agents without Agent Contract
create AI agents without audit
create AI agents without review rules
create AI agents without authorized knowledge
allow AI to finalize professional decisions
allow AI to submit official filings
allow AI to mutate Core Objects directly
allow Codex to define architecture
expose reserved agents as MVP external APIs
remove risk classifications
remove human review rules from high-risk agents
```

---

# 35. Handoff to core-specs/agents/

This index will generate future files under:

```text
core-specs/agents/
```

Expected scaffold:

```text
core-specs/agents/README.md
core-specs/agents/_template.md
core-specs/agents/ai-governance-agent.md
core-specs/agents/classification-assistant-agent.md
core-specs/agents/document-draft-assistant-agent.md
core-specs/agents/evidence-review-assistant-agent.md
core-specs/agents/trademark-status-summary-agent.md
core-specs/agents/communication-summary-agent.md
core-specs/agents/routing-assistant-agent.md
core-specs/agents/workflow-assistant-agent.md
core-specs/agents/codex-implementation-agent.md
core-specs/agents/spec-consistency-review-agent.md
```

Reserved future specs may include:

```text
core-specs/agents/office-action-assistant.md
core-specs/agents/opportunity-discovery-agent.md
core-specs/agents/deadline-check-system-agent.md
```

Reserved specs must not be production-enabled in MVP.

---

# 36. Handoff to codex-task-index.md

The next index should be checked against this agent index.

```text
indexes/codex-task-index.md
```

Codex tasks must include AI and agent-related tasks for:

```text
Agent Contract template
AI Agent Identity object
AI Output object
AI Recommendation object
AI Audit Record object
Agent Contract Validation Service
AI Review Routing Service
AI Audit Recording Service
AI Governance Agent
Classification Assistant Agent baseline
Trademark Status Summary Agent baseline
Codex Implementation Agent constraints
Spec Consistency Review Agent baseline
agent tests and fixtures
```

A Codex task must not implement an unindexed agent.

---

# 37. Acceptance Criteria

This index is accepted only if it satisfies the following criteria.

```text
[ ] It defines Agent operationally.
[ ] It distinguishes Agent from prompt, model call and chat session.
[ ] It defines Agent Index fields.
[ ] It defines Agent categories.
[ ] It defines MVP status vocabulary.
[ ] It defines risk levels.
[ ] It defines AI output statuses.
[ ] It lists all baseline agents.
[ ] It identifies high-priority MVP agents.
[ ] It defines AI Governance Agent.
[ ] It defines Classification Assistant Agent.
[ ] It defines Document Draft Assistant Agent.
[ ] It defines Evidence Review Assistant Agent.
[ ] It defines Trademark Status Summary Agent.
[ ] It reserves Office Action Assistant.
[ ] It defines Communication Summary Agent.
[ ] It defines Opportunity Discovery Agent as reserved.
[ ] It defines Routing Assistant Agent.
[ ] It defines Workflow Assistant Agent.
[ ] It defines Codex Implementation Agent.
[ ] It defines Spec Consistency Review Agent.
[ ] It maps agents to objects, services and events.
[ ] It defines Agent Contract requirements.
[ ] It defines authorized knowledge rules.
[ ] It defines API exposure rules.
[ ] It defines audit requirements.
[ ] It defines prohibited agent behavior.
[ ] It defines validation rules.
[ ] It prepares core-specs/agents/.
[ ] It hands off to codex-task-index.md.
```

---

# 38. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial operational Agent Index derived from B02-APP-G. Defines governed agents, AI governance, baseline agents, Agent Contract requirements, object/service/event mappings, validation rules and handoff to codex-task-index.md. |

---

**End of Index**
