# B04-REV-0002 — CH00–CH27 Architecture and Editorial Review

**Review date:** 2026-07-14  
**Book:** Book 04 — MarkOrbit Workplace and Product Architecture  
**Chapter map:** B04-TOC-V0.1  
**Scope:** B04-CH-00 through B04-CH-27  
**Reviewer role:** Architecture and editorial review  
**Outcome:** Revision applied; owner review pending

## 1. Review Purpose

This review pauses manuscript expansion after CH27 and re-reads Book 04 from CH00 to CH27 as one continuous architecture argument.

The review tests whether the completed Front Matter and Parts I–IV:

- remain aligned with the MarkOrbit Orbital Architecture Canon vNext;
- preserve the Frozen Book 02 Core Specification Baseline;
- preserve the owner-accepted Book 03 Execution authority model;
- follow B04-TOC-V0.1 without title, numbering, or structural drift;
- maintain consistent responsibility and authority language;
- avoid turning architectural profiles into PRDs or implementation specifications;
- preserve progression from Workplace to organization context, capability consumption, Product architecture, and lifecycle continuity.

The review does not authorize CH28–CH39 drafting, final publication, unrestricted implementation, production deployment, or external protected action.

## 2. Authority Sources

The review used the following precedence:

1. MarkOrbit Orbital Architecture Canon vNext;
2. Frozen Book 02 Core Specification Baseline v0.1;
3. owner-accepted Book 03 Execution System;
4. B04-TOC-V0.1;
5. Book 04 governance, planning, and existing manuscript drafts.

## 3. Review Method

The review covered:

- chapter title and numbering validation;
- Part and chapter-boundary validation;
- Core / Execution / Workplace / Product / MGSN / Owning Service responsibility alignment;
- Candidate Before Canonical and Human Review boundaries;
- Product-profile conformance for Lite, MarkReg, and MGSN Gateway;
- cross-Product context, Handoff, Review, Artifact, and outcome continuity;
- terminology and responsibility wording;
- code-fence and numbered-section integrity;
- repository status and manuscript-inventory accuracy.

## 4. Overall Finding

CH00–CH27 form a coherent Draft baseline for Front Matter and Parts I–IV.

No chapter renumbering, title change, Part movement, Book 02 semantic amendment, or Book 03 Execution amendment is required.

The review found no critical architecture contradiction and no reason to reopen B04-TOC-V0.1.

The main corrections were:

- replacing wording that attributed organizational control to Workplace itself rather than to the organization represented through Workplace;
- replacing ownership wording for Core and Execution with the Canon's responsibility verbs;
- replacing `formal truth` with `formal business facts` or `authoritative formal business state`;
- clarifying that Candidate Before Canonical requires professional validation and governed review, not automatically the formal Human Review contract in every case;
- clarifying that Approval is attributable to an eligible human acting under a governed authority, while Permission and Policy remain separate gates;
- aligning Lite's action spine with the Canon;
- aligning MarkReg's lifecycle with search and risk, proposal and quote, Order and Matter formalization, governed filing, and the managed professional-service ecosystem positioning;
- correcting registration-certificate treatment across Artifact, Document, and Evidence boundaries;
- aligning Artifact continuity with `Content → Artifact → Human Review → Render → Optional Edit → Delivery / Publish`;
- synchronizing repository-level and Book 04 status records with the actual CH00–CH27 manuscript state.

## 5. Chapter Review Matrix

