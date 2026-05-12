"""Initialize public-safe AuditME repo artifacts."""

from __future__ import annotations

import json
from pathlib import Path


AUDITME_DIR_NAME = "90_AUDITME"

DEFAULT_MARKDOWN_FILES = {
    "AUDITME_RESUME.md": """# AuditME Resume

Status: initialized

## Project Summary

Describe this project in public-safe terms.

## Current Work

- Next approved task: not recorded yet
- Allowed write scope: not recorded yet
- Stop conditions: not recorded yet

## Handoff

Run `auditme handoff --project . --next-move "Describe the next safe task"` after meaningful work.
""",
    "AUDITME_TASK_QUEUE.md": """# AuditME Task Queue

No approved tasks recorded yet.

Add task scope deliberately. Do not use this file for secrets, credentials, customer data, or private runtime state.
""",
    "AUDITME_DECISION_LEDGER.md": """# AuditME Decision Ledger

No decisions recorded yet.

Record durable project decisions here when they affect future agent behavior.
""",
    "AUDITME_VERIFICATION_RECEIPTS.md": """# AuditME Verification Receipts

No verification receipts recorded yet.

Record proof here only after checks actually run.
""",
}


def _is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def _validate_safe_target(target: Path, project_path: Path) -> None:
    if target.is_symlink():
        raise OSError(f"Refusing to write through symlink: {target}")
    if not _is_within(target.resolve(), project_path):
        raise OSError(f"Refusing to write outside project: {target}")


def _default_config(project_path: Path) -> dict[str, object]:
    return {
        "schema_version": 1,
        "auditme_dir": AUDITME_DIR_NAME,
        "project": {"name": project_path.name},
        "commands": {
            "init": {"status": "initialized"},
            "resume": {"status": "available"},
            "verify": {"status": "available"},
            "handoff": {"status": "available"},
        },
    }


def initialize_project(project: str | Path) -> Path:
    """Create the public-safe AuditME folder in a target project."""
    project_path = Path(project).expanduser().resolve()
    project_path.mkdir(parents=True, exist_ok=True)

    auditme_dir = project_path / AUDITME_DIR_NAME
    _validate_safe_target(auditme_dir, project_path)
    auditme_dir.mkdir(exist_ok=True)

    file_targets = [auditme_dir / file_name for file_name in DEFAULT_MARKDOWN_FILES]
    config_path = auditme_dir / "auditme.config.json"
    for target in [*file_targets, config_path]:
        _validate_safe_target(target, project_path)

    for file_name, contents in DEFAULT_MARKDOWN_FILES.items():
        target = auditme_dir / file_name
        if not target.exists():
            target.write_text(contents, encoding="utf-8")

    if not config_path.exists():
        config_path.write_text(
            json.dumps(_default_config(project_path), indent=2) + "\n",
            encoding="utf-8",
        )

    return auditme_dir
