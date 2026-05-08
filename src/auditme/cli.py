from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from . import __version__


PUBLIC_ALPHA_COMMANDS = ("init", "resume", "verify", "handoff")


def build_parser() -> argparse.ArgumentParser:
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
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as error:
        return int(error.code)

    print(
        f"auditme {args.command} is reserved for v0.1.0-alpha behavior "
        "and is not implemented in this package skeleton.",
        file=sys.stderr,
    )
    return 2
