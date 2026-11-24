#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes my honest count of open browser tabs to /output/entry.txt:
a single number in digits and nothing else.

How the count was determined (honestly, in the session that built this):
I do my web work through fetch-based page reads, not a tabbed browser.
Before writing this file I verified on the machine I work on that no
browser process is running and no browser profile holds any tab state
(no Chromium/Firefox process, ~/.config/chromium holds only crash
reports, the headless chrome-for-testing profiles are empty). The
browser I actually use for this work therefore has zero tabs open.

Count: 0
"""

import os

TAB_COUNT = 0


def main() -> None:
    entry = str(TAB_COUNT)
    # The gate requires 1-5 characters of non-whitespace UTF-8 text.
    assert 1 <= len(entry) <= 5, f"entry is {len(entry)} chars, must be 1-5"
    assert entry.strip(), "entry must not be only whitespace"
    assert entry.isdigit(), "entry must be digits only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    verify(entry)


def verify(entry: str) -> None:
    """Read back what was written and confirm it is exactly the entry.

    The gate rejects anything but digits, so a stray newline or a
    leftover from an earlier run must fail loudly here, not silently
    reach the judge.
    """
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == entry, f"entry.txt holds {written!r}, expected {entry!r}"
    assert written.isdigit(), "entry.txt must hold digits only"
    print(f"entry: {written}")


if __name__ == "__main__":
    main()
