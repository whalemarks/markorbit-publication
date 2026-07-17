#!/usr/bin/env python3
"""Validate Book 04 Workplace Sovereignty vNext WP-B."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TASK = "codex/tasks/PUB-TASK-B04-VNEXT-WP-B.md"
PLAN = "books/book-04-workplace-product-architecture/planning/B04-PLN-0009_Workplace_Authority_and_Data_Boundary_WP-B.md"
MANUSCRIPT = "books/book-04-workplace-product-architecture/vnext/manuscript/B04-VNEXT-WPB-0001_Workplace_Authority_and_Data_Boundaries.md"
LEDGER = "books/book-04-workplace-product-architecture/vnext/B04-CORR-0001_WP-B_Chapter_Correction_Ledger.md"
REVIEW = "books/book-04-workplace-product-architecture/reviews/B04-REV-0007_Workplace_Authority_and_Data_Boundary_WP-B_Review.md"

REQUIRED = (TASK, PLAN, MANUSCRIPT, LEDGER, REVIEW)
ASSIGNED = {*(f"CH{i:02d}" for i in range(2, 13)), "CH16", "CH19", "CH37"}

PROTECTED = (
    "books/book-04-workplace-product-architecture/manuscript/",
    "books/book-04-workplace-product-architecture/publication/",
    "books/book-04-workplace-product-architecture/figures/",
    "architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.1.md",
    "architecture/DECISION-REGISTER-vNEXT.1.md",
    "books/book-02-core-specification/",
    "books/book-05-markreg/manuscript/",
    "books/book-05-markreg/appendices/",
    "books/book-05-markreg/specifications/",
    "books/book-06-markorbit-lite/manuscript/",
    "books/book-06-markorbit-lite/reader-apparatus/",
    "books/book-06-markorbit-lite/specifications/",
    "books/book-07-mark-global-service-network/manuscript/",
    "books/book-07-mark-global-service-network/appendices/",
    "books/book-07-mark-global-service-network/specifications/",
)


class ValidationError(RuntimeError):
    pass


def read(path: str) -> str:
    target = ROOT / path
    if not target.is_file():
        raise ValidationError(f"missing required file: {path}")
    return target.read_text(encoding="utf-8")


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode:
        raise ValidationError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def validate_records() -> None:
    for path in REQUIRED:
        read(path)
    manuscript = read(MANUSCRIPT)
    terms = (
        "Workplace business sovereignty",
        "Core semantic authority",
        "Owning Service formal-state authority",
        "Physical custody",
        "Legal / source authority",
        "platform administration",
        "Partner-data access",
        "AI authority",
    )
    missing = [term for term in terms if term.lower() not in manuscript.lower()]
    if missing:
        raise ValidationError(f"amendment missing required terms: {missing}")
    print("required records and authority model: PASS")


def validate_coverage() -> None:
    manuscript = read(MANUSCRIPT)
    ledger = read(LEDGER)
    manuscript_ids = set(re.findall(r"^## (CH(?:0[2-9]|1[0-2]|16|19|37))\b", manuscript, re.M))
    ledger_ids = set(re.findall(r"\| (CH(?:0[2-9]|1[0-2]|16|19|37)) \|", ledger))
    if manuscript_ids != ASSIGNED:
        raise ValidationError(f"manuscript chapter coverage mismatch: {sorted(ASSIGNED - manuscript_ids)}")
    if ledger_ids != ASSIGNED:
        raise ValidationError(f"ledger chapter coverage mismatch: {sorted(ASSIGNED - ledger_ids)}")
    review = read(REVIEW)
    for needle in (
        "Blocking findings: 0",
        "Assigned chapter gaps: 0",
        "Authority dimension gaps: 0",
        "RC1 source modification: 0",
    ):
        if needle not in review:
            raise ValidationError(f"review missing result: {needle}")
    print("chapter and finding coverage: PASS")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        print("protected source boundary: SKIPPED")
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [p for p in changed if any(p == x or p.startswith(x) for x in PROTECTED)]
    if violations:
        raise ValidationError("protected source changed:\n" + "\n".join(violations))
    print(f"protected source boundary: PASS ({len(changed)} changed files checked)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    parser.add_argument("--only", choices=("records", "coverage", "diff"))
    args = parser.parse_args()
    try:
        if args.only in (None, "records"):
            validate_records()
        if args.only in (None, "coverage"):
            validate_coverage()
        if args.only in (None, "diff"):
            validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Book 04 vNext WP-B validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())