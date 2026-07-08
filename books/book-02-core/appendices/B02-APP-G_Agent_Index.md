# Book 02

# Appendix G — Agent Index

**Book Title:** MarkOrbit Core Specification  
**Appendix ID:** B02-APP-G  
**Appendix Title:** Agent Index  
**Appendix Type:** Canonical Index  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Chapters:**

- B02-CH-03 — Core Position
- B02-CH-04 — Core Boundary
- B02-CH-05 — Core Principles
- B02-CH-17 — Core Contract Architecture
- B02-CH-23 — Object Specification
- B02-CH-24 — Service Specification
- B02-CH-25 — Event Specification
- B02-CH-26 — AI Capability and Agent Governance Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-28 — Core MVP Boundary
- B02-CH-30 — MVP Execution Matrix
- B02-CH-31 — Codex Implementation Roadmap

**Related Appendices:**

- B02-APP-A — Glossary
- B02-APP-C — Core Object Index
- B02-APP-D — Core Service Index
- B02-APP-E — Event Index
- B02-APP-F — API Index
- B02-APP-H — Codex Task Index

---

# 1. Appendix Purpose

This appendix defines the canonical Agent Index for Book 02.

The Agent Index exists because AI capabilities must not be implemented as informal prompts, isolated chat tools or product-specific helpers.

In MarkOrbit, an agent is a governed execution actor.

An AI Agent may assist professional work, but it must operate under Core governance.

This appendix defines:

```text
agent categories
agent identity requirements
Agent Contract requirements
MVP agent baseline
allowed capabilities
prohibited capabilities
authorized knowledge
object access
service access
event requirements
audit requirements
human review rules
risk levels
product consumers
core-specs/agents readiness
Codex handoff requirements
```

The Agent Index is required before detailed `core-specs/agents/` and Codex AI implementation tasks are generated.

---

# 2. Canonical Agent Rule

Book 02 uses the following rule:

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

This appendix focuses primarily on AI Agents and Codex-related agents.

External professional agents belong to the Agent domain and are also indexed in Appendix B and Appendix C as collaboration network concepts.

---

# 4. Agent vs Prompt

An AI prompt is not an Agent.

A model call is not an Agent.

A chat session is not an Agent.

A product helper is not automatically an Agent.

An Agent requires:

