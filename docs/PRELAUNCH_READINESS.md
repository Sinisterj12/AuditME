# AuditME Prelaunch Readiness Snapshot

> Status: release-candidate readiness snapshot. AuditME is still not officially released.

This snapshot records what has been checked before release, without turning the check into a tag, package publication, or launch announcement.

## Current Public Posture

AuditME remains in public coming-soon mode.

The repo may explain the product, show public-safe visuals, document the intended alpha path, and capture release-candidate proof. It should not claim that the official installable alpha has launched until the owner explicitly approves the release.

## Current Product Spine

The visible alpha command path is:

```bash
auditme init --project .
auditme resume --project .
auditme verify --project .
auditme handoff --project . --next-move "Describe the next safe task"
```

The public package metadata exposes only the `auditme` console script and keeps the runtime dependency set empty for the first alpha.

## Latest Local Prelaunch Proof

Latest checked date: 2026-05-23

Proof summary:

| Check | Result |
| --- | --- |
| Unit tests | `uv run pytest -q` passed with 48 tests |
| CLI help | `uv run auditme --help` exposed `init`, `resume`, `verify`, and `handoff` |
| Package build | `uv build` produced wheel and source distribution |
| Development smoke | `init`, `resume`, `verify`, and `handoff` worked in a throwaway project |
| Wheel install smoke | built wheel installed into an isolated virtual environment and ran the four-command path |
| Generated file audit | only expected `90_AUDITME/` files were created |
| Private marker scan | generated smoke output contained no private repo, relay, or personal path markers |
| Public posture check | README and planning docs still describe AuditME as coming soon, not officially released |

## Not A Release

This snapshot does not approve:

- Git tag creation
- GitHub Release creation
- PyPI publication
- public launch announcement
- broad code import from private/internal repositories
- desktop, sync, fleet, or multi-agent orchestration scope

## Remaining Release-Candidate Work

Before an official alpha, finish:

- one final docs-vs-behavior consistency check
- one final package boundary inspection
- security/trust-boundary review of generated memory and receipts
- owner approval for the exact release moment and announcement wording

## Release Decision Rule

If the repo is clean, the package installs, the four-command smoke passes, and the docs still tell the truth, AuditME can be considered ready for release-candidate review.

It still should not be released until the owner explicitly says to release it.
