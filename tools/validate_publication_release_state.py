#!/usr/bin/env python3
"""Validate MarkOrbit publication release-state consistency."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK06_FREEZE = "4fce03cb7380117417b1ad479c743ef31a65b6c6"
BOOK07_CONTENT = "7ab3ea3e01b42afda8b2f675e514b91df436e47d"
BOOK07_OWNER_DECISION = "2f59951ceacfde3ed379e6de5dad602a192f48e3"
BOOK07_FREEZE = "3d3469a5845c352a2d73f698ffc085d5abb3aa85"
EXPECTED_RELEASE_REFS = {
    "release/book-06-rc1": BOOK06_FREEZE,
    "release/book-07-rc1": BOOK07_FREEZE,
}
PROTECTED_PREFIXES = (
    "architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.1.md",
    "architecture/DECISION-REGISTER-vNEXT.1.md",
    "books/book-02-core-specification/manuscript/",
    "books/book-02-core-specification/core-specs/",
    "books/book-05-markreg/manuscript/",
    "books/book-05-markreg/appendices/",
    "books/book-05-markreg/specifications/",
    "books/book-06-markorbit-lite/manuscript/",
    "books/book-06-markorbit-lite/reader-apparatus/",
    "books/book-06-markorbit-lite/specifications/",
    "books/book-07-mark-global-service-network/manuscript/",
    "books/book-07-mark-global-service-network/appendices/",
    "books/book-07-mark-global-service-network/specifications/",
)


class ValidationError(RuntimeError):
    pass


def read_text(relative_path: str) -> str:
    path = ROOT / relative_path
    if not path.is_file():
        raise ValidationError(f"missing required file: {relative_path}")
    return path.read_text(encoding="utf-8")


def require_contains(relative_path: str, *needles: str) -> None:
    content = read_text(relative_path)
    for needle in needles:
        if needle not in content:
            raise ValidationError(f"{relative_path} is missing required text: {needle}")


def require_not_contains(relative_path: str, *needles: str) -> None:
    content = read_text(relative_path)
    for needle in needles:
        if needle in content:
            raise ValidationError(f"{relative_path} contains stale or forbidden text: {needle}")


def run_git(*args: str) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=ROOT, check=False, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        raise ValidationError(f"git {' '.join(args)} failed: {completed.stderr.strip()}")
    return completed.stdout.strip()


def validate_root_metadata() -> None:
    require_contains(
        "README.md",
        "Book 06 | MarkOrbit Lite | Release Candidate 1 — Approved and Frozen",
        "Book 07 | Mark Global Service Network | Release Candidate 1 — Approved and Frozen",
        "Book 04 Workplace Sovereignty vNext Correction",
    )
    require_contains(
        "books/README.md",
        "Book 06 | MarkOrbit Lite",
        "Release Candidate 1 — Approved and Frozen",
        "Book 07 | Mark Global Service Network",
    )
    require_contains(
        "PUBLICATION-MANIFEST.md",
        "Book 06 | MarkOrbit Lite | Release Candidate 1 — Approved and Frozen",
        "Book 07 | Mark Global Service Network | Release Candidate 1 — Approved and Frozen",
        BOOK07_FREEZE,
    )
    print("root metadata consistency: PASS")


def validate_book07_docs() -> None:
    require_contains(
        "books/book-07-mark-global-service-network/BOOK-STATUS.md",
        "Release Candidate 1 — APPROVED AND FROZEN",
        BOOK07_CONTENT, BOOK07_OWNER_DECISION, BOOK07_FREEZE,
    )
    require_contains(
        "books/book-07-mark-global-service-network/BOOK-MANIFEST.md",
        "Status: Release Candidate 1 — APPROVED AND FROZEN",
        BOOK07_FREEZE, "release/book-07-rc1",
    )
    require_contains(
        "books/book-07-mark-global-service-network/README.md",
        "Release Candidate 1 — Approved and Frozen",
        BOOK07_FREEZE, "release/book-07-rc1",
    )
    require_contains(
        "books/book-07-mark-global-service-network/release/README.md",
        "B07-REL-0002", "FROZEN", "release/book-07-rc1",
    )
    print("Book 07 document metadata: PASS")


def validate_book07_machine() -> None:
    require_contains(
        "books/book-07-mark-global-service-network/book-07-state.yaml",
        "status: release_candidate_1_frozen",
        f"freeze_activation_commit: {BOOK07_FREEZE}",
        "release_branch_created: true",
    )
    require_contains(
        "books/book-07-mark-global-service-network/release/B07-RC1.yaml",
        "status: frozen",
        f"freeze_activation_commit: {BOOK07_FREEZE}",
        "release_branch: release/book-07-rc1",
        "release_branch_created: true",
    )
    require_not_contains(
        "books/book-07-mark-global-service-network/release/B07-RC1.yaml",
        "set_to_freeze_pr_merge_commit_after_owner_merge",
    )
    require_not_contains(
        "books/book-07-mark-global-service-network/book-07-state.yaml",
        "release_candidate_1_ready_for_owner_acceptance",
        "release_candidate_owner_decision",
    )
    print("Book 07 machine metadata: PASS")


def validate_release_refs() -> None:
    for branch, expected_sha in EXPECTED_RELEASE_REFS.items():
        output = run_git("ls-remote", "--heads", "origin", f"refs/heads/{branch}")
        match = re.fullmatch(r"([0-9a-f]{40})\s+refs/heads/.+", output)
        if not match:
            raise ValidationError(f"release branch not found on origin: {branch}")
        actual_sha = match.group(1)
        if actual_sha != expected_sha:
            raise ValidationError(f"{branch} points to {actual_sha}, expected {expected_sha}")
        print(f"release ref PASS: {branch} -> {actual_sha}")


def validate_protected_diff(base_sha: str | None) -> None:
    if not base_sha:
        print("protected source diff: SKIPPED (no base SHA supplied)")
        return
    changed = run_git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    violations = [
        path for path in changed
        if any(path == prefix or path.startswith(prefix) for prefix in PROTECTED_PREFIXES)
    ]
    if violations:
        raise ValidationError(
            "frozen or canonical source files changed in a governance-only task:\n"
            + "\n".join(f"- {path}" for path in violations)
        )
    print(f"protected source diff PASS: {len(changed)} changed files checked")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    parser.add_argument(
        "--only",
        choices=("root", "book07-docs", "book07-machine", "protected", "refs"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.only in (None, "root"):
            validate_root_metadata()
        if args.only in (None, "book07-docs"):
            validate_book07_docs()
        if args.only in (None, "book07-machine"):
            validate_book07_machine()
        if args.only in (None, "protected"):
            validate_protected_diff(args.base_sha)
        if args.only in (None, "refs"):
            validate_release_refs()
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("publication release-state validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
