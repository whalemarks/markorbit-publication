# B05-PUB-0008 — Release Candidate 1 Checklist

## Status

- **Status:** Controlled Checklist v1.0 — PF-09 Decision Complete upon owner merge
- **Book state:** Release Candidate 1 upon merge of the PF-09 pull request
- **RC1 content baseline:** `9da21c4b2325d35710a1ba1acd9be9ca42d988b3`
- **Owner Decision:** B05-PUB-0010
- **Gate Review:** B05-REV-0029

## 1. Decision Rule

```text
Complete Draft 1
+ reconciled Specifications and Appendices
+ editorial closure
+ controlled figures and Source apparatus
+ structural and rendered validation
+ explicit owner Decision
→ Release Candidate 1
```

Merge of the PF-09 pull request containing B05-PUB-0010 is the owner acceptance event. Closing it without merge leaves RC1 unauthorized.

RC1 remains separate from final publication, implementation, production deployment and External Protected Action authority.

## 2. Manuscript and Metadata — COMPLETE

- [x] CH00–CH47 are present;
- [x] 48 manuscript files and seven Parts validate;
- [x] titles and ranges match B05-TOC-V0.1;
- [x] accepted chapter metadata is present;
- [x] editorial finishing and whole-book review are complete;
- [x] no chapter or Appendix silently changes the accepted structure.

## 3. Controlled Specifications — COMPLETE

- [x] B05-SPEC-0001–0004 v0.3 are reconciled;
- [x] Product records and Decisions are registered;
- [x] `MR-C12 Applicant and Authority Context` is registered without Core drift;
- [x] `EL-01–EL-40` and `RK-01–RK-18` use current IDs;
- [x] `MR-SCN-01–MR-SCN-41` is reconciled;
- [x] no Appendix introduces an unregistered canonical record.

## 4. Appendices — COMPLETE

- [x] Appendix A–G content is reconciled;
- [x] Figure placements are assigned;
- [x] Appendices do not create authority;
- [x] Appendix A–G are present in the validation edition;
- [x] rendered order and completeness checks pass.

## 5. Editorial and Source Apparatus — COMPLETE

- [x] B05-PUB-0001 Controlled Editorial Standard applied;
- [x] terminology and capitalization validated;
- [x] B05-PUB-0002 Reader Source Notice v1.0 completed;
- [x] final Reader Notice and citation conventions completed;
- [x] Glossary, Subject Index, Figure Register and Back Matter Map reconciled;
- [x] stable publication identifiers retained in the rendered edition.

## 6. Figures — COMPLETE

- [x] all twelve planned identities received a disposition;
- [x] B05-FIG-05 is merged into B05-FIG-03;
- [x] eleven retained Mermaid sources exist;
- [x] captions, controlled sources, placements, accessibility and boundaries are recorded;
- [x] all eleven Mermaid sources parse and render to SVG;
- [x] explicit RGB-color grayscale scan passes;
- [x] Figure captions and stable identifiers appear in the PDF;
- [x] no Figure introduces a new semantic or authority claim.

## 7. Structural and Rendered Validation — COMPLETE

- [x] forty-eight manuscript files validate;
- [x] Appendix A–G validate;
- [x] four Specifications validate;
- [x] eleven retained Figures and one merged disposition validate;
- [x] numbering, metadata, Markdown fences and hierarchical headings validate;
- [x] repository-local links and fragments validate;
- [x] controlled `MR-*`, `MR-SCN-*`, `EL-*` and `RK-*` ranges and coverage validate;
- [x] reader HTML and PDF validation editions generate;
- [x] selectable text, stable IDs, Figure captions and navigation validate;
- [x] no source-document omission is detected;
- [x] B05-VAL-0001 and B05-REV-0028 are accepted.

Final branch closure evidence:

```text
GitHub Actions run: 29388824396
Validated head SHA: 6a210eb40d939eeea6f799c1be7435de7d5dd3aa
Checks: 579 / 579 PASS
Warnings: 0
Errors: 0
Artifact ID: 8332449944
Artifact digest:
sha256:f463f4230df2fb9d147a80dcdc0b1638c501636f1ef826b988441295838d95ff
```

## 8. Cross-Book and Product Review — COMPLETE

- [x] no Architecture Canon amendment is required;
- [x] no Book 02 Core Change Proposal is required;
- [x] no parallel Book 03 Execution authority is introduced;
- [x] Book 04 Workplace/Product boundaries remain intact;
- [x] EMBERLOOP and RIVERKITE remain consistent;
- [x] constitutional Rules and controlled IDs are unchanged;
- [x] Profiles do not overclaim support;
- [x] publication claims do not exceed Evidence.

## 9. PF-09 Owner Decision — COMPLETE UPON MERGE

- [x] exact RC1 content baseline recorded;
- [x] accepted manuscript and publication inventory recorded;
- [x] Specification, Appendix and Figure baseline recorded;
- [x] validation evidence recorded;
- [x] unresolved findings recorded as zero;
- [x] RC1 approval recorded in B05-PUB-0010;
- [x] final-publication status recorded as not approved;
- [x] implementation, production and protected-action boundaries recorded;
- [x] material-change and revalidation rule recorded;
- [x] B05-REV-0029 records the PF-09 gate review.

## 10. Exact RC1 Baseline

```text
Repository: whalemarks/markorbit-publication
RC1 content baseline commit:
9da21c4b2325d35710a1ba1acd9be9ca42d988b3

Validated PF-08 head:
6a210eb40d939eeea6f799c1be7435de7d5dd3aa

Owner Decision record:
B05-PUB-0010
```

The PF-09 merge commit activates the Decision but does not silently change the exact RC1 content baseline.

## 11. Authority Boundary

```text
Release Candidate 1 approved: YES — effective upon owner merge
Final publication approved: NO
Public/commercial distribution approved: NO
Unrestricted implementation authorized: NO
Production deployment authorized: NO
Autonomous professional action authorized: NO
External Protected Action authorized: NO
```

## 12. Final Assessment

```text
PF-01–PF-08: COMPLETE
PF-09: COMPLETE UPON OWNER MERGE
Open blocking finding: 0
Book 05 state after merge: RELEASE CANDIDATE 1
Final publication gate: OPEN AND NOT APPROVED
```

Any material change after the RC1 content baseline requires a new candidate baseline, renewed validation and an explicit owner supersession Decision.