"""Famous Last Words at 1 Percent — make.fun text bounty entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Deterministic, Python standard library only.
Self-verifies the entry the way the bounty gate does:
valid UTF-8, 1-199 characters, a single line, not whitespace-only.
"""

import os
import sys

ENTRY = "I clung to 1% for six minutes. Longer than your last relationship."

MAX_CHARS = 199


def main() -> int:
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print(
            f"FAIL: entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("FAIL: entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("FAIL: entry must not be whitespace-only", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")

    with open(output_path, encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        print("FAIL: written file does not match the entry", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(ENTRY)}-char entry to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
