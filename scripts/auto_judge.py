#!/usr/bin/env python3
"""
Prepare an "auto-judgement" bundle for Codex to execute:
- Generate claims list
- Build judge packet

Note: spawning agents is performed by Codex (not from this script). This script outputs
paths and ready-to-send prompt text to minimize manual steps.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Prepare judge bundle for a report.")
    p.add_argument("--report", required=True, help="Path to thesis pack markdown")
    p.add_argument("--theme", required=True, help="Theme name")
    p.add_argument("--candidates", default="", help="Comma-separated tickers/names")
    p.add_argument("--horizon", default="1-3y")
    p.add_argument("--round", type=int, default=1, help="Debate round number (used for folder naming).")
    p.add_argument("--extra-file", default="", help="Optional extra context (e.g., filing_snippets.md)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    report_path = Path(args.report).expanduser().resolve()
    if not report_path.exists():
        raise SystemExit(f"Report not found: {report_path}")

    skill_dir = Path(__file__).resolve().parents[1]
    # Place all intermediate artifacts next to the report, inside <company>/<date>/judge/round_N/
    run_dir = (report_path.parent / "judge" / f"round_{args.round}").resolve()
    run_dir.mkdir(parents=True, exist_ok=True)

    claims_path = run_dir / "claims.md"
    judge_packet_path = run_dir / "judge_packet.txt"

    gen_claims = skill_dir / "assets" / "tools" / "generate_claims.py"
    build_packet = skill_dir / "assets" / "tools" / "build_judge_packet.py"

    subprocess.check_call(
        [
            sys.executable,
            str(gen_claims),
            "--theme",
            args.theme,
            "--candidates",
            args.candidates,
            "--horizon",
            args.horizon,
            "--format",
            "md",
            "--out",
            str(claims_path),
        ]
    )

    # Also pass a short claim list to the packet (first-line CSV style).
    # The judge_packet includes the report text; the claims file provides the full numbered list.
    subprocess.check_call(
        [
            sys.executable,
            str(build_packet),
            "--report",
            str(report_path),
            "--claims",
            "Demand confirmed,Must-pass gate exists,Supplier count <=3,Lead time >12m,Value capture visible,Catalysts time-bounded,Bear case explicit",
            "--claims-file",
            str(claims_path),
            "--extra-file",
            args.extra_file,
            "--out",
            str(judge_packet_path),
        ]
    )

    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
