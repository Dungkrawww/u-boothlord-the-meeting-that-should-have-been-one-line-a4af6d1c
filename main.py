#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line entry.

One sentence that could have replaced an entire pointless meeting:
the meeting collapses into an email, and the email collapses into
nothing. Office humor, one line, no context needed.
"""

import os
import sys

LINE = "This meeting could have been an email, and honestly, the email could have been nothing."
# Gate: sealed scorer checks /output/entry.txt is UTF-8, 1-200 chars.

MIN_CHARS = 1
MAX_CHARS = 200


def validate(line):
    """Return a list of gate violations; empty means the line passes."""
    problems = []
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        problems.append(
            "length %d is outside %d-%d characters" % (len(line), MIN_CHARS, MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    if line != line.strip():
        problems.append("line must not have leading or trailing whitespace")
    if not line.strip():
        problems.append("line must not be only whitespace")
    return problems


def main():
    problems = validate(LINE)
    if problems:
        for problem in problems:
            print("FAIL: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != LINE:
        print("FAIL: entry.txt on disk does not match the line", file=sys.stderr)
        return 1
    print("OK: %d chars" % len(LINE))
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
