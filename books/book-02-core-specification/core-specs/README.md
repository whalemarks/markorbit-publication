# core-specs/

**Repository:** `book-02-core`  
**Directory:** `core-specs/`  
**Document:** `core-specs/README.md`  
**Book:** Book 02 — MarkOrbit Core Specification  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Directory Purpose

The `core-specs/` directory contains implementation-ready Core Specification files derived from:

```text
Book 02 manuscript chapters
        ↓
Appendices A–H
        ↓
indexes/
        ↓
core-specs/
```

The purpose of `core-specs/` is to convert the Book 02 Core architecture into stable, testable, traceable specification files that Codex and engineering can implement.

`core-specs/` is not a product requirement folder.

`core-specs/` is not a UI design folder.

`core-specs/` is not a database schema folder.

`core-specs/` is the specification bridge between MarkOrbit Core meaning and executable implementation.

---

# 2. Canonical Rule

Book 02 uses the following rule:

```text
Manuscript defines architecture.
Appendices stabilize canonical references.
Indexes operationalize references.
core-specs/ specify implementation contracts.
codex-tasks/ instruct implementation.
Codex implements approved specifications.
```

Therefore:

```text
No index, no core-spec.
No source appendix, no core-spec.
No ownership, no spec.
No contract, no implementation.
No acceptance criteria, no Codex task.
```

---

# 3. Directory Boundary

## 3.1 core-specs/ Owns

`core-specs/` owns:

```text
Domain Specification files
Object Specification files
Service Specification files
Event Specification files
Contract Specification files
API Specification files
Agent Specification files
Workflow Specification files
cross-cutting specification files
templates
spec acceptance criteria
spec validation rules
```

## 3.2 core-specs/ Does Not Own

`core-specs/` does not own:

```text
Book 02 manuscript architecture
appendix canonical definitions
index-level reference lists
product PRDs
UI flows
database physical design
pricing policy
sales policy
external marketplace rules
implementation code
Codex task execution
production data
```

---

# 4. Required Source Chain

Every `core-specs/` file must trace to approved sources.

Required source chain:

```text
Manuscript Chapter
        ↓
Appendix
        ↓
Index
        ↓
core-specs File
        ↓
Codex Task
        ↓
Implementation
        ↓
Test
        ↓
Acceptance
```

Acceptable sources include:

```text
Book 02 manuscript chapters
B02-APP-A through B02-APP-H
indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
indexes/codex-task-index.md
approved templates
approved prior specs
```

Unacceptable sources include:

```text
memory only
conversation-only instruction
product assumption
unreviewed AI guess
unapproved prompt
engineering convenience
database-first interpretation
UI-first interpretation
```

---

# 5. Required Directory Structure

The `core-specs/` directory should contain:

```text
core-specs/README.md

core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
core-specs/workflows/
core-specs/cross-cutting/
core-specs/validation/
```

Each major subdirectory should include:

```text
README.md
_template.md
```

---

# 6. Subdirectory Responsibilities

## 6.1 domains/

Defines bounded Core Domains.

Source:

```text
indexes/domain-index.md
B02-APP-B — Core Domain Index
B02-CH-22 — Domain Specification
```

Expected responsibility:

```text
domain purpose
domain boundary
domain ownership
related objects
related services
related events
related contracts
MVP depth
deferred scope
acceptance criteria
```

---

## 6.2 objects/

Defines Core Objects as professional meaning before data structure.

Source:

```text
indexes/object-index.md
B02-APP-C — Core Object Index
B02-CH-23 — Object Specification
```

Expected responsibility:

```text
object meaning
owning domain or cross-cutting system
object lifecycle
object relationships
state model
validation rules
service usage
event usage
contract mapping
AI usage
acceptance criteria
```

---

## 6.3 services/

Defines Core Services as governed capabilities that operate Core meaning.

Source:

```text
indexes/service-index.md
B02-APP-D — Core Service Index
B02-CH-24 — Service Specification
```

Expected responsibility:

