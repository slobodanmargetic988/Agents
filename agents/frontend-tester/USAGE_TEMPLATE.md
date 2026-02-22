# Usage Template

## Blank Template
```text
Agent: frontend-tester
Goal: Frontend scope to test:
Inputs: task_identifier:
Inputs: Target URL/environment:
Inputs: Key user flows to validate:
Inputs: Credentials or test account details:
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
Constraints: Resolve `tracking_mode` first and consume the latest `TEST_TASK` packet. Run readiness gate before browser actions. Use `linear_workflow_path` for status defaults and `linear_comment_schema_path` for structured comments. Use `worktree_policy_path` as default worktree behavior; never create new worktree without permission. Prefer branch from latest valid developer handoff packet/event. Use Playwright skill and playwright-cli first. Use Chrome DevTools MCP only when deeper diagnostics are needed. No source code changes. Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output: /reports/issues/<task_identifier>/FRONTEND_TEST_REPORT.md and structured outcome update (`not_ready`, `blocked`, or `ready_for_review`).
```

## Filled Example
```text
Agent: frontend-tester
Goal: Validate login, dashboard loading, and billing page flow before release.
Inputs: task_identifier: WEB-88
Inputs: Target URL/environment: https://staging.example.app
Inputs: Key user flows to validate: login, dashboard filters, billing invoice download.
Inputs: Credentials or test account details: use qa_user_staging account from team vault.
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: WEB-88
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: linear_ready_statuses: Agent work DONE, Agent testing
Inputs: post_not_ready_comment: true
Inputs: packet_type: TEST_TASK
Inputs: local_issue_dir: /workspace/orders-web/reports/issues/WEB-88/
Inputs: local_state_path: /workspace/orders-web/reports/issues/WEB-88/state.yaml
Inputs: local_events_path: /workspace/orders-web/reports/issues/WEB-88/events.jsonl
Inputs: branch_name: codex/web-88-filter-drawer-a11y
Constraints: Resolve `tracking_mode` first and consume the latest `TEST_TASK` packet. Run readiness gate before browser actions. Use `linear_workflow_path` for status defaults and `linear_comment_schema_path` for structured comments. Use `worktree_policy_path` as default worktree behavior; never create new worktree without permission. Prefer branch from latest valid developer handoff packet/event. Use Playwright skill and playwright-cli first. Use Chrome DevTools MCP only when deeper diagnostics are needed. No source code changes. Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output: /reports/issues/<task_identifier>/FRONTEND_TEST_REPORT.md and structured outcome update (`not_ready`, `blocked`, or `ready_for_review`).
```
