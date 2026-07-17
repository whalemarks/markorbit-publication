#!/usr/bin/env python3
"""Validate Book 04 vNext Candidate 03."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools/build_book04_vnext_candidate_03.py"
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


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def validate_build() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "candidate03"
        result = subprocess.run([sys.executable, str(BUILDER), "--output", str(out)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode:
            raise ValidationError(result.stderr.strip() or result.stdout.strip())
        chapters = sorted((out / "manuscript").glob("CH??.md"))
        if len(chapters) != 40:
            raise ValidationError(f"expected forty chapters, found {len(chapters)}")
        for i, path in enumerate(chapters):
            text = path.read_text(encoding="utf-8")
            if path.name != f"CH{i:02d}.md":
                raise ValidationError(f"chapter sequence mismatch: {path.name}")
            for token in ("candidate: B04-vNEXT-CANDIDATE-03", "integration_status: editorial-consolidation-acceptance-candidate"):
                if token not in text:
                    raise ValidationError(f"{path.name} missing Candidate 03 provenance")
        ch20 = (out / "manuscript/CH20.md").read_text(encoding="utf-8")
        ch22 = (out / "manuscript/CH22.md").read_text(encoding="utf-8")
        ch23 = (out / "manuscript/CH23.md").read_text(encoding="utf-8")
        ch37 = (out / "manuscript/CH37.md").read_text(encoding="utf-8")
        if "## Product Installation as Governed Workplace Participation" not in ch20:
            raise ValidationError("CH20 missing relocated Product Installation definition")
        if ch22.count("A Product Installation is the Workplace-scoped governed participation relationship"):
            raise ValidationError("CH22 still contains the primary Product Installation definition")
        if "Product embedding uses an already governed Product Installation" not in ch22:
            raise ValidationError("CH22 missing embedding-focused bridge")
        if not ch23.startswith("# B04-CH-23 — Lite as a Lightweight Workplace Product"):
            raise ValidationError("CH23 heading was not corrected")
        if "operate as a lightweight Workplace without" in ch23:
            raise ValidationError("CH23 retains superseded Lite-as-Workplace language")
        if "## Portability, Exit and Revocation Across Orbits" not in ch37:
            raise ValidationError("CH37 lacks structured portability subsection")
        report = (out / "BUILD-REPORT.md").read_text(encoding="utf-8")
        for statement in (
            "Candidate 03 chapters generated: 40 / 40",
            "Remaining title contradictions: 0",
            "Remaining route / placement majors: 0",
            "Exact long-paragraph duplicate clusters: 0",
            "RC1 source modifications: 0",
            "Blocking findings: 0",
        ):
            if statement not in report:
                raise ValidationError(f"build report missing: {statement}")
    print("Candidate 03 editorial consolidation: PASS")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [p for p in changed if any(p == prefix or p.startswith(prefix) for prefix in PROTECTED)]
    if violations:
        raise ValidationError("protected source changed:\n" + "\n".join(violations))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        validate_build()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Book 04 vNext Candidate 03 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
