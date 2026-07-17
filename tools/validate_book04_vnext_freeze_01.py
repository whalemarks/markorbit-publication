#!/usr/bin/env python3
"""Validate the frozen Book 04 vNext baseline and its SHA-256 bindings."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "books/book-04-workplace-product-architecture/accepted-vnext"
MANIFEST = BASE / "MATERIALIZATION-MANIFEST.md"
FREEZE = BASE / "FREEZE-MANIFEST.md"
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
ENTRY = re.compile(r"^- `([^`]+)` — `([0-9a-f]{64})`$", re.MULTILINE)


class ValidationError(RuntimeError):
    pass


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def validate_hashes() -> None:
    if not MANIFEST.is_file() or not FREEZE.is_file():
        raise ValidationError("freeze or materialization manifest missing")
    text = MANIFEST.read_text(encoding="utf-8")
    entries = ENTRY.findall(text)
    if len(entries) != 45:
        raise ValidationError(f"expected 45 SHA-256 entries, found {len(entries)}")
    chapters = [path for path, _ in entries if path.startswith("manuscript/CH")]
    metadata = [path for path, _ in entries if not path.startswith("manuscript/CH")]
    if len(chapters) != 40 or len(metadata) != 5:
        raise ValidationError(f"unexpected frozen set: chapters={len(chapters)}, metadata={len(metadata)}")
    for relative, expected in entries:
        target = BASE / relative
        if not target.is_file():
            raise ValidationError(f"missing frozen file: {relative}")
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            raise ValidationError(f"hash mismatch: {relative}")
    freeze = FREEZE.read_text(encoding="utf-8")
    for statement in (
        "B04-vNEXT-FROZEN-01",
        "Frozen chapters: 40 / 40",
        "Frozen metadata files: 5 / 5",
        "SHA-256 entries bound: 45 / 45",
        "Public/commercial distribution: NOT AUTHORIZED",
    ):
        if statement not in freeze:
            raise ValidationError(f"freeze manifest missing: {statement}")
    print("frozen content hashes: PASS (45 / 45)")


def validate_status() -> None:
    status = (ROOT / "books/book-04-workplace-product-architecture/BOOK-STATUS.md").read_text(encoding="utf-8")
    roadmap = (ROOT / "PUBLICATION-ROADMAP.md").read_text(encoding="utf-8")
    for statement in (
        "B04-vNEXT-FROZEN-01",
        "Book 04 vNext freeze: GRANTED",
        "Public/commercial distribution: NOT AUTHORIZED",
    ):
        if statement not in status:
            raise ValidationError(f"status missing: {statement}")
    if "B04-vNEXT-FROZEN-01" not in roadmap or "Freeze decision: GRANTED" not in roadmap:
        raise ValidationError("roadmap freeze state missing")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        print("protected diff: SKIPPED")
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    frozen_prefix = "books/book-04-workplace-product-architecture/accepted-vnext/"
    allowed_frozen = frozen_prefix + "FREEZE-MANIFEST.md"
    frozen_changes = [path for path in changed if path.startswith(frozen_prefix) and path != allowed_frozen]
    if frozen_changes:
        raise ValidationError("frozen content changed during freeze:\n" + "\n".join(frozen_changes))
    violations = [path for path in changed if any(path == prefix or path.startswith(prefix) for prefix in PROTECTED)]
    if violations:
        raise ValidationError("protected source changed:\n" + "\n".join(violations))
    print(f"protected diff: PASS ({len(changed)} changed files checked)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        validate_hashes()
        validate_status()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Book 04 vNext Freeze 01 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
