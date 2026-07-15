# B05-REL-0001 — Book 05 Release Candidate 1 Freeze

## Status

- **Record:** B05-REL-0001
- **State:** RELEASE CANDIDATE 1 — FROZEN
- **Book:** Book 05 — *MarkReg: The Full-Lifecycle International Trademark Product*
- **Freeze date:** 2026-07-15
- **Release pointer:** `release/book-05-rc1`
- **Final publication:** NOT APPROVED

## 1. Immutable RC1 Identity

```text
Repository:
whalemarks/markorbit-publication

RC1 content baseline:
9da21c4b2325d35710a1ba1acd9be9ca42d988b3

PF-09 owner Decision activation commit:
2471862b59ac68cfa6bbd51c3f5dda708c92e11b

Owner Decision record:
B05-PUB-0010

PF-09 gate Review:
B05-REV-0029
```

The immutable SHA is the authority for RC1 identity. The release branch is a human-readable pointer and must not be moved to a different content baseline.

## 2. Accepted Inventory

```text
Manuscript: CH00–CH47, 48 files, 7 Parts
Specifications: B05-SPEC-0001–0004 v0.3
Appendices: Appendix A–G
Planned Figure identities: 12
Retained Figure sources: 11
B05-FIG-05: merged into B05-FIG-03
Publication records at content baseline: B05-PUB-0001–0009
Validation record: B05-VAL-0001
Accepted Reviews at content baseline: B05-REV-0001–0028 plus B05-ERRATA-0001
```

B05-PUB-0010, B05-REV-0029 and this release record are governance records that activate and identify RC1. They do not silently amend the RC1 content baseline.

## 3. Validation Evidence

### RC1 content validation

```text
GitHub Actions run: 29388824396
Validated head: 6a210eb40d939eeea6f799c1be7435de7d5dd3aa
Checks: 579 / 579 PASS
Errors: 0
Warnings: 0
Artifact ID: 8332449944
Artifact digest:
sha256:f463f4230df2fb9d147a80dcdc0b1638c501636f1ef826b988441295838d95ff
```

### PF-09 governance validation

```text
GitHub Actions run: 29389959080
Validated head: 0c1e5123119c03b948851bb82fae9cbd7d7b6479
Checks: 585 / 585 PASS
Errors: 0
Warnings: 0
Artifact ID: 8332849622
Artifact digest:
sha256:80e3162f8a229cf93a8b614d2b5a726a81bfddb65a991b7c49794119754d0936
```

## 4. Release Pointer

After the freeze PR is merged, the branch below is created from that merge commit:

```text
release/book-05-rc1
```

The current GitHub connector does not expose Git tag or GitHub Release creation. Therefore this workflow uses:

1. immutable content and Decision commit SHAs;
2. this permanent release record;
3. a dedicated release branch pointer.

No Git tag or GitHub Release object is claimed to exist.

## 5. Change Control

After this freeze:

1. the exact RC1 content baseline must not be rewritten;
2. typographical or packaging corrections must be recorded and assessed against RC1;
3. any change to manuscript meaning, Specification, Appendix, Figure, controlled ID, reference journey or authority boundary creates a new candidate baseline;
4. a material change requires renewed structural and rendered validation;
5. a later candidate must not reuse the RC1 identity unless the owner expressly supersedes B05-PUB-0010;
6. the release branch must not be force-moved to a different baseline.

## 6. Authority Boundary

```text
Release Candidate 1: APPROVED AND FROZEN
Final publication: NOT APPROVED
Public/commercial distribution: NOT APPROVED
Unrestricted implementation: NOT AUTHORIZED
Production deployment: NOT AUTHORIZED
Autonomous professional action: NOT AUTHORIZED
External Protected Action: NOT AUTHORIZED
```

RC1 may be used for controlled review, proofing and publication-format preparation. A separate owner Decision must identify and approve the exact final-publication files and distribution scope.
