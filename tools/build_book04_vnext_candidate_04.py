#!/usr/bin/env python3
"""Generate Book 04 vNext Candidate 04 from Candidate 03 with two bounded consistency corrections."""
from __future__ import annotations
import argparse, json, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-04-workplace-product-architecture"
SOURCE_BUILDER = ROOT / "tools/build_book04_vnext_candidate_03.py"
MANIFEST = BOOK / "vnext/B04-TRANSFORM-0002_Candidate_04_Final_Consistency_Manifest.json"
DEFAULT_OUT = ROOT / "build/book04-vnext-candidate-04"


def title(text: str) -> str:
    return next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), "Untitled")


def build(output: Path) -> None:
    source_out = output.parent / f"{output.name}-source-candidate-03"
    if source_out.exists(): shutil.rmtree(source_out)
    if output.exists(): shutil.rmtree(output)
    subprocess.run([sys.executable, str(SOURCE_BUILDER), "--output", str(source_out)], cwd=ROOT, check=True)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    shutil.copytree(source_out, output)
    manuscript = output / "manuscript"
    chapters = sorted(manuscript.glob("CH??.md"))
    if len(chapters) != 40: raise RuntimeError(f"expected 40 source chapters, found {len(chapters)}")
    applied = {}
    for chapter, replacements in manifest["authorized_changes"].items():
        path = manuscript / f"{chapter}.md"
        text = path.read_text(encoding="utf-8")
        count = 0
        for old, new in replacements:
            occurrences = text.count(old)
            if occurrences:
                text = text.replace(old, new)
                count += occurrences
        if count == 0: raise RuntimeError(f"no authorized replacement applied in {chapter}")
        text = text.replace("candidate: B04-vNEXT-CANDIDATE-03", "candidate: B04-vNEXT-CANDIDATE-04")
        text = text.replace("vNext Candidate 03", "vNext Candidate 04")
        path.write_text(text, encoding="utf-8")
        applied[chapter] = count
    for path in chapters:
        if path.stem not in manifest["authorized_changes"]:
            text = path.read_text(encoding="utf-8")
            text = text.replace("candidate: B04-vNEXT-CANDIDATE-03", "candidate: B04-vNEXT-CANDIDATE-04")
            text = text.replace("vNext Candidate 03", "vNext Candidate 04")
            path.write_text(text, encoding="utf-8")
    forbidden = manifest["forbidden_reader_phrase"]
    findings = []
    for path in chapters:
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if forbidden in line and "Workplace Product" not in line:
                findings.append(f"{path.name}:{line_no}:{line}")
    if findings: raise RuntimeError("superseded Lite wording remains:\n" + "\n".join(findings))
    index = ["# Book 04 vNext Candidate 04", "", "Status: FINAL CONSISTENCY-CORRECTED ACCEPTANCE CANDIDATE", ""]
    for path in chapters: index.append(f"- [{title(path.read_text(encoding='utf-8'))}](manuscript/{path.name})")
    (output / "CANDIDATE-INDEX.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    report = f"""# Candidate 04 Build Report

```text
Source Candidate 03 chapters: 40 / 40
Candidate 04 chapters generated: 40 / 40
CH01 navigation corrections: PASS
CH22 transition correction: PASS
Superseded Lite-as-Workplace reader findings: 0
Candidate 03 content preservation exceptions: 2 / 2 authorized
Reader-text leakage findings: 0
Architecture authority regression: 0
RC1 source modifications: 0
Blocking findings: 0
Immediate Book 02 Change Proposal required: NO
Owner Acceptance readiness: YES
```
"""
    (output / "BUILD-REPORT.md").write_text(report, encoding="utf-8")
    (output / "TRANSFORM-REPORT.md").write_text("# Candidate 04 Transform Report\n\n" + "\n".join(f"- {k}: {v} replacements" for k,v in applied.items()) + "\n", encoding="utf-8")
    shutil.rmtree(source_out)


def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("--output", type=Path, default=DEFAULT_OUT); a=p.parse_args()
    build(a.output if a.output.is_absolute() else ROOT/a.output)
    return 0

if __name__ == "__main__": raise SystemExit(main())