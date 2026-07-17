#!/usr/bin/env python3
"""Validate controls for seven-book PDF review rendering."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ValidationError(RuntimeError):
    pass


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def require(path: str, phrases: tuple[str, ...] = ()) -> None:
    target = ROOT / path
    if not target.is_file():
        raise ValidationError(f"missing file: {path}")
    text = target.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            raise ValidationError(f"{path} missing: {phrase}")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    protected = (
        "books/book-01-operating-system/manuscript/",
        "books/book-01-operating-system/publication/",
        "books/book-02-core-specification/",
        "books/book-03-execution-system/manuscript/",
        "books/book-03-execution-system/publication/",
        "books/book-04-workplace-product-architecture/accepted-vnext/",
        "books/book-05-markreg/manuscript/",
        "books/book-06-markorbit-lite/manuscript/",
        "books/book-07-mark-global-service-network/manuscript/",
    )
    violations = [path for path in changed if any(path.startswith(prefix) for prefix in protected)]
    if violations:
        raise ValidationError("frozen content changed:\n" + "\n".join(violations))
    font_suffixes = {".ttf", ".otf", ".woff", ".woff2", ".eot"}
    fonts = [path for path in changed if Path(path).suffix.lower() in font_suffixes]
    if fonts:
        raise ValidationError("font binaries committed:\n" + "\n".join(fonts))


def validate_outputs() -> None:
    out = ROOT / ".artifacts/portfolio-review-render-01"
    render = json.loads((out / "render-report.json").read_text(encoding="utf-8"))
    preflight = json.loads((out / "preflight-report.json").read_text(encoding="utf-8"))
    if render.get("books_rendered") != 7:
        raise ValidationError("rendered book count is not 7")
    if render.get("publication_authorized") is not False:
        raise ValidationError("render report release gate missing")
    if preflight.get("books_preflighted") != 7:
        raise ValidationError("preflighted book count is not 7")
    for key in ("pdf_readable", "page_size_pass", "extractable_text_pass", "low_content_pass"):
        if preflight.get(key) is not True:
            raise ValidationError(f"preflight failed: {key}")
    pdfs = list(out.glob("book-*/book-*-review.pdf"))
    if len(pdfs) != 7:
        raise ValidationError(f"expected 7 PDFs, found {len(pdfs)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    parser.add_argument("--outputs", action="store_true")
    args = parser.parse_args()
    try:
        require("codex/tasks/PUB-TASK-PORTFOLIO-REVIEW-RENDER-01.md", ("Books rendered: 7/7", "NOT GRANTED"))
        require("portfolio/planning/PORTFOLIO-PLN-0005_Seven_PDF_Review_Editions.md", ("6 x 9", "review artifact"))
        require("tools/render_portfolio_review_editions_01.py")
        require("tools/preflight_portfolio_review_editions_01.py")
        validate_diff(args.base_sha)
        if args.outputs:
            validate_outputs()
    except (ValidationError, json.JSONDecodeError, FileNotFoundError) as exc:
        print(f"FAIL: {exc}")
        return 1
    print("Portfolio Review Render 01 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
