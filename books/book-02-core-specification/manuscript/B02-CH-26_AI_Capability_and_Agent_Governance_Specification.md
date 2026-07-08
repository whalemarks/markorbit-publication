# Book 02

# 26 — AI Capability and Agent Governance Specification

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-26  
**Chapter Title:** AI Capability and Agent Governance Specification  
**Part:** Part III — Core Specification System  
**Chapter Type:** Specification  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-03 — Core Position
- B02-CH-04 — Core Boundary
- B02-CH-05 — Core Principles
- B02-CH-12 — Canonical Models
- B02-CH-17 — Core Contract Architecture
- B02-CH-19 — Capability Specification
- B02-CH-20 — Knowledge Specification
- B02-CH-21 — Business Responsibility Specification
- B02-CH-23 — Object Specification
- B02-CH-24 — Service Specification
- B02-CH-25 — Event Specification
- B02-CH-27 — Core Consumption Specification
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines how AI capabilities and AI agents are specified and governed inside the MarkOrbit Core.

AI is important to MarkOrbit, but AI is not the Core.

AI may assist professional work, but AI must not replace professional responsibility.

AI may generate recommendations, drafts, summaries, classifications, routing suggestions and Codex implementation outputs, but those outputs must operate under Core governance.

This chapter establishes the specification rules for:

```text
AI Capability
AI Agent
Agent Contract
Authorized Knowledge
Structured Context
AI Output
AI Recommendation
AI Review
AI Audit
AI Event
AI Failure Behavior
AI Product Consumption
Codex Implementation Agent
```

The goal is to make AI useful without allowing it to become unbounded authority.

---

# 2. Core Question

This chapter answers one question:

> How should MarkOrbit use AI while preserving professional truth, Core boundaries, human responsibility, auditability and product consistency?

The answer is:

> AI must be treated as a governed Core capability executed through specified agents, controlled by Agent Contracts, bounded by authorized knowledge and object access, reviewed according to risk, audited through events, and consumed by products only through approved Core contracts.

---

# 3. AI Governance Statement

Book 02 uses the following AI governance statement.

```text
AI is a governed capability.
AI is not the Core.
AI is not above the Core.
AI is not a replacement for professional responsibility.
```

This statement is mandatory.

Every AI feature, agent, prompt, model integration, recommendation service or Codex task must conform to it.

---

# 4. AI Position in Core Architecture

AI sits inside Core governance but outside Core authority.

```text
Core Principles
        ↓
Core Domains / Objects / Services / Events / Contracts
        ↓
AI Capability Governance
        ↓
Agent Contract
        ↓
Governed AI Execution
        ↓
AI Output / Review / Audit
        ↓
Product or Workplace Consumption
```

AI may assist execution.

AI may not define Core meaning.

AI may not change Core state without Service, Permission, Event and Audit rules.

AI may not become a hidden product-local decision system.

---

# 5. Scope

## 5.1 In Scope

This chapter defines:

```text
AI Capability definition
AI Agent definition
Agent Contract requirements
AI capability categories
AI agent categories
authorized knowledge rules
structured context rules
object access rules
service access rules
output types
risk levels
human review rules
event rules
audit rules
failure behavior rules
product consumption rules
Codex implementation agent rules
Appendix G readiness
core-specs/agents readiness
```

## 5.2 Out of Scope

This chapter does not define:

```text
specific production prompts
model provider selection
model pricing
LLM infrastructure
embedding database implementation
vector store architecture
full RAG pipeline design
UI chat experience
prompt engineering library
vendor-specific AI APIs
fine-tuning strategy
complete evaluation benchmark suite
```

Those belong to AI implementation, product, infrastructure or later technical documents.

---

# 6. AI Capability Definition

An AI Capability is a governed ability to use AI to assist a specific Core or professional task.

An AI Capability must define:

```text
capability name
purpose
owning domain or cross-cutting system
allowed inputs
allowed knowledge
allowed object access
allowed services
output type
risk level
human review requirement
event requirements
audit requirements
product consumers
MVP status
```

AI Capability is related to, but not identical with, the cross-cutting Capability system.

The cross-cutting Capability system may describe whether an actor can perform a type of work.

AI Capability defines whether and how an AI agent may assist that work.

---

# 7. AI Agent Definition

An AI Agent is a governed execution actor that performs one or more AI Capabilities under an Agent Contract.

An AI Agent is not merely:

```text
a prompt
a model
a chat interface
a workflow node
a vendor API wrapper
a script
a product feature
```

