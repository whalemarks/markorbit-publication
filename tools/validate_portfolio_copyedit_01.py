#!/usr/bin/env python3
"""Validate the seven-book publication copyedit control layer."""
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


def require(path: str, statements: tuple[str, ...] = ()) -> None:
    target = ROOT / path
    if not target.is_file():
        raise ValidationError(f"missing file: {path}")
    text = target.read_text(encoding="utf-8")
    for statement in statements:
        if statement not in text:
            raise ValidationError(f"{path} missing: {statement}")


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        require("codex/tasks/PUB-TASK-PORTFOLIO-COPYEDIT-01.md", ("Books scanned: 7/7",))
        require("portfolio/copyedit/PORTFOLIO-STYLE-0001.md", (
            "MarkOrbit Workplace and Product Architecture",
            "Product ≠ Product Installation ≠ Product Projection",
            "CHANGE PROPOSAL",
        ))
        require("portfolio/copyedit/normalization-rules.json")
        rules = json.loads((ROOT / "portfolio/copyedit/normalization-rules.json").read_text(encoding="utf-8"))
        if len(rules.get("canonical_titles", {})) != 7:
            raise ValidationError("canonical title coverage is not 7 / 7")
        if rules.get("semantic_change_policy") != "CHANGE PROPOSAL REQUIRED":
            raise ValidationError("semantic change policy not locked")
        require("tools/audit_portfolio_copyedit_01.py")
        validate_diff(args.base_sha)
    except (ValidationError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 1
    print("Portfolio Copyedit 01 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
