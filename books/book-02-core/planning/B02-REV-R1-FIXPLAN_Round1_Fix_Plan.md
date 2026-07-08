# B02-REV-R1-FIXPLAN — Round 1 Fix Plan

**Book:** Book 02 — MarkOrbit Core Specification  
**Repository:** `book-02-core`  
**Fix Plan ID:** B02-REV-R1-FIXPLAN  
**Related Review:** B02-REV-R1 — Round 1 Manuscript Architecture Review  
**Plan Type:** Architecture Review Fix Plan  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Fix Plan Purpose

This document converts the findings from **B02-REV-R1 — Round 1 Manuscript Architecture Review** into an actionable fix plan.

Round 1 concluded that the Book 02 manuscript body is architecturally coherent and ready for light fixes plus appendices.

This fix plan defines:

- which Round 1 issues must be fixed;
- where each fix should be applied;
- which fixes require manuscript edits;
- which fixes can be handled through appendices or repository indexes;
- which fixes should be deferred to `core-specs/`;
- what acceptance criteria must be met before Round 1 can be closed.

The principle of this fix plan is:

```text
Do not rewrite the manuscript body unless necessary.
Clarify unresolved architecture points through appendices, indexes and repository metadata.
```

---

# 2. Round 1 Review Summary

Round 1 identified the following issues.

```text
R1-001 — Cross-cutting Capability / Business Responsibility Placement
R1-002 — API Specification Needs Explicit Scaffold
R1-003 — Appendices Are Required Before core-specs/
R1-004 — Repository Packaging Needed
R1-005 — MVP / Future Consumer Classification Needs Index Support
R1-006 — AI Agent / AI Audit / AI Output Need Index Confirmation
```

Round 1 preliminary decision:

```text
Book 02 manuscript body is architecturally coherent and ready for Round 1 fixes plus appendices.
```

Round 1 does not require a major rewrite of chapters 00–31.

---

# 3. Fix Strategy

Round 1 fixes are divided into four categories.

```text
Category A — Canonical Clarification
Category B — Appendix Requirement
Category C — Repository Structure Fix
Category D — Index / core-specs Preparation
```

## 3.1 Category A — Canonical Clarification

Clarify Core concepts that may otherwise cause domain or responsibility drift.

## 3.2 Category B — Appendix Requirement

Use appendices to stabilize vocabulary and indexes before generating executable specs.

## 3.3 Category C — Repository Structure Fix

Ensure the repository layout matches publication metadata and future scaffolding.

## 3.4 Category D — Index / core-specs Preparation

Prepare, but do not yet generate, executable specification indexes and scaffolds.

---

# 4. Fix Priority

Fix priority is as follows.

```text
P0 — Required before appendices
P1 — Required during appendices
P2 — Required before core-specs/
P3 — Required before Codex tasks
```

Round 1 fixes should be completed in this order.

---

# 5. R1-001 — Cross-cutting Capability / Business Responsibility Placement

## 5.1 Issue

Capability and Business Responsibility appear in multiple roles:

```text
Canonical Models
Specification chapters
MVP priority concepts
Execution matrix rows
Possible implementation artifacts
```

This is architecturally valid, but it may confuse readers if these concepts are treated as normal domains and silently expand the baseline domain count.

## 5.2 Risk

Readers or Codex may incorrectly conclude:

```text
The baseline Core Domain Map has changed from 26 domains to 28 domains.
```

This would create inconsistency across:

```text
Chapter 08 — Ontology and Domain Classification
Chapter 12 — Canonical Models
Chapter 19 — Capability Specification
Chapter 21 — Business Responsibility Specification
Chapter 29 — MVP Domain Priority
Chapter 30 — MVP Execution Matrix
Appendix B — Core Domain Index
```

## 5.3 Fix Decision

Treat Capability and Business Responsibility as:

```text
Cross-Cutting Core Specification Systems
```

They may produce executable objects, services, events and contracts.

They do not change the 26 baseline Core Domain count.

## 5.4 Canonical Wording

