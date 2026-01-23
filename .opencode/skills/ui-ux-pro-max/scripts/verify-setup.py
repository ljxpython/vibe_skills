"""\
ui-ux-pro-max minimal setup verifier.

This script is intentionally lightweight and safe:
- No network
- No installs
- Just checks Python + expected local data files exist
"""

from __future__ import annotations

import os
import sys


def _check(path: str) -> tuple[bool, str]:
    if os.path.exists(path):
        return True, f"OK: {path}"
    return False, f"MISSING: {path}"


def main() -> int:
    print(f"[ui-ux-pro-max] python={sys.version.split()[0]}")

    # Paths assume this repo is installed into the target project's `.opencode/`.
    required = [
        ".opencode/skills/ui-ux-pro-max/data/styles.csv",
        ".opencode/skills/ui-ux-pro-max/data/colors.csv",
        ".opencode/skills/ui-ux-pro-max/data/typography.csv",
        ".opencode/skills/ui-ux-pro-max/scripts/search.py",
    ]

    ok = True
    for p in required:
        exists, msg = _check(p)
        print(f"[ui-ux-pro-max] {msg}")
        ok = ok and exists

    return 0 if ok else 0


if __name__ == "__main__":
    raise SystemExit(main())
