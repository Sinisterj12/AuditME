# AuditME

![AuditME banner](assets/auditme-banner.svg)

> **Keep the agent. Lose the drift.**

AuditME turns agent chaos into repo truth: durable project memory, scoped next moves, verification receipts, and session context that live with the code instead of disappearing into chat history.

AI agents are getting faster. AuditME is being built for the part that speed does not solve: knowing what is true, what changed, what was proven, and what the next session should do without trusting a fading chat thread.

AuditME is in public preview. This repository is being prepared as the public home for the product, but the official installable release is intentionally not launched yet.

`coming soon` | `AI coding workflow` | `repo-local memory` | `honest verification`

## Coming Soon

AuditME is for builders who use AI agents heavily and need the repo to remember what the chat forgets.

The public launch is being held until the first alpha is clean enough to install, explain, and trust. For now, this repo is the public preview: the product story, brand direction, release boundaries, and planned first workflow.

The release is intentionally suspenseful, not vague: the product spine is visible, the first command path is defined, and the remaining work is about proving the install, tightening the trust model, and making the first alpha feel boringly reliable.

## The Shift

AI coding is moving from one-off prompts to long-running agent work. That creates a new failure mode: the repo can keep compiling while the project truth drifts out of sight.

AuditME is the answer to that drift.

It is not trying to replace the agent. It is trying to give the agent a control layer: memory the repo owns, proof humans can inspect, and handoffs that survive a new chat, a new machine, or a new agent.

## Status

AuditME is not officially released yet.

This repo currently showcases the product direction, public-safe documentation, visual identity, and planned first command path. Release-candidate proof and publication approval are intentionally waiting before a public alpha is tagged or announced.

Watch this repo if you want to follow the public launch.

## Why It Exists

AI coding agents are powerful, but long-running projects drift. A fresh session forgets decisions, scopes creep, proof gets fuzzy, and the repo starts depending on whatever the last chat remembered.

Without AuditME, project memory gets trapped in chat instead of living with the repo.

AuditME gives that work a control layer: a small, repo-local operating surface that tells agents what is true, what is allowed, what proof exists, and what should happen next.

## Without AuditME / With AuditME

| Without AuditME | With AuditME |
| --- | --- |
| Context is scattered across chats. | Project memory lives in repo-local files. |
| New sessions rediscover the same facts. | `auditme resume` gives a copyable starting point. |
| "Done" can mean "the agent sounded confident." | `auditme verify` separates proof, warnings, and failures. |
| Scope depends on prompt discipline. | Guardrails and task context travel with the project. |
| Handoffs are fragile. | The next move is meant to be recorded before the session ends. |

## Planned Command Path

The first public alpha is intended to be intentionally small:

```bash
auditme init --project .
auditme resume --project .
auditme verify --project .
auditme handoff --project . --next-move "Describe the next safe task"
```

These commands describe the target public workflow. Until the alpha release is tagged, treat the repo as a preview of the product and its direction, not as an official installation source.

## What The First Alpha Should Feel Like

The first alpha should feel like a seatbelt for agent-heavy development:

- small enough to understand in one sitting
- strong enough to stop obvious drift
- honest enough to say `warn` when proof is missing
- boring enough that generated files are easy to review
- useful enough that a fresh agent can start with repo truth instead of chat archaeology

## What It Is

AuditME is:

- a repo-native memory and verification layer for AI-assisted development
- a CLI-first workflow for serious builders and small teams
- a way to make agent handoffs, task scope, decisions, and proof easier to inspect
- a product being prepared for a clean public alpha

## What It Is Not

AuditME is not:

- a replacement for a coding agent
- a guarantee that generated code is correct
- a cloud sync system
- a desktop dashboard in the first alpha
- a place to store secrets, customer data, private relay notes, or personal machine paths

## First 5 Minutes, Once Released

A new repo should eventually be able to start with:

```bash
auditme init --project .
auditme resume --project .
auditme verify --project .
auditme handoff --project . --next-move "Describe the next safe task"
```

`init` creates a small public-safe `90_AUDITME/` folder in the target project. `resume` prints useful context for the next agent. `verify` reports honest status: `pass` when proof exists, `warn` when proof is missing or weak, and failure for broken required state. `handoff` records the next safe move in repo-local state.

In the first public alpha, `warn` is expected to be advisory and able to exit successfully. Treat it as "not ready to claim done," not as a broken install.

## Current Status

This repository is not the official release yet. It is the public coming-soon repo for AuditME.

Current state:

- Public repo scaffold and brand direction are live.
- Public-safe docs describe the intended product and first alpha shape.
- Visual assets are present for the README and future launch materials.
- Release packaging and official alpha publication are intentionally waiting.
- Private implementation files, private workflow state, private relay notes, and generated private runtime state are not published here.
- MIT license is in place.

Current prelaunch proof is tracked in [Prelaunch Readiness](docs/PRELAUNCH_READINESS.md). That proof is a readiness signal, not a launch announcement.

What is intentionally not here yet:

- an official release tag
- PyPI or install instructions
- private implementation history
- private generated AuditME state
- customer, work, relay, or personal machine data

## Who It Is For

AuditME is for builders using AI coding agents across real projects: solo operators, small teams, product builders, and engineers who want agents to move fast without losing the thread.

It is especially useful when the cost of drift is high: production apps, customer-facing tools, internal business systems, long-running branches, or repos touched by more than one agent.

If your agents move quickly but your project memory lives in screenshots, scattered chats, and "I think we already did that," AuditME is being built for you.

## Follow The Drop

The next public signals should be visible here before the alpha is released:

- sharper examples of repo-local memory and handoff flow
- clean release-candidate proof from fresh installs
- tighter security and trust-boundary docs
- public-safe visuals that show agent chaos becoming repo truth
- one clear owner-approved moment when coming soon becomes installable

## Release Principles

AuditME should be:

- easy to install
- safe by default
- path-neutral
- honest about verification status
- clear for humans and agents
- useful without private workflow knowledge
- strong enough for serious projects, but small enough to understand quickly

## Docs

Start here:

- [Coming Soon](COMING_SOON.md)
- [First 5 Minutes](docs/FIRST_5_MINUTES.md)
- [Adopter Guide](docs/ADOPTER_GUIDE.md)
- [Release Preflight](docs/RELEASE_PREFLIGHT.md)
- [Prelaunch Readiness Snapshot](docs/PRELAUNCH_READINESS.md)
- [Public Repo Experience](docs/PUBLIC_REPO_EXPERIENCE.md)
- [Smoke Test Plan](docs/SMOKE_TEST_PLAN.md)

Release and implementation planning:

- [Architecture Direction](docs/ARCHITECTURE.md)
- [Roadmap](docs/ROADMAP.md)
- [Productization Plan](docs/PRODUCTIZATION_PLAN.md)
- [Code Publication Plan](docs/CODE_PUBLICATION_PLAN.md)
- [Package And Install Plan](docs/PACKAGE_INSTALL_PLAN.md)
- [Public Import Map](docs/IMPORT_MAP.md)
- [Brand Direction](docs/BRAND_DIRECTION.md)

## License

This repository uses the [MIT License](LICENSE).
