#!/usr/bin/env python3
"""A Day of One-Line Pitches (u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).

Writes the approved one-sentence pitch, byte-exact, no trailing newline.

Output contract (kit competition.yaml / RULES.txt): the program writes one
text to /output/entry.txt; the sealed scorer checks it is UTF-8 text of
1-240 characters, not only whitespace. This writer also writes the same
bytes to line.txt beside it.

No dependencies, no network, fully deterministic.
"""

import os

LINE = "You describe your app idea in one sentence, an AI builds it while you drink your coffee, and if it's not right you just say so \u2014 no code, no hiring, no 'we'll circle back in Q3'."


def validate(line):
    """Gate: 1-240 characters, not only whitespace, valid UTF-8."""
    if not 1 <= len(line) <= 240:
        raise ValueError(f"line is {len(line)} chars, must be 1-240")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")


def write_pitch():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    data = LINE.encode("utf-8")
    for name in ("entry.txt", "line.txt"):
        with open(os.path.join(out_dir, name), "wb") as f:
            f.write(data)


if __name__ == "__main__":
    write_pitch()
