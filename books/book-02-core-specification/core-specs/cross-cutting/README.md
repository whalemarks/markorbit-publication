# core-specs/cross-cutting/

**Repository:** `book-02-core`  
**Directory:** `core-specs/cross-cutting/`  
**Document:** `core-specs/cross-cutting/README.md`  
**Book:** Book 02 — MarkOrbit Core Specification  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Directory Purpose

The `core-specs/cross-cutting/` directory contains specifications for Core systems that operate across multiple baseline Core Domains.

A cross-cutting Core specification system is not an ordinary baseline Core Domain.

It defines a governed layer of meaning, responsibility, capability, policy, review, audit or implementation control that must be applied consistently across Domains, Objects, Services, Events, APIs, Agents, Workflows and Codex tasks.

This directory exists to prevent cross-domain concepts from being silently misclassified as ordinary domains or scattered across product code.

It provides a controlled place for specifications such as:

```text
Capability
Business Responsibility
AI Governance references
Specification Governance references
Codex Governance references
Policy references
Review and Approval references
Audit references
```

---

# 2. Canonical Cross-Cutting Rule

Book 02 uses the following canonical rule:

```text
Capability and Business Responsibility are cross-cutting Core specification systems.
They are not counted as additional baseline Core Domains.
```

Therefore:

```text
The baseline Core Domain Map remains 26 domains.
Capability is not silently added as domain 27.
Business Responsibility is not silently added as domain 28.
Cross-cutting systems may own specs, objects, services, contracts and validation rules.
Cross-cutting systems must be explicitly marked.
```

---

# 3. Cross-Cutting Is Not Domain Expansion

A cross-cutting system is not automatically:

```text
a new Core Domain
a product module
a UI section
a database schema
a background service
a reporting category
a shortcut for unclear ownership
```

A cross-cutting system exists only when the same governed responsibility must apply across multiple domains.

Cross-cutting systems must not be used to bypass domain ownership.

---

# 4. Directory Boundary

## 4.1 cross-cutting/ Owns

This directory owns:

```text
Cross-Cutting Specification files
Capability specification rules
Business Responsibility specification rules
cross-domain ownership rules
cross-domain responsibility rules
cross-domain capability rules
cross-domain review and approval rules
cross-domain policy references
cross-domain AI governance references
cross-domain audit references
cross-domain Codex governance references
validation rules for cross-cutting systems
prohibited overreach rules
acceptance criteria
```

## 4.2 cross-cutting/ Does Not Own

This directory does not own:

```text
ordinary baseline Core Domain files
product modules
product UI
physical database schema
service implementation code
API endpoint code
AI Agent prompts
workflow screen flows
pricing policy
sales policy
external marketplace rules
Codex execution code
```

Those belong to other specification layers or product books.

---

# 5. Source Chain

Every Cross-Cutting Specification file must cite its source chain.

Required source chain:

```text
B02-CH-19 — Capability Specification
B02-CH-21 — Business Responsibility Specification
B02-CH-26 — AI Capability and Agent Governance Specification
B02-CH-27 — Core Consumption Specification
B02-APP-A — Glossary
indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
core-specs/cross-cutting/{spec-name}.md
codex-tasks/{task}.md
```

Related sources may include:

```text
B02-CH-05 — Core Principles
B02-CH-08 — Ontology and Domain Classification
B02-CH-13 — Core Domain Architecture
B02-CH-17 — Core Contract Architecture
B02-CH-28 — Core MVP Boundary
B02-CH-29 — MVP Domain Priority
B02-CH-30 — MVP Execution Matrix
B02-CH-31 — Codex Implementation Roadmap
```

---

# 6. Required Cross-Cutting Spec Groups

Expected directory structure:

```text
core-specs/cross-cutting/README.md
core-specs/cross-cutting/_template.md

core-specs/cross-cutting/capability/
core-specs/cross-cutting/business-responsibility/
core-specs/cross-cutting/policy/
core-specs/cross-cutting/review-approval/
core-specs/cross-cutting/audit/
core-specs/cross-cutting/ai-governance/
core-specs/cross-cutting/specification-governance/
core-specs/cross-cutting/codex-governance/
```

Each subdirectory should contain specs for the corresponding cross-cutting system or governance concern.

---

# 7. Cross-Cutting Categories

This directory uses the following categories.

```text
Capability System
Business Responsibility System
Policy System
Review and Approval System
Audit System
AI Governance System
Specification Governance System
Codex Governance System
Validation System
```

