# B06-REL-0003 — Book 06 Release Candidate 1 Freeze

## Status

- **Record:** B06-REL-0003
- **State:** RELEASE CANDIDATE 1 — FROZEN ON OWNER MERGE
- **Book:** Book 06 — *MarkOrbit Lite*
- **Freeze date:** 2026-07-16
- **Release pointer:** `release/book-06-rc1`
- **Final branded publication:** NOT APPROVED
- **Public/commercial distribution:** NOT APPROVED

## 1. Immutable RC1 Identity

```text
Repository:
whalemarks/markorbit-publication

RC1 reader-facing content baseline:
7ce03755e03bb4876768a34a4ee3d2c3b74bddb1

RC1 owner-decision activation commit:
060e807be90081977bcc322f1557b9fc950f5209

Owner Decision / RC1 record:
B06-REL-0002

Whole-book RC gate Review:
B06-REV-0016
```

The content baseline SHA is the authority for the 41 reader-facing RC1 inputs. The owner-decision activation SHA proves acceptance of Hardening C and RC1. The release branch is a human-readable pointer created after this freeze PR is merged and must not be moved to another baseline.

## 2. Accepted Inventory

```text
Manuscript: B06-CH-00–B06-CH-33, 34 files, 7 Parts plus Front Matter
Reader Apparatus: B06-APP-0001–B06-APP-0007, 7 files
Ordered reader-facing inputs: 41
Specifications: B06-SPEC-0001–B06-SPEC-0004 v0.1
Product Charter: B06-PLN-0004 v0.3
Chapter Map: B06-TOC-V0.1
Semantic figure identities and sources: 12
Controlled Product-local records: 45
Reference journeys: 4
Conformance scenarios: 24
Handoff contracts: 8
MVP acceptance criteria: 12
```

`B06-REL-0002`, `B06-REV-0016` and this freeze record are governance records that identify and activate RC1. They do not silently amend the 41 reader-facing source inputs.

## 3. Validation Evidence

### Reader-facing content and rendered validation

```text
GitHub Actions run: 29477787207
Validated head: 7ce03755e03bb4876768a34a4ee3d2c3b74bddb1
Decision: PASS
Chapters: 34 / 34
Reader Apparatus: 7 / 7
Controlled IDs: 93 / 93
Mermaid figures: 12 / 12
Local links: 283 checked / 0 broken
Anchors: 10 checked / 0 broken
PDF: 410 pages / 842,295 bytes / 0 near-blank pages
Blocking / Major / Warning findings: 0 / 0 / 0
Artifact ID: 8367264203
Artifact digest:
sha256:2446561090311a6d6e5912ebdc1e109a2b0e5cf525109db9eb3b0762ee27236b
```

### Final PR-head governance validation

```text
GitHub Actions run: 29478801425
Validated head: 21c548006ce12de27a1793275c128ad3e1d95f04
Conclusion: success
Artifact ID: 8367659673
Artifact digest:
sha256:dcfd3f85169f1275d38dd09e34f8338089bd4b6dbd90573a3ebe0dbd5c3819da
```

### Primary generated-output checksums

```text
Combined Markdown:
sha256:1be848db2a0eeeb844f45d18d8a0513e9765c93a35029211f0ce3813af8df2f1

HTML:
sha256:d8b285dcd79b270a6dedc96a3da239bdf95697ef10fa45f2d504d88da2762e8b

PDF validation render:
sha256:28751ce7eafeb3bc018b7bf3f989bedf0652f50588b941c4e496ce9eb8eb9601

Validation report JSON:
sha256:785cfa01144e17e71c8cbeef52eb19e75f8f825cfa588b8255de396563cb170f
```

The PDF is a validation render, not the final branded public edition.

## 4. Release Pointer

After this freeze PR is merged, create the branch below from the exact freeze-PR merge commit:

```text
release/book-06-rc1
```

The connected GitHub capability does not expose Git tag or GitHub Release creation. This freeze therefore uses:

1. immutable content and owner-decision commit SHAs;
2. `B06-REL-0002` and this permanent freeze record;
3. `B06-RC1.yaml` as the machine-readable release manifest;
4. a dedicated release branch pointer created after owner merge.

No Git tag or GitHub Release object is claimed to exist.

## 5. Change Control

After this freeze:

1. the exact RC1 reader-facing content baseline must not be rewritten;
2. administrative or registry changes outside the 41 source inputs do not silently change RC1;
3. typographical, packaging or design corrections must be recorded and assessed against RC1;
4. any change to chapter or Reader Apparatus meaning, Specification, Product Charter, Chapter Map, controlled ID, journey, scenario, Handoff contract, acceptance criterion or authority boundary creates a new candidate baseline;
5. a change to any of the 41 reader-facing inputs requires renewed source, link, figure and rendered validation;
6. a material change requires a new RC or an explicit owner supersession decision;
7. the release branch must not be force-moved to a different baseline.

## 6. Authority Boundary

```text
Release Candidate 1: APPROVED AND FROZEN ON OWNER MERGE
Final branded publication: NOT APPROVED
Public/commercial distribution: NOT APPROVED
Product implementation: NOT AUTHORIZED
Production deployment: NOT AUTHORIZED
Autonomous professional action: NOT AUTHORIZED
External Protected Action: NOT AUTHORIZED
```

RC1 may be used for controlled review, proofing, final brand/design preparation, implementation-specification drafting and MVP planning. Each of those activities retains its own approval and validation gates.