---
name: gitnexus-refactoring
description: "Use when safely renaming, extracting, splitting, moving, or restructuring code. Examples: \"Rename this function\", \"Split this module\", \"Extract this class\"."
---

# GitNexus Refactoring

Use this skill before and during structural edits.

## Workflow

1. Read `gitnexus://repo/{name}/context`.
2. Run `impact` on the target symbol or file.
3. Run `context` to understand callers, callees, imports, and process membership.
4. Use `rename` with `dry_run: true` for coordinated renames.
5. Apply the edit only after reviewing the preview.
6. Run `detect_changes` after the edit to verify the affected scope.
7. Re-run the most relevant tests for affected flows.

## Checklists

### Rename

- [ ] `rename(..., dry_run: true)`
- [ ] Review all proposed edits
- [ ] Apply only if the preview is sensible
- [ ] `detect_changes` after apply
- [ ] Re-test affected flows

### Extract or Split

- [ ] `context` on the current symbol/module
- [ ] `impact` on the symbol to understand dependents
- [ ] define the new seam or interface
- [ ] make the change
- [ ] `detect_changes` and test affected flows

## Main Tools

- `rename`: safest path for multi-file renames
- `impact`: tells you who depends on the target
- `context`: shows surrounding structure
- `detect_changes`: verifies what the refactor actually touched
- `cypher`: optional for advanced structural questions

## Practical Rules

- Never rename a shared symbol blind
- Preview first for coordinated renames
- Treat depth-1 dependents as mandatory update targets
- Re-test flows, not just files
