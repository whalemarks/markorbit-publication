#!/usr/bin/env python3
"""Validate Book 04 vNext Integration 02A editorial weave package."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-INTEGRATION-02A.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0015_CH00-CH12_Editorial_Integration_02A.md",
    "books/book-04-workplace-product-architecture/vnext/editorial/B04-EDIT-0001_CH00-CH12_Editorial_Weave_Patch_Set.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0013_CH00-CH12_Editorial_Integration_02A.md",
)

PROTECTED = (
    "books/book-04-workplace-product-architecture/manuscript/",
    "books/book-04-workplace-product-architecture/publication/",
    "books/book-04-workplace-product-architecture/figures/",
    "architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.1.md",
    "architecture/DECISION-REGISTER-vNEXT.1.md",
    "books/book-02-core-specification/",
    "books/book-05-markreg/manuscript/",
    "books/book-06-markorbit-lite/manuscript/",
    "books/book-07-mark-global-service-network/manuscript/",
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
        ["git", *args], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def validate_package() -> None:
    for path in REQUIRED:
        read(path)

    patch = read(REQUIRED[2])
    review = read(REQUIRED[3])
    chapters = re.findall(r"^## (CH(?:0[0-9]|1[0-2])) —", patch, flags=re.MULTILINE)
    expected = [f"CH{i:02d}" for i in range(13)]
    if chapters != expected:
        raise ValidationError(f"chapter weave coverage mismatch: {chapters}")

    required_terms = (
        "Organization-scoped business sovereignty",
        "Core semantic authority",
        "Owning Service formal-state authority",
        "Physical custody",
        "Legal / source authority",
        "Platform support and administration",
        "Originating Workplace retains",
        "AI context is assembled for a bounded task",
        "surface visibility",
        "Synchronization must preserve provenance",
    )
    for term in required_terms:
        if term not in patch:
            raise ValidationError(f"patch set missing required term: {term}")

    required_results = (
        "Assigned chapters: 13 / 13",
        "Chapter weave modules: 13 / 13",
        "Unattributed weave modules: 0",
        "RC1 source modifications: 0",
        "Immediate Book 02 Change Proposal required: NO",
        "Blocking findings: 0",
    )
    for result in required_results:
        if result not in review:
            raise ValidationError(f"review missing result: {result}")

    print("Integration 02A records and editorial coverage: PASS")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        print("protected diff: SKIPPED")
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [
        path for path in changed
        if any(path == prefix or path.startswith(prefix) for prefix in PROTECTED)
    ]
    if violations:
        raise ValidationError("protected source changed:\n" + "\n".join(violations))
    print(f"protected diff: PASS ({len(changed)} changed files checked)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        validate_package()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Book 04 vNext Integration 02A validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
