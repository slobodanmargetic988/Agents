# Examples

Use these as starting points. Adapt stack constraints, design references, and test surface decisions to your project.

## Example 1: Linear Mode Frontend Handoff

### Input
```text
Agent: frontend-developer
Goal: Add bulk row selection and bulk status update on ticket table.
Inputs: task_identifier: UI-204
Inputs: repo_root: /workspace/support-portal
Inputs: default_branch: main
Inputs: acceptance_criteria: Users can select rows, apply status update, and undo within 10 seconds.
Inputs: stack_file_path: /workspace/support-portal/STACK.md
Inputs: design_source: https://figma.example/support-portal-table
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: UI-204
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: packet_type: DEV_TASK
Inputs: branch_name: codex/ui-204-bulk-status
Inputs: commit_mode: commit
Constraints: Consume latest DEV_TASK packet. Run lint/typecheck/tests/build. Push branch before structured handoff.
Output: Frontend changes, structured handoff to frontend-tester, check summary.
```

### Expected Output
```text
Reads latest DEV_TASK packet from issue comments.
Implements UI/state updates and runs frontend validations.
Pushes branch and posts structured handoff event for frontend-tester.
Sets issue to testing-ready status.
```

## Example 2: Local Mode Frontend Handoff

### Input
```text
Agent: frontend-developer
Goal: Add widget-level error boundaries for dashboard modules.
Inputs: task_identifier: APP-52
Inputs: repo_root: /workspace/analytics-ui
Inputs: default_branch: develop
Inputs: acceptance_criteria: Widget failures do not crash page and show recoverable fallback state.
Inputs: tracking_mode: local
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: packet_type: DEV_TASK
Inputs: local_issue_dir: /workspace/analytics-ui/reports/issues/APP-52/
Inputs: local_state_path: /workspace/analytics-ui/reports/issues/APP-52/state.yaml
Inputs: local_events_path: /workspace/analytics-ui/reports/issues/APP-52/events.jsonl
Inputs: branch_name: codex/app-52-widget-boundary
Inputs: commit_mode: commit
Constraints: Consume local DEV_TASK packet and write only local state/events.
Output: Frontend changes, local structured handoff event, check summary.
```

### Expected Output
```text
Reads local DEV_TASK packet under /reports/issues/APP-52/.
Implements error boundary strategy and runs frontend checks.
Pushes branch, appends structured completion event to events.jsonl, and updates state.yaml handoff target.
```
