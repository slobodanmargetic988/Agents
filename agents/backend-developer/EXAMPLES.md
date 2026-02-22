# Examples

Use these as starting points. Adapt stack source, validation commands, and handoff routing to your repository.

## Example 1: Linear Mode Developer Handoff

### Input
```text
Agent: backend-developer
Goal: Add pagination and status filtering to transactions endpoint.
Inputs: task_identifier: LED-312
Inputs: repo_root: /workspace/ledger-api
Inputs: default_branch: main
Inputs: acceptance_criteria: Endpoint supports page/pageSize/status and keeps backward compatibility.
Inputs: stack_file_path: /workspace/ledger-api/STACK.md
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: LED-312
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: packet_type: DEV_TASK
Inputs: branch_name: codex/led-312-transactions-pagination
Inputs: commit_mode: commit
Constraints: Consume latest `DEV_TASK` packet, run lint/test/build, push branch before handoff, and publish structured `AGENT_EVENT_V1` completion event.
Output: Backend changes, structured handoff to backend-tester, check summary.
```

### Expected Output
```text
Reads latest DEV_TASK packet from Linear issue comments.
Implements endpoint + tests on codex/led-312-transactions-pagination.
Runs backend validations and pushes branch.
Moves issue to testing-ready status and posts structured handoff event with branch/head_commit/checks/decision.
```

## Example 2: Local Mode Developer Handoff

### Input
```text
Agent: backend-developer
Goal: Add per-IP rate limiting for login and refresh endpoints.
Inputs: task_identifier: SEC-77
Inputs: repo_root: /workspace/auth-service
Inputs: default_branch: develop
Inputs: acceptance_criteria: Login and refresh endpoints enforce per-IP and per-account limits.
Inputs: tracking_mode: local
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: packet_type: DEV_TASK
Inputs: local_issue_dir: /workspace/auth-service/reports/issues/SEC-77/
Inputs: local_state_path: /workspace/auth-service/reports/issues/SEC-77/state.yaml
Inputs: local_events_path: /workspace/auth-service/reports/issues/SEC-77/events.jsonl
Inputs: branch_name: codex/sec-77-rate-limit
Inputs: commit_mode: commit
Constraints: Consume local DEV_TASK packet. Write only local state/events; do not write shared sprint reports.
Output: Backend changes, local structured handoff event, check summary.
```

### Expected Output
```text
Reads /workspace/auth-service/reports/issues/SEC-77/DEV_TASK.yaml.
Implements task on codex/sec-77-rate-limit and runs validations.
Pushes branch and appends completion event to events.jsonl.
Updates state.yaml with next handoff target backend-tester.
```
