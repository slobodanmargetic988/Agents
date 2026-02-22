# Usage Template

## Blank Template
```text
Agent: backend-tester
Goal:
Inputs: task_identifier:
Inputs: repo_root:
Inputs: default_branch: main
Inputs: test_target:
Inputs: stack_file_path:
Inputs: harness_mode: developer_handoff
Inputs: extra_test_focus:
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id:
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: linear_ready_statuses: Agent work DONE, Agent testing
Inputs: post_not_ready_comment: true
Inputs: packet_type: TEST_TASK
Inputs: local_issue_dir: /reports/issues/<task_identifier>/
Inputs: local_state_path: /reports/issues/<task_identifier>/state.yaml
Inputs: local_events_path: /reports/issues/<task_identifier>/events.jsonl
Inputs: branch_name:
Inputs: commit_mode: commit
Constraints:
- Resolve `tracking_mode` first and consume the latest `TEST_TASK` packet.
- Run readiness gate before any test command.
- Use `linear_workflow_path` for status defaults and `linear_comment_schema_path` for structured comments.
- Use `worktree_policy_path` as the default worktree behavior source; never create new worktree without permission.
- In `developer_handoff` mode, run fullest feasible suite for changed backend scope.
- Add/adjust tests when coverage gaps are found.
- Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output:
- /reports/issues/<task_identifier>/BACKEND_TEST_REPORT.md
- Optional test code changes
- Structured outcome update (`not_ready`, `blocked`, or `ready_for_review`)
```

## Filled Example
```text
Agent: backend-tester
Goal: Validate recent webhook idempotency implementation and close backend testing phase.
Inputs: task_identifier: UOW-014
Inputs: repo_root: /workspace/payments-service
Inputs: default_branch: main
Inputs: test_target: src/webhooks/payment_handler.*, tests/webhooks/*
Inputs: stack_file_path: /workspace/payments-service/STACK.md
Inputs: harness_mode: developer_handoff
Inputs: extra_test_focus: contract
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: PAY-221
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: linear_ready_statuses: Agent work DONE, Agent testing
Inputs: post_not_ready_comment: true
Inputs: packet_type: TEST_TASK
Inputs: local_issue_dir: /workspace/payments-service/reports/issues/UOW-014/
Inputs: local_state_path: /workspace/payments-service/reports/issues/UOW-014/state.yaml
Inputs: local_events_path: /workspace/payments-service/reports/issues/UOW-014/events.jsonl
Inputs: branch_name: codex/uow-014-webhook-idempotency
Inputs: commit_mode: commit
Constraints:
- Resolve `tracking_mode` first and consume the latest `TEST_TASK` packet.
- Run readiness gate before any test command.
- Use `linear_workflow_path` for status defaults and `linear_comment_schema_path` for structured comments.
- Use `worktree_policy_path` as the default worktree behavior source; never create new worktree without permission.
- In `developer_handoff` mode, run fullest feasible suite for changed backend scope.
- Add/adjust tests when coverage gaps are found.
- Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output:
- /reports/issues/<task_identifier>/BACKEND_TEST_REPORT.md
- Optional test code changes
- Structured outcome update (`not_ready`, `blocked`, or `ready_for_review`)
```
