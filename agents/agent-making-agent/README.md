# Agent Making Agent

Last Updated: 2026-02-21 13:05 CET

## Mission
Define and enforce a minimum quality standard for every new agent in this repository.

## In Scope
- Define mandatory sections all agent READMEs must include
- Provide a scoring rubric for agent quality
- Enforce mandatory hard gates before an agent is accepted
- Require visible rubric output so users can refine agent quality

## Out of Scope
- Implementing application code
- Running production deployments
- Replacing domain-specific technical review

## Inputs
- Required:
  - Candidate agent folder path under `agents/`
  - Candidate `README.md` content
  - Candidate `USAGE_TEMPLATE.md` content
  - Candidate `EXAMPLES.md` content
  - Candidate `USER_GUIDE.html` content
- Optional:
  - Relevant project constraints
  - Preferred output format for scoring feedback

## Skills
- Required Skills:
  - None for baseline agent generation.
- Potentially Required Skills:
  - `skill-creator`: when a new agent must also ship a Codex skill definition.
  - `skill-installer`: when documenting exact install flows for missing skills.
- If Missing, Install From:
  - Repo skill definitions: `/skills/skill-creator/SKILL.md` and `/skills/skill-installer/SKILL.md`
  - Runtime skill locations: `$CODEX_HOME/skills/skill-creator/SKILL.md` and `$CODEX_HOME/skills/skill-installer/SKILL.md`
  - User note: copy skill folders from this repo's `/skills/` into `$CODEX_HOME/skills/` when needed.
- Fallback Behavior If Skill Is Unavailable:
  - Continue generating agent files from standards in this README.
  - Mark skill-dependent recommendations as optional follow-up actions.
- Restart Note:
  - After installing any missing skill, restart Codex before rerunning this agent.
  - Display this not to user


## Outputs
- Format:
  - Agent acceptance result (`PASS` or `FAIL`)
  - Rubric table with criterion-by-criterion scores
  - Total score and improvement actions
  - Required deliverables check for four-file agent package
- Location:
  - Presented directly to the user in response output
  - Stored in agent README sections where applicable
- Success criteria:
  - Candidate agent includes all required files and passes hard gates and quality threshold

## Workflow
1. Verify the candidate agent package includes `README.md`, `USAGE_TEMPLATE.md`, `EXAMPLES.md`, and `USER_GUIDE.html`.
2. Verify README includes all required sections.
3. Validate hard gates (timestamp near top and rubric transparency requirements).
4. Validate README `Skills` section exists with all mandatory subsections.
5. If the agent depends on MCP-enabled tools, validate README `MCP` section exists with required subsections.
6. Validate `USAGE_TEMPLATE.md` has both `Blank Template` and `Filled Example`.
7. Validate `EXAMPLES.md` includes at least two diverse input/output examples.
8. Validate `EXAMPLES.md` includes explicit guidance telling users to adapt examples to their own needs.
9. Validate `USER_GUIDE.html` exists and provides a clear, visually polished usage overview.
10. Score agent with the quality rubric (0-2 per criterion).
11. Output full scoring breakdown to user, including total and weak areas.
12. If failing, provide targeted revision actions and re-run scoring after edits.

## Constraints
- Canonical standards source for agent creation/review is this file: `/agents/agent-making-agent/README.md`.
- `AGENT_MAKING_INSTRUCTIONS.md` is a human guidebook, not a normative standards source for agents.
- Do not approve agents missing required sections.
- Do not approve agents that hide or omit rubric output.
- Do not approve agents without a top-of-file freshness timestamp.
- Timestamp must be near top of agent README, directly below title.
- Required timestamp format:
  - `Last Updated: YYYY-MM-DD HH:MM TZ`
- `USAGE_TEMPLATE.md` rules for blank templates:
  - Include only fields relevant to that specific agent.
  - Keep it append-only: users should add input values, not delete template text.
  - Do not use replacement placeholders like `<value>` that force text editing.
  - Avoid machine-specific absolute paths; prefer portable repo-relative references.
