#!/usr/bin/env python3
"""
Lightweight OHLCV downloader (best-effort).

Primary purpose: support the “price/volume” evidence channel by producing a CSV
that can be inspected or charted.

Strategy:
- Prefer yfinance if installed.
- Fallback to Stooq for many symbols (mostly US tickers).
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

import urllib.error
import urllib.request


@dataclass(frozen=True)
class Bar:
    date: str
    open: str
    high: str
    low: str
    close: str
    volume: str


def _write_csv(path: Path, rows: Iterable[Bar]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "open", "high", "low", "close", "volume"])
        for r in rows:
            w.writerow([r.date, r.open, r.high, r.low, r.close, r.volume])


def _try_yfinance(symbol: str) -> list[Bar] | None:
    try:
        import yfinance as yf  # type: ignore
    except Exception:
        return None
    df = yf.download(symbol, period="max", auto_adjust=False, progress=False)
    if df is None or df.empty:
        return []
    out: list[Bar] = []
    for idx, row in df.iterrows():
        dt = idx.to_pydatetime().date().isoformat()
        out.append(
            Bar(
                date=dt,
                open=str(row.get("Open", "")),
                high=str(row.get("High", "")),
                low=str(row.get("Low", "")),
                close=str(row.get("Close", "")),
                volume=str(int(row.get("Volume", 0))) if row.get("Volume") is not None else "",
            )
        )
    return out


def _stooq_symbol(symbol: str) -> str:
    # Stooq uses lowercase for US tickers: aapl.us
    s = symbol.strip().lower()
    if "." in s:
        return s
    return f"{s}.us"


def _fetch_stooq(symbol: str) -> list[Bar]:
    stooq = _stooq_symbol(symbol)
    url = f"https://stooq.com/q/d/l/?s={stooq}&i=d"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            text = resp.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as e:
        raise SystemExit(f"Failed to fetch from Stooq: {e}") from e

    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if len(lines) <= 1:
        return []
    out: list[Bar] = []
    for ln in lines[1:]:
        parts = ln.split(",")
        if len(parts) < 6:
            continue
        dt = parts[0]
        try:
            datetime.fromisoformat(dt)
        except ValueError:
            continue
        out.append(Bar(date=dt, open=parts[1], high=parts[2], low=parts[3], close=parts[4], volume=parts[5]))
    return out


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--symbol", required=True, help="Ticker/symbol (best-effort), e.g. AAPL or 000001.SZ")
    p.add_argument("--out", default="ohlcv.csv", help="Output CSV path")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    rows = _try_yfinance(args.symbol)
    if rows is None:
        rows = _fetch_stooq(args.symbol)
    out_path = Path(args.out)
    _write_csv(out_path, rows)
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

