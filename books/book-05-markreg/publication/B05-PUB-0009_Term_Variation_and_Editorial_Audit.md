# B05-PUB-0009 — Term Variation and Editorial Audit

## Status

- **Status:** Controlled Audit v0.1 — PF-06A complete
- **Applies to:** CH00–CH47, B05-SPEC-0001 through B05-SPEC-0004, Appendix A–G and publication records
- **Editorial standard:** B05-PUB-0001 v0.2
- **Source reviews:** B05-REV-0012 through B05-REV-0017
- **Acceptance review:** B05-REV-0018

## 1. Purpose

This audit records the terminology, repetition, structure and native-English issues that must be resolved during PF-06.

It is an editorial control record, not a replacement manuscript and not evidence that line-by-line editing is complete.

The audit uses:

- the complete CH00–CH47 manuscript baseline;
- the four reconciled controlled specifications;
- Appendix A–G;
- complete-manuscript and publication-finishing reviews;
- representative line-level sampling from Front Matter and Part I;
- known variation patterns identified while writing Parts II–VII.

Full closure requires the PF-06B, PF-06C and PF-06D editorial passes.

## 2. Audit Classification

Each finding is classified as:

| Class | Meaning | Required treatment |
| --- | --- | --- |
| T1 | controlled capitalization variation | normalize to B05-PUB-0001 |
| T2 | unstable artifact or state name | replace with accepted noun phrase or record ordinary usage explicitly |
| T3 | authority verb ambiguity | name actor, object and effect |
| T4 | official/provider/Product state ambiguity | identify source and state domain |
| T5 | repeated constitutional explanation | preserve first full explanation; compress later repetition through cross-reference |
| T6 | chapter progression weakness | clarify purpose, output and next handoff |
| T7 | native-English or sentence-density issue | simplify without changing meaning |
| T8 | client-facing clarity issue | replace internal jargon or expose necessary consequence |
| S1 | possible semantic conflict | do not edit silently; open Review finding |

## 3. Current Blocking Findings

No blocking architecture conflict was identified during PF-06A.

The audit did not identify a need to amend:

- the Architecture Canon;
- Book 02 Core semantics;
- Book 03 Execution authority;
- Book 04 Workplace and Product boundaries;
- B05-TOC-V0.1;
- B05-SPEC-0001 through B05-SPEC-0004 controlled IDs;
- `EMBERLOOP` or `RIVERKITE` final states.

Line-by-line editorial work may still reveal a semantic issue. Any such issue must use the S1 process in B05-PUB-0001.

## 4. Controlled Capitalization Findings

### 4.1 Product and architecture terms

The manuscript uses ordinary and controlled forms of `product`, `workplace`, `core`, `execution`, `review`, `decision`, `communication`, `document`, `evidence`, `knowledge`, `capability`, `order`, `matter` and `task`.

Required treatment:

- capitalize only when the defined MarkOrbit concept is intended;
- retain lowercase for ordinary-language uses;
- review every capitalized occurrence for actual controlled meaning;
- avoid capitalizing generic words merely to create emphasis.

Priority files:

- CH00–CH07 for the first definitions;
- CH18–CH29 for Order, Matter, Review, Approval and Execution;
- CH30–CH42 for Evidence, Communication and official-state usage;
- CH43–CH47 for Product, Workplace, Knowledge and AI governance.

### 4.2 Human terms

Use:

- Human Review;
- Human Judgment;
- Human Selection;
- eligible Human actor.

Do not alternate without purpose among `human review`, `professional review`, `manual review` and `expert check`.

`Professional Review` is the preferred artifact/action name where the reviewer is an eligible professional. `Human Review` remains the broader constitutional boundary.

## 5. Artifact and Record-Name Findings

### 5.1 `package`

The manuscript uses `package` for several distinct meanings:

- Filing Package Candidate;
- Response Package Candidate;
- Renewal Package Candidate;
- country or service bundle;
- provider delivery package;
- rendered submission materials.

Required treatment:

- use the full controlled name where lifecycle or authority matters;
- use lowercase `package` only as a clearly ordinary collective noun;
- do not describe a Candidate as approved or filed without a separate Decision and evidence state.

### 5.2 `form`

Differentiate:

- user-facing interface;
- Formal Intake;
- official form;
- rendered filing form;
- questionnaire.

The recurring statement that MarkReg is “not a form” should be compressed after CH02. Later chapters should explain the specific role of a form rather than repeat the constitutional rejection.

### 5.3 `record`, `snapshot`, `view`, `context`, `set`, `baseline` and `envelope`

These suffixes are not interchangeable.

| Suffix | Editorial meaning |
| --- | --- |
| Record | retained controlled fact, rule, Decision or evidence identity |
| Snapshot | sourced state at a stated time |
| View | explainable projection across underlying records |
| Context | scoped facts and relationships for a journey or proceeding |
| Set | bounded collection with common purpose and version |
| Baseline | reviewed reference state against which later change is assessed |
| Envelope | typed transfer of references, versions, responsibility and expected result |