A spec must use one canonical category.

---

# 8. Cross-Cutting Spec Metadata

Each Cross-Cutting Specification file must begin with metadata.

```text
# Cross-Cutting Specification — {Spec Name}

**Spec ID:** B02-XCUT-{SPEC-ID}
**Spec Type:** Cross-Cutting
**Spec Name:** {Spec Name}
**Cross-Cutting Category:** Capability | Business Responsibility | Policy | Review and Approval | Audit | AI Governance | Specification Governance | Codex Governance | Validation
**Owning System:** {Cross-Cutting System}
**Source Chapters:** B02-CH-19; B02-CH-21; B02-CH-26; B02-CH-27
**Source Indexes:** indexes/domain-index.md; indexes/object-index.md; indexes/service-index.md; indexes/event-index.md; indexes/api-index.md; indexes/agent-index.md
**Related Domain Specs:** core-specs/domains/{domain}.md
**Related Object Specs:** core-specs/objects/{object}.md
**Related Service Specs:** core-specs/services/{service}.md
**Related Event Specs:** core-specs/events/{event}.md
**Related Contract Specs:** core-specs/contracts/{contract}.md
**Related Agent Specs:** core-specs/agents/{agent}.md
**Status:** Draft
**Version:** 0.1.0
**MVP Phase/Wave:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Wave 0–7
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred
**Owner:** MarkOrbit Publications Editorial Board
```

---

# 9. Cross-Cutting Spec Required Sections

Every Cross-Cutting Specification must include the following sections.

```text
1. Purpose
2. Cross-Cutting Meaning
3. Cross-Cutting Category
4. Owning System
5. Scope
6. Boundary
7. Applies To
8. Does Not Apply To
9. Related Domains
10. Related Objects
11. Related Services
12. Related Events
13. Related Contracts
14. Related APIs
15. Related Agents
16. Workflow Usage
17. Policy Rules
18. Review and Approval Rules
19. Audit Rules
20. AI Governance Rules
21. Codex Governance Rules
22. MVP Scope
23. Deferred Scope
24. Data and Implementation Notes
25. Codex Implementation Notes
26. Validation Rules
27. Prohibited Overreach
28. Acceptance Criteria
29. Revision Notes
```

---

# 10. Capability System Rules

Capability defines what a Domain, Service, Agent, User, Organization or Service Provider is able and authorized to do within Core.

Capability is cross-cutting because it may apply to:

```text
Identity
Organization
User
Permission
Knowledge
Classification
Document
Evidence
Order
Matter
Task
Agent
Service Provider
Routing
AI Agents
Codex Implementation
```

Capability specs may define:

```text
capability identity
capability type
capability owner
capability scope
capability requirement
capability evidence
capability validation
capability matching
capability restriction
capability review
capability audit
```

Capability specs must not:

```text
be counted as an ordinary Core Domain
replace Permission
replace Business Responsibility
become a full marketplace ranking system in MVP
allow unreviewed provider selection
```

---

# 11. Business Responsibility System Rules

Business Responsibility defines accountable ownership for professional and operational decisions.

Business Responsibility is cross-cutting because responsibility may apply to:

```text
Order
Matter
Task
Workflow Contract
Classification
Document
Evidence
Review
Approval
Routing
Communication
AI Output
Codex Task
```

Business Responsibility specs may define:

```text
responsibility assignment
responsible actor
review owner
approval owner
task owner
matter owner
decision owner
escalation owner
handoff rules
accountability records
```

Business Responsibility specs must not:

```text
be counted as an ordinary Core Domain
replace Task
replace Workflow Contract
replace Permission
allow AI to own final professional responsibility
allow anonymous responsibility in professional workflows
```

---

# 12. Policy System Rules

Policy defines governed constraints applied before execution, exposure, review, AI use or Codex implementation.

Policy specs may define:

```text
policy source
policy scope
policy evaluation point
policy-sensitive objects
policy-sensitive services
policy-sensitive APIs
policy-sensitive agents
policy violation behavior
review requirement
audit requirement
```

Policy-sensitive areas include:

```text
Permission
Jurisdiction
Classification
Document
Evidence
AI Governance
Routing
Communication
External Integration
Codex Implementation
```

Policy specs must not hide policy rules inside product code.

---

# 13. Review and Approval System Rules

Review and Approval define how high-risk outputs, state transitions and decisions are checked before acceptance.

