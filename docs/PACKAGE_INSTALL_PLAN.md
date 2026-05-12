# Package And Install Plan

> Status: release-preflight plan. The public alpha command spine has been rewritten clean in focused slices; no private engine code or private runtime state has been imported.

This plan defines the public packaging target for AuditME `v0.1.0-alpha`.

The goal is not to publish a clever Python package. The goal is to let a stranger install AuditME, run four commands, and see predictable repo-local behavior without knowing anything about the private development repo.

## Package Goal

`v0.1.0-alpha` should ship as a small Python CLI package named `auditme`.

Public install target:

```bash
pipx install .
auditme --help
```

Development target:

```bash
uv sync
uv run auditme --help
```

The package must not require:

- a private development checkout
- private generated `90_AUDITME/` state
- private Google Drive access
- private sync/relay files
- personal local paths

## Recommended Public Layout

```text
pyproject.toml
src/
  auditme/
    __init__.py
    __main__.py
    cli.py
    commands/
      __init__.py
      init.py
      resume.py
      verify.py
      handoff.py
tests/
  test_cli_help.py
  test_init_command.py
  test_resume_command.py
  test_verify_command.py
  test_handoff_command.py
```

Do not add desktop, sync, fleet, lab, update, or orchestration modules to the alpha package.

## `pyproject.toml` Target

Recommended baseline:

```toml
[build-system]
requires = ["setuptools>=77", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "auditme"
version = "0.1.0a0"
description = "Repo-native memory, guardrails, handoff state, and verification receipts for AI-assisted development."
readme = "README.md"
requires-python = ">=3.10"
license = "MIT"
license-files = ["LICENSE"]
authors = [
  { name = "AuditME contributors" }
]
keywords = ["ai", "agents", "cli", "developer-tools", "verification"]
dependencies = []

[project.scripts]
auditme = "auditme.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[project.optional-dependencies]
dev = [
  "pytest>=8",
  "tomli>=2; python_version < '3.11'"
]
```

Notes:

- `version = "0.1.0a0"` keeps the Python package version aligned with an alpha release without pretending it is stable.
- Runtime dependencies should stay empty for the first alpha unless a dependency removes real risk.
- The package license must stay aligned with the root `LICENSE` file before release.

## Python Version

Target:

```text
Python >= 3.10
```

Reasoning:

- broad enough for real users
- modern enough for clean type hints and `pathlib`
- avoids unnecessary compatibility work before the CLI contract is proven

Do not use Python-version-specific features unless tests cover the minimum supported version.

## Console Script

The only public console script for `v0.1.0-alpha` should be:

```toml
[project.scripts]
auditme = "auditme.cli:main"
```

Do not expose:

- `auditme-desktop`
- private maintenance commands
- sync/relay tools
- lab or fleet launchers
- experimental import/migration commands

## Public Alpha Command Surface

The first public CLI should support only:

```bash
auditme init --project .
auditme resume --project .
auditme verify --project .
auditme handoff --project . --next-move "Describe the next safe task"
```

Also required:

```bash
auditme --help
auditme <command> --help
```

Every command must:

- accept `--project`
- resolve paths without private assumptions
- fail with clear messages
- avoid writing outside the target project
- avoid claiming verification passed without proof

## Runtime Dependencies

Allowed for `v0.1.0-alpha`:

- Python standard library

Avoid for `v0.1.0-alpha` unless a concrete blocker appears:

- CLI frameworks such as Click, Typer, or Rich
- schema frameworks such as Pydantic
- background service frameworks
- desktop UI dependencies
- network clients
- AI SDKs
- file watcher libraries

The alpha should prove the workflow before it grows a dependency tree.

## Development Tooling

Use `uv` for local development:

```bash
uv sync
uv run auditme --help
uv run pytest
```

Recommended dev dependencies:

```text
pytest>=8
tomli>=2; python_version < "3.11"
```

Do not require contributors to install the private development repo.

## Install Verification

Development smoke:

```bash
uv sync
uv run auditme --help
uv run auditme init --project ../auditme-smoke-project
uv run auditme resume --project ../auditme-smoke-project
uv run auditme verify --project ../auditme-smoke-project
uv run auditme handoff --project ../auditme-smoke-project --next-move "Continue safely"
```

Package smoke:

```bash
pipx install .
auditme --help
auditme init --project ../auditme-smoke-project
auditme resume --project ../auditme-smoke-project
auditme verify --project ../auditme-smoke-project
auditme handoff --project ../auditme-smoke-project --next-move "Continue safely"
```

Expected:

- package installs without private setup
- console script works outside the source tree
- generated files appear only under the target repo
- no private paths appear in generated output
- `verify` distinguishes `pass`, advisory `warn`, and blocking `fail`
- `verify` warning output is non-blocking in the first alpha; strict CI behavior can come later as an explicit mode

## Code Import Gate

Do not import engine code until these exist in the public repo:

- package/install plan
- import map
- smoke-test plan
- beginner first-run guide
- public-safe package skeleton
- minimum tests for command behavior

Before copying or extracting private implementation code, classify each candidate as:

- `copy`
- `extract`
- `rewrite`
- `later`
- `never`

If a module requires private state, private paths, sync/relay files, desktop UI, or broad internal commands, rewrite it clean or defer it.

## Completed Code Lanes

The first code PR was package skeleton only:

- `pyproject.toml`
- `src/auditme/__init__.py`
- `src/auditme/__main__.py`
- `src/auditme/cli.py`
- basic `auditme --help`
- first CLI help test

The current behavior slices are `auditme init`, `auditme resume`, `auditme verify`, and `auditme handoff`. The generated config includes a small validated mode field: `advisory`, `balanced`, or `strict`; the first alpha treats missing proof as advisory unless required state is broken. No generated `90_AUDITME/` folder should be committed. The folder should only be created inside throwaway test projects or explicit user target projects.

## Release Blockers

Block alpha if:

- `pipx install .` fails
- `uv run auditme --help` fails
- package metadata promises commands that do not exist
- generated files include private state
- commands require a private development checkout
- tests rely on machine-specific filesystem paths
- README claims the package is installable before install smoke passes

## Next Safest Action

Run the full release-preflight pass: clean install smoke, package build, README/docs truth check, and release checklist closure before any official public release.
