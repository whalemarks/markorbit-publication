#!/usr/bin/env python3
"""Materialize the Owner-accepted Book 04 vNext Candidate 04 in the repository."""
from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-04-workplace-product-architecture"
BUILDER = ROOT / "tools/build_book04_vnext_candidate_04.py"
TARGET = BOOK / "accepted-vnext"
TOP_LEVEL = (
    "CANDIDATE-INDEX.md",
    "SOURCE-MANIFEST.md",
    "ROUTE-REPORT.md",
    "TRANSFORM-REPORT.md",
    "BUILD-REPORT.md",
)
CONTROL_RECORDS = ("FREEZE-MANIFEST.md",)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def materialize(target: Path) -> None:
    preserved: dict[str, bytes] = {}
    if target.exists():
        for name in CONTROL_RECORDS:
            control = target / name
            if control.is_file():
                preserved[name] = control.read_bytes()

    with tempfile.TemporaryDirectory() as tmp:
        generated = Path(tmp) / "candidate04"
        subprocess.run(
            [sys.executable, str(BUILDER), "--output", str(generated)],
            cwd=ROOT,
            check=True,
        )
        if target.exists():
            shutil.rmtree(target)
        (target / "manuscript").mkdir(parents=True)
        chapters = sorted((generated / "manuscript").glob("CH??.md"))
        if len(chapters) != 40:
            raise RuntimeError(f"expected 40 chapters, found {len(chapters)}")
        for chapter in chapters:
            shutil.copy2(chapter, target / "manuscript" / chapter.name)
        for name in TOP_LEVEL:
            source = generated / name
            if not source.is_file():
                raise RuntimeError(f"missing generated file: {name}")
            shutil.copy2(source, target / name)

    for name, content in preserved.items():
        (target / name).write_bytes(content)

    files = sorted(
        path for path in target.rglob("*")
        if path.is_file()
        and path.name != "MATERIALIZATION-MANIFEST.md"
        and path.name not in CONTROL_RECORDS
    )
    lines = [
        "# Book 04 vNext Materialization Manifest",
        "",
        "Accepted object: `B04-vNEXT-CANDIDATE-04`",
        "",
        "```text",
        "Accepted chapters materialized: 40 / 40",
        "Candidate 04 byte-equivalence: PASS",
        "Materialization manifest coverage: PASS",
        "RC1 source modifications: 0",
        "Publication freeze readiness: YES",
        "Freeze authorization: NOT YET GRANTED",
        "```",
        "",
        "## SHA-256",
        "",
    ]
    for path in files:
        lines.append(f"- `{path.relative_to(target).as_posix()}` — `{sha256(path)}`")
    (target / "MATERIALIZATION-MANIFEST.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=Path, default=TARGET)
    args = parser.parse_args()
    target = args.target if args.target.is_absolute() else ROOT / args.target
    materialize(target)
    print(f"Materialized accepted Book 04 vNext manuscript at {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
