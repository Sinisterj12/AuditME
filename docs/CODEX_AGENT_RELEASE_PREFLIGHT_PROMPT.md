# CodexSystem Agent Prompt: AuditME Public Release Preflight

Copy this prompt into the CodexSystem agent working in the private/internal AuditME development repo.

---

You are working in the private CodexSystem/AuditME development environment.

Your job is not to publish everything.

Your job is to prepare a clean public-release candidate for the new public repository:

```text
Sinisterj12/AuditME
```

The local public checkout is expected to be:

```text
C:\Projects\AuditME
```

## Mission

Prepare AuditME for public release without leaking private/internal development history, personal local paths, private generated state, or CodexSystem-only assumptions.

AuditME should become a clean, installable, repo-native control layer for AI-assisted development.

Public product promise:

```bash
auditme init
auditme resume
auditme verify
auditme handoff
```

## Hard boundaries

Do not copy the full CodexSystem repo.

Do not copy private generated `90_AUDITME` state from CodexSystem into the public repo.

Do not publish personal local paths as required runtime behavior.

Do not assume `C:\Projects\CodexSystem` exists for public users.

Do not add secrets, tokens, credentials, customer data, private repo memory, or private work notes.

Do not expand scope into shiny features. This is release hardening, not feature invention.

## Required analysis

First inspect the current AuditME implementation and produce a short release-preflight report covering:

1. Minimal file set required for v0.1.0-alpha.
2. Files that must not be copied publicly.
3. Hardcoded private/local path assumptions.
4. Public command readiness for `init`, `resume`, `verify`, and `handoff`.
5. Packaging readiness.
6. Test readiness.
7. Security risks around repo-memory poisoning or unsafe generated files.
8. Recommended first import branch name for public repo.

Do not modify files until this report is produced.

## Desired public architecture

Favor this public architecture:

```text
CLI -> project detection -> state manager -> policy checks -> reporter
```

Desktop UI and advanced multi-agent orchestration are optional later. The CLI must be clean first.

## Public repo target

The public repo currently has launch docs only. Code should be imported only after preflight passes.

Expected public repo docs to align with:

- `README.md`
- `docs/RELEASE_PREFLIGHT.md`
- `docs/ADOPTER_GUIDE.md`
- `docs/ARCHITECTURE.md`
- `docs/ROADMAP.md`
- `docs/CODE_PUBLICATION_PLAN.md`
- `SECURITY.md`
- `CONTRIBUTING.md`

Do not contradict these documents without explaining why.

## v0.1.0-alpha target

Minimum acceptable public release:

- installable Python package
- `auditme --help`
- `auditme init --project .`
- `auditme resume --project .`
- `auditme verify --project .`
- `auditme handoff --project . --next-move "..."`
- default config
- generated `90_AUDITME/` folder
- clear generated-file policy
- tests for command behavior
- clean smoke test from a fresh repo

## Output format

Return:

```markdown
# AuditME Public Release Preflight Report

## Verdict
Ready / Not ready / Ready after fixes

## Minimal v0.1.0-alpha import set
- ...

## Do not publish
- ...

## Required fixes before code import
- ...

## Suggested public branch
`release-preflight/v0.1.0-alpha`

## Smoke test plan
```bash
...
```

## Risks
- ...

## Next safest action
...
```

## Important

Be strict. If something is not ready, say so clearly.

The goal is not to make the repo look impressive. The goal is to make the public release adoptable by people who are not James and do not know the original CodexSystem workflow.
