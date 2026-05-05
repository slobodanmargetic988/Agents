---
name: gitnexus-exploring
description: "Use when the user wants to understand architecture, execution flow, main modules, or unfamiliar code. Examples: \"How does X work?\", \"What calls this function?\", \"Show me the auth flow\"."
---

# GitNexus Exploring

Use this skill when the goal is orientation, not editing.

## Workflow

1. Read `gitnexus://repos` if the target repo is not already obvious.
2. Read `gitnexus://repo/{name}/context`.
3. If needed, read `gitnexus://repo/{name}/clusters` or `gitnexus://repo/{name}/processes`.
4. Use `query` for the feature or concept.
5. Use `context` on the key returned symbol.
6. Read the source files for implementation detail only after the graph has narrowed the area.

## Checklist

- [ ] Identify the correct repo
- [ ] Read repo context first
- [ ] Use `query` to find execution flows or relevant symbols
- [ ] Use `context` to inspect the best symbol from the results
- [ ] Read one process trace if behavior flow matters
- [ ] Then read code

## When To Reach For Which Resource

- `gitnexus://repo/{name}/context`: start here every time
- `gitnexus://repo/{name}/clusters`: use for module overview
- `gitnexus://repo/{name}/processes`: use for runtime/flow overview
- `gitnexus://repo/{name}/process/{processName}`: use for one concrete execution path

## Tool Mapping

- `query`: "show me the code related to this concept"
- `context`: "show me the real neighborhood of this symbol"
- `cypher`: only when you need a custom structural question

## Good Use Cases

- onboarding to a repo
- understanding where a feature lives
- tracing an execution path before a change
- mapping a subsystem before refactoring
