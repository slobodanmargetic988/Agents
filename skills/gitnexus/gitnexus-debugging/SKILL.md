---
name: gitnexus-debugging
description: "Use when the user is tracing a bug, error path, unexpected behavior, or runtime failure. Examples: \"Why is this failing?\", \"Where does this error come from?\", \"Trace this bug\"."
---

# GitNexus Debugging

Use GitNexus to narrow the suspect area before reading a lot of files.

## Workflow

1. Read `gitnexus://repo/{name}/context` to confirm the repo and freshness.
2. Use `query` with the error text, symptom, or feature name.
3. Use `context` on the most relevant returned symbol.
4. Read `gitnexus://repo/{name}/process/{processName}` when a returned process looks promising.
5. Use `cypher` only when the normal tools cannot express the path you need.
6. Confirm the root cause in source files and tests.

## Checklist

- [ ] Confirm which indexed repo you are debugging
- [ ] `query` for the symptom, error string, or affected feature
- [ ] `context` on likely suspect symbols
- [ ] Inspect one or two execution flows, not all of them
- [ ] Use `cypher` only for custom path tracing
- [ ] Confirm the finding in code before concluding

## Tool Mapping

- `query`: best first pass for "what area/process is this likely in?"
- `context`: best for callers, callees, imports, and process participation
- `cypher`: best for custom graph traversal when you already know what you want
- `detect_changes`: useful if the bug is likely tied to recent edits

## Common Patterns

### Trace an error

1. `query` with the error text or failing feature.
2. Pick the most relevant process or symbol.
3. `context` on that symbol.
4. Read the source files for confirmation.

### Trace a bad return value

1. `context` on the function producing the value.
2. Inspect its outgoing calls and related process.
3. Follow the data-producing callee, not every caller.

### Trace a regression

1. Use `detect_changes` on the repo if there are local edits.
2. Use `impact` or `context` on changed high-risk symbols.
3. Verify whether the change touched the failing execution flow.
