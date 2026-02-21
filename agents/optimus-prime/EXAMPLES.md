# Examples

Use these examples as starting points. Review and adapt task scope, worker caps, branch policy, and mission target to your own repository and workflow.

## Example 1: Finish First 20 Tasks With Adaptive Dev Capacity

### Input
```text
Agent: optimus-prime
Goal: Complete first 20 ready tasks while keeping workers token-efficient and deterministic.
Inputs: primary_mission: Finish first 20 ready tasks in current sprint.
Inputs: task_source: Linear project Ouroboros, status Ready, ordered by priority.
Inputs: repo_root: ../Ouroboros
Inputs: tracking_mode: automated-handoff
Inputs: sleep_minutes: 5
Inputs: max_initialized_workers: 10
Inputs: max_running_workers: 6
Inputs: branch_lineage_path: reports/optimus-prime/BRANCH_LINEAGE.json
Inputs: packet_require_start_point: true
Inputs: developer_agent_path: agents/optimus-fullstack-developer/README.md
Inputs: tester_agent_path: agents/optimus-fullstack-tester/README.md
Inputs: reviewer_agent_path: agents/optimus-reviewer/README.md
Inputs: worker_role_policy: developers up to 3, testers up to 2, reviewer up to 1
Inputs: developer_scaling: ready 1-3 => 1 dev, ready 4-9 => 2 devs, ready >=10 => 3 devs
Constraints: Workers do not use linear skill. Optimus performs all Linear updates after worker summaries. Every packet includes explicit start_from_branch and start_from_commit resolved from branch lineage state.
Output: reports/optimus-prime logs + continuous cycle summaries + completed dev/test/review chain for mission target
```

### Expected Output
```text
Optimus initializes workstation slots, starts only required developer threads, and keeps at most 6 running workers.
Optimus dispatches complete unit packets and reuses workers by fixed role and fixed thinking profile.
Tester starts after first developer completion; reviewer starts after first tester completion.
No developer receives a new task until current task passes test and review.
Optimus publishes concise cycle summary, sleeps 5 minutes, and repeats until 20 tasks are fully done.
```

## Example 2: Branch Conflict During Tester Assignment

### Input
```text
Agent: optimus-prime
Goal: Continue orchestration when assigned branch is locked by another worktree.
Inputs: primary_mission: Complete task MYO-23 through review.
Inputs: task_source: Explicit task MYO-23.
Inputs: repo_root: ../Ouroboros
Inputs: tracking_mode: automated-handoff
Inputs: branch_lineage_path: reports/optimus-prime/BRANCH_LINEAGE.json
Inputs: packet_require_start_point: true
Inputs: developer_agent_path: agents/optimus-fullstack-developer/README.md
Inputs: tester_agent_path: agents/optimus-fullstack-tester/README.md
Inputs: reviewer_agent_path: agents/optimus-reviewer/README.md
Constraints: Assigned tester cannot checkout branch MYO-23-make-menu-navbar because branch is active elsewhere.
Output: Deterministic fallback branch handling with minimal token chatter
```

### Expected Output
```text
Optimus packet instructs tester to create a role-suffixed fallback branch (MYO-23-make-menu-navbar-test).
Tester proceeds with test work on fallback branch and returns short summary.
Optimus records branch mapping in handoff log and performs required Linear update itself.
Task remains in deterministic dev/test/review flow without blocking unrelated workers.
```

## Example 3: Stuck Worker Intervention

### Input
```text
Agent: optimus-prime
Goal: Detect and recover from a looping developer worker.
Inputs: primary_mission: Complete 8 tasks.
Inputs: task_source: Ready tasks list MYO-101..MYO-108.
Inputs: repo_root: ../Ouroboros
Inputs: tracking_mode: automated-handoff
Inputs: branch_lineage_path: reports/optimus-prime/BRANCH_LINEAGE.json
Inputs: packet_require_start_point: true
Inputs: developer_agent_path: agents/optimus-fullstack-developer/README.md
Inputs: tester_agent_path: agents/optimus-fullstack-tester/README.md
Inputs: reviewer_agent_path: agents/optimus-reviewer/README.md
Constraints: dev-high-1 repeatedly retries same failing command with no progress for multiple cycles.
Output: Controlled intervention and continued mission execution
```

### Expected Output
```text
Optimus flags worker as stale/stuck using cycle logs and repeated-attempt signal.
Optimus sends steering prompt with corrective instructions and timeout.
If still unresolved, Optimus stops that worker, marks task blocked or reassigns to another developer profile, and continues mission cycles.
No worker besides Optimus updates tracking state in Linear.
```

## Example 4: Unmerged Dependency Chain

### Input
```text
Agent: optimus-prime
Goal: Dispatch dependent tasks where MYO-52 and MYO-53 both depend on unmerged MYO-51.
Inputs: primary_mission: Complete MYO-51..MYO-53 in order.
Inputs: task_source: Explicit ordered task set with dependencies MYO-52->MYO-51 and MYO-53->MYO-52.
Inputs: repo_root: ../Ouroboros
Inputs: tracking_mode: automated-handoff
Inputs: branch_lineage_path: reports/optimus-prime/BRANCH_LINEAGE.json
Inputs: packet_require_start_point: true
Constraints: No tasks are merged yet. Each packet must declare exact start anchor from latest unmerged parent branch head commit.
Output: deterministic chained packet dispatch without ambiguous branch starts
```

### Expected Output
```text
Optimus stores MYO-51 branch and head commit in branch lineage registry after developer completion.
MYO-52 packet includes start_from_branch and start_from_commit pointing to MYO-51 head.
MYO-53 packet includes start anchor pointing to latest MYO-52 head.
Workers always receive explicit branch starting point and continue without guesswork.
```
