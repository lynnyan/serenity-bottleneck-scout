#!/usr/bin/env python3
"""
Move an existing task's artifacts into a single <company>/<date>/ folder.

This is a one-time helper for older runs created before the folder convention.

It moves:
- report.md (and sibling *_zh.md if present)
- claims.md if present next to report
- judge_runs/<stem>/... and debate_runs/... if present, into report_dir/judge/ and report_dir/debate/
"""

from __future__ import annotations

import argparse
import shutil
from datetime import date
from pathlib import Path
import re


def _slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "misc"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--company", required=True, help="Anchor company name for folder")
    p.add_argument("--date", default="", help="YYYY-MM-DD (default: today)")
    p.add_argument("--report", required=True, help="Path to the existing report markdown")
    return p.parse_args()


def _move(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        raise SystemExit(f"Refusing to overwrite: {dst}")
    shutil.move(str(src), str(dst))


def main() -> int:
    args = parse_args()
    report_path = Path(args.report).expanduser().resolve()
    if not report_path.exists():
        raise SystemExit(f"Report not found: {report_path}")

    skill_dir = Path(__file__).resolve().parents[1]
    day = args.date.strip() or date.today().isoformat()
    task_dir = (skill_dir / "reports" / _slugify(args.company) / day).resolve()
    task_dir.mkdir(parents=True, exist_ok=True)

    # Move report + chinese sibling + claims sibling
    _move(report_path, task_dir / report_path.name)

    zh = report_path.with_name(report_path.stem + "_zh.md")
    if zh.exists():
        _move(zh, task_dir / zh.name)

    claims = report_path.with_name(report_path.stem + "_claims.md")
    if claims.exists():
        _move(claims, task_dir / claims.name)

    # Move legacy judge_runs and debate_runs, if any exist, into task_dir
    legacy_judge = skill_dir / "reports" / "judge_runs"
    if legacy_judge.exists():
        # move any subfolder matching this report stem
        cand = legacy_judge / report_path.stem
        if cand.exists():
            _move(cand, task_dir / "judge" / "legacy" / cand.name)

    legacy_debate = skill_dir / "reports" / "debate_runs"
    if legacy_debate.exists():
        # move any folder that contains the stem
        for child in legacy_debate.iterdir():
            if report_path.stem in child.name and child.is_dir():
                _move(child, task_dir / "debate" / "legacy" / child.name)

    print(task_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

