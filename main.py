"""Make the Judge Laugh in One Line.

Writes a single original one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt). Stdlib only, deterministic: the same
bytes on every run.
"""

import os

LINE = (
    "I asked my smart speaker to play something relaxing, so it read "
    "my bank statement aloud in a spa voice."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
