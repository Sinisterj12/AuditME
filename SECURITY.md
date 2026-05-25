# Security Policy

AuditME is designed to manage repo-local memory and agent-facing context. That means security is not only about code execution. It is also about instruction integrity.

## Current status

AuditME is in public alpha release-preflight mode. The public CLI command spine exists, but it is still pre-release software.

Security review is required before a stable release.

The public trust model is tracked in [docs/TRUST_MODEL.md](docs/TRUST_MODEL.md). That document explains what AuditME should trust, what it should only summarize, and what must remain human-reviewable before the official alpha release.

## Main risks

### Repo-memory poisoning

A pull request could modify AuditME memory files and try to influence future AI agents.

Mitigation direction:

- Treat AuditME memory as reviewable repo data.
- Validate structured state before using it.
- Do not treat arbitrary markdown as trusted executable instruction.
- Show AuditME file changes clearly during review.

### Prompt injection through project files

An attacker could add instructions inside project files, docs, comments, or generated output that attempt to redirect an AI agent.

Mitigation direction:

- Keep agent instructions separated from observed project content.
- Label generated summaries as summaries, not authority.
- Prefer schema-validated config for policy decisions.

### False verification claims

A receipt could claim that verification happened when it did not.

Mitigation direction:

- Record exact commands where possible.
- Label manual verification separately.
- Avoid treating manual verification as equal to automated proof.
- Make receipts reviewable and auditable.

### Secrets in memory files

Users may accidentally store credentials, tokens, customer data, or private context in AuditME files.

Mitigation direction:

- Warn users not to store secrets in AuditME files.
- Avoid collecting secrets.
- Avoid copying environment variables or credentials into generated reports.

## Reporting vulnerabilities

Until a formal process is published, report suspected security issues by opening a private communication path with the repository owner rather than posting exploitable details publicly.

## Alpha security requirements

Before widening adoption beyond the first alpha:

- Document trust boundaries.
- Add config validation.
- Add generated-file warnings.
- Add secret-handling guidance.
- Add tests for unsafe overwrite behavior.
- Add tests for malformed state handling.
