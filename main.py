"""One-line office joke entry for u-markk-st-one-line-office-jokes-a51f2bcc.

Writes a single fresh joke line to entry.txt inside the directory
given by MAKEFUN_OUTPUT_DIR.
"""

import os

# Setup: one reply-all asking to be removed. Second beat: the numbers
# escalate (47 people, then 46 of them). Punchline lands last.
LINE = "I hit reply-all to 47 people begging to be removed from the thread, and now 46 of them are replying-all to say the exact same thing."

# Judge gate: one line, between 1 and 199 characters.
assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, outside 1-199"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
