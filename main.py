#!/usr/bin/env python3
"""Entry point for news-image-20261118.

Copies the bundled entry.png (a one-page newspaper of 2026-11-18,
drawn by gen_image.py) to the output directory. Standard library
only, no network, deterministic: the same bytes every run.
Output dir: $MAKEFUN_OUTPUT_DIR if set, else /output.
"""
import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
