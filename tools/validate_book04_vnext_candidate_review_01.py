#!/usr/bin/env python3
"""Validate the Book 04 Candidate 01 full-book review and its recorded findings."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-04-workplace-product-architecture"

REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-CANDIDATE-REVIEW-01.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0019_Candidate_01_Full_Book_Review.md",
    "books/book-04-workplace-product-architecture/vnext/B04-AUD-0002_Candidate_01_Full_Book_Findings.md",
    "books/book-04-workplace-product-architecture/vnext/B04-DEC-0002_Candidate_01_Review_Decision.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0017_Candidate_01_Full_Book_Review.md",
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


def generate(output: Path) -> None:
    result = subprocess.run(
        [sys.executable, "tools/build_book04_vnext_candidate_01.py", "--output", str(output)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise ValidationError(result.stderr.strip() or result.stdout.strip())


def validate_findings() -> None:
    for path in REQUIRED:
        read(path)
    audit = read(REQUIRED[2])
    decision = read(REQUIRED[3])
    review = read(REQUIRED[4])

    expected = (
        "Candidate chapters inspected: 40 / 40",
        "Chapter-route blockers: 7",
        "Reader-text leakage blockers: 3",
        "Owner Acceptance readiness: NO",
        "Candidate 02 required: YES",
        "REVISE — generate Candidate 02 before Owner Acceptance.",
    )
    for statement in expected:
        if statement not in audit and statement not in decision and statement not in review:
            raise ValidationError(f"missing review result: {statement}")

    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "candidate"
        generate(out)
        chapters = sorted((out / "manuscript").glob("CH*.md"))
        if len(chapters) != 40:
            raise ValidationError("Candidate 01 did not regenerate forty chapters")

        checks = {
            "CH01.md": ("Table of Contents", "Single organizational container", "Independence is not architectural isolation"),
            "CH15.md": ("Capability Discovery and Skill Selection", "Intelligence is a derived and contextual evaluation"),
            "CH18.md": ("From Prepared Action to Governed Execution", "A Capability describes what governed work can be supported"),
            "CH22.md": ("Product Embedding and Cross-Product Context", "A Product Installation is the Workplace-scoped"),
            "CH28.md": ("Asset Library and Reusable Resources", "Content is meaning under preparation"),
            "CH39.md": ("Conclusion: Each in Its Own Orbit", "Assigned chapters: 12 / 12"),
        }
        for filename, tokens in checks.items():
            text = (out / "manuscript" / filename).read_text(encoding="utf-8")
            for token in tokens:
                if token not in text:
                    raise ValidationError(f"expected diagnostic finding absent from {filename}: {token}")

    print("Candidate 01 diagnostic findings reproduced: PASS")


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
        validate_findings()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Book 04 vNext Candidate Review 01 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
