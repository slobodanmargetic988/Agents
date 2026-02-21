#!/usr/bin/env python3
"""Prepare standardized workstation worktrees for worker handoff."""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
import re


MAX_WORKSTATIONS = 10
SLOT_RE = re.compile(r"^workstation-(?:[1-9]|10)$")


@dataclass
class WorktreeEntry:
    path: Path
    branch: str | None


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=check, text=True, capture_output=True)


def fail(message: str) -> int:
    print(f"[workstation] error: {message}", file=sys.stderr)
    return 2


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


def default_base_ref(repo_root: Path) -> str:
    result = run(
        ["git", "-C", str(repo_root), "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD"],
        check=False,
    )
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()
    return "HEAD"


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


def working_tree_dirty(worktree_path: Path) -> bool:
    result = run(
        ["git", "-C", str(worktree_path), "status", "--porcelain"],
        check=True,
    )
    return bool(result.stdout.strip())


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
        help="parent directory for new worktrees (default: parent of repo root)",
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
        return fail(str(exc))

    managed_slots: dict[str, WorktreeEntry] = {}
    for entry in all_worktrees:
        slot = slot_name_for_path(entry.path)
        if not slot:
            continue
        if slot in managed_slots:
            return fail(f"duplicate managed slot detected for {slot}")
        managed_slots[slot] = entry

    if args.worktree_name:
        if not SLOT_RE.fullmatch(args.worktree_name):
            return fail("worktree name must be workstation-1 through workstation-10")
        worktree_name = args.worktree_name
    else:
        worktree_name = ""
        for index in range(1, MAX_WORKSTATIONS + 1):
            candidate = f"workstation-{index}"
            if candidate not in managed_slots:
                worktree_name = candidate
                break
        if not worktree_name:
            return fail("all workstation slots are occupied; max is 10")

    branch_name = args.branch_name or worktree_name
    if not branch_name.strip() or any(ch.isspace() for ch in branch_name):
        return fail("branch name must be non-empty and cannot contain whitespace")

    existing_slot = managed_slots.get(worktree_name)
    managed_count = len(managed_slots)
    if existing_slot is None and managed_count >= MAX_WORKSTATIONS:
        return fail("max workstation limit reached (10); refusing to create additional worktrees")

    base_ref = args.base_ref or default_base_ref(repo_root)
    parent_dir = Path(args.worktrees_parent).resolve() if args.worktrees_parent else repo_root.parent.resolve()
    target_path = existing_slot.path if existing_slot else (parent_dir / worktree_name).resolve()

    print(f"[workstation] repo_root={repo_root}")
    print(f"[workstation] worktree_name={worktree_name}")
    print(f"[workstation] branch_name={branch_name}")
    print(f"[workstation] base_ref={base_ref}")
    print(f"[workstation] target_path={target_path}")
    print(f"[workstation] managed_slots={managed_count}/{MAX_WORKSTATIONS}")

    if existing_slot:
        try:
            dirty = working_tree_dirty(target_path)
            head_ahead = revlist_count(target_path, f"{base_ref}...HEAD", right_only=True)
            branch_ahead = 0
            if branch_exists(target_path, branch_name):
                branch_ahead = revlist_count(target_path, f"{base_ref}...{branch_name}", right_only=True)
        except Exception as exc:  # noqa: BLE001
            return fail(str(exc))

        needs_force = dirty or head_ahead > 0 or branch_ahead > 0
        if needs_force and not args.force_reset_existing:
            details = []
            if dirty:
                details.append("working tree has local changes")
            if head_ahead > 0:
                details.append(f"HEAD is ahead of {base_ref} by {head_ahead} commit(s)")
            if branch_ahead > 0:
                details.append(f"branch '{branch_name}' is ahead of {base_ref} by {branch_ahead} commit(s)")
            return fail(
                "existing slot requires reset but --force-reset-existing is not set: "
                + "; ".join(details)
            )

        if args.dry_run:
            print("[workstation] dry-run: would reset existing slot")
            return 0

        try:
            run(["git", "-C", str(target_path), "checkout", "-B", branch_name, base_ref], check=True)
            run(["git", "-C", str(target_path), "reset", "--hard", base_ref], check=True)
            run(["git", "-C", str(target_path), "clean", "-fd"], check=True)
        except subprocess.CalledProcessError as exc:
            return fail(exc.stderr.strip() or str(exc))

        print("[workstation] existing slot prepared in clean state")
        return 0

    if target_path.exists():
        return fail(f"target path already exists and is not a managed slot: {target_path}")

    if args.dry_run:
        print("[workstation] dry-run: would create new slot")
        return 0

    try:
        run(
            [
                "git",
                "-C",
                str(repo_root),
                "worktree",
                "add",
                "-B",
                branch_name,
                str(target_path),
                base_ref,
            ],
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        return fail(exc.stderr.strip() or str(exc))

    print("[workstation] new slot created")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
