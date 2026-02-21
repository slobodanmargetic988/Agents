# Usage Template

## Blank Template
```text
Agent: agent-making-agent
Goal: New agent to create:
Inputs: Use /agents/agent-making-agent/README.md as the standards source.
Inputs: Additional context:
Constraints: Documentation only, no code edits.
Output: four files in the new agent folder: README.md + USAGE_TEMPLATE.md + EXAMPLES.md + USER_GUIDE.html
```

## Filled Example
```text
Agent: agent-making-agent
Goal: Define a new agent that drafts release notes from merged pull requests.
Inputs: Use /agents/agent-making-agent/README.md as the standards source.
Inputs: Additional context: release notes should group changes by feature area.
Constraints: Documentation only, no code edits.
Output: New agent package with README.md (required sections, hard gates, visible rubric), USAGE_TEMPLATE.md (blank + filled templates), EXAMPLES.md (at least 2 diverse input/output examples + adaptation guidance), and USER_GUIDE.html (polished responsive onboarding page similar quality to Optimus guides).
```
