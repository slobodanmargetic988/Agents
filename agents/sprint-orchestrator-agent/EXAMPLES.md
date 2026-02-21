# Examples

## Example 1: Adaptive Overnight Orchestration

### Input
```text
Agent: sprint-orchestrator-agent
Goal: Keep sprint execution moving overnight with background workers and 5-minute control cycles.
Inputs: Sprint task source: Linear project "Ouroboros" issues MYO-45..MYO-70
Inputs: tracking_mode: linear
Inputs: dispatch_skill_path: /Users/slobodan/.codex/skills/thread-dispatch/SKILL.md
Inputs: sleep_skill_path: /Users/slobodan/.codex/skills/sleep/SKILL.md
Inputs: poll_interval_minutes: 5
Inputs: Developer scaling rule: ready=1-2 -> 1 dev, ready=3-10 -> 2 devs, ready>10 -> 3 devs
Inputs: Worker slot policy: dedicated worktree per slot + per-task feature branch
Inputs: Start gates: tester after first dev DONE, reviewer after first tester DONE
Constraints: Planning/orchestration only. Launch and monitor background workers; no implementation coding.
Output: /reports/SPRINT_PLAN.md, /reports/SPRINT_AGENT_ACTIVATIONS.md, /reports/SPRINT_EXECUTION_LOG.md, /reports/SPRINT_MERGE_PLAN.md, /reports/SPRINT_MERGE_RESULT.md
```

### Expected Output
```text
Orchestrator computes ready queue, starts only required number of developer workers, and scales up/down as queue changes.
Tester is started only after first developer completion handoff is recorded.
Reviewer is started only after first tester completion handoff is recorded.
Every 5 minutes orchestrator posts control summary in visible chat and refreshes report snapshots.
```

## Example 2: Small Queue, Minimal Parallelism

### Input
```text
Agent: sprint-orchestrator-agent
Goal: Orchestrate only four ready tasks safely with minimal concurrency.
Inputs: Sprint task source: MYO-81..MYO-84
Inputs: tracking_mode: linear
Inputs: poll_interval_minutes: 5
Inputs: Developer scaling rule: ready=1-2 -> 1 dev, ready=3-10 -> 2 devs, ready>10 -> 3 devs
Constraints: Keep dependency order strict; no coding work in orchestrator.
Output: /reports/SPRINT_PLAN.md, /reports/SPRINT_AGENT_ACTIVATIONS.md, /reports/SPRINT_EXECUTION_LOG.md, /reports/SPRINT_MERGE_PLAN.md, /reports/SPRINT_MERGE_RESULT.md
```

### Expected Output
```text
Orchestrator starts exactly two developers (not three), because ready tasks are between 3 and 10.
Each developer is assigned a dedicated worktree and per-task feature branch.
Tester and reviewer start only after their gate events are satisfied.
```
