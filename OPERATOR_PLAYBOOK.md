# AuditME Operator Playbook

This is the stable agent operating playbook for the public AuditME release repository. 
Follow these guidelines to maintain repository health, safety, and professional release-candidate quality.

## Core Directives

1. **Toolchain Standard**: Always use `uv` for python environments, package management, and script execution.
   - Run tests: `uv run pytest`
   - Run the CLI: `uv run auditme <command>`
   - Build package: `uv build`
2. **Release Boundaries**: Never tag, publish, or announce a release without explicit owner approval.
3. **No Private Leaks**: Never commit private agent relay chatter, local machine paths (`C:\\Projects\\...`), internal credentials, or CodexSystem development files.
4. **Advisory Verification**: In this first alpha, verification warnings are advisory. `auditme verify` prints advisory `Status: warn` when receipts are blank but does not exit with an error.

## Verification Checklist before Pushing

Before any code changes are merged to `main`:
- Run `uv run pytest` and ensure 100% test success.
- Run `uv run auditme verify --project .` and verify the status reports cleanly.
- Ensure `git status` shows no untracked file pollution.
