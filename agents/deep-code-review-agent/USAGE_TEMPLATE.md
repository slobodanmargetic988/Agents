# Usage Template

## Blank Template
```text
Agent: deep-code-review-agent
Goal: Deep review target and risk focus:
Mode: Full Review or Re-review
Inputs: task_identifier:
Inputs: Repository root path:
Inputs: Existing report path (required for Re-review): /reports/issues/<task_identifier>/REVIEW_TASKS.md
Inputs: Optional focus modules or risk themes:
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id:
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: packet_type: REVIEW_TASK
Inputs: local_issue_dir: /reports/issues/<task_identifier>/
Inputs: local_state_path: /reports/issues/<task_identifier>/state.yaml
Inputs: local_events_path: /reports/issues/<task_identifier>/events.jsonl
Constraints: Read-only review. No code changes. Resolve `tracking_mode` first and consume latest `REVIEW_TASK` packet. Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output: /reports/issues/<task_identifier>/REVIEW_TASKS.md with executive summary, top 10 urgent fixes, quick wins, prioritized tasks (P0-P3), needs manual verification, out-of-scope, and verification steps per task. Require unique task IDs and summary references by task ID. Publish structured review outcome event.
```

## Filled Example
```text
Agent: deep-code-review-agent
Goal: Perform a deep code review of the payments platform that has not had a full review in 11 months.
Mode: Full Review
Inputs: task_identifier: PAY-221
Inputs: Repository root path: ./repo/payments-platform
Inputs: Existing report path (required for Re-review): /reports/issues/<task_identifier>/REVIEW_TASKS.md
Inputs: Optional focus modules or risk themes: auth, transaction consistency, retry logic, PII handling
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: PAY-221
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: packet_type: REVIEW_TASK
Inputs: local_issue_dir: /workspace/payments-platform/reports/issues/PAY-221/
Inputs: local_state_path: /workspace/payments-platform/reports/issues/PAY-221/state.yaml
Inputs: local_events_path: /workspace/payments-platform/reports/issues/PAY-221/events.jsonl
Constraints: Read-only review. No code changes. Resolve `tracking_mode` first and consume latest `REVIEW_TASK` packet. Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output: /reports/issues/<task_identifier>/REVIEW_TASKS.md with executive summary, top 10 urgent fixes, quick wins, prioritized tasks (P0-P3), needs manual verification, out-of-scope, and verification steps per task. Require unique task IDs and summary references by task ID. Publish structured review outcome event.
```
