#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlparse


def _slug(url: str) -> str:
    p = urlparse(url)
    base = (p.path.rsplit("/", 1)[-1] or "doc").strip()
    base = "".join([c if c.isalnum() or c in ("-", "_", ".") else "_" for c in base])[:80]
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    if not base.lower().endswith(".pdf"):
        base = base + ".pdf"
    return f"{h}_{base}"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Lead-hunter for exchange/filing PDFs: fetch PDFs (best-effort) and extract supply-chain clues."
    )
    p.add_argument("--url", action="append", default=[], help="PDF/filing URL (repeatable)")
    p.add_argument("--url-file", default="", help="Text file with one URL per line")
    p.add_argument("--out-dir", default="leads", help="Output directory (default: ./leads)")
    p.add_argument(
        "--groups",
        default="supplychain_leads,geo,capex,backlog,risk",
        help="Groups passed to extract_pdf_snippets.py",
    )
    p.add_argument("--max-pages", type=int, default=0, help="If >0, only scan first N pages per PDF")
    p.add_argument("--timeout", type=int, default=25, help="Fetch timeout seconds (passed to fetch_snapshot.py)")
    p.add_argument("--user-agent", default="", help="Override User-Agent for fetching (optional)")
    p.add_argument("--referer", default="", help="Optional Referer header for fetching (some exchanges need it)")
    p.add_argument("--accept", default="", help="Optional Accept header for fetching")
    p.add_argument("--max-bytes", type=int, default=25_000_000, help="Abort fetch if body exceeds this size")
    p.add_argument("--insecure", action="store_true", help="Disable TLS verification for fetch (use sparingly)")
    return p.parse_args()


def _read_urls(args: argparse.Namespace) -> list[str]:
    urls = [u.strip() for u in args.url if u.strip()]
    if args.url_file:
        p = Path(args.url_file).expanduser()
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            urls.append(line)
    # de-dup preserving order
    seen = set()
    out: list[str] = []
    for u in urls:
        if u in seen:
            continue
        seen.add(u)
        out.append(u)
    return out


def main() -> int:
    args = parse_args()
    urls = _read_urls(args)
    if not urls:
        raise SystemExit("No URLs provided. Use --url and/or --url-file.")

    out_dir = Path(args.out_dir).expanduser().resolve()
    sources_dir = out_dir / "sources"
    snippets_dir = out_dir / "snippets"
    sources_dir.mkdir(parents=True, exist_ok=True)
    snippets_dir.mkdir(parents=True, exist_ok=True)

    root = Path(__file__).resolve().parents[1]
    fetcher = root / "assets" / "tools" / "fetch_snapshot.py"
    extractor = root / "assets" / "tools" / "extract_pdf_snippets.py"

    index_lines: list[str] = []
    index_lines.append("# Filing lead-hunter results")
    index_lines.append("")
    index_lines.append("> Notes:")
    index_lines.append("> - This is a heuristic lead-capture tool. Always open the original filing PDF for full context.")
    index_lines.append("> - If a URL is blocked by WAF (common for some exchanges), download via a real browser and rerun the extractor on the saved PDF.")
    index_lines.append("")

    for url in urls:
        name = _slug(url)
        pdf_path = sources_dir / name
        index_lines.append(f"## {name}")
        index_lines.append("")
        index_lines.append(f"- Source URL: {url}")

        try:
            fetch_cmd = [sys.executable, str(fetcher), "--url", url, "--out", str(pdf_path)]
            fetch_cmd.extend(["--timeout", str(int(args.timeout))])
            fetch_cmd.extend(["--max-bytes", str(int(args.max_bytes))])
            if args.user_agent:
                fetch_cmd.extend(["--user-agent", str(args.user_agent)])
            if args.referer:
                fetch_cmd.extend(["--referer", str(args.referer)])
            if args.accept:
                fetch_cmd.extend(["--accept", str(args.accept)])
            if args.insecure:
                fetch_cmd.append("--insecure")

            subprocess.run(
                fetch_cmd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            index_lines.append(f"- Fetch: FAILED (`{e.returncode}`)")
            if e.stderr:
                index_lines.append("")
                index_lines.append("```")
                index_lines.append(e.stderr.strip()[:1200])
                index_lines.append("```")
                index_lines.append("")
            continue

        # Run extractor (will fail with a clear message if the file is HTML/WAF instead of PDF).
        out_md = snippets_dir / (pdf_path.stem + ".snippets.md")
        cmd = [
            sys.executable,
            str(extractor),
            "--in",
            str(pdf_path),
            "--out",
            str(out_md),
            "--groups",
            str(args.groups),
        ]
        if int(args.max_pages) > 0:
            cmd.extend(["--max-pages", str(int(args.max_pages))])

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            index_lines.append(f"- Snippets: `{out_md}`")
        except subprocess.CalledProcessError as e:
            index_lines.append("- Snippets: FAILED (likely not a real PDF; see below)")
            if e.stderr:
                index_lines.append("")
                index_lines.append("```")
                index_lines.append(e.stderr.strip()[:1200])
                index_lines.append("```")
                index_lines.append("")

        index_lines.append("")

    out_index = out_dir / "filing_leads.md"
    out_index.write_text("\n".join(index_lines), encoding="utf-8")
    print(str(out_index))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
