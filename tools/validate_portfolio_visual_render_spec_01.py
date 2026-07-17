#!/usr/bin/env python3
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


def require(path: str, statements: tuple[str, ...] = ()) -> str:
    target = ROOT / path
    if not target.is_file():
        raise ValidationError(f"missing file: {path}")
    text = target.read_text(encoding="utf-8")
    for statement in statements:
        if statement not in text:
            raise ValidationError(f"{path} missing: {statement}")
    return text


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
    font_ext = (".ttf", ".otf", ".woff", ".woff2")
    font_files = [path for path in changed if path.lower().endswith(font_ext)]
    if font_files:
        raise ValidationError("font binaries committed:\n" + "\n".join(font_files))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        require("codex/tasks/PUB-TASK-PORTFOLIO-VISUAL-RENDER-SPEC-01.md", ("Books covered: 7 / 7",))
        visual = require("portfolio/visual/PORTFOLIO-VISUAL-0001_Seven_Book_Visual_System.md", ("6 × 9 in", "OS", "CORE", "EXEC", "WORK", "REG", "LITE", "NET"))
        render = require("portfolio/render/PORTFOLIO-RENDER-0001_Rendering_Specification.md", ("PDF review profile", "Print profile", "EPUB profile", "PORTFOLIO-RC-01"))
        require("portfolio/decisions/PORTFOLIO-DEC-0005_Visual_and_Rendering_Specification.md", ("Review rendering: AUTHORIZED", "Publication and distribution: NOT AUTHORIZED"))
        require("portfolio/reviews/PORTFOLIO-REV-0004_Visual_and_Rendering_Specification_Review.md")
        tokens = json.loads((ROOT / "portfolio/visual/design-tokens.json").read_text(encoding="utf-8"))
        profiles = json.loads((ROOT / "portfolio/render/render-profiles.json").read_text(encoding="utf-8"))
        if len(tokens.get("books", {})) != 7:
            raise ValidationError("design-token book coverage is not 7 / 7")
        if set(profiles.get("profiles", {})) != {"pdf_review", "pdf_print", "epub3"}:
            raise ValidationError("render profile coverage incomplete")
        if tokens.get("font_binaries_committed") is not False:
            raise ValidationError("font binary policy not locked")
        if profiles.get("publication_authorized") is not False:
            raise ValidationError("publication gate not locked")
        if "color alone" not in visual or "owner legal metadata unresolved" not in render:
            raise ValidationError("accessibility or release gate missing")
        validate_diff(args.base_sha)
    except (ValidationError, json.JSONDecodeError, FileNotFoundError) as exc:
        print(f"FAIL: {exc}")
        return 1
    print("Portfolio Visual Render Spec 01 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
