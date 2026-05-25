# AuditME Is Coming Soon

![AuditME social preview](assets/auditme-social-preview.svg)

AuditME is a repo-native control layer for AI-assisted development.

It is being built for people who work with coding agents across real projects and need stronger continuity than chat history can provide.

The promise is simple:

```text
Keep the agent. Lose the drift.
```

## The Problem

AI agents move quickly, but long-running projects can drift:

- decisions get buried in old chats
- scope changes without a clear record
- proof becomes hard to inspect
- a new session has to rediscover the same facts
- handoffs depend on memory instead of the repo

AuditME is designed to pull that work back into the project itself.

## The Product Idea

AuditME should help a repo answer five questions:

```text
What is true?
What is approved?
What is allowed?
What proof exists?
What should happen next?
```

The first public alpha is planned around a small CLI workflow:

```bash
auditme init --project .
auditme resume --project .
auditme verify --project .
auditme handoff --project . --next-move "Describe the next safe task"
```

That is the target public path, not a release announcement.

## Why This Feels Different

Most AI coding tools focus on making the agent more powerful.

AuditME focuses on what happens around the agent:

- the memory that should survive the chat
- the proof that should survive confidence
- the next move that should survive handoff
- the boundaries that should survive speed

The product bet is that serious AI-assisted work needs a repo-native control layer, not just a smarter prompt.

## Current Status

AuditME is not officially released yet.

This repository is public so the product direction, docs, and visual identity can be shaped in the open before the installable alpha is launched.

The release code, package proof, final release notes, and publication path are intentionally waiting until the alpha is ready.

The current repo is meant to feel alive before it is installable: product story, release boundaries, first alpha spine, visual direction, and prelaunch proof are being assembled in public-safe form.

## What Will Not Be Published

The public release will not include:

- private CodexSystem history
- private relay notes
- generated private runtime state
- customer or work data
- secrets or credentials
- personal local machine assumptions

## Watch This Repo

Star or watch this repo if you want to follow the public alpha as it gets closer.

## What To Watch For

The next public signals should be concrete, not hype:

- clean install proof from a fresh checkout
- a short first-alpha release candidate report
- a tighter explanation of the trust model
- examples that show how repo-local memory changes an agent handoff
- no official package, tag, or announcement until those checks are done

AuditME should feel like a product before it asks anyone to install it.

## Preview The Shape

The public repo now includes two pre-drop guides:

- [Example Handoff Flow](docs/EXAMPLE_HANDOFF_FLOW.md): a public-safe walkthrough of the kind of repo-local handoff AuditME is meant to make boring and repeatable.
- [Pre-Drop Checklist](docs/PRE_DROP_CHECKLIST.md): the line between "coming soon" and "ready to ask for release approval."

These pages are intentionally previews. They build understanding and anticipation without claiming the official alpha has shipped.

## The Line Before Launch

The intended stopping point before release is clear:

- the repo looks intentional
- the docs explain the product without private context
- the first command path is understandable
- the trust boundaries are visible
- the release-candidate proof is current
- the only thing left is explicit approval to tag, publish, and announce

That is the edge AuditME is moving toward.
