# Agents Repository

This repository is a documentation-first project for building and organizing software agents.

There is no application code here.  
Instead, this repo stores:

- Agent definitions and plans
- Reusable instructions and templates
- Tutorials for creating and using agents effectively

## Support This Project

Sponsor on GitHub: [github.com/sponsors/slobodanmargetic988](https://github.com/sponsors/slobodanmargetic988)

## Project Goals

- Keep agent work structured and easy to browse
- Make onboarding simple for programmers new to agents
- Capture standards so future agents are consistent and useful

## Usage with agentic AI
Inside whatever tool you are using find the personalisation settings and add this or a similar prompt:
"
I have an entire project used for managing agents I created for use with your workflow. If I specify an agent you can find it under this root directory APSOLUTE_PATH_TO_WHERE_YOU_CLONED_AGENTS_REPO each agent definition is inside subfolder and a README.md and there are examples of agents input and output where possible. Files named TEMPLATES.md are used to generate structured prompts by you or me, I use the blank templates and fill them in.
If I ask you to make a prompt for an agent you should figure out what agent I mean because I will sometimes say orchestrator agent when i mean sprint-orchestrator-agent etc. You should always generate prompts using the template format for that agent so it is clear what agent is being used and the agent gets everithing it needs. 

When working as one of my agents pay attention to the agents/_shared folder and its instructions.
""
## Folder Structure

```text
.
├── agents/
│   ├── agent-making-agent/
│   │   └── README.md
│   └── agent-reviewing-agent/
│       └── README.md
└── guides/
    ├── AGENT_MAKING_INSTRUCTIONS.md
    └── AGENT_USING_INSTRUCTIONS.md
```

## First Agent: Agent Making Agent

The first agent in this repository is **Agent Making Agent**.

Its purpose is to define what all future agents should include:

- Clear purpose
- Well-scoped responsibilities
- Inputs and outputs
- Constraints and safety boundaries
- Verification and quality checks

See `/agents/agent-making-agent/README.md` for the full checklist.

## Getting Started

1. Initialize git:
   ```powershell
   git init
   ```
2. Add files:
   ```powershell
   git add .
   ```
3. Create first commit:
   ```powershell
   git commit -m "Initialize agents documentation repository"
   ```

## How to Work in This Repo

1. Define a new agent folder under `/agents`.
2. Use the guide in `/guides/AGENT_MAKING_INSTRUCTIONS.md`.
3. Document how the agent should be used and validated.
4. Keep changes small and commit frequently.

## Shared Linear Workflow

If you use Linear, keep workflow statuses in one place:

- `C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md`

Agents that synchronize Linear state should receive:

- `Inputs: linear_workflow_path: C:/Users/<username>/Projects/Agents/agents/_shared/LINEAR_WORKFLOW.md`

Update that single file when your Linear status names change (for example `Agent work DONE`, `Agent testing`, `Agent test DONE`), then rerun agents without editing each agent definition.

## Shared Worktree Policy

If you run agents in parallel worktrees, keep worktree behavior in one place:

- `C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md`

Agents should receive:

- `Inputs: worktree_policy_path: C:/Users/<username>/Projects/Agents/agents/_shared/WORKTREE_POLICY.md`

Default behavior:
- Never create a new worktree without explicit user permission.
- If branch switch is blocked and a safe checkpoint commit resolves it, commit with a clear message and continue.
- If safe commit is unclear, stop and ask the user how to proceed.

## Recommended Naming Conventions

- Agent folders: lowercase-kebab-case (example: `bug-finder-agent`)
- Docs: UPPER_SNAKE_CASE for top-level guides, `README.md` inside each agent folder
- Checklists: `CHECKLIST.md` when needed per agent

## Next Step

Use **Agent Making Agent** to create a standard template, then build your second agent using that template.

## Credits

- Made by Slobodan Margetic
- Contact: slobodanmargetic988@gmail.com

## Sponsors

<!-- sponsors --><!-- sponsors -->
