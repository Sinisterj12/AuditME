# Graphics Plan

This file tracks public-safe graphics work for AuditME.

Current posture: coming soon. Visuals should make the repo feel intentional and memorable without implying the installable product has launched.

## Current Assets

| Asset | Purpose | Status |
| --- | --- | --- |
| `assets/auditme-mark.svg` | Compact project mark for README, social previews, and future docs headers. | Added |
| `assets/auditme-banner.svg` | README hero banner for the public repo with coming-soon status. | Updated |
| `assets/auditme-social-preview.svg` | Public-safe social preview / future GitHub card source art. | Added |

## Direction

The visual system should communicate:

- fast agent work
- visible drift
- a controlled path back to repo truth
- durable memory
- guardrails
- verification receipts
- handoff readiness

## Constraints

Keep all graphics:

- public-safe
- SVG-first for now
- readable on GitHub light and dark themes
- free of private screenshots, local paths, secrets, relay content, customer data, and generated runtime state
- truthful about release status

## Future Ideas

- Export PNG social preview from `assets/auditme-social-preview.svg` if a platform needs raster upload
- small docs header mark
- command-flow diagram for First 5 Minutes
- small visual for `docs/EXAMPLE_HANDOFF_FLOW.md` showing chat drift becoming repo truth
- release announcement graphic after alpha release approval and final package proof

## Copy Pairing

When graphics need text, prefer short lines from `docs/TEASER_COPY_BANK.md`.

Best current pairings:

- `Keep the agent. Lose the drift.`
- `Proof should beat confidence.`
- `The repo should remember what the chat forgets.`
- `Agent work needs repo truth.`

Avoid any graphic copy that sounds like `install now`, `available today`, or `official release`.

## Visual QA Checklist

Before adding or replacing public graphics:

- confirm the asset is readable on GitHub light and dark themes
- avoid screenshots of private tools, private repos, relay rows, customer data, or local machine paths
- keep wording aligned with coming-soon status
- avoid fake install buttons, fake package badges, or fake release claims
- prefer simple repo-truth and handoff imagery over busy compliance visuals