```text
Agent Identity
Agent Contract
owning domain or cross-cutting system
allowed capabilities
prohibited capabilities
authorized knowledge
allowed object access
allowed service access
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

# 5. Agent Categories

Book 02 recognizes the following agent categories.

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

## 5.1 Governance Agent

A Governance Agent supports AI governance, review, audit or compliance.

## 5.2 Professional Assistance Agent

A Professional Assistance Agent supports trademark, jurisdiction, classification, document, evidence or office action work.

## 5.3 Execution Assistance Agent

An Execution Assistance Agent supports task, workflow, matter, notification or execution coordination.

## 5.4 Communication Agent

A Communication Agent supports communication analysis, summarization, drafting or linkage.

## 5.5 Opportunity and Routing Agent

An Opportunity and Routing Agent supports business opportunity discovery, provider selection or routing recommendation.

## 5.6 Codex Implementation Agent

A Codex Implementation Agent assists with implementation based on approved specs.

It does not define architecture.

## 5.7 Spec Review Agent

A Spec Review Agent assists with consistency checking, linting, validation or review of specifications.

## 5.8 External Professional Agent

An External Professional Agent is a foreign associate, law firm, service provider or professional actor.

It is not the same as an AI Agent.

## 5.9 System Agent

A System Agent is a non-human actor used for system-level actions such as scheduled checks, data sync or event processing.

---

# 6. Required Agent Index Fields

Each Agent Index entry should include:

```text
Agent ID
Agent Name
Agent Category
Agent Type
Owning Domain or Cross-Cutting System
Purpose
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
Product Consumers
Workflow Usage
API Surface
Related Objects
Related Services
Related Contracts
Related Appendices
Future Scope
Acceptance Criteria
```

---

# 7. Agent Contract Required Fields

Each detailed Agent Contract should include:

```text
1. Agent Identity
2. Agent Purpose
3. Owning Domain or Cross-Cutting System
4. Agent Category
5. Agent Type
6. MVP Status
7. Allowed Capabilities
8. Prohibited Capabilities
9. Authorized Knowledge Sources
10. Authorized Knowledge Assets
11. Allowed Core Objects
12. Allowed Core Services
13. Allowed Core Events
14. Input Context Rules
15. Output Type
16. Output Status
17. Risk Level
18. Human Review Requirement
19. Permission Requirements
20. Policy Requirements
21. Events Emitted
22. Audit Requirements
23. Data Retention Rules
24. Failure Behavior
25. Product Consumers
26. API Exposure
27. Workflow Usage
28. Deferred Scope
29. Acceptance Criteria
30. Revision Notes
```

---

# 8. Agent MVP Status Types

Agents use the following MVP status types.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## 8.1 Must Implement

The agent or agent governance is required for MVP execution.

## 8.2 Partial Implement

The agent requires baseline specification or limited execution but not full automation.

## 8.3 Reserved Boundary

The agent is reserved for future products or network operations.

## 8.4 Deferred

The agent should not be implemented in MVP.

---

# 9. Agent Risk Levels

Book 02 uses the following risk levels for agents.

```text
Low
Medium
High
Critical
```

## 9.1 Low Risk

Low-risk agents may summarize, classify low-impact data, or assist with non-final suggestions.

Human review may be optional depending on product context.

## 9.2 Medium Risk

Medium-risk agents may influence service direction, document preparation, classification suggestions or workflow routing.

Human review is usually required before external use or state change.

## 9.3 High Risk

High-risk agents may affect legal strategy, official filing content, refusal response, evidence sufficiency, agent selection or client-facing professional advice.

Human review is required.

## 9.4 Critical Risk

Critical-risk agents may affect final professional judgment, legal submissions, binding commitments, payment, external filing, or high-liability decisions.

AI may assist, but human approval is mandatory and state mutation must be service-mediated.

---

# 10. Agent Output Status

AI outputs should use controlled statuses.

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

# 11. Core Agent Baseline

The following agents form the canonical Book 02 baseline.

```text
AI Governance Agent
Classification Assistant Agent
Document Draft Assistant Agent
Evidence Review Assistant Agent
Trademark Status Summary Agent
Office Action Assistant
Communication Summary Agent
Opportunity Discovery Agent
Routing Assistant Agent
Workflow Assistant Agent
Codex Implementation Agent
Spec Consistency Review Agent
```

These are not all necessarily Must Implement in MVP.

Their implementation depth is defined individually.

---

# 12. Agent Index Summary Table

| Agent ID | Agent Name | Category | Owning Domain/System | MVP Status | Risk |
|---------|------------|----------|----------------------|------------|------|
| AGT-AI-GOV-001 | AI Governance Agent | Governance | AI Governance | Must Implement | High |
| AGT-CLS-001 | Classification Assistant Agent | Professional Assistance | Classification | Must Implement / Partial | High |
| AGT-DOC-001 | Document Draft Assistant Agent | Professional Assistance | Document | Partial Implement | High |
| AGT-EVD-001 | Evidence Review Assistant Agent | Professional Assistance | Evidence | Partial Implement | High |
| AGT-TM-001 | Trademark Status Summary Agent | Professional Assistance | Trademark | Must Implement / Partial | Medium |
| AGT-OA-001 | Office Action Assistant | Professional Assistance | Trademark / Document / Knowledge | Reserved Boundary | Critical |
| AGT-COMM-001 | Communication Summary Agent | Communication | Communication | Partial Implement | Medium |
| AGT-OPP-001 | Opportunity Discovery Agent | Opportunity and Routing | Opportunity | Reserved Boundary | Medium |
| AGT-ROUTE-001 | Routing Assistant Agent | Opportunity and Routing | Routing | Partial Implement | High |
| AGT-WF-001 | Workflow Assistant Agent | Execution Assistance | Workflow Contract / Task | Partial Implement | Medium |
| AGT-CODEX-001 | Codex Implementation Agent | Codex Implementation | Codex Task System | Must Implement | High |
| AGT-SPEC-001 | Spec Consistency Review Agent | Spec Review | Specification Governance | Partial Implement | Medium |

---

# 13. AGT-AI-GOV-001 — AI Governance Agent

## Purpose

The AI Governance Agent supports the enforcement of AI governance rules.

It helps check whether an AI capability has an Agent Contract, authorized knowledge, object access limits, risk level, review rule and audit requirement.

## Owning System

```text
AI Governance
```

## MVP Status

```text
Must Implement
```

## Allowed Capabilities

```text
check Agent Contract completeness
check missing authorized knowledge
check missing review rule
check missing audit rule
check risk level declaration
check prohibited capability declarations
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

