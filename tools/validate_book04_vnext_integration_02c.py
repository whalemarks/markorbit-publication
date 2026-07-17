#!/usr/bin/env python3
"""Validate Book 04 vNext Integration 02C editorial weave package."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-INTEGRATION-02C.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0017_CH28-CH39_Editorial_Integration_02C.md",
    "books/book-04-workplace-product-architecture/vnext/editorial/B04-EDIT-0003_CH28-CH39_Editorial_Weave_Patch_Set.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0015_CH28-CH39_Editorial_Integration_02C.md",
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

EXPECTED_CHAPTERS = tuple(f"CH{i:02d}" for i in range(28, 40))
EXPECTED_RESULTS = (
    "Assigned chapters: 12 / 12",
    "Chapter weave modules: 12 / 12",
    "Placement rules present: 12 / 12",
    "Unattributed weave modules: 0",
    "Artifact / formal-record separation: PASS",
    "Render / Edit / Delivery / Publish separation: PASS",
    "Routing / appointment separation: PASS",
    "Trust contextuality: PASS",
    "Cross-Workplace sovereignty: PASS",
    "Portability boundary: PASS",
    "Adjacent-chapter continuity: PASS",
    "Blocking findings: 0",
    "RC1 source modification: 0",
    "Immediate Book 02 Change Proposal required: NO",
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
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def validate_records() -> None:
    for path in REQUIRED:
        read(path)
    patch = read(REQUIRED[2])
    review = read(REQUIRED[3])
    status = read("books/book-04-workplace-product-architecture/BOOK-STATUS.md")

    for chapter in EXPECTED_CHAPTERS:
        marker = f"## {chapter} —"
        if marker not in patch:
            raise ValidationError(f"missing chapter weave module: {chapter}")

    if patch.count("**PLACEMENT**") != 12:
        raise ValidationError("expected exactly twelve placement rules")
    if patch.count("**AUTHORITY**") != 12:
        raise ValidationError("expected exactly twelve authority routes")
    if patch.count("**CONTINUITY**") != 12:
        raise ValidationError("expected exactly twelve continuity routes")

    for statement in EXPECTED_RESULTS:
        if statement not in patch:
            raise ValidationError(f"patch set missing result: {statement}")
        if statement not in review:
            raise ValidationError(f"review missing result: {statement}")

    required_concepts = (
        "Artifact\n≠ formal business fact",
        "Delivery\n≠ Publish",
        "candidate surfaced\n≠ candidate selected",
        "Trust evidence\n≠ universal score",
        "Originating Workplace",
        "Workplace portability\n≠ portability of the platform network",
    )
    for concept in required_concepts:
        if concept not in patch:
            raise ValidationError(f"missing required concept lock: {concept}")

    if "Integration 02C editorial weave input: READY FOR OWNER ACCEPTANCE" not in status:
        raise ValidationError("status does not expose Integration 02C Owner gate")
    if "Total chapter weave coverage: 40 / 40" not in status:
        raise ValidationError("status does not expose full editorial coverage")

    print("Integration 02C records and chapter coverage: PASS")


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
    print("Book 04 vNext Integration 02C validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
