---
name: custom-thread-spawner
description: Spawn ready-to-open Codex Desktop worker threads by writing valid session JSONL files into ~/.codex/sessions/YYYY/MM/DD with correct IDs, timestamps, and seeded transcript events. Includes bundled starter templates for `optimus-prime` (full app-development orchestrator) and `project-planner` (documentation/plan priming before task breakdown), plus custom file/text overrides.
metadata:
  short-description: Spawn Codex Desktop worker threads with bundled starters
---

# Custom Thread Spawner

## Overview

This skill writes a new Codex Desktop session file with:
- Auto-generated thread/session ID (`UUID` format)
- Auto-generated turn ID
- Auto-generated filename `rollout-<timestamp>-<thread-id>.jsonl`
- Auto-generated path `~/.codex/sessions/YYYY/MM/DD/`
- Timestamps seeded from `now - 30s` (default) and spread forward monotonically
- Full transcript event shape by default (`full-template`) so the UI does not show stuck "thinking"
- Optional one-flag starter-template presets that auto-load base instructions + personalization + tools descriptions

Default output mode is `full-template` (17 lines). This is the safe mode for normal use because it includes the completion events/response items that prevent the UI from looking like it is still thinking.

`minimum-visible` (11 lines) is still available for debugging, but may leave the seeded answer looking permanently in-progress in Codex Desktop.

## Bundled Starter Templates

- `optimus-prime`: Full app development orchestrator starter for autonomous multi-worker execution, blocker handling, and continuous cycle-based delivery.
- `project-planner`: Planning-first starter used to prime project documentation, feature definitions, and planning quality before turning work into implementation tasks.

## Script

Local repo path:
- `/Users/slobodan/Projects/Agents/skills/custom-thread-spawner/scripts/custom_thread_spawner.py`

Installed skill path (after copy to `~/.codex/skills`):
- `/Users/slobodan/.codex/skills/custom-thread-spawner/scripts/custom_thread_spawner.py`

## Required Inputs

Required (custom mode):
- `--core-base-instructions-text` or `--core-base-instructions-file`
- `--user-personalization-text` or `--user-personalization-file`

Usually also provide:
- `--tools-descriptions-and-when-to-use-text` or `--tools-descriptions-and-when-to-use-file`
  - If omitted, it defaults to the `user-personalization` value.

Shorthand mode:
- `--starter-template optimus-prime` or `--starter-template project-planner`
- `--cwd` is optional and defaults to the current working directory (`PWD`)

## Defaults

- `application-context`: defaults to the captured Codex Desktop app-context from the sample thread
- `first-actual-user-message`: defaults to `initialize`
- `first-actual-ai-response`: defaults to `initialized`
- `permissions-set`: defaults to captured full-access permissions block from sample
- `cwd`: defaults to current working directory if `--cwd` is omitted
- `git` metadata: autodetected from resolved `cwd` if omitted

## Usage

### Dry run (preview file path / IDs)

```bash
python3 /Users/slobodan/Projects/Agents/skills/custom-thread-spawner/scripts/custom_thread_spawner.py \
  --cwd /Users/slobodan/Projects/ThreadSeeder \
  --core-base-instructions-file /Users/slobodan/Projects/ThreadSeeder/base_instructions/optimus-prime.txt \
  --user-personalization-text "User preferences go here." \
  --tools-descriptions-and-when-to-use-text "Tool usage instructions go here." \
  --dry-run
```

### Shorthand (spawn an Optimus Prime thread in the current project directory)

```bash
python3 /Users/slobodan/Projects/Agents/skills/custom-thread-spawner/scripts/custom_thread_spawner.py \
  --starter-template optimus-prime
```

### Shorthand (spawn a Project Planner thread in the current project directory)

```bash
python3 /Users/slobodan/Projects/Agents/skills/custom-thread-spawner/scripts/custom_thread_spawner.py \
  --starter-template project-planner
```

### Write a new thread into `~/.codex/sessions/...`

```bash
python3 /Users/slobodan/Projects/Agents/skills/custom-thread-spawner/scripts/custom_thread_spawner.py \
  --cwd /Users/slobodan/Projects/ThreadSeeder \
  --core-base-instructions-file /Users/slobodan/Projects/ThreadSeeder/base_instructions/optimus-prime.txt \
  --user-personalization-file /path/to/user-personalization.txt \
  --tools-descriptions-and-when-to-use-file /path/to/tools-instructions.txt \
  --first-actual-user-message-text "initialize" \
  --first-actual-ai-response-text "initialized"
```

### Full template mode (17 lines, default)

```bash
python3 /Users/slobodan/Projects/Agents/skills/custom-thread-spawner/scripts/custom_thread_spawner.py \
  --cwd /Users/slobodan/Projects/ThreadSeeder \
  --core-base-instructions-file /Users/slobodan/Projects/ThreadSeeder/base_instructions/optimus-prime.txt \
  --user-personalization-text "..." \
  --tools-descriptions-and-when-to-use-text "..."
```

### Minimum-visible mode (experimental/debug)

```bash
python3 /Users/slobodan/Projects/Agents/skills/custom-thread-spawner/scripts/custom_thread_spawner.py \
  --mode minimum-visible \
  --cwd /Users/slobodan/Projects/ThreadSeeder \
  --core-base-instructions-file /Users/slobodan/Projects/ThreadSeeder/base_instructions/optimus-prime.txt \
  --user-personalization-text "..." \
  --tools-descriptions-and-when-to-use-text "..."
```

## Notes

- The script preserves the session identity invariant: filename thread ID == `session_meta.payload.id`.
- The generated filename timestamp uses the same UTC second as the first JSONL line timestamp so they match.
- `--starter-template` only fills the 3 primary text inputs; you can still override any of them explicitly with `--*-text` or `--*-file`.
- Template/source files used by the skill are bundled in:
  - `/Users/slobodan/Projects/Agents/skills/custom-thread-spawner/assets/`
  - `/Users/slobodan/Projects/Agents/skills/custom-thread-spawner/references/`