## Events Emitted

```text
AgentContractValidated
AgentContractValidationFailed
AIUsagePolicyViolationDetected
AIReviewRequired
```

## Audit Requirement

```text
Required
```

## Acceptance Criteria

```text
[ ] Agent cannot operate without Agent Contract.
[ ] Agent checks governance completeness.
[ ] Agent cannot approve itself.
[ ] Agent produces audit record.
```

---

# 14. AGT-CLS-001 — Classification Assistant Agent

## Purpose

The Classification Assistant Agent assists with goods/services classification, Nice class mapping, local classification constraints and recommendation preparation.

## Owning Domain

```text
Classification
```

## MVP Status

```text
Must Implement / Partial Implement
```

## Risk Level

```text
High
```

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
bypass professional review for high-risk classification
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
Knowledge Asset
AI Recommendation
Review Record
```

## Related Services

```text
Classification Recommendation Service
Classification Validation Service
Knowledge Retrieval Service
Review Assignment Service
```

## Events Emitted

```text
ClassificationRecommendationGenerated
ClassificationReviewRequired
ClassificationRecommendationApproved
ClassificationRecommendationRejected
```

## Human Review Rule

```text
Required before client-facing final recommendation or filing use.
```

## Product Consumers

```text
MarkOrbit Lite
MarkReg
Workplace
```

## Acceptance Criteria

```text
[ ] Agent uses authorized classification knowledge.
[ ] Agent output is marked as Recommendation or ReviewRequired.
[ ] Agent cannot finalize official filing terms.
[ ] Agent emits review-required event when risk is high.
```

---

# 15. AGT-DOC-001 — Document Draft Assistant Agent

## Purpose

The Document Draft Assistant Agent assists with drafting, summarizing, translating or preparing professional documents.

## Owning Domain

```text
Document
```

## MVP Status

```text
Partial Implement
```

## Risk Level

```text
High
```

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

## Authorized Knowledge

```text
approved document templates
jurisdiction document requirements
Matter context
Trademark context
Knowledge Assets
```

## Related Objects

```text
Document
Document Requirement
AI Draft
AI Output
Review Record
```

## Related Services

```text
Document Requirement Service
Document Draft Service
Document Validation Service
Review Assignment Service
```

## Events Emitted

```text
DocumentDraftGenerated
DocumentReviewRequired
DocumentDraftApproved
DocumentDraftRejected
```

## Human Review Rule

```text
Required before external use.
```

## Product Consumers

```text
MarkReg
Workplace
MarkOrbit Lite
```

---

# 16. AGT-EVD-001 — Evidence Review Assistant Agent

## Purpose

The Evidence Review Assistant Agent assists with preliminary evidence review, evidence grouping and evidence sufficiency notes.

## Owning Domain

```text
Evidence
```

## MVP Status

```text
Partial Implement
```

## Risk Level

```text
High
```

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

## Authorized Knowledge

```text
evidence rules
jurisdiction requirements
Matter context
Document metadata
approved evidence examples
```

## Related Objects

```text
Evidence
Evidence Package
AI Review Note
Review Record
AI Audit Record
```

## Events Emitted

```text
EvidenceReviewGenerated
EvidenceReviewRequired
EvidencePackageFlagged
```

## Human Review Rule

```text
Required.
```

---

# 17. AGT-TM-001 — Trademark Status Summary Agent

## Purpose

The Trademark Status Summary Agent assists with summarizing trademark status and lifecycle information.

## Owning Domain

```text
Trademark
```

## MVP Status

```text
Must Implement / Partial Implement
```

## Risk Level

```text
Medium
```

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

## Authorized Knowledge

```text
official trademark data
jurisdiction status rules
Trademark Object
Matter Object
Knowledge Assets
```

## Related Objects

```text
Trademark
Trademark Status Summary
AI Summary
AI Audit Record
```

## Events Emitted

```text
TrademarkStatusSummaryGenerated
TrademarkStatusReviewRequired
```

## Human Review Rule

```text
Required for client-facing legal interpretation.
```

---

# 18. AGT-OA-001 — Office Action Assistant

## Purpose

The Office Action Assistant supports analysis and draft response preparation for official refusals or office actions.

## Owning Domains

```text
Trademark
Document
Knowledge
Evidence
```

## MVP Status

```text
Reserved Boundary
```

## Risk Level

```text
Critical
```

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

## Authorized Knowledge

```text
official office action document
jurisdiction law/practice knowledge
case context
approved templates
reviewed prior examples
```

## Related Objects

```text
Office Action
Document
Evidence
AI Draft
Review Record
AI Audit Record
```

## Events Emitted

```text
OfficeActionSummaryGenerated
OfficeActionReviewRequired
OfficeActionDraftGenerated
```

## Human Review Rule

```text
Mandatory.
```

---

# 19. AGT-COMM-001 — Communication Summary Agent

## Purpose

The Communication Summary Agent assists with summarizing and linking communications to Core Objects such as Matter, Task, Customer, Agent or Document.

## Owning Domain

```text
Communication
```

## MVP Status

```text
Partial Implement
```

## Risk Level

```text
Medium
```

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
Matter
Task
Agent
Customer
AI Summary
```

