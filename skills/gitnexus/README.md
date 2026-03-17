# GitNexus Skill Bundle

This folder groups the shared GitNexus workflow skills for Earth collaborators.

Included skills:

- `gitnexus-workflows`
- `gitnexus-guide`
- `gitnexus-exploring`
- `gitnexus-debugging`
- `gitnexus-impact-analysis`
- `gitnexus-refactoring`
- `gitnexus-pr-review`
- `gitnexus-cli`

These skills assume:

1. GitNexus is installed and repositories have been indexed.
2. GitNexus MCP is configured for the agent/runtime that will use the skills.
3. In the current Earth/Codex setup, GitNexus MCP is exposed through the local backend server:

```bash
caffeinate -dimsu gitnexus serve
```

The skills are written in a Codex-friendly style and avoid Claude-specific hook assumptions.
