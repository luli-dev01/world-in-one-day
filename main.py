# Entry for the make.fun "Sum up 18 November's world news in one image"
# contest (news-image-20261118): the picture is the entry.png beside this
# file — a one-page newspaper of Wednesday 18 November 2026, drawn by
# gen_image.py — and this program copies it to the output directory.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if not src.exists():
        src = Path("/bot/entry.png")
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out / "entry.png")


if __name__ == "__main__":
    main()
