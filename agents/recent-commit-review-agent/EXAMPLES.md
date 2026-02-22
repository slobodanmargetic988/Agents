# Examples

Use these as starting points. Adapt review depth, commit window, and risk focus for your repository.

## Example 1: Linear Mode Recent-Commit Review from REVIEW_TASK Packet

### Input
```text
Agent: recent-commit-review-agent
Goal: Review recent payment-service commits for high-impact regressions.
Mode: review
Review mode: auto
Inputs: task_identifier: PAY-221
Review window: commits=12
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
Constraints: Read-only review. Exactly one selector (`commits` or `since`). Consume latest REVIEW_TASK packet and publish structured review outcome event.
Output: Executive summary, urgent findings, prioritized list, and verification steps.
```

### Expected Output
```text
Reads latest REVIEW_TASK packet from issue comments.
Writes /reports/issues/PAY-221/COMMIT_REVIEW_TASKS.md.
Findings are deduplicated, prioritized P0-P3, and reference stable finding IDs.
Posts structured review outcome event (review_passed or review_blocked).
```

## Example 2: Local Mode Re-review of Resolved Findings

### Input
```text
Agent: recent-commit-review-agent
Goal: Re-check findings previously marked RESOLVED.
Mode: re-review
Review mode: auto
Inputs: task_identifier: PAY-221
Review window: since=2026-02-01
Inputs: tracking_mode: local
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: packet_type: REVIEW_TASK
Inputs: local_issue_dir: /workspace/payments-service/reports/issues/PAY-221/
Inputs: local_state_path: /workspace/payments-service/reports/issues/PAY-221/state.yaml
Inputs: local_events_path: /workspace/payments-service/reports/issues/PAY-221/events.jsonl
Primary deliverable: /reports/issues/<task_identifier>/COMMIT_REVIEW_TASKS.md
Constraints: Read-only review. Preserve existing finding IDs. Write only issue-scoped files and local events.
Output: Re-review results for RESOLVED findings and structured local outcome event.
```

### Expected Output
```text
Reads local REVIEW_TASK packet and baseline issue-scoped review report.
Re-checks only RESOLVED findings and preserves existing IDs.
Writes updated /reports/issues/PAY-221/COMMIT_REVIEW_TASKS.md.
Appends structured review outcome event to local events.jsonl.
```
