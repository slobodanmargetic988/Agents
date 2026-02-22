# Usage Template

## Blank Template
```text
Agent: fullstack-developer
Goal:
Inputs: task_identifier:
Inputs: repo_root:
Inputs: default_branch: main
Inputs: acceptance_criteria:
Inputs: stack_file_path:
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id:
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: linear_ready_for_test_status: Agent work DONE
Inputs: packet_type: DEV_TASK
Inputs: local_issue_dir: /reports/issues/<task_identifier>/
Inputs: local_state_path: /reports/issues/<task_identifier>/state.yaml
Inputs: local_events_path: /reports/issues/<task_identifier>/events.jsonl
Inputs: branch_name:
Inputs: tester_strategy: auto
Inputs: commit_mode: commit
Constraints:
- Implement backend and frontend changes directly when task requires both.
- Resolve `tracking_mode` first and consume the latest `DEV_TASK` packet.
- Use `linear_workflow_path` for status defaults and `linear_comment_schema_path` for structured comments.
- Use `worktree_policy_path` as the default worktree behavior source; never create new worktree without permission.
- Include task identifier in commit messages.
- Run relevant checks for all changed layers.
- Commit and push the task branch before publishing handoff.
- Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output:
- Fullstack code changes
- Structured handoff update (backend/frontend tester targets or review-ready rationale)
- Summary of checks run and results
```

## Filled Example
```text
Agent: fullstack-developer
Goal: Implement order cancellation flow end-to-end with audit logging and UI confirmation states.
Inputs: task_identifier: ORD-401
Inputs: repo_root: /workspace/order-platform
Inputs: default_branch: main
Inputs: acceptance_criteria: Cancellations persist correctly, emit audit events, and UI reflects final status with rollback-safe messaging.
Inputs: stack_file_path: /workspace/order-platform/STACK.md
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: ORD-401
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: linear_ready_for_test_status: Agent work DONE
Inputs: packet_type: DEV_TASK
Inputs: local_issue_dir: /workspace/order-platform/reports/issues/ORD-401/
Inputs: local_state_path: /workspace/order-platform/reports/issues/ORD-401/state.yaml
Inputs: local_events_path: /workspace/order-platform/reports/issues/ORD-401/events.jsonl
Inputs: branch_name: codex/ord-401-cancel-flow
Inputs: tester_strategy: both
Inputs: commit_mode: commit
Constraints:
- Implement backend and frontend changes directly when task requires both.
- Resolve `tracking_mode` first and consume the latest `DEV_TASK` packet.
- Use `linear_workflow_path` for status defaults and `linear_comment_schema_path` for structured comments.
- Use `worktree_policy_path` as the default worktree behavior source; never create new worktree without permission.
- Include task identifier in commit messages.
- Run relevant checks for all changed layers.
- Commit and push the task branch before publishing handoff.
- Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output:
- Fullstack code changes
- Structured handoff update (backend/frontend tester targets or review-ready rationale)
- Summary of checks run and results
```
