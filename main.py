"""One Line, One Laugh -- make.fun entry (program/v1).

Writes a single funny line (<=200 chars) to /output/entry.txt.
Pure standard library only.
"""

import os

LINE = (
    "A museum guard followed me for an hour, then apologised: "
    "I'd been standing in the exhibit the whole time \u2014 "
    "I'm now catalogued as 'Man Checking His Phone, 2026.'"
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert line.strip() == line and line, "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    print(f"({len(line)} characters)")


if __name__ == "__main__":
    main()
