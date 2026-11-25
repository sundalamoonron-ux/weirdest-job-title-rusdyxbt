#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes a single job title to /output/entry.txt — nothing else.
Gate: UTF-8 text of 1 to 60 characters, not only white space.
"""

import os

TITLE = "Senior Dog Food Taste Tester (Human Division)"

# A real-sounding job (pet-food tasters exist) with one hilariously specific
# twist: the "(Human Division)" punchline. No trailing newline — the file
# must hold exactly the title, byte for byte, and nothing else.
assert 1 <= len(TITLE) <= 60, "title must be 1-60 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
