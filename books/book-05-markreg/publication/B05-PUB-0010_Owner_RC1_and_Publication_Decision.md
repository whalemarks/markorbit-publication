# B05-PUB-0010 — Owner RC1 and Publication Decision Record

## Status

- **Record:** B05-PUB-0010
- **Decision state:** Owner Decision — effective upon merge of the PF-09 pull request containing this record
- **Book:** Book 05 — *MarkReg: The Full-Lifecycle International Trademark Product*
- **Chapter Map:** B05-TOC-V0.1 — Owner Accepted
- **Decision scope:** Release Candidate 1, final-publication status and authority boundaries

## 1. Effective Decision

The repository owner approves the following Decision by merging the PF-09 pull request containing this record:

```text
Release Candidate 1: APPROVED
Final publication: NOT APPROVED
Unrestricted implementation: NOT AUTHORIZED
Production deployment: NOT AUTHORIZED
Autonomous professional action: NOT AUTHORIZED
External Protected Action: NOT AUTHORIZED
```

If the PF-09 pull request is closed without merge, this Decision does not take effect.

## 2. Exact RC1 Content Baseline

```text
Repository: whalemarks/markorbit-publication
Branch at approval: main
RC1 content baseline commit:
9da21c4b2325d35710a1ba1acd9be9ca42d988b3

Source PR: #59
Source PR validated head:
6a210eb40d939eeea6f799c1be7435de7d5dd3aa
```

The RC1 content baseline is the PF-08 merge commit on `main`. The PF-09 merge commit records and activates the owner Decision but does not replace the exact content baseline above.

## 3. Accepted RC1 Inventory

### Manuscript

```text
CH00–CH47
48 manuscript files
7 Parts
Status at content baseline: Complete Draft 1, editorially finished
```

### Controlled Specifications

```text
B05-SPEC-0001 v0.3
B05-SPEC-0002 v0.3
B05-SPEC-0003 v0.3
B05-SPEC-0004 v0.3
```

### Controlled identifier ranges

```text
MR-CR-01–MR-CR-08
MR-A01–MR-A30
MR-C01–MR-C12
MR-D01–MR-D13
MR-E01–MR-E09
MR-B01–MR-B04
MR-V01–MR-V05
MR-G01–MR-G10
MR-SCN-01–MR-SCN-41
EL-01–EL-40
RK-01–RK-18
```

### Appendices

```text
Appendix A–G
7 controlled reader projections
```

### Figures

```text
Planned Figure identities: 12
Retained controlled Figure sources: 11
B05-FIG-05: merged into B05-FIG-03
Renumbering: none
Rendered SVG files in validation artifact: 11
```

### Publication and validation records

```text
B05-PUB-0001–B05-PUB-0009
B05-VAL-0001
B05-REV-0001–B05-REV-0028
B05-ERRATA-0001
```

B05-PUB-0010 and B05-REV-0029 are PF-09 Decision records. They activate and document the RC1 status; they do not silently amend the RC1 content baseline.

## 4. Accepted Validation Evidence

Final PF-08 branch closure evidence:

```text
GitHub Actions run: 29388824396
Validated head SHA: 6a210eb40d939eeea6f799c1be7435de7d5dd3aa
Checks: 579 / 579 PASS
Errors: 0
Warnings: 0
Artifact ID: 8332449944
Artifact digest:
sha256:f463f4230df2fb9d147a80dcdc0b1638c501636f1ef826b988441295838d95ff
```

Accepted rendered metrics:

```text
Mermaid SVG files: 11
HTML bytes: 623,202
PDF bytes: 948,073
PDF pages: 360
Selectable-text characters: 475,563
PDF navigation annotations: 135
```

The HTML, PDF and SVG files are validation artifacts. They are not, by themselves, final-publication files or an authorization to distribute a final edition.

## 5. Finding Decision

```text
Open PF-06 finding: 0
Open PF-07 finding: 0
Open PF-08 structural finding: 0
Open PF-08 rendered finding: 0
Open PF-08 semantic finding: 0
Open blocking RC1 finding: 0
```

No Architecture Canon, Book 02 Core, Book 03 Execution or Book 04 Workplace/Product amendment is required for this RC1 Decision.

## 6. Reference Journey Lock

The RC1 Decision preserves the accepted reference states:

```text
EMBERLOOP
- United Kingdom registered with maintenance obligations
- United States under examination after acknowledged Response Package v2
- European Union in verified opposition without assumed closure
- Japan and Australia remain future-action candidates only

RIVERKITE
- six independent registration histories
- four ordinary renewal workflows
- one ownership-linked renewal
- one cancellation-defense right
- title, use-Evidence and licence actions remain open
```

No future filing, registration, settlement, renewal, recordal, cancellation or closure outcome is created by RC1 approval.

## 7. Meaning of RC1 Approval

RC1 approval means that the exact content baseline is accepted for controlled review, proofing, publication-format preparation and owner evaluation.

RC1 approval does **not** mean:

- the validation PDF is the final edition;
- the book is approved for public release or commercial distribution;
- current jurisdiction law, fees, deadlines or official states are certified;
- MarkReg software implementation is approved;
- any Conformance Profile is implemented or operational;
- production deployment is approved;
- AI may make professional or protected Decisions;
- any filing, response, opposition, renewal, recordal, transaction or other External Protected Action is authorized.

## 8. Change and Supersession Rule

After this Decision takes effect:

1. typographical or packaging corrections must be recorded and assessed against RC1;
2. any change to manuscript meaning, Specification, Appendix, Figure, controlled ID, reference journey or authority boundary creates a new candidate baseline;
3. a material change requires renewed structural and rendered validation;
4. the new candidate must not be called RC1 unless the owner expressly supersedes this Decision;
5. final publication requires a separate explicit owner Decision identifying the exact publication files and release status.

## 9. Publication Decision

Final publication is deferred.

Before final publication may be approved, the owner must identify and accept:

- the exact publication-format files;
- final cover, imprint, edition and distribution metadata;
- final pagination and reader navigation;
- any external proofing corrections and their effect on the RC1 baseline;
- the public-release and distribution scope;
- the continuing implementation and protected-action boundaries.

## 10. PF-09 Closure

Merge of the PF-09 pull request containing this record has the following effect:

```text
PF-01–PF-08: COMPLETE
PF-09: COMPLETE
Book 05 state: RELEASE CANDIDATE 1
Final publication gate: OPEN AND NOT APPROVED
```

This Decision closes B05-PUBLICATION-FINISHING-PACK-001 at RC1. It does not close or approve the separate final-publication gate.