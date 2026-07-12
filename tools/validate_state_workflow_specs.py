#!/usr/bin/env python3
"""Validate Book 02 state value and workflow component specifications."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

LEGACY_IDS = {"OBJ-TM-003", "OBJ-ORD-004", "OBJ-MAT-002", "OBJ-TSK-003", "OBJ-WFC-002", "OBJ-WFC-003"}
DECISIONS = ["Allowed", "Denied", "Blocked", "ReviewRequired", "ApprovalRequired", "PermissionRequired", "PolicyRequired", "InvalidState", "InvalidTransition", "Unknown"]
LEGACY_TERMS = ["Rejected", "BlockedByPermission", "BlockedByPolicy", "BlockedByGuard"]

STATUS_VALUES = {
    "Trademark": ["Draft", "Planned", "PendingFiling", "Filed", "UnderExamination", "Published", "Opposed", "Registered", "Refused", "Abandoned", "Cancelled", "Expired", "Invalidated", "RenewalDue", "ReviewRequired", "Archived", "DeletedReferenceOnly"],
    "Order": ["Draft", "PendingConfirmation", "Confirmed", "ReadyForMatter", "MatterCreated", "InProgress", "WaitingForCustomer", "Completed", "Cancelled", "Archived", "DeletedReferenceOnly"],
    "Matter": ["Draft", "Open", "InProgress", "WaitingForCustomer", "WaitingForAgent", "WaitingForOffice", "ReviewRequired", "Blocked", "Completed", "Cancelled", "Archived", "DeletedReferenceOnly"],
    "Task": ["Draft", "Open", "Assigned", "InProgress", "Waiting", "Blocked", "ReviewRequired", "Completed", "Cancelled", "Archived", "DeletedReferenceOnly"],
}

STATUS_SPECS = {
    "Trademark": ("B02-CSV-TRADEMARK-STATUS", "trademark-status-values.md", "objects/trademark.md", 17),
    "Order": ("B02-CSV-ORDER-STATUS", "order-status-values.md", "objects/order.md", 11),
    "Matter": ("B02-CSV-MATTER-STATUS", "matter-status-values.md", "objects/matter.md", 12),
    "Task": ("B02-CSV-TASK-STATUS", "task-status-values.md", "objects/task.md", 11),
}

TRANSITIONS = {
    "Trademark": ["Draft -> Planned", "Planned -> Draft", "Draft -> PendingFiling", "Planned -> PendingFiling", "PendingFiling -> Planned", "PendingFiling -> Filed", "PendingFiling -> ReviewRequired", "PendingFiling -> Abandoned", "Filed -> UnderExamination", "Filed -> Published", "Filed -> Opposed", "Filed -> Registered", "Filed -> Refused", "Filed -> Abandoned", "Filed -> ReviewRequired", "UnderExamination -> Published", "UnderExamination -> Opposed", "UnderExamination -> Registered", "UnderExamination -> Refused", "UnderExamination -> Abandoned", "UnderExamination -> ReviewRequired", "Published -> Opposed", "Published -> Registered", "Published -> Refused", "Published -> Abandoned", "Published -> ReviewRequired", "Opposed -> Registered", "Opposed -> Refused", "Opposed -> Abandoned", "Opposed -> ReviewRequired", "Registered -> RenewalDue", "Registered -> Expired", "Registered -> Cancelled", "Registered -> Invalidated", "Registered -> ReviewRequired", "RenewalDue -> Registered", "RenewalDue -> Expired", "RenewalDue -> Cancelled", "RenewalDue -> ReviewRequired", "Refused -> ReviewRequired", "Refused -> Abandoned", "Refused -> Archived", "Abandoned -> ReviewRequired", "Abandoned -> Archived", "Cancelled -> ReviewRequired", "Cancelled -> Archived", "Expired -> ReviewRequired", "Expired -> Archived", "Invalidated -> ReviewRequired", "Invalidated -> Archived"],
    "Order": ["Draft -> PendingConfirmation", "Draft -> Cancelled", "Draft -> Archived", "PendingConfirmation -> Draft", "PendingConfirmation -> Confirmed", "PendingConfirmation -> Cancelled", "Confirmed -> ReadyForMatter", "Confirmed -> InProgress", "Confirmed -> Cancelled", "ReadyForMatter -> MatterCreated", "ReadyForMatter -> InProgress", "ReadyForMatter -> Cancelled", "MatterCreated -> InProgress", "MatterCreated -> Completed", "MatterCreated -> Cancelled", "InProgress -> WaitingForCustomer", "InProgress -> Completed", "InProgress -> Cancelled", "WaitingForCustomer -> InProgress", "WaitingForCustomer -> Cancelled", "Completed -> Archived", "Cancelled -> Archived"],
    "Matter": ["Draft -> Open", "Draft -> Cancelled", "Draft -> Archived", "Open -> InProgress", "Open -> WaitingForCustomer", "Open -> WaitingForAgent", "Open -> WaitingForOffice", "Open -> ReviewRequired", "Open -> Blocked", "Open -> Completed", "Open -> Cancelled", "InProgress -> WaitingForCustomer", "InProgress -> WaitingForAgent", "InProgress -> WaitingForOffice", "InProgress -> ReviewRequired", "InProgress -> Blocked", "InProgress -> Completed", "InProgress -> Cancelled", "WaitingForCustomer -> InProgress", "WaitingForCustomer -> ReviewRequired", "WaitingForCustomer -> Blocked", "WaitingForCustomer -> Cancelled", "WaitingForAgent -> InProgress", "WaitingForAgent -> ReviewRequired", "WaitingForAgent -> Blocked", "WaitingForAgent -> Cancelled", "WaitingForOffice -> InProgress", "WaitingForOffice -> ReviewRequired", "WaitingForOffice -> Blocked", "WaitingForOffice -> Cancelled", "ReviewRequired -> InProgress", "ReviewRequired -> WaitingForCustomer", "ReviewRequired -> WaitingForAgent", "ReviewRequired -> WaitingForOffice", "ReviewRequired -> Blocked", "ReviewRequired -> Completed", "ReviewRequired -> Cancelled", "Blocked -> InProgress", "Blocked -> ReviewRequired", "Blocked -> Cancelled", "Completed -> Archived", "Cancelled -> Archived"],
    "Task": ["Draft -> Open", "Draft -> Assigned", "Draft -> Cancelled", "Draft -> Archived", "Open -> Assigned", "Open -> InProgress", "Open -> Waiting", "Open -> Blocked", "Open -> ReviewRequired", "Open -> Completed", "Open -> Cancelled", "Assigned -> InProgress", "Assigned -> Waiting", "Assigned -> Blocked", "Assigned -> ReviewRequired", "Assigned -> Completed", "Assigned -> Cancelled", "InProgress -> Waiting", "InProgress -> Blocked", "InProgress -> ReviewRequired", "InProgress -> Completed", "InProgress -> Cancelled", "Waiting -> Assigned", "Waiting -> InProgress", "Waiting -> Blocked", "Waiting -> ReviewRequired", "Waiting -> Cancelled", "Blocked -> Assigned", "Blocked -> InProgress", "Blocked -> Waiting", "Blocked -> ReviewRequired", "Blocked -> Cancelled", "ReviewRequired -> Assigned", "ReviewRequired -> InProgress", "ReviewRequired -> Completed", "ReviewRequired -> Cancelled", "Completed -> Archived", "Cancelled -> Archived", "Completed -> Open", "Cancelled -> Open"],
}

@dataclass
class Violation:
    file: Path
    violation_type: str
    expected: object
    actual: object

class Validator:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.core = root / "books/book-02-core-specification/core-specs"
        self.errors: list[Violation] = []

    def fail(self, file: Path, typ: str, expected: object, actual: object) -> None:
        try:
            file = file.relative_to(self.root)
        except ValueError:
            pass
        self.errors.append(Violation(file, typ, expected, actual))

    def read(self, path: Path) -> str:
        if not path.exists():
            self.fail(path, "missing-file", "file exists", "missing")
            return ""
        return path.read_text(encoding="utf-8")

    def fenced_block_after(self, text: str, heading: str) -> list[str]:
        pattern = rf"^# {re.escape(heading)}\s*\n\s*```text\s*\n(.*?)\n```"
        match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
        return [line.strip() for line in match.group(1).splitlines() if line.strip()] if match else []

    def parent_values(self, text: str) -> list[str]:
        section = re.search(r"^## 7\.2 status\s*\n(.*?)(?=^## 7\.3 )", text, re.MULTILINE | re.DOTALL)
        source = section.group(1) if section else text
        match = re.search(r"^MVP controlled values:\s*\n\s*```text\s*\n(.*?)\n```", source, re.MULTILINE | re.DOTALL)
        return [line.strip() for line in match.group(1).splitlines() if line.strip()] if match else []

    def edge_set(self, file: Path, values: list[str], lines: Iterable[str]) -> set[tuple[str, str]]:
        edges: list[tuple[str, str]] = []
        for line in lines:
            match = re.fullmatch(r"([A-Za-z0-9]+)\s*->\s*([A-Za-z0-9]+)", line)
            if not match:
                self.fail(file, "malformed-transition", "From -> To", line)
                continue
            source, target = match.groups()
            if source not in values or target not in values:
                self.fail(file, "unknown-transition-state", f"states in {values}", line)
            edges.append((source, target))
        duplicate_edges = sorted({edge for edge in edges if edges.count(edge) > 1})
        if duplicate_edges:
            self.fail(file, "duplicate-transition", "no duplicate edges", duplicate_edges)
        return set(edges)

    def validate_status_specs(self) -> None:
        seen: dict[str, Path] = {}
        for name, (expected_id, spec_file, parent_file, expected_count) in STATUS_SPECS.items():
            path = self.core / "controlled-state-values" / spec_file
            text = self.read(path)
            spec_id_match = re.search(r"^Spec ID:\s*(\S+)", text, re.MULTILINE)
            actual_id = spec_id_match.group(1) if spec_id_match else None
            if actual_id is None:
                self.fail(path, "missing-spec-id", expected_id, "missing")
            elif actual_id != expected_id:
                self.fail(path, "unexpected-spec-id", expected_id, actual_id)
            if actual_id in LEGACY_IDS:
                self.fail(path, "legacy-id-used-as-spec-id", "non-legacy Spec ID", actual_id)
            if actual_id:
                if actual_id in seen:
                    self.fail(path, "duplicate-spec-id", f"unique Spec ID, first seen in {seen[actual_id]}", actual_id)
                seen[actual_id] = path
            if "Spec Type: Controlled State Value Specification" not in text:
                self.fail(path, "spec-type", "Controlled State Value Specification", "missing")
            expected_values = STATUS_VALUES[name]
            actual_values = self.fenced_block_after(text, "5. Canonical Values")
            if actual_values != expected_values:
                self.fail(path, "canonical-values", expected_values, actual_values)
            if len(actual_values) != expected_count:
                self.fail(path, "canonical-value-count", expected_count, len(actual_values))
            parent_path = self.core / parent_file
            parent_actual = self.parent_values(self.read(parent_path))
            if parent_actual != expected_values:
                self.fail(parent_path, "parent-controlled-values", expected_values, parent_actual)
            actual_edges = self.edge_set(path, expected_values, self.fenced_block_after(text, "10. Transition Model"))
            expected_edges = self.edge_set(path, expected_values, TRANSITIONS[name])
            if actual_edges != expected_edges:
                self.fail(path, "transition-matrix", sorted(expected_edges), sorted(actual_edges))
            if name == "Task":
                required = "Ordinary `changeTaskStatus` must not silently reopen"
                if required not in text or "governed reopen operation" not in text:
                    self.fail(path, "governed-reopen-text", required, "missing")
            if "Canonical " in text and " lifecycle state `" in text:
                self.fail(path, "boilerplate-semantics", "value-specific semantics", "boilerplate lifecycle text")
        component_ids = {
            "B02-WFC-STATE-DEFINITION": self.core / "workflows/components/workflow-state-definition.md",
            "B02-WFC-TRANSITION-DEFINITION": self.core / "workflows/components/workflow-transition-definition.md",
        }
        for expected_id, path in component_ids.items():
            text = self.read(path)
            actual_id = re.search(r"^Spec ID:\s*(\S+)", text, re.MULTILINE)
            if not actual_id or actual_id.group(1) != expected_id:
                self.fail(path, "component-spec-id", expected_id, actual_id.group(1) if actual_id else "missing")
            if "Spec Type: Workflow Contract Component Specification" not in text:
                self.fail(path, "component-spec-type", "Workflow Contract Component Specification", "missing")

    def validate_required_sections(self) -> None:
        for _name, (_sid, spec_file, _parent, _count) in STATUS_SPECS.items():
            path = self.core / "controlled-state-values" / spec_file
            text = self.read(path)
            for number in range(1, 29):
                if not re.search(rf"^# {number}\. ", text, re.MULTILINE):
                    self.fail(path, "required-section", f"section {number}", "missing")
        required_component_sections = ["Purpose", "Canonical Meaning", "Required Fields"]
        for file in ["workflow-state-definition.md", "workflow-transition-definition.md"]:
            path = self.core / "workflows/components" / file
            text = self.read(path)
            for section in required_component_sections:
                if section not in text:
                    self.fail(path, "component-section", section, "missing")

    def decision_block(self, text: str) -> list[str]:
        match = re.search(r"```text\s*\n(Allowed\nDenied\nBlocked\nReviewRequired\nApprovalRequired\nPermissionRequired\nPolicyRequired\nInvalidState\nInvalidTransition\nUnknown)\s*\n```", text)
        return match.group(1).splitlines() if match else []

    def validate_decision_vocabulary(self) -> None:
        files = [
            self.core / "workflows/components/workflow-transition-definition.md",
            self.core / "services/workflow-contract-service.md",
            self.core / "objects/workflow-contract.md",
            self.core / "api/workflow-contract-api.md",
            self.core / "contracts/api/workflow-contract-api-contract.md",
        ]
        for path in files:
            actual = self.decision_block(self.read(path))
            if actual != DECISIONS:
                self.fail(path, "workflow-decision-vocabulary", DECISIONS, actual)

    def validate_legacy_term_scope(self) -> None:
        scoped_files = [
            self.core / "workflows/components/workflow-transition-definition.md",
            self.core / "services/workflow-contract-service.md",
            self.core / "objects/workflow-contract.md",
            self.core / "api/workflow-contract-api.md",
            self.core / "contracts/api/workflow-contract-api-contract.md",
        ]
        for path in scoped_files:
            text = self.read(path)
            for term in ["BlockedByPermission", "BlockedByPolicy", "BlockedByGuard"]:
                if term not in text:
                    continue
                if path == self.core / "workflows/components/workflow-transition-definition.md" and "Compatibility Notes" in text:
                    continue
                self.fail(path, "legacy-workflow-decision-term", "compatibility mapping/note only", term)

    def validate_object_index(self) -> None:
        path = self.root / "books/book-02-core-specification/indexes/object-index.md"
        text = self.read(path)
        split = text.split("## 7.6 Reclassified Legacy Status and Workflow Entries", 1)
        active_region = split[0]
        for legacy_id in LEGACY_IDS:
            if legacy_id in active_region:
                self.fail(path, "active-object-regression", f"{legacy_id} absent before reclassification section", "present")
        pattern = re.compile(r"\[([^\]]+\.md)\]\((\.\./core-specs/[^)]+\.md)\)")
        links = dict(pattern.findall(text))
        expected = {
            "controlled-state-values/trademark-status-values.md",
            "controlled-state-values/order-status-values.md",
            "controlled-state-values/matter-status-values.md",
            "controlled-state-values/task-status-values.md",
            "workflows/components/workflow-state-definition.md",
            "workflows/components/workflow-transition-definition.md",
        }
        if set(links) & expected != expected:
            self.fail(path, "object-index-canonical-links", expected, set(links) & expected)
        for label, target in links.items():
            if label in expected:
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    self.fail(path, "canonical-link-target", f"existing target for {label}", target)

    def run(self) -> int:
        for required in [self.core / "controlled-state-values/index.md", self.core / "workflows/components/index.md"]:
            if not required.exists():
                self.fail(required, "required-index", "exists", "missing")
        self.validate_status_specs()
        self.validate_required_sections()
        self.validate_decision_vocabulary()
        self.validate_legacy_term_scope()
        self.validate_object_index()
        if self.errors:
            for error in self.errors:
                print(f"file={error.file}; violation type={error.violation_type}; expected={error.expected}; actual={error.actual}")
            return 1
        print("State/workflow specification validation passed.")
        return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    return Validator(args.root.resolve()).run()

if __name__ == "__main__":
    sys.exit(main())
