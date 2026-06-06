#!/usr/bin/env python3
"""
Generate a default “must-be-true claims” list for Serenity-style bottleneck research.

This is intentionally deterministic and template-driven (no LLM required), so it can be
reused in teams and runs reliably offline.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(frozen=True)
class Inputs:
    theme: str
    candidates: list[str]
    horizon: str
    out: str
    fmt: str


def parse_args() -> Inputs:
    p = argparse.ArgumentParser(description="Generate must-be-true claims list (template).")
    p.add_argument("--theme", required=True, help="Theme, e.g. 'ELS / optical interconnect'")
    p.add_argument(
        "--candidates",
        default="",
        help="Comma-separated tickers/names (optional). Example: 'AAA,BBB,CCC'",
    )
    p.add_argument("--horizon", default="1-3y", help="0-6m / 1-3y / 3-5y (free text ok)")
    p.add_argument("--format", choices=["md", "json"], default="md")
    p.add_argument("--out", default="", help="Output file path (default: stdout)")
    args = p.parse_args()
    candidates = [c.strip() for c in args.candidates.split(",") if c.strip()]
    return Inputs(theme=args.theme, candidates=candidates, horizon=args.horizon, out=args.out, fmt=args.format)


def build_claims(inputs: Inputs) -> list[str]:
    base = [
        f"Demand is real and expanding for '{inputs.theme}' over horizon '{inputs.horizon}', confirmed by >=2 independent primary signals.",
        "A physical, end-to-end supply chain map exists (raw materials → substrates → devices → modules → systems → end customers), and the node under study is unavoidable for at least one critical path.",
        "Chokepoint test: the node is a must-pass interface/platform/standard gate (e.g., MSA/PDK/qualification) connecting >=2 Tier-1 downstream ecosystems.",
        "Bottleneck test: supply is constrained (lead times >12 months watch / >18 months strong) and expansion is slow or capital/tooling constrained.",
        "Supplier concentration is high (<=3 credible suppliers) OR switching/qualification time is long enough to create durable pricing/lead-time power.",
        "Value capture will show up in company-level numbers (mix/GM/ASP/backlog) within 4–8 quarters, not only as an industry narrative.",
        "Catalyst clock is concrete: >=1 hard catalyst in 3–9 months AND >=1 confirmation catalyst in 12–18 months.",
        "Bear case is explicit: credible substitution paths, second-source qualification, OEM vertical integration, policy/geography shocks, and valuation/liquidity risks are addressed with monitoring signals.",
    ]

    if not inputs.candidates:
        return base

    per_name = []
    for c in inputs.candidates:
        per_name.extend(
            [
                f"{c}: downstream must-pass customers/partners are evidenced by primary sources (both sides if possible).",
                f"{c}: management commentary or filings indicate capacity/lead-time constraints and plans (capex/financing) to address them.",
                f"{c}: geography/policy exposure (export controls, single-site risks) is mapped and monitored.",
            ]
        )
    return base + per_name


def render_md(inputs: Inputs, claims: list[str]) -> str:
    lines = []
    lines.append(f"# Must-be-true claims — {inputs.theme}\n")
    lines.append(f"Date: {date.today().isoformat()}\n")
    lines.append(f"Horizon: {inputs.horizon}\n")
    if inputs.candidates:
        lines.append(f"Candidates: {', '.join(inputs.candidates)}\n")
    lines.append("\n")
    for i, c in enumerate(claims, start=1):
        lines.append(f"{i}. {c}\n")
    return "".join(lines)


def main() -> int:
    inputs = parse_args()
    claims = build_claims(inputs)

    if inputs.fmt == "json":
        out_text = json.dumps({"theme": inputs.theme, "horizon": inputs.horizon, "candidates": inputs.candidates, "claims": claims}, ensure_ascii=False, indent=2)
    else:
        out_text = render_md(inputs, claims)

    if inputs.out:
        out_path = Path(inputs.out).expanduser().resolve()
        out_path.write_text(out_text, encoding="utf-8")
        print(out_path)
    else:
        print(out_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