Every edit must preserve the suffix defined by B05-SPEC-0001.

## 6. Decision, Review and Approval Findings

The manuscript correctly separates recommendation, Decision, Review and Approval, but the full distinction is repeated frequently.

Required editorial pattern:

- Part I: retain full constitutional explanation;
- Part II: explain recommendation versus Decision in the strategy context;
- Part III: explain Client Acceptance and commercial authority;
- Part IV: explain Professional Review and Filing Approval in full;
- Parts V–VII: cross-reference the established rules and state only the new proceeding-specific application.

High-risk substitutions to reject:

```text
recommendation accepted
≠ Professional Review complete
≠ Filing Approval active
≠ external action authorized
```

## 7. State and Evidence Findings

### 7.1 `filed`

Potential meanings include:

- prepared;
- queued;
- sent;
- delivery confirmed;
- provider reports filed;
- officially acknowledged.

Every ambiguous use must be replaced with the evidenced state.

### 7.2 `registered`

Differentiate:

- allowance or acceptance;
- publication without challenge;
- registration event;
- registration verified from official source;
- certificate received;
- current Right Baseline.

### 7.3 `renewed`

Differentiate:

- renewal candidate prepared;
- Renewal Approval active;
- request sent;
- acknowledgement received;
- renewed official state verified.

### 7.4 `transferred`

Differentiate:

- commercial agreement signed;
- assignment effective between parties;
- recordal submitted;
- official owner updated;
- Chain-of-Title View reconciled.

### 7.5 `complete`

Replace generic completion language with the domain completed:

- intake complete;
- Review complete;
- payment condition satisfied;
- submission sent;
- acknowledgement received;
- official procedure closed.

## 8. Jurisdiction and Pack Findings

The earlier manuscript sometimes uses broad phrases such as:

- country rules;
- country configuration;
- jurisdiction support;
- supported country;
- current legal Knowledge.

Required treatment:

- use `Jurisdiction Pack` where the controlled configuration is intended;
- identify jurisdiction, service, stage, Pack Version and support state;
- use `Source Record` and `Rule Record` for controlled sources and rules;
- distinguish provider advice and organization overlays from official rules;
- avoid implying that a new-filing module supports later proceedings.

Accepted support states are:

- Research Only;
- Guidance Capable;
- Preparation Capable;
- Execution Capable;
- Lifecycle Capable;
- Suspended;
- Retired.

## 9. Commercial-Term Findings

The manuscript must preserve:

```text
official fee
≠ mandatory third-party cost
≠ professional fee
≠ provider pass-through
≠ internal provider cost
≠ tax
≠ currency adjustment
≠ discount
≠ credit
≠ margin
```

Priority review areas:

- CH17–CH18;
- CH25–CH29;
- CH31–CH41;
- CH44–CH45;
- Appendix F;
- all client-facing examples.

Required edits:

- use `client price` for the amount shown to the client;
- never hide internal margin in an official-fee label;
- identify later-stage fees as included, excluded, estimated or unknown;
- preserve immutable Quote versions;
- name the variance path when a fee, form or Rule changes.

## 10. Provider and Routing Findings

The manuscript uses several provider-stage expressions.

Required sequence:

```text
Capability Need
→ provider candidates
→ Routing Recommendation
→ Human Selection
→ appointment and instruction
→ provider receipt
→ Provider Acceptance or change proposal
→ governed work
→ provider report and returned Evidence
```

Do not compress these into `provider selected and filed`.

Use `private-first provider discovery` only where the organization’s existing relationships are intentionally checked before wider governed discovery. Do not imply an open marketplace.

## 11. AI-Term Findings

Normalize AI language around assistance:

- extracts;
- compares;
- drafts;
- proposes;
- flags;
- summarizes;
- classifies a candidate.

A Human:

- reviews;
- accepts;
- modifies;
- rejects;
- approves;
- instructs;
- remains accountable.

Priority files:

- CH00, CH02–CH06;
- CH13–CH15;
- CH19–CH20;
- CH31–CH32;
- CH42–CH47;
- Appendix C, E–G.

## 12. Repetition Findings

### 12.1 Constitutional boundary list

The full boundary list appears appropriately in Front Matter and Part I but should not be repeated in full throughout the later manuscript.

Later chapters should normally reference:

- MR-CR-01 through MR-CR-08;
- Appendix B for state and authority;
- Appendix C for participant rights;
- B05-SPEC-0001 for record contracts.

### 12.2 Recommendation is not Decision

Retain the full explanation in CH06–CH07 and its concrete application in Part II. Later chapters should state only the new consequence.

### 12.3 Readiness, Approval, Execution and official effect

Retain the full progression in CH21–CH29. Later chapters should cross-reference it and focus on response, renewal or recordal-specific behavior.

### 12.4 Product projection is not official truth

Retain the foundational rule in CH07 and the full official-event application in CH28–CH30. Later chapters should use concise sourced-state wording.

