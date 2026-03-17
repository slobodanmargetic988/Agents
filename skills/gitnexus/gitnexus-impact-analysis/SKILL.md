---
name: gitnexus-impact-analysis
description: "Use when the user wants to know what depends on a symbol, what may break if code changes, or what tests and flows should be revisited before editing or merging."
---

# GitNexus Impact Analysis

Use this skill before non-trivial code changes and during review.

## Workflow

1. Read `gitnexus://repo/{name}/context`.
2. Run `impact` on the target symbol with `direction: upstream`.
3. Review the highest-confidence depth-1 results first.
4. Read affected process traces if the symbol participates in important flows.
5. If there are local changes, run `detect_changes`.
6. Report the likely blast radius before editing or merging.

## Checklist

- [ ] `impact` on the target symbol
- [ ] Review depth 1 before anything else
- [ ] Check process participation for critical flows
- [ ] Use `includeTests: true` when test coverage matters
- [ ] Use `detect_changes` if code is already modified
- [ ] Summarize risk clearly

## How To Read The Output

- `d=1`: direct callers/importers, highest break risk
- `d=2`: likely affected downstream logic
- `d=3`: wider retest zone

## Risk Heuristics

- Few direct callers, few processes: low to medium risk
- Many direct callers or shared/core module: high risk
- Auth, payment, storage, migration, or runtime orchestration paths: treat as high or critical

## Main Tools

- `impact`: primary blast-radius tool
- `detect_changes`: change-set impact after edits
- `context`: inspect one high-risk symbol in more detail

## Good Use Cases

- before renaming a shared function
- before changing a contract or data shape
- before merging a risky branch
- when deciding which tests need to be rerun
