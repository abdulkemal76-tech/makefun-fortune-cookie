#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes the single best fortune cookie line for a software engineer to
/output/entry.txt. Standard library only.
"""

from pathlib import Path

# The fortune: a Friday deploy, the engineer's oldest superstition,
# delivered in classic fortune-cookie voice.
FORTUNE = "You will deploy on Friday at 4:59 PM. It will work. Nobody will ever know why."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
