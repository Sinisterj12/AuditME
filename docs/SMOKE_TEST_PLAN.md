# Smoke Test Plan

> Status: planned verification. These tests become executable after the public package skeleton exists.

AuditME `v0.1.0-alpha` should not ship because the docs sound good. It should ship because a clean install and first-run path work in a fresh repo.

## Test Environments

Minimum before alpha:

- Windows fresh folder
- Python supported by package metadata
- `uv` development path
- clean Git checkout of public AuditME repo

Recommended before wider adoption:

- macOS or Linux fresh folder
- `pipx install .`
- GitHub Actions smoke job

## Fresh Repo Setup

Create a throwaway project that has no private AuditME state:

```bash
mkdir auditme-smoke-project
cd auditme-smoke-project
git init
echo "# Smoke Project" > README.md
git add README.md
git commit -m "initial smoke project"
```

The smoke project must not contain copied private generated files.

## Development Install Smoke

From the public AuditME repo:

```bash
uv sync
uv run auditme --help
uv run auditme init --project ../auditme-smoke-project
uv run auditme resume --project ../auditme-smoke-project
uv run auditme verify --project ../auditme-smoke-project
uv run auditme handoff --project ../auditme-smoke-project --next-move "Add a tiny test"
```

Expected:

- help output lists only public alpha commands
- init creates only expected files
- resume output is useful and honest
- verify reports pass/warn/fail clearly
- handoff records the next move without touching unrelated files

## Package Install Smoke

From a clean checkout:

```bash
pipx install .
auditme --help
auditme init --project ../auditme-smoke-project
auditme resume --project ../auditme-smoke-project
auditme verify --project ../auditme-smoke-project
auditme handoff --project ../auditme-smoke-project --next-move "Continue safely"
```

Expected:

- console script works outside the source tree
- no command requires the private implementation repo
- no command requires a private Google Drive folder
- no command requires a personal machine path

## Generated File Audit

After `auditme init`, inspect:

```text
90_AUDITME/
  AUDITME_RESUME.md
  AUDITME_TASK_QUEUE.md
  AUDITME_DECISION_LEDGER.md
  AUDITME_VERIFICATION_RECEIPTS.md
  auditme.config.json
```

Required checks:

- files are predictable
- files explain their purpose
- config is valid JSON
- rerunning init is idempotent
- unrelated files are untouched
- generated content contains no private paths or private project names

## Failure Smoke

Run commands in bad states:

```bash
auditme resume --project missing-folder
auditme verify --project missing-folder
auditme handoff --project . --next-move ""
```

Expected:

- errors are clear
- exits are honest
- no partial state is created on invalid input

## Release Blockers

Block alpha if:

- README promises a command that does not work
- install requires private CodexSystem code
- smoke output contains private paths
- init overwrites unrelated files
- verify reports success without proof
- generated files include private state or relay content
- tests pass only on one local machine

## Evidence To Capture

Before tagging alpha, save concise verification evidence in the release PR:

- install command used
- `auditme --help` output summary
- generated file tree
- command pass/warn/fail summary
- failing or skipped checks with reason

No giant terminal dumps. Receipts should prove the path without burying the reviewer.
