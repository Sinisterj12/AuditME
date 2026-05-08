# Package And Install Plan

> Status: release-preflight plan. No package source has been imported yet.

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
    project.py
    config.py
    artifacts.py
    verify.py
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
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "auditme"
version = "0.1.0a0"
description = "Repo-native memory, guardrails, handoff state, and verification receipts for AI-assisted development."
readme = "README.md"
requires-python = ">=3.10"
license = { text = "LicenseRef-Pending" }
authors = [
  { name = "AuditME contributors" }
]
keywords = ["ai", "agents", "cli", "developer-tools", "verification"]
dependencies = []

[project.scripts]
auditme = "auditme.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[dependency-groups]
dev = [
  "pytest>=8"
]
```

Notes:

- `version = "0.1.0a0"` keeps the Python package version aligned with an alpha release without pretending it is stable.
- Runtime dependencies should stay empty for the first alpha unless a dependency removes real risk.
- The license field must be updated before publishing reuse rights.

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

Recommended dev dependency:

```text
pytest>=8
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
- `verify` distinguishes `pass`, `warn`, and `fail`

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

## First Code Lane After This Plan

The first code PR should be package skeleton only:

- `pyproject.toml`
- `src/auditme/__init__.py`
- `src/auditme/__main__.py`
- `src/auditme/cli.py`
- basic `auditme --help`
- first CLI help test

No generated `90_AUDITME/` folder should be committed. The folder should only be created inside throwaway test projects when the `init` command exists.

## Release Blockers

Block alpha if:

- `pipx install .` fails
- `uv run auditme --help` fails
- package metadata promises commands that do not exist
- generated files include private state
- commands require a private development checkout
- tests require one local machine path
- README claims the package is installable before install smoke passes

## Next Safest Action

After this plan is reviewed, create a package-skeleton branch. Keep it boring: metadata, console script, help output, and tests before any state-writing command.