## Events Emitted

```text
CommunicationSummaryGenerated
CommunicationLinkedToMatter
CommunicationActionItemDetected
```

## Human Review Rule

```text
Required before external reply or binding action.
```

---

# 20. AGT-OPP-001 — Opportunity Discovery Agent

## Purpose

The Opportunity Discovery Agent identifies possible business opportunities from trademark, customer, jurisdiction, status or portfolio signals.

## Owning Domain

```text
Opportunity
```

## MVP Status

```text
Reserved Boundary
```

## Risk Level

```text
Medium
```

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
Customer
Trademark
Jurisdiction
AI Recommendation
Responsibility Assignment
```

## Events Emitted

```text
OpportunitySignalDetected
OpportunityCreated
OpportunityReviewRequired
```

## Human Review Rule

```text
Required before sales action.
```

---

# 21. AGT-ROUTE-001 — Routing Assistant Agent

## Purpose

The Routing Assistant Agent assists with recommending internal assignees, foreign agents or service providers.

## Owning Domain

```text
Routing
```

## MVP Status

```text
Partial Implement
```

## Risk Level

```text
High
```

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

## Authorized Knowledge

```text
Agent data
Service Provider data
Capability data
Jurisdiction context
Matter context
Routing rules
```

## Related Objects

```text
Routing Decision
Agent
Service Provider
Capability
Matter
Responsibility Assignment
```

## Events Emitted

```text
RoutingRecommendationGenerated
RoutingReviewRequired
RoutingDecisionMade
```

## Human Review Rule

```text
Required for external assignment or provider selection.
```

---

# 22. AGT-WF-001 — Workflow Assistant Agent

## Purpose

The Workflow Assistant Agent assists with task sequencing, review reminders, workflow progress and execution coordination.

## Owning Domains

```text
Workflow Contract
Task
Matter
```

## MVP Status

```text
Partial Implement
```

## Risk Level

```text
Medium
```

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
Task
Matter
Review Record
Notification
AI Recommendation
```

## Events Emitted

```text
WorkflowProgressSummarized
NextTaskSuggested
WorkflowReviewRequired
```

## Human Review Rule

```text
Required when state transition affects legal or business responsibility.
```

---

# 23. AGT-CODEX-001 — Codex Implementation Agent

## Purpose

The Codex Implementation Agent assists with implementing approved Core specifications.

It consumes Book 02, appendices, indexes, `core-specs/` and Codex tasks.

It must not define architecture.

## Owning System

```text
Codex Task System
```

## MVP Status

```text
Must Implement
```

## Risk Level

