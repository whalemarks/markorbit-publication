#!/usr/bin/env python3
"""Validate seven generated publication release candidates."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".artifacts/portfolio-release-candidates-01"


class ValidationError(RuntimeError):
    pass


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    protected = (
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
    violations = [path for path in changed if any(path.startswith(prefix) for prefix in protected)]
    if violations:
        raise ValidationError("frozen content changed:\n" + "\n".join(violations))


def validate_outputs() -> None:
    report_path = OUT / "portfolio-release-candidates-report.json"
    build_report = OUT / "BUILD-REPORT.md"
    if not report_path.is_file() or not build_report.is_file():
        raise ValidationError("portfolio build reports missing")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    expected = {
        "books_generated": 7,
        "overlay_corrections_applied": 18,
        "semantic_changes": 0,
        "frozen_source_mutations": 0,
        "publication_authorized": False,
    }
    for key, value in expected.items():
        if report.get(key) != value:
            raise ValidationError(f"report mismatch for {key}: {report.get(key)!r}")
    for index in range(1, 8):
        candidate = OUT / f"book-{index:02d}"
        for required in (
            "00-SERIES-PAGE.md",
            "01-MARKORBIT-PROJECT.md",
            "02-BOOK-FRONT-MATTER.md",
            "CANDIDATE-MANIFEST.md",
        ):
            if not (candidate / required).is_file():
                raise ValidationError(f"Book {index:02d} missing {required}")
        manuscript = candidate / "manuscript"
        if not manuscript.is_dir() or not any(manuscript.rglob("*.md")):
            raise ValidationError(f"Book {index:02d} manuscript missing")
        manifest = (candidate / "CANDIDATE-MANIFEST.md").read_text(encoding="utf-8")
        if "Publication authorization: `NOT GRANTED`" not in manifest:
            raise ValidationError(f"Book {index:02d} release gate missing")
        for path in candidate.rglob("*"):
            if path.is_file() and path.name != "CANDIDATE-MANIFEST.md":
                binding = f"- `{path.relative_to(candidate).as_posix()}` — `{digest(path)}`"
                if binding not in manifest:
                    raise ValidationError(f"Book {index:02d} stale manifest binding: {path}")

    book1 = (OUT / "book-01/manuscript/13_Appendix_C.md").read_text(encoding="utf-8")
    if "Book 1" in book1 or "Book 01" not in book1:
        raise ValidationError("Book 01 numbering overlay not applied")
    book4_manuscript = OUT / "book-04/manuscript"
    book4_text = "\n".join(path.read_text(encoding="utf-8") for path in book4_manuscript.rglob("*.md"))
    if re.search(r"(?<!\.)\.\./publication/", book4_text):
        raise ValidationError("Book 04 stale publication links remain")
    if re.search(r"(?<!\.)\.\./figures/", book4_text):
        raise ValidationError("Book 04 stale figure links remain")
    fixed_publication = book4_text.count("../../publication/")
    fixed_figures = book4_text.count("../../figures/")
    if fixed_publication != 7 or fixed_figures != 10:
        raise ValidationError(f"Book 04 fixed link counts wrong: {fixed_publication}, {fixed_figures}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        validate_diff(args.base_sha)
        validate_outputs()
    except (ValidationError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 1
    print("Portfolio Release Candidates 01 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
