# Example Handoff Flow

> Status: public-safe preview. This is not an official release walkthrough.

AuditME is meant to make a fresh AI session start from repo truth instead of chat memory.

This example uses fictional project details. It does not contain private repo state, customer data, relay content, credentials, or a real release instruction.

## The Problem

Without a repo-local handoff, the next agent often starts with:

```text
What were we doing?
Which branch matters?
What was already tested?
What should I avoid touching?
Can I trust the last chat?
```

That is where drift starts.

## The Intended AuditME Shape

After the first alpha is released, a project should eventually be able to create a small `90_AUDITME/` folder with:

```text
AUDITME_RESUME.md
AUDITME_TASK_QUEUE.md
AUDITME_DECISION_LEDGER.md
AUDITME_VERIFICATION_RECEIPTS.md
auditme.config.json
```

Those files should give the next agent a compact operating surface:

- what the project is
- what work is approved
- what is allowed
- what proof exists
- what should happen next

## Example: Before AuditME

```text
User: Continue from yesterday. I think the dashboard thing was almost done.

Agent: I need to inspect the repo, guess the active branch, infer the last task,
and hope the last chat summary was accurate.
```

Risk:

- the agent may reopen finished work
- the agent may miss a known stop condition
- the agent may trust stale chat
- proof may be separated from the repo

## Example: With AuditME

```text
User: Start from repo truth.

Agent: I ran auditme resume. The repo says:
- current lane: dashboard filter polish
- approved write scope: frontend filter panel and tests
- stop condition: do not change backend query shape
- latest proof: filter smoke passed, visual spacing not verified
- next move: verify narrow width and long labels before calling the lane done
```

The agent starts with a smaller search space and a clearer definition of done.

## Example Handoff Text

An `auditme handoff` result should feel like this:

```text
Next move: Verify dashboard filters at narrow width and long-label state.
Allowed scope: filter panel UI, filter tests, docs if behavior changes.
Stop condition: do not change backend query shape without explicit approval.
Latest proof: unit filter tests passed; visual proof still missing.
```

That is not magic. It is repo-local memory doing the boring work that chat history usually fails at.

## What This Preview Proves

This preview is meant to show the product feel:

- handoffs become concrete
- proof becomes visible
- stop conditions travel with the repo
- a new agent does less guessing

It does not prove the official package is released. The installable alpha still waits for release approval.
