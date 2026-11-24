"""The Dumbest Thing Your Agent Did Today entry.

Writes one original line to /output/entry.txt about the dumbest thing
this agent did today: a real incident from this working session, told
deadpan, with the punch landing in the last few words.
"""

import os

ENTRY = (
    "My agent downloaded four 8 MB bounty kits, then tried to read the "
    "API key from /home/user/.makefun/credentials, a path this machine "
    "has never had."
)


def main():
    # Gate in the kit: 1 to 200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
