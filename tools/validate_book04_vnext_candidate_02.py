#!/usr/bin/env python3
"""Validate route-aware generation of Book 04 vNext Candidate 02."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools/build_book04_vnext_candidate_02.py"
REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-CANDIDATE-02.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0020_Candidate_02_Route_Aware_Regeneration.md",
    "books/book-04-workplace-product-architecture/vnext/B04-ROUTE-0001_Candidate_02_Chapter_Route_Manifest.json",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0018_Candidate_02_Route_Aware_Generation_Review.md",
    "tools/build_book04_vnext_candidate_02.py",
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
EXPECTED_REPORT = (
    "RC1 chapters discovered: 40 / 40",
    "Editorial modules discovered: 40 / 40",
    "Target chapters generated: 40 / 40",
    "Apparatus-only chapters: 1 / 1",
    "Explicit route entries: 40 / 40",
    "Accepted editorial modules represented: 40 / 40",
    "Reader-text leakage findings: 0",
    "Unresolved numeric-only routes: 0",
    "Duplicate chapter identities: 0",
    "Missing chapter identities: 0",
    "RC1 source modifications: 0",
    "Blocking findings: 0",
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
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def validate_generated() -> None:
    for path in REQUIRED:
        read(path)
    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp) / "candidate02"
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
        for index, path in enumerate(chapters):
            if path.name != f"CH{index:02d}.md":
                raise ValidationError(f"chapter sequence mismatch at {path.name}")
            text = path.read_text(encoding="utf-8")
            for token in (
                "candidate: B04-vNEXT-CANDIDATE-02",
                f"chapter: CH{index:02d}",
                "route_manifest:",
                "placement:",
                "integration_status: route-aware-review-candidate",
            ):
                if token not in text:
                    raise ValidationError(f"{path.name} missing provenance token: {token}")
        checks = {
            "CH01.md": (("Table of Contents",), ("Independence is not architectural isolation", "Single organizational container")),
            "CH15.md": (("Capability Discovery and Skill Selection", "A Capability describes what governed work can be supported"), ("Intelligence is a derived and contextual evaluation",)),
            "CH17.md": (("Intelligence is a derived and contextual evaluation", "candidate recommendation"), ()),
            "CH18.md": (("From Prepared Action to Governed Execution",), ("A Capability describes what governed work can be supported",)),
            "CH29.md": (("Content, Artifact and Document Boundaries", "Content is meaning under preparation"), ()),
            "CH30.md": (("Artifact Lifecycle, Versioning and Provenance", "A Render is a representation of an exact Artifact version"), ()),
            "CH31.md": (("Render, Edit, Delivery and Publish", "material Edit", "Delivery makes an approved Artifact"), ()),
            "CH38.md": (("Conformance and Future Architecture Specifications", "constitutional architecture"), ("Workplace portability",)),
            "CH39.md": (("Conclusion: Each in Its Own Orbit", "Core defines shared meaning"), ("Assigned chapters:", "Chapter weave modules:")),
        }
        for filename, (required, forbidden) in checks.items():
            text = (output / "manuscript" / filename).read_text(encoding="utf-8")
            for token in required:
                if token not in text:
                    raise ValidationError(f"{filename} missing routed content: {token}")
            for token in forbidden:
                if token in text:
                    raise ValidationError(f"{filename} contains forbidden content: {token}")
        report = (output / "BUILD-REPORT.md").read_text(encoding="utf-8")
        for statement in EXPECTED_REPORT:
            if statement not in report:
                raise ValidationError(f"build report missing: {statement}")
        route_report = (output / "ROUTE-REPORT.md").read_text(encoding="utf-8")
        if sum(1 for line in route_report.splitlines() if line.startswith("| CH")) != 40:
            raise ValidationError("route report does not contain forty target entries")
    status = read("books/book-04-workplace-product-architecture/BOOK-STATUS.md")
    if "Candidate 02 generation: READY FOR OWNER ACCEPTANCE" not in status:
        raise ValidationError("status does not expose Candidate 02 Owner gate")
    print("Candidate 02 route-aware generation: PASS")


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
        validate_generated()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Book 04 vNext Candidate 02 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
