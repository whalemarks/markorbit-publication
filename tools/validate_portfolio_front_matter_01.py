#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FM = ROOT / "portfolio/front-matter"
PROTECTED = (
    "books/book-01-operating-system/manuscript/",
    "books/book-02-core-specification/",
    "books/book-03-execution-system/manuscript/",
    "books/book-04-workplace-product-architecture/accepted-vnext/",
    "books/book-05-markreg/manuscript/",
    "books/book-06-markorbit-lite/manuscript/",
    "books/book-07-mark-global-service-network/manuscript/",
)

class ValidationError(RuntimeError): pass

def git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode: raise ValidationError(r.stderr.strip())
    return r.stdout.strip()

def validate() -> None:
    required = [FM / "SERIES-PAGE.md", FM / "MARKORBIT-PROJECT.md", FM / "release-metadata.json"]
    required += [FM / f"books/BOOK-{i:02d}.md" for i in range(1, 8)]
    for path in required:
        if not path.is_file(): raise ValidationError(f"missing: {path.relative_to(ROOT)}")
    metadata = json.loads((FM / "release-metadata.json").read_text(encoding="utf-8"))
    if len(metadata.get("books", [])) != 7: raise ValidationError("release metadata must contain seven books")
    if metadata.get("publication_authorized") is not False: raise ValidationError("publication must remain unauthorized")
    for i, record in enumerate(metadata["books"], 1):
        if record.get("number") != i: raise ValidationError(f"book order mismatch at {i}")
        if record.get("isbn") != "OWNER DECISION REQUIRED": raise ValidationError(f"ISBN must remain gated for Book {i:02d}")
        text = (FM / f"books/BOOK-{i:02d}.md").read_text(encoding="utf-8")
        for phrase in ("## Title page", "## Copyright page", "OWNER DECISION REQUIRED", "Public/commercial distribution: **NOT AUTHORIZED**"):
            if phrase not in text: raise ValidationError(f"Book {i:02d} front matter missing: {phrase}")
    for path in (FM / "SERIES-PAGE.md", FM / "MARKORBIT-PROJECT.md"):
        if len(path.read_text(encoding="utf-8").strip()) < 200: raise ValidationError(f"shared asset too short: {path.name}")

def validate_diff(base_sha: str | None) -> None:
    if not base_sha: return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [p for p in changed if any(p.startswith(prefix) for prefix in PROTECTED)]
    if violations: raise ValidationError("frozen content changed:\n" + "\n".join(violations))

def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("--base-sha"); a = p.parse_args()
    try: validate(); validate_diff(a.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}"); return 1
    print("Portfolio common front matter validation: PASS"); return 0

if __name__ == "__main__": raise SystemExit(main())
