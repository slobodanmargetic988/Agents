#!/usr/bin/env python3
"""Prepare standardized workstation worktrees for worker handoff."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


MAX_WORKSTATIONS = 10
SLOT_RE = re.compile(r"^workstation-(?:[1-9]|10)$")
AGENT_INSTRUCTIONS = (
    "Next step: if this project depends on generated dependency folders "
    "(for example node_modules, .venv, vendor), create a symlink in this workstation "
    "to the source repo's dependency folder before running build/test commands."
)


@dataclass
class WorktreeEntry:
    path: Path
    branch: str | None


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=check, text=True, capture_output=True)


def git_root(repo_input: str) -> Path:
    result = run(
        ["git", "-C", repo_input, "rev-parse", "--show-toplevel"],
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "not a git repository")
    return Path(result.stdout.strip()).resolve()


def list_worktrees(repo_root: Path) -> list[WorktreeEntry]:
    result = run(
        ["git", "-C", str(repo_root), "worktree", "list", "--porcelain"],
        check=True,
    )
    entries: list[WorktreeEntry] = []
    current_path: str | None = None
    current_branch: str | None = None

    for line in result.stdout.splitlines():
        if not line:
            if current_path:
                entries.append(WorktreeEntry(path=Path(current_path).resolve(), branch=current_branch))
            current_path = None
            current_branch = None
            continue

        key, _, value = line.partition(" ")
        if key == "worktree":
            current_path = value
        elif key == "branch":
            current_branch = value.removeprefix("refs/heads/")

    if current_path:
        entries.append(WorktreeEntry(path=Path(current_path).resolve(), branch=current_branch))

    return entries


def slot_name_for_path(path: Path) -> str | None:
    name = path.name
    return name if SLOT_RE.fullmatch(name) else None


def slot_sort_key(slot_name: str) -> int:
    return int(slot_name.rsplit("-", 1)[1])


def default_base_ref(repo_root: Path) -> str:
    result = run(
        ["git", "-C", str(repo_root), "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD"],
        check=False,
    )
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()
    return "HEAD"


def default_worktrees_parent(repo_root: Path) -> Path:
    return (repo_root.parent / f"{repo_root.name}-workstations").resolve()


def revlist_count(repo_path: Path, revspec: str, right_only: bool) -> int:
    args = ["git", "-C", str(repo_path), "rev-list", "--count"]
    args.append("--right-only" if right_only else "--left-only")
    args.append(revspec)
    result = run(args, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"unable to evaluate rev-list for {revspec}")
    raw = result.stdout.strip() or "0"
    return int(raw)


def branch_exists(repo_path: Path, branch_name: str) -> bool:
    result = run(
        ["git", "-C", str(repo_path), "show-ref", "--verify", "--quiet", f"refs/heads/{branch_name}"],
        check=False,
    )
    return result.returncode == 0


def branch_divergence(repo_path: Path, base_ref: str, branch_name: str) -> tuple[int, int]:
    ahead = revlist_count(repo_path, f"{base_ref}...{branch_name}", right_only=True)
    behind = revlist_count(repo_path, f"{base_ref}...{branch_name}", right_only=False)
    return ahead, behind


def working_tree_dirty(worktree_path: Path) -> bool:
    result = run(
        ["git", "-C", str(worktree_path), "status", "--porcelain"],
        check=True,
    )
    return bool(result.stdout.strip())


def checked_out_paths(
    all_worktrees: list[WorktreeEntry],
    branch_name: str,
    exclude_path: Path | None = None,
) -> list[Path]:
    conflicts: list[Path] = []
    for entry in all_worktrees:
        if entry.branch != branch_name:
            continue
        if exclude_path is not None and entry.path == exclude_path:
            continue
        conflicts.append(entry.path)
    return conflicts


def resolve_branch_name(
    *,
    requested_branch: str,
    all_worktrees: list[WorktreeEntry],
    repo_root: Path,
    exclude_path: Path | None,
    fallback_suffix: str | None,
    allow_existing_branch_ref: bool,
) -> tuple[str, bool, list[str], str | None]:
    conflicts = checked_out_paths(all_worktrees, requested_branch, exclude_path)
    if not conflicts:
        return requested_branch, False, [], None

    conflict_paths = [str(path) for path in conflicts]
    if not fallback_suffix:
        return requested_branch, False, conflict_paths, None

    suffix = fallback_suffix.strip()
    if not suffix or any(ch.isspace() for ch in suffix):
        return requested_branch, False, conflict_paths, "fallback suffix must be non-empty and contain no whitespace"

    base_candidate = f"{requested_branch}{suffix}"
    for idx in range(0, 100):
        candidate = base_candidate if idx == 0 else f"{base_candidate}-{idx + 1}"
        candidate_conflicts = checked_out_paths(all_worktrees, candidate, exclude_path)
        if candidate_conflicts:
            continue
        if branch_exists(repo_root, candidate) and not allow_existing_branch_ref:
            continue
        return candidate, True, conflict_paths, None

    return requested_branch, False, conflict_paths, "could not resolve unique fallback branch after 100 attempts"


def payload_base(
    *,
    repo_root: Path,
    base_ref: str,
    managed_count: int,
    output_mode: str,
    dry_run: bool,
) -> dict[str, object]:
    return {
        "repo_root": str(repo_root),
        "base_ref": base_ref,
        "managed_slots": managed_count,
        "max_workstations": MAX_WORKSTATIONS,
        "output": output_mode,
        "dry_run": dry_run,
    }


def with_agent_instructions(payload: dict[str, object]) -> dict[str, object]:
    next_payload = dict(payload)
    next_payload["agent-instructions"] = AGENT_INSTRUCTIONS
    return next_payload


def emit_text(payload: dict[str, object]) -> None:
    if payload.get("ok"):
        print(f"[workstation] repo_root={payload.get('repo_root')}")
        print(f"[workstation] base_ref={payload.get('base_ref')}")
        print(f"[workstation] managed_slots={payload.get('managed_slots')}/{payload.get('max_workstations')}")
        if payload.get("worktree_name"):
            print(f"[workstation] worktree_name={payload.get('worktree_name')}")
        if payload.get("target_path"):
            print(f"[workstation] target_path={payload.get('target_path')}")
        if payload.get("branch_name_resolved"):
            print(f"[workstation] branch_name={payload.get('branch_name_resolved')}")
        if payload.get("branch_fallback_applied"):
            print(
                "[workstation] branch_fallback="
                f"requested={payload.get('branch_name_requested')} resolved={payload.get('branch_name_resolved')}"
            )
        if payload.get("branch_conflict_paths"):
            print(
                "[workstation] branch_conflict_paths=" + ",".join(payload.get("branch_conflict_paths", []))
            )
        if payload.get("repair_results"):
            for item in payload.get("repair_results", []):
                print(
                    "[workstation] repair "
                    f"slot={item.get('worktree_name')} branch={item.get('branch_name_resolved')} "
                    f"status={item.get('status')}"
                )
        if payload.get("message"):
            print(f"[workstation] {payload.get('message')}")
        if payload.get("agent-instructions"):
            print(f"[workstation] agent-instructions={payload.get('agent-instructions')}")
        return

    if payload.get("repo_root"):
        print(f"[workstation] repo_root={payload.get('repo_root')}")
    if payload.get("worktree_name"):
        print(f"[workstation] worktree_name={payload.get('worktree_name')}")
    if payload.get("branch_name_requested"):
        print(f"[workstation] branch_name={payload.get('branch_name_requested')}")
    if payload.get("base_ref"):
        print(f"[workstation] base_ref={payload.get('base_ref')}")
    if payload.get("target_path"):
        print(f"[workstation] target_path={payload.get('target_path')}")
    if payload.get("managed_slots") is not None and payload.get("max_workstations") is not None:
        print(f"[workstation] managed_slots={payload.get('managed_slots')}/{payload.get('max_workstations')}")
    print(f"[workstation] error: {payload.get('error')}", file=sys.stderr)


def emit(payload: dict[str, object], output_mode: str) -> int:
    if output_mode == "json":
        print(json.dumps(payload, sort_keys=True))
    else:
        emit_text(payload)
    return 0 if payload.get("ok") else 2


def fail(message: str, output_mode: str, context: dict[str, object]) -> int:
    payload = dict(context)
    payload.update({"ok": False, "error": message})
    return emit(payload, output_mode)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare workstation worktrees with a hard max-10 gate.")
    parser.add_argument(
        "--repo-root",
        default=".",
        help="path inside the target git repository (default: current directory)",
    )
    parser.add_argument(
        "--worktree-name",
        help="slot name; when omitted, first free standardized slot is selected",
    )
    parser.add_argument(
        "--branch-name",
        help="branch to initialize; defaults to resolved worktree slot name",
    )
    parser.add_argument(
        "--worktrees-parent",
        help=(
            "parent directory for new worktrees "
            "(default: <repo-parent>/<repo-name>-workstations)"
        ),
    )
    parser.add_argument(
        "--base-ref",
        help="base ref used to initialize/reset the branch (default: origin/HEAD fallback HEAD)",
    )
    parser.add_argument(
        "--force-reset-existing",
        action="store_true",
        help="allow destructive reset for existing dirty/diverged slots",
    )
    parser.add_argument(
        "--branch-in-use-fallback-suffix",
        help=(
            "suffix to append when requested branch is already checked out in another worktree "
            "(for example '-dev' or '-test')"
        ),
    )
    parser.add_argument(
        "--repair-all-existing",
        action="store_true",
        help="reset all managed workstation slots in one run",
    )
    parser.add_argument(
        "--output",
        choices=["text", "json"],
        default="text",
        help="output mode for orchestrator parsing (default: text)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print actions only",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        repo_root = git_root(args.repo_root)
        all_worktrees = list_worktrees(repo_root)
    except Exception as exc:  # noqa: BLE001
        return emit(
            {
                "ok": False,
                "error": str(exc),
            },
            args.output,
        )

    managed_slots: dict[str, WorktreeEntry] = {}
    for entry in all_worktrees:
        slot = slot_name_for_path(entry.path)
        if not slot:
            continue
        if slot in managed_slots:
            context = payload_base(
                repo_root=repo_root,
                base_ref=args.base_ref or default_base_ref(repo_root),
                managed_count=len(managed_slots),
                output_mode=args.output,
                dry_run=args.dry_run,
            )
            return fail(f"duplicate managed slot detected for {slot}", args.output, context)
        managed_slots[slot] = entry

    base_ref = args.base_ref or default_base_ref(repo_root)
    context_common = payload_base(
        repo_root=repo_root,
        base_ref=base_ref,
        managed_count=len(managed_slots),
        output_mode=args.output,
        dry_run=args.dry_run,
    )

    if args.repair_all_existing:
        if args.worktree_name:
            return fail("--repair-all-existing cannot be combined with --worktree-name", args.output, context_common)
        if args.branch_name:
            return fail("--repair-all-existing cannot be combined with --branch-name", args.output, context_common)
        if not managed_slots:
            return fail("no managed workstation slots found to repair", args.output, context_common)
        if not args.force_reset_existing and not args.dry_run:
            return fail(
                "--repair-all-existing is destructive; pass --force-reset-existing or use --dry-run",
                args.output,
                context_common,
            )

        repair_results: list[dict[str, object]] = []
        for slot in sorted(managed_slots.keys(), key=slot_sort_key):
            entry = managed_slots[slot]
            requested_branch = entry.branch or slot
            resolved_branch, fallback_used, conflict_paths, resolution_error = resolve_branch_name(
                requested_branch=requested_branch,
                all_worktrees=all_worktrees,
                repo_root=repo_root,
                exclude_path=entry.path,
                fallback_suffix=args.branch_in_use_fallback_suffix,
                allow_existing_branch_ref=True,
            )
            if resolution_error:
                return fail(
                    f"slot '{slot}' branch resolution failed: {resolution_error}",
                    args.output,
                    {
                        **context_common,
                        "worktree_name": slot,
                        "target_path": str(entry.path),
                        "branch_name_requested": requested_branch,
                        "branch_conflict_paths": conflict_paths,
                    },
                )
            if conflict_paths and not fallback_used:
                return fail(
                    f"slot '{slot}' branch '{requested_branch}' is checked out elsewhere; "
                    "set --branch-in-use-fallback-suffix to auto-resolve",
                    args.output,
                    {
                        **context_common,
                        "worktree_name": slot,
                        "target_path": str(entry.path),
                        "branch_name_requested": requested_branch,
                        "branch_conflict_paths": conflict_paths,
                    },
                )

            item_result: dict[str, object] = {
                "worktree_name": slot,
                "target_path": str(entry.path),
                "branch_name_requested": requested_branch,
                "branch_name_resolved": resolved_branch,
                "branch_fallback_applied": fallback_used,
                "branch_conflict_paths": conflict_paths,
                "status": "dry_run" if args.dry_run else "prepared",
            }
            if not args.dry_run:
                try:
                    run(["git", "-C", str(entry.path), "checkout", "-B", resolved_branch, base_ref], check=True)
                    run(["git", "-C", str(entry.path), "reset", "--hard", base_ref], check=True)
                    run(["git", "-C", str(entry.path), "clean", "-fd"], check=True)
                except subprocess.CalledProcessError as exc:
                    return fail(
                        exc.stderr.strip() or str(exc),
                        args.output,
                        {**context_common, **item_result},
                    )
            repair_results.append(item_result)

        return emit(
            {
                **context_common,
                "ok": True,
                "action": "repair_all_existing",
                "repair_results": repair_results,
                "message": (
                    "dry-run: would reset all managed slots"
                    if args.dry_run
                    else "all managed slots prepared in clean state"
                ),
            },
            args.output,
        )

    if args.worktree_name:
        if not SLOT_RE.fullmatch(args.worktree_name):
            return fail("worktree name must be workstation-1 through workstation-10", args.output, context_common)
        worktree_name = args.worktree_name
    else:
        worktree_name = ""
        for index in range(1, MAX_WORKSTATIONS + 1):
            candidate = f"workstation-{index}"
            if candidate not in managed_slots:
                worktree_name = candidate
                break
        if not worktree_name:
            return fail("all workstation slots are occupied; max is 10", args.output, context_common)

    branch_name_requested = args.branch_name or worktree_name
    if not branch_name_requested.strip() or any(ch.isspace() for ch in branch_name_requested):
        return fail("branch name must be non-empty and cannot contain whitespace", args.output, context_common)

    existing_slot = managed_slots.get(worktree_name)
    managed_count = len(managed_slots)
    if existing_slot is None and managed_count >= MAX_WORKSTATIONS:
        return fail("max workstation limit reached (10); refusing to create additional worktrees", args.output, context_common)

    parent_dir = Path(args.worktrees_parent).resolve() if args.worktrees_parent else default_worktrees_parent(repo_root)
    target_path = existing_slot.path if existing_slot else (parent_dir / worktree_name).resolve()

    branch_name_resolved, fallback_used, conflict_paths, resolution_error = resolve_branch_name(
        requested_branch=branch_name_requested,
        all_worktrees=all_worktrees,
        repo_root=repo_root,
        exclude_path=target_path if existing_slot else None,
        fallback_suffix=args.branch_in_use_fallback_suffix,
        allow_existing_branch_ref=args.force_reset_existing,
    )
    if resolution_error:
        return fail(
            resolution_error,
            args.output,
            {
                **context_common,
                "worktree_name": worktree_name,
                "target_path": str(target_path),
                "branch_name_requested": branch_name_requested,
                "branch_conflict_paths": conflict_paths,
            },
        )

    if conflict_paths and not fallback_used:
        return fail(
            f"branch '{branch_name_requested}' is checked out in another worktree; "
            "set --branch-in-use-fallback-suffix to auto-resolve",
            args.output,
            {
                **context_common,
                "worktree_name": worktree_name,
                "target_path": str(target_path),
                "branch_name_requested": branch_name_requested,
                "branch_conflict_paths": conflict_paths,
            },
        )

    context = {
        **context_common,
        "worktree_name": worktree_name,
        "target_path": str(target_path),
        "branch_name_requested": branch_name_requested,
        "branch_name_resolved": branch_name_resolved,
        "branch_fallback_applied": fallback_used,
        "branch_conflict_paths": conflict_paths,
    }

    if existing_slot:
        try:
            dirty = working_tree_dirty(target_path)
            head_ahead = revlist_count(target_path, f"{base_ref}...HEAD", right_only=True)
            branch_ahead = 0
            if branch_exists(target_path, branch_name_resolved):
                branch_ahead = revlist_count(target_path, f"{base_ref}...{branch_name_resolved}", right_only=True)
        except Exception as exc:  # noqa: BLE001
            return fail(str(exc), args.output, context)

        needs_force = dirty or head_ahead > 0 or branch_ahead > 0
        if needs_force and not args.force_reset_existing:
            details = []
            if dirty:
                details.append("working tree has local changes")
            if head_ahead > 0:
                details.append(f"HEAD is ahead of {base_ref} by {head_ahead} commit(s)")
            if branch_ahead > 0:
                details.append(
                    f"branch '{branch_name_resolved}' is ahead of {base_ref} by {branch_ahead} commit(s)"
                )
            return fail(
                "existing slot requires reset but --force-reset-existing is not set: " + "; ".join(details),
                args.output,
                context,
            )

        if args.dry_run:
            return emit(
                {
                    **context,
                    "ok": True,
                    "action": "reset_existing_slot",
                    "message": "dry-run: would reset existing slot",
                },
                args.output,
            )

        try:
            run(["git", "-C", str(target_path), "checkout", "-B", branch_name_resolved, base_ref], check=True)
            run(["git", "-C", str(target_path), "reset", "--hard", base_ref], check=True)
            run(["git", "-C", str(target_path), "clean", "-fd"], check=True)
        except subprocess.CalledProcessError as exc:
            return fail(exc.stderr.strip() or str(exc), args.output, context)

        return emit(
            {
                **context,
                "ok": True,
                "action": "reset_existing_slot",
                "message": "existing slot prepared in clean state",
            },
            args.output,
        )

    if target_path.exists():
        return fail(f"target path already exists and is not a managed slot: {target_path}", args.output, context)

    if not parent_dir.exists():
        if args.dry_run:
            pass
        else:
            try:
                parent_dir.mkdir(parents=True, exist_ok=True)
            except OSError as exc:
                return fail(f"unable to create worktrees parent directory {parent_dir}: {exc}", args.output, context)
    elif not parent_dir.is_dir():
        return fail(f"worktrees parent path is not a directory: {parent_dir}", args.output, context)

    branch_already_exists = branch_exists(repo_root, branch_name_resolved)
    if branch_already_exists:
        try:
            branch_ahead, branch_behind = branch_divergence(repo_root, base_ref, branch_name_resolved)
        except Exception as exc:  # noqa: BLE001
            return fail(str(exc), args.output, context)
        if not args.force_reset_existing:
            divergence_note = (
                f" (ahead {branch_ahead}, behind {branch_behind} vs {base_ref})"
                if branch_ahead > 0 or branch_behind > 0
                else ""
            )
            return fail(
                f"branch '{branch_name_resolved}' already exists{divergence_note}; "
                "refusing to reset existing branch without --force-reset-existing",
                args.output,
                context,
            )

    if args.dry_run:
        message = (
            "dry-run: would create new slot and force-reset existing branch ref"
            if branch_already_exists
            else "dry-run: would create new slot"
        )
        return emit(
            with_agent_instructions(
                {
                **context,
                "ok": True,
                "action": "create_new_slot",
                "message": message,
                }
            ),
            args.output,
        )

    add_args = [
        "git",
        "-C",
        str(repo_root),
        "worktree",
        "add",
        str(target_path),
    ]
    if branch_already_exists:
        add_args.extend(["-B", branch_name_resolved, base_ref])
    else:
        add_args.extend(["-b", branch_name_resolved, base_ref])

    try:
        run(add_args, check=True)
    except subprocess.CalledProcessError as exc:
        return fail(exc.stderr.strip() or str(exc), args.output, context)

    return emit(
        with_agent_instructions(
            {
            **context,
            "ok": True,
            "action": "create_new_slot",
            "message": "new slot created",
            }
        ),
        args.output,
    )


if __name__ == "__main__":
    raise SystemExit(main())
