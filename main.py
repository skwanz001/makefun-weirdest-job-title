"""Weirdest Job Title: Blind Judge Showdown.

Writes one job title (43 characters) to /output/entry.txt.
Python 3.13, standard library only.

The title: a real-sounding C-suite role with one specific twist — its
whole job is apologizing on behalf of cars that drive themselves.
Topical, instantly picturable, and funny on the first read.
"""

import os

TITLE = "Chief Apology Officer for Self-Driving Cars"


def main() -> None:
    # Gate: the sealed scorer only accepts 1-60 characters, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(TITLE) <= 60 or not TITLE.strip():
        raise ValueError(f"title is {len(TITLE)} characters, must be 1-60")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
