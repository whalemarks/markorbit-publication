#!/usr/bin/env python3
"""Validate materialized Book 04 vNext accepted manuscript and protected boundaries."""
from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-04-workplace-product-architecture"
TARGET = BOOK / "accepted-vnext"
BUILDER = ROOT / "tools/build_book04_vnext_candidate_04.py"
PROTECTED = (
    "books/book-04-workplace-product-architecture/manuscript/",
    "books/book-04-workplace-product-architecture/publication/",
    "architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.1.md",
    "architecture/DECISION-REGISTER-vNEXT.1.md",
    "books/book-02-core-specification/",
    "books/book-05-markreg/manuscript/",
    "books/book-06-markorbit-lite/manuscript/",
    "books/book-07-mark-global-service-network/manuscript/",
)
TOP_LEVEL = (
    "CANDIDATE-INDEX.md",
    "SOURCE-MANIFEST.md",
    "ROUTE-REPORT.md",
    "TRANSFORM-REPORT.md",
    "BUILD-REPORT.md",
)

class ValidationError(RuntimeError):
    pass


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_materialized() -> None:
    chapters = sorted((TARGET / "manuscript").glob("CH??.md"))
    if len(chapters) != 40:
        raise ValidationError(f"expected 40 materialized chapters, found {len(chapters)}")
    with tempfile.TemporaryDirectory() as tmp:
        fresh = Path(tmp) / "candidate04"
        result = subprocess.run([sys.executable, str(BUILDER), "--output", str(fresh)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode:
            raise ValidationError(result.stderr.strip() or result.stdout.strip())
        for chapter in chapters:
            source = fresh / "manuscript" / chapter.name
            if digest(chapter) != digest(source):
                raise ValidationError(f"materialized chapter differs from Candidate 04: {chapter.name}")
        for name in TOP_LEVEL:
            target = TARGET / name
            source = fresh / name
            if not target.is_file() or digest(target) != digest(source):
                raise ValidationError(f"materialized metadata differs from Candidate 04: {name}")
    manifest = (TARGET / "MATERIALIZATION-MANIFEST.md").read_text(encoding="utf-8")
    for statement in (
        "Accepted chapters materialized: 40 / 40",
        "Candidate 04 byte-equivalence: PASS",
        "Materialization manifest coverage: PASS",
        "RC1 source modifications: 0",
        "Publication freeze readiness: YES",
        "Freeze authorization: NOT YET GRANTED",
    ):
        if statement not in manifest:
            raise ValidationError(f"manifest missing: {statement}")
    for path in chapters:
        if path.name not in manifest:
            raise ValidationError(f"manifest missing chapter: {path.name}")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [path for path in changed if any(path == prefix or path.startswith(prefix) for prefix in PROTECTED)]
    if violations:
        raise ValidationError("protected source changed:\n" + "\n".join(violations))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        validate_materialized()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Book 04 vNext publication preparation validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