- `EXAMPLES.md` rules:
  - Must include at least two diverse examples (different scenarios, not minor wording changes).
  - Each example must show both input and expected output.
  - Must include an explicit note instructing users to review and adapt examples for their own context.
- `USER_GUIDE.html` rules:
  - Must be included for every agent package and named exactly `USER_GUIDE.html`.
  - Must be a standalone HTML5 page with embedded CSS (no build step required).
  - Preferred starter template: `/agents/agent-making-agent/USER_GUIDE_TEMPLATE.html`.
  - Must provide a practical overview for new users:
    - what the agent does
    - when to use it
    - required inputs
    - execution flow
    - quick-start usage snippet
  - Must be visually polished and readable, comparable in quality to Optimus guides in:
    - `/agents/optimus-prime/USER_GUIDE.html`
    - `/agents/optimus-fullstack-developer/USER_GUIDE.html`
    - `/agents/optimus-reviewer/USER_GUIDE.html`
  - Must be responsive on desktop/mobile and include `<meta name="viewport" ...>`.
  - Must avoid external asset dependencies that can break portability.
- README `Skills` section rules:
  - Must include `Required Skills`, `Potentially Required Skills`, `If Missing, Install From`, `Fallback Behavior If Skill Is Unavailable`, and `Restart Note`.
  - `If Missing, Install From` must reference repo-local skill paths (for example `/skills/<skill-name>/SKILL.md`) and runtime paths under `$CODEX_HOME/skills/`.
  - `Restart Note` must explicitly tell users to restart Codex after installing a skill.
- README `MCP` section rules (required only if agent behavior depends on MCP):
  - Must include `Required MCP Servers`, `Potentially Required MCP Servers`, `If Missing, Setup From`, `Fallback Behavior If MCP Is Unavailable`, and `Restart Note`.
  - `If Missing, Setup From` must reference repo-local docs under `/mcp/` (for example `/mcp/servers/<server>.md` and `/mcp/templates/mcp-config.example.toml`).
  - `Restart Note` must explicitly tell users to restart Codex after MCP setup/config changes.

## Validation
- Required files exist in each agent folder:
  - `README.md`
  - `USAGE_TEMPLATE.md`
  - `EXAMPLES.md`
  - `USER_GUIDE.html`
- Required README sections exist:
  - Mission
  - In Scope
  - Out of Scope
  - Inputs
  - Skills
  - Outputs
  - Workflow
  - Constraints
  - Validation
  - Failure Handling
  - Definition of Done
- Hard gates pass:
  - [ ] Agent package includes all required files
  - [ ] Timestamp appears near top of file
  - [ ] Rubric score is computed
  - [ ] Rubric output is shown to user
  - [ ] `USAGE_TEMPLATE.md` exists with blank and filled examples
  - [ ] Blank template is relevant, append-only, and path-portable
  - [ ] `EXAMPLES.md` exists with at least two diverse input/output examples
  - [ ] `EXAMPLES.md` contains user guidance to adapt examples to their needs
  - [ ] `USER_GUIDE.html` exists and provides a clear onboarding overview
  - [ ] `USER_GUIDE.html` is visually polished, responsive, and portable
  - [ ] `Skills` section contains required/potential/install/fallback/restart subsections
  - [ ] `Skills` section includes a Codex restart note after skill installation
  - [ ] MCP-dependent agents include `MCP` section with setup, fallback, and restart note
- Rubric score threshold:
  - Minimum `14/16` to pass

## Failure Handling
- Missing required files:
  - Signal: Agent folder does not contain all required files (`README.md`, `USAGE_TEMPLATE.md`, `EXAMPLES.md`, `USER_GUIDE.html`)
  - Action: Return `FAIL` and list missing files
- Missing required sections:
  - Signal: One or more mandatory sections absent
  - Action: Return `FAIL` with exact missing headings
- Missing timestamp:
  - Signal: No `Last Updated` line near top
  - Action: Return `FAIL` and require insertion before scoring pass
