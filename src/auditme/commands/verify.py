"""Verify public-safe AuditME repo artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .init import AUDITME_DIR_NAME


REQUIRED_ARTIFACTS = (
    "AUDITME_RESUME.md",
    "AUDITME_TASK_QUEUE.md",
    "AUDITME_DECISION_LEDGER.md",
    "AUDITME_VERIFICATION_RECEIPTS.md",
    "auditme.config.json",
)


class VerifyError(OSError):
    """Raised when AuditME verification cannot run safely."""


def _required_artifact_path(auditme_dir: Path, file_name: str) -> Path:
    """Return a required artifact path or raise a clear verification error."""
    path = auditme_dir / file_name
    if not path.is_file():
        raise VerifyError(f"Missing AuditME artifact: {AUDITME_DIR_NAME}/{file_name}")
    return path


def _load_config(path: Path) -> dict[str, Any]:
    """Load an AuditME config file as a JSON object."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise VerifyError(f"Invalid AuditME config: {path}") from error
    if not isinstance(data, dict):
        raise VerifyError(f"Invalid AuditME config: {path}")
    return data


def _validate_config(config: dict[str, Any]) -> None:
    """Validate the minimum public alpha config contract."""
    if config.get("schema_version") != 1:
        raise VerifyError("Invalid AuditME config: schema_version must be 1")
    if config.get("auditme_dir") != AUDITME_DIR_NAME:
        raise VerifyError(f"Invalid AuditME config: auditme_dir must be {AUDITME_DIR_NAME}")
    project = config.get("project")
    if not isinstance(project, dict):
        raise VerifyError("Invalid AuditME config: project must be an object")
    name = project.get("name")
    if not isinstance(name, str) or not name.strip():
        raise VerifyError("Invalid AuditME config: project.name must be a non-empty string")
    commands = config.get("commands")
    if not isinstance(commands, dict):
        raise VerifyError("Invalid AuditME config: commands must be an object")
    for command in ("init", "resume", "verify", "handoff"):
        command_config = commands.get(command)
        if not isinstance(command_config, dict) or not isinstance(command_config.get("status"), str):
            raise VerifyError(f"Invalid AuditME config: commands.{command}.status is required")


def _has_recorded_receipt(receipts_text: str) -> bool:
    """Return whether the receipts file contains proof beyond the template text."""
    ignored_lines = {
        "# auditme verification receipts",
        "no verification receipts recorded yet.",
        "record proof here only after checks actually run.",
    }
    for line in receipts_text.splitlines():
        normalized = line.strip().casefold()
        if normalized and normalized not in ignored_lines:
            return True
    return False


def render_verify(project: str | Path) -> str:
    """Return an honest verification report for an initialized project."""
    project_path = Path(project).expanduser().resolve()
    if not project_path.exists():
        raise VerifyError(f"Project path does not exist: {project_path}")
    if not project_path.is_dir():
        raise VerifyError(f"Project path is not a directory: {project_path}")

    auditme_dir = project_path / AUDITME_DIR_NAME
    if not auditme_dir.is_dir():
        raise VerifyError(
            f"AuditME is not initialized at {project_path}. "
            f"Run `auditme init --project {project_path}` first."
        )

    artifact_paths = {
        file_name: _required_artifact_path(auditme_dir, file_name)
        for file_name in REQUIRED_ARTIFACTS
    }
    config = _load_config(artifact_paths["auditme.config.json"])
    _validate_config(config)

    receipt_text = artifact_paths["AUDITME_VERIFICATION_RECEIPTS.md"].read_text(
        encoding="utf-8"
    )
    has_receipts = _has_recorded_receipt(receipt_text)
    status = "pass" if has_receipts else "warn"
    receipt_line = (
        "PASS receipts: verification receipts recorded"
        if has_receipts
        else "WARN receipts: no verification receipts recorded yet"
    )
    next_action = (
        "continue with the next approved task"
        if has_receipts
        else "record verification proof before claiming the work is done"
    )

    return "\n".join(
        [
            "AuditME Verify",
            f"Project: {project_path.name}",
            f"AuditME directory: {AUDITME_DIR_NAME}",
            f"Status: {status}",
            "",
            "PASS config: valid AuditME config",
            "PASS artifacts: required AuditME artifacts present",
            receipt_line,
            "",
            f"Next action: {next_action}",
            "",
        ]
    )