Review and Approval specs may define:

```text
review trigger
review owner
review status
approval trigger
approver role
approval object
blocking behavior
review events
approval events
rejection behavior
audit requirement
```

Review-sensitive outputs include:

```text
Classification Recommendation
Document Draft
Evidence Review Note
Routing Recommendation
AI Output
Office Action Draft
Workflow Transition
Codex Task Acceptance
```

Review and Approval specs must not allow AI to approve its own output.

---

# 14. Audit System Rules

Audit defines the trace requirements for governed execution.

Audit specs may define:

```text
audit trigger
audit object
audit content
audit event
audit retention meaning
audit consumer
audit access restriction
```

Audit is required for:

```text
AI output
AI recommendation
AI policy violation
professional recommendation
classification review
document draft
evidence review
routing recommendation
review and approval
permission change
responsibility assignment
workflow transition
Codex task execution
prohibited overreach detection
```

Audit specs must not be optional for high-risk execution.

---

# 15. AI Governance Cross-Cutting Rules

AI Governance defines how AI may operate across Core.

AI Governance specs must reference:

```text
AI Agent
AI Agent Identity
Agent Contract
Authorized Knowledge
AI Output
AI Recommendation
AI Audit Record
Review Record
Policy Rule
Permission Rule
```

AI Governance applies to:

```text
Knowledge
Classification
Trademark
Document
Evidence
Communication
Routing
Workflow Assistance
Spec Review
Codex Implementation
```

AI Governance must preserve:

```text
AI is a governed capability.
AI is not the Core.
AI is not above the Core.
AI is not a replacement for professional responsibility.
```

---

# 16. Specification Governance Rules

Specification Governance controls how manuscript, appendices, indexes and core-specs remain aligned.

Specification Governance specs may define:

```text
source chain validation
appendix-to-index validation
index-to-core-spec validation
metadata validation
ownership validation
status validation
MVP scope validation
prohibited-overreach validation
release readiness validation
```

Specification Governance must not rewrite architecture automatically.

Spec review may detect issues, but human editorial review accepts architecture changes.

---

# 17. Codex Governance Rules

Codex Governance controls implementation execution.

Codex Governance specs may define:

```text
Codex Task source requirements
Codex Task template requirements
implementation acceptance gates
test requirements
fixture requirements
prohibited-overreach checks
release candidate validation
```

Codex Governance must preserve:

```text
Codex implements approved Core specifications.
Codex does not define Core architecture.
```

Codex must not:

```text
invent Core Domains
invent Core Object meaning
invent Service responsibility
invent Event semantics
expand MVP scope
implement reserved systems as MVP
```

---

# 18. High-Priority Cross-Cutting Specs

Initial cross-cutting specs should include:

```text
capability/capability-system.md
capability/capability-record.md
capability/capability-validation.md
capability/capability-matching-boundary.md

business-responsibility/business-responsibility-system.md
business-responsibility/responsibility-assignment.md
business-responsibility/review-ownership.md
business-responsibility/approval-ownership.md
business-responsibility/escalation-rule.md

policy/policy-rule.md
policy/policy-evaluation.md
policy/ai-risk-policy.md
policy/jurisdiction-rule-policy.md
policy/data-exposure-policy.md

review-approval/review-rule.md
review-approval/approval-rule.md
review-approval/review-blocking-behavior.md

audit/audit-rule.md
audit/audit-record-requirement.md
audit/high-risk-execution-audit.md

ai-governance/authorized-knowledge.md
ai-governance/ai-output-review-rule.md
ai-governance/ai-audit-rule.md

specification-governance/source-chain-validation.md
specification-governance/index-consistency-validation.md
specification-governance/spec-status-validation.md

codex-governance/codex-source-requirement.md
codex-governance/prohibited-overreach-check.md
codex-governance/codex-acceptance-gate.md
```

---

# 19. MVP Depth Rules

Cross-cutting specs must use controlled MVP depth values.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

Recommended MVP depth:

```text
Capability: Partial Implement
Business Responsibility: Partial Implement
Policy: Partial Implement
Review and Approval: Must Implement where high-risk execution exists
Audit: Must Implement where AI, review, responsibility or Codex exists
AI Governance: Must Implement for AI Agent baseline
Specification Governance: Partial Implement
Codex Governance: Must Implement before Codex execution
```

---

# 20. Product Consumer Rules

Cross-cutting specs must classify consumers.

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

