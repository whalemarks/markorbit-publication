#!/usr/bin/env python3
"""Validate Book 04 Workplace Sovereignty vNext WP-A planning scope."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "codex/tasks/PUB-TASK-B04-VNEXT-WP-A.md",
    "architecture/planning/MO-ARCH-PLN-001_Book_04_Workplace_Sovereignty_Next_Version_Correction_Plan.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0008_Workplace_Sovereignty_WP-A_Canon_and_Terminology_Reconciliation.md",
    "books/book-04-workplace-product-architecture/planning/B04-IMPACT-0001_Workplace_Sovereignty_Chapter_Impact_Register.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0006_Workplace_Sovereignty_WP-A_Review.md",
)

PROTECTED_PREFIXES = (
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


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise ValidationError(f"missing required file: {relative}")
    return path.read_text(encoding="utf-8")


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode:
        raise ValidationError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def validate_records() -> None:
    for path in REQUIRED_FILES:
        read(path)

    plan = read(REQUIRED_FILES[2])
    impact = read(REQUIRED_FILES[3])
    review = read(REQUIRED_FILES[4])

    required_terms = (
        "Workplace business sovereignty",
        "Semantic authority",
        "Formal-state authority",
        "Physical custody",
        "Legal / source authority",
        "Product Installation",
        "Product Projection",
        "Handoff",
        "Return",
        "MGSN Connection / Gateway",
        "MGSN Network",
        "Originating Workplace",
        "Execution Provider Workplace",
        "Sites",
    )
    missing_terms = [term for term in required_terms if term not in plan]
    if missing_terms:
        raise ValidationError(f"terminology lock missing: {', '.join(missing_terms)}")

    chapter_ids = set(re.findall(r"\bCH(?:0[0-9]|[1-3][0-9])\b", impact))
    expected = {f"CH{i:02d}" for i in range(40)}
    if chapter_ids != expected:
        missing = sorted(expected - chapter_ids)
        extra = sorted(chapter_ids - expected)
        raise ValidationError(f"chapter coverage mismatch; missing={missing}, extra={extra}")

    if "MO-ARCH-PLN-001 corrections mapped: 12 / 12" not in read(
        "books/book-04-workplace-product-architecture/BOOK-STATUS.md"
    ):
        raise ValidationError("Book 04 status does not record 12 / 12 correction coverage")

    for needle in (
        "Blocking findings: 0",
        "Unmapped Canon correction: 0",
        "Unmapped chapter: 0",
        "RC1 source modification: 0",
    ):
        if needle not in review:
            raise ValidationError(f"review missing result: {needle}")

    print("WP-A records and coverage: PASS")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        print("protected diff: SKIPPED (no base SHA)")
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [
        path for path in changed if any(path == p or path.startswith(p) for p in PROTECTED_PREFIXES)
    ]
    if violations:
        raise ValidationError("protected source changed:\n" + "\n".join(f"- {p}" for p in violations))
    print(f"protected diff: PASS ({len(changed)} changed files checked)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        validate_records()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Book 04 vNext WP-A validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