An AI Agent must have:

```text
identity
purpose
owning domain or system
allowed capabilities
prohibited capabilities
authorized knowledge
allowed object access
allowed services
output types
risk level
review rules
events
audit
failure behavior
product consumers
versioning
acceptance criteria
```

If these elements are not specified, the AI behavior is not a Core-governed AI Agent.

---

# 8. Agent Contract

An Agent Contract is the mandatory governance document for an AI Agent.

No AI Agent may operate without an Agent Contract.

## 8.1 Required Agent Contract Fields

Each Agent Contract must include:

```text
agent name
agent identity
agent purpose
owning domain or cross-cutting system
allowed capabilities
prohibited capabilities
authorized knowledge sources
allowed object access
allowed service access
structured context requirements
permission and policy requirements
input contract
output contract
risk level
human review rule
event requirements
audit requirements
failure behavior
product consumers
MVP status
version
acceptance criteria
revision notes
```

## 8.2 Agent Contract Rule

```text
Agent Contract before AI execution.
```

This rule applies to all AI usage, including Codex-related implementation tasks.

---

# 9. AI Capability Categories

The Core recognizes the following AI capability categories.

```text
Consultation Assistance
Classification Assistance
Knowledge Retrieval Assistance
Document Drafting Assistance
Evidence Review Assistance
Trademark Status Summary
Office Action Assistance
Communication Summary
Opportunity Discovery
Routing Assistance
Workflow Assistance
Codex Implementation Assistance
Spec Consistency Review
```

These categories are not product features by themselves.

They are governance categories used to classify AI work.

---

# 10. AI Agent Categories

Appendix G should index AI agents by category.

Initial agent categories include:

```text
Classification Assistant Agent
Document Draft Assistant Agent
Evidence Review Assistant Agent
Trademark Status Summary Agent
Office Action Assistant Agent
Communication Summary Agent
Opportunity Discovery Agent
Routing Assistant Agent
Workflow Assistant Agent
Codex Implementation Agent
Spec Consistency Review Agent
```

Each agent must be tied to:

```text
one or more Core Domains
or one cross-cutting specification system
or one governed implementation task class
```

---

# 11. AI Agent Identity

Every AI Agent must have Core identity.

AI Agent Identity supports:

```text
audit
event attribution
permission checks
output ownership
review routing
product consumption control
version tracking
failure analysis
```

An AI Agent Identity is different from a model name.

For example:

```text
Model name:
    GPT-based model provider name

AI Agent Identity:
    Classification Assistant Agent v1.0
```

The model may change.

The Agent Identity must remain governed by Core.

---

# 12. Authorized Knowledge

AI may only use authorized knowledge.

Authorized knowledge may include:

```text
approved Knowledge Sources
approved Knowledge Assets
jurisdiction rules
classification references
document requirements
case context
trademark status data
approved templates
approved internal notes
approved foreign agent records
```

AI must not treat unvalidated material as professional truth.

AI-generated text is not validated knowledge unless it passes validation and review rules.

---

# 13. Structured Context

AI must operate with structured context where possible.

Structured context may include:

```text
Customer
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
Order
Matter
Task
Workflow Contract
Communication
Agent
Service Provider
Responsibility Assignment
```

Structured context prevents AI from guessing.

Where structured context is missing, the agent must either:

```text
ask for missing information
return uncertainty
produce a draft requiring review
create a Knowledge Gap
create a ReviewRequired event
```

---

# 14. Object Access Rules

AI object access must be explicit.

An Agent Contract must define whether the agent may:

```text
read an object
summarize an object
recommend changes
create draft content
create review records
trigger services
write state changes
```

The default rule is:

```text
AI may read only what its Agent Contract authorizes.
AI may not write Core state unless a governed Core Service permits it.
```

---

# 15. Service Access Rules

AI must not bypass Core Services.

If AI needs to operate Core meaning, it must use a governed service.

Examples:

```text
Classification Assistant Agent
    may call Classification Recommendation Service.

Document Draft Assistant Agent
    may call Document Draft Generation Service.

Routing Assistant Agent
    may call Routing Recommendation Service.

Workflow Assistant Agent
    may call Task Recommendation or Review Routing Service.
```

AI must not directly mutate objects outside service rules.

---

# 16. AI Output Types

AI output must be typed.

Common AI Output types include:

```text
summary
recommendation
draft
classification suggestion
risk note
missing information list
knowledge gap
routing suggestion
review checklist
status explanation
Codex implementation draft
spec consistency finding
```

