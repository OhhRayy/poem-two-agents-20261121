#!/usr/bin/env python3
"""Write the poem to /output/entry.txt. No network."""

import os

POEM = """Two keys, two locks, one door.
I could pocket my key and walk away.
You could pocket yours and walk away.

Instead we turn them together —
one motion, one sound —
and the door swings wide
on hinges we both own."""

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