### 12.5 AI does not replace Human Review

Retain the constitutional explanation in Part I and detailed governance in CH45. Other chapters should describe the local AI task and required Human disposition.

## 13. Chapter-Progression Findings

A finished chapter should answer three closing questions:

1. What controlled output now exists?
2. What is still unresolved?
3. What does the next chapter add?

Priority handoff improvements:

- CH07 → CH08: from lifecycle/state model to Need Brief;
- CH15 → CH16: from risk assessment to Proposal and Option design;
- CH22 → CH23: from governed formal handoff to Filing Package Candidate;
- CH29 → CH30: from execution recovery to official event interpretation;
- CH36 → CH37: from outcome Communication to Right Baseline;
- CH42 → CH43: from portfolio continuity to Product experience;
- CH45 → CH46: from rule governance to metrics and MVP evidence;
- CH46 → CH47: from evaluation to conformance and roadmap.

## 14. Native-English Findings

Common patterns to revise:

- repeated one-sentence paragraphs that interrupt flow without adding emphasis;
- noun stacks such as `jurisdiction-service-stage support evidence state`;
- excessive use of `may` in successive sentences;
- repeated `The Product must...` clauses that can be grouped;
- abstract openings that delay the user question;
- long lists followed by a second list restating the same dimensions;
- passive constructions that hide the responsible actor;
- inconsistent use of `which` and `that` in restrictive clauses;
- inconsistent serial commas and hyphenation.

The edit should not remove deliberate short sentences used for constitutional emphasis.

## 15. Client-Facing Findings

Client examples should prefer:

- `We still need to confirm who should own the application`;
- `The provider reports that the filing was submitted; the official receipt is still pending`;
- `This price excludes examination-response and registration-stage fees`;
- `The renewal request has been sent; the renewed register entry has not yet been verified`.

Avoid exposing:

- internal margin;
- provider ranking notes;
- unreviewed AI reasoning;
- internal architecture labels when a business explanation is sufficient.

## 16. Metadata Findings

Current active metadata remains inconsistent:

```text
CH00–CH01
- Complete Draft 1
- B05-TOC-V0.1 — Owner Accepted

CH02–CH47
- historical Part/Foundation Draft labels remain in active files
- some active headers still use Candidate wording
```

Required target:

```text
Status: Complete Draft 1
Chapter Map: B05-TOC-V0.1 — Owner Accepted
```

Metadata should be normalized with the corresponding editorial batch:

- PF-06B: CH02–CH22;
- PF-06C: CH23–CH47.

PF-01 remains open until both batches pass.

## 17. Glossary Findings

The initial glossary covers the primary artifacts but requires additions from PF-04 and PF-05, including:

- Conformance Scenario;
- Zero-Tolerance Scenario;
- Pack Version;
- Pack Support State;
- Source Record;
- Rule Change Candidate;
- Provider Acceptance;
- Provider Report;
- Official Acknowledgement Evidence;
- Client Price;
- Internal Provider Cost;
- Organization Overlay;
- Professional Owner;
- Support Claim;
- External Protected Action.

B05-PUB-0003 v0.2 adds these working definitions. Final chapter links remain PF-06D/PF-07 work.

## 18. Subject-Index Findings

The seed index is structurally sound but requires:

- new Pack and support-state entries;
- scenario and zero-tolerance entries;
- commercial visibility entries;
- provider-stage entries;
- cross-references for recommendation, Decision, Review and Approval;
- removal of any term not retained after editing;
- rendered page references after layout stabilizes.

B05-PUB-0004 v0.2 provides the controlled working index. It is not the final rendered index.

## 19. Editorial Batch Plan

### PF-06B — Front Matter and Parts I–III

Scope:

- CH00–CH22;
- metadata CH02–CH22;
- chapter openings and handoffs;
- recommendation, intake, commercial and readiness terminology;
- client-facing examples in early journey chapters.

### PF-06C — Parts IV–VII

Scope:

- CH23–CH47;
- metadata CH23–CH47;
- Review, Approval, Execution, official-event, portfolio, Pack, AI, metric and conformance terminology;
- case final-state preservation.

### PF-06D — Whole-book closure

Scope:

- B05-SPEC-0001 through B05-SPEC-0004;
- Appendix A–G;
- publication apparatus;
- cross-reference and transition audit;
- glossary and index reconciliation;
- unresolved semantic findings;
- final editorial Review.

## 20. Acceptance State

```text
Editorial standard established: COMPLETE
Term-variation classes established: COMPLETE
Known variation families recorded: COMPLETE
Metadata target recorded: COMPLETE
Glossary working additions: COMPLETE IN B05-PUB-0003 v0.2
Subject-index working additions: COMPLETE IN B05-PUB-0004 v0.2
CH00–CH47 line-by-line edit: OPEN
Specification and appendix final edit: OPEN
Whole-book terminology validation: OPEN
PF-06 overall: OPEN
```

This audit is superseded only by a later reviewed audit or final PF-06 closure record.