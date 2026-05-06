# AuditME v0.1.0-alpha Release Preflight Report Template

Use this template for the read-first release preflight review before importing or mutating production code in the public AuditME repository.

## Operating rule

This is a repo-switch operation.

The active target repo is:

```text
C:\Projects\AuditME
```

The public GitHub repo is:

```text
Sinisterj12/AuditME
```

Do not treat this as ordinary CodexSystem work. Any cross-repo reference must be explicit, read-first, and intentionally targeted.

## Verdict

Choose one:

- `Ready`
- `Ready after fixes`
- `Not ready`

Required answer:

```text
Verdict: <Ready / Ready after fixes / Not ready>
Reason: <one short paragraph>
Confidence: <High / Medium / Low>
```

## Current repo context

```text
Active repo path:
Active branch:
Git status summary:
Public repo initialized: yes/no
Code present in public repo: yes/no
Docs present in public repo: yes/no
```

## What AuditME currently is

Explain the current private/internal implementation in plain English.

Required fields:

```text
Core product:
Primary user:
Primary pain solved:
Current strongest capability:
Current riskiest assumption:
```

## What makes AuditME valuable

Be direct. No hype fluff.

Answer:

- What problem does this solve that normal AI coding tools do not solve well?
- Why would another vibe coder or AI-heavy builder care?
- What is the minimum useful version of this product?

## What could confuse public users

List anything that feels:

- too personal
- too internal
- too CodexSystem-specific
- too Windows-path-specific
- too magical
- too hard to explain
- too tied to one developer's workflow

Use this format:

| Concern | Why it confuses users | Fix before public release? |
|---|---|---|
|  |  | yes/no |

## Mandatory Do Not Publish checklist

Mark each item `PASS`, `FAIL`, or `NEEDS REVIEW`.

| Exclusion | Status | Notes |
|---|---:|---|
| Private generated `90_AUDITME` runtime state from CodexSystem is not copied |  |  |
| Private task queues are not copied |  |  |
| Private decision ledgers are not copied |  |  |
| Personal local paths such as `C:\Projects\CodexSystem` are not required public behavior |  |  |
| Sync notes / private operator notes are not copied |  |  |
| Secret-bearing state is not copied |  |  |
| Customer data or work data is not copied |  |  |
| Private branch history is not imported wholesale |  |  |
| Experimental junk is not copied into public release |  |  |
| README promises only commands that will actually exist or are clearly marked planned |  |  |

## Minimal v0.1.0-alpha import set

List the exact folders/files/modules that should be imported first.

Use this format:

| Source path | Public target path | Why needed | Safe to publish now? |
|---|---|---|---:|
|  |  |  | yes/no |

Do not include optional or shiny features here.

The first alpha should focus on:

- installable Python package
- CLI entrypoint
- project detection
- config defaults
- generated folder creation
- `auditme init`
- `auditme resume`
- `auditme verify`
- `auditme handoff`
- basic tests

## Do not publish

List exact files/folders/modules/docs/state that should not be published.

Use this format:

| Path or pattern | Why excluded | Future public equivalent? |
|---|---|---|
|  |  |  |

## Required fixes before code import

Grade each area.

Status options:

- `PASS`
- `FIX BEFORE IMPORT`
- `CAN FIX AFTER ALPHA`
- `BLOCKER`

| Area | Status | Required fix | Owner suggestion |
|---|---:|---|---|
| Path neutrality |  |  |  |
| Package naming |  |  |  |
| Install flow |  |  |  |
| CLI command accuracy |  |  |  |
| Config model |  |  |  |
| Generated file safety |  |  |  |
| Verification receipt trust boundary |  |  |  |
| Security docs alignment |  |  |  |
| Tests |  |  |  |
| README accuracy |  |  |  |

## Public command readiness

Review each exported public command.

| Command | Ready now? | Imports/modules used | Exit behavior known? | Help text accurate? | Notes |
|---|---:|---|---:|---:|---|
| `auditme init` |  |  |  |  |  |
| `auditme resume` |  |  |  |  |  |
| `auditme verify` |  |  |  |  |  |
| `auditme handoff` |  |  |  |  |  |

## Dependency map

For each exported public command, list the exact module/function dependency chain.

Example format:

```text
auditme init
- CLI entrypoint: <module:function>
- Parser/handler: <module:function>
- Project detection: <module:function>
- State writes: <module:function>
- Report output: <module:function>
- External dependencies: <packages>
```

Required commands:

```text
auditme init
auditme resume
auditme verify
auditme handoff
```

## Packaging readiness

Answer:

```text
Package manager target: pip / pipx / uv / undecided
Python versions supported:
Console script entrypoint:
Current pyproject status:
Fresh install tested: yes/no
Editable install tested: yes/no
Known packaging blockers:
```

## Security risks

Review at minimum:

- repo-memory poisoning
- prompt injection through markdown
- false verification receipts
- generated files overwriting user files
- secrets accidentally stored in AuditME memory
- arbitrary path writes
- unsafe trust in generated state

Use this format:

| Risk | Severity | Current mitigation | Required mitigation before alpha |
|---|---:|---|---|
|  | low/medium/high |  |  |

## Smoke-run command block

Provide exact commands and expected results.

Include:

1. Fresh clone
2. Install
3. `auditme --help`
4. `auditme init`
5. `auditme verify --help`
6. `auditme handoff --help`

Template:

```powershell
# Fresh clone
cd C:\Projects
git clone https://github.com/Sinisterj12/AuditME.git AuditME-smoke
cd C:\Projects\AuditME-smoke

# Install
uv sync
# Expected exit code: 0
# Expected output contains: <fill in>

# CLI help
uv run auditme --help
# Expected exit code: 0
# Expected output contains: <fill in>

# Init
uv run auditme init --project .
# Expected exit code: 0
# Expected created paths: <fill in>

# Verify help
uv run auditme verify --help
# Expected exit code: 0
# Expected output contains: <fill in>

# Handoff help
uv run auditme handoff --help
# Expected exit code: 0
# Expected output contains: <fill in>
```

Also provide a `pipx` version if packaging is ready:

```powershell
pipx install .
auditme --help
auditme init --project .
auditme verify --help
auditme handoff --help
```

## README and positioning review

Current positioning:

AuditME is professional, but openly built from a hardcore vibe-coder workflow.

Review:

```text
Professional enough? yes/no
Too much humor? yes/no
Vibe coder positioning strong? yes/no
Could scare traditional developers? yes/no
Recommended adjustment:
```

## Recommended public branch

Suggested default:

```text
release-preflight/v0.1.0-alpha
```

Confirm or propose a better branch.

## Final recommendation

Choose one:

```text
Proceed with code import after listed fixes.
Do not import code yet; fix blockers first.
Import only docs/templates now; code later.
```

## Next safest action

Give one concrete next action for the human operator.

No vague endings. No “let me know.”
