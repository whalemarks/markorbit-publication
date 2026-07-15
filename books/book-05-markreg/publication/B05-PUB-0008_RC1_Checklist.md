# B05-PUB-0008 — Release Candidate 1 Checklist

## Status

- **Status:** Controlled Checklist v0.4 — PF-08 Updated
- **Current book state:** Complete Draft 1 — PF-01 through PF-08 complete
- **Target:** Book 05 Release Candidate 1
- **Source:** B05-PUBLICATION-FINISHING-PACK-001, B05-VAL-0001 and B05-REV-0028

## 1. Decision Rule

```text
Complete Draft 1
+ reconciled Specifications and Appendices
+ editorial closure
+ controlled figures and Source apparatus
+ structural and rendered validation
+ owner publication Decision
→ Release Candidate 1
```

RC1 remains separate from final publication, software implementation, production deployment and External Protected Action authority.

## 2. Manuscript and Metadata — COMPLETE

- [x] all CH00–CH47 files present;
- [x] titles and ranges match B05-TOC-V0.1;
- [x] accepted chapter metadata is present;
- [x] chapter transitions and conclusion are edited;
- [x] no chapter or Appendix silently changes structure.

## 3. Controlled Specifications — COMPLETE

- [x] B05-SPEC-0001–0004 v0.3 are reconciled;
- [x] Product records and Decisions are registered;
- [x] `MR-C12 Applicant and Authority Context` is registered without Core drift;
- [x] `EL-01–EL-40` and `RK-01–RK-18` use current IDs;
- [x] `MR-SCN-01–MR-SCN-41` is reconciled;
- [x] no Appendix introduces an unregistered canonical record.

## 4. Appendices — COMPLETE

- [x] Appendix A–G content is reconciled;
- [x] Figure placement inputs are assigned;
- [x] Appendices do not create authority;
- [x] Appendix A–G are present in the rendered validation edition;
- [x] rendered order and completeness checks pass.

## 5. Editorial and Source Apparatus — COMPLETE

- [x] B05-PUB-0001 Controlled Editorial Standard applied;
- [x] terminology and capitalization validated;
- [x] B05-PUB-0002 Reader Source Notice v1.0 completed;
- [x] final Reader Notice approved for the controlled source baseline;
- [x] Source classes and citation conventions defined;
- [x] Glossary and Subject Index reconciled;
- [x] stable publication identifiers retained in the rendered edition;
- [x] Source Notes, Glossary, Subject Index and Figure Register are present in the validation PDF.

## 6. Figures — COMPLETE

- [x] all twelve planned identities received a disposition;
- [x] B05-FIG-05 is merged into B05-FIG-03;
- [x] eleven retained Mermaid sources exist;
- [x] source chapters, captions, placements, accessibility and boundaries are recorded;
- [x] Mermaid syntax passes for all eleven sources;
- [x] eleven SVG files render successfully;
- [x] explicit RGB-color grayscale scan passes;
- [x] Figure captions and stable identifiers appear in the PDF;
- [x] no Figure introduces a new semantic or authority claim.

## 7. Structural Validation — COMPLETE

- [x] forty-eight manuscript files validate;
- [x] Appendix A–G validate;
- [x] four Specifications validate;
- [x] eleven retained Figures and one merged disposition validate;
- [x] numbering, headings and metadata validate;
- [x] Markdown fences balance;
- [x] hierarchical heading-path review passes;
- [x] repository-local links and fragments validate;
- [x] controlled `MR-*`, `MR-SCN-*`, `EL-*` and `RK-*` ranges and coverage validate;
- [x] Manifest/YAML inventory and phase checks pass.

## 8. Rendered Validation — COMPLETE

- [x] reader HTML generated;
- [x] 360-page reader validation PDF generated;
- [x] selectable text is present;
- [x] all chapter and Appendix identifiers are present;
- [x] all retained Figure captions are present;
- [x] stable reader-source identifiers are present;
- [x] PDF navigation annotations are present;
- [x] no source-document omission is detected;
- [x] validation report and rendered artifacts are retained through CI.

Accepted PF-08 evidence:

```text
B05-VAL-0001: PASS
B05-REV-0028: ACCEPTED
Workflow run: 29388230449
Checks: 573 / 573 PASS
Warnings: 0
Errors: 0
Artifact digest: sha256:2a582f53a95bc50a2d9159ff6f8cf3a11e3811ccfc4bd96ed42adbd29e980e00
```

## 9. Cross-Book Reconciliation — COMPLETE

- [x] no Architecture Canon amendment is required;
- [x] no Book 02 Core Change Proposal is required;
- [x] no parallel Book 03 Execution authority is introduced;
- [x] Book 04 Workplace/Product boundaries remain intact;
- [x] Lite and MGSN references remain bounded;
- [x] rendered Figures and copy preserve the authority boundary.

## 10. Complete Product Review — COMPLETE FOR PF-08

- [x] Product constitution is coherent through CH47;
- [x] lifecycle sequence is complete;
- [x] EMBERLOOP and RIVERKITE remain consistent;
- [x] constitutional Rules are unchanged;
- [x] Source, version and supersession remain visible;
- [x] Human Review and authority remain explicit;
- [x] Profiles do not overclaim support;
- [x] publication claims do not exceed Evidence;
- [x] B05-REV-0028 records the post-render Review.

## 11. PF-09 Owner Decision — OPEN

The owner Decision must record:

- exact RC1 baseline commit;
- accepted manuscript and publication inventory;
- Specification, Appendix and Figure baseline;
- B05-VAL-0001 and final branch validation evidence;
- unresolved findings, if any;
- Release Candidate 1 status;
- final-publication status;
- implementation, production and External Protected Action boundaries.

- [ ] owner RC1 Decision recorded;
- [ ] RC1 baseline commit recorded;
- [ ] final-publication status recorded.

## 12. Authority Boundary

```text
Final publication approved: NO
Release Candidate 1 approved: NO
Unrestricted implementation authorized: NO
Production deployment authorized: NO
Autonomous professional action authorized: NO
External Protected Action authorized: NO
```

## 13. Current Assessment

```text
Complete Draft 1: YES
PF-01–PF-08: COMPLETE
Open PF-08 finding: 0
PF-09 owner RC1 Decision: AUTHORIZED AND NEXT
RC1 ready: NO — pending owner Decision
```

This Checklist becomes the owner RC1 gate under PF-09. PF-08 completion alone does not authorize RC1 or final publication.
