---
name: gitnexus-workflows
description: "Use when a task should probably use GitNexus but it is not yet clear which GitNexus workflow fits best. Routes the task to exploring, debugging, impact analysis, refactoring, PR review, or CLI maintenance."
---

# GitNexus Workflows

Use this skill as the entrypoint when GitNexus is relevant but the exact GitNexus skill is not obvious yet.

## First Step

Always start by identifying the indexed repo:

1. Read `gitnexus://repos` or call `list_repos`
2. Read `gitnexus://repo/{name}/context`
3. Then route to the best workflow below

## Routing Guide

### Use `gitnexus-exploring`

When the user wants to understand:

- how a feature works
- where logic lives
- what calls a symbol
- what the main modules or flows are

### Use `gitnexus-debugging`

When the user wants to know:

- why something is failing
- where an error comes from
- what path leads to a bad runtime behavior

### Use `gitnexus-impact-analysis`

When the user wants to know:

- what depends on a symbol
- what might break if code changes
- what tests or flows should be revisited before editing

### Use `gitnexus-refactoring`

When the user wants to:

- rename a symbol
- split or extract a module
- restructure code safely

### Use `gitnexus-pr-review`

When the user wants to:

- review a PR or diff
- assess merge risk
- find missing caller updates or missing tests

### Use `gitnexus-cli`

When the job is to:

- index or refresh a repo
- clean or rebuild a broken index
- list indexed repos
- maintain the GitNexus installation rather than query it

## Quick Decision Rules

- "How does this work?" -> `gitnexus-exploring`
- "Why is this broken?" -> `gitnexus-debugging`
- "What breaks if I change this?" -> `gitnexus-impact-analysis`
- "Refactor or rename this safely" -> `gitnexus-refactoring`
- "Review this diff or PR" -> `gitnexus-pr-review`
- "Refresh or manage the graph" -> `gitnexus-cli`

## Tool Order Preference

Inside the chosen workflow, prefer this order unless the task clearly needs something else:

1. `list_repos` or `gitnexus://repos`
2. `gitnexus://repo/{name}/context`
3. `query`, `context`, or `impact`
4. `detect_changes` or `rename` when the task becomes change-oriented
5. `cypher` only for advanced structural questions

## Practical Guardrails

- Do not jump to `cypher` first
- Do not read large amounts of source before using the graph to narrow the area
- Re-index with `gitnexus analyze` if the repo context says the index is stale
- In this setup, Codex reaches GitNexus through the backend server, so keep `gitnexus serve` running when MCP access is needed
