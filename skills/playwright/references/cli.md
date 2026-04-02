# Playwright CLI Quick Reference

Use the bundled wrapper:

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export PWCLI="$CODEX_HOME/skills/playwright/scripts/playwright_cli.sh"
```

Common commands:

```bash
"$PWCLI" open https://example.com --headed
"$PWCLI" snapshot
"$PWCLI" click e3
"$PWCLI" fill e5 "hello@example.com"
"$PWCLI" press Enter
"$PWCLI" screenshot
"$PWCLI" tracing-start
"$PWCLI" tracing-stop
"$PWCLI" tab-list
"$PWCLI" tab-select 0
```

Always take a fresh `snapshot` before using element refs such as `e3`.
