---
name: gitnexus-guide
description: "Use when the user asks about GitNexus itself: available MCP tools, resources, graph schema, query strategy, or workflow selection. Examples: \"How do I use GitNexus?\", \"What tools does GitNexus expose?\"."
---

# GitNexus Guide

This is the quick reference skill for GitNexus in Codex.

## Start Here

For almost any GitNexus task:

1. Read `gitnexus://repos` or call `list_repos`
2. Read `gitnexus://repo/{name}/context`
3. Pick the right workflow skill:
   - `gitnexus-exploring`
   - `gitnexus-debugging`
   - `gitnexus-impact-analysis`
   - `gitnexus-refactoring`
   - `gitnexus-pr-review`
   - `gitnexus-cli`

## MCP Tools

- `list_repos`: list all indexed repos
- `query`: find execution flows and related symbols for a concept
- `context`: deep symbol neighborhood, callers, callees, and process membership
- `impact`: blast radius of a proposed change
- `detect_changes`: map changed files to affected flows and symbols
- `rename`: coordinated multi-file rename with preview support
- `cypher`: raw graph queries for advanced cases

## MCP Resources

- `gitnexus://repos`
- `gitnexus://setup`
- `gitnexus://repo/{name}/context`
- `gitnexus://repo/{name}/clusters`
- `gitnexus://repo/{name}/processes`
- `gitnexus://repo/{name}/schema`
- `gitnexus://repo/{name}/cluster/{clusterName}`
- `gitnexus://repo/{name}/process/{processName}`

## Practical Rules

- Prefer `query` and `context` before `cypher`
- Prefer `impact` before non-trivial refactors
- Prefer `detect_changes` before review or merge-risk analysis
- Re-index with `gitnexus analyze` when the repo context says the index is stale

## Graph Schema Reminder

The graph is code-centric:

- nodes include files, functions, classes, interfaces, methods, communities, and processes
- relationships are carried through `CodeRelation.type`
- common edge types include `CALLS`, `IMPORTS`, `EXTENDS`, `IMPLEMENTS`, `DEFINES`, `MEMBER_OF`, and `STEP_IN_PROCESS`

Use `gitnexus://repo/{name}/schema` before writing non-trivial Cypher.
