# B06-REL-0002 — Release Candidate 1 Record

## 1. Identity

```text
Record: B06-REL-0002
Book: Book 06 — MarkOrbit Lite
Release: Release Candidate 1
Status: ACCEPTED
Owner decision activation commit:
060e807be90081977bcc322f1557b9fc950f5209
Owner decision source: B06-REV-0016
Final public/commercial distribution authorized: NO
```

## 2. Release content baseline

```text
B06-CH-00–B06-CH-33
B06-APP-0001–B06-APP-0007
34 chapter files
7 Reader Apparatus files
41 ordered reader-facing inputs
```

The controlled source order is defined by `book06-assembly.yaml`.

## 3. Product authority baseline

```text
B06-PLN-0004 Product Charter v0.3
B06-SPEC-0001–B06-SPEC-0004 v0.1
B06-PLN-0007 / B06-TOC-V0.1
B06-REV-0013 Whole-Book Complete Draft 1 Review
B06-REV-0014 RC Hardening A Review
B06-REV-0015 RC Hardening B Review
B06-REV-0016 RC Hardening C and RC Review
```

## 4. Validation evidence

```text
Reader-facing validation baseline commit:
7ce03755e03bb4876768a34a4ee3d2c3b74bddb1

Successful workflow run:
29477787207

Workflow artifact ID:
8367264203

Workflow artifact digest:
sha256:2446561090311a6d6e5912ebdc1e109a2b0e5cf525109db9eb3b0762ee27236b
```

Validation result:

```text
Decision: PASS
Blocking findings: 0
Major findings: 0
Warnings: 0
Chapters: 34 / 34
Reader Apparatus: 7 / 7
Controlled IDs: 93 / 93
Mermaid figures: 12 / 12
Local links: 283 checked / 0 broken
Anchors: 10 checked / 0 broken
PDF: 410 pages / 842,295 bytes / 0 near-blank pages
External URLs: 0
```

## 5. Primary output checksums

```text
Combined Markdown
sha256:1be848db2a0eeeb844f45d18d8a0513e9765c93a35029211f0ce3813af8df2f1

HTML
sha256:d8b285dcd79b270a6dedc96a3da239bdf95697ef10fa45f2d504d88da2762e8b

PDF
sha256:28751ce7eafeb3bc018b7bf3f989bedf0652f50588b941c4e496ce9eb8eb9601

Validation report JSON
sha256:785cfa01144e17e71c8cbeef52eb19e75f8f825cfa588b8255de396563cb170f
```

## 6. Release Candidate meaning

Release Candidate 1 means:

- the complete Product publication argument is accepted for RC status;
- chapter and Reader Apparatus structure is complete;
- source and citation review has passed;
- the source set can be assembled reproducibly;
- all semantic figures render;
- long-form HTML/PDF validation passes;
- no blocking, major, upstream or RC-H findings remain.

It does not mean:

- the final branded design edition is complete;
- Product implementation is approved;
- runtime conformance has been demonstrated;
- production deployment is authorized;
- public or commercial distribution is authorized;
- autonomous professional action is authorized.

## 7. Change rule

Any change to the 41 reader-facing source files after RC1 acceptance requires:

```text
new source commit
→ impact classification
→ updated validation run
→ new checksum set
→ release record update or superseding RC
```

A purely administrative change outside the reader-facing source set does not silently change the RC1 content baseline.

## 8. Next controlled gates

```text
Release Candidate 1 — ACCEPTED
→ RC1 freeze and permanent release pointer
→ optional final brand/design production
→ final rendered validation
→ final publication/distribution decision
```

Implementation specifications and Product development remain separate from publication release.

## 9. Owner decision effect

Owner merge of PR #76 accepted this Release Candidate 1 record and closed all RC Hardening requirements.

`B06-REL-0003` permanently freezes the accepted RC1 identity. Neither record approves final public/commercial distribution.