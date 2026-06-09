#!/usr/bin/env python3
"""You Search API (provider: ModelHub).

定位：
- 这是一个 **线索/导航** 工具（默认 T4），用于补齐“消息面/小站点/博客”等线索来源。
- 不要把搜索结果页面当作一手证据；必须回溯到公告/财报/IR/监管披露等原文。

配置（可选）：
- MODELHUB_SEARCH_URL：覆盖 endpoint
- MODELHUB_SEARCH_AK：覆盖 X-API-Key
- MODELHUB_CRAWL_TIMEOUT：超时秒数（默认 60）
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import time
from typing import Any


DEFAULT_SEARCH_URL = "https://aidp-i18ntt-sg.tiktok-row.net/api/modelhub/online/v2/crawl/you/v1/search"
# NOTE: kept for backward-compat with existing deployments. Prefer overriding via env var.
DEFAULT_API_KEY = "Q9BMmt4oIpImK2bkCLTqFYXXQcmJq8Iu_GPT_AK"


@dataclass
class SearchResultItem:
    title: str
    description: str
    url: str
    snippets: list[str] = field(default_factory=list)


def search_response_to_items(data: dict[str, Any]) -> list[SearchResultItem]:
    results = data.get("results")
    if not isinstance(results, dict):
        return []
    web = results.get("web")
    if not isinstance(web, list):
        return []
    out: list[SearchResultItem] = []
    for row in web:
        if not isinstance(row, dict):
            continue
        title = row.get("title") or ""
        desc = row.get("description") or ""
        url = row.get("url") or ""
        snips: list[str] = []
        raw_snips = row.get("snippets")
        if isinstance(raw_snips, str):
            snips = [raw_snips] if raw_snips.strip() else []
        elif isinstance(raw_snips, list):
            snips = [str(s) for s in raw_snips if s is not None]
        elif raw_snips is not None:
            snips = [str(raw_snips)]
        out.append(
            SearchResultItem(
                title=str(title).strip(),
                description=str(desc).strip(),
                url=str(url).strip(),
                snippets=snips,
            )
        )
    return out


def search_results_to_markdown(items: list[SearchResultItem], *, metadata: dict[str, Any] | None = None) -> str:
    lines: list[str] = ["# Web search results (You Search API / ModelHub)", ""]
    if metadata:
        if (q := metadata.get("query")) is not None:
            lines.append(f"**Query:** {q}")
        lat = metadata.get("latency")
        if lat is not None:
            try:
                lines.append(f"**Latency:** {float(lat):.2f}s")
            except (TypeError, ValueError):
                lines.append(f"**Latency:** {lat}")
        if (su := metadata.get("search_uuid")) is not None:
            lines.append(f"**Search id:** {su}")
        if len(lines) > 2:
            lines.append("")

    if not items:
        lines.append("_No web results._")
        return "\n".join(lines)

    for i, it in enumerate(items, start=1):
        head = f"[{it.title}]({it.url})" if it.url else (it.title or f"Result {i}")
        lines.append(f"## {i}. {head}")
        if it.description:
            lines.append(f"**Description:** {it.description}")
        if it.snippets:
            lines.append("**Snippets:**")
            for s in it.snippets:
                lines.append(f"- {s.replace(chr(10), ' ').strip()}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def search_web(
    *,
    query: str,
    count: int,
    include_domains: str = "",
    api_key: str,
    search_url: str,
    timeout_seconds: float,
    retry_times: int,
    retry_sleep_seconds: float,
) -> dict[str, Any]:
    q = (query or "").strip()
    if not q:
        return {"metadata": {"query": query}, "results": {"web": []}}

    try:
        import requests
    except Exception as e:  # pragma: no cover
        raise SystemExit(f"Missing dependency 'requests': {e}")

    params: dict[str, Any] = {"query": q, "count": int(count)}
    if include_domains.strip():
        params["include_domains"] = include_domains.strip()

    last_exception: Exception | None = None
    retry_times = max(1, int(retry_times))
    for attempt in range(1, retry_times + 1):
        try:
            connect_timeout = min(10.0, float(timeout_seconds))
            read_timeout = float(timeout_seconds)
            resp = requests.get(
                search_url,
                headers={"X-API-Key": api_key},
                params=params,
                timeout=(connect_timeout, read_timeout),
            )
            try:
                data = resp.json()
            except Exception:
                text = (resp.text or "").strip()
                raise SystemExit(f"Search returned HTTP {resp.status_code}: {text[:1500] if text else '(empty)'}")

            if resp.status_code >= 400:
                text = json.dumps(data, ensure_ascii=False) if isinstance(data, dict) else str(data)
                raise SystemExit(f"Search error HTTP {resp.status_code}: {text}")

            if not isinstance(data, dict):
                return {"raw": data}
            return data
        except Exception as e:
            last_exception = e
            if attempt < retry_times:
                time.sleep(float(retry_sleep_seconds))

    raise SystemExit(f"Search request failed after {retry_times} attempts: {last_exception}")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Web search via ModelHub crawl API (leads/navigation only).")
    p.add_argument("--query", required=True, help="Search query")
    p.add_argument("--count", type=int, default=10, help="Max results (default 10)")
    p.add_argument("--include-domains", default="", help="Comma-separated hostnames to restrict results")
    p.add_argument("--out", default="", help="Write Markdown results to this path")
    p.add_argument("--raw-json", action="store_true", help="Print raw JSON instead of Markdown")
    p.add_argument("--api-key", default="", help="Override API key (else MODELHUB_SEARCH_AK env, else built-in default)")
    p.add_argument("--url", dest="search_url", default="", help="Override endpoint (else MODELHUB_SEARCH_URL env)")
    p.add_argument("--timeout", type=float, default=float(os.getenv("MODELHUB_CRAWL_TIMEOUT", "60")), help="HTTP timeout seconds")
    p.add_argument("--retry-times", type=int, default=5, help="Retry times (default 5)")
    p.add_argument("--retry-sleep", type=float, default=10.0, help="Sleep seconds between retries (default 10)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    api_key = (args.api_key or os.getenv("MODELHUB_SEARCH_AK", "") or DEFAULT_API_KEY).strip()
    search_url = (args.search_url or os.getenv("MODELHUB_SEARCH_URL", "") or DEFAULT_SEARCH_URL).strip()

    data = search_web(
        query=args.query,
        count=int(args.count),
        include_domains=str(args.include_domains or ""),
        api_key=api_key,
        search_url=search_url,
        timeout_seconds=float(args.timeout),
        retry_times=int(args.retry_times),
        retry_sleep_seconds=float(args.retry_sleep),
    )

    if args.raw_json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0

    items = search_response_to_items(data if isinstance(data, dict) else {})
    meta = data.get("metadata") if isinstance(data, dict) else None
    mdict = meta if isinstance(meta, dict) else None
    md = search_results_to_markdown(items, metadata=mdict)

    if args.out:
        out_path = Path(args.out).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
        print(str(out_path))
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