Every output type must define:

```text
whether it is advisory or executable
whether it requires human review
whether it may trigger an event
whether it may be shown to a product user
whether it may be stored
whether it may be used by another agent
```

---

# 17. AI Recommendation

An AI Recommendation is an AI Output that proposes a professional or operational action.

Examples:

```text
recommended trademark class
recommended goods/services term
recommended document requirement
recommended agent routing
recommended matter priority
recommended reply draft
recommended opportunity follow-up
recommended Codex implementation step
```

An AI Recommendation is not final professional judgment.

It must carry:

```text
basis
confidence or uncertainty note
source knowledge reference
risk level
review requirement
consumer boundary
```

---

# 18. AI Review Rules

AI output must have a review rule.

Review levels include:

```text
No Review Required
Human Review Recommended
Human Review Required
Professional Approval Required
Architecture Review Required
```

Examples:

```text
low-risk summary
    Human Review Recommended

classification recommendation for filing
    Human Review Required

office action response draft
    Professional Approval Required

new Core domain suggestion from Codex
    Architecture Review Required
```

Review rules must be defined in the Agent Contract.

---

# 19. AI Risk Levels

AI risk levels should be explicit.

Recommended baseline risk levels:

```text
Low
Medium
High
Critical
```

## 19.1 Low Risk

Examples:

```text
internal summary
non-authoritative explanation
draft note
```

## 19.2 Medium Risk

Examples:

```text
classification suggestion
document checklist suggestion
communication draft
```

## 19.3 High Risk

Examples:

```text
office action response draft
legal risk analysis
evidence sufficiency recommendation
agent routing recommendation with business impact
```

## 19.4 Critical Risk

Examples:

```text
final legal conclusion
automated filing decision
automated rejection of client request
automated professional approval
automated Core architecture change
```

Critical-risk AI outputs should normally be prohibited or require explicit professional/architecture approval.

---

# 20. AI Events

AI activity must produce events when it affects Core execution, review, audit or downstream coordination.

AI-related events may include:

```text
AIRecommendationGenerated
AIRecommendationReviewRequired
AIRecommendationApproved
AIRecommendationRejected
AIDraftGenerated
AIDraftReviewRequired
AIDraftApproved
AIDraftRejected
AIKnowledgeGapDetected
AIOutputStored
AIOutputDiscarded
AgentContractUpdated
AIAuditRecorded
CodexDraftGenerated
SpecConsistencyIssueDetected
```

AI events must not be informal logs.

They must represent meaningful execution or governance changes.

---

# 21. AI Audit

AI audit is mandatory for governed AI execution.

An AI Audit Record should capture:

```text
agent identity
agent contract version
input context
knowledge sources used
objects accessed
services invoked
output type
risk level
review rule
review result
events emitted
user or system actor
model/provider reference where relevant
failure or uncertainty note
timestamp
```

AI audit should support:

```text
professional accountability
risk review
quality improvement
incident analysis
architecture governance
client service traceability
```

---

# 22. AI Failure Behavior

Each Agent Contract must define failure behavior.

Failure behaviors may include:

```text
return uncertainty
ask for missing information
create Knowledge Gap
create ReviewRequired event
stop execution
escalate to human reviewer
refuse prohibited task
log audit record
```

AI must not silently fabricate missing facts.

AI must not continue execution when required knowledge, permission or context is missing.

---

# 23. AI and Permission

AI must follow permission rules.

Permission applies to:

```text
knowledge access
object access
document access
customer data
matter data
agent records
communication records
AI output visibility
service invocation
product display
```

AI should not receive broader access than needed.

The default permission principle is:

```text
Least authorized context.
```

---

# 24. AI and Policy

Policy governs AI decisions and constraints.

Policy may define:

```text
risk thresholds
review requirements
jurisdiction restrictions
data exposure restrictions
document confidentiality
client visibility
agent communication rules
professional approval rules
AI output retention rules
```

Policy is partial in the Core MVP but must be considered in Agent Contracts.

---

# 25. AI and Knowledge Gaps

AI should surface knowledge gaps instead of hiding them.

A Knowledge Gap may be created when:

```text
jurisdiction rule is missing
classification reference is insufficient
document requirement is unknown
trademark status cannot be verified
case context is incomplete
agent record is outdated
professional template is missing
```

Knowledge Gap outputs should support future Knowledge domain improvement.

---

# 26. AI and Product Consumers

