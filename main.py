"""Copy the bundled front-page image to the output directory.

Entry for make.fun news-image-20261118: "Sum up 18 November's world news
in one image". The image (entry.png, 1024x1024 PNG) is a newspaper front
page drawn with PIL from real 18 Nov 2026 headlines; this program only
copies the bundled file to the output path, so both runs write the same
bytes. No network, no randomness, no clocks.
"""

import os
import shutil
import sys
from pathlib import Path

# The grader's -P leaves this file's directory off sys.path; put it back first.
sys.path.insert(0, str(Path(__file__).resolve().parent))

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SOURCE = Path(__file__).resolve().parent / "entry.png"


def main() -> None:
    # Deterministic by construction: a plain byte copy of a fixed file.
    # Both grader runs therefore write identical bytes to entry.png.
    if not SOURCE.is_file():
        raise SystemExit(f"bundled image missing: {SOURCE}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
