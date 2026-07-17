#!/usr/bin/env python3
"""Validate pagination optimization controls and generated PDFs."""
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".artifacts/portfolio-pagination-optimization-01"
BASELINE = {1:163, 2:1642, 3:1037, 4:1612, 5:390, 6:534, 7:183}

class ValidationError(RuntimeError): pass

def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode: raise ValidationError(result.stderr.strip())
    return result.stdout.strip()

def validate_diff(base_sha: str | None) -> None:
    if not base_sha: return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    protected = ("books/", "portfolio/front-matter/")
    violations = [p for p in changed if p.startswith(protected)]
    if violations: raise ValidationError("protected content changed:\n" + "\n".join(violations))

def validate_controls() -> None:
    required = [
        "codex/tasks/PUB-TASK-PORTFOLIO-PAGINATION-OPTIMIZATION-01.md",
        "portfolio/render/pagination-optimization-profile.json",
        "tools/render_portfolio_paginated_editions_01.py",
        "tools/preflight_portfolio_paginated_editions_01.py",
    ]
    for item in required:
        if not (ROOT / item).is_file(): raise ValidationError(f"missing {item}")
    profile = json.loads((ROOT / required[1]).read_text(encoding="utf-8"))
    if profile.get("semantic_changes") != 0 or profile.get("frozen_source_mutation") is not False:
        raise ValidationError("protected boundaries not locked")

def validate_outputs() -> None:
    report_path = OUT / "preflight-report.json"
    if not report_path.is_file(): raise ValidationError("preflight report missing")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if report.get("books_preflighted") != 7 or not report.get("page_size_pass") or not report.get("extractable_text_pass") or not report.get("low_content_pass"):
        raise ValidationError("PDF preflight failed")
    pages = {int(r["book"].split()[1]): int(r["pages"]) for r in report["books"]}
    for book, baseline in BASELINE.items():
        if pages[book] > baseline: raise ValidationError(f"Book {book:02d} page count increased")
    old_total, new_total = sum(BASELINE.values()), sum(pages.values())
    if new_total > int(old_total * 0.75):
        raise ValidationError(f"insufficient total reduction: {old_total} -> {new_total}")
    for book in (2, 3, 4):
        if pages[book] > int(BASELINE[book] * 0.75):
            raise ValidationError(f"Book {book:02d} reduction below target")
    summary = {"baseline_pages": BASELINE, "optimized_pages": pages, "baseline_total": old_total, "optimized_total": new_total, "reduction_percent": round((old_total-new_total)*100/old_total, 2), "publication_authorized": False}
    (OUT / "pagination-comparison.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))

def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--base-sha"); parser.add_argument("--outputs", action="store_true"); args = parser.parse_args()
    try:
        validate_diff(args.base_sha); validate_controls()
        if args.outputs: validate_outputs()
    except (ValidationError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}"); return 1
    print("Portfolio Pagination Optimization 01 validation: PASS"); return 0

if __name__ == "__main__": raise SystemExit(main())