Use the following wording in Appendix A and Appendix B:

```text
The baseline Core Domain Map contains 26 domains.

Capability and Business Responsibility are cross-cutting Core specification systems.
They govern multiple domains and may produce executable specs, objects, services, events and contracts.
They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.
```

## 5.5 Files to Update

Primary:

```text
appendices/B02-APP-A_Glossary.md
appendices/B02-APP-B_Core_Domain_Index.md
```

Secondary if needed:

```text
publication.yaml
README.md
```

Optional manuscript note:

```text
manuscript/B02-CH-29_MVP_Domain_Priority.md
```

## 5.6 Implementation Approach

Do not rewrite chapters 19 and 21.

Add clarification through appendices first.

Only add a short note to Chapter 29 if later review shows the appendix is insufficient.

## 5.7 Acceptance Criteria

```text
[ ] Appendix A defines Capability as a cross-cutting Core specification system.
[ ] Appendix A defines Business Responsibility as a cross-cutting Core specification system.
[ ] Appendix B states that the canonical baseline domain map remains 26 domains.
[ ] Appendix B does not list Capability and Business Responsibility as ordinary baseline domains.
[ ] publication.yaml remains consistent with the 26-domain baseline.
```

## 5.8 Priority

```text
P1 — Required during appendices
```

---

# 6. R1-002 — API Specification Needs Explicit Scaffold

## 6.1 Issue

Book 02 references API contracts and `core-specs/api/`, but there is no standalone chapter titled “API Specification.”

This is acceptable because API is handled through Contract Architecture, Service Specification and Core Consumption.

However, the executable repository still needs an explicit API index and template.

## 6.2 Risk

Without an explicit API scaffold, Codex may:

```text
create services without stable API surfaces
create API endpoints that bypass contracts
skip permission and event side-effect rules
create product-local API assumptions
```

## 6.3 Fix Decision

Do not add a new manuscript chapter.

Instead, define API explicitly in:

```text
Appendix F — API Index
core-specs/api/_template.md
```

## 6.4 Appendix F Must Include

```text
API Index purpose
API naming rules
API-to-Service relationship
API-to-Contract relationship
MVP API surfaces
Future API surfaces
Input / output contract requirement
Permission requirement
Event side effects
Product consumer boundaries
```

## 6.5 MVP API Surfaces

Appendix F should include at least:

```text
Identity API
Knowledge Retrieval API
Trademark API
Jurisdiction Requirement API
Classification Recommendation API
Document API
Customer API
Order API
Matter API
Task API
Event API
AI Invocation API
Core Consumption API baseline
```

## 6.6 Future API Surfaces

Appendix F should reserve:

```text
External Partner API
MGSN Provider API
Brand Asset Vault API
Opportunity Engine API
Reporting API
Public Developer API
Webhook API
```

## 6.7 Files to Update

Primary:

```text
appendices/B02-APP-F_API_Index.md
```

Later:

```text
core-specs/api/_template.md
indexes/api-index.md
```

## 6.8 Acceptance Criteria

```text
[ ] Appendix F exists.
[ ] Appendix F defines API surfaces as contract-bound consumption surfaces.
[ ] Appendix F lists MVP API surfaces.
[ ] Appendix F lists future/deferred API surfaces.
[ ] Appendix F defines API template expectations.
[ ] `core-specs/api/_template.md` is scheduled before Codex Wave 0.
```

## 6.9 Priority

```text
P1 — Required during appendices
P2 — Required before core-specs/
```

---

# 7. R1-003 — Appendices Are Required Before core-specs/

## 7.1 Issue

The manuscript body is complete, but appendices A–H are still pending.

The appendices are required because they stabilize:

```text
terms
domains
objects
services
events
APIs
agents
Codex tasks
```

## 7.2 Risk

If `core-specs/` is generated before appendices, the following may happen:

```text
Core Objects may be inconsistently named.
Events may be duplicated or renamed.
API surfaces may be skipped.
AI Agent / AI Output / AI Audit may be omitted.
Codex tasks may be generated from chapters instead of stable indexes.
```

