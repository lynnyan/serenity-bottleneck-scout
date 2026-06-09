#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
import gzip
from io import BytesIO
from pathlib import Path
import re
from typing import Iterable
import warnings


@dataclass(frozen=True)
class Group:
    name: str
    keywords: list[str]


DEFAULT_GROUPS: dict[str, Group] = {
    "supplychain_leads": Group(
        name="supplychain_leads",
        keywords=[
            # Anchor / product
            "Tesla",
            "特斯拉",
            "Optimus",
            "humanoid",
            "人形机器人",
            "机器人",
            # Relationship / confirmation
            "客户",
            "customer",
            "供应商",
            "supplier",
            "Tier",
            "tier",
            "一级供应商",
            "二级供应商",
            "定点",
            "design-in",
            "qualification",
            # Cooperation / JV / site
            "合资",
            "合资企业",
            "joint venture",
            "JV",
            "共同出资",
            "设立",
            "工业园",
            "园区",
            "Mexico",
            "墨西哥",
            # Robot-specific common bottlenecks (generic, for fast grep)
            "谐波",
            "harmonic",
            "减速器",
            "reducer",
            "actuator",
            "关节",
            "servo",
            "丝杠",
            "ball screw",
            "轴承",
            "bearing",
            "编码器",
            "encoder",
        ],
    ),
    "risk": Group(
        name="risk",
        keywords=[
            "风险",
            "Risk",
            "risk factor",
            "forward-looking",
            "不确定",
            "uncertain",
            "诉讼",
            "litigation",
            "供应链",
            "supply chain",
            "原材料",
            "raw material",
        ],
    ),
    "backlog": Group(
        name="backlog",
        keywords=[
            "在手",
            "订单",
            "合同",
            "backlog",
            "order",
            "booking",
            "pipeline",
            "预付款",
            "prepayment",
        ],
    ),
    "capex": Group(
        name="capex",
        keywords=[
            "资本开支",
            "资本性支出",
            "capex",
            "capital expenditure",
            "固定资产",
            "在建工程",
            "扩产",
            "产能",
            "募投",
            "投资",
            "设备",
            "tooling",
        ],
    ),
    "geo": Group(
        name="geo",
        keywords=[
            "海外",
            "出口",
            "进口",
            "美国",
            "中国",
            "Europe",
            "APAC",
            "export",
            "tariff",
            "关税",
            "制裁",
            "出口管制",
        ],
    ),
}


