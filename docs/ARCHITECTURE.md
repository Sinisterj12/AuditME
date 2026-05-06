# Architecture Direction

This document defines the public architecture direction for AuditME.

AuditME should be split into clear layers so the public release is understandable, testable, and adaptable.

## Product definition

AuditME is a repo-native control layer for AI-assisted development.

It records project truth, agent handoff state, approved work, guardrail policy, and verification receipts in version-controlled files.

## Core layers

### 1. CLI layer

The CLI is the primary public interface.

Target command family:

```bash
auditme init
auditme resume
auditme verify
auditme handoff
auditme status
```

The CLI should be stable before the desktop layer is considered public-critical.

### 2. Project detection layer

Responsible for locating and understanding the target repo.

Responsibilities:

- detect project root
- detect Git state
- detect configured AuditME folder
- normalize paths
- avoid hardcoded local machine assumptions

### 3. State layer

Responsible for reading and writing AuditME-managed files.

Responsibilities:

- config
- resume state
- task queue
- decision ledger
- verification receipts
- generated markdown
- JSON/state schemas where needed

Rules:

- use atomic writes where practical
- avoid overwriting unrelated files
- separate generated files from human-owned files
- preserve manually authored sections when documented

### 4. Policy layer

Responsible for guardrails.

Responsibilities:

- load configured rule mode
- evaluate checks
- produce warnings and failures
- distinguish blocking vs advisory items

Policy should not be hardcoded only for one developer's preferences.

Recommended first modes:

- `advisory`
- `balanced`
- `strict`

### 5. Verification layer

Responsible for proving current repo state.

Responsibilities:

- run checks
- record command proof
- record manual proof separately
- report missing proof
- summarize pass/fail/warn state

Verification receipts should be evidence, not executable authority.

### 6. Reporting layer

Responsible for human and agent-readable output.

Responsibilities:

- markdown renderers
- compact CLI output
- JSON output
- agent handoff text

Reports should be deterministic enough for tests.

### 7. Optional desktop layer

The desktop app can provide visibility, but it should not be required for core adoption.

Responsibilities:

- display project health
- display task queue
- display receipts
- display drift warnings
- help non-CLI users understand status

The CLI must remain the source of truth.

## Public repo boundaries

The public release should not require:

- CodexSystem checkout
- private local paths
- private Google Drive or workspace state
- personal repo memory
- private branch naming conventions

## Generated folder

Default folder:

```text
90_AUDITME/
```

This is already part of the internal design and can remain the public default if documented clearly.

Potential future option:

```bash
auditme init --folder .auditme
```

Do not add that option until the default release is stable.

## Config direction

Potential config file:

```text
90_AUDITME/auditme.config.json
```

Minimum config fields:

```json
{
  "version": 1,
  "mode": "balanced",
  "audit_folder": "90_AUDITME",
  "allowed_write_scope": ["src/", "tests/", "docs/"],
  "receipt_policy": {
    "manual_verification_allowed": true,
    "visual_proof_required_for_ui": false
  }
}
```

## Trust model

AuditME should assume repo-local files may be modified by branches or pull requests.

Therefore:

- schema validation matters
- unknown fields should be ignored or warned on
- generated markdown should not become executable instruction without validation
- users should review AuditME file changes like code changes

## First release architecture goal

The first public release should favor clarity over feature count.

Minimum viable public architecture:

```text
CLI -> project detection -> state manager -> policy checks -> reporter
```

Desktop, advanced automation, and multi-agent orchestration should come after the clean public command contract is proven.
