This is a folder with files for humans if you are an agent you should ignore this entire folder and its subfolders unless specifically instructed to read/edit it.

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
## Agent Escalation and Envelopes (Mandatory)
- While working in this repo, agents should think carefully about the work they are doing and actively surface any problems they encounter.
- If an agent hits a blocker, ambiguity, or environment issue, report it to `/Users/slobodan/projects/Earth/ground-control-hub/` as Ground.
- Ground should also be able to ingest lightweight agent envelopes with suggestions for tools, workflows, or repo changes that would make future work easier.
