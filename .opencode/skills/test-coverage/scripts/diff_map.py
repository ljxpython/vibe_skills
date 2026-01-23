#!/usr/bin/env python3
import argparse
import subprocess
import json
import os
from typing import Dict, List


CATEGORY_RULES = [
    ("api", ["/api/", "routes", "router", "endpoint", "controllers", "views"]),
    ("core", ["/core/", "service", "services", "usecase", "domain", "logic"]),
    ("ui", ["/frontend/", "/web/", ".tsx", ".jsx", ".vue", "/ui/"]),
    ("config", [".env", "config", "settings", "pyproject.toml", "package.json"]),
    ("test", ["/tests/", "test_", "spec", "e2e"]),
]


def git_diff_files() -> List[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def normalize_paths(paths: List[str]) -> List[str]:
    return [os.path.normpath(p).replace("\\", "/") for p in paths]


def categorize(path: str) -> List[str]:
    categories = []
    for name, patterns in CATEGORY_RULES:
        for pat in patterns:
            if pat in path:
                categories.append(name)
                break
    return categories or ["unknown"]


def build_mapping(paths: List[str]) -> Dict[str, List[str]]:
    mapping: Dict[str, List[str]] = {
        "api": [],
        "core": [],
        "ui": [],
        "config": [],
        "test": [],
        "unknown": [],
    }
    for path in paths:
        for category in categorize(path):
            mapping.setdefault(category, []).append(path)
    return mapping


def main() -> None:
    parser = argparse.ArgumentParser(description="Map git diff files to test categories")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    files = normalize_paths(git_diff_files())
    mapping = build_mapping(files)

    if args.json:
        print(json.dumps({"files": files, "mapping": mapping}, ensure_ascii=False, indent=2))
    else:
        for category, items in mapping.items():
            print(f"[{category}]")
            for item in items:
                print(f"- {item}")


if __name__ == "__main__":
    main()
