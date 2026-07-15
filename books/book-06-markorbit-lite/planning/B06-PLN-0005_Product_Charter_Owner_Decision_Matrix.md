# B06-PLN-0005 — Product Charter Owner Decision Matrix

## 1. Identity

```text
Record: B06-PLN-0005
Book: Book 06 — MarkOrbit Lite
Record type: Owner Decision Matrix
Version: v0.1
Status: Candidate — recommended dispositions become accepted on owner merge
Authority: B06-PLN-0004 Product Charter Candidate
```

## 2. Purpose

This record isolates the Product-local decisions that remain after the Books 01–05 authority review.

The options below do not reopen upstream architecture.

Merge of the Product Charter pull request records acceptance of the recommended option for each decision unless the pull request is changed before merge.

## 3. Decision standard

Each option is evaluated against:

- user clarity;
- commercial value;
- professional value;
- architectural conformance;
- privacy and authority;
- MVP feasibility;
- distinctiveness;
- future extensibility;
- evidence required to increase automation.

Decision outcomes:

- **RECOMMENDED** — preferred Charter baseline;
- **ALTERNATIVE** — conforming but weaker for the first baseline;
- **DEFERRED** — useful after evidence or additional systems exist;
- **REJECTED** — conflicts with accepted boundaries or creates unnecessary risk.

## OD-01 — Canonical identity and market positioning

### Decision question

> Should Lite be constitutionally redefined as an AI Growth Workspace, or should growth remain a market promise under the accepted lightweight Workplace Product identity?

### Option A — canonical identity plus growth/action promise

```text
MarkOrbit Lite
= Today-centered lightweight Workplace Product

Market promise
= AI-assisted growth and action workspace for trademark professionals
```

**Disposition:** RECOMMENDED

Advantages:

- preserves Book 04 authority;
- explains Lite’s scope beyond sales;
- allows strong market differentiation;
- supports growth, cases, Artifacts, attention and handoffs;
- avoids presenting Lite as generic CRM or AI chat;
- leaves room for future Growth, Solo, Team or local/private profiles.

Risks:

- external messaging must explain two levels clearly;
- “Workplace Product” is architecturally precise but less immediate as marketing language.

### Option B — redefine Lite as AI Growth Workspace

**Disposition:** REJECTED AS CANONICAL IDENTITY

Advantages:

- simple market message;
- directly communicates commercial benefit.

Risks:

- narrows missed-work, judgment, delivery, privacy and learning value;
- encourages revenue-only ranking;
- risks turning Lite into CRM/sales automation;
- conflicts with accepted Book 04 identity.

### Option C — position Lite only as a personal AI assistant

**Disposition:** REJECTED

Risks:

- ignores Product loop, organization context, Artifacts and Handoffs;
- weakens the distinction between AI capability and Product responsibility;
- underrepresents team and Workplace participation.

### Recommended decision

**Accept Option A.**

## OD-02 — First reference journey and MVP loop

### Decision question

> Which single end-to-end journey best proves Lite’s distinct Product value while exercising the accepted cross-Product boundaries?

### Option A — Existing Client Value Journey

```text
authorized client/trademark observation
→ Today
→ explainable service-value candidate
→ case-supported client Artifact
→ purpose-specific Communication draft
→ final user confirmation
→ Communication and/or MarkReg Handoff
→ typed result return
→ feedback and learning candidate
```

**Disposition:** RECOMMENDED

Advantages:

- connects professional and commercial value;
- tests Today, Case, Artifact, Communication and MarkReg;
- fits independent professionals and small teams;
- can use manual-confirmation mode;
- produces measurable value without requiring autonomous action;
- reflects the user’s existing trademark-service business reality.

Risks:

- requires careful client and Matter scope handling;
- service-value ranking must not become sales pressure;
- client response and conversion may remain partly external or user-reported.

### Option B — Personal productivity / missed deadline journey

**Disposition:** ALTERNATIVE

Advantages:

- simpler and lower risk;
- strong missed-work value;
- easy to explain.

Weaknesses:

- overlaps with ordinary task/reminder products;
- under-tests Case and Artifact differentiation;
- risks shadow Task/deadline semantics.

### Option C — Case-to-content publishing journey

**Disposition:** ALTERNATIVE / SECOND REFERENCE JOURNEY

Advantages:

- highly distinctive;
- demonstrates case reuse and professional presentation;
- supports growth.

Weaknesses:

- does not sufficiently test MarkReg Handoff;
- rights, anonymization and Publish boundaries may dominate the first MVP;
- may make Lite appear primarily as a content tool.

### Option D — Provider discovery journey

**Disposition:** DEFERRED

Weaknesses:

- depends more heavily on Book 07 MGSN;
- risks predefining Trust and Routing;
- weaker as the first independent Lite proof.

### Recommended decision

**Accept Option A as the first reference journey.**

Use Option C as a second journey when defining the Product record and scenario baseline.

## OD-03 — Case Center MVP depth

### Decision question

> How much case ingestion, structuring, memory and external reuse should be included in the first validated loop?

### Option A — curated, reference-first case-to-Artifact scope

The MVP supports:

- user-selected or rule-selected case references;
- minimum authorized timeline and facts;
- manual fact confirmation;
- selected lesson/case-use candidate;
- one reviewed client-facing Artifact;
- source, audience, anonymization and rights notes;
- no automatic promotion to Knowledge.

**Disposition:** RECOMMENDED

Advantages:

- proves distinctive value;
- limits privacy and data-quality risk;
- avoids creating a universal Case object;
- works with local/private sources;
- supports meaningful client follow-up.

### Option B — universal automatic case ingestion

