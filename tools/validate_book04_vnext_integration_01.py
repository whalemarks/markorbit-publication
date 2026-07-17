#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-INTEGRATION-01.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0014_Integrated_Candidate_Baseline_Preparation.md",
    "books/book-04-workplace-product-architecture/vnext/B04-INT-0002_Deterministic_Candidate_Build_Specification.md",
    "books/book-04-workplace-product-architecture/vnext/B04-PROV-0001_CH00-CH39_Integrated_Candidate_Provenance_Ledger.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0012_Integrated_Candidate_Baseline_Preparation_Review.md",
    "tools/build_book04_vnext_candidate.py",
)
PROTECTED = (
    "books/book-04-workplace-product-architecture/manuscript/",
    "books/book-04-workplace-product-architecture/publication/",
    "books/book-04-workplace-product-architecture/figures/",
    "architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.1.md",
    "architecture/DECISION-REGISTER-vNEXT.1.md",
    "books/book-02-core-specification/",
    "books/book-05-markreg/",
    "books/book-06-markorbit-lite/",
    "books/book-07-mark-global-service-network/",
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

def validate(base_sha: str | None) -> None:
    for path in REQUIRED:
        read(path)
    ledger = read(REQUIRED[3])
    for i in range(40):
        chapter = f"CH{i:02d}"
        if f"| {chapter} |" not in ledger:
            raise ValidationError(f"provenance ledger missing {chapter}")
    for statement in (
        "Chapter source entries: 40 / 40",
        "Accepted amendment packages represented: 4 / 4",
        "Candidate generation readiness: PASS",
        "Blocking findings: 0",
    ):
        combined = read(REQUIRED[3]) + read(REQUIRED[4])
        if statement not in combined:
            raise ValidationError(f"integration records missing result: {statement}")

    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "candidate"
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/build_book04_vnext_candidate.py"), "--output", str(out)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode:
            raise ValidationError(f"candidate build failed: {result.stderr.strip()}")
        chapters = sorted((out / "manuscript").glob("CH??.md"))
        if len(chapters) != 40:
            raise ValidationError(f"candidate chapter count is {len(chapters)}, expected 40")
        report = (out / "BUILD-REPORT.md").read_text(encoding="utf-8")
        for statement in (
            "RC1 chapters discovered: 40 / 40",
            "Candidate chapters generated: 40 / 40",
            "Accepted amendments registered: 4 / 4",
            "Unattributed inserted controls: 0",
            "RC1 mutations: 0",
        ):
            if statement not in report:
                raise ValidationError(f"build report missing: {statement}")

    if base_sha:
        changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
        violations = [p for p in changed if any(p == prefix or p.startswith(prefix) for prefix in PROTECTED)]
        if violations:
            raise ValidationError("protected source changed:\n" + "\n".join(violations))
    print("Book 04 vNext integration preparation validation: PASS")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        validate(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
