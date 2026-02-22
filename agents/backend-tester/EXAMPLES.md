# Examples

Use these as starting points. Adapt test targets, harness mode, and evidence depth to your service architecture.

## Example 1: Linear Mode Tester Run from TEST_TASK Packet

### Input
```text
Agent: backend-tester
Goal: Validate inventory reservation implementation and close backend testing handoff.
Inputs: task_identifier: INV-118
Inputs: repo_root: /workspace/inventory-service
Inputs: default_branch: main
Inputs: test_target: src/reservations/*, src/api/reservations_controller.*, tests/reservations/*
Inputs: stack_file_path: /workspace/inventory-service/STACK.md
Inputs: harness_mode: developer_handoff
Inputs: extra_test_focus: contract
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: INV-118
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: packet_type: TEST_TASK
Inputs: local_issue_dir: /workspace/inventory-service/reports/issues/INV-118/
Inputs: local_state_path: /workspace/inventory-service/reports/issues/INV-118/state.yaml
Inputs: local_events_path: /workspace/inventory-service/reports/issues/INV-118/events.jsonl
Inputs: branch_name: codex/inv-118-reservation-fixes
Inputs: commit_mode: commit
Constraints: Consume latest TEST_TASK packet. Execute readiness gate before tests. Publish structured outcome event.
Output: /reports/issues/<task_identifier>/BACKEND_TEST_REPORT.md and structured outcome.
```

### Expected Output
```text
Reads latest TEST_TASK packet and checks readiness gate (status + latest developer handoff event).
Runs fullest feasible suite for changed backend scope.
Writes /reports/issues/INV-118/BACKEND_TEST_REPORT.md.
On pass: updates issue to test-done and posts structured ready_for_review event.
```

## Example 2: Local Mode Not-Ready Early Exit

### Input
```text
Agent: backend-tester
Goal: Run targeted auth regression tests for hotfix validation.
Inputs: task_identifier: SEC-90
Inputs: repo_root: /workspace/auth-service
Inputs: default_branch: release
Inputs: test_target: src/auth/token_service.*, tests/auth/token_service_spec.*
Inputs: harness_mode: targeted
Inputs: extra_test_focus: security-smoke
Inputs: tracking_mode: local
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: packet_type: TEST_TASK
Inputs: local_issue_dir: /workspace/auth-service/reports/issues/SEC-90/
Inputs: local_state_path: /workspace/auth-service/reports/issues/SEC-90/state.yaml
Inputs: local_events_path: /workspace/auth-service/reports/issues/SEC-90/events.jsonl
Inputs: commit_mode: no-commit
Constraints: If local readiness state is not ready-for-testing, emit `not_ready` event and stop before test commands.
Output: /reports/issues/<task_identifier>/BACKEND_TEST_REPORT.md (only if tests run) and structured outcome.
```

### Expected Output
```text
Reads local TEST_TASK packet and readiness state.
If not ready, appends structured not_ready event and exits without running tests.
If ready, runs targeted checks and writes issue-scoped report.
```
