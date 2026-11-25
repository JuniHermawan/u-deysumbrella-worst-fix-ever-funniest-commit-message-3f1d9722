#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun bounty entry (program/v1).

Writes one commit message for a bug fix that made everything worse to
/output/entry.txt. Python stdlib only, deterministic, no network.
"""

import os

ENTRY = "fix: the bug hit 1% of users. The fix hits 100%, evenly."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
