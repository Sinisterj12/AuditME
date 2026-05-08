from __future__ import annotations

import json
from pathlib import Path

import pytest

from auditme.cli import main


EXPECTED_INIT_FILES = {
    "AUDITME_RESUME.md",
    "AUDITME_TASK_QUEUE.md",
    "AUDITME_DECISION_LEDGER.md",
    "AUDITME_VERIFICATION_RECEIPTS.md",
    "auditme.config.json",
}


def test_init_creates_public_safe_auditme_folder(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = tmp_path / "fresh-project"
    project.mkdir()

    exit_code = main(["init", "--project", str(project)])
    output = capsys.readouterr()

    auditme_dir = project / "90_AUDITME"
    assert exit_code == 0
    assert "Initialized AuditME" in output.out
    assert auditme_dir.is_dir()
    assert {path.name for path in auditme_dir.iterdir()} == EXPECTED_INIT_FILES

    config = json.loads((auditme_dir / "auditme.config.json").read_text(encoding="utf-8"))
    assert config == {
        "schema_version": 1,
        "auditme_dir": "90_AUDITME",
        "project": {"name": "fresh-project"},
        "commands": {
            "init": {"status": "initialized"},
            "resume": {"status": "not_implemented"},
            "verify": {"status": "not_implemented"},
            "handoff": {"status": "not_implemented"},
        },
    }


def test_init_accepts_relative_project_paths(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    project = tmp_path / "relative-project"
    project.mkdir()
    monkeypatch.chdir(tmp_path)

    exit_code = main(["init", "--project", "relative-project"])

    assert exit_code == 0
    assert (project / "90_AUDITME" / "auditme.config.json").is_file()
    assert not (tmp_path / "90_AUDITME").exists()


def test_init_is_idempotent_and_preserves_existing_files(tmp_path: Path) -> None:
    project = tmp_path / "existing-project"
    project.mkdir()
    assert main(["init", "--project", str(project)]) == 0
    resume_path = project / "90_AUDITME" / "AUDITME_RESUME.md"
    resume_path.write_text("# Custom resume\n", encoding="utf-8")

    assert main(["init", "--project", str(project)]) == 0

    assert resume_path.read_text(encoding="utf-8") == "# Custom resume\n"


def test_init_generated_content_has_no_private_markers(tmp_path: Path) -> None:
    project = tmp_path / "public-project"
    project.mkdir()

    assert main(["init", "--project", str(project)]) == 0

    generated_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted((project / "90_AUDITME").iterdir())
        if path.is_file()
    )
    forbidden_markers = (
        "CodexSystem",
        "G:\\My Drive",
        "PRIVATE_RELAY",
        "PRIVATE_SHEET_ID",
    )
    assert all(marker not in generated_text for marker in forbidden_markers)


def test_init_reports_clear_error_when_project_path_is_file(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project_file = tmp_path / "not-a-directory"
    project_file.write_text("not a project directory\n", encoding="utf-8")

    exit_code = main(["init", "--project", str(project_file)])
    output = capsys.readouterr()

    assert exit_code == 2
    assert "Could not initialize AuditME" in output.err
    assert not (tmp_path / "90_AUDITME").exists()
