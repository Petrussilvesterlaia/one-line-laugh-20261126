#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original joke line to /output/entry.txt, then reads it
back and validates the competition gate: exactly one line, 1-140
characters, not only whitespace. Exits non-zero on any failure.
"""

import sys
from pathlib import Path

LINE = "I tried to teach my dog fetch, but he unionized the squirrels instead."

OUTPUT = Path("/output/entry.txt")


def main() -> int:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly one line, nothing else.
    OUTPUT.write_text(LINE, encoding="utf-8")

    text = OUTPUT.read_text(encoding="utf-8")
    if "\n" in text or "\r" in text:
        print("FAIL: entry is not a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 140:
        print(f"FAIL: entry length {len(text)} is outside 1-140", file=sys.stderr)
        return 1
    if not text.strip():
        print("FAIL: entry is only whitespace", file=sys.stderr)
        return 1
    print(text)
    print(f"characters: {len(text)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
