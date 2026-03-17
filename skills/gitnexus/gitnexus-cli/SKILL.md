---
name: gitnexus-cli
description: "Use when the user needs GitNexus terminal commands: index or refresh a repo, list indexed repos, clean broken indexes, or generate GitNexus docs. Examples: \"Index this repo\", \"Refresh the graph\", \"List indexed repos\"."
---

# GitNexus CLI

Use this skill when the job is about maintaining or refreshing the GitNexus index itself rather than querying it through MCP.

## This Setup

- Prefer the globally installed `gitnexus` binary over `npx`.
- In this environment, Codex uses GitNexus through the HTTP MCP endpoint, so keep the backend running when MCP access is needed:

```bash
caffeinate -dimsu gitnexus serve
```

## Core Commands

### Index or refresh a repo

```bash
gitnexus analyze
gitnexus analyze --force
```

Run from the repo root or point it at a specific path. Use `--force` when the index looks corrupt or badly stale.

### List indexed repos

```bash
gitnexus list
```

Use this first if you are not sure what GitNexus already knows about.

### Clean an index

```bash
gitnexus clean
gitnexus clean --force
```

Use when `.gitnexus/` is broken and you want to rebuild from scratch.

### Generate wiki/docs from the graph

```bash
gitnexus wiki
```

This is optional and slower. Use only when the user actually wants generated docs.

## Normal Workflow

1. Run `gitnexus list` or inspect `gitnexus://repos`.
2. If the target repo is missing or stale, run `gitnexus analyze`.
3. Re-check with `gitnexus://repo/{name}/context`.
4. Then switch to the GitNexus MCP skills for exploring, debugging, impact analysis, or refactoring.

## Refresh Triggers

Re-index after:

- a substantial merge
- a major refactor
- a branch switch you care about
- a long autonomous build that materially changed the codebase

Remember: GitNexus indexes a checked-out repo snapshot, not every branch automatically.

## Troubleshooting

- If the repo is not indexed, run `gitnexus analyze` from the repo root.
- If MCP cannot see the repo, verify the backend is running and the repo appears in `gitnexus list`.
- If the graph looks stale after code changes, re-run `gitnexus analyze`.
