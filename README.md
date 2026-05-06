# AuditME

> **Public alpha coming soon.** AuditME is in release-preflight now: docs are live, the public repo is staged, and the engine is being cleaned for a proper first release.

AuditME is a repo-native control layer for AI-assisted software work.

It was built from the perspective of a hardcore vibe coder: someone who can drive the vision, pressure-test the result, and ship real tools with AI agents, even without pretending to be a traditional software engineer.

That is the point.

Modern AI coding is powerful, but it can also turn into a very confident raccoon with commit access. AuditME exists to keep the raccoon useful.

It keeps durable project memory, handoff context, task scope, verification receipts, and guardrail rules inside the repository instead of relying only on chat history.

AuditME is being prepared for public release. This repository is currently in launch-preflight mode while the engine is cleaned, packaged, documented, and separated from private/internal development history.

## The problem

AI coding agents are powerful, but long-running projects drift.

Common failure modes:

- The agent forgets prior decisions.
- The agent edits outside the intended scope.
- The agent says work is done without proof.
- A new session wastes time rediscovering the repo.
- Multiple agents create conflicting assumptions.
- Project memory lives in chat instead of version control.
- The human operator knows the goal, but the repo does not carry enough truth forward.

AuditME exists to make those problems visible, reviewable, and harder to repeat.

## Why vibe coders need this

Vibe coding is not magic. It is fast human direction plus AI execution.

That speed is the advantage, but it also creates risk:

- too much trust in the last AI response
- too many half-finished branches
- too much context trapped in chat windows
- too many "done" claims without proof
- too much accidental drift from the original idea

AuditME gives the workflow a memory spine.

It helps the human stay in charge while giving the agent enough durable context to work like it has been paying attention. Wild concept.

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

The goal is simple: a developer, builder, or AI agent should be able to enter a repo, run AuditME, and quickly understand what is true, what is allowed, what changed, what proof exists, and what should happen next.

## Current status

This repository is not yet the installable release.

Current phase:

- Public repo scaffold created
- Launch documentation prepared
- Engine code pending release preflight
- Internal/private paths being removed
- Packaging and install flow being finalized
- Security and adopter guidance being written

## Coming soon

The first public target is `v0.1.0-alpha`.

Expected first-release focus:

- Clean Python package install
- `auditme init`
- `auditme resume`
- `auditme verify`
- `auditme handoff`
- Path-neutral project detection
- Safe generated repo-memory files
- Basic config model
- Honest verification reporting

Watch this repo if you want to follow the public release work.

## Who this is for

AuditME is for builders using AI coding agents heavily, especially people working across multiple sessions, branches, repos, or agents.

It is especially useful when the cost of AI drift is high: production apps, customer-facing tools, internal business systems, or long-running projects where context matters.

It is also for hardcore vibe coders who are done apologizing for building with AI and would rather put guardrails around the chaos than pretend the chaos is not there.

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
- [Code Publication Plan](docs/CODE_PUBLICATION_PLAN.md)

## License

License decision is pending before code publication. No reuse rights are granted until a license is added.
