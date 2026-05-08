"""Command-line entrypoint for the public AuditME package skeleton."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from . import __version__


PUBLIC_ALPHA_COMMANDS = ("init", "resume", "verify", "handoff")


def _exit_code_from_system_exit(error: SystemExit) -> int:
    """Return a stable integer exit code from argparse's SystemExit."""
    code = error.code
    if code is None:
        return 0
    if isinstance(code, int):
        return code
    try:
        return int(code)
    except (TypeError, ValueError):
        return 1


def build_parser() -> argparse.ArgumentParser:
    """Build the public alpha command parser."""
    parser = argparse.ArgumentParser(
        prog="auditme",
        description=(
            "Repo-native memory, guardrails, handoff state, and verification "
            "receipts for AI-assisted development."
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in PUBLIC_ALPHA_COMMANDS:
        subparser = subparsers.add_parser(
            command,
            help=f"Public alpha placeholder for auditme {command}.",
        )
        subparser.add_argument(
            "--project",
            default=".",
            help="Path to the target project. Defaults to the current directory.",
        )
        if command == "handoff":
            subparser.add_argument(
                "--next-move",
                required=False,
                help="Short description of the next safe task.",
            )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the AuditME command-line interface."""
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as error:
        return _exit_code_from_system_exit(error)

    print(
        f"auditme {args.command} is reserved for v0.1.0-alpha behavior "
        "and is not implemented in this package skeleton.",
        file=sys.stderr,
    )
    return 2
