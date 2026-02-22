# Usage Template

## Blank Template
```text
Agent: sprint-orchestrator-agent
Goal: Monitor and update execution of existing sprint issues, enforce dependency order, and drive continuous worker dispatch.
Inputs: Sprint task source:
Inputs: Agent root path: /agents
Inputs: Standards source: /agents/agent-making-agent/README.md
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: dispatch_skill_path: $env:USERPROFILE/.codex/skills/thread-dispatch/SKILL.md
Inputs: sleep_skill_path: $env:USERPROFILE/.codex/skills/sleep/SKILL.md
Inputs: poll_interval_minutes: 5
Inputs: merge_mode: sequential
Inputs: review_required: false
Inputs: Team capacity constraints: max 3 developers + 1 tester + 1 reviewer
Inputs: Developer scaling rule: ready=1-2 -> 1 dev, ready=3-10 -> 2 devs, ready>10 -> 3 devs
Inputs: Worker slot policy: dedicated worktree per slot; per-task feature branch inside each slot worktree
Inputs: Start gates: tester starts after first developer DONE, reviewer starts after first tester DONE
Constraints: Planning/orchestration only. No implementation coding. Use thread-dispatch skill to spawn background workers and sleep skill for 5-minute loop waits. Publish packet-driven assignments and monitor AGENT_EVENT_V1 status comments. Before each sleep, post visible control summary in this orchestrator chat (active workers, task per worker, blockers, next actions).
Output: /reports/SPRINT_PLAN.md, /reports/SPRINT_AGENT_ACTIVATIONS.md, /reports/SPRINT_EXECUTION_LOG.md, /reports/SPRINT_MERGE_PLAN.md, /reports/SPRINT_MERGE_RESULT.md
```

## Filled Example
```text
Agent: sprint-orchestrator-agent
Goal: Orchestrate and continuously dispatch MYO-45..MYO-70 with adaptive worker concurrency and strict dependency ordering.
Inputs: Sprint task source: Linear project "Ouroboros" team "Myownmint" issues MYO-45..MYO-70
Inputs: Agent root path: C:/Users/<username>/Projects/Agents/agents
Inputs: Standards source: C:/Users/<username>/Projects/Agents/agents/agent-making-agent/README.md
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: dispatch_skill_path: $env:USERPROFILE/.codex/skills/thread-dispatch/SKILL.md
Inputs: sleep_skill_path: $env:USERPROFILE/.codex/skills/sleep/SKILL.md
Inputs: poll_interval_minutes: 5
Inputs: merge_mode: sequential
Inputs: review_required: false
Inputs: Team capacity constraints: max 3 developers + 1 tester + 1 reviewer
Inputs: Developer scaling rule: ready=1-2 -> 1 dev, ready=3-10 -> 2 devs, ready>10 -> 3 devs
Inputs: Worker slot policy: dedicated worktrees `C:/Users/<username>/Projects/Oroboros/.worktrees/dev-1|dev-2|dev-3|test-1|review-1`; task branches `codex/<slot>/<issue-id>`
Inputs: Start gates: tester starts after first developer DONE, reviewer starts after first tester DONE
Constraints: Planning/orchestration only. No implementation coding. Launch background workers via thread-dispatch skill and use sleep skill for 5-minute loop. Keep assignments packet-driven on Linear comments. Before every sleep cycle, post visible control summary with worker health and next dispatch.
Output: C:/Users/<username>/Projects/Oroboros/reports/SPRINT_PLAN.md, C:/Users/<username>/Projects/Oroboros/reports/SPRINT_AGENT_ACTIVATIONS.md, C:/Users/<username>/Projects/Oroboros/reports/SPRINT_EXECUTION_LOG.md, C:/Users/<username>/Projects/Oroboros/reports/SPRINT_MERGE_PLAN.md, C:/Users/<username>/Projects/Oroboros/reports/SPRINT_MERGE_RESULT.md
```
