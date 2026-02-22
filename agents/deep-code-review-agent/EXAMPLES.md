# Examples

Use these as starting points. Adapt scope, module priorities, and risk themes to your repository.

## Example 1: Linear Mode Full Deep Review from REVIEW_TASK Packet

### Input
```text
Agent: deep-code-review-agent
Goal: Run deep review of commerce monorepo after long review gap.
Mode: Full Review
Inputs: task_identifier: COM-900
Inputs: Repository root path: ./repo/commerce-monorepo
Inputs: Existing report path (required for Re-review): /reports/issues/<task_identifier>/REVIEW_TASKS.md
Inputs: Optional focus modules or risk themes: checkout, inventory sync, shared auth middleware
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: COM-900
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: packet_type: REVIEW_TASK
Inputs: local_issue_dir: /workspace/commerce-monorepo/reports/issues/COM-900/
Inputs: local_state_path: /workspace/commerce-monorepo/reports/issues/COM-900/state.yaml
Inputs: local_events_path: /workspace/commerce-monorepo/reports/issues/COM-900/events.jsonl
Constraints: Read-only review. Consume latest REVIEW_TASK packet. Publish structured review outcome event.
Output: /reports/issues/<task_identifier>/REVIEW_TASKS.md with executive summary, top 10, quick wins, prioritized tasks, needs-manual-verification, and out-of-scope.
```

### Expected Output
```text
Reads latest REVIEW_TASK packet from issue comments.
Writes /reports/issues/COM-900/REVIEW_TASKS.md with P0-P3 tasks and stable task IDs.
Deduplicates findings and preserves evidence references.
Posts structured review outcome event to Linear.
```

## Example 2: Local Mode Re-review of Resolved Tasks

### Input
```text
Agent: deep-code-review-agent
Goal: Validate whether previously resolved P0/P1 tasks are truly fixed.
Mode: Re-review
Inputs: task_identifier: COM-900
Inputs: Repository root path: ./repo/commerce-monorepo
Inputs: Existing report path (required for Re-review): /reports/issues/<task_identifier>/REVIEW_TASKS.md
Inputs: Optional focus modules or risk themes: resolved tasks in checkout + auth
Inputs: tracking_mode: local
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: packet_type: REVIEW_TASK
Inputs: local_issue_dir: /workspace/commerce-monorepo/reports/issues/COM-900/
Inputs: local_state_path: /workspace/commerce-monorepo/reports/issues/COM-900/state.yaml
Inputs: local_events_path: /workspace/commerce-monorepo/reports/issues/COM-900/events.jsonl
Constraints: Read-only review. Re-review only tasks marked RESOLVED. Preserve task IDs.
Output: /reports/issues/<task_identifier>/REVIEW_TASKS.md with re-review outcomes and structured local outcome event.
```

### Expected Output
```text
Reads local REVIEW_TASK packet and existing issue-scoped report.
Re-evaluates only RESOLVED tasks and preserves existing IDs.
Writes updated /reports/issues/COM-900/REVIEW_TASKS.md.
Appends structured review outcome event to local events.jsonl.
```