```text
High
```

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
Codex Task Index
Codex task files
```

## Related Objects

```text
Codex Task
Spec File
Acceptance Criteria
Test Fixture
Implementation Artifact
```

## Events Emitted

```text
CodexTaskStarted
CodexTaskImplemented
CodexTaskTested
CodexTaskBlocked
CodexTaskAccepted
```

## Human Review Rule

```text
Required for acceptance.
```

## Acceptance Criteria

```text
[ ] Every implementation references approved source specs.
[ ] Every task has tests.
[ ] No deferred scope is implemented without approval.
[ ] Architecture is not invented by Codex.
```

---

# 24. AGT-SPEC-001 — Spec Consistency Review Agent

## Purpose

The Spec Consistency Review Agent assists with reviewing manuscript, appendices, indexes and `core-specs/` for consistency.

## Owning System

```text
Specification Governance
```

## MVP Status

```text
Partial Implement
```

## Risk Level

```text
Medium
```

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

## Events Emitted

```text
SpecConsistencyIssueDetected
SpecReviewRequired
SpecReviewCompleted
```

## Human Review Rule

```text
Required for architecture changes.
```

---

# 25. External Professional Agent Boundary

External Professional Agent refers to foreign associates, law firms, local agents or service providers.

They are not AI Agents.

They belong primarily to:

```text
Agent
Service Provider
Routing
Communication
Service Network
Capability
Business Responsibility
```

External Professional Agents may be represented by Core Objects and services.

They may consume or provide professional work through contracts.

They do not operate under AI Agent Contract unless AI is acting on their behalf, which requires separate governance.

---

# 26. System Agent Boundary

System Agents may perform scheduled or automated tasks.

Examples:

```text
deadline checker
status sync worker
notification dispatcher
event processor
data import validator
audit recorder
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

System Agents are not allowed to bypass Core Services.

---

# 27. Agent-to-Object Mapping

| Agent | Primary Objects |
|------|-----------------|
| AI Governance Agent | AI Agent, Agent Contract, AI Audit Record |
| Classification Assistant Agent | Classification Recommendation, Trademark, Jurisdiction |
| Document Draft Assistant Agent | Document, Document Requirement, AI Draft |
| Evidence Review Assistant Agent | Evidence, Evidence Package, Review Record |
| Trademark Status Summary Agent | Trademark, Trademark Status Summary |
| Office Action Assistant | Office Action, Document, Evidence, AI Draft |
| Communication Summary Agent | Communication, Matter, Task |
| Opportunity Discovery Agent | Opportunity, Customer, Trademark |
| Routing Assistant Agent | Routing Decision, Agent, Service Provider |
| Workflow Assistant Agent | Workflow Contract, Task, Matter |
| Codex Implementation Agent | Codex Task, Spec File, Test Fixture |
| Spec Consistency Review Agent | Spec File, Appendix, Index, Review Record |

---

# 28. Agent-to-Service Mapping

| Agent | Primary Services |
|------|------------------|
| AI Governance Agent | Agent Contract Validation Service |
| Classification Assistant Agent | Classification Recommendation Service |
| Document Draft Assistant Agent | Document Draft Service |
| Evidence Review Assistant Agent | Evidence Review Service |
| Trademark Status Summary Agent | Trademark Status Summary Service |
| Office Action Assistant | Office Action Analysis Service |
| Communication Summary Agent | Communication Summary Service |
| Opportunity Discovery Agent | Opportunity Discovery Service |
| Routing Assistant Agent | Routing Recommendation Service |
| Workflow Assistant Agent | Workflow Assistance Service |
| Codex Implementation Agent | Codex Task Execution Service |
| Spec Consistency Review Agent | Spec Consistency Check Service |

---

# 29. Agent-to-Event Mapping

| Agent | Events |
|------|--------|
| AI Governance Agent | AgentContractValidated, AIUsagePolicyViolationDetected |
| Classification Assistant Agent | ClassificationRecommendationGenerated, ClassificationReviewRequired |
| Document Draft Assistant Agent | DocumentDraftGenerated, DocumentReviewRequired |
| Evidence Review Assistant Agent | EvidenceReviewGenerated, EvidenceReviewRequired |
| Trademark Status Summary Agent | TrademarkStatusSummaryGenerated |
| Office Action Assistant | OfficeActionSummaryGenerated, OfficeActionReviewRequired |
| Communication Summary Agent | CommunicationSummaryGenerated, CommunicationActionItemDetected |
| Opportunity Discovery Agent | OpportunitySignalDetected, OpportunityReviewRequired |
| Routing Assistant Agent | RoutingRecommendationGenerated, RoutingReviewRequired |
| Workflow Assistant Agent | NextTaskSuggested, WorkflowReviewRequired |
| Codex Implementation Agent | CodexTaskStarted, CodexTaskImplemented, CodexTaskTested |
| Spec Consistency Review Agent | SpecConsistencyIssueDetected, SpecReviewRequired |

