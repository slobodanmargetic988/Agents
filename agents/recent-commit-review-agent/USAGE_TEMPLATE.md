# Usage Template

## Blank Template
```text
Agent: recent-commit-review-agent
Goal:
Mode: review
Review mode: auto
Inputs: task_identifier:
Review window:
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id:
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: packet_type: REVIEW_TASK
Inputs: local_issue_dir: /reports/issues/<task_identifier>/
Inputs: local_state_path: /reports/issues/<task_identifier>/state.yaml
Inputs: local_events_path: /reports/issues/<task_identifier>/events.jsonl
Primary deliverable: /reports/issues/<task_identifier>/COMMIT_REVIEW_TASKS.md
Constraints:
- Exactly one selector in Review window: use `commits=8` OR `since=2026-02-01`.
- Read-only review. Do not modify source code.
- Resolve `tracking_mode` first and consume latest `REVIEW_TASK` packet.
- Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output: Executive summary, top urgent items, findings sorted P0-P3, duplicate-merge notes, and verification steps per finding. Require unique finding IDs and require summary mentions to reference finding IDs. Publish structured review outcome event.
```

## Filled Example
```text
Agent: recent-commit-review-agent
Goal: Review recent commits for high-impact defects and produce prioritized remediation tasks.
Mode: review
Review mode: auto
Inputs: task_identifier: PAY-221
Review window: commits=8
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: PAY-221
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: packet_type: REVIEW_TASK
Inputs: local_issue_dir: /workspace/payments-service/reports/issues/PAY-221/
Inputs: local_state_path: /workspace/payments-service/reports/issues/PAY-221/state.yaml
Inputs: local_events_path: /workspace/payments-service/reports/issues/PAY-221/events.jsonl
Primary deliverable: /reports/issues/<task_identifier>/COMMIT_REVIEW_TASKS.md
Constraints:
- Exactly one selector in Review window: use `commits=8` OR `since=2026-02-01`.
- Read-only review. Do not modify source code.
- Resolve `tracking_mode` first and consume latest `REVIEW_TASK` packet.
- Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output: Executive summary, top urgent items, findings sorted P0-P3, duplicate-merge notes, and verification steps per finding. Require unique finding IDs and require summary mentions to reference finding IDs. Publish structured review outcome event.
```
