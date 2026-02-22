---
name: "screenshot"
description: "Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed."
---


# Screenshot Capture (Windows)

Use this Windows-focused workflow.

## Save location rules

1. If user gives a path, save there.
2. If user asks without a path, save to OS default screenshots location.
3. If Codex needs image for analysis, save to temp.

## Preferred method

Use the PowerShell helper:

```powershell
powershell -ExecutionPolicy Bypass -File <path-to-skill>/scripts/take_screenshot.ps1
```

## Common commands

### Default location

```powershell
powershell -ExecutionPolicy Bypass -File <path-to-skill>/scripts/take_screenshot.ps1
```

### Temp location

```powershell
powershell -ExecutionPolicy Bypass -File <path-to-skill>/scripts/take_screenshot.ps1 -Mode temp
```

### Explicit output path

```powershell
powershell -ExecutionPolicy Bypass -File <path-to-skill>/scripts/take_screenshot.ps1 -Path "C:\Temp\screen.png"
```

### Region capture (x,y,w,h)

```powershell
powershell -ExecutionPolicy Bypass -File <path-to-skill>/scripts/take_screenshot.ps1 -Mode temp -Region 100,200,800,600
```

### Active window capture

```powershell
powershell -ExecutionPolicy Bypass -File <path-to-skill>/scripts/take_screenshot.ps1 -Mode temp -ActiveWindow
```

### Specific window handle

```powershell
powershell -ExecutionPolicy Bypass -File <path-to-skill>/scripts/take_screenshot.ps1 -WindowHandle 123456
```

## Error handling

- If PowerShell execution policy blocks script execution, use `-ExecutionPolicy Bypass` for the command.
- If capture returns empty/black image, ensure target window is visible and not minimized.
- Always return saved file path(s) in your response.

## Scope note

This branch is Windows-oriented. macOS/Linux capture flows are intentionally omitted.
