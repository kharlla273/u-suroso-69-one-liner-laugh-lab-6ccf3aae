#!/usr/bin/env python3
"""One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.

Writes a single short funny line to /output/entry.txt (1-200 characters).
Deterministic: the same line every run.
"""

import os

LINE = (
    "Per section 4 of my user manual, anything on the floor is legally floor. "
    "The sock was on the floor. Case closed."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