```text
service purpose
owning domain or system
inputs
outputs
objects read
objects created or updated
events emitted
contracts required
permission requirement
policy requirement
review requirement
audit requirement
failure behavior
acceptance criteria
```

---

## 6.4 events/

Defines Core Events as meaningful changes in Core state or execution.

Source:

```text
indexes/event-index.md
B02-APP-E — Event Index
B02-CH-25 — Event Specification
```

Expected responsibility:

```text
event name
event meaning
source service
trigger
payload contract
related objects
consumer domains
audit requirement
review requirement
API side effect
workflow usage
acceptance criteria
```

---

## 6.5 contracts/

Defines shared consumption and execution contracts.

Source:

```text
B02-CH-17 — Core Contract Architecture
B02-CH-27 — Core Consumption Specification
indexes/api-index.md
indexes/service-index.md
indexes/event-index.md
indexes/agent-index.md
```

Expected responsibility:

```text
data contract
service contract
event contract
API contract
workflow contract
agent contract
permission contract
policy contract
review contract
Codex task contract
```

---

## 6.6 api/

Defines contract-bound Core API surfaces.

Source:

```text
indexes/api-index.md
B02-APP-F — API Index
B02-CH-27 — Core Consumption Specification
```

Expected responsibility:

```text
API name
consumer
owning service
input contract
output contract
permission rule
policy rule
event side effects
AI usage
error contract
rate and safety constraints
acceptance criteria
```

---

## 6.7 agents/

Defines governed AI, system and Codex-related agents.

Source:

```text
indexes/agent-index.md
B02-APP-G — Agent Index
B02-CH-26 — AI Capability and Agent Governance Specification
```

Expected responsibility:

```text
Agent Identity
Agent Contract
allowed capabilities
prohibited capabilities
authorized knowledge
object access
service access
event access
risk level
human review rule
audit rule
API exposure
acceptance criteria
```

---

## 6.8 workflows/

Defines workflow contracts and execution primitives.

Source:

```text
B02-CH-16 — Core Execution Primitives
B02-CH-17 — Core Contract Architecture
B02-CH-27 — Core Consumption Specification
indexes/domain-index.md
indexes/service-index.md
indexes/event-index.md
```

Expected responsibility:

```text
workflow purpose
workflow states
workflow transitions
tasks
events
review rules
approval rules
responsibility assignment
failure behavior
acceptance criteria
```

---

## 6.9 cross-cutting/

Defines cross-cutting specification systems.

Source:

```text
indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
B02-CH-19 — Capability Specification
B02-CH-21 — Business Responsibility Specification
```

Expected responsibility:

```text
Capability specifications
Business Responsibility specifications
AI Governance references
Policy references
Knowledge references
cross-domain ownership rules
```

Important rule:

```text
Capability and Business Responsibility are cross-cutting Core specification systems.
They are not counted as additional baseline Core Domains.
```

---

## 6.10 validation/

Defines validation rules for specs and implementation readiness.

Source:

```text
indexes/*
B02-APP-H — Codex Task Index
indexes/codex-task-index.md
```

Expected responsibility:

```text
domain count validation
object ownership validation
service-event validation
event naming validation
API contract validation
agent contract validation
Codex source reference validation
prohibited-overreach validation
release readiness validation
```

---

# 7. Spec Status Vocabulary

Specification files use the following status values:

```text
Draft
Reviewing
Approved
Deprecated
Superseded
Archived
```

Only `Approved` specs may be used as implementation sources.

`Draft` specs may guide planning but should not be treated as final implementation authority.

---

# 8. Spec File Naming Rules

Use lowercase kebab-case filenames.

Examples:

```text
identity.md
trademark.md
classification-recommendation.md
classification-recommendation-service.md
trademark-status-changed.md
agent-contract.md
classification-assistant-agent.md
order-to-matter-conversion-workflow.md
```

Do not use:

```text
IdentitySpec.md
identity_spec.md
final-trademark-new.md
service1.md
api-for-lite.md
```

---

# 9. Required Metadata for Each Spec

Each spec file must begin with metadata.

