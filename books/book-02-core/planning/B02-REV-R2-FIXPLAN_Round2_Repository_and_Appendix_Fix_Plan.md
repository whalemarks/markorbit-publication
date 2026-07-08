# B02-REV-R2-FIXPLAN — Round 2 Repository and Appendix Fix Plan

**Book:** Book 02 — MarkOrbit Core Specification  
**Repository:** `book-02-core`  
**Fix Plan ID:** B02-REV-R2-FIXPLAN  
**Related Review:** B02-REV-R2 — Round 2 Packaged Manuscript Review  
**Plan Type:** Repository and Appendix Fix Plan  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Fix Plan Purpose

This document converts the findings from **B02-REV-R2 — Round 2 Packaged Manuscript Review** into an actionable repository and appendix fix plan.

Round 2 confirmed that the organized Book 2 package is manuscript-complete and architecturally coherent, but not yet ready for `core-specs/` generation or Codex task generation.

This fix plan defines:

- repository structure fixes;
- metadata fixes;
- appendix generation sequence;
- index readiness requirements;
- `core-specs/` hold rules;
- Codex hold rules;
- acceptance criteria for closing Round 2.

Round 2 fix principle:

```text
Stabilize repository structure and appendices before generating executable specs.
```

---

# 2. Round 2 Review Summary

Round 2 reviewed the uploaded organized package:

```text
book 2.zip
```

The package passed manuscript completeness review.

Confirmed:

```text
manuscript/B02-CH-00 through B02-CH-31 are present
all manuscript paths listed in publication.yaml exist
no manuscript chapter is missing
no extra manuscript chapter was found outside publication.yaml
chapter metadata IDs match file numbers
all manuscript chapters end with “End of Chapter”
```

Round 2 decision:

```text
PASS — Manuscript Complete
PASS — Architecture Coherent
PASS WITH FIXES — Repository Metadata
NOT YET — core-specs Generation
NOT YET — Codex Task Generation
```

---

# 3. Round 2 Issue List

Round 2 identified nine issues.

```text
R2-001 — Normalize B02-PLN-0003 Planning File Name
R2-002 — Clarify Publication / Chapter / Release Status Layers
R2-003 — Add appendices/ Directory
R2-004 — Add appendices/ to README Repository Tree
R2-005 — Scaffold core-specs/, indexes/, codex-tasks/
R2-006 — Clarify 26 Domains vs Cross-Cutting Systems
R2-007 — Ensure AI Agent / AI Audit / AI Output Are Indexed
R2-008 — Add API Template and API Index
R2-009 — Tag Consumers by MVP / Partial / Future
```

---

# 4. Fix Categories

Round 2 fixes are grouped into five categories.

```text
Category A — Repository Path and Folder Fixes
Category B — Metadata and Status Fixes
Category C — Canonical Architecture Clarifications
Category D — Appendix Generation Fixes
Category E — Pre-core-specs and Pre-Codex Scaffolding
```

---

# 5. Fix Priority

Fix priorities:

```text
P0 — Required before Appendix A
P1 — Required during Appendices A–H
P2 — Required before indexes/
P3 — Required before core-specs/
P4 — Required before Codex Wave 0
```

Round 2 fixes should be executed in this order:

```text
P0 repository structure and metadata
P1 appendices
P2 indexes
P3 core-specs scaffold
P4 Codex Wave 0 scaffold
```

---

# 6. R2-001 — Normalize B02-PLN-0003 Planning File Name

## 6.1 Issue

Actual file found in package:

```text
planning/B02-PLN-0003_Core_Domain_Map_v1.0_rewrite.md
```

Canonical expected reference:

```text
planning/B02-PLN-0003_Core_Domain_Map_v1.0.md
```

## 6.2 Risk

If the `_rewrite` suffix remains in the canonical planning file name, future metadata and Codex tasks may refer to inconsistent paths.

This may affect:

```text
README.md
publication.yaml
CHANGELOG.md
appendices
indexes
Codex source spec references
```

## 6.3 Fix Decision

Normalize the planning file name by removing `_rewrite`.

Preferred canonical path:

