"""Render public-safe AuditME resume context."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from .init import AUDITME_DIR_NAME


class ResumeError(OSError):
    """Raised when resume context cannot be loaded safely."""


def _load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ResumeError(f"Invalid AuditME config: {path}") from error
    if not isinstance(data, dict):
        raise ResumeError(f"Invalid AuditME config: {path}")
    return data


def _detect_branch(project_path: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(project_path), "branch", "--show-current"],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return "unknown"
    branch = result.stdout.strip()
    return branch if result.returncode == 0 and branch else "unknown"


def _extract_section(markdown: str, heading: str) -> str:
    lines = markdown.splitlines()
    marker = f"## {heading}".casefold()
    start: int | None = None
    for index, line in enumerate(lines):
        if line.strip().casefold() == marker:
            start = index + 1
            break
    if start is None:
        return "not recorded yet"

    section_lines: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        section_lines.append(line)
    section = "\n".join(section_lines).strip()
    return section if section else "not recorded yet"


def _strip_title(markdown: str) -> str:
    lines = markdown.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    text = "\n".join(lines).strip()
    return text if text else "not recorded yet"


def render_resume(project: str | Path) -> str:
    """Return copyable resume context for an initialized project."""
    project_path = Path(project).expanduser().resolve()
    if not project_path.exists():
        raise ResumeError(f"Project path does not exist: {project_path}")
    if not project_path.is_dir():
        raise ResumeError(f"Project path is not a directory: {project_path}")

    auditme_dir = project_path / AUDITME_DIR_NAME
    config_path = auditme_dir / "auditme.config.json"
    if not auditme_dir.is_dir() or not config_path.is_file():
        raise ResumeError(
            f"AuditME is not initialized at {project_path}. "
            f"Run `auditme init --project {project_path}` first."
        )

    config = _load_json(config_path)
    project_config = config.get("project", {})
    project_name = (
        project_config.get("name")
        if isinstance(project_config, dict) and isinstance(project_config.get("name"), str)
        else project_path.name
    )

    resume_text = (auditme_dir / "AUDITME_RESUME.md").read_text(encoding="utf-8")
    receipt_text = (auditme_dir / "AUDITME_VERIFICATION_RECEIPTS.md").read_text(
        encoding="utf-8"
    )

    return "\n".join(
        [
            "AuditME Resume",
            f"Project: {project_name}",
            f"Branch: {_detect_branch(project_path)}",
            f"AuditME directory: {AUDITME_DIR_NAME}",
            "",
            "## Project Summary",
            _extract_section(resume_text, "Project Summary"),
            "",
            "## Current Work",
            _extract_section(resume_text, "Current Work"),
            "",
            "## Recent Verification",
            _strip_title(receipt_text),
            "",
            "## Handoff",
            _extract_section(resume_text, "Handoff"),
            "",
        ]
    )
