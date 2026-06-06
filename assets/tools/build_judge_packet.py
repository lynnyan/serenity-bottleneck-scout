#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build a single judge packet prompt from a report + claims.")
    p.add_argument("--report", required=True, help="Path to thesis pack markdown")
    p.add_argument("--claims", default="", help="Comma-separated claims (optional)")
    p.add_argument("--claims-file", default="", help="Path to a claims markdown/text file (optional)")
    p.add_argument("--extra-file", default="", help="Optional extra context file (e.g., filing snippets, bear attacks)")
    p.add_argument("--out", default="", help="Output text file (default: stdout)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    report_path = Path(args.report).expanduser().resolve()
    if not report_path.exists():
        raise SystemExit(f"Report not found: {report_path}")

    skill_dir = Path(__file__).resolve().parents[2]
    judge_prompt_path = skill_dir / "assets" / "templates" / "judge_prompt.md"
    if not judge_prompt_path.exists():
        raise SystemExit(f"Missing judge prompt template: {judge_prompt_path}")

    judge_prompt = judge_prompt_path.read_text(encoding="utf-8")
    report_text = report_path.read_text(encoding="utf-8")
    claims = [c.strip() for c in args.claims.split(",") if c.strip()]
    claims_file_text = ""
    if args.claims_file:
        cf = Path(args.claims_file).expanduser().resolve()
        if not cf.exists():
            raise SystemExit(f"Claims file not found: {cf}")
        claims_file_text = cf.read_text(encoding="utf-8")

    extra_text = ""
    if args.extra_file:
        ef = Path(args.extra_file).expanduser().resolve()
        if not ef.exists():
            raise SystemExit(f"Extra file not found: {ef}")
        extra_text = ef.read_text(encoding="utf-8")

    packet = []
    packet.append(judge_prompt.strip())
    packet.append("\n\n---\n\nINPUTS\n")
    packet.append(f"Report path: {report_path}\n")
    if claims:
        packet.append("Must-be-true claims:\n")
        for i, c in enumerate(claims, start=1):
            packet.append(f"{i}. {c}\n")
    if claims_file_text:
        packet.append("\nClaims file:\n")
        packet.append(claims_file_text)
        if not claims_file_text.endswith("\n"):
            packet.append("\n")
    if extra_text:
        packet.append("\nExtra context:\n")
        packet.append(extra_text)
        if not extra_text.endswith("\n"):
            packet.append("\n")
    packet.append("\nReport text:\n")
    packet.append(report_text)
    out_text = "".join(packet)

    if args.out:
        out_path = Path(args.out).expanduser().resolve()
        out_path.write_text(out_text, encoding="utf-8")
        print(out_path)
    else:
        print(out_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
