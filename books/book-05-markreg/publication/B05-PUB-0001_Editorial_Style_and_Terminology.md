# B05-PUB-0001 — Editorial Style and Terminology

## Status

- **Status:** Controlled Editorial Standard v0.2 — PF-06A complete
- **Source:** B05-REV-0012, B05-REV-0014 through B05-REV-0017 and B05-PUBLICATION-FINISHING-PACK-001
- **Primary workstream:** PF-06
- **Applies to:** CH00–CH47, B05-SPEC-0001 through B05-SPEC-0004, Appendix A–G and the publication apparatus
- **Last reconciliation:** B05-REV-0018

## 1. Purpose

This record controls the editorial finishing of Book 05.

The goal is to make the publication shorter, clearer and more natural in English without changing Product semantics, authority, source hierarchy, controlled identifiers, reference-journey states or declared support scope.

```text
editorial improvement
= clearer expression of accepted meaning

editorial improvement
≠ silent Product redesign
```

A proposed change that alters meaning must be recorded as a semantic finding and reviewed separately.

## 2. Editorial Voice

Book 05 should be:

- direct;
- precise;
- professionally neutral;
- readable by Product, legal, operations and engineering audiences;
- explicit about uncertainty, responsibility and authority;
- concrete through named artifacts, examples and scenarios;
- concise where a controlled specification or appendix already carries the detail.

Avoid:

- promotional superlatives;
- unsupported legal certainty;
- vague futurism;
- generic claims that AI, automation or the Product “handles everything”;
- repeated architectural disclaimers that do not add chapter-specific meaning;
- long parallel lists where a table or controlled cross-reference is clearer.

## 3. Normative Language

Use normative verbs intentionally.

| Verb | Controlled use |
| --- | --- |
| `must` | constitutional, safety, authority or conformance requirement |
| `must not` | prohibited behavior or boundary |
| `should` | recommended Product or editorial behavior with possible justified exceptions |
| `may` | permitted but not required behavior |
| `can` | factual capability, not permission or authority |

Do not use `can` when the intended meaning is permission, and do not use `should` where a zero-tolerance rule requires `must`.

## 4. Controlled Capitalization

Capitalize a term when it refers to a defined MarkOrbit or MarkReg concept.

| Controlled term | Usage |
| --- | --- |
| Product | a focused governed Product under Book 04 architecture |
| Workplace | the organization-level operating environment and Orbit context |
| Core | Book 02 shared semantics and contracts |
| Execution | Book 03 governed execution system or a defined execution context |
| Review | a defined accountable review action or record |
| Decision | a defined accountable decision, not an informal choice |
| Communication | a governed communication artifact or action |
| Document | a formal or controlled document object, not every uploaded file |
| Evidence | controlled evidence with provenance and purpose |
| Knowledge | governed reusable Knowledge, not any text or memory |
| Capability | a typed ability with evidence and scope |
| Matter / Order / Task | formal shared objects where applicable |
| Human Review / Human Judgment / Human Selection | accountable Human roles and actions |
| Jurisdiction Pack / Pack | a controlled jurisdiction-and-service configuration defined by B05-SPEC-0004 |
| Rule Record / Source Record | controlled governance records defined by B05-SPEC-0001 and B05-SPEC-0004 |
| Conformance Profile | a declared capability profile defined by Appendix G |

Use lowercase for ordinary language when the defined concept is not intended.

Examples:

- `the client reviews the summary` — ordinary activity;
- `Professional Review is complete` — controlled action;
- `the system executes a calculation` — ordinary verb;
- `the request enters Execution` — Book 03 context.

## 5. Stable Artifact Names

Use the accepted noun phrase consistently.

### Recommendation and commercial journey

- Business Context Snapshot;
- Need Brief;
- Recommendation Set;
- Option Set;
- Proposal;
- Quote;
- Client Acceptance;
- Commercial Instruction.

### Intake and filing journey

- Formal Intake;
- Requirement Set;
- Readiness Assessment;
- Handoff Envelope;
- Filing Package Candidate;
- Professional Review;
- Filing Approval;
- Capability Need;
- Routing Recommendation;
- Provider Acceptance;
- Execution Request;
- Submission Evidence;
- Official Acknowledgement Evidence.

### Post-filing and portfolio journey

- Official Event Snapshot;
- Examination Context;
- Issue Set;
- Response Strategy;
- Response Package Candidate;
- Adversarial Context;
- Deadline Record;
- Outcome Snapshot;
- Registration Outcome Snapshot;
- Right Baseline;
- Maintenance Obligation Set;
- Renewal Package Candidate;
- Recordal Context;
- Transaction Context;
- Chain-of-Title View;
- Portfolio Continuity View;
- Portfolio Action Plan.

### Product and governance journey

- Product Session;
- Return Envelope;
- Jurisdiction Pack;
- Pack Version;
- Source Record;
- Rule Record;
- Rule Change Candidate;
- Conformance Scenario;
- Conformance Profile.

Do not alternate casually between `form`, `record`, `package`, `context`, `snapshot`, `view`, `set`, `envelope`, `candidate` and `baseline`. Each suffix communicates a different lifecycle and authority meaning.

