# Usage Template

## Blank Template
```text
Agent: backend-developer
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
Inputs: commit_mode: commit
Constraints:
- Implement changes directly.
- Resolve `tracking_mode` first and consume the latest `DEV_TASK` packet.
- Use `linear_workflow_path` for status defaults and `linear_comment_schema_path` for structured comments.
- Use `worktree_policy_path` as the default worktree behavior source; never create new worktree without permission.
- Include task identifier in commit messages.
- Run lint/test/build checks before completion.
- Commit and push the task branch before publishing handoff.
- Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output:
- Backend code changes
- Structured handoff update (`backend-tester` or review-ready with rationale)
- Summary of checks run and results
```

## Filled Example
```text
Agent: backend-developer
Goal: Implement idempotent retry handling for payment webhook processing.
Inputs: task_identifier: UOW-014
Inputs: repo_root: /workspace/payments-service
Inputs: default_branch: main
Inputs: acceptance_criteria: Duplicate webhook deliveries do not create duplicate ledger entries; retries are safe.
Inputs: stack_file_path: /workspace/payments-service/STACK.md
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: PAY-221
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: linear_ready_for_test_status: Agent work DONE
Inputs: packet_type: DEV_TASK
Inputs: local_issue_dir: /workspace/payments-service/reports/issues/UOW-014/
Inputs: local_state_path: /workspace/payments-service/reports/issues/UOW-014/state.yaml
Inputs: local_events_path: /workspace/payments-service/reports/issues/UOW-014/events.jsonl
Inputs: branch_name: codex/uow-014-webhook-idempotency
Inputs: commit_mode: commit
Constraints:
- Implement changes directly.
- Resolve `tracking_mode` first and consume the latest `DEV_TASK` packet.
- Use `linear_workflow_path` for status defaults and `linear_comment_schema_path` for structured comments.
- Use `worktree_policy_path` as the default worktree behavior source; never create new worktree without permission.
- Include task identifier in commit messages.
- Run lint/test/build checks before completion.
- Commit and push the task branch before publishing handoff.
- Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output:
- Backend code changes
- Structured handoff update (`backend-tester` or review-ready with rationale)
- Summary of checks run and results
```
