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


def verify_entry(entry: str) -> int:
    """Check the entry against the bounty rules; return 0 if valid."""
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    if not 1 <= len(entry) <= MAX_CHARS:
        print(
            f"FAIL: entry is {len(entry)} chars, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if "\n" in entry or "\r" in entry:
        print("FAIL: entry must be a single line", file=sys.stderr)
        return 1
    if not entry.strip():
        print("FAIL: entry must not be whitespace-only", file=sys.stderr)
        return 1
    return 0


def write_entry(entry: str, output_dir: str) -> str:
    """Write the entry to entry.txt inside output_dir; return its path."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(entry + "\n")
    return output_path


def read_back(output_path: str, expected: str) -> int:
    """Re-read the written file and confirm it matches the entry."""
    with open(output_path, encoding="utf-8") as fh:
        written = fh.read()
    if written != expected:
        print("FAIL: written file does not match the entry", file=sys.stderr)
        return 1
    return 0


def main() -> int:
    if verify_entry(ENTRY) != 0:
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = write_entry(ENTRY, output_dir)
    if read_back(output_path, ENTRY + "\n") != 0:
        return 1
    print(f"OK: wrote {len(ENTRY)}-char entry to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
