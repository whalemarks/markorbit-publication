#!/usr/bin/env python3
"""Generate a non-mutating cross-book copyedit and reference audit."""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_ROOTS = sorted((ROOT / "books").glob("book-*"))
OUT = ROOT / ".artifacts" / "portfolio-copyedit-01"
RULES = ROOT / "portfolio/copyedit/normalization-rules.json"

EXCLUDED_PARTS = {
    "planning", "reviews", "tasks", "audits", "decisions", "vnext", "codex"
}


def controlled_files(book: Path) -> list[Path]:
    if (book / "accepted-vnext" / "manuscript").is_dir():
        roots = [book / "accepted-vnext" / "manuscript"]
    else:
        roots = [path for path in (book / "manuscript", book / "publication") if path.is_dir()]
    files: list[Path] = []
    for root in roots:
        files.extend(path for path in root.rglob("*.md") if not EXCLUDED_PARTS.intersection(path.parts))
    return sorted(set(files))


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def main() -> int:
    rules = json.loads(RULES.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    findings: list[dict[str, object]] = []
    scanned: dict[str, int] = {}
    category_counts: Counter[str] = Counter()

    variants = [(item["from"], item["to"]) for item in rules["safe_replacements"]]
    markdown_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    stale_series = re.compile(r"Books?\s+01[–-]06\b|six-book", re.IGNORECASE)
    page_ref = re.compile(r"\b(?:p\.|page)\s*\d+\b", re.IGNORECASE)

    for book in BOOK_ROOTS:
        files = controlled_files(book)
        if not files:
            continue
        book_id = book.name.split("-")[1]
        scanned[f"Book {book_id}"] = len(files)
        for path in files:
            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(ROOT).as_posix()
            for old, new in variants:
                for match in re.finditer(re.escape(old), text):
                    findings.append({
                        "book": f"Book {book_id}", "file": rel,
                        "line": line_number(text, match.start()),
                        "category": "SAFE_NORMALIZATION",
                        "found": old, "recommended": new,
                    })
                    category_counts["SAFE_NORMALIZATION"] += 1
            for match in stale_series.finditer(text):
                findings.append({
                    "book": f"Book {book_id}", "file": rel,
                    "line": line_number(text, match.start()),
                    "category": "SERIES_REFERENCE_REVIEW",
                    "found": match.group(0),
                    "recommended": "Review against the current Books 01–07 portfolio",
                })
                category_counts["SERIES_REFERENCE_REVIEW"] += 1
            for match in page_ref.finditer(text):
                findings.append({
                    "book": f"Book {book_id}", "file": rel,
                    "line": line_number(text, match.start()),
                    "category": "PAGINATION_DEPENDENT",
                    "found": match.group(0),
                    "recommended": "Resolve after final pagination",
                })
                category_counts["PAGINATION_DEPENDENT"] += 1
            for match in markdown_link.finditer(text):
                target = match.group(1).strip()
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                clean = target.split("#", 1)[0]
                if not clean:
                    continue
                resolved = (path.parent / clean).resolve()
                try:
                    resolved.relative_to(ROOT.resolve())
                except ValueError:
                    continue
                if not resolved.exists():
                    findings.append({
                        "book": f"Book {book_id}", "file": rel,
                        "line": line_number(text, match.start()),
                        "category": "BROKEN_LOCAL_LINK",
                        "found": target,
                        "recommended": "Correct unambiguous target in publication overlay",
                    })
                    category_counts["BROKEN_LOCAL_LINK"] += 1

    report = {
        "schema": "markorbit-portfolio-copyedit-audit/v1",
        "books_scanned": len(scanned),
        "files_scanned": scanned,
        "finding_count": len(findings),
        "category_counts": dict(sorted(category_counts.items())),
        "findings": findings,
        "frozen_manuscript_modifications": 0,
        "semantic_changes_applied": 0,
    }
    (OUT / "portfolio-copyedit-findings.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    lines = [
        "# PORTFOLIO-AUD-0002 — Cross-Book Publication Copyedit Findings",
        "",
        "## Summary",
        "",
        f"- Books scanned: {len(scanned)} / 7",
        f"- Findings recorded: {len(findings)}",
        "- Frozen manuscript modifications: 0",
        "- Semantic changes applied: 0",
        "",
        "## Category counts",
        "",
    ]
    if category_counts:
        for category, count in sorted(category_counts.items()):
            lines.append(f"- **{category}:** {count}")
    else:
        lines.append("- No machine-detectable findings.")
    lines += ["", "## Book coverage", ""]
    for book, count in sorted(scanned.items()):
        lines.append(f"- **{book}:** {count} controlled Markdown files")
    lines += [
        "", "## Decision", "",
        "Safe normalization findings may be applied only in a publication overlay.",
        "Ambiguous or meaning-changing findings require a separately reviewed change proposal.",
    ]
    (OUT / "PORTFOLIO-AUD-0002_Cross_Book_Copyedit_Findings.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print(f"Books scanned: {len(scanned)} / 7")
    print(f"Findings recorded: {len(findings)}")
    return 0 if len(scanned) == 7 else 1


if __name__ == "__main__":
    raise SystemExit(main())
