#!/usr/bin/env python3
"""Invite-letter entry program: publish the letter image.

The finished letter (entry.png, drawn at build time by gen_image.py)
sits next to this file. Running the program places a copy of it at
entry.png inside the directory named by the MAKEFUN_OUTPUT_DIR
environment variable, falling back to /output when that is unset.
The bytes are moved unchanged, so both grading runs produce exactly
the letter that was drawn and checked. Standard library only; nothing
is fetched.
"""

import os
from pathlib import Path

PAGE = Path(__file__).resolve().parent / "entry.png"


def publish() -> Path:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    target.write_bytes(PAGE.read_bytes())
    return target


if __name__ == "__main__":
    print("published", publish())
