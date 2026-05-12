"""Record public-safe AuditME handoff state."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .init import AUDITME_DIR_NAME


class HandoffError(OSError):
    """Raised when handoff state cannot be recorded safely."""


def _is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def _required_artifact_path(auditme_dir: Path, file_name: str, project_path: Path) -> Path:
    path = auditme_dir / file_name
    if path.is_symlink():
        raise HandoffError(f"Refusing to write through symlink: {path}")
    if not path.is_file():
        raise HandoffError(f"Missing AuditME artifact: {AUDITME_DIR_NAME}/{file_name}")
    if not _is_within(path.resolve(), project_path):
        raise HandoffError(f"Refusing to write outside project: {path}")
    return path


def _load_config(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise HandoffError(f"Invalid AuditME config: {path}") from error
    if not isinstance(data, dict):
        raise HandoffError(f"Invalid AuditME config: {path}")
    return data


def _normalize_next_move(next_move: str | None) -> str:
    normalized = " ".join((next_move or "").split())
    if not normalized:
        raise HandoffError("Handoff next move cannot be blank.")
    return normalized


def _replace_section(markdown: str, heading: str, body: str) -> str:
    lines = markdown.splitlines()
    marker = f"## {heading}".casefold()
    start: int | None = None
    for index, line in enumerate(lines):
        if line.strip().casefold() == marker:
            start = index
            break

    replacement = ["", *body.splitlines()]
    if start is None:
        prefix = markdown.rstrip()
        if prefix:
            return f"{prefix}\n\n## {heading}\n\n{body}\n"
        return f"## {heading}\n\n{body}\n"

    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break

    return "\n".join([*lines[: start + 1], *replacement, *lines[end:]]).rstrip() + "\n"


def render_handoff(project: str | Path, next_move: str | None) -> str:
    """Record and return a public-safe handoff summary for a project."""
    project_path = Path(project).expanduser().resolve()
    if not project_path.exists():
        raise HandoffError(f"Project path does not exist: {project_path}")
    if not project_path.is_dir():
        raise HandoffError(f"Project path is not a directory: {project_path}")

    auditme_dir = project_path / AUDITME_DIR_NAME
    if auditme_dir.is_symlink():
        raise HandoffError(f"Refusing to write through symlink: {auditme_dir}")
    if not auditme_dir.is_dir():
        raise HandoffError(
            f"AuditME is not initialized at {project_path}. "
            f"Run `auditme init --project {project_path}` first."
        )

    config_path = _required_artifact_path(auditme_dir, "auditme.config.json", project_path)
    _load_config(config_path)
    resume_path = _required_artifact_path(auditme_dir, "AUDITME_RESUME.md", project_path)

    normalized_next_move = _normalize_next_move(next_move)
    resume_text = resume_path.read_text(encoding="utf-8")
    updated_resume = _replace_section(
        resume_text,
        "Handoff",
        f"Next move: {normalized_next_move}",
    )
    resume_path.write_text(updated_resume, encoding="utf-8")

    return "\n".join(
        [
            "AuditME Handoff",
            f"Project: {project_path.name}",
            f"AuditME directory: {AUDITME_DIR_NAME}",
            f"Next move recorded: {normalized_next_move}",
            f"Updated: {AUDITME_DIR_NAME}/AUDITME_RESUME.md",
            "",
        ]
    )
