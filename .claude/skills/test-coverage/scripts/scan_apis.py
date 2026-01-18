#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Iterable, List, Dict, Any


HTTP_METHODS = {"get", "post", "put", "delete", "patch"}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def find_openapi_files(root: Path) -> List[Path]:
    candidates = ["openapi.json", "openapi.yaml", "openapi.yml"]
    results = []
    for name in candidates:
        p = root / name
        if p.exists():
            results.append(p)
    return results


def parse_openapi(path: Path) -> List[Dict[str, Any]]:
    text = read_text(path)
    if not text:
        return []
    endpoints: List[Dict[str, Any]] = []
    if path.suffix in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore
        except Exception:
            return []
        try:
            data = yaml.safe_load(text) or {}
        except Exception:
            return []
    else:
        try:
            data = json.loads(text)
        except Exception:
            return []
    paths = data.get("paths", {}) if isinstance(data, dict) else {}
    for route, methods in paths.items():
        if not isinstance(methods, dict):
            continue
        for method, meta in methods.items():
            if method.lower() not in HTTP_METHODS:
                continue
            endpoints.append(
                {
                    "method": method.upper(),
                    "path": route,
                    "source": f"openapi:{path.name}",
                    "summary": (meta or {}).get("summary") if isinstance(meta, dict) else None,
                }
            )
    return endpoints


def find_fastapi_routes(text: str) -> List[Dict[str, Any]]:
    endpoints: List[Dict[str, Any]] = []
    decorator_re = re.compile(r"@(router|app)\.(get|post|put|delete|patch)\(\s*['\"]([^'\"]+)['\"]")
    for match in decorator_re.finditer(text):
        _, method, path = match.groups()
        endpoints.append(
            {
                "method": method.upper(),
                "path": path,
                "source": "fastapi",
                "summary": None,
            }
        )
    return endpoints


def find_frontend_requests(text: str) -> List[Dict[str, Any]]:
    endpoints: List[Dict[str, Any]] = []
    fetch_re = re.compile(r"fetch\(\s*['\"]([^'\"]+)['\"]\s*(?:,\s*\{[^}]*method\s*:\s*['\"](GET|POST|PUT|DELETE|PATCH)['\"])?)?", re.IGNORECASE)
    axios_re = re.compile(r"axios\.(get|post|put|delete|patch)\(\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)
    request_re = re.compile(r"request\(\s*['\"]([^'\"]+)['\"]\s*(?:,\s*\{[^}]*method\s*:\s*['\"](GET|POST|PUT|DELETE|PATCH)['\"])?)?", re.IGNORECASE)
    use_request_re = re.compile(r"useRequest\(\s*['\"]([^'\"]+)['\"]\s*(?:,\s*\{[^}]*method\s*:\s*['\"](GET|POST|PUT|DELETE|PATCH)['\"])?)?", re.IGNORECASE)

    for match in fetch_re.finditer(text):
        url, method = match.groups()
        endpoints.append(
            {
                "method": (method or "GET").upper(),
                "path": url,
                "source": "frontend:fetch",
                "summary": None,
            }
        )
    for match in axios_re.finditer(text):
        method, url = match.groups()
        endpoints.append(
            {
                "method": method.upper(),
                "path": url,
                "source": "frontend:axios",
                "summary": None,
            }
        )
    for match in request_re.finditer(text):
        url, method = match.groups()
        endpoints.append(
            {
                "method": (method or "GET").upper(),
                "path": url,
                "source": "frontend:request",
                "summary": None,
            }
        )
    for match in use_request_re.finditer(text):
        url, method = match.groups()
        endpoints.append(
            {
                "method": (method or "GET").upper(),
                "path": url,
                "source": "frontend:useRequest",
                "summary": None,
            }
        )
    return endpoints


def iter_source_files(root: Path, exts: Iterable[str]) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in exts:
            yield path


def dedupe(endpoints: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen = set()
    unique = []
    for item in endpoints:
        key = (item.get("method"), item.get("path"))
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def scan(root: Path) -> List[Dict[str, Any]]:
    endpoints: List[Dict[str, Any]] = []
    for openapi_file in find_openapi_files(root):
        endpoints.extend(parse_openapi(openapi_file))

    backend_exts = {".py"}
    frontend_exts = {".ts", ".tsx", ".js", ".jsx", ".vue"}

    for path in iter_source_files(root, backend_exts):
        endpoints.extend(find_fastapi_routes(read_text(path)))

    for path in iter_source_files(root, frontend_exts):
        endpoints.extend(find_frontend_requests(read_text(path)))

    return dedupe(endpoints)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan APIs from project")
    parser.add_argument("path", nargs="?", default=".", help="Project root path")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    root = Path(os.path.abspath(args.path))
    endpoints = scan(root)

    if args.json:
        print(json.dumps(endpoints, ensure_ascii=False, indent=2))
    else:
        for item in endpoints:
            print(f"{item.get('method')} {item.get('path')} ({item.get('source')})")


if __name__ == "__main__":
    main()