## 7.3 Fix Decision

Do not generate `core-specs/` yet.

Generate appendices first.

## 7.4 Required Appendix Order

```text
1. Appendix A — Glossary
2. Appendix B — Core Domain Index
3. Appendix C — Core Object Index
4. Appendix D — Core Service Index
5. Appendix E — Event Index
6. Appendix F — API Index
7. Appendix G — Agent Index
8. Appendix H — Codex Task Index
```

## 7.5 Files to Create

```text
appendices/B02-APP-A_Glossary.md
appendices/B02-APP-B_Core_Domain_Index.md
appendices/B02-APP-C_Core_Object_Index.md
appendices/B02-APP-D_Core_Service_Index.md
appendices/B02-APP-E_Event_Index.md
appendices/B02-APP-F_API_Index.md
appendices/B02-APP-G_Agent_Index.md
appendices/B02-APP-H_Codex_Task_Index.md
```

## 7.6 Acceptance Criteria

```text
[ ] Appendices A–H are generated.
[ ] Glossary terms are canonical.
[ ] Domain Index preserves 26-domain baseline.
[ ] Object Index includes AI, audit and review objects.
[ ] Service Index maps services to owning domains or cross-cutting systems.
[ ] Event Index maps events to source domains.
[ ] API Index defines API surfaces and template expectations.
[ ] Agent Index defines AI agent governance.
[ ] Codex Task Index maps tasks to waves and matrix rows.
```

## 7.7 Priority

```text
P0 — Required before core-specs/
```

---

# 8. R1-004 — Repository Packaging Needed

## 8.1 Issue

The repository package must be organized so that manuscript, planning, editorial, appendices, indexes, specs and tasks are located in predictable paths.

Round 2 later confirmed that manuscript files are already organized under `manuscript/`, but the repository still needs appendix and implementation scaffolding.

## 8.2 Risk

If the repository is zipped or handed to Codex before structure is complete:

```text
Codex may not find source chapters.
Appendix references may fail.
Publication metadata may point to missing paths.
core-specs/ generation may be inconsistent.
```

## 8.3 Fix Decision

Maintain the repository structure:

```text
book-02-core/
├── README.md
├── publication.yaml
├── CHANGELOG.md
├── planning/
├── editorial/
├── manuscript/
├── appendices/
├── core-specs/
├── indexes/
├── codex-tasks/
├── assets/
└── releases/
```

## 8.4 Required Repository Fixes

```text
Add appendices/
Add appendices/ to README repository tree.
Add appendices/ to publication.yaml directory mapping.
Later scaffold core-specs/
Later scaffold indexes/
Later scaffold codex-tasks/
Normalize planning file names.
```

## 8.5 File Name Normalization

Normalize:

```text
planning/B02-PLN-0003_Core_Domain_Map_v1.0_rewrite.md
```

to:

```text
planning/B02-PLN-0003_Core_Domain_Map_v1.0.md
```

or update all metadata references to the `_rewrite` filename.

Preferred action:

```text
Rename file and remove `_rewrite` from canonical planning filename.
```

## 8.6 Acceptance Criteria

```text
[ ] `appendices/` exists.
[ ] README tree includes appendices/.
[ ] publication.yaml directory mapping includes appendices.
[ ] planning file names are canonical.
[ ] manuscript files remain under manuscript/.
[ ] future scaffolds are scheduled for core-specs/, indexes/ and codex-tasks/.
```

## 8.7 Priority

```text
P0 — Required before appendices
P2 — Full scaffold required before core-specs/
```

---

# 9. R1-005 — MVP / Future Consumer Classification Needs Index Support

## 9.1 Issue

Book 02 defines multiple consumers:

```text
MarkReg
MarkOrbit Lite
Workplace
MGSN
Brand Asset Vault
Opportunity Engine
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
AI Agents
Codex Implementation
```

But they need classification by MVP readiness.

## 9.2 Risk

Without classification, future consumers may accidentally pull too much scope into MVP.

