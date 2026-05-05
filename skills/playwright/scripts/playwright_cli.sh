#!/usr/bin/env bash
set -euo pipefail

timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

log_line() {
  printf "%s [playwright-cli-wrapper] %s\n" "$(timestamp)" "$*" >&2
}

if ! command -v npx >/dev/null 2>&1; then
  log_line "npx is not available. Install Node.js and npm before using this wrapper."
  exit 1
fi

if [[ $# -eq 0 ]]; then
  log_line "No Playwright CLI arguments were provided. Showing help."
fi

log_line "Launching Playwright CLI through npx."
exec npx --yes --package @playwright/cli@latest playwright-cli "$@"
