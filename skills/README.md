# Project Skills Catalog

This folder stores portable skill definitions used by agents in this repository.

## Included Skills
- `codex-rate-snapshot`
- `figma`
- `figma-implement-design`
- `linear`
- `pdf`
- `playwright`
- `screenshot`
- `sleep`
- `speech`
- `spreadsheet`
- `skill-creator`
- `skill-installer`
- `thread-dispatch`
- `workstation-preparation`

## Install To Codex Runtime
For a missing skill `<skill-name>`, copy its folder into `$env:CODEX_HOME/skills/` (usually `$env:USERPROFILE/.codex/skills/`):

```powershell
if (-not $env:CODEX_HOME) { $env:CODEX_HOME = "$env:USERPROFILE/.codex" }
New-Item -ItemType Directory -Force -Path "$env:CODEX_HOME/skills" | Out-Null
Copy-Item -Recurse -Force "<repo-root>/skills/<skill-name>" "$env:CODEX_HOME/skills/<skill-name>"
```

For curated OpenAI skills, you can also use `skill-installer`.

After any skill install, restart Codex so the skill is available in new runs.
