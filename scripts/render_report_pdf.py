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
    p.add_argument("--strict", action="store_true", help="Fail on markdown preflight warnings.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    in_path = Path(args.in_path).expanduser().resolve()
    if not in_path.exists():
        raise SystemExit(f"Input not found: {in_path}")
    if in_path.suffix.lower() not in {".md", ".markdown"}:
        raise SystemExit("Input must be a markdown file (.md)")

    # Preflight: fix common markdown issues that break PDF rendering (esp. tables).
    # Also warns on local-only reference paths for shareability.
    skill_dir = Path(__file__).resolve().parents[1]
    preflight_script = skill_dir / "scripts" / "md_preflight.py"
    if preflight_script.exists():
        preflight_cmd = [sys.executable, str(preflight_script), "--in", str(in_path)]
        if args.strict:
            preflight_cmd.append("--strict")
        try:
            subprocess.check_call(preflight_cmd)
        except subprocess.CalledProcessError as e:
            raise SystemExit(f"Markdown preflight failed. Exit code: {e.returncode}")

    out_path = Path(args.out_path).expanduser().resolve() if args.out_path else in_path.with_suffix(".pdf")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    npx = shutil.which("npx")
    if not npx:
        raise SystemExit("Missing `npx`. Install Node.js/npm, or provide a different PDF renderer.")

    default_css = skill_dir / "assets" / "templates" / "pdf_styles.css"
    css_path = Path(args.css).expanduser().resolve() if args.css else (default_css if default_css.exists() else None)

    # md-to-pdf CLI (as of 2026) writes output next to the input file as <in>.pdf.
    # It no longer supports an explicit --output flag, so we render to the default
    # location and then move if the user requested a different path.
    default_rendered_pdf = in_path.with_suffix(".pdf")
    if default_rendered_pdf.exists() and default_rendered_pdf.resolve() != out_path:
        default_rendered_pdf.unlink()

    cmd = [npx, "--yes", "md-to-pdf", str(in_path)]
    if css_path:
        cmd.extend(["--stylesheet", str(css_path)])
    if args.title:
        cmd.extend(["--document-title", args.title])
    if args.no_sandbox:
        cmd.extend(["--launch-options", '{"args":["--no-sandbox"]}'])

    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        raise SystemExit(f"PDF render failed (md-to-pdf). Exit code: {e.returncode}")

    if not default_rendered_pdf.exists():
        raise SystemExit(f"PDF render failed (md-to-pdf): expected output not found: {default_rendered_pdf}")

    if default_rendered_pdf.resolve() != out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        default_rendered_pdf.replace(out_path)

    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
