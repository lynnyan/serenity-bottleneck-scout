#!/usr/bin/env python3
from __future__ import annotations

"""
Preflight checks / lightweight auto-fixes for Serenity reports before PDF rendering.

Goals:
- Prevent common md-to-pdf rendering failures (especially broken tables).
- Keep reports shareable: avoid local-only reference paths in public-facing sections.

This script is intentionally conservative:
- It only auto-fixes Markdown table separator rows ("|---|---|") when they have the wrong column count.
- Everything else is reported as a warning (exit code 0) unless --strict is passed.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Result:
    changed: bool
    warnings: list[str]


_TABLE_SEP_RE = re.compile(r"^\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*$")


def _count_table_columns(line: str) -> int:
    # Count cells by '|' separators, ignoring leading/trailing pipes.
    s = line.strip()
    if not s.startswith("|"):
        return 0
    # Split and drop first/last (empty due to leading/trailing |)
    parts = [p.strip() for p in s.split("|")]
    if len(parts) < 3:
        return 0
    return len(parts) - 2


def _build_sep_row(num_cols: int) -> str:
    return "|" + "|".join(["---"] * num_cols) + "|"


def fix_table_separators(lines: list[str]) -> tuple[list[str], bool]:
    changed = False
    out = list(lines)
    for i in range(1, len(out)):
        if not _TABLE_SEP_RE.match(out[i]):
            continue
        header = out[i - 1]
        header_cols = _count_table_columns(header)
        if header_cols <= 0:
            continue
        sep_cols = _count_table_columns(out[i])
        if sep_cols != header_cols:
            out[i] = _build_sep_row(header_cols)
            changed = True
    return out, changed


def scan_shareability_warnings(text: str) -> list[str]:
    warnings: list[str] = []
    # Only warn on actual local-path usage patterns, not explanatory prose.
    if re.search(r"\bLocal snapshot:\b", text):
        warnings.append("Found 'Local snapshot' in report; consider removing for shareable/public version.")
    # Warn when 'sources/<something>' appears as a path (not just mentioned as `sources/`).
    if re.search(r"(^|[^\w`])sources/[A-Za-z0-9_.-]", text):
        warnings.append("Found 'sources/' paths in report; consider removing for shareable/public version.")
    if re.search(r"/Users/|[A-Z]:\\\\", text):
        warnings.append("Found absolute local filesystem paths; consider removing for shareable/public version.")
    return warnings


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Preflight Serenity markdown report before PDF rendering.")
    p.add_argument("--in", dest="in_path", required=True, help="Input markdown path")
    p.add_argument("--strict", action="store_true", help="Fail (exit 1) on warnings.")
    return p.parse_args()


def run(in_path: Path) -> Result:
    text = in_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()

    lines2, changed = fix_table_separators(lines)
    if changed:
        in_path.write_text("\n".join(lines2) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")
        text = in_path.read_text(encoding="utf-8", errors="ignore")

    warnings = scan_shareability_warnings(text)
    return Result(changed=changed, warnings=warnings)


def main() -> int:
    args = parse_args()
    in_path = Path(args.in_path).expanduser().resolve()
    if not in_path.exists():
        print(f"Input not found: {in_path}", file=sys.stderr)
        return 2
    if in_path.suffix.lower() not in {".md", ".markdown"}:
        print("Input must be a markdown file (.md)", file=sys.stderr)
        return 2

    res = run(in_path)
    for w in res.warnings:
        print(f"[md_preflight] WARN: {w}", file=sys.stderr)

    if args.strict and res.warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
