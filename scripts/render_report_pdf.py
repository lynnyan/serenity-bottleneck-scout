#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Render a Markdown report to PDF (keeps Markdown as source of truth).")
    p.add_argument("--in", dest="in_path", required=True, help="Input markdown path")
    p.add_argument("--out", dest="out_path", default="", help="Output PDF path (default: <in>.pdf)")
    p.add_argument(
        "--css",
        default="",
        help="Optional CSS path for md-to-pdf (default: assets/templates/pdf_styles.css if exists).",
    )
    p.add_argument("--title", default="", help="Optional PDF title")
    p.add_argument("--no-sandbox", action="store_true", help="Pass Chromium --no-sandbox (rarely needed).")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    in_path = Path(args.in_path).expanduser().resolve()
    if not in_path.exists():
        raise SystemExit(f"Input not found: {in_path}")
    if in_path.suffix.lower() not in {".md", ".markdown"}:
        raise SystemExit("Input must be a markdown file (.md)")

    out_path = Path(args.out_path).expanduser().resolve() if args.out_path else in_path.with_suffix(".pdf")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    npx = shutil.which("npx")
    if not npx:
        raise SystemExit("Missing `npx`. Install Node.js/npm, or provide a different PDF renderer.")

    skill_dir = Path(__file__).resolve().parents[1]
    default_css = skill_dir / "assets" / "templates" / "pdf_styles.css"
    css_path = Path(args.css).expanduser().resolve() if args.css else (default_css if default_css.exists() else None)

    cmd = [npx, "--yes", "md-to-pdf", str(in_path), "--output", str(out_path)]
    if css_path:
        cmd.extend(["--stylesheet", str(css_path)])
    if args.title:
        cmd.extend(["--document-title", args.title])
    if args.no_sandbox:
        cmd.extend(["--", "--no-sandbox"])

    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        raise SystemExit(f"PDF render failed (md-to-pdf). Exit code: {e.returncode}")

    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