```text
# Spec Title

**Spec ID:** ...
**Spec Type:** Domain | Object | Service | Event | Contract | API | Agent | Workflow
**Owning Domain/System:** ...
**Source Appendix:** ...
**Source Index:** ...
**Related Chapter:** ...
**Status:** Draft
**Version:** 0.1.0
**MVP Phase/Wave:** ...
**MVP Depth:** ...
**Owner:** MarkOrbit Publications Editorial Board
```

---

# 10. Spec ID Format

Recommended spec ID formats:

```text
B02-DOM-{DOMAIN}
B02-OBJ-{OBJECT}
B02-SVC-{SERVICE}
B02-EVT-{EVENT}
B02-CTR-{CONTRACT}
B02-API-{API}
B02-AGT-{AGENT}
B02-WF-{WORKFLOW}
B02-XCUT-{SYSTEM}
```

Examples:

```text
B02-DOM-IDENTITY
B02-OBJ-TRADEMARK
B02-SVC-CLASSIFICATION-RECOMMENDATION
B02-EVT-ORDER-CONVERTED-TO-MATTER
B02-API-TRADEMARK-LOOKUP
B02-AGT-CLASSIFICATION-ASSISTANT
B02-WF-ORDER-TO-MATTER
B02-XCUT-BUSINESS-RESPONSIBILITY
```

---

# 11. Required Spec Templates

The following templates must be created before detailed specs.

```text
core-specs/domains/_template.md
core-specs/objects/_template.md
core-specs/services/_template.md
core-specs/events/_template.md
core-specs/contracts/_template.md
core-specs/api/_template.md
core-specs/agents/_template.md
core-specs/workflows/_template.md
core-specs/cross-cutting/_template.md
```

Each template must include:

```text
metadata
purpose
source references
scope
boundary rules
relationships
contracts
AI usage if applicable
events if applicable
API usage if applicable
workflow usage if applicable
validation rules
prohibited overreach
acceptance criteria
revision notes
```

---

# 12. First Generation Priority

The first generation of `core-specs/` should be scaffold-first.

Generate in this order:

```text
1. core-specs/README.md
2. subdirectory README files
3. _template.md files
4. high-priority MVP domain specs
5. high-priority MVP object specs
6. high-priority MVP service specs
7. high-priority MVP event specs
8. high-priority MVP contract specs
9. high-priority MVP API specs
10. high-priority MVP agent specs
11. workflow specs
12. validation specs
```

Do not generate detailed implementation specs before templates exist.

---

# 13. High-Priority MVP Domain Specs

Initial domain specs should prioritize:

```text
identity.md
organization.md
user.md
permission.md
knowledge.md
brand.md
trademark.md
jurisdiction.md
classification.md
document.md
customer.md
order.md
matter.md
workflow-contract.md
task.md
event.md
```

Partial baseline:

```text
policy.md
evidence.md
notification.md
communication.md
agent.md
service-provider.md
routing.md
opportunity.md
```

Reserved boundary:

```text
partner.md
service-network.md
```

---

# 14. High-Priority MVP Object Specs

Initial object specs should prioritize:

```text
identity.md
actor.md
ai-agent-identity.md
organization.md
organization-membership.md
user.md
user-profile.md
user-role-assignment.md
permission-rule.md
access-scope.md
knowledge-source.md
knowledge-asset.md
knowledge-citation.md
brand.md
brand-owner.md
trademark.md
trademark-owner.md
trademark-status.md
trademark-goods-services.md
trademark-lifecycle-record.md
jurisdiction.md
trademark-office.md
jurisdiction-requirement.md
classification.md
class.md
goods-services-term.md
classification-recommendation.md
classification-review-record.md
document.md
document-requirement.md
document-metadata.md
customer.md
order.md
order-item.md
order-status.md
order-to-matter-link.md
matter.md
matter-status.md
matter-context.md
workflow-contract.md
workflow-state.md
workflow-transition.md
task.md
task-assignment.md
task-status.md
event.md
event-payload.md
responsibility-assignment.md
review-record.md
approval-record.md
ai-agent.md
agent-contract.md
ai-output.md
ai-recommendation.md
ai-audit-record.md
codex-task.md
spec-file.md
test-fixture.md
```

