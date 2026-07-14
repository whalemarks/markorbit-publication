# B05-PUB-0008 — Release Candidate 1 Checklist

## Status

- **Status:** Controlled Scaffold
- **Current book state:** Complete Draft 1
- **Target:** Book 05 Release Candidate 1
- **Source:** B05-REV-0012 and B05-PUBLICATION-FINISHING-PACK-001

## 1. Decision Rule

Book 05 may advance to Release Candidate 1 only when the manuscript, controlled specifications, appendices, publication apparatus, figures and validation evidence form one reconciled publication baseline.

```text
Complete Draft 1
+ specification reconciliation
+ publication finishing
+ structural and rendered validation
+ review
→ RC1 candidate

RC1 candidate
+ owner publication gate
→ RC1
```

RC1 is still not software implementation or production authority.

## 2. Manuscript and Metadata

- [ ] all CH00–CH47 files are present;
- [ ] all active chapter titles match B05-TOC-V0.1;
- [ ] all active chapter metadata uses the owner-accepted chapter map;
- [ ] historical `Candidate` and obsolete active status wording is removed;
- [ ] chapter and part ranges validate;
- [ ] CH01 includes Appendix A–G and reader-facing Back Matter;
- [ ] chapter transitions and final conclusion are reconciled;
- [ ] no new chapter or appendix silently changes the accepted structure.

## 3. Controlled Specifications

- [ ] B05-SPEC-0001 applies through CH47;
- [ ] all material artifacts and decisions are registered or explicitly classified;
- [ ] B05-SPEC-0002 contains complete `EMBERLOOP` and `RIVERKITE` timelines;
- [ ] B05-SPEC-0003 applies through CH47 and indexes priority scenarios and surfaces;
- [ ] B05-SPEC-0004 covers filing, post-filing, maintenance, renewal, recordal and rule-version controls;
- [ ] specification IDs and chapter references validate;
- [ ] no appendix conflicts with a controlled specification.

## 4. Appendices

- [ ] Appendix A reconciled with B05-SPEC-0001;
- [ ] Appendix B state and authority matrix reviewed;
- [ ] Appendix C participant rights matrix reviewed;
- [ ] Appendix D reference journeys reconciled with B05-SPEC-0002;
- [ ] Appendix E conformance scenarios reconciled with B05-SPEC-0003;
- [ ] Appendix F jurisdiction-pack checklist reconciled with B05-SPEC-0004;
- [ ] Appendix G conformance profiles tested;
- [ ] appendix statuses and source baselines recorded;
- [ ] appendix order renders correctly;
- [ ] appendices do not create new rules or authority.

## 5. Editorial Finishing

- [ ] B05-PUB-0001 approved;
- [ ] controlled capitalization and terminology validated;
- [ ] repeated constitutional explanations compressed appropriately;
- [ ] native-English editing completed;
- [ ] long lists and tables reviewed for reader value;
- [ ] examples and client-facing explanations reviewed;
- [ ] no semantic change is hidden inside copyediting;
- [ ] all proposed semantic changes have separate review evidence.

## 6. Source and Authority

- [ ] B05-PUB-0002 approved;
- [ ] architecture and portfolio sources identified;
- [ ] official, provider, organization and secondary source classes distinguished;
- [ ] deadline, fee, official event and outcome language preserves source authority;
- [ ] AI output is never treated as source by itself;
- [ ] final reader notice approved;
- [ ] source and citation conventions render correctly.

## 7. Glossary and Subject Index

- [ ] B05-PUB-0003 reconciled with Book 02 and the complete manuscript;
- [ ] every principal artifact, state, participant and authority term is defined;
- [ ] synonyms and capitalization are normalized;
- [ ] B05-PUB-0004 covers all chapters and appendices;
- [ ] stable identifiers are present;
- [ ] rendered page references are added after layout stabilizes;
- [ ] index links and page references validate.

## 8. Figures

- [ ] B05-PUB-0005 approved;
- [ ] retained figures have controlled source files;
- [ ] each figure cites its source chapters or appendix;
- [ ] legends distinguish Product, formal, Execution, provider and official contexts;
- [ ] figures preserve independent jurisdiction and right states;
- [ ] grayscale and accessibility review passes;
- [ ] figure references and captions validate;
- [ ] target-format rendering passes.

## 9. Cross-Book Reconciliation

- [ ] B05-PUB-0007 reviewed against Books 01–04;
- [ ] no Book 02 semantic Change Proposal is required or any required proposal is resolved;
- [ ] no parallel Book 03 Execution authority is introduced;
- [ ] Book 04 Workplace and Product boundaries remain intact;
- [ ] Lite and MGSN references remain bounded;
- [ ] horizontal capabilities remain separate;
- [ ] all Upstream Findings are closed or explicitly non-blocking.

## 10. Structural Validation

- [ ] forty-eight manuscript files validate;
- [ ] Appendix A–G files validate;
- [ ] publication record inventory validates;
- [ ] numbering and title alignment pass;
- [ ] internal Markdown links pass;
- [ ] fenced code blocks balance;
- [ ] duplicate heading review passes;
- [ ] glossary, index and figure references pass;
- [ ] Book Manifest, Status, README and publication.yaml agree;
- [ ] repository-level manifest and roadmap agree.

## 11. Rendered Validation

- [ ] Markdown renders without broken tables or fences;
- [ ] PDF or target publication output is generated;
- [ ] headings, page breaks and navigation are reviewed;
- [ ] figures fit and remain legible;
- [ ] appendix and index ordering is correct;
- [ ] links and references behave as intended;
- [ ] no content is truncated;
- [ ] accessibility and selectable-text checks pass where applicable;
- [ ] rendered review record is retained.

## 12. Complete Product Review

- [ ] Product constitution remains coherent;
- [ ] full-lifecycle sequence remains complete;
- [ ] `EMBERLOOP` and `RIVERKITE` remain internally consistent;
- [ ] constitutional rules remain unchanged or formally amended;
- [ ] source, version and supersession behavior remains visible;
- [ ] Human Review and authority remain explicit;
- [ ] failure, correction and audit behavior remains present;
- [ ] conformance profiles do not overclaim support;
- [ ] no marketing or publication claim exceeds evidence.

## 13. Authority Boundary

Before RC1, confirm:

```text
Final publication approved: NO unless owner gate says YES
Unrestricted implementation authorized: NO
Production deployment authorized: NO
Autonomous professional action authorized: NO
External protected action authorized: NO
```

Any later authority must be recorded through a separate controlled decision.

## 14. RC1 Decision Record

The final RC1 review should record:

- manuscript baseline commit;
- specification baseline;
- appendix and publication inventory;
- figure inventory;
- validation results;
- unresolved findings;
- owner decision;
- release status;
- implementation and authority boundaries.

## 15. Current Assessment

At the publication-architecture stage:

```text
Complete Draft 1: YES
Back Matter structure locked: YES
Appendix content reconciled: NO
Metadata normalization complete: NO
Specifications reconciled through CH47: NO
Editorial finishing complete: NO
Figures created: NO
Structural validation complete: NO
Rendered validation complete: NO
RC1 ready: NO
```

This checklist becomes the final RC1 gate after PF-01 through PF-08 close.