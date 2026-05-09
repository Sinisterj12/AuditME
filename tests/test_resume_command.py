from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from auditme.cli import main
from auditme.commands.resume import _detect_branch


def test_resume_outputs_initialized_project_context(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "fresh-project"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()

    exit_code = main(["resume", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 0
    assert "AuditME Resume" in output.out
    assert "Project: fresh-project" in output.out
    assert "Branch: unknown" in output.out
    assert "Next approved task: not recorded yet" in output.out
    assert "Allowed write scope: not recorded yet" in output.out
    assert "Stop conditions: not recorded yet" in output.out
    assert "No verification receipts recorded yet." in output.out
    assert output.err == ""


def test_resume_reads_updated_public_artifacts(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "updated-project"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()
    auditme_dir = project / "90_AUDITME"
    (auditme_dir / "AUDITME_RESUME.md").write_text(
        "# AuditME Resume\n\n"
        "## Project Summary\n\n"
        "Public package release repo.\n\n"
        "## Current Work\n\n"
        "- Next approved task: implement resume\n"
        "- Allowed write scope: src/auditme and tests\n"
        "- Stop conditions: private state appears\n",
        encoding="utf-8",
    )
    (auditme_dir / "AUDITME_VERIFICATION_RECEIPTS.md").write_text(
        "# AuditME Verification Receipts\n\n"
        "- `uv run pytest`: pending for resume lane\n",
        encoding="utf-8",
    )

    exit_code = main(["resume", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 0
    assert "Public package release repo." in output.out
    assert "Next approved task: implement resume" in output.out
    assert "Allowed write scope: src/auditme and tests" in output.out
    assert "Stop conditions: private state appears" in output.out
    assert "`uv run pytest`: pending for resume lane" in output.out


def test_resume_reports_clear_error_before_init(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "not-initialized"
    project.mkdir()

    exit_code = main(["resume", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "AuditME is not initialized" in output.err
    assert "Run `auditme init --project" in output.err
    assert not (project / "90_AUDITME").exists()


def test_resume_reports_clear_error_for_missing_project(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "missing-project"

    exit_code = main(["resume", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Could not resume AuditME" in output.err
    assert "Project path does not exist" in output.err
    assert not project.exists()


def test_resume_reports_clear_error_when_project_path_is_file(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project_file = tmp_path / "not-a-directory"
    project_file.write_text("not a project directory\n", encoding="utf-8")

    exit_code = main(["resume", "--project", str(project_file)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Could not resume AuditME" in output.err
    assert "Project path is not a directory" in output.err


def test_resume_reports_clear_error_for_missing_resume_artifact(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "missing-resume"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()
    (project / "90_AUDITME" / "AUDITME_RESUME.md").unlink()

    exit_code = main(["resume", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Missing AuditME artifact" in output.err
    assert "AUDITME_RESUME.md" in output.err


def test_resume_reports_clear_error_for_missing_verification_artifact(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "missing-receipts"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()
    (project / "90_AUDITME" / "AUDITME_VERIFICATION_RECEIPTS.md").unlink()

    exit_code = main(["resume", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Missing AuditME artifact" in output.err
    assert "AUDITME_VERIFICATION_RECEIPTS.md" in output.err


def test_resume_reports_clear_error_for_corrupt_config(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "corrupt-config"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()
    (project / "90_AUDITME" / "auditme.config.json").write_text("{", encoding="utf-8")

    exit_code = main(["resume", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Invalid AuditME config" in output.err


def test_resume_reports_clear_error_for_missing_config(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "missing-config"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()
    (project / "90_AUDITME" / "auditme.config.json").unlink()

    exit_code = main(["resume", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Missing AuditME artifact" in output.err
    assert "auditme.config.json" in output.err


def test_branch_detection_uses_timeout(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    calls: list[float | int | None] = []

    def fake_run(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
        calls.append(kwargs.get("timeout"))
        return subprocess.CompletedProcess(args=args, returncode=0, stdout="main\n")

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert _detect_branch(tmp_path) == "main"
    assert calls == [2]


def test_branch_detection_returns_unknown_on_timeout(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    def fake_run(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
        raise subprocess.TimeoutExpired(cmd="git", timeout=kwargs.get("timeout"))

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert _detect_branch(tmp_path) == "unknown"
