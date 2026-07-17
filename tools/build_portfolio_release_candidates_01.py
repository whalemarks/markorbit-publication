#!/usr/bin/env python3
"""Build deterministic seven-book publication release-candidate overlays."""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".artifacts/portfolio-release-candidates-01"

BOOKS = {
    "Book 01": ("book-01", ROOT / "books/book-01-operating-system", "manuscript"),
    "Book 02": ("book-02", ROOT / "books/book-02-core-specification", "manuscript"),
    "Book 03": ("book-03", ROOT / "books/book-03-execution-system", "manuscript"),
    "Book 04": ("book-04", ROOT / "books/book-04-workplace-product-architecture", "accepted-vnext/manuscript"),
    "Book 05": ("book-05", ROOT / "books/book-05-markreg", "manuscript"),
    "Book 06": ("book-06", ROOT / "books/book-06-markorbit-lite", "manuscript"),
    "Book 07": ("book-07", ROOT / "books/book-07-mark-global-service-network", "manuscript"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def copy_tree_if_present(source: Path, target: Path) -> int:
    if not source.is_dir():
        return 0
    shutil.copytree(source, target)
    return sum(1 for path in target.rglob("*") if path.is_file())


def apply_overlay(candidate_dirs: dict[str, Path]) -> list[dict[str, object]]:
    overlay = json.loads((ROOT / "portfolio/copyedit/PORTFOLIO-OVERLAY-0001.json").read_text(encoding="utf-8"))
    applied: list[dict[str, object]] = []
    total = 0
    for operation in overlay["operations"]:
        book = operation["book"]
        candidate = candidate_dirs[book]
        source_base = operation.get("base")
        if "file" in operation:
            source_path = Path(operation["file"])
            source_name = source_path.name
            target = candidate / "manuscript" / source_name
            targets = [target]
        else:
            targets = [candidate / "manuscript" / name for name in operation["files"]]
        op_count = 0
        for target in targets:
            if not target.is_file():
                raise FileNotFoundError(f"overlay target missing: {target}")
            text = target.read_text(encoding="utf-8")
            count = text.count(operation["from"])
            if count:
                text = text.replace(operation["from"], operation["to"])
                target.write_text(text, encoding="utf-8")
            op_count += count
        expected = operation.get("expected_occurrences", 1)
        if op_count != expected:
            raise RuntimeError(f"overlay count mismatch for {book}: expected {expected}, got {op_count}")
        total += op_count
        applied.append({"book": book, "classification": operation["classification"], "count": op_count})
    if total != overlay["total_expected_corrections"]:
        raise RuntimeError(f"total overlay mismatch: expected {overlay['total_expected_corrections']}, got {total}")
    return applied


def write_manifest(candidate: Path, book: str, source_root: Path, manuscript_source: Path) -> dict[str, object]:
    files = sorted(
        (path for path in candidate.rglob("*") if path.is_file() and path.name != "CANDIDATE-MANIFEST.md"),
        key=lambda path: path.relative_to(candidate).as_posix(),
    )
    placeholders = 0
    lines = [
        f"# {book} Publication Release Candidate 01",
        "",
        f"- Source book root: `{source_root.relative_to(ROOT).as_posix()}`",
        f"- Frozen manuscript source: `{manuscript_source.relative_to(ROOT).as_posix()}`",
        "- Overlay: `PORTFOLIO-OVERLAY-0001`",
        "- Semantic changes: `0`",
        "- Publication authorization: `NOT GRANTED`",
        "",
        "## SHA-256 bindings",
        "",
    ]
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore") if path.suffix.lower() in {".md", ".json", ".txt"} else ""
        placeholders += text.count("OWNER DECISION REQUIRED")
        lines.append(f"- `{path.relative_to(candidate).as_posix()}` — `{sha256(path)}`")
    manifest = candidate / "CANDIDATE-MANIFEST.md"
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"book": book, "files": len(files) + 1, "owner_decision_markers": placeholders, "manifest_sha256": sha256(manifest)}


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    series = ROOT / "portfolio/front-matter/SERIES-PAGE.md"
    project = ROOT / "portfolio/front-matter/MARKORBIT-PROJECT.md"
    candidate_dirs: dict[str, Path] = {}
    build_rows: list[dict[str, object]] = []

    for index, (book, (slug, book_root, manuscript_rel)) in enumerate(BOOKS.items(), start=1):
        manuscript_source = book_root / manuscript_rel
        if not manuscript_source.is_dir():
            raise FileNotFoundError(f"manuscript source missing: {manuscript_source}")
        candidate = OUT / slug
        candidate.mkdir(parents=True)
        shutil.copy2(series, candidate / "00-SERIES-PAGE.md")
        shutil.copy2(project, candidate / "01-MARKORBIT-PROJECT.md")
        shutil.copy2(ROOT / f"portfolio/front-matter/books/BOOK-{index:02d}.md", candidate / "02-BOOK-FRONT-MATTER.md")
        manuscript_files = copy_tree_if_present(manuscript_source, candidate / "manuscript")
        publication_files = copy_tree_if_present(book_root / "publication", candidate / "publication")
        figure_files = copy_tree_if_present(book_root / "figures", candidate / "figures")
        candidate_dirs[book] = candidate
        build_rows.append({
            "book": book,
            "slug": slug,
            "manuscript_files": manuscript_files,
            "publication_files": publication_files,
            "figure_files": figure_files,
            "source": manuscript_source.relative_to(ROOT).as_posix(),
        })

    applied = apply_overlay(candidate_dirs)
    manifests = []
    for book, (slug, book_root, manuscript_rel) in BOOKS.items():
        manifests.append(write_manifest(candidate_dirs[book], book, book_root, book_root / manuscript_rel))

    report = {
        "schema": "markorbit-portfolio-release-candidates/v1",
        "identifier": "PORTFOLIO-RC-01",
        "books_generated": 7,
        "overlay_corrections_applied": sum(int(row["count"]) for row in applied),
        "semantic_changes": 0,
        "frozen_source_mutations": 0,
        "publication_authorized": False,
        "books": build_rows,
        "overlay": applied,
        "manifests": manifests,
    }
    (OUT / "portfolio-release-candidates-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    (OUT / "BUILD-REPORT.md").write_text(
        "# PORTFOLIO-RC-01 Build Report\n\n"
        "```text\n"
        "Books generated: 7 / 7\n"
        f"Approved overlay corrections applied: {report['overlay_corrections_applied']} / 18\n"
        "Semantic changes: 0\n"
        "Frozen manuscript modifications: 0\n"
        "Candidate manifests: 7 / 7\n"
        "Candidate release authorization: NOT GRANTED\n"
        "```\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
