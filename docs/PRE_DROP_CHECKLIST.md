# AuditME Pre-Drop Checklist

> Status: coming-soon checklist. This is the stop line before the official alpha release.

The goal is to get the public repo as close as possible to launch quality without releasing AuditME yet.

Do not use this checklist as permission to tag, publish, announce, or release. It defines what should be ready before asking for that approval.

## Public Story

- [x] README explains the problem and promise quickly.
- [x] Coming-soon page says the product is not officially released.
- [x] Productization plan defines the first public audience and product spine.
- [x] Public repo experience guide defines the intended visitor journey.
- [x] Example handoff flow makes the value tangible without private state.

## Visual And Design Surface

- [x] README banner exists.
- [x] Social preview art exists.
- [x] Brand direction defines promise, voice, and public boundaries.
- [ ] Final visual QA pass confirms assets are readable on GitHub light and dark themes.
- [ ] Optional public-safe release-candidate graphic is prepared but not announced.

## Trust And Safety

- [x] Security policy explains repo-memory poisoning, prompt injection, false verification, and secrets risk.
- [x] Public docs warn against private relay notes, customer data, credentials, and personal machine paths.
- [x] Release preflight blocks private checkout requirements and personal path assumptions.
- [ ] Final security/trust-boundary review is completed against generated files and receipts.

## Package And Behavior Proof

- [x] Public alpha command spine is documented: `init`, `resume`, `verify`, `handoff`.
- [x] Prelaunch readiness snapshot records prior local proof.
- [ ] Fresh release-candidate proof is rerun immediately before release approval.
- [ ] Package boundary inspection is rerun immediately before release approval.
- [ ] Fresh throwaway-project smoke is rerun immediately before release approval.

## Release Boundary

- [x] README does not include official install instructions.
- [x] Coming-soon docs do not claim the alpha is live.
- [x] Prelaunch readiness says proof is not a release.
- [x] No PyPI publication is approved here.
- [x] No Git tag or GitHub Release is approved here.
- [x] No public announcement is approved here.

## Ready-To-Ask-For-Release Standard

AuditME is ready to ask for release approval when:

- the repo looks intentional and coherent
- a stranger can understand the product without private context
- the example handoff makes the value concrete
- final package/install smoke passes from a fresh environment
- security and generated-file boundaries are reviewed
- release notes and announcement wording are prepared but not published

The final required action remains explicit owner approval to tag, publish, and announce.
