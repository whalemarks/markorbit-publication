#!/usr/bin/env python3
"""Validate Book 04 Workplace Sovereignty vNext WP-F."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-WP-F.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0013_Full_Book_Impact_Review_and_Next_Version_Decision_WP-F.md",
    "books/book-04-workplace-product-architecture/reviews/B04-AUD-0001_Full_Book_vNext_Impact_Audit.md",
    "books/book-04-workplace-product-architecture/decisions/B04-DEC-0001_Next_Version_Integration_Decision.md",
    "books/book-04-workplace-product-architecture/vnext/B04-INT-0001_Integrated_Candidate_Baseline_Manifest.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0011_Full_Book_Impact_Review_and_Next_Version_Decision.md",
)

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
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def validate_records() -> None:
    for path in REQUIRED:
        read(path)
    audit = read(REQUIRED[2])
    decision = read(REQUIRED[3])
    review = read(REQUIRED[5])
    status = read("books/book-04-workplace-product-architecture/BOOK-STATUS.md")
    for statement in (
        "Chapters accounted for: 40 / 40",
        "Required correction classes: 12 / 12",
        "Blocking contradictions: 0",
        "Immediate Book 02 Change Proposal required: NO",
    ):
        if statement not in audit:
            raise ValidationError(f"audit missing result: {statement}")
    if "GO — authorize preparation of an integrated Book 04 vNext Candidate Baseline" not in decision:
        raise ValidationError("decision does not record GO")
    for statement in (
        "WP-F recommendation: PASS",
        "Integrated candidate preparation decision: GO",
        "Accepted amendment packages: 4 / 4",
        "Blocking findings: 0",
    ):
        if statement not in review:
            raise ValidationError(f"review missing result: {statement}")
    if "WP-F audit and GO decision: READY FOR OWNER ACCEPTANCE" not in status:
        raise ValidationError("status does not expose WP-F owner gate")
    print("WP-F records and decision: PASS")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        print("protected diff: SKIPPED")
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [p for p in changed if any(p == prefix or p.startswith(prefix) for prefix in PROTECTED)]
    if violations:
        raise ValidationError("protected source changed:\n" + "\n".join(violations))
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
    print("Book 04 vNext WP-F validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
