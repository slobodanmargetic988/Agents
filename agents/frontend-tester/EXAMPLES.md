# Examples

Use these as starting points. Adapt flow scope, credentials, and severity thresholds to your project.

## Example 1: Linear Mode Browser Validation from TEST_TASK Packet

### Input
```text
Agent: frontend-tester
Goal: Validate authentication and checkout flows for release candidate.
Inputs: task_identifier: SHOP-301
Inputs: Target URL/environment: https://staging.shop.example
Inputs: Key user flows to validate: sign in, add to cart, checkout confirmation
Inputs: Credentials or test account details: use qa_checkout_user from team vault
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: SHOP-301
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: linear_ready_statuses: Agent work DONE, Agent testing
Inputs: packet_type: TEST_TASK
Inputs: local_issue_dir: /workspace/shop-web/reports/issues/SHOP-301/
Inputs: local_state_path: /workspace/shop-web/reports/issues/SHOP-301/state.yaml
Inputs: local_events_path: /workspace/shop-web/reports/issues/SHOP-301/events.jsonl
Constraints: Consume latest TEST_TASK packet, run readiness gate before browser actions, use Playwright first, and publish structured outcome event.
Output: /reports/issues/<task_identifier>/FRONTEND_TEST_REPORT.md and structured outcome.
```

### Expected Output
```text
Reads latest TEST_TASK packet and verifies readiness before browser execution.
Runs Playwright flows and captures evidence.
Writes /reports/issues/SHOP-301/FRONTEND_TEST_REPORT.md.
On pass: updates issue to test-done and posts structured ready_for_review event.
```

## Example 2: Local Mode Flaky Investigation with DevTools Evidence

### Input
```text
Agent: frontend-tester
Goal: Investigate intermittent checkout-button freeze in staging.
Inputs: task_identifier: SHOP-342
Inputs: Target URL/environment: https://staging.shop.example
Inputs: Key user flows to validate: cart update, checkout submit, payment redirect
Inputs: Credentials or test account details: use qa_checkout_user from team vault
Inputs: tracking_mode: local
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: packet_type: TEST_TASK
Inputs: local_issue_dir: /workspace/shop-web/reports/issues/SHOP-342/
Inputs: local_state_path: /workspace/shop-web/reports/issues/SHOP-342/state.yaml
Inputs: local_events_path: /workspace/shop-web/reports/issues/SHOP-342/events.jsonl
Constraints: Consume local TEST_TASK packet. If flaky behavior appears, include console/network diagnostics in report and structured blocked outcome when unresolved.
Output: /reports/issues/<task_identifier>/FRONTEND_TEST_REPORT.md and structured outcome.
```

### Expected Output
```text
Reads local TEST_TASK packet and local readiness state.
Runs Playwright scenarios and gathers evidence.
Writes issue-scoped report with failure diagnostics.
Appends structured blocked or ready_for_review event to local events.jsonl.
```
