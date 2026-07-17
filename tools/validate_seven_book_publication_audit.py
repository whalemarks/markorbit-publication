#!/usr/bin/env python3
"""Validate seven-book publication readiness audit outputs and protected boundaries."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDITOR = ROOT / "tools/audit_seven_book_publication_readiness.py"
REQUIRED = (
    "codex/tasks/PUB-TASK-PORTFOLIO-PUBLICATION-AUDIT-01.md",
    "portfolio/planning/PORTFOLIO-PLN-0004_Seven_Book_Publication_Readiness_Audit.md",
    "portfolio/decisions/PORTFOLIO-DEC-0001_Publication_Closeout_Sequence.md",
)
PROTECTED = (
    "books/book-01-operating-system/manuscript/",
    "books/book-01-operating-system/publication/",
    "books/book-02-core-specification/",
    "books/book-03-execution-system/manuscript/",
    "books/book-03-execution-system/publication/",
    "books/book-04-workplace-product-architecture/accepted-vnext/",
    "books/book-05-markreg/manuscript/",
    "books/book-06-markorbit-lite/manuscript/",
    "books/book-07-mark-global-service-network/manuscript/",
)

class ValidationError(RuntimeError):
    pass


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def validate_outputs() -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            raise ValidationError(f"missing required file: {relative}")
    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp) / "audit"
        result = subprocess.run([sys.executable, str(AUDITOR), "--output", str(output)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode:
            raise ValidationError(result.stderr.strip() or result.stdout.strip())
        json_path = output / "portfolio-publication-audit.json"
        md_path = output / "PORTFOLIO-AUD-0001_Seven_Book_Publication_Readiness.md"
        if not json_path.is_file() or not md_path.is_file():
            raise ValidationError("audit outputs missing")
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        summary = payload.get("summary", {})
        books = payload.get("books", [])
        if summary.get("books_audited") != 7 or len(books) != 7:
            raise ValidationError("expected seven audited books")
        if summary.get("dimensions_assessed") != 6:
            raise ValidationError("expected six readiness dimensions")
        if summary.get("publication_authorization") != "NOT GRANTED":
            raise ValidationError("audit must not grant publication authorization")
        for book in books:
            dimensions = book.get("dimensions", {})
            if len(dimensions) != 6:
                raise ValidationError(f"{book.get('book')} missing dimensions")
            for value in dimensions.values():
                if value.get("rating") not in {"READY", "PARTIAL", "MISSING", "DECISION"}:
                    raise ValidationError("invalid audit rating")
        report = md_path.read_text(encoding="utf-8")
        for statement in (
            "Books audited: 7 / 7",
            "Readiness dimensions assessed: 6 / 6",
            "Frozen manuscript modifications: 0",
            "Publication authorization: NOT GRANTED",
            "Required remediation sequence",
        ):
            if statement not in report:
                raise ValidationError(f"report missing: {statement}")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [path for path in changed if any(path.startswith(prefix) for prefix in PROTECTED)]
    if violations:
        raise ValidationError("frozen content changed:\n" + "\n".join(violations))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        validate_outputs()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Seven-book publication readiness audit validation: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
