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

## Behavior Notes

- Default mode is detached/background.
- Detached runs write logs into `<cwd>/.codex-dispatch/`.
- Use `--full-auto` by default. Add `--no-full-auto` to disable.
- Use `--dry-run` to print the exact command without starting it.

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
