from __future__ import annotations

from pathlib import Path

import pytest

from auditme.cli import main


def test_handoff_records_next_move_in_initialized_project(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "fresh-project"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    task_queue_path = project / "90_AUDITME" / "AUDITME_TASK_QUEUE.md"
    task_queue_before = task_queue_path.read_text(encoding="utf-8")
    capsys.readouterr()

    exit_code = main(
        [
            "handoff",
            "--project",
            str(project),
            "--next-move",
            "Add focused handoff tests",
        ]
    )
    output = capsys.readouterr()

    resume_text = (project / "90_AUDITME" / "AUDITME_RESUME.md").read_text(
        encoding="utf-8"
    )
    assert exit_code == 0
    assert "AuditME Handoff" in output.out
    assert "Next move recorded: Add focused handoff tests" in output.out
    assert "## Handoff" in resume_text
    assert "Next move: Add focused handoff tests" in resume_text
    assert task_queue_path.read_text(encoding="utf-8") == task_queue_before
    assert output.err == ""


def test_resume_outputs_recorded_handoff(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "resume-project"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    assert (
        main(
            [
                "handoff",
                "--project",
                str(project),
                "--next-move",
                "Run the smoke test plan",
            ]
        )
        == 0
    )
    capsys.readouterr()

    assert main(["resume", "--project", str(project)]) == 0
    output = capsys.readouterr()

    assert "## Handoff" in output.out
    assert "Next move: Run the smoke test plan" in output.out


def test_handoff_replaces_existing_handoff_without_losing_other_resume_sections(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "preserve-project"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    resume_path = project / "90_AUDITME" / "AUDITME_RESUME.md"
    resume_path.write_text(
        "\n".join(
            [
                "# AuditME Resume",
                "",
                "Status: initialized",
                "",
                "## Project Summary",
                "",
                "Public-safe summary stays.",
                "",
                "## Current Work",
                "",
                "- Existing work stays.",
                "",
                "## Handoff",
                "",
                "Next move: old task",
                "",
            ]
        ),
        encoding="utf-8",
    )

    assert (
        main(
            [
                "handoff",
                "--project",
                str(project),
                "--next-move",
                "Review release preflight",
            ]
        )
        == 0
    )
    capsys.readouterr()

    resume_text = resume_path.read_text(encoding="utf-8")
    assert "Public-safe summary stays." in resume_text
    assert "- Existing work stays." in resume_text
    assert "Next move: Review release preflight" in resume_text
    assert "old task" not in resume_text


def test_handoff_requires_next_move(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "needs-next-move"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()

    exit_code = main(["handoff", "--project", str(project)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "--next-move" in output.err


def test_handoff_rejects_blank_next_move(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "blank-next-move"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    capsys.readouterr()

    exit_code = main(["handoff", "--project", str(project), "--next-move", "   "])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "next move cannot be blank" in output.err


def test_handoff_reports_clear_error_before_init(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "not-initialized"
    project.mkdir()

    exit_code = main(
        ["handoff", "--project", str(project), "--next-move", "Start from init"]
    )
    output = capsys.readouterr()

    assert exit_code == 2
    assert "AuditME is not initialized" in output.err
    assert not (project / "90_AUDITME").exists()


def test_handoff_reports_clear_error_for_missing_project(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "missing-project"

    exit_code = main(
        ["handoff", "--project", str(project), "--next-move", "Start from init"]
    )
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Project path does not exist" in output.err
    assert not project.exists()


def test_handoff_reports_clear_error_for_missing_resume_artifact(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = tmp_path / "missing-resume"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    resume_path = project / "90_AUDITME" / "AUDITME_RESUME.md"
    resume_path.unlink()
    capsys.readouterr()

    exit_code = main(
        ["handoff", "--project", str(project), "--next-move", "Continue safely"]
    )
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Missing AuditME artifact: 90_AUDITME/AUDITME_RESUME.md" in output.err
