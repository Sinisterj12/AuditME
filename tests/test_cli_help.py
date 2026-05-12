from __future__ import annotations

import subprocess
import sys
import os
from pathlib import Path

import pytest

import auditme
from auditme.cli import _exit_code_from_system_exit, main

try:
    import tomllib
except ImportError:  # pragma: no cover - exercised on Python 3.10
    import tomli as tomllib


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_package_version_matches_pyproject() -> None:
    pyproject = tomllib.loads((PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert auditme.__version__ == pyproject["project"]["version"]


def test_package_license_matches_root_license() -> None:
    pyproject = tomllib.loads((PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["license"] == "MIT"
    assert pyproject["project"]["license-files"] == ["LICENSE"]
    assert (PROJECT_ROOT / "LICENSE").is_file()


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
    env = dict(os.environ)
    src_path = str(PROJECT_ROOT / "src")
    existing_pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = (
        src_path
        if not existing_pythonpath
        else os.pathsep.join([src_path, existing_pythonpath])
    )

    result = subprocess.run(
        [sys.executable, "-m", "auditme", "--help"],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.returncode == 0
    assert "auditme" in result.stdout


@pytest.mark.parametrize(
    ("system_exit", "expected"),
    [
        (SystemExit(None), 0),
        (SystemExit(2), 2),
        (SystemExit("3"), 3),
        (SystemExit("not-a-number"), 1),
    ],
)
def test_system_exit_codes_are_normalized(system_exit: SystemExit, expected: int) -> None:
    assert _exit_code_from_system_exit(system_exit) == expected
