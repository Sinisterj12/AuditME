# AuditME

AuditME is a repo-native control layer for AI-assisted software work.

It helps coding agents stay aligned with the real project state by keeping durable project memory, handoff context, task scope, verification receipts, and guardrail rules inside the repository instead of relying only on chat history.

AuditME is being prepared for public release. The public repository is currently in launch-preflight mode while the engine is cleaned, packaged, documented, and separated from private/internal development history.

## The problem

AI coding agents are powerful, but long-running projects drift.

Common failure modes:

- The agent forgets prior decisions.
- The agent edits outside the intended scope.
- The agent says work is done without proof.
- A new session wastes time rediscovering the repo.
- Multiple agents create conflicting assumptions.
- Project memory lives in chat instead of version control.

AuditME exists to make those problems visible, reviewable, and harder to repeat.

## What AuditME provides

Planned public release capabilities:

- Repo-local project memory
- Agent resume and handoff files
- Approved task queues
- Verification receipt tracking
- Guardrails for unsafe or lazy AI changes
- Configurable rule packs
- CLI-first workflow
- Optional desktop visibility layer
- Release and preflight checks for AI-assisted repos

## Intended workflow

The public workflow is being designed around a small command set:

```bash
auditme init
auditme resume
auditme verify
auditme handoff
```

The goal is simple: a developer or AI agent should be able to enter a repo, run AuditME, and quickly understand what is true, what is allowed, what changed, and what proof exists.

## Current status

This repository is not yet the installable release.

Current phase:

- Public repo scaffold created
- Launch documentation being prepared
- Engine code pending release preflight
- Internal/private paths being removed
- Packaging and install flow being finalized
- Security and adopter guidance being written

## Who this is for

AuditME is for builders using AI coding agents heavily, especially people working across multiple sessions, branches, repos, or agents.

It is especially useful when the cost of AI drift is high: production apps, customer-facing tools, internal business systems, or long-running projects where context matters.

## Public release principles

AuditME should be:

- Easy to install
- Safe by default
- Configurable per repo
- Honest about verification status
- Clear for humans and agents
- Useful without requiring private workflow knowledge
- Strong enough for serious projects, but simple enough for solo builders

## Repository state

This repo currently contains launch scaffolding only. The production code will be added after release preflight passes.

See:

- [Release Preflight](docs/RELEASE_PREFLIGHT.md)
- [Adopter Guide](docs/ADOPTER_GUIDE.md)
- [Architecture Direction](docs/ARCHITECTURE.md)
- [Roadmap](docs/ROADMAP.md)

## License

License decision is pending before code publication. No reuse rights are granted until a license is added.
