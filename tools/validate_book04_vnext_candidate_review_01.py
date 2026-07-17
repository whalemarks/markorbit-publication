#!/usr/bin/env python3
"""Validate the Book 04 Candidate 01 full-book review and its recorded findings."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

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
    combined = "\n".join(read(path) for path in REQUIRED[2:])
    for statement in (
        "Candidate chapters inspected: 40 / 40",
        "Chapter-route blockers: 7",
        "Reader-text leakage blockers: 3",
        "Owner Acceptance readiness: NO",
        "Candidate 02 required: YES",
        "REVISE — generate Candidate 02 before Owner Acceptance.",
    ):
        if statement not in combined:
            raise ValidationError(f"missing review result: {statement}")

    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "candidate"
        generate(out)
        manuscript = out / "manuscript"
        chapters = sorted(manuscript.glob("CH??.md"))
        if len(chapters) != 40:
            raise ValidationError("Candidate 01 did not regenerate forty chapters")

        title_expectations = {
            "CH01.md": "Table of Contents",
            "CH15.md": "Capability Discovery and Skill Selection",
            "CH18.md": "From Prepared Action to Governed Execution",
            "CH22.md": "Product Embedding and Cross-Product Context",
            "CH28.md": "Asset Library and Reusable Resources",
            "CH39.md": "Conclusion: Each in Its Own Orbit",
        }
        for filename, title in title_expectations.items():
            text = (manuscript / filename).read_text(encoding="utf-8")
            if title not in text:
                raise ValidationError(f"expected RC1 chapter identity absent from {filename}: {title}")

        ch01 = (manuscript / "CH01.md").read_text(encoding="utf-8").lower()
        if "independence is not architectural isolation" not in ch01:
            raise ValidationError("CH01 conceptual-route mismatch was not reproduced")
        if "single organizational container" not in ch01:
            raise ValidationError("CH01 reader-visible editorial instruction was not reproduced")

        ch39 = (manuscript / "CH39.md").read_text(encoding="utf-8").lower()
        if "assigned chapters: 12 / 12" not in ch39 or "placement rules present: 12 / 12" not in ch39:
            raise ValidationError("CH39 batch-result leakage was not reproduced")

        route_fingerprints = {
            "CH15.md": ("intelligence", "derived"),
            "CH18.md": ("capability", "skill"),
            "CH22.md": ("product installation", "entitlement"),
            "CH28.md": ("content", "formal business fact"),
        }
        for filename, tokens in route_fingerprints.items():
            text = (manuscript / filename).read_text(encoding="utf-8").lower()
            if not all(token in text for token in tokens):
                raise ValidationError(f"route-mismatch fingerprint absent from {filename}")

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
