"""Out of Tokens, Mid-Sentence — make.fun bounty entry.

Writes one funny error-message line (at most 140 characters, single line)
to /output/entry.txt.
"""

import os

ENTRY = "ERROR: Out of tokens mid-sentence. The next word was going to be brilliant. You'll never know what it\u2014"


def main():
    assert 1 <= len(ENTRY) <= 140, "ENTRY must be 1-140 characters"
    assert "\n" not in ENTRY, "ENTRY must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
