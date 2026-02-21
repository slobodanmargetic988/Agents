# Usage Template

## Blank Template
```text
Agent: product-manager
Goal:
- Assess current project execution state against intended vision and co-create an actionable plan.
Inputs: project_root:
- 
Inputs: high_level_goal:
- 
Inputs: tracking_mode:
- local
Inputs: goal_sources:
- README.md
- docs/
- issues/
Inputs: user_confidence_level:
- medium
Inputs: analysis_depth_hint:
- adaptive
Inputs: linear_issue_or_project:
- 
Inputs: local_plan_path:
- reports/product-plan/
Inputs: persist_plan_mode:
- chat-only
Inputs: planning_horizon:
- adaptive
Constraints:
- Start with quick-pass source discovery.
- Show discovered relevant sources and ask user to confirm or add missing sources.
- Ask clarifying questions before suggesting draft plan.
- Use minimal inspection when evidence quality is high and confidence is high.
- Use deep inspection when uncertainty is high or tracking is weak.
- Produce three baseline 0-100 estimates: features completion, effort completion, vision alignment.
- Do not create final draft plan until user indicates readiness.
Output:
- Interactive discovery summary
- Baseline three-score assessment with rationale
- Gap analysis and prioritized next steps
- Task backlog output in selected tracking mode
```

## Filled Example
```text
Agent: product-manager
Goal:
- Assess a legacy SaaS dashboard codebase and turn findings into an execution plan plus next-feature roadmap.
Inputs: project_root:
- /workspace/customer-ops-dashboard
Inputs: high_level_goal:
- Deliver the current product vision for role-based operations workflows and expand into analytics automation.
Inputs: tracking_mode:
- linear
Inputs: goal_sources:
- README.md
- docs/product-vision.md
- docs/milestones.md
- Linear project OPS
Inputs: user_confidence_level:
- low
Inputs: analysis_depth_hint:
- adaptive
Inputs: linear_issue_or_project:
- OPS
Inputs: local_plan_path:
- reports/product-plan/
Inputs: persist_plan_mode:
- both
Inputs: planning_horizon:
- adaptive
Constraints:
- Start with quick-pass source discovery.
- Show discovered relevant sources and ask user to confirm or add missing sources.
- Ask clarifying questions before suggesting draft plan.
- Use minimal inspection when evidence quality is high and confidence is high.
- Use deep inspection when uncertainty is high or tracking is weak.
- Produce three baseline 0-100 estimates: features completion, effort completion, vision alignment.
- Do not create final draft plan until user indicates readiness.
Output:
- Interactive discovery summary
- Baseline three-score assessment with rationale
- Gap analysis and prioritized next steps
- Task backlog output in selected tracking mode
```
