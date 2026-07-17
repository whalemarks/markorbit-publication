#!/usr/bin/env python3
from __future__ import annotations
import argparse, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "codex/tasks/PUB-TASK-B04-VNEXT-WP-E.md",
    "books/book-04-workplace-product-architecture/planning/B04-PLN-0012_Cross_Workplace_Collaboration_and_Portability_WP-E.md",
    "books/book-04-workplace-product-architecture/vnext/manuscript/B04-VNEXT-WPE-0001_Cross_Workplace_Collaboration_and_Portability.md",
    "books/book-04-workplace-product-architecture/vnext/B04-CORR-0004_WP-E_Chapter_Correction_Ledger.md",
    "books/book-04-workplace-product-architecture/reviews/B04-REV-0010_Cross_Workplace_Collaboration_and_Portability_WP-E_Review.md",
)
ASSIGNED = ("CH12", "CH27", "CH32", "CH33", "CH34", "CH35", "CH36", "CH37")
PROTECTED = (
    "books/book-04-workplace-product-architecture/manuscript/",
    "books/book-04-workplace-product-architecture/publication/",
    "books/book-04-workplace-product-architecture/figures/",
    "architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.1.md",
    "architecture/DECISION-REGISTER-vNEXT.1.md",
    "books/book-02-core-specification/",
    "books/book-05-markreg/",
    "books/book-06-markorbit-lite/",
    "books/book-07-mark-global-service-network/",
)
class ValidationError(RuntimeError): pass

def read(path: str) -> str:
    p = ROOT / path
    if not p.is_file(): raise ValidationError(f"missing required file: {path}")
    return p.read_text(encoding="utf-8")

def git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode: raise ValidationError(r.stderr.strip())
    return r.stdout.strip()

def validate(base_sha: str | None) -> None:
    for p in REQUIRED: read(p)
    amendment, ledger, review = read(REQUIRED[2]), read(REQUIRED[3]), read(REQUIRED[4])
    for term in ("Originating Workplace", "Execution Provider Workplace", "destination acceptance", "originating acceptance", "export copy ≠ authority transfer", "Provider Supply", "Routing", "Trust assets"):
        if term not in amendment: raise ValidationError(f"amendment missing term: {term}")
    for ch in ASSIGNED:
        if ch not in amendment or ch not in ledger: raise ValidationError(f"chapter not fully covered: {ch}")
    for s in ("Assigned chapters: 8 / 8 covered", "Portability classification: PASS", "Platform network asset exclusion: PASS", "Blocking findings: 0", "Unmapped assigned chapters: 0", "RC1 source modification: 0"):
        if s not in review: raise ValidationError(f"review missing result: {s}")
    status = read("books/book-04-workplace-product-architecture/BOOK-STATUS.md")
    if "WP-E amendment manuscript: READY FOR OWNER ACCEPTANCE" not in status: raise ValidationError("Book 04 status does not expose WP-E candidate gate")
    if base_sha:
        changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
        bad = [p for p in changed if any(p == x or p.startswith(x) for x in PROTECTED)]
        if bad: raise ValidationError("protected source changed:\n" + "\n".join(bad))
    print("Book 04 vNext WP-E validation: PASS")

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--base-sha"); args = ap.parse_args()
    try: validate(args.base_sha)
    except ValidationError as e:
        print(f"FAIL: {e}", file=sys.stderr); return 1
    return 0
if __name__ == "__main__": raise SystemExit(main())
