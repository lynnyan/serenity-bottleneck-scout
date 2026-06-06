#!/usr/bin/env python3
"""
Minimal SEC EDGAR helper (US only).

Purpose: support the “IR/filings” evidence channel by fetching recent filings metadata
and downloading primary documents for offline reading.

Requirements:
- Set SEC_USER_AGENT (SEC requires a descriptive User-Agent).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request
import gzip
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


SEC_BASE = "https://data.sec.gov"
SEC_ARCHIVES_BASE = "https://www.sec.gov"
TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"


@dataclass(frozen=True)
class FilingRef:
    accession: str
    form: str
    filing_date: str
    primary_doc: str


def _ua() -> str:
    ua = os.environ.get("SEC_USER_AGENT", "").strip()
    if not ua:
        raise SystemExit(
            "Missing SEC_USER_AGENT. Example: export SEC_USER_AGENT='name email@example.com'"
        )
    return ua


def _http_get_json(url: str) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": _ua(), "Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read()
            encoding = (resp.headers.get("Content-Encoding") or "").lower()
            if encoding == "gzip" or raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            return json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise SystemExit(f"HTTP error {e.code} for {url}") from e
    except urllib.error.URLError as e:
        raise SystemExit(f"Network error for {url}: {e}") from e


def _http_get_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": _ua(), "Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
            encoding = (resp.headers.get("Content-Encoding") or "").lower()
            if encoding == "gzip" or raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            return raw
    except urllib.error.HTTPError as e:
        raise SystemExit(f"HTTP error {e.code} for {url}") from e
    except urllib.error.URLError as e:
        raise SystemExit(f"Network error for {url}: {e}") from e


def ticker_to_cik(ticker: str) -> str:
    ticker = ticker.strip().upper()
    mapping = _http_get_json(TICKER_MAP_URL)
    for _, row in mapping.items():
        if str(row.get("ticker", "")).upper() == ticker:
            cik_int = int(row["cik_str"])
            return f"{cik_int:010d}"
    raise SystemExit(f"Ticker not found in SEC mapping: {ticker}")


def list_recent_filings(cik10: str, forms: set[str], limit: int) -> list[FilingRef]:
    data = _http_get_json(f"{SEC_BASE}/submissions/CIK{cik10}.json")
    recent = data.get("filings", {}).get("recent", {})
    accessions = recent.get("accessionNumber", [])
    form_list = recent.get("form", [])
    filing_dates = recent.get("filingDate", [])
    primary_docs = recent.get("primaryDocument", [])

    out: list[FilingRef] = []
    for accession, form, fdate, pdoc in zip(accessions, form_list, filing_dates, primary_docs):
        if forms and form not in forms:
            continue
        out.append(FilingRef(accession=accession, form=form, filing_date=fdate, primary_doc=pdoc))
        if len(out) >= limit:
            break
    return out


def _sanitize_filename(name: str) -> str:
    name = name.strip()
    name = re.sub(r"[^A-Za-z0-9_.-]+", "_", name)
    return name or "file"


def download_filing_docs(cik10: str, filings: Iterable[FilingRef], out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    saved: list[Path] = []
    for ref in filings:
        accession_nodash = ref.accession.replace("-", "")
        url = f"{SEC_ARCHIVES_BASE}/Archives/edgar/data/{int(cik10)}/{accession_nodash}/{ref.primary_doc}"
        content = _http_get_bytes(url)
        fname = _sanitize_filename(f"{ref.filing_date}_{ref.form}_{ref.primary_doc}")
        path = out_dir / fname
        path.write_bytes(content)
        saved.append(path)
        time.sleep(0.2)  # be polite
    return saved


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--ticker", required=True, help="US ticker, e.g. AAPL")
    p.add_argument(
        "--forms",
        default="10-K,10-Q,8-K",
        help="Comma-separated form list, e.g. '10-K,10-Q,8-K' (empty = all)",
    )
    p.add_argument("--limit", type=int, default=10, help="Number of recent filings to list/download")
    p.add_argument("--out-dir", default="edgar_downloads", help="Output directory for downloaded docs")
    p.add_argument("--download", action="store_true", help="Download primary documents")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    forms = {f.strip() for f in args.forms.split(",") if f.strip()}
    cik10 = ticker_to_cik(args.ticker)
    filings = list_recent_filings(cik10, forms=forms, limit=args.limit)

    print(json.dumps([ref.__dict__ for ref in filings], ensure_ascii=False, indent=2))
    if args.download:
        out_dir = Path(args.out_dir)
        saved = download_filing_docs(cik10, filings, out_dir)
        print("\nDownloaded:")
        for p in saved:
            print(p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