---

# 30. Agent API Surface Baseline

Agent APIs must be contract-bound.

MVP or partial API surfaces may include:

```text
AI Governance API
Classification Recommendation API
Document Draft API
Trademark Status Summary API
Communication Summary API
Routing Recommendation API
Workflow Assistance API
Codex Task Execution API
Spec Consistency Review API
```

Deferred or reserved API surfaces may include:

```text
Office Action Assistant API
Evidence Review API
Opportunity Discovery API
Full Provider Ranking API
Full AI Legal Strategy API
```

Agent APIs must be indexed in Appendix F before implementation.

---

# 31. Agent Audit Requirements

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

# 32. Agent Anti-Patterns

The following patterns are prohibited.

## 32.1 Prompt as Agent

A prompt is treated as a governed agent.

Correction:

```text
Create Agent Identity and Agent Contract first.
```

## 32.2 AI Without Review

AI output is used directly in high-risk professional work.

Correction:

```text
Apply risk level and human review rule.
```

## 32.3 AI Mutates Core State Directly

An agent changes Core Objects without Service Specification.

Correction:

```text
Use governed Core Service and emit Events.
```

## 32.4 AI Uses Unauthorized Knowledge

An agent uses unapproved sources or generated content as professional truth.

Correction:

```text
Use authorized Knowledge Sources and Knowledge Assets.
```

## 32.5 Codex Invents Architecture

Codex creates domains, objects or events not in approved specs.

Correction:

```text
Require Codex Task Contract and source spec references.
```

## 32.6 Agent Expands MVP Scope

An agent implements future product functions too early.

Correction:

```text
Use MVP / Partial / Future classification.
```

---

# 33. core-specs/agents Readiness

This appendix prepares future `core-specs/agents/`.

Expected scaffold:

```text
core-specs/agents/README.md
core-specs/agents/_template.md
core-specs/agents/ai-governance-agent.md
core-specs/agents/classification-assistant-agent.md
core-specs/agents/document-draft-assistant-agent.md
core-specs/agents/trademark-status-summary-agent.md
core-specs/agents/routing-assistant-agent.md
core-specs/agents/workflow-assistant-agent.md
core-specs/agents/codex-implementation-agent.md
core-specs/agents/spec-consistency-review-agent.md
```

Detailed agent specs should not be generated until Appendix H and baseline indexes are complete.

---

# 34. Handoff to Appendix H

Appendix H — Codex Task Index must use this Agent Index to generate AI and Codex-related implementation tasks.

Appendix H should include task groups for:

```text
Agent Contract template
AI Agent Identity object
AI Output object
AI Audit Record object
Agent Index validation
AI Governance baseline
Classification Assistant baseline
Trademark Status Summary baseline
Codex Implementation Agent constraints
Spec Consistency Review Agent baseline
agent tests and fixtures
```

Codex tasks must not implement unindexed agents.

---

# 35. Acceptance Criteria

This appendix is accepted only if it satisfies the following criteria.

```text
[ ] It defines Agent clearly.
[ ] It distinguishes Agent from prompt.
[ ] It defines required Agent Contract fields.
[ ] It defines Agent Index fields.
[ ] It includes MVP agent baseline.
[ ] It includes AI Governance Agent.
[ ] It includes Classification Assistant Agent.
[ ] It includes Document Draft Assistant Agent.
[ ] It includes Evidence Review Assistant Agent.
[ ] It includes Trademark Status Summary Agent.
[ ] It includes Office Action Assistant as reserved/critical.
[ ] It includes Communication Summary Agent.
[ ] It includes Opportunity Discovery Agent.
[ ] It includes Routing Assistant Agent.
[ ] It includes Workflow Assistant Agent.
[ ] It includes Codex Implementation Agent.
[ ] It includes Spec Consistency Review Agent.
[ ] It defines risk levels.
[ ] It defines output statuses.
[ ] It maps agents to objects, services and events.
[ ] It defines audit requirements.
[ ] It defines agent anti-patterns.
[ ] It prepares core-specs/agents/.
[ ] It hands off to Appendix H.
```

---

# 36. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Agent Index for second canonical draft. Defines agent categories, baseline agents, Agent Contract requirements, AI governance boundaries, object/service/event mapping and Appendix H handoff. |

---

**End of Appendix**
