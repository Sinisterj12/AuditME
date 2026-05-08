from __future__ import annotations

import subprocess
import sys
import tomllib
import os
from pathlib import Path

import pytest

import auditme
from auditme.cli import main


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_package_version_matches_pyproject() -> None:
    pyproject = tomllib.loads((PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert auditme.__version__ == pyproject["project"]["version"]


def test_top_level_help_lists_public_alpha_commands(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["--help"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "auditme" in output
    for command in ("init", "resume", "verify", "handoff"):
        assert command in output
    for private_command in ("auditme-desktop", "handoff-sync", "lab", "rollout-update"):
        assert private_command not in output


def test_each_public_alpha_command_has_help(capsys: pytest.CaptureFixture[str]) -> None:
    for command in ("init", "resume", "verify", "handoff"):
        exit_code = main([command, "--help"])
        output = capsys.readouterr().out

        assert exit_code == 0
        assert "--project" in output


def test_module_execution_shows_help() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "auditme", "--help"],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONPATH": str(PROJECT_ROOT / "src")},
    )

    assert result.returncode == 0
    assert "auditme" in result.stdout
