# Contributing

AuditME is currently in launch-preflight mode.

The first priority is not feature expansion. The first priority is making the public release clean, installable, safe, and understandable.

## Current contribution focus

Helpful work right now:

- remove private path assumptions
- improve install flow
- simplify public commands
- document config behavior
- harden generated-file safety
- improve verification receipts
- write tests
- improve onboarding docs

Avoid for now:

- adding unrelated features
- expanding desktop UI before CLI is stable
- copying private repo memory into public docs
- adding agent-specific assumptions too early

## Public release rule

Every public-facing feature should answer at least one of these questions:

```text
What is true?
What is approved?
What is allowed?
What proof exists?
What should happen next?
```

If it does not help answer one of those, it probably belongs in the backlog.

## Development expectations

Before a change is considered done:

- tests should pass
- docs should match behavior
- generated files should not include private local paths
- command examples should be accurate
- verification status should be honest

## Pull request expectations

A good PR should include:

- what changed
- why it changed
- how it was tested
- risks or limitations
- follow-up work if needed

## Coding style

Prefer boring, readable code over clever code.

AuditME exists to reduce AI-driven chaos, not become more of it.
