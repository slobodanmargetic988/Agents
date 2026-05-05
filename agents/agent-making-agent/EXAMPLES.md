# Examples

Use these as starting points. Review them carefully and adapt goals, inputs, and constraints to your own project.

## Example 1: Create a Testing Agent

### Input
```text
Agent: agent-making-agent
Goal: New agent to create: test-plan-agent
Inputs: Use /agents/agent-making-agent/README.md as the standards source.
Inputs: Additional context: focus test plans on API and DB changes.
Constraints: Documentation only, no code edits.
Output: four files in the new agent folder: README.md + USAGE_TEMPLATE.md + EXAMPLES.md + USER_GUIDE.html
```

### Expected Output
```text
Creates /agents/test-plan-agent/README.md, /agents/test-plan-agent/USAGE_TEMPLATE.md, /agents/test-plan-agent/EXAMPLES.md, and /agents/test-plan-agent/USER_GUIDE.html.
README.md includes required sections, hard gates, timestamp, and rubric.
USAGE_TEMPLATE.md is append-only and portable.
EXAMPLES.md has at least two diverse input/output examples and adaptation guidance.
USER_GUIDE.html is polished, responsive, and gives clear onboarding + quick-start usage.
```

## Example 2: Improve an Existing Agent

### Input
```text
Agent: agent-making-agent
Goal: Upgrade /agents/deployment-agent/ to match current standards.
Inputs: Existing files in /agents/deployment-agent/ and /agents/agent-making-agent/README.md.
Constraints: Keep original mission intact; only documentation changes.
Output: four-file compliant package for deployment-agent.
```

### Expected Output
```text
Updates deployment-agent to include README.md, USAGE_TEMPLATE.md, EXAMPLES.md, and USER_GUIDE.html.
Adds missing hard-gate requirements and rubric visibility.
Rewrites usage template to append-only format with portable paths.
Provides diverse examples with user adaptation note.
Adds a polished responsive USER_GUIDE.html aligned to Optimus visual quality baseline.
```