def _normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _iter_keywords(groups: Iterable[str], extra_keywords: list[str]) -> list[str]:
    kws: list[str] = []
    for g in groups:
        group = DEFAULT_GROUPS.get(g)
        if group:
            kws.extend(group.keywords)
    kws.extend([k.strip() for k in extra_keywords if k.strip()])
    # de-dup preserving order
    seen = set()
    out: list[str] = []
    for k in kws:
        if k in seen:
            continue
        seen.add(k)
        out.append(k)
    return out


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Extract keyword-centered snippets from a PDF into Markdown.")
    p.add_argument("--in", dest="in_path", required=True, help="Input PDF path")
    p.add_argument("--out", dest="out_path", required=True, help="Output markdown path")
    p.add_argument(
        "--groups",
        default="risk,backlog,capex,geo",
        help="Comma-separated groups: supplychain_leads,risk,backlog,capex,geo (default: risk,backlog,capex,geo)",
    )
    p.add_argument("--keyword", action="append", default=[], help="Extra keyword (repeatable)")
    p.add_argument("--max-pages", type=int, default=0, help="If >0, only scan first N pages")
    p.add_argument("--max-hits", type=int, default=120, help="Max snippets to output")
    p.add_argument("--window-left", type=int, default=140, help="Chars to capture left of match")
    p.add_argument("--window-right", type=int, default=260, help="Chars to capture right of match")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    in_path = Path(args.in_path).expanduser().resolve()
    out_path = Path(args.out_path).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if not in_path.exists():
        raise SystemExit(f"PDF not found: {in_path}")

    try:
        warnings.filterwarnings("ignore", message=r".*ARC4 has been moved.*")
        from pypdf import PdfReader
    except Exception as e:  # pragma: no cover
        raise SystemExit(f"Missing dependency pypdf: {e}")

    groups = [g.strip() for g in str(args.groups).split(",") if g.strip()]
    keywords = _iter_keywords(groups, list(args.keyword))
    if not keywords:
        raise SystemExit("No keywords to search. Provide --groups and/or --keyword.")

    # Fast header sniff (avoid loading huge PDFs into memory unless needed).
    with in_path.open("rb") as f:
        head = f.read(8192)

    is_gzip = head[:2] == b"\x1f\x8b"
    pdf_bytes: bytes | None = None
    probe = head

    # Some sources may save gzipped bytes to disk (mis-labeled .pdf). Only then we fully materialize.
    if is_gzip:
        try:
            pdf_bytes = gzip.decompress(in_path.read_bytes())
        except Exception:
            raise SystemExit(
                "Input looks like gzip-compressed bytes but could not be decompressed. "
                "Re-download the PDF (or fetch via a browser) and retry."
            )
        probe = pdf_bytes[:8192]

    # Some WAF/HTML responses may have leading whitespace or UTF-8 BOM.
    probe2 = probe
    if probe2.startswith(b"\xef\xbb\xbf"):
        probe2 = probe2[3:]
    probe2 = probe2.lstrip()

    if probe2[:4].lower() in (b"<htm", b"<!do"):
        raise SystemExit(
            "Input is HTML, not a PDF (likely an exchange/WAF anti-bot page). "
            "Open the link in a real browser to download the PDF, then rerun this tool on the saved PDF file."
        )
    if not probe2.startswith(b"%PDF"):
        raise SystemExit(
            "Input does not look like a PDF (missing %PDF header). "
            "Please verify the file is an actual PDF and not a redirected HTML page."
        )

    reader = PdfReader(BytesIO(pdf_bytes)) if pdf_bytes is not None else PdfReader(str(in_path))
    page_count = len(reader.pages)
    scan_pages = page_count if args.max_pages <= 0 else min(page_count, args.max_pages)

    hits: list[tuple[int, str, str]] = []  # (page, keyword, snippet)
    for idx in range(scan_pages):
        page_no = idx + 1
        text = _normalize_space(reader.pages[idx].extract_text() or "")
        if not text:
            continue
        text_lower = text.lower()
        for kw in keywords:
            kw_norm = kw.lower()
            if kw_norm not in text_lower:
                continue
            for m in list(re.finditer(re.escape(kw), text, flags=re.IGNORECASE))[:2]:
                start = max(0, m.start() - int(args.window_left))
                end = min(len(text), m.end() + int(args.window_right))
                snippet = text[start:end].strip()
                hits.append((page_no, kw, snippet))

    # de-dup by (page, snippet) and keep stable order
    seen = set()
    dedup: list[tuple[int, str, str]] = []
    for page_no, kw, snippet in hits:
        key = (page_no, snippet)
        if key in seen:
            continue
        seen.add(key)
        dedup.append((page_no, kw, snippet))

    dedup = dedup[: int(args.max_hits)]

    md: list[str] = []
    md.append("# Extracted PDF snippets")
    md.append("")
    md.append(f"Source PDF: {in_path}")
    md.append(f"Scanned pages: 1..{scan_pages} (of {page_count})")
    md.append(f"Groups: {', '.join(groups) if groups else '(none)'}")
    md.append(f"Extra keywords: {', '.join(args.keyword) if args.keyword else '(none)'}")
    md.append("")
    md.append("> Heuristic extraction around keywords. Use the PDF for full context and exact numbers.")
    md.append("")

    cur = None
    for page_no, kw, snippet in dedup:
        if page_no != cur:
            md.append(f"## Page {page_no}")
            cur = page_no
        md.append(f"- KW `{kw}`: {snippet}")
    md.append("")

    out_path.write_text("\n".join(md), encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
