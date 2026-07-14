# B05-REV-0004 — Book 05 Whole-Draft Review

## Review Identity

- **Book:** Book 05 — MarkReg: The Full-Lifecycle International Trademark Product
- **Scope:** CH00–CH22, Book governance, planning records, manifests, status records, and prior Part I–III reviews
- **Chapter Map:** B05-TOC-V0.1 — Owner Accepted
- **Review type:** Whole-draft product, architecture, editorial, lifecycle, and publication-readiness review
- **Status:** Completed
- **Decision:** Revision required before Part IV drafting

## 1. Review Purpose

This is the first review of Book 05 as one continuous Product publication.

B05-REV-0001 through B05-REV-0003 checked individual writing packs while they were being produced. They did not test whether CH00–CH22 work as one book, whether the chapters collectively define a usable MarkReg Product, or whether the manuscript is ready to extend into governed filing execution.

This review therefore evaluates:

- whole-book progression;
- Product completeness;
- architecture conformance;
- cross-chapter consistency;
- terminology discipline;
- duplication and editorial density;
- practical product artifacts;
- user and professional usability;
- readiness to draft Part IV.

## 2. Material Reviewed

### Manuscript

- CH00 — Preface
- CH01 — Table of Contents
- CH02–CH07 — Part I: Product Constitution and Lifecycle Position
- CH08–CH15 — Part II: Need, Strategy and Recommendation
- CH16–CH22 — Part III: Commercial Journey and Formal Intake

### Control Records

- BOOK-GOVERNANCE.md
- BOOK-MANIFEST.md
- BOOK-STATUS.md
- README.md
- publication.yaml
- B05-PLN-0001 through B05-PLN-0003
- B05-REV-0001 through B05-REV-0003
- Books 01–04 Portfolio Baseline and Architecture Canon references

## 3. Executive Decision

```text
Architecture conformance: PASS
Product positioning: PASS
Lifecycle direction: PASS
Responsibility boundaries: PASS
Part-to-part logical sequence: PASS
Whole-book editorial coherence: CONDITIONAL PASS
Practical Product definition: REVISION REQUIRED
Examples and validation evidence: REVISION REQUIRED
Publication readiness: NOT READY
Part IV drafting authorization: HOLD
```

The existing draft is a strong constitutional and conceptual foundation. It successfully prevents MarkReg from becoming an ungoverned mega-system, an autonomous legal actor, an open provider marketplace, or an alternative source of official truth.

However, the manuscript currently explains boundaries more often than it demonstrates the Product. Across CH00–CH22, the reader repeatedly learns what MarkReg is not, which authority it does not own, and which states must remain distinct. Those controls are necessary, but the book has not yet converted them into a sufficiently concrete, testable Product model.

Part IV would introduce filing packages, approval, provider routing, submission, retry, acknowledgement, and audit. Drafting those chapters before closing the present Product-definition gaps would amplify abstraction and repetition.

## 4. What Is Working

### 4.1 The central Product thesis is coherent

The draft consistently defines MarkReg as a focused, full-lifecycle international trademark Product that reduces user complexity while preserving professional responsibility, organization ownership, official-source authority, and governed execution.

### 4.2 The pre-form journey is correctly prioritized

The manuscript correctly rejects the assumption that a trademark journey begins with a filing form. Need understanding, market context, applicant structure, filing units, jurisdictions, routes, classes, goods and services, search, risk, cost, and timing are treated as connected decisions.

### 4.3 State and authority distinctions are unusually disciplined

The draft preserves important separations, including:

```text
Recommendation ≠ Decision
Proposal ≠ Quote
Quote acceptance ≠ Payment
Payment ≠ Filing approval
Need Brief ≠ Formal Intake
Complete Intake ≠ Filing readiness
Uploaded file ≠ Valid Document
Order ≠ Matter
Matter ≠ Workflow
Submission ≠ Official acknowledgement
Product projection ≠ Official truth
```

These distinctions are suitable foundations for implementation contracts and professional governance.

### 4.4 The surrounding architecture is respected

The draft does not silently redefine Core, Execution, Workplace, MGSN, Owning Services, or official offices. The relationship between Product-local state and formal shared objects remains controlled.

### 4.5 The seven-part lifecycle map remains viable

The movement from Product constitution through recommendation, intake, filing, post-filing work, portfolio continuity, and Product evolution is logical. No structural renumbering is required at this stage.

