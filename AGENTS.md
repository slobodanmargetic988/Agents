Ignore `guides/` and its subfolders unless the user explicitly asks to read or edit files there.

Never create a new Git worktree without explicit user permission. If branch switch is blocked by local tracked changes and a safe checkpoint commit resolves it, commit with a clear message and continue; otherwise stop and ask the user.

## Review guidelines
- Read the pull request description first.
- If the pull request description includes expected outcome/task intent, review against that expected outcome before style comments.
- Validate linked issue acceptance criteria before best-practice/style-only suggestions.
- Prioritize correctness, regressions, and security over formatting.
- Treat auth, permissions, payment, and data-loss risks as high priority findings.
- Flag missing or weak tests for changed behavior.
- Require concrete evidence in findings (file/line references and why it matters).
- Keep feedback scoped to changed code unless the change introduces a broader risk.

## Earth Ecosystem Routing (Mandatory)
- Earth-wide project ownership and routing rules live in `/Users/slobodan/projects/Earth/AGENTS.md`.
- OpenRouter model/profile/cost/findings must be written in `/Users/slobodan/projects/Earth/OpenRouter/`.
- Canonical findings ledger: `/Users/slobodan/projects/Earth/OpenRouter/MODEL_EVALUATION_TRACKER.md`.
- Keep this repo focused on agent standards/governance docs; route global model-evaluation findings to `OpenRouter`.
- Example: if asked here to "add findings about OpenRouter minimax cost/quality", add/update `OpenRouter/MODEL_EVALUATION_TRACKER.md` instead of only documenting it in `Agents`.

## TruthGraph Default Context Policy (Mandatory)
- Earth-wide TruthGraph usage policy lives in `/Users/slobodan/projects/Earth/AGENTS.md` and is inherited here.
- For indexed Earth repos, prefer TruthGraph first for deterministic context, impact, ownership, runtime evidence, and worker-bundle retrieval.
- This is a default-first rule, not an exclusive one. Agents must still verify in code when the graph is stale, coverage is shallow, or the requested change is high-risk.
- When the local TruthGraph skill/MCP is available, prefer `truthgraph.resolve_context` before lower-level graph operations or broad filesystem grep.

## LLM Interaction Classification (Mandatory)
- This policy applies to any code step/phase that interacts with an LLM (direct calls, wrappers, dispatchers, orchestrators).
- Classification is for workflow steps/phases, not for planner task entries.
- Every LLM-interacting code step must declare both enums: `reasoning_effort` and `tooling_effort`.
- Allowed `reasoning_effort` values: `low_effort`, `medium_effort`, `high_effort`, `extreme_coordinated_effort`, `requires_input_classification`.
- Allowed `tooling_effort` values: `no_tooling`, `low_tooling`, `medium_tooling`, `high_tooling`, `extreme_mostly_tooling`, `requires_input_classification`.
- If effort depends on runtime input, set both enums to `requires_input_classification` until input-driven classification is resolved.
- Any repo with LLM interactions must contain and maintain a classification document (recommended path: `docs/LLM_INTERACTION_CLASSIFICATION.md`) mapping code steps to both enums.
- Any function/method that performs LLM interaction must include a nearby code comment describing its two classifications.
- Default routing guardrail: do not use variable/free-tier model routing for steps above `medium_effort` or above `medium_tooling`, or for steps marked `requires_input_classification`.
- All agents across Earth must honor this classification before selecting models, agents, or delegation strategy.


## Earth Project Quick Lookup (Mandatory)
- `Agents`: agent standards, shared policies, and reusable skills (`/Users/slobodan/projects/Earth/Agents/`).
- `MyBoard`: operator workspace product (FastAPI + Nuxt) for board/task orchestration (`/Users/slobodan/projects/Earth/MyBoard/`).
- `MyOwnMint`: safety-first trading intelligence and execution workflows (`/Users/slobodan/projects/Earth/MyOwnMint/`).
- `OpenRouter`: canonical model/provider findings and profile metadata (`/Users/slobodan/projects/Earth/OpenRouter/`).
- `Optimus-Prime-GSD-Fusion`: OP/BP orchestration runtime and `/op-*` automation core (`/Users/slobodan/projects/Earth/Optimus-Prime-GSD-Fusion/`).
- `Tetris`, `Tetris2`, `Tetris2 copy`: canary repos for orchestration validation, not product strategy baselines.
- `bitnet`: low-bit inference experimentation/reference integration (`/Users/slobodan/projects/Earth/bitnet/`).
- `contracts`: frozen cross-project schemas/contracts (`/Users/slobodan/projects/Earth/contracts/`).
- `elastic-mesh`: telemetry ingest/index/search mesh (`/Users/slobodan/projects/Earth/elastic-mesh/`).
- `go-backend-lab`: Go vs Python backend benchmark evidence (`/Users/slobodan/projects/Earth/go-backend-lab/`).
- `ground-control-hub`: portfolio control-plane and cross-project graph (`/Users/slobodan/projects/Earth/ground-control-hub/`).
- `merge-watch-core`: archived historical reference only (active merge authority is `op-tools/active-merger`).
- `ninja-doctor-core`: autonomous maintenance/integrity defense (`/Users/slobodan/projects/Earth/ninja-doctor-core/`).
- `oroboro-core`: identity/brand system execution artifacts (`/Users/slobodan/projects/Earth/oroboro-core/`).
- `token-format-lab`: token-efficient structured format R&D (`/Users/slobodan/projects/Earth/token-format-lab/`).
- `torrent-vault-lab`: distributed storage/replication feasibility (`/Users/slobodan/projects/Earth/torrent-vault-lab/`).
- `trace-clarity-engine`: explainability and trace instrumentation standards (`/Users/slobodan/projects/Earth/trace-clarity-engine/`).
- `wallet-recovery-lab`: lawful, ownership-bound wallet recovery workflows (`/Users/slobodan/projects/Earth/wallet-recovery-lab/`).

## Cross-Project Discovery Workflow (Mandatory)
- Start with `/Users/slobodan/projects/Earth/AGENTS.md` for global ownership/routing rules.
- For project intent and boundaries, read that repo's `mission.md` and `scope.md` first.
- For model/provider usage findings, write canonical entries in `/Users/slobodan/projects/Earth/OpenRouter/MODEL_EVALUATION_TRACKER.md`.
- For shared interface/schema questions, use `/Users/slobodan/projects/Earth/contracts/` as source of truth.
- When a request spans repos, update the canonical owner repo first, then add local backlinks where helpful.

## OP-Build Alignment (Mandatory)
- Earth root policy lives in `/Users/slobodan/projects/Earth/AGENTS.md`.
- Canonical `op-build` usage lives in `/Users/slobodan/projects/Earth/OP_BUILD_ECOSYSTEM_GUIDE.md`.
- This repo defines and sharpens agent behavior for Earth-wide build work, so keep its guidance aligned with the canonical `op-build` contract.
- If you make a commit during an `op-build` task, push it immediately after the commit.

## Repo-Specific OP-Build Role Guidance
- `planner`: write guidance that reduces ambiguity for future workers instead of mirroring one temporary task packet.
- `architect`: keep shared standards composable so repo-local `AGENTS.md` files can inherit them without losing local specificity.
- `implementer`: favor small, auditable doc and policy changes that clearly improve build behavior across Earth.
- `tester`: verify that new guidance is concrete, non-conflicting, and usable by agents working without extra explanation from the operator.
- `reviewer`: flag vague language, duplicated policy, or repo instructions that silently override Earth root behavior.
- `documenter`: treat this file and sibling governance docs as living operator memory and record durable standards here.
