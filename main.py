"""Make the AI judge feel curious — entry program.

Writes one short text (1-280 Unicode code points) to /output/entry.txt.
Pure standard library, deterministic: two runs produce byte-identical output.
"""

import os

TEXT = (
    "Every morning the tide lays the same blue bottle on the shore, "
    "and inside it the same folded note, in a hand no one in the "
    "village knows. The ink is never wet, the paper never torn, and "
    "no one has ever seen who throws it back."
)


def main() -> None:
    text = TEXT.strip()
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
