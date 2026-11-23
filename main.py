#!/usr/bin/env python3
"""One Line, Best Line — make.fun entry.

Writes exactly one line of text to /output/entry.txt.
Pure standard library, no network, fully deterministic.
"""

import os

LINE = (
    "I bought a cactus because I heard they thrive on neglect, "
    "and honestly, it's the healthiest relationship I've ever had."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
