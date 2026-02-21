# Usage Template

## Blank Template
```text
Agent: optimus-prime
Goal: Orchestrate mission completion in automated-handoff mode with cycle-based worker dispatch.
Inputs: primary_mission:
Inputs: task_source:
Inputs: repo_root:
Inputs: tracking_mode: automated-handoff
Inputs: agent_root_path: agents
Inputs: standards_source: agents/agent-making-agent/README.md
Inputs: worktree_policy_path: agents/_shared/WORKTREE_POLICY.md
Inputs: linear_workflow_path: agents/_shared/LINEAR_WORKFLOW.md
Inputs: sleep_minutes: 5
Inputs: max_initialized_workers: 10
Inputs: max_running_workers: 6
Inputs: worker_registry_path: reports/optimus-prime/WORKER_REGISTRY.json
Inputs: cycle_log_path: reports/optimus-prime/CYCLE_LOG.jsonl
Inputs: handoff_log_path: reports/optimus-prime/HANDOFF_LOG.jsonl
Inputs: linear_sync_log_path: reports/optimus-prime/LINEAR_SYNC_LOG.jsonl
Inputs: identity_checkpoint_path: reports/optimus-prime/IDENTITY_CHECKPOINT.md
Inputs: branch_lineage_path: reports/optimus-prime/BRANCH_LINEAGE.json
Inputs: packet_require_start_point: true
Inputs: developer_agent_path: agents/optimus-fullstack-developer/README.md
Inputs: tester_agent_path: agents/optimus-fullstack-tester/README.md
Inputs: reviewer_agent_path: agents/optimus-reviewer/README.md
Inputs: worker_role_policy: developers up to 3, testers up to 2, reviewer up to 1
Inputs: developer_scaling: ready 1-3 => 1 dev, ready 4-9 => 2 devs, ready >=10 => 3 devs
Inputs: concurrency_policy: developers do not get next task before test+review pass; testers wait for reviewer outcome before next task
Constraints: Optimus-only Linear updates. Workers do not use linear skill. Workers use minimum required skills only. Every worker packet must include start_from_branch and start_from_commit. Run in 5-minute cycles and skip sleep only while handling user steering.
Output: reports/optimus-prime runtime logs + worker prompt packets + synchronized Linear statuses/comments
```

## Filled Example
```text
Agent: optimus-prime
Goal: Finish first 20 ready tasks in MYO backlog with deterministic handoff loops and low token overhead.
Inputs: primary_mission: Complete first 20 ready MYO tasks from current sprint with full dev/test/review chain.
Inputs: task_source: Linear team Myownmint, project Ouroboros, status Ready, ordered by priority then age.
Inputs: repo_root: ../Ouroboros
Inputs: tracking_mode: automated-handoff
Inputs: agent_root_path: agents
Inputs: standards_source: agents/agent-making-agent/README.md
Inputs: worktree_policy_path: agents/_shared/WORKTREE_POLICY.md
Inputs: linear_workflow_path: agents/_shared/LINEAR_WORKFLOW.md
Inputs: sleep_minutes: 5
Inputs: max_initialized_workers: 10
Inputs: max_running_workers: 6
Inputs: worker_registry_path: reports/optimus-prime/WORKER_REGISTRY.json
Inputs: cycle_log_path: reports/optimus-prime/CYCLE_LOG.jsonl
Inputs: handoff_log_path: reports/optimus-prime/HANDOFF_LOG.jsonl
Inputs: linear_sync_log_path: reports/optimus-prime/LINEAR_SYNC_LOG.jsonl
Inputs: identity_checkpoint_path: reports/optimus-prime/IDENTITY_CHECKPOINT.md
Inputs: branch_lineage_path: reports/optimus-prime/BRANCH_LINEAGE.json
Inputs: packet_require_start_point: true
Inputs: developer_agent_path: agents/optimus-fullstack-developer/README.md
Inputs: tester_agent_path: agents/optimus-fullstack-tester/README.md
Inputs: reviewer_agent_path: agents/optimus-reviewer/README.md
Inputs: worker_role_policy: developers up to 3, testers up to 2, reviewer up to 1
Inputs: developer_scaling: ready 1-3 => 1 dev, ready 4-9 => 2 devs, ready >=10 => 3 devs
Inputs: concurrency_policy: developers do not get next task before test+review pass; testers wait for reviewer outcome before next task
Constraints: Use workstation-preparation before every new worker thread. Keep medium-thinking and high-thinking worker threads stable and reused. Build packet start anchors from branch lineage map so dependent unmerged tasks always get explicit starting point. If branch checkout is denied, workers create role-suffixed branch and continue.
Output: Cycle-by-cycle orchestration until 20 tasks are fully done, with Optimus-managed Linear synchronization and complete local trace logs.
```
