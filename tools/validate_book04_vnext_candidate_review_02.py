#!/usr/bin/env python3
"""Validate Candidate 02 full-book review findings and protected boundaries."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-CANDIDATE-REVIEW-02.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0021_Candidate_02_Full_Book_Review.md",
    "books/book-04-workplace-product-architecture/vnext/B04-AUD-0003_Candidate_02_Full_Book_Findings.md",
    "books/book-04-workplace-product-architecture/vnext/B04-DEC-0003_Candidate_02_Review_Decision.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0019_Candidate_02_Full_Book_Review.md",
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
    audit = read(REQUIRED[2])
    decision = read(REQUIRED[3])
    expected = (
        "Candidate chapters inspected: 40 / 40",
        "Candidate 01 route blockers closed: 7 / 7",
        "Reader-text leakage findings: 0",
        "Remaining title contradictions: 1",
        "Candidate 03 required: YES",
        "REVISE — generate Candidate 03 before Owner Acceptance.",
    )
    for statement in expected:
        if statement not in audit and statement not in decision:
            raise ValidationError(f"missing review result: {statement}")

    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "candidate"
        result = subprocess.run(
            [sys.executable, "tools/build_book04_vnext_candidate_02.py", "--output", str(out)],
            cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        if result.returncode:
            raise ValidationError(result.stderr.strip() or result.stdout.strip())
        chapters = sorted((out / "manuscript").glob("CH??.md"))
        if len(chapters) != 40:
            raise ValidationError("Candidate 02 did not regenerate forty chapters")
        ch01 = (out / "manuscript/CH01.md").read_text(encoding="utf-8")
        ch22 = (out / "manuscript/CH22.md").read_text(encoding="utf-8")
        ch23 = (out / "manuscript/CH23.md").read_text(encoding="utf-8")
        ch39 = (out / "manuscript/CH39.md").read_text(encoding="utf-8")
        if "editorial_modules: none" not in ch01:
            raise ValidationError("CH01 is not apparatus-only")
        if "editorial_modules: CH22" not in ch22 or "A Product Installation is the Workplace-scoped" not in ch22:
            raise ValidationError("CH22 Product Installation placement finding not reproduced")
        if "# B04-CH-23 — Lite as a Lightweight Workplace" not in ch23 or "Lite is a lightweight Workplace Product" not in ch23:
            raise ValidationError("CH23 title contradiction not reproduced")
        for token in ("Assigned chapters:", "Chapter weave modules:", "Placement rules present:"):
            if token in ch39:
                raise ValidationError(f"reader-text leakage remains: {token}")

    print("Candidate 02 review findings reproduced: PASS")

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
        validate_review()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Book 04 vNext Candidate Review 02 validation: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
