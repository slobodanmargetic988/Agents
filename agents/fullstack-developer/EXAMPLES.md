# Examples

Use these as starting points. Adapt stack assumptions, tester strategy, and handoff policy to your project.

## Example 1: Linear Mode Fullstack Handoff to Both Testers

### Input
```text
Agent: fullstack-developer
Goal: Add invoice approval flow with backend role checks and server-rendered confirmation states.
Inputs: task_identifier: BILL-55
Inputs: repo_root: /workspace/billing-app
Inputs: default_branch: main
Inputs: acceptance_criteria: Only approvers can approve; transitions are auditable; UI reflects final state.
Inputs: stack_file_path: /workspace/billing-app/STACK.md
Inputs: tracking_mode: linear
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: linear_issue_id: BILL-55
Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md
Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md
Inputs: packet_type: DEV_TASK
Inputs: tester_strategy: both
Inputs: branch_name: codex/bill-55-approval-flow
Inputs: commit_mode: commit
Constraints: Consume latest DEV_TASK packet. Run backend + frontend checks. Push branch before structured handoff.
Output: Fullstack changes, structured handoff to backend-tester + frontend-tester, check summary.
```

### Expected Output
```text
Reads latest DEV_TASK packet from issue comments.
Implements backend/frontend changes and runs layer-specific validations.
Pushes branch and posts structured handoff event listing both tester targets.
Moves issue to testing-ready status.
```

## Example 2: Local Mode Fullstack Handoff

### Input
```text
Agent: fullstack-developer
Goal: Introduce pricing rule engine and expose computed total in existing dashboard widget.
Inputs: task_identifier: PRC-90
Inputs: repo_root: /workspace/pricing-suite
Inputs: default_branch: develop
Inputs: acceptance_criteria: Rule engine computes expected totals and widget displays totals without layout regression.
Inputs: tracking_mode: local
Inputs: tracking_contract_path: C:/Users/<username>/Projects/Agents/agents/_shared/TRACKING_MODE_CONTRACT.md
Inputs: linear_comment_schema_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_COMMENT_SCHEMA.md
Inputs: packet_type: DEV_TASK
Inputs: local_issue_dir: /workspace/pricing-suite/reports/issues/PRC-90/
Inputs: local_state_path: /workspace/pricing-suite/reports/issues/PRC-90/state.yaml
Inputs: local_events_path: /workspace/pricing-suite/reports/issues/PRC-90/events.jsonl
Inputs: tester_strategy: auto
Inputs: branch_name: codex/prc-90-pricing-engine
Inputs: commit_mode: commit
Constraints: Consume local DEV_TASK packet and write only local state/events.
Output: Fullstack changes, local structured handoff event, check summary.
```

### Expected Output
```text
Reads local DEV_TASK packet under /reports/issues/PRC-90/.
Implements backend-heavy changes with scoped UI update and runs relevant checks.
Pushes branch, updates local state.yaml, and appends completion event with tester target(s).
```
