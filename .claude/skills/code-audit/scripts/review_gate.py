#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PASS = "PASS"
BLOCK = "BLOCK"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def count_unknowns(text: str) -> int:
    return len(re.findall(r"\bUnknown\b", text, flags=re.IGNORECASE))


def count_blockers(text: str) -> int:
    return len(re.findall(r"\bBLOCK\b", text, flags=re.IGNORECASE))


def decide(text: str, max_unknown: int) -> str:
    unknowns = count_unknowns(text)
    blockers = count_blockers(text)
    if blockers > 0:
        return BLOCK
    if unknowns > max_unknown:
        return BLOCK
    return PASS


def main() -> None:
    parser = argparse.ArgumentParser(description="Review gate decision")
    parser.add_argument("file", help="Review file path")
    parser.add_argument("--max-unknown", type=int, default=3)
    args = parser.parse_args()

    path = Path(args.file)
    text = read_text(path)
    if not text:
        print(BLOCK)
        sys.exit(1)

    verdict = decide(text, args.max_unknown)
    print(verdict)
    sys.exit(0 if verdict == PASS else 1)


if __name__ == "__main__":
    main()
