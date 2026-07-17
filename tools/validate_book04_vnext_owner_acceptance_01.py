#!/usr/bin/env python3
"""Validate the final Book 04 vNext Owner Acceptance decision."""
from __future__ import annotations
import argparse, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools/build_book04_vnext_candidate_04.py"
REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-OWNER-ACCEPTANCE-01.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0025_Final_Owner_Acceptance.md",
    "books/book-04-workplace-product-architecture/decisions/B04-DEC-0005_Final_Owner_Acceptance_Decision.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0023_Final_Owner_Acceptance_Review.md",
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

class ValidationError(RuntimeError): pass

def read(path: str) -> str:
    target = ROOT / path
    if not target.is_file(): raise ValidationError(f"missing required file: {path}")
    return target.read_text(encoding="utf-8")

def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode: raise ValidationError(result.stderr.strip())
    return result.stdout.strip()

def validate_acceptance() -> None:
    for path in REQUIRED: read(path)
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "candidate04"
        result = subprocess.run([sys.executable, str(BUILDER), "--output", str(out)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode: raise ValidationError(result.stderr.strip() or result.stdout.strip())
        chapters = sorted((out / "manuscript").glob("CH??.md"))
        if len(chapters) != 40: raise ValidationError(f"expected forty chapters, found {len(chapters)}")
        report = (out / "BUILD-REPORT.md").read_text(encoding="utf-8")
        for statement in (
            "Candidate 04 chapters generated: 40 / 40",
            "Superseded Lite-as-Workplace reader findings: 0",
            "Reader-text leakage findings: 0",
            "Architecture authority regression: 0",
            "RC1 source modifications: 0",
            "Blocking findings: 0",
            "Owner Acceptance readiness: YES",
        ):
            if statement not in report: raise ValidationError(f"Candidate 04 report missing: {statement}")
        ch01 = (out / "manuscript/CH01.md").read_text(encoding="utf-8")
        ch22 = (out / "manuscript/CH22.md").read_text(encoding="utf-8")
        ch23 = (out / "manuscript/CH23.md").read_text(encoding="utf-8")
        if "Lite as a Lightweight Workplace Product" not in ch01: raise ValidationError("CH01 final navigation regressed")
        if "Lite operate as a lightweight Workplace Product" not in ch22: raise ValidationError("CH22 final transition regressed")
        if "# B04-CH-23 — Lite as a Lightweight Workplace Product" not in ch23: raise ValidationError("CH23 accepted heading regressed")
    decision = read("books/book-04-workplace-product-architecture/decisions/B04-DEC-0005_Final_Owner_Acceptance_Decision.md")
    if "ACCEPT — Candidate 04 is accepted as the Book 04 vNext editorial baseline." not in decision:
        raise ValidationError("formal ACCEPT decision missing")
    status = read("books/book-04-workplace-product-architecture/BOOK-STATUS.md")
    for statement in (
        "Candidate 04 as final vNext prose: ACCEPTED",
        "Book 04 vNext owner acceptance: GRANTED",
        "Freeze, publication and distribution: NOT AUTHORIZED",
    ):
        if statement not in status: raise ValidationError(f"status missing: {statement}")

def validate_diff(base_sha: str | None) -> None:
    if not base_sha: return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [p for p in changed if any(p == prefix or p.startswith(prefix) for prefix in PROTECTED)]
    if violations: raise ValidationError("protected source changed:\n" + "\n".join(violations))

def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("--base-sha"); a = p.parse_args()
    try:
        validate_acceptance(); validate_diff(a.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr); return 1
    print("Book 04 vNext final Owner Acceptance validation: PASS"); return 0

if __name__ == "__main__": raise SystemExit(main())
