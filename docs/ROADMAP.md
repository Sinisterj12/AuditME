# Roadmap

This roadmap is intentionally conservative. AuditME should become public by getting smaller, clearer, and easier to install before it gets bigger.

## Current public posture

AuditME is in coming-soon mode.

This repo should make the product idea clear, credible, and public-safe before the official installable release is launched. The live release code, package proof, tag, release notes, and publication path can wait until the remaining private product work is ready.

## Phase 0: Public preview scaffold

Status: complete

Goals:

- Create public repository
- Add launch-facing README
- Add public-safe coming-soon framing
- Add release preflight checklist
- Add adopter guide
- Add architecture direction
- Add roadmap
- Add security notes
- Do not publish private engine code or private runtime state

Success standard:

The public repo clearly explains what AuditME is, why it matters, and what must happen before code publication.

## Phase 0.5: Pre-drop public readiness

Status: in progress

Goal: make the public repo feel intentional, credible, and worth watching before the official installable alpha is released.

Includes:

- sharper README and coming-soon narrative
- public-safe example handoff flow
- teaser copy bank for consistent suspenseful language
- trust model and security boundary docs
- pre-drop checklist
- GitHub issue and PR templates that protect the release boundary

Success standard:

The repo should feel like something serious is about to drop, while still making it impossible to confuse the current state with an official release.

## Phase 1: v0.1.0-alpha readiness

Goal: clean install and basic repo memory.

Target features:

- Python package install
- `auditme --help`
- `auditme init --project .`
- `auditme resume --project .`
- `auditme verify --project .`
- `auditme handoff --project . --next-move "..."`
- basic generated `90_AUDITME/` folder
- default config
- clean docs
- smoke tests from fresh folder

Non-goals:

- immediate public launch before the product is ready
- full desktop polish
- every internal CodexSystem feature
- complex multi-agent orchestration
- public cloud sync

## Phase 2: v0.2.0-alpha

Goal: configurable guardrails.

Target features:

- advisory/balanced/strict modes
- documented rule pack behavior
- clear warning vs failure output
- first config schema stability
- safer generated-file handling

## Phase 3: v0.3.0-beta

Goal: adoption polish.

Target features:

- better onboarding docs
- example repos or example fixtures
- GitHub Actions / CI guidance
- migration/import guide from existing internal AuditME repos
- compact agent prompt output

## Phase 4: v0.4.0-beta

Goal: stronger verification receipts.

Target features:

- documented receipt schema
- stronger proof summaries
- receipt history commands
- optional signed or hash-linked receipt exploration
- clearer manual-proof labeling

## Phase 5: v1.0.0

Goal: stable public contract.

Required:

- stable command names
- stable config schema
- tested install path
- changelog
- license
- contribution guide
- security guide
- release artifacts
- public examples

## Backlog ideas

These are valuable but should not block first release.

- Desktop dashboard release
- Web dashboard
- GitHub PR comment integration
- Multi-agent lane visualization
- Worktree helper commands
- Visual proof enforcement for UI projects
- Agent-specific adapters for Codex, Claude Code, Gemini CLI, Cursor, etc.
- Public template repo

## Product rule

Do not add a feature unless it improves one of these questions:

```text
What is true?
What is approved?
What is allowed?
What proof exists?
What should happen next?
```