```text
planning/B02-PLN-0003_Core_Domain_Map_v1.0.md
```

## 6.4 Required Actions

```text
1. Rename planning/B02-PLN-0003_Core_Domain_Map_v1.0_rewrite.md
   to planning/B02-PLN-0003_Core_Domain_Map_v1.0.md.

2. Update README.md if it references the old name.

3. Update publication.yaml if it references the old name.

4. Update CHANGELOG.md if it references the old name.

5. Ensure future appendices and indexes use the canonical name.
```

## 6.5 Acceptance Criteria

```text
[ ] Only one canonical B02-PLN-0003 file exists.
[ ] The canonical filename does not include `_rewrite`.
[ ] README references the canonical file.
[ ] publication.yaml references the canonical file.
[ ] CHANGELOG does not create a conflicting canonical name.
```

## 6.6 Priority

```text
P0 — Required before Appendix A
```

---

# 7. R2-002 — Clarify Publication / Chapter / Release Status Layers

## 7.1 Issue

Current status values exist at different layers:

```text
publication.yaml status: canonical_draft
chapter status: Draft
release status: manuscript_draft_completed
```

This is acceptable, but the layers must be defined.

## 7.2 Risk

Without status layer definitions, future contributors may incorrectly interpret chapter Draft status as contradicting publication canonical_draft status.

## 7.3 Fix Decision

Define separate status vocabularies for:

```text
Publication Status
Chapter Status
Spec Status
Codex Task Status
Implementation Status
Release Status
```

## 7.4 Canonical Status Vocabularies

### Publication Status

```text
draft
canonical_draft
reviewing
approved
released
deprecated
superseded
archived
```

### Chapter Status

```text
Draft
Reviewing
Approved
Revised
Deprecated
Superseded
Archived
```

### Spec Status

```text
Draft
Reviewing
Approved
Deprecated
Superseded
Archived
```

### Codex Task Status

```text
Draft
Ready
In Progress
Blocked
Implemented
Tested
Accepted
Rejected
Deferred
Superseded
```

### Implementation Status

```text
Not Started
Planned
In Progress
Implemented
Tested
Accepted
Deferred
Blocked
Deprecated
```

### Release Status

```text
planning
manuscript_draft_completed
appendix_in_progress
spec_scaffold_ready
implementation_in_progress
release_candidate
released
archived
```

## 7.5 Required Actions

```text
1. Add status vocabulary to Appendix A — Glossary.
2. Add a short status layer note to README.md.
3. Add status vocabularies or references to publication.yaml.
```

## 7.6 Acceptance Criteria

```text
[ ] Appendix A defines status layers.
[ ] README explains that publication, chapter, spec, task and release statuses are different.
[ ] publication.yaml status fields remain consistent with the defined vocabulary.
```

## 7.7 Priority

```text
P1 — Required during Appendix A
```

---

# 8. R2-003 — Add appendices/ Directory

## 8.1 Issue

`publication.yaml` references appendix paths, but the package does not include an `appendices/` folder.

Expected paths include:

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

## 8.2 Risk

Appendix generation and publication build processes may fail if the folder does not exist.

## 8.3 Fix Decision

Create:

```text
book-02-core/appendices/
```

before generating Appendix A.

## 8.4 Required Actions

```text
1. Create appendices/ directory.
2. Add placeholder README.md or .gitkeep if appendices are not generated immediately.
3. Generate Appendix A first.
```

## 8.5 Acceptance Criteria

```text
[ ] appendices/ directory exists.
[ ] Appendix A path can be created.
[ ] publication.yaml appendix paths resolve after generation.
```

## 8.6 Priority

```text
P0 — Required before Appendix A
```

---

# 9. R2-004 — Add appendices/ to README Repository Tree

## 9.1 Issue

README includes appendices in the book contents, but the repository tree does not show an `appendices/` directory.

## 9.2 Risk

Repository documentation will be inconsistent with `publication.yaml`.

## 9.3 Fix Decision

Update README repository structure to include:

```text
appendices/
```

