from __future__ import annotations

from pathlib import Path

import pytest

from auditme.cli import main


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