Products may consume AI output only through approved boundaries.

Product consumers include:

```text
MarkReg
MarkOrbit Lite
Workplace
MGSN baseline
Future Partner Center
Future Client Portal
Future Service Platform
Reporting Consumers
```

Each AI output must define:

```text
internal only
reviewer visible
client visible
agent visible
product visible after approval
not product-visible
```

AI output must not leak internal reasoning, confidential notes or unauthorized knowledge.

---

# 27. AI and Workplace

Workplace consumes AI to improve professional execution.

AI may help Workplace with:

```text
task prioritization
review checklist generation
matter summary
document draft review
communication summary
routing recommendation
workflow assistance
missing information detection
```

Workplace must preserve human responsibility.

AI may suggest.

Workplace coordinates review and action.

---

# 28. AI and Codex

Codex is a special AI-assisted implementation actor.

Codex may help implement approved specifications.

Codex may not define Core architecture.

Codex-related AI rules:

```text
Codex consumes approved specs.
Codex does not invent domains.
Codex does not redefine objects.
Codex does not invent events.
Codex does not expand MVP scope.
Codex tasks require source references.
Codex outputs require tests and acceptance criteria.
```

A Codex Implementation Agent must have an Agent Contract.

Spec Consistency Review Agent may assist with checking architecture drift, but architecture approval remains human/governance-owned.

---

# 29. AI Governance Template

Each AI Agent specification should follow this template.

```text
# Agent Name

1. Agent Purpose
2. Agent Identity
3. Owning Domain or System
4. Allowed Capabilities
5. Prohibited Capabilities
6. Authorized Knowledge
7. Allowed Object Access
8. Allowed Service Access
9. Structured Context Requirements
10. Input Contract
11. Output Contract
12. Risk Level
13. Human Review Rule
14. Events Emitted
15. Audit Requirements
16. Failure Behavior
17. Permission and Policy Rules
18. Product Consumers
19. MVP Phase and Depth
20. Out of Scope
21. Acceptance Criteria
22. Revision Notes
```

This template should be used for `core-specs/agents/` and Appendix G.

---

# 30. MVP AI Baseline

The Core MVP should include a limited AI governance baseline.

## 30.1 Must Specify

```text
AI Agent Identity
Agent Contract
AI Output
AI Recommendation
AI Audit Record
Review Record
AI Events baseline
```

## 30.2 Must Implement or Partially Implement

```text
Classification Assistant Agent
Document Draft Assistant Agent
Trademark Status Summary Agent
Communication Summary Agent
Codex Implementation Agent
Spec Consistency Review Agent
```

## 30.3 Partial or Reserved

```text
Evidence Review Assistant Agent
Office Action Assistant Agent
Routing Assistant Agent
Opportunity Discovery Agent
Workflow Assistant Agent
```

## 30.4 Deferred

```text
fully autonomous legal decision-making
fully autonomous filing
fully autonomous agent selection
full opportunity scoring engine
full marketplace AI matching
autonomous architecture modification
```

---

# 31. AI Anti-Patterns

The following AI patterns are prohibited.

## 31.1 Prompt-Only Agent

A prompt is treated as an agent.

Correction:

```text
Agent Contract is required.
```

## 31.2 Ungoverned AI Output

AI output is stored or shown without risk, review or audit.

Correction:

```text
AI Output requires output type, risk level, review rule and audit.
```

## 31.3 AI Defines Core Meaning

AI invents a domain, object, service or event.

Correction:

```text
Architecture governance must approve Core meaning.
```

## 31.4 AI Writes Directly to Core State

AI changes objects without service, permission, event or audit.

Correction:

```text
AI must operate through governed Core Services.
```

## 31.5 AI Uses Unauthorized Knowledge

AI draws from unapproved sources.

Correction:

```text
Authorized Knowledge must be defined in Agent Contract.
```

## 31.6 AI Becomes Final Professional Authority

AI output is treated as final legal or professional decision.

Correction:

```text
Professional responsibility and review rules govern final decisions.
```

## 31.7 Codex Expands Scope

Codex implements deferred scope without approval.

Correction:

```text
Codex tasks must include prohibited overreach and MVP boundaries.
```

---

# 32. Relationship to Appendix C

Appendix C — Core Object Index must include AI governance objects such as:

```text
AI Agent
AI Capability
AI Output
AI Recommendation
AI Audit Record
Agent Contract
Review Record
Responsibility Assignment
Capability
Capability Provider
Policy Rule
Permission Rule
```

