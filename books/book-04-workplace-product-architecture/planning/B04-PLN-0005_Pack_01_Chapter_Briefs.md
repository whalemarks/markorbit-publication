# B04-PLN-0005 — Pack 01 Chapter Briefs

Status: Approved upon merge of PUB-TASK-B04-002  
Pack: B04-PACK-01 — Front Matter and Part I  
Chapter Map: B04-TOC-V0.1  
Manuscript prose authorized: NO

Pack 01 includes B04-CH-00 through B04-CH-06. CH01 is already present as the accepted Table of Contents and is not rewritten as prose. A later controlled drafting task may create CH00 and CH02–CH06 only; it must not create Part II chapters.

## B04-CH-00 — Preface

### Chapter ID and title
B04-CH-00 — Preface

### Purpose
- Explain why Book 04 follows Core and Execution.
- Introduce Workplace as an independent Orbit.
- Explain the book’s reader and scope.
- Establish that this is architecture, not a Product PRD.

### Primary questions answered
- Why does MarkOrbit need a Workplace and Product Architecture book?
- What changed after Books 01–03?
- What does the reader gain from Book 04?

### Canonical authorities
Architecture Canon vNext; Book 01 Operating System positioning; Book 02 frozen baseline; Book 03 owner-accepted Execution baseline; ARC-002, ARC-003, ARC-005, ARC-008, ARC-023 and ARC-028.

### Required concepts
Constitutional spine, independent organizational Orbit, Workplace/Product separation, publication versus implementation readiness, and protected-action boundary.

### Required distinctions and boundaries
Architecture book versus Product PRD; Book 04 versus Books 01–03; chapter-map acceptance versus prose completion; publication planning versus implementation authorization.

### Required examples or diagram briefs
A short reader-orientation diagram showing Book 01 → Book 02 → Book 03 → Book 04 → Books 05–07.

### Non-goals
No full architecture summary; no product catalog; no implementation plan; no claims of final publication or implementation readiness.

### Required cross-references
Architecture Canon vNext; Decision Register vNext; PUBLICATION-ROADMAP.md; Book 04 governance.

### Acceptance conditions
Frames the book without redefining Core or Execution, keeps manuscript status honest, and states no implementation or protected action is authorized.

### Indicative drafting range
1,500–2,500 English words

## B04-CH-01 — Table of Contents

### Chapter ID and title
B04-CH-01 — Table of Contents

### Purpose
Record the accepted Book 04 chapter order and numbering governed by B04-TOC-V0.1.

### Primary questions answered
What is the accepted CH00–CH39 map? Which parts exist? What change control applies?

### Canonical authorities
B04-REV-0001; B04-TOC-V0.1; Book 04 governance; Architecture Open Questions vNext resolved OQ-001 record.

### Required concepts
Accepted chapter map, six-part structure, CH00–CH39 numbering, controlled writing packs.

### Required distinctions and boundaries
CH01 is already present; no new prose is required; future changes require explicit Book 04 change control; CH01 does not authorize drafting outside approved packs.

### Required examples or diagram briefs
No diagram required beyond the TOC structure.

### Non-goals
No rewrite as prose; no chapter expansion; no structural movement without change control.

### Required cross-references
B04-REV-0001; B04-PLN-0006; OPEN-QUESTIONS-vNEXT.md.

### Acceptance conditions
Retains exactly one occurrence of CH00–CH39 in the TOC and preserves the accepted titles.

### Indicative drafting range
Existing TOC only; no additional prose.

## B04-CH-02 — Why Workplace Exists

### Chapter ID and title
B04-CH-02 — Why Workplace Exists

### Purpose
Explain the missing layer between a shared professional Operating System and the individuality of each organization.

### Primary questions answered
Why is Workplace necessary? What does it mediate between shared foundations and organization-specific operation? Why is it more than a dashboard or tenant account?

### Canonical authorities
Architecture Canon vNext; ARC-003; ARC-005; ARC-008; Book 02 frozen baseline; Book 03 Execution baseline.

### Required concepts
Common OS versus organization-specific operation; identity, authority, clients, knowledge, rules and relationships; Workplace as operating environment, not merely dashboard; organization as accountable professional unit; Workplace as the ecosystem’s primary operating unit.

### Required distinctions and boundaries
Workplace ≠ Product; Workplace ≠ tenant account; Workplace ≠ case-management UI; Workplace ≠ centralized platform ownership; Workplace ≠ Core; Workplace ≠ Execution.

### Required examples or diagram briefs
Shared MarkOrbit foundation → Independent Organization Workplace → Products and network participation.

### Non-goals
No Core semantic amendment; no Workflow or Task redefinition; no Product feature catalog; no central SaaS tenancy model.

### Required cross-references
Book 04 positioning and scope; dependency map; Chapter Writing Gates; Architecture Canon Workplace decisions.

### Acceptance conditions
Defines the need for Workplace without absorbing Core, Execution, Products or MGSN.

### Indicative drafting range
3,000–4,500 English words

## B04-CH-03 — The Orbit Principle and Organizational Autonomy

### Chapter ID and title
B04-CH-03 — The Orbit Principle and Organizational Autonomy

### Purpose
Explain the original meaning of MarkOrbit and the principle: 各行其道，彼此牵引，共同演进.

### Primary questions answered
What is an organizational Orbit? How can Workplaces be autonomous and connected? How does the ecosystem evolve without platform absorption?

### Canonical authorities
Architecture Canon vNext; ARC-002; ARC-003; ARC-008; ARC-011; ARC-012; ARC-028.

