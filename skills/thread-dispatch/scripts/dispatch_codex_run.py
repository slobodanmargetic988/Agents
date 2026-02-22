#!/usr/bin/env python3
"""Dispatch a separate Codex exec run from the current thread."""

from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Start a separate codex exec run with prompt text."
    )
    parser.add_argument(
        "--cwd",
        required=True,
        help="Workspace directory where the new codex run should execute.",
    )
    parser.add_argument("--prompt", help="Prompt text to send to codex exec.")
    parser.add_argument(
        "--prompt-file",
        help="Path to a UTF-8 text file containing the prompt.",
    )
    parser.add_argument(
        "--background",
        action="store_true",
        default=True,
        help="Run detached in background (default behavior).",
    )
    parser.add_argument(
        "--foreground",
        action="store_true",
        help="Run in foreground and stream output to current terminal.",
    )
    parser.add_argument(
        "--full-auto",
        action="store_true",
        default=True,
        help="Pass --full-auto to codex exec (default behavior).",
    )
    parser.add_argument(
        "--no-full-auto",
        action="store_true",
        help="Do not pass --full-auto to codex exec.",
    )
    parser.add_argument(
        "--extra-arg",
        action="append",
        default=[],
        help="Additional argument to pass to codex exec (repeatable).",
    )
    parser.add_argument(
        "--log-dir",
        help="Directory for detached run logs. Default: <cwd>/.codex-dispatch",
    )
    parser.add_argument(
        "--codex-home",
        help=(
            "Override CODEX_HOME for the spawned codex process "
            "(same effect as prefixing the command with CODEX_HOME=...)"
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the command and metadata without starting it.",
    )
    return parser.parse_args()


def load_prompt(args: argparse.Namespace) -> str:
    if bool(args.prompt) == bool(args.prompt_file):
        raise ValueError("provide exactly one of --prompt or --prompt-file")
    if args.prompt:
        return args.prompt.strip()
    prompt_path = Path(args.prompt_file).expanduser().resolve()
    if not prompt_path.is_file():
        raise ValueError(f"prompt_file_not_found:{prompt_path}")
    text = prompt_path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("prompt_file_empty")
    return text


def build_command(args: argparse.Namespace, prompt_text: str) -> list[str]:
    cmd = ["codex", "exec"]
    use_full_auto = args.full_auto and not args.no_full_auto
    if use_full_auto:
        cmd.append("--full-auto")
    cmd.extend(["--cd", str(Path(args.cwd).expanduser().resolve())])
    if args.extra_arg:
        cmd.extend(args.extra_arg)
    cmd.append(prompt_text)
    return cmd


def build_env(args: argparse.Namespace) -> dict[str, str]:
    env = os.environ.copy()
    if args.codex_home:
        env["CODEX_HOME"] = str(Path(args.codex_home).expanduser())
    return env


def main() -> int:
    args = parse_args()
    cwd = Path(args.cwd).expanduser().resolve()
    if not cwd.is_dir():
        print(f"error: cwd_not_found:{cwd}", file=sys.stderr)
        return 2

    try:
        prompt_text = load_prompt(args)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    cmd = build_command(args, prompt_text)
    env = build_env(args)
    mode = "foreground" if args.foreground else "background"
    if args.foreground:
        args.background = False

    if args.log_dir:
        log_dir = Path(args.log_dir).expanduser().resolve()
    else:
        log_dir = cwd / ".codex-dispatch"
    log_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    log_file = log_dir / f"dispatch-{ts}.log"

    payload = {
        "mode": mode,
        "cwd": str(cwd),
        "command": cmd,
        "command_shell": shlex.join(cmd),
        "log_file": str(log_file),
        "codex_home": env.get("CODEX_HOME"),
    }
    if payload["codex_home"]:
        payload["command_shell_with_env"] = (
            f"CODEX_HOME={shlex.quote(payload['codex_home'])} " + shlex.join(cmd)
        )

    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=True, indent=2))
        return 0

    if args.background:
        with log_file.open("w", encoding="utf-8") as out:
            proc = subprocess.Popen(  # noqa: S603
                cmd,
                cwd=str(cwd),
                stdout=out,
                stderr=subprocess.STDOUT,
                start_new_session=True,
                env=env,
            )
        payload["pid"] = proc.pid
        payload["status"] = "started"
        print(json.dumps(payload, ensure_ascii=True, indent=2))
        return 0

    completed = subprocess.run(  # noqa: S603
        cmd,
        cwd=str(cwd),
        env=env,
        check=False,
    )
    payload["status"] = "finished"
    payload["exit_code"] = completed.returncode
    print(json.dumps(payload, ensure_ascii=True, indent=2))
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