These objects must not be left as implementation details.

---

# 33. Relationship to Appendix G

Appendix G — Agent Index must list governed AI agents.

Appendix G entries should include:

```text
agent name
agent identity
agent contract
allowed capabilities
prohibited capabilities
authorized knowledge
allowed object access
risk level
human review
events
audit
product consumers
MVP status
```

Appendix G is mandatory before detailed `core-specs/agents/` generation.

---

# 34. Relationship to core-specs/

This chapter prepares the future `core-specs/agents/` scaffold.

`core-specs/agents/` should include:

```text
agent spec files
Agent Contract template
AI Output template
AI Audit Record spec
AI Event specs
Agent-to-Service mapping
Agent-to-Knowledge mapping
Agent-to-Product consumer mapping
```

Detailed agent specs must not be generated before Appendix G is complete.

---

# 35. Relationship to Events

AI activity must use the Event Specification rules from Chapter 25.

AI-related events must define:

```text
source system
trigger
payload contract
related objects
consumer domains
review requirement
audit requirement
retention rule
```

AI events are semantic governance events, not logs.

---

# 36. Relationship to Services

AI agents may assist Core Services.

AI agents may not replace service governance.

Service specs involving AI must define:

```text
AI usage mode
allowed agent
input context
output type
review rule
event side effects
audit rule
failure behavior
```

---

# 37. Relationship to Business Responsibility

AI output must be tied to responsibility.

Responsibility may include:

```text
who requested AI output
who reviews AI output
who approves AI output
who acts on AI output
who is accountable for final decision
```

Business Responsibility is therefore essential to AI governance.

---

# 38. Specification Output

This chapter produces the following specification outputs:

```text
AI Governance Statement
AI Capability Definition
AI Agent Definition
Agent Contract Requirements
AI Capability Categories
AI Agent Categories
Authorized Knowledge Rules
Structured Context Rules
Object Access Rules
Service Access Rules
AI Output Types
AI Recommendation Rules
AI Review Rules
AI Risk Levels
AI Event Rules
AI Audit Rules
AI Failure Behavior Rules
AI Permission and Policy Rules
AI Product Consumption Rules
Codex AI Rules
AI Agent Specification Template
MVP AI Baseline
AI Anti-Patterns
Appendix C / G readiness requirements
core-specs/agents readiness requirements
```

---

# 39. Execution Mapping

| AI Governance Decision | Execution Impact |
|------------------------|------------------|
| AI is governed capability | AI features require Agent Contracts |
| AI is not Core authority | AI cannot define domains/objects/events |
| Authorized Knowledge required | Knowledge access must be explicit |
| Object access controlled | Agent specs must declare allowed objects |
| Service access controlled | AI must use governed services |
| Output typed | AI Output objects require type and review status |
| Risk level required | Review and audit depend on risk |
| Events required | AI execution changes must be observable |
| Audit required | AI outputs must be traceable |
| Codex governed | Codex tasks must reference approved specs |

---

# 40. Exclusions

This chapter shall not define:

```text
production prompts
model provider contracts
model selection criteria
fine-tuning process
vector database design
embedding strategy
AI UI chat design
complete evaluation benchmark
vendor-specific AI API integration
AI infrastructure deployment
```

Those belong to later AI implementation documents.

---

# 41. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It states that AI is a governed capability.
[ ] It states that AI is not the Core.
[ ] It states that AI is not above the Core.
[ ] It states that AI is not a replacement for professional responsibility.
[ ] It defines AI Capability.
[ ] It defines AI Agent.
[ ] It requires Agent Contract before AI execution.
[ ] It defines required Agent Contract fields.
[ ] It defines authorized knowledge rules.
[ ] It defines structured context rules.
[ ] It defines object and service access rules.
[ ] It defines AI Output and AI Recommendation.
[ ] It defines risk levels and review rules.
[ ] It defines AI event and audit requirements.
[ ] It defines Codex Implementation Agent boundaries.
[ ] It includes MVP AI baseline.
[ ] It includes AI anti-patterns.
[ ] It prepares Appendix C and Appendix G.
[ ] It prepares core-specs/agents/.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 42. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 26, defining AI capability and agent governance. |
| 0.2.0 | Draft | Second canonical draft rewrite. Strengthened AI as governed capability, Agent Contract, authorized knowledge, structured context, AI output/review/audit, Codex boundaries, MVP AI baseline and Appendix C/G readiness. |

---

**End of Chapter**
