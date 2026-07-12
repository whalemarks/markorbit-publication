#!/usr/bin/env python3
"""Negative tests for validate_state_workflow_specs.py using temporary copies."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools/validate_state_workflow_specs.py"


def copy_fixture(tmp: Path) -> Path:
    target = tmp / "repo"
    def ignore(dir_name: str, names: list[str]) -> set[str]:
        return {".git", "__pycache__", ".pytest_cache"}.intersection(names)
    shutil.copytree(ROOT, target, ignore=ignore)
    return target


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), "--root", str(root)], text=True, capture_output=True)


def replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"fixture text not found in {path}: {old}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def case_order_value_removed(root: Path) -> None:
    replace(root / "books/book-02-core-specification/core-specs/controlled-state-values/order-status-values.md", "\nConfirmed\n", "\n")


def case_unexpected_status_added(root: Path) -> None:
    replace(root / "books/book-02-core-specification/core-specs/controlled-state-values/order-status-values.md", "DeletedReferenceOnly\n\n```", "DeletedReferenceOnly\nUnexpectedStatus\n\n```")


def case_transition_removed(root: Path) -> None:
    replace(root / "books/book-02-core-specification/core-specs/controlled-state-values/matter-status-values.md", "\nDraft -> Open\n", "\n")


def case_unauthorized_transition_added(root: Path) -> None:
    replace(root / "books/book-02-core-specification/core-specs/controlled-state-values/order-status-values.md", "Cancelled -> Archived\n\n```", "Cancelled -> Archived\nArchived -> Draft\n\n```")


def case_duplicate_spec_id(root: Path) -> None:
    replace(root / "books/book-02-core-specification/core-specs/controlled-state-values/order-status-values.md", "Spec ID: B02-CSV-ORDER-STATUS", "Spec ID: B02-CSV-TRADEMARK-STATUS")


def case_legacy_id_active_inventory(root: Path) -> None:
    path = root / "books/book-02-core-specification/indexes/object-index.md"
    text = path.read_text(encoding="utf-8")
    marker = "## 7.6 Reclassified Legacy Status and Workflow Entries"
    path.write_text(text.replace(marker, "| OBJ-TM-003 | Trademark Status | Active regression |\n\n" + marker, 1), encoding="utf-8")


def case_rejected_active_decision(root: Path) -> None:
    replace(root / "books/book-02-core-specification/core-specs/workflows/components/workflow-transition-definition.md", "Denied\nBlocked", "Denied\nRejected\nBlocked")


def case_missing_canonical_path(root: Path) -> None:
    (root / "books/book-02-core-specification/core-specs/controlled-state-values/order-status-values.md").unlink()


def case_order_service_quoted_active(root: Path) -> None:
    replace(root / "books/book-02-core-specification/core-specs/services/order-service.md", "Confirmed\nReadyForMatter", "Confirmed\nQuoted\nReadyForMatter")


def case_matter_service_suspended_active(root: Path) -> None:
    replace(root / "books/book-02-core-specification/core-specs/services/matter-service.md", "Cancelled\nArchived", "Cancelled\nSuspended\nArchived")


def case_task_service_reopened_active(root: Path) -> None:
    replace(root / "books/book-02-core-specification/core-specs/services/task-service.md", "Cancelled\nArchived", "Cancelled\nReopened\nArchived")


def case_service_reference_removed(root: Path) -> None:
    path = root / "books/book-02-core-specification/core-specs/services/order-service.md"
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace("core-specs/controlled-state-values/order-status-values.md", "core-specs/controlled-state-values/order-status-values-removed.md"), encoding="utf-8")


def case_service_order_changed(root: Path) -> None:
    replace(root / "books/book-02-core-specification/core-specs/services/order-service.md", "Draft\nPendingConfirmation", "PendingConfirmation\nDraft")


def case_component_permission_section_removed(root: Path) -> None:
    path = root / "books/book-02-core-specification/core-specs/workflows/components/workflow-state-definition.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("# Permission and Policy")
    end = text.index("# Human Review and Approval")
    path.write_text(text[:start] + text[end:], encoding="utf-8")


def case_component_versioning_section_removed(root: Path) -> None:
    path = root / "books/book-02-core-specification/core-specs/workflows/components/workflow-transition-definition.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("# Versioning")
    end = text.index("# Failure Behavior")
    path.write_text(text[:start] + text[end:], encoding="utf-8")


def case_component_acceptance_section_removed(root: Path) -> None:
    path = root / "books/book-02-core-specification/core-specs/workflows/components/workflow-transition-definition.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("# Acceptance Criteria")
    end = text.index("# Revision Notes")
    path.write_text(text[:start] + text[end:], encoding="utf-8")


CASES: list[tuple[str, Callable[[Path], None], str]] = [
    ("order status value removed", case_order_value_removed, "canonical-values"),
    ("unexpected status value added", case_unexpected_status_added, "canonical-values"),
    ("transition edge removed", case_transition_removed, "transition-matrix"),
    ("unauthorized transition added", case_unauthorized_transition_added, "transition-matrix"),
    ("duplicate Spec ID", case_duplicate_spec_id, "duplicate-spec-id"),
    ("legacy ID active inventory", case_legacy_id_active_inventory, "active-object-regression"),
    ("Rejected active decision", case_rejected_active_decision, "workflow-decision-vocabulary"),
    ("missing canonical path", case_missing_canonical_path, "missing-file"),
    ("Order Service Quoted active", case_order_service_quoted_active, "service-controlled-values"),
    ("Matter Service Suspended active", case_matter_service_suspended_active, "service-controlled-values"),
    ("Task Service Reopened active", case_task_service_reopened_active, "service-controlled-values"),
    ("Service canonical reference removed", case_service_reference_removed, "service-status-source-reference"),
    ("Service active status order changed", case_service_order_changed, "service-controlled-values"),
    ("component Permission and Policy removed", case_component_permission_section_removed, "component-section"),
    ("component Versioning removed", case_component_versioning_section_removed, "component-section"),
    ("component Acceptance Criteria removed", case_component_acceptance_section_removed, "component-section"),
]


def main() -> int:
    failures: list[str] = []
    for name, mutator, expected in CASES:
        with tempfile.TemporaryDirectory() as directory:
            fixture = copy_fixture(Path(directory))
            mutator(fixture)
            result = run_validator(fixture)
            output = result.stdout + result.stderr
            if result.returncode == 0 or expected not in output:
                failures.append(f"{name}: expected failure containing {expected!r}; rc={result.returncode}; output={output}")
            else:
                print(f"PASS negative case: {name}")
    if failures:
        print("Negative validator test failures:")
        for failure in failures:
            print(failure)
        return 1
    print("All negative validator tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
