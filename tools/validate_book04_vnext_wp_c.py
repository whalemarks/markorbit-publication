#!/usr/bin/env python3
"""Validate Book 04 Workplace Sovereignty vNext WP-C."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-WP-C.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0010_Product_Installation_and_Projection_WP-C.md",
    "books/book-04-workplace-product-architecture/vnext/manuscript/B04-VNEXT-WPC-0001_Product_Installation_and_Projection_Model.md",
    "books/book-04-workplace-product-architecture/vnext/B04-CORR-0002_WP-C_Chapter_Correction_Ledger.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0008_Product_Installation_and_Projection_WP-C_Review.md",
)

ASSIGNED = ("CH20", "CH21", "CH22", "CH26", "CH27", "CH30", "CH31", "CH32", "CH38")

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
    amendment = read(REQUIRED[2])
    ledger = read(REQUIRED[3])
    review = read(REQUIRED[4])

    for term in (
        "Product Installation",
        "Product Projection",
        "Projection",
        "Handoff",
        "Return",
        "entitlement",
        "configuration",
        "formal-state authority",
    ):
        if term not in amendment:
            raise ValidationError(f"amendment missing term: {term}")

    for chapter in ASSIGNED:
        if chapter not in amendment:
            raise ValidationError(f"amendment missing chapter module: {chapter}")
        if chapter not in ledger:
            raise ValidationError(f"ledger missing chapter: {chapter}")

    for statement in (
        "Assigned chapters: 9 / 9 covered",
        "Product / Installation / Projection distinction: PASS",
        "Projection / Handoff / Return distinction: PASS",
        "Blocking findings: 0",
        "Unmapped assigned chapters: 0",
        "RC1 source modification: 0",
    ):
        if statement not in review:
            raise ValidationError(f"review missing result: {statement}")

    status = read("books/book-04-workplace-product-architecture/BOOK-STATUS.md")
    if "WP-C amendment manuscript: READY FOR OWNER ACCEPTANCE" not in status:
        raise ValidationError("Book 04 status does not expose WP-C candidate gate")

    print("WP-C records and chapter coverage: PASS")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        print("protected diff: SKIPPED")
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [p for p in changed if any(p == prefix or p.startswith(prefix) for prefix in PROTECTED)]
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
    print("Book 04 vNext WP-C validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
