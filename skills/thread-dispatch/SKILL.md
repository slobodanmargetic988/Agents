---
name: thread-dispatch
description: Launch a separate Codex execution from the current thread by passing a prompt and target workspace. Use when you want this thread to delegate work to another autonomous Codex run without manual copy/paste into another chat thread.
---

# Thread Dispatch

## Overview

Use this skill to dispatch work as a separate Codex process.
It is best for long-running tasks or parallel work where the current thread should continue independently.

## Scope

- Starts a separate `codex exec` run.
- Accepts prompt text directly or from file.
- Supports detached/background mode with log capture.
- Does not directly create or control a GUI chat thread in Codex Desktop.

## Script

`/Users/slobodan/.codex/skills/thread-dispatch/scripts/dispatch_codex_run.py`
`/Users/slobodan/.codex/skills/thread-dispatch/scripts/dispatch_codex_desktop_thread.py`

## Inputs

- Required:
  - `cwd`
  - `prompt` or `prompt_file`
- Optional:
  - `codex_home` (custom `CODEX_HOME` path for spawned Codex process, e.g. `~/.codex-second`, `~/.codex-third`)
  - `foreground` / `background`
  - `full_auto` override
  - `log_dir`
  - `extra_arg` (repeatable)
  - `dry_run`

## Usage

### 1) Dispatch with inline prompt (background)

```bash
python3 /Users/slobodan/.codex/skills/thread-dispatch/scripts/dispatch_codex_run.py \
  --cwd /Users/slobodan/Projects/Oroboros \
  --prompt "Review open Linear blockers and write a concise summary." \
  --background
```

### 2) Dispatch prompt from file (background)

```bash
python3 /Users/slobodan/.codex/skills/thread-dispatch/scripts/dispatch_codex_run.py \
  --cwd /Users/slobodan/Projects/Oroboros \
  --prompt-file /Users/slobodan/Projects/Oroboros/tmp/worker_prompt.txt \
  --background
```

### 3) Foreground run (stream to current terminal)

```bash
python3 /Users/slobodan/.codex/skills/thread-dispatch/scripts/dispatch_codex_run.py \
  --cwd /Users/slobodan/Projects/Oroboros \
  --prompt "Summarize test failures in backend logs." \
  --foreground
```

### 4) Use a different Codex profile (`CODEX_HOME`) via shell prefix

This is useful when you want parallel Codex setups with different skills/customization.
Treat the profile path as a parameter (`codex_home`), not a fixed value.

```bash
CODEX_HOME="$HOME/.codex-<profile-name>" \
python3 /Users/slobodan/.codex/skills/thread-dispatch/scripts/dispatch_codex_run.py \
  --cwd /Users/slobodan/Projects/Oroboros \
  --prompt "Your prompt here" \
  --background
```

### 5) Use a different Codex profile via `--codex-home`

Equivalent to the shell-prefix approach above, but explicit in the script args.

```bash
python3 /Users/slobodan/.codex/skills/thread-dispatch/scripts/dispatch_codex_run.py \
  --cwd /Users/slobodan/Projects/Oroboros \
  --prompt "Your prompt here" \
  --background \
  --codex-home "$HOME/.codex-<profile-name>"
```

## Behavior Notes

- Default mode is detached/background.
- Detached runs write logs into `<cwd>/.codex-dispatch/`.
- Use `--full-auto` by default. Add `--no-full-auto` to disable.
- Use `--dry-run` to print the exact command without starting it.
- The script inherits environment variables from the current shell, so `CODEX_HOME=...` prefixes are passed to the spawned `codex exec`.
- `--codex-home` is available when you want the skill command itself to set the spawned Codex profile explicitly.
- When using this skill from another agent, pass `codex_home` as an explicit input/parameter when you want a non-default Codex profile.

## Visible Desktop Thread Mode (macOS)

To create a visible Codex Desktop chat thread:

```bash
python3 /Users/slobodan/.codex/skills/thread-dispatch/scripts/dispatch_codex_desktop_thread.py \
  --prompt "just say good day back to me"
```

From file:

```bash
python3 /Users/slobodan/.codex/skills/thread-dispatch/scripts/dispatch_codex_desktop_thread.py \
  --prompt-file /Users/slobodan/Projects/Oroboros/tmp/prompt.txt
```

Notes:
- Requires macOS `osascript` and Accessibility permission for terminal/Codex automation.
- Uses `Cmd+N`, paste clipboard, then Enter.
- Use `--no-send` to open/paste without sending.