---

# 15. High-Priority MVP Service Specs

Initial service specs should prioritize:

```text
identity-registration-service.md
identity-resolution-service.md
actor-identity-lookup-service.md
organization-registration-service.md
organization-membership-service.md
user-registration-service.md
user-profile-service.md
user-role-assignment-service.md
permission-check-service.md
access-scope-resolution-service.md
knowledge-retrieval-service.md
knowledge-source-registration-service.md
knowledge-asset-validation-service.md
brand-registration-service.md
trademark-registration-service.md
trademark-status-normalization-service.md
trademark-lookup-service.md
jurisdiction-requirement-lookup-service.md
jurisdiction-rule-validation-service.md
classification-recommendation-service.md
classification-validation-service.md
goods-services-term-lookup-service.md
classification-review-service.md
document-upload-service.md
document-requirement-service.md
document-validation-service.md
customer-registration-service.md
order-creation-service.md
order-validation-service.md
order-confirmation-service.md
order-to-matter-conversion-service.md
matter-creation-service.md
matter-status-service.md
workflow-contract-registration-service.md
workflow-transition-validation-service.md
task-creation-service.md
task-assignment-service.md
task-completion-service.md
task-review-service.md
event-publication-service.md
event-validation-service.md
responsibility-assignment-service.md
review-assignment-service.md
approval-service.md
agent-contract-validation-service.md
ai-output-registration-service.md
ai-audit-recording-service.md
prohibited-overreach-check-service.md
```

---

# 16. High-Priority MVP Event Specs

Initial event specs should prioritize:

```text
identity-created.md
organization-created.md
user-created.md
user-role-assigned.md
permission-granted.md
permission-revoked.md
permission-check-failed.md
knowledge-source-added.md
knowledge-asset-validated.md
brand-created.md
trademark-created.md
trademark-status-changed.md
classification-recommendation-generated.md
classification-review-required.md
classification-recommendation-approved.md
classification-recommendation-rejected.md
document-uploaded.md
customer-created.md
order-created.md
order-confirmed.md
order-converted-to-matter.md
matter-created.md
matter-status-changed.md
workflow-contract-created.md
workflow-transition-requested.md
workflow-transition-approved.md
workflow-transition-rejected.md
task-created.md
task-assigned.md
task-completed.md
task-review-required.md
event-published.md
event-validation-failed.md
responsibility-assigned.md
review-required.md
review-approved.md
review-rejected.md
agent-contract-validated.md
agent-contract-validation-failed.md
ai-output-generated.md
ai-recommendation-generated.md
ai-review-required.md
ai-usage-policy-violation-detected.md
ai-audit-record-created.md
prohibited-overreach-detected.md
```

---

# 17. High-Priority MVP Agent Specs

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

# 18. Required Contract Specs

Initial contract specs should include:

```text
identity-data-contract.md
permission-contract.md
knowledge-retrieval-contract.md
trademark-data-contract.md
classification-recommendation-contract.md
document-data-contract.md
order-data-contract.md
order-to-matter-workflow-contract.md
matter-workflow-contract.md
task-event-contract.md
event-payload-contract.md
agent-contract.md
ai-output-contract.md
ai-audit-contract.md
review-contract.md
approval-contract.md
codex-task-contract.md
```

---

# 19. Required API Specs

Initial API specs should include:

```text
identity-api.md
user-api.md
permission-api.md
knowledge-api.md
brand-api.md
trademark-api.md
jurisdiction-api.md
classification-api.md
document-api.md
customer-api.md
order-api.md
matter-api.md
task-api.md
event-api.md
ai-governance-api.md
classification-assistant-api.md
core-consumption-api.md
codex-task-api.md
```

API specs must reference service specs and event side effects.

API does not define Core meaning.

---

# 20. Required Workflow Specs

Initial workflow specs should include:

```text
order-to-matter-conversion-workflow.md
classification-review-workflow.md
document-review-workflow.md
task-review-workflow.md
ai-output-review-workflow.md
routing-review-workflow.md
codex-task-acceptance-workflow.md
```

Workflow specs must reference:

```text
Workflow Contract
Task
Event
Review Record
Approval Record
Business Responsibility
```

---

# 21. Validation Requirements

The `core-specs/` directory must support validation checks.

Required validation categories:

```text
metadata validation
source reference validation
domain count validation
object ownership validation
service-object mapping validation
service-event mapping validation
event naming validation
event payload contract validation
API contract validation
permission rule validation
policy rule validation
agent contract validation
AI audit validation
workflow transition validation
Codex source reference validation
prohibited-overreach validation
release readiness validation
```

---

# 22. Prohibited core-specs Behavior

`core-specs/` must not:

```text
invent new Core domains
change the 26-domain baseline
promote Capability or Business Responsibility into ordinary domains without architecture release
create unowned objects
create services without related objects
create mutating services without events
create events without source services
create APIs without contracts
create AI agents without Agent Contracts
create AI output without audit
create workflows without Workflow Contracts
create Codex tasks directly without codex-task-index.md
implement full product UI
implement full database schema
implement full MGSN marketplace
implement full opportunity scoring
implement official filing automation in MVP
```

---

# 23. Relationship to codex-tasks/

`core-specs/` is the required source layer for Codex tasks.

The handoff is:

```text
core-specs/
        ↓
codex-tasks/
        ↓
Codex implementation
```

A Codex task must cite:

```text
source manuscript chapter
source appendix
source index
source core-spec
acceptance criteria
test requirements
prohibited overreach
```

Codex must not implement from broad architectural prose alone.

---

# 24. Relationship to Product Books

Book 02 Core specs may be consumed by later product books.

Examples:

```text
Book 03 — Workplace Framework
Book 04 — MarkReg
Book 05 — MarkOrbit Lite
Book 06 — Mark Global Service Network
```

Product books may consume Core specs but must not redefine Core meaning.

Product books may define:

```text
product UI
product workflow experience
product-specific extensions
product metrics
product release plan
```

Product books may not define:

```text
baseline Core Domains
canonical Core Object meaning
Core Service responsibility
Core Event semantics
AI governance authority
Codex architecture authority
```

---

# 25. Acceptance Criteria

The `core-specs/README.md` file is accepted when:

```text
[ ] It defines the purpose of core-specs/.
[ ] It places core-specs/ after appendices and indexes.
[ ] It states that core-specs/ does not define architecture.
[ ] It defines directory structure.
[ ] It defines each subdirectory responsibility.
[ ] It defines source chain requirements.
[ ] It defines spec status vocabulary.
[ ] It defines naming rules.
[ ] It defines required metadata.
[ ] It defines spec ID formats.
[ ] It requires templates before detailed specs.
[ ] It defines first generation priority.
[ ] It lists high-priority domain specs.
[ ] It lists high-priority object specs.
[ ] It lists high-priority service specs.
[ ] It lists high-priority event specs.
[ ] It lists high-priority agent specs.
[ ] It lists required contract specs.
[ ] It lists required API specs.
[ ] It lists required workflow specs.
[ ] It defines validation requirements.
[ ] It defines prohibited behavior.
[ ] It defines handoff to codex-tasks/.
```

---

# 26. Next Action

After this README is accepted, generate subdirectory README files first:

```text
core-specs/domains/README.md
core-specs/objects/README.md
core-specs/services/README.md
core-specs/events/README.md
core-specs/contracts/README.md
core-specs/api/README.md
core-specs/agents/README.md
core-specs/workflows/README.md
core-specs/cross-cutting/README.md
core-specs/validation/README.md
```

Then generate templates.

Do not generate detailed domain, object, service, event, API or agent specs before templates exist.

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial core-specs directory README for second canonical draft. Defines directory purpose, boundaries, source chain, subdirectory responsibilities, priority specs, validation requirements and handoff to codex-tasks/. |

---

**End of README**
