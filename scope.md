# Scope

This is a tuning/hardening scope for an existing documentation-and-template repository, not a greenfield product build.

## Baseline reality

- repository already contains many agents, skills, guides, and shared conventions,
- quality is uneven across assets (format, contract strictness, examples, validation depth),
- cross-agent behavior and shared terminology need normalization,
- orchestration consumers need clearer machine-friendly contracts.

## Scope objectives for this era

- normalize all primary agent definitions to a common contract structure,
- enforce explicit input/output/verification sections for each agent family,
- update prompt templates so they are deterministic, role-aware, and reusable by OP/BP flows,
- remove stale assumptions and references that conflict with local-task workflows,
- add compatibility matrix and migration notes where agent behavior changed,
- create deterministic quality checks for agent docs/templates (schema/content checks),
- produce practical examples showing high-quality prompts and expected outputs,
- improve discoverability: index pages by function, lifecycle phase, and dependency,
- define versioning policy for breaking vs non-breaking agent changes,
- ensure every critical shared policy lives in one canonical path and is linked consistently.

## Boundaries

- do not convert this repo into a runtime web app; keep docs+assets-first architecture,
- do not introduce heavy platform dependencies that block contributor onboarding,
- preserve useful existing material; refactor instead of deleting unless clearly obsolete.

## Deliverables

- updated agent catalog with standardized contracts,
- updated shared templates and examples,
- quality-check scripts for docs/template integrity,
- migration/changelog notes for changed contracts,
- operator-facing quickstart for applying agents in Earth projects.

## Definition of done

- critical agent families pass deterministic contract checks,
- at least one full end-to-end example exists per major agent role,
- no broken internal references for core docs/templates,
- autonomous orchestrators can consume repository outputs without ad-hoc interpretation.

## Planning decomposition requirement (hard gate)

Before any build starts, planning must produce **at least 400 atomic tasks** in plan artifacts.

Task quality requirements:

- each task should fit a 5-10 minute worker execution window,
- each task must have explicit acceptance criteria and evidence expectation,
- dependencies must allow strong parallelization after setup tasks,
- phases and lanes must be explicit so execution can scale safely.
