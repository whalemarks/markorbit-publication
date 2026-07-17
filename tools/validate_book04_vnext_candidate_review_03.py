#!/usr/bin/env python3
"""Validate the final Candidate 03 review and reproduce its bounded findings."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools/build_book04_vnext_candidate_03.py"
REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-CANDIDATE-REVIEW-03.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0023_Candidate_03_Final_Review.md",
    "books/book-04-workplace-product-architecture/audits/B04-AUD-0004_Candidate_03_Final_Findings.md",
    "books/book-04-workplace-product-architecture/decisions/B04-DEC-0004_Candidate_03_Final_Review_Decision.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0021_Candidate_03_Final_Full_Book_Review.md",
)
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


def validate_review() -> None:
    for path in REQUIRED:
        read(path)
    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp) / "candidate03"
        result = subprocess.run(
            [sys.executable, str(BUILDER), "--output", str(output)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode:
            raise ValidationError(result.stderr.strip() or result.stdout.strip())
        chapters = sorted((output / "manuscript").glob("CH??.md"))
        if len(chapters) != 40:
            raise ValidationError(f"expected forty chapters, found {len(chapters)}")
        ch01 = (output / "manuscript/CH01.md").read_text(encoding="utf-8")
        ch20 = (output / "manuscript/CH20.md").read_text(encoding="utf-8")
        ch22 = (output / "manuscript/CH22.md").read_text(encoding="utf-8")
        ch23 = (output / "manuscript/CH23.md").read_text(encoding="utf-8")
        ch37 = (output / "manuscript/CH37.md").read_text(encoding="utf-8")
        if "# B04-CH-23 — Lite as a Lightweight Workplace Product" not in ch23:
            raise ValidationError("CH23 corrected heading is missing")
        if "## Product Installation as Governed Workplace Participation" not in ch20:
            raise ValidationError("CH20 Product Installation section is missing")
        if ch22.count("A Product Installation is the Workplace-scoped governed participation relationship") != 0:
            raise ValidationError("CH22 still contains the relocated primary definition")
        if "## Portability, Exit and Revocation Across Orbits" not in ch37:
            raise ValidationError("CH37 portability section is missing")
        stale_title = "B04-CH-23 — Lite as a Lightweight Workplace"
        stale_question = "How should Lite operate as a lightweight Workplace for independent professionals"
        if stale_title not in ch01:
            raise ValidationError("review finding not reproduced: stale CH01 title absent")
        if stale_question not in ch22:
            raise ValidationError("review finding not reproduced: stale CH22 transition absent")
        if "Assigned chapters:" in "\n".join(path.read_text(encoding="utf-8") for path in chapters):
            raise ValidationError("reader-text leakage regressed")
    status = read("books/book-04-workplace-product-architecture/BOOK-STATUS.md")
    for statement in (
        "Candidate Review 03: Review PASS / Candidate Acceptance FAIL",
        "Candidate 04 required: YES",
        "Candidate 04 preparation: READY FOR OWNER ACCEPTANCE",
    ):
        if statement not in status:
            raise ValidationError(f"status missing: {statement}")
    print("Candidate 03 final review findings: PASS")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        print("protected diff: SKIPPED")
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [path for path in changed if any(path == prefix or path.startswith(prefix) for prefix in PROTECTED)]
    if violations:
        raise ValidationError("protected source changed:\n" + "\n".join(violations))
    print(f"protected diff: PASS ({len(changed)} changed files checked)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        validate_review()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Book 04 vNext Candidate Review 03 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
