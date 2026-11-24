#!/usr/bin/env python3
"""The One-Line Exit: write one funny one-line resignation letter.

The letter is a single fixed string, written verbatim to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). It is 101
characters: a real, sendable resignation line whose joke lands on the
last three words, reframing the notice period itself as the company's
only project ever finished on time.
"""

import os

LETTER = (
    "I hereby resign \u2014 my two weeks' notice is the longest project "
    "this company has ever finished on time."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    print(f"wrote {len(LETTER)} characters to {path}")


if __name__ == "__main__":
    main()
