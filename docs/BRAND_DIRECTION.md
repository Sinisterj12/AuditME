# AuditME Brand Direction

AuditME should look like a serious developer tool with a sharp product idea, not like a generic compliance checklist.

## Core Promise

```text
Keep the agent. Lose the drift.
```

Secondary line:

```text
Turn agent chaos into repo truth.
```

## Story

AI coding agents are useful because they move fast. The risk is that speed can turn into drift: forgotten decisions, fuzzy scope, scattered proof, and handoffs that depend on chat memory.

AuditME should present itself as the control layer that pulls that motion back into the repo. The product does not shame AI-assisted work. It makes the workflow more honest, inspectable, and repeatable.

The emotional frame should be anticipation, not availability. A visitor should feel that a serious new agent-workflow layer is about to arrive, while still understanding that the official installable alpha is intentionally held back until the proof is ready.

## Current Public Posture

AuditME is in coming-soon mode.

The public repo should feel worth watching before the official installable alpha is launched. The right tone is confident but restrained: strong product idea, clear visual identity, honest status, and no claim that the release is live before the owner approves it.

The README and preview docs should make three things obvious:

- AuditME has a sharp purpose.
- The official release is intentionally waiting.
- Private implementation state is not being exposed as public product code.

They should also make the repo feel active and close to a drop:

- the first alpha spine is already visible
- the release gates are explicit
- the visual identity is deliberate
- the project is being productized in public-safe layers
- the next public signal is concrete proof, not vague hype

## Visual Idea

The visual system should show controlled chaos:

- scattered signal paths becoming one clean route
- repo memory as the stable anchor
- verification receipts as visible proof
- guardrails as structure, not decoration
- handoff as the next safe move

The current public-safe SVG assets are:

- `assets/auditme-mark.svg`
- `assets/auditme-banner.svg`

They intentionally avoid private product screenshots, generated runtime state, customer data, or internal relay details.

## Voice

Use direct, confident language.

Good:

- "AuditME turns agent chaos into repo truth."
- "Without AuditME, project memory gets trapped in chat instead of living with the repo."
- "Verify separates proof, warnings, and failures."

Avoid:

- vague enterprise language
- fake launch claims
- implying the alpha is already fully released
- claiming commands or release artifacts before they land
- making private CodexSystem behavior sound public
- making the preview sound abandoned or unfinished in a careless way

Prefer suspenseful but honest language:

- "coming soon"
- "first alpha spine"
- "release-candidate proof"
- "repo truth"
- "agent drift"
- "before the official installable alpha"
- "proof should beat confidence"
- "the repo should remember what the chat forgets"

Avoid language that sounds like the package is already generally available:

- "install now"
- "available on PyPI"
- "official release"
- "download the alpha"
- "production ready"

## Public Release Boundaries

Brand polish must stay public-safe:

- no private relay content
- no private CodexSystem paths
- no committed or generated `90_AUDITME` runtime state artifacts in docs/assets lanes
- no fake install/download badges
- no release tag language before release
- no package behavior or pyproject changes in docs/assets lanes

## README Shape

The README should lead with:

1. banner or mark
2. tagline
3. one-sentence product promise
4. truthful current status
5. coming-soon framing
6. compact problem framing
7. "Without AuditME / With AuditME"
8. planned command path
9. current status and docs links

The first screen should make the repo worth starring or watching without overpromising what has shipped.

## Coming-Soon Narrative Shape

The public coming-soon surface should follow this arc:

1. Agents are fast, but project truth drifts.
2. AuditME pulls memory, proof, boundaries, and next moves back into the repo.
3. The first alpha is intentionally small: `init`, `resume`, `verify`, `handoff`.
4. The repo is public now so the idea, visuals, and proof can be shaped safely.
5. The official release waits for clean install proof, trust-boundary review, and owner approval.

The story should make the wait feel disciplined, not stalled.

## Copy System

Reusable public-safe copy belongs in `docs/TEASER_COPY_BANK.md`.

Use that file for:

- short taglines
- social-preview language
- README pull quotes
- prelaunch update language
- release-boundary-safe teaser copy

Do not use teaser copy to imply AuditME is installable, tagged, published, or generally available.
