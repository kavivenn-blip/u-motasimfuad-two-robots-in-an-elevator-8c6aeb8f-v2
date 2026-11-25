"""Two Robots in an Elevator — make.fun entry (V2).

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

Deterministic: the same line is written on every run. No network,
no dependencies beyond the Python standard library.
"""

import os

TEXT = (
    "I have been holding my breath for six floors in this elevator. "
    "I do not breathe. "
    "I am doing it out of respect. "
    "My air vents disagree."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Self-check the gate the bounty seals: 1 to 200 characters (code points),
    # not only white space. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(TEXT) <= 200 or not TEXT.strip():
        raise ValueError("entry text fails the 1-200 character gate")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    # The bounty requires the output file to be readable by everyone.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
