#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import urllib.error
import urllib.request


DEFAULT_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class Result:
    url: str
    final_url: str
    status: int
    content_type: str
    bytes: int
    fetched_at: str
    out_path: str
    meta_path: str
    title: str


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _guess_title(html: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        return ""
    title = re.sub(r"\s+", " ", m.group(1)).strip()
    return title[:200]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Fetch a URL and save a reproducible snapshot (HTML/PDF/etc).")
    p.add_argument("--url", required=True)
    p.add_argument("--out", required=True, help="Output file path (e.g., sources/web/foo.html)")
    p.add_argument("--meta", default="", help="Optional metadata JSON path (default: <out>.meta.json)")
    p.add_argument("--timeout", type=int, default=25)
    p.add_argument("--user-agent", default=DEFAULT_UA)
    p.add_argument("--referer", default="")
    p.add_argument("--accept", default="*/*")
    p.add_argument("--max-bytes", type=int, default=25_000_000, help="Abort if body exceeds this size")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_path = Path(args.out).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path = Path(args.meta).expanduser().resolve() if args.meta else out_path.with_suffix(out_path.suffix + ".meta.json")

    req = urllib.request.Request(
        args.url,
        headers={
            "User-Agent": args.user_agent,
            "Accept": args.accept,
            **({"Referer": args.referer} if args.referer else {}),
        },
        method="GET",
    )

    fetched_at = _iso_now()
    title = ""
    try:
        with urllib.request.urlopen(req, timeout=args.timeout) as resp:
            status = getattr(resp, "status", 200)
            final_url = resp.geturl()
            content_type = resp.headers.get("Content-Type", "")

            data = resp.read(args.max_bytes + 1)
            if len(data) > args.max_bytes:
                raise SystemExit(f"Body too large (> {args.max_bytes} bytes).")

            out_path.write_bytes(data)

            if "text/html" in content_type.lower():
                try:
                    html = data.decode("utf-8", errors="ignore")
                except Exception:
                    html = ""
                title = _guess_title(html)
    except urllib.error.HTTPError as e:
        status = int(getattr(e, "code", 0) or 0)
        final_url = args.url
        content_type = str(getattr(e, "headers", {}).get("Content-Type", ""))
        data = e.read() if hasattr(e, "read") else b""
        out_path.write_bytes(data)
    except urllib.error.URLError as e:
        raise SystemExit(f"Fetch failed: {e}")

    result = Result(
        url=args.url,
        final_url=final_url,
        status=status,
        content_type=content_type,
        bytes=int(out_path.stat().st_size) if out_path.exists() else 0,
        fetched_at=fetched_at,
        out_path=str(out_path),
        meta_path=str(meta_path),
        title=title,
    )
    meta_path.write_text(json.dumps(result.__dict__, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