## 5. Blocking Findings

### B05-WR-F01 — The manuscript is too boundary-heavy and repetitive

**Severity:** High  
**Affected scope:** CH02–CH22

The same constitutional distinctions recur in many chapters with only small contextual changes. Human responsibility, AI limits, official-source authority, Product-versus-Core boundaries, readiness-versus-approval, and provider-selection limits are restated frequently.

This repetition protects architecture but weakens the book as a publication. It increases length without proportionally increasing understanding and makes later chapters feel like parallel restatements rather than progressive Product definition.

**Required correction:**

- retain full constitutional explanations in Part I;
- convert later repetitions into short references to named rules;
- add a reusable “MarkReg Constitutional Rules” table;
- require each later chapter to add new Product meaning, artifacts, decisions, or flows rather than repeat general boundaries.

### B05-WR-F02 — The Product lacks a canonical artifact and decision model

**Severity:** Blocking  
**Affected scope:** CH07–CH22

Many Product outputs are named, including Need Brief, recommendation, proposal, quote, Commercial Instruction, Formal Intake, document requirement, readiness result, Order handoff, Matter handoff, and Execution Context. They are described separately, but the manuscript does not yet provide one canonical cross-chapter map showing:

- artifact or decision name;
- purpose;
- owner;
- source inputs;
- version identity;
- review requirement;
- approval authority;
- supersession rules;
- formalization target;
- downstream consumers.

Without this map, the book explains a journey but does not yet define a stable Product contract.

**Required correction:** Add a controlled “MarkReg Product Artifact and Decision Map” to Part I or immediately after CH07, and reference it throughout Parts II and III.

### B05-WR-F03 — There is no end-to-end reference journey

**Severity:** Blocking  
**Affected scope:** Whole draft

The book has many local examples and conceptual sequences, but no single trademark case travels through CH08–CH22. As a result, the reader cannot observe how facts, assumptions, options, documents, pricing, readiness, and responsibility change across the Product lifecycle.

**Required correction:** Introduce at least one canonical reference case and carry it through:

```text
Business need
→ Need Brief
→ jurisdiction and route options
→ filing-unit strategy
→ classification and goods/services
→ search and risk
→ proposal and quote
→ acceptance and instruction
→ Formal Intake
→ document collection
→ readiness decision
→ Order/Matter/Execution handoff
```

A second contrasting case should test a different operating model, such as a portfolio renewal, office action, assignment, or multi-country expansion.

### B05-WR-F04 — Product behavior is not expressed as testable scenarios

**Severity:** High  
**Affected scope:** CH08–CH22

The manuscript defines principles but rarely states observable acceptance scenarios. It does not consistently show what MarkReg should display, ask, block, warn, preserve, or hand off when information changes or conflicts.

**Required correction:** Add scenario-based conformance statements using a consistent format:

```text
Given
When
Then
Authority boundary
Evidence retained
```

Priority scenarios include applicant ambiguity, conflicting mark variants, country-bundle comparison, class uncertainty, invalid POA, expired quote, changed official fee, missing payment, professional override, and stale official status.

### B05-WR-F05 — User experience remains secondary to architecture language

**Severity:** High  
**Affected scope:** CH08–CH22

The Product promises fewer questions, progressive disclosure, clear options, transparent pricing, and explainable recommendations. Yet most chapters are written from the architecture’s perspective rather than from the user’s screen, decision, or next action.

**Required correction:** For each journey chapter, define:

- user question being resolved;
- minimum information requested;
- context reused without re-asking;
- options shown;
- assumptions exposed;
- professional intervention point;
- action available to the user;
- next-state explanation.

### B05-WR-F06 — Jurisdiction intelligence is deferred too far

**Severity:** Medium-High  
**Affected scope:** Parts II and III; planned CH45

Versioned jurisdiction packs are introduced as a solution, but their operational role is mostly deferred to Part VII. Parts II and III already depend on jurisdiction-specific rules for routes, fees, classes, item limits, documents, POA, signatures, searches, and readiness.

**Required correction:** Establish a minimum jurisdiction-pack contract before Part IV. CH45 may later address Product evolution and AI/rule versioning, but Parts II–IV need a normative dependency now.

### B05-WR-F07 — Commercial treatment needs stronger real-world controls

