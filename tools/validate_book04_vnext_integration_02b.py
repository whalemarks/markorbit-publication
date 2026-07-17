#!/usr/bin/env python3
"""Validate Book 04 vNext Integration 02B editorial weave package."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATCH = ROOT / "books/book-04-workplace-product-architecture/vnext/editorial/B04-EDIT-0002_CH13-CH27_Editorial_Weave_Patch_Set.md"
REVIEW = ROOT / "books/book-04-workplace-product-architecture/reviews/B04-REV-0014_CH13-CH27_Editorial_Integration_02B.md"
REQUIRED = (
    ROOT / "codex/tasks/PUB-TASK-B04-VNEXT-INTEGRATION-02B.md",
    ROOT / "books/book-04-workplace-product-architecture/planning/B04-PLN-0016_CH13-CH27_Editorial_Integration_02B.md",
    PATCH,
    REVIEW,
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


def read(path: Path) -> str:
    if not path.is_file():
        raise ValidationError(f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def validate_records() -> None:
    for path in REQUIRED:
        read(path)
    patch = read(PATCH)
    review = read(REVIEW)
    expected = {f"CH{i:02d}" for i in range(13, 28)}
    modules = set(re.findall(r"^## (CH(?:1[3-9]|2[0-7])) —", patch, flags=re.MULTILINE))
    if modules != expected:
        raise ValidationError(f"chapter module mismatch: missing={sorted(expected-modules)}, extra={sorted(modules-expected)}")
    for chapter in expected:
        start = patch.index(f"## {chapter} —")
        next_match = re.search(r"\n## CH(?:1[3-9]|2[0-7]) —", patch[start + 1 :])
        end = len(patch) if not next_match else start + 1 + next_match.start()
        block = patch[start:end]
        if not any(marker in block for marker in ("**RETAIN:**", "**REPLACE:**", "**MERGE", "**INSERT")):
            raise ValidationError(f"{chapter} missing editorial operation")
        if "**Authority:**" not in block or "**Continuity:**" not in block:
            raise ValidationError(f"{chapter} missing authority or continuity")
    for statement in (
        "Assigned chapters: 15 / 15",
        "Chapter weave modules: 15 / 15",
        "Placement rules present: 15 / 15",
        "Unattributed weave modules: 0",
        "Knowledge / Intelligence authority separation: PASS",
        "AI scope inheritance: PASS",
        "Human Review / Owning Service separation: PASS",
        "Product / Installation / Projection distinction: PASS",
        "Handoff / Return continuity: PASS",
        "Blocking findings: 0",
        "RC1 source modification: 0",
        "Immediate Book 02 Change Proposal required: NO",
    ):
        if statement not in patch or statement not in review:
            raise ValidationError(f"missing result statement: {statement}")
    print("Integration 02B records: PASS")


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
    print("Book 04 vNext Integration 02B validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