**Disposition:** REJECTED FOR MVP

Risks:

- uncontrolled client/Matter mixing;
- weak source and authority mapping;
- expensive normalization;
- automatic anonymization may be unsafe;
- high token, storage and review cost;
- pressures Book 02 object boundaries.

### Option C — no Case Center in MVP

**Disposition:** ALTERNATIVE BUT NOT PREFERRED

Advantages:

- simpler MVP;
- lower privacy burden.

Weaknesses:

- removes one of Lite’s strongest differentiators;
- weakens professional presentation and reuse;
- reduces the value of the Existing Client Value Journey.

### Recommended decision

**Accept Option A.**

## OD-04 — Local/private data baseline

### Decision question

> Should Lite require all relevant case and professional context to be synchronized centrally, remain local-only, or use a purpose-bound hybrid model?

### Option A — hybrid minimization

```text
raw local/private material remains in its authorized zone
→ governed retrieval or local processing
→ minimum candidate/reference/Artifact context crosses when authorized
→ source class and restrictions remain attached
```

**Disposition:** RECOMMENDED

Advantages:

- aligns with Local Vault and data-zone architecture;
- permits large local case libraries;
- reduces unnecessary synchronization;
- supports standalone and organization modes;
- allows future local AI and browser helpers.

Risks:

- requires explicit bridge contracts;
- source availability may affect reproducibility;
- local and cloud version conflicts need visible handling.

### Option B — cloud-first synchronization

**Disposition:** DEFERRED AS AN ORGANIZATION POLICY OPTION

Risks:

- unnecessary privacy and ownership exposure;
- large local data cost;
- mistaken assumption that central storage creates authority;
- not appropriate for every organization.

### Option C — local-only Lite

**Disposition:** REJECTED AS UNIVERSAL BASELINE

Risks:

- weakens cross-Product Handoff, collaboration and continuity;
- reduces recoverability and shared review;
- cannot support all Workplaces.

### Recommended decision

**Accept Option A.**

## OD-05 — Lite-visible MGSN depth

### Decision question

> How much provider discovery, comparison, Trust and ordering should Lite expose before Book 07 defines the full MGSN Product/network model?

### Option A — trusted shortlist and Capability Need Handoff

Lite may:

- show organization-authorized provider relationships;
- present a purpose-limited shortlist or comparison preview;
- explain source and evidence limits;
- prepare a Capability Need;
- hand off to MGSN;
- display returned candidate or collaboration results.

**Disposition:** RECOMMENDED

Advantages:

- useful to professionals;
- preserves MGSN ownership;
- supports gradual Book 07 integration;
- avoids open-marketplace behavior.

### Option B — full Global Agent Center inside Lite

**Disposition:** REJECTED

Risks:

- duplicates Book 07;
- risks open bidding and automatic appointment;
- confuses relationship ownership and Trust;
- expands Lite beyond its focused loop.

### Option C — no provider visibility in Lite

**Disposition:** ALTERNATIVE BUT TOO RESTRICTIVE

Weaknesses:

- breaks useful continuity;
- forces unnecessary Product switching;
- prevents Today from showing provider-related attention.

### Recommended decision

**Accept Option A.**

## OD-06 — External-action mode

### Decision question

> Should the first Lite release send, publish and follow up automatically, or prepare and require final human confirmation?

### Option A — final human confirmation default

```text
Lite prepares
→ user/reviewer inspects exact version, recipient, audience and consequence
→ user confirms
→ governed service or local helper performs bounded operation
→ typed evidence returns
```

**Disposition:** RECOMMENDED

Advantages:

- preserves professional accountability;
- avoids wrong recipient/channel/account errors;
- works with manual and connector modes;
- allows safe learning from confirmed outcomes;
- does not block later policy-bounded automation.

### Option B — organization-policy automation for selected low-risk actions

**Disposition:** DEFERRED

May be considered after:

- supported channel contracts;
- exact policy scope;
- approved account and recipient rules;
- evaluation evidence;
- safe retry and reconciliation;
- incident ownership;
- opt-out and disable controls.

### Option C — silent autonomous send/publish/follow-up

**Disposition:** REJECTED

Risks:

- recipient and confidentiality errors;
- professional and commercial commitments;
- duplicate or unknown external effects;
- loss of version-specific approval;
- account and platform risk;
- incompatible with Books 02–04.

### Recommended decision

**Accept Option A.**

## 4. Decision summary

| Decision | Recommended option | Owner-merge effect |
| --- | --- | --- |
| OD-01 identity | canonical Lite + AI growth/action promise | accepted Charter positioning |
| OD-02 first journey | Existing Client Value Journey | accepted first reference-journey baseline |
| OD-03 Case Center | curated, reference-first case-to-Artifact | accepted MVP depth |
| OD-04 local/private | hybrid minimization | accepted data-topology assumption |
| OD-05 MGSN depth | shortlist/preview + Capability Need Handoff | accepted Lite-visible boundary |
| OD-06 external action | final human confirmation default | accepted MVP action mode |

## 5. Decisions not created by this record

This matrix does not decide:

- final module names;
- navigation structure;
- controlled Product record IDs;
- complete reference-journey set;
- exact scenario count;
- chapter count or Part structure;
- implementation stack;
- cloud/local deployment choice for every organization;
- production authorization;
- External Protected Action authorization.

## 6. Gate effect

```text
Owner merge
→ OD-01–OD-06 recommended options accepted
→ Product Charter baseline accepted
→ Product record / journey / scenario baseline authorized next
→ chapter-map candidate authorized after that baseline
→ manuscript drafting remains unauthorized
```
