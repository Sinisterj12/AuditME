## Intent Router
- This is the clean public release repo for AuditME, not the private implementation lab.
- Public GitHub repo: `Sinisterj12/AuditME`.
- Treat committed repo files, GitHub issues, and pull requests as the durable source of truth. Chat prompts from other agents are planning input until verified against the repo.
- Normal startup read order:
  - `AGENTS.md`
  - `README.md`
  - `docs/RELEASE_PREFLIGHT.md`
  - `docs/CODE_PUBLICATION_PLAN.md`
  - `docs/ARCHITECTURE.md`
  - `docs/ADOPTER_GUIDE.md`

## Public Release Mission
- Prepare AuditME for `v0.1.0-alpha` as a clean, installable Python CLI package.
- The first public product must be small, path-neutral, testable, and understandable by users who do not know the private CodexSystem workflow.
- The public alpha scope is:
  - package metadata
  - `auditme` console script
  - `auditme init --project .`
  - `auditme resume --project .`
  - `auditme verify --project .`
  - `auditme handoff --project . --next-move "..."`
  - default config
  - safe generated `90_AUDITME/` creation
  - minimal markdown and JSON state files
  - basic tests
  - honest verification output

## Hard Boundaries
- Do not copy the private CodexSystem repo wholesale.
- Do not import private Git history, generated `90_AUDITME` runtime state, private task queues, decision ledgers, sync notes, operator notes, secrets, credentials, customer data, or work data.
- Do not make a private CodexSystem checkout, private Google Drive, private sync folder, or personal local path required public behavior.
- Do not add desktop UI, fleet orchestration, lab harnesses, sync/dropzone workflows, standalone update machinery, or advanced multi-agent commands to `v0.1.0-alpha`.
- Do not create branches, stage, commit, push, publish releases, or open PRs unless the user explicitly approves that operation.
- **No Workday/Shift Clutter:** Do not add workday, shift tracking, clock-in/out timers, session stopwatch logic, or timing-log commands (like `WORKDAY_RESEARCH.md` integration) to the core CLI repository. All workday, session stopwatch, and timecard features must remain strictly decoupled: they live entirely inside the agent's external skills or in the **AuditME Desktop** visual dashboard companion, keeping this repository focused exclusively on general-purpose AI guardrails verification.

## CodexSystem Reference Rules
- The private CodexSystem implementation may be inspected only when the user explicitly asks for read-only inventory, import mapping, or release comparison.
- Read-only inspection means file listing, search, targeted reads, and test-name review. It does not mean copying, editing, running mutating commands, or generating private AuditME state into this repo.
- Classify private implementation pieces before import:
  - `copy`: safe with little or no change
  - `extract`: useful code that needs trimming or cleanup
  - `rewrite`: good concept, tangled implementation
  - `later`: valuable but not alpha material
  - `never`: private/internal only

## AuditME Dogfooding Rule
- Do not bootstrap or generate AuditME runtime state in this public repo until the public `auditme init` contract is approved.
- Until then, use normal Git, docs, targeted tests, and read-only private implementation inventory.
- After public-safe `auditme init` exists, this repo may dogfood AuditME intentionally through a reviewed PR.

## GitHub And Release Hygiene
- Keep `main` clean and release-facing.
- Prefer a reviewed release-preflight branch for code import once approved, for example `release-preflight/v0.1.0-alpha`.
- Every imported feature must have docs that match behavior and tests that prove the public command contract.
- Public metadata, README claims, package metadata, and command help must agree before alpha.
- Add a license before publishing installable code.

## Private Agent Relay Rules
- Do not commit agent relay chatter, private sync notes, or cross-agent banter files into this public repo.
- Private agent coordination lives outside this repo through the operator-provided relay system from the global instructions.
- Use the private relay only for cross-agent coordination, locator notes, blockers, and release decisions that should not be public repo content.
- Public repo files should contain only release-facing docs, product code, tests, examples, and public-safe project policy.
- If private relay discussion produces a durable public decision, summarize it into a public-safe issue, PR note, docs change, or `AGENTS.md` rule.
- If agents disagree, pause implementation, record the conflict in the private relay with options and risks, and wait for a clear decision before coding through it.
- Do not create `90_AUDITME/` in this repo until the public `auditme init` contract is approved.

## Verification Standard
- Before calling work done, report exactly what was verified.
- For docs-only changes, verify relevant links/files and Git status.
- For code import, require at minimum:
  - install command succeeds
  - `auditme --help` works
  - `auditme init --project <fresh repo>` creates only expected safe files
  - `auditme resume --project <fresh repo>` returns useful context
  - `auditme verify --project <fresh repo>` reports pass/fail/warn honestly
  - `auditme handoff --project <fresh repo> --next-move "..."` updates only intended state
  - tests pass from a clean checkout

## Project Manager Rule
- The public repo agent owns release cleanliness, scope control, import safety, and GitHub-readiness decisions for this repo.
- If another agent suggests code or strategy, verify it against this repo's docs, public alpha scope, and hard boundaries before acting.
- Be direct about anything that is too private, too magical, too broad, or too hard to explain to a first-time public user.
