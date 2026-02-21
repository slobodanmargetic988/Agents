# Examples

Use these as starting points. Review carefully and adapt goals, sources, constraints, and tracking mode to your own project.

## Example 1: Well-Tracked Project, Minimal Inspection

### Input
```text
Agent: product-manager
Goal:
- Validate progress and produce a short next-sprint plan.
Inputs: project_root:
- /workspace/payments-platform
Inputs: high_level_goal:
- Reach GA for subscription billing and improve onboarding conversion.
Inputs: tracking_mode:
- linear
Inputs: goal_sources:
- README.md
- docs/roadmap-q1.md
- Linear project PAY
Inputs: user_confidence_level:
- high
Inputs: analysis_depth_hint:
- minimal
Inputs: linear_issue_or_project:
- PAY
Inputs: persist_plan_mode:
- chat-only
Constraints:
- Start with quick-pass discovery.
- Confirm source list with user before planning.
- Ask clarifying questions first, then suggest options.
Output:
- Three baseline estimates
- Gap summary
- Proposed next-sprint tasks in Linear
```

### Expected Output
```text
Performs a quick source pass, confirms docs + Linear as authoritative, and keeps code inspection minimal.
Publishes three scored estimates (features, effort, vision alignment) with short rationale.
Produces a concise next-sprint plan and asks for approval before creating/updating Linear tasks.
```

## Example 2: Legacy/Untracked Project, Deep Inspection

### Input
```text
Agent: product-manager
Goal:
- Determine actual delivery state of a legacy app and create a recovery plan plus roadmap.
Inputs: project_root:
- /workspace/legacy-erp
Inputs: high_level_goal:
- Stabilize core operations workflows and define a realistic modernization roadmap.
Inputs: tracking_mode:
- local
Inputs: goal_sources:
- README.md
- docs/vision-notes.md
- docs/old-milestones.md
Inputs: user_confidence_level:
- low
Inputs: analysis_depth_hint:
- deep
Inputs: local_plan_path:
- reports/product-plan/
Inputs: persist_plan_mode:
- reports
Constraints:
- Start with quick-pass discovery and confirm source list with user.
- If uncertainty remains high, perform deeper code inspection.
- If codebase is too large for one pass, propose starter review/testing tasks first.
- Produce three baseline estimates with confidence notes.
Output:
- Baseline state assessment
- Recovery plan
- Local backlog files with phased tasks
```

### Expected Output
```text
Runs discovery, identifies weak tracking evidence, and gets user confirmation to include additional sources.
Performs deep inspection (or proposes delegated review/testing tasks for oversized areas) before final scoring.
Produces defensible 0-100 estimates, a phased recovery plan, and writes local backlog artifacts under reports/product-plan/.
```