Products may consume cross-cutting specs.

Products must not redefine cross-cutting Core meaning.

---

# 21. Data and Implementation Notes

Cross-cutting specs may include implementation-facing notes.

Allowed notes:

```text
cross-domain references required
source chain must be validated
ownership must be explicit
review owner must be recorded
audit record must be emitted for high-risk execution
Codex task must cite source specs
policy evaluation must happen before exposure or mutation
AI output must reference Agent Contract and Authorized Knowledge
```

Prohibited notes:

```text
physical database schema
controller code
product UI design
workflow screen layout
vendor-specific infrastructure
unreviewed implementation shortcuts
```

---

# 22. Codex Implementation Rules

Codex tasks generated from cross-cutting specs must:

```text
cite the cross-cutting spec
cite source chapters and indexes
preserve cross-cutting classification
preserve the 26-domain baseline
preserve MVP depth
preserve deferred scope
write tests
follow prohibited-overreach rules
```

Codex must not:

```text
turn cross-cutting systems into ordinary domains
invent new baseline domains
create hidden policy behavior
create AI execution without Agent Contract
create responsibility records without accountable owner
create audit-optional high-risk execution
implement reserved systems as MVP
```

---

# 23. Validation Rules

The `core-specs/cross-cutting/` directory must pass the following checks.

```text
[ ] It contains README.md.
[ ] It contains _template.md before detailed specs.
[ ] Every cross-cutting spec has metadata.
[ ] Every cross-cutting spec has a category.
[ ] Every cross-cutting spec has an owning system.
[ ] Every cross-cutting spec cites source chapters and indexes.
[ ] Capability is not counted as a baseline Core Domain.
[ ] Business Responsibility is not counted as a baseline Core Domain.
[ ] Cross-cutting object ownership is explicit.
[ ] Cross-cutting service ownership is explicit.
[ ] Cross-cutting event usage is explicit.
[ ] Cross-cutting contract usage is explicit.
[ ] AI-related specs require Agent Contract, Authorized Knowledge, Review and Audit.
[ ] Responsibility-related specs require accountable owner.
[ ] Policy-related specs define evaluation point and violation behavior.
[ ] Codex-related specs define source requirements and prohibited overreach.
[ ] No cross-cutting spec bypasses Domain/Object/Service/Event ownership.
```

---

# 24. Prohibited Behavior

This directory must not:

```text
change the 26-domain baseline
silently promote Capability into an ordinary domain
silently promote Business Responsibility into an ordinary domain
use cross-cutting specs as unclear ownership dumping ground
create unowned objects
create services without owners
create policies hidden from service/API specs
allow AI execution without Agent Contract
allow AI output without audit
allow AI to own final professional responsibility
allow Codex to define architecture
implement full marketplace capability ranking in MVP
implement product UI
implement database schema
```

---

# 25. Acceptance Criteria

The `core-specs/cross-cutting/README.md` file is accepted when:

```text
[ ] It defines the purpose of core-specs/cross-cutting/.
[ ] It preserves the 26-domain baseline.
[ ] It states Capability and Business Responsibility are cross-cutting systems.
[ ] It distinguishes cross-cutting systems from ordinary domains.
[ ] It defines directory boundary.
[ ] It defines source chain requirements.
[ ] It defines required cross-cutting spec groups.
[ ] It defines cross-cutting categories.
[ ] It defines required metadata.
[ ] It defines required sections.
[ ] It defines Capability System rules.
[ ] It defines Business Responsibility System rules.
[ ] It defines Policy System rules.
[ ] It defines Review and Approval System rules.
[ ] It defines Audit System rules.
[ ] It defines AI Governance cross-cutting rules.
[ ] It defines Specification Governance rules.
[ ] It defines Codex Governance rules.
[ ] It lists high-priority cross-cutting specs.
[ ] It defines MVP depth rules.
[ ] It defines product consumer rules.
[ ] It defines data and implementation notes.
[ ] It defines Codex implementation rules.
[ ] It defines validation rules.
[ ] It defines prohibited behavior.
```

---

# 26. Next Action

After this README is accepted, generate:

```text
core-specs/cross-cutting/_template.md
```

Do not generate detailed cross-cutting specs before the template exists.

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial README for core-specs/cross-cutting/. Defines directory purpose, cross-cutting boundary, Capability and Business Responsibility rules, Policy/Review/Audit/AI/Codex governance references, validation rules and template handoff. |

---

**End of README**
