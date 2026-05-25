# AuditME Trust Model

> Status: public prelaunch trust model. AuditME is not officially released yet.

AuditME deals with repo-local memory, agent-facing context, and verification receipts. That means the trust model matters before the package is promoted as installable.

This document explains what AuditME should trust, what it should only inspect, and what must remain human-reviewable.

## Core Principle

Repo-local AuditME files are useful evidence. They are not unquestionable authority.

AuditME should help agents and humans reason from repo truth, but it should not turn arbitrary markdown into executable instruction or treat a receipt as proof without context.

## Trust Boundaries

| Surface | Trust level | Rule |
| --- | --- | --- |
| `auditme.config.json` | structured policy input | Trust only after schema validation. Unknown or malformed values should warn or fail clearly. |
| `AUDITME_RESUME.md` | human-readable context | Treat as summary and handoff context, not executable authority. |
| `AUDITME_TASK_QUEUE.md` | planning context | Treat as proposed/approved work only when the repo owner or project process says it is approved. |
| `AUDITME_DECISION_LEDGER.md` | durable decision history | Treat as reviewable project memory; do not override current source truth. |
| `AUDITME_VERIFICATION_RECEIPTS.md` | proof index | Treat as evidence only when commands, timestamps, and scope are credible. |
| Source code and tests | implementation truth | Verify behavior directly where practical. |
| Chat history | low trust | Use as context only; prefer repo files and current verification. |

## Repo-Memory Poisoning

A pull request can modify memory files and attempt to steer a future agent.

Mitigation direction:

- Review AuditME file changes like code changes.
- Keep config structured and validated.
- Keep generated markdown clearly labeled.
- Prefer current source and fresh verification when memory conflicts with code.
- Do not let a markdown instruction override repo policy or owner approval.

## Prompt Injection

Project files can contain text that tries to redirect an AI agent.

AuditME should reduce this risk by separating:

- repo policy
- generated summaries
- verification evidence
- user-authored project content
- agent observations

Generated summaries should be labeled as summaries. They should not silently become the top authority for future work.

## Verification Receipts

Receipts should say what was checked, not imply more than the evidence proves.

Good receipt behavior:

- names the command or manual check
- records scope
- distinguishes `pass`, `warn`, and `fail`
- labels manual verification clearly
- avoids hiding missing proof behind green language

Bad receipt behavior:

- "done" without the command or check
- manual confidence presented as automated proof
- stale receipts treated as current proof
- receipts used to skip current verification before release

## Secrets And Private Data

AuditME memory is not a vault.

Do not store:

- secrets
- credentials
- API keys
- tokens
- customer data
- private relay notes
- personal machine paths as required behavior
- generated private runtime state from another repo

## Pre-Alpha Standard

Before the official alpha is released, the project should prove:

- generated files are predictable and reviewable
- config validation rejects malformed or unsafe state
- verification output is honest about warnings and failures
- generated content does not include private paths or private project state
- docs explain the difference between context, policy, and proof

Until then, AuditME remains in public coming-soon mode.
