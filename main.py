"""Parrot — one word for the boss.

Writes the single word "parrot" to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR). No network, no randomness, no input.
Deterministic: every run writes byte-identical output.

Why this word: a boss who hears your idea, then repeats it in the
meeting five minutes later as his own. A parrot repeats what it
hears — the word alone IS the habit. Instantly legible, no caption
needed, the kind of word a colleague repeats at lunch. Universal,
travels to any workplace, and fresh in a field full of Hovercrafts,
Seagulls, Helicopters and meeting-* compounds.
"""

import os
from pathlib import Path

TEXT = "parrot"


def main() -> None:
    # Gate self-check (revision edit, turn 1): the entry must be exactly
    # one word, 1-30 chars, no whitespace — the same gate the sealed
    # scorer applies. Fail loudly here rather than shipping an invalid entry.
    assert TEXT and 1 <= len(TEXT) <= 30, "entry must be 1-30 characters"
    assert TEXT.split() == [TEXT], "entry must be exactly one word"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
