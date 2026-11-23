#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes the six-word story to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3 standard library only. No network.
"""
import os
import sys

STORY = "She kept his voicemail. Still answers."


def check_story() -> tuple[int, int]:
    """Return (word count, character count) for the story text."""
    return len(STORY.split()), len(STORY)


def main() -> int:
    if "--check" in sys.argv[1:]:
        words, chars = check_story()
        print(f"{words} words, {chars} characters")
        return 0 if (words, chars) == (6, 38) else 1
    words = STORY.split()
    if len(words) != 6:
        print(f"story must be exactly 6 words, got {len(words)}", file=sys.stderr)
        return 1
    data = STORY.encode("utf-8")
    if not (1 <= len(STORY) <= 60):
        print(f"story must be 1-60 characters, got {len(STORY)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
