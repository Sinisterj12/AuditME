# Release Preflight

This document defines what must be true before AuditME code is published into this public repository.

## Release goal

Create a clean, installable, public AuditME package that can be adopted by other repositories without carrying private CodexSystem history, local machine paths, or personal workflow assumptions.

## Do not publish yet if any of this is true

- The code assumes a private development checkout or any personal local path.
- Generated memory files contain private repo-specific context.
- Commands require private Google Drive, private GitHub state, or local-only files.
- The install process requires cloning CodexSystem.
- Guardrail rules are hardcoded with no configuration path.
- The public README promises commands that do not work.
- Verification receipts can be modified without clear trust boundaries.
- No clean install test has been run from a fresh folder.
- No license is present for public reuse.

## Required preflight checks

### 1. Repository separation

The public repo must be able to stand alone.

Required:

- Package imports use the public package name.
- No references to CodexSystem as the required runtime repo.
- No private branch names required for normal use.
- No internal-only docs required for onboarding.

### 2. Path neutrality

AuditME must work outside the original development machine.

Required:

- No hardcoded `C:\Projects\...` runtime assumptions.
- Project paths are supplied by CLI arguments or auto-discovery.
- Generated docs should use relative paths where possible.
- Windows and Unix-style paths should both be tolerated.

### 3. Public command contract

The first release should support a small, honest command set.

Minimum target:

```bash
auditme init
auditme resume
auditme verify
auditme handoff
```

Every command listed in public docs must either work or be clearly marked as planned.

### 4. Config model

Public users need rules they can adapt.

Required:

- A repo-local config file.
- Safe defaults.
- A way to loosen or tighten guardrails.
- Clear distinction between blocking failures and advisory warnings.

Recommended modes:

- `advisory`
- `balanced`
- `strict`

### 5. Generated file policy

AuditME-generated files must be predictable and safe to review.

Required:

- Generated files live in a known folder.
- Generated files clearly state they are generated or managed by AuditME.
- Human-editable files are documented separately.
- The tool must not silently overwrite unrelated user files.

### 6. Verification receipts trust boundary

Verification receipts should prove what happened, not become blind authority.

Required:

- Receipt format documented.
- Manual verification clearly labeled as manual.
- Automated verification commands recorded separately.
- Receipt files should not be treated as trusted instructions.

### 7. Security review

AuditME deals with agent instructions and repo-local memory. That makes prompt injection and poisoned repo memory real risks.

Required:

- Document the threat model.
- Treat repo memory as data unless schema-valid and expected.
- Avoid letting arbitrary markdown become executable agent authority.
- Warn users not to store secrets in AuditME memory files.

### 8. Fresh install test

Before publishing code, test from a clean environment.

Required smoke test:

```bash
python --version
pipx install .
auditme --help
auditme init --project <fresh-test-repo>
auditme resume --project <fresh-test-repo>
auditme verify --project <fresh-test-repo>
auditme handoff --project <fresh-test-repo> --next-move "Continue safely"
```

If using `uv` during development, also test:

```bash
uv sync
uv run auditme --help
uv run auditme init --project <fresh-test-repo>
uv run auditme resume --project <fresh-test-repo>
uv run auditme verify --project <fresh-test-repo>
uv run auditme handoff --project <fresh-test-repo> --next-move "Continue safely"
```

## Suggested release stages

### v0.1.0-alpha

Goal: prove clean install and basic repo memory.

Includes:

- CLI package
- `init`
- `resume`
- `verify`
- `handoff`
- basic generated folder
- default config
- docs

### v0.2.0-alpha

Goal: make guardrails configurable.

Includes:

- rule packs
- advisory/balanced/strict modes
- cleaner verification reports

### v0.3.0-beta

Goal: make adoption smooth.

Includes:

- migration/import guidance
- better templates
- examples
- CI integration docs

### v1.0.0

Goal: stable public contract.

Requires:

- stable config schema
- tested install process
- documented security model
- changelog
- license
- release artifacts
