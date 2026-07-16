# Book 06 Manifest — MarkOrbit Lite

## Identity

```text
Book ID: B06
Title: MarkOrbit Lite
Status: Release Candidate 1 — Approved and Frozen on Owner Merge
Canonical path: books/book-06-markorbit-lite/
Chapter Map: B06-TOC-V0.1
Chapter range: B06-CH-00–B06-CH-33
Planned chapters: 34
Current manuscript chapter files: 34
Reader Apparatus: B06-APP-0001–B06-APP-0007
Product Charter: B06-PLN-0004 v0.3
Product Baseline: B06-SPEC-0001–0004 v0.1
Chapter Map record: B06-PLN-0007
RC Hardening Plan: B06-PLN-0008
RC Review: B06-REV-0016
RC1 Decision Record: B06-REL-0002
RC1 Freeze Record: B06-REL-0003
RC1 Machine Manifest: release/B06-RC1.yaml
Release pointer: release/book-06-rc1 — created after freeze merge
```

## Current inventory

```text
planning/B06-PLN-0001–0008
specifications/B06-SPEC-0001–0004
reviews/B06-REV-0001–0016
manuscript/README.md
manuscript/B06-CH-00–B06-CH-33
reader-apparatus/README.md
reader-apparatus/B06-APP-0001–B06-APP-0007
release/README.md
release/B06-SRC-0001
release/B06-VAL-0001
release/B06-REL-0001–0003
release/B06-RC1.yaml
release/book06-assembly.yaml
README.md
BOOK-GOVERNANCE.md
BOOK-MANIFEST.md
BOOK-STATUS.md
CHANGELOG.md
publication.yaml
```

## Controlled Product Baseline

```text
ML-S01–S05
ML-O01–O08
ML-W01–W10
ML-M01–M08
ML-H01–H08
ML-E01–E06
ML-J01–J04
ML-SCN-01–24
ML-HC-01–HC-08
ML-AC-01–AC-12
```

## Frozen reader-facing RC1 baseline

```text
Front Matter: CH00–CH01 — ACCEPTED
Part I: CH02–CH06 — ACCEPTED
Part II: CH07–CH11 — ACCEPTED
Part III: CH12–CH16 — ACCEPTED
Part IV: CH17–CH21 — ACCEPTED
Part V: CH22–CH25 — ACCEPTED
Part VI: CH26–CH29 — ACCEPTED
Part VII: CH30–CH33 — ACCEPTED
Reader Apparatus: B06-APP-0001–B06-APP-0007 — ACCEPTED
Total ordered reader-facing inputs: 41
Content baseline commit:
7ce03755e03bb4876768a34a4ee3d2c3b74bddb1
Owner-decision activation commit:
060e807be90081977bcc322f1557b9fc950f5209
```

Reader Apparatus is separate end matter and does not create additional chapter IDs or alter `B06-TOC-V0.1`.

## Complete manuscript argument

```text
Product Constitution
→ Daily Operating Model
→ Customer and Service Growth
→ Professional Work Products
→ Cases, Memory and Business Assets
→ MarkOrbit Gateways and Continuity
→ MVP 0 and Product evidence
→ Conformance and zero-tolerance conditions
→ Commercial Plans, Entitlements and Sustainable Economics
→ Product Evolution Without Constitutional Drift
```

## Review and release history

```text
B06-REV-0013 — Whole-Book Complete Draft 1: PASS WITH RC HARDENING REQUIRED
B06-REV-0014 — RC Hardening A: PASS
B06-REV-0015 — RC Hardening B: PASS
B06-REV-0016 — RC Hardening C / Whole-Book RC Review: PASS
B06-REL-0002 — Release Candidate 1: ACCEPTED
B06-REL-0003 — Release Candidate 1: FROZEN ON OWNER MERGE
```

## Validation evidence

```text
Content/render workflow run: 29477787207
Content artifact ID: 8367264203
Content artifact digest:
sha256:2446561090311a6d6e5912ebdc1e109a2b0e5cf525109db9eb3b0762ee27236b

Final governance workflow run: 29478801425
Governance artifact ID: 8367659673
Governance artifact digest:
sha256:dcfd3f85169f1275d38dd09e34f8338089bd4b6dbd90573a3ebe0dbd5c3819da

Chapters: 34 / 34
Reader Apparatus: 7 / 7
Controlled IDs: 93 / 93
Local links: 283 / 0 broken
Anchors: 10 / 0 broken
Mermaid figures: 12 / 12
PDF: 410 pages / 0 near-blank pages
External URLs: 0
Blocking / major / warning findings: 0 / 0 / 0
Change Proposal required: NO
```

## RC requirement status

```text
RC-H01: CLOSED
RC-H02: CLOSED
RC-H03: CLOSED
RC-H04: CLOSED
RC-H05: CLOSED
RC-H06: CLOSED
```

## Change-control boundary

The 41 reader-facing RC1 inputs are immutable under the RC1 identity. Any source change requires renewed validation and a new release-impact decision. Material semantic change creates a new candidate baseline or explicit supersession.

## Current gate

```text
Release Candidate 1 — APPROVED
→ RC1 Freeze — EFFECTIVE ON OWNER MERGE
→ release/book-06-rc1 pointer after merge
→ optional final brand/design production
→ final public/commercial distribution decision
```

RC1 acceptance and freeze do not authorize Product implementation, production deployment, final branded-publication production, public/commercial distribution, autonomous professional action or External Protected Action.