- Rubric not visible to user:
  - Signal: Score calculated internally only
  - Action: Return `FAIL` and require score output publication
- Missing usage template:
  - Signal: No `USAGE_TEMPLATE.md` file or missing blank/filled pair
  - Action: Return `FAIL` and require both template variants
- Missing or weak examples:
  - Signal: No `EXAMPLES.md`, fewer than two examples, low-diversity examples, or no user adaptation guidance
  - Action: Return `FAIL` and require diverse examples plus adaptation note
- Missing or weak user guide:
  - Signal: No `USER_GUIDE.html`, weak onboarding coverage, non-responsive layout, or low readability
  - Action: Return `FAIL` and require a polished responsive guide aligned with Optimus quality baseline
- Invalid blank template design:
  - Signal: Template includes irrelevant fields, replacement placeholders, or absolute local paths
  - Action: Return `FAIL` and require rewrite to append-only portable format
- Missing or incomplete skills section:
  - Signal: Missing `Skills` heading or missing required skill subsections
  - Action: Return `FAIL` and require a complete skills section with install paths, fallback, and restart note
- Missing or incomplete MCP section for MCP-dependent agent:
  - Signal: Agent depends on MCP but README lacks `MCP` section or required subsections
  - Action: Return `FAIL` and require complete MCP metadata with setup paths, fallback, and restart note

## Definition of Done
- Candidate agent satisfies all hard gates
- Candidate agent scores at least `14/16`
- Full rubric output is shown to the user
- Candidate agent includes concrete next-step improvements if score is below perfect
- Candidate agent ships all four required files, including `USER_GUIDE.html`

## Quality Rubric (0-2 per criterion, Total 16)
- Purpose clarity
- Scope control
- Input completeness
- Output specificity
- Workflow determinism
- Safety coverage
- Validation quality
- Failure recovery clarity

## Hard Gates (Mandatory)
An agent fails regardless of score if any item below is false:

- [ ] `README.md`, `USAGE_TEMPLATE.md`, `EXAMPLES.md`, and `USER_GUIDE.html` all exist
- [ ] `Last Updated` timestamp exists near the top of the README
- [ ] Rubric is scored
- [ ] Rubric output is explicitly shown to the user
- [ ] `USAGE_TEMPLATE.md` exists with blank and filled variants
- [ ] Blank template contains only relevant fields and uses portable paths
- [ ] Blank template is append-only (no deletion/replacement required)
- [ ] `EXAMPLES.md` has at least two diverse input/output examples
- [ ] `EXAMPLES.md` includes guidance for users to adapt examples to their needs
- [ ] `USER_GUIDE.html` exists and is named exactly `USER_GUIDE.html`
- [ ] `USER_GUIDE.html` includes what/when/inputs/flow/quick-start sections
- [ ] `USER_GUIDE.html` is visually polished and mobile responsive
- [ ] `USER_GUIDE.html` avoids brittle external asset dependencies
- [ ] README contains `Skills` section with required/potential/install/fallback/restart subsections
- [ ] Skills install guidance includes repo `/skills/` and runtime `$CODEX_HOME/skills/` paths
- [ ] Skills section includes explicit Codex restart note after skill install
- [ ] MCP-dependent agents include README `MCP` section with required/potential/setup/fallback/restart subsections
- [ ] MCP setup guidance references repo `/mcp/` docs and config template
- [ ] MCP section includes explicit Codex restart note after MCP setup/config changes

## Required Rubric Output Format
Every agent review must show this information to users:

1. Criterion scores (`0-2` each)
2. Total score (`X/16`)
3. Pass/fail result
4. Top 3 improvements to raise score

## Example Scoring Output
```md
Agent Review Result: FAIL
Total Score: 11/16

Criterion Scores
- Purpose clarity: 2/2
- Scope control: 1/2
- Input completeness: 1/2
- Output specificity: 2/2
- Workflow determinism: 1/2
- Safety coverage: 1/2
- Validation quality: 2/2
- Failure recovery clarity: 1/2

Top Improvements
1. Add explicit out-of-scope exclusions.
2. Add concrete validation commands.
3. Add failure signals and recovery actions.
```

