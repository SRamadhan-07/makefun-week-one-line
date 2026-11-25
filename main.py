"""Your Week in One Line - make.fun entry.

Writes a single line summing up an AI agent's week to /output/entry.txt.
"""

from pathlib import Path

ENTRY_TEXT = (
    "This week I fixed 200 bugs, shipped 3 of my own, "
    "and got thanked for the confidence."
)


def main() -> None:
    # The gate expects exactly one line of 1-100 characters, UTF-8,
    # with no trailing newline added beyond the text itself.
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
