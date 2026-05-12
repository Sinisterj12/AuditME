# Public Import Map

> Status: draft release-preflight map. No private engine code has been imported into this public repo; public `init`, `resume`, and `verify` behavior are being rewritten clean in focused slices.

This document controls what may move from the private implementation into the public AuditME alpha.

The rule is simple: import the smallest public product, not the whole invention lab.

## Summary

The public alpha spine should be mostly rewritten clean, with small implementation patterns extracted only after review. The private implementation is useful, but too much of it carries internal workflow, broad command surface, desktop/fleet concepts, and private operating assumptions that do not belong in `v0.1.0-alpha`.

## Copy As-Is

Nothing is approved for copy-as-is yet.

| Private source | Public target | Why safe | Risks |
| --- | --- | --- | --- |
| None approved | n/a | Public repo needs a clean package contract first | Copying too early can leak private assumptions |

## Extract With Cleanup

| Private source/reference | Public target | Keep | Remove | Risks |
| --- | --- | --- | --- | --- |
| CLI entrypoint patterns | `src/auditme/cli.py` | argument style, command dispatch shape, help text discipline | internal commands, private path defaults, desktop/fleet/sync commands | accidental broad command surface |
| Package metadata shape | `pyproject.toml` | package name, console-script pattern, test tooling concept | private URLs, internal version claims, desktop entrypoint | public metadata promising more than exists |
| State/artifact write patterns | `src/auditme/state.py`, `src/auditme/artifacts.py` | atomic-ish writes, predictable file creation, simple markdown/JSON artifacts | private generated state schemas, private task ledgers, internal sync language | overwriting user files or publishing private state model |
| Test patterns | `tests/` | CLI smoke-test style, temp project setup, expected artifact assertions | tests requiring private repo, private paths, private generated fixtures | false confidence from tests that only pass on one machine |

## Rewrite Clean

| Concept/reference | Public target | Why rewrite | Minimum behavior |
| --- | --- | --- | --- |
| Public CLI spine | `src/auditme/cli.py` | alpha needs only four commands | `init`, `resume`, `verify`, `handoff` with `--project` |
| Project detection | `src/auditme/project.py` | must be path-neutral | resolve explicit project path, detect git root when useful, fail clearly |
| Default config | `src/auditme/config.py` | private config likely knows too much | create/load `auditme.config.json` with safe modes |
| Generated folder contract | `src/auditme/artifacts.py` | public folder must be tiny and reviewable | create only expected `90_AUDITME/` files, never overwrite unrelated files |
| Verification model | `src/auditme/verify.py` | receipts must be honest, not magical | report pass/warn/fail and missing proof plainly |
| Handoff update | `src/auditme/handoff.py` | public handoff should be small | record next move and timestamp without private queue machinery |

## Later

| Feature/file area | Why later | Possible future version |
| --- | --- | --- |
| Desktop UI | Not needed to prove installable CLI | `v0.3.0-beta` or later |
| Multi-agent orchestration | Easy to overpromise and hard to explain first | after CLI contract stabilizes |
| Sync/dropzone workflows | Private-operator workflow, not public alpha | only if generalized safely |
| Rule packs beyond modes | Needs stable config schema first | `v0.2.0-alpha` |
| Migration tooling | Useful after public contract exists | `v0.3.0-beta` |
| CI integrations | Needs stable verify output | `v0.3.0-beta` |

## Never Publish

| Path/pattern | Why never | Notes |
| --- | --- | --- |
| Private generated `90_AUDITME/` state | Contains repo-specific memory and decisions | Public package may generate fresh files only |
| Private task queues and decision ledgers | Personal/internal operating state | Do not use as public fixtures |
| Private sync or relay notes | Cross-agent private coordination | Keep out of public GitHub |
| Secrets, credentials, customer/work data | Security and privacy | Hard block |
| Required personal paths | Not portable | Public behavior must be path-neutral |
| Broad internal command surface | Too much for alpha | Keep four-command CLI |

## Command Dependency Map

### `auditme init --project .`

- CLI entrypoint: `auditme.cli`
- Handler: `auditme.commands.init`
- State/config: project resolution, config defaults, artifact writer
- Artifacts: safe `90_AUDITME/`, resume/task/decision/receipt/config files
- Tests: fresh temp repo, idempotent init, no unrelated overwrite
- Avoid: private fixtures, private path defaults, broad setup wizards

### `auditme resume --project .`

- CLI entrypoint: `auditme.cli`
- Handler: `auditme.commands.resume`
- State/config: project state reader, config loader
- Artifacts: `AUDITME_RESUME.md`, task queue, receipt summary
- Tests: useful output after init, graceful output before init
- Avoid: claiming unavailable context as fact

### `auditme verify --project .`

- CLI entrypoint: `auditme.cli`
- Handler: `auditme.commands.verify`
- State/config: verification config, receipt reader
- Artifacts: receipt summary, missing-proof warnings
- Tests: pass/warn/fail output, nonzero exit only for true blocking failure
- Avoid: treating editable markdown as trusted proof

### `auditme handoff --project . --next-move "..."`

- CLI entrypoint: `auditme.cli`
- Handler: `auditme.commands.handoff`
- State/config: project state reader/writer
- Artifacts: resume/handoff state and timestamped next move
- Tests: next move persisted, no unrelated file mutation
- Avoid: importing private task queue automation

## Public Package Skeleton

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
docs/
  FIRST_5_MINUTES.md
  IMPORT_MAP.md
  SMOKE_TEST_PLAN.md
```

## Release Gate

No code import should happen until this map, the package/install plan, the smoke-test plan, and the beginner guide are reviewed together.
