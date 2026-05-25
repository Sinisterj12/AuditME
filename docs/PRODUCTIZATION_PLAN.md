# AuditME Productization Plan

> Status: public coming-soon plan. This is not a release announcement.

AuditME should become a product by getting clearer, safer, and easier to trust before it gets bigger.

The goal is not to expose every internal workflow. The goal is to give public users a small control layer that makes AI-assisted development easier to resume, audit, and hand off.

## Product Positioning

Primary promise:

```text
Keep the agent. Lose the drift.
```

Plain-English product category:

```text
Repo-native memory and verification for AI-assisted development.
```

AuditME should be understood as the layer that answers:

```text
What is true?
What is approved?
What is allowed?
What proof exists?
What should happen next?
```

## First Public Audience

The first alpha should serve builders who already use coding agents and feel the pain of:

- losing context between sessions
- relying on chat history for project memory
- accepting vague "done" claims
- handing work between agents or machines
- needing a repo to explain itself quickly

The alpha does not need to convince people who have never used coding agents. It should make serious agent users think, "I need this in my repos."

## Product Spine

The first alpha product spine is intentionally small:

```bash
auditme init --project .
auditme resume --project .
auditme verify --project .
auditme handoff --project . --next-move "Describe the next safe task"
```

Each command should have one job:

- `init`: create a predictable repo-local control surface.
- `resume`: give the next agent copyable repo truth.
- `verify`: separate proof, warnings, and failures.
- `handoff`: record the next safe move before context disappears.

If a new feature does not strengthen that spine, defer it.

## Suspense Without Overclaiming

The public repo should build interest by showing a clear idea under disciplined restraint.

Good suspense:

- public-safe visuals that make the product memorable
- precise coming-soon language
- concrete preflight proof
- a small command path that is easy to understand
- honest blockers and release gates

Bad suspense:

- fake install badges
- claiming PyPI availability before publish
- implying private CodexSystem workflows are public product behavior
- broad roadmaps that make the alpha feel unfocused
- screenshots or generated state from private projects

## Alpha Readiness Gates

Before any official alpha release, AuditME needs:

- clean package build proof
- wheel or isolated install proof
- fresh throwaway-project smoke for all four commands
- generated file audit showing only expected `90_AUDITME/` files
- private-marker scan of generated output
- docs-vs-behavior consistency check
- security/trust-boundary review
- explicit owner approval for tag, release, publish, and announcement

Passing these gates means "ready for release-candidate review," not "automatically released."

## Near-Term Product Work

The next useful work should stay focused:

- tighten the prelaunch readiness report after each serious proof pass
- add one public-safe example handoff that shows the product value
- improve docs around verification receipts and trust boundaries
- keep README and coming-soon language suspenseful but truthful
- avoid new command families until the four-command spine is boringly reliable

Current public-safe example surface:

- `docs/EXAMPLE_HANDOFF_FLOW.md` shows the intended handoff feel without using private repo memory, private relay data, or official install claims.
- `docs/PRE_DROP_CHECKLIST.md` keeps the pre-release stop line visible so documentation polish does not drift into release action.

## Public Repo Experience Standard

Before the official alpha drops, the repository should feel like a coherent product surface:

- README explains the product in under three minutes.
- Coming-soon page builds interest without pretending the release is live.
- Brand docs define the promise, tone, and visual direction.
- Readiness docs show proof without turning proof into publication.
- Security docs make trust boundaries visible.
- Planning docs explain why the first alpha is small on purpose.

The repo should leave visitors with one clear impression: AuditME is not another prompt trick; it is a serious control layer for agent-heavy development.

## Pre-Drop Stop Point

Stop before actual release when these are true:

- public docs and visuals feel launch-grade
- no public file requires private context to understand the product
- release gates are documented and mostly proven
- package proof exists but is not marketed as an official launch
- examples show the value without leaking private state
- GitHub repo presentation is clean enough for watchers and early adopters
- the only remaining action is explicit approval to tag, publish, and announce

That is the intended "right before the drop" state.

## Product Rule

AuditME productization is successful when a first-time user can understand the value before installing it, then install it and see the same promise proven by the first four commands.
