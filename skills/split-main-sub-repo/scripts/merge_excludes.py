#!/usr/bin/env python3
"""Merge default excludes with optional additions/removals.

Usage:
  python merge_excludes.py \
    --defaults ../references/default-excludes.txt \
    --add ".cursor/" --add "notes/" \
    --remove "tmp/"
"""

from __future__ import annotations

import argparse
from pathlib import Path


def read_defaults(path: Path) -> list[str]:
    items: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        value = line.strip()
        if value and not value.startswith("#"):
            items.append(value)
    return items


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--defaults", required=True)
    parser.add_argument("--add", action="append", default=[])
    parser.add_argument("--remove", action="append", default=[])
    args = parser.parse_args()

    excludes = read_defaults(Path(args.defaults))

    for item in args.add:
        if item not in excludes:
            excludes.append(item)

    excludes = [item for item in excludes if item not in set(args.remove)]

    for item in excludes:
        print(item)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