## 9.4 Recommended README Tree

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
│   ├── domains/
│   ├── objects/
│   ├── services/
│   ├── events/
│   ├── contracts/
│   ├── api/
│   ├── agents/
│   └── workflows/
├── indexes/
├── codex-tasks/
├── assets/
└── releases/
```

## 9.5 Required Actions

```text
1. Update README repository tree.
2. Update directory responsibilities section with appendices/.
3. Confirm publication.yaml directory mapping matches README.
```

## 9.6 Acceptance Criteria

```text
[ ] README tree includes appendices/.
[ ] README explains appendices/ responsibility.
[ ] README and publication.yaml directory mappings are aligned.
```

## 9.7 Priority

```text
P0 — Required before Appendix A
```

---

# 10. R2-005 — Scaffold core-specs/, indexes/, codex-tasks/

## 10.1 Issue

The repository defines or implies the following folders, but they are not present yet:

```text
core-specs/
indexes/
codex-tasks/
```

## 10.2 Risk

If implementation begins without scaffolding, Codex may create files inconsistently.

## 10.3 Fix Decision

Do not generate full contents yet.

Create structural scaffolds after appendices A–H are complete.

## 10.4 Required Folders

```text
core-specs/
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
core-specs/workflows/

indexes/

codex-tasks/
codex-tasks/wave-0/
codex-tasks/wave-1/
codex-tasks/wave-2/
codex-tasks/wave-3/
codex-tasks/wave-4/
codex-tasks/wave-5/
codex-tasks/wave-6/
codex-tasks/wave-7/
```

## 10.5 Required Placeholder Files

Recommended placeholders:

```text
core-specs/README.md
core-specs/domains/README.md
core-specs/objects/README.md
core-specs/services/README.md
core-specs/events/README.md
core-specs/contracts/README.md
core-specs/api/README.md
core-specs/agents/README.md
core-specs/workflows/README.md

indexes/README.md

codex-tasks/README.md
codex-tasks/wave-0/README.md
...
codex-tasks/wave-7/README.md
```

## 10.6 Acceptance Criteria

```text
[ ] core-specs/ scaffold exists after appendices.
[ ] indexes/ scaffold exists after appendices.
[ ] codex-tasks/ scaffold exists after appendices and before Codex Wave 0.
[ ] No detailed core-specs are generated before appendices A–H are complete.
[ ] No Codex implementation task is generated before Appendix H and indexes exist.
```

## 10.7 Priority

```text
P2 — indexes scaffold after appendices
P3 — core-specs scaffold after appendices/indexes
P4 — codex-tasks scaffold before Codex Wave 0
```

---

# 11. R2-006 — Clarify 26 Domains vs Cross-Cutting Systems

## 11.1 Issue

Capability and Business Responsibility appear as cross-cutting concepts, specification chapters and execution-priority items.

## 11.2 Risk

They may be incorrectly counted as additional baseline domains.

## 11.3 Fix Decision

Preserve the 26-domain baseline.

Classify Capability and Business Responsibility as cross-cutting specification systems.

## 11.4 Canonical Clarification

Use this wording:

```text
The canonical baseline Core Domain Map contains 26 domains.

Capability and Business Responsibility are cross-cutting Core specification systems.
They govern multiple domains and may produce executable specs, objects, services, events and contracts.
They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.
```

## 11.5 Files to Update

Primary:

```text
appendices/B02-APP-A_Glossary.md
appendices/B02-APP-B_Core_Domain_Index.md
```

Secondary:

```text
publication.yaml
README.md
```

## 11.6 Acceptance Criteria

```text
[ ] Appendix A defines cross-cutting specification system.
[ ] Appendix B preserves the 26-domain map.
[ ] Appendix B separately lists Capability and Business Responsibility as cross-cutting systems.
[ ] No appendix silently changes domain count.
```

## 11.7 Priority

```text
P1 — Required during Appendices A/B
```

---

# 12. R2-007 — Ensure AI Agent / AI Audit / AI Output Are Indexed

## 12.1 Issue

AI Agent, AI Output and AI Audit are central to AI governance, but they are not yet indexed.

## 12.2 Risk

AI may be implemented as prompt-only behavior without identity, review, event and audit.

## 12.3 Fix Decision

Index AI execution concepts as first-class Core execution concepts.

## 12.4 Required Object Index Entries

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

## 12.5 Required Agent Index Entries

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

## 12.6 Required Agent Index Fields

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

## 12.7 Files to Update

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
core-specs/objects/
```

## 12.8 Acceptance Criteria

```text
[ ] AI Agent is indexed.
[ ] AI Output is indexed.
[ ] AI Recommendation is indexed.
[ ] AI Audit Record is indexed.
[ ] Agent Contract is indexed.
[ ] MVP AI agents are included in Appendix G.
[ ] AI entries include review, event and audit requirements.
```

## 12.9 Priority

```text
P1 — Required during Appendices C/G
P3 — Required before core-specs/
```

---

# 13. R2-008 — Add API Template and API Index

## 13.1 Issue

API is referenced in Book 02 but needs explicit index and template support.

## 13.2 Risk

Codex may implement API surfaces without contract, permission or event rules.

## 13.3 Fix Decision

Generate Appendix F — API Index.

Later create:

```text
core-specs/api/_template.md
```

## 13.4 Appendix F Required Content

```text
API Index purpose
API naming rules
API-to-Service relationship
API-to-Contract relationship
MVP API surfaces
Future API surfaces
input contract
output contract
permission requirement
event side effects
product consumer boundaries
```

## 13.5 MVP API Surfaces

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

## 13.6 Future API Surfaces

```text
External Partner API
MGSN Provider API
Brand Asset Vault API
Opportunity Engine API
Reporting API
Public Developer API
Webhook API
```

## 13.7 Files to Update

Primary:

```text
appendices/B02-APP-F_API_Index.md
```

Later:

```text
core-specs/api/_template.md
indexes/api-index.md
```

## 13.8 Acceptance Criteria

```text
[ ] Appendix F exists.
[ ] Appendix F defines MVP API surfaces.
[ ] Appendix F defines future API surfaces.
[ ] Appendix F defines API template expectations.
[ ] core-specs/api/_template.md is scheduled.
```

## 13.9 Priority

```text
P1 — Required during Appendix F
P3 — Required before core-specs/
```

---

# 14. R2-009 — Tag Consumers by MVP / Partial / Future

## 14.1 Issue

Book 02 includes multiple consumers but does not yet have a canonical consumer status index.

## 14.2 Risk

Future product consumers may be pulled into MVP too early.

## 14.3 Fix Decision

Classify consumers.

## 14.4 Canonical Consumer Classification

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

## 14.5 Files to Update

Primary:

```text
appendices/B02-APP-A_Glossary.md
appendices/B02-APP-H_Codex_Task_Index.md
```

Secondary:

```text
appendices/B02-APP-F_API_Index.md
README.md
publication.yaml
```

Later:

```text
indexes/consumer-index.md
core-specs/contracts/*-core-consumption.md
```

## 14.6 Acceptance Criteria

```text
[ ] MVP Consumer is defined.
[ ] Partial Consumer is defined.
[ ] Future Consumer is defined.
[ ] Consumers are classified in appendices or indexes.
[ ] Product consumption tasks respect classification.
```

## 14.7 Priority

```text
P1 — Required during appendices
P4 — Required before Codex Wave 0
```

---

# 15. Round 2 Execution Sequence

Execute Round 2 fixes in this sequence.

```text
Step 1 — Normalize repository metadata
    Rename B02-PLN-0003 file or align all references.
    Clarify status layers.

Step 2 — Add appendices structure
    Create appendices/.
    Update README tree.
    Update publication.yaml mapping.

Step 3 — Generate Appendix A
    Include glossary, status vocabulary, consumer classification, cross-cutting systems note.

Step 4 — Generate Appendix B
    Lock 26-domain baseline and MVP phase mapping.

Step 5 — Generate Appendix C
    Include object index and AI governance objects.

Step 6 — Generate Appendix D
    Generate service index.

Step 7 — Generate Appendix E
    Generate event index.

Step 8 — Generate Appendix F
    Generate API index and template expectations.

Step 9 — Generate Appendix G
    Generate agent index and AI governance entries.

Step 10 — Generate Appendix H
    Generate Codex task index and consumer classification usage.

Step 11 — Scaffold indexes/
    Generate baseline index files from appendices.

Step 12 — Scaffold core-specs/
    Generate folders and templates only.

Step 13 — Scaffold codex-tasks/
    Generate wave folders and Codex task template.

Step 14 — Generate Wave 0 Codex tasks
    Only after Appendix H and indexes exist.
```

