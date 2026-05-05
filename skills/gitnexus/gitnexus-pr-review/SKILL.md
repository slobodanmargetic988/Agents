---
name: gitnexus-pr-review
description: "Use when reviewing a PR or diff and you want structural blast-radius analysis, affected flows, likely missing updates, or missing test coverage."
---

# GitNexus PR Review

Use GitNexus to understand what a diff changes structurally, not just textually.

## Workflow

1. Get the diff with `gh pr diff`, `git diff`, or equivalent.
2. Run `detect_changes` for the changed files.
3. Run `impact` on the most important changed symbols.
4. Use `context` on the highest-risk symbols.
5. Read one or two affected process traces if needed.
6. Write findings in terms of break risk, missing updates, and missing tests.

## Checklist

- [ ] Map the change set with `detect_changes`
- [ ] Inspect high-risk changed symbols with `impact`
- [ ] Check direct callers/importers for compatibility
- [ ] Check affected flows, not just changed files
- [ ] Include tests in impact analysis when relevant
- [ ] Report concrete findings first

## What GitNexus Is Good At In Review

- finding callers not updated by a signature change
- showing which execution flows the diff touches
- showing whether shared symbols changed without downstream updates
- identifying which tests are structurally near the change

## Review Structure

- Risk level
- Key affected symbols/modules/processes
- Findings ordered by severity
- Missing coverage or missing updates
- Merge recommendation

## Main Tools

- `detect_changes`: first-pass structural map of the diff
- `impact`: blast radius per changed symbol
- `context`: deep dive on one suspicious symbol