## 6. Controlled Substitutions

Use these substitutions where the old wording is not intentionally ordinary language.

| Avoid or review | Preferred controlled expression |
| --- | --- |
| application form as the whole journey | filing form or official form, within a broader Product journey |
| final recommendation | Recommendation Set or reviewed recommendation |
| approved package | exact Filing Package Candidate version with stated Review and Approval states |
| case | Matter, proceeding, journey or reference case, according to meaning |
| official status | sourced official state or Product projection, according to authority |
| filed | provider reports submitted, sent, officially acknowledged or filed according to evidence |
| completed | name the completed Product, commercial, Review, Execution or official state |
| country database | Jurisdiction Pack, official source collection or country data, according to meaning |
| country support | jurisdiction/service Pack module and support state |
| AI decision | AI proposal or draft followed by accountable Human Decision |
| provider selected | Routing Recommendation or Human Selection, according to stage |
| provider instructed | instruction sent, provider received or Provider Acceptance, according to evidence |
| legal owner | applicant, business owner, contractual owner or official owner, according to source |
| renewal complete | renewal request sent, acknowledged or renewed state verified |
| transfer complete | assignment signed or ownership recordal verified |
| one global status | Portfolio Continuity View across independent rights |

## 7. Authority Verbs

Prefer explicit actor-and-effect verbs:

- proposes;
- recommends;
- records;
- confirms;
- reviews;
- approves;
- instructs;
- accepts;
- executes;
- reports;
- acknowledges;
- verifies;
- corrects;
- supersedes;
- suspends;
- retires.

Avoid vague verbs such as `handles`, `owns everything`, `automates`, `completes` or `decides` unless the actor, object and authority are clear.

## 8. State Language

Do not write `filed`, `registered`, `renewed`, `transferred`, `accepted` or `completed` without identifying the source or state domain where ambiguity is possible.

Preferred examples:

- provider reports submission completed — official acknowledgement pending;
- delivery confirmed — provider receipt not yet verified;
- official acknowledgement received;
- registration verified from the official record;
- certificate file received — current official record still controls;
- renewal request sent — renewed status pending verification;
- assignment signed — ownership recordal pending;
- Rule Change Candidate detected — Pack Version not yet released.

## 9. AI Language

AI is an assisting capability, not an accountable participant.

Preferred language:

- AI assists;
- AI proposes;
- AI extracts;
- AI compares;
- AI drafts;
- AI classifies a candidate;
- AI flags uncertainty;
- a Human reviews, accepts, modifies or rejects the output.

Prohibited or misleading language includes:

- AI approves;
- AI grants authority;
- AI files autonomously;
- AI determines the legal owner;
- AI guarantees availability or registration;
- AI publishes a Jurisdiction Pack;
- AI creates official truth.

## 10. Source and Confidence Language

Every material rule, fee, deadline, official event or outcome should use appropriate source and freshness language.

Use distinctions such as:

- official source;
- verified official Evidence;
- verified provider evidence;
- professional interpretation;
- organization experience;
- secondary source;
- Product projection;
- current, checked, stale, disputed, superseded, unavailable or unknown.

Avoid `the law says`, `the fee is` or `the deadline is` where the jurisdiction, source, effective period and interpretation status are not controlled.

## 11. Commercial Language

Preserve the commercial layers defined by B05-SPEC-0004:

```text
official fee
≠ mandatory third-party cost
≠ professional fee
≠ provider pass-through
≠ internal provider cost
≠ tax
≠ currency adjustment
≠ margin
```

Use `client price` for the amount or component shown to the client. Use `internal cost` or `internal margin` only in organization-private contexts.

Never describe internal cost or margin as an official fee.

## 12. Jurisdiction-Support Language

Do not state that MarkReg “supports a country” without scope.

Preferred form:

```text
jurisdiction
+ service family
+ lifecycle stage
+ Pack Version
+ support state
```

Use the accepted support states:

- Research Only;
- Guidance Capable;
- Preparation Capable;
- Execution Capable;
- Lifecycle Capable;
- Suspended;
- Retired.

A new-filing module does not imply support for examination, opposition, renewal, recordal or transaction work.

## 13. Chapter Structure

A finished chapter should make the following progression visible:

1. purpose or user question;
2. chapter-specific Product problem;
3. controlled concepts, artifacts or states;
4. authority, source and version boundaries;
5. reference journey or concrete example;
6. conformance or failure behavior;
7. minimum Product lock;
8. handoff to the next chapter.

Not every chapter needs identical headings. Repeated template headings may be compressed when the logical progression remains clear.

## 14. Compression Rules

### Keep a full explanation when

- the concept is introduced for the first time;
- the chapter changes the reader’s mental model;
- a safety or authority distinction would otherwise be lost;
- the chapter applies a shared rule in a materially new lifecycle context.

### Use a cross-reference when

- the same constitutional boundary has already been established;
- a full state or role matrix exists in Appendix B or C;
- the detailed record contract exists in B05-SPEC-0001;
- the scenario already exists in B05-SPEC-0003 or Appendix E;
- the jurisdiction and commercial rule exists in B05-SPEC-0004 or Appendix F.

