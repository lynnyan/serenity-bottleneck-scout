#!/usr/bin/env python3
"""
Debate bundle helper for multi-round workflow.

Creates:
- a thesis-pack skeleton (if requested)
- a claims file
- a reporter packet (Round 1)
- a judge packet (after Round 1, once the report is filled) can be generated via scripts/auto_judge.py

This script does NOT spawn agents; Codex does. It just produces ready-to-send prompt files.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--company", default="misc", help="Anchor company (used for output folder name).")
    p.add_argument("--theme", required=True)
    p.add_argument("--market", default="US / CN")
    p.add_argument("--horizon", default="1-3y")
    p.add_argument("--candidates", default="", help="Comma-separated (optional)")
    p.add_argument("--date", default="", help="YYYY-MM-DD (default: today). Used for reports/<company>/<date>/")
    p.add_argument("--run", default="", help='Optional run subfolder under the date, e.g. "run_01".')
    p.add_argument("--create-report", action="store_true", help="Create a new thesis-pack skeleton in reports/")
    p.add_argument("--report", default="", help="Existing report path (if not creating)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    skill_dir = Path(__file__).resolve().parents[1]

    if args.create_report:
        new_report = skill_dir / "scripts" / "new_serenity_report.py"
        cmd = [
            sys.executable,
            str(new_report),
            "--company",
            args.company,
            "--theme",
            args.theme,
            "--market",
            args.market,
            "--horizon",
            args.horizon,
            "--candidates",
            args.candidates,
        ]
        if args.date:
            cmd.extend(["--date", args.date])
        if args.run:
            cmd.extend(["--run", args.run])

        out = subprocess.check_output(
            [
                *cmd
            ],
            text=True,
        ).strip()
        report_path = Path(out).resolve()
    else:
        if not args.report:
            raise SystemExit("Provide --report or use --create-report")
        report_path = Path(args.report).expanduser().resolve()
        if not report_path.exists():
            raise SystemExit(f"Report not found: {report_path}")

    # Place debate artifacts next to the report, inside <company>/<date>/debate/round_1/
    round_dir = (report_path.parent / "debate" / "round_1").resolve()
    round_dir.mkdir(parents=True, exist_ok=True)

    claims_path = round_dir / "claims.md"
    reporter_packet_path = round_dir / "reporter_packet_round1.txt"

    gen_claims = skill_dir / "assets" / "tools" / "generate_claims.py"
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

    reporter_prompt = (skill_dir / "assets" / "templates" / "reporter_prompt.md").read_text(encoding="utf-8")
    supplier_rules = (skill_dir / "assets" / "templates" / "supplier_confirmation_rules.md").read_text(encoding="utf-8")
    protocol = (skill_dir / "assets" / "templates" / "debate_protocol.md").read_text(encoding="utf-8")

    packet = []
    packet.append(reporter_prompt.strip())
    packet.append("\n\n---\n\nINPUTS\n")
    packet.append(f"Theme: {args.theme}\n")
    packet.append(f"Market: {args.market}\n")
    packet.append(f"Horizon: {args.horizon}\n")
    packet.append(f"Candidates: {args.candidates}\n")
    if args.date:
        packet.append(f"Date: {args.date}\n")
    if args.run:
        packet.append(f"Run: {args.run}\n")
    packet.append(f"Thesis pack path to edit: {report_path}\n")
    packet.append(f"Claims path: {claims_path}\n")
    packet.append("\nSupplier confirmation rules:\n")
    packet.append(supplier_rules)
    packet.append("\nDebate protocol:\n")
    packet.append(protocol)

    reporter_packet_path.write_text("".join(packet), encoding="utf-8")

    print(round_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
