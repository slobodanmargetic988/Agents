---
name: "playwright"
description: "Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via playwright-cli."
---


# Playwright CLI Skill (Windows)

Windows-first guide for browser automation from terminal.

## Prerequisite check

```powershell
Get-Command npx -ErrorAction SilentlyContinue
```

If `npx` is missing, install Node.js first.

## One-time helper function (current shell)

```powershell
function pwcli { npx --yes --package @playwright/cli playwright-cli @Args }
```

## Quick start

```powershell
pwcli open https://playwright.dev --headed
pwcli snapshot
pwcli click e15
pwcli type "Playwright"
pwcli press Enter
pwcli screenshot
```

## Core loop

1. Open page.
2. Snapshot to get refs (`e1`, `e2`, ...).
3. Interact.
4. Snapshot again after UI changes or navigation.
5. Save artifacts if needed.

```powershell
pwcli open https://example.com
pwcli snapshot
pwcli click e3
pwcli snapshot
```

## Patterns

### Form fill

```powershell
pwcli open https://example.com/form
pwcli snapshot
pwcli fill e1 "user@example.com"
pwcli fill e2 "password123"
pwcli click e3
pwcli snapshot
```

### Trace a flaky flow

```powershell
pwcli open https://example.com --headed
pwcli tracing-start
# interactions
pwcli tracing-stop
```

### Multi-tab

```powershell
pwcli tab-new https://example.com
pwcli tab-list
pwcli tab-select 0
pwcli snapshot
```

## Guardrails

- Always snapshot before using element refs.
- Re-snapshot after navigation or major DOM changes.
- Prefer explicit commands; avoid `eval` unless necessary.
- For artifacts in this repo, use `output/playwright/`.
