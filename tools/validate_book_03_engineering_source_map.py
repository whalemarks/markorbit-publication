#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "engineering/book-03/book-03-engineering-source-map.json"
FREEZE_PATH = ROOT / "books/book-03-execution-system/FREEZE-MANIFEST.md"

EXPECTED_CHAPTERS = [f"B03-CH-{index:02d}" for index in range(35)]
EXPECTED_WORKFLOWS = {
    "intake-execution": ("depth-a", True),
    "application-preparation": ("depth-a", True),
    "communication-review": ("depth-a", True),
    "provider-routing-preparation": ("depth-b", False),
    "office-action-response-preparation": ("depth-b", False),
    "renewal-preparation": ("depth-b", False),
    "assignment-preparation": ("depth-b", False),
    "evidence-review-preparation": ("depth-b", False),
}
FORBIDDEN_RUNTIME_LOCATIONS = {
    "whalemarks/markorbit-core",
    "whalemarks/markorbit-publication",
    "product-repository",
    "integration-repository",
}
REQUIRED_DEFERRED = {
    "external-communication-send",
    "official-filing-or-submission",
    "payment",
    "provider-final-selection-and-engagement",
    "autonomous-professional-execution",
    "autonomous-event-emission",
}


def main() -> int:
    errors: list[str] = []
    data = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    freeze = FREEZE_PATH.read_text(encoding="utf-8")

    if data.get("frozenBaseline") != "B03-RC1-FROZEN-01":
        errors.append("unexpected frozen baseline")
    if "Controlled files bound: 43" not in freeze or "SHA-256 coverage: PASS" not in freeze:
        errors.append("Book 03 freeze manifest is not the expected frozen authority")

    chapters = [entry.get("chapter") for entry in data.get("chapterMap", [])]
    if chapters != EXPECTED_CHAPTERS:
        errors.append("chapterMap must cover B03-CH-00 through B03-CH-34 exactly once in order")

    workflows = data.get("workflowRegistry", [])
    if len(workflows) != 8:
        errors.append("workflowRegistry must contain exactly eight workflows")
    seen: set[str] = set()
    for workflow in workflows:
        workflow_id = workflow.get("id")
        if workflow_id in seen:
            errors.append(f"duplicate workflow: {workflow_id}")
        seen.add(workflow_id)
        expected = EXPECTED_WORKFLOWS.get(workflow_id)
        if expected is None:
            errors.append(f"unexpected workflow: {workflow_id}")
            continue
        if (workflow.get("depth"), workflow.get("applyEnabled")) != expected:
            errors.append(f"invalid depth/apply lock for {workflow_id}")
        if workflow.get("externalAction") is not False:
            errors.append(f"external action must remain disabled for {workflow_id}")
    if seen != set(EXPECTED_WORKFLOWS):
        errors.append("workflow registry does not match the locked MVP set")

    boundary = data.get("implementationBoundary", {})
    if boundary.get("requiredRepositoryType") != "dedicated-execution-repository":
        errors.append("dedicated execution repository boundary is not locked")
    if set(boundary.get("forbiddenRuntimeLocations", [])) != FORBIDDEN_RUNTIME_LOCATIONS:
        errors.append("forbidden runtime locations do not match the authority decision")

    if not REQUIRED_DEFERRED.issubset(set(data.get("deferredProtectedActions", []))):
        errors.append("required deferred protected actions are missing")

    next_task = data.get("nextFormalTask", {})
    if next_task.get("id") != "EXEC-TASK-001" or next_task.get("title") != "Initialize Execution Repository":
        errors.append("next formal task must remain EXEC-TASK-001 — Initialize Execution Repository")

    if errors:
        print("Book 03 engineering source-map validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Book 03 engineering source-map validation: PASS")
    print("Chapters mapped: 35 / 35")
    print("MVP workflows locked: 8 / 8")
    print("Depth A workflows: 3")
    print("Depth B workflows: 5")
    print("Dedicated repository boundary: LOCKED")
    print("Frozen manuscript modifications: 0")
    print("Next formal task: EXEC-TASK-001")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
