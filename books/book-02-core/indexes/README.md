# indexes/

**Repository:** `book-02-core`  
**Directory:** `indexes/`  
**Document:** `indexes/README.md`  
**Book:** Book 02 — MarkOrbit Core Specification  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Directory Purpose

The `indexes/` directory contains machine-readable and implementation-ready index documents derived from Book 02 appendices.

The appendices are canonical manuscript references.

The `indexes/` directory converts those appendix references into operational indexes that can be consumed by:

```text
core-specs/
codex-tasks/
validation scripts
implementation planning
release checks
```

The purpose of `indexes/` is not to replace appendices.

The purpose is to make appendices executable.

---

# 2. Position in the Specification Flow

Book 02 uses the following flow:

```text
Manuscript chapters
        ↓
Appendices A–H
        ↓
indexes/
        ↓
core-specs/
        ↓
codex-tasks/
        ↓
Codex implementation
        ↓
tests and release validation
```

Therefore:

```text
Appendices canonize.
Indexes operationalize.
core-specs/ specify.
codex-tasks/ implement.
```

---

# 3. Canonical Rule

The canonical rule for this directory is:

```text
Indexes must be derived from appendices.
Indexes must not invent Core architecture.
Indexes must not silently change domain, object, service, event, API, agent or Codex task meaning.
```

Any mismatch between an appendix and an index must be treated as an architecture issue.

---

# 4. Required Index Files

The `indexes/` directory should include the following files.

```text
indexes/README.md
indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
indexes/codex-task-index.md
```

Optional later indexes may include:

```text
indexes/consumer-index.md
indexes/contract-index.md
indexes/workflow-index.md
indexes/status-vocabulary.md
indexes/mvp-depth-index.md
indexes/release-gate-index.md
```

---

# 5. Source Appendix Mapping

Each index file must be generated from a specific appendix.

| Index File | Source Appendix | Purpose |
|-----------|-----------------|---------|
| `domain-index.md` | B02-APP-B — Core Domain Index | Operational domain list and MVP depth map |
| `object-index.md` | B02-APP-C — Core Object Index | Operational object list and ownership map |
| `service-index.md` | B02-APP-D — Core Service Index | Operational service list and service ownership map |
| `event-index.md` | B02-APP-E — Event Index | Operational event list and event contract map |
| `api-index.md` | B02-APP-F — API Index | Operational API surface map |
| `agent-index.md` | B02-APP-G — Agent Index | Operational AI and agent governance map |
| `codex-task-index.md` | B02-APP-H — Codex Task Index | Operational Codex wave and task map |

Appendix A — Glossary applies to all index files.

---

# 6. Index File Responsibilities

## 6.1 `domain-index.md`

Defines the operational domain map.

Must preserve:

```text
26 baseline Core Domains
4 domain categories
Capability / Business Responsibility as cross-cutting systems
MVP Phase
MVP Depth
Product Consumers
Deferred Scope
```

Must not:

```text
add new domains
rename domains
treat cross-cutting systems as ordinary domains
expand MVP scope
```

---

## 6.2 `object-index.md`

Defines the operational object map.

Must include:

```text
object name
owning domain or cross-cutting system
object category
MVP phase
MVP depth
related services
related events
related contracts
AI usage
product consumers
```

Must not:

```text
treat database tables as Core Objects
create unowned objects
duplicate product-local objects
omit AI governance objects
```

---

## 6.3 `service-index.md`

Defines the operational service map.

Must include:

```text
service name
owning domain or cross-cutting system
service category
objects read
objects created or updated
events emitted
contracts required
AI usage
workflow usage
API exposure
MVP phase
MVP depth
```

Must not:

```text
treat UI buttons as Core Services
hide state changes
omit emitted events
bypass permission or policy rules
```

---

## 6.4 `event-index.md`

Defines the operational event map.

Must include:

```text
event name
event file name
source domain or source system
trigger
payload contract
related objects
consumer domains
audit requirement
MVP phase
MVP depth
```

Must preserve:

```text
Event ≠ log
Event ≠ UI action
Event ≠ activity feed
Event ≠ queue message
Event ≠ analytics ping
```

---

## 6.5 `api-index.md`

Defines the operational API surface map.

Must include:

```text
API name
owning domain or service
consumer
input contract
output contract
permission requirement
policy requirement
event side effects
AI usage
MVP status
future status
```

Must preserve:

```text
API is a contract-bound consumption surface.
API does not define Core meaning.
```

---

## 6.6 `agent-index.md`

Defines the operational agent governance map.

Must include:

```text
agent ID
agent name
agent category
owning domain or system
Agent Contract
allowed capabilities
prohibited capabilities
authorized knowledge
allowed object access
allowed service access
risk level
human review rule
events emitted
audit requirement
product consumers
MVP status
```

Must preserve:

```text
AI is a governed capability.
AI is not the Core.
AI is not above the Core.
AI is not a replacement for professional responsibility.
```

---

## 6.7 `codex-task-index.md`

Defines the operational Codex task map.

Must include:

```text
task ID
task title
wave
package
status
source specifications
dependencies
expected outputs
tests
fixtures
validation requirements
prohibited overreach
acceptance criteria
```

