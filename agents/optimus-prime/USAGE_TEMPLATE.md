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
Inputs: feature_lane_registry_path: reports/optimus-prime/FEATURE_LANES.json
Inputs: packet_require_start_point: true
Inputs: feature_parallelism_policy: feature-affinity-first
Inputs: feature_grouping_fields: parent_issue,epic,label:feature
Inputs: allow_multi_developers_per_feature_when_blocked: true
Inputs: feature_lane_reassignment_policy: sticky-until-complete-or-blocked
Inputs: codex_profile_aliases: codex=default
Inputs: worker_codex_profile_policy: role:developer=codex; role:tester=codex; role:reviewer=codex
Inputs: dispatch_codex_profile_mode: thread-dispatch-codex-home
Inputs: dispatch_worker_mcp_mode: thread-dispatch-disable-all-by-default
Inputs: worker_mcp_policy: role:developer=none; role:tester=none|playwright,chrome_devtools(on-demand); role:reviewer=none; deny:all-workers=linear,linear_sse; allow:on-demand-developer=context7
Inputs: rate_gate_5h_percent: 15
Inputs: rate_gate_weekly_percent: 10
Inputs: soft_rate_gate_5h_percent: 40
Inputs: soft_rate_gate_weekly_percent: 25
Inputs: soft_rate_gated_max_running_workers: 3
Inputs: rate_reset_wait_max_hours: 4
Inputs: status_check_interval_cycles: 1
Inputs: status_check_on_start: true
Inputs: status_profiles_scope: all-configured-plus-primary
Inputs: status_primary_profile_alias: codex
Inputs: rate_status_log_path: reports/optimus-prime/RATE_STATUS_LOG.jsonl
Inputs: profile_rate_registry_path: reports/optimus-prime/PROFILE_RATE_REGISTRY.json
Inputs: rate_gate_action_mode: wind-down-or-wait
Inputs: status_account_parse_required: true
Inputs: developer_agent_path: agents/optimus-fullstack-developer/README.md
Inputs: tester_agent_path: agents/optimus-fullstack-tester/README.md
Inputs: reviewer_agent_path: agents/optimus-reviewer/README.md
Inputs: worker_role_policy: developers up to 3, testers up to 2, reviewer up to 1
Inputs: developer_scaling: ready 1-3 => 1 dev, ready 4-9 => 2 devs, ready >=10 => 3 devs
Inputs: concurrency_policy: developers do not get next task before test+review pass; testers wait for reviewer outcome before next task
Constraints: Optimus-only Linear updates. Workers do not use linear skill. Workers use minimum required skills only. Worker MCP access must be default-deny via thread-dispatch --disable-all-mcp and expanded only with --enable-only-mcp when packet requirements justify it; never grant workers linear or linear_sse MCP. Every worker packet must include start_from_branch and start_from_commit. Apply feature-affinity-first planning: spread developers across distinct ready features where possible, keep developer-feature lanes sticky, and only assign multiple developers to one feature when other features are blocked/unavailable. Optimus must use codex-rate-snapshot skill periodically for all configured profiles, derive single-user vs multiple-users from profile identity (auth.json best effort), apply hard rate gates before dispatching new work, and apply soft concurrency throttle caps when soft-gated. Run in 5-minute cycles and skip sleep only while handling user steering.
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
Inputs: feature_lane_registry_path: reports/optimus-prime/FEATURE_LANES.json
Inputs: packet_require_start_point: true
Inputs: feature_parallelism_policy: feature-affinity-first
Inputs: feature_grouping_fields: parent_issue,epic,label:feature
Inputs: allow_multi_developers_per_feature_when_blocked: true
Inputs: feature_lane_reassignment_policy: sticky-until-complete-or-blocked
Inputs: codex_profile_aliases: codex=default, codex-second=$HOME/.codex-second, codex-third=$HOME/.codex-third, codex-fourth=$HOME/.codex-fourth
Inputs: worker_codex_profile_policy: role:developer=codex-second; role:tester=codex; role:reviewer=codex
Inputs: dispatch_codex_profile_mode: thread-dispatch-codex-home
Inputs: dispatch_worker_mcp_mode: thread-dispatch-disable-all-by-default
Inputs: worker_mcp_policy: role:developer=none; role:tester=none|playwright,chrome_devtools(on-demand); role:reviewer=none; deny:all-workers=linear,linear_sse; allow:on-demand-developer=context7
Inputs: rate_gate_5h_percent: 15
Inputs: rate_gate_weekly_percent: 10
Inputs: soft_rate_gate_5h_percent: 40
Inputs: soft_rate_gate_weekly_percent: 25
Inputs: soft_rate_gated_max_running_workers: 3
Inputs: rate_reset_wait_max_hours: 4
Inputs: status_check_interval_cycles: 1
Inputs: status_check_on_start: true
Inputs: status_profiles_scope: all-configured-plus-primary
Inputs: status_primary_profile_alias: codex
Inputs: rate_status_log_path: reports/optimus-prime/RATE_STATUS_LOG.jsonl
Inputs: profile_rate_registry_path: reports/optimus-prime/PROFILE_RATE_REGISTRY.json
Inputs: rate_gate_action_mode: wind-down-or-wait
Inputs: status_account_parse_required: true
Inputs: developer_agent_path: agents/optimus-fullstack-developer/README.md
Inputs: tester_agent_path: agents/optimus-fullstack-tester/README.md
Inputs: reviewer_agent_path: agents/optimus-reviewer/README.md
Inputs: worker_role_policy: developers up to 3, testers up to 2, reviewer up to 1
Inputs: developer_scaling: ready 1-3 => 1 dev, ready 4-9 => 2 devs, ready >=10 => 3 devs
Inputs: concurrency_policy: developers do not get next task before test+review pass; testers wait for reviewer outcome before next task
Constraints: Use workstation-preparation before every new worker thread. Keep medium-thinking and high-thinking worker threads stable and reused. Build packet start anchors from branch lineage map so dependent unmerged tasks always get explicit starting point. Use feature-affinity-first scheduling so developers stay feature-specific when parallel feature work exists. Launch worker threads with thread-dispatch MCP minimization (default disable-all; enable only task-required MCPs, never linear/linear_sse for workers). Use codex-rate-snapshot skill on configured profiles every cycle, stop new dispatch when hard rate gates are hit (or sleep until reset if under 4h), and reduce active background workers to soft throttle cap when soft-gated. If branch checkout is denied, workers create role-suffixed branch and continue.
Output: Cycle-by-cycle orchestration until 20 tasks are fully done, with Optimus-managed Linear synchronization and complete local trace logs.
```
