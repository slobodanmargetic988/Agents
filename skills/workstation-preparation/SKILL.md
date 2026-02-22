---
name: workstation-preparation
description: Prepare a clean worker slot worktree for orchestration by creating or resetting workstation-1 through workstation-10 with a requested branch. Use when orchestrator agents need a clean git worktree slot before dispatching a worker.
metadata:
  short-description: Prepare clean workstation slot
---

# Workstation Preparation

## Overview

Use this skill to create or reset a worker slot worktree in a clean state.

Mandatory policy gate:
- Do not create or reset any worktree slot without explicit user permission.
- If permission is not already explicit in the current request, stop and ask first.
- This requirement follows `agents/_shared/WORKTREE_POLICY.md`.

The skill enforces:
- allowed slot names: `workstation-1` ... `workstation-10`
- hard limit: never create an 11th workstation slot
- slot reset to requested branch and base ref for deterministic starts

## Script

`/Users/slobodan/.codex/skills/workstation-preparation/scripts/prepare_workstation.py`

## Inputs

- `worktree_name` (optional): workstation slot name (`workstation-1` ... `workstation-10`)
- `branch_name` (optional): branch to initialize in that slot

Defaults:
- if `worktree_name` is omitted, script auto-selects first free standardized slot
- if `branch_name` is omitted, script uses the resolved `worktree_name`

## Usage

### Create or reset a slot
```bash
python3 /Users/slobodan/.codex/skills/workstation-preparation/scripts/prepare_workstation.py \
  --repo-root /path/to/repo \
  --worktree-name workstation-3 \
  --branch-name workstation-3
```

### Auto-select next free standardized slot
```bash
python3 /Users/slobodan/.codex/skills/workstation-preparation/scripts/prepare_workstation.py \
  --repo-root /path/to/repo
```

### Use explicit base ref
```bash
python3 /Users/slobodan/.codex/skills/workstation-preparation/scripts/prepare_workstation.py \
  --repo-root /path/to/repo \
  --worktree-name workstation-4 \
  --branch-name workstation-4 \
  --base-ref origin/main
```

### Force reset existing slot (destructive cleanup)
```bash
python3 /Users/slobodan/.codex/skills/workstation-preparation/scripts/prepare_workstation.py \
  --repo-root /path/to/repo \
  --worktree-name workstation-2 \
  --branch-name workstation-2 \
  --force-reset-existing
```

## Notes

- If slot already exists and contains local changes/diverged commits, command fails unless `--force-reset-existing` is passed.
- New slots are created next to the repository root by default (sibling directory). Override with `--worktrees-parent` when needed.
