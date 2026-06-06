#!/usr/bin/env python3
"""
Extract key filing snippets for Serenity-style evidence gathering.

Goal: given one or more filing documents (HTML or text), output a compact markdown
with paragraphs that mention:
- risk factors
- backlog / orders
- capex / capacity expansion
- geography / export / policy exposure

This is heuristic (keyword-based) and meant to speed up the “find the right passages”
step. Users should still read the primary document around the snippet.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from html.parser import HTMLParser


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []

    def handle_data(self, data: str) -> None:
        if data:
            self._chunks.append(data)

    def text(self) -> str:
        return "\n".join(self._chunks)


@dataclass(frozen=True)
class Section:
    title: str
    patterns: list[re.Pattern[str]]


DEFAULT_SECTIONS: list[Section] = [
    Section(
        title="Risk / risk factors",
        patterns=[
            re.compile(r"\brisk factors?\b", re.I),
            re.compile(r"\bitem\s*1a\b", re.I),
            re.compile(r"\bmaterial adverse\b", re.I),
        ],
    ),
    Section(
        title="Backlog / orders / demand signals",
        patterns=[
            re.compile(r"\bbacklog\b", re.I),
            re.compile(r"\bbook[- ]?to[- ]?bill\b", re.I),
            re.compile(r"\border(s|ed|ing)?\b", re.I),
            re.compile(r"\bcontract(s)?\b", re.I),
        ],
    ),
    Section(
        title="Capex / capacity / expansion",
        patterns=[
            re.compile(r"\bcapex\b", re.I),
            re.compile(r"\bcapital expenditure(s)?\b", re.I),
            re.compile(r"\bexpand(ing|ed)?\b", re.I),
            re.compile(r"\bcapacity\b", re.I),
            re.compile(r"\bnew facility\b", re.I),
            re.compile(r"\bfinanc(ing|ed|e)\b", re.I),
        ],
    ),
    Section(
        title="Geography / policy / export controls",
        patterns=[
            re.compile(r"\bchina\b", re.I),
            re.compile(r"\bexport\b", re.I),
            re.compile(r"\bsanction(s)?\b", re.I),
            re.compile(r"\btarriff(s)?\b", re.I),
            re.compile(r"\blicense(s|d)?\b", re.I),
            re.compile(r"\bgeograph(y|ic)\b", re.I),
        ],
    ),
]


def _looks_like_html(text: str) -> bool:
    return "<html" in text.lower() or "</" in text or "<!doctype" in text.lower()


def _to_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    if _looks_like_html(raw):
        parser = _TextExtractor()
        parser.feed(raw)
        raw = parser.text()
    # normalize whitespace
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    raw = re.sub(r"[ \t]+", " ", raw)
    return raw


def _split_paragraphs(text: str) -> list[str]:
    # Split on blank lines or long runs of whitespace/newlines.
    chunks = re.split(r"\n\s*\n+", text)
    paras = []
    for c in chunks:
        c = c.strip()
        if not c:
            continue
        # squash single newlines inside paragraphs for readability
        c = re.sub(r"\n+", " ", c)
        # avoid huge blobs
        if len(c) > 2000:
            c = c[:2000] + "…"
        paras.append(c)
    return paras


def _match_any(patterns: list[re.Pattern[str]], para: str) -> bool:
    return any(p.search(para) for p in patterns)


def extract(path: Path, sections: list[Section], max_per_section: int) -> dict[str, list[str]]:
    text = _to_text(path)
    paras = _split_paragraphs(text)
    out: dict[str, list[str]] = {s.title: [] for s in sections}

    for para in paras:
        for s in sections:
            if len(out[s.title]) >= max_per_section:
                continue
            if _match_any(s.patterns, para):
                out[s.title].append(para)
    return out


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Extract filing snippets by keyword sections.")
    p.add_argument("--in", dest="inputs", action="append", required=True, help="Input filing path (repeatable)")
    p.add_argument("--out", default="filing_snippets.md", help="Output markdown path")
    p.add_argument("--max", type=int, default=8, help="Max snippets per section per file")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_path = Path(args.out).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append("# Filing snippet extraction\n\n")
    lines.append("> Heuristic keyword extraction. Read primary sources for full context.\n\n")

    for in_path_str in args.inputs:
        path = Path(in_path_str).expanduser().resolve()
        if not path.exists():
            raise SystemExit(f"Input not found: {path}")
        lines.append(f"## Source: {path}\n\n")
        extracted = extract(path, DEFAULT_SECTIONS, max_per_section=args.max)
        for section_title, snippets in extracted.items():
            lines.append(f"### {section_title}\n\n")
            if not snippets:
                lines.append("- (no matches)\n\n")
                continue
            for s in snippets:
                lines.append(f"- {s}\n")
            lines.append("\n")

    out_path.write_text("".join(lines), encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