### Required concepts
Each organization has its own Orbit; autonomy over clients, data, knowledge, rules, pricing and relationships; capability, service demand and trust as attraction; controlled connection rather than isolation; ecosystem evolution without platform absorption.

### Required distinctions and boundaries
Autonomy ≠ isolation; Connection ≠ central ownership; Routing ≠ forced allocation; Network ≠ open bidding; Federated governance ≠ primary architecture name.

### Required examples or diagram briefs
A multi-orbit ecosystem showing independent Workplaces connected through capability and trust without a central marketplace controlling them.

### Non-goals
No open marketplace model; no forced routing; no centralized professional ownership; no MGSN implementation design.

### Required cross-references
Architecture Canon vNext; Decision Register ARC-028; Book 04 MGSN boundary planning.

### Acceptance conditions
Uses the canonical principle while preserving independent organizational authority and private-first network boundaries.

### Indicative drafting range
3,000–4,500 English words

## B04-CH-04 — Position Between Core, Execution, Products and Network

### Chapter ID and title
B04-CH-04 — Position Between Core, Execution, Products and Network

### Purpose
Define Book 04’s precise position in the constitutional spine.

### Primary questions answered
What does each layer own? Where does Workplace sit? How do Products and MGSN relate to Workplace without replacing it?

### Canonical authorities
Architecture Canon vNext; ARC-001; ARC-005; ARC-006; ARC-011; ARC-015; ARC-016; Book 02 and Book 03 governance.

### Required concepts
Core → shared semantics and formal contracts; Execution → governed coordination and handoff; Workplace → authorized organization context; Products → user experience and domain composition; MGSN → connection among independent Workplaces; Owning Services → formal business-state mutation.

### Required distinctions and boundaries
Workplace consumes Core but does not redefine it; Workplace invokes Execution but does not replace it; Products operate in or connect to Workplace but do not own the organization; MGSN connects Orbits but does not absorb them.

### Required examples or diagram briefs
A responsibility and non-responsibility matrix for Core, Execution, Workplace, Product, MGSN, Owning Service, Human Professional and AI Agent.

### Non-goals
No implementation topology; no authority reassignment; no Book 02 or Book 03 rewrite.

### Required cross-references
Book 04 dependency map; Book 04 governance; Book 03 planning reference for Execution authority.

### Acceptance conditions
Makes responsibility boundaries explicit and keeps formal state mutation with the proper owning authorities.

### Indicative drafting range
3,500–5,000 English words

## B04-CH-05 — Workplace Principles

### Chapter ID and title
B04-CH-05 — Workplace Principles

### Purpose
Define the durable architectural principles every Workplace implementation must preserve.

### Primary questions answered
Which principles constrain all Workplace designs? What must implementations preserve even when product forms vary? What violations should reviewers detect?

### Canonical authorities
Architecture Canon vNext; ARC-003; ARC-005; ARC-008; ARC-021; ARC-022; ARC-026; ARC-027; ARC-028.

### Required concepts
Organizational autonomy; authorized context; private and local by default; shared foundations without central ownership; Human professional accountability; candidate before canonical; governed Execution before protected action; evidence, provenance and audit; Product Loop First, Shared Platform Extraction Second; evolution without forced replacement.

### Required distinctions and boundaries
For every principle include: Principle; Why it exists; What it requires; What would violate it. Do not transform principles into product features or implementation acceptance tests.

### Required examples or diagram briefs
A principle-to-violation table suitable for later conformance review.

### Non-goals
No PRD, no API, no schema, no deployment guidance, no authorization for external protected action.

### Required cross-references
Book 04 governance; Architecture Canon vNext; Decision Register ARC-021 and ARC-022; Book 03 authority boundary.

### Acceptance conditions
Covers all ten minimum principles and ties each to a concrete preservation and violation boundary.

### Indicative drafting range
4,000–5,500 English words

## B04-CH-06 — Workplace Boundaries and Non-Goals

### Chapter ID and title
B04-CH-06 — Workplace Boundaries and Non-Goals

### Purpose
Close Part I by defining what Workplace and Book 04 do not own.

### Primary questions answered
What does Workplace consume but not own? Which future books or specifications own adjacent subjects? Which implementation details are outside Book 04?

### Canonical authorities
Architecture Canon vNext; Book 02 frozen baseline; Book 03 Execution baseline; ARC-005; ARC-024; ARC-025; ARC-026; ARC-027.

### Required concepts
Workplace from Core; Workplace from Execution; Workplace from Product; Workplace from MGSN; Workplace from Local Vault; Workplace from AI Agent Runtime; Workplace from a centralized SaaS tenant; Book 04 from Books 05–07; Book 04 from implementation specifications.

### Required distinctions and boundaries
No Core semantic amendment; no Workflow or Task redefinition; no Product feature catalog; no universal database; no forced cloud centralization; no open marketplace; no autonomous external professional action; no API, schema, microservice or deployment design.

### Required examples or diagram briefs
A table with columns: Concept; Owned by Workplace?; Consumed by Workplace?; Authority owner; Book 04 treatment.

### Non-goals
No implementation specifications, no product catalogs, no external protected action, no Book 05–07 drafting.

### Required cross-references
Book 04 governance; writing pack plan; Architecture Open Questions vNext; Book 04 review record.

### Acceptance conditions
Ends Part I with clear ownership boundaries and leaves downstream specifications and future books outside the Pack 01 scope.

### Indicative drafting range
3,500–5,000 English words
