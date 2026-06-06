#!/usr/bin/env python3
"""
Create a Reporter revision packet for multi-round debate.

Given:
- a thesis-pack report path
- a judge verdict file path (Round N)

Outputs:
- debate/round_{N+1}/reporter_packet.txt next to the report

This script does NOT spawn agents; Codex does. It just produces a ready-to-send packet.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--report", required=True, help="Path to thesis-pack markdown")
    p.add_argument("--judge-verdict", required=True, help="Path to judge verdict markdown/text")
    p.add_argument("--next-round", type=int, required=True, help="Next round number, e.g. 2")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    report_path = Path(args.report).expanduser().resolve()
    verdict_path = Path(args.judge_verdict).expanduser().resolve()
    if not report_path.exists():
        raise SystemExit(f"Report not found: {report_path}")
    if not verdict_path.exists():
        raise SystemExit(f"Judge verdict not found: {verdict_path}")

    skill_dir = Path(__file__).resolve().parents[1]

    reporter_revision_prompt = (skill_dir / "assets" / "templates" / "reporter_revision_prompt.md").read_text(
        encoding="utf-8"
    )
    supplier_rules = (skill_dir / "assets" / "templates" / "supplier_confirmation_rules.md").read_text(encoding="utf-8")
    protocol = (skill_dir / "assets" / "templates" / "debate_protocol.md").read_text(encoding="utf-8")

    verdict_text = verdict_path.read_text(encoding="utf-8")

    out_dir = (report_path.parent / "debate" / f"round_{args.next_round}").resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "reporter_packet.txt"

    packet = []
    packet.append(reporter_revision_prompt.strip())
    packet.append("\n\n---\n\nINPUTS\n")
    packet.append(f"Thesis pack path to edit: {report_path}\n")
    packet.append(f"Judge verdict path: {verdict_path}\n\n")
    packet.append("Judge verdict text:\n")
    packet.append(verdict_text)
    if not verdict_text.endswith("\n"):
        packet.append("\n")
    packet.append("\nSupplier confirmation rules:\n")
    packet.append(supplier_rules)
    packet.append("\nDebate protocol:\n")
    packet.append(protocol)

    out_path.write_text("".join(packet), encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

