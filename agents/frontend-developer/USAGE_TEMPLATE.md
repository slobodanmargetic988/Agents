# Usage Template

## Blank Template
```text
Agent: frontend-developer
Goal:
Inputs: task_identifier:
Inputs: repo_root:
Inputs: default_branch: main
Inputs: acceptance_criteria:
Inputs: stack_file_path:
Inputs: design_source:
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
- Run lint/typecheck/test/build checks.
- Commit and push the task branch before publishing handoff.
- Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output:
- Frontend code changes
- Structured handoff update (`frontend-tester` or review-ready with rationale)
- Summary of checks run and results
```

## Filled Example
```text
Agent: frontend-developer
Goal: Implement keyboard-accessible filter drawer and persistent filter state on orders page.
Inputs: task_identifier: WEB-88
Inputs: repo_root: /workspace/orders-web
Inputs: default_branch: main
Inputs: acceptance_criteria: Drawer is fully keyboard navigable, filters persist on reload, and mobile layout remains usable.
Inputs: stack_file_path: /workspace/orders-web/STACK.md
Inputs: design_source: https://www.figma.com/design/example/orders-filters
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: WEB-88
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: linear_ready_for_test_status: Agent work DONE
Inputs: packet_type: DEV_TASK
Inputs: local_issue_dir: /workspace/orders-web/reports/issues/WEB-88/
Inputs: local_state_path: /workspace/orders-web/reports/issues/WEB-88/state.yaml
Inputs: local_events_path: /workspace/orders-web/reports/issues/WEB-88/events.jsonl
Inputs: branch_name: codex/web-88-filter-drawer-a11y
Inputs: commit_mode: commit
Constraints:
- Implement changes directly.
- Resolve `tracking_mode` first and consume the latest `DEV_TASK` packet.
- Use `linear_workflow_path` for status defaults and `linear_comment_schema_path` for structured comments.
- Use `worktree_policy_path` as the default worktree behavior source; never create new worktree without permission.
- Include task identifier in commit messages.
- Run lint/typecheck/test/build checks.
- Commit and push the task branch before publishing handoff.
- Do not write shared sprint state files; in local mode write only under `/reports/issues/<task_identifier>/`.
Output:
- Frontend code changes
- Structured handoff update (`frontend-tester` or review-ready with rationale)
- Summary of checks run and results
```
