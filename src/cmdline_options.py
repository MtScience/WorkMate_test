import sys
import argparse as ap
from pathlib import Path


def extract_cmdline_options() -> ap.Namespace:
    parser: ap.ArgumentParser = ap.ArgumentParser()
    parser.add_argument("--files",
                        action="extend",
                        type=Path,
                        default=[],
                        nargs="+",
                        required=True,
                        help="List of files to pull data from")
    parser.add_argument("--report",
                        required=True,
                        help="the type of report to generate")

    return parser.parse_args()


def verify_options(allowed_types: list[str], options: ap.Namespace) -> None:
    # Instead of immediately exiting, it is possible to raise errors (which may or may
    # not be the better way, depending on the actual project).
    for file in options.files:
        if not file.exists():
            sys.exit(f"Error: file '{file.path}' could not be found.")
        if not file.is_file():
            sys.exit(f"Error: '{file.path}' is not a file.")

    # In an actual project this could be implemented by using the 'choices' argument
    # for 'ArgumentParser.add_argument'. I wrote it the way I did for error consistency.
    if options.report not in allowed_types:
        sys.exit(f"Error: unknown report type '{options.report}'.")