| Chapter | Review result | Action |
| --- | --- | --- |
| CH00 | Conformant with one sequence wording issue | Reordered Part IV topic summary to match B04-TOC-V0.1 |
| CH01 | Conformant | No manuscript change |
| CH02 | Conformant | No manuscript change |
| CH03 | Conformant | No manuscript change |
| CH04 | Conformant | No manuscript change |
| CH05 | Conformant after governance wording repair | Replaced automatic Human Review implication with professional validation and governed review |
| CH06 | Conformant after actor-language repair | Returned network participation and selection authority to the organization represented through Workplace |
| CH07 | Conformant | No manuscript change |
| CH08 | Conformant | No manuscript change |
| CH09 | Conformant | No manuscript change |
| CH10 | Conformant after control-language repair | Clarified that the organization or authorized client context governs private Knowledge within Workplace |
| CH11 | Conformant | No manuscript change |
| CH12 | Conformant | No manuscript change |
| CH13 | Conformant | No manuscript change |
| CH14 | Conformant | No manuscript change |
| CH15 | Conformant | No manuscript change |
| CH16 | Conformant | No manuscript change |
| CH17 | Conformant after formal-state wording repair | Replaced `formal truth` with `formal business facts` |
| CH18 | Conformant | No manuscript change |
| CH19 | Conformant after Approval-authority clarification | Bound Approval to an eligible human and separated Permission / Policy decisions |
| CH20 | Conformant | No manuscript change |
| CH21 | Conformant after responsibility-language repair | Restored Canon verbs for Workplace, Core, Execution, Owning Services, and humans |
| CH22 | Conformant | No manuscript change |
| CH23 | Conformant after Canon alignment | Added the canonical Lite action spine and refined outcome-preparation language |
| CH24 | Conformant after lifecycle and object-boundary repair | Added search/risk, quote, Order/Matter formalization, managed-ecosystem positioning, and certificate distinctions |
| CH25 | Conformant after organization/Routing wording repair | Returned participation control to the organization and clarified Routing Service responsibility |
| CH26 | Conformant after local-authority wording repair | Replaced `formal truth` with authoritative formal business state and corrected `on-premises` terminology |
| CH27 | Conformant after Artifact and formal-state repair | Aligned Artifact progression with the Canon and restored Owning Service language |

## 6. Structural Validation

The reviewed manuscript contains:

- 28 files from CH00 through CH27;
- exact title alignment with B04-TOC-V0.1;
- continuous chapter numbering;
- balanced fenced code blocks;
- sequential numbered sections within each chapter;
- no duplicate chapter titles;
- no Part V or Part VI manuscript draft added by this review.

Approximate manuscript size for CH00–CH27: 118,000 English word tokens under the repository review script's counting method.

## 7. Cross-Book Boundary Finding

The reviewed chapters preserve the following lock:

```text
Core defines shared meaning.

Execution governs coordinated work.

Workplace preserves and provides authorized organizational context.

Products own focused user journeys.

MGSN connects independent Orbits.

Owning Services change formal business facts.

Human professionals remain accountable.

AI assists under identity, permission, context, review, and audit.
```

No reviewed chapter authorizes:

- autonomous filing;
- autonomous external Communication;
- payment;
- provider appointment or instruction;
- official recordal;
- Product-level protected-state mutation;
- unrestricted cross-Product or cross-Workplace data sharing.

## 8. Product Profile Finding

The Lite, MarkReg, and MGSN Gateway chapters remain architectural profiles.

They do not replace:

- Book 05 — MarkReg;
- Book 06 — MarkOrbit Lite;
- Book 07 — Mark Global Service Network;
- Product charters;
- PRDs;
- jurisdiction specifications;
- technical architecture;
- implementation ADRs.

## 9. Repository Status Finding

Repository metadata was materially stale before this review. It still described Book 04 as Pack 01 drafting with only CH02 completed, even though CH00–CH27 existed.

This review updates:

- root README, manifest, roadmap, and changelog;
- `books/README.md`;
- Book 04 README, manifest, status, governance, and `publication.yaml`;
- Book 04 writing-gate and writing-pack planning records;
- Book 04 review index.

## 10. Deferred Work

The following remain open:

1. owner review of this CH00–CH27 revision branch;
2. final compression and repetition review after the complete CH00–CH39 manuscript exists;
3. native-English line editing;
4. diagrams and architecture figures;
5. cross-book citations and link enrichment;
6. glossary and index reconciliation;
7. Part V and Part VI chapter briefs and drafting;
8. final publication readiness review;
9. implementation and protected-action gates.

## 11. Review Decision

```text
CH00–CH27
→ architecture and editorial review completed
→ targeted corrections applied
→ repository status synchronized
→ drafting paused before CH28
→ owner review pending
```

Ready for final publication: **NO**  
Ready for unrestricted implementation: **NO**  
External protected action authorized: **NO**
