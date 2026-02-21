# Shared Worktree Policy
Last Updated: 2026-02-21 01:40 CET

Use this file as the default policy for worktree handling across agents.

## Policy
- Do not create a new Git worktree without explicit user permission.
- Prefer resolving branch-switch blockers inside the current assigned worktree.
- If local tracked changes block branch switch and a commit will safely resolve it, commit with a clear message and continue.
- If commit is unsafe or ambiguous, stop and ask the user how to proceed.

## Dedicated Worker Slots
- Preferred orchestration model is dedicated slot worktrees:
  - `dev-1`, `dev-2`, `dev-3`, `test-1`, `review-1`
- One slot must keep one stable worktree path during a sprint cycle.
- Inside each slot worktree, each task must use its own feature branch:
  - branch format: `codex/<slot>/<issue-or-task-id>`
- Never run two different active tasks on the same branch.

## Safe Auto-Commit Rule
Agent may auto-commit blocked local changes only when all conditions are true:
1. Changes are task-scoped or orchestration/report-file scoped for the current task.
2. Commit resolves branch-switch blocker without hiding unrelated work.
3. Commit message is explicit and traceable (for example `chore: checkpoint local report updates before branch switch`).
4. No destructive git operation is needed.

## Ask-User Rule
Agent must stop and ask the user when any condition is true:
- Local changes appear unrelated/mixed across multiple tasks.
- Agent cannot confidently determine safe commit scope.
- Branch strategy is unclear (for example target branch uncertain).
- Proposed commit would include files the user likely did not intend to checkpoint.

## Override Precedence
1. Explicit user instruction in current request
2. Per-agent explicit input
3. This shared policy file
4. Agent-local fallback behavior
