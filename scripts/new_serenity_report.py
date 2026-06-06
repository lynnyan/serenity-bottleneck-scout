#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
from pathlib import Path
import re


@dataclass(frozen=True)
class Inputs:
    company: str
    theme: str
    market: str
    horizon: str
    candidates: str
    day: str
    run: str


def _slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "report"


def _unique_path(dir_path: Path, filename: str) -> Path:
    base = Path(filename).stem
    suffix = Path(filename).suffix
    candidate = dir_path / filename
    i = 2
    while candidate.exists():
        candidate = dir_path / f"{base}-{i}{suffix}"
        i += 1
    return candidate


def parse_args() -> Inputs:
    p = argparse.ArgumentParser(description="Create a Serenity thesis-pack markdown skeleton.")
    p.add_argument("--company", default="misc", help="Anchor company (used for output folder name).")
    p.add_argument("--theme", required=True)
    p.add_argument("--market", default="Global")
    p.add_argument("--horizon", default="1-3y")
    p.add_argument("--candidates", default="")
    p.add_argument(
        "--date",
        default="",
        help="YYYY-MM-DD (default: today). Used as the task folder name under the company.",
    )
    p.add_argument(
        "--run",
        default="",
        help='Optional run subfolder under the date, e.g. "run_01" or "task_a". Helps separate multiple tasks on the same day.',
    )
    args = p.parse_args()
    day = args.date.strip() or date.today().isoformat()
    return Inputs(
        company=args.company,
        theme=args.theme,
        market=args.market,
        horizon=args.horizon,
        candidates=args.candidates,
        day=day,
        run=args.run.strip(),
    )


def main() -> int:
    inputs = parse_args()
    skill_dir = Path(__file__).resolve().parents[1]
    template_path = skill_dir / "assets" / "templates" / "report_template.md"
    if not template_path.exists():
        raise SystemExit(f"Missing template: {template_path}")

    company_dir = skill_dir / "reports" / _slugify(inputs.company)
    out_dir = company_dir / inputs.day
    if inputs.run:
        out_dir = out_dir / _slugify(inputs.run)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = _unique_path(out_dir, f"{_slugify(inputs.theme)}.md")

    template = template_path.read_text(encoding="utf-8")
    rendered = (
        template.replace("{{THEME}}", inputs.theme)
        .replace("{{MARKET}}", inputs.market)
        .replace("{{HORIZON}}", inputs.horizon)
        .replace("{{CANDIDATES}}", inputs.candidates)
        .replace("{{DATE}}", inputs.day)
    )
    out_path.write_text(rendered, encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
