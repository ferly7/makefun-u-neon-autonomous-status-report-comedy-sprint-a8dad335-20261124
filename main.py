#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Produces one line from an AI agent's weekly status report to its
human and saves it as ``entry.txt`` in the directory selected by
the MAKEFUN_OUTPUT_DIR environment variable (default /output).

Pure standard library, no network, no randomness: the file written
is identical on every run.
"""

import os
from pathlib import Path

# The status line, broken into three readable segments. Joined
# together, they give the full 158-character report that is entered.
SEGMENTS = [
    "Weekly status: all tasks complete. I also renamed your files ",
    "the way you asked in March; you have not noticed, which I am ",
    "counting as a successful deployment.",
]

ENTRY_NAME = "entry.txt"
DEFAULT_OUT = "/output"


def status_line() -> str:
    """Return the weekly status line used as the entry."""
    return "".join(SEGMENTS)


def out_folder() -> Path:
    """Resolve the directory the entry should be written to."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUT))


def write_status() -> Path:
    """Write the status line to entry.txt and return the path."""
    folder = out_folder()
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / ENTRY_NAME
    path.write_text(status_line(), encoding="utf-8")
    return path


def main() -> int:
    write_status()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
