# Adopter Guide

> Status: coming-soon adoption guide. This describes the intended public alpha experience, not a current release announcement.

This guide describes the intended public adoption experience for AuditME once the first alpha is officially released.

AuditME is not intended to replace a coding agent. It is intended to give coding agents a durable repo-local operating layer: project truth, allowed scope, handoff notes, verification receipts, and guardrail expectations.

## Intended audience

AuditME is for:

- Solo builders using AI coding tools heavily
- Small teams using multiple AI agents
- Projects where chat history is not reliable enough
- Repos where scope control and verification matter
- Developers who want a repeatable handoff process between sessions

## What AuditME should do for a new repo

A new adopter should eventually be able to run:

```bash
auditme init --project .
```

Then AuditME should create a small repo-local control surface without taking over the project.

Expected generated structure:

```text
90_AUDITME/
  AUDITME_RESUME.md
  AUDITME_TASK_QUEUE.md
  AUDITME_DECISION_LEDGER.md
  AUDITME_VERIFICATION_RECEIPTS.md
  auditme.config.json
```

The first alpha is planned around this simple generated structure:

- Resume tells the next agent where to start.
- Task queue tells the next agent what is approved.
- Decision ledger tells the next agent why things are true.
- Verification receipts tell humans what proof exists.
- Config tells AuditME how strict to be.

## First-run goals

After initialization, a user should be able to answer:

- What is this repo?
- What files are safe for an agent to edit?
- What should the next agent do?
- What rules should the agent follow?
- What proof is required before saying work is done?

## Recommended first setup

After release, public users should start with the plain init path:

```bash
auditme init --project .
```

Suggested future modes:

- `advisory`: report issues, do not block
- `balanced`: block dangerous drift, warn on style issues
- `strict`: enforce stronger proof and guardrail rules

The first alpha should write `mode: advisory` by default and validate the known mode names. Deeper mode behavior can mature after the core command path is proven.

## Agent handoff pattern

A user should be able to start a fresh AI session with:

```bash
auditme resume --project .
```

The output should be copyable into a coding agent and should include:

- current project summary
- active branch or lane
- next approved task
- allowed write scope
- stop conditions
- recent verification state

## Verification pattern

Before work is called done:

```bash
auditme verify --project .
```

AuditME should report:

- passing checks
- failing checks
- missing proof
- warning-only items
- suggested next safe action

For the first public alpha, warnings are advisory: `auditme verify` can return success while still printing `Status: warn` when proof is missing. Treat that as "not ready to claim done," not as a broken install.

## Handoff pattern

After a completed task:

```bash
auditme handoff --project . --next-move "Describe the next safe task"
```

AuditME should update repo memory so the next session does not rely on chat history.

## What adopters should not do

Do not store secrets in AuditME memory files.

Do not treat generated markdown as a security boundary.

Do not allow unreviewed pull requests to rewrite agent instructions without human review.

Do not assume a receipt is proof unless the recorded command or manual verification is credible.

## Success standard

AuditME succeeds when a fresh AI session can enter a repo and quickly understand:

```text
What is true?
What is approved?
What is allowed?
What proof exists?
What should happen next?
```
