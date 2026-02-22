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

- Preferred runtime path:
  - `"$env:CODEX_HOME/skills/thread-dispatch/scripts/dispatch_codex_run.py"`
- Repo-local alternative (when running from this repo root):
  - `"./skills/thread-dispatch/scripts/dispatch_codex_run.py"`

## Inputs

- Required:
  - `cwd`
  - `prompt` or `prompt_file`
- Optional:
  - `codex_home` (custom `CODEX_HOME` path for spawned Codex process, e.g. `$env:USERPROFILE/.codex-second`, `$env:USERPROFILE/.codex-third`)
  - `disable_all_mcp` (disable all MCP servers defined in target profile `config.toml`)
  - `enable_only_mcp` (repeatable; disable all configured MCP servers except the listed names)
  - `foreground` / `background`
  - `full_auto` override
  - `log_dir`
  - `extra_arg` (repeatable)
  - `dry_run`

## Usage

Set script paths once (runtime-path preferred; repo-local fallback shown in comments):

```powershell
if (-not $env:CODEX_HOME) { $env:CODEX_HOME = "$env:USERPROFILE/.codex" }
$DISPATCH_SCRIPT = "$env:CODEX_HOME/skills/thread-dispatch/scripts/dispatch_codex_run.py"
# $DISPATCH_SCRIPT = "./skills/thread-dispatch/scripts/dispatch_codex_run.py"
```

### 1) Dispatch with inline prompt (background)

```powershell
python "$DISPATCH_SCRIPT" `
  --cwd C:/Users/<username>/Projects/Oroboros `
  --prompt "Review open Linear blockers and write a concise summary." `
  --background
```

### 2) Dispatch prompt from file (background)

```powershell
python "$DISPATCH_SCRIPT" `
  --cwd C:/Users/<username>/Projects/Oroboros `
  --prompt-file C:/Users/<username>/Projects/Oroboros/tmp/worker_prompt.txt `
  --background
```

### 3) Foreground run (stream to current terminal)

```powershell
python "$DISPATCH_SCRIPT" `
  --cwd C:/Users/<username>/Projects/Oroboros `
  --prompt "Summarize test failures in backend logs." `
  --foreground
```

### 4) Use a different Codex profile (`CODEX_HOME`) via PowerShell env var

This is useful when you want parallel Codex setups with different skills/customization.
Treat the profile path as a parameter (`codex_home`), not a fixed value.

```powershell
$env:CODEX_HOME = "$env:USERPROFILE/.codex-<profile-name>"
python "$env:CODEX_HOME/skills/thread-dispatch/scripts/dispatch_codex_run.py" `
  --cwd C:/Users/<username>/Projects/Oroboros `
  --prompt "Your prompt here" `
  --background
```

### 5) Use a different Codex profile via `--codex-home`

Equivalent to the shell-prefix approach above, but explicit in the script args.

```powershell
python "$DISPATCH_SCRIPT" `
  --cwd C:/Users/<username>/Projects/Oroboros `
  --prompt "Your prompt here" `
  --background `
  --codex-home "$env:USERPROFILE/.codex-<profile-name>"
```

### 6) Disable all MCP servers for spawned run (reads target profile `config.toml`)

```powershell
python "$DISPATCH_SCRIPT" `
  --cwd C:/Users/<username>/Projects/Oroboros `
  --prompt "Your prompt here" `
  --background `
  --codex-home "$env:USERPROFILE/.codex-second" `
  --disable-all-mcp
```

Equivalent spawned Codex command will include generated `-c 'mcp_servers.<name>.enabled=false'` overrides for every MCP defined in the selected profile.

### 7) Enable only specific MCP servers (disable all others)

```powershell
python "$DISPATCH_SCRIPT" `
  --cwd C:/Users/<username>/Projects/Oroboros `
  --prompt "Use Linear only for this task." `
  --background `
  --codex-home "$env:USERPROFILE/.codex-second" `
  --enable-only-mcp linear `
  --enable-only-mcp linear_sse
```

## Behavior Notes

- Default mode is detached/background.
- Detached runs write logs into `<cwd>/.codex-dispatch/`.
- Use `--full-auto` by default. Add `--no-full-auto` to disable.
- Use `--dry-run` to print the exact command without starting it.
- The script inherits environment variables from the current shell, so `$env:CODEX_HOME` is passed to the spawned `codex exec`.
- `--codex-home` is available when you want the skill command itself to set the spawned Codex profile explicitly.
- `--disable-all-mcp` and `--enable-only-mcp` read the target profile's `config.toml` (under the effective `CODEX_HOME`) to discover configured MCP names, then generate `-c mcp_servers.<name>.enabled=false` overrides.
- The MCP modes are mutually exclusive.
- If `--enable-only-mcp` names an MCP not defined in the target profile `config.toml`, the command fails with a validation error.
- Use `--dry-run` to inspect generated `mcp_disable_overrides` before launching.
- When using this skill from another agent, pass `codex_home` as an explicit input/parameter when you want a non-default Codex profile.
- When using this skill from another agent, pass MCP mode explicitly when you want low-overhead worker runs (for example disable all MCPs for simple coding/review tasks).

## Windows note

Use `dispatch_codex_run.py` only.  
The desktop-thread helper is macOS-only and not part of this Windows branch workflow.
