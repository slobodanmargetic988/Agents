#!/usr/bin/env python3

from __future__ import annotations

import argparse
import copy
import json
import subprocess
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


MINIMUM_VISIBLE_TEMPLATE_INDICES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13]
STARTER_TEMPLATES: dict[str, dict[str, str]] = {
    "optimus-prime": {
        "description": "Full app-development orchestrator thread starter for autonomous multi-worker execution.",
        "core_base_instructions_file": "optimus-prime/optimus-prime-base-instructions.txt",
        "user_personalization_file": "optimus-prime/optimus-prime-personalization.txt",
        "tools_descriptions_and_when_to_use_file": "optimus-prime/optimus-prime-tools-descriptions.txt",
    },
    "project-planner": {
        "description": "Project planning/priming thread starter for building documentation and plans before task execution.",
        "core_base_instructions_file": "project-planner/project-planner.txt",
        "user_personalization_file": "project-planner/project-planner-personalization.txt",
        "tools_descriptions_and_when_to_use_file": "project-planner/project-planner-tools-descriptions.txt",
    },
}


def _script_dir() -> Path:
    return Path(__file__).resolve().parent


def _skill_root() -> Path:
    return _script_dir().parent


def _assets_dir() -> Path:
    return _skill_root() / "assets"


def _load_text_file(path: str | Path) -> str:
    return Path(path).expanduser().read_text()


def _read_text_or_file(
    *,
    text: str | None,
    file_path: str | None,
    default: str | None = None,
    trim_trailing_newlines: bool = False,
) -> str:
    if text is not None and file_path is not None:
        raise ValueError("Provide either text or file, not both")
    if file_path is not None:
        value = _load_text_file(file_path)
    elif text is not None:
        value = text
    elif default is not None:
        value = default
    else:
        raise ValueError("Missing required text/file input")
    if trim_trailing_newlines:
        value = value.rstrip("\n")
    return value


def _iso_z(dt: datetime) -> str:
    dt = dt.astimezone(timezone.utc)
    return dt.isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _filename_timestamp(dt: datetime) -> str:
    dt = dt.astimezone(timezone.utc)
    return dt.strftime("%Y-%m-%dT%H-%M-%S")


def _build_environment_context(cwd: str, shell: str) -> str:
    return (
        "<environment_context>\n"
        f"  <cwd>{cwd}</cwd>\n"
        f"  <shell>{shell}</shell>\n"
        "</environment_context>"
    )


def _extract_collaboration_mode_inner(events: list[dict[str, Any]]) -> str:
    text = events[5]["payload"]["content"][0]["text"]
    prefix = "<collaboration_mode>"
    suffix = "</collaboration_mode>"
    if text.startswith(prefix) and text.endswith(suffix):
        return text[len(prefix) : -len(suffix)]
    # Fallback to the common default inner block if template was changed unexpectedly.
    return (
        "# Collaboration Mode: Default\n\n"
        "You are now in Default mode. Any previous instructions for other modes (e.g. Plan mode) are no longer active.\n\n"
        "Your active mode changes only when new developer instructions with a different "
        "`<collaboration_mode>...</collaboration_mode>` change it; user requests or tool descriptions do not change mode by themselves. "
        "Known mode names are Default and Plan.\n\n"
        "## request_user_input availability\n\n"
        "The `request_user_input` tool is unavailable in Default mode. If you call it while in Default mode, it will return an error.\n\n"
        "If a decision is necessary and cannot be discovered from local context, ask the user directly. "
        "However, in Default mode you should strongly prefer executing the user's request rather than stopping to ask questions.\n"
    )