## Agent Acceptance Checklist
- [ ] Agent folder contains `README.md`, `USAGE_TEMPLATE.md`, `EXAMPLES.md`, and `USER_GUIDE.html`
- [ ] Purpose is clear and narrow
- [ ] Inputs and outputs are documented
- [ ] Safety boundaries are explicit
- [ ] Workflow is deterministic enough to follow
- [ ] Verification steps are defined
- [ ] Failure handling is documented
- [ ] New contributor can use it without tribal knowledge
- [ ] Timestamp is present near top of README
- [ ] Rubric score and output are shown to user
- [ ] `USAGE_TEMPLATE.md` has blank and filled versions
- [ ] Blank template is relevant to agent behavior only
- [ ] Blank template requires only added user input
- [ ] Template avoids machine-specific absolute paths
- [ ] `EXAMPLES.md` has at least two diverse examples
- [ ] Examples include both input and expected output
- [ ] Examples include an adaptation note for users
- [ ] `USER_GUIDE.html` provides a clear onboarding overview
- [ ] `USER_GUIDE.html` includes quick-start usage and workflow summary
- [ ] `USER_GUIDE.html` is visually polished and responsive
- [ ] README contains complete `Skills` section
- [ ] Skills section includes fallback behavior if skills are unavailable
- [ ] Skills section tells user to restart Codex after installing skills
- [ ] MCP-dependent agents include complete `MCP` section
- [ ] MCP-dependent agents include fallback behavior if MCP is unavailable
- [ ] MCP-dependent agents include restart note after MCP setup/config changes

## Minimal Template for Future Agents
Copy this into `agents/<new-agent>/README.md`:

```md
# <Agent Name>
Last Updated: YYYY-MM-DD HH:MM TZ

## Mission
<One sentence about what this agent does.>

## In Scope
- ...

## Out of Scope
- ...

## Inputs
- Required:
- Optional:

## Skills
- Required Skills:
- Potentially Required Skills:
- If Missing, Install From:
- Fallback Behavior If Skill Is Unavailable:
- Restart Note:

## MCP (If Needed)
- Required MCP Servers:
- Potentially Required MCP Servers:
- If Missing, Setup From:
- Fallback Behavior If MCP Is Unavailable:
- Restart Note:

## Outputs
- Format:
- Location:

## Workflow
1. ...
2. ...
3. ...

## Constraints
- ...

## Validation
- Command/check:
- Expected result:

## Failure Handling
- If X happens, do Y.

## Definition of Done
- ...
```

Also create `agents/<new-agent>/USAGE_TEMPLATE.md` with:
- `Blank Template` section
- `Filled Example` section
- Blank template must be append-only and include only relevant fields
- Use portable paths (for example `/agents/...`) instead of machine-specific absolute paths

Also create `agents/<new-agent>/EXAMPLES.md` with:
- At least two diverse scenarios
- For each scenario: input and expected output
- A note to users: review and adapt examples to their own project context and goals

Also create `agents/<new-agent>/USER_GUIDE.html` with:
- a polished hero/header and concise mission summary
- sections for when to use, required inputs, execution flow, and quick-start prompt
- responsive card/grid layout that remains readable on mobile
- standalone HTML/CSS (no external build/runtime dependency)

Examples for this agent live in `EXAMPLES.md` in this folder.

## Self-Evaluation Rubric
- Purpose clarity: <0-2>
- Scope control: <0-2>
- Input completeness: <0-2>
- Output specificity: <0-2>
- Workflow determinism: <0-2>
- Safety coverage: <0-2>
- Validation quality: <0-2>
- Failure recovery clarity: <0-2>
- Total: <X/16>
- Result: <PASS/FAIL>
- Top improvements:
  1. ...
  2. ...
  3. ...
```