**Severity:** Medium  
**Affected scope:** CH16–CH18 and CH22

Pricing distinctions are conceptually sound, but the draft needs a clearer model for:

- tax-inclusive versus tax-exclusive presentation;
- currency and exchange-rate validity;
- pass-through provider fees;
- official-fee changes after acceptance;
- discounts, margin, and approval authority;
- deposits and staged payments;
- refunds and failed filings;
- later-stage fees not included in the initial quote;
- client-visible versus internal cost components.

These are essential to a Product used by agencies and professional organizations.

### B05-WR-F08 — Existing chapter metadata and review state are inconsistent

**Severity:** Medium  
**Affected scope:** manuscript headers and control records

B05-TOC-V0.1 is recorded as owner accepted in BOOK-STATUS, while some manuscript headers and prior reviews still describe it as candidate. Prior reviews also say “Owner Review Pending,” even though continued owner-directed drafting and merged PRs established acceptance of the structure and writing packs.

**Required correction:** Treat B05-REV-0001 through B05-REV-0003 as superseded pack reviews, normalize the current gate, and align chapter-map metadata during the revision pass.

## 6. Non-Blocking Findings

### B05-WR-F09 — The title is accurate but publication positioning should be clearer

The current title works as an architecture/product-specification title. The README and Preface should explicitly state that Book 05 is a Product constitution and lifecycle specification, not a jurisdictional legal manual, filing handbook, or implementation PRD.

### B05-WR-F10 — Metrics arrive too late

Metrics are planned for CH46, but Parts II and III already make measurable Product claims. Early chapters should name provisional success measures such as question reduction, recommendation revision rate, intake rework, quote-to-instruction conversion, readiness blocker frequency, and filing-package defect rate.

### B05-WR-F11 — The “full lifecycle” claim needs service-family coverage criteria

The chapter map includes filing, examination, opposition, renewal, changes, assignment, licensing, and portfolio strategy. The book should state how a service family qualifies as supported: minimum journey, required artifacts, source rules, professional gates, execution route, outcome mapping, and maintenance continuity.

### B05-WR-F12 — The manuscript needs diagrams and summary tables

The text relies heavily on prose and repeated inequality statements. Publication quality would improve through a small controlled diagram set:

- architecture responsibility map;
- end-to-end Product journey;
- artifact and decision lineage;
- readiness dimensions;
- provider route alternatives;
- Product state versus formal state versus official state.

## 7. Required Revision Pack

The next controlled pack is not Part IV. It is:

**B05-REVISION-PACK-001 — Whole-Draft Productization and Editorial Consolidation**

Required work:

1. Create the canonical Product Artifact and Decision Map.
2. Create one end-to-end filing reference journey and one contrasting lifecycle journey.
3. Add scenario-based conformance cases for Parts II and III.
4. Consolidate repeated constitutional language and add reusable rule references.
5. Define the minimum jurisdiction-pack contract required by Parts II–IV.
6. Strengthen the commercial-control model.
7. Add user-surface and next-action summaries to CH08–CH22.
8. Normalize chapter and review metadata.
9. Add the minimum diagram and summary-table set.
10. Re-run whole-draft review and decide whether Part IV may begin.

## 8. Upstream Impact

```text
Architecture Canon change required: NO
Book 02 semantic Change Proposal required: NO
Book 03 Execution change required: NO
Book 04 Product-boundary change required: NO
Book 05 structural change control required: NO
Book 05 controlled revision required: YES
```

The findings are Product-publication issues. They do not reveal a blocking contradiction in the Books 01–04 Portfolio Baseline.

## 9. Gate Decision

```text
CH00–CH22 whole-draft review: COMPLETE
B05-TOC-V0.1: RETAIN
Part I constitutional foundation: RETAIN AND CONSOLIDATE
Parts II–III Product detail: REVISE
Part IV writing: HOLD
Unrestricted implementation: NOT AUTHORIZED
Production deployment: NOT AUTHORIZED
External protected action: NOT AUTHORIZED
```

## 10. Conclusion

Book 05 has a sound architecture and a credible Product thesis. It is not yet a sufficiently concrete, testable, and publication-ready MarkReg specification.

The correct next move is a single whole-draft productization and editorial consolidation pass. Part IV should begin only after the Product artifact model, reference journeys, testable scenarios, jurisdiction-pack dependency, user surfaces, and commercial controls are made explicit.