Must preserve:

```text
Codex implements approved Core specifications.
Codex does not define Core architecture.
```

---

# 7. Index Generation Rules

All index files must follow these generation rules.

```text
1. Use appendices as the source of truth.
2. Do not invent new architecture.
3. Preserve canonical names.
4. Preserve MVP depth.
5. Preserve consumer classification.
6. Preserve cross-cutting system classification.
7. Preserve AI governance requirements.
8. Preserve event naming rules.
9. Preserve API contract rules.
10. Preserve Codex prohibited-overreach rules.
```

---

# 8. Index Status Vocabulary

Index files use the following status values.

```text
Draft
Reviewing
Approved
Deprecated
Superseded
Archived
```

A `Draft` index may guide planning but should not be used for implementation without review.

An `Approved` index may be used as input for `core-specs/` generation.

---

# 9. Naming Rules

Index files should use lowercase kebab-case filenames.

Examples:

```text
domain-index.md
object-index.md
service-index.md
event-index.md
api-index.md
agent-index.md
codex-task-index.md
```

Do not use:

```text
DomainIndex.md
domain_index.md
domains.md
object-list-final.md
new-api-map.md
```

---

# 10. Required Metadata for Each Index

Each index file should begin with metadata.

```text
# Index Title

**Repository:** book-02-core
**Directory:** indexes/
**Index ID:** ...
**Source Appendix:** ...
**Status:** Draft
**Version:** 0.1.0
**Owner:** MarkOrbit Publications Editorial Board
```

---

# 11. Relationship to `core-specs/`

The `indexes/` directory controls the first generation of `core-specs/`.

The expected handoff is:

```text
domain-index.md
        → core-specs/domains/

object-index.md
        → core-specs/objects/

service-index.md
        → core-specs/services/

event-index.md
        → core-specs/events/

api-index.md
        → core-specs/api/

agent-index.md
        → core-specs/agents/

codex-task-index.md
        → codex-tasks/
```

The `core-specs/` directory should not generate detailed specs from manuscript chapters alone.

It must use appendices and indexes.

---

# 12. Relationship to `codex-tasks/`

The `codex-task-index.md` file is the source for later Codex task files.

The expected handoff is:

```text
indexes/codex-task-index.md
        ↓
codex-tasks/_template.md
        ↓
codex-tasks/wave-0/
codex-tasks/wave-1/
codex-tasks/wave-2/
codex-tasks/wave-3/
codex-tasks/wave-4/
codex-tasks/wave-5/
codex-tasks/wave-6/
codex-tasks/wave-7/
```

Codex tasks must not be generated directly from broad chapter language.

They must reference:

```text
appendices
indexes
core-specs
approved templates
MVP Execution Matrix
```

---

# 13. Validation Requirements

The `indexes/` directory should support validation.

Validation checks should include:

```text
domain count check
domain category check
cross-cutting system check
object ownership check
service ownership check
service-event mapping check
event naming check
event source domain check
API contract requirement check
agent contract requirement check
AI audit requirement check
Codex source spec reference check
MVP depth consistency check
consumer classification check
deferred scope protection check
```

---

# 14. Prohibited Index Behavior

Indexes must not:

```text
change the 26-domain baseline
promote Capability or Business Responsibility into ordinary domains without architecture release
invent Core Objects not listed in Appendix C
invent Core Services not listed in Appendix D
invent Core Events not listed in Appendix E
invent API surfaces not listed in Appendix F
invent AI Agents not listed in Appendix G
invent Codex tasks not listed or allowed by Appendix H
remove review requirements from AI outputs
expand deferred scope
turn product UI into Core specification
turn database schemas into Core meaning
```

---

# 15. Initial Generation Order

Generate indexes in this order:

```text
1. indexes/domain-index.md
2. indexes/object-index.md
3. indexes/service-index.md
4. indexes/event-index.md
5. indexes/api-index.md
6. indexes/agent-index.md
7. indexes/codex-task-index.md
```

This order follows dependency:

```text
Domain
↓
Object
↓
Service
↓
Event
↓
API
↓
Agent
↓
Codex Task
```

---

# 16. Acceptance Criteria

The `indexes/README.md` file is accepted when:

```text
[ ] It defines the purpose of indexes/.
[ ] It states that indexes are derived from appendices.
[ ] It lists required index files.
[ ] It maps each index file to its source appendix.
[ ] It defines responsibilities for each index.
[ ] It preserves 26 baseline Core Domains.
[ ] It preserves cross-cutting system rules.
[ ] It preserves AI governance rules.
[ ] It preserves API contract rules.
[ ] It preserves Codex implementation rules.
[ ] It defines index generation rules.
[ ] It defines validation requirements.
[ ] It defines prohibited index behavior.
[ ] It defines handoff to core-specs/.
[ ] It defines handoff to codex-tasks/.
```

---

# 17. Next Action

After this README is accepted, generate:

```text
indexes/domain-index.md
```

This file should be derived from:

```text
B02-APP-B_Core_Domain_Index.md
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial indexes directory README for second canonical draft. Defines index purpose, source appendix mapping, required files, validation rules, prohibited behavior and handoff to core-specs/codex-tasks. |

---

**End of README**