def _run_git(cwd: str, args: list[str]) -> str | None:
    try:
        proc = subprocess.run(
            ["git", "-C", cwd, *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    value = proc.stdout.strip()
    return value or None


def _resolve_git_values(
    *,
    cwd: str,
    commit_hash: str | None,
    branch: str | None,
    repository_url: str | None,
) -> tuple[str, str, str]:
    resolved_commit = commit_hash or _run_git(cwd, ["rev-parse", "HEAD"])
    resolved_branch = branch or _run_git(cwd, ["rev-parse", "--abbrev-ref", "HEAD"])
    resolved_repo = repository_url or _run_git(cwd, ["config", "--get", "remote.origin.url"])
    missing = []
    if not resolved_commit:
        missing.append("git commit hash (--git-commit-hash)")
    if not resolved_branch:
        missing.append("git branch (--git-branch)")
    if not resolved_repo:
        missing.append("git repository url (--git-repository-url)")
    if missing:
        raise ValueError(
            "Missing required git metadata and autodetect failed: " + ", ".join(missing)
        )
    return resolved_commit, resolved_branch, resolved_repo


def _load_template(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for idx, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Template JSONL parse failed on line {idx}: {exc}") from exc
    if len(events) < 14:
        raise ValueError("Template is shorter than expected and does not contain required lines")
    return events


def _build_event_timestamps(base_utc: datetime, count: int, buffer_seconds: int) -> list[str]:
    if count <= 0:
        return []
    if count == 1:
        return [_iso_z(base_utc)]
    buffer_ms = max(1000, buffer_seconds * 1000)
    # Spread timestamps across the buffer while keeping the first one exactly at base_utc.
    step_ms = max(1, buffer_ms // (count + 1))
    out: list[str] = []
    for i in range(count):
        ts = base_utc + timedelta(milliseconds=i * step_ms)
        out.append(_iso_z(ts))
    return out


def _set_common_fields(
    events: list[dict[str, Any]],
    *,
    session_id: str,
    turn_id: str,
    cwd: str,
    shell: str,
    originator: str,
    source: str,
    start_ts_iso: str,
    core_base_instructions: str,
    user_personalization: str,
    tools_descriptions: str,
    application_context: str,
    first_user_message: str,
    first_ai_response: str,
    permissions_set: str,
    git_commit_hash: str,
    git_branch: str,
    git_repository_url: str,
    encrypted_reasoning_content: str,
) -> None:
    environment_context = _build_environment_context(cwd, shell)
    collaboration_mode_inner = _extract_collaboration_mode_inner(events)

    # Line 1: session_meta
    events[0]["payload"]["id"] = session_id
    events[0]["payload"]["timestamp"] = start_ts_iso
    events[0]["payload"]["cwd"] = cwd
    events[0]["payload"]["originator"] = originator
    events[0]["payload"]["source"] = source
    events[0]["payload"]["base_instructions"]["text"] = core_base_instructions
    events[0]["payload"]["git"]["commit_hash"] = git_commit_hash
    events[0]["payload"]["git"]["branch"] = git_branch
    events[0]["payload"]["git"]["repository_url"] = git_repository_url

    # Line 2: permissions block (developer message)
    events[1]["payload"]["content"][0]["text"] = permissions_set

    # Line 3: application context block (template typo placeholder is <enviromental-context>)
    events[2]["payload"]["content"][0]["text"] = application_context

    # Line 4: user personalization
    events[3]["payload"]["content"][0]["text"] = user_personalization

    # Line 5: environment_context
    events[4]["payload"]["content"][0]["text"] = environment_context

    # Line 7: task_started
    events[6]["payload"]["turn_id"] = turn_id

    # Line 8: first user message
    events[7]["payload"]["content"][0]["text"] = first_user_message

    # Line 9: user_message event mirror
    events[8]["payload"]["message"] = (
        first_user_message if first_user_message.endswith("\n") else f"{first_user_message}\n"
    )

    # Line 10: turn_context
    events[9]["payload"]["turn_id"] = turn_id
    events[9]["payload"]["cwd"] = cwd
    events[9]["payload"]["collaboration_mode"]["settings"][
        "developer_instructions"
    ] = collaboration_mode_inner
    events[9]["payload"]["user_instructions"] = tools_descriptions
    events[9]["payload"]["developer_instructions"] = f"{application_context}\n# Code"

    # Line 13: reasoning item encrypted content (only used in full mode)
    if len(events) > 12 and events[12]["type"] == "response_item":
        payload = events[12].get("payload", {})
        if payload.get("type") == "reasoning":
            payload["encrypted_content"] = encrypted_reasoning_content

    # Line 14: agent_message (kept in both modes)
    events[13]["payload"]["message"] = first_ai_response

    # Line 15: assistant visible response (full mode only)
    if len(events) > 14 and events[14]["type"] == "response_item":
        payload = events[14].get("payload", {})
        if payload.get("type") == "message":
            payload["content"][0]["text"] = first_ai_response

    # Line 17: task_complete (full mode only)
    if len(events) > 16 and events[16]["type"] == "event_msg":
        payload = events[16].get("payload", {})
        if payload.get("type") == "task_complete":
            payload["turn_id"] = turn_id
            payload["last_agent_message"] = first_ai_response


def _assign_line_timestamps(events: list[dict[str, Any]], base_utc: datetime, buffer_seconds: int) -> None:
    timestamps = _build_event_timestamps(base_utc, len(events), buffer_seconds)
    for event, ts in zip(events, timestamps):
        event["timestamp"] = ts
    # Keep session_meta.payload.timestamp aligned to first line timestamp.
    if events and events[0].get("type") == "session_meta":
        events[0]["payload"]["timestamp"] = events[0]["timestamp"]


def _strip_reasoning_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for event in events:
        event_type = event.get("type")
        payload = event.get("payload", {})
        payload_type = payload.get("type") if isinstance(payload, dict) else None
        if event_type == "event_msg" and payload_type == "agent_reasoning":
            continue
        if event_type == "response_item" and payload_type == "reasoning":
            continue
        out.append(event)
    return out


def _validate(events: list[dict[str, Any]], expected_session_id: str) -> None:
    if not events:
        raise ValueError("No events generated")
    if events[0].get("type") != "session_meta":
        raise ValueError("First line is not session_meta")
    payload_id = events[0].get("payload", {}).get("id")
    if payload_id != expected_session_id:
        raise ValueError("session_meta.payload.id does not match generated session id")
    previous: datetime | None = None
    for idx, event in enumerate(events, start=1):
        ts = event.get("timestamp")
        if not isinstance(ts, str) or not ts.endswith("Z"):
            raise ValueError(f"Line {idx} timestamp is missing/invalid")
        current = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        if previous is not None and current <= previous:
            raise ValueError(f"Timestamps are not strictly increasing at line {idx}")
        previous = current


def _default_asset(name: str) -> str:
    return (_assets_dir() / name).read_text()


def _starter_templates_dir() -> Path:
    return _assets_dir() / "starter-templates"


def _starter_template_choices() -> list[str]:
    return sorted(STARTER_TEMPLATES.keys())


def _starter_template_manifest() -> list[dict[str, str]]:
    manifest: list[dict[str, str]] = []
    for name in _starter_template_choices():
        spec = STARTER_TEMPLATES[name]
        manifest.append(
            {
                "name": name,
                "description": spec["description"],
                "core_base_instructions_file": str(_starter_templates_dir() / spec["core_base_instructions_file"]),
                "user_personalization_file": str(_starter_templates_dir() / spec["user_personalization_file"]),
                "tools_descriptions_file": str(
                    _starter_templates_dir() / spec["tools_descriptions_and_when_to_use_file"]
                ),
            }
        )
    return manifest


def _apply_starter_template_defaults(args: argparse.Namespace) -> None:
    if not getattr(args, "starter_template", None):
        return
    spec = STARTER_TEMPLATES[args.starter_template]
    base_dir = _starter_templates_dir()
    field_pairs = [
        ("core_base_instructions_text", "core_base_instructions_file"),
        ("user_personalization_text", "user_personalization_file"),
        (
            "tools_descriptions_and_when_to_use_text",
            "tools_descriptions_and_when_to_use_file",
        ),
    ]
    for text_attr, file_attr in field_pairs:
        if getattr(args, text_attr) is not None or getattr(args, file_attr) is not None:
            continue
        rel = spec[file_attr]
        file_path = base_dir / rel
        if not file_path.exists():
            raise ValueError(
                f"Starter template asset missing for {args.starter_template}: {file_path}"
            )
        setattr(args, file_attr, str(file_path))


def _add_text_or_file_args(
    parser: argparse.ArgumentParser,
    *,
    base_name: str,
    help_text: str,
) -> None:
    parser.add_argument(f"--{base_name}-text", help=f"{help_text} (inline text)")
    parser.add_argument(f"--{base_name}-file", help=f"{help_text} (read from file)")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a Codex Desktop session JSONL thread from a template",
    )
    parser.add_argument(
        "--codex-root",
        default="~/.codex",
        help="Codex root directory (default: ~/.codex). Output is written under sessions/YYYY/MM/DD/",
    )
    parser.add_argument(
        "--template-file",
        default=str(_assets_dir() / "rollout-template.jsonl"),
        help="Template JSONL file with placeholders",
    )
    parser.add_argument(
        "--mode",
        choices=["minimum-visible", "full-template"],
        default="full-template",
        help="Output shape to write (default: full-template)",
    )
    parser.add_argument(
        "--starter-template",
        choices=_starter_template_choices(),
        help=(
            "Use bundled starter template assets to auto-fill base instructions, personalization, "
            "and tools descriptions (overrides allowed per field)"
        ),
    )
    parser.add_argument(
        "--list-starter-templates",
        action="store_true",
        help="Print bundled starter template names/descriptions as JSON and exit",
    )
    parser.add_argument(
        "--cwd",
        help="Thread working directory to embed (defaults to current working directory)",
    )
    parser.add_argument("--shell", default="zsh", help="Shell value for <environment_context>")
    parser.add_argument(
        "--originator-descriptor",
        default="Codex Desktop",
        help='Default "Codex Desktop" (required for UI visibility based on observed behavior)',
    )
    parser.add_argument(
        "--source",
        default="vscode",
        help='Default "vscode" (required for UI visibility based on observed behavior)',
    )
    parser.add_argument(
        "--buffer-seconds",
        type=int,
        default=30,
        help="Use current UTC time minus this many seconds as seed; timestamps are spread across this window",
    )
    parser.add_argument("--thread-id", help="Optional override for generated session/thread id")
    parser.add_argument("--turn-id", help="Optional override for generated turn id")
    parser.add_argument("--git-commit-hash", help="Git commit hash to embed (autodetects from --cwd if omitted)")
    parser.add_argument("--git-branch", help="Git branch to embed (autodetects from --cwd if omitted)")
    parser.add_argument(
        "--git-repository-url",
        help="Git remote.origin.url to embed (autodetects from --cwd if omitted)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not write file, only print the computed output path and ids",
    )
    parser.add_argument(
        "--encrypted-reasoning-content",
        default="redacted-generated-placeholder",
        help="Replacement for <encrypted-reasoning-content> when using --mode full-template",
    )

    _add_text_or_file_args(
        parser,
        base_name="core-base-instructions",
        help_text="Base instructions text (<core-base-instructions>)",
    )
    _add_text_or_file_args(
        parser,
        base_name="user-personalization",
        help_text="User personalization text (<user-personalization>)",
    )
    _add_text_or_file_args(
        parser,
        base_name="tools-descriptions-and-when-to-use",
        help_text="Turn context user instructions (<tools-descriptions-and-when-to-use>)",
    )
    _add_text_or_file_args(
        parser,
        base_name="application-context",
        help_text="Application context block (<application-context>)",
    )
    _add_text_or_file_args(
        parser,
        base_name="first-actual-user-message",
        help_text="First user message (<first-actual-user-message>)",
    )
    _add_text_or_file_args(
        parser,
        base_name="first-actual-ai-response",
        help_text="First assistant response (<first-actual-AI-response>)",
    )
    _add_text_or_file_args(
        parser,
        base_name="permissions-set",
        help_text="Permissions block (<permissions-set>)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.list_starter_templates:
        print(json.dumps({"starter_templates": _starter_template_manifest()}, ensure_ascii=False))
        return 0

    try:
        _apply_starter_template_defaults(args)
    except ValueError as exc:
        parser.error(str(exc))
        return 2

    cwd = str(Path(args.cwd).expanduser().resolve()) if args.cwd else str(Path.cwd().resolve())

    try:
        core_base_instructions = _read_text_or_file(
            text=args.core_base_instructions_text,
            file_path=args.core_base_instructions_file,
        )
        user_personalization = _read_text_or_file(
            text=args.user_personalization_text,
            file_path=args.user_personalization_file,
        )
        application_context = _read_text_or_file(
            text=args.application_context_text,
            file_path=args.application_context_file,
            default=_default_asset("default_application_context.txt"),
        )
        first_user_message = _read_text_or_file(
            text=args.first_actual_user_message_text,
            file_path=args.first_actual_user_message_file,
            default="initialize",
            trim_trailing_newlines=True,
        )
        first_ai_response = _read_text_or_file(
            text=args.first_actual_ai_response_text,
            file_path=args.first_actual_ai_response_file,
            default="initialized",
            trim_trailing_newlines=True,
        )
        permissions_set = _read_text_or_file(
            text=args.permissions_set_text,
            file_path=args.permissions_set_file,
            default=_default_asset("default_permissions_set.txt"),
        )
        tools_descriptions = _read_text_or_file(
            text=args.tools_descriptions_and_when_to_use_text,
            file_path=args.tools_descriptions_and_when_to_use_file,
            default=user_personalization,
        )
        git_commit_hash, git_branch, git_repository_url = _resolve_git_values(
            cwd=cwd,
            commit_hash=args.git_commit_hash,
            branch=args.git_branch,
            repository_url=args.git_repository_url,
        )
    except ValueError as exc:
        parser.error(str(exc))
        return 2

    template_events = _load_template(Path(args.template_file).expanduser())
    events = copy.deepcopy(template_events)

    base_utc = (datetime.now(timezone.utc) - timedelta(seconds=args.buffer_seconds)).replace(
        microsecond=0
    )
    session_id = args.thread_id or str(uuid.uuid4())
    turn_id = args.turn_id or str(uuid.uuid4())

    _set_common_fields(
        events,
        session_id=session_id,
        turn_id=turn_id,
        cwd=cwd,
        shell=args.shell,
        originator=args.originator_descriptor,
        source=args.source,
        start_ts_iso=_iso_z(base_utc),
        core_base_instructions=core_base_instructions,
        user_personalization=user_personalization,
        tools_descriptions=tools_descriptions,
        application_context=application_context,
        first_user_message=first_user_message,
        first_ai_response=first_ai_response,
        permissions_set=permissions_set,
        git_commit_hash=git_commit_hash,
        git_branch=git_branch,
        git_repository_url=git_repository_url,
        encrypted_reasoning_content=args.encrypted_reasoning_content,
    )

    if args.mode == "minimum-visible":
        print(
            "warning: minimum-visible mode may leave Codex Desktop showing perpetual thinking for the seeded answer; "
            "prefer full-template for normal use",
            file=sys.stderr,
        )
        events = [events[i] for i in MINIMUM_VISIBLE_TEMPLATE_INDICES]

    # Strip seeded reasoning lines to avoid invalid placeholder encrypted content.
    events = _strip_reasoning_events(events)

    _assign_line_timestamps(events, base_utc, args.buffer_seconds)
    _validate(events, session_id)

    sessions_root = Path(args.codex_root).expanduser() / "sessions"
    ts_for_path = datetime.fromisoformat(events[0]["timestamp"].replace("Z", "+00:00"))
    out_dir = sessions_root / ts_for_path.strftime("%Y") / ts_for_path.strftime("%m") / ts_for_path.strftime("%d")
    filename = f"rollout-{_filename_timestamp(ts_for_path)}-{session_id}.jsonl"
    out_path = out_dir / filename

    result = {
        "mode": args.mode,
        "path": str(out_path),
        "thread_id": session_id,
        "turn_id": turn_id,
        "cwd": cwd,
        "starter_template": args.starter_template,
        "line_count": len(events),
        "first_timestamp": events[0]["timestamp"],
        "dry_run": bool(args.dry_run),
    }

    if args.dry_run:
        print(json.dumps(result, ensure_ascii=False))
        return 0

    out_dir.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        parser.error(f"Refusing to overwrite existing file: {out_path}")
        return 2
    with out_path.open("w", encoding="utf-8") as fh:
        for event in events:
            fh.write(json.dumps(event, ensure_ascii=False, separators=(",", ":")))
            fh.write("\n")

    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