Examples:

```text
MGSN full marketplace may be built too early.
Opportunity Engine full scoring may be built too early.
Brand Asset Vault full portfolio system may be built too early.
External integrations may be built before contracts.
```

## 9.3 Fix Decision

Add consumer classification.

## 9.4 Canonical Consumer Classification

```text
MVP Consumers
    MarkReg
    MarkOrbit Lite
    Workplace
    AI Agents
    Codex Implementation

Partial Consumers
    MGSN
    Opportunity Engine baseline
    Brand Asset Vault baseline

Future Consumers
    Partner Center
    Client Portal
    Service Platform
    External Integrations
    Reporting Consumers
```

## 9.5 Files to Update

Primary:

```text
appendices/B02-APP-A_Glossary.md
appendices/B02-APP-H_Codex_Task_Index.md
```

Secondary:

```text
appendices/B02-APP-B_Core_Domain_Index.md
appendices/B02-APP-F_API_Index.md
README.md
publication.yaml
```

Later:

```text
indexes/consumer-index.md
core-specs/contracts/*-core-consumption.md
```

## 9.6 Acceptance Criteria

```text
[ ] Appendix A defines MVP Consumer, Partial Consumer and Future Consumer.
[ ] Appendix H uses consumer classification in Codex task sequencing.
[ ] Consumer classification prevents MGSN, Brand Asset Vault and Opportunity Engine from becoming full MVP scope.
[ ] Core Consumption contracts later reference consumer classification.
```

## 9.7 Priority

```text
P1 — Required during appendices
P3 — Required before Codex tasks
```

---

# 10. R1-006 — AI Agent / AI Audit / AI Output Need Index Confirmation

## 10.1 Issue

Chapter 26 and Chapter 31 define AI governance, but AI-related implementation concepts must be indexed to avoid being treated as prompt-only implementation details.

## 10.2 Risk

If AI concepts are not indexed:

```text
AI Agent may be treated as a prompt.
AI Output may not have status, review or audit.
AI Audit may be omitted.
Agent Contract may be skipped.
Review Record may be inconsistently modeled.
```

## 10.3 Fix Decision

Index AI execution concepts as first-class Core execution concepts.

## 10.4 Required Object Index Entries

Appendix C should include:

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

## 10.5 Required Agent Index Entries

Appendix G should include:

```text
AI Governance
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

## 10.6 Required AI Index Fields

Appendix G entries should include:

```text
Agent identity
Allowed capabilities
Prohibited capabilities
Authorized knowledge
Allowed object access
Risk level
Human review
Events
Audit
Product consumers
MVP status
```

## 10.7 Files to Update

Primary:

```text
appendices/B02-APP-C_Core_Object_Index.md
appendices/B02-APP-G_Agent_Index.md
```

Secondary:

```text
appendices/B02-APP-A_Glossary.md
appendices/B02-APP-E_Event_Index.md
```

Later:

```text
core-specs/agents/
core-specs/objects/ai-agent.md
core-specs/objects/ai-output.md
core-specs/objects/ai-audit-record.md
```

## 10.8 Acceptance Criteria

```text
[ ] Appendix C includes AI Agent, AI Output, AI Recommendation and AI Audit Record.
[ ] Appendix G includes MVP AI agents.
[ ] Appendix G defines required governance fields.
[ ] AI Agent is not treated as prompt-only.
[ ] AI Output includes risk/review/audit concepts.
```

## 10.9 Priority

```text
P1 — Required during appendices
P2 — Required before core-specs/
```

---

# 11. Round 1 Fix Execution Order

Execute Round 1 fixes in this order.

```text
Step 1
    Normalize repository structure and create appendices/ path.

Step 2
    Generate Appendix A — Glossary.
    Include cross-cutting systems, status vocabulary and consumer classification.

Step 3
    Generate Appendix B — Core Domain Index.
    Preserve 26-domain baseline and clarify Capability / Business Responsibility.