### Do not compress

- source hierarchy;
- exact-version approval;
- official versus provider evidence;
- unknown-state and duplicate-safety behavior;
- participant authority;
- case final-state locks;
- Pack support scope;
- zero-tolerance requirements.

## 15. Repeated Constitutional Language

Part I may explain the full architecture boundaries.

Parts II–VII should normally use a short reference such as:

> The chapter applies MR-CR-01 through MR-CR-08 and the state distinctions in Appendix B. It adds the chapter-specific behavior below.

Do not repeat the complete `MarkReg ≠ Workplace ≠ Core ≠ Execution` list in every chapter unless a new boundary is being tested.

## 16. Chapter Transitions

Each chapter should end with a forward link that states:

- what controlled output now exists;
- what remains unresolved;
- why the next chapter is necessary.

Preferred pattern:

```text
This chapter produces [artifact/state].
It does not yet resolve [next material question].
CHxx therefore defines [next subject].
```

Avoid generic endings such as `the next chapter continues the journey` without naming the handoff.

## 17. Lists and Tables

Use a table when the reader compares:

- participants;
- states;
- alternatives;
- price components;
- sources;
- versions;
- support levels;
- lifecycle stages.

Use bullets for a small set of parallel items.

Avoid long repeated lists that restate a controlled matrix. Reference the specification or appendix instead.

## 18. Reference Cases

Use `EMBERLOOP` and `RIVERKITE` as the recurring examples.

Their final reviewed states are locked:

```text
EMBERLOOP
- United Kingdom: registered with a Right Baseline and maintenance obligations
- United States: under examination after acknowledged Response Package v2
- European Union: verified opposition without assumed closure
- Japan and Australia: future-action candidates only

RIVERKITE
- six independent registrations
- four ordinary renewal workflows
- one ownership-linked renewal
- one cancellation-defense right
- evidence and licence actions remain open
```

A new example should appear only when it tests materially different behavior. Examples are not legal advice, precedent or guaranteed outcomes.

## 19. Cross-References

Use stable identifiers consistently:

- `CH24`;
- `Appendix B`;
- `B05-SPEC-0001`;
- `B05-REV-0017`;
- `MR-CR-04`;
- `MR-SCN-23`;
- `EL-28`;
- `RK-12`.

Final rendered editions may add page references, but source Markdown must retain stable identifiers.

## 20. Metadata Rule

Active manuscript metadata must use:

```text
Status: Complete Draft 1
Chapter Map: B05-TOC-V0.1 — Owner Accepted
```

Historical reviews may retain their original status language.

Metadata normalization may be completed with the corresponding editorial chapter batch. PF-01 remains open until CH02–CH47 are normalized.

## 21. Client-Facing Examples

Client-facing wording should:

- use business language first;
- state the relevant jurisdiction and service scope;
- distinguish recommendation from Decision;
- distinguish price from official fee;
- distinguish provider report from official status;
- show the next accountable actor;
- avoid internal margin, provider ranking notes and unreviewed AI reasoning.

## 22. Prohibited Editorial Drift

Editing may not silently:

- redefine a Core object;
- move authority from Human to Product or AI;
- merge readiness, approval, Execution and official effect;
- convert provider evidence into official truth;
- convert one jurisdiction, provider or case into a global rule;
- turn MGSN into an open marketplace;
- make Product metrics imply legal causation;
- broaden a Jurisdiction Pack support claim;
- change `EMBERLOOP` or `RIVERKITE` final states;
- change controlled IDs or scenario behavior;
- expand implementation, production or protected-action authority.

## 23. Semantic-Finding Rule

When an editor finds a possible meaning conflict:

1. preserve the current controlled wording;
2. record the exact file and passage;
3. identify the conflicting specification, chapter or upstream book;
4. classify the issue as terminology, internal contradiction, cross-book conflict or proposed semantic change;
5. resolve it through a Review record before changing meaning.

## 24. Editorial Batch Sequence

```text
PF-06A
- editorial standard
- term-variation audit
- glossary and index working baseline

PF-06B
- CH00–CH22
- Front Matter and Parts I–III
- metadata normalization for CH02–CH22

PF-06C
- CH23–CH47
- Parts IV–VII
- metadata normalization for CH23–CH47

PF-06D
- specifications, appendices and publication apparatus
- whole-book terminology and transition review
- semantic-finding closure
```

The batches are editorial control boundaries, not new chapter-map stages.

## 25. Completion Evidence

PF-06 is complete only when:

- CH00–CH47 pass line-by-line editorial review;
- B05-SPEC-0001 through B05-SPEC-0004 and Appendix A–G use the controlled terminology;
- the term-variation report has no unresolved blocking variation;
- metadata normalization is complete or formally closed under PF-01;
- the Glossary and Subject Index reflect the edited manuscript;
- no uncontrolled semantic change remains;
- a whole-book editorial Review accepts the result.

B05-PUB-0001 v0.2 completes the editorial standard. It does not by itself complete PF-06.