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

## Current Public Posture

AuditME is in coming-soon mode.

The public repo should feel worth watching before the official installable alpha is launched. The right tone is confident but restrained: strong product idea, clear visual identity, honest status, and no claim that the release is live before the owner approves it.

The README and preview docs should make three things obvious:

- AuditME has a sharp purpose.
- The official release is intentionally waiting.
- Private implementation state is not being exposed as public product code.

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