Step 4
    Generate Appendix C — Core Object Index.
    Include AI Agent / AI Output / AI Audit / Review objects.

Step 5
    Generate Appendix D — Core Service Index.

Step 6
    Generate Appendix E — Event Index.

Step 7
    Generate Appendix F — API Index.
    Make API surface explicit.

Step 8
    Generate Appendix G — Agent Index.
    Include AI governance and MVP agents.

Step 9
    Generate Appendix H — Codex Task Index.
    Use consumer classification and Codex wave structure.

Step 10
    Only after appendices, scaffold indexes/.

Step 11
    Only after indexes, scaffold core-specs/.

Step 12
    Only after core-specs scaffold, generate Codex Wave 0 tasks.
```

---

# 12. Files to Create or Update

## 12.1 Create

```text
book-02-core/appendices/
book-02-core/appendices/B02-APP-A_Glossary.md
book-02-core/appendices/B02-APP-B_Core_Domain_Index.md
book-02-core/appendices/B02-APP-C_Core_Object_Index.md
book-02-core/appendices/B02-APP-D_Core_Service_Index.md
book-02-core/appendices/B02-APP-E_Event_Index.md
book-02-core/appendices/B02-APP-F_API_Index.md
book-02-core/appendices/B02-APP-G_Agent_Index.md
book-02-core/appendices/B02-APP-H_Codex_Task_Index.md
```

## 12.2 Update

```text
book-02-core/README.md
book-02-core/publication.yaml
book-02-core/CHANGELOG.md
```

## 12.3 Later Scaffold

```text
book-02-core/indexes/
book-02-core/core-specs/
book-02-core/codex-tasks/
```

## 12.4 Optional Manuscript Update

Only if needed after appendices:

```text
manuscript/B02-CH-29_MVP_Domain_Priority.md
```

---

# 13. Round 1 Fix Acceptance Checklist

Round 1 fix plan is complete when:

```text
[ ] R1-001 cross-cutting systems clarification is included in Appendix A/B.
[ ] R1-002 API scaffold requirement is included in Appendix F.
[ ] R1-003 appendices A–H are generated or queued before core-specs/.
[ ] R1-004 repository structure includes appendices/ and normalized planning references.
[ ] R1-005 consumers are classified as MVP / Partial / Future.
[ ] R1-006 AI Agent / AI Audit / AI Output are included in Object and Agent indexes.
[ ] core-specs/ generation remains on hold until appendices are complete.
[ ] Codex task generation remains on hold until Appendix H and indexes exist.
```

---

# 14. Round 1 Closure Criteria

Round 1 can be closed when the following are true.

```text
1. No major manuscript architecture issue remains open.
2. All six Round 1 issues have a fix location and acceptance criteria.
3. Appendices A–H are approved as the next workstream.
4. The 26-domain baseline remains canonical.
5. Capability and Business Responsibility cross-cutting status is clarified.
6. API, AI and consumer classification are explicitly scheduled.
7. Repository structure is aligned with future specification production.
```

Round 1 does not require full `core-specs/` generation.

Round 1 closes when the path to appendices is clear and controlled.

---

# 15. Fix Plan Decision

The Round 1 Fix Plan decision is:

```text
APPROVED — LIGHT FIXES THROUGH APPENDICES AND REPOSITORY METADATA
NO MAJOR MANUSCRIPT REWRITE REQUIRED
CORE-SPECS GENERATION REMAINS ON HOLD
CODEX TASK GENERATION REMAINS ON HOLD
```

---

# 16. Immediate Next Action

Proceed to Round 2 / Round 3 / Round 4 review sequence or, if those are already complete, start:

```text
book-02-core/appendices/B02-APP-A_Glossary.md
```

Appendix A must include:

```text
canonical terms
26-domain clarification
cross-cutting systems clarification
AI governance vocabulary
consumer classification
status vocabulary
MVP depth vocabulary
Codex wave vocabulary
```

---

# 17. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Round 1 Fix Plan converting R1 review issues into appendix and repository fix actions. |

---

**End of Fix Plan**
