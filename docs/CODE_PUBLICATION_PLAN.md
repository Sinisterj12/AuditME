# Code Publication Plan

This plan defines how code should move from the private/internal AuditME development repo into the public AuditME release repo.

## Goal

Publish only the clean, reusable AuditME product code.

Do not copy private repo history, personal workflow state, machine-specific paths, or internal-only generated memory into the public release.

## Source repo role

The private CodexSystem repo remains the invention and dogfood lab.

It may contain:

- experimental branches
- private generated memory
- personal paths
- internal task queues
- rough agent work
- unreleased feature trials

That is expected. Do not expose that entire history publicly.

## Public repo role

The public AuditME repo should contain:

- clean package source
- public docs
- public tests
- public examples
- release notes
- security policy
- contribution guide

It should not require knowledge of CodexSystem to be useful.

## Recommended migration method

Use a clean copy/import, not a full git history transfer.

Recommended steps:

1. Identify the minimal package files required for public v0.1.0-alpha.
2. Copy only those files into a clean local `C:\Projects\AuditME` checkout.
3. Rename or normalize package/module references if needed.
4. Remove private paths and internal repo assumptions.
5. Add public tests.
6. Run smoke tests from a fresh folder.
7. Commit to a feature branch in the public repo.
8. Open a pull request into `main`.
9. Merge only after release preflight passes.

## First code import scope

Target only the minimum useful product:

- package metadata
- CLI entrypoint
- project detection
- state manager
- config defaults
- init command
- resume command
- verify command
- handoff command
- tests for public command behavior

Avoid importing:

- private generated `90_AUDITME` state
- local-only launch scripts
- private path references
- personal branch history
- desktop UI unless isolated and optional
- experimental multi-agent features

## Branch naming

Use clean public branch names:

```text
release-preflight/v0.1.0-alpha
feature/init-command
feature/public-config-schema
fix/path-neutrality
```

## Success standard

A stranger should be able to clone the public repo, install the package, run `auditme init`, and understand what happened without knowing anything about the original private repo.
