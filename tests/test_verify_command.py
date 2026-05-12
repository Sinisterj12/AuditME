from __future__ import annotations

from pathlib import Path

import pytest

from auditme.cli import main


def test_verify_warns_when_initialized_project_has_no_receipts(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "fresh-project"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()

    exit_code = main(["verify", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 0
    assert output.err == ""
    assert "AuditME Verify" in output.out
    assert "Project: fresh-project" in output.out
    assert "Status: warn" in output.out
    assert "PASS config: valid AuditME config" in output.out
    assert "PASS artifacts: required AuditME artifacts present" in output.out
    assert "WARN receipts: no verification receipts recorded yet" in output.out
    assert "Next action: record verification proof before claiming the work is done" in output.out


def test_verify_passes_when_receipt_file_contains_recorded_proof(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "verified-project"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()
    (project / "90_AUDITME" / "AUDITME_VERIFICATION_RECEIPTS.md").write_text(
        "# AuditME Verification Receipts\n\n"
        "- `uv run pytest`: pass on focused verify lane\n",
        encoding="utf-8",
    )

    exit_code = main(["verify", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 0
    assert "Status: pass" in output.out
    assert "PASS receipts: verification receipts recorded" in output.out
    assert "Next action: continue with the next approved task" in output.out


def test_verify_reports_clear_error_before_init(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "not-initialized"
    project.mkdir()

    exit_code = main(["verify", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Could not verify AuditME" in output.err
    assert "AuditME is not initialized" in output.err
    assert not (project / "90_AUDITME").exists()


def test_verify_reports_clear_error_for_missing_project(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "missing-project"

    exit_code = main(["verify", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Could not verify AuditME" in output.err
    assert "Project path does not exist" in output.err
    assert not project.exists()


def test_verify_reports_clear_error_for_missing_required_artifact(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "missing-artifact"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()
    (project / "90_AUDITME" / "AUDITME_TASK_QUEUE.md").unlink()

    exit_code = main(["verify", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Could not verify AuditME" in output.err
    assert "Missing AuditME artifact" in output.err
    assert "AUDITME_TASK_QUEUE.md" in output.err


def test_verify_reports_clear_error_for_corrupt_config(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "corrupt-config"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()
    (project / "90_AUDITME" / "auditme.config.json").write_text("{", encoding="utf-8")

    exit_code = main(["verify", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Could not verify AuditME" in output.err
    assert "Invalid AuditME config" in output.err