---

# 16. Files to Create

## 16.1 Immediate

```text
book-02-core/appendices/
```

## 16.2 Appendices

```text
book-02-core/appendices/B02-APP-A_Glossary.md
book-02-core/appendices/B02-APP-B_Core_Domain_Index.md
book-02-core/appendices/B02-APP-C_Core_Object_Index.md
book-02-core/appendices/B02-APP-D_Core_Service_Index.md
book-02-core/appendices/B02-APP-E_Event_Index.md
book-02-core/appendices/B02-APP-F_API_Index.md
book-02-core/appendices/B02-APP-G_Agent_Index.md
book-02-core/appendices/B02-APP-H_Codex_Task_Index.md
```

## 16.3 Later Scaffolds

```text
book-02-core/indexes/
book-02-core/core-specs/
book-02-core/codex-tasks/
```

---

# 17. Files to Update

```text
book-02-core/README.md
book-02-core/publication.yaml
book-02-core/CHANGELOG.md
planning/B02-PLN-0003_Core_Domain_Map_v1.0.md
```

Optional, only if appendices are insufficient:

```text
manuscript/B02-CH-29_MVP_Domain_Priority.md
manuscript/B02-CH-30_MVP_Execution_Matrix.md
```

---

# 18. Hold Rules

## 18.1 core-specs Hold

Do not generate detailed `core-specs/` until:

```text
Appendices A–H are complete.
indexes/ baseline exists.
API template requirement is defined.
AI object/agent indexes are complete.
```

## 18.2 Codex Hold

Do not generate Codex implementation tasks until:

```text
Appendix H is complete.
indexes/codex-task-index.md exists.
codex task template exists.
core-specs/ template scaffold exists.
```

---

# 19. Round 2 Fix Acceptance Checklist

Round 2 fixes are accepted when:

```text
[ ] R2-001 planning filename/reference is normalized.
[ ] R2-002 status layers are defined.
[ ] R2-003 appendices/ exists.
[ ] R2-004 README includes appendices/.
[ ] R2-005 core-specs/, indexes/, codex-tasks/ scaffold plan is explicit.
[ ] R2-006 26 domains vs cross-cutting systems is clarified.
[ ] R2-007 AI Agent / AI Audit / AI Output are scheduled for indexes.
[ ] R2-008 API Index and API template are scheduled.
[ ] R2-009 consumers are classified as MVP / Partial / Future.
[ ] core-specs/ generation remains on hold.
[ ] Codex task generation remains on hold.
```

---

# 20. Round 2 Closure Criteria

Round 2 can be closed when:

```text
1. Repository metadata and folder fixes are defined.
2. Appendices A–H are approved as the next production step.
3. The 26-domain baseline is preserved.
4. Cross-cutting systems are clarified.
5. AI indexing requirement is explicit.
6. API indexing requirement is explicit.
7. Consumer classification is explicit.
8. Implementation scaffolding is sequenced after appendices.
9. Codex task generation is sequenced after indexes.
```

---

# 21. Fix Plan Decision

The Round 2 Fix Plan decision is:

```text
APPROVED — REPOSITORY AND APPENDIX FIXES REQUIRED
APPENDICES A–H SHALL BE GENERATED BEFORE CORE-SPECS
CORE-SPECS GENERATION REMAINS ON HOLD
CODEX TASK GENERATION REMAINS ON HOLD
```

---

# 22. Immediate Next Action

Proceed to:

```text
book-02-core/appendices/B02-APP-A_Glossary.md
```

Before or during Appendix A generation, apply:

```text
create appendices/
update README tree
update publication.yaml directory mapping
normalize B02-PLN-0003 reference
```

---

# 23. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Round 2 Repository and Appendix Fix Plan based on B02-REV-R2 findings. |

---

**End of Fix Plan**